#!/usr/bin/env python3
"""
Simple Web Server for RHCert XML Viewer
--------------------------------------
Provides a drag-and-drop interface for uploading Red Hat certification XML
files. Uploaded files are processed with the existing ``viewer_generator``
module to produce the interactive HTML viewer, CSS, and JS.

Run:
    python web_server.py
Then visit http://localhost:5000 in your browser.
"""

import os
from pathlib import Path

# Jinja templates need flash messages & list of generated viewers.
from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    send_from_directory,
    send_file,
    url_for,
)
import io
import zipfile
from werkzeug.utils import secure_filename

from viewer_generator import create_viewer

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

UPLOAD_FOLDER = "uploads"  # XML files are stored here before processing
ALLOWED_EXTENSIONS = {"xml"}

# Glob patterns for generated viewer assets; used for cleanup
GENERATED_PATTERNS = ["*-viewer.html", "*-styles.css", "*-script.js"]

# ``static_url_path=''`` allows us to serve generated viewer files directly
# from the project root (``static_folder='.'``).
app = Flask(__name__, static_url_path="", static_folder=".")  # serve assets from project root
app.config.update(
    SECRET_KEY="rhcert-upload",  # required for ``flash``
    UPLOAD_FOLDER=UPLOAD_FOLDER,
)

Path(UPLOAD_FOLDER).mkdir(exist_ok=True)

# ---------------------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------------------

def _allowed_file(filename: str) -> bool:
    """Check if *filename* has an allowed extension."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ---------------------------------------------------------------------------
# Utility to purge previously generated viewer assets
# ---------------------------------------------------------------------------


def _cleanup_generated_files() -> None:
    """Delete previously generated viewer, CSS and JS artifacts."""
    root = Path(".")
    for pattern in GENERATED_PATTERNS:
        for p in root.glob(pattern):
            try:
                p.unlink()
            except OSError:
                pass


# ---------------------------------------------------------------------------
# Helper to create a zip package for download
# ---------------------------------------------------------------------------


def _create_zip_package(base_name: str) -> io.BytesIO:
    """Create an in-memory zip containing viewer, css and js for download."""
    files = [
        f"{base_name}-viewer.html",
        f"{base_name}-styles.css",
        f"{base_name}-script.js",
    ]
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for fname in files:
            if Path(fname).exists():
                zf.write(fname, arcname=fname)
    buf.seek(0)
    return buf


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------


@app.route("/")
def index():
    """Render the upload page."""
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    """Handle XML file upload and trigger viewer generation."""

    if "file" not in request.files:
        flash("No file part in the request.")
        return redirect(url_for("index"))

    file = request.files["file"]

    # If user submits an empty form without selecting a file
    if file.filename == "":
        flash("No file selected.")
        return redirect(url_for("index"))

    if not _allowed_file(file.filename):
        flash("Unsupported file type. Please upload an XML file.")
        return redirect(url_for("index"))

    # Before processing, purge earlier generated assets so we only keep the new ones
    _cleanup_generated_files()

    # Sanitize filename and store to *uploads/*
    filename = secure_filename(file.filename)
    xml_path = Path(app.config["UPLOAD_FOLDER"]) / filename
    file.save(xml_path)

    # Trigger viewer generation (HTML, CSS, JS)
    success = create_viewer(str(xml_path))
    if not success:
        flash("Failed to generate viewer from the uploaded XML file.")
        return redirect(url_for("index"))

    # The viewer filenames follow the pattern: <base>-viewer.html
    base_name = xml_path.stem
    viewer_filename = f"{base_name}-viewer.html"

    action = request.form.get("action", "view")

    if action == "download":
        # Send file as attachment
        zip_bytes = _create_zip_package(base_name)
        return send_file(
            zip_bytes,
            download_name=f"{base_name}-viewer.zip",
            mimetype="application/zip",
            as_attachment=True,
        )

    # Default: view online (inline)
    return redirect(url_for("downloads", filename=viewer_filename))


# ---------------------------------------------------------------------------
# Convenience route: explicitly serve generated files if required
# ---------------------------------------------------------------------------


@app.route("/downloads/<path:filename>")
def downloads(filename: str):
    """Serve files from the project root (HTML, CSS, JS)."""
    root_dir = Path(__file__).resolve().parent
    return send_from_directory(root_dir, filename, as_attachment=False)


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # Enable reloader & debug for local development
    app.run(host="0.0.0.0", port=5000, debug=True)