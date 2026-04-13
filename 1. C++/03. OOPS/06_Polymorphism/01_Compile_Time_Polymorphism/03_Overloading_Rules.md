# Overloading Rules in C++ - Complete Guide

## 📖 Overview

Function and operator overloading in C++ follows specific rules that determine how the compiler selects the correct overloaded version. Understanding these rules is essential for writing unambiguous, maintainable code. This guide covers the resolution process, rules for function matching, and common pitfalls.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Overload Resolution** | Process of selecting the best matching function |
| **Candidate Functions** | All functions with the same name |
| **Viable Functions** | Functions with matching number and convertible arguments |
| **Best Viable Function** | Function with the best match after ranking conversions |
| **Ranking** | Exact match > Promotion > Conversion > User-defined |

---

## 1. **Function Overloading Rules**

```cpp
#include <iostream>
#include <string>
using namespace std;

// Overloaded functions
void display(int x) {
    cout << "display(int): " << x << endl;
}

void display(double x) {
    cout << "display(double): " << x << endl;
}

void display(const string& x) {
    cout << "display(string): " << x << endl;
}

void display(int x, int y) {
    cout << "display(int, int): " << x << ", " << y << endl;
}

void display(double x, double y) {
    cout << "display(double, double): " << x << ", " << y << endl;
}

class Number {
public:
    Number(int v) : value(v) {}
    operator int() const { return value; }  // Conversion to int
    int value;
};

void process(int x) {
    cout << "process(int): " << x << endl;
}

void process(double x) {
    cout << "process(double): " << x << endl;
}

int main() {
    cout << "=== Function Overloading Rules ===" << endl;
    
    cout << "\n1. Exact matches:" << endl;
    display(42);           // int
    display(3.14);         // double
    display("Hello");      // const char* -> string
    
    cout << "\n2. Different parameter count:" << endl;
    display(10);           // one parameter
    display(10, 20);       // two parameters
    
    cout << "\n3. Type promotion:" << endl;
    char c = 'A';
    display(c);            // char promoted to int
    float f = 3.14f;
    display(f);            // float promoted to double
    
    cout << "\n4. Type conversion:" << endl;
    short s = 100;
    display(s);            // short converted to int
    
    cout << "\n5. User-defined conversion:" << endl;
    Number n(42);
    process(n);            // Number converted to int
    
    return 0;
}
```

---

## 2. **Overload Resolution Ranking**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Ranking demonstration
void rank1(int x) {
    cout << "rank1(int): " << x << endl;
}

void rank1(long x) {
    cout << "rank1(long): " << x << endl;
}

void rank1(double x) {
    cout << "rank1(double): " << x << endl;
}

// Multiple parameters
void rank2(int x, int y) {
    cout << "rank2(int, int): " << x << ", " << y << endl;
}

void rank2(double x, double y) {
    cout << "rank2(double, double): " << x << ", " << y << endl;
}

void rank2(int x, double y) {
    cout << "rank2(int, double): " << x << ", " << y << endl;
}

void rank2(double x, int y) {
    cout << "rank2(double, int): " << x << ", " << y << endl;
}

// Reference and const
void rank3(int& x) {
    cout << "rank3(int&): " << x << endl;
}

void rank3(const int& x) {
    cout << "rank3(const int&): " << x << endl;
}

void rank3(int&& x) {
    cout << "rank3(int&&): " << x << endl;
}

int main() {
    cout << "=== Overload Resolution Ranking ===" << endl;
    
    cout << "\n1. Exact match ranking:" << endl;
    rank1(42);           // int (exact)
    rank1(42L);          // long (exact)
    rank1(3.14);         // double (exact)
    
    cout << "\n2. Promotion vs conversion:" << endl;
    char c = 'A';
    rank1(c);            // char -> int (promotion) beats char -> long (conversion)
    
    cout << "\n3. Multiple parameters:" << endl;
    rank2(10, 20);       // int,int (exact)
    rank2(10, 20.5);     // int,double (exact match for second)
    rank2(10.5, 20);     // double,int (exact match for first)
    rank2(10.5, 20.5);   // double,double (exact)
    
    cout << "\n4. Reference binding:" << endl;
    int x = 10;
    rank3(x);            // lvalue reference (int&)
    const int y = 20;
    rank3(y);            // const lvalue reference (const int&)
    rank3(30);           // rvalue reference (int&&)
    
    return 0;
}
```

---

## 3. **Ambiguity in Overloading**

```cpp
#include <iostream>
#include <string>
using namespace std;

// Ambiguous overloads
void ambiguous(int a, double b) {
    cout << "ambiguous(int, double)" << endl;
}

void ambiguous(double a, int b) {
    cout << "ambiguous(double, int)" << endl;
}

void ambiguous(int a, int b) {
    cout << "ambiguous(int, int)" << endl;
}

void ambiguous(double a, double b) {
    cout << "ambiguous(double, double)" << endl;
}

