# Standard Exceptions

## 📖 Overview

C++ provides a comprehensive hierarchy of standard exception classes in the `<stdexcept>` header and other standard library headers. These built-in exceptions cover common error scenarios and provide a solid foundation for exception handling in object-oriented programs.

---

## 🎯 Standard Exception Hierarchy

```
exception
├── logic_error
│   ├── invalid_argument
│   ├── domain_error
│   ├── length_error
│   ├── out_of_range
│   └── future_error (C++11)
├── runtime_error
│   ├── range_error
│   ├── overflow_error
│   ├── underflow_error
│   ├── regex_error (C++11)
│   ├── system_error (C++11)
│   └── ios_base::failure
├── bad_alloc
├── bad_cast
├── bad_typeid
└── bad_exception
```

---

## 🔍 Detailed Explanation

### 1. **Base Exception Class**

```cpp
#include <iostream>
#include <exception>
#include <string>
using namespace std;

// Demonstrating the base exception class
void demonstrateBaseException() {
    cout << "=== Base Exception Class ===" << endl;
    
    try {
        throw exception(); // Generic exception
    } catch (const exception& e) {
        cout << "Caught base exception: " << e.what() << endl;
    }
    
    // Creating custom exception by inheriting from exception
    class MyException : public exception {
    public:
        const char* what() const noexcept override {
            return "My custom exception message";
        }
    };
    
    try {
        throw MyException();
    } catch (const exception& e) {
        cout << "Caught custom exception: " << e.what() << endl;
    }
}

int main() {
    demonstrateBaseException();
    return 0;
}
```

### 2. **Logic Errors**

```cpp
#include <iostream>
#include <stdexcept>
#include <vector>
#include <string>
using namespace std;

// invalid_argument example
void processAge(int age) {
    if (age < 0) {
        throw invalid_argument("Age cannot be negative: " + to_string(age));
    }
    if (age > 150) {
        throw invalid_argument("Age seems unrealistic: " + to_string(age));
    }
    cout << "Valid age: " << age << endl;
}

// domain_error example
double calculateSquareRoot(double value) {
    if (value < 0) {
        throw domain_error("Cannot calculate square root of negative number: " + to_string(value));
    }
    return sqrt(value);
}

// length_error example
void processString(const string& str) {
    const size_t MAX_LENGTH = 10;
    if (str.length() > MAX_LENGTH) {
        throw length_error("String length exceeds maximum of " + to_string(MAX_LENGTH) + " characters");
    }
    cout << "Processed string: " << str << endl;
}

// out_of_range example
void accessVectorElement(const vector<int>& vec, size_t index) {
    if (index >= vec.size()) {
        throw out_of_range("Vector index " + to_string(index) + 
                          " is out of range (size: " + to_string(vec.size()) + ")");
    }
    cout << "Element at index " << index << ": " << vec[index] << endl;
}

int main() {
    cout << "=== Logic Errors ===" << endl;
    
    // Test invalid_argument
    cout << "\n--- invalid_argument ---" << endl;
    vector<int> testAges = {25, -5, 200, 30};
    for (int age : testAges) {
        try {
            processAge(age);
        } catch (const invalid_argument& e) {
            cout << "Invalid argument: " << e.what() << endl;
        }
    }
    
    // Test domain_error
    cout << "\n--- domain_error ---" << endl;
    vector<double> testValues = {9.0, 16.0, -4.0, 25.0};
    for (double value : testValues) {
        try {
            double result = calculateSquareRoot(value);
            cout << "sqrt(" << value << ") = " << result << endl;
        } catch (const domain_error& e) {
            cout << "Domain error: " << e.what() << endl;
        }
    }
    
    // Test length_error
    cout << "\n--- length_error ---" << endl;
    vector<string> testStrings = {"Hello", "World", "ThisStringIsTooLong"};
    for (const string& str : testStrings) {
        try {
            processString(str);
        } catch (const length_error& e) {
            cout << "Length error: " << e.what() << endl;
        }
    }
    
    // Test out_of_range
    cout << "\n--- out_of_range ---" << endl;
    vector<int> numbers = {10, 20, 30, 40, 50};
    vector<size_t> testIndices = {0, 2, 4, 5, 10};
    for (size_t index : testIndices) {
        try {
            accessVectorElement(numbers, index);
        } catch (const out_of_range& e) {
            cout << "Out of range: " << e.what() << endl;
        }
    }
    
    return 0;
}
```

