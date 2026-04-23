# README.md

## Exception Handling in OOP - Complete Guide

### Overview

Exception handling is a mechanism in C++ that allows programs to respond to exceptional conditions (errors) at runtime. It provides a structured way to handle errors, separating error-handling code from normal code flow. In object-oriented programming, exception handling works seamlessly with classes, inheritance, and polymorphism, allowing for robust and maintainable error management.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [01_Try_Catch_Throw.md](01_Try_Catch_Throw.md) | understand Try, Catch, and Throw |
| 2. | [02_Standard_Exceptions.md](02_Standard_Exceptions.md) | understand Standard Exception Classes |
| 3. | [03_Custom_Exceptions.md](03_Custom_Exceptions.md) | understand Custom Exception Classes |
| 4. | [04_Exception_Specifications.md](04_Exception_Specifications.md) | understand Exception Specifications |
| 5. | [05_RAII.md](05_RAII.md) | understand Resource Acquisition Is Initialization |
| 6. | [Theory.md](Theory.md) | understand Theoretical Foundations of Exception Handling |

---

## 1. Try, Catch, and Throw

This topic explains the fundamental syntax and mechanics of exception handling in C++.

**File:** [01_Try_Catch_Throw.md](01_Try_Catch_Throw.md)

**What you will learn:**
- What are exceptions and when to use them
- Syntax of `try`, `catch`, and `throw` keywords
- How to throw exceptions of different types
- Multiple catch blocks for different exception types
- Catch-all handler (`catch(...)`)
- Rethrowing exceptions (`throw;`)
- Exception propagation through function calls

**Key Concepts:**

| Concept | Description | Example |
|---------|-------------|---------|
| **try** | Block where exceptions are monitored | `try { risky_code(); }` |
| **throw** | Signals that an exception has occurred | `throw runtime_error("Error");` |
| **catch** | Handles exceptions thrown in try block | `catch (const exception& e) { }` |
| **Rethrow** | Propagates exception to outer handler | `throw;` (no argument) |
| **Catch-all** | Handles any exception type | `catch (...) { }` |

**Syntax:**
```cpp
#include <iostream>
#include <stdexcept>
using namespace std;

void riskyFunction(int value) {
    if (value < 0) {
        throw invalid_argument("Negative value not allowed");
    }
    if (value == 0) {
        throw runtime_error("Zero value encountered");
    }
    if (value > 100) {
        throw "Value too large";  // Throwing const char*
    }
    cout << "Value is valid: " << value << endl;
}

int main() {
    try {
        riskyFunction(-5);
    }
    catch (const invalid_argument& e) {
        cout << "Invalid argument: " << e.what() << endl;
    }
    catch (const runtime_error& e) {
        cout << "Runtime error: " << e.what() << endl;
    }
    catch (const char* msg) {
        cout << "String exception: " << msg << endl;
    }
    catch (...) {
        cout << "Unknown exception caught" << endl;
    }
    
    return 0;
}
```

---

## 2. Standard Exception Classes

This topic explains the built-in exception hierarchy provided by the C++ standard library.

**File:** [02_Standard_Exceptions.md](02_Standard_Exceptions.md)

**What you will learn:**
- The `std::exception` base class hierarchy
- Standard exception classes and their purposes
- `what()` virtual function for error messages
- Exception class inheritance relationships
- When to use each standard exception type

**Key Concepts:**

| Exception Class | Purpose | Typical Use Case |
|-----------------|---------|------------------|
| **exception** | Base class for all standard exceptions | Catching any standard exception |
| **bad_alloc** | Memory allocation failure | `new` operator failure |
| **bad_cast** | Failed dynamic_cast | Invalid type conversion |
| **bad_typeid** | Null pointer in typeid | Dereferencing null in typeid |
| **logic_error** | Errors in program logic | Precondition violations |
| **domain_error** | Domain error | Mathematical domain error |
| **invalid_argument** | Invalid argument | Function argument out of range |
| **length_error** | Exceeds maximum length | String/container too large |
| **out_of_range** | Out of bounds access | Array/vector index error |
| **runtime_error** | Runtime errors | General runtime problems |
| **overflow_error** | Arithmetic overflow | Integer overflow |
| **underflow_error** | Arithmetic underflow | Floating point underflow |
| **range_error** | Range error | Value out of valid range |

