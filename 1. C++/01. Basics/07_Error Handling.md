
# Exception Handling in C++ - Complete Guide

## Overview

Exception handling is a powerful mechanism in C++ that allows programs to respond to exceptional conditions (errors) at runtime. It provides a structured way to handle errors, separating error-handling code from normal code flow. Exception handling uses three keywords: `try`, `catch`, and `throw`.

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Exception** | An event that disrupts the normal flow of program execution |
| **throw** | Signals that an exception has occurred |
| **try** | Encloses code that might throw an exception |
| **catch** | Handles exceptions thrown in the try block |
| **Stack Unwinding** | Process of destroying local objects as exceptions propagate |

---

## 1. Basic Exception Handling

This section demonstrates the fundamental syntax of exception handling using try, catch, and throw. The function `divideNumbers` checks for division by zero and throws an exception. The main function calls it inside a try block and catches any exception that occurs.

```cpp
#include <iostream>
#include <stdexcept>
using namespace std;

void divideNumbers(double a, double b) {
    if (b == 0) {
        throw runtime_error("Error: Division by zero!");
    }
    cout << "Result: " << a / b << endl;
}

int main() {
    cout << "=== Basic Exception Handling ===" << endl;
    
    try {
        cout << "Trying 10 / 2..." << endl;
        divideNumbers(10, 2);
        
        cout << "\nTrying 10 / 0..." << endl;
        divideNumbers(10, 0);
        
        cout << "This line will never execute" << endl;
    }
    catch (const runtime_error& e) {
        cout << "Caught exception: " << e.what() << endl;
    }
    
    cout << "\nProgram continues normally after catch block" << endl;
    
    return 0;
}
```

**Output:**
```
=== Basic Exception Handling ===
Trying 10 / 2...
Result: 5

Trying 10 / 0...
Caught exception: Error: Division by zero!

Program continues normally after catch block
```

---

## 2. Multiple Catch Blocks

This example shows how to handle different types of exceptions with separate catch blocks. The function `processValue` throws different exception types based on the input value. The main function demonstrates catching specific exception types in order (most specific to most general) and the catch-all handler `catch(...)`.

```cpp
#include <iostream>
#include <stdexcept>
#include <cstring>
using namespace std;

void processValue(int value) {
    if (value < 0) {
        throw invalid_argument("Negative values are not allowed!");
    }
    else if (value == 0) {
        throw runtime_error("Zero is not a valid input!");
    }
    else if (value > 100) {
        throw out_of_range("Value exceeds maximum limit of 100!");
    }
    else if (value == 42) {
        throw "The answer to everything!";  // Throwing a string literal
    }
    else {
        cout << "Successfully processed value: " << value << endl;
    }
}

int main() {
    cout << "=== Multiple Catch Blocks ===" << endl;
    
    int testValues[] = {50, -5, 0, 150, 42, 75};
    
    for (int val : testValues) {
        cout << "\n--- Testing value: " << val << " ---" << endl;
        
        try {
            processValue(val);
        }
        catch (const invalid_argument& e) {
            cout << "Invalid argument caught: " << e.what() << endl;
        }
        catch (const runtime_error& e) {
            cout << "Runtime error caught: " << e.what() << endl;
        }
        catch (const out_of_range& e) {
            cout << "Out of range caught: " << e.what() << endl;
        }
        catch (const char* msg) {
            cout << "String exception caught: " << msg << endl;
        }
        catch (...) {
            cout << "Unknown exception caught!" << endl;
        }
    }
    
    return 0;
}
```

**Output:**
```
=== Multiple Catch Blocks ===

--- Testing value: 50 ---
Successfully processed value: 50

--- Testing value: -5 ---
Invalid argument caught: Negative values are not allowed!

--- Testing value: 0 ---
Runtime error caught: Zero is not a valid input!

--- Testing value: 150 ---
Out of range caught: Value exceeds maximum limit of 100!

--- Testing value: 42 ---
String exception caught: The answer to everything!

--- Testing value: 75 ---
Successfully processed value: 75
```

