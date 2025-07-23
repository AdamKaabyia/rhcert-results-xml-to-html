#!/usr/bin/env python3
"""
HTML Generator Module
Handles generation of HTML structure for the Red Hat certification viewer.
"""

from typing import List, Dict


def generate_sidebar_html(tests: List[Dict]) -> str:
    """Generate the sidebar navigation HTML"""
    sidebar_content = '''
    <div class="nav-header">
        <div class="nav-title">Test Navigator</div>
        <div class="nav-controls">
            <button class="nav-btn" onclick="jumpToTop()">Top</button>
            <input type="text" class="nav-search" placeholder="Search tests/commands..." oninput="filterTests()">
        </div>
    </div>

    <div class="nav-content">'''

    for i, test in enumerate(tests):
        status_class = f"status-{test['status'].lower()}"
        test_id = f"test_{i}"

        sidebar_content += f'''
        <div class="test-item">
            <div class="test-header {status_class}" onclick="toggleTest('{test_id}')">
                <div class="test-info">
                    <div class="test-name">{test['name']}</div>
                    <div class="test-stats">✓ {test['passed_commands']}/{test['total_commands']} commands</div>
                </div>
                <span class="test-toggle">▼</span>
            </div>
            <div class="command-list" id="nav_{test_id}">'''

        for cmd in test['commands']:
            status_icon = '✓' if cmd['status'] == 'PASS' else '✗'
            status_class = 'cmd-success' if cmd['status'] == 'PASS' else 'cmd-error'

            sidebar_content += f'''
                <div class="command-item" onclick="jumpToCommand('{cmd['text']}')">
                    <span class="cmd-number">#{cmd['number']}</span>
                    <span class="cmd-status {status_class}">{status_icon}</span>
                    <span class="cmd-text">{cmd['text'][:50]}...</span>
                </div>'''

        sidebar_content += '''
            </div>
        </div>'''

    sidebar_content += '''
    </div>'''

    return sidebar_content


def generate_complete_html(xml_file_path: str, css_filename: str, js_filename: str,
                          tests: List[Dict], xml_attributes: Dict[str, str]) -> str:
    """Generate the complete HTML document"""

    sidebar_html = generate_sidebar_html(tests)

    # Read the original XML content
    with open(xml_file_path, 'r', encoding='utf-8') as f:
        xml_content = f.read()

    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Red Hat Certification Viewer</title>
    <link rel="stylesheet" href="{css_filename}">
    <style>
        .back-btn {{ position: fixed; top: 10px; right: 10px; z-index: 1100; background: #cc0000; color: #fff; border: none; padding: 8px 14px; border-radius: 6px; cursor: pointer; font-weight: bold; }}
        .back-btn:hover {{ background: #a30000; }}
    </style>
</head>
<body>
    <button class="back-btn" onclick="window.location.href='/'">Back to Upload</button>
    <!-- Navigation Sidebar -->
    <div class="nav-sidebar" id="sidebar">
        <div class="sidebar-resizer" id="resizer"></div>
        {sidebar_html}
    </div>

    <!-- Sidebar Toggle Button -->
    <button class="sidebar-toggle" id="toggleBtn" onclick="toggleSidebar()">◀</button>

    <!-- Main Content -->
    <div class="main-content">
        {xml_content}
    </div>

    <script src="{js_filename}"></script>
</body>
</html>'''

    return html_content


def create_html_file(xml_file_path: str, css_filename: str, js_filename: str,
                    tests: List[Dict], xml_attributes: Dict[str, str],
                    output_filename: str) -> str:
    """Create HTML file and return filename"""

    html_content = generate_complete_html(
        xml_file_path, css_filename, js_filename, tests, xml_attributes
    )

    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(html_content)

    return output_filename