### 3. **Runtime Errors**

```cpp
#include <iostream>
#include <stdexcept>
#include <vector>
#include <fstream>
using namespace std;

// range_error example
double calculatePercentage(double part, double total) {
    if (total == 0) {
        throw range_error("Cannot calculate percentage with zero total");
    }
    double percentage = (part / total) * 100.0;
    if (percentage < 0 || percentage > 100) {
        throw range_error("Calculated percentage " + to_string(percentage) + 
                         " is outside valid range [0, 100]");
    }
    return percentage;
}

// overflow_error example
int safeAdd(int a, int b) {
    if (a > 0 && b > INT_MAX - a) {
        throw overflow_error("Integer overflow in addition");
    }
    if (a < 0 && b < INT_MIN - a) {
        throw overflow_error("Integer underflow in addition");
    }
    return a + b;
}

// underflow_error example
double safeDivide(double a, double b) {
    if (b == 0) {
        throw underflow_error("Division by zero would cause underflow");
    }
    double result = a / b;
    if (abs(result) < 1e-10) {
        throw underflow_error("Result too small, possible underflow");
    }
    return result;
}

// system_error example (C++11)
#include <system_error>
#include <filesystem>

void demonstrateSystemError() {
    cout << "\n--- system_error ---" << endl;
    
    try {
        // Try to open a file that doesn't exist
        ifstream file("nonexistent_file.txt");
        if (!file) {
            throw system_error(errno, system_category(), "Failed to open file");
        }
    } catch (const system_error& e) {
        cout << "System error: " << e.what() << endl;
        cout << "Error code: " << e.code() << endl;
        cout << "Error message: " << e.code().message() << endl;
    }
}

// ios_base::failure example
void demonstrateIOFailure() {
    cout << "\n--- ios_base::failure ---" << endl;
    
    try {
        ifstream file("nonexistent_file.txt");
        file.exceptions(ios::failbit | ios::badbit);
        file.get(); // This will throw
    } catch (const ios_base::failure& e) {
        cout << "IO failure: " << e.what() << endl;
    }
}

int main() {
    cout << "=== Runtime Errors ===" << endl;
    
    // Test range_error
    cout << "\n--- range_error ---" << endl;
    vector<pair<double, double>> testCases = {{25, 50}, {75, 50}, {10, 0}, {-5, 20}};
    for (auto [part, total] : testCases) {
        try {
            double percentage = calculatePercentage(part, total);
            cout << part << "/" << total << " = " << percentage << "%" << endl;
        } catch (const range_error& e) {
            cout << "Range error: " << e.what() << endl;
        }
    }
    
    // Test overflow_error
    cout << "\n--- overflow_error ---" << endl;
    vector<pair<int, int>> addTests = {{1000, 2000}, {INT_MAX, 1}, {-1000, -2000}, {INT_MIN, -1}};
    for (auto [a, b] : addTests) {
        try {
            int result = safeAdd(a, b);
            cout << a << " + " << b << " = " << result << endl;
        } catch (const overflow_error& e) {
            cout << "Overflow error: " << e.what() << endl;
        }
    }
    
    // Test underflow_error
    cout << "\n--- underflow_error ---" << endl;
    vector<pair<double, double>> divTests = {{10, 2}, {1e-15, 1000}, {5, 0}};
    for (auto [a, b] : divTests) {
        try {
            double result = safeDivide(a, b);
            cout << a << " / " << b << " = " << result << endl;
        } catch (const underflow_error& e) {
            cout << "Underflow error: " << e.what() << endl;
        }
    }
    
    // Demonstrate system and IO errors
    demonstrateSystemError();
    demonstrateIOFailure();
    
    return 0;
}
```

