# Theory.md

## Modern C++ OOP Features - Theoretical Foundations

### Overview

Modern C++ refers to the evolution of the C++ language starting with C++11, which introduced a paradigm shift in how C++ is written. These features emphasize type safety, resource management, performance, and expressiveness. This document covers the theoretical foundations of modern C++ features, their design principles, and their impact on object-oriented programming.

---

### 1. Evolution of C++ Standards

| Standard | Year | Key Features |
|----------|------|--------------|
| **C++98** | 1998 | First standardized version, STL, RTTI |
| **C++03** | 2003 | Bug fixes, minor improvements |
| **C++11** | 2011 | Auto, lambdas, smart pointers, move semantics, constexpr |
| **C++14** | 2014 | Generic lambdas, digit separators, variable templates |
| **C++17** | 2017 | Fold expressions, structured bindings, if constexpr |
| **C++20** | 2020 | Concepts, ranges, coroutines, modules, spaceship operator |
| **C++23** | 2023 | std::expected, std::mdspan, deducing this |

---

### 2. Design Philosophy of Modern C++

**Zero-Overhead Principle (Stroustrup):**

> "What you don't use, you don't pay for. And further: What you do use, you couldn't hand-code any better."

| Principle | Implication |
|-----------|-------------|
| **Abstraction without penalty** | High-level constructs compile to efficient code |
| **Type safety** | Catch errors at compile time, not runtime |
| **Resource safety** | RAII ensures no leaks |
| **Performance** | No unnecessary overhead |

**The C++11 Evolution Goals:**

| Goal | Description |
|------|-------------|
| **Make C++ easier to teach and learn** | Simplify common tasks |
| **Improve type safety** | Reduce unsafe casts and conversions |
| **Improve performance** | Enable move semantics, constexpr |
| **Make C++ more consistent** | Uniform initialization, auto |
| **Improve concurrency support** | Thread library, atomics |

---

### 3. Type Deduction Theory

**auto Type Deduction Rules:**

| Initializer Type | Deduced Type |
|-----------------|--------------|
| `auto x = expr;` | Type of expr (cv-qualifiers removed) |
| `auto& x = expr;` | Reference to expr's type |
| `const auto& x = expr;` | const reference |
| `auto&& x = expr;` | Forwarding reference |

**decltype Type Deduction Rules:**

| Expression | decltype Result |
|------------|-----------------|
| Variable name | Type of variable |
| Lvalue expression (parenthesized) | Lvalue reference |
| Function call | Return type of function |
| Rvalue expression | Type of expression |

**Example:**
```cpp
int x = 10;
const int y = 20;

auto a = x;      // int (const removed)
auto& b = x;     // int&
const auto& c = y; // const int&
decltype(x) d;   // int
decltype((x)) e; // int& (parenthesized)
```

---

### 4. Move Semantics and Rvalue References

**Value Categories in C++11:**

```
Expression
    │
    ├── glvalue (generalized lvalue)
    │       ├── lvalue (has identity, cannot be moved)
    │       └── xvalue (expiring value, can be moved)
    │
    └── rvalue (can be moved)
            ├── xvalue (expiring value)
            └── prvalue (pure rvalue, temporary)
```

**Key Distinctions:**

| Category | Has Identity | Can be Moved | Examples |
|----------|--------------|--------------|----------|
| **lvalue** | Yes | No | Variables, function names |
| **xvalue** | Yes | Yes | `std::move(x)`, `arr[n]` |
| **prvalue** | No | Yes | Literals, temporaries |

**Move Semantics Theory:**

| Concept | Description |
|---------|-------------|
| **Move Constructor** | Transfers resources from source to new object |
| **Move Assignment** | Transfers resources from source to existing object |
| **Source State** | Left in valid but unspecified state (usually empty) |
| **Noexcept** | Move operations should be noexcept for optimal performance |

---

### 5. Lambda Expressions Theory

**Lambda Closure Type:**

Each lambda expression generates a unique, unnamed function object type (closure type).