---

## 3. Standard Exception Classes

This example demonstrates the built-in exception classes provided by the C++ standard library. Each exception type handles a specific error scenario: `bad_alloc` for memory allocation failures, `bad_cast` for failed dynamic casts, `bad_typeid` for null pointer typeid, `out_of_range` for out-of-bounds access, `invalid_argument` for invalid function arguments, and `length_error` for exceeding maximum length.

```cpp
#include <iostream>
#include <stdexcept>
#include <new>
#include <typeinfo>
#include <vector>
#include <string>
using namespace std;

class Base {
public:
    virtual void dummy() {}
};

class Derived : public Base {};

int main() {
    cout << "=== Standard Exception Classes ===" << endl;
    
    // 1. bad_alloc - when new fails to allocate memory
    cout << "\n1. bad_alloc exception:" << endl;
    try {
        // Attempt to allocate an impossibly large array
        int* hugeArray = new int[1000000000000];
        delete[] hugeArray;
    }
    catch (const bad_alloc& e) {
        cout << "bad_alloc caught: " << e.what() << endl;
    }
    
    // 2. bad_cast - when dynamic_cast fails for references
    cout << "\n2. bad_cast exception:" << endl;
    try {
        Base baseObj;
        Base& baseRef = baseObj;
        // This cast will fail because baseRef is not of type Derived
        Derived& derivedRef = dynamic_cast<Derived&>(baseRef);
        // The above line throws bad_cast
    }
    catch (const bad_cast& e) {
        cout << "bad_cast caught: " << e.what() << endl;
    }
    
    // 3. bad_typeid - when typeid is used on null pointer
    cout << "\n3. bad_typeid exception:" << endl;
    try {
        Base* nullPtr = nullptr;
        cout << typeid(*nullPtr).name() << endl;  // Throws bad_typeid
    }
    catch (const bad_typeid& e) {
        cout << "bad_typeid caught: " << e.what() << endl;
    }
    
    // 4. out_of_range - when accessing vector element out of bounds
    cout << "\n4. out_of_range exception:" << endl;
    try {
        vector<int> numbers = {1, 2, 3};
        cout << "Accessing element at index 10: ";
        cout << numbers.at(10) << endl;  // Throws out_of_range
    }
    catch (const out_of_range& e) {
        cout << "out_of_range caught: " << e.what() << endl;
    }
    
    // 5. invalid_argument - when stoi receives invalid input
    cout << "\n5. invalid_argument exception:" << endl;
    try {
        string invalidNumber = "abc123";
        int result = stoi(invalidNumber);  // Throws invalid_argument
        cout << "Converted: " << result << endl;
    }
    catch (const invalid_argument& e) {
        cout << "invalid_argument caught: " << e.what() << endl;
    }
    
    // 6. length_error - when string exceeds maximum length
    cout << "\n6. length_error exception:" << endl;
    try {
        string longString;
        // Attempt to resize beyond max_size()
        longString.resize(longString.max_size() + 1);  // Throws length_error
    }
    catch (const length_error& e) {
        cout << "length_error caught: " << e.what() << endl;
    }
    
    return 0;
}
```

---

## 4. Custom Exception Classes

This example shows how to create your own exception classes by inheriting from `std::exception`. Custom exceptions can store additional information like line numbers, field names, and provide getter methods. This allows more specific error handling in your application.

