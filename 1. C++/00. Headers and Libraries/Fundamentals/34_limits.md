# limits - Numeric Limits

The `limits` header provides a uniform, type-safe way to query the minimum, maximum, and special properties of every arithmetic type, replacing the macro-based approach of C's `<climits>` and `<cfloat>`.

## 📖 Overview

`<limits>` defines the class template `std::numeric_limits<T>`, which is specialised for every built-in arithmetic type. Every member is `constexpr`, meaning you can use the values in compile-time expressions, array sizes, and `static_assert` checks.

Key design advantages over C macros (`INT_MAX`, `DBL_EPSILON`, etc.):
- **Type-safe** — parameterised by the exact type, not by a macro name
- **Template-friendly** — works generically in templated code
- **More information** — exposes many more properties than raw macros
- **`constexpr`** — all values are usable at compile time

## 🎯 Key Components

### Commonly Used Members

| Member | Description | Example (int) | Example (double) |
|--------|-------------|---------------|-----------------|
| `min()` | Smallest finite value | `-2147483648` | `~5e-324` (smallest positive) |
| `max()` | Largest finite value | `2147483647` | `~1.8e+308` |
| `lowest()` | Most negative finite value | `-2147483648` | `~-1.8e+308` |
| `epsilon()` | Difference between 1 and next value | `0` | `~2.22e-16` |
| `infinity()` | Positive infinity | `0` | `inf` |
| `quiet_NaN()` | Quiet not-a-number | `0` | `nan` |
| `digits` | Number of significant radix digits | `31` | `53` |
| `digits10` | Significant decimal digits | `9` | `15` |
| `is_integer` | True for integral types | `true` | `false` |
| `is_signed` | True for signed types | `true` | `true` |
| `is_exact` | True if representation is exact | `true` | `false` |
| `has_infinity` | True if type can represent ∞ | `false` | `true` |
| `has_quiet_NaN` | True if type has quiet NaN | `false` | `true` |
| `radix` | Base of the representation | `2` | `2` |
| `round_style` | Rounding mode | — | `round_to_nearest` |

### Important Notes on `min()`
```
- For integral types:   min() = the most negative value (e.g., INT_MIN)
- For floating-point:   min() = the smallest POSITIVE normalised value
- Use lowest() to get the most negative floating-point value
```

## 🔧 Basic Operations

### Querying Basic Limits
```cpp
#include <limits>
#include <iostream>

int main() {
    std::cout << "=== int ===\n";
    std::cout << "  min:    " << std::numeric_limits<int>::min()    << "\n";
    std::cout << "  max:    " << std::numeric_limits<int>::max()    << "\n";
    std::cout << "  digits: " << std::numeric_limits<int>::digits   << " bits\n";

    std::cout << "\n=== unsigned int ===\n";
    std::cout << "  min:    " << std::numeric_limits<unsigned int>::min() << "\n";
    std::cout << "  max:    " << std::numeric_limits<unsigned int>::max() << "\n";

    std::cout << "\n=== double ===\n";
    std::cout << "  min:    " << std::numeric_limits<double>::min()     << "\n";
    std::cout << "  max:    " << std::numeric_limits<double>::max()     << "\n";
    std::cout << "  lowest: " << std::numeric_limits<double>::lowest()  << "\n";
    std::cout << "  eps:    " << std::numeric_limits<double>::epsilon()  << "\n";

    return 0;
}
```

### `min()` vs `lowest()` for Floats
```cpp
#include <limits>
#include <iostream>

int main() {
    // min() for double = smallest positive normalised number (NOT most negative!)
    double d_min    = std::numeric_limits<double>::min();    // ~2.22e-308
    double d_lowest = std::numeric_limits<double>::lowest(); // ~-1.8e+308

    std::cout << "double min:    " << d_min    << "\n"; // tiny positive
    std::cout << "double lowest: " << d_lowest << "\n"; // large negative

    // For int, min() and lowest() are the same
    int i_min    = std::numeric_limits<int>::min();    // -2147483648
    int i_lowest = std::numeric_limits<int>::lowest(); // -2147483648

    std::cout << "int min:    " << i_min    << "\n";
    std::cout << "int lowest: " << i_lowest << "\n";

    return 0;
}
```

