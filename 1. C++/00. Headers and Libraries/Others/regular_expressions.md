# Regular Expressions - Pattern Matching with `<regex>`

The `<regex>` header (C++11) provides a full regular expression engine with support for matching, searching, iterating over all matches, and replacing substrings.

## 📖 Overview

Regular expressions describe patterns in text. C++ implements the ECMAScript (default), POSIX Basic, POSIX Extended, awk, grep, and egrep syntax variants through `std::regex`.

Three core operations:
- **`regex_match`** — does the entire string match the pattern?
- **`regex_search`** — does a pattern appear anywhere in the string?
- **`regex_replace`** — replace occurrences of a pattern with a replacement string

## 🎯 Key Components

### Classes
| Class | Description |
|-------|-------------|
| `std::regex` | Compiled regular expression |
| `std::smatch` | Match results for `std::string` |
| `std::cmatch` | Match results for C-strings |
| `std::ssub_match` | One captured sub-group from a string match |
| `std::sregex_iterator` | Iterate over all non-overlapping matches |
| `std::sregex_token_iterator` | Iterate over tokens (splits) |

### Syntax Flags
| Flag | Grammar |
|------|---------|
| `std::regex::ECMAScript` | JavaScript-style (default) |
| `std::regex::icase` | Case-insensitive matching |
| `std::regex::multiline` | `^`/`$` match start/end of each line |
| `std::regex::nosubs` | Disable capture groups |

### Common ECMAScript Pattern Elements
| Pattern | Meaning |
|---------|---------|
| `.` | Any character (except newline) |
| `\d` | Digit `[0-9]` |
| `\w` | Word character `[a-zA-Z0-9_]` |
| `\s` | Whitespace |
| `^` / `$` | Start / end of string (or line with multiline) |
| `[abc]` | Character class |
| `(...)` | Capture group |
| `(?:...)` | Non-capturing group |
| `*`, `+`, `?` | Quantifiers: 0+, 1+, 0 or 1 |
| `{n,m}` | Repeat n to m times |
| `\|` | Alternation (or) |

## 🔧 Basic Operations

### `regex_match` — Full String Match
```cpp
#include <iostream>
#include <regex>
#include <string>

int main() {
    std::regex intPattern(R"(\d+)");           // one or more digits
    std::regex emailPattern(R"(\w+@\w+\.\w+)"); // simple email
    std::regex ipPattern(R"((\d{1,3}\.){3}\d{1,3})"); // IPv4

    std::cout << std::boolalpha;
    std::cout << "\"123\" is int:   " << std::regex_match("123",   intPattern)   << "\n"; // true
    std::cout << "\"12a\" is int:   " << std::regex_match("12a",   intPattern)   << "\n"; // false
    std::cout << "email match:    "   << std::regex_match("a@b.c", emailPattern) << "\n"; // true
    std::cout << "IP match:       "   << std::regex_match("192.168.1.1", ipPattern) << "\n"; // true

    return 0;
}
```

### `regex_search` — Find Pattern Anywhere
```cpp
#include <iostream>
#include <regex>
#include <string>

int main() {
    std::string text = "Order #42 was placed on 2024-03-15 for $99.99";

    std::smatch match;

    // Find order number
    if (std::regex_search(text, match, std::regex(R"(#(\d+))"))) {
        std::cout << "Full match: " << match[0] << "\n"; // #42
        std::cout << "Group 1:   " << match[1] << "\n"; // 42
    }

    // Find date
    if (std::regex_search(text, match, std::regex(R"(\d{4}-\d{2}-\d{2})"))) {
        std::cout << "Date: " << match[0] << "\n"; // 2024-03-15
    }

    // Find price
    if (std::regex_search(text, match, std::regex(R"(\$(\d+\.\d{2}))"))) {
        std::cout << "Price: " << match[1] << "\n"; // 99.99
    }

    return 0;
}
```

### `regex_replace` — Substitution
```cpp
#include <iostream>
#include <regex>
#include <string>

int main() {
    std::string text = "Hello World, hello C++, HELLO regex!";

    // Case-insensitive replace
    std::regex helloRe("hello", std::regex::icase);
    std::string result = std::regex_replace(text, helloRe, "Hi");
    std::cout << result << "\n"; // Hi World, Hi C++, Hi regex!

    // Reformat date: YYYY-MM-DD → DD/MM/YYYY
    std::string date = "Date: 2024-03-15";
    std::regex dateRe(R"((\d{4})-(\d{2})-(\d{2}))");
    std::string reformatted = std::regex_replace(date, dateRe, "$3/$2/$1");
    std::cout << reformatted << "\n"; // Date: 15/03/2024

    // Remove all digits
    std::string mixed = "a1b2c3d4e5";
    std::string lettersOnly = std::regex_replace(mixed, std::regex(R"(\d)"), "");
    std::cout << lettersOnly << "\n"; // abcde

    return 0;
}
```