// Another ambiguous example
void convert(int a) {
    cout << "convert(int): " << a << endl;
}

void convert(long a) {
    cout << "convert(long): " << a << endl;
}

void convert(float a) {
    cout << "convert(float): " << a << endl;
}

class Base {
public:
    virtual void func() { cout << "Base::func()" << endl; }
};

class Derived : public Base {
public:
    void func() override { cout << "Derived::func()" << endl; }
};

void handle(Base& b) {
    cout << "handle(Base&): ";
    b.func();
}

void handle(Derived& d) {
    cout << "handle(Derived&): ";
    d.func();
}

int main() {
    cout << "=== Ambiguity in Overloading ===" << endl;
    
    cout << "\n1. Ambiguous function calls:" << endl;
    // ambiguous(10, 20.5);  // ambiguous(int, double) - exact match
    // ambiguous(10.5, 20);  // ambiguous(double, int) - exact match
    // ambiguous(10, 20);    // ambiguous(int, int) - exact match
    
    cout << "   Use explicit casts to resolve:" << endl;
    ambiguous(static_cast<double>(10), 20.5);
    ambiguous(10.5, static_cast<int>(20));
    
    cout << "\n2. Ambiguous conversions:" << endl;
    // convert('A');        // ambiguous: char -> int, long, or float?
    convert(static_cast<int>('A'));  // Explicit cast resolves
    convert(10L);          // long - exact match
    convert(3.14f);        // float - exact match
    
    cout << "\n3. Inheritance ambiguity:" << endl;
    Derived d;
    Base& b = d;
    handle(b);   // handle(Base&) - base reference
    handle(d);   // handle(Derived&) - exact match preferred
    
    return 0;
}
```

---

## 4. **Overloading with Default Arguments**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Logger {
public:
    // Overloaded with default arguments
    void log(const string& msg, int level = 1) {
        cout << "[INFO] " << msg << " (level=" << level << ")" << endl;
    }
    
    // This would cause ambiguity with the default argument version
    // void log(const string& msg) {
    //     cout << "[INFO] " << msg << endl;
    // }
    
    // OK: different parameter types
    void log(int code) {
        cout << "[CODE] Error code: " << code << endl;
    }
    
    void log(const string& msg, const string& module) {
        cout << "[" << module << "] " << msg << endl;
    }
};

class Config {
public:
    // Default arguments can cause ambiguity with overloads
    void set(int value, bool enabled = true) {
        cout << "set(int, bool): " << value << ", " << enabled << endl;
    }
    
    void set(int value) {
        cout << "set(int): " << value << endl;
    }
    // set(int) and set(int, bool) are distinct - OK
    
    void set(double value) {
        cout << "set(double): " << value << endl;
    }
};

int main() {
    cout << "=== Overloading with Default Arguments ===" << endl;
    
    Logger logger;
    
    cout << "\n1. Logger with default arguments:" << endl;
    logger.log("Message with default level");
    logger.log("Message with custom level", 3);
    logger.log(404);  // Different overload
    logger.log("Module message", "Auth");
    
    cout << "\n2. Config with multiple overloads:" << endl;
    Config cfg;
    cfg.set(42);           // set(int)
    cfg.set(42, false);    // set(int, bool)
    cfg.set(3.14);         // set(double)
    
    cout << "\n3. Rules for default arguments:" << endl;
    cout << "   ✓ Cannot overload with functions that would be ambiguous" << endl;
    cout << "   ✓ Default arguments are not part of function signature" << endl;
    cout << "   ✓ Default arguments are resolved at compile time" << endl;
    
    return 0;
}
```

---

## 5. **Operator Overloading Rules**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Vector {
private:
    int x, y;
    
public:
    Vector(int xVal = 0, int yVal = 0) : x(xVal), y(yVal) {}
    
    // Member operator (left operand is *this)
    Vector operator+(const Vector& other) const {
        cout << "member operator+ called" << endl;
        return Vector(x + other.x, y + other.y);
    }
    
    // Member comparison
    bool operator==(const Vector& other) const {
        return x == other.x && y == other.y;
    }
    
    // Member compound assignment
    Vector& operator+=(const Vector& other) {
        x += other.x;
        y += other.y;
        return *this;
    }
    
    // Friend operator for symmetric operations
    friend Vector operator*(int scalar, const Vector& v) {
        cout << "friend operator* (scalar * vector) called" << endl;
        return Vector(scalar * v.x, scalar * v.y);
    }
    
    // Member operator for vector * scalar
    Vector operator*(int scalar) const {
        cout << "member operator* (vector * scalar) called" << endl;
        return Vector(x * scalar, y * scalar);
    }
    
    void display() const {
        cout << "(" << x << ", " << y << ")" << endl;
    }
};

// Non-member operator (can be defined outside)
Vector operator+(int scalar, const Vector& v) {
    cout << "non-member operator+ (scalar + vector) called" << endl;
    return Vector(scalar + v.x, scalar + v.y);
}