### 4. **Memory and Type Exceptions**

```cpp
#include <iostream>
#include <exception>
#include <memory>
#include <typeinfo>
using namespace std;

// bad_alloc example
void demonstrateBadAlloc() {
    cout << "=== bad_alloc ===" << endl;
    
    try {
        // Try to allocate a very large amount of memory
        size_t hugeSize = SIZE_MAX;
        int* hugeArray = new int[hugeSize];
        delete[] hugeArray;
    } catch (const bad_alloc& e) {
        cout << "Bad allocation: " << e.what() << endl;
        cout << "Memory allocation failed - not enough memory available" << endl;
    }
    
    // More realistic example
    try {
        vector<vector<int>> matrix;
        // Keep adding rows until memory runs out
        while (true) {
            vector<int> row(1000000, 42); // 1 million integers
            matrix.push_back(move(row));
        }
    } catch (const bad_alloc& e) {
        cout << "Matrix allocation failed: " << e.what() << endl;
    }
}

// bad_cast example
class Base {
public:
    virtual ~Base() = default;
};

class Derived : public Base {
public:
    void derivedMethod() {
        cout << "Derived method called" << endl;
    }
};

class Unrelated {
public:
    void unrelatedMethod() {
        cout << "Unrelated method called" << endl;
    }
};

void demonstrateBadCast() {
    cout << "\n=== bad_cast ===" << endl;
    
    Base base;
    Derived derived;
    
    // Successful cast
    try {
        Base* basePtr = &derived;
        Derived* derivedPtr = dynamic_cast<Derived*>(basePtr);
        if (derivedPtr) {
            derivedPtr->derivedMethod();
        }
    } catch (const bad_cast& e) {
        cout << "Bad cast: " << e.what() << endl;
    }
    
    // Failed cast with reference
    try {
        Base& baseRef = base;
        Derived& derivedRef = dynamic_cast<Derived&>(baseRef);
        derivedRef.derivedMethod();
    } catch (const bad_cast& e) {
        cout << "Bad cast (reference): " << e.what() << endl;
    }
}

// bad_typeid example
void demonstrateBadTypeId() {
    cout << "\n=== bad_typeid ===" << endl;
    
    try {
        Base* basePtr = nullptr;
        const type_info& typeInfo = typeid(*basePtr);
        cout << "Type: " << typeInfo.name() << endl;
    } catch (const bad_typeid& e) {
        cout << "Bad typeid: " << e.what() << endl;
        cout << "Cannot get typeid of null pointer through polymorphic object" << endl;
    }
    
    // Successful typeid
    try {
        Derived derived;
        Base* basePtr = &derived;
        const type_info& typeInfo = typeid(*basePtr);
        cout << "Dynamic type: " << typeInfo.name() << endl;
    } catch (const bad_typeid& e) {
        cout << "Bad typeid: " << e.what() << endl;
    }
}

// bad_exception example
void unexpectedFunction() {
    throw "Unexpected exception type";
}

void demonstrateBadException() {
    cout << "\n=== bad_exception ===" << endl;
    
    // Set unexpected handler (deprecated in C++11, but shown for completeness)
    set_unexpected([]() {
        cout << "Unexpected handler called" << endl;
        throw bad_exception();
    });
    
    try {
        // This would call unexpected handler in older C++ versions
        // In modern C++, this just throws the string directly
        unexpectedFunction();
    } catch (const bad_exception& e) {
        cout << "Caught bad_exception: " << e.what() << endl;
    } catch (const char* e) {
        cout << "Caught string exception: " << e << endl;
    }
}

int main() {
    demonstrateBadAlloc();
    demonstrateBadCast();
    demonstrateBadTypeId();
    demonstrateBadException();
    
    return 0;
}
```

### 5. **Modern C++ Exceptions (C++11 and later)**

