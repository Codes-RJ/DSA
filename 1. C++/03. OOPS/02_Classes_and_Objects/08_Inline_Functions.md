# 02_Classes_and_Objects/08_Inline_Functions.md

# Inline Functions in C++ - Complete Guide

## 📖 Overview

Inline functions are a C++ optimization feature that suggests to the compiler to expand the function's code at the call site, eliminating function call overhead. This is particularly useful for small, frequently called functions. Inline functions can be defined inside the class definition or outside with the `inline` keyword.

---

## 🎯 Types of Inline Functions

| Type | Declaration | Location | Use Case |
|------|-------------|----------|----------|
| **Implicit Inline** | Function defined inside class | Inside class definition | Small, trivial functions |
| **Explicit Inline** | `inline` keyword before definition | Outside class or in header | Functions defined outside class |
| **Default Inline** | Not specified | Compiler decides | Compiler may inline without keyword |

---

## 1. **Inline Functions Inside Class (Implicit Inline)**

### Definition
Functions defined inside the class definition are automatically treated as inline by the compiler.

```cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

class Point {
private:
    double x, y;
    
public:
    // Constructor - implicitly inline
    Point(double x = 0, double y = 0) : x(x), y(y) {}
    
    // Getters - implicitly inline (small, frequently called)
    double getX() const { return x; }
    double getY() const { return y; }
    
    // Setters - implicitly inline
    void setX(double val) { x = val; }
    void setY(double val) { y = val; }
    
    // Distance function - small calculation
    double distanceFromOrigin() const {
        return sqrt(x * x + y * y);
    }
    
    // Overloaded operators - implicitly inline
    Point operator+(const Point& other) const {
        return Point(x + other.x, y + other.y);
    }
    
    Point operator-(const Point& other) const {
        return Point(x - other.x, y - other.y);
    }
    
    // Display function - also inline
    void display() const {
        cout << "(" << x << ", " << y << ")" << endl;
    }
};

class Rectangle {
private:
    double width, height;
    
public:
    Rectangle(double w = 0, double h = 0) : width(w), height(h) {}
    
    // All these are implicitly inline
    double area() const { return width * height; }
    double perimeter() const { return 2 * (width + height); }
    double getWidth() const { return width; }
    double getHeight() const { return height; }
    void setWidth(double w) { width = w; }
    void setHeight(double h) { height = h; }
    
    bool isSquare() const { return width == height; }
    
    void scale(double factor) {
        width *= factor;
        height *= factor;
    }
};

int main() {
    Point p1(3, 4);
    Point p2(1, 2);
    
    cout << "Point p1: ";
    p1.display();
    cout << "Distance from origin: " << p1.distanceFromOrigin() << endl;
    
    Point p3 = p1 + p2;
    cout << "p1 + p2: ";
    p3.display();
    
    Rectangle rect(5, 3);
    cout << "\nRectangle area: " << rect.area() << endl;
    cout << "Rectangle perimeter: " << rect.perimeter() << endl;
    cout << "Is square? " << (rect.isSquare() ? "Yes" : "No") << endl;
    
    rect.scale(2);
    cout << "After scaling: area = " << rect.area() << endl;
    
    return 0;
}
```

**Output:**
```
Point p1: (3, 4)
Distance from origin: 5
p1 + p2: (4, 6)

Rectangle area: 15
Rectangle perimeter: 16
Is square? No
After scaling: area = 60
```

---

## 2. **Explicit Inline Functions (Defined Outside Class)**

### Definition
Functions defined outside the class with the `inline` keyword. This is typically done in header files.

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class MathUtils {
private:
    static inline int callCount = 0;  // C++17 inline static member
    
public:
    // Declaration only - defined outside
    static int square(int x);
    static int cube(int x);
    static bool isEven(int x);
    static int max(int a, int b);
    static int min(int a, int b);
    static int absolute(int x);
    static int getCallCount() { return callCount; }
};

// Explicit inline definitions
inline int MathUtils::square(int x) {
    callCount++;
    return x * x;
}

inline int MathUtils::cube(int x) {
    callCount++;
    return x * x * x;
}

inline bool MathUtils::isEven(int x) {
    callCount++;
    return (x % 2 == 0);
}