**Hierarchy:**
```
exception
├── bad_alloc
├── bad_cast
├── bad_typeid
├── logic_error
│   ├── domain_error
│   ├── invalid_argument
│   ├── length_error
│   └── out_of_range
└── runtime_error
    ├── overflow_error
    ├── underflow_error
    └── range_error
```

**Syntax:**
```cpp
#include <iostream>
#include <stdexcept>
#include <vector>
#include <string>
using namespace std;

int main() {
    // bad_alloc example
    try {
        int* huge = new int[1000000000000];
        delete[] huge;
    }
    catch (const bad_alloc& e) {
        cout << "Memory allocation failed: " << e.what() << endl;
    }
    
    // out_of_range example
    try {
        vector<int> vec = {1, 2, 3};
        cout << vec.at(10) << endl;
    }
    catch (const out_of_range& e) {
        cout << "Out of range: " << e.what() << endl;
    }
    
    // invalid_argument example
    try {
        int x = stoi("abc123");
    }
    catch (const invalid_argument& e) {
        cout << "Invalid argument: " << e.what() << endl;
    }
    
    return 0;
}
```

---

## 3. Custom Exception Classes

This topic explains how to create your own exception classes by inheriting from `std::exception`.

**File:** [03_Custom_Exceptions.md](03_Custom_Exceptions.md)

**What you will learn:**
- Creating custom exception classes
- Inheriting from `std::exception`
- Overriding the `what()` virtual function
- Adding custom data members and methods
- Creating exception hierarchies
- Best practices for custom exceptions

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Inheritance** | Derive from `std::exception` or its derivatives |
| **what() override** | Provide meaningful error messages |
| **Additional Data** | Add error codes, line numbers, field names |
| **Noexcept Specification** | `what()` should be `noexcept` |
| **Exception Hierarchy** | Create family of related exceptions |

**Syntax:**
```cpp
#include <iostream>
#include <exception>
#include <string>
using namespace std;

// Base custom exception
class MyException : public exception {
private:
    string message_;
    
public:
    MyException(const string& msg) : message_(msg) { }
    
    const char* what() const noexcept override {
        return message_.c_str();
    }
};

// Exception with additional data
class FileException : public exception {
private:
    string filename_;
    int errorCode_;
    string message_;
    
public:
    FileException(const string& filename, int code, const string& msg)
        : filename_(filename), errorCode_(code), message_(msg) { }
    
    const char* what() const noexcept override {
        static string fullMsg;
        fullMsg = "File error [" + filename_ + "]: " + message_;
        return fullMsg.c_str();
    }
    
    string getFilename() const { return filename_; }
    int getErrorCode() const { return errorCode_; }
};

// Specific exceptions
class FileNotFoundException : public FileException {
public:
    FileNotFoundException(const string& filename)
        : FileException(filename, 404, "File not found") { }
};

class PermissionDeniedException : public FileException {
public:
    PermissionDeniedException(const string& filename)
        : FileException(filename, 403, "Permission denied") { }
};

int main() {
    try {
        throw FileNotFoundException("config.txt");
    }
    catch (const FileNotFoundException& e) {
        cout << "Error: " << e.what() << endl;
        cout << "File: " << e.getFilename() << endl;
        cout << "Code: " << e.getErrorCode() << endl;
    }
    
    return 0;
}
```

---

## 4. Exception Specifications

This topic explains exception specifications, including the deprecated throw specifier and the modern `noexcept` specifier.

**File:** [04_Exception_Specifications.md](04_Exception_Specifications.md)

**What you will learn:**
- Old-style exception specifications (`throw(type)`) - deprecated
- Modern `noexcept` specifier (C++11)
- `noexcept` operator for compile-time checks
- When to use `noexcept` (move constructors, swap, destructors)
- Exception safety guarantees

**Key Concepts:**

