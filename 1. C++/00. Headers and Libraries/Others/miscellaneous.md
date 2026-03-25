# Miscellaneous - Practical C++ Utilities and Modern Features

A collection of essential modern C++ features and small utilities that don't belong to a single header but appear constantly in real-world code.

## 📖 Overview

Modern C++ (C++11 through C++23) added many quality-of-life features that improve code safety, readability, and performance without requiring external libraries. This guide covers the most practically useful ones:

- Type-safe enumerations (`enum class`)
- Structured bindings (`auto [k, v]`)
- `auto` and `decltype`
- `std::optional<T>` — nullable values without pointers
- `std::variant<...>` — type-safe union
- `std::any` — type-erased container
- Bit manipulation utilities
- Assertions and contracts
- `std::byte`, `std::span`, and other C++17/20 utilities

## 🎯 Key Features Quick Reference

| Feature | Since | Purpose |
|---------|-------|---------|
| `enum class` | C++11 | Scoped, strongly-typed enums |
| `auto` | C++11 | Type deduction for variables |
| `decltype` | C++11 | Query type of an expression |
| Structured bindings | C++17 | `auto [a, b] = pair;` |
| `if constexpr` | C++17 | Compile-time branch selection |
| `std::optional<T>` | C++17 | Represent "value or nothing" |
| `std::variant<T...>` | C++17 | Type-safe tagged union |
| `std::any` | C++17 | Type-erased value container |
| `std::string_view` | C++17 | Non-owning string reference |
| `std::span<T>` | C++20 | Non-owning view of a contiguous range |

## 🔧 Basic Operations

### `enum class` — Scoped Enumerations
```cpp
#include <iostream>
#include <string>

// Old-style enum: values leak into enclosing scope, implicit int conversion
// enum Color { Red, Green, Blue }; // Red, Green, Blue pollute the namespace

// enum class: fully scoped, no implicit conversion
enum class Color  : uint8_t { Red, Green, Blue, Yellow };
enum class Status : int     { OK = 200, NotFound = 404, Error = 500 };

std::string colorName(Color c) {
    switch (c) {
        case Color::Red:    return "Red";
        case Color::Green:  return "Green";
        case Color::Blue:   return "Blue";
        case Color::Yellow: return "Yellow";
    }
    return "Unknown";
}

int main() {
    Color c = Color::Red;
    std::cout << colorName(c) << "\n"; // Red

    Status s = Status::NotFound;
    std::cout << static_cast<int>(s) << "\n"; // 404 (explicit cast required)

    // c == 0; // compile error — cannot compare enum class to int
    std::cout << std::boolalpha << (c == Color::Red) << "\n"; // true

    return 0;
}
```

### `auto` and `decltype` — Type Deduction
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <string>

int compute(double x) { return static_cast<int>(x * 2); }

int main() {
    // auto: deduced from initialiser
    auto x     = 42;          // int
    auto y     = 3.14;        // double
    auto s     = std::string("hello"); // std::string
    auto v     = std::vector<int>{1, 2, 3};

    // auto in range-for loop
    for (const auto& element : v)
        std::cout << element << " ";
    std::cout << "\n";

    // auto for complex iterator types
    std::map<std::string, int> scores{{"Alice", 95}, {"Bob", 87}};
    for (const auto& [name, score] : scores)   // structured binding
        std::cout << name << ": " << score << "\n";

    // decltype: query type of expression (no evaluation)
    decltype(compute(0.0)) result = compute(2.5); // int
    std::cout << "Result: " << result << "\n";   // 5

    // decltype(auto): preserve exact type (including ref/const)
    auto& ref = x;
    decltype(auto) also_ref = x; // int& — preserves reference

    return 0;
}
```

### Structured Bindings (C++17)
```cpp
#include <iostream>
#include <map>
#include <tuple>
#include <string>
#include <utility>

struct Point { double x, y, z; };

