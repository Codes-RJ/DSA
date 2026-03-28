# Exception Handling in OOP - Complete Guide

## 📖 Overview

Exception handling is a powerful mechanism in C++ that allows you to manage runtime errors in a structured and elegant way. In object-oriented programming, exceptions provide a way to handle error conditions that disrupt the normal flow of program execution, enabling robust and maintainable code.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Exception** | An object that represents an error condition |
| **Try Block** | Code block where exceptions might occur |
| **Catch Block** | Code that handles specific exceptions |
| **Throw** | Statement that raises an exception |
| **Exception Hierarchy** | Inheritance structure for exception types |
| **RAII** | Resource Acquisition Is Initialization pattern |

---

## 🔄 Exception Handling Flow

```cpp
try {
    // Code that might throw an exception
    riskyOperation();
} catch (const ExceptionType& e) {
    // Handle the exception
    handleException(e);
} catch (...) {
    // Handle any other exception
    handleUnknownException();
}
```

---

## 1. **Basic Exception Handling**

```cpp
#include <iostream>
#include <stdexcept>
#include <string>
using namespace std;

// Function that might throw an exception
double divide(double a, double b) {
    if (b == 0.0) {
        throw runtime_error("Division by zero!");
    }
    return a / b;
}

// Function with multiple exception types
void processValue(int value) {
    if (value < 0) {
        throw invalid_argument("Value cannot be negative");
    } else if (value > 100) {
        throw out_of_range("Value exceeds maximum limit");
    } else if (value == 42) {
        throw "The answer to everything!"; // String literal exception
    }
    cout << "Processing value: " << value << endl;
}

int main() {
    cout << "=== Basic Exception Handling ===" << endl;
    
    // Example 1: Basic try-catch
    try {
        double result = divide(10.0, 2.0);
        cout << "10 / 2 = " << result << endl;
        
        result = divide(10.0, 0.0); // This will throw
        cout << "This line won't execute" << endl;
    } catch (const runtime_error& e) {
        cout << "Caught runtime_error: " << e.what() << endl;
    }
    
    cout << endl;
    
    // Example 2: Multiple catch blocks
    try {
        processValue(50);
        processValue(-5); // This will throw
    } catch (const invalid_argument& e) {
        cout << "Caught invalid_argument: " << e.what() << endl;
    } catch (const out_of_range& e) {
        cout << "Caught out_of_range: " << e.what() << endl;
    } catch (const char* e) {
        cout << "Caught string literal: " << e << endl;
    }
    
    cout << endl;
    
    // Example 3: Catch-all handler
    try {
        processValue(42); // Throws string literal
    } catch (const invalid_argument& e) {
        cout << "Invalid argument: " << e.what() << endl;
    } catch (const out_of_range& e) {
        cout << "Out of range: " << e.what() << endl;
    } catch (...) {
        cout << "Caught unknown exception type" << endl;
    }
    
    return 0;
}
```

---

## 2. **Custom Exception Classes**

