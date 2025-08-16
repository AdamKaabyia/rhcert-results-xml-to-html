# RHCert Results XML to HTML Viewer

Convert Red Hat Certification result XML files into a modern, interactive HTML viewer - either locally with Python **or** inside a lightweight container.

---

## 1. Quick Start (local dev)

```bash
# clone & enter the project
$ git clone https://github.com/AdamKaabyia/rhcert-results-xml-to-html.git
$ cd rhcert-results-xml-to-html

# create virtual-env (optional but recommended)
$ python -m venv .venv && source .venv/bin/activate

# install runtime deps
$ pip install flask gunicorn

# run the dev server
$ python web_server.py            # http://localhost:5000
```

* Drag & drop an `*.xml` file onto the page.
* Leave the **Auto-open viewer after upload** checkbox ticked to view instantly, or untick it to show "View Online" / "Download HTML" buttons.
* Use the **Show Failures** button in the left-hand sidebar of the generated viewer to quickly filter to only failing commands/tests.

The app deletes previous viewers automatically - the workspace never fills up with old files.

---

## 2. Run from a published container image (Docker / Podman)

If you just want to use the pre-built image from Quay:

```bash
# pull latest tag from Quay
$ podman run -d --name viewer -p 8080:8080 quay.io/akaabyia/rhcert-viewer:latest
# docker run -d --name viewer -p 8080:8080 quay.io/akaabyia/rhcert-viewer:latest

# open in browser
http://localhost:8080

If you need the exact host IP (e.g. to reach it from another machine on your LAN):

```bash
$ hostname -I        # prints something like "10.50.15.137 127.0.0.1"
# use the non-127 address

http://10.50.15.137:8080
```

---

## 3. Build the image yourself (optional)

```bash
# build image (~160 MB)
$ podman build -t rhcert-viewer .      # or: docker build -t rhcert-viewer .

# run - port 8080 inside container mapped to 8080 on host
$ podman run -d --name viewer -p 8080:8080 rhcert-viewer
# or use host-network
# podman run -d --name viewer --network host rhcert-viewer

# open in browser
http://localhost:8080
```

To test in one line:
```bash
curl -I http://127.0.0.1:8080/    # expect 200 OK
```

---

## 4. Running in Kubernetes / OpenShift

Below is a minimal Deployment + Service you can `kubectl apply` as-is (edit the image reference if you use a different tag).

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: rhcert-viewer
spec:
  replicas: 1
  selector:
    matchLabels:
      app: rhcert-viewer
  template:
    metadata:
      labels:
        app: rhcert-viewer
    spec:
      containers:
      - name: viewer
        image: quay.io/akaabyia/rhcert-viewer:latest
        ports:
        - containerPort: 8080
```

Expose it:

```yaml
# Service
apiVersion: v1
kind: Service
metadata:
  name: rhcert-viewer
spec:
  selector:
    app: rhcert-viewer
  ports:
  - port: 80
    targetPort: 8080
```

• OpenShift: add a Route
```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: rhcert-viewer
spec:
  to:
    kind: Service
    name: rhcert-viewer
  port:
    targetPort: 80
```

• Vanilla Kubernetes: add an Ingress with your controller (NGINX, Traefik). After that you’ll get an external URL.

---

## 5. Additional production hints

---

## Features


- Professional Red Hat styling (official font & colours)
- Resizable, collapsible sidebar
- Precise command highlighting
- Responsive layout
- Clean, self-contained HTML/CSS/JS output
- Optional auto-open toggle (skip the buttons and load the viewer immediately)
- Sidebar filter **Show Failures** to focus on non-passing commands
- One-click ZIP download of the viewer assets

---

## Directory overview

```
├─ css_generator.py     # builds styles
├─ js_generator.py      # builds JS behaviour
├─ html_generator.py    # assembles final HTML viewer
├─ viewer_generator.py  # orchestrator (CLI)
├─ web_server.py        # Flask upload UI / API
├─ templates/index.html # drag-and-drop frontend
├─ Dockerfile           # container image definition
└─ requirements.txt     # Flask + Gunicorn
```