class Restricted {
public:
    // Cannot overload these operators
    // :: (scope resolution)
    // . (member access)
    // .* (pointer to member)
    // ?: (ternary conditional)
    
    // These can be overloaded
    int operator()() { return 42; }
    int operator[](int i) { return i * 2; }
};

int main() {
    cout << "=== Operator Overloading Rules ===" << endl;
    
    Vector v1(3, 4);
    Vector v2(1, 2);
    
    cout << "\n1. Member operators:" << endl;
    Vector v3 = v1 + v2;
    cout << "v1 + v2 = "; v3.display();
    
    cout << "\n2. Symmetric operators:" << endl;
    Vector v4 = v1 * 2;
    cout << "v1 * 2 = "; v4.display();
    Vector v5 = 3 * v1;
    cout << "3 * v1 = "; v5.display();
    
    cout << "\n3. Scalar + vector:" << endl;
    Vector v6 = 5 + v1;
    cout << "5 + v1 = "; v6.display();
    
    cout << "\n4. Operators that must be members:" << endl;
    cout << "   = (assignment)" << endl;
    cout << "   [] (subscript)" << endl;
    cout << "   () (function call)" << endl;
    cout << "   -> (member access)" << endl;
    
    cout << "\n5. Operators that cannot be overloaded:" << endl;
    cout << "   :: (scope resolution)" << endl;
    cout << "   . (member access)" << endl;
    cout << "   .* (pointer to member)" << endl;
    cout << "   ?: (ternary conditional)" << endl;
    
    return 0;
}
```

---

## 6. **Overloading Resolution in Templates**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Template function
template<typename T>
void process(T value) {
    cout << "template process(T): " << value << endl;
}

// Non-template overload
void process(int value) {
    cout << "non-template process(int): " << value << endl;
}

void process(double value) {
    cout << "non-template process(double): " << value << endl;
}

// Template specialization
template<>
void process<string>(string value) {
    cout << "specialized process<string>: " << value << endl;
}

// Multiple template parameters
template<typename T>
void compare(T a, T b) {
    cout << "compare(T,T): " << a << " vs " << b << endl;
}

template<typename T, typename U>
void compare(T a, U b) {
    cout << "compare(T,U): " << a << " vs " << b << endl;
}

class Number {
private:
    int value;
    
public:
    Number(int v) : value(v) {}
    operator int() const { return value; }
};

int main() {
    cout << "=== Overloading Resolution in Templates ===" << endl;
    
    cout << "\n1. Template vs non-template:" << endl;
    process(42);           // Non-template (exact match)
    process(3.14);         // Non-template (exact match)
    process("Hello");      // Template (const char*)
    
    cout << "\n2. Template specialization:" << endl;
    process(string("World"));  // Specialized version
    
    cout << "\n3. Template parameter deduction:" << endl;
    compare(10, 20);       // compare(T,T) - both int
    compare(10, 3.14);     // compare(T,U) - int and double
    
    cout << "\n4. User-defined conversion in templates:" << endl;
    Number n(100);
    process(n);            // Number -> int conversion, calls non-template process(int)
    compare(n, 50);        // Number converted to int, calls compare(T,T)
    
    return 0;
}
```

---

## 📊 Overloading Rules Summary

| Rule Category | Description |
|---------------|-------------|
| **Signature** | Function name + parameter list (not return type) |
| **Candidate Functions** | All functions with matching name |
| **Viable Functions** | Functions with matching parameter count and convertible arguments |
| **Ranking** | Exact > Promotion > Conversion > User-defined |
| **Ambiguity** | Occurs when multiple functions are equally good |
| **Default Arguments** | Not part of signature, can cause ambiguity |

---

## ✅ Best Practices

1. **Avoid ambiguous overloads** - Ensure unique signatures
2. **Use consistent parameter order** across overloads
3. **Document overloaded functions** clearly
4. **Prefer non-member operators** for symmetry
5. **Use `const` and `&` appropriately** for parameters
6. **Consider templates** as alternative to overloading

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Ambiguous calls** | Compiler error | Use explicit casts or unique signatures |
| **Default argument conflict** | Unexpected ambiguity | Avoid mixing defaults with overloads |
| **Const confusion** | Wrong overload called | Add const where appropriate |
| **Reference binding** | Unexpected selection | Understand lvalue/rvalue binding rules |
| **Template vs non-template** | Surprising selection | Know that non-templates are preferred |

---

## ✅ Key Takeaways

1. **Overload resolution** selects best matching function
2. **Ranking order**: Exact match > Promotion > Conversion
3. **Ambiguity** occurs when multiple functions are equally good
4. **Default arguments** are not part of function signature
5. **Non-template functions** are preferred over templates
6. **Reference binding** rules affect overload selection
7. **Use explicit casts** to resolve ambiguity

---
---

## Next Step

- Go to [Run Time Polymorphism](../02_Run_Time_Polymorphism/README.md) to continue forward.