```cpp
#include <iostream>
#include <string>
#include <exception>
using namespace std;

// Base custom exception class
class ApplicationException : public exception {
private:
    string message;
    
public:
    ApplicationException(const string& msg) : message(msg) {}
    
    const char* what() const noexcept override {
        return message.c_str();
    }
};

// Specific exception classes
class FileNotFoundException : public ApplicationException {
public:
    FileNotFoundException(const string& filename) 
        : ApplicationException("File not found: " + filename) {}
};

class PermissionDeniedException : public ApplicationException {
public:
    PermissionDeniedException(const string& resource)
        : ApplicationException("Permission denied: " + resource) {}
};

class NetworkException : public ApplicationException {
private:
    int errorCode;
    
public:
    NetworkException(const string& msg, int code) 
        : ApplicationException(msg), errorCode(code) {}
    
    int getErrorCode() const { return errorCode; }
};

// File handler class with custom exceptions
class FileHandler {
private:
    string filename;
    bool isOpen;
    
public:
    FileHandler(const string& name) : filename(name), isOpen(false) {}
    
    void open() {
        if (filename.empty()) {
            throw FileNotFoundException("empty filename");
        }
        
        if (filename == "restricted.txt") {
            throw PermissionDeniedException(filename);
        }
        
        if (filename == "network.txt") {
            throw NetworkException("Network connection failed", 404);
        }
        
        isOpen = true;
        cout << "File " << filename << " opened successfully" << endl;
    }
    
    void close() {
        if (isOpen) {
            cout << "File " << filename << " closed" << endl;
            isOpen = false;
        }
    }
    
    void read() {
        if (!isOpen) {
            throw ApplicationException("File is not open");
        }
        cout << "Reading from " << filename << endl;
    }
    
    ~FileHandler() {
        try {
            close();
        } catch (...) {
            // Destructor should not throw
        }
    }
};

int main() {
    cout << "=== Custom Exception Classes ===" << endl;
    
    // Test normal operation
    try {
        FileHandler file("data.txt");
        file.open();
        file.read();
        file.close();
    } catch (const exception& e) {
        cout << "Exception: " << e.what() << endl;
    }
    
    cout << endl;
    
    // Test file not found
    try {
        FileHandler file("");
        file.open();
    } catch (const FileNotFoundException& e) {
        cout << "File not found: " << e.what() << endl;
    } catch (const exception& e) {
        cout << "Other exception: " << e.what() << endl;
    }
    
    cout << endl;
    
    // Test permission denied
    try {
        FileHandler file("restricted.txt");
        file.open();
    } catch (const PermissionDeniedException& e) {
        cout << "Permission denied: " << e.what() << endl;
    } catch (const exception& e) {
        cout << "Other exception: " << e.what() << endl;
    }
    
    cout << endl;
    
    // Test network exception
    try {
        FileHandler file("network.txt");
        file.open();
    } catch (const NetworkException& e) {
        cout << "Network error: " << e.what() << endl;
        cout << "Error code: " << e.getErrorCode() << endl;
    } catch (const exception& e) {
        cout << "Other exception: " << e.what() << endl;
    }
    
    return 0;
}
```

---

## 3. **Exception Hierarchy and Inheritance**

