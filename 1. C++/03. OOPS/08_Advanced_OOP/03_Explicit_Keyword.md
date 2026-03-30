# Explicit Keyword in C++ - Complete Guide

## 📖 Overview

The `explicit` keyword in C++ prevents the compiler from using single-argument constructors for implicit conversions. It helps avoid unintended type conversions that can lead to subtle bugs and improves code safety and readability. Since C++11, `explicit` can also be applied to conversion operators.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Implicit Conversion** | Automatic conversion performed by compiler |
| **Explicit Constructor** | Constructor that cannot be used for implicit conversions |
| **explicit Keyword** | Prevents implicit conversions for constructors |
| **explicit Conversion Operator (C++11)** | Prevents implicit conversions for conversion operators |

---

## 1. **Basic Explicit Constructor**

```cpp
#include <iostream>
#include <string>
using namespace std;

// Without explicit - can cause unintended conversions
class String {
private:
    string data;
    
public:
    // Implicit conversion constructor (dangerous)
    String(const char* str) : data(str) {
        cout << "String created from: " << str << endl;
    }
    
    void display() const {
        cout << data << endl;
    }
};

// With explicit - prevents implicit conversions
class SafeString {
private:
    string data;
    
public:
    // Explicit constructor - prevents implicit conversion
    explicit SafeString(const char* str) : data(str) {
        cout << "SafeString created from: " << str << endl;
    }
    
    void display() const {
        cout << data << endl;
    }
};

void printString(const String& s) {
    s.display();
}

void printSafeString(const SafeString& s) {
    s.display();
}

int main() {
    cout << "=== Basic Explicit Constructor ===" << endl;
    
    cout << "\n1. Without explicit (dangerous implicit conversions):" << endl;
    String s1 = "Hello";        // Implicit conversion! const char* → String
    String s2("World");         // Explicit call
    printString("Direct");      // Implicit conversion in function call!
    s1.display();
    
    cout << "\n2. With explicit (safe):" << endl;
    SafeString s3("Hello");     // OK - explicit call
    // SafeString s4 = "World"; // Error! Implicit conversion prevented
    // printSafeString("Direct"); // Error! Implicit conversion prevented
    printSafeString(SafeString("Direct")); // OK - explicit
    s3.display();
    
    return 0;
}
```

**Output:**
```
=== Basic Explicit Constructor ===

1. Without explicit (dangerous implicit conversions):
String created from: Hello
String created from: World
String created from: Direct
Hello

2. With explicit (safe):
SafeString created from: Hello
SafeString created from: Direct
Hello
```

---

## 2. **Explicit with Multiple Parameters**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Point {
private:
    int x, y;
    
public:
    // Single-parameter constructor (implicit conversion)
    Point(int xVal) : x(xVal), y(0) {
        cout << "Point(int) called: (" << x << ", " << y << ")" << endl;
    }
    
    // Two-parameter constructor
    Point(int xVal, int yVal) : x(xVal), y(yVal) {
        cout << "Point(int,int) called: (" << x << ", " << y << ")" << endl;
    }
    
    void display() const {
        cout << "(" << x << ", " << y << ")" << endl;
    }
};

class SafePoint {
private:
    int x, y;
    
public:
    // Explicit single-parameter constructor
    explicit SafePoint(int xVal) : x(xVal), y(0) {
        cout << "SafePoint(int) called: (" << x << ", " << y << ")" << endl;
    }
    
    // Two-parameter constructor (not explicit by default)
    SafePoint(int xVal, int yVal) : x(xVal), y(yVal) {
        cout << "SafePoint(int,int) called: (" << x << ", " << y << ")" << endl;
    }
    
    void display() const {
        cout << "(" << x << ", " << y << ")" << endl;
    }
};

class Array {
private:
    vector<int> data;
    
public:
    // Implicit conversion from size_t
    Array(size_t size) : data(size) {
        cout << "Array created with size: " << size << endl;
    }
    
    void set(size_t index, int value) {
        if (index < data.size()) data[index] = value;
    }
    
