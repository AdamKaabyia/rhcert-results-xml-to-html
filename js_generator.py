#!/usr/bin/env python3
"""
JavaScript Generator Module
Handles generation of JavaScript functionality for the Red Hat certification viewer.
"""


def generate_js_content() -> str:
    """Generate the complete JavaScript content for the viewer"""
    return '''// RHCert Viewer JavaScript Functionality

let sidebarWidth = 320;
let isDragging = false;
let sidebarCollapsed = false;
let showOnlyFailed = false;

// Initialize sidebar functionality
document.addEventListener('DOMContentLoaded', function() {
    initializeResizer();
    updateMainContentMargin();
    // attach keyboard shortcut? none
});

function initializeResizer() {
    const resizer = document.getElementById('resizer');
    const sidebar = document.getElementById('sidebar');

    resizer.addEventListener('mousedown', function(e) {
        if (sidebarCollapsed) return; // Don't resize when collapsed
        isDragging = true;
        document.body.classList.add('no-select');
        resizer.classList.add('dragging');
        e.preventDefault();
    });

    document.addEventListener('mousemove', function(e) {
        if (!isDragging || sidebarCollapsed) return;

        const newWidth = Math.max(200, Math.min(600, e.clientX));
        sidebarWidth = newWidth;
        sidebar.style.width = newWidth + 'px';
        updateMainContentMargin();
        updateToggleButtonPosition();
    });

    document.addEventListener('mouseup', function() {
        if (isDragging) {
            isDragging = false;
            document.body.classList.remove('no-select');
            resizer.classList.remove('dragging');
        }
    });
}

function updateMainContentMargin() {
    const mainContent = document.querySelector('certification-test');
    if (mainContent) {
        const margin = sidebarCollapsed ? '10px' : (sidebarWidth + 10) + 'px';
        mainContent.style.marginLeft = margin;
    }
}

function updateToggleButtonPosition() {
    const toggleBtn = document.getElementById('toggleBtn');
    if (toggleBtn && !sidebarCollapsed) {
        toggleBtn.style.left = sidebarWidth + 'px';
    }
}

function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const toggleBtn = document.getElementById('toggleBtn');

    sidebarCollapsed = !sidebarCollapsed;

    if (sidebarCollapsed) {
        sidebar.classList.add('collapsed');
        toggleBtn.classList.add('collapsed');
        toggleBtn.textContent = '▶';
    } else {
        sidebar.classList.remove('collapsed');
        toggleBtn.classList.remove('collapsed');
        toggleBtn.textContent = '◀';
        updateToggleButtonPosition();
    }

    updateMainContentMargin();
}

function toggleTest(testId) {
    const commandList = document.getElementById('nav_' + testId);
    const header = event.target.closest('.test-header');
    const toggle = header.querySelector('.test-toggle');

    if (commandList.classList.contains('expanded')) {
        commandList.classList.remove('expanded');
        toggle.textContent = '▼';
    } else {
        commandList.classList.add('expanded');
        toggle.textContent = '▲';
    }
}

function jumpToCommand(commandText) {
    // Add click animation to sidebar item
    const clickedItem = event.target.closest('.command-item');
    if (clickedItem) {
        clickedItem.classList.add('clicked');
        setTimeout(() => clickedItem.classList.remove('clicked'), 600);
    }

    // Remove existing highlights
    document.querySelectorAll('.highlight').forEach(el => el.classList.remove('highlight'));

    // Find the exact command element in original XML
    const commands = document.querySelectorAll('command');
    let commandFound = false;

    for (let cmd of commands) {
        if (cmd.getAttribute('command') === commandText) {
            // Highlight the specific command with enhanced animation
            cmd.classList.add('highlight');

            // Scroll to command with better positioning
            const rect = cmd.getBoundingClientRect();
            const offset = window.innerHeight / 3; // Show command in upper third of screen
            window.scrollTo({
                top: window.pageYOffset + rect.top - offset,
                behavior: 'smooth'
            });

            // Remove highlight after animation
            setTimeout(() => cmd.classList.remove('highlight'), 3000);
            commandFound = true;
            break;
        }
    }

    // If exact match not found, try partial matching
    if (!commandFound) {
        for (let cmd of commands) {
            const cmdAttr = cmd.getAttribute('command') || '';
            if (cmdAttr.includes(commandText.split(' ')[0])) {
                cmd.classList.add('highlight');

                const rect = cmd.getBoundingClientRect();
                const offset = window.innerHeight / 3;
                window.scrollTo({
                    top: window.pageYOffset + rect.top - offset,
                    behavior: 'smooth'
                });

                setTimeout(() => cmd.classList.remove('highlight'), 3000);
                break;
            }
        }
    }
}

function jumpToTop() {
    document.querySelector('certification-test').scrollIntoView({ behavior: 'smooth' });
}

function filterTests() {
    const searchTerm = event.target.value.toLowerCase();
    const testItems = document.querySelectorAll('.test-item');

    testItems.forEach(item => {
        const testText = item.textContent.toLowerCase();
        if (testText.includes(searchTerm) || searchTerm === '') {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
}

function toggleFailed() {
    showOnlyFailed = !showOnlyFailed;
    const btn = document.getElementById('failedToggle');
    btn.textContent = showOnlyFailed ? 'Show All' : 'Show Failures';
    applyFailureFilter();
}

function applyFailureFilter() {
    const commandItems = document.querySelectorAll('.command-item');
    commandItems.forEach(item => {
        const isPass = item.querySelector('.cmd-status')?.classList.contains('cmd-success');
        if (showOnlyFailed && isPass) {
            item.style.display = 'none';
        } else {
            item.style.display = 'flex';
        }
    });

    // Hide entire tests that now have no visible commands
    const testItems = document.querySelectorAll('.test-item');
    testItems.forEach(test => {
        const anyVisible = test.querySelectorAll('.command-item').length && Array.from(test.querySelectorAll('.command-item')).some(ci => ci.style.display !== 'none');
        test.style.display = anyVisible ? 'block' : 'none';
    });
}'''


def create_js_file(base_name: str) -> str:
    """Create JavaScript file and return filename"""
    js_filename = f"{base_name}-script.js"

    with open(js_filename, 'w', encoding='utf-8') as f:
        f.write(generate_js_content())

    return js_filename