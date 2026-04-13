# README.md

## Compile-Time Polymorphism in C++ - Complete Guide

### Overview

Compile-time polymorphism, also known as static polymorphism or early binding, is a type of polymorphism where the function to be called is determined at compile time. It is achieved through function overloading and operator overloading. Compile-time polymorphism offers better performance since there is no runtime overhead for function dispatch.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [01_Function_Overloading.md](01_Function_Overloading.md) | understand Function Overloading |
| 2. | [02_Operator_Overloading.md](02_Operator_Overloading.md) | understand Operator Overloading |
| 3. | [03_Overloading_Rules.md](03_Overloading_Rules.md) | understand Overloading Rules |

---

## 1. Function Overloading

This topic explains how multiple functions can share the same name but different parameters.

**File:** [01_Function_Overloading.md](01_Function_Overloading.md)

**What you will learn:**
- Definition of function overloading
- Rules for overloading functions
- Different ways to overload (different number of parameters, different parameter types, different order of parameters)
- Return type cannot be used for overloading
- Function overloading resolution process
- Best practices for function overloading

**Key Concepts:**

| Concept | Description | Example |
|---------|-------------|---------|
| **Same Name** | Multiple functions share the same name | `void print(int); void print(double);` |
| **Different Parameters** | Must differ in number, type, or order of parameters | `add(int,int); add(int,int,int);` |
| **Return Type** | Cannot be used to differentiate overloaded functions | `int get(); double get();` // Invalid |
| **Default Arguments** | Can cause ambiguity with overloads | `void func(int); void func(int, int=0);` |

**Rules for Function Overloading:**
1. Functions must have the same name
2. Functions must have different parameter lists (number, type, or order)
3. Return type alone cannot distinguish overloaded functions
4. Const and non-const member functions can be overloaded
5. Reference and value parameters can be overloaded

**Syntax:**
```cpp
#include <iostream>
using namespace std;

// Function overloading examples

// 1. Different number of parameters
int add(int a, int b) {
    return a + b;
}

int add(int a, int b, int c) {
    return a + b + c;
}

// 2. Different parameter types
double add(double a, double b) {
    return a + b;
}

// 3. Different order of parameters
void display(int id, string name) {
    cout << "ID: " << id << ", Name: " << name << endl;
}

void display(string name, int id) {
    cout << "Name: " << name << ", ID: " << id << endl;
}

// 4. Const and non-const (for member functions)
class Printer {
public:
    void print(int x) {
        cout << "Non-const print: " << x << endl;
    }
    
    void print(int x) const {
        cout << "Const print: " << x << endl;
    }
};

// 5. Reference and value
void process(int x) {
    cout << "By value: " << x << endl;
}

void process(int& x) {
    cout << "By reference: " << x << endl;
}

int main() {
    // Calling overloaded functions
    cout << "add(5, 10): " << add(5, 10) << endl;
    cout << "add(5, 10, 15): " << add(5, 10, 15) << endl;
    cout << "add(5.5, 10.5): " << add(5.5, 10.5) << endl;
    
    display(101, "Alice");
    display("Bob", 102);
    
    // Const vs non-const
    Printer p1;
    const Printer p2;
    p1.print(100);  // Calls non-const version
    p2.print(200);  // Calls const version
    
    return 0;
}
```

**Invalid Overloading Examples:**
```cpp
// INVALID - Only return type differs
int getValue() { return 10; }
double getValue() { return 10.5; }  // Error!

// INVALID - Parameter names don't matter, only types
void func(int a) { }
void func(int b) { }  // Error - same parameter list

// INVALID - Ambiguous with default arguments
void func(int a) { }
void func(int a, int b = 0) { }  // func(5) is ambiguous
```

---

## 2. Operator Overloading

This topic explains how to define custom behavior for operators when used with user-defined types.

**File:** [02_Operator_Overloading.md](02_Operator_Overloading.md)

**What you will learn:**
- What is operator overloading
- Which operators can be overloaded
- Which operators cannot be overloaded
- Syntax for operator overloading (member function vs friend function)
- Overloading unary operators (++, --, -, !)
- Overloading binary operators (+, -, *, /, ==, !=, <, >)
- Overloading subscript operator `[]`
- Overloading function call operator `()`
- Overloading stream insertion `<<` and extraction `>>` operators

**Key Concepts:**

