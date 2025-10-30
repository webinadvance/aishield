#!/usr/bin/env python3
"""CLI entry point for code-defender"""

import sys
import argparse
from .minify import main as obfuscate_main
from .unminify import main as deobfuscate_main

def print_help():
    """Display help message"""
    help_text = """
code-defender - Intelligent Code Obfuscator Against AI Detection

USAGE:
    code-defender [COMMAND] [OPTIONS]

COMMANDS:
    obfuscate       Obfuscate code (default)
    unminify        Reverse obfuscation using mapping file
    deobfuscate     Alias for unminify

OPTIONS:
    -h, --help      Show this help message
    -v, --version   Show version information
    -u              Unminify mode (shorthand for --unminify)

EXAMPLES:
    code-defender                    # Interactive obfuscation
    code-defender --help             # Show this help message
    code-defender -u                 # Interactive unminification (short form)
    code-defender --unminify         # Interactive unminification
    code-defender unminify           # Interactive unminification

SUPPORTED LANGUAGES:
    - C# / .NET
    - JavaScript / TypeScript

WORKFLOW:
    1. Copy code to clipboard
    2. Run 'code-defender'
    3. Select language (auto-detected or manual entry)
    4. Result is copied to clipboard
    5. Obfuscation mapping saved to obfuscation_mapping_<language>.json

For more information, visit: https://github.com/webinadvance/aishield
"""
    print(help_text)

def print_version():
    """Display version information"""
    from . import __version__
    print(f"code-defender version {__version__}")

def main():
    """Main CLI dispatcher - obfuscate by default, unminify with flag"""
    # Check for help/version flags FIRST (before any imports or initialization)
    if len(sys.argv) > 1:
        first_arg = sys.argv[1]

        if first_arg in ['-h', '--h', '--help', 'help']:
            print_help()
            return

        if first_arg in ['-v', '--version', 'version']:
            print_version()
            return

        # Check for unminify command
        if first_arg in ['-u', '--unminify', '--deobfuscate', 'unminify', 'deobfuscate']:
            deobfuscate_main()
            return

    # Default: obfuscate
    obfuscate_main()

if __name__ == "__main__":
    main()