| Concept | Description | Example |
|---------|-------------|---------|
| **noexcept** | Function guarantees no exceptions | `void func() noexcept { }` |
| **noexcept(false)** | Function may throw | `void func() noexcept(false) { }` |
| **noexcept operator** | Compile-time check | `bool b = noexcept(func());` |
| **Conditional noexcept** | noexcept depends on condition | `void func() noexcept(noexcept(expr))` |

**Syntax:**
```cpp
#include <iostream>
#include <vector>
#include <type_traits>
using namespace std;

// Guarantees no exceptions
void safeFunction() noexcept {
    cout << "This never throws" << endl;
}

// May throw exceptions
void riskyFunction() {
    throw runtime_error("Oops!");
}

// Conditional noexcept
template <typename T>
void swapObjects(T& a, T& b) noexcept(is_nothrow_move_constructible_v<T> &&
                                       is_nothrow_move_assignable_v<T>) {
    T temp = move(a);
    a = move(b);
    b = move(temp);
}

// Move constructor should be noexcept
class Widget {
public:
    Widget(Widget&& other) noexcept {
        // Move implementation
    }
};

int main() {
    // noexcept operator
    cout << "safeFunction is noexcept: " << noexcept(safeFunction()) << endl;
    cout << "riskyFunction is noexcept: " << noexcept(riskyFunction()) << endl;
    
    // noexcept function can still throw - terminates
    // safeFunction();  // If it throws, program terminates
    
    try {
        riskyFunction();
    }
    catch (const exception& e) {
        cout << "Caught: " << e.what() << endl;
    }
    
    return 0;
}
```

---

## 5. RAII (Resource Acquisition Is Initialization)

This topic explains RAII, a fundamental C++ idiom for resource management that works hand-in-hand with exception handling.

**File:** [05_RAII.md](05_RAII.md)

**What you will learn:**
- What is RAII (Resource Acquisition Is Initialization)
- How RAII ensures exception-safe resource management
- RAII for memory management (smart pointers)
- RAII for file handles, mutexes, database connections
- Stack unwinding and automatic cleanup
- Benefits of RAII over manual resource management

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Constructor Acquires** | Resources acquired in constructor |
| **Destructor Releases** | Resources released in destructor |
| **Automatic Cleanup** | Destructor runs during stack unwinding |
| **Exception Safety** | No resource leaks even with exceptions |
| **Smart Pointers** | RAII wrappers for dynamic memory |

**Syntax:**
```cpp
#include <iostream>
#include <fstream>
#include <mutex>
using namespace std;

// RAII for file handling
class FileHandler {
private:
    FILE* file_;
    string filename_;
    
public:
    FileHandler(const string& filename, const char* mode) 
        : filename_(filename) {
        file_ = fopen(filename.c_str(), mode);
        if (!file_) {
            throw runtime_error("Cannot open file: " + filename);
        }
        cout << "File opened: " << filename << endl;
    }
    
    void write(const string& data) {
        if (file_) {
            fprintf(file_, "%s\n", data.c_str());
        }
    }
    
    ~FileHandler() {
        if (file_) {
            fclose(file_);
            cout << "File closed: " << filename_ << endl;
        }
    }
};

// RAII for mutex locking
class MutexGuard {
private:
    mutex& mtx_;
    
public:
    MutexGuard(mutex& mtx) : mtx_(mtx) {
        mtx_.lock();
        cout << "Mutex locked" << endl;
    }
    
    ~MutexGuard() {
        mtx_.unlock();
        cout << "Mutex unlocked" << endl;
    }
};

int main() {
    try {
        FileHandler file("data.txt", "w");
        file.write("Hello, World!");
        // File automatically closes even if exception occurs
    }
    catch (const exception& e) {
        cout << "Error: " << e.what() << endl;
    }
    
    mutex m;
    try {
        MutexGuard lock(m);
        // Critical section
        throw runtime_error("Exception in critical section");
        // Mutex automatically unlocked during stack unwinding
    }
    catch (const exception& e) {
        cout << "Caught: " << e.what() << endl;
    }
    
    return 0;
}
```

---

## 6. Theoretical Foundations

This topic covers the theoretical concepts behind exception handling.