| Operator Type | Can Overload? | Examples |
|--------------|---------------|----------|
| **Arithmetic** | Yes | `+ - * / %` |
| **Relational** | Yes | `== != < > <= >=` |
| **Logical** | Yes (but avoid) | `&& || !` |
| **Bitwise** | Yes | `& | ^ ~ << >>` |
| **Assignment** | Yes | `= += -= *= /=` |
| **Increment/Decrement** | Yes | `++ --` |
| **Subscript** | Yes | `[]` |
| **Function Call** | Yes | `()` |
| **Member Access** | No | `.` `.*` |
| **Scope Resolution** | No | `::` |
| **Ternary** | No | `?:` |
| **Sizeof** | No | `sizeof` |
| **Typeid** | No | `typeid` |

**Syntax - Member Function (Unary Operator):**
```cpp
class Counter {
private:
    int value_;
    
public:
    Counter(int v = 0) : value_(v) {}
    
    // Prefix increment (++c)
    Counter& operator++() {
        value_++;
        return *this;
    }
    
    // Postfix increment (c++)
    Counter operator++(int) {
        Counter temp = *this;
        value_++;
        return temp;
    }
    
    // Unary minus (-c)
    Counter operator-() const {
        return Counter(-value_);
    }
    
    int getValue() const { return value_; }
};
```

**Syntax - Member Function (Binary Operator):**
```cpp
class Complex {
private:
    double real_, imag_;
    
public:
    Complex(double r = 0, double i = 0) : real_(r), imag_(i) {}
    
    // Binary + operator
    Complex operator+(const Complex& other) const {
        return Complex(real_ + other.real_, imag_ + other.imag_);
    }
    
    // Binary - operator
    Complex operator-(const Complex& other) const {
        return Complex(real_ - other.real_, imag_ - other.imag_);
    }
    
    // Equality operator
    bool operator==(const Complex& other) const {
        return (real_ == other.real_ && imag_ == other.imag_);
    }
    
    // Subscript operator
    double operator[](int index) const {
        if (index == 0) return real_;
        if (index == 1) return imag_;
        throw out_of_range("Index must be 0 or 1");
    }
    
    // Function call operator
    double operator()(double r, double i) {
        real_ = r;
        imag_ = i;
        return real_ + imag_;
    }
    
    void display() const {
        cout << real_ << " + " << imag_ << "i" << endl;
    }
};
```

**Syntax - Friend Function (For Stream Operators):**
```cpp
class Vector3D {
private:
    double x_, y_, z_;
    
public:
    Vector3D(double x = 0, double y = 0, double z = 0) : x_(x), y_(y), z_(z) {}
    
    // Friend function for << operator
    friend ostream& operator<<(ostream& os, const Vector3D& v) {
        os << "(" << v.x_ << ", " << v.y_ << ", " << v.z_ << ")";
        return os;
    }
    
    // Friend function for >> operator
    friend istream& operator>>(istream& is, Vector3D& v) {
        cout << "Enter x y z: ";
        is >> v.x_ >> v.y_ >> v.z_;
        return is;
    }
    
    // Friend function for + operator (when left operand is not the class)
    friend Vector3D operator+(const Vector3D& v1, const Vector3D& v2) {
        return Vector3D(v1.x_ + v2.x_, v1.y_ + v2.y_, v1.z_ + v2.z_);
    }
};

// Usage
int main() {
    Vector3D v1(1, 2, 3);
    Vector3D v2(4, 5, 6);
    
    Vector3D v3 = v1 + v2;
    cout << v3 << endl;  // Output: (5, 7, 9)
    
    return 0;
}
```

---

## 3. Overloading Rules

This topic explains the rules, limitations, and best practices for overloading functions and operators.

**File:** [03_Overloading_Rules.md](03_Overloading_Rules.md)

**What you will learn:**
- Rules for function overloading
- Rules for operator overloading
- Functions that cannot be overloaded
- Operators that cannot be overloaded
- Ambiguity in overloading
- Name mangling mechanism
- Best practices for overloading

**Key Concepts:**

| Rule Category | Description |
|---------------|-------------|
| **Function Overloading** | Functions must differ in parameter list (number, type, or order) |
| **Return Type** | Cannot be used to differentiate overloaded functions |
| **Const Overloading** | Const and non-const member functions can be overloaded |
| **Default Arguments** | Can cause ambiguity with overloaded functions |
| **Operator Overloading** | Cannot change precedence or associativity |
| **Operator Arity** | Cannot change number of operands |
| **New Operators** | Cannot create new operators (e.g., ** for exponent) |

