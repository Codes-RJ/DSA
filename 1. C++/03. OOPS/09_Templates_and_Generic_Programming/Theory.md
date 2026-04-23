# Theory.md

## Templates and Generic Programming - Theoretical Foundations

### Overview

Templates are a cornerstone of C++ programming, enabling generic programming and compile-time polymorphism. Unlike runtime polymorphism (virtual functions), templates generate code at compile time, providing performance benefits and type safety. This document covers the theoretical foundations of templates, their design principles, implementation mechanisms, and trade-offs.

---

### 1. Generic Programming Paradigm

#### Definition

Generic programming is a programming paradigm that focuses on writing algorithms and data structures that work with any data type without modification. The goal is to write code once and reuse it with different types, while maintaining type safety and performance.

**Key Principles:**

| Principle | Description |
|-----------|-------------|
| **Type Abstraction** | Algorithms operate on abstract type parameters |
| **Efficiency** | No runtime overhead compared to type-specific code |
| **Reusability** | Single implementation works with many types |
| **Type Safety** | Errors caught at compile time, not runtime |

#### Generic Programming vs Other Paradigms

| Paradigm | Abstraction Mechanism | Overhead | Flexibility |
|----------|----------------------|----------|-------------|
| **Procedural** | Functions, macros | None (macros) | Low (macros unsafe) |
| **Object-Oriented** | Virtual functions (runtime polymorphism) | Virtual table lookup | High |
| **Generic (Templates)** | Template instantiation (compile-time) | None (per type) | Very High |

---

### 2. Compile-Time vs Runtime Polymorphism

C++ offers two forms of polymorphism:

| Aspect | Compile-Time (Templates) | Runtime (Virtual Functions) |
|--------|--------------------------|----------------------------|
| **Resolution Time** | Compile time | Run time |
| **Mechanism** | Code generation | VTable dispatch |
| **Performance** | No overhead | Indirect call overhead |
| **Code Size** | Increases with each type | Single set of functions |
| **Flexibility** | Types known at compile time | Types can be dynamic |
| **Error Detection** | Compile time | Runtime (or compile time) |

**Example Comparison:**
```cpp
// Compile-time polymorphism (templates)
template <typename T>
T add(T a, T b) {
    return a + b;  // Generated for each type
}

// Runtime polymorphism (virtual functions)
class Number {
public:
    virtual double add(double b) = 0;
};

class IntNumber : public Number {
    int value_;
public:
    double add(double b) override { return value_ + b; }
};
```

---

### 3. Template Instantiation Mechanism

When the compiler encounters a template, it does not generate code immediately. Instead, code generation occurs when the template is instantiated with concrete types.

**Instantiation Process:**

```
Step 1: Template Definition
    └── Compiler parses syntax, stores template AST

Step 2: Template Usage
    └── Compiler sees Stack<int> or max<double>(a, b)

Step 3: Name Lookup (Two-Phase)
    └── Phase 1: At definition (non-dependent names)
    └── Phase 2: At instantiation (dependent names)

Step 4: Code Generation
    └── Compiler generates type-specific code

Step 5: Optimization
    └── Same as regular functions (inlining, etc.)
```

**Implicit vs Explicit Instantiation:**

| Type | Description | Example |
|------|-------------|---------|
| **Implicit** | Compiler instantiates when used | `Stack<int> s;` |
| **Explicit** | Programmer requests instantiation | `template class Stack<int>;` |
| **Extern** | Suppresses implicit instantiation | `extern template class Stack<int>;` |

---

### 4. Two-Phase Name Lookup

Template names are looked up in two phases, which is a common source of confusion.

**Phase 1: At Template Definition**
- Non-dependent names (not depending on template parameters) are looked up
- Errors are reported at this phase

**Phase 2: At Template Instantiation**
- Dependent names (depending on template parameters) are looked up
- ADL (Argument-Dependent Lookup) is applied

**Example:**
```cpp
void f(int) { cout << "f(int)" << endl; }

template <typename T>
void wrapper(T t) {
    f(t);  // Name lookup depends on T
}

void f(double) { cout << "f(double)" << endl; }

int main() {
    wrapper(42);     // Calls f(int) - found in Phase 2
    wrapper(3.14);   // Calls f(double) - found in Phase 2
}
```

---

### 5. Template Compilation Model

Unlike regular functions and classes, templates cannot be compiled separately (cannot be defined in .cpp files and used elsewhere). This is because the compiler needs to see the full definition to generate code for each instantiation.

