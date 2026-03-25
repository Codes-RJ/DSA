# Templates - Generic Programming in C++

Templates are one of C++'s most powerful features, allowing you to write code once and use it with any type — achieving zero-cost abstraction and maximum code reuse.

## 📖 Overview

A **template** is a blueprint for generating type-specific code at compile time. The compiler instantiates a separate version of the template for each unique set of type arguments. This happens at compile time, so there is no runtime overhead.

Two primary kinds:
- **Function templates** — generic functions parameterised by type
- **Class templates** — generic classes (e.g., `std::vector<T>`, `std::pair<K,V>`)

## 🎯 Key Concepts

- **Type parameters** (`typename T` / `class T`) — placeholders for types
- **Non-type parameters** — constant values as template arguments (e.g., `int N`)
- **Template argument deduction** — compiler infers T from function arguments
- **Specialisation** — custom implementation for a specific type
- **Partial specialisation** — custom implementation for a subset of types
- **Variadic templates** — templates accepting any number of arguments (C++11)
- **SFINAE** — Substitution Failure Is Not An Error — used for overload selection
- **Concepts** (C++20) — named constraints on template parameters

## 🔧 Basic Operations

### Function Templates
```cpp
#include <iostream>

// Basic function template
template <typename T>
T maximum(T a, T b) {
    return (a > b) ? a : b;
}

// Multiple type parameters
template <typename T, typename U>
auto add(T a, U b) -> decltype(a + b) {
    return a + b;
}

int main() {
    std::cout << maximum(3, 7)         << "\n"; // int version:    7
    std::cout << maximum(3.14, 2.71)   << "\n"; // double version: 3.14
    std::cout << maximum('a', 'z')     << "\n"; // char version:   z

    std::cout << add(3, 2.5)           << "\n"; // int + double:   5.5
    return 0;
}
```

### Class Templates
```cpp
#include <iostream>
#include <stdexcept>

template <typename T, int Capacity = 10>
class FixedStack {
    T data_[Capacity];
    int top_ = 0;

public:
    void push(const T& value) {
        if (top_ >= Capacity)
            throw std::overflow_error("Stack is full");
        data_[top_++] = value;
    }

    T pop() {
        if (top_ == 0)
            throw std::underflow_error("Stack is empty");
        return data_[--top_];
    }

    T& peek() {
        if (top_ == 0) throw std::underflow_error("Stack is empty");
        return data_[top_ - 1];
    }

    bool empty() const { return top_ == 0; }
    int  size()  const { return top_; }
};

int main() {
    FixedStack<int, 5> intStack;
    intStack.push(10);
    intStack.push(20);
    intStack.push(30);

    std::cout << "Top: " << intStack.peek() << "\n"; // 30
    std::cout << "Pop: " << intStack.pop()  << "\n"; // 30
    std::cout << "Size: "  << intStack.size() << "\n"; // 2
    return 0;
}
```

### Template Specialisation
```cpp
#include <iostream>
#include <string>

// Primary template
template <typename T>
struct TypeName {
    static std::string name() { return "unknown"; }
};

// Full specialisations
template <> struct TypeName<int>    { static std::string name() { return "int"; } };
template <> struct TypeName<double> { static std::string name() { return "double"; } };
template <> struct TypeName<std::string> { static std::string name() { return "string"; } };

// Partial specialisation: pointer types
template <typename T>
struct TypeName<T*> { static std::string name() { return TypeName<T>::name() + "*"; } };

int main() {
    std::cout << TypeName<int>::name()         << "\n"; // int
    std::cout << TypeName<double>::name()      << "\n"; // double
    std::cout << TypeName<int*>::name()        << "\n"; // int*
    std::cout << TypeName<float>::name()       << "\n"; // unknown
    return 0;
}
```

