# AIShield - Code Obfuscation Against AI Detection

A language-agnostic code obfuscator designed to protect proprietary code from AI-based analysis and reverse engineering. AIShield preserves framework identifiers while intelligently obfuscating custom code, maintaining functionality while disrupting AI pattern recognition.

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![GitHub](https://img.shields.io/badge/GitHub-AIShield-blue?logo=github)](https://github.com/webinadvance/aishield)

## Features

- **Smart Obfuscation:** Preserves framework APIs (React, AspNetCore, etc.) while obfuscating custom logic
- **Multi-Language:** C#, JavaScript/TypeScript with extensible plugin architecture
- **AI-Resistant:** Disrupts pattern matching and intent inference by AI models
- **Deterministic:** Consistent hashing ensures reproducible results across builds
- **Framework-Aware:** Preserves common patterns (Async, Controller, Service, Handler, etc.)
- **Reversible:** Generates mapping files for unminification if needed
- **Developer-Friendly:** Auto-language detection and clipboard integration

## Installation

### Prerequisites
- Python 3.8+
- pip

### Quick Setup

```bash
pip install -r requirements.txt
```

Or install directly from distribution:
```bash
pip install code-defender
```

## Quick Start

### CLI Usage

```bash
code-defender
```

**Workflow:**
1. Copy code to clipboard
2. Run `code-defender`
3. Select language (auto-detected) or press Enter to skip
4. Obfuscated code copied to clipboard

### Language Support

```bash
code-defender
# Loaded languages: csharp, javascript
```

## How It Works

### Obfuscation Strategy

AIShield uses **intelligent preservation** to balance security and maintainability:

| Element | Handling | Reason |
|---------|----------|--------|
| Framework APIs | ✅ Preserved | Needed for compilation/runtime |
| Custom identifiers | ❌ Obfuscated | Protects business logic |
| Method suffixes | ✅ Preserved | Date, Service, Handler, Controller, etc. |
| Imports/Namespaces | ✅ Preserved | Required for code functionality |
| String literals | ❌ Encrypted | Hides hardcoded values |

### Example Impact

- `UserController` → `E1234Controller` (class name hidden, pattern preserved)
- `calculateTotalAmount()` → `C5892E1234()` (logic hidden)
- `HttpClient.Get()` → `HttpClient.Get()` (framework unchanged)
- Custom namespaces → Obfuscated
- Framework namespaces → Preserved

## Configuration

### Global Preservation

Edit `preserve_custom.json` to add project-specific terms:

```json
{
  "preserve": [
    "MyCompany",
    "ProjectX",
    "PartnerAPI"
  ]
}
```

### Language-Specific Lists

Framework words are configured per language:
- `languages/csharp/preserve_language.json` - C# framework terms
- `languages/javascript/preserve_language.json` - JS/TypeScript framework terms

**Don't edit these unless adding new framework words.**

### Custom Suffixes

Modify `get_preserve_suffixes()` in language adapters to preserve domain-specific patterns:

```python
def get_preserve_suffixes(self):
    return ['Async', 'Controller', 'Service', 'Repository', 'Handler']
```

## Advanced Usage

### Reverse Mapping

Obfuscation mappings are saved in `obfuscation_mapping_<language>.json`:

```json
{
  "created_at": "2025-10-30T12:00:00",
  "language": "csharp",
  "reverse_map": {
    "C1234": "MyCompany",
    "E5678": "UserService"
  }
}
```

Use this to track obfuscated identifiers or unminify code if needed.

### Add New Language Support

Create a language plugin:

1. **Create directory:**
   ```bash
   mkdir languages/python
   ```

2. **Create `adapter.py`** (inherit from `LanguageAdapter`):
   - Implement parser setup
   - Define identifier patterns
   - Add detection patterns

3. **Create `preserve_language.json`** with framework terms

4. **Install tree-sitter parser:**
   ```bash
   pip install tree-sitter-python
   ```

See existing adapters (`languages/csharp/adapter.py`, `languages/javascript/adapter.py`) for reference.

## Use Cases

- **AI Protection:** Defend proprietary algorithms from AI code analysis and regeneration
- **IP Protection:** Obfuscate business logic while maintaining code readability for developers
- **Supply Chain Security:** Secure code from AI training dataset absorption
- **Demo Code:** Share samples without exposing business logic
- **Code Size Reduction:** Minify while maintaining AI resistance

## Limitations

- **Not Encryption:** Obfuscation is reversible; determined reverse engineering can recover logic
- **Parser Dependent:** Relies on tree-sitter; edge cases may not parse correctly
- **String Literals:** Obfuscates all strings; may break hardcoded dependencies
- **Dynamic Code:** Cannot handle runtime code generation or reflection-based logic

## Architecture

```
aishield/
├── base.py                    # Base language adapter interface
├── minify.py                  # Obfuscation engine
├── unminify.py                # Reverse obfuscation utility
├── cli.py                     # Command-line interface
├── preserve_custom.json       # Global preservation list
├── languages/
│   ├── csharp/
│   │   ├── adapter.py
│   │   └── preserve_language.json
│   └── javascript/
│       ├── adapter.py
│       └── preserve_language.json
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

**Areas for contribution:**
- Additional language support (Python, Go, Java, Rust, etc.)
- Framework word list expansion
- CLI enhancements
- Documentation improvements

## License

BSD 3-Clause License - see [LICENSE](LICENSE)

## Support

- **Issues:** [GitHub Issues](https://github.com/webinadvance/aishield/issues)
- **Discussions:** [GitHub Discussions](https://github.com/webinadvance/aishield/discussions)

---

**⚠️ Note:** AIShield is a defensive obfuscation tool. Use responsibly and in compliance with applicable laws and regulations.