### Using Limits in Templates
```cpp
#include <limits>
#include <iostream>
#include <vector>

template <typename T>
T findMax(const std::vector<T>& v) {
    T result = std::numeric_limits<T>::lowest(); // works for any arithmetic type

    for (const T& val : v) {
        if (val > result) result = val;
    }

    return result;
}

int main() {
    std::vector<int>    ints   = {3, -5, 7, 1, -2};
    std::vector<double> floats = {1.1, -2.2, 3.3, 0.5};

    std::cout << "Max int:    " << findMax(ints)   << "\n"; // 7
    std::cout << "Max double: " << findMax(floats) << "\n"; // 3.3

    return 0;
}
```

## 🎮 Practical Examples

### Example 1: Overflow-Safe Addition
```cpp
#include <limits>
#include <iostream>
#include <stdexcept>

int safeAdd(int a, int b) {
    if (b > 0 && a > std::numeric_limits<int>::max() - b)
        throw std::overflow_error("Integer overflow");
    if (b < 0 && a < std::numeric_limits<int>::min() - b)
        throw std::underflow_error("Integer underflow");
    return a + b;
}

int main() {
    try {
        std::cout << safeAdd(100, 200) << "\n"; // 300

        int big = std::numeric_limits<int>::max();
        std::cout << safeAdd(big, 1);  // throws overflow_error
    } catch (const std::overflow_error& e) {
        std::cerr << "Error: " << e.what() << "\n";
    }
    return 0;
}
```

### Example 2: Floating-Point Equality with `epsilon`
```cpp
#include <limits>
#include <iostream>
#include <cmath>

bool almostEqual(double a, double b, int ulp = 4) {
    // ULP = Units in the Last Place
    double diff = std::abs(a - b);
    double scale = std::max(std::abs(a), std::abs(b));
    return diff <= std::numeric_limits<double>::epsilon() * scale * ulp;
}

int main() {
    double x = 0.1 + 0.2;          // 0.30000000000000004
    double y = 0.3;

    std::cout << std::boolalpha;
    std::cout << "x == y:          " << (x == y)             << "\n"; // false
    std::cout << "almostEqual:     " << almostEqual(x, y)    << "\n"; // true

    std::cout << "epsilon(double): " << std::numeric_limits<double>::epsilon() << "\n";
    std::cout << "epsilon(float):  " << std::numeric_limits<float>::epsilon()  << "\n";

    return 0;
}
```

### Example 3: Printing a Full Type Spec Table
```cpp
#include <limits>
#include <iostream>
#include <iomanip>
#include <string>

template <typename T>
void printLimits(const std::string& name) {
    std::cout << std::left << std::setw(18) << name
              << " | min=" << std::setw(20) << std::numeric_limits<T>::min()
              << " | max=" << std::numeric_limits<T>::max()
              << "\n";
}

int main() {
    std::cout << std::string(70, '-') << "\n";
    printLimits<bool>              ("bool");
    printLimits<char>              ("char");
    printLimits<short>             ("short");
    printLimits<int>               ("int");
    printLimits<long>              ("long");
    printLimits<long long>         ("long long");
    printLimits<unsigned int>      ("unsigned int");
    printLimits<unsigned long long>("unsigned long long");
    printLimits<float>             ("float");
    printLimits<double>            ("double");
    printLimits<long double>       ("long double");
    std::cout << std::string(70, '-') << "\n";
    return 0;
}
```

### Example 4: Generic Clamp Function
```cpp
#include <limits>
#include <iostream>
#include <algorithm>

template <typename T>
T clampToType(long long value) {
    static_assert(std::is_integral_v<T>, "T must be an integral type");

    long long lo = static_cast<long long>(std::numeric_limits<T>::min());
    long long hi = static_cast<long long>(std::numeric_limits<T>::max());

    if (value < lo) return std::numeric_limits<T>::min();
    if (value > hi) return std::numeric_limits<T>::max();
    return static_cast<T>(value);
}

int main() {
    long long big  = 300LL;
    long long neg  = -200LL;
    long long fine = 42LL;

    std::cout << "Clamp 300  to uint8_t: " << (int)clampToType<uint8_t>(big)  << "\n"; // 255
    std::cout << "Clamp -200 to uint8_t: " << (int)clampToType<uint8_t>(neg)  << "\n"; // 0
    std::cout << "Clamp 42   to uint8_t: " << (int)clampToType<uint8_t>(fine) << "\n"; // 42

    return 0;
}
```

