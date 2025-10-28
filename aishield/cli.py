#!/usr/bin/env python3
"""CLI entry point for code-defender"""

import sys
from .minify import main as obfuscate_main
from .unminify import main as deobfuscate_main

def main():
    """Main CLI dispatcher - obfuscate by default, unminify with flag"""
    if len(sys.argv) > 1 and sys.argv[1] in ['--unminify', '--deobfuscate', 'unminify', 'deobfuscate']:
        deobfuscate_main()
    else:
        # Default: obfuscate
        obfuscate_main()

if __name__ == "__main__":
    main()