int main() {
    // Decompose pair
    std::pair<std::string, int> person{"Alice", 30};
    auto [name, age] = person;
    std::cout << name << " is " << age << "\n";

    // Decompose tuple
    auto t = std::make_tuple(1, 3.14, std::string("hello"));
    auto [i, d, str] = t;
    std::cout << i << ", " << d << ", " << str << "\n";

    // Decompose struct (aggregate)
    Point p{1.0, 2.0, 3.0};
    auto [px, py, pz] = p;
    std::cout << "Point: " << px << ", " << py << ", " << pz << "\n";

    // Structured binding in range-for
    std::map<std::string, int> scores{{"Math", 95}, {"Science", 88}};
    for (const auto& [subject, score] : scores)
        std::cout << subject << ": " << score << "\n";

    // Useful with insert result
    auto [it, inserted] = scores.insert({"History", 76});
    std::cout << "Inserted: " << std::boolalpha << inserted << "\n";

    return 0;
}
```

### `if constexpr` — Compile-Time Branching
```cpp
#include <iostream>
#include <string>
#include <type_traits>

// Without if constexpr: need separate specialisations
// With if constexpr: single function body, dead branches discarded at compile time
template <typename T>
std::string describe(const T& value) {
    if constexpr (std::is_integral_v<T>) {
        return "integer(" + std::to_string(value) + ")";
    } else if constexpr (std::is_floating_point_v<T>) {
        return "float(" + std::to_string(value) + ")";
    } else if constexpr (std::is_same_v<T, std::string>) {
        return "string(\"" + value + "\")";
    } else {
        return "unknown";
    }
}

int main() {
    std::cout << describe(42)            << "\n"; // integer(42)
    std::cout << describe(3.14)          << "\n"; // float(3.140000)
    std::cout << describe(std::string("hi")) << "\n"; // string("hi")
    return 0;
}
```

## 🎮 Practical Examples

### Example 1: `std::optional` — Values Without Nulls
```cpp
#include <iostream>
#include <optional>
#include <string>
#include <map>

// Return optional instead of sentinel values or output parameters
std::optional<int> findScore(const std::map<std::string, int>& db,
                              const std::string& name) {
    auto it = db.find(name);
    if (it == db.end()) return std::nullopt; // explicit "no value"
    return it->second;
}

std::optional<double> safeDivide(double a, double b) {
    if (b == 0.0) return std::nullopt;
    return a / b;
}

int main() {
    std::map<std::string, int> scores{{"Alice", 95}, {"Bob", 87}};

    // Check and use with value_or
    auto alice = findScore(scores, "Alice");
    auto carol = findScore(scores, "Carol");

    std::cout << "Alice: " << alice.value_or(-1) << "\n"; // 95
    std::cout << "Carol: " << carol.value_or(-1) << "\n"; // -1

    // Explicit check
    if (alice) {
        std::cout << "Alice's score: " << *alice << "\n";
    }

    // Safe division
    auto result = safeDivide(10.0, 3.0);
    if (result) std::cout << "10 / 3 = " << *result << "\n";

    auto bad = safeDivide(10.0, 0.0);
    std::cout << "Divide by zero: " << (bad ? "got value" : "nullopt") << "\n";

    return 0;
}
```

### Example 2: `std::variant` — Type-Safe Union
```cpp
#include <iostream>
#include <variant>
#include <string>
#include <vector>

// Represent a JSON-like value
using JsonValue = std::variant<std::nullptr_t, bool, int, double, std::string>;

std::string stringify(const JsonValue& val) {
    return std::visit([](const auto& v) -> std::string {
        using T = std::decay_t<decltype(v)>;
        if constexpr (std::is_same_v<T, std::nullptr_t>) return "null";
        else if constexpr (std::is_same_v<T, bool>)    return v ? "true" : "false";
        else if constexpr (std::is_same_v<T, int>)     return std::to_string(v);
        else if constexpr (std::is_same_v<T, double>)  return std::to_string(v);
        else if constexpr (std::is_same_v<T, std::string>) return '"' + v + '"';
        return "?";
    }, val);
}

