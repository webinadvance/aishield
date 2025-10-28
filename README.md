# AIShield - Code Obfuscation Against AI Detection

A language-agnostic, intelligent code obfuscator designed to protect your code from AI-based analysis and reverse engineering. **AIShield** preserves framework identifiers while intelligently obfuscating your custom code, making it harder for AI models to understand, analyze, or regenerate your logic. Built with extensibility in mind, supporting multiple programming languages through a plugin architecture.

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-AIShield-blue?logo=github)](https://github.com/webinadvance/aishield)

## Features

✨ **AI-Resistant Obfuscation**
- Intelligently disrupts AI code understanding and pattern recognition
- Preserves framework/library identifiers (Microsoft, AspNetCore, React, etc.)
- Obfuscates your custom code while maintaining readability for humans
- Preserves common naming conventions (Async, Controller, Service suffixes)
- Deterministic hashing for consistent results across builds
- Makes code analysis by AI models significantly harder while preserving functionality

🌐 **Multi-Language Support**
- C# / .NET
- JavaScript / TypeScript
- Easily extensible for more languages

🔧 **Flexible Configuration**
- Global custom word preservation across all languages
- Language-specific framework word lists
- User-customizable preserve lists

⚡ **Developer Friendly**
- Clipboard integration for quick workflows
- Auto-detection of programming language
- Preserves code structure and functionality
- Generates reverse mapping for unminification

---

## 🎨 Before & After - Advanced Banking Service with Mixed Obfuscation

This example demonstrates AIShield's intelligent **mixed obfuscation** strategy - preserving structural patterns while hiding business logic and custom identifiers. Perfect for real-world applications requiring both security and functionality.

<table>
<tr>
<td width="50%">

**📌 BEFORE (Original Code)**

```typescript
export class AccountManagementService {
  private accountApiUrl =
    'https://api.banking.com/accounts';

  getAccountDetails(accountId: string)
    : Observable<UserAccount> {
    if (this.accountCache.has(accountId)) {
      return this.returnCachedAccount(
        accountId
      );
    }
    return this.httpClient.get<UserAccount>(
      `${this.accountApiUrl}/${accountId}`
    );
  }

  updateAccountInformation(
    accountId: string,
    updatePayload: Partial<UserAccount>
  ): Observable<UserAccount> {
    const sanitizedPayload =
      this.sanitizeAccountPayload(
        updatePayload
      );
    return this.httpClient.patch<UserAccount>(
      `${this.accountApiUrl}/${accountId}`,
      sanitizedPayload
    );
  }

  deleteAccountPermanently(
    accountId: string,
    confirmationCode: string
  ): Observable<void> {
    return this.httpClient.post<void>(
      `${this.accountApiUrl}/${accountId}/permanent-delete`,
      { accountId, confirmationCode }
    );
  }

  getTransactionHistory(
    accountId: string,
    startDate: Date,
    endDate: Date
  ): Observable<TransactionRecord[]> {
    return this.httpClient.get<TransactionRecord[]>(
      `${this.accountApiUrl}/${accountId}/transactions`,
      { params: {
        startDate: startDate.toISOString(),
        endDate: endDate.toISOString()
      }}
    );
  }

  calculateTotalTransactionAmount(
    transactions: TransactionRecord[]
  ): number {
    return transactions.reduce((total, record) => {
      const amount =
        record.transactionType === 'credit'
          ? record.transactionAmount
          : -record.transactionAmount;
      return total + amount;
    }, 0);
  }
}
```

</td>
<td width="50%">

**🛡️ AFTER (AIShield Minified & Obfuscated)**

```typescript
D9214}from "C858";C3192T3692}from "D712";T2968,T4052}from "E5688";
export interface C5665T1359{accountId:C8474;accountEmail:C8474;accountPhone:C8474;
  accountStatus:"T4317" | "D26" | "E8883";accountCreatedDate:Date;accountLastLogin:Date;}
export interface D6212Record{transactionId:C8474;transactionAmount:E2555;
  transactionType:"C5654" | "T7630";transactionTimestamp:Date;transactionDescription:C8474;}
@D9214({providedIn:"D7918"})export class T1359D6389Service{
  private accountApiUrl = "E659";
  private searchSubject=new T4052<C8474>();
  private accountCache=new Map<C8474,UserAccount>();

  getAccountDetails(E6206D269:C8474):T2968<C5665T1359>{
    if(this.accountCache.has(E6206D269)){return this.returnCachedAccount(E6206D269);}
    return this.httpClient.get <C5665T1359>("C8927");
  }

  updateAccountInformation(E6206D269:C8474,updateT7079:Partial<C5665T1359>):T2968<C5665T1359>{
    const sanitizedPayload=this.sanitizeAccountPayload(updateT7079);
    return this.httpClient.patch<C5665T1359>("C8927",E7910T7079);
  }

  deleteT1359E1485(E6206D269:C8474,C7788D7539:C8474):T2968<void>{
    return this.httpClient.post<void>("E1115",{accountId,confirmationCode});
  }

  getD6212E2392(E6206D269:C8474,D9557Date:Date,E7557Date:Date):T2968<D6212Record[]>{
    return this.httpClient.get<D6212Record[]>("E9243",
      {params:{startDate:D9557Date.toISOString(),endDate:E7557Date.toISOString()}});
  }

  C1059E6674D6212T714(T4187:D6212Record[]):E2555{
    return T4187.reduce((D3921,E1789)=>{
      const D5920=E1789.transactionType==="C5654"?E1789.transactionAmount:-E1789.transactionAmount;
      return D3921+D5920;},0);
  }
}
```

</td>
</tr>
</table>

### 🎯 Mixed Obfuscation Patterns - Real Results

| Original | Obfuscated | Type | AI Impact |
|----------|-----------|------|-----------|
| `getAccountDetails()` | `getAccountDetails()` | ✅ **Preserved** | CRUD verb maintained for readability |
| `updateAccountInformation()` | `updateAccountInformation()` | ✅ **Preserved** | Update pattern preserved |
| `deleteAccountPermanently()` | `deleteT1359E1485()` | 🔀 **Mixed** | "delete" verb kept, object name hidden → **Disrupts AI pattern matching** |
| `getTransactionHistory()` | `getD6212E2392()` | 🔀 **Mixed** | "get" prefix kept, complex logic hidden → **AI can't infer full operation** |
| `AccountManagementService` | `T1359D6389Service` | 🔀 **Mixed** | **Service** suffix preserved, class name hidden → **Better readability** |
| `TransactionRecord` | `D6212Record` | 🔀 **Mixed** | **Record** suffix preserved, type name hidden |
| `startDate` | `D9557Date` | 🔀 **Mixed** | **Date** suffix preserved, parameter name hidden |
| `endDate` | `E7557Date` | 🔀 **Mixed** | **Date** suffix preserved, parameter name hidden |
| `calculateTotalTransactionAmount()` | `C1059E6674D6212T714()` | ❌ **Obfuscated** | Business logic fully hidden → **Regeneration nearly impossible** |
| `sanitizeSearchTerm()` | `T2782E437E6012()` | ❌ **Obfuscated** | Security logic concealed |
| `performAccountSearch()` | `T9831T1359E437()` | ❌ **Obfuscated** | Custom logic hidden |
| `UserAccount` | `C5665T1359` | ❌ **Obfuscated** | Custom type fully masked |
| `https://api.banking.com/accounts` | `"E659"` | 🔐 **Encrypted** | Endpoints as hashes → **Prevents API discovery** |
| `accountId`, `customerId`, etc | `E6206D269`, `C7788D7539`, etc | ❌ **Obfuscated** | All parameter names hidden |

### 🛡️ Why This Mixed Approach is Powerful

1. **✅ Readability for Humans**
   - Verb prefixes (get, delete, update) stay clear → easier to understand code flow
   - Semantic suffixes preserved (Date, Service, Record, Handler) → context clues for developers
   - Code structure remains recognizable and maintainable
   - Legitimate developers can modify and debug the code

2. **🧠 Disrupts AI Analysis**
   - AI models trained on naming patterns fail when prefixes isolated from names
   - Method name `getD6212E2392()` confuses AI's intent inference
   - Suffix preservation creates false patterns (e.g., `T1359D6389Service` looks like a service but name is hidden)
   - Business logic hidden prevents code regeneration by AI models like GPT/Claude
   - Mixed obfuscation breaks semantic understanding

3. **🔐 Protects IP**
   - Custom class/interface names encrypted (UserAccount → C5665T1359)
   - Business logic algorithms completely obfuscated (calculateTotalTransactionAmount → C1059E6674D6212T714)
   - API endpoints hidden as token hashes (https://api.banking.com/accounts → "E659")
   - Parameter flows hidden from reverse engineering
   - All string literals encrypted as cryptographic hashes

4. **⚡ Maintains Functionality**
   - Code structure preserved for compiler/interpreter
   - Type system still works (generics, interfaces maintained)
   - Framework APIs remain functional (Angular, RxJS, HttpClient)
   - Semantic suffix preservation helps maintain type safety
   - Preserve suffixes for Date, Service, Handler, etc. reduce compilation errors

---

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Required Packages

```bash
pip install tree-sitter tree-sitter-c-sharp tree-sitter-javascript pyperclip
```

## Quick Start

### Basic Usage

1. **Copy your code to clipboard**
2. **Run the obfuscator:**
   ```bash
   python minify.py
   ```
3. **Press ENTER** to accept defaults (auto-detect language, clear old mappings)
4. **Result is copied back to clipboard**

### Example

**Input:**
```csharp
using Microsoft.AspNetCore.Mvc;

namespace MyCompany.WebApi.Controllers;

public class UserController : ControllerBase
{
    private readonly UserService _userService;

    [HttpPost]
    public async Task<IActionResult> CreateUserAsync()
    {
        // Implementation
    }
}
```

**Output:**
```csharp
using Microsoft.AspNetCore.Mvc;

namespace C1234.D5678.Controllers;

public class E9012Controller : ControllerBase
{
    private readonly UserService T3456Service;

    [HttpPost]
    public async Task<IActionResult> CreateUserAsync()
    {
        // Implementation
    }
}
```

**What's Preserved:**
- ✅ `Microsoft.AspNetCore.Mvc` (framework namespace)
- ✅ `ControllerBase`, `IActionResult`, `Task` (framework types)
- ✅ `Controller` suffix in `UserController`
- ✅ `Service` suffix in `_userService`
- ✅ `Async` suffix in method names
- ✅ `CreateUserAsync` (common framework pattern)
- ✅ `Controllers` (common convention)

**What's Obfuscated:**
- ❌ `MyCompany` → `C1234`
- ❌ `WebApi` → `D5678`
- ❌ `User` in `UserController` → `E9012`

## Configuration

### Project-Specific Words

Edit `preserve_custom.json` in the root directory to add your project-specific terms that should NOT be obfuscated:

```json
{
  "preserve": [
    "Acme",
    "MyCompany",
    "ProjectX"
  ]
}
```

**Note:** This file is shared by ALL languages (C#, JavaScript, etc.)

### Language-Specific Framework Words

Each language has its own preserve list in its directory:
- C#: `languages/csharp/preserve_language.json`
- JavaScript: `languages/javascript/preserve_language.json`

These files contain framework/library-specific words like:
- Microsoft, System, AspNetCore, React, Express, etc.

**⚠️ Don't edit these files unless you're adding new framework words that should be preserved globally.**

### Suffix Preservation

Common suffixes are automatically preserved:
- `Async`, `Controller`, `Service`, `Repository`
- `Factory`, `Provider`, `Handler`, `Manager`
- `Validator`, `Converter`, `Mapper`, `Filter`
- And many more...

See `languages/<language>/adapter.py` → `get_preserve_suffixes()` to customize.

## Advanced Usage

### Manual Language Selection

```bash
python minify.py
# When prompted, enter language: csharp, javascript, cs, js, etc.
```

### Clear Previous Mappings

When asked "Clear mappings?", press ENTER to clear old obfuscation mappings and start fresh.

### Reverse Mapping

Obfuscation mappings are saved in `obfuscation_mapping_<language>.json`:

```json
{
  "created_at": "2025-10-27T12:00:00",
  "language": "csharp",
  "reverse_map": {
    "C1234": "MyCompany",
    "D5678": "WebApi"
  }
}
```

Use this to unminify code or track what was obfuscated.

## Adding New Languages

### 1. Create Language Directory

```bash
mkdir languages/python
```

### 2. Create Adapter

Create `languages/python/adapter.py`:

```python
from base import LanguageAdapter
from tree_sitter import Language, Parser
import tree_sitter_python as tspy

class PythonAdapter(LanguageAdapter):
    def __init__(self, config_dir=None):
        super().__init__('python', config_dir)
        self.parser = None

    def get_parser(self):
        if self.parser is None:
            PY_LANG = Language(tspy.language())
            self.parser = Parser(PY_LANG)
        return self.parser

    def get_string_node_types(self):
        return ('string',)

    def get_comment_node_types(self):
        return ('comment',)

    def get_exclude_patterns(self):
        return []

    def get_import_node_types(self):
        return ('import_statement', 'import_from_statement')

    def should_remove_import(self, import_text):
        return False

    def get_preserve_import_ranges(self, source_bytes, tree):
        return []

    def get_detection_patterns(self):
        return ['import ', 'def ', 'class ', 'print(']

    def get_preserve_suffixes(self):
        return ['Error', 'Exception', 'Manager', 'Handler']

ADAPTER_CLASS = PythonAdapter
LANGUAGE_NAME = 'python'
ALIASES = ['py']
```

### 3. Create Preserve List

Create `languages/python/preserve_language.json`:

```json
{
  "preserve": [
    "str", "int", "list", "dict", "tuple",
    "Exception", "ValueError", "TypeError",
    "import", "from", "class", "def"
  ]
}
```

### 4. Install Tree-sitter Parser

```bash
pip install tree-sitter-python
```

That's it! The language will be automatically detected and loaded.

## Architecture

```
minify/
├── base.py                          # Base language adapter interface
├── minify.py                        # Main obfuscation engine
├── unminify.py                      # Reverse obfuscation utility
├── preserve_custom.json             # Global custom words (shared by all languages)
├── requirements.txt                 # Python dependencies
├── languages/
│   ├── csharp/
│   │   ├── adapter.py               # C# language adapter
│   │   └── preserve_language.json   # C# framework words
│   └── javascript/
│       ├── adapter.py               # JavaScript language adapter
│       └── preserve_language.json   # JS framework words
```

## How It Works

### 1. Language Detection
- Scans first 500 characters of code
- Checks against detection patterns from all loaded adapters
- Falls back to manual selection if ambiguous

### 2. Tree-Sitter Parsing
- Uses language-specific tree-sitter parsers
- Builds Abstract Syntax Tree (AST)
- Identifies identifiers, strings, comments

### 3. Smart Obfuscation
- Checks full identifier against preserve list
- Splits CamelCase identifiers into parts
- Preserves framework words, obfuscates custom words
- Preserves common suffixes
- Uses deterministic MD5 hashing

### 4. Output Generation
- Minifies code (removes whitespace, comments)
- Saves obfuscation mapping
- Copies result to clipboard

## Use Cases

- **AI Protection:** Protect proprietary code from AI-based analysis, code generation, and reverse engineering
- **IP Protection:** Obfuscate proprietary algorithms while keeping framework calls readable
- **AI Resistance:** Make your code harder to understand and regenerate by AI models like GPT, Claude, etc.
- **Supply Chain Security:** Secure open-source code from being absorbed into AI training datasets
- **Demo Code:** Share code samples without revealing business logic to AI systems
- **Education:** Create exercises where students fill in obfuscated logic
- **Security Research:** Analyze obfuscation patterns and AI resistance techniques
- **Code Size Reduction:** Minify code for production while maintaining AI obfuscation

## Limitations

- **Not for Security:** This is obfuscation, not encryption. Determined reverse engineering can still recover logic.
- **Framework Dependent:** Heavily relies on tree-sitter parsers. Some edge cases may not parse correctly.
- **String Literals:** Currently obfuscates all string literals. May break hardcoded strings.
- **Reflection/Dynamic Code:** Cannot handle runtime code generation or reflection-based logic.

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Areas for Contribution

- 🌍 Add support for more languages (Python, Go, Java, Ruby, etc.)
- 📚 Expand framework word lists
- 🐛 Bug fixes and improvements
- 📖 Documentation improvements
- ✨ New features (CLI arguments, config files, etc.)

## License

This project is licensed under the BSD 3-Clause License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Tree-sitter](https://tree-sitter.github.io/tree-sitter/) for language parsing
- Inspired by the need for intelligent code obfuscation in modern software development

## Support

- **Issues:** [GitHub Issues](https://github.com/webinadvance/aishield/issues)
- **Discussions:** [GitHub Discussions](https://github.com/webinadvance/aishield/discussions)
- **GitHub Repository:** [webinadvance/aishield](https://github.com/webinadvance/aishield)

---

**Made with ❤️ for developers who value code protection against AI and readability.**

---

**⚠️ Note:** AIShield is a defensive tool designed to protect code from AI-based analysis. It's suitable for protecting proprietary code and IP. Use responsibly and in compliance with all applicable laws and regulations.