### Non-Type Template Parameters
```cpp
#include <iostream>
#include <array>

// Matrix with compile-time dimensions
template <typename T, int Rows, int Cols>
class Matrix {
    T data_[Rows][Cols] = {};

public:
    T& at(int r, int c)             { return data_[r][c]; }
    const T& at(int r, int c) const { return data_[r][c]; }

    constexpr int rows() const { return Rows; }
    constexpr int cols() const { return Cols; }

    void print() const {
        for (int r = 0; r < Rows; r++) {
            for (int c = 0; c < Cols; c++)
                std::cout << data_[r][c] << "\t";
            std::cout << "\n";
        }
    }
};

int main() {
    Matrix<int, 2, 3> m;
    m.at(0, 0) = 1; m.at(0, 1) = 2; m.at(0, 2) = 3;
    m.at(1, 0) = 4; m.at(1, 1) = 5; m.at(1, 2) = 6;
    m.print();
    return 0;
}
```

## 🎮 Practical Examples

### Example 1: Generic Pair with Comparison
```cpp
#include <iostream>
#include <string>

template <typename First, typename Second>
class Pair {
public:
    First  first;
    Second second;

    Pair(const First& f, const Second& s) : first(f), second(s) {}

    bool operator==(const Pair& other) const {
        return first == other.first && second == other.second;
    }

    void print() const {
        std::cout << "(" << first << ", " << second << ")\n";
    }
};

template <typename F, typename S>
Pair<F, S> make_pair_custom(const F& f, const S& s) {
    return Pair<F, S>(f, s);
}

int main() {
    auto p1 = make_pair_custom(1, std::string("hello"));
    auto p2 = make_pair_custom(3.14, 42);
    auto p3 = make_pair_custom(1, std::string("hello"));

    p1.print(); // (1, hello)
    p2.print(); // (3.14, 42)

    std::cout << std::boolalpha;
    std::cout << (p1 == p3) << "\n"; // true
    return 0;
}
```

### Example 2: Variadic Template — `print_all`
```cpp
#include <iostream>

// Base case: nothing to print
void print_all() {}

// Recursive variadic template
template <typename First, typename... Rest>
void print_all(const First& first, const Rest&... rest) {
    std::cout << first;
    if constexpr (sizeof...(rest) > 0) std::cout << ", ";
    print_all(rest...);
}

// Variadic sum
template <typename T>
T sum(T value) { return value; }

template <typename T, typename... Args>
T sum(T first, Args... rest) {
    return first + sum(rest...);
}

int main() {
    print_all(1, 2.5, "hello", 'X');    // 1, 2.5, hello, X
    std::cout << "\n";
    std::cout << sum(1, 2, 3, 4, 5)    << "\n"; // 15
    std::cout << sum(1.1, 2.2, 3.3)    << "\n"; // 6.6
    return 0;
}
```

### Example 3: CRTP (Curiously Recurring Template Pattern)
```cpp
#include <iostream>

// CRTP base provides derived-dependent behaviour at zero cost
template <typename Derived>
class Printable {
public:
    void print() const {
        static_cast<const Derived*>(this)->print_impl();
    }
};

class Point : public Printable<Point> {
public:
    int x, y;
    Point(int x, int y) : x(x), y(y) {}
    void print_impl() const {
        std::cout << "Point(" << x << ", " << y << ")\n";
    }
};

class Circle : public Printable<Circle> {
public:
    int cx, cy, r;
    Circle(int cx, int cy, int r) : cx(cx), cy(cy), r(r) {}
    void print_impl() const {
        std::cout << "Circle(center=(" << cx << "," << cy << "), r=" << r << ")\n";
    }
};

template <typename T>
void printShape(const Printable<T>& shape) {
    shape.print();
}

int main() {
    Point  p(3, 4);
    Circle c(0, 0, 5);
    printShape(p);  // Point(3, 4)
    printShape(c);  // Circle(center=(0,0), r=5)
    return 0;
}
```

### Example 4: Type-Safe Builder with Templates
```cpp
#include <iostream>
#include <string>
#include <sstream>

template <typename T>
class Builder {
    T object_;

public:
    Builder() = default;
    explicit Builder(T init) : object_(std::move(init)) {}

    template <typename Member, typename Value>
    Builder& set(Member T::* field, Value&& value) {
        object_.*field = std::forward<Value>(value);
        return *this;
    }

    T build() { return std::move(object_); }
};

struct Config {
    std::string host = "localhost";
    int port         = 8080;
    bool tls         = false;
    int timeout      = 30;
};

int main() {
    Config cfg = Builder<Config>{}
        .set(&Config::host,    "example.com")
        .set(&Config::port,    443)
        .set(&Config::tls,     true)
        .set(&Config::timeout, 60)
        .build();

    std::cout << "Host:    " << cfg.host    << "\n";
    std::cout << "Port:    " << cfg.port    << "\n";
    std::cout << "TLS:     " << std::boolalpha << cfg.tls << "\n";
    std::cout << "Timeout: " << cfg.timeout << "s\n";
    return 0;
}
```