```cpp
#include <iostream>
#include <string>
#include <exception>
#include <stdexcept>
using namespace std;

// Exception hierarchy
class ShapeException : public exception {
protected:
    string message;
    
public:
    ShapeException(const string& msg) : message(msg) {}
    const char* what() const noexcept override { return message.c_str(); }
};

class InvalidDimensionException : public ShapeException {
private:
    double dimension;
    
public:
    InvalidDimensionException(const string& dim, double value)
        : ShapeException("Invalid dimension for " + dim + ": " + to_string(value)), 
          dimension(value) {}
    
    double getInvalidDimension() const { return dimension; }
};

class InsufficientAreaException : public ShapeException {
private:
    double requiredArea;
    double actualArea;
    
public:
    InsufficientAreaException(double required, double actual)
        : ShapeException("Insufficient area: required " + to_string(required) + 
                        ", actual " + to_string(actual)),
          requiredArea(required), actualArea(actual) {}
    
    double getRequiredArea() const { return requiredArea; }
    double getActualArea() const { return actualArea; }
};

// Base shape class
class Shape {
protected:
    string name;
    
public:
    Shape(const string& n) : name(n) {}
    virtual ~Shape() = default;
    
    virtual double getArea() const = 0;
    virtual void validate() const = 0;
    
    const string& getName() const { return name; }
};

class Circle : public Shape {
private:
    double radius;
    
public:
    Circle(double r) : Shape("Circle"), radius(r) {
        validate();
    }
    
    double getArea() const override {
        return 3.14159 * radius * radius;
    }
    
    void validate() const override {
        if (radius <= 0) {
            throw InvalidDimensionException("radius", radius);
        }
    }
    
    double getRadius() const { return radius; }
};

class Rectangle : public Shape {
private:
    double width, height;
    
public:
    Rectangle(double w, double h) : Shape("Rectangle"), width(w), height(h) {
        validate();
    }
    
    double getArea() const override {
        return width * height;
    }
    
    void validate() const override {
        if (width <= 0) {
            throw InvalidDimensionException("width", width);
        }
        if (height <= 0) {
            throw InvalidDimensionException("height", height);
        }
    }
    
    double getWidth() const { return width; }
    double getHeight() const { return height; }
};

// Shape factory with exception handling
class ShapeFactory {
public:
    static unique_ptr<Shape> createCircle(double radius) {
        return make_unique<Circle>(radius);
    }
    
    static unique_ptr<Shape> createRectangle(double width, double height) {
        return make_unique<Rectangle>(width, height);
    }
    
    static unique_ptr<Shape> createSquare(double side) {
        return make_unique<Rectangle>(side, side);
    }
};

// Area validator
class AreaValidator {
public:
    static void validateMinimumArea(const Shape& shape, double minArea) {
        double actualArea = shape.getArea();
        if (actualArea < minArea) {
            throw InsufficientAreaException(minArea, actualArea);
        }
    }
};

int main() {
    cout << "=== Exception Hierarchy and Inheritance ===" << endl;
    
    vector<unique_ptr<Shape>> shapes;
    
    // Create valid shapes
    try {
        shapes.push_back(ShapeFactory::createCircle(5.0));
        shapes.push_back(ShapeFactory::createRectangle(4.0, 6.0));
        shapes.push_back(ShapeFactory::createSquare(3.0));
        
        cout << "Created valid shapes:" << endl;
        for (const auto& shape : shapes) {
            cout << shape->getName() << " area: " << shape->getArea() << endl;
        }
    } catch (const ShapeException& e) {
        cout << "Shape creation failed: " << e.what() << endl;
    }
    
    cout << endl;
    
    // Test invalid dimension
    try {
        auto invalidCircle = ShapeFactory::createCircle(-2.0);
    } catch (const InvalidDimensionException& e) {
        cout << "Invalid dimension: " << e.what() << endl;
        cout << "Invalid value: " << e.getInvalidDimension() << endl;
    } catch (const ShapeException& e) {
        cout << "Other shape exception: " << e.what() << endl;
    }
    
    cout << endl;
    
    // Test area validation
    try {
        auto smallCircle = ShapeFactory::createCircle(1.0);
        AreaValidator::validateMinimumArea(*smallCircle, 10.0);
    } catch (const InsufficientAreaException& e) {
        cout << "Area validation failed: " << e.what() << endl;
        cout << "Required: " << e.getRequiredArea() << ", Actual: " << e.getActualArea() << endl;
    } catch (const ShapeException& e) {
        cout << "Other shape exception: " << e.what() << endl;
    }
    
    cout << endl;
    
    // Exception handling with polymorphism
    cout << "Polymorphic exception handling:" << endl;
    vector<function<void()>> tests = {
        []() { throw InvalidDimensionException("radius", -1.0); },
        []() { throw InsufficientAreaException(100.0, 50.0); },
        []() { throw runtime_error("Runtime error"); }
    };
    
    for (size_t i = 0; i < tests.size(); i++) {
        try {
            tests[i]();
        } catch (const ShapeException& e) {
            cout << "Test " << i + 1 << ": Shape exception - " << e.what() << endl;
        } catch (const exception& e) {
            cout << "Test " << i + 1 << ": Standard exception - " << e.what() << endl;
        }
    }
    
    return 0;
}
```

---

## 4. **RAII and Exception Safety**