```cpp
#include <iostream>
#include <exception>
#include <string>
#include <sstream>
using namespace std;

// Base custom exception class
class MyBaseException : public exception {
private:
    string message;
    
public:
    MyBaseException(const string& msg) : message(msg) {}
    
    const char* what() const noexcept override {
        return message.c_str();
    }
};

// Specific exception for file not found
class FileNotFoundException : public MyBaseException {
public:
    FileNotFoundException(const string& filename)
        : MyBaseException("Unable to locate file: " + filename) {}
};

// Specific exception for permission denied
class PermissionDeniedException : public MyBaseException {
public:
    PermissionDeniedException(const string& resource)
        : MyBaseException("Access denied to: " + resource) {}
};

// Exception with additional data
class ValidationException : public exception {
private:
    string fieldName;
    string reason;
    int lineNumber;
    
public:
    ValidationException(const string& field, const string& msg, int line)
        : fieldName(field), reason(msg), lineNumber(line) {}
    
    const char* what() const noexcept override {
        static string fullMessage;
        fullMessage = "Validation failed at line " + to_string(lineNumber) +
                      " for field '" + fieldName + "': " + reason;
        return fullMessage.c_str();
    }
    
    string getField() const { return fieldName; }
    string getReason() const { return reason; }
    int getLine() const { return lineNumber; }
};

// Function that throws custom exceptions
void openConfigurationFile(const string& filename) {
    if (filename.empty()) {
        throw ValidationException("filename", "cannot be empty", __LINE__);
    }
    if (filename == "config.txt") {
        cout << "Successfully opened: " << filename << endl;
    }
    else if (filename == "secret.txt") {
        throw PermissionDeniedException(filename);
    }
    else {
        throw FileNotFoundException(filename);
    }
}

int main() {
    cout << "=== Custom Exception Classes ===" << endl;
    
    string files[] = {"config.txt", "", "unknown.dat", "secret.txt"};
    
    for (const string& file : files) {
        cout << "\nAttempting to open: '" << file << "'" << endl;
        
        try {
            openConfigurationFile(file);
        }
        catch (const FileNotFoundException& e) {
            cout << "File Error: " << e.what() << endl;
        }
        catch (const PermissionDeniedException& e) {
            cout << "Permission Error: " << e.what() << endl;
        }
        catch (const ValidationException& e) {
            cout << "Validation Error: " << e.what() << endl;
            cout << "  Field: " << e.getField() << endl;
            cout << "  Reason: " << e.getReason() << endl;
            cout << "  Line: " << e.getLine() << endl;
        }
        catch (const exception& e) {
            cout << "Standard exception: " << e.what() << endl;
        }
    }
    
    return 0;
}
```

**Output:**
```
=== Custom Exception Classes ===

Attempting to open: 'config.txt'
Successfully opened: config.txt

Attempting to open: ''
Validation Error: Validation failed at line XX for field 'filename': cannot be empty
  Field: filename
  Reason: cannot be empty
  Line: XX

Attempting to open: 'unknown.dat'
File Error: Unable to locate file: unknown.dat

Attempting to open: 'secret.txt'
Permission Error: Access denied to: secret.txt
```

---

## 5. noexcept Specifier

This example explains the `noexcept` specifier introduced in C++11. Functions marked `noexcept` guarantee they will not throw exceptions, which allows compilers to optimize code. The `noexcept` operator checks at compile time whether a function can throw.

```cpp
#include <iostream>
#include <stdexcept>
using namespace std;

// Function that guarantees no exceptions
void safeFunction() noexcept {
    cout << "This function will never throw an exception" << endl;
}

// Function that may throw exceptions
void riskyFunction() {
    cout << "This function may throw..." << endl;
    throw runtime_error("Something went wrong!");
}

// Function with conditional noexcept
template<typename T>
void processData(const T& data) noexcept(noexcept(data)) {
    cout << "Processing data..." << endl;
}

// noexcept operator example
void demonstrateNoexceptOperator() {
    cout << "\n--- noexcept operator ---" << endl;
    
    cout << "safeFunction() is noexcept: " << noexcept(safeFunction()) << endl;
    cout << "riskyFunction() is noexcept: " << noexcept(riskyFunction()) << endl;
    cout << "int() is noexcept: " << noexcept(int()) << endl;
    cout << "string() is noexcept: " << noexcept(string()) << endl;
}

int main() {
    cout << "=== noexcept Specifier ===" << endl;
    
    // Calling noexcept function
    safeFunction();
    
    // Demonstrating noexcept operator
    demonstrateNoexceptOperator();
    
    // Function that may throw - requires try-catch
    try {
        riskyFunction();
    }
    catch (const exception& e) {
        cout << "Caught exception: " << e.what() << endl;
    }
    
    // Note: If a noexcept function throws, program terminates
    // This is usually undesirable
    
    return 0;
}
```

