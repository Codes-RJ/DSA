# Lambda Expressions - Inline Anonymous Functions

Lambda expressions (introduced in C++11) let you define small, anonymous function objects inline, right where they are used — perfect for callbacks, predicates, and short-lived operations.

## 📖 Overview

A lambda is syntactic sugar for a **closure** — an automatically generated class with an `operator()`. The compiler captures the surrounding variables you specify and stores them as data members of that hidden class.

**Syntax:**
```
[capture-list](parameter-list) specifiers -> return-type { body }
```
All parts except the capture list and body are optional for simple lambdas.

## 🎯 Key Components

### Capture Modes
| Capture | Meaning |
|---------|---------|
| `[]` | Capture nothing |
| `[=]` | Capture all locals by **copy** |
| `[&]` | Capture all locals by **reference** |
| `[x]` | Capture `x` by copy |
| `[&x]` | Capture `x` by reference |
| `[=, &x]` | Default copy, but `x` by reference |
| `[&, x]` | Default reference, but `x` by copy |
| `[this]` | Capture `this` pointer |
| `[*this]` | Capture `*this` by value (C++17) |

### Specifiers
- `mutable` — allows a by-copy capture to be modified inside the lambda
- `noexcept` — marks the lambda as non-throwing
- `constexpr` (C++17) — lambda usable in constant expressions

## 🔧 Basic Operations

### Simple Lambdas
```cpp
#include <iostream>
#include <algorithm>
#include <vector>

int main() {
    // No capture, no parameters
    auto greet = []() { std::cout << "Hello, World!\n"; };
    greet();

    // With parameter
    auto square = [](int x) { return x * x; };
    std::cout << square(5) << "\n"; // 25

    // Capture by value
    int factor = 3;
    auto multiply = [factor](int x) { return x * factor; };
    std::cout << multiply(7) << "\n"; // 21

    // Capture by reference
    int count = 0;
    auto increment = [&count]() { count++; };
    increment(); increment(); increment();
    std::cout << "Count: " << count << "\n"; // 3

    return 0;
}
```

### Mutable Lambdas
```cpp
#include <iostream>

int main() {
    int start = 10;

    // By-copy capture is const by default — need 'mutable' to modify it
    auto counter = [start]() mutable {
        return start++;  // modifies the COPY, not the original
    };

    std::cout << counter() << "\n"; // 10
    std::cout << counter() << "\n"; // 11
    std::cout << counter() << "\n"; // 12
    std::cout << "Original start: " << start << "\n"; // 10 (unchanged)

    return 0;
}
```

### Explicit Return Type
```cpp
#include <iostream>

int main() {
    // Return type deduced automatically
    auto f1 = [](double x) { return x * 2.0; }; // deduced: double

    // Explicit return type (required when body has multiple returns of different types)
    auto clamp = [](int val, int lo, int hi) -> int {
        if (val < lo) return lo;
        if (val > hi) return hi;
        return val;
    };

    std::cout << clamp(5, 0, 10)  << "\n"; // 5
    std::cout << clamp(-3, 0, 10) << "\n"; // 0
    std::cout << clamp(15, 0, 10) << "\n"; // 10

    return 0;
}
```

### Generic Lambdas (C++14)
```cpp
#include <iostream>
#include <string>

int main() {
    // 'auto' parameters make it a generic lambda
    auto print = [](const auto& value) {
        std::cout << value << "\n";
    };

    print(42);
    print(3.14);
    print(std::string("hello"));

    // Generic comparator
    auto less_than = [](const auto& a, const auto& b) { return a < b; };
    std::cout << std::boolalpha << less_than(3, 5) << "\n";   // true
    std::cout << less_than(3.5, 1.2) << "\n";                  // false

    return 0;
}
```

## 🎮 Practical Examples

### Example 1: Lambdas with STL Algorithms
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

