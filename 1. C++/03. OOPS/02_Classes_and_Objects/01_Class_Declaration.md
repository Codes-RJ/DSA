# Class Declaration in C++ - Complete Guide

## 📖 Overview

A class declaration defines a new user-defined data type that encapsulates data and functions. It serves as a blueprint for creating objects. Understanding how to properly declare classes is fundamental to object-oriented programming in C++.

---

## 🎯 Basic Class Declaration Syntax

### Simple Class Declaration

```cpp
#include <iostream>
#include <string>
using namespace std;

// Basic class declaration
class Student {
public:
    // Data members (attributes)
    string name;
    int rollNumber;
    float marks;
    
    // Member functions (methods)
    void display() {
        cout << "Name: " << name << endl;
        cout << "Roll Number: " << rollNumber << endl;
        cout << "Marks: " << marks << endl;
    }
};

int main() {
    Student s1;
    s1.name = "Alice";
    s1.rollNumber = 101;
    s1.marks = 85.5;
    s1.display();
    
    return 0;
}
```

**Output:**
```
Name: Alice
Roll Number: 101
Marks: 85.5
```

---

## 📝 Complete Class Declaration Structure

```cpp
// Forward declaration (optional)
class ClassName;

// Class declaration
class ClassName {
private:
    // Private data members (encapsulated)
    int privateData;
    string privateString;
    
protected:
    // Protected members (accessible to derived classes)
    int protectedData;
    
public:
    // Constructors
    ClassName();                              // Default constructor
    ClassName(int param);                     // Parameterized constructor
    ClassName(const ClassName& other);        // Copy constructor
    ClassName(ClassName&& other) noexcept;    // Move constructor (C++11)
    
    // Destructor
    ~ClassName();                              // Destructor
    
    // Member functions
    void publicMethod();                       // Public method
    int getPrivateData() const;                // Getter
    void setPrivateData(int value);            // Setter
    
    // Static members
    static int staticData;                     // Static data member
    static void staticMethod();                // Static method
    
    // Operator overloads
    ClassName& operator=(const ClassName& other);  // Copy assignment
    
    // Friend declarations
    friend void friendFunction(ClassName& obj);     // Friend function
    friend class FriendClass;                       // Friend class
};

// Static member definition (outside class)
int ClassName::staticData = 0;

// Member function definitions (outside class)
ClassName::ClassName() : privateData(0), privateString("") {
    // Constructor body
}

void ClassName::publicMethod() {
    // Method implementation
}
```

---

## 🔧 Different Class Declaration Styles

### 1. **All Members Public (Simple Structure)**

```cpp
// Simple data structure (like C struct)
class Point {
public:
    int x;
    int y;
    
    void display() {
        cout << "(" << x << ", " << y << ")" << endl;
    }
};

int main() {
    Point p;
    p.x = 10;
    p.y = 20;
    p.display();
    
    return 0;
}
```

### 2. **Encapsulated Class (Data Hiding)**

```cpp
class BankAccount {
private:
    string accountNumber;
    double balance;
    string pin;
    
public:
    BankAccount(string accNo, double initial, string p) {
        accountNumber = accNo;
        balance = initial;
        pin = p;
    }
    
    bool deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            return true;
        }
        return false;
    }
    
    bool withdraw(double amount, string inputPin) {
        if (inputPin != pin) {
            cout << "Invalid PIN!" << endl;
            return false;
        }
        
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            return true;
        }
        return false;
    }
    
    double getBalance(string inputPin) {
        if (inputPin == pin) {
            return balance;
        }
        return -1;
    }
};

int main() {
    BankAccount account("12345678", 1000, "1234");
    
    account.deposit(500);
    account.withdraw(200, "1234");
    
    cout << "Balance: " << account.getBalance("1234") << endl;
    
    // Cannot access private members directly
    // account.balance = 9999;  // Error!
    
    return 0;
}
```

### 3. **Class with Constant Members**

```cpp
class Employee {
private:
    const int employeeID;      // Must be initialized in constructor
    string name;
    static int nextID;          // Static counter
    
public:
    Employee(string n) : employeeID(nextID++) {
        name = n;
    }
    
    void display() const {      // Const method - doesn't modify object
        cout << "ID: " << employeeID << ", Name: " << name << endl;
    }
    
    int getID() const { return employeeID; }
};

int Employee::nextID = 1000;    // Initialize static member

int main() {
    Employee e1("Alice");
    Employee e2("Bob");
    Employee e3("Charlie");
    
    e1.display();  // ID: 1000, Name: Alice
    e2.display();  // ID: 1001, Name: Bob
    e3.display();  // ID: 1002, Name: Charlie
    
    return 0;
}
```

