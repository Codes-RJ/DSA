# 31_exception - Exception Handling Utilities

The `exception` header is the foundation of C++'s standard error-handling hierarchy. It defines the base exception types and the machinery for throwing, catching, and inspecting runtime errors.

## 📖 Overview

C++ exception handling is built on three keywords — `try`, `throw`, `catch` — and a hierarchy of classes rooted at `std::exception`. The `<exception>` header provides that root class, while `<stdexcept>` provides the commonly-used derived types.

Benefits of using exceptions over error codes:
- Errors cannot be silently ignored
- Error-handling code is separated from normal logic
- Constructors and operators can signal failure
- Stack unwinding guarantees destructor calls (RAII)

## 🎯 Key Components

### Standard Exception Hierarchy
```
std::exception
├── std::logic_error        (programming bugs, detectable before runtime)
│   ├── std::invalid_argument
│   ├── std::domain_error
│   ├── std::length_error
│   └── std::out_of_range
├── std::runtime_error      (runtime conditions)
│   ├── std::range_error
│   ├── std::overflow_error
│   └── std::underflow_error
├── std::bad_alloc          (new fails to allocate memory)
├── std::bad_cast           (dynamic_cast fails on a reference)
├── std::bad_typeid         (typeid applied to null pointer)
└── std::bad_exception
```

### Key Functions in `<exception>`
- `what()` — returns a C-string description of the exception
- `std::terminate()` — called when an exception is uncaught
- `std::current_exception()` — captures the current exception (C++11)
- `std::rethrow_exception()` — re-throws a captured exception (C++11)
- `std::exception_ptr` — smart pointer to an exception object (C++11)

## 🔧 Basic Operations

### Throwing and Catching Standard Exceptions
```cpp
#include <exception>
#include <stdexcept>
#include <iostream>

int divide(int a, int b) {
    if (b == 0)
        throw std::invalid_argument("Division by zero is undefined");
    return a / b;
}

int main() {
    try {
        std::cout << divide(10, 2) << "\n"; // 5
        std::cout << divide(10, 0) << "\n"; // throws
    } catch (const std::invalid_argument& e) {
        std::cerr << "Invalid argument: " << e.what() << "\n";
    } catch (const std::exception& e) {
        std::cerr << "General error: " << e.what() << "\n";
    }

    return 0;
}
```

### Multiple Catch Blocks (Specific to General)
```cpp
#include <stdexcept>
#include <iostream>

void process(int choice) {
    if (choice == 1) throw std::out_of_range("Index out of range");
    if (choice == 2) throw std::runtime_error("Runtime failure");
    if (choice == 3) throw 42; // throwing a non-exception type
}

int main() {
    for (int i = 1; i <= 4; i++) {
        try {
            process(i);
            std::cout << "Choice " << i << ": OK\n";
        } catch (const std::out_of_range& e) {
            std::cerr << "Range error: " << e.what() << "\n";
        } catch (const std::runtime_error& e) {
            std::cerr << "Runtime error: " << e.what() << "\n";
        } catch (...) {
            std::cerr << "Unknown exception caught\n";
        }
    }
    return 0;
}
```

### Custom Exception Classes
```cpp
#include <exception>
#include <string>
#include <iostream>

class DatabaseError : public std::exception {
private:
    std::string message_;
    int errorCode_;

public:
    DatabaseError(const std::string& msg, int code)
        : message_("DatabaseError [" + std::to_string(code) + "]: " + msg),
          errorCode_(code) {}

    const char* what() const noexcept override {
        return message_.c_str();
    }

    int code() const noexcept { return errorCode_; }
};

int main() {
    try {
        throw DatabaseError("Connection refused", 1001);
    } catch (const DatabaseError& e) {
        std::cerr << e.what() << "\n";
        std::cerr << "Error code: " << e.code() << "\n";
    }
    return 0;
}
```

## 🎮 Practical Examples

### Example 1: Safe Array Access
```cpp
#include <stdexcept>
#include <iostream>
#include <vector>

int safeGet(const std::vector<int>& v, int index) {
    if (index < 0 || index >= static_cast<int>(v.size()))
        throw std::out_of_range(
            "Index " + std::to_string(index) +
            " is out of range [0, " + std::to_string(v.size() - 1) + "]"
        );
    return v[index];
}

int main() {
    std::vector<int> data = {10, 20, 30};

    try {
        std::cout << safeGet(data, 1) << "\n";  // 20
        std::cout << safeGet(data, 5) << "\n";  // throws
    } catch (const std::out_of_range& e) {
        std::cerr << "Access error: " << e.what() << "\n";
    }

    return 0;
}
```

### Example 2: Exception-Safe Resource Management
```cpp
#include <stdexcept>
#include <iostream>
#include <fstream>
#include <string>

std::string readFile(const std::string& path) {
    std::ifstream file(path);
    if (!file.is_open())
        throw std::runtime_error("Cannot open file: " + path);

    std::string content, line;
    while (std::getline(file, line))
        content += line + "\n";

    return content; // file closes via RAII (destructor)
}

int main() {
    try {
        std::string content = readFile("notes.txt");
        std::cout << content;
    } catch (const std::runtime_error& e) {
        std::cerr << "File error: " << e.what() << "\n";
    }
    return 0;
}
```