inline int MathUtils::max(int a, int b) {
    callCount++;
    return (a > b) ? a : b;
}

inline int MathUtils::min(int a, int b) {
    callCount++;
    return (a < b) ? a : b;
}

inline int MathUtils::absolute(int x) {
    callCount++;
    return (x < 0) ? -x : x;
}

class StringUtil {
public:
    // Declaration
    static size_t length(const char* str);
    static void toUpper(char* str);
    static void toLower(char* str);
    static bool startsWith(const char* str, const char* prefix);
    static bool endsWith(const char* str, const char* suffix);
};

// Explicit inline implementations
inline size_t StringUtil::length(const char* str) {
    size_t len = 0;
    while (str[len] != '\0') len++;
    return len;
}

inline void StringUtil::toUpper(char* str) {
    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] >= 'a' && str[i] <= 'z') {
            str[i] -= 32;
        }
    }
}

inline void StringUtil::toLower(char* str) {
    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] >= 'A' && str[i] <= 'Z') {
            str[i] += 32;
        }
    }
}

inline bool StringUtil::startsWith(const char* str, const char* prefix) {
    for (int i = 0; prefix[i] != '\0'; i++) {
        if (str[i] != prefix[i]) return false;
    }
    return true;
}

inline bool StringUtil::endsWith(const char* str, const char* suffix) {
    size_t strLen = StringUtil::length(str);
    size_t suffixLen = StringUtil::length(suffix);
    
    if (suffixLen > strLen) return false;
    
    for (size_t i = 0; i < suffixLen; i++) {
        if (str[strLen - suffixLen + i] != suffix[i]) return false;
    }
    return true;
}

int main() {
    cout << "=== MathUtils Inline Functions ===" << endl;
    cout << "square(5): " << MathUtils::square(5) << endl;
    cout << "cube(3): " << MathUtils::cube(3) << endl;
    cout << "isEven(4): " << MathUtils::isEven(4) << endl;
    cout << "max(10, 20): " << MathUtils::max(10, 20) << endl;
    cout << "min(10, 20): " << MathUtils::min(10, 20) << endl;
    cout << "absolute(-42): " << MathUtils::absolute(-42) << endl;
    cout << "Function calls: " << MathUtils::getCallCount() << endl;
    
    cout << "\n=== StringUtil Inline Functions ===" << endl;
    char str1[] = "Hello World";
    char str2[] = "Hello";
    char str3[] = "World";
    
    cout << "Length of 'Hello World': " << StringUtil::length(str1) << endl;
    
    StringUtil::toUpper(str1);
    cout << "toUpper: " << str1 << endl;
    
    StringUtil::toLower(str1);
    cout << "toLower: " << str1 << endl;
    
    cout << "Starts with 'Hello'? " 
         << (StringUtil::startsWith(str1, str2) ? "Yes" : "No") << endl;
    cout << "Ends with 'World'? " 
         << (StringUtil::endsWith(str1, str3) ? "Yes" : "No") << endl;
    
    return 0;
}
```

---

## 3. **Inline vs Non-Inline Performance Comparison**

```cpp
#include <iostream>
#include <chrono>
#include <vector>
#include <cmath>
using namespace std;
using namespace chrono;

// Non-inline function
double nonInlineFunction(double x) {
    return sin(x) * cos(x) + sqrt(x);
}

// Inline function
inline double inlineFunction(double x) {
    return sin(x) * cos(x) + sqrt(x);
}

class Calculator {
public:
    // Non-inline method
    double nonInlineMethod(double x);
    
    // Inline method
    inline double inlineMethod(double x) {
        return sin(x) * cos(x) + sqrt(x);
    }
    
    // Virtual function (cannot be inlined)
    virtual double virtualMethod(double x) {
        return sin(x) * cos(x) + sqrt(x);
    }
};

// Define non-inline method outside class
double Calculator::nonInlineMethod(double x) {
    return sin(x) * cos(x) + sqrt(x);
}

class ComplexCalculation {
private:
    double data;
    
public:
    ComplexCalculation(double d) : data(d) {}
    
    // Small, simple functions - good for inlining
    double getValue() const { return data; }
    void setValue(double d) { data = d; }
    