**Output:**
```
=== noexcept Specifier ===
This function will never throw an exception

--- noexcept operator ---
safeFunction() is noexcept: 1
riskyFunction() is noexcept: 0
int() is noexcept: 1
string() is noexcept: 1
This function may throw...
Caught exception: Something went wrong!
```

---

## 6. Stack Unwinding and RAII

This section demonstrates RAII (Resource Acquisition Is Initialization), a fundamental C++ idiom where resources are tied to object lifetimes. When an exception occurs, the stack unwinds and all local objects are destroyed automatically. This ensures proper cleanup of resources even when exceptions are thrown.

```cpp
#include <iostream>
#include <fstream>
#include <stdexcept>
using namespace std;

// RAII class for file handling
class FileHandler {
private:
    FILE* filePtr;
    string filename;
    
public:
    FileHandler(const string& name) : filename(name) {
        cout << "Opening file: " << filename << endl;
        filePtr = fopen(filename.c_str(), "w");
        if (!filePtr) {
            throw runtime_error("Failed to open file: " + filename);
        }
    }
    
    void write(const string& data) {
        if (filePtr) {
            fprintf(filePtr, "%s\n", data.c_str());
            cout << "Wrote to file: " << data << endl;
        }
    }
    
    ~FileHandler() {
        if (filePtr) {
            fclose(filePtr);
            cout << "Closed file: " << filename << endl;
        }
    }
};

// RAII class for memory management
class MemoryBlock {
private:
    int* data;
    size_t size;
    
public:
    MemoryBlock(size_t sz) : size(sz) {
        cout << "Allocating " << size << " integers" << endl;
        data = new int[size];
        if (!data) {
            throw bad_alloc();
        }
    }
    
    ~MemoryBlock() {
        cout << "Deallocating " << size << " integers" << endl;
        delete[] data;
    }
};

// Function that demonstrates stack unwinding
void performRiskyOperation() {
    cout << "\n--- Entering performRiskyOperation ---" << endl;
    
    FileHandler file("output.txt");
    MemoryBlock memory(100);
    
    file.write("Starting operation");
    
    cout << "About to throw exception..." << endl;
    throw runtime_error("Operation failed unexpectedly!");
    
    // This code never executes
    file.write("Operation completed");
    cout << "Operation finished successfully" << endl;
}

int main() {
    cout << "=== Stack Unwinding and RAII ===" << endl;
    
    try {
        performRiskyOperation();
    }
    catch (const exception& e) {
        cout << "\nCaught exception: " << e.what() << endl;
    }
    
    cout << "\nProgram continues normally after exception" << endl;
    cout << "Notice that all resources were automatically cleaned up!" << endl;
    
    return 0;
}
```

**Output:**
```
=== Stack Unwinding and RAII ===

--- Entering performRiskyOperation ---
Opening file: output.txt
Allocating 100 integers
Wrote to file: Starting operation
About to throw exception...

Caught exception: Operation failed unexpectedly!
Deallocating 100 integers
Closed file: output.txt

Program continues normally after exception
Notice that all resources were automatically cleaned up!
```

---

## 7. Function Try Blocks

Function try blocks allow catching exceptions that occur during member initialization in constructors. This is especially useful for catching exceptions thrown by base class constructors or member object constructors.