```cpp
#include <iostream>
#include <stdexcept>
#include <future>
#include <regex>
#include <system_error>
#include <thread>
using namespace std;

// future_error example (C++11)
void demonstrateFutureError() {
    cout << "=== future_error (C++11) ===" << endl;
    
    try {
        promise<int> prom;
        future<int> fut = prom.get_future();
        
        // Try to get the future twice
        int value = fut.get();
        value = fut.get(); // This will throw
    } catch (const future_error& e) {
        cout << "Future error: " << e.what() << endl;
    }
    
    try {
        promise<int> prom;
        prom.set_value(42);
        prom.set_value(24); // Try to set value twice
    } catch (const future_error& e) {
        cout << "Promise error: " << e.what() << endl;
    }
}

// regex_error example (C++11)
void demonstrateRegexError() {
    cout << "\n=== regex_error (C++11) ===" << endl;
    
    vector<string> invalidPatterns = {
        "(",           // Unmatched parenthesis
        "[a-z",        // Unclosed character class
        "*abc",        // Invalid quantifier
        "(?P<name>a)", // Named groups not supported in basic regex
    };
    
    for (const string& pattern : invalidPatterns) {
        try {
            regex re(pattern);
            cout << "Pattern '" << pattern << "' is valid" << endl;
        } catch (const regex_error& e) {
            cout << "Regex error in pattern '" << pattern << "': " << e.what() << endl;
            cout << "Error code: " << e.code() << endl;
        }
    }
}

// Advanced system_error examples
void demonstrateAdvancedSystemError() {
    cout << "\n=== Advanced system_error (C++11) ===" << endl;
    
    // Filesystem errors (C++17)
    try {
        // This would require <filesystem> and C++17
        // filesystem::create_directory("/nonexistent/path/file.txt");
        throw system_error(make_error_code(errc::permission_denied), 
                         "Cannot create directory");
    } catch (const system_error& e) {
        cout << "Filesystem error: " << e.what() << endl;
        cout << "Error category: " << e.code().category().name() << endl;
        cout << "Error value: " << e.code().value() << endl;
    }
    
    // Thread errors
    try {
        thread t;
        t.join(); // Joining a non-joinable thread
    } catch (const system_error& e) {
        cout << "Thread error: " << e.what() << endl;
    }
}

// Custom error codes
class CustomErrorCategory : public error_category {
public:
    const char* name() const noexcept override {
        return "custom_error";
    }
    
    string message(int condition) const override {
        switch (condition) {
            case 1: return "Custom error 1 occurred";
            case 2: return "Custom error 2 occurred";
            default: return "Unknown custom error";
        }
    }
};

const CustomErrorCategory customCategory{};

void demonstrateCustomErrorCodes() {
    cout << "\n=== Custom Error Codes ===" << endl;
    
    try {
        error_code customError(1, customCategory);
        throw system_error(customError, "Custom operation failed");
    } catch (const system_error& e) {
        cout << "Custom system error: " << e.what() << endl;
        cout << "Error category: " << e.code().category().name() << endl;
    }
}

int main() {
    demonstrateFutureError();
    demonstrateRegexError();
    demonstrateAdvancedSystemError();
    demonstrateCustomErrorCodes();
    
    return 0;
}
```

---

## 🎮 Complete Example: File Processing System

