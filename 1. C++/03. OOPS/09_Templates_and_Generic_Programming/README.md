# README.md

## Templates and Generic Programming in C++ - Complete Guide

### Overview

Templates are a powerful feature in C++ that enable generic programming. They allow writing code that works with any data type without duplicating the code for each type. Templates are the foundation of the C++ Standard Template Library (STL) and enable compile-time polymorphism. Understanding templates is essential for writing reusable, type-safe, and efficient C++ code.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [01_Function_Templates.md](01_Function_Templates.md) | understand Function Templates |
| 2. | [02_Class_Templates.md](02_Class_Templates.md) | understand Class Templates |
| 3. | [03_Template_Specialization.md](03_Template_Specialization.md) | understand Template Specialization |
| 4. | [04_Variadic_Templates.md](04_Variadic_Templates.md) | understand Variadic Templates (C++11) |
| 5. | [05_Template_Metaprogramming.md](05_Template_Metaprogramming.md) | understand Template Metaprogramming |
| 6. | [Theory.md](Theory.md) | understand Theoretical Foundations of Templates |

---

## 1. Function Templates

This topic explains how to write function templates that work with any data type.

**File:** [01_Function_Templates.md](01_Function_Templates.md)

**What you will learn:**
- What are function templates
- Syntax for declaring function templates (`template <typename T>`)
- Template parameter deduction
- Explicit template instantiation
- Function template overloading
- Benefits of function templates (code reuse, type safety)

**Key Concepts:**

| Concept | Description | Example |
|---------|-------------|---------|
| **Template Parameter** | Placeholder for a type | `typename T` or `class T` |
| **Template Instantiation** | Compiler generates function for specific type | `swap<int>(a, b)` |
| **Type Deduction** | Compiler deduces template arguments from function arguments | `swap(a, b)` |
| **Explicit Specialization** | Custom implementation for specific type | `template <> void swap<char>(...)` |

**Syntax:**
```cpp
// Function template definition
template <typename T>
T max(T a, T b) {
    return (a > b) ? a : b;
}

// Usage
int main() {
    int x = 5, y = 10;
    int intResult = max(x, y);        // T deduced as int
    
    double a = 3.14, b = 2.71;
    double doubleResult = max(a, b);  // T deduced as double
    
    string s1 = "apple", s2 = "orange";
    string stringResult = max(s1, s2); // T deduced as string
    
    // Explicit instantiation
    int explicitResult = max<int>(x, y);
}
```

---

## 2. Class Templates

This topic explains how to create class templates for generic data structures.

**File:** [02_Class_Templates.md](02_Class_Templates.md)

**What you will learn:**
- What are class templates
- Syntax for declaring class templates
- Defining member functions outside the class
- Creating objects from class templates
- Template parameters with default types
- Non-type template parameters (e.g., `int N`)

**Key Concepts:**

| Concept | Description | Example |
|---------|-------------|---------|
| **Generic Class** | Class that works with any type | `class Stack<T>` |
| **Template Instantiation** | Creating specific class from template | `Stack<int> intStack;` |
| **Member Function Definition** | Functions defined outside require `template <typename T>` | `void Stack<T>::push(T item)` |
| **Non-Type Parameter** | Compile-time constant as template argument | `template <typename T, int size>` |

**Syntax:**
```cpp
// Class template definition
template <typename T, int capacity = 100>
class Stack {
private:
    T data_[capacity];
    int top_;
    
public:
    Stack() : top_(-1) {}
    
    void push(const T& item) {
        if (top_ < capacity - 1) {
            data_[++top_] = item;
        }
    }
    
    T pop() {
        if (top_ >= 0) {
            return data_[top_--];
        }
        throw out_of_range("Stack is empty");
    }
    
    bool isEmpty() const { return top_ == -1; }
};

// Usage
int main() {
    Stack<int> intStack;           // T=int, capacity=100 (default)
    Stack<double, 50> doubleStack; // T=double, capacity=50
    
    intStack.push(10);
    intStack.push(20);
    cout << intStack.pop() << endl;  // 20
}
```

---

## 3. Template Specialization

This topic explains how to provide custom implementations for specific types.

**File:** [03_Template_Specialization.md](03_Template_Specialization.md)

**What you will learn:**
- What is template specialization
- Full specialization (for specific types)
- Partial specialization (for specific patterns)
- Function template specialization
- Class template specialization
- When to use specialization (optimization, type-specific behavior)

**Key Concepts:**

| Concept | Description | Example |
|---------|-------------|---------|
| **Full Specialization** | Custom implementation for one specific type | `template <> class Stack<bool>` |
| **Partial Specialization** | Custom implementation for a category of types | `template <typename T> class Stack<T*>` |
| **Primary Template** | The generic template definition | `template <typename T> class Stack` |
| **Specialization Priority** | Specializations are chosen over primary template | More specific = higher priority |

