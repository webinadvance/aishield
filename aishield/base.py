#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Base classes for language adapters.

Copyright (c) 2025, Code Minifier Contributors
SPDX-License-Identifier: BSD-3-Clause
"""

import json
from abc import ABC, abstractmethod
from pathlib import Path


class LanguageAdapter(ABC):
    """Abstract base class for language-specific adapters"""

    def __init__(self, name, config_dir=None):
        self.name = name
        self.config_dir = config_dir or Path(__file__).parent

    @abstractmethod
    def get_parser(self):
        """Return a configured tree-sitter parser for this language"""
        pass

    @abstractmethod
    def get_string_node_types(self):
        """Return tuple of tree-sitter node types for string literals"""
        pass

    @abstractmethod
    def get_comment_node_types(self):
        """Return tuple of tree-sitter node types for comments"""
        pass

    @abstractmethod
    def get_exclude_patterns(self):
        """Return list of identifier patterns to exclude from obfuscation"""
        pass

    @abstractmethod
    def get_import_node_types(self):
        """Return tuple of tree-sitter node types for import/using statements"""
        pass

    @abstractmethod
    def should_remove_import(self, import_text):
        """Determine if an import statement should be removed (True) or kept (False)"""
        pass

    @abstractmethod
    def get_preserve_import_ranges(self, source_bytes, tree):
        """Return list of (start_byte, end_byte) tuples for imports to preserve from obfuscation"""
        pass

    @abstractmethod
    def get_detection_patterns(self):
        """Return list of lowercase patterns that identify this language in code samples

        Returns:
            list[str]: Patterns like ['namespace ', 'using system', 'class ', 'async task']
        """
        pass

    def get_preserve_suffixes(self):
        """Return list of common suffixes that should be preserved during obfuscation

        Override this method in language-specific adapters to preserve common naming conventions.
        For example, in C# you might want to preserve 'Async', 'Controller', 'Service', etc.

        Returns:
            list[str]: Suffixes to preserve (e.g., ['Async', 'Controller', 'Service'])
        """
        return []

    def load_keywords(self):
        """Load language keywords from JSON config file"""
        config_file = self.config_dir / f'keywords_{self.name}.json'
        if config_file.exists():
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            return config.get(f'{self.name}_keywords', [])
        return []

    def load_preserve_words(self):
        """Load words/identifiers to preserve from obfuscation

        Loads from two sources:
        1. Language-specific: preserve_language.json (in language directory)
        2. Global custom: preserve_custom.json (in root directory, shared by all languages)

        Returns:
            set: Combined words to preserve (used for both full identifiers and partial word matching)
        """
        preserve_words = set()

        # Load language-specific preserve words
        language_file = self.config_dir / 'preserve_language.json'
        if language_file.exists():
            with open(language_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
                preserve_words.update(config.get('preserve', []))

        # Load global custom preserve words (in root directory)
        root_dir = Path(__file__).parent
        custom_file = root_dir / 'preserve_custom.json'
        if custom_file.exists():
            with open(custom_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
                preserve_words.update(config.get('preserve', []))

        return preserve_words
