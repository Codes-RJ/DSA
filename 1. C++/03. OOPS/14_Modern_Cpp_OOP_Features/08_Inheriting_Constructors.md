# Inheriting Constructors in C++ - Complete Guide

## 📖 Overview

Inheriting constructors (C++11) allow a derived class to inherit constructors from its base class. This feature eliminates the need to write boilerplate constructors in derived classes that simply forward arguments to the base class constructor. It significantly reduces code duplication in class hierarchies.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Constructor Inheritance** | Derived class inherits base class constructors |
| **`using` Declaration** | Brings base constructors into derived class scope |
| **Default Arguments** | Inherited constructors preserve default arguments |
| **Overriding** | Derived class can provide its own constructors |

---

## 1. **Basic Constructor Inheritance**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Base {
protected:
    int value_;
    string name_;
    
public:
    Base() : value_(0), name_("Default") {
        cout << "Base default constructor" << endl;
    }
    
    Base(int v) : value_(v), name_("Value") {
        cout << "Base(int) constructor: " << value_ << endl;
    }
    
    Base(string n) : value_(0), name_(n) {
        cout << "Base(string) constructor: " << name_ << endl;
    }
    
    Base(int v, string n) : value_(v), name_(n) {
        cout << "Base(int, string) constructor: " << value_ << ", " << name_ << endl;
    }
    
    void display() const {
        cout << "Value: " << value_ << ", Name: " << name_ << endl;
    }
};

// Derived class inheriting constructors
class Derived : public Base {
public:
    // Inherit all constructors from Base
    using Base::Base;
    
    // Additional member
    void derivedOnly() {
        cout << "Derived specific method" << endl;
    }
};

int main() {
    cout << "=== Basic Constructor Inheritance ===" << endl;
    
    cout << "\n1. Using inherited constructors:" << endl;
    Derived d1;              // Base default constructor
    Derived d2(42);          // Base(int) constructor
    Derived d3("Hello");     // Base(string) constructor
    Derived d4(100, "World"); // Base(int, string) constructor
    
    cout << "\n2. Displaying objects:" << endl;
    d1.display();
    d2.display();
    d3.display();
    d4.display();
    
    cout << "\n3. Derived specific method:" << endl;
    d4.derivedOnly();
    
    return 0;
}
```

**Output:**
```
=== Basic Constructor Inheritance ===

1. Using inherited constructors:
Base default constructor
Base(int) constructor: 42
Base(string) constructor: Hello
Base(int, string) constructor: 100, World

2. Displaying objects:
Value: 0, Name: Default
Value: 42, Name: Value
Value: 0, Name: Hello
Value: 100, Name: World

3. Derived specific method:
Derived specific method
```

---

## 2. **Inheriting with Additional Members**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Shape {
protected:
    string color_;
    
public:
    Shape() : color_("Black") {
        cout << "Shape default constructor" << endl;
    }
    
    Shape(string c) : color_(c) {
        cout << "Shape(string) constructor: " << color_ << endl;
    }
    
    virtual double area() const = 0;
    virtual ~Shape() = default;
};

class Circle : public Shape {
private:
    double radius_;
    
public:
    // Inherit constructors from Shape
    using Shape::Shape;
    
    // Additional constructor for radius
    Circle(double r) : Shape(), radius_(r) {
        cout << "Circle(double) constructor: radius=" << radius_ << endl;
    }
    
    Circle(string c, double r) : Shape(c), radius_(r) {
        cout << "Circle(string, double) constructor: " << color_ << ", radius=" << radius_ << endl;
    }
    
    double area() const override {
        return 3.14159 * radius_ * radius_;
    }
    
    void display() const {
        cout << "Circle: color=" << color_ << ", radius=" << radius_ 
             << ", area=" << area() << endl;
    }
};

class Rectangle : public Shape {
private:
    double width_, height_;
    
public:
    // Inherit constructors
    using Shape::Shape;
    
    // Additional constructors
    Rectangle(double w, double h) : Shape(), width_(w), height_(h) {
        cout << "Rectangle(double, double) constructor: " << width_ << "x" << height_ << endl;
    }
    
    Rectangle(string c, double w, double h) : Shape(c), width_(w), height_(h) {
        cout << "Rectangle(string, double, double) constructor: " 
             << color_ << ", " << width_ << "x" << height_ << endl;
    }
    
    double area() const override {
        return width_ * height_;
    }
    
    void display() const {
        cout << "Rectangle: color=" << color_ << ", size=" << width_ << "x" << height_ 
             << ", area=" << area() << endl;
    }
};

int main() {
    cout << "=== Inheriting with Additional Members ===" << endl;
    
    cout << "\n1. Circle using inherited constructors:" << endl;
    Circle c1;                    // Inherited Shape default
    Circle c2("Red");             // Inherited Shape(string)
    Circle c3(5.0);               // Circle's own constructor
    Circle c4("Blue", 7.0);       // Circle's own constructor
    
    c1.display();
    c2.display();
    c3.display();
    c4.display();
    
    cout << "\n2. Rectangle using inherited constructors:" << endl;
    Rectangle r1;                 // Inherited Shape default
    Rectangle r2("Green");        // Inherited Shape(string)
    Rectangle r3(4.0, 6.0);       // Rectangle's own constructor
    Rectangle r4("Yellow", 5.0, 8.0); // Rectangle's own constructor
    
    r1.display();
    r2.display();
    r3.display();
    r4.display();
    
    return 0;
}
```