int main() {
    std::vector<int> nums = {5, 2, 8, 1, 9, 3, 7, 4, 6};

    // Sort descending
    std::sort(nums.begin(), nums.end(), [](int a, int b) { return a > b; });
    std::cout << "Descending: ";
    for (int n : nums) std::cout << n << " ";
    std::cout << "\n";

    // Count elements > 5
    int above5 = std::count_if(nums.begin(), nums.end(), [](int n) { return n > 5; });
    std::cout << "Above 5: " << above5 << "\n";

    // Transform: square each element
    std::vector<int> squared(nums.size());
    std::transform(nums.begin(), nums.end(), squared.begin(), [](int n) { return n * n; });
    std::cout << "Squared: ";
    for (int n : squared) std::cout << n << " ";
    std::cout << "\n";

    // Accumulate with lambda
    int sum = std::accumulate(nums.begin(), nums.end(), 0, [](int acc, int n) { return acc + n; });
    std::cout << "Sum: " << sum << "\n";

    return 0;
}
```

### Example 2: Lambda as Callback / Event Handler
```cpp
#include <iostream>
#include <functional>
#include <vector>
#include <string>

class Button {
    std::string label_;
    std::function<void()> onClick_;
    std::function<void(int, int)> onHover_;

public:
    Button(const std::string& label) : label_(label) {}

    void setOnClick(std::function<void()> fn) { onClick_ = fn; }
    void setOnHover(std::function<void(int, int)> fn) { onHover_ = fn; }

    void click()              { if (onClick_) onClick_(); }
    void hover(int x, int y)  { if (onHover_) onHover_(x, y); }
};

int main() {
    int clickCount = 0;

    Button btn("Submit");

    btn.setOnClick([&clickCount]() {
        clickCount++;
        std::cout << "Button clicked! (count=" << clickCount << ")\n";
    });

    btn.setOnHover([](int x, int y) {
        std::cout << "Hovering at (" << x << ", " << y << ")\n";
    });

    btn.click();
    btn.click();
    btn.hover(100, 200);
    btn.click();

    std::cout << "Total clicks: " << clickCount << "\n";
    return 0;
}
```

### Example 3: Lambda Factory (Returning Lambdas)
```cpp
#include <iostream>
#include <functional>

// Returns a lambda that adds 'n' to its argument
auto makeAdder(int n) {
    return [n](int x) { return x + n; };
}

// Returns a lambda that multiplies by 'factor'
auto makeMultiplier(double factor) {
    return [factor](double x) { return x * factor; };
}

// Function composition
auto compose(std::function<int(int)> f, std::function<int(int)> g) {
    return [f, g](int x) { return f(g(x)); };
}

int main() {
    auto add5     = makeAdder(5);
    auto add10    = makeAdder(10);
    auto double_  = makeMultiplier(2.0);

    std::cout << add5(3)    << "\n"; // 8
    std::cout << add10(3)   << "\n"; // 13
    std::cout << double_(4) << "\n"; // 8.0

    // Compose: add5 after add10 → adds 15
    auto add15 = compose(add5, add10);
    std::cout << add15(0)   << "\n"; // 15
    std::cout << add15(7)   << "\n"; // 22

    return 0;
}
```

### Example 4: IIFE and Complex Initialisation
```cpp
#include <iostream>
#include <vector>
#include <string>

int main() {
    // IIFE (Immediately Invoked Function Expression)
    int expensiveValue = []() {
        int result = 0;
        for (int i = 1; i <= 100; i++) result += i;
        return result;
    }();
    std::cout << "Sum 1–100: " << expensiveValue << "\n"; // 5050

    // Complex const initialisation using IIFE
    const std::vector<std::string> days = []() {
        std::vector<std::string> d;
        d.reserve(7);
        for (const auto& name : {"Mon","Tue","Wed","Thu","Fri","Sat","Sun"})
            d.emplace_back(name);
        return d;
    }();

    for (const auto& d : days) std::cout << d << " ";
    std::cout << "\n";

    // Recursive lambda (C++14+)
    std::function<int(int)> factorial = [&factorial](int n) -> int {
        return n <= 1 ? 1 : n * factorial(n - 1);
    };

    std::cout << "5! = " << factorial(5) << "\n"; // 120
    std::cout << "8! = " << factorial(8) << "\n"; // 40320

    return 0;
}
```

## ⚡ Performance Tips

### Prefer Lambdas Over `std::function` in Hot Paths
```cpp
// std::function has type-erasure overhead (heap alloc, virtual call)
std::function<int(int)> heavy = [](int x) { return x * 2; }; // slow