int main() {
    std::vector<JsonValue> values = {nullptr, true, 42, 3.14, std::string("hello")};

    for (const auto& v : values)
        std::cout << stringify(v) << "\n";

    // Type-safe access
    JsonValue score = 95;
    if (std::holds_alternative<int>(score)) {
        std::cout << "Score: " << std::get<int>(score) << "\n";
    }

    // std::get_if — non-throwing access
    if (auto* str = std::get_if<std::string>(&score)) {
        std::cout << "String: " << *str << "\n";
    } else {
        std::cout << "Not a string\n";
    }

    return 0;
}
```

### Example 3: Bit Manipulation Utilities
```cpp
#include <iostream>
#include <bitset>
#include <bit>          // C++20: std::popcount, std::countl_zero, std::has_single_bit
#include <cstdint>

int main() {
    uint32_t flags = 0b1010'0101;

    // Test, set, clear, toggle individual bits
    auto testBit  = [](uint32_t v, int b) { return (v >> b) & 1; };
    auto setBit   = [](uint32_t v, int b) { return v |  (1u << b); };
    auto clearBit = [](uint32_t v, int b) { return v & ~(1u << b); };
    auto flipBit  = [](uint32_t v, int b) { return v ^  (1u << b); };

    std::cout << "Original: " << std::bitset<8>(flags) << "\n"; // 10100101
    std::cout << "Bit 0: " << testBit(flags, 0) << "\n";        // 1
    flags = setBit(flags, 1);
    std::cout << "Set bit 1: " << std::bitset<8>(flags) << "\n"; // 10100111
    flags = clearBit(flags, 7);
    std::cout << "Clear bit 7: " << std::bitset<8>(flags) << "\n"; // 00100111

    // C++20 bit utilities
    uint32_t n = 0b0101'1100;
    std::cout << "popcount: "       << std::popcount(n)       << "\n"; // 4
    std::cout << "has_single_bit: " << std::has_single_bit(8u)<< "\n"; // 1

    // Bitmask flags pattern (enum class + bitwise ops)
    enum class Permission : uint8_t {
        None    = 0,
        Read    = 1 << 0,
        Write   = 1 << 1,
        Execute = 1 << 2
    };

    auto perms = static_cast<uint8_t>(Permission::Read) |
                 static_cast<uint8_t>(Permission::Write);
    std::cout << "Read+Write: " << std::bitset<3>(perms) << "\n"; // 011

    return 0;
}
```

### Example 4: `std::string_view` and `std::span` — Non-Owning Views
```cpp
#include <iostream>
#include <string>
#include <string_view>
#include <vector>
#include <span>         // C++20
#include <numeric>

// string_view: reference to string data — no copy, no allocation
void printPrefix(std::string_view sv, size_t n) {
    std::cout << sv.substr(0, n) << "\n"; // no allocation
}

bool startsWith(std::string_view str, std::string_view prefix) {
    return str.size() >= prefix.size() &&
           str.substr(0, prefix.size()) == prefix;
}

// span: non-owning view of a contiguous container (array, vector, etc.)
double average(std::span<const int> data) {
    if (data.empty()) return 0.0;
    return static_cast<double>(
        std::accumulate(data.begin(), data.end(), 0)
    ) / data.size();
}

void doubleAll(std::span<int> data) {
    for (auto& x : data) x *= 2;
}

int main() {
    // string_view — works with string literals, std::string, slices — no copy
    std::string  s   = "Hello, World!";
    std::string_view sv1 = s;
    std::string_view sv2 = "Hello, World!"; // no allocation
    std::string_view sv3 = sv1.substr(7, 5); // "World" — still no allocation

    printPrefix(sv1, 5);               // Hello
    std::cout << startsWith(sv1, "Hello") << "\n"; // 1

    // span — works with arrays, vectors, parts of vectors
    std::vector<int> v = {1, 2, 3, 4, 5, 6, 7, 8};
    std::cout << "Average: " << average(v)             << "\n"; // 4.5
    std::cout << "First half avg: " << average(std::span(v).first(4)) << "\n"; // 2.5

    doubleAll(v);
    for (int n : v) std::cout << n << " ";
    std::cout << "\n"; // 2 4 6 8 10 12 14 16

    return 0;
}
```

## ⚡ Performance Tips

### Prefer `string_view` Over `const string&` for Read-Only Parameters
```cpp
// const string& forces the caller to have a std::string
void bad(const std::string& s);  // "hello" creates a temporary string!

