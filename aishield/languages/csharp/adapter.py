#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
C# Language Adapter.

Provides C# language support for the Smart Code Obfuscator.

Copyright (c) 2025, Code Minifier Contributors
SPDX-License-Identifier: BSD-3-Clause
"""

from tree_sitter import Language, Parser
import tree_sitter_c_sharp as tscs
import sys
from pathlib import Path

try:
    from aishield.base import LanguageAdapter
except ImportError:
    from base import LanguageAdapter


class CSharpAdapter(LanguageAdapter):
    def __init__(self, config_dir=None):
        super().__init__('csharp', config_dir)
        self.parser = None
    
    def get_parser(self):
        if self.parser is None:
            CS_LANGUAGE = Language(tscs.language())
            self.parser = Parser(CS_LANGUAGE)
        return self.parser
    
    def get_string_node_types(self):
        return ('string_literal', 'interpolated_string_text', 'verbatim_string_literal')
    
    def get_comment_node_types(self):
        return ('comment',)
    
    def get_exclude_patterns(self):
        return ['data', 'value', 'result', 'error', 'message', 'model', 'entity']
    
    def get_import_node_types(self):
        return ('using_directive',)
    
    def should_remove_import(self, import_text):
        """Keep system imports, remove local imports"""
        text_lower = import_text.lower()
        keep_namespaces = ['system', 'microsoft', 'newtonsoft', 'automapper', 
                          'serilog', 'polly', 'fluentvalidation', 'mediatr']
        return not any(ns in text_lower for ns in keep_namespaces)
    
    def get_preserve_import_ranges(self, source_bytes, tree):
        """Preserve system and common library imports completely"""
        preserve = []
        keep_namespaces = ['system', 'microsoft', 'newtonsoft', 'automapper',
                          'serilog', 'polly', 'fluentvalidation', 'mediatr']

        def collect(node):
            if node.type == 'using_directive':
                import_text = source_bytes[node.start_byte:node.end_byte].decode('utf8').lower()
                if any(ns in import_text for ns in keep_namespaces):
                    preserve.append((node.start_byte, node.end_byte))
            for child in node.children:
                collect(child)

        collect(tree.root_node)
        return preserve

    def get_detection_patterns(self):
        """Return patterns that identify C# code"""
        return [
            'namespace ',
            'using system',
            'async task',
            'public class',
            'private class',
            'internal class',
            'public interface',
            'public void',
            'string[] args'
        ]

    def get_preserve_suffixes(self):
        """Return common C# suffixes to preserve"""
        return [
            'Async',           # Async methods
            'Controller',      # MVC controllers
            'Service',         # Services
            'Repository',      # Repositories
            'Factory',         # Factory classes
            'Provider',        # Providers
            'Handler',         # Handlers (event, command, etc.)
            'Attribute',       # Attributes
            'Exception',       # Custom exceptions
            'Builder',         # Builder pattern
            'Manager',         # Managers
            'Helper',          # Helper classes
            'Validator',       # Validators
            'Converter',       # Converters
            'Mapper',          # Mappers
            'Filter',          # Filters
            'Middleware',      # Middleware
            'Options',         # Configuration options
            'Settings',        # Settings classes
            'Context',         # Contexts (DB, HTTP, etc.)
            'Model',           # Models
            'ViewModel',       # View models
            'Dto',             # DTOs
            'Entity',          # Entities
            'Configuration'    # Configuration classes
        ]


ADAPTER_CLASS = CSharpAdapter
LANGUAGE_NAME = 'csharp'
ALIASES = ['cs', 'c#', 'dotnet']