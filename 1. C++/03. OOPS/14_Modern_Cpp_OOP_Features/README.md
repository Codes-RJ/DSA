# README.md

## Modern C++ OOP Features - Complete Guide

### Overview

Modern C++ (C++11 and later) introduced significant enhancements to object-oriented programming in C++. These features improve type safety, reduce boilerplate code, enable better resource management, and make C++ more expressive and easier to use. Understanding modern C++ features is essential for writing contemporary, efficient, and maintainable C++ code.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [01_Auto_and_Decltype.md](01_Auto_and_Decltype.md) | understand Auto and Decltype Type Deduction |
| 2. | [02_Range_Based_For_Loops.md](02_Range_Based_For_Loops.md) | understand Range-Based For Loops |
| 3. | [03_Lambda_Expressions.md](03_Lambda_Expressions.md) | understand Lambda Expressions |
| 4. | [04_Smart_Pointers.md](04_Smart_Pointers.md) | understand Smart Pointers |
| 5. | [05_Move_Semantics.md](05_Move_Semantics.md) | understand Move Semantics |
| 6. | [06_Initializer_Lists.md](06_Initializer_Lists.md) | understand Initializer Lists |
| 7. | [07_Delegating_Constructors.md](07_Delegating_Constructors.md) | understand Delegating Constructors |
| 8. | [08_Inheriting_Constructors.md](08_Inheriting_Constructors.md) | understand Inheriting Constructors |
| 9. | [09_Override_and_Final.md](09_Override_and_Final.md) | understand Override and Final Specifiers |
| 10. | [10_Concepts.md](10_Concepts.md) | understand Concepts (C++20) |
| 11. | [Theory.md](Theory.md) | understand Theoretical Foundations of Modern C++ |

---

## 1. Auto and Decltype

This topic explains type deduction using `auto` and `decltype` for writing more flexible and maintainable code.

**File:** [01_Auto_and_Decltype.md](01_Auto_and_Decltype.md)

**What you will learn:**
- What is `auto` type deduction (C++11)
- When to use `auto` (iterator types, complex template types)
- `auto` with references, pointers, and qualifiers
- What is `decltype` (C++11)
- Difference between `auto` and `decltype`
- `decltype(auto)` (C++14)

**Key Concepts:**

| Keyword | Purpose | Example |
|---------|---------|---------|
| `auto` | Deduce type from initializer | `auto x = 42;` // x is int |
| `decltype` | Get type of expression | `decltype(x) y = x;` // y same type as x |
| `decltype(auto)` | Combine both (C++14) | Perfect forwarding |

**Syntax:**
```cpp
// Auto examples
auto i = 42;           // int
auto d = 3.14;         // double
auto s = "hello";      // const char*
auto v = vector<int>{1,2,3};
auto it = v.begin();   // vector<int>::iterator

// decltype examples
int x = 10;
decltype(x) y = 20;    // y is int
decltype((x)) ref = x; // ref is int&

// decltype(auto) - preserves reference
int& getRef() { static int x; return x; }
decltype(auto) r = getRef();  // r is int&
```

---

## 2. Range-Based For Loops

This topic explains the simplified iteration syntax for containers.

**File:** [02_Range_Based_For_Loops.md](02_Range_Based_For_Loops.md)

**What you will learn:**
- What are range-based for loops (C++11)
- Syntax for iterating over containers
- Auto with range-based for loops
- Modification of elements using references
- Custom container support (begin/end functions)

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Range Expression** | Container or array to iterate over |
| **Declaration** | Variable that takes each element |
| **Auto** | Type deduction for element type |
| **Reference** | Use `&` to modify elements |

**Syntax:**
```cpp
vector<int> vec = {1, 2, 3, 4, 5};

// Read-only iteration
for (int x : vec) {
    cout << x << " ";
}

// Modification using reference
for (int& x : vec) {
    x *= 2;
}

// Using auto
for (auto& x : vec) {
    x *= 2;
}

// Using const auto& for read-only (no copy)
for (const auto& x : vec) {
    cout << x << " ";
}
```

---

## 3. Lambda Expressions

This topic explains lambda expressions for creating anonymous function objects.

**File:** [03_Lambda_Expressions.md](03_Lambda_Expressions.md)

**What you will learn:**
- What are lambda expressions (C++11)
- Lambda syntax: `[capture](params) -> ret { body }`
- Capture by value (`[=]`) and by reference (`[&]`)
- Mutable lambdas
- Generic lambdas (C++14)
- Lambda expressions with STL algorithms