```cpp
#include <iostream>
#include <memory>
#include <vector>
#include <fstream>
using namespace std;

// RAII class for file handling
class FileWrapper {
private:
    FILE* file;
    
public:
    FileWrapper(const string& filename, const string& mode) {
        file = fopen(filename.c_str(), mode.c_str());
        if (!file) {
            throw runtime_error("Failed to open file: " + filename);
        }
        cout << "File opened: " << filename << endl;
    }
    
    ~FileWrapper() {
        if (file) {
            fclose(file);
            cout << "File closed" << endl;
        }
    }
    
    void write(const string& data) {
        if (file) {
            fprintf(file, "%s\n", data.c_str());
        }
    }
    
    string readLine() {
        if (!file) return "";
        
        char buffer[256];
        if (fgets(buffer, sizeof(buffer), file)) {
            return string(buffer);
        }
        return "";
    }
    
    // Prevent copying
    FileWrapper(const FileWrapper&) = delete;
    FileWrapper& operator=(const FileWrapper&) = delete;
    
    // Allow moving
    FileWrapper(FileWrapper&& other) noexcept : file(other.file) {
        other.file = nullptr;
    }
    
    FileWrapper& operator=(FileWrapper&& other) noexcept {
        if (this != &other) {
            if (file) fclose(file);
            file = other.file;
            other.file = nullptr;
        }
        return *this;
    }
};

// RAII class for database connection
class DatabaseConnection {
private:
    string connectionString;
    bool connected;
    
public:
    DatabaseConnection(const string& connStr) : connectionString(connStr), connected(false) {
        // Simulate connection
        if (connStr == "invalid") {
            throw runtime_error("Invalid connection string");
        }
        connected = true;
        cout << "Database connected: " << connectionString << endl;
    }
    
    ~DatabaseConnection() {
        if (connected) {
            cout << "Database disconnected" << endl;
            connected = false;
        }
    }
    
    void executeQuery(const string& query) {
        if (!connected) {
            throw runtime_error("Not connected to database");
        }
        
        if (query == "error") {
            throw runtime_error("Query execution failed");
        }
        
        cout << "Executing query: " << query << endl;
    }
    
    void commit() {
        if (!connected) {
            throw runtime_error("Cannot commit: not connected");
        }
        cout << "Transaction committed" << endl;
    }
    
    void rollback() {
        if (!connected) {
            throw runtime_error("Cannot rollback: not connected");
        }
        cout << "Transaction rolled back" << endl;
    }
};

// Exception-safe transaction manager
class TransactionManager {
private:
    DatabaseConnection& db;
    bool committed;
    
public:
    TransactionManager(DatabaseConnection& connection) 
        : db(connection), committed(false) {}
    
    ~TransactionManager() {
        if (!committed) {
            try {
                db.rollback();
                cout << "Auto-rollback on destruction" << endl;
            } catch (...) {
                // Destructor should not throw
            }
        }
    }
    
    void commit() {
        db.commit();
        committed = true;
    }
    
    void execute(const string& query) {
        db.executeQuery(query);
    }
};

// Exception-safe data processor
class DataProcessor {
private:
    vector<unique_ptr<FileWrapper>> files;
    DatabaseConnection db;
    
public:
    DataProcessor(const string& dbConn) : db(dbConn) {}
    
    void addFile(const string& filename) {
        files.emplace_back(make_unique<FileWrapper>(filename, "w"));
    }
    
    void processData(const string& data) {
        TransactionManager transaction(db);
        
        try {
            // Write to all files
            for (auto& file : files) {
                file->write(data);
            }
            
            // Execute database operations
            transaction.execute("INSERT INTO data VALUES ('" + data + "')");
            
            // If everything succeeds, commit
            transaction.commit();
            cout << "Data processed successfully" << endl;
            
        } catch (...) {
            cout << "Data processing failed, changes rolled back" << endl;
            throw; // Re-throw the exception
        }
    }
};

int main() {
    cout << "=== RAII and Exception Safety ===" << endl;
    
    // Example 1: Basic RAII
    cout << "Example 1: Basic RAII" << endl;
    {
        FileWrapper file("test.txt", "w");
        file.write("Hello, RAII!");
        // File automatically closed when leaving scope
    }
    cout << "File scope ended" << endl;
    
    cout << endl;
    
    // Example 2: Exception safety with RAII
    cout << "Example 2: Exception safety" << endl;
    try {
        DatabaseConnection db("localhost:5432");
        db.executeQuery("SELECT * FROM users");
        db.commit();
    } catch (const exception& e) {
        cout << "Database error: " << e.what() << endl;
    }
    cout << "Database connection scope ended" << endl;
    
    cout << endl;
    
    // Example 3: Transaction manager
    cout << "Example 3: Transaction manager" << endl;
    try {
        DatabaseConnection db("localhost:5432");
        {
            TransactionManager transaction(db);
            transaction.execute("INSERT INTO logs VALUES ('test')");
            transaction.execute("UPDATE stats SET count = count + 1");
            transaction.commit(); // Explicit commit
        }
        
        {
            TransactionManager transaction(db);
            transaction.execute("INSERT INTO logs VALUES ('test2')");
            transaction.execute("error"); // This will throw
            transaction.commit(); // Never reached
        }
    } catch (const exception& e) {
        cout << "Transaction error: " << e.what() << endl;
    }
    
    cout << endl;
    
    // Example 4: Complex data processing
    cout << "Example 4: Complex data processing" << endl;
    try {
        DataProcessor processor("localhost:5432");
        processor.addFile("output1.txt");
        processor.addFile("output2.txt");
        
        processor.processData("Sample data 1");
        processor.processData("Sample data 2");
        
    } catch (const exception& e) {
        cout << "Processing error: " << e.what() << endl;
    }
    
    cout << endl;
    
    // Example 5: Exception with invalid connection
    cout << "Example 5: Invalid connection" << endl;
    try {
        DatabaseConnection invalidDb("invalid");
    } catch (const exception& e) {
        cout << "Connection error: " << e.what() << endl;
    }
    
    return 0;
}
```

