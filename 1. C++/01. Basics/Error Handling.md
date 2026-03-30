# Exception Handling in C++ - Complete Guide

## 📖 Overview

Exception handling is a powerful mechanism in C++ that allows programs to respond to exceptional conditions (errors) at runtime. It provides a structured way to handle errors, separating error-handling code from normal code flow. Exception handling uses three keywords: `try`, `catch`, and `throw`.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Exception** | An event that disrupts the normal flow of program execution |
| **throw** | Signals that an exception has occurred |
| **try** | Encloses code that might throw an exception |
| **catch** | Handles exceptions thrown in the try block |
| **Stack Unwinding** | Process of destroying local objects as exceptions propagate |

---

## 1. **Basic Exception Handling**

```cpp
#include <iostream>
#include <string>
#include <stdexcept>
using namespace std;

void divideNumbers(double a, double b) {
    if (b == 0) {
        throw runtime_error("Division by zero error!");
    }
    cout << "Result: " << a / b << endl;
}

int main() {
    cout << "=== Basic Exception Handling ===" << endl;
    
    try {
        cout << "Trying to divide 10 by 2..." << endl;
        divideNumbers(10, 2);
        
        cout << "\nTrying to divide 10 by 0..." << endl;
        divideNumbers(10, 0);
        
        cout << "This line will not execute" << endl;
    }
    catch (const runtime_error& e) {
        cout << "Caught exception: " << e.what() << endl;
    }
    
    cout << "\nProgram continues after exception handling" << endl;
    
    return 0;
}
```

**Output:**
```
=== Basic Exception Handling ===
Trying to divide 10 by 2...
Result: 5

Trying to divide 10 by 0...
Caught exception: Division by zero error!

Program continues after exception handling
```

---

## 2. **Multiple Catch Blocks**

```cpp
#include <iostream>
#include <string>
#include <stdexcept>
#include <cstring>
using namespace std;

void processValue(int value) {
    if (value < 0) {
        throw invalid_argument("Negative value not allowed!");
    }
    else if (value == 0) {
        throw runtime_error("Zero value encountered!");
    }
    else if (value > 100) {
        throw out_of_range("Value exceeds maximum limit!");
    }
    else if (value == 42) {
        throw "The answer to everything!";
    }
    else {
        cout << "Processing value: " << value << endl;
    }
}

int main() {
    cout << "=== Multiple Catch Blocks ===" << endl;
    
    int values[] = {50, -5, 0, 150, 42, 75};
    
    for (int v : values) {
        cout << "\nProcessing " << v << ":" << endl;
        try {
            processValue(v);
        }
        catch (const invalid_argument& e) {
            cout << "Invalid argument: " << e.what() << endl;
        }
        catch (const runtime_error& e) {
            cout << "Runtime error: " << e.what() << endl;
        }
        catch (const out_of_range& e) {
            cout << "Out of range: " << e.what() << endl;
        }
        catch (const char* msg) {
            cout << "String exception: " << msg << endl;
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

Processing 50:
Processing value: 50

Processing -5:
Invalid argument: Negative value not allowed!

Processing 0:
Runtime error: Zero value encountered!

Processing 150:
Out of range: Value exceeds maximum limit!

Processing 42:
String exception: The answer to everything!

Processing 75:
Processing value: 75
```

---

## 3. **Standard Exception Classes**

```cpp
#include <iostream>
#include <string>
#include <stdexcept>
#include <exception>
#include <new>
#include <typeinfo>
using namespace std;

// Standard exception hierarchy
void demonstrateStandardExceptions() {
    cout << "\n=== Standard Exception Classes ===" << endl;
    
    // 1. bad_alloc - memory allocation failure
    try {
        int* p = new int[1000000000000];
        delete[] p;
    }
    catch (const bad_alloc& e) {
        cout << "bad_alloc caught: " << e.what() << endl;
    }
    
    // 2. bad_cast - dynamic_cast failure
    class Base { virtual void f() {} };
    class Derived : public Base {};
    class Other {};
    
    try {
        Base b;
        Derived d;
        Other& o = dynamic_cast<Other&>(b);  // This will throw
    }
    catch (const bad_cast& e) {
        cout << "bad_cast caught: " << e.what() << endl;
    }
    
    // 3. bad_typeid - typeid of null pointer
    try {
        Base* p = nullptr;
        cout << typeid(*p).name() << endl;
    }
    catch (const bad_typeid& e) {
        cout << "bad_typeid caught: " << e.what() << endl;
    }
    
    // 4. out_of_range - vector access
    try {
        vector<int> vec;
        cout << vec.at(10) << endl;
    }
    catch (const out_of_range& e) {
        cout << "out_of_range caught: " << e.what() << endl;
    }
    
    // 5. invalid_argument
    try {
        int x = stoi("abc");
    }
    catch (const invalid_argument& e) {
        cout << "invalid_argument caught: " << e.what() << endl;
    }
    
    // 6. length_error
    try {
        string s;
        s.resize(s.max_size() + 1);
    }
    catch (const length_error& e) {
        cout << "length_error caught: " << e.what() << endl;
    }
}

int main() {
    demonstrateStandardExceptions();
    return 0;
}
```

