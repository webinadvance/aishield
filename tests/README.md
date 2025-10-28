# TypeScript Obfuscation Test Suite

Comprehensive test suite for validating TypeScript/JavaScript obfuscation and deobfuscation functionality.

## 📁 Test Files

### Test 1: Basic TypeScript (`test1_basic.ts`)
- **Complexity**: ⭐ Basic
- **Lines**: ~45
- **Tests**:
  - Function declarations with comments
  - Type annotations (string, boolean, Map)
  - Comments with parameter documentation
  - Variable declarations
  - Function calls and console logging

**Key Features Tested**:
- ✅ Basic function obfuscation
- ✅ Type preservation (string, boolean)
- ✅ Comment restoration with newlines
- ✅ Variable renaming

---

### Test 2: Classes & Interfaces (`test2_classes.ts`)
- **Complexity**: ⭐⭐ Intermediate
- **Lines**: ~110
- **Tests**:
  - Interface definitions
  - Abstract class inheritance
  - Public/protected/private access modifiers
  - Method declarations with complex logic
  - Array operations and functional programming

**Key Features Tested**:
- ✅ Interface preservation
- ✅ Class and method obfuscation
- ✅ Access modifier handling
- ✅ Comment documentation preservation
- ✅ Complex identifier renaming

---

### Test 3: Async/Await & Generics (`test3_async.ts`)
- **Complexity**: ⭐⭐⭐ Advanced
- **Lines**: ~160
- **Tests**:
  - Generic types and constraints
  - Async/await patterns
  - Promise handling
  - Generic class implementation
  - Service pattern with dependency injection
  - Try/catch error handling
  - Array operations (map, filter)

**Key Features Tested**:
- ✅ Generic type parameter preservation
- ✅ Async/await keyword preservation
- ✅ Promise type handling
- ✅ Complex class hierarchies
- ✅ Error handling patterns

---

### Test 4: React with TypeScript (`test4_react.tsx`)
- **Complexity**: ⭐⭐⭐⭐ Expert
- **Lines**: ~165
- **Tests**:
  - React functional components
  - TypeScript interfaces for props
  - React hooks (useState, useEffect, useCallback)
  - JSX syntax
  - React.FC type annotations
  - Event handling

**Key Features Tested**:
- ✅ React imports preservation
- ✅ JSX element preservation
- ✅ Hook obfuscation safety
- ✅ Props interface handling
- ✅ Callback function preservation

---

### Test 5: Advanced TypeScript (`test5_advanced.ts`)
- **Complexity**: ⭐⭐⭐⭐⭐ Expert
- **Lines**: ~300
- **Tests**:
  - Enumerations (HttpMethod, RequestStatus)
  - Generic types and constraints
  - Utility types (Partial, Readonly, etc.)
  - Conditional types
  - Mapped types
  - Repository pattern with generics
  - CRUD operations
  - Pagination logic

**Key Features Tested**:
- ✅ Enum preservation
- ✅ Complex generic constraints
- ✅ Utility type handling
- ✅ Conditional type patterns
- ✅ Repository pattern obfuscation

---

## 🚀 Running Tests

### Run All Tests
```bash
python3 test_runner.py
```

### Run Individual Test
```bash
# Using the test_workflow.py script from root
python3 test_workflow.py
```

## 📊 Test Results

All tests verify:

1. **Obfuscation Quality**
   - Compression ratio (% saved)
   - Identifier count
   - Comment preservation count

2. **Deobfuscation Accuracy**
   - Keywords restored (export, function, class, interface, const, async)
   - Comments restored with proper newlines
   - String literals restored
   - Type annotations preserved

3. **Code Integrity**
   - No syntax errors after deobfuscation
   - All identifiers properly mapped back
   - Comments properly positioned

## 📈 Expected Results

| Test | Original | Obfuscated | Ratio | Status |
|------|----------|-----------|-------|--------|
| Basic TypeScript | 1,130 | 493 | 56.4% | ✅ PASS |
| Classes & Interfaces | 2,757 | 1,546 | 43.9% | ✅ PASS |
| Async/Await & Generics | 4,405 | 2,697 | 38.8% | ✅ PASS |
| React with TypeScript | 4,218 | 2,826 | 33.0% | ✅ PASS |
| Advanced TypeScript | 6,632 | 4,407 | 33.5% | ✅ PASS |

## 🔧 Configuration

### Preserve Words
Located at: `languages/javascript/preserve_language.json`

Includes:
- All JavaScript/TypeScript keywords
- React hooks and APIs
- Common library identifiers
- DOM APIs
- Built-in objects and methods

### Keywords
Located at: `languages/javascript/keywords_javascript.json`

Includes:
- Language-specific keywords
- Async/await patterns
- Module syntax (import/export)
- Type modifiers

## 📝 Mapping File

After running tests, check `mapping.json` for:

```json
{
  "word_mapping": { ... },
  "identifier_mapping": { ... },
  "comment_mapping": { ... },
  "reverse_map": { ... }
}
```

## ✅ Verification Checklist

- [x] All test files load correctly
- [x] Obfuscation succeeds for all test files
- [x] Compression ratios meet expectations (30-56%)
- [x] Comments are properly restored
- [x] Keywords are preserved
- [x] Identifiers are correctly mapped
- [x] Type annotations are preserved
- [x] React/JSX syntax is handled
- [x] Async/await patterns work correctly
- [x] Generic types are preserved

## 🐛 Troubleshooting

### Issue: Test file not found
**Solution**: Ensure you're running `test_runner.py` from the project root directory

### Issue: Deobfuscation missing keywords
**Solution**: Check `preserve_language.json` contains the required keywords

### Issue: Mapping file conflicts
**Solution**: Delete `mapping.json` and regenerate with fresh test

## 📚 Files Included

```
tests/
├── README.md                          # This file
├── typescript/
│   ├── test1_basic.ts                # Basic functions & variables
│   ├── test2_classes.ts              # Classes & interfaces
│   ├── test3_async.ts                # Async/Await & generics
│   ├── test4_react.tsx               # React components
│   └── test5_advanced.ts             # Advanced TypeScript features
```

## 🎯 Test Coverage

### Language Features
- ✅ Functions & arrow functions
- ✅ Classes & inheritance
- ✅ Interfaces
- ✅ Generics
- ✅ Async/Await
- ✅ Promises
- ✅ Decorators
- ✅ Enums
- ✅ Type annotations
- ✅ React components
- ✅ JSX syntax

### Comments & Documentation
- ✅ Single-line comments
- ✅ Multi-line comments
- ✅ JSDoc documentation
- ✅ Parameter documentation

### Advanced Features
- ✅ Mapped types
- ✅ Conditional types
- ✅ Utility types
- ✅ Generic constraints
- ✅ Repository patterns
- ✅ Async patterns

## 📞 Support

For issues or questions:
1. Check this README
2. Review test output logs
3. Examine the generated `mapping.json`
4. Check `preserve_language.json` for keyword inclusion

---

**Last Updated**: 2025-10-28
**Test Suite Version**: 1.0
**Compatibility**: TypeScript 4.0+, JavaScript ES2020+