**Traditional Compilation Model:**

| Component | Header (.h) | Source (.cpp) |
|-----------|-------------|---------------|
| **Regular Functions** | Declaration | Definition |
| **Templates** | Definition (full) | Nothing (or explicit instantiation) |

**Reasons for Header-Only Templates:**

1. Compiler needs definition to instantiate for new types
2. Separate compilation units cannot share template definitions
3. Linker would see multiple definitions (not a problem due to weak symbols)

**Solutions:**
- Define templates in headers (most common)
- Use explicit instantiation in .cpp files (for known types)
- Use `export` keyword (C++98, removed in C++11, rarely used)

---

### 6. Code Bloat and Minimization

Each template instantiation generates separate code, which can lead to binary size increase (code bloat).

**Causes of Code Bloat:**

| Cause | Description | Example |
|-------|-------------|---------|
| **Type Instantiations** | Different types generate different code | `Stack<int>`, `Stack<double>` |
| **Non-Type Parameters** | Different values generate different code | `Array<int, 10>`, `Array<int, 20>` |
| **Inline Functions** | Each instantiation inlines separately | Template functions often inline |

**Minimization Techniques:**

| Technique | Description |
|-----------|-------------|
| **Common Code Extraction** | Move type-independent code to base class |
| **Type Erasure** | Use `void*` with type-specific operations |
| **Explicit Instantiation** | Instantiate once for common types |
| **Non-Template Base** | Store data in non-template base class |

**Example - Code Bloat Reduction:**
```cpp
// Bloat - each instantiation has its own implementation
template <typename T>
class Stack {
    T* data_;
    int size_;
    int capacity_;
public:
    void push(const T& value) { /* ... */ }
};

// Reduced - type-independent code in base class
class StackBase {
protected:
    int size_;
    int capacity_;
    void* data_;
public:
    void push(void* value);
    void* pop();
};

template <typename T>
class Stack : private StackBase {
public:
    void push(const T& value) {
        StackBase::push(const_cast<void*>(static_cast<const void*>(&value)));
    }
    T pop() {
        return *static_cast<T*>(StackBase::pop());
    }
};
```

---

### 7. SFINAE (Substitution Failure Is Not An Error)

SFINAE is a principle that prevents substitution failures from causing compilation errors. Instead, the candidate is simply removed from the overload set.

**Principle:** When substituting template parameters fails, that specialization is discarded rather than causing a compilation error.

**Use Cases:**
- Enable/disable templates based on type properties
- Detect type capabilities at compile time
- Implement type traits

**Example:**
```cpp
// Only enabled for integral types
template <typename T>
typename enable_if<is_integral<T>::value, T>::type
half(T value) {
    return value / 2;
}

// Only enabled for floating-point types
template <typename T>
typename enable_if<is_floating_point<T>::value, T>::type
half(T value) {
    return value / 2.0;
}

int main() {
    cout << half(10) << endl;    // Calls integral version (5)
    cout << half(3.14) << endl;  // Calls floating-point version (1.57)
    // half("string");           // Error - no matching function
}
```

---

### 8. Type Traits

Type traits are template metaprogramming utilities that provide information about types at compile time.

**Categories of Type Traits:**

| Category | Examples |
|----------|----------|
| **Primary Type** | `is_void`, `is_integral`, `is_floating_point`, `is_pointer` |
| **Composite Type** | `is_array`, `is_enum`, `is_class`, `is_function` |
| **Type Properties** | `is_const`, `is_volatile`, `is_trivial`, `is_polymorphic` |
| **Type Relationships** | `is_same`, `is_base_of`, `is_convertible` |
| **Type Modifications** | `remove_const`, `add_pointer`, `make_signed`, `decay` |

**Implementation of a Simple Type Trait:**
```cpp
// Primary template (false by default)
template <typename T>
struct is_pointer {
    static constexpr bool value = false;
};

// Partial specialization for pointers (true)
template <typename T>
struct is_pointer<T*> {
    static constexpr bool value = true;
};

// Usage
static_assert(is_pointer<int>::value == false);
static_assert(is_pointer<int*>::value == true);
```

---

### 9. Concepts (C++20)

Concepts are a C++20 feature that allows specifying requirements on template parameters, improving error messages and code clarity.

**Key Benefits:**

| Benefit | Description |
|---------|-------------|
| **Clear Error Messages** | Replace template substitution errors with readable constraints |
| **Overloading on Concepts** | Different implementations for different type categories |
| **Code Documentation** | Concepts document template requirements |
| **Constraint Checking** | Compiler checks requirements before instantiation |