```cpp
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stdexcept>
#include <system_error>
#include <regex>
using namespace std;

class FileProcessor {
private:
    string filename;
    ifstream file;
    
public:
    FileProcessor(const string& fname) : filename(fname) {
        if (filename.empty()) {
            throw invalid_argument("Filename cannot be empty");
        }
        
        // Validate filename format
        regex filenamePattern(R"(^[a-zA-Z0-9_\-\.]+\.(txt|csv|dat)$)");
        if (!regex_match(filename, filenamePattern)) {
            throw invalid_argument("Invalid filename format: " + filename);
        }
        
        file.open(filename);
        if (!file.is_open()) {
            throw system_error(errno, system_category(), 
                             "Failed to open file: " + filename);
        }
    }
    
    ~FileProcessor() {
        if (file.is_open()) {
            file.close();
        }
    }
    
    vector<string> readLines(size_t maxLines = 1000) {
        if (!file.is_open()) {
            throw runtime_error("File is not open");
        }
        
        vector<string> lines;
        string line;
        size_t lineCount = 0;
        
        while (getline(file, line)) {
            if (lineCount >= maxLines) {
                throw length_error("File exceeds maximum line count of " + 
                                 to_string(maxLines));
            }
            
            if (line.length() > 1000) {
                throw length_error("Line " + to_string(lineCount + 1) + 
                                 " exceeds maximum length of 1000 characters");
            }
            
            lines.push_back(line);
            lineCount++;
        }
        
        return lines;
    }
    
    int extractNumberFromLine(const string& line, size_t lineNumber) {
        try {
            size_t pos;
            int number = stoi(line, &pos);
            
            // Check if entire line was converted
            if (pos != line.length()) {
                throw invalid_argument("Line contains non-numeric characters");
            }
            
            if (number < 0) {
                throw domain_error("Negative numbers not allowed: " + to_string(number));
            }
            
            if (number > 1000000) {
                throw out_of_range("Number " + to_string(number) + 
                                  " exceeds maximum allowed value of 1000000");
            }
            
            return number;
        } catch (const invalid_argument& e) {
            throw invalid_argument("Invalid number format at line " + 
                                 to_string(lineNumber) + ": " + e.what());
        } catch (const out_of_range& e) {
            throw out_of_range("Number out of range at line " + 
                              to_string(lineNumber) + ": " + e.what());
        }
    }
    
    vector<int> processNumbers() {
        auto lines = readLines();
        vector<int> numbers;
        
        for (size_t i = 0; i < lines.size(); i++) {
            try {
                int number = extractNumberFromLine(lines[i], i + 1);
                numbers.push_back(number);
            } catch (const exception& e) {
                cout << "Warning: " << e.what() << " - skipping line" << endl;
            }
        }
        
        if (numbers.empty()) {
            throw runtime_error("No valid numbers found in file");
        }
        
        return numbers;
    }
    
    double calculateAverage(const vector<int>& numbers) {
        if (numbers.empty()) {
            throw domain_error("Cannot calculate average of empty vector");
        }
        
        long long sum = 0;
        for (int num : numbers) {
            if (sum > LLONG_MAX - num) {
                throw overflow_error("Sum overflow while calculating average");
            }
            sum += num;
        }
        
        return static_cast<double>(sum) / numbers.size();
    }
    
    void displayStatistics() {
        try {
            cout << "Processing file: " << filename << endl;
            
            vector<int> numbers = processNumbers();
            cout << "Found " << numbers.size() << " valid numbers" << endl;
            
            double average = calculateAverage(numbers);
            cout << "Average: " << average << endl;
            
            // Find min and max
            if (!numbers.empty()) {
                int minNum = numbers[0], maxNum = numbers[0];
                for (int num : numbers) {
                    minNum = min(minNum, num);
                    maxNum = max(maxNum, num);
                }
                cout << "Minimum: " << minNum << endl;
                cout << "Maximum: " << maxNum << endl;
            }
            
        } catch (const exception& e) {
            cout << "Error processing file: " << e.what() << endl;
            throw;
        }
    }
};

int main() {
    cout << "=== File Processing System with Standard Exceptions ===" << endl;
    
    vector<string> testFiles = {
        "data.txt",      // Valid file
        "invalid",       // Invalid extension
        "",              // Empty filename
        "nonexistent.txt", // File doesn't exist
        "toolong.txt"    // File with too long lines (simulated)
    };
    
    for (const string& filename : testFiles) {
        cout << "\n--- Testing file: " << filename << " ---" << endl;
        
        try {
            FileProcessor processor(filename);
            processor.displayStatistics();
            
        } catch (const invalid_argument& e) {
            cout << "Invalid argument: " << e.what() << endl;
        } catch (const length_error& e) {
            cout << "Length error: " << e.what() << endl;
        } catch (const domain_error& e) {
            cout << "Domain error: " << e.what() << endl;
        } catch (const out_of_range& e) {
            cout << "Out of range: " << e.what() << endl;
        } catch (const overflow_error& e) {
            cout << "Overflow error: " << e.what() << endl;
        } catch (const runtime_error& e) {
            cout << "Runtime error: " << e.what() << endl;
        } catch (const system_error& e) {
            cout << "System error: " << e.what() << endl;
            cout << "Error code: " << e.code().value() << endl;
        } catch (const exception& e) {
            cout << "Standard exception: " << e.what() << endl;
        } catch (...) {
            cout << "Unknown exception occurred" << endl;
        }
    }
    
    // Create a test file for successful processing
    cout << "\n--- Creating test file ---" << endl;
    try {
        ofstream testFile("data.txt");
        testFile << "100\n";
        testFile << "200\n";
        testFile << "300\n";
        testFile << "400\n";
        testFile << "500\n";
        testFile.close();
        
        FileProcessor processor("data.txt");
        processor.displayStatistics();
        
    } catch (const exception& e) {
        cout << "Error: " << e.what() << endl;
    }
    
    return 0;
}
```