**Functions That Cannot Be Overloaded:**
```cpp
// 1. Functions that differ only in return type
int getValue();
double getValue();  // Error

// 2. Functions that differ only in parameter names
void process(int a);
void process(int b);  // Error

// 3. Functions with same parameter types but different typedef names
typedef int Age;
typedef int Score;
void display(Age a);
void display(Score s);  // Error - same type (int)

// 4. Non-member functions with same name but different const
void func(int x);
void func(const int x);  // Error - top-level const ignored
```

**Operators That Cannot Be Overloaded:**
```cpp
// Cannot overload these operators:
// ::     - Scope resolution
// .      - Member access
// .*     - Pointer to member access
// ?:     - Ternary conditional
// sizeof - Size of operator
// typeid - Type identification
// alignof - Alignment operator
// noexcept - Exception specifier
```

**Best Practices for Overloading:**
```cpp
// 1. Maintain natural semantics
class Fraction {
public:
    // Good: + returns a new Fraction
    Fraction operator+(const Fraction& other) const {
        return Fraction(numerator_ * other.denominator_ + other.numerator_ * denominator_,
                        denominator_ * other.denominator_);
    }
    
    // Bad: + should not modify the object
    // Fraction& operator+(const Fraction& other) { /* modifies this */ }
};

// 2. Provide symmetric operators as friend functions
class Number {
private:
    int value_;
public:
    Number(int v) : value_(v) {}
    
    // Friend function allows 5 + num and num + 5
    friend Number operator+(int left, const Number& right) {
        return Number(left + right.value_);
    }
    
    Number operator+(int right) const {
        return Number(value_ + right);
    }
};

// 3. Overload << and >> as friend functions
class Person {
private:
    string name_;
    int age_;
public:
    friend ostream& operator<<(ostream& os, const Person& p) {
        os << p.name_ << " (" << p.age_ << ")";
        return os;
    }
};

// 4. Use const correctness
class Matrix {
public:
    // Const version for reading
    int get(int row, int col) const;
    
    // Non-const version for writing
    int& get(int row, int col);
};
```

**Ambiguity Examples:**
```cpp
// Ambiguity 1: Default arguments
void func(int a) { }
void func(int a, int b = 0) { }
// func(5);  // Ambiguous - which one to call?

// Ambiguity 2: Type conversion
void func(double d) { }
void func(float f) { }
// func(5);  // Ambiguous - int can convert to both

// Ambiguity 3: Reference vs value
void process(int x) { }
void process(int& x) { }
// int a = 5; process(a);  // Ambiguous

// Resolution: Use explicit casting or redesign
func(static_cast<double>(5));  // Calls double version
```

---

### Compile-Time Polymorphism Summary

| Feature | Function Overloading | Operator Overloading |
|---------|---------------------|---------------------|
| **Purpose** | Same name, different behaviors | Custom operator behavior for user types |
| **Resolution** | Compile time (by parameters) | Compile time (by operand types) |
| **Performance** | No overhead | No overhead |
| **Flexibility** | High | Medium (limited by operator rules) |
| **Complexity** | Low | Medium to High |

---

### Prerequisites

Before starting this section, you should have completed:

- [01. Basics](../../../01.%20Basics/README.md) - Functions, operators
- [02_Classes_and_Objects/README.md](../../02_Classes_and_Objects/README.md) - Class basics
- [03_Constructors_and_Destructors/README.md](../../03_Constructors_and_Destructors/README.md) - Object initialization

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Overloading only by return type | Not allowed - use different parameters |
| Creating ambiguous overloads | Avoid default arguments that cause ambiguity |
| Overloading with different meaning | Maintain natural semantics (e.g., + should add) |
| Forgetting const for read-only operations | Mark getters and non-modifying operators const |
| Not providing symmetric operators | Provide friend functions for left operand conversion |
| Overloading operators that shouldn't be overloaded (&&, ||) | Avoid - short-circuit behavior lost |

---

### Practice Questions

After completing this section, you should be able to:

1. Define function overloading and list its rules
2. Write overloaded functions for different parameter types
3. Explain why return type cannot be used for overloading
4. List operators that can and cannot be overloaded
5. Overload the + operator for a custom class
6. Overload the << operator for output
7. Distinguish between prefix and postfix increment overloading
8. Identify and resolve ambiguous overloads

---

### Next Steps

- Go to [01_Function_Overloading.md](01_Function_Overloading.md) to understand Function Overloading.