```cpp
#include <iostream>
#include <stdexcept>
using namespace std;

class Resource {
private:
    int* data;
    int size;
    
public:
    Resource(int sz) : size(sz) {
        cout << "Allocating Resource of size " << size << endl;
        data = new int[size];
        if (sz < 0) {
            throw invalid_argument("Size cannot be negative");
        }
    }
    
    ~Resource() {
        cout << "Destroying Resource" << endl;
        delete[] data;
    }
};

class DatabaseConnection {
private:
    string connectionString;
    bool isConnected;
    
public:
    DatabaseConnection(const string& conn) : connectionString(conn), isConnected(false) {
        cout << "Creating DatabaseConnection to " << conn << endl;
        if (conn.empty()) {
            throw runtime_error("Empty connection string not allowed");
        }
        // Simulate connection
        isConnected = true;
        cout << "Connected to database" << endl;
    }
    
    ~DatabaseConnection() {
        if (isConnected) {
            cout << "Disconnected from database" << endl;
        }
    }
};

// Class using function try block
class Application {
private:
    Resource res;
    DatabaseConnection db;
    
public:
    Application(int size, const string& conn)
    try : res(size), db(conn) {
        cout << "Application constructor completed successfully" << endl;
    }
    catch (const exception& e) {
        cout << "Application constructor caught: " << e.what() << endl;
        // Member objects that were constructed will be destroyed automatically
        throw;  // Re-throw to let the caller know construction failed
    }
    
    ~Application() {
        cout << "Application destructor" << endl;
    }
};

int main() {
    cout << "=== Function Try Blocks ===" << endl;
    
    cout << "\n1. Successful construction:" << endl;
    try {
        Application app(100, "localhost:5432");
        cout << "Application created successfully" << endl;
    }
    catch (const exception& e) {
        cout << "Main caught: " << e.what() << endl;
    }
    
    cout << "\n2. Failed construction (invalid size):" << endl;
    try {
        Application app(-5, "localhost:5432");
        cout << "This won't be printed" << endl;
    }
    catch (const exception& e) {
        cout << "Main caught: " << e.what() << endl;
    }
    
    cout << "\n3. Failed construction (empty connection):" << endl;
    try {
        Application app(100, "");
        cout << "This won't be printed" << endl;
    }
    catch (const exception& e) {
        cout << "Main caught: " << e.what() << endl;
    }
    
    return 0;
}
```

**Output:**
```
=== Function Try Blocks ===

1. Successful construction:
Allocating Resource of size 100
Creating DatabaseConnection to localhost:5432
Connected to database
Application constructor completed successfully
Application created successfully
Destroying Resource
Disconnected from database
Application destructor

2. Failed construction (invalid size):
Allocating Resource of size -5
Application constructor caught: Size cannot be negative
Destroying Resource
Main caught: Size cannot be negative

3. Failed construction (empty connection):
Allocating Resource of size 100
Creating DatabaseConnection to 
Application constructor caught: Empty connection string not allowed
Destroying Resource
Main caught: Empty connection string not allowed
```

---

## 8. Rethrowing Exceptions

This example demonstrates how to rethrow exceptions using `throw;` without an argument. This preserves the original exception type and allows for nested error handling.

```cpp
#include <iostream>
#include <stdexcept>
using namespace std;

void logError(const string& context, const exception& e) {
    cout << "[LOG] Error in " << context << ": " << e.what() << endl;
}

void levelThree() {
    cout << "  Entering levelThree" << endl;
    throw runtime_error("Database connection timeout");
}

void levelTwo() {
    cout << " Entering levelTwo" << endl;
    try {
        levelThree();
    }
    catch (const exception& e) {
        cout << " levelTwo caught: " << e.what() << endl;
        logError("levelTwo", e);
        cout << " Rethrowing from levelTwo..." << endl;
        throw;  // Rethrow the original exception
    }
}

void levelOne() {
    cout << "Entering levelOne" << endl;
    try {
        levelTwo();
    }
    catch (const exception& e) {
        cout << "levelOne caught: " << e.what() << endl;
        logError("levelOne", e);
        cout << "Rethrowing from levelOne..." << endl;
        throw;  // Rethrow again
    }
}

int main() {
    cout << "=== Rethrowing Exceptions ===" << endl;
    
    try {
        levelOne();
    }
    catch (const runtime_error& e) {
        cout << "\nMain caught runtime_error: " << e.what() << endl;
    }
    catch (const exception& e) {
        cout << "\nMain caught generic exception: " << e.what() << endl;
    }
    
    cout << "\nNotice that the original exception type (runtime_error) is preserved" << endl;
    
    return 0;
}
```