### `sregex_iterator` — All Matches
```cpp
#include <iostream>
#include <regex>
#include <string>

int main() {
    std::string log = "ERROR 404 at 10:30, WARNING 200 at 11:00, ERROR 500 at 12:15";

    std::regex errorRe(R"(ERROR (\d+) at (\d{2}:\d{2}))");

    auto begin = std::sregex_iterator(log.begin(), log.end(), errorRe);
    auto end   = std::sregex_iterator();

    std::cout << "Errors found:\n";
    for (auto it = begin; it != end; ++it) {
        const std::smatch& m = *it;
        std::cout << "  Code " << m[1] << " at " << m[2] << "\n";
    }

    return 0;
}
```

## 🎮 Practical Examples

### Example 1: Form Input Validator
```cpp
#include <iostream>
#include <regex>
#include <string>
#include <map>
#include <functional>

bool validate(const std::string& value, const std::string& pattern) {
    return std::regex_match(value, std::regex(pattern));
}

int main() {
    std::map<std::string, std::string> rules = {
        {"username",    R"([a-zA-Z][a-zA-Z0-9_]{2,15})"},
        {"email",       R"([a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,})"},
        {"phone",       R"(\+?\d[\d\-\s]{8,14}\d)"},
        {"zip_code",    R"(\d{5}(-\d{4})?)"},
        {"hex_color",   R"(#([0-9a-fA-F]{3}|[0-9a-fA-F]{6}))"}
    };

    std::map<std::string, std::string> inputs = {
        {"username",  "john_doe"},
        {"email",     "user@example.com"},
        {"phone",     "+1-800-555-0100"},
        {"zip_code",  "90210"},
        {"hex_color", "#1A2B3C"}
    };

    std::cout << std::boolalpha;
    for (const auto& [field, value] : inputs) {
        bool ok = validate(value, rules[field]);
        std::cout << field << " (\"" << value << "\"): " << ok << "\n";
    }

    return 0;
}
```

### Example 2: Log File Parser
```cpp
#include <iostream>
#include <regex>
#include <string>
#include <vector>
#include <sstream>

struct LogEntry {
    std::string timestamp;
    std::string level;
    std::string message;
};

std::vector<LogEntry> parseLogs(const std::string& log) {
    // Format: [2024-03-15 10:30:00] [ERROR] Something failed
    std::regex lineRe(R"(\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] \[(\w+)\] (.+))");

    std::vector<LogEntry> entries;
    std::istringstream stream(log);
    std::string line;

    while (std::getline(stream, line)) {
        std::smatch m;
        if (std::regex_match(line, m, lineRe)) {
            entries.push_back({m[1], m[2], m[3]});
        }
    }

    return entries;
}

int main() {
    std::string logs =
        "[2024-03-15 10:30:00] [INFO] Server started\n"
        "[2024-03-15 10:31:05] [ERROR] Database connection failed\n"
        "[2024-03-15 10:31:06] [WARN] Retrying connection\n"
        "[2024-03-15 10:31:10] [INFO] Connection restored\n";

    auto entries = parseLogs(logs);
    for (const auto& e : entries) {
        std::cout << "[" << e.level << "] " << e.timestamp << " — " << e.message << "\n";
    }

    return 0;
}
```

### Example 3: Tokeniser / Splitter
```cpp
#include <iostream>
#include <regex>
#include <string>
#include <vector>

// Split by any delimiter (regex-based, handles multiple delimiters)
std::vector<std::string> splitTokens(const std::string& text, const std::string& delim) {
    std::regex re(delim);
    std::sregex_token_iterator begin(text.begin(), text.end(), re, -1);
    std::sregex_token_iterator end;
    return {begin, end};
}

int main() {
    // Split by comma + optional space
    auto words = splitTokens("apple, banana,cherry , date", R"(\s*,\s*)");
    for (const auto& w : words) std::cout << '"' << w << '"' << " ";
    std::cout << "\n";

    // Split by one or more whitespace
    auto parts = splitTokens("hello   world\ttab\nnewline", R"(\s+)");
    for (const auto& p : parts) std::cout << '"' << p << '"' << " ";
    std::cout << "\n";

    // Extract all numbers from text
    std::string text = "I have 3 cats and 12 dogs and 0 fish";
    std::regex numRe(R"(\d+)");
    auto it = std::sregex_iterator(text.begin(), text.end(), numRe);
    std::cout << "Numbers: ";
    for (; it != std::sregex_iterator(); ++it)
        std::cout << (*it)[0] << " ";
    std::cout << "\n";

    return 0;
}
```