// Direct lambda: inlined by compiler — zero overhead
auto fast = [](int x) { return x * 2; }; // call gets inlined
```

### Avoid Capturing Large Objects by Value
```cpp
std::vector<int> big(1'000'000, 42);

// Bad: copies the entire vector into the closure
auto bad = [big]() { return big.size(); };

// Good: capture by reference or capture only what you need
auto good  = [&big]() { return big.size(); };
auto good2 = [sz = big.size()]() { return sz; }; // init capture
```

### Use Init Captures (C++14) for Move-Only Types
```cpp
#include <memory>

auto ptr = std::make_unique<int>(42);

// Can't capture unique_ptr by value (not copyable)
// Use init capture to MOVE it into the lambda
auto lambda = [p = std::move(ptr)]() {
    return *p;
};
std::cout << lambda() << "\n"; // 42
```

## 🐛 Common Pitfalls & Solutions

### 1. Dangling Reference Capture
```cpp
// Problem: capturing reference to local variable that outlives scope
std::function<int()> bad;
{
    int local = 42;
    bad = [&local]() { return local; }; // local is destroyed!
}
bad(); // undefined behaviour!

// Solution: capture by value if the lambda outlives the variable
auto good = [local]() { return local; }; // owns a copy
```

### 2. `[=]` Doesn't Capture `this` the Way You Think
```cpp
class MyClass {
    int value_ = 10;
public:
    auto getAdder() {
        return [=](int x) { return value_ + x; }; // captures 'this', NOT a copy of value_!
        // Better (C++17): [*this](int x) { return value_ + x; }
    }
};
```

### 3. Modifying a By-Copy Capture Without `mutable`
```cpp
int x = 5;
auto bad = [x]() { x++; };   // compile error: x is const in lambda

auto good = [x]() mutable { x++; return x; }; // OK; modifies the copy
```

### 4. Recursive Lambda Requires `std::function`
```cpp
// Plain 'auto' lambda can't call itself — type not known yet
// Use std::function (with overhead) or pass lambda as argument
std::function<int(int)> fib = [&fib](int n) -> int {
    return n <= 1 ? n : fib(n-1) + fib(n-2);
};
```

## 🎯 Best Practices

1. **Capture only what you need** — avoid `[=]` and `[&]` when you can be specific
2. **Prefer `[&]` for short lambdas**, `[=]` or init-captures for lambdas that outlive the scope
3. **Use `auto` parameters** (generic lambdas) instead of writing redundant template functions
4. **Use `[p = std::move(ptr)]`** to move unique types into a lambda
5. **Mark `noexcept`** if the lambda cannot throw — enables compiler optimisations
6. **Use IIFEs** for complex `const` initialisation instead of non-`const` temporaries

## 📚 Related Topics

- [`functional.md`](../Fundamentals/25_functional.md) — `std::function`, `std::bind`, `std::invoke`
- [`algorithm.md`](../Fundamentals/04_algorithm.md) — Algorithms that accept lambdas as predicates
- [`templates.md`](templates.md) — Generic lambdas and template metaprogramming
- [`move_semantics.md`](move_semantics.md) — Init captures with `std::move`

## 🚀 Next Steps

1. Rewrite all your `std::function` / functor patterns using lambdas
2. Implement a simple event system with `std::vector<std::function<void()>>`
3. Explore C++20 lambda improvements: template lambdas, `[=, this]` capture
4. Study `std::bind` vs lambdas — when each is appropriate

---

**Examples in this file**: 4 complete programs  
**Key Syntax**: `[capture](params) -> type { body }`, `mutable`, `constexpr`  
**Key Patterns**: Callback, factory, IIFE, recursive lambda, init capture  
**Common Use Cases**: STL predicates, event handlers, deferred execution, closures
