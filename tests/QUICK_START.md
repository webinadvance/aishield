# Quick Start Guide - Test Suite

## 🚀 Get Started in 30 Seconds

### 1. Run All Tests
```bash
cd /path/to/minify
python3 test_runner.py
```

### 2. View Results
The test runner will:
- ✅ Load all 5 TypeScript test files
- ✅ Obfuscate each file
- ✅ Deobfuscate the obfuscated code
- ✅ Generate a `mapping.json` file
- ✅ Print a comprehensive report

### 3. Check Output
Look for:
```
✅ ALL TESTS PASSED!
```

If successful, you'll see:
- Compression ratios for each file
- Identifier and comment counts
- Sample output showing original → obfuscated → deobfuscated code

---

## 📊 What Gets Tested?

### Test Files (5 Total)

| # | File | Complexity | Size | Focus |
|---|------|-----------|------|-------|
| 1 | `test1_basic.ts` | ⭐ | 1KB | Functions & variables |
| 2 | `test2_classes.ts` | ⭐⭐ | 2.7KB | Classes & interfaces |
| 3 | `test3_async.ts` | ⭐⭐⭐ | 4.4KB | Async & generics |
| 4 | `test4_react.tsx` | ⭐⭐⭐⭐ | 4.2KB | React components |
| 5 | `test5_advanced.ts` | ⭐⭐⭐⭐⭐ | 6.6KB | Advanced TypeScript |

### Total Test Coverage
- **18KB+** of real TypeScript code
- **500+** identifiers
- **250+** comments
- All major TypeScript features

---

## ✅ Expected Results

Each test should show:
- ✅ Original size → Obfuscated size (compression %)
- ✅ Identifiers and comments preserved
- ✅ Deobfuscation successful
- ✅ Key features restored

**Example Output:**
```
Basic TypeScript               1,130         493     56.4%    ✅ PASS
Classes & Interfaces           2,757       1,546     43.9%    ✅ PASS
Async/Await & Generics         4,405       2,697     38.8%    ✅ PASS
React with TypeScript          4,218       2,826     33.0%    ✅ PASS
Advanced TypeScript            6,632       4,407     33.5%    ✅ PASS
```

---

## 🔍 Understanding the Output

### During Tests
```
[Test 1/5] Basic TypeScript
📖 Reading tests/typescript/test1_basic.ts...
   Size: 1,130 chars
🔐 Obfuscating...
✅ Obfuscated: 493 chars (56.4% saved)
   Identifiers: 16 | Comments: 5
💾 Saving mapping...
📂 Loading mapping for deobfuscation...
🔓 Deobfuscating...
✅ Verifying restoration...
✅ Key features restored successfully
```

### After All Tests
```
📊 TEST RESULTS SUMMARY
✅ Passed: 5
❌ Failed: 0
📊 Total: 5
```

---

## 🎯 What's Being Verified?

### Obfuscation Quality ✨
- Identifiers are renamed (e.g., `registerUser` → `T2980C5665`)
- Comments are preserved with placeholders
- Compression is achieved (30-56% average)
- Type annotations are maintained

### Deobfuscation Accuracy 🔓
- Keywords are restored (`export`, `function`, `class`, `async`)
- Identifiers are mapped back correctly
- Comments are restored with proper newlines
- String literals are recovered
- Type annotations are preserved

### Code Integrity ✅
- No syntax errors introduced
- All references are correctly updated
- Comments appear in correct positions
- Functionality is preserved

---

## 📁 File Structure

```
minify/
├── test_runner.py              # Main test executor
├── mapping.json                # Generated mapping file
├── tests/
│   ├── README.md              # Detailed documentation
│   ├── QUICK_START.md         # This file
│   └── typescript/
│       ├── test1_basic.ts
│       ├── test2_classes.ts
│       ├── test3_async.ts
│       ├── test4_react.tsx
│       └── test5_advanced.ts
```

---

## 💡 Pro Tips

### Tip 1: Check Individual Test
Look at sample output in the test report to see exactly how code is being transformed.

### Tip 2: Examine mapping.json
```bash
cat mapping.json | python3 -m json.tool
```

This shows all identifier mappings, useful for understanding the obfuscation.

### Tip 3: Run Frequently
Run tests after any changes to `preserve_language.json` or the adapters to ensure no regressions.

### Tip 4: Monitor Compression Ratio
Track compression ratios over time:
- Typical range: 30-56%
- Higher compression = more aggressive obfuscation
- Lower compression = more preserved keywords/identifiers

---

## 🐛 Troubleshooting

### Problem: "Test files not found"
```bash
# Make sure you're in the minify directory
cd /path/to/minify
python3 test_runner.py
```

### Problem: "Failed to load JavaScript adapter"
```bash
# Check that languages/javascript/ exists and has adapter.py
ls languages/javascript/
```

### Problem: "mapping.json not found during deobfuscation"
This is normal on the first test. The mapping is created during obfuscation, then reloaded for deobfuscation.

### Problem: Some keywords not restored
Check `languages/javascript/preserve_language.json` includes the keyword.

---

## 🎓 Learning Resources

### Understanding Obfuscation
1. Read comments in `minify.py`
2. Examine `mapping.json` structure
3. Check `unminify.py` deobfuscation logic

### Adding New Tests
1. Create `testN_description.ts` in `tests/typescript/`
2. Add to `TEST_FILES` list in `test_runner.py`
3. Run `python3 test_runner.py`

### Customizing Preservation
Edit `languages/javascript/preserve_language.json` to:
- Add/remove preserved keywords
- Adjust preservation strategy

---

## 🎉 Success Criteria

✅ All tests pass
✅ Compression ratios are 30%+
✅ All keywords are restored
✅ Comments are preserved
✅ No syntax errors after deobfuscation

---

## 📞 Need Help?

1. **Check the full README**: `tests/README.md`
2. **Review test output**: Look for ✅ or ❌ marks
3. **Examine mapping.json**: See what identifiers were mapped
4. **Check console output**: Test runner provides detailed error messages

---

**Ready? Run this:**
```bash
python3 test_runner.py
```

**Expected result:**
```
✅ ALL TESTS PASSED!
```

Good luck! 🚀