### Example 3: Re-throwing and Exception Chains
```cpp
#include <stdexcept>
#include <iostream>

void innerFunction() {
    throw std::runtime_error("Database connection lost");
}

void outerFunction() {
    try {
        innerFunction();
    } catch (const std::exception& e) {
        // Wrap inner exception with additional context
        throw std::runtime_error(
            std::string("outerFunction failed: ") + e.what()
        );
    }
}

int main() {
    try {
        outerFunction();
    } catch (const std::exception& e) {
        std::cerr << e.what() << "\n";
        // Output: outerFunction failed: Database connection lost
    }
    return 0;
}
```

### Example 4: Exception-Safe Class (Strong Guarantee)
```cpp
#include <stdexcept>
#include <iostream>
#include <vector>
#include <string>

class SafeStack {
    std::vector<int> data_;

public:
    void push(int value) {
        data_.push_back(value); // vector push_back offers strong guarantee
    }

    int pop() {
        if (data_.empty())
            throw std::underflow_error("Pop from empty stack");

        int top = data_.back();
        data_.pop_back(); // noexcept
        return top;
    }

    int top() const {
        if (data_.empty())
            throw std::underflow_error("Top of empty stack");
        return data_.back();
    }

    size_t size() const noexcept { return data_.size(); }
};

int main() {
    SafeStack s;
    s.push(1);
    s.push(2);
    s.push(3);

    try {
        while (true) {
            std::cout << "Popped: " << s.pop() << "\n";
        }
    } catch (const std::underflow_error& e) {
        std::cerr << "Stack error: " << e.what() << "\n";
    }

    return 0;
}
```

## ⚡ Performance Tips

### Exception Handling Has Zero Cost When Not Triggered
```cpp
// Modern C++ uses "zero-cost exception" model:
// - In the normal path (no throw), exception handling adds NO overhead
// - Cost is only paid when an exception is actually thrown
// Use exceptions for exceptional conditions, not control flow
```

### Mark Functions `noexcept` When They Don't Throw
```cpp
int add(int a, int b) noexcept { return a + b; }
// Enables compiler optimizations and communicates intent to callers
// STL containers move elements using noexcept move constructors → faster
```

### Avoid Throwing in Destructors
```cpp
// BAD: throwing from a destructor during stack unwinding calls terminate()
class BadResource {
public:
    ~BadResource() {
        throw std::runtime_error("Oops"); // DANGEROUS
    }
};

// GOOD: catch and swallow errors in destructors
class GoodResource {
public:
    ~GoodResource() noexcept {
        try { cleanup(); } catch (...) { /* swallow */ }
    }
};
```

## 🐛 Common Pitfalls & Solutions

### 1. Catching by Value Instead of Reference
```cpp
// Bad: copying slices derived exception types (object slicing)
catch (std::exception e) { /* e loses derived info */ }

// Good: catch by const reference
catch (const std::exception& e) { std::cerr << e.what(); }
```

### 2. Catching `...` Without Re-throwing
```cpp
// Bad: swallows all exceptions silently
try { risky(); } catch (...) { /* nothing */ }

// Good: log then rethrow, or handle intentionally
try { risky(); } catch (...) {
    std::cerr << "Unexpected exception\n";
    throw; // rethrow to propagate
}
```

### 3. Using `throw` Without an Active Exception in the `catch` Block
```cpp
// Only call bare throw; inside a catch block
try {
    doSomething();
} catch (const std::exception& e) {
    log(e.what());
    throw; // re-throws the current exception — correct
}
// throw; outside a catch block calls std::terminate()
```

### 4. Ignoring `what()` Messages
```cpp
// Bad
catch (const std::exception& e) { /* silently absorbed */ }

// Good: always log or display what()
catch (const std::exception& e) {
    std::cerr << "Caught: " << e.what() << "\n";
}
```

## 🎯 Best Practices

1. **Catch by `const` reference** to avoid object slicing and unnecessary copies
2. **Order `catch` blocks from most specific to most general** — derived before base
3. **Mark `noexcept`** any function that is guaranteed not to throw
4. **Never throw from destructors** — use `noexcept` and swallow errors there
5. **Use standard exception types** from `<stdexcept>` before creating custom ones
6. **Follow exception safety guarantees**: basic (no leaks) → strong (atomic) → noexcept

## 📚 Related Headers

- [`stdexcept`](https://en.cppreference.com/w/cpp/header/stdexcept) — `runtime_error`, `logic_error`, and all derived types
- [`typeinfo.md`](32_typeinfo.md) — `std::bad_cast`, `std::bad_typeid`
- [`memory.md`](22_memory.md) — `std::bad_alloc` from failed `new`
- [`type_traits.md`](33_type_traits.md) — Compile-time checks that help avoid runtime exceptions

## 🚀 Next Steps

1. Write a custom exception hierarchy for a domain (e.g., `NetworkError`, `TimeoutError`)
2. Study the three exception safety levels: basic, strong, and no-throw
3. Learn about `std::nested_exception` for chaining exceptions (C++11)
4. Explore `std::exception_ptr` for passing exceptions across threads

---

**Examples in this file**: 4 complete programs  
**Key Types**: `std::exception`, `std::runtime_error`, `std::logic_error`, `std::out_of_range`, `std::invalid_argument`  
**Key Concepts**: `try`/`catch`/`throw`, `noexcept`, `what()`, exception safety  
**Common Use Cases**: Error propagation, input validation, resource failure handling
