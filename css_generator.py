#!/usr/bin/env python3
"""
CSS Generator Module
Handles generation of CSS styling for the Red Hat certification viewer.
"""


def generate_css_content() -> str:
    """Generate the complete CSS content for the viewer"""
    return '''/* Red Hat Certification Viewer Styles */
@import url('https://fonts.googleapis.com/css2?family=Red+Hat+Mono:wght@300;400;500;600&display=swap');

/* Red Hat Official CSS */
* {
  font-family: 'Red Hat Mono', monospace, mono;
  font-size: 12px;
  padding: 3px;
}

certification-test::before {
  display: block;
  content: 'Certification Test Results,  rhcert ' attr(rhcert-version) ' '
    attr(rhcert-release) '   ' attr(plan-time);
  font-weight: 700;
  background-image: url('https://rhcert.connect.redhat.com/rhcert/img/Logo-RedHat-A-Standard-RGB.png');
  background-position: 0px 20px;
  background-size: 200px auto;
  background-repeat: no-repeat;
  width: 100%;
  height: 80px;
  border-bottom: 2px solid gray;
  padding-left: 220px;
}

certification-test {
  display: block;
  border: 1px solid black;
  padding: 10px;
  margin: 10px;
  margin-left: 330px; /* Space for sidebar */
  transition: margin-left 0.3s ease;
}

certification::before {
  display: block;
  content: 'Certification: ' attr(type) '  ID: ' attr(id);
}

certification {
  display: block;
  border: 1px solid gray;
}

hardware {
  display: grid;
  grid-template-rows: 2fr;
  width: fit-content;
  text-align: center;
}

hardware vendor::before {
  content: 'Host: ';
}

hardware vendor {
  grid-row: 1;
  order: 1;
}

hardware make {
  grid-row: 1;
  order: 2;
}

hardware model {
  grid-row: 1;
  order: 3;
}

hardware arch {
  grid-row: 1;
  order: 4;
}

hardware test-server {
  display: none;
}

hardware os,
os {
  grid-row: 2;
  grid-column: 1 / 5;
  display: flex;
  justify-content: flex-start;
  align-items: center;
}

os hostname::before {
  content: 'Host Name: ';
  font-weight: 700;
}

os hostname {
  order: 1;
}

os ip-address {
  order: 2;
}

os product::before {
  content: ' | OS: ';
  font-weight: 700;
}

os product {
  order: 3;
}

os release {
  order: 4;
}

os name {
  display: none;
}
os platform {
  order: 5;
}
os platform::before {
  content: ' | Platform: ';
  font-weight: 700;
}

os variant {
  order: 6;
}
os variant::before {
  content: ' | Variant: ';
  font-weight: 700;
}

os build {
  order: 7;
}
os build::before {
  content: ' | Build: ';
  font-weight: 700;
}

certification os {
  display: none;
}

certification vendor::before {
  display: block;
  content: attr(name);
}

certification vendor {
  display: flex;
}

certification vendor product::before {
  display: block;
  content: attr(name);
}

certification vendor product {
  display: flex;
  padding-top: 0px;
  padding-bottom: 0px;
}

certification vendor product version::before {
  display: block;
  content: attr(version) ' ' attr(platform);
}

certification vendor product version {
  display: flex;
  padding-top: 0px;
  padding-bottom: 0px;
}

certification vendor product make {
  display: block;
  padding-top: 0px;
  padding-bottom: 0px;
}

certification host-role::before {
  display: block;
  content: 'Host Role: ' attr(name);
}

certification host-role {
  display: block;
}

device-class::before {
  display: block;
  font-size: 16px;
  content: ' class: ' attr(name);
  font-weight: 700;
  border-bottom: 1px solid black;
  width: 100%;
  background-color: #cccccc;
}

device-class {
  display: block;
  margin: 12px;
}

test::before {
  display: block;
  content: ' test: ' attr(name) '  ' attr(logical-device) '  ' attr(description);
  font-weight: 700;
  border-bottom: 1px solid black;
  width: 750px;
}

test {
  display: block;
  margin: 12px;
}

run::before {
  display: block;
  content: 'run ' attr(number) ': ' attr(run-time);
  font-weight: 700;
  margin: 12px 6px;
}

test parameters property::before {
  display: inline-block;
  content: attr(name) ': ';
  font-weight: 700;
}

test parameters property {
  display: block;
}

summary {
  display: block;
  font-weight: 700;
  font-size: 0px;
  content: attr(data-value);
}

summary:after {
  display: block;
  color: blue;
  font-weight: 700;
  font-size: 10px;
  content: attr(data-value);
}

summary[data-value='FAIL']:after {
  color: red;
}

summary[data-value='WARN']:after {
  color: darkorange;
}

summary[data-value='REVIEW']:after {
  color: blueviolet;
}

summary[data-value='PASS']:after {
  color: green;
}

message {
  display: block;
  font-weight: 700;
  font-size: 10px;
}

message[level='FAIL'] {
  color: red;
}

message[level='WARN'] {
  color: darkorange;
}

message[level='REVIEW'] {
  color: blueviolet;
}

message[level='PASS'] {
  color: green;
}

output::before {
  display: table;
  content: attr(name) ':  ' attr(description);
  font-weight: 700;
}

output {
  display: table;
  width: 760px;
  white-space: pre;
  font-family: 'Red Hat Mono', monospace, mono;
  font-size: 10px;
  background-color: #eee;
  border: 1px solid gray;
  padding: 3px;
  margin: 10px;
}

command::before {
  display: table;
  content: attr(command);
  font-size: 10px;
  font-weight: 500;
}

command:after {
  display: table;
  content: 'returned: ' attr(return-value);
  font-size: 10px;
  font-weight: 500;
}

regex::before {
  content: 'search: ' attr(group) ' in: ';
  font-size: 10px;
  font-weight: 500;
}

regex[group='None']::before {
  content: 'search: ';
  font-size: 10px;
  font-weight: 500;
}

regex {
  display: block;
  font-weight: 500;
}

stdout {
  display: table;
  width: 720px;
  white-space: pre;
  font-family: 'Red Hat Mono', monospace, mono;
  font-size: 10px;
  background-color: #b6ff6e;
  border: 1px solid gray;
  padding: 3px;
  margin: 10px;
}

stderr {
  display: table;
  width: 720px;
  white-space: pre;
  font-family: 'Red Hat Mono', monospace, mono;
  font-size: 10px;
  background-color: #fcaf3e;
  border: 1px solid gray;
  padding: 3px;
  margin: 10px;
}

keyword {
  white-space: pre;
  font-family: 'Red Hat Mono', monospace, mono;
  font-size: 10px;
  color: black;
  background-color: white;
  font-weight: 700;
  padding: 0px;
  margin: 0px;
}

keyword[type='error'] {
  color: red;
}

keyword[type='warning'] {
  color: darkorange;
}

keyword[type='review'] {
  color: goldenrod;
}

attachment::before {
  content: 'attachment: ' attr(name) '  mime-type: ' attr(mime-type);
  font-size: 10px;
}

attachment {
  display: block;
  font-size: 0px;
}

/* hidden */
device,
hal,
kudzu,
system,
test-server,
deferred,
headers,
payload,
property,
plan-component {
  display: none;
}

certification-test::before {
  display: block;
  content: 'Certification Test Results,  rhcert ' attr(rhcert-version) ' '
    attr(rhcert-release) '   ' attr(plan-time);
  font-weight: 700;
  background-image: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABMoAAAEiCAYAAAAI3D5xAAAACXBIWXMAABYlAAAWJQFJUiTwAAAgAElEQVR4nO3df4xd553f98/j5XpFZeHLKxBLA440o222GyNRZhQYCYKo5gjBLoLd2BwXadEC1g71T5EuAnMEFCgQJOZwt8gfRQANja0boCg4zBpttmigoZ11i3UDzni1KLowqmG1wG42qDmUIsAsCB2Ompiy7OgJHt7vIQ/vj5n74/x4nnPeL2BA6d4Rde8598c5n/P9fh/nvRcAAAAADQdae6vgHQAABJREFUAe6/j5XpFZeHLKxBLA440o222GyNRZhQYCYKo5gjBLoLd2BwXadEC1g71T5EuAnMEFCgQJOZwt8gfRQANja0boCg4zBpttmigoZ11i3UDzni1KLowqmG1wG42qDmUIsAsCB2Ompiy7OgJHt7vIQ/vj5n74/x4nnPeL2BA6d4Rde8598c5n/P9fh/nvRcAAAAP');
  background-position: 0px 20px;
  background-size: 200px auto;
  background-repeat: no-repeat;
  width: 100%;
  height: 80px;
  border-bottom: 2px solid gray;
  padding-left: 220px;
}

certification-test {
  display: block;
  border: 1px solid black;
  padding: 10px;
  margin: 10px;
  margin-left: 330px; /* Space for sidebar */
  transition: margin-left 0.3s ease;
}

certification::before {
  display: block;
  content: 'Certification: ' attr(type) '  ID: ' attr(id);
}

certification {
  display: block;
  border: 1px solid gray;
}

hardware {
  display: grid;
  grid-template-rows: 2fr;
  width: fit-content;
  text-align: center;
}

hardware vendor::before {
  content: 'Host: ';
}

hardware vendor {
  grid-row: 1;
  order: 1;
}

hardware make {
  grid-row: 1;
  order: 2;
}

hardware model {
  grid-row: 1;
  order: 3;
}

hardware arch {
  grid-row: 1;
  order: 4;
}

hardware test-server {
  display: none;
}

hardware os,
os {
  grid-row: 2;
  grid-column: 1 / 5;
  display: flex;
  justify-content: flex-start;
  align-items: center;
}

os hostname::before {
  content: 'Host Name: ';
  font-weight: 700;
}

os hostname {
  order: 1;
}

os ip-address {
  order: 2;
}

os product::before {
  content: ' | OS: ';
  font-weight: 700;
}

os product {
  order: 3;
}

os release {
  order: 4;
}

os name {
  display: none;
}
os platform {
  order: 5;
}
os platform::before {
  content: ' | Platform: ';
  font-weight: 700;
}

os variant {
  order: 6;
}
os variant::before {
  content: ' | Variant: ';
  font-weight: 700;
}

os build {
  order: 7;
}
os build::before {
  content: ' | Build: ';
  font-weight: 700;
}

/* Navigation Sidebar Styles */
.nav-sidebar {
    position: fixed;
    left: 0;
    top: 0;
    width: 320px;
    height: 100vh;
    background: #f8f9fa;
    border-right: 2px solid #cc0000;
    overflow-y: auto;
    z-index: 1000;
    font-family: 'Red Hat Mono', monospace;
    font-size: 11px;
    transition: width 0.3s ease, transform 0.3s ease;
    min-width: 200px;
    max-width: 600px;
}

.nav-sidebar.collapsed {
    transform: translateX(-100%);
}

.sidebar-resizer {
    position: absolute;
    top: 0;
    right: 0;
    width: 8px;
    height: 100%;
    background: #cc0000;
    cursor: col-resize;
    opacity: 0.8;
    transition: all 0.2s;
    z-index: 1002;
}

.sidebar-resizer:hover {
    opacity: 1;
    background: #990000;
    width: 12px;
}

.sidebar-resizer.dragging {
    opacity: 1;
    background: #660000;
    width: 12px;
}

.nav-header {
    background: #cc0000;
    color: white;
    padding: 12px;
    position: sticky;
    top: 0;
    z-index: 1001;
    border-bottom: 2px solid #990000;
}

.nav-title {
    font-weight: 600;
    margin-bottom: 8px;
    font-size: 14px;
}

.nav-controls {
    display: flex;
    gap: 4px;
    flex-wrap: wrap;
}

.nav-btn {
    background: rgba(255,255,255,0.2);
    color: white;
    border: 1px solid rgba(255,255,255,0.3);
    padding: 4px 8px;
    border-radius: 3px;
    cursor: pointer;
    font-size: 9px;
    font-family: 'Red Hat Mono', monospace;
    transition: all 0.2s;
}

.nav-btn:hover {
    background: rgba(255,255,255,0.3);
    transform: translateY(-1px);
}

.nav-search {
    width: 100%;
    padding: 6px;
    border: 1px solid rgba(255,255,255,0.3);
    border-radius: 3px;
    margin-top: 8px;
    background: rgba(255,255,255,0.1);
    color: white;
    font-family: 'Red Hat Mono', monospace;
    font-size: 10px;
}

.nav-search::placeholder {
    color: rgba(255,255,255,0.7);
}

.nav-content {
    padding: 10px;
}

.test-item {
    margin-bottom: 8px;
    border: 1px solid #dee2e6;
    border-radius: 4px;
    background: white;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.test-header {
    padding: 8px;
    cursor: pointer;
    font-weight: 500;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 10px;
}

.test-header:hover {
    opacity: 0.8;
}

.test-header.status-pass {
    background: #d4edda;
    color: #155724;
    border-left: 3px solid #28a745;
}

.test-header.status-fail {
    background: #f8d7da;
    color: #721c24;
    border-left: 3px solid #dc3545;
}

.test-header.status-partial {
    background: #fff3cd;
    color: #856404;
    border-left: 3px solid #ffc107;
}

.test-header.status-unknown {
    background: #e2e3e5;
    color: #383d41;
    border-left: 3px solid #6c757d;
}

.test-info {
    display: flex;
    flex-direction: column;
    flex: 1;
}

.test-name {
    font-size: 10px;
    font-weight: 600;
}

.test-stats {
    font-size: 8px;
    opacity: 0.8;
    margin-top: 2px;
}

.test-toggle {
    font-size: 10px;
    color: #6c757d;
}

.command-list {
    display: none;
    max-height: 200px;
    overflow-y: auto;
    background: #f8f9fa;
}

.command-list.expanded {
    display: block;
}

.command-item {
    padding: 4px 8px;
    border-top: 1px solid #e9ecef;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 9px;
    transition: all 0.2s;
}

.command-item:hover {
    background: #e9ecef;
    transform: translateX(2px);
}

.command-item.clicked {
    background: #007bff;
    color: white;
    animation: commandClick 0.6s ease-out;
}

@keyframes commandClick {
    0% { background: #007bff; transform: scale(1.02); }
    100% { background: #e9ecef; transform: scale(1); color: inherit; }
}

.cmd-number {
    font-weight: 600;
    font-size: 8px;
    color: #6c757d;
    min-width: 18px;
}

.cmd-status {
    font-size: 9px;
    font-weight: 600;
    min-width: 12px;
}

.cmd-success {
    color: #28a745;
}

.cmd-error {
    color: #dc3545;
}

.cmd-text {
    flex: 1;
    font-size: 8px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

/* Enhanced Command Highlighting */
command.highlight {
    background: linear-gradient(135deg, #ff6b6b, #4ecdc4, #45b7d1, #f9ca24) !important;
    background-size: 200% 200% !important;
    animation: commandHighlight 2.5s ease-in-out !important;
    border-radius: 6px !important;
    padding: 6px 12px !important;
    margin: 8px 0 !important;
    border: 3px solid #ff6b6b !important;
    box-shadow: 0 0 25px rgba(255, 107, 107, 0.7) !important;
    position: relative !important;
    z-index: 100 !important;
}

command.highlight::before {
    content: "SELECTED COMMAND" !important;
    position: absolute !important;
    top: -20px !important;
    left: 0 !important;
    background: #ff6b6b !important;
    color: white !important;
    padding: 2px 8px !important;
    border-radius: 4px !important;
    font-size: 9px !important;
    font-weight: bold !important;
    z-index: 101 !important;
}

@keyframes commandHighlight {
    0% {
        background-position: 0% 50%;
        box-shadow: 0 0 25px rgba(255, 107, 107, 0.9);
        transform: scale(1.03);
        border-color: #ff6b6b;
    }
    25% {
        background-position: 100% 50%;
        box-shadow: 0 0 30px rgba(78, 205, 196, 0.9);
        border-color: #4ecdc4;
    }
    50% {
        background-position: 0% 50%;
        box-shadow: 0 0 30px rgba(69, 183, 209, 0.9);
        border-color: #45b7d1;
    }
    75% {
        background-position: 100% 50%;
        box-shadow: 0 0 30px rgba(249, 202, 36, 0.9);
        border-color: #f9ca24;
    }
    100% {
        background-position: 0% 50%;
        box-shadow: 0 0 15px rgba(255, 107, 107, 0.5);
        transform: scale(1);
        border-color: #ff6b6b;
    }
}

/* Sidebar Toggle Button */
.sidebar-toggle {
    position: fixed;
    left: 320px;
    top: 50%;
    background: #cc0000;
    color: white;
    border: none;
    padding: 12px 4px;
    border-radius: 0 8px 8px 0;
    cursor: pointer;
    z-index: 1001;
    font-size: 14px;
    font-weight: bold;
    transition: all 0.3s ease;
    box-shadow: 2px 0 5px rgba(0,0,0,0.2);
}

.sidebar-toggle:hover {
    background: #990000;
    padding: 12px 6px;
}

.sidebar-toggle.collapsed {
    left: 0px;
    border-radius: 0 8px 8px 0;
}

/* Utility Classes */
.no-select {
    user-select: none;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
}'''


def create_css_file(base_name: str) -> str:
    """Create CSS file and return filename"""
    css_filename = f"{base_name}-styles.css"

    with open(css_filename, 'w', encoding='utf-8') as f:
        f.write(generate_css_content())

    return css_filename