---

## 5. **Exception Specifications and noexcept**

```cpp
#include <iostream>
#include <string>
#include <exception>
#include <vector>
using namespace std;

// Function with basic exception specification (deprecated in C++11)
// void oldStyleFunction() throw(int, double) { // Deprecated
//     throw 42;
// }

// Function with noexcept specification
void noThrowFunction() noexcept {
    cout << "This function promises not to throw" << endl;
}

void functionThatThrows() {
    throw runtime_error("This function throws");
}

// Conditional noexcept
template <typename T>
void conditionalNoThrow(const T& value) noexcept(noexcept(value.toString())) {
    cout << "Conditional noexcept function" << endl;
}

// Class with noexcept methods
class SafeCalculator {
private:
    double value;
    
public:
    SafeCalculator(double v) : value(v) {}
    
    // Noexcept getter
    double getValue() const noexcept {
        return value;
    }
    
    // Noexcept setter (might throw if value is invalid)
    void setValue(double v) noexcept {
        if (v < 0) {
            // Can't throw in noexcept function, so we handle it differently
            value = 0;
            return;
        }
        value = v;
    }
    
    // Regular method that can throw
    void divideBy(double divisor) {
        if (divisor == 0.0) {
            throw invalid_argument("Division by zero");
        }
        value /= divisor;
    }
    
    // Noexcept arithmetic operations
    SafeCalculator operator+(const SafeCalculator& other) const noexcept {
        return SafeCalculator(value + other.value);
    }
    
    SafeCalculator operator*(const SafeCalculator& other) const noexcept {
        return SafeCalculator(value * other.value);
    }
};

// Exception-safe vector operations
class SafeVector {
private:
    vector<int> data;
    
public:
    void push_back(int value) noexcept {
        try {
            data.push_back(value);
        } catch (...) {
            // Handle allocation failure without throwing
            cout << "Failed to add element: memory allocation failed" << endl;
        }
    }
    
    int at(size_t index) const noexcept {
        if (index >= data.size()) {
            return -1; // Return error value instead of throwing
        }
        return data[index];
    }
    
    size_t size() const noexcept {
        return data.size();
    }
    
    void clear() noexcept {
        data.clear();
    }
};

// Function with different exception guarantees
class ExceptionGuarantees {
private:
    int* data;
    size_t size;
    
public:
    ExceptionGuarantees(size_t s) : size(s) {
        data = new int[size];
        for (size_t i = 0; i < size; i++) {
            data[i] = 0;
        }
    }
    
    // No-throw guarantee
    ~ExceptionGuarantees() noexcept {
        delete[] data;
    }
    
    // Strong guarantee
    void resize(size_t newSize) {
        int* newData = new int[newSize];
        
        // Copy existing data
        size_t copySize = min(size, newSize);
        for (size_t i = 0; i < copySize; i++) {
            newData[i] = data[i];
        }
        
        // If everything succeeded, update state
        delete[] data;
        data = newData;
        size = newSize;
    }
    
    // Basic guarantee
    void setElement(size_t index, int value) {
        if (index >= size) {
            throw out_of_range("Index out of bounds");
        }
        data[index] = value;
    }
    
    // No-throw guarantee
    size_t getSize() const noexcept {
        return size;
    }
    
    // No-throw guarantee
    int getElement(size_t index) const noexcept {
        if (index >= size) {
            return 0; // Return default value
        }
        return data[index];
    }
};

int main() {
    cout << "=== Exception Specifications and noexcept ===" << endl;
    
    // Example 1: noexcept functions
    cout << "Example 1: noexcept functions" << endl;
    noThrowFunction();
    
    try {
        functionThatThrows();
    } catch (const exception& e) {
        cout << "Caught exception: " << e.what() << endl;
    }
    
    cout << endl;
    
    // Example 2: Safe calculator
    cout << "Example 2: Safe calculator" << endl;
    SafeCalculator calc1(10.0);
    SafeCalculator calc2(5.0);
    
    cout << "Calc1 value: " << calc1.getValue() << endl;
    cout << "Calc2 value: " << calc2.getValue() << endl;
    
    SafeCalculator sum = calc1 + calc2;
    cout << "Sum: " << sum.getValue() << endl;
    
    calc1.setValue(-5.0); // Won't throw, sets to 0
    cout << "Calc1 after invalid setValue: " << calc1.getValue() << endl;
    
    try {
        calc2.divideBy(0.0);
    } catch (const exception& e) {
        cout << "Division error: " << e.what() << endl;
    }
    
    cout << endl;
    
    // Example 3: Safe vector
    cout << "Example 3: Safe vector" << endl;
    SafeVector safeVec;
    
    safeVec.push_back(10);
    safeVec.push_back(20);
    safeVec.push_back(30);
    
    cout << "Vector size: " << safeVec.size() << endl;
    cout << "Element at 1: " << safeVec.at(1) << endl;
    cout << "Element at 10: " << safeVec.at(10) << endl; // Returns -1, no exception
    
    cout << endl;
    
    // Example 4: Exception guarantees
    cout << "Example 4: Exception guarantees" << endl;
    try {
        ExceptionGuarantees eg(5);
        cout << "Initial size: " << eg.getSize() << endl;
        
        eg.setElement(2, 42);
        cout << "Element at 2: " << eg.getElement(2) << endl;
        
        eg.resize(10);
        cout << "Size after resize: " << eg.getSize() << endl;
        
        eg.setElement(15, 100); // This will throw
    } catch (const exception& e) {
        cout << "Exception: " << e.what() << endl;
    }
    
    cout << endl;
    
    // Example 5: noexcept operator
    cout << "Example 5: noexcept operator" << endl;
    cout << "noThrowFunction is noexcept: " << noexcept(noThrowFunction()) << endl;
    cout << "functionThatThrows is noexcept: " << noexcept(functionThatThrows()) << endl;
    cout << "SafeCalculator::getValue is noexcept: " << noexcept(declval<SafeCalculator>().getValue()) << endl;
    
    return 0;
}
```