**Key Concepts:**

| Concept | Syntax | Description |
|---------|--------|-------------|
| **Capture** | `[&]` `[=]` `[a, &b]` | What variables are accessible |
| **Parameters** | `(int x, int y)` | Function parameters |
| **Return Type** | `-> int` | Optional, can be deduced |
| **Body** | `{ return x + y; }` | Lambda code |

**Syntax:**
```cpp
// Basic lambda
auto add = [](int a, int b) { return a + b; };
cout << add(3, 5);  // 8

// Capture by value
int multiplier = 10;
auto times = [multiplier](int x) { return x * multiplier; };

// Capture by reference
int counter = 0;
auto increment = [&counter]() { counter++; };

// Capture everything
auto print = [&]() { cout << counter << endl; };

// Generic lambda (C++14)
auto generic = [](auto a, auto b) { return a + b; };
cout << generic(3, 5);      // 8
cout << generic(3.14, 2.71); // 5.85

// Lambda with STL
sort(vec.begin(), vec.end(), 
     [](int a, int b) { return a > b; });
```

---

## 4. Smart Pointers

This topic explains RAII wrappers for dynamic memory management.

**File:** [04_Smart_Pointers.md](04_Smart_Pointers.md)

**What you will learn:**
- What are smart pointers (C++11)
- `std::unique_ptr` for exclusive ownership
- `std::shared_ptr` for shared ownership
- `std::weak_ptr` for breaking cycles
- `std::make_unique` and `std::make_shared`
- Custom deleters

**Key Concepts:**

| Smart Pointer | Ownership | Overhead | Use Case |
|---------------|-----------|----------|----------|
| **unique_ptr** | Exclusive | Zero | Single owner |
| **shared_ptr** | Shared | Control block | Multiple owners |
| **weak_ptr** | Non-owning | Same as shared | Breaking cycles |

**Syntax:**
```cpp
// unique_ptr
unique_ptr<int> u1 = make_unique<int>(42);
unique_ptr<int> u2 = move(u1);  // Transfer ownership

// shared_ptr
shared_ptr<int> s1 = make_shared<int>(100);
shared_ptr<int> s2 = s1;  // Shared ownership
cout << s1.use_count();    // 2

// weak_ptr
weak_ptr<int> w = s1;
if (auto sp = w.lock()) {  // Check if still alive
    cout << *sp;
}

// Custom deleter
auto deleter = [](int* p) { delete p; };
unique_ptr<int, decltype(deleter)> u(new int(42), deleter);
```

---

## 5. Move Semantics

This topic explains move semantics for efficient transfer of resources.

**File:** [05_Move_Semantics.md](05_Move_Semantics.md)

**What you will learn:**
- What are move semantics (C++11)
- Lvalues and rvalues
- Move constructor and move assignment
- `std::move` function
- Move-only types (unique_ptr)
- Perfect forwarding with `std::forward`

**Key Concepts:**

| Concept | Description | Example |
|---------|-------------|---------|
| **Lvalue** | Has address, persists | `int x = 5;` |
| **Rvalue** | Temporary, will be destroyed | `int(5)` |
| **Move** | Transfer resources, not copy | `std::move(x)` |
| **Perfect Forwarding** | Preserve value category | `std::forward<T>(arg)` |

**Syntax:**
```cpp
class Buffer {
    int* data_;
    size_t size_;
public:
    // Move constructor
    Buffer(Buffer&& other) noexcept 
        : data_(other.data_), size_(other.size_) {
        other.data_ = nullptr;
        other.size_ = 0;
    }
    
    // Move assignment
    Buffer& operator=(Buffer&& other) noexcept {
        if (this != &other) {
            delete[] data_;
            data_ = other.data_;
            size_ = other.size_;
            other.data_ = nullptr;
            other.size_ = 0;
        }
        return *this;
    }
};

// Using std::move
vector<string> v1 = {"a", "b"};
vector<string> v2 = std::move(v1);  // v1 now empty
```

---

## 6. Initializer Lists

This topic explains uniform initialization and initializer lists.

**File:** [06_Initializer_Lists.md](06_Initializer_Lists.md)

**What you will learn:**
- Uniform initialization syntax (C++11)
- `std::initializer_list` class
- Initializer list constructors
- Preventing narrowing conversions
- Initializer lists for containers