    // Large, complex functions - not good for inlining
    double complexAlgorithm() const {
        double result = 0;
        for (int i = 0; i < 1000; i++) {
            result += sin(data * i) * cos(data * i);
        }
        return result;
    }
};

int main() {
    const int ITERATIONS = 10000000;
    vector<double> results(ITERATIONS);
    
    // Test non-inline function
    auto start = high_resolution_clock::now();
    for (int i = 0; i < ITERATIONS; i++) {
        results[i] = nonInlineFunction(i * 0.000001);
    }
    auto end = high_resolution_clock::now();
    auto nonInlineTime = duration_cast<milliseconds>(end - start).count();
    
    // Test inline function
    start = high_resolution_clock::now();
    for (int i = 0; i < ITERATIONS; i++) {
        results[i] = inlineFunction(i * 0.000001);
    }
    end = high_resolution_clock::now();
    auto inlineTime = duration_cast<milliseconds>(end - start).count();
    
    cout << "=== Performance Comparison (10 million iterations) ===" << endl;
    cout << "Non-inline function: " << nonInlineTime << " ms" << endl;
    cout << "Inline function: " << inlineTime << " ms" << endl;
    cout << "Speedup: " << (nonInlineTime - inlineTime) << " ms faster" << endl;
    
    // Test class methods
    Calculator calc;
    
    start = high_resolution_clock::now();
    for (int i = 0; i < ITERATIONS; i++) {
        results[i] = calc.nonInlineMethod(i * 0.000001);
    }
    end = high_resolution_clock::now();
    auto nonInlineMethodTime = duration_cast<milliseconds>(end - start).count();
    
    start = high_resolution_clock::now();
    for (int i = 0; i < ITERATIONS; i++) {
        results[i] = calc.inlineMethod(i * 0.000001);
    }
    end = high_resolution_clock::now();
    auto inlineMethodTime = duration_cast<milliseconds>(end - start).count();
    
    start = high_resolution_clock::now();
    for (int i = 0;i < ITERATIONS; i++) {
        results[i] = calc.virtualMethod(i * 0.000001);
    }
    end = high_resolution_clock::now();
    auto virtualMethodTime = duration_cast<milliseconds>(end - start).count();
    
    cout << "\n=== Class Method Comparison ===" << endl;
    cout << "Non-inline method: " << nonInlineMethodTime << " ms" << endl;
    cout << "Inline method: " << inlineMethodTime << " ms" << endl;
    cout << "Virtual method: " << virtualMethodTime << " ms" << endl;
    
    // Complex calculations - inline may not help
    ComplexCalculation comp(1.5);
    
    start = high_resolution_clock::now();
    for (int i = 0; i < 100000; i++) {
        double val = comp.complexAlgorithm();
    }
    end = high_resolution_clock::now();
    auto complexTime = duration_cast<milliseconds>(end - start).count();
    
    cout << "\n=== Complex Calculation ===" << endl;
    cout << "Large function (100k iterations): " << complexTime << " ms" << endl;
    cout << "Note: Inlining large functions provides little benefit" << endl;
    
    return 0;
}
```

---

## 4. **Inline Functions in Header Files**

### Definition
Inline functions are typically defined in header files to avoid multiple definition errors.

```cpp
// ---------- geometry.h ----------
#ifndef GEOMETRY_H
#define GEOMETRY_H

#include <cmath>

namespace Geometry {
    
    // Inline function in header - safe for multiple includes
    inline double circleArea(double radius) {
        return 3.141592653589793 * radius * radius;
    }
    
    inline double circleCircumference(double radius) {
        return 2 * 3.141592653589793 * radius;
    }
    
    inline double rectangleArea(double width, double height) {
        return width * height;
    }
    
    inline double rectanglePerimeter(double width, double height) {
        return 2 * (width + height);
    }
    
    inline double triangleArea(double base, double height) {
        return 0.5 * base * height;
    }
    
    // Constexpr implies inline (C++11)
    constexpr double square(double x) {
        return x * x;
    }
    
    constexpr double cube(double x) {
        return x * x * x;
    }
    
} // namespace Geometry

#endif // GEOMETRY_H

// ---------- utilities.h ----------
#ifndef UTILITIES_H
#define UTILITIES_H

#include <string>
#include <vector>
using namespace std;

