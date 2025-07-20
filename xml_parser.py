#!/usr/bin/env python3
"""
XML Parser Module
Handles parsing of Red Hat certification XML files and extracting test structure.
"""

import xml.etree.ElementTree as ET
from typing import List, Dict


def extract_test_structure(root: ET.Element) -> List[Dict]:
    """Extract test structure from XML root element"""
    tests = []

    for test_elem in root.findall('.//test'):
        test_name = test_elem.get('name', 'Unknown Test')
        test_description = test_elem.get('description', '')
        logical_device = test_elem.get('logical-device', '')

        # Get test status from summary
        status = 'UNKNOWN'
        summary_elem = test_elem.find('.//summary')
        if summary_elem is not None:
            status = summary_elem.get('data-value', 'UNKNOWN')

        # Extract commands
        commands = []
        for i, command_elem in enumerate(test_elem.findall('.//command'), 1):
            command_text = command_elem.get('command', '')
            return_value = command_elem.get('return-value', '0')

            if command_text:
                commands.append({
                    'number': i,
                    'text': command_text,
                    'return_value': return_value,
                    'status': 'PASS' if return_value == '0' else 'FAIL'
                })

        # Calculate test status from commands
        if commands:
            passed = sum(1 for cmd in commands if cmd['status'] == 'PASS')
            total = len(commands)
            if passed == total:
                overall_status = 'PASS'
            elif passed == 0:
                overall_status = 'FAIL'
            else:
                overall_status = 'PARTIAL'
        else:
            overall_status = status

        tests.append({
            'name': test_name,
            'description': test_description,
            'logical_device': logical_device,
            'status': overall_status,
            'commands': commands,
            'command_count': len(commands),
            'total_commands': len(commands),
            'passed_commands': sum(1 for cmd in commands if cmd['status'] == 'PASS')
        })

    return tests


def get_xml_attributes(xml_file_path: str) -> Dict[str, str]:
    """Extract XML attributes needed for the viewer"""
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        return {
            'rhcert_version': root.get('rhcert-version', ''),
            'rhcert_release': root.get('rhcert-release', ''),
            'plan_time': root.get('plan-time', '')
        }
    except Exception as e:
        print(f"Error extracting XML attributes: {e}")
        return {}