---

## 4. **Custom Exception Classes**

```cpp
#include <iostream>
#include <string>
#include <exception>
#include <sstream>
using namespace std;

// Base custom exception
class MyException : public exception {
private:
    string message_;
    
public:
    MyException(const string& msg) : message_(msg) {}
    
    const char* what() const noexcept override {
        return message_.c_str();
    }
};

// Specific exception types
class FileNotFoundException : public MyException {
public:
    FileNotFoundException(const string& filename)
        : MyException("File not found: " + filename) {}
};

class PermissionDeniedException : public MyException {
public:
    PermissionDeniedException(const string& operation)
        : MyException("Permission denied for: " + operation) {}
};

class InvalidDataException : public MyException {
private:
    int lineNumber_;
    string fieldName_;
    
public:
    InvalidDataException(int line, const string& field)
        : MyException("Invalid data at line " + to_string(line) + 
                      ", field: " + field),
          lineNumber_(line), fieldName_(field) {}
    
    int getLineNumber() const { return lineNumber_; }
    string getFieldName() const { return fieldName_; }
};

class ValidationException : public exception {
private:
    string field_;
    string reason_;
    
public:
    ValidationException(const string& field, const string& reason)
        : field_(field), reason_(reason) {}
    
    const char* what() const noexcept override {
        static string msg;
        msg = "Validation failed for '" + field_ + "': " + reason_;
        return msg.c_str();
    }
    
    string getField() const { return field_; }
    string getReason() const { return reason_; }
};

// Function that throws custom exceptions
void openFile(const string& filename) {
    if (filename.empty()) {
        throw InvalidDataException(1, "filename");
    }
    if (filename == "nonexistent.txt") {
        throw FileNotFoundException(filename);
    }
    if (filename == "protected.txt") {
        throw PermissionDeniedException("read " + filename);
    }
    cout << "File opened: " << filename << endl;
}

void validateUser(const string& username, const string& password) {
    if (username.length() < 3) {
        throw ValidationException("username", "Minimum length is 3 characters");
    }
    if (password.length() < 6) {
        throw ValidationException("password", "Minimum length is 6 characters");
    }
    if (username == password) {
        throw ValidationException("password", "Cannot be same as username");
    }
    cout << "User validated: " << username << endl;
}

int main() {
    cout << "=== Custom Exception Classes ===" << endl;
    
    // Test file operations
    cout << "\n1. File operations:" << endl;
    string files[] = {"data.txt", "", "nonexistent.txt", "protected.txt"};
    
    for (const auto& file : files) {
        try {
            openFile(file);
        }
        catch (const FileNotFoundException& e) {
            cout << "File error: " << e.what() << endl;
        }
        catch (const PermissionDeniedException& e) {
            cout << "Permission error: " << e.what() << endl;
        }
        catch (const InvalidDataException& e) {
            cout << "Data error at line " << e.getLineNumber() 
                 << ", field: " << e.getFieldName() << endl;
        }
    }
    
    // Test user validation
    cout << "\n2. User validation:" << endl;
    struct User {
        string username;
        string password;
    };
    
    User users[] = {
        {"alice", "secret123"},
        {"bo", "pass"},
        {"bob", "bob12345"},
        {"charlie", "charlie"}
    };
    
    for (const auto& user : users) {
        try {
            validateUser(user.username, user.password);
        }
        catch (const ValidationException& e) {
            cout << "Validation failed: " << e.what() << endl;
            cout << "  Field: " << e.getField() << endl;
            cout << "  Reason: " << e.getReason() << endl;
        }
    }
    
    return 0;
}
```

---

## 5. **Exception Specifications (Deprecated) and noexcept**