class Utilities {
public:
    // Inline static methods in header
    static inline bool isPrime(int n) {
        if (n <= 1) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        
        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }
    
    static inline int factorial(int n) {
        if (n <= 1) return 1;
        return n * factorial(n - 1);
    }
    
    static inline int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    
    static inline int lcm(int a, int b) {
        return a * b / gcd(a, b);
    }
    
    // Template functions are implicitly inline
    template<typename T>
    static T max(const T& a, const T& b) {
        return (a > b) ? a : b;
    }
    
    template<typename T>
    static T min(const T& a, const T& b) {
        return (a < b) ? a : b;
    }
    
    template<typename T>
    static void swap(T& a, T& b) {
        T temp = a;
        a = b;
        b = temp;
    }
};

#endif // UTILITIES_H

// ---------- main.cpp ----------
#include <iostream>
#include "geometry.h"
#include "utilities.h"
using namespace std;

int main() {
    cout << "=== Geometry Calculations ===" << endl;
    cout << "Circle area (r=5): " << Geometry::circleArea(5) << endl;
    cout << "Circle circumference (r=5): " << Geometry::circleCircumference(5) << endl;
    cout << "Rectangle area (5x3): " << Geometry::rectangleArea(5, 3) << endl;
    cout << "Square of 5: " << Geometry::square(5) << endl;
    
    cout << "\n=== Utilities ===" << endl;
    cout << "Is 17 prime? " << (Utilities::isPrime(17) ? "Yes" : "No") << endl;
    cout << "Factorial of 5: " << Utilities::factorial(5) << endl;
    cout << "GCD of 48 and 18: " << Utilities::gcd(48, 18) << endl;
    cout << "LCM of 12 and 18: " << Utilities::lcm(12, 18) << endl;
    
    cout << "\n=== Template Functions ===" << endl;
    cout << "Max of 10 and 20: " << Utilities::max(10, 20) << endl;
    cout << "Min of 3.14 and 2.71: " << Utilities::min(3.14, 2.71) << endl;
    
    int a = 5, b = 10;
    Utilities::swap(a, b);
    cout << "After swap: a=" << a << ", b=" << b << endl;
    
    return 0;
}
```

---

## 5. **When NOT to Use Inline Functions**

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class LargeClass {
private:
    vector<int> data;
    string name;
    
public:
    LargeClass(string n) : name(n) {
        for (int i = 0; i < 1000; i++) {
            data.push_back(i);
        }
    }
    
    // BAD candidate for inlining - large function
    void processData() {
        for (size_t i = 0; i < data.size(); i++) {
            data[i] = data[i] * 2;
            // Many operations here
            if (data[i] > 1000) {
                data[i] = data[i] % 1000;
            }
            // More complex logic
        }
    }
    
    // BAD candidate for inlining - recursive
    int factorial(int n) {
        if (n <= 1) return 1;
        return n * factorial(n - 1);
    }
    
    // BAD candidate for inlining - virtual function
    virtual void virtualMethod() {
        cout << "Virtual method called" << endl;
    }
    
    // GOOD candidate for inlining - simple getter
    string getName() const { return name; }
    
    // GOOD candidate for inlining - simple setter
    void setName(const string& n) { name = n; }
};

class RecursiveClass {
public:
    // BAD - recursive inline
    inline int fibonacci(int n) {
        if (n <= 1) return n;
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
    
    // GOOD - small iterative version can be inline
    inline int factorialIterative(int n) {
        int result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }
};

class ComplexLoop {
public:
    // BAD - contains loops, not good for inlining
    inline void bubbleSort(vector<int>& arr) {
        for (size_t i = 0; i < arr.size() - 1; i++) {
            for (size_t j = 0; j < arr.size() - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr[j], arr[j + 1]);
                }
            }
        }
    }
    
    // BAD - contains I/O operations
    inline void printLargeVector(const vector<int>& vec) {
        for (int val : vec) {
            cout << val << " ";
        }
        cout << endl;
    }
    
    // GOOD - simple condition
    inline bool isEmpty(const vector<int>& vec) {
        return vec.empty();
    }
    
    // GOOD - simple size
    inline size_t getSize(const vector<int>& vec) {
        return vec.size();
    }
};

int main() {
    cout << "=== When NOT to Use Inline Functions ===" << endl;
    cout << endl;
    
    cout << "1. LARGE FUNCTIONS:" << endl;
    cout << "   - Functions with many lines of code" << endl;
    cout << "   - Functions with complex logic" << endl;
    cout << "   - Functions containing loops" << endl;
    cout << endl;
    
    cout << "2. RECURSIVE FUNCTIONS:" << endl;
    cout << "   - Recursion cannot be inlined effectively" << endl;
    cout << "   - Compiler will likely ignore inline request" << endl;
    cout << endl;
    
    cout << "3. VIRTUAL FUNCTIONS:" << endl;
    cout << "   - Virtual functions resolved at runtime" << endl;
    cout << "   - Cannot be inlined when called polymorphically" << endl;
    cout << endl;
    
    cout << "4. FUNCTIONS WITH I/O OPERATIONS:" << endl;
    cout << "   - I/O operations dominate execution time" << endl;
    cout << "   - Inlining provides minimal benefit" << endl;
    cout << endl;
    
    cout << "5. FUNCTIONS WITH LOOPS:" << endl;
    cout << "   - Loop overhead > function call overhead" << endl;
    cout << "   - Not beneficial to inline" << endl;
    cout << endl;
    
    cout << "=== Good Candidates for Inlining ===" << endl;
    cout << "✓ Simple getters and setters" << endl;
    cout << "✓ Small mathematical operations" << endl;
    cout << "✓ Functions with 1-3 lines of code" << endl;
    cout << "✓ Functions called very frequently" << endl;
    
    return 0;
}
```

