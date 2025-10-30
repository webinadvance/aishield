#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JavaScript Language Adapter.

Provides JavaScript/TypeScript language support for the Smart Code Obfuscator.

Copyright (c) 2025, Code Minifier Contributors
SPDX-License-Identifier: BSD-3-Clause
"""

from tree_sitter import Language, Parser
import tree_sitter_javascript as tsjs
from pathlib import Path

try:
    from aishield.base import LanguageAdapter
except ImportError:
    from base import LanguageAdapter


class JavaScriptAdapter(LanguageAdapter):
    """JavaScript language adapter for tree-sitter"""
    
    def __init__(self, config_dir=None):
        super().__init__('javascript', config_dir)
        self.parser = None
    
    def get_parser(self):
        if self.parser is None:
            JS_LANGUAGE = Language(tsjs.language())
            self.parser = Parser(JS_LANGUAGE)
        return self.parser
    
    def get_string_node_types(self):
        return ('string', 'template_string')
    
    def get_comment_node_types(self):
        return ('comment',)
    
    def get_exclude_patterns(self):
        return ['data', 'value', 'result', 'error', 'message', 'props', 'state']
    
    def get_import_node_types(self):
        return ('import_statement', 'export_statement')
    
    def should_remove_import(self, import_text):
        """Keep node modules/npm packages and export declarations, remove local imports"""
        # Never remove export statements (they're part of function declarations)
        text_lower = import_text.lower()
        if 'export' in text_lower:
            return False

        # Keep imports from node_modules or known packages
        keep_patterns = ['react', 'express', 'lodash', 'axios', 'moment', 'uuid', 'dotenv']
        return not any(p in text_lower for p in keep_patterns)

    def get_preserve_import_ranges(self, source_bytes, tree):
        """Preserve common library imports completely"""
        preserve = []
        keep_patterns = ['react', 'express', 'lodash', 'axios', 'moment', 'uuid', 'dotenv']

        def collect(node):
            if node.type in ('import_statement', 'export_statement'):
                import_text = source_bytes[node.start_byte:node.end_byte].decode('utf8').lower()
                if any(p in import_text for p in keep_patterns):
                    preserve.append((node.start_byte, node.end_byte))
            for child in node.children:
                collect(child)

        collect(tree.root_node)
        return preserve

    def get_detection_patterns(self):
        """Return patterns that identify JavaScript code"""
        return [
            'import ',
            'export ',
            'require(',
            'const ',
            'let ',
            'function ',
            'arrow function',
            '=>',
            'async function',
            'console.log'
        ]

    def get_preserve_suffixes(self):
        """Return common suffixes that should be preserved in JavaScript/TypeScript identifiers"""
        return [
            'Async',        # async methods: getDataAsync, updateUserAsync
            'Callback',     # callback functions: onClickCallback
            'Controller',   # Angular controllers
            'Service',      # Angular services
            'Handler',      # event handlers: onChangeHandler
            'Manager',      # managers: StateManager
            'Provider',     # providers
            'Factory',      # factory functions
            'Repository',   # data repositories
            'Validator',    # validators
            'Error',        # error classes
            'Exception',    # exceptions
            'Date',         # date variables: startDate, createdDate
            'Time',         # time variables: startTime, endTime
            'Type',         # type definitions
            'Record',       # record types
            'Config',       # configuration objects
            'Options',      # options objects
            'Params',       # parameters
            'Props',        # React props
            'State',        # state objects
            'Result',       # result objects
            'Response',     # HTTP responses
            'Request',      # HTTP requests
            'Query',        # query strings
            'Filter',       # filters
            'Mapper',       # mappers
            'Converter',    # converters
        ]


# Module registration
ADAPTER_CLASS = JavaScriptAdapter
LANGUAGE_NAME = 'javascript'
ALIASES = ['js', 'node', 'typescript']