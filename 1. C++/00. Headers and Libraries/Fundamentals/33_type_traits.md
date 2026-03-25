# type_traits - Compile-Time Type Utilities

The `type_traits` header is the backbone of C++ template metaprogramming. It provides a rich set of compile-time predicates and transformations that let you inspect and manipulate types without any runtime cost.

## 📖 Overview

`<type_traits>` was introduced in C++11 and greatly expanded in C++14/17/20. Every trait is a template class (or alias) whose value or `type` member is determinable at compile time.

Two broad categories:
- **Type predicates** — answer yes/no questions about a type (e.g., `is_integral<T>`)
- **Type transformations** — produce a modified type (e.g., `remove_const<T>`, `add_pointer<T>`)

The naming convention `_v` (for value) and `_t` (for type) are C++17 convenience aliases.

## 🎯 Key Components

### Type Predicates (Boolean Traits)

#### Primary Type Categories
| Trait | True when T is… |
|-------|----------------|
| `is_void<T>` | `void` |
| `is_integral<T>` | `bool`, `char`, `int`, `long`, etc. |
| `is_floating_point<T>` | `float`, `double`, `long double` |
| `is_array<T>` | An array type `T[]` or `T[N]` |
| `is_pointer<T>` | A pointer type |
| `is_reference<T>` | lvalue or rvalue reference |
| `is_enum<T>` | An enum or enum class |
| `is_class<T>` | A class or struct |
| `is_function<T>` | A function type |

#### Type Properties
| Trait | True when T is… |
|-------|----------------|
| `is_const<T>` | const-qualified |
| `is_volatile<T>` | volatile-qualified |
| `is_signed<T>` | A signed arithmetic type |
| `is_unsigned<T>` | An unsigned arithmetic type |
| `is_arithmetic<T>` | Integral or floating-point |
| `is_fundamental<T>` | Arithmetic, void, or nullptr_t |
| `is_trivial<T>` | Trivially constructible and copyable |
| `is_standard_layout<T>` | Compatible with C structs |
| `is_pod<T>` | Both trivial and standard layout (C++17: deprecated) |

#### Type Relationships
| Trait | Meaning |
|-------|---------|
| `is_same<T, U>` | T and U are the same type |
| `is_base_of<Base, Derived>` | Base is a base class of Derived |
| `is_convertible<From, To>` | From is implicitly convertible to To |
| `is_constructible<T, Args...>` | T can be constructed with Args |
| `is_copy_constructible<T>` | T has a copy constructor |
| `is_move_constructible<T>` | T has a move constructor |

### Type Transformations

| Transformation | Result |
|----------------|--------|
| `remove_const<T>` | T without `const` |
| `remove_volatile<T>` | T without `volatile` |
| `remove_cv<T>` | T without `const` and `volatile` |
| `remove_reference<T>` | T without `&` or `&&` |
| `remove_pointer<T>` | T without `*` |
| `add_const<T>` | `const T` |
| `add_pointer<T>` | `T*` |
| `add_lvalue_reference<T>` | `T&` |
| `make_signed<T>` | Signed version of T |
| `make_unsigned<T>` | Unsigned version of T |
| `decay<T>` | Remove cv-qualifiers and references, arrays→pointer |
| `conditional<B, T, F>` | T if B is true, F otherwise |
| `enable_if<B, T>` | T if B is true, else substitution failure |
| `common_type<T, U>` | Common type of T and U |
| `underlying_type<Enum>` | Underlying integer type of enum |

## 🔧 Basic Operations

### Checking Type Properties
```cpp
#include <type_traits>
#include <iostream>

int main() {
    // Value-based checks (C++17 _v aliases)
    std::cout << std::boolalpha;
    std::cout << "int is integral:      " << std::is_integral_v<int>      << "\n"; // true
    std::cout << "double is integral:   " << std::is_integral_v<double>   << "\n"; // false
    std::cout << "float is floating:    " << std::is_floating_point_v<float> << "\n"; // true
    std::cout << "int* is pointer:      " << std::is_pointer_v<int*>      << "\n"; // true
    std::cout << "const int is const:   " << std::is_const_v<const int>   << "\n"; // true
    std::cout << "int is const:         " << std::is_const_v<int>         << "\n"; // false

    return 0;
}
```

### Type Transformations
```cpp
#include <type_traits>
#include <iostream>

int main() {
    // Transformation: _t alias gives the resulting type
    using T1 = std::remove_const_t<const int>;        // int
    using T2 = std::remove_reference_t<int&>;          // int
    using T3 = std::add_pointer_t<double>;             // double*
    using T4 = std::decay_t<const double[]>;           // double* (array decay)
    using T5 = std::conditional_t<true, int, double>;  // int
    using T6 = std::conditional_t<false, int, double>; // double

    std::cout << std::boolalpha;
    std::cout << std::is_same_v<T1, int>    << "\n"; // true
    std::cout << std::is_same_v<T2, int>    << "\n"; // true
    std::cout << std::is_same_v<T3, double*> << "\n"; // true
    std::cout << std::is_same_v<T5, int>    << "\n"; // true
    std::cout << std::is_same_v<T6, double> << "\n"; // true

    return 0;
}
```

### `if constexpr` — Compile-Time Branching (C++17)
```cpp
#include <type_traits>
#include <iostream>
#include <string>

template <typename T>
std::string describe(T value) {
    if constexpr (std::is_integral_v<T>) {
        return "integral: " + std::to_string(value);
    } else if constexpr (std::is_floating_point_v<T>) {
        return "floating-point: " + std::to_string(value);
    } else if constexpr (std::is_same_v<T, std::string>) {
        return "string: " + value;
    } else {
        return "unknown type";
    }
}

int main() {
    std::cout << describe(42)        << "\n";
    std::cout << describe(3.14)      << "\n";
    std::cout << describe(std::string("hello")) << "\n";
    return 0;
}
```

### `enable_if` — SFINAE-Based Overload Selection
```cpp
#include <type_traits>
#include <iostream>

// Only participates in overload resolution if T is integral
template <typename T>
std::enable_if_t<std::is_integral_v<T>, bool>
isEven(T value) {
    return value % 2 == 0;
}

int main() {
    std::cout << std::boolalpha;
    std::cout << isEven(4)  << "\n"; // true
    std::cout << isEven(7)  << "\n"; // false
    // isEven(3.14);  // compile-time error — not integral
    return 0;
}
```

## 🎮 Practical Examples

### Example 1: Generic `print` With Type Dispatch
```cpp
#include <type_traits>
#include <iostream>
#include <string>

template <typename T>
void print(const T& value) {
    if constexpr (std::is_same_v<T, bool>) {
        std::cout << (value ? "true" : "false");
    } else if constexpr (std::is_integral_v<T>) {
        std::cout << value << " (int)";
    } else if constexpr (std::is_floating_point_v<T>) {
        std::cout << value << " (float)";
    } else if constexpr (std::is_same_v<T, std::string>) {
        std::cout << '"' << value << '"';
    } else {
        std::cout << "[complex type]";
    }
    std::cout << "\n";
}

int main() {
    print(true);
    print(42);
    print(3.14);
    print(std::string("hello"));
    return 0;
}
```

### Example 2: Safe Numeric Converter
```cpp
#include <type_traits>
#include <iostream>
#include <limits>
#include <stdexcept>

template <typename To, typename From>
To safe_cast(From value) {
    static_assert(std::is_arithmetic_v<From> && std::is_arithmetic_v<To>,
                  "safe_cast only works on arithmetic types");

    if constexpr (std::is_integral_v<To> && std::is_floating_point_v<From>) {
        if (value != static_cast<From>(static_cast<To>(value)))
            throw std::overflow_error("Precision lost in cast");
    }
    if constexpr (std::is_integral_v<To> && std::is_integral_v<From>) {
        if (value > static_cast<From>(std::numeric_limits<To>::max()))
            throw std::overflow_error("Value too large for target type");
        if (value < static_cast<From>(std::numeric_limits<To>::min()))
            throw std::underflow_error("Value too small for target type");
    }

    return static_cast<To>(value);
}

int main() {
    try {
        int n = safe_cast<int>(42.0);       // OK
        std::cout << n << "\n";

        int m = safe_cast<int>(3.7);        // throws
    } catch (const std::exception& e) {
        std::cerr << "Cast error: " << e.what() << "\n";
    }
    return 0;
}
```

### Example 3: Compile-Time Serializer
```cpp
#include <type_traits>
#include <iostream>
#include <string>

// Serialize integral types as decimal
template <typename T>
std::enable_if_t<std::is_integral_v<T>, std::string>
serialize(T value) {
    return "int:" + std::to_string(value);
}

// Serialize floating-point types
template <typename T>
std::enable_if_t<std::is_floating_point_v<T>, std::string>
serialize(T value) {
    return "float:" + std::to_string(value);
}

// Serialize strings
std::string serialize(const std::string& value) {
    return "str:" + value;
}

int main() {
    std::cout << serialize(42)               << "\n"; // int:42
    std::cout << serialize(3.14)             << "\n"; // float:3.14
    std::cout << serialize(std::string("hi")) << "\n"; // str:hi
    return 0;
}
```

### Example 4: Zero-Initialisation Trait-Based Factory
```cpp
#include <type_traits>
#include <iostream>
#include <string>

template <typename T>
T makeDefault() {
    if constexpr (std::is_integral_v<T>)
        return T{0};
    else if constexpr (std::is_floating_point_v<T>)
        return T{0.0};
    else if constexpr (std::is_same_v<T, std::string>)
        return "";
    else
        return T{};
}

int main() {
    auto i = makeDefault<int>();
    auto d = makeDefault<double>();
    auto s = makeDefault<std::string>();

    std::cout << "int: "    << i << "\n";
    std::cout << "double: " << d << "\n";
    std::cout << "string: " << (s.empty() ? "(empty)" : s) << "\n";
    return 0;
}
```

## ⚡ Performance Tips

### All Traits are Zero Runtime Cost
```cpp
// Everything in <type_traits> is resolved during compilation.
// No if/else at runtime — the compiler eliminates dead branches with if constexpr.
static_assert(std::is_integral_v<int>, "int must be integral"); // compile-time check
```

### Prefer `if constexpr` Over Specialisation for Simple Cases
```cpp
// Simpler and more readable than explicit template specialisations
template <typename T>
void process(T val) {
    if constexpr (std::is_pointer_v<T>)
        std::cout << "pointer: " << *val << "\n";
    else
        std::cout << "value: " << val << "\n";
}
```

### Use `static_assert` to Catch Template Misuse Early
```cpp
template <typename T>
void sortArray(T* arr, int n) {
    static_assert(std::is_arithmetic_v<T>,
                  "sortArray requires an arithmetic element type");
    // ...
}
```

## 🐛 Common Pitfalls & Solutions

### 1. Forgetting That References Must Be Stripped First
```cpp
int& r = someInt;
// is_integral_v<int&> is FALSE — references are not integral!
std::cout << std::is_integral_v<int&> << "\n"; // 0

// Solution: strip the reference first
using Base = std::remove_reference_t<decltype(r)>; // int
std::cout << std::is_integral_v<Base> << "\n";    // 1
```

### 2. `is_pod` is Deprecated in C++17
```cpp
// Avoid is_pod — use is_trivial and is_standard_layout separately
static_assert(std::is_trivial_v<MyStruct>);
static_assert(std::is_standard_layout_v<MyStruct>);
```

### 3. `enable_if` in Return Type vs. Template Parameter
```cpp
// Both are valid; return type form is cleaner for non-template parameters
template <typename T>
std::enable_if_t<std::is_integral_v<T>, void> foo(T); // return type form

template <typename T, std::enable_if_t<std::is_integral_v<T>, int> = 0>
void bar(T); // non-type template param form — avoids ambiguity in some cases
```

### 4. `conditional` Evaluates Both Branches
```cpp
// Both types must be valid even if only one is chosen
// Won't compile if EvilType is broken even when conditional selects SafeType
using T = std::conditional_t<someCondition, SafeType, EvilType>;
```

## 🎯 Best Practices

1. **Use `_v` and `_t` aliases** (`is_integral_v`, `remove_const_t`) instead of `::value` / `::type`
2. **Prefer `if constexpr`** over SFINAE for readability in C++17 and later
3. **Use `static_assert`** to give clear error messages when templates are misused
4. **Strip CV-qualifiers and references** before applying traits to generic types
5. **Use `std::decay_t`** when you want "the plain value type" of any reference/array/CV-qualified type
6. **Pair with `<concepts>`** in C++20 for even more expressive constraints

## 📚 Related Headers

- [`typeinfo.md`](32_typeinfo.md) — Runtime type information (RTTI); complement to compile-time traits
- [`functional.md`](25_functional.md) — `std::invoke`, `std::is_invocable` use type traits heavily
- [`utility.md`](09_utility.md) — `std::declval` — used with type traits in SFINAE
- [`limits.md`](34_limits.md) — Runtime numeric limits that complement compile-time type info

## 🚀 Next Steps

1. Write a `TypePrinter<T>` that uses traits to describe any type in readable English
2. Implement a trait-constrained `sum()` function that only works on arithmetic types
3. Explore C++20 `<concepts>` (`std::integral`, `std::floating_point`) — traits in a cleaner syntax
4. Study `std::void_t` and detection idiom for advanced SFINAE patterns

---

**Examples in this file**: 4 complete programs  
**Key Predicates**: `is_integral`, `is_floating_point`, `is_same`, `is_pointer`, `is_constructible`  
**Key Transformations**: `remove_const`, `remove_reference`, `decay`, `conditional`, `enable_if`  
**Common Use Cases**: Template constraints, overload selection, compile-time dispatch, generic programming