## ⚡ Performance Tips

### All Values are `constexpr` — Zero Runtime Cost
```cpp
// Use as compile-time constants — no function call at runtime
constexpr int MAX_INT = std::numeric_limits<int>::max(); // evaluated at compile time

// Use in array sizes (C++11 constexpr)
constexpr int DIGITS = std::numeric_limits<long long>::digits10; // 18
char buf[DIGITS + 2]; // safely sized buffer
```

### Prefer `lowest()` Over `min()` for Initialising Running Minimum/Maximum
```cpp
// Wrong: initialise max-search with min() for floats
double current_max = std::numeric_limits<double>::min(); // tiny positive, NOT most negative!

// Correct: always use lowest()
double current_max = std::numeric_limits<double>::lowest(); // works for any arithmetic type
```

## 🐛 Common Pitfalls & Solutions

### 1. `min()` for Floats Is NOT the Most Negative Value
```cpp
// Bug: using min() as "most negative" for double
double worst = std::numeric_limits<double>::min(); // 2.22e-308, NOT -1.8e+308

// Fix: use lowest()
double worst = std::numeric_limits<double>::lowest(); // -1.79769e+308
```

### 2. Comparing Floats with `==` Instead of `epsilon`
```cpp
// Bug
double a = 0.1 + 0.2;
if (a == 0.3) { /* never true */ }

// Fix: use epsilon-based comparison
double eps = std::numeric_limits<double>::epsilon();
if (std::abs(a - 0.3) < eps * 10) { /* correct */ }
```

### 3. Integer Overflow Without Checking Limits
```cpp
int a = std::numeric_limits<int>::max();
int b = a + 1; // undefined behaviour! wraps or crashes

// Fix: check before arithmetic
if (a > std::numeric_limits<int>::max() - 1)
    throw std::overflow_error("Overflow!");
```

### 4. Using C Macros Instead of `numeric_limits` in Templates
```cpp
// Bad: INT_MAX is not generic — breaks in templates
template <typename T>
T myMax() { return INT_MAX; } // Only works for int!

// Good: generic and correct
template <typename T>
T myMax() { return std::numeric_limits<T>::max(); }
```

## 🎯 Best Practices

1. **Always use `lowest()`** (not `min()`) when initialising a maximum-search variable for floats
2. **Use `epsilon()` for floating-point comparisons** — never compare with `==`
3. **Make limits `constexpr`** local constants to document intent and avoid repeated function calls
4. **Use `numeric_limits` in templates** instead of type-specific macros (`INT_MAX`, etc.)
5. **Combine with `<type_traits>`** — check `is_integral` or `is_floating_point` before applying limits-specific logic
6. **Check before arithmetic** when overflow is possible (especially with `long long` → `int` narrowing)

## 📚 Related Headers

- [`type_traits.md`](33_type_traits.md) — Compile-time type queries that complement numeric limits
- [`cstdlib.md`](06_cstdlib.md) — Legacy C macros (`INT_MAX`) that `numeric_limits` replaces
- [`cmath.md`](05_cmath.md) — `INFINITY`, `NAN` and functions like `isinf()`, `isnan()`
- [`numeric.md`](24_numeric.md) — Algorithms that operate on numeric ranges

## 🚀 Next Steps

1. Write a generic `findMin` / `findMax` using `numeric_limits<T>::lowest()` and `max()`
2. Implement an overflow-safe arithmetic library using limits checks
3. Explore `std::numeric_limits<T>::epsilon()` for robust floating-point unit tests
4. Investigate `<cstdint>` fixed-width types (`int8_t`, `uint64_t`) and their limits

---

**Examples in this file**: 4 complete programs  
**Key Type**: `std::numeric_limits<T>`  
**Key Members**: `min()`, `max()`, `lowest()`, `epsilon()`, `infinity()`, `quiet_NaN()`, `digits10`  
**Common Use Cases**: Overflow protection, float comparison, generic algorithms, sentinel values