### Example 4: URL Parser
```cpp
#include <iostream>
#include <regex>
#include <string>

struct URL {
    std::string scheme, host, port, path, query, fragment;
};

URL parseURL(const std::string& url) {
    // scheme://host:port/path?query#fragment
    std::regex urlRe(
        R"(^(https?|ftp)://([^/:?#]+)(?::(\d+))?([^?#]*)(?:\?([^#]*))?(?:#(.*))?$)"
    );

    std::smatch m;
    URL result;
    if (std::regex_match(url, m, urlRe)) {
        result.scheme   = m[1];
        result.host     = m[2];
        result.port     = m[3];
        result.path     = m[4];
        result.query    = m[5];
        result.fragment = m[6];
    }
    return result;
}

int main() {
    std::string url = "https://api.example.com:8080/v1/users?page=2&limit=10#results";
    URL u = parseURL(url);

    std::cout << "Scheme:   " << u.scheme   << "\n";
    std::cout << "Host:     " << u.host     << "\n";
    std::cout << "Port:     " << (u.port.empty() ? "(default)" : u.port) << "\n";
    std::cout << "Path:     " << u.path     << "\n";
    std::cout << "Query:    " << u.query    << "\n";
    std::cout << "Fragment: " << u.fragment << "\n";

    return 0;
}
```

## ⚡ Performance Tips

### Compile Regex Once, Use Many Times
```cpp
// BAD: compiles the regex on every loop iteration
for (const auto& line : lines) {
    if (std::regex_search(line, std::regex(R"(\d+)"))) { /* ... */ }
}

// GOOD: compile once outside the loop
std::regex numRe(R"(\d+)");
for (const auto& line : lines) {
    if (std::regex_search(line, numRe)) { /* ... */ }
}
```

### Use `regex_search` Instead of `regex_match` for Substrings
```cpp
// regex_match requires whole string to match — slow for partial finding
// regex_search finds the first occurrence — much faster for partial match
std::regex_search(text, match, pattern); // preferred for partial match
```

### Use Raw String Literals for Patterns
```cpp
// Without raw literals: double-escape everything
std::regex re("\\d{3}-\\d{4}"); // messy

// With raw literals: write patterns naturally
std::regex re(R"(\d{3}-\d{4})"); // clean
```

## 🐛 Common Pitfalls & Solutions

### 1. `regex_match` vs `regex_search` Confusion
```cpp
std::string text = "phone: 555-1234";
std::regex re(R"(\d{3}-\d{4})");

// WRONG: regex_match checks the ENTIRE string
bool a = std::regex_match(text, re); // false — "phone: " is not matched

// RIGHT: regex_search finds the pattern anywhere
bool b = std::regex_search(text, re); // true
```

### 2. Forgetting to Double-Escape Backslashes (Without Raw Literals)
```cpp
// BUG: single backslash is an escape sequence in string literal
std::regex re("\d+"); // compile error or wrong pattern

// FIX option 1: double escape
std::regex re("\\d+");

// FIX option 2: raw string literal (preferred)
std::regex re(R"(\d+)");
```

### 3. Invalid Regex Throws `std::regex_error`
```cpp
try {
    std::regex bad("[invalid"); // unclosed bracket
} catch (const std::regex_error& e) {
    std::cerr << "Regex error: " << e.what() << "\n";
}
```

### 4. C++ `<regex>` Can Be Slow for Complex Patterns
```cpp
// For very large texts or performance-critical code:
// Consider using PCRE2, RE2, or hyperscan libraries instead of <regex>
// std::regex can be 10–100x slower than dedicated regex libraries
```

## 🎯 Best Practices

1. **Use raw string literals** (`R"(...)"`) to write clean, readable patterns
2. **Compile regex once** outside loops — `std::regex` construction is expensive
3. **Wrap regex in try/catch** for `std::regex_error` when the pattern comes from user input
4. **Prefer `regex_search`** when you want to find a pattern inside a larger string
5. **Use capture groups `(...)` deliberately** — name what you extract
6. **For performance-critical code** with complex patterns, evaluate PCRE2 or RE2

## 📚 Related Topics

- [`string.md`](../Fundamentals/03_string.md) — `find()`, `replace()`, `substr()` for simple string ops without regex
- [`sstream.md`](../Fundamentals/29_sstream.md) — Tokenising with `getline` for simple delimiters
- [`algorithm.md`](../Fundamentals/04_algorithm.md) — `find_if` for character-level searches

## 🚀 Next Steps

1. Parse a CSV file with regex to handle quoted fields containing commas
2. Write an email/URL sanitiser using `regex_replace`
3. Build a simple lexer / tokeniser using `sregex_token_iterator`
4. Benchmark `<regex>` vs manual `string::find` for your specific use case
---

## Next Step

- Go to [smart_pointers.md](smart_pointers.md) to continue with smart pointers.