**Key Concepts:**

| Syntax | Description | Example |
|--------|-------------|---------|
| **Braced Initialization** | Uniform initialization | `int x{5};` |
| **Narrowing Prevention** | Compile-time error | `int x{3.14};` // Error |
| **Initializer List Constructor** | Takes `initializer_list<T>` | `vector<int> v{1,2,3};` |

**Syntax:**
```cpp
// Uniform initialization
int a{10};
double b{3.14};
string s{"hello"};

// Preventing narrowing
int x{3.14};  // Error - narrowing

// Initializer list constructor
class MyVector {
    vector<int> data_;
public:
    MyVector(initializer_list<int> list) : data_(list) { }
};

MyVector v = {1, 2, 3, 4, 5};

// Function with initializer_list
int sum(initializer_list<int> list) {
    int total = 0;
    for (int x : list) total += x;
    return total;
}
cout << sum({1, 2, 3, 4});  // 10
```

---

## 7. Delegating Constructors

This topic explains how constructors can call other constructors of the same class.

**File:** [07_Delegating_Constructors.md](07_Delegating_Constructors.md)

**What you will learn:**
- What are delegating constructors (C++11)
- Syntax for delegating to another constructor
- Reducing code duplication
- Delegation chains
- Limitations and best practices

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Target Constructor** | Constructor that does the actual work |
| **Delegating Constructor** | Calls another constructor |
| **Initialization List** | Delegation happens in initialization list |

**Syntax:**
```cpp
class Rectangle {
    int width_, height_;
public:
    // Target constructor (does the work)
    Rectangle(int w, int h) : width_(w), height_(h) { }
    
    // Delegating constructors
    Rectangle() : Rectangle(0, 0) { }           // Delegates to target
    Rectangle(int side) : Rectangle(side, side) { }  // Delegates
    Rectangle(int side, int ratio) : Rectangle(side, side * ratio) { }
};

// Usage
Rectangle r1;           // Uses Rectangle(0,0)
Rectangle r2(10);       // Uses Rectangle(10,10)
Rectangle r3(5, 10);    // Direct call
```

---

## 8. Inheriting Constructors

This topic explains how derived classes can inherit constructors from base classes.

**File:** [08_Inheriting_Constructors.md](08_Inheriting_Constructors.md)

**What you will learn:**
- What are inheriting constructors (C++11)
- Syntax: `using Base::Base;`
- Bringing all base constructors into derived class
- Overriding specific constructors
- Limitations

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Constructor Inheritance** | Derived class inherits base constructors |
| **Using Declaration** | `using Base::Base;` |
| **Custom Constructors** | Can add new constructors |

**Syntax:**
```cpp
class Base {
public:
    Base() { }
    Base(int x) { }
    Base(int x, double y) { }
};

class Derived : public Base {
public:
    // Inherit all Base constructors
    using Base::Base;
    
    // Add a custom constructor
    Derived(string s) { }
};

// Usage
Derived d1;           // Base()
Derived d2(10);       // Base(int)
Derived d3(10, 3.14); // Base(int, double)
Derived d4("hello");  // Derived(string)
```

---

## 9. Override and Final Specifiers

This topic explains specifiers for controlling virtual function overriding and inheritance.

**File:** [09_Override_and_Final.md](09_Override_and_Final.md)

**What you will learn:**
- `override` specifier (C++11)
- `final` specifier for functions (C++11)
- `final` specifier for classes (C++11)
- Preventing further overriding
- Preventing inheritance

**Key Concepts:**

| Specifier | Purpose | Example |
|-----------|---------|---------|
| `override` | Explicitly marks overriding function | `void func() override;` |
| `final` (function) | Prevents further overriding | `void func() final;` |
| `final` (class) | Prevents inheritance | `class Derived final { };` |

**Syntax:**
```cpp
class Base {
public:
    virtual void f1();
    virtual void f2();
    virtual void f3();
};

class Derived : public Base {
public:
    void f1() override;     // OK - overrides Base::f1
    // void f2() override;  // Error if signature mismatch
    void f3() final;        // OK - can't be overridden further
};

class MoreDerived : public Derived {
public:
    // void f3() override;  // Error - f3 is final
};

// Final class
class FinalClass final {
    // No class can inherit from this
};
// class DerivedFinal : public FinalClass { };  // Error!
```

---

## 10. Concepts

This topic explains concepts for constraining template parameters (C++20).

