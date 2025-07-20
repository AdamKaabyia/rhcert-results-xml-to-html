#!/usr/bin/env python3
"""
Red Hat Certification Viewer Generator
Main orchestrator script that creates the complete viewer using modular components.
"""

import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

# Import our modular components
from xml_parser import extract_test_structure, get_xml_attributes
from css_generator import create_css_file
from js_generator import create_js_file
from html_generator import create_html_file


def create_viewer(xml_file_path: str) -> bool:
    """Create the complete Red Hat certification viewer"""

    if not os.path.exists(xml_file_path):
        print(f"Error: XML file '{xml_file_path}' not found!")
        return False

    print(f"Processing: {xml_file_path}")

    try:
        # Extract base name for output files
        base_name = Path(xml_file_path).stem

        # Parse XML and extract test structure
        print("Parsing XML and extracting test structure...")
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        tests = extract_test_structure(root)
        xml_attrs = get_xml_attributes(xml_file_path)

        print(f"Found {len(tests)} tests with {sum(len(t['commands']) for t in tests)} total commands")

        # Generate separate files
        print("Generating CSS file...")
        css_filename = create_css_file(base_name)

        print("Generating JavaScript file...")
        js_filename = create_js_file(base_name)

        print("Generating HTML file...")
        html_filename = f"{base_name}-viewer.html"
        create_html_file(xml_file_path, css_filename, js_filename, tests, xml_attrs, html_filename)

        # Print success message
        print("\nRed Hat Certification Viewer created successfully!")
        print(f"   HTML: {html_filename}")
        print(f"   CSS:  {css_filename}")
        print(f"   JS:   {js_filename}")
        print("\nFeatures:")
        print("   - Official Red Hat logo and styling")
        print("   - Draggable/resizable sidebar")
        print("   - Collapsible sidebar with toggle")
        print("   - Precise command highlighting")
        print("   - Color-coded test status")
        print("   - Command numbering and search")
        print("   - Modular, maintainable code")
        print(f"\nOpen {html_filename} in your browser!")

        return True

    except Exception as e:
        print(f"Error creating viewer: {e}")
        return False


def main():
    """Main entry point"""
    if len(sys.argv) != 2:
        print("Usage: python viewer_generator.py <xml_file>")
        sys.exit(1)

    xml_file = sys.argv[1]
    success = create_viewer(xml_file)

    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()