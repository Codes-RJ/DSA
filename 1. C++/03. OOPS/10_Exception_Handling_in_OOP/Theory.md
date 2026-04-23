# Theory.md

## Exception Handling - Theoretical Foundations

### Overview

Exception handling is a language mechanism designed to handle runtime errors and exceptional conditions in a structured, controlled manner. Unlike traditional error handling using return codes, exception handling separates error detection from error handling, leading to cleaner code and more robust systems. This document covers the theoretical foundations of exception handling, its design principles, implementation mechanisms, and trade-offs.

---

### 1. The Error Handling Problem

Traditional error handling using return codes has several limitations:

| Problem | Description |
|---------|-------------|
| **Error Path Clutter** | Error checking code interspersed with normal logic |
| **Error Propagation** | Each function must manually propagate errors up the call stack |
| **Ignored Errors** | Callers can easily ignore return codes |
| **Resource Leaks** | Difficult to ensure cleanup on all error paths |
| **Type Safety** | Return codes are often integers (not type-safe) |

**Traditional Return Code Approach:**
```cpp
int processFile(const char* filename) {
    FILE* f = fopen(filename, "r");
    if (!f) return -1;  // Error
    
    int data;
    if (fread(&data, sizeof(data), 1, f) != 1) {
        fclose(f);
        return -2;  // Error
    }
    
    fclose(f);
    return data;  // Success
}

// Every caller must check return codes
int result = processFile("data.txt");
if (result < 0) {
    // Handle error
}
```

---

### 2. The Exception Handling Model

Exception handling introduces three key concepts:

| Concept | Description |
|---------|-------------|
| **Exception** | An object that represents an exceptional condition |
| **Throw** | The act of signaling that an exception has occurred |
| **Catch** | The act of handling an exception |

**Exception Handling Flow:**
```
Normal Flow:     try → function calls → function returns → catch (skip)
Exception Flow:  try → function throws → stack unwinding → catch (execute)
```

**Example:**
```cpp
try {
    // Normal execution starts here
    riskyOperation();
    // If exception thrown, control jumps to catch
    // This line never executes if exception occurs
}
catch (const exception& e) {
    // Exception handling code
}
// Execution continues here after catch
```

---

### 3. Stack Unwinding

When an exception is thrown, the runtime system performs stack unwinding:

**Definition:** Stack unwinding is the process of destroying local objects as the call stack is unwound while searching for an exception handler.

**Unwinding Process:**

```
Step 1: Exception thrown at point E
        ↓
Step 2: Runtime searches for matching catch handler
        ↓
Step 3: While searching, destructors of local objects are called
        ↓
Step 4: Handler found, control transfers to catch block
        ↓
Step 5: Execution continues after catch block
```

**Key Properties:**

| Property | Description |
|----------|-------------|
| **Automatic Destruction** | Local objects destroyed in reverse order of construction |
| **No Return** | Stack unwinding does not execute function return paths |
| **No Exception Escape** | Destructors should not throw (causes terminate) |
| **RAII Reliance** | Relies on RAII for resource cleanup |

```cpp
class Resource {
public:
    Resource() { cout << "Acquire" << endl; }
    ~Resource() { cout << "Release" << endl; }
};

void func() {
    Resource r;  // Acquire
    throw runtime_error("Error");  // Exception thrown
    // ~Resource() called during unwinding (Release)
}

int main() {
    try {
        func();
    }
    catch (...) { }
    // Output: Acquire, Release
}
```

---

### 4. Exception Safety Levels

Exception safety guarantees describe what guarantees a function provides when exceptions occur.

| Level | Guarantee | Description |
|-------|-----------|-------------|
| **No-throw** | Never throws | Operation always succeeds |
| **Strong** | Commit or rollback | Either succeeds or leaves state unchanged |
| **Basic** | No leaks, valid state | No resource leaks, object in valid state |
| **No guarantee** | Nothing guaranteed | Potential resource leaks, corrupted state |

**No-throw Guarantee:**
```cpp
void swap(int& a, int& b) noexcept {
    int temp = a;
    a = b;
    b = temp;  // No allocation, cannot throw
}
```