    void display() const {
        cout << "Array size: " << data.size() << endl;
    }
};

class SafeArray {
private:
    vector<int> data;
    
public:
    // Explicit constructor
    explicit SafeArray(size_t size) : data(size) {
        cout << "SafeArray created with size: " << size << endl;
    }
    
    void set(size_t index, int value) {
        if (index < data.size()) data[index] = value;
    }
    
    void display() const {
        cout << "SafeArray size: " << data.size() << endl;
    }
};

int main() {
    cout << "=== Explicit with Multiple Parameters ===" << endl;
    
    cout << "\n1. Point (implicit conversion from int):" << endl;
    Point p1 = 5;           // Implicit conversion!
    Point p2(10, 20);
    p1.display();
    p2.display();
    
    cout << "\n2. SafePoint (explicit prevents conversion):" << endl;
    SafePoint sp1(5);       // OK - explicit
    SafePoint sp2(10, 20);
    // SafePoint sp3 = 5;   // Error! Implicit conversion prevented
    sp1.display();
    sp2.display();
    
    cout << "\n3. Array (implicit conversion bug):" << endl;
    Array arr = 10;         // Creates array of size 10! Not obvious
    arr.display();
    
    cout << "\n4. SafeArray (explicit prevents bug):" << endl;
    SafeArray sarr(10);     // OK - explicit
    // SafeArray sarr2 = 10; // Error! Must be explicit
    sarr.display();
    
    return 0;
}
```

---

## 3. **Explicit Conversion Operators (C++11)**

```cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

class Rational {
private:
    int numerator;
    int denominator;
    
    void simplify() {
        int gcd = 1;
        for (int i = 2; i <= abs(numerator) && i <= abs(denominator); i++) {
            if (numerator % i == 0 && denominator % i == 0) gcd = i;
        }
        numerator /= gcd;
        denominator /= gcd;
    }
    
public:
    Rational(int num = 0, int den = 1) : numerator(num), denominator(den) {
        if (denominator == 0) throw invalid_argument("Denominator cannot be zero");
        simplify();
    }
    
    // Implicit conversion to double (dangerous)
    operator double() const {
        return static_cast<double>(numerator) / denominator;
    }
    
    void display() const {
        cout << numerator << "/" << denominator;
    }
};

class SafeRational {
private:
    int numerator;
    int denominator;
    
    void simplify() {
        int gcd = 1;
        for (int i = 2; i <= abs(numerator) && i <= abs(denominator); i++) {
            if (numerator % i == 0 && denominator % i == 0) gcd = i;
        }
        numerator /= gcd;
        denominator /= gcd;
    }
    
public:
    SafeRational(int num = 0, int den = 1) : numerator(num), denominator(den) {
        if (denominator == 0) throw invalid_argument("Denominator cannot be zero");
        simplify();
    }
    
    // Explicit conversion to double (safe)
    explicit operator double() const {
        return static_cast<double>(numerator) / denominator;
    }
    
    void display() const {
        cout << numerator << "/" << denominator;
    }
};

class Vector {
private:
    double x, y;
    
public:
    Vector(double xVal = 0, double yVal = 0) : x(xVal), y(yVal) {}
    
    // Implicit conversion to bool (dangerous)
    operator bool() const {
        return x != 0 || y != 0;
    }
    
    void display() const {
        cout << "(" << x << ", " << y << ")" << endl;
    }
};

class SafeVector {
private:
    double x, y;
    
public:
    SafeVector(double xVal = 0, double yVal = 0) : x(xVal), y(yVal) {}
    
    // Explicit conversion to bool (safe)
    explicit operator bool() const {
        return x != 0 || y != 0;
    }
    
    void display() const {
        cout << "(" << x << ", " << y << ")" << endl;
    }
};

void printRational(double d) {
    cout << "Double value: " << d << endl;
}