**Example:**
```cpp
// C++20 concept definition
template <typename T>
concept Numeric = is_integral_v<T> || is_floating_point_v<T>;

template <typename T>
concept Incrementable = requires(T a) {
    ++a;
    a++;
};

// Using concepts in templates
template <Numeric T>
T add(T a, T b) {
    return a + b;  // Only numeric types allowed
}

template <Incrementable T>
T increment(T value) {
    return ++value;
}

int main() {
    add(10, 20);        // OK - int is Numeric
    add(3.14, 2.71);    // OK - double is Numeric
    // add("hello", "world");  // Error - string not Numeric
    
    int x = 5;
    increment(x);       // OK - int is Incrementable
    
    return 0;
}
```

---

### 10. Template Metaprogramming (TMP)

Template metaprogramming is a technique that uses templates to perform computations at compile time.

**Capabilities:**

| Capability | Description | Example |
|------------|-------------|---------|
| **Compile-Time Arithmetic** | Calculate values at compile time | `Factorial<5>::value` |
| **Type Computations** | Create new types from existing ones | `remove_pointer<T>::type` |
| **Conditional Types** | Select type based on condition | `conditional<cond, T, F>::type` |
| **Recursion** | Recursive template instantiations | `Fibonacci<N>::value` |

**Limitations:**

| Limitation | Description |
|------------|-------------|
| **Readability** | Complex TMP code is hard to understand |
| **Compile Time** | Deep recursion increases compilation time |
| **Debugging** | Difficult to debug template errors |
| **Recursion Depth** | Compiler limits recursion depth (usually 1024) |

**Modern Alternatives:**
- `constexpr` functions (C++11, improved in C++14/17/20)
- `if constexpr` (C++17)
- Concepts (C++20)

---

### 11. Template Specialization Hierarchy

When multiple templates match, the compiler selects the most specialized one.

**Priority Order (from highest to lowest):**

```
1. Full specialization (exact match)
2. Partial specialization (pattern match)
3. Primary template (generic)
```

**Example:**
```cpp
// Primary template (most general)
template <typename T, typename U>
struct Pair { };

// Partial specialization (both same type)
template <typename T>
struct Pair<T, T> { };

// Full specialization (int, int)
template <>
struct Pair<int, int> { };

// Which one is chosen?
Pair<int, int> p1;      // Full specialization
Pair<int, double> p2;   // Primary template
Pair<double, double> p3; // Partial specialization
```

---

### 12. Trade-offs and Best Practices

**Advantages of Templates:**

| Advantage | Description |
|-----------|-------------|
| **Type Safety** | Errors caught at compile time |
| **Performance** | No runtime overhead |
| **Reusability** | Write once, use with any type |
| **Flexibility** | Works with user-defined types |

**Disadvantages of Templates:**

| Disadvantage | Description |
|--------------|-------------|
| **Code Bloat** | Multiple instantiations increase binary size |
| **Compile Time** | Templates increase compilation time |
| **Error Messages** | Template errors are notoriously hard to read |
| **Header-Only** | Definitions must be visible to all users |
| **Debugging** | Cannot step into template code easily |

**Best Practices:**

| Practice | Description |
|----------|-------------|
| **Define in Headers** | Templates must be defined in header files |
| **Use `typename` for Dependent Types** | `typename T::value_type` |
| **Prefer `constexpr` for Computations** | More readable than TMP |
| **Use Concepts (C++20)** | Better error messages and constraints |
| **Minimize Code Bloat** | Factor common code into non-template functions |
| **Document Requirements** | Clearly state what types must support |

---

### Key Takeaways

1. **Templates** enable generic programming and compile-time polymorphism
2. **Compile-time polymorphism** has no runtime overhead but increases binary size
3. **Two-phase lookup** separates name resolution into definition and instantiation phases
4. **Templates must be defined in headers** (except with explicit instantiation)
5. **Code bloat** can be minimized by extracting type-independent code
6. **SFINAE** allows conditional template selection based on type properties
7. **Type traits** provide compile-time information about types
8. **Concepts (C++20)** improve template error messages and constraints
9. **Template metaprogramming** performs computations at compile time
10. **`constexpr`** is often a better alternative to TMP for value computations

---

### Next Steps

- Go to [01_Function_Templates.md](01_Function_Templates.md) to understand Function Templates.