// string_view works with string literals, string, string slices — zero copy
void good(std::string_view sv);  // "hello" passes directly — no allocation
```

### Use `optional` Instead of `bool` + Output Parameters
```cpp
// Old pattern: out parameter + bool return
bool findValue(const Map& m, const Key& k, Value& out);

// Modern: return optional — cleaner, safer, just as fast
std::optional<Value> findValue(const Map& m, const Key& k);
```

### `enum class` With Explicit Underlying Type Saves Space
```cpp
// Default underlying type is int (4 bytes)
enum class Status { OK, Error, Pending }; // 4 bytes

// Specify uint8_t when values fit
enum class Status : uint8_t { OK, Error, Pending }; // 1 byte
// Useful in packed structs and arrays
```

## 🐛 Common Pitfalls & Solutions

### 1. `string_view` Dangling — Outliving the Source String
```cpp
std::string_view bad() {
    std::string local = "hello";
    return local; // DANGLING — local is destroyed on return!
}

// Fix: return std::string; use string_view only within the lifetime of the source
std::string good() { return "hello"; }
```

### 2. `std::optional::value()` Throws; `*opt` Is UB When Empty
```cpp
std::optional<int> opt;

// Throws std::bad_optional_access:
// int v = opt.value();

// Undefined behaviour:
// int v = *opt;

// Safe:
int v = opt.value_or(0); // returns 0 if empty
if (opt) int v2 = *opt;  // check first
```

### 3. `std::variant` — `std::get<T>` Throws if Wrong Type
```cpp
std::variant<int, std::string> v = 42;
// std::get<std::string>(v); // throws std::bad_variant_access!

// Safe alternatives:
if (std::holds_alternative<std::string>(v)) { /* ... */ }
if (auto* p = std::get_if<std::string>(&v)) { std::cout << *p; }
```

### 4. `auto` Doesn't Always Deduce What You Expect
```cpp
std::vector<bool> vb = {true, false};
auto elem = vb[0]; // NOT bool — it's vector<bool>::reference (proxy type)!

// Fix: be explicit
bool elem2 = vb[0];
```

## 🎯 Best Practices

1. **Use `enum class` always** — scoped enums are strictly safer than plain enums
2. **Use `std::optional<T>`** for functions that may return "no value" — avoid sentinel values like `-1` or `nullptr`
3. **Use `std::string_view`** for read-only string parameters — faster than `const string&` for literals
4. **Use `std::span<T>`** for functions that process contiguous data — works with `vector`, arrays, raw buffers
5. **Use structured bindings** (`auto [k, v]`) when decomposing pairs, tuples, or structs for clarity
6. **Use `if constexpr`** instead of template specialisation for simple type-dependent branching

## 📚 Related Topics

- [`type_traits.md`](../Fundamentals/33_type_traits.md) — `is_integral_v`, `is_same_v`, `enable_if` — used with `if constexpr`
- [`templates.md`](templates.md) — `if constexpr` and structured bindings in template contexts
- [`lambda_expressions.md`](lambda_expressions.md) — Lambdas with `auto` parameters and `[=, this]` captures
- [`move_semantics.md`](move_semantics.md) — `decltype(auto)` and perfect forwarding

## 🚀 Next Steps

1. Replace all sentinel-returning functions (`-1`, `nullptr`) with `std::optional<T>`
2. Convert all plain `enum` to `enum class` in an existing codebase
3. Use `std::variant` to implement a simple expression tree (int, +, *, variables)
4. Explore C++20 `std::format` for type-safe, Python-style string formatting

---

**Examples in this file**: 4 complete programs  
**Key Features**: `enum class`, `auto`/`decltype`, structured bindings, `if constexpr`, `optional`, `variant`, `string_view`, `span`, bit ops  
**Standards Coverage**: C++11, C++14, C++17, C++20  
**Common Use Cases**: Type-safe APIs, nullable returns, compile-time dispatch, non-owning views, bitmask flags