| Component | Description |
|-----------|-------------|
| **Captured Variables** | Stored as data members in closure object |
| **Call Operator** | `operator()` is const by default (unless mutable) |
| **Conversion to Function Pointer** | Only for non-capturing lambdas |

**Capture Categories:**

| Capture | Effect |
|---------|--------|
| `[&]` | Capture all by reference |
| `[=]` | Capture all by value |
| `[a, &b]` | Capture a by value, b by reference |
| `[this]` | Capture this pointer |
| `[*this]` (C++17) | Capture *this by value |

**Lifetime Considerations:**

| Capture Type | Lifetime Risk | Solution |
|--------------|---------------|----------|
| **By reference** | Dangling reference | Ensure captured variables outlive lambda |
| **By value** | Copy overhead | Acceptable for small types |
| **`this` capture** | Object destruction | Ensure object outlives lambda |

---

### 6. Smart Pointers Theory

**Ownership Models:**

| Model | Description | C++ Implementation |
|-------|-------------|-------------------|
| **No ownership** | Observer, no deletion responsibility | Raw pointer, reference |
| **Exclusive ownership** | Single owner, unique responsibility | `std::unique_ptr` |
| **Shared ownership** | Multiple owners, last one deletes | `std::shared_ptr` |
| **Weak ownership** | Non-owning observer, breaks cycles | `std::weak_ptr` |

**Control Block (shared_ptr):**

```
shared_ptr Control Block
┌─────────────────────────┐
│ strong ref count        │  (number of shared_ptr owners)
├─────────────────────────┤
│ weak ref count          │  (number of weak_ptr observers)
├─────────────────────────┤
│ deleter (function ptr)  │  (custom deletion strategy)
├─────────────────────────┤
│ allocator (optional)    │  (custom memory allocator)
└─────────────────────────┘
```

**Performance Characteristics:**

| Operation | unique_ptr | shared_ptr | weak_ptr |
|-----------|------------|------------|----------|
| **Size** | 8 bytes (same as raw) | 16 bytes (two pointers) | 16 bytes |
| **Construction** | O(1) | O(1) + control block | O(1) |
| **Copy** | Not allowed | O(1) + atomic increment | O(1) + atomic increment |
| **Destruction** | O(1) | O(1) + atomic decrement | O(1) + atomic decrement |
| **Dereference** | O(1) | O(1) | O(1) (after lock) |

---

### 7. Perfect Forwarding Theory

**The Forwarding Problem:**

```cpp
template <typename T>
void wrapper(T&& arg) {
    // Want to call func with same value category as arg
    func(arg);  // Always passes as lvalue
    func(std::move(arg));  // Always passes as rvalue
}
```

**Solution: std::forward**

| Rule | Description |
|------|-------------|
| **std::forward<T>(arg)** | Casts arg to T&& |
| **Reference Collapsing** | `T& &` collapses to `T&` |
| **Universal Reference** | `T&&` where T is deduced |

**Reference Collapsing Rules:**

| Original | Collapsed |
|----------|-----------|
| `T& &` | `T&` |
| `T& &&` | `T&` |
| `T&& &` | `T&` |
| `T&& &&` | `T&&` |

**Perfect Forwarding Implementation:**

```cpp
template <typename T>
void wrapper(T&& arg) {
    // Forward preserves value category
    func(std::forward<T>(arg));
}
```

---

### 8. Uniform Initialization Theory

**Problems with Old Initialization Syntax:**

| Problem | Description |
|---------|-------------|
| **Narrowing conversions** | Allowed silently |
| **Most vexing parse** | `Widget w();` declares function |
| **Inconsistent syntax** | Different syntax for different types |

**Uniform Initialization Solution:**

| Feature | Description |
|---------|-------------|
| **Braced initialization** | `T{args...}` |
| **Narrowing prevention** | Compile-time error |
| **Initializer list constructors** | `std::initializer_list<T>` |
| **Aggregate initialization** | Works with arrays and aggregates |

**Initialization Priority:**

```
1. Initializer list constructor (if matches)
2. Regular constructor
3. Aggregate initialization
```