---

## 📐 Class Declaration Modifiers

### 1. **`const` Member Functions**

```cpp
class Date {
private:
    int day, month, year;
    
public:
    Date(int d, int m, int y) : day(d), month(m), year(y) {}
    
    // Const method - cannot modify object
    void display() const {
        cout << day << "/" << month << "/" << year << endl;
        // day = 1;  // Error! Cannot modify in const method
    }
    
    // Non-const method - can modify
    void setDay(int d) {
        day = d;
    }
    
    // Overloaded based on const-ness
    int& operator[](int index) {
        return index == 0 ? day : (index == 1 ? month : year);
    }
    
    const int& operator[](int index) const {
        return index == 0 ? day : (index == 1 ? month : year);
    }
};

int main() {
    Date d1(15, 3, 2024);
    const Date d2(25, 12, 2024);
    
    d1.display();     // OK - non-const object can call const method
    d2.display();     // OK - const object calls const overload
    
    d1.setDay(20);    // OK
    // d2.setDay(20); // Error! const object can't call non-const method
    
    return 0;
}
```

### 2. **`static` Members**

```cpp
class Counter {
private:
    static int count;        // Shared across all objects
    int instanceID;
    
public:
    Counter() {
        instanceID = ++count;
        cout << "Object " << instanceID << " created" << endl;
    }
    
    ~Counter() {
        cout << "Object " << instanceID << " destroyed" << endl;
    }
    
    static int getCount() {   // Static method
        return count;
    }
    
    int getInstanceID() const {
        return instanceID;
    }
};

int Counter::count = 0;       // Initialize static member

int main() {
    cout << "Initial count: " << Counter::getCount() << endl;
    
    Counter c1;
    Counter c2;
    Counter c3;
    
    cout << "Total objects: " << Counter::getCount() << endl;
    
    return 0;
}
```

### 3. **`mutable` Members**

```cpp
class Logger {
private:
    string name;
    mutable int accessCount;    // Can be modified in const methods
    
public:
    Logger(string n) : name(n), accessCount(0) {}
    
    void log(const string& message) const {
        accessCount++;          // Allowed even in const method
        cout << "[" << name << "] " << message << endl;
    }
    
    int getAccessCount() const {
        return accessCount;
    }
};

int main() {
    const Logger logger("System");
    
    logger.log("Starting up");
    logger.log("Processing data");
    logger.log("Shutting down");
    
    cout << "Log count: " << logger.getAccessCount() << endl;
    
    return 0;
}
```

---

## 🏗️ Class Declaration Best Practices

### 1. **Separation of Interface and Implementation**

```cpp
// ---------- Rectangle.h ----------
#ifndef RECTANGLE_H
#define RECTANGLE_H

class Rectangle {
private:
    double width;
    double height;
    
public:
    Rectangle(double w, double h);
    double area() const;
    double perimeter() const;
    void scale(double factor);
    void display() const;
};

#endif

// ---------- Rectangle.cpp ----------
#include "Rectangle.h"
#include <iostream>
using namespace std;

Rectangle::Rectangle(double w, double h) : width(w), height(h) {}

double Rectangle::area() const {
    return width * height;
}

double Rectangle::perimeter() const {
    return 2 * (width + height);
}

void Rectangle::scale(double factor) {
    width *= factor;
    height *= factor;
}

void Rectangle::display() const {
    cout << "Rectangle: " << width << " x " << height << endl;
    cout << "Area: " << area() << ", Perimeter: " << perimeter() << endl;
}

// ---------- main.cpp ----------
#include "Rectangle.h"

int main() {
    Rectangle rect(10, 5);
    rect.display();
    rect.scale(2);
    rect.display();
    
    return 0;
}
```

### 2. **Use Initialization Lists**

```cpp
class Student {
private:
    const int rollNumber;     // Must use initialization list
    string& name;              // Reference must use initialization list
    int age;
    
public:
    // Correct: Using initialization list
    Student(int roll, string& n, int a) 
        : rollNumber(roll), name(n), age(a) {
        // Constructor body
    }
    
    // Wrong: Assignment in body
    // Student(int roll, string& n, int a) {
    //     rollNumber = roll;  // Error! const can't be assigned
    //     name = n;           // Error! reference can't be assigned
    //     age = a;
    // }
};
```