```cpp
#include <iostream>
#include <string>
#include <stdexcept>
using namespace std;

// C++11: noexcept specifier
void noThrowFunction() noexcept {
    cout << "This function guarantees no exceptions" << endl;
}

void mayThrowFunction() {
    cout << "This function may throw exceptions" << endl;
    throw runtime_error("Something went wrong!");
}

// noexcept operator - compile-time check
template<typename T>
void callFunction(T func) {
    if constexpr (noexcept(func())) {
        cout << "Function is noexcept - can optimize" << endl;
        func();
    } else {
        cout << "Function may throw - need try-catch" << endl;
        try {
            func();
        }
        catch (const exception& e) {
            cout << "Caught: " << e.what() << endl;
        }
    }
}

// noexcept(false) - explicitly stating it can throw
void canThrow() noexcept(false) {
    throw runtime_error("Throwing as expected");
}

// Function that should never throw
int safeDivide(int a, int b) noexcept {
    if (b == 0) {
        // This will terminate the program if called
        // Use with caution!
        terminate();
    }
    return a / b;
}

int main() {
    cout << "=== Exception Specifications (noexcept) ===" << endl;
    
    cout << "\n1. noexcept functions:" << endl;
    noThrowFunction();
    
    cout << "\n2. noexcept operator:" << endl;
    callFunction(noThrowFunction);
    callFunction(mayThrowFunction);
    
    cout << "\n3. noexcept(false):" << endl;
    try {
        canThrow();
    }
    catch (const exception& e) {
        cout << "Caught: " << e.what() << endl;
    }
    
    cout << "\n4. noexcept guarantees:" << endl;
    cout << "noexcept(noThrowFunction): " << noexcept(noThrowFunction()) << endl;
    cout << "noexcept(mayThrowFunction): " << noexcept(mayThrowFunction()) << endl;
    
    // Warning: This will terminate!
    // cout << "\n5. Dangerous safeDivide:" << endl;
    // safeDivide(10, 0);
    
    return 0;
}
```

---

## 6. **Stack Unwinding and RAII**

```cpp
#include <iostream>
#include <string>
#include <stdexcept>
using namespace std;

class Resource {
private:
    string name_;
    
public:
    Resource(const string& name) : name_(name) {
        cout << "Resource " << name_ << " acquired" << endl;
    }
    
    ~Resource() {
        cout << "Resource " << name_ << " released" << endl;
    }
    
    void use() {
        cout << "Using resource " << name_ << endl;
    }
};

class FileHandle {
private:
    FILE* file_;
    string filename_;
    
public:
    FileHandle(const string& filename) : filename_(filename) {
        file_ = fopen(filename.c_str(), "w");
        if (!file_) {
            throw runtime_error("Cannot open file: " + filename);
        }
        cout << "File opened: " << filename << endl;
    }
    
    ~FileHandle() {
        if (file_) {
            fclose(file_);
            cout << "File closed: " << filename_ << endl;
        }
    }
    
    void write(const string& data) {
        if (file_) {
            fprintf(file_, "%s\n", data.c_str());
        }
    }
};

class DatabaseConnection {
private:
    string connectionString_;
    bool connected_;
    
public:
    DatabaseConnection(const string& conn) : connectionString_(conn), connected_(false) {
        cout << "Database connection object created" << endl;
    }
    
    void connect() {
        if (!connected_) {
            // Simulate connection
            connected_ = true;
            cout << "Connected to " << connectionString_ << endl;
        }
    }
    
    ~DatabaseConnection() {
        if (connected_) {
            cout << "Disconnected from " << connectionString_ << endl;
        }
        cout << "Database connection object destroyed" << endl;
    }
    
    void query(const string& sql) {
        if (!connected_) {
            throw runtime_error("Not connected to database");
        }
        cout << "Executing: " << sql << endl;
    }
};

void complexOperation() {
    Resource r1("Resource1");
    Resource r2("Resource2");
    
    FileHandle file("data.txt");
    file.write("Starting operation");
    
    DatabaseConnection db("postgresql://localhost/mydb");
    db.connect();
    db.query("BEGIN TRANSACTION");
    
    // Simulate error
    throw runtime_error("Operation failed!");
    
    db.query("COMMIT");
    file.write("Operation completed");
}

void nestedFunction() {
    Resource r("NestedResource");
    cout << "In nested function" << endl;
    complexOperation();
}

int main() {
    cout << "=== Stack Unwinding and RAII ===" << endl;
    
    cout << "\n1. Normal operation (no exception):" << endl;
    try {
        FileHandle file("normal.txt");
        file.write("Normal data");
    }
    catch (const exception& e) {
        cout << "Exception: " << e.what() << endl;
    }
    
    cout << "\n2. Exception with RAII (automatic cleanup):" << endl;
    try {
        nestedFunction();
    }
    catch (const exception& e) {
        cout << "\nCaught exception: " << e.what() << endl;
    }
    
    cout << "\n3. Stack unwinding demonstration:" << endl;
    cout << "   Resources are destroyed in reverse order of construction" << endl;
    cout << "   Files, mutexes, database connections are automatically cleaned up" << endl;
    
    return 0;
}
```

