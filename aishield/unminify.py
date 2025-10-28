#!/usr/bin/env python3
"""
C# DEOBFUSCATOR - With Comment Restoration
Reverses obfuscation using mapping file
Adds newlines after each comment block during restoration
"""

import pyperclip
import json
import re
from pathlib import Path


def get_mapping_file():
    return 'mapping.json'


def load_mapping():
    """Load obfuscation mapping"""
    mapping_file = Path(get_mapping_file())
    
    if not mapping_file.exists():
        raise FileNotFoundError(f"Mapping file not found: {mapping_file}")
    
    with open(mapping_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    return data


def deobfuscate_text(obfuscated_code, word_mapping, identifier_mapping, comment_mapping, string_mapping=None):
    """Deobfuscate using mappings + restore comments with newlines"""
    if string_mapping is None:
        string_mapping = {}

    result = obfuscated_code

    # Step 1: Restore comments with newlines
    if comment_mapping:
        sorted_comments = sorted(comment_mapping.items(), key=lambda x: len(x[0]), reverse=True)
        for key, original_comment in sorted_comments:
            # Key is stored as __CMT0__, reconstruct full placeholder
            placeholder = f"/*{key}*/" if not key.startswith('/*') else key
            result = result.replace(placeholder, original_comment + '\n')

    # Step 2: Restore string literals (new in v1.1.0)
    if string_mapping:
        reverse_strings = {v: k for k, v in string_mapping.items()}
        sorted_strings = sorted(reverse_strings.items(), key=lambda x: len(x[0]), reverse=True)
        for obf_hash, orig_string in sorted_strings:
            # Replace quoted hashes
            pattern = re.compile(r'\b' + re.escape(obf_hash) + r'\b')
            result = pattern.sub(f'"{orig_string}"', result)

    # Step 3: Replace full identifiers (handle strings and regular identifiers separately)
    if identifier_mapping:
        reverse_identifiers = {v: k for k, v in identifier_mapping.items() if v != k}

        # Process quoted strings first (with exact match including quotes)
        string_mappings = {obf: orig for obf, orig in reverse_identifiers.items()
                          if obf.startswith('"') and obf.endswith('"')}
        # Process unquoted string hashes (like D4213 -> I'm a disabled button)
        # Map from hash (without quotes) to original (without quotes)
        unquoted_string_hashes = {obf.strip('"'): orig.strip('"')
                                  for obf, orig in string_mappings.items()}
        # Regular identifiers (not strings)
        regular_mappings = {obf: orig for obf, orig in reverse_identifiers.items()
                           if obf not in string_mappings}

        # Replace quoted strings first
        sorted_strings = sorted(string_mappings.items(), key=lambda x: len(x[0]), reverse=True)
        for obf, orig in sorted_strings:
            result = result.replace(obf, orig)

        # Replace unquoted string hashes (like D4213 that appear in attributes without quotes)
        sorted_unquoted = sorted(unquoted_string_hashes.items(), key=lambda x: len(x[0]), reverse=True)
        for obf_hash, orig_str in sorted_unquoted:
            # Replace only whole word matches for unquoted hashes
            pattern = re.compile(r'\b' + re.escape(obf_hash) + r'\b')
            result = pattern.sub(orig_str, result)

        # Replace regular identifiers (word boundary matching)
        sorted_ids = sorted(regular_mappings.items(), key=lambda x: len(x[0]), reverse=True)
        for obf, orig in sorted_ids:
            pattern = re.compile(r'\b' + re.escape(obf) + r'\b')
            result = pattern.sub(orig, result)

    # Step 4: Restore word mappings for any remaining obfuscated words
    if word_mapping:
        reverse_words = {v: k for k, v in word_mapping.items() if v != k}
        sorted_words = sorted(reverse_words.items(), key=lambda x: len(x[0]), reverse=True)
        for obf_word, orig_word in sorted_words:
            pattern = re.compile(r'\b' + re.escape(obf_word) + r'\b')
            result = pattern.sub(orig_word, result)

    return result


def main():
    try:
        print("🔓 DEOBFUSCATOR - Restore Original Code")
        print("=" * 60)

        print("📂 Loading mapping...")
        mapping_data = load_mapping()

        word_mapping = mapping_data.get('word_mapping', {})
        identifier_mapping = mapping_data.get('identifier_mapping', {})
        comment_mapping = mapping_data.get('comment_mapping', {})
        string_mapping = mapping_data.get('string_mapping', {})
        reverse_map = mapping_data.get('reverse_map', {})

        if not reverse_map and not word_mapping:
            print("❌ No mappings found!")
            return

        total_mappings = len(word_mapping) + len(reverse_map)
        print(f"✅ Loaded {total_mappings} mappings")
        print(f"   Words: {len(word_mapping)} | Identifiers: {len(reverse_map)}")
        print(f"   Comments: {len(comment_mapping)} | Strings: {len(string_mapping)}")

        obfuscated = pyperclip.paste()

        if not obfuscated or not obfuscated.strip():
            print("❌ Clipboard is empty!")
            return

        print(f"📊 Input: {len(obfuscated):,} chars")

        print("\n🔓 Deobfuscating...")
        deobfuscated = deobfuscate_text(obfuscated, word_mapping, identifier_mapping, comment_mapping, string_mapping)

        print(f"📊 Output: {len(deobfuscated):,} chars")

        pyperclip.copy(deobfuscated)
        print("\n✅ Deobfuscated code copied to clipboard!")

        print(f"\n📋 Full Output:")
        print("=" * 60)
        print(deobfuscated)
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()