---

## 3. **Constructor Inheritance with Default Arguments**

```cpp
#include <iostream>
#include <string>
#include <chrono>
#include <ctime>
using namespace std;

class Logger {
protected:
    string prefix_;
    int level_;
    bool timestamp_;
    
public:
    // Constructor with default arguments
    Logger(string prefix = "INFO", int level = 1, bool timestamp = true) 
        : prefix_(prefix), level_(level), timestamp_(timestamp) {
        cout << "Logger created: " << prefix_ << " (level=" << level_ 
             << ", timestamp=" << timestamp_ << ")" << endl;
    }
    
    void log(const string& message) {
        if (timestamp_) {
            auto now = chrono::system_clock::now();
            auto time = chrono::system_clock::to_time_t(now);
            cout << ctime(&time) << " ";
        }
        cout << "[" << prefix_ << "] " << message << endl;
    }
};

class FileLogger : public Logger {
private:
    string filename_;
    
public:
    // Inherit constructors (including default arguments)
    using Logger::Logger;
    
    // Additional constructor
    FileLogger(string filename, string prefix = "FILE", int level = 1, bool timestamp = true)
        : Logger(prefix, level, timestamp), filename_(filename) {
        cout << "FileLogger created: " << filename_ << endl;
    }
    
    void logToFile(const string& message) {
        cout << "[FILE:" << filename_ << "] " << message << endl;
    }
};

class DatabaseLogger : public Logger {
private:
    string connection_;
    
public:
    // Inherit constructors
    using Logger::Logger;
    
    // Additional constructor
    DatabaseLogger(string conn, string prefix = "DB", int level = 1, bool timestamp = true)
        : Logger(prefix, level, timestamp), connection_(conn) {
        cout << "DatabaseLogger created: " << connection_ << endl;
    }
    
    void logToDB(const string& message) {
        cout << "[DB:" << connection_ << "] " << message << endl;
    }
};

int main() {
    cout << "=== Constructor Inheritance with Default Arguments ===" << endl;
    
    cout << "\n1. Logger (base class):" << endl;
    Logger l1;
    Logger l2("DEBUG");
    Logger l3("WARN", 2);
    Logger l4("ERROR", 3, false);
    
    l1.log("Message 1");
    l2.log("Message 2");
    l3.log("Message 3");
    l4.log("Message 4");
    
    cout << "\n2. FileLogger (derived with inherited constructors):" << endl;
    FileLogger f1;                    // Inherited Logger default
    FileLogger f2("DEBUG");           // Inherited Logger(string)
    FileLogger f3("app.log", "FILE"); // Own constructor
    
    f1.log("Log to console");
    f2.logToFile("Log to file");
    f3.logToFile("Custom file log");
    
    cout << "\n3. DatabaseLogger (derived with inherited constructors):" << endl;
    DatabaseLogger db1;
    DatabaseLogger db2("postgresql://localhost/db", "DB", 2);
    
    db1.logToDB("Database log 1");
    db2.logToDB("Database log 2");
    
    return 0;
}
```

---

## 4. **Overriding Inherited Constructors**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Employee {
protected:
    string name_;
    int id_;
    double salary_;
    static int nextId_;
    