---

## 📊 Exception Handling Summary

| Technique | Purpose | Example |
|-----------|---------|---------|
| **try-catch** | Handle exceptions | `try { risky(); } catch(e) { handle(e); }` |
| **Custom Exceptions** | Domain-specific errors | `class MyException : public exception` |
| **Exception Hierarchy** | Organized error handling | Inheritance-based exceptions |
| **RAII** | Resource management | Smart pointers, file handles |
| **noexcept** | Exception specifications | `void func() noexcept` |

---

## ⚡ Performance Considerations

### Advantages
- ✅ **Clean Error Handling**: Separates error handling from normal flow
- ✅ **Resource Safety**: RAII ensures proper cleanup
- ✅ **Exception Safety**: Strong, basic, and no-throw guarantees
- ✅ **Maintainability**: Centralized error handling

### Considerations
- ⚠️ **Runtime Overhead**: Exception handling has some performance cost
- ⚠️ **Binary Size**: Exception handling increases executable size
- ⚠️ **Compiler Optimization**: May limit some optimizations
- ⚠️ **Memory Usage**: Stack unwinding requires additional memory

---

## 🐛 Common Pitfalls

| Problem | Solution |
|---------|----------|
| **Throwing in destructors** | Never throw in destructors or use noexcept |
| **Memory leaks in exceptions** | Use RAII and smart pointers |
| **Catching by value** | Catch exceptions by reference |
| **Exception specifications** | Use noexcept instead of throw() |
| **Swallowing exceptions** | Handle or re-throw exceptions appropriately |

---

## ✅ Best Practices

1. **Use RAII** for resource management
2. **Catch by reference** to avoid slicing
3. **Create custom exception hierarchies** for domain-specific errors
4. **Use noexcept** for functions that don't throw
5. **Provide strong exception guarantees** when possible
6. **Don't throw in destructors** unless you catch all exceptions
7. **Be specific** about which exceptions you catch

---

## 📚 Related Topics

- [RAII Pattern](../11_Memory_Management_in_OOP/05_Smart_Pointers_Intro.md)
- [Smart Pointers](../14_Modern_Cpp_OOP_Features/04_Smart_Pointers.md)
- [Design Patterns](../12_Design_Patterns/01_Creational_Patterns/Singleton.md)
- [Error Handling Best Practices](../13_Best_Practices/06_Common_Pitfalls.md)

---

## 🚀 Next Steps

After mastering exception handling, explore:
- **Advanced RAII Techniques**: Custom deleters, resource pools
- **Exception-Safe Design Patterns**: Exception-safe implementations
- **Error Handling Strategies**: Error codes vs exceptions
- **Performance Optimization**: Minimizing exception overhead

---