---

## 📊 Standard Exception Summary

| Category | Exception | Use Case |
|----------|-----------|----------|
| **Logic Errors** | `invalid_argument` | Invalid function arguments |
| | `domain_error` | Domain violation |
| | `length_error` | Length limit exceeded |
| | `out_of_range` | Index out of bounds |
| **Runtime Errors** | `runtime_error` | General runtime errors |
| | `range_error` | Range violations |
| | `overflow_error` | Arithmetic overflow |
| | `underflow_error` | Arithmetic underflow |
| **Memory Errors** | `bad_alloc` | Memory allocation failure |
| **Type Errors** | `bad_cast` | Failed dynamic cast |
| | `bad_typeid` | typeid on null pointer |
| **System Errors** | `system_error` | OS-level errors |
| | `ios_base::failure` | I/O stream failures |

---

## ⚡ Performance Considerations

### Advantages
- ✅ **Standardized**: Consistent interface across all implementations
- ✅ **Type Safety**: Strong typing for different error categories
- ✅ **Hierarchy**: Organized inheritance structure
- ✅ **Extensible**: Can inherit from standard exceptions

### Considerations
- ⚠️ **Overhead**: Exception handling has performance cost
- ⚠️ **Memory**: Exception objects consume memory
- ⚠️ **Binary Size**: Increases executable size
- ⚠️ **Compilation**: May increase compilation time

---

## 🐛 Common Pitfalls

| Problem | Solution |
|---------|----------|
| **Catching base exception first** | Order catch blocks from specific to general |
| **Throwing by value** | Throw by reference: `throw MyException()` |
| **Ignoring exception hierarchy** | Use appropriate derived exception types |
| **Not checking what()** | Always call `what()` for error details |
| **Mixing error codes and exceptions** | Choose one approach consistently |

---

## ✅ Best Practices

1. **Use appropriate exception types** from the standard hierarchy
2. **Inherit from standard exceptions** for custom exceptions
3. **Catch by reference** to avoid slicing
4. **Order catch blocks** from specific to general
5. **Provide meaningful messages** in exception objects
6. **Handle system errors** with `system_error` when applicable
7. **Document exception specifications** for your functions

---

## 📚 Related Topics

- [Try-Catch-Throw](01_Try_Catch_Throw.md)
- [Custom Exceptions](03_Custom_Exceptions.md)
- [Exception Specifications](04_Exception_Specifications.md)
- [RAII Pattern](05_RAII.md)

---

## 🚀 Next Steps

Continue learning about:
- **Custom Exception Design**: Creating domain-specific exceptions
- **Exception Specifications**: noexcept and exception guarantees
- **RAII Pattern**: Resource management with exceptions
- **Advanced Exception Handling**: Exception-safe design patterns

---