**Strong Guarantee (Copy-and-Swap):**
```cpp
class Widget {
    vector<int> data_;
public:
    void add(int value) {
        vector<int> temp = data_;  // Copy
        temp.push_back(value);      // Modify copy
        data_.swap(temp);           // Commit (no-throw)
    }
};
```

**Basic Guarantee:**
```cpp
void resize(size_t newSize) {
    int* newData = new int[newSize];
    // ... copy data ...
    delete[] data_;
    data_ = newData;  // If exception, newData deleted, no leak
}
```

---

### 5. Exception Handling Implementation

Most C++ compilers implement exception handling using one of two models:

**Table-Driven Model (Itanium C++ ABI):**

| Component | Description |
|-----------|-------------|
| **LSDA** | Language-Specific Data Area (exception handling tables) |
| **Call Frame Info** | Information about each function's stack frame |
| **Personality Routine** | Function that searches for handlers |
| **Unwind Library** | Performs stack unwinding |

**Overview of Table-Driven EH:**

```
Each function has an exception handling table:
┌─────────────────────────────────────┐
│  try block 1: catch typeid(A)       │
│  try block 2: catch typeid(B)       │
│  cleanup actions for local objects  │
└─────────────────────────────────────┘

When exception thrown:
1. Runtime examines current function's EH table
2. If handler found, jumps to it
3. If not, calls destructors and unwinds to caller
4. Repeats until handler found or main is unwound
```

**Performance Characteristics:**

| Operation | Cost |
|-----------|------|
| **Try block entry** | Minimal (table lookup only) |
| **No exception path** | No overhead (optimized) |
| **Exception thrown** | Significant (table search, unwinding) |
| **Code size** | Increases (EH tables) |

---

### 6. Exception Handling vs Error Codes

| Aspect | Exceptions | Error Codes |
|--------|-----------|-------------|
| **Error Path Clarity** | Clean separation | Mixed with normal code |
| **Error Propagation** | Automatic | Manual |
| **Ignored Errors** | Cannot ignore | Easily ignored |
| **Type Safety** | Type-safe | Often int/enum |
| **Performance (no error)** | No overhead | Minimal |
| **Performance (error)** | Slower | Fast |
| **Code Size** | Larger | Smaller |
| **Predictability** | Less predictable | More predictable |

**Guidelines for Choosing:**

| Scenario | Recommendation |
|----------|----------------|
| Constructors | Use exceptions (no return value) |
| Destructors | Never throw (use error codes internally) |
| Operators | Use exceptions (operator overloading) |
| Performance-critical paths | Use error codes |
| Embedded systems | Use error codes (predictability) |
| Large projects | Use exceptions (error propagation) |

---

### 7. Exception Safety in Constructors and Destructors

**Constructors:**

| Aspect | Description |
|--------|-------------|
| **No Return Value** | Cannot return error code |
| **Partial Construction** | If exception thrown, fully constructed members destroyed |
| **Member Initialization** | Use function try blocks to catch initialization errors |
| **Resource Acquisition** | Must use RAII to avoid leaks |

```cpp
class ResourceHolder {
    int* data_;
    FileHandle file_;
public:
    ResourceHolder(int size, const string& filename)
    try : data_(new int[size]), file_(filename) {
        // Constructor body
    }
    catch (const exception& e) {
        // Members constructed so far are destroyed automatically
        throw;  // Re-throw
    }
};
```

**Destructors:**

| Rule | Reason |
|------|--------|
| **Never throw from destructor** | Called during stack unwinding |
| **Terminate on double-exception** | Two active exceptions cause terminate() |
| **Mark noexcept** | Default in C++11 for destructors |
| **Log errors internally** | Handle errors without throwing |

```cpp
class SafeDestructor {
public:
    ~SafeDestructor() noexcept {
        try {
            // Risky cleanup
        }
        catch (...) {
            // Log error, but don't throw
            logError("Cleanup failed");
        }
    }
};
```

---

### 8. Exception Specifications Evolution

| Standard | Feature | Status |
|----------|---------|--------|
| **C++98** | `throw(type)` specifier | Deprecated in C++11, removed in C++17 |
| **C++11** | `noexcept` specifier | Modern replacement |
| **C++11** | `noexcept` operator | Compile-time check |
| **C++17** | `noexcept` in type system | Part of function type |

