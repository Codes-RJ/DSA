# 29_sstream - String Stream Library

The `sstream` header lets you treat a `std::string` as a stream, so you can use familiar `>>` and `<<` operators to parse or build strings without dealing with raw character arrays.

## 📖 Overview

`<sstream>` provides three stream classes backed by an internal string buffer:

- **`istringstream`** — Read data *out of* a string (parsing)
- **`ostringstream`** — Write data *into* a string (building)
- **`stringstream`** — Both read and write (bidirectional)

Because they share the same interface as `cin` and `cout`, any code that works with streams can be switched to use string streams with minimal changes.

## 🎯 Key Components

### Classes
- `std::istringstream` — Input string stream
- `std::ostringstream` — Output string stream
- `std::stringstream` — Bidirectional string stream

### Key Methods
- `str()` — get or set the underlying string
- `str("")` — clear/reset the stream
- `clear()` — reset error/eof flags
- `<<` / `>>` — standard stream insertion/extraction
- `good()`, `fail()`, `eof()` — stream state checks

## 🔧 Basic Operations

### Building a String with `ostringstream`
```cpp
#include <sstream>
#include <iostream>
#include <string>

int main() {
    std::ostringstream oss;

    oss << "Name: " << "Alice" << ", Age: " << 30;
    oss << ", GPA: " << 3.85;

    std::string result = oss.str();
    std::cout << result << "\n";
    // Output: Name: Alice, Age: 30, GPA: 3.85

    return 0;
}
```

### Parsing a String with `istringstream`
```cpp
#include <sstream>
#include <iostream>
#include <string>

int main() {
    std::string data = "John 25 89.5";
    std::istringstream iss(data);

    std::string name;
    int age;
    double score;

    iss >> name >> age >> score;
    std::cout << "Name:  " << name  << "\n";
    std::cout << "Age:   " << age   << "\n";
    std::cout << "Score: " << score << "\n";

    return 0;
}
```

### Bidirectional with `stringstream`
```cpp
#include <sstream>
#include <iostream>

int main() {
    std::stringstream ss;
    ss << 10 << ' ' << 20 << ' ' << 30;

    int a, b, c;
    ss >> a >> b >> c;

    std::cout << "Sum: " << a + b + c << "\n"; // 60

    return 0;
}
```

### Resetting a `stringstream`
```cpp
#include <sstream>
#include <iostream>

int main() {
    std::stringstream ss;

    ss << "first use";
    std::cout << ss.str() << "\n";

    // Reset completely for reuse
    ss.str("");   // clear content
    ss.clear();   // clear error flags

    ss << "second use";
    std::cout << ss.str() << "\n";

    return 0;
}
```

## 🎮 Practical Examples

### Example 1: Tokenizing a CSV Line
```cpp
#include <sstream>
#include <iostream>
#include <string>
#include <vector>

std::vector<std::string> splitCSV(const std::string& line) {
    std::vector<std::string> tokens;
    std::istringstream iss(line);
    std::string token;

    while (std::getline(iss, token, ',')) {
        tokens.push_back(token);
    }
    return tokens;
}

int main() {
    std::string row = "Alice,30,Engineer,New York";
    auto fields = splitCSV(row);

    for (size_t i = 0; i < fields.size(); i++) {
        std::cout << "Field " << i << ": " << fields[i] << "\n";
    }

    return 0;
}
```

### Example 2: Number-to-String Formatting
```cpp
#include <sstream>
#include <iomanip>
#include <iostream>
#include <string>

std::string formatPrice(double price) {
    std::ostringstream oss;
    oss << "$" << std::fixed << std::setprecision(2) << price;
    return oss.str();
}

std::string padLeft(int num, int width) {
    std::ostringstream oss;
    oss << std::setw(width) << std::setfill('0') << num;
    return oss.str();
}

int main() {
    std::cout << formatPrice(9.5)    << "\n"; // $9.50
    std::cout << formatPrice(1234.1) << "\n"; // $1234.10
    std::cout << padLeft(42, 5)      << "\n"; // 00042

    return 0;
}
```