public:
    Employee() : name_("Unknown"), id_(nextId_++), salary_(0.0) {
        cout << "Employee default constructor: " << name_ << " (ID: " << id_ << ")" << endl;
    }
    
    Employee(string name) : name_(name), id_(nextId_++), salary_(0.0) {
        cout << "Employee(string) constructor: " << name_ << " (ID: " << id_ << ")" << endl;
    }
    
    Employee(string name, double salary) : name_(name), id_(nextId_++), salary_(salary) {
        cout << "Employee(string, double) constructor: " << name_ 
             << " (ID: " << id_ << ", salary: $" << salary_ << ")" << endl;
    }
    
    virtual void display() const {
        cout << "ID: " << id_ << ", Name: " << name_ << ", Salary: $" << salary_ << endl;
    }
    
    virtual ~Employee() = default;
};

int Employee::nextId_ = 1000;

class Manager : public Employee {
private:
    int teamSize_;
    
public:
    // Inherit base constructors
    using Employee::Employee;
    
    // Override default constructor
    Manager() : Employee("Default Manager", 0.0), teamSize_(0) {
        cout << "Manager default constructor (overridden)" << endl;
    }
    
    // Additional constructor
    Manager(string name, double salary, int teamSize) 
        : Employee(name, salary), teamSize_(teamSize) {
        cout << "Manager(string, double, int) constructor: team size=" << teamSize << endl;
    }
    
    void display() const override {
        Employee::display();
        cout << "  Team Size: " << teamSize_ << endl;
    }
};

class Developer : public Employee {
private:
    string language_;
    
public:
    // Inherit base constructors
    using Employee::Employee;
    
    // Additional constructor
    Developer(string name, double salary, string lang) 
        : Employee(name, salary), language_(lang) {
        cout << "Developer(string, double, string) constructor: language=" << lang << endl;
    }
    
    void display() const override {
        Employee::display();
        cout << "  Language: " << language_ << endl;
    }
};

