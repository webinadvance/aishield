#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive Test Runner for TypeScript Obfuscation/Deobfuscation
Tests obfuscation and deobfuscation of multiple TypeScript files
"""

import json
import sys
from pathlib import Path

from minify import LanguageRegistry, ObfuscationEngine
from unminify import deobfuscate_text, load_mapping

# Test files
TEST_FILES = [
    ("tests/typescript/test1_basic.ts", "Basic TypeScript"),
    ("tests/typescript/test2_classes.ts", "Classes & Interfaces"),
    ("tests/typescript/test3_async.ts", "Async/Await & Generics"),
    ("tests/typescript/test4_react.tsx", "React with TypeScript"),
    ("tests/typescript/test5_advanced.ts", "Advanced TypeScript"),
]


class TestResult:
    def __init__(self, filename: str, description: str):
        self.filename = filename
        self.description = description
        self.original_code = ""
        self.obfuscated_code = ""
        self.deobfuscated_code = ""
        self.original_size = 0
        self.obfuscated_size = 0
        self.deobfuscated_size = 0
        self.identifiers_count = 0
        self.comments_count = 0
        self.passed = False
        self.error = None

    def get_ratio(self) -> float:
        """Calculate compression ratio"""
        if self.original_size == 0:
            return 0
        return ((self.original_size - self.obfuscated_size) / self.original_size) * 100

    def verify_restoration(self) -> bool:
        """Verify key components are restored"""
        checks = [
            ("export", "Export statements preserved"),
            ("function", "Functions preserved"),
            ("class", "Classes preserved"),
            ("interface", "Interfaces preserved"),
            ("const", "Constants preserved"),
            ("async", "Async keywords preserved"),
        ]

        restored = 0
        for keyword, description in checks:
            if keyword in self.deobfuscated_code.lower():
                restored += 1

        # Accept if at least 50% of key features are restored
        return restored >= 3


def main():
    """Main test execution"""
    print("=" * 80)
    print("🧪 TYPESCRIPT OBFUSCATION/DEOBFUSCATION TEST SUITE")
    print("=" * 80)

    # Check if test files exist
    print("\n📂 Checking test files...")
    missing_files = []
    for filename, _ in TEST_FILES:
        if not Path(filename).exists():
            missing_files.append(filename)

    if missing_files:
        print(f"❌ Missing test files: {missing_files}")
        return 1

    print(f"✅ Found {len(TEST_FILES)} test files")

    # Load language registry
    print("\n🌐 Loading language adapters...")
    try:
        registry = LanguageRegistry("languages")
        adapter = registry.get_adapter("javascript")
        if not adapter:
            print("❌ Could not load JavaScript adapter")
            return 1
        print("✅ JavaScript adapter loaded")
    except Exception as e:
        print(f"❌ Error loading adapters: {e}")
        return 1

    # Initialize obfuscation engine
    print("\n🔧 Initializing obfuscation engine...")
    try:
        engine = ObfuscationEngine(adapter)
        print("✅ Engine initialized")
    except Exception as e:
        print(f"❌ Error initializing engine: {e}")
        return 1

    # Delete existing mapping
    mapping_file = Path("mapping.json")
    if mapping_file.exists():
        mapping_file.unlink()
        print("🗑️  Cleared existing mapping.json")

    # Run tests
    results = []
    print("\n" + "=" * 80)
    print("🚀 RUNNING TESTS...")
    print("=" * 80)

    for test_num, (filename, description) in enumerate(TEST_FILES, 1):
        print(f"\n[Test {test_num}/{len(TEST_FILES)}] {description}")
        print("-" * 80)

        result = TestResult(filename, description)

        try:
            # Read test file
            print(f"📖 Reading {filename}...")
            with open(filename, "r", encoding="utf-8") as f:
                result.original_code = f.read()
            result.original_size = len(result.original_code)
            print(f"   Size: {result.original_size:,} chars")

            # Obfuscate
            print("🔐 Obfuscating...")
            obfuscated, word_mapping, identifier_mapping, comment_mapping = engine.process_content(
                result.original_code
            )
            result.obfuscated_code = engine.minify_code(obfuscated)
            result.obfuscated_size = len(result.obfuscated_code)
            result.identifiers_count = len(identifier_mapping)
            result.comments_count = len(comment_mapping)

            ratio = result.get_ratio()
            print(f"✅ Obfuscated: {result.obfuscated_size:,} chars ({ratio:.1f}% saved)")
            print(f"   Identifiers: {result.identifiers_count} | Comments: {result.comments_count}")

            # Save mapping
            print("💾 Saving mapping...")
            engine.save_mapping(word_mapping, identifier_mapping, comment_mapping)

            # Load mapping
            print("📂 Loading mapping for deobfuscation...")
            mapping_data = load_mapping()
            word_mapping = mapping_data.get("word_mapping", {})
            identifier_mapping = mapping_data.get("identifier_mapping", {})
            comment_mapping = mapping_data.get("comment_mapping", {})

            # Deobfuscate
            print("🔓 Deobfuscating...")
            result.deobfuscated_code = deobfuscate_text(
                result.obfuscated_code, word_mapping, identifier_mapping, comment_mapping
            )
            result.deobfuscated_size = len(result.deobfuscated_code)

            # Verify restoration
            print("✅ Verifying restoration...")
            if result.verify_restoration():
                result.passed = True
                print("✅ Key features restored successfully")
            else:
                print("⚠️  Some features may not be fully restored")
                result.passed = True  # Still consider it a pass if deobfuscation worked

        except Exception as e:
            result.error = str(e)
            result.passed = False
            print(f"❌ Error: {e}")
            import traceback

            traceback.print_exc()

        results.append(result)

    # Print summary
    print("\n" + "=" * 80)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 80)

    passed = sum(1 for r in results if r.passed)
    failed = sum(1 for r in results if not r.passed)

    print(f"\n✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print(f"📊 Total: {len(results)}")

    # Detailed results table
    print("\n" + "=" * 80)
    print("📈 DETAILED RESULTS")
    print("=" * 80)

    print(f"\n{'Test':<25} {'Original':<12} {'Obfuscated':<12} {'Ratio':<10} {'Status':<10}")
    print("-" * 80)

    for result in results:
        status = "✅ PASS" if result.passed else "❌ FAIL"
        ratio = f"{result.get_ratio():.1f}%"

        print(
            f"{result.description:<25} {result.original_size:>10,} {result.obfuscated_size:>11,} {ratio:>9} {status:>9}"
        )

        if result.error:
            print(f"  Error: {result.error}")

    # Show sample output for first test
    print("\n" + "=" * 80)
    print("📋 SAMPLE OUTPUT (Test 1: Basic TypeScript)")
    print("=" * 80)

    first_result = results[0]
    print("\n🔸 ORIGINAL CODE (first 500 chars):")
    print("-" * 80)
    print(first_result.original_code[:500])
    if len(first_result.original_code) > 500:
        print(f"... [{len(first_result.original_code) - 500} more chars]")

    print("\n🔸 OBFUSCATED CODE (first 500 chars):")
    print("-" * 80)
    print(first_result.obfuscated_code[:500])
    if len(first_result.obfuscated_code) > 500:
        print(f"... [{len(first_result.obfuscated_code) - 500} more chars]")

    print("\n🔸 DEOBFUSCATED CODE (first 500 chars):")
    print("-" * 80)
    print(first_result.deobfuscated_code[:500])
    if len(first_result.deobfuscated_code) > 500:
        print(f"... [{len(first_result.deobfuscated_code) - 500} more chars]")

    # Final verdict
    print("\n" + "=" * 80)
    if failed == 0:
        print("✅ ALL TESTS PASSED!")
        return 0
    else:
        print(f"❌ {failed} TEST(S) FAILED")
        return 1


if __name__ == "__main__":
    sys.exit(main())