**Why `throw(type)` was deprecated:**

| Problem | Description |
|---------|-------------|
| **Runtime Checking** | Checked at runtime, not compile time |
| **Performance Overhead** | Unwinding overhead even for other exception types |
| **Unexpected Handler** | Unexpected exceptions call `unexpected()` |
| **Template Issues** | Difficult to use correctly with templates |

**Modern `noexcept` Semantics:**

```cpp
// Guarantees no exceptions
void func() noexcept { }

// Conditionally noexcept
template <typename T>
void swap(T& a, T& b) noexcept(noexcept(T(move(a)))) { }

// noexcept operator
static_assert(noexcept(func()));
```

---

### 9. Exception Handling and Polymorphism

Exceptions work seamlessly with polymorphism:

| Feature | Description |
|---------|-------------|
| **Catch by Base Class** | Catch `const exception&` for any derived exception |
| **Virtual what()** | `what()` is virtual, returns correct message |
| **Exception Hierarchies** | Create application-specific exception families |
| **Polymorphic Throw** | Throw derived, catch base |

```cpp
class MyException : public exception {
public:
    const char* what() const noexcept override {
        return "My specific error";
    }
};

try {
    throw MyException();
}
catch (const exception& e) {
    cout << e.what();  // "My specific error"
}
```

---

### 10. Exception Neutrality

An exception-neutral function does not handle exceptions but allows them to propagate.

**Properties:**

| Property | Description |
|----------|-------------|
| **No try-catch** | Does not catch exceptions |
| **No throw specification** | Does not restrict exceptions |
| **RAII compliance** | Properly cleans up resources |
| **Propagation** | Allows exceptions to pass through |

```cpp
// Exception-neutral function
void processData(const string& input) {
    FileReader reader(input);     // RAII
    vector<int> data = reader.read();  // May throw
    auto result = process(data);       // May throw
    // No catch - exceptions propagate to caller
}
```

---

### 11. Cost of Exception Handling

**Space Overhead:**

| Component | Typical Size |
|-----------|--------------|
| **Exception Handling Tables** | 5-15% of code size |
| **Stack Frame Information** | 1-4 bytes per function |
| **Personality Routine** | Shared across program |

**Time Overhead:**

| Operation | Cost |
|-----------|------|
| **Try block (no throw)** | Negligible (often 0) |
| **Function entry (EH info)** | Minimal (table lookup) |
| **Throwing exception** | Significant (unwinding) |
| **Catching exception** | Moderate (handler search) |

**Guidelines for Performance-Sensitive Code:**

| Recommendation | Reason |
|----------------|--------|
| Avoid exceptions in hot paths | Unwinding is expensive |
| Use `noexcept` where possible | Enables optimizations |
| Don't use exceptions for flow control | Not designed for normal conditions |
| Consider error codes for leaf functions | Avoid EH overhead |

---

### 12. Best Practices Summary

| Practice | Rationale |
|----------|-----------|
| **Throw by value, catch by const reference** | Avoids slicing, no copy overhead |
| **Use standard exceptions** | Consistent, well-understood hierarchy |
| **Create custom exceptions** | Application-specific error information |
| **Use RAII for resources** | Automatic cleanup during unwinding |
| **Mark functions `noexcept`** | Enables optimizations, expresses intent |
| **Never throw from destructors** | Avoids terminate during unwinding |
| **Keep exception hierarchies shallow** | Easier to maintain and understand |
| **Document exception guarantees** | Helps callers write safe code |

---

### Key Takeaways

1. **Exception handling** separates error detection from error handling
2. **Stack unwinding** automatically destroys local objects
3. **RAII** is essential for exception-safe resource management
4. **Three exception safety levels** provide different guarantees
5. **No-throw guarantee** is the strongest safety level
6. **Constructors** should use exceptions for error reporting
7. **Destructors** should never throw exceptions
8. **`noexcept`** is the modern exception specification
9. **Exceptions have costs** - space and time overhead
10. **Error codes** are still appropriate in some contexts

---

### Next Steps

- Go to [01_Try_Catch_Throw.md](01_Try_Catch_Throw.md) to understand Try, Catch, and Throw.