**File:** [Theory.md](Theory.md)

**What you will learn:**
- Stack unwinding mechanism
- Exception safety levels (basic, strong, no-throw)
- Exception handling overhead
- When to use exceptions vs error codes
- Exception-neutral functions
- Exception handling in constructors and destructors

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Stack Unwinding** | Automatic destruction of local objects during exception propagation |
| **Basic Guarantee** | No resource leaks, object in valid state |
| **Strong Guarantee** | Commit or rollback (transactional) |
| **No-throw Guarantee** | Operation never throws exceptions |
| **Exception Neutral** | Function passes exceptions through without handling |

---

### Prerequisites

Before starting this section, you should have completed:

- [01. Basics](../../01.%20Basics/README.md) - Functions, pointers, references
- [02_Classes_and_Objects/README.md](../02_Classes_and_Objects/README.md) - Class basics
- [03_Constructors_and_Destructors/README.md](../03_Constructors_and_Destructors/README.md) - Object lifecycle
- [05_Inheritance/README.md](../05_Inheritance/README.md) - Inheritance concepts

---

### Sample Exception Handling Code

```cpp
#include <iostream>
#include <stdexcept>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

// RAII class for resource management
class DatabaseConnection {
private:
    string connectionString_;
    bool connected_;
    
public:
    DatabaseConnection(const string& conn) 
        : connectionString_(conn), connected_(false) {
        // Simulate connection
        connected_ = true;
        cout << "Connected to: " << conn << endl;
    }
    
    void query(const string& sql) {
        if (!connected_) {
            throw runtime_error("Not connected to database");
        }
        cout << "Executing: " << sql << endl;
    }
    
    ~DatabaseConnection() {
        if (connected_) {
            cout << "Disconnected from: " << connectionString_ << endl;
        }
    }
};

// Function demonstrating exception safety
void processData(const string& filename, const string& sql) {
    DatabaseConnection db("localhost:5432");
    ifstream file(filename);
    
    if (!file.is_open()) {
        throw runtime_error("Cannot open file: " + filename);
    }
    
    db.query(sql);
    // File automatically closed, DB automatically disconnected
}

int main() {
    try {
        processData("data.txt", "SELECT * FROM users");
    }
    catch (const ifstream::failure& e) {
        cout << "File error: " << e.what() << endl;
    }
    catch (const runtime_error& e) {
        cout << "Runtime error: " << e.what() << endl;
    }
    catch (const exception& e) {
        cout << "Exception: " << e.what() << endl;
    }
    catch (...) {
        cout << "Unknown exception" << endl;
    }
    
    return 0;
}
```

---

### Learning Path

```
Level 1: Basic Exception Handling
├── Try, Catch, Throw
├── Multiple Catch Blocks
└── Catch-All Handler

Level 2: Standard and Custom Exceptions
├── Standard Exception Classes
├── Custom Exception Classes
└── Exception Hierarchies

Level 3: Exception Safety
├── Exception Specifications (noexcept)
├── RAII (Resource Acquisition Is Initialization)
└── Stack Unwinding

Level 4: Advanced Topics
├── Exception Safety Levels
├── Exception in Constructors/Destructors
└── Function Try Blocks
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Catching by value (object slicing) | Catch by const reference |
| Empty catch block | Always handle or rethrow |
| Throwing from destructor | Destructors should be noexcept |
| Memory leak in constructor | Use RAII for all resources |
| Not using RAII | Let destructors clean up automatically |
| Catching too broadly | Catch specific exceptions first |
| Swallowing exceptions with `catch(...)` | Only use when necessary |

---

### Practice Questions

After completing this section, you should be able to:

1. Write a function that throws different exceptions based on input
2. Create a custom exception class inheriting from `std::exception`
3. Explain the difference between `throw` and `throw;`
4. Implement RAII for a custom resource (file, memory, lock)
5. Mark appropriate functions as `noexcept`
6. Explain the three exception safety levels
7. Write exception-safe constructors and destructors
8. Use function try blocks for constructor initialization lists

---

### Next Steps

- Go to [Theory.md](Theory.md) to understand the basics of the module.