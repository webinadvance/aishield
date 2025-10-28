# Contributing to AIShield

Thank you for considering contributing to AIShield! This document provides guidelines and instructions for contributing to our code obfuscation and AI protection project.

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. Please be respectful and constructive in all interactions.

### Our Standards

✅ **Do:**
- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards others

❌ **Don't:**
- Use inappropriate language or imagery
- Engage in personal attacks or trolling
- Harass others publicly or privately
- Publish others' private information

## How to Contribute

### Reporting Bugs

Before creating a bug report, please check existing issues to avoid duplicates.

**When filing a bug report, include:**
- Clear, descriptive title
- Steps to reproduce the issue
- Expected vs actual behavior
- Code samples (obfuscated if needed)
- Your environment:
  - OS (Windows, macOS, Linux)
  - Python version
  - Package versions
- Screenshots if applicable

**Example:**
```markdown
## Bug: C# async methods not preserving Async suffix

**Environment:**
- OS: Windows 11
- Python: 3.11.0
- tree-sitter: 0.20.0
- tree-sitter-c-sharp: 0.20.0

**Steps to Reproduce:**
1. Copy C# code with `GetDataAsync()` method
2. Run `python minify.py`
3. Method becomes `C1234D5678()`

**Expected:** `GetDataAsync` → `C1234D5678Async`
**Actual:** `GetDataAsync` → `C1234D5678`

**Code Sample:**
\`\`\`csharp
public async Task<Data> GetDataAsync() { }
\`\`\`
```

### Suggesting Features

Feature requests are welcome! Please provide:
- Clear use case and motivation
- Expected behavior
- Any alternative solutions you've considered
- Willingness to implement (if applicable)

### Pull Requests

#### Before Submitting

1. **Check existing issues/PRs** to avoid duplication
2. **Discuss major changes** in an issue first
3. **Fork the repository** and create a branch from `main`
4. **Follow the coding standards** (see below)

#### Pull Request Process

1. **Create a branch:**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

2. **Make your changes:**
   - Write clear, concise commit messages
   - Add tests if applicable
   - Update documentation

3. **Test thoroughly:**
   ```bash
   # Ensure no syntax errors
   python -m py_compile *.py languages/*/*.py

   # Test with sample code
   python minify.py
   ```

4. **Update documentation:**
   - Update README.md if adding features
   - Add docstrings to new functions/classes
   - Update CHANGELOG.md (if exists)

5. **Submit PR:**
   - Clear title describing the change
   - Reference related issues (#123)
   - Describe what changed and why
   - Include before/after examples if applicable

#### PR Title Format

```
[TYPE] Brief description

Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation only
- style: Code formatting
- refactor: Code restructuring
- perf: Performance improvement
- test: Adding tests
- chore: Maintenance tasks
```

**Examples:**
- `feat: Add Python language support`
- `fix: Preserve Async suffix in C# methods`
- `docs: Update installation instructions`

## Development Setup

### 1. Fork and Clone

```bash
git clone https://github.com/yourusername/aishield.git
cd aishield
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create Test Branch

```bash
git checkout -b test/your-test
```

### 4. Make Changes

### 5. Test

```bash
# Quick syntax check
python -m py_compile minify.py base.py

# Manual test
python minify.py
```

## Coding Standards

### Python Style

Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines:

```python
# Good
def obfuscate_composite(self, name, word_mapping):
    """Obfuscate a composite identifier.

    Args:
        name: The identifier to obfuscate
        word_mapping: Dictionary mapping words to hashes

    Returns:
        str: Obfuscated identifier
    """
    if self.should_preserve(name):
        return name
    # ... implementation

# Bad
def obfuscateComposite(self,name,word_mapping):
    if self.should_preserve(name):return name
```

### Documentation

**All public methods must have docstrings:**

```python
def get_preserve_suffixes(self):
    """Return common suffixes that should be preserved during obfuscation.

    Override this method in language-specific adapters to preserve
    common naming conventions.

    Returns:
        list[str]: Suffixes to preserve (e.g., ['Async', 'Controller'])
    """
    return []
```

### Naming Conventions

- **Variables:** `snake_case`
- **Functions:** `snake_case`
- **Classes:** `PascalCase`
- **Constants:** `UPPER_SNAKE_CASE`
- **Private methods:** `_leading_underscore`

### File Organization

```python
#!/usr/bin/env python3
"""
Brief module description.

Detailed description if needed.
"""

# Standard library imports
import json
import sys
from pathlib import Path

# Third-party imports
from tree_sitter import Language, Parser

# Local imports
from base import LanguageAdapter

# Constants
DEFAULT_TIMEOUT = 30

# Classes and functions
class MyClass:
    pass
```

## Adding New Languages

### Step-by-Step Guide

1. **Create language directory:**
   ```bash
   mkdir languages/python
   ```

2. **Create adapter:** `languages/python/adapter.py`

3. **Implement all abstract methods:**
   - `get_parser()`
   - `get_string_node_types()`
   - `get_comment_node_types()`
   - `get_exclude_patterns()`
   - `get_import_node_types()`
   - `should_remove_import()`
   - `get_preserve_import_ranges()`
   - `get_detection_patterns()`
   - `get_preserve_suffixes()` (optional)

4. **Create preserve list:** `languages/python/preserve_language.json`

5. **Install tree-sitter parser:**
   ```bash
   pip install tree-sitter-python
   ```

6. **Test thoroughly with real code**

7. **Update README.md** with new language

8. **Submit PR**

## Testing Guidelines

### Manual Testing Checklist

For language adapters:

- [ ] Auto-detection works correctly
- [ ] Framework identifiers are preserved
- [ ] Custom code is obfuscated
- [ ] Suffixes are preserved correctly
- [ ] Import statements handled properly
- [ ] String literals obfuscated
- [ ] Comments removed/replaced
- [ ] Output is valid code
- [ ] Mapping file generated correctly

### Test with Real Code

Test with at least 3 different code samples:
1. Small snippet (10-20 lines)
2. Medium file (100-200 lines)
3. Large file (500+ lines)

## Project Structure

```
aishield/
├── base.py                    # Abstract base classes
├── minify.py                  # Main obfuscation engine
├── unminify.py                # Reverse utility
├── preserve_custom.json       # User custom words
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation
├── CONTRIBUTING.md            # This file
├── LICENSE                    # BSD 3-Clause License
├── .gitignore                 # Git ignore rules
└── languages/                 # Language adapters
    ├── csharp/
    │   ├── adapter.py
    │   └── preserve_language.json
    └── javascript/
        ├── adapter.py
        └── preserve_language.json
```

## Versioning

We follow [Semantic Versioning](https://semver.org/):
- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes (backward compatible)

## Questions?

- **Open an issue** for questions about contributing
- **Start a discussion** for general questions
- **Check existing docs** in README.md

## License

By contributing, you agree that your contributions will be licensed under the BSD 3-Clause License.

---

**Thank you for contributing!** 🎉