### Example 3: Type-Safe String Conversion
```cpp
#include <sstream>
#include <iostream>
#include <string>

// Convert any type to string
template <typename T>
std::string toString(const T& value) {
    std::ostringstream oss;
    oss << value;
    return oss.str();
}

// Convert string to type
template <typename T>
bool fromString(const std::string& s, T& out) {
    std::istringstream iss(s);
    return static_cast<bool>(iss >> out);
}

int main() {
    std::string s = toString(3.14159);
    std::cout << "String: " << s << "\n";

    double d;
    if (fromString(s, d)) {
        std::cout << "Double: " << d << "\n";
    }

    int n;
    if (!fromString("abc", n)) {
        std::cout << "Conversion failed (expected)\n";
    }

    return 0;
}
```

### Example 4: Building SQL-Like Query Strings
```cpp
#include <sstream>
#include <iostream>
#include <string>
#include <vector>

std::string buildQuery(const std::string& table,
                       const std::vector<std::string>& columns,
                       const std::string& condition) {
    std::ostringstream oss;
    oss << "SELECT ";

    for (size_t i = 0; i < columns.size(); i++) {
        if (i > 0) oss << ", ";
        oss << columns[i];
    }

    oss << " FROM " << table;

    if (!condition.empty())
        oss << " WHERE " << condition;

    oss << ";";
    return oss.str();
}

int main() {
    auto q = buildQuery("students", {"name", "score", "grade"}, "score > 80");
    std::cout << q << "\n";
    // SELECT name, score, grade FROM students WHERE score > 80;

    return 0;
}
```

## ⚡ Performance Tips

### Prefer `ostringstream` Over Many `+` Concatenations
```cpp
// Slow: each + creates a temporary string
std::string result;
for (int i = 0; i < 10000; i++) {
    result = result + std::to_string(i) + ","; // O(n^2) copies
}

// Fast: single buffer, append all at once
std::ostringstream oss;
for (int i = 0; i < 10000; i++) {
    oss << i << ",";
}
std::string result = oss.str(); // one extraction
```

### Reuse Streams to Avoid Reallocation
```cpp
std::ostringstream oss;
for (const auto& item : bigList) {
    oss.str("");
    oss.clear();
    oss << item;
    process(oss.str());
}
```

## 🐛 Common Pitfalls & Solutions

### 1. Forgetting to Reset Both `str()` AND `clear()`
```cpp
// Problem: clear() doesn't reset the content; str("") doesn't reset flags
std::stringstream ss;
ss << "hello";
ss >> some_var; // stream hits eof

ss.str("");   // clears content but eofbit stays set
ss >> more;   // still fails!

// Solution: always do both
ss.str("");
ss.clear();
ss >> more; // now works
```

### 2. Reading Until EOF, Then Trying Again
```cpp
std::istringstream iss("10 20");
int a, b, c;
iss >> a >> b; // fine
iss >> c;      // fails silently — eof already reached

// Solution: check the stream state
if (!(iss >> c)) {
    std::cerr << "No more tokens\n";
}
```

### 3. Locale-Dependent Number Formatting
```cpp
// std::ostringstream respects the current locale
// In some locales '.' becomes ',' for decimals
std::ostringstream oss;
oss << 3.14; // might output "3,14" in some locales

// Fix: imbue with classic locale
oss.imbue(std::locale::classic());
oss << 3.14; // always "3.14"
```

## 🎯 Best Practices

1. **Use `istringstream` for parsing** strings — it's cleaner than `sscanf`
2. **Use `ostringstream` for building** formatted strings
3. **Always `str("")` then `clear()`** when reusing a stream
4. **Use `ostringstream` instead of repeated `+`** for large string building
5. **Check stream state (`>>` result)** when parsing untrusted input

## 📚 Related Headers

- [`iostream.md`](01_iostream.md) — Same stream model for stdin/stdout
- [`fstream.md`](28_fstream.md) — File-backed streams using the same interface
- [`iomanip.md`](30_iomanip.md) — Formatting manipulators (work inside `ostringstream`)
- [`string.md`](03_string.md) — Underlying string type

## 🚀 Next Steps

1. Use `istringstream` to write a robust CSV parser
2. Build a logging class that uses `ostringstream` internally
3. Write a template `toString`/`fromString` utility and test it on custom types
4. Explore `std::format` (C++20) as a modern alternative for formatting

---

**Examples in this file**: 4 complete programs  
**Key Classes**: `istringstream`, `ostringstream`, `stringstream`  
**Key Methods**: `str()`, `clear()`, `<<`, `>>`  
**Common Use Cases**: Parsing, string building, type conversion, tokenization