int main() {
    cout << "=== Overriding Inherited Constructors ===" << endl;
    
    cout << "\n1. Using inherited constructors:" << endl;
    Developer d1;                    // Inherited Employee default
    Developer d2("Alice");           // Inherited Employee(string)
    Developer d3("Bob", 75000);      // Inherited Employee(string, double)
    Developer d4("Charlie", 85000, "C++"); // Own constructor
    
    d1.display();
    d2.display();
    d3.display();
    d4.display();
    
    cout << "\n2. Manager with overridden default constructor:" << endl;
    Manager m1;                      // Overridden default constructor
    Manager m2("Diana", 95000, 5);   // Own constructor
    Manager m3("Eve");               // Inherited Employee(string)
    Manager m4("Frank", 80000);      // Inherited Employee(string, double)
    
    m1.display();
    m2.display();
    m3.display();
    m4.display();
    
    return 0;
}
```

---

## 5. **Practical Example: Shape Hierarchy**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <cmath>
using namespace std;

class Shape {
protected:
    string color_;
    
public:
    Shape() : color_("Black") {
        cout << "Shape default constructor" << endl;
    }
    
    Shape(string color) : color_(color) {
        cout << "Shape(string) constructor: " << color_ << endl;
    }
    
    virtual double area() const = 0;
    virtual void draw() const = 0;
    virtual ~Shape() = default;
};

class Circle : public Shape {
private:
    double radius_;
    
public:
    using Shape::Shape;
    
    Circle(double r) : Shape(), radius_(r) {
        cout << "Circle(double) constructor: radius=" << radius_ << endl;
    }
    
    Circle(string c, double r) : Shape(c), radius_(r) {
        cout << "Circle(string, double) constructor: " << color_ << ", radius=" << radius_ << endl;
    }
    
    double area() const override {
        return M_PI * radius_ * radius_;
    }
    
    void draw() const override {
        cout << "Drawing " << color_ << " circle with radius " << radius_ << endl;
    }
};

class Rectangle : public Shape {
private:
    double width_, height_;
    
public:
    using Shape::Shape;
    
    Rectangle(double w, double h) : Shape(), width_(w), height_(h) {
        cout << "Rectangle(double, double) constructor: " << width_ << "x" << height_ << endl;
    }
    
    Rectangle(string c, double w, double h) : Shape(c), width_(w), height_(h) {
        cout << "Rectangle(string, double, double) constructor: " 
             << color_ << ", " << width_ << "x" << height_ << endl;
    }
    
    double area() const override {
        return width_ * height_;
    }
    
    void draw() const override {
        cout << "Drawing " << color_ << " rectangle " << width_ << "x" << height_ << endl;
    }
};

class Triangle : public Shape {
private:
    double base_, height_;
    
public:
    using Shape::Shape;
    
    Triangle(double b, double h) : Shape(), base_(b), height_(h) {
        cout << "Triangle(double, double) constructor: base=" << base_ << ", height=" << height_ << endl;
    }
    
    Triangle(string c, double b, double h) : Shape(c), base_(b), height_(h) {
        cout << "Triangle(string, double, double) constructor: " 
             << color_ << ", base=" << base_ << ", height=" << height_ << endl;
    }
    
    double area() const override {
        return 0.5 * base_ * height_;
    }
    
    void draw() const override {
        cout << "Drawing " << color_ << " triangle with base " << base_ 
             << " and height " << height_ << endl;
    }
};

class ShapeFactory {
public:
    static unique_ptr<Shape> createCircle(const string& color, double radius) {
        return make_unique<Circle>(color, radius);
    }
    
    static unique_ptr<Shape> createRectangle(const string& color, double w, double h) {
        return make_unique<Rectangle>(color, w, h);
    }
    
    static unique_ptr<Shape> createTriangle(const string& color, double b, double h) {
        return make_unique<Triangle>(color, b, h);
    }
};

int main() {
    cout << "=== Practical Example: Shape Hierarchy ===" << endl;
    
    cout << "\n1. Creating shapes with different constructors:" << endl;
    Circle c1;                        // Inherited Shape default
    Circle c2("Red");                 // Inherited Shape(string)
    Circle c3(5.0);                   // Circle's own constructor
    Circle c4("Blue", 7.0);           // Circle's own constructor
    
    Rectangle r1;                     // Inherited Shape default
    Rectangle r2("Green");            // Inherited Shape(string)
    Rectangle r3(4.0, 6.0);           // Rectangle's own constructor
    Rectangle r4("Yellow", 5.0, 8.0); // Rectangle's own constructor
    
    cout << "\n2. Drawing shapes:" << endl;
    c4.draw();
    r4.draw();
    
    cout << "\n3. Using factory:" << endl;
    auto circle = ShapeFactory::createCircle("Purple", 10.0);
    auto rect = ShapeFactory::createRectangle("Orange", 6.0, 9.0);
    auto triangle = ShapeFactory::createTriangle("Cyan", 3.0, 4.0);
    
    circle->draw();
    rect->draw();
    triangle->draw();
    
    cout << "\nAreas: Circle=" << circle->area() 
         << ", Rectangle=" << rect->area() 
         << ", Triangle=" << triangle->area() << endl;
    
    return 0;
}
```

---

## 📊 Inheriting Constructors Summary

| Feature | Description |
|---------|-------------|
| **Syntax** | `using Base::Base;` |
| **Visibility** | Inherited constructors have same access as in base |
| **Default Arguments** | Preserved in inherited constructors |
| **Overriding** | Derived can provide its own constructors |
| **Multiple Inheritance** | Can inherit from multiple base classes |

---

## ✅ Best Practices

1. **Use inheriting constructors** to avoid boilerplate code
2. **Combine with own constructors** when additional initialization needed
3. **Be aware of default arguments** - they are inherited
4. **Document inherited constructors** for clarity
5. **Use with virtual inheritance** carefully
6. **Consider factory methods** as alternative

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Ambiguity** | Multiple base classes with same constructor | Explicitly call base constructors |
| **Missing initialization** | Derived members not initialized | Add own constructors for extra members |
| **Default arguments confusion** | Unexpected behavior | Understand inheritance of defaults |
| **Access restrictions** | Inherited private constructors | Use public/protected constructors |

---

## ✅ Key Takeaways

1. **Inheriting constructors** eliminates boilerplate code
2. **`using Base::Base`** brings all base constructors
3. **Default arguments** are preserved
4. **Can combine** with own constructors
5. **C++11 feature** - improves code maintainability
6. **Useful for** wrapper classes, proxy classes
7. **Reduces code duplication** in hierarchies

---