int main() {
    cout << "=== Explicit Conversion Operators (C++11) ===" << endl;
    
    cout << "\n1. Rational (implicit conversion to double):" << endl;
    Rational r(3, 4);
    double d = r;  // Implicit conversion!
    cout << "r = "; r.display();
    cout << " converted to double: " << d << endl;
    printRational(r);  // Implicit conversion in function call!
    
    cout << "\n2. SafeRational (explicit conversion):" << endl;
    SafeRational sr(3, 4);
    // double sd = sr;  // Error! Implicit conversion prevented
    double sd = static_cast<double>(sr);  // OK - explicit
    cout << "sr = "; sr.display();
    cout << " converted explicitly: " << sd << endl;
    // printRational(sr);  // Error! Implicit conversion prevented
    printRational(static_cast<double>(sr));  // OK
    
    cout << "\n3. Vector (implicit conversion to bool):" << endl;
    Vector v(3, 4);
    if (v) {  // Implicit conversion to bool!
        cout << "Vector is non-zero" << endl;
    }
    int result = v ? 100 : 0;  // Implicit conversion in conditional!
    cout << "Result: " << result << endl;
    
    cout << "\n4. SafeVector (explicit conversion):" << endl;
    SafeVector sv(3, 4);
    // if (sv) { }  // Error! Implicit conversion prevented
    if (static_cast<bool>(sv)) {  // OK - explicit
        cout << "SafeVector is non-zero" << endl;
    }
    
    return 0;
}
```

---

## 4. **Explicit in Templates**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

template<typename T>
class Wrapper {
private:
    T value;
    
public:
    // Implicit constructor
    Wrapper(const T& v) : value(v) {
        cout << "Wrapper created with value" << endl;
    }
    
    T get() const { return value; }
};

template<typename T>
class SafeWrapper {
private:
    T value;
    
public:
    // Explicit constructor
    explicit SafeWrapper(const T& v) : value(v) {
        cout << "SafeWrapper created with value" << endl;
    }
    
    T get() const { return value; }
};

template<typename T>
void process(const Wrapper<T>& w) {
    cout << "Processing wrapper with value: " << w.get() << endl;
}

template<typename T>
void processSafe(const SafeWrapper<T>& w) {
    cout << "Processing safe wrapper with value: " << w.get() << endl;
}

class Widget {
public:
    Widget(int x) {
        cout << "Widget created with " << x << endl;
    }
};

int main() {
    cout << "=== Explicit in Templates ===" << endl;
    
    cout << "\n1. Wrapper (implicit):" << endl;
    Wrapper<int> w1 = 42;           // Implicit conversion!
    Wrapper<string> w2 = "Hello";   // Implicit conversion!
    process(w1);
    process(w2);
    process(100);                   // Implicit conversion in function call!
    
    cout << "\n2. SafeWrapper (explicit):" << endl;
    SafeWrapper<int> sw1(42);       // OK - explicit
    // SafeWrapper<int> sw2 = 42;   // Error! Implicit conversion prevented
    processSafe(sw1);
    // processSafe(100);            // Error! Implicit conversion prevented
    processSafe(SafeWrapper<int>(100));  // OK - explicit
    
    cout << "\n3. Widget with explicit constructor:" << endl;
    Widget w(10);           // OK
    // Widget w2 = 20;      // Error! Widget constructor is explicit
    vector<Widget> widgets;
    widgets.emplace_back(30);  // OK - explicit construction
    // widgets.push_back(40);   // Error! Implicit conversion not allowed
    
    return 0;
}
```

---

## 5. **Practical Example: String Class with Explicit**