**Output:**
```
=== Rethrowing Exceptions ===
Entering levelOne
 Entering levelTwo
  Entering levelThree
 levelTwo caught: Database connection timeout
[LOG] Error in levelTwo: Database connection timeout
 Rethrowing from levelTwo...
levelOne caught: Database connection timeout
[LOG] Error in levelOne: Database connection timeout
Rethrowing from levelOne...

Main caught runtime_error: Database connection timeout

Notice that the original exception type (runtime_error) is preserved
```

---

## Libraries Used in This File

| Header | Functions/Classes Used | Purpose |
|--------|------------------------|---------|
| `<iostream>` | `cout`, `endl` | Standard input/output operations |
| `<stdexcept>` | `runtime_error`, `invalid_argument`, `out_of_range`, `length_error`, `bad_alloc` | Standard exception classes |
| `<exception>` | `exception`, `set_terminate`, `terminate()` | Base exception class and termination handling |
| `<new>` | `bad_alloc`, `nothrow` | Memory allocation exceptions |
| `<typeinfo>` | `bad_typeid`, `typeid` | Runtime type information and exceptions |
| `<sstream>` | `stringstream` | String stream for message construction |
| `<vector>` | `vector`, `at()` | Dynamic array container with bounds checking |
| `<string>` | `string`, `to_string()` | String manipulation and conversion |
| `<fstream>` | `ifstream`, `ofstream` | File input/output operations |
| `<cstring>` | `strcpy`, `strlen` | C string functions (reference) |

---

## Exception Handling Summary

| Concept | Description |
|---------|-------------|
| **try** | Block where exceptions are monitored |
| **catch** | Block that handles specific exception types |
| **throw** | Signals that an exception has occurred |
| **throw;** | Rethrows the current exception |
| **noexcept** | Function guarantees no exceptions |
| **Stack Unwinding** | Automatic destruction of local objects |

---

## Best Practices

1. **Throw by value, catch by const reference**
2. **Use standard exception classes when possible**
3. **Create custom exceptions for application-specific errors**
4. **Use RAII for automatic resource management**
5. **Provide strong exception safety guarantee when possible**
6. **Mark functions that don't throw as `noexcept`**
7. **Never throw exceptions from destructors**
8. **Use `throw;` to rethrow, not `throw e;` (preserves type)**

---

## Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Catching by value** | Object slicing occurs | Catch by `const&` |
| **Empty catch block** | Swallows errors silently | At least log the error |
| **Throwing from destructor** | Program may terminate | Log errors, don't throw |
| **Memory leak in constructor** | Resource not freed | Use RAII for members |
| **`throw e;` instead of `throw;`** | Loses original exception type | Use `throw;` to rethrow |

---

## Key Takeaways

1. **Exception handling** separates error handling from normal code
2. **Stack unwinding** ensures proper cleanup
3. **RAII** is essential for exception safety
4. **Standard exceptions** cover common error scenarios
5. **Custom exceptions** provide application-specific error information
6. **noexcept** enables compiler optimizations
7. **Exception safety levels** guide robust design
8. **Function try blocks** catch constructor initialization errors

---

## Next Step

- Go to [Basic Problems](../02.%20Basic%20Problems/README.md) to practice what you learned till now and understand some simple algorithms.
- Must visit [Headers and Libraries](../00.%20Headers%20and%20Libraries/README.md) to understand more about the used `Libraries` in the files alongside continuation of your further chapters.