---

## 7. **Function try Blocks**

```cpp
#include <iostream>
#include <string>
#include <stdexcept>
using namespace std;

class Base {
private:
    int* data_;
    
public:
    Base(int size) try : data_(new int[size]) {
        cout << "Base constructor: allocating " << size << " ints" << endl;
        if (size < 0) {
            throw invalid_argument("Size cannot be negative");
        }
    }
    catch (const exception& e) {
        cout << "Base constructor caught: " << e.what() << endl;
        throw;  // Re-throw
    }
    
    ~Base() {
        delete[] data_;
        cout << "Base destructor" << endl;
    }
};

class Derived : public Base {
private:
    int* extraData_;
    
public:
    Derived(int size, int extra) 
    try : Base(size), extraData_(new int[extra]) {
        cout << "Derived constructor: allocating " << extra << " ints" << endl;
        if (extra < 0) {
            throw invalid_argument("Extra size cannot be negative");
        }
    }
    catch (const exception& e) {
        cout << "Derived constructor caught: " << e.what() << endl;
        // extraData_ is not yet initialized here
        throw;
    }
    
    ~Derived() {
        delete[] extraData_;
        cout << "Derived destructor" << endl;
    }
};

class Member {
private:
    string name_;
    
public:
    Member(const string& name) : name_(name) {
        cout << "Member " << name_ << " constructed" << endl;
        if (name.empty()) {
            throw runtime_error("Empty name not allowed");
        }
    }
    
    ~Member() {
        cout << "Member " << name_ << " destroyed" << endl;
    }
};

class Container {
private:
    Member m1_;
    Member m2_;
    
public:
    Container(const string& name1, const string& name2)
    try : m1_(name1), m2_(name2) {
        cout << "Container constructed" << endl;
    }
    catch (const exception& e) {
        cout << "Container constructor caught: " << e.what() << endl;
        // Members that were constructed are destroyed automatically
        throw;
    }
    
    ~Container() {
        cout << "Container destroyed" << endl;
    }
};

int main() {
    cout << "=== Function try Blocks ===" << endl;
    
    cout << "\n1. Successful construction:" << endl;
    try {
        Derived d(10, 5);
        cout << "Derived object created successfully" << endl;
    }
    catch (const exception& e) {
        cout << "Main caught: " << e.what() << endl;
    }
    
    cout << "\n2. Construction failure (Base throws):" << endl;
    try {
        Derived d(-5, 10);
        cout << "This won't be printed" << endl;
    }
    catch (const exception& e) {
        cout << "Main caught: " << e.what() << endl;
    }
    
    cout << "\n3. Construction failure (Derived throws):" << endl;
    try {
        Derived d(10, -5);
        cout << "This won't be printed" << endl;
    }
    catch (const exception& e) {
        cout << "Main caught: " << e.what() << endl;
    }
    
    cout << "\n4. Member initialization with try block:" << endl;
    try {
        Container c("First", "");
        cout << "Container created" << endl;
    }
    catch (const exception& e) {
        cout << "Main caught: " << e.what() << endl;
    }
    
    return 0;
}
```

---

## 8. **Exception Safety Levels**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

// Basic guarantee: No resource leaks, object in valid state
class BasicGuarantee {
private:
    int* data_;
    size_t size_;
    
public:
    BasicGuarantee(size_t size) : size_(size) {
        data_ = new int[size];
        for (size_t i = 0; i < size; i++) {
            data_[i] = i;
        }
    }
    
    // Basic guarantee: If exception occurs, no leak, object valid
    void resize(size_t newSize) {
        int* newData = new int[newSize];
        try {
            size_t copySize = min(size_, newSize);
            for (size_t i = 0; i < copySize; i++) {
                newData[i] = data_[i];
            }
            delete[] data_;
            data_ = newData;
            size_ = newSize;
        }
        catch (...) {
            delete[] newData;
            throw;
        }
    }
    