```cpp
#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

class String {
private:
    char* data;
    size_t length;
    
public:
    // Implicit constructor (dangerous)
    String(const char* str = "") {
        length = strlen(str);
        data = new char[length + 1];
        strcpy(data, str);
        cout << "String created: " << data << endl;
    }
    
    // Copy constructor
    String(const String& other) {
        length = other.length;
        data = new char[length + 1];
        strcpy(data, other.data);
        cout << "String copied: " << data << endl;
    }
    
    ~String() {
        delete[] data;
    }
    
    void display() const {
        cout << data << endl;
    }
    
    size_t size() const { return length; }
    
    char& operator[](size_t index) { return data[index]; }
    const char& operator[](size_t index) const { return data[index]; }
};

class SafeString {
private:
    char* data;
    size_t length;
    
public:
    // Explicit constructor (safe)
    explicit SafeString(const char* str = "") {
        length = strlen(str);
        data = new char[length + 1];
        strcpy(data, str);
        cout << "SafeString created: " << data << endl;
    }
    
    // Copy constructor
    SafeString(const SafeString& other) {
        length = other.length;
        data = new char[length + 1];
        strcpy(data, other.data);
        cout << "SafeString copied: " << data << endl;
    }
    
    ~SafeString() {
        delete[] data;
    }
    
    void display() const {
        cout << data << endl;
    }
    
    size_t size() const { return length; }
    
    char& operator[](size_t index) { return data[index]; }
    const char& operator[](size_t index) const { return data[index]; }
};

void print(const String& s) {
    s.display();
}

void printSafe(const SafeString& s) {
    s.display();
}

int main() {
    cout << "=== Practical Example: String Class ===" << endl;
    
    cout << "\n1. Implicit String (dangerous):" << endl;
    String s1 = "Hello";        // Implicit conversion
    String s2("World");
    String s3 = s1;
    
    print("Direct call");       // Implicit conversion in function!
    
    vector<String> strings;
    strings.push_back("First");  // Implicit conversion
    strings.emplace_back("Second");
    
    cout << "\n2. SafeString (explicit):" << endl;
    SafeString ss1("Hello");     // OK - explicit
    // SafeString ss2 = "World"; // Error! Implicit conversion prevented
    SafeString ss3(ss1);
    
    // printSafe("Direct");      // Error! Implicit conversion prevented
    printSafe(SafeString("Direct"));  // OK - explicit
    
    vector<SafeString> safeStrings;
    // safeStrings.push_back("First");  // Error! Implicit conversion prevented
    safeStrings.emplace_back("First");  // OK - explicit construction
    safeStrings.push_back(SafeString("Second"));  // OK
    
    cout << "\nBenefits of explicit:" << endl;
    cout << "  ✓ Prevents accidental conversions" << endl;
    cout << "  ✓ Makes code intentions clear" << endl;
    cout << "  ✓ Catches bugs at compile time" << endl;
    cout << "  ✓ Required for single-argument constructors in good design" << endl;
    
    return 0;
}
```

---

## 📊 Explicit Keyword Summary

| Usage | Syntax | Effect |
|-------|--------|--------|
| **Explicit Constructor** | `explicit ClassName(params);` | Prevents implicit conversions |
| **Explicit Conversion Operator (C++11)** | `explicit operator Type() const;` | Prevents implicit conversions |
| **explicit(bool) (C++20)** | `explicit(expression)` | Conditional explicitness |

---

## ✅ Best Practices

1. **Use explicit for single-argument constructors** - Prevent implicit conversions
2. **Use explicit for conversion operators** - Avoid unintended conversions
3. **Default constructors don't need explicit** - No arguments to convert from
4. **Consider explicit for multi-arg constructors** - If first argument is conversion source
5. **Be consistent** - Apply explicit throughout codebase
6. **Document when explicit is omitted** - Explain intentional implicit conversion

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Missing explicit** | Unexpected conversions | Add explicit keyword |
| **Overusing explicit** | Unnecessary verbosity | Use only when needed |
| **Forgetting copy constructor** | Still implicit | Copy constructor not affected by explicit |
| **C++11 conversion operators** | Still implicit | Add explicit to conversion operators |

---

## ✅ Key Takeaways

1. **explicit** prevents implicit conversions
2. **Single-argument constructors** should usually be explicit
3. **C++11** adds explicit conversion operators
4. **C++20** adds conditional explicit
5. **Prevents bugs** from unintended conversions
6. **Makes code** more readable and maintainable
7. **Recommended** for modern C++ code

---