---

## 6. **Inline with constexpr and noexcept**

```cpp
#include <iostream>
#include <array>
using namespace std;

class MathConstants {
public:
    // constexpr implies inline (C++11)
    static constexpr double PI = 3.141592653589793;
    static constexpr double E = 2.718281828459045;
    
    // constexpr functions are implicitly inline
    static constexpr double square(double x) {
        return x * x;
    }
    
    static constexpr double cube(double x) {
        return x * x * x;
    }
    
    // constexpr with conditional
    static constexpr double max(double a, double b) {
        return (a > b) ? a : b;
    }
    
    // noexcept inline function
    static inline int add(int a, int b) noexcept {
        return a + b;
    }
    
    // constexpr + noexcept
    static constexpr int multiply(int a, int b) noexcept {
        return a * b;
    }
};

class StringHelper {
public:
    // constexpr string operations (C++20)
    static constexpr bool isEmpty(const char* str) {
        return str == nullptr || str[0] == '\0';
    }
    
    static constexpr size_t length(const char* str) {
        size_t len = 0;
        while (str[len] != '\0') ++len;
        return len;
    }
    
    // Inline with exception specification
    static inline char* duplicate(const char* str) {
        if (!str) return nullptr;
        size_t len = length(str);
        char* newStr = new char[len + 1];
        for (size_t i = 0; i <= len; i++) {
            newStr[i] = str[i];
        }
        return newStr;
    }
};

template<typename T>
class Vector3D {
private:
    T x, y, z;
    
public:
    // constexpr constructor
    constexpr Vector3D(T x = 0, T y = 0, T z = 0) 
        : x(x), y(y), z(z) {}
    
    // constexpr inline getters
    constexpr T getX() const { return x; }
    constexpr T getY() const { return y; }
    constexpr T getZ() const { return z; }
    
    // constexpr inline setters
    constexpr void setX(T val) { x = val; }
    constexpr void setY(T val) { y = val; }
    constexpr void setZ(T val) { z = val; }
    
    // constexpr inline operations
    constexpr T magnitudeSquared() const {
        return x * x + y * y + z * z;
    }
    
    constexpr Vector3D operator+(const Vector3D& other) const {
        return Vector3D(x + other.x, y + other.y, z + other.z);
    }
    
    constexpr Vector3D operator-(const Vector3D& other) const {
        return Vector3D(x - other.x, y - other.y, z - other.z);
    }
    
    constexpr T dot(const Vector3D& other) const {
        return x * other.x + y * other.y + z * other.z;
    }
    
    constexpr Vector3D cross(const Vector3D& other) const {
        return Vector3D(
            y * other.z - z * other.y,
            z * other.x - x * other.z,
            x * other.y - y * other.x
        );
    }
    
    // Display (cannot be constexpr due to I/O)
    void display() const {
        cout << "(" << x << ", " << y << ", " << z << ")" << endl;
    }
};

int main() {
    cout << "=== constexpr Inline Functions ===" << endl;
    
    // Compile-time evaluation
    constexpr double area = MathConstants::PI * MathConstants::square(5);
    cout << "Area (compile-time): " << area << endl;
    
    constexpr double maxVal = MathConstants::max(10, 20);
    cout << "Max (compile-time): " << maxVal << endl;
    
    constexpr int product = MathConstants::multiply(6, 7);
    cout << "Product (compile-time): " << product << endl;
    
    cout << "\n=== Vector3D constexpr Operations ===" << endl;
    
    // Compile-time vector operations
    constexpr Vector3D<int> v1(1, 2, 3);
    constexpr Vector3D<int> v2(4, 5, 6);
    constexpr Vector3D<int> v3 = v1 + v2;
    constexpr int dot = v1.dot(v2);
    
    cout << "v1: "; v1.display();
    cout << "v2: "; v2.display();
    cout << "v1 + v2: "; v3.display();
    cout << "Dot product: " << dot << endl;
    
    // Cross product (compile-time)
    constexpr auto cross = v1.cross(v2);
    cout << "Cross product: "; cross.display();
    
    cout << "\n=== String Helper ===" << endl;
    const char* test = "Hello";
    cout << "Is empty? " << (StringHelper::isEmpty(test) ? "Yes" : "No") << endl;
    cout << "Length: " << StringHelper::length(test) << endl;
    
    char* dup = StringHelper::duplicate(test);
    cout << "Duplicate: " << dup << endl;
    delete[] dup;
    
    return 0;
}
```