**Syntax:**
```cpp
// Primary template
template <typename T>
class Printer {
public:
    void print(const T& value) {
        cout << "Generic: " << value << endl;
    }
};

// Full specialization for bool
template <>
class Printer<bool> {
public:
    void print(const bool& value) {
        cout << "Boolean: " << (value ? "true" : "false") << endl;
    }
};

// Full specialization for string
template <>
class Printer<string> {
public:
    void print(const string& value) {
        cout << "String: \"" << value << "\"" << endl;
    }
};

// Partial specialization for pointers
template <typename T>
class Printer<T*> {
public:
    void print(T* value) {
        cout << "Pointer: " << (value ? *value : 0) << endl;
    }
};

// Usage
int main() {
    Printer<int> p1;      // Generic
    p1.print(42);
    
    Printer<bool> p2;     // Specialized for bool
    p2.print(true);
    
    Printer<string> p3;   // Specialized for string
    p3.print("Hello");
    
    int x = 100;
    Printer<int*> p4;     // Partial specialization for pointers
    p4.print(&x);
}
```

---

## 4. Variadic Templates

This topic explains variadic templates (C++11) that accept a variable number of template arguments.

**File:** [04_Variadic_Templates.md](04_Variadic_Templates.md)

**What you will learn:**
- What are variadic templates (C++11)
- Syntax for template parameter pack (`typename... Args`)
- Syntax for function parameter pack (`Args... args`)
- Recursive expansion of parameter packs
- Fold expressions (C++17)
- Use cases (printf-style functions, tuple implementation, perfect forwarding)

**Key Concepts:**

| Concept | Description | Example |
|---------|-------------|---------|
| **Parameter Pack** | Variable number of template parameters | `typename... Args` |
| **Function Parameter Pack** | Variable number of function parameters | `Args... args` |
| **Pack Expansion** | Expanding pack with `...` | `func(args)...` |
| **Fold Expression** | Binary operation over pack (C++17) | `(args + ...)` |

**Syntax:**
```cpp
// Base case for recursion (no arguments)
void print() {
    cout << endl;
}

// Variadic template with recursion
template <typename T, typename... Args>
void print(T first, Args... rest) {
    cout << first << " ";
    print(rest...);  // Recursive call with rest
}

// Using fold expression (C++17)
template <typename... Args>
void printFold(Args... args) {
    ((cout << args << " "), ...);  // Fold expression
    cout << endl;
}

// Creating a tuple-like structure
template <typename... Types>
class MyTuple {
    // Implementation using recursive inheritance
};

// Perfect forwarding with variadic templates
template <typename T, typename... Args>
T* createObject(Args&&... args) {
    return new T(forward<Args>(args)...);
}

// Usage
int main() {
    print(1, 2.5, "hello", 'A');
    // Output: 1 2.5 hello A
    
    printFold(10, 20, 30, 40);
    // Output: 10 20 30 40
    
    // Creating object with forwarded arguments
    string* s = createObject<string>("Hello World");
    cout << *s << endl;
    delete s;
}
```

---

## 5. Template Metaprogramming

This topic explains template metaprogramming for compile-time computations.

**File:** [05_Template_Metaprogramming.md](05_Template_Metaprogramming.md)

**What you will learn:**
- What is template metaprogramming (TMP)
- Compile-time computations using templates
- Type traits (`is_pointer`, `is_integral`, etc.)
- SFINAE (Substitution Failure Is Not An Error)
- `static_assert` for compile-time checks
- `constexpr` vs template metaprogramming
- Common TMP applications (factorial, Fibonacci, type selection)

**Key Concepts:**

| Concept | Description | Example |
|---------|-------------|---------|
| **Compile-Time Computation** | Calculations performed at compile time | `Factorial<5>::value` |
| **Type Traits** | Compile-time type properties | `is_integral<int>::value` |
| **SFINAE** | Failed substitutions are not errors | Enable/disable templates |
| **constexpr** | Compile-time functions (C++11) | `constexpr int square(int x)` |

