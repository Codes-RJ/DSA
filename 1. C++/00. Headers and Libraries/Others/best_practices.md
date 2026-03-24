# C++ Best Practices and Coding Standards

This guide covers essential C++ best practices, coding standards, and conventions that will help you write clean, efficient, and maintainable code.

## 📋 Table of Contents

1. [Code Style and Formatting](#code-style-and-formatting)
2. [Memory Management](#memory-management)
3. [Error Handling](#error-handling)
4. [Performance Optimization](#performance-optimization)
5. [Safety and Security](#safety-and-security)
6. [Modern C++ Features](#modern-c-features)
7. [Documentation](#documentation)
8. [Testing](#testing)

## 🎨 Code Style and Formatting

### Naming Conventions
```cpp
// Classes: PascalCase
class DataProcessor {
private:
    // Member variables: snake_case with m_ prefix
    int m_data_count;
    std::string m_file_name;
    
public:
    // Functions: camelCase
    void processData();
    
    // Constants: UPPER_SNAKE_CASE
    static const int MAX_SIZE = 1000;
};

// Variables: snake_case
int user_count = 0;
std::string file_path = "data.txt";

// Functions: camelCase
void calculateAverage();
bool isValidInput(const std::string& input);

// Constants: UPPER_SNAKE_CASE
const double PI = 3.14159;
const int MAX_RETRIES = 3;

// Enums: PascalCase
enum class LogLevel {
    DEBUG,
    INFO,
    WARNING,
    ERROR
};
```

### Formatting Guidelines
```cpp
// Indentation: 4 spaces (no tabs)
class Example {
public:
    // Braces on same line for functions/classes
    void process() {
        // Space around operators
        int result = a + b * c;
        
        // Consistent spacing
        if (condition) {
            doSomething();
        } else {
            doSomethingElse();
        }
    }
    
private:
    // One declaration per line
    int m_member1;
    int m_member2;
    std::string m_member3;
};

// Template declarations
template<typename T, typename U>
class Container {
    // Implementation
};

// Long function declarations
void veryLongFunctionName(
    const std::string& parameter1,
    int parameter2,
    double parameter3
);
```

## 🧠 Memory Management

### RAII (Resource Acquisition Is Initialization)
```cpp
#include <memory>
#include <fstream>

class GoodExample {
private:
    std::unique_ptr<int[]> m_data;
    std::ifstream m_file;
    
public:
    GoodExample(size_t size, const std::string& filename) 
        : m_data(std::make_unique<int[]>(size))
        , m_file(filename) {
        // Resources automatically managed
    }
    
    // No need for explicit cleanup - destructor handles it
    ~GoodExample() = default;
    
    // Rule of Five
    GoodExample(const GoodExample&) = delete;
    GoodExample& operator=(const GoodExample&) = delete;
    GoodExample(GoodExample&&) = default;
    GoodExample& operator=(GoodExample&&) = default;
};

// Bad example - manual memory management
class BadExample {
private:
    int* m_data;
    FILE* m_file;
    
public:
    BadExample(size_t size, const std::string& filename) {
        m_data = new int[size];  // Potential memory leak
        m_file = fopen(filename.c_str(), "r");  // Resource leak
    }
    
    ~BadExample() {
        delete[] m_data;  // Might not be called if exception occurs
        if (m_file) fclose(m_file);
    }
};
```

### Smart Pointers
```cpp
#include <memory>

class SmartPointerExample {
public:
    void demonstrateSmartPointers() {
        // unique_ptr - exclusive ownership
        auto unique_data = std::make_unique<int>(42);
        
        // shared_ptr - shared ownership
        auto shared_data = std::make_shared<std::vector<int>>(100);
        
        // weak_ptr - non-owning reference
        std::weak_ptr<std::vector<int>> weak_data = shared_data;
        
        // Use weak_ptr safely
        if (auto locked = weak_data.lock()) {
            locked->push_back(10);
        }
    }
    
    // Factory function returning smart pointer
    static std::unique_ptr<SmartPointerExample> create() {
        return std::make_unique<SmartPointerExample>();
    }
};
```

## ⚠️ Error Handling

### Exceptions vs Error Codes
```cpp
#include <stdexcept>
#include <optional>

class ErrorHandlingExample {
public:
    // Use exceptions for exceptional circumstances
    int divide(int a, int b) {
        if (b == 0) {
            throw std::invalid_argument("Division by zero");
        }
        return a / b;
    }
    
    // Use optional for values that might not exist
    std::optional<int> findValue(const std::vector<int>& data, int target) {
        auto it = std::find(data.begin(), data.end(), target);
        if (it != data.end()) {
            return *it;
        }
        return std::nullopt;
    }
    
    // Use expected for operations that can fail (C++23)
    // std::expected<int, std::string> riskyOperation();
    
    void demonstrateErrorHandling() {
        try {
            int result = divide(10, 2);
            std::cout << "Result: " << result << std::endl;
        } catch (const std::invalid_argument& e) {
            std::cerr << "Error: " << e.what() << std::endl;
        }
        
        std::vector<int> data = {1, 2, 3, 4, 5};
        if (auto value = findValue(data, 3)) {
            std::cout << "Found: " << *value << std::endl;
        } else {
            std::cout << "Value not found" << std::endl;
        }
    }
};
```

### RAII for Error Handling
```cpp
class FileHandler {
private:
    std::FILE* m_file;
    
public:
    FileHandler(const std::string& filename, const std::string& mode) {
        m_file = std::fopen(filename.c_str(), mode.c_str());
        if (!m_file) {
            throw std::runtime_error("Cannot open file: " + filename);
        }
    }
    
    ~FileHandler() {
        if (m_file) {
            std::fclose(m_file);
        }
    }
    
    // Prevent copying
    FileHandler(const FileHandler&) = delete;
    FileHandler& operator=(const FileHandler&) = delete;
    
    // Allow moving
    FileHandler(FileHandler&& other) noexcept : m_file(other.m_file) {
        other.m_file = nullptr;
    }
    
    std::FILE* get() const { return m_file; }
};

void processFile(const std::string& filename) {
    FileHandler file(filename, "r");
    // File automatically closed when function exits
    // Even if exception occurs
}
```

## ⚡ Performance Optimization

### Move Semantics
```cpp
class PerformanceExample {
private:
    std::vector<int> m_large_data;
    
public:
    // Pass by const reference for reading
    void processData(const std::vector<int>& data) const {
        // Read-only operations
    }
    
    // Pass by value when you need to copy anyway
    void storeData(std::vector<int> data) {
        m_large_data = std::move(data);  // Move instead of copy
    }
    
    // Return by value (NRVO/move semantics)
    std::vector<int> generateData() const {
        std::vector<int> result;
        result.reserve(1000);
        
        for (int i = 0; i < 1000; ++i) {
            result.push_back(i * i);
        }
        
        return result;  // Move semantics or NRVO
    }
    
    // Use emplace_back instead of push_back for complex objects
    void addComplexObject(int x, int y, const std::string& name) {
        m_objects.emplace_back(x, y, name);  // Construct in-place
    }
    
private:
    std::vector<std::pair<int, int>> m_objects;
};
```

### Efficient Algorithms
```cpp
#include <algorithm>
#include <unordered_map>

class EfficientAlgorithms {
public:
    // Use appropriate containers
    void demonstrateContainerChoice() {
        std::vector<int> data = {1, 2, 3, 4, 5};
        
        // For frequent lookups, use unordered_map
        std::unordered_map<int, std::string> lookup;
        lookup[1] = "one";
        lookup[2] = "two";
        
        // Use STL algorithms instead of manual loops
        std::sort(data.begin(), data.end());
        
        // Use lambda expressions with algorithms
        auto it = std::find_if(data.begin(), data.end(),
                              [](int x) { return x > 3; });
        
        // Remove-erase idiom
        data.erase(std::remove_if(data.begin(), data.end(),
                                 [](int x) { return x % 2 == 0; }),
                   data.end());
    }
    
    // Reserve space to avoid reallocations
    void efficientVectorUsage() {
        std::vector<int> vec;
        vec.reserve(1000);  // Reserve space if you know the size
        
        for (int i = 0; i < 1000; ++i) {
            vec.push_back(i);
        }
    }
};
```

## 🔒 Safety and Security

### Safe Coding Practices
```cpp
class SafeCodingExample {
public:
    // Use const correctness
    int getValue() const { return m_value; }
    
    // Use range-based for loops
    void processContainer(const std::vector<int>& data) const {
        for (int value : data) {  // Safer than index-based loops
            processValue(value);
        }
    }
    
    // Use std::array for fixed-size arrays
    void useStdArray() {
        std::array<int, 5> arr = {1, 2, 3, 4, 5};  // Bounds checking with at()
        
        for (size_t i = 0; i < arr.size(); ++i) {
            std::cout << arr.at(i) << " ";  // at() provides bounds checking
        }
    }
    
    // Safe string operations
    void safeStringOperations() {
        std::string str = "Hello, World!";
        
        // Use string methods instead of C-style functions
        if (str.find("World") != std::string::npos) {
            std::cout << "Found World!" << std::endl;
        }
        
        // Avoid buffer overflows
        std::string result = str.substr(0, 5);  // Safe substring
    }
    
private:
    int m_value = 0;
    void processValue(int value) const {
        // Process value
    }
};
```

### Input Validation
```cpp
class InputValidation {
public:
    bool validateInput(const std::string& input) const {
        // Check for empty input
        if (input.empty()) {
            return false;
        }
        
        // Check for valid characters
        for (char c : input) {
            if (!std::isalnum(c) && c != '_' && c != '-') {
                return false;
            }
        }
        
        // Check length limits
        if (input.length() > MAX_INPUT_LENGTH) {
            return false;
        }
        
        return true;
    }
    
    int safeStringToInt(const std::string& str) const {
        try {
            return std::stoi(str);
        } catch (const std::invalid_argument&) {
            throw std::runtime_error("Invalid number format");
        } catch (const std::out_of_range&) {
            throw std::runtime_error("Number out of range");
        }
    }
    
private:
    static const size_t MAX_INPUT_LENGTH = 100;
};
```

## 🚀 Modern C++ Features

### C++11 and Later Features
```cpp
#include <memory>
#include <functional>
#include <tuple>
#include <optional>

class ModernCppFeatures {
public:
    // Auto and decltype
    void demonstrateAuto() {
        auto i = 42;                    // int
        auto s = std::string("hello");  // std::string
        
        std::vector<int> vec = {1, 2, 3};
        for (auto& elem : vec) {       // Reference to avoid copies
            elem *= 2;
        }
    }
    
    // Lambda expressions
    void demonstrateLambdas() {
        std::vector<int> data = {1, 2, 3, 4, 5};
        
        // Simple lambda
        std::for_each(data.begin(), data.end(), [](int& x) { x *= 2; });
        
        // Lambda with capture
        int multiplier = 3;
        std::transform(data.begin(), data.end(), data.begin(),
                      [multiplier](int x) { return x * multiplier; });
        
        // Generic lambda (C++14)
        auto generic = [](auto x, auto y) { return x + y; };
    }
    
    // Smart pointers and move semantics
    std::unique_ptr<ModernCppFeatures> create() {
        return std::make_unique<ModernCppFeatures>();
    }
    
    // Optional for nullable values
    std::optional<std::string> findName(int id) const {
        if (id > 0 && id <= 100) {
            return "Name" + std::to_string(id);
        }
        return std::nullopt;
    }
    
    // Tuple for multiple return values
    std::tuple<int, double, std::string> getMultipleValues() const {
        return {42, 3.14, "answer"};
    }
    
    void demonstrateTuple() {
        auto [int_val, double_val, string_val] = getMultipleValues();
        std::cout << int_val << ", " << double_val << ", " << string_val << std::endl;
    }
};
```

### Constexpr and Compile-Time Programming
```cpp
class CompileTimeFeatures {
public:
    // Compile-time calculations
    static constexpr int factorial(int n) {
        return n <= 1 ? 1 : n * factorial(n - 1);
    }
    
    // Constexpr if (C++17)
    template<typename T>
    auto process(T value) {
        if constexpr (std::is_integral_v<T>) {
            return value * 2;
        } else {
            return value + 1.0;
        }
    }
    
    // Compile-time assertions
    static_assert(factorial(5) == 120, "Factorial calculation error");
};
```

## 📚 Documentation

### Code Documentation
```cpp
/**
 * @brief Processes input data and returns results
 * 
 * This function takes a vector of integers, applies a transformation,
 * and returns the processed data. The transformation is applied
 * using the specified operation.
 * 
 * @param data Input data to be processed
 * @param operation Operation to apply ("add", "multiply", "subtract")
 * @return std::vector<int> Processed data
 * 
 * @throws std::invalid_argument if operation is not supported
 * 
 * @example
 * std::vector<int> input = {1, 2, 3};
 * auto result = processData(input, "add");
 * // result = {2, 3, 4}
 */
std::vector<int> processData(
    const std::vector<int>& data,
    const std::string& operation
);
```

### Comments Guidelines
```cpp
class CommentExample {
public:
    void calculate() {
        // Good: Explain why, not what
        // Using cache-friendly iteration order for better performance
        for (size_t i = 0; i < m_data.size(); ++i) {
            m_result[i] = m_data[i] * m_factor;
        }
        
        // Bad: Redundant comment
        // Increment i by 1
        // for (size_t i = 0; i < m_data.size(); ++i) {
        
        // Complex algorithm explanation
        // Floyd-Warshall algorithm for shortest paths
        // Time complexity: O(V^3), Space complexity: O(V^2)
        for (size_t k = 0; k < m_vertices; ++k) {
            for (size_t i = 0; i < m_vertices; ++i) {
                for (size_t j = 0; j < m_vertices; ++j) {
                    if (m_distance[i][k] + m_distance[k][j] < m_distance[i][j]) {
                        m_distance[i][j] = m_distance[i][k] + m_distance[k][j];
                    }
                }
            }
        }
    }
    
private:
    std::vector<int> m_data;
    std::vector<int> m_result;
    int m_factor = 2;
    size_t m_vertices = 0;
    std::vector<std::vector<int>> m_distance;
};
```

## 🧪 Testing

### Unit Testing Principles
```cpp
#include <cassert>
#include <vector>

class Calculator {
public:
    int add(int a, int b) { return a + b; }
    int divide(int a, int b) {
        if (b == 0) throw std::invalid_argument("Division by zero");
        return a / b;
    }
};

// Simple test framework
class TestCalculator {
private:
    Calculator calc;
    
    void assertEqual(int actual, int expected, const std::string& message) {
        if (actual != expected) {
            std::cerr << "FAIL: " << message 
                      << " (expected: " << expected 
                      << ", actual: " << actual << ")" << std::endl;
        } else {
            std::cout << "PASS: " << message << std::endl;
        }
    }
    
public:
    void runTests() {
        // Test addition
        assertEqual(calc.add(2, 3), 5, "Addition test");
        assertEqual(calc.add(-1, 1), 0, "Negative addition test");
        
        // Test division
        assertEqual(calc.divide(10, 2), 5, "Division test");
        
        // Test exception
        try {
            calc.divide(1, 0);
            std::cerr << "FAIL: Division by zero test" << std::endl;
        } catch (const std::invalid_argument&) {
            std::cout << "PASS: Division by zero test" << std::endl;
        }
    }
};
```

## 🎯 Best Practices Summary

### Do's
- ✅ Use RAII for resource management
- ✅ Prefer smart pointers over raw pointers
- ✅ Use `const` correctness throughout
- ✅ Choose appropriate containers for your use case
- ✅ Use STL algorithms instead of manual loops
- ✅ Handle errors appropriately (exceptions vs error codes)
- ✅ Write clear, self-documenting code
- ✅ Use modern C++ features when appropriate
- ✅ Write tests for critical functionality

### Don'ts
- ❌ Use raw pointers without clear ownership
- ❌ Ignore exception safety
- ❌ Use `using namespace std` in header files
- ❌ Mix new/delete with smart pointers
- ❌ Ignore const correctness
- ❌ Write overly complex code without comments
- ❌ Use C-style arrays when std::array is better
- ❌ Ignore performance implications of design choices
- ❌ Skip error handling "for simplicity"

---

**This guide covers the essential best practices for writing modern, safe, and efficient C++ code. Follow these guidelines to improve code quality and maintainability.**