---

## 📊 Inline Functions Summary

| Aspect | Description | Best Practice |
|--------|-------------|---------------|
| **Purpose** | Eliminate function call overhead | Use for small, frequently called functions |
| **Syntax** | `inline` keyword or define inside class | Define inside class for getters/setters |
| **Location** | Usually in header files | Keep inline definitions in headers |
| **Compilation** | Compiler may ignore `inline` | Don't rely on it for performance |
| **Recursion** | Cannot be inlined effectively | Avoid inline for recursive functions |
| **Virtual** | Not inlined when called polymorphically | Virtual functions are rarely inlined |

---

## ✅ Best Practices

### 1. **Use Inline for Small Functions**
```cpp
class Good {
public:
    int getValue() const { return value; }     // ✓ Good - 1 line
    void setValue(int v) { value = v; }        // ✓ Good - 1 line
    bool isEmpty() const { return data.empty(); } // ✓ Good - 1 line
};
```

### 2. **Define Inline Functions in Headers**
```cpp
// utils.h
#ifndef UTILS_H
#define UTILS_H

inline int square(int x) { return x * x; }  // ✓ Safe in header

#endif
```

### 3. **Use constexpr for Compile-Time Evaluation**
```cpp
constexpr int factorial(int n) {
    return n <= 1 ? 1 : n * factorial(n - 1);
}
```

### 4. **Don't Force Inline on Large Functions**
```cpp
class Bad {
public:
    void complexAlgorithm() {  // ✗ Too large for inline
        // 100+ lines of code
    }
};
```

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Inline in cpp file** | Multiple definition errors | Define inline in headers |
| **Large inline functions** | Code bloat | Only inline small functions |
| **Recursive inline** | Compiler ignores inline | Don't inline recursion |
| **Virtual inline** | Not inlined when polymorphic | Accept that virtual functions won't be inlined |
| **Debugging inline** | Harder to debug | Disable inlining for debug builds |

---

## ✅ Key Takeaways

1. **Inline functions** suggest to the compiler to expand code at call site
2. **Implicit inline**: Functions defined inside class
3. **Explicit inline**: Functions defined with `inline` keyword outside class
4. **Best for**: Small, frequently called functions (getters, setters, simple math)
5. **Not for**: Large functions, recursion, virtual functions
6. **Header files**: Inline functions belong in headers
7. **constexpr**: Implies inline and enables compile-time evaluation

---