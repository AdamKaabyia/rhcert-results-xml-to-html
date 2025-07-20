# Red Hat XML to HTML Converter

Simple Python tool to convert Red Hat certification XML files into beautiful, interactive HTML viewers.

## Installation

```bash
git clone git@gitlab.cee.redhat.com:akaabyia/rhcert-results-xml-to-html.git
cd rhcert-results-xml-to-html
```

## Usage

```bash
python viewer_generator.py your-xml-file.xml
```

## Generated Files

For each XML file, the tool creates:
- `filename-viewer.html` - Interactive HTML viewer
- `filename-styles.css` - Professional Red Hat styling
- `filename-script.js` - Navigation and interactivity

## Features

- **Professional Red Hat styling** with official fonts and branding
- **Interactive navigation** with resizable sidebar
- **Command highlighting** - click commands to highlight in XML
- **Responsive design** - works on all devices
- **Self-contained** - no dependencies, pure Python

## Requirements

- Python 3.6+
- No additional dependencies (uses standard library only)