    ~BasicGuarantee() {
        delete[] data_;
    }
};

// Strong guarantee: Commit or rollback
class StrongGuarantee {
private:
    vector<int> data_;
    
public:
    StrongGuarantee(initializer_list<int> list) : data_(list) {}
    
    // Strong guarantee: Either succeeds or leaves object unchanged
    void addElement(int value) {
        vector<int> temp = data_;  // Copy
        temp.push_back(value);      // Modify copy
        data_.swap(temp);           // Commit (no-throw)
    }
    
    void display() const {
        for (int x : data_) cout << x << " ";
        cout << endl;
    }
};

// No-throw guarantee: Always succeeds
class NoThrowGuarantee {
private:
    int* data_;
    size_t size_;
    
public:
    NoThrowGuarantee(size_t size) : size_(size) {
        data_ = new (nothrow) int[size];
        if (!data_) {
            throw bad_alloc();
        }
    }
    
    // No-throw guarantee: Swap is noexcept
    void swap(NoThrowGuarantee& other) noexcept {
        std::swap(data_, other.data_);
        std::swap(size_, other.size_);
    }
    
    ~NoThrowGuarantee() {
        delete[] data_;
    }
};

// Exception-safe assignment (copy-and-swap idiom)
class SafeAssignment {
private:
    string name_;
    int* data_;
    size_t size_;
    
public:
    SafeAssignment(const string& name, size_t size) 
        : name_(name), size_(size), data_(new int[size]) {}
    
    // Copy-and-swap: Strong guarantee
    SafeAssignment& operator=(SafeAssignment other) noexcept {
        swap(other);
        return *this;
    }
    
    void swap(SafeAssignment& other) noexcept {
        std::swap(name_, other.name_);
        std::swap(data_, other.data_);
        std::swap(size_, other.size_);
    }
    
    ~SafeAssignment() {
        delete[] data_;
    }
};

int main() {
    cout << "=== Exception Safety Levels ===" << endl;
    
    cout << "\n1. Basic Guarantee:" << endl;
    BasicGuarantee bg(5);
    try {
        bg.resize(1000000000);  // May throw bad_alloc
    }
    catch (const exception& e) {
        cout << "Exception: " << e.what() << endl;
        // bg is still valid, no memory leak
    }
    
    cout << "\n2. Strong Guarantee:" << endl;
    StrongGuarantee sg{1, 2, 3};
    cout << "Before: ";
    sg.display();
    
    try {
        sg.addElement(4);
        cout << "After success: ";
        sg.display();
    }
    catch (...) {
        cout << "After failure: ";
        sg.display();  // Unchanged
    }
    
    cout << "\n3. No-throw Guarantee:" << endl;
    NoThrowGuarantee nt1(10);
    NoThrowGuarantee nt2(20);
    nt1.swap(nt2);  // Guaranteed not to throw
    
    cout << "\n4. Exception Safety Levels:" << endl;
    cout << "   Basic: No leaks, object in valid state" << endl;
    cout << "   Strong: Commit or rollback" << endl;
    cout << "   No-throw: Never throws exceptions" << endl;
    
    return 0;
}
```

---

## 📊 Exception Handling Summary

| Concept | Description |
|---------|-------------|
| **try** | Block where exceptions are monitored |
| **catch** | Block that handles specific exception types |
| **throw** | Signals that an exception has occurred |
| **noexcept** | Function guarantees no exceptions |
| **Stack Unwinding** | Automatic destruction of local objects |

---

## ✅ Best Practices

1. **Throw by value, catch by const reference**
2. **Use standard exception classes when possible**
3. **Create custom exceptions for application-specific errors**
4. **Use RAII for automatic resource management**
5. **Provide strong exception safety guarantee when possible**
6. **Mark functions that don't throw as noexcept**
7. **Never throw exceptions from destructors**

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Catching by value** | Object slicing | Catch by const reference |
| **Empty catch block** | Swallowing exceptions | At least log the error |
| **Throwing from destructor** | Program termination | Log errors, don't throw |
| **Memory leak in constructor** | Resource leak | Use RAII for members |

---

## ✅ Key Takeaways

1. **Exception handling** separates error handling from normal code
2. **Stack unwinding** ensures proper cleanup
3. **RAII** is essential for exception safety
4. **Standard exceptions** cover common error scenarios
5. **Custom exceptions** provide application-specific error information
6. **noexcept** enables compiler optimizations
7. **Exception safety levels** guide robust design