### 3. **Forward Declarations for Circular Dependencies**

```cpp
// Forward declarations
class ClassB;

class ClassA {
private:
    ClassB* b;        // Pointer to forward-declared class
    
public:
    void setB(ClassB* ptr);
    void callB();
};

class ClassB {
private:
    ClassA a;         // Can use complete type
    
public:
    void callA();
};

// Implementation can include full definitions
#include "ClassA.h"
#include "ClassB.h"

void ClassA::callB() {
    // Now ClassB is fully defined
}
```

---

## 🎮 Complete Example: Complex Number Class

```cpp
#include <iostream>
#include <cmath>
using namespace std;

class Complex {
private:
    double real;
    double imag;
    
public:
    // Constructors
    Complex() : real(0), imag(0) {}
    Complex(double r, double i) : real(r), imag(i) {}
    Complex(const Complex& other) : real(other.real), imag(other.imag) {}
    
    // Destructor
    ~Complex() {
        // No dynamic memory to free
    }
    
    // Accessors
    double getReal() const { return real; }
    double getImag() const { return imag; }
    void setReal(double r) { real = r; }
    void setImag(double i) { imag = i; }
    
    // Arithmetic operations
    Complex add(const Complex& other) const {
        return Complex(real + other.real, imag + other.imag);
    }
    
    Complex subtract(const Complex& other) const {
        return Complex(real - other.real, imag - other.imag);
    }
    
    Complex multiply(const Complex& other) const {
        return Complex(
            real * other.real - imag * other.imag,
            real * other.imag + imag * other.real
        );
    }
    
    Complex conjugate() const {
        return Complex(real, -imag);
    }
    
    double magnitude() const {
        return sqrt(real * real + imag * imag);
    }
    
    // Display
    void display() const {
        cout << real;
        if (imag >= 0) cout << " + " << imag << "i";
        else cout << " - " << -imag << "i";
    }
    
    // Static methods
    static Complex fromPolar(double magnitude, double angle) {
        return Complex(magnitude * cos(angle), magnitude * sin(angle));
    }
};

int main() {
    Complex c1(3, 4);
    Complex c2(1, -2);
    
    cout << "c1 = "; c1.display(); cout << endl;
    cout << "c2 = "; c2.display(); cout << endl;
    
    Complex sum = c1.add(c2);
    cout << "Sum = "; sum.display(); cout << endl;
    
    Complex product = c1.multiply(c2);
    cout << "Product = "; product.display(); cout << endl;
    
    cout << "|c1| = " << c1.magnitude() << endl;
    
    Complex polar = Complex::fromPolar(5, 3.14159 / 4);
    cout << "From polar: "; polar.display(); cout << endl;
    
    return 0;
}
```

**Output:**
```
c1 = 3 + 4i
c2 = 1 - 2i
Sum = 4 + 2i
Product = 11 - 2i
|c1| = 5
From polar: 3.53553 + 3.53553i
```

---

## 📊 Class Declaration Summary

| Component | Syntax | Purpose |
|-----------|--------|---------|
| **Class Keyword** | `class ClassName { ... };` | Defines a new class type |
| **Data Members** | `type name;` | Store object state |
| **Member Functions** | `returnType name(params);` | Define object behavior |
| **Access Specifiers** | `public:`, `private:`, `protected:` | Control visibility |
| **Constructor** | `ClassName(params);` | Initialize objects |
| **Destructor** | `~ClassName();` | Clean up resources |
| **Static Member** | `static type name;` | Shared across objects |
| **Const Member** | `returnType name() const;` | Read-only methods |

---

## ✅ Key Takeaways

1. **Class declaration** defines the blueprint for objects
2. **Access specifiers** control member visibility (`public`, `private`, `protected`)
3. **Constructors** initialize objects; **destructors** clean up
4. **Static members** belong to the class, not individual objects
5. **Const methods** promise not to modify the object
6. **Initialization lists** are preferred over assignment in constructors
7. **Separate interface** (header) from implementation (cpp) for large projects

---

## 🐛 Common Pitfalls

| Pitfall | Explanation | Solution |
|---------|-------------|----------|
| Missing semicolon after class | `class MyClass { }` | Add semicolon: `class MyClass { };` |
| Forgetting to define static members | `static int count;` only declared | Define in cpp: `int MyClass::count = 0;` |
| Const method modifying data | `void func() const { data = 1; }` | Use `mutable` or remove `const` |
| Not using initialization list for const/reference | Const members must be initialized | Use member initializer list |

---