---

### 9. constexpr Theory

**constexpr vs const:**

| Aspect | const | constexpr |
|--------|-------|-----------|
| **Evaluation time** | Runtime | Compile time (or runtime) |
| **Initialization** | At runtime | Must be constant expression |
| **Function calls** | No | Yes (C++11 limited, C++14 expanded) |
| **Variables** | Can be initialized at runtime | Must be initialized at compile time |

**constexpr Function Requirements (C++14):**

| Requirement | Description |
|-------------|-------------|
| **Body** | Can have loops, multiple statements |
| **Parameters** | Must be literal types |
| **Return type** | Must be literal type |
| **No static/thread_local** | Not allowed |
| **No goto** | Not allowed |
| **No try-catch** | Not allowed (except for consteval) |

---

### 10. Concepts Theory (C++20)

**Problems with Traditional Templates:**

| Problem | Description |
|---------|-------------|
| **Error messages** | Long, cryptic errors when constraints violated |
| **No intent documentation** | Template requirements not explicit |
| **Overload resolution** | Difficult to constrain templates |

**Concept Solution:**

| Feature | Description |
|---------|-------------|
| **Named requirements** | Concepts document template constraints |
| **Early checking** | Constraints checked before instantiation |
| **Better errors** | Clear, readable error messages |
| **Overload resolution** | Concepts participate in overload resolution |

**Concept vs requires Clause:**

| Approach | Syntax | Use Case |
|----------|--------|----------|
| **Concept** | `template <Integral T>` | Most common, readable |
| **Requires clause** | `template <typename T> requires Integral<T>` | Complex constraints |
| **Trailing requires** | `auto add(T a, T b) requires Integral<T>` | After function declaration |

---

### 11. RAII Evolution

**Traditional RAII (C++98):**

```cpp
class Resource {
    int* data_;
public:
    Resource() : data_(new int[100]) { }
    ~Resource() { delete[] data_; }
    // Copy not implemented - resource can't be copied
};
```

**Modern RAII (C++11):**

```cpp
class Resource {
    unique_ptr<int[]> data_;
public:
    Resource() : data_(make_unique<int[]>(100)) { }
    // Default destructor works
    // Move semantics enabled automatically
};
```

**RAII + Move Semantics Benefits:**

| Benefit | Description |
|---------|-------------|
| **Automatic cleanup** | Destructor still works |
| **Move support** | Resources can be transferred |
| **No manual copy** | unique_ptr prevents accidental copy |
| **Exception safety** | No leaks during stack unwinding |

---

### 12. Performance Implications

| Feature | Overhead | When to Use |
|---------|----------|-------------|
| **auto** | Zero (compile time) | Always when type is obvious |
| **Range-based for** | Zero (same as manual loop) | Always for iteration |
| **Lambda** | Zero (function object) | Local functions, STL algorithms |
| **unique_ptr** | Zero (same as raw pointer) | Exclusive ownership |
| **shared_ptr** | Control block, atomic ops | Shared ownership |
| **move semantics** | Zero (transfer instead of copy) | Expensive-to-copy objects |
| **constexpr** | Zero (compile time) | Compile-time computations |
| **Concepts** | Zero (compile time) | Template constraints |

---

### Key Takeaways

1. **Modern C++** (C++11 onward) fundamentally changed how C++ is written
2. **Zero-overhead principle** ensures abstractions don't cost performance
3. **Type deduction** (`auto`, `decltype`) reduces verbosity while maintaining safety
4. **Move semantics** enables efficient transfer of resources
5. **Smart pointers** provide RAII for dynamic memory
6. **Lambdas** enable local function objects for algorithms
7. **Uniform initialization** provides consistent, safe initialization syntax
8. **constexpr** moves computation to compile time
9. **Concepts** (C++20) improve template error messages and constraints
10. **RAII + move semantics** enables safe, efficient resource management

---

### Next Steps

- Go to [01_Auto_and_Decltype.md](01_Auto_and_Decltype.md) to understand Auto and Decltype.