**Syntax:**
```cpp
// Compile-time factorial
template <int N>
struct Factorial {
    static constexpr int value = N * Factorial<N - 1>::value;
};

template <>
struct Factorial<0> {
    static constexpr int value = 1;
};

// Compile-time Fibonacci
template <int N>
struct Fibonacci {
    static constexpr int value = Fibonacci<N - 1>::value + Fibonacci<N - 2>::value;
};

template <>
struct Fibonacci<0> {
    static constexpr int value = 0;
};

template <>
struct Fibonacci<1> {
    static constexpr int value = 1;
};

// Type traits - checking if type is pointer
template <typename T>
struct IsPointer {
    static constexpr bool value = false;
};

template <typename T>
struct IsPointer<T*> {
    static constexpr bool value = true;
};

// SFINAE - enable only for integral types
template <typename T>
typename enable_if<is_integral<T>::value, T>::type
half(T value) {
    return value / 2;
}

// Using constexpr (modern alternative)
constexpr int factorial(int n) {
    return (n <= 1) ? 1 : n * factorial(n - 1);
}

// Usage
int main() {
    cout << "Factorial<5>::value = " << Factorial<5>::value << endl;     // 120
    cout << "Fibonacci<10>::value = " << Fibonacci<10>::value << endl;   // 55
    cout << "IsPointer<int>::value = " << IsPointer<int>::value << endl; // false
    cout << "IsPointer<int*>::value = " << IsPointer<int*>::value << endl; // true
    
    cout << "half(10) = " << half(10) << endl;     // 5
    // half(3.14);  // Error - not integral type
    
    cout << "constexpr factorial(5) = " << factorial(5) << endl;  // 120
    
    static_assert(Factorial<5>::value == 120, "Factorial calculation error");
    static_assert(factorial(5) == 120, "constexpr factorial error");
}
```

---

## 6. Theoretical Foundations

This topic covers the theoretical concepts behind templates and generic programming.

**File:** [Theory.md](Theory.md)

**What you will learn:**
- Generic programming paradigm
- Compile-time vs runtime polymorphism
- Template instantiation mechanism
- Two-phase name lookup
- Template compilation model
- Concepts (C++20)
- Trade-offs of templates (code bloat, compile time)

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Generic Programming** | Writing code that works with any type |
| **Compile-Time Polymorphism** | Polymorphism resolved at compile time via templates |
| **Template Instantiation** | Compiler generates code for each template instantiation |
| **Two-Phase Lookup** | Names are looked up in two phases (definition and instantiation) |
| **Code Bloat** | Multiple instantiations increase binary size |
| **Concepts** | C++20 feature for constraining template parameters |

---

### Prerequisites

Before starting this section, you should have completed:

- [01. Basics](../../01.%20Basics/README.md) - Functions, classes, pointers
- [02_Classes_and_Objects/README.md](../02_Classes_and_Objects/README.md) - Class basics
- [06_Polymorphism/README.md](../06_Polymorphism/README.md) - Polymorphism concepts

---

### Sample Template Code

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Function template
template <typename T>
T getMax(T a, T b) {
    return (a > b) ? a : b;
}

// Class template
template <typename T, int size = 10>
class Array {
private:
    T data_[size];
    
public:
    T& operator[](int index) {
        if (index < 0 || index >= size) {
            throw out_of_range("Index out of bounds");
        }
        return data_[index];
    }
    
    int getSize() const { return size; }
};

// Template specialization
template <>
class Array<bool, 10> {
    // Specialized implementation for bool
};

int main() {
    // Function template usage
    cout << getMax(10, 20) << endl;       // T deduced as int
    cout << getMax(3.14, 2.71) << endl;   // T deduced as double
    cout << getMax('A', 'Z') << endl;     // T deduced as char
    
    // Class template usage
    Array<int, 5> intArray;
    intArray[0] = 100;
    cout << intArray[0] << endl;
    
    Array<string> stringArray;  // size defaults to 10
    stringArray[0] = "Hello";
    cout << stringArray[0] << endl;
    
    return 0;
}
```

---

### Learning Path

```
Level 1: Basic Templates
├── Function Templates
├── Class Templates
└── Non-Type Template Parameters

Level 2: Template Specialization
├── Full Specialization
├── Partial Specialization
└── Function Template Specialization

Level 3: Advanced Templates
├── Variadic Templates (C++11)
├── Template Metaprogramming
└── Type Traits

Level 4: Modern C++ Templates
├── Fold Expressions (C++17)
├── Concepts (C++20)
└── constexpr Templates
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Defining templates in .cpp files | Define templates in header files |
| Forgetting `typename` for dependent types | Use `typename` before dependent types |
| Template code bloat | Factor common code into non-template functions |
| Complicated template syntax | Use type aliases (`using`) for readability |
| Mixing compile-time and runtime | Understand what happens at compile time |
| Not using `constexpr` when possible | Use `constexpr` for compile-time computations |

---

### Practice Questions

After completing this section, you should be able to:

1. Write a function template that swaps two values of any type
2. Create a class template for a generic Stack data structure
3. Specialize a template for a specific type (e.g., `bool`)
4. Use variadic templates to create a function that prints any number of arguments
5. Implement compile-time factorial using template metaprogramming
6. Use `static_assert` to enforce type constraints
7. Explain the difference between `typename` and `class` in template parameters
8. Understand when to use function templates vs function overloading

---

### Next Steps

- Go to [Theory.md](Theory.md) to understand the basics of this module.