**File:** [10_Concepts.md](10_Concepts.md)

**What you will learn:**
- What are concepts (C++20)
- Defining concepts with `concept` keyword
- Using concepts with `requires` clause
- Predefined standard concepts
- Benefits (clear error messages, better code organization)

**Key Concepts:**

| Concept | Description | Example |
|---------|-------------|---------|
| **Concept Definition** | Names set of requirements | `template <typename T> concept Integral = is_integral_v<T>;` |
| **Requires Clause** | Constrains template parameters | `requires Integral<T>` |
| **Standard Concepts** | C++20 standard library concepts | `std::integral`, `std::floating_point` |

**Syntax:**
```cpp
// Defining a concept
template <typename T>
concept Numeric = std::is_arithmetic_v<T>;

// Using concept with requires clause
template <Numeric T>
T add(T a, T b) {
    return a + b;
}

// Alternative syntax with requires
template <typename T>
requires Numeric<T>
T multiply(T a, T b) {
    return a * b;
}

// Using standard concepts
#include <concepts>

template <std::integral T>
T doubleValue(T x) {
    return x * 2;
}

// Compile-time error with clear message
// doubleValue(3.14);  // Error: double is not integral
```

---

## 11. Theoretical Foundations

This topic covers the theoretical concepts behind modern C++ features.

**File:** [Theory.md](Theory.md)

**What you will learn:**
- Evolution of C++ standards (C++11, C++14, C++17, C++20, C++23)
- Type deduction rules
- Move semantics theory
- Perfect forwarding mechanics
- RAII evolution
- Zero-overhead principle

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Zero-Overhead Principle** | What you don't use, you don't pay for |
| **Type Deduction** | Compiler infers types automatically |
| **Value Categories** | Lvalue, rvalue, xvalue, prvalue, glvalue |
| **RAII** | Resource Acquisition Is Initialization |

---

### Prerequisites

Before starting this section, you should have completed:

- [01. Basics](../../01.%20Basics/README.md) - C++ fundamentals
- [02_Classes_and_Objects/README.md](../02_Classes_and_Objects/README.md) - Class basics
- [05_Inheritance/README.md](../05_Inheritance/README.md) - Inheritance
- [06_Polymorphism/README.md](../06_Polymorphism/README.md) - Polymorphism
- [09_Templates_and_Generic_Programming/README.md](../09_Templates_and_Generic_Programming/README.md) - Templates

---

### Modern C++ Features by Standard

| Standard | Key Features |
|----------|--------------|
| **C++11** | auto, decltype, range-based for, lambdas, smart pointers, move semantics, initializer lists, delegating constructors, inheriting constructors, override/final |
| **C++14** | Generic lambdas, decltype(auto), variable templates |
| **C++17** | Fold expressions, structured bindings, if constexpr, inline variables |
| **C++20** | Concepts, ranges, coroutines, three-way comparison (spaceship operator) |
| **C++23** | std::expected, std::mdspan, deducing this |

---

### Learning Path

```
Level 1: Type Deduction and Iteration
├── Auto and Decltype
├── Range-Based For Loops
└── Initializer Lists

Level 2: Function Objects
├── Lambda Expressions
└── Move Semantics

Level 3: Resource Management
├── Smart Pointers
└── RAII Evolution

Level 4: Constructor Improvements
├── Delegating Constructors
├── Inheriting Constructors
└── Override and Final

Level 5: Template Improvements (C++20)
├── Concepts
└── Ranges
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Using `auto` when type is not obvious | Use explicit types for clarity |
| Capturing by reference in lambdas that outlive scope | Capture by value or ensure lifetime |
| Using `shared_ptr` when `unique_ptr` suffices | Prefer `unique_ptr` for single ownership |
| Forgetting `std::move` for move-only types | Use `std::move` to transfer ownership |
| Using raw pointers for ownership | Use smart pointers |
| Ignoring `override` specifier | Use `override` to catch errors |

---

### Practice Questions

After completing this section, you should be able to:

1. Use `auto` to simplify iterator declarations
2. Write lambda expressions for sorting and filtering
3. Implement move constructor and move assignment
4. Use `unique_ptr` and `shared_ptr` correctly
5. Apply `override` and `final` specifiers
6. Create delegating constructors to reduce code duplication
7. Use range-based for loops for container iteration
8. Define and use concepts (C++20)

---

### Next Steps

- Go to [Theory.md](Theory.md) to understand basics of the module.