## ⚡ Performance Tips

### Templates Are Zero Runtime Cost
```cpp
// The compiler generates separate, fully optimised code for each instantiation
maximum<int>(3, 7);     // generates an int-specific function
maximum<double>(3.14, 2.71); // generates a double-specific function
// No virtual dispatch, no type erasure overhead
```

### Avoid Unnecessary Instantiations
```cpp
// Every unique set of template args = separate binary code
// Use explicit instantiation declarations to control what is compiled
template class FixedStack<int, 100>;   // explicit instantiation (put in .cpp)
extern template class FixedStack<int, 100>; // declaration (put in header)
```

### Inline Small Templates in Headers
```cpp
// Template definitions MUST be visible at the point of instantiation
// Typically: put both declaration and definition in the .h file
// Large templates: use explicit instantiation in a .cpp to limit code bloat
```

## 🐛 Common Pitfalls & Solutions

### 1. Definition Must Be in the Header
```cpp
// Problem: template defined in .cpp won't link
// template.h:
template <typename T> T square(T x); // declaration only

// template.cpp:
template <typename T> T square(T x) { return x * x; } // definition — won't link!

// Solution: put definition in the header
template <typename T> T square(T x) { return x * x; }
```

### 2. Confusing `typename` and `class`
```cpp
// Both are identical for simple type parameters
template <typename T> void foo(T); // preferred in modern C++
template <class T>    void bar(T); // also valid, older style

// Only `typename` can be used to disambiguate dependent types:
template <typename T>
void baz() {
    typename T::value_type val; // 'typename' required here
}
```

### 3. Long, Unreadable Error Messages
```cpp
// Problem: template errors appear at the point of instantiation, not definition
// Solution: use static_assert to produce clear messages
template <typename T>
T sqrt_positive(T x) {
    static_assert(std::is_floating_point_v<T>, "sqrt_positive requires a float type");
    static_assert(!std::is_same_v<T, void>,    "T cannot be void");
    return std::sqrt(x);
}
```

### 4. Accidental Copies in Template Functions
```cpp
// Bad: copies the entire container
template <typename T>
void process(T container) { /* ... */ }

// Good: use const reference
template <typename T>
void process(const T& container) { /* ... */ }

// Or perfect forwarding for maximum flexibility
template <typename T>
void process(T&& container) { /* ... */ }
```

## 🎯 Best Practices

1. **Put template definitions in headers** — the compiler needs them at instantiation sites
2. **Use `static_assert`** for readable error messages when type constraints are violated
3. **Prefer `if constexpr`** over template specialisation for simple type-dependent branches
4. **Use Concepts (C++20)** to express constraints readably: `template <std::integral T>`
5. **Keep templates small and focused** — a 500-line template is a maintenance nightmare
6. **Use CRTP** for zero-cost compile-time polymorphism when virtual dispatch is too slow

## 📚 Related Topics

- [`type_traits.md`](../Fundamentals/33_type_traits.md) — `enable_if`, `is_integral`, `conditional` — essential for templates
- [`functional.md`](../Fundamentals/25_functional.md) — `std::function` and lambdas as template arguments
- [`move_semantics.md`](move_semantics.md) — Perfect forwarding in templates
- [`smart_pointers.md`](smart_pointers.md) — Class templates in action

## 🚀 Next Steps

1. Implement a generic `Optional<T>` (or study `std::optional`)
2. Write a type-safe heterogeneous container using variadic templates
3. Explore CRTP to add mixin behaviour without virtual functions
4. Learn C++20 Concepts for expressive, readable template constraints

---

**Examples in this file**: 4 complete programs  
**Key Keywords**: `template`, `typename`, `class`, `auto`, `if constexpr`, `static_assert`  
**Key Patterns**: CRTP, variadic templates, specialisation, non-type parameters  
**Common Use Cases**: Containers, algorithms, policies, mixins, metaprogramming
