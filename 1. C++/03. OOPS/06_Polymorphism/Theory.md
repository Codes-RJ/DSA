I'll now start with the **Polymorphism** section. Let me begin with the theory file.

---

# 06_Polymorphism/Theory.md

# Polymorphism in C++ - Complete Guide

## 📖 Overview

Polymorphism is one of the four fundamental principles of Object-Oriented Programming (along with encapsulation, inheritance, and abstraction). It allows objects of different classes to be treated as objects of a common base class, with the appropriate method being called based on the actual object type. Polymorphism enables code to be written that works with objects of multiple types in a uniform way.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Polymorphism** | "Many forms" - ability to take multiple forms |
| **Compile-time Polymorphism** | Resolved at compile time (function overloading, operator overloading) |
| **Run-time Polymorphism** | Resolved at run time (virtual functions) |
| **Virtual Function** | Function that can be overridden in derived classes |
| **Abstract Class** | Class with pure virtual functions, cannot be instantiated |

---

## 📊 Types of Polymorphism

| Type | Resolution | Mechanism | Example |
|------|------------|-----------|---------|
| **Compile-time** | Compiler | Function overloading | Same function name, different parameters |
| **Compile-time** | Compiler | Operator overloading | Custom operators for user-defined types |
| **Compile-time** | Compiler | Templates | Generic functions and classes |
| **Run-time** | Runtime | Virtual functions | Base pointer calling derived method |

---

## 1. **Compile-time Polymorphism (Function Overloading)**

```cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

class Math {
public:
    // Function overloading - same name, different parameters
    int add(int a, int b) {
        cout << "int add(int, int)" << endl;
        return a + b;
    }
    
    double add(double a, double b) {
        cout << "double add(double, double)" << endl;
        return a + b;
    }
    
    int add(int a, int b, int c) {
        cout << "int add(int, int, int)" << endl;
        return a + b + c;
    }
    
    string add(const string& a, const string& b) {
        cout << "string add(string, string)" << endl;
        return a + b;
    }
};

class Area {
public:
    double calculate(double radius) {
        cout << "Circle area: ";
        return M_PI * radius * radius;
    }
    
    double calculate(double length, double width) {
        cout << "Rectangle area: ";
        return length * width;
    }
    
    double calculate(double base, double height, bool isTriangle) {
        cout << "Triangle area: ";
        return 0.5 * base * height;
    }
};

int main() {
    cout << "=== Compile-time Polymorphism (Function Overloading) ===" << endl;
    
    Math math;
    cout << "add(5, 3) = " << math.add(5, 3) << endl;
    cout << "add(5.5, 3.2) = " << math.add(5.5, 3.2) << endl;
    cout << "add(1, 2, 3) = " << math.add(1, 2, 3) << endl;
    cout << "add(\"Hello\", \" World\") = " << math.add("Hello", " World") << endl;
    
    cout << "\n" << math.add(5, 3) << endl;
    
    Area area;
    cout << area.calculate(5.0) << endl;
    cout << area.calculate(4.0, 6.0) << endl;
    cout << area.calculate(3.0, 4.0, true) << endl;
    
    return 0;
}
```

**Output:**
```
=== Compile-time Polymorphism (Function Overloading) ===
int add(int, int)
add(5, 3) = 8
double add(double, double)
add(5.5, 3.2) = 8.7
int add(int, int, int)
add(1, 2, 3) = 6
string add(string, string)
add("Hello", " World") = Hello World

int add(int, int)
8
Circle area: 78.5398
Rectangle area: 24
Triangle area: 6
```

---

## 2. **Run-time Polymorphism (Virtual Functions)**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

// Base class
class Shape {
protected:
    string color;
    
public:
    Shape(string c) : color(c) {}
    
    // Virtual function - can be overridden
    virtual double area() const {
        return 0;
    }
    
    // Virtual function with default implementation
    virtual void draw() const {
        cout << "Drawing a generic shape" << endl;
    }
    
    // Pure virtual function - makes Shape abstract
    virtual void display() const = 0;
    
    // Virtual destructor - essential for polymorphism
    virtual ~Shape() {
        cout << "Shape destructor" << endl;
    }
};

// Derived class 1
class Circle : public Shape {
private:
    double radius;
    
public:
    Circle(string c, double r) : Shape(c), radius(r) {}
    
    double area() const override {
        return 3.14159 * radius * radius;
    }
    
    void draw() const override {
        cout << "Drawing a " << color << " circle with radius " << radius << endl;
    }
    
    void display() const override {
        cout << "Circle: color=" << color << ", radius=" << radius 
             << ", area=" << area() << endl;
    }
    
    ~Circle() override {
        cout << "Circle destructor" << endl;
    }
};

// Derived class 2
class Rectangle : public Shape {
private:
    double width, height;
    
public:
    Rectangle(string c, double w, double h) : Shape(c), width(w), height(h) {}
    
    double area() const override {
        return width * height;
    }
    
    void draw() const override {
        cout << "Drawing a " << color << " rectangle " << width << "x" << height << endl;
    }
    
    void display() const override {
        cout << "Rectangle: color=" << color << ", size=" << width << "x" << height 
             << ", area=" << area() << endl;
    }
    
    ~Rectangle() override {
        cout << "Rectangle destructor" << endl;
    }
};

// Derived class 3
class Triangle : public Shape {
private:
    double base, height;
    
public:
    Triangle(string c, double b, double h) : Shape(c), base(b), height(h) {}
    
    double area() const override {
        return 0.5 * base * height;
    }
    
    void draw() const override {
        cout << "Drawing a " << color << " triangle with base " << base 
             << " and height " << height << endl;
    }
    
    void display() const override {
        cout << "Triangle: color=" << color << ", base=" << base 
             << ", height=" << height << ", area=" << area() << endl;
    }
    
    ~Triangle() override {
        cout << "Triangle destructor" << endl;
    }
};

int main() {
    cout << "=== Run-time Polymorphism (Virtual Functions) ===" << endl;
    
    // Polymorphic behavior
    vector<unique_ptr<Shape>> shapes;
    shapes.push_back(make_unique<Circle>("Red", 5.0));
    shapes.push_back(make_unique<Rectangle>("Blue", 4.0, 6.0));
    shapes.push_back(make_unique<Triangle>("Green", 3.0, 4.0));
    
    cout << "\nDisplaying all shapes:" << endl;
    for (const auto& shape : shapes) {
        shape->display();
        shape->draw();
        cout << "Area: " << shape->area() << endl << endl;
    }
    
    // Function using base class pointer
    cout << "Function using base class pointer:" << endl;
    auto processShape = [](const Shape& shape) {
        shape.display();
        cout << "Area: " << shape.area() << endl;
    };
    
    processShape(*shapes[0]);
    
    return 0;
}
```

---

## 3. **Virtual Function Table (vtable)**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Base {
public:
    virtual void func1() { cout << "Base::func1" << endl; }
    virtual void func2() { cout << "Base::func2" << endl; }
    void func3() { cout << "Base::func3 (non-virtual)" << endl; }
    virtual ~Base() {}
};

class Derived : public Base {
public:
    void func1() override { cout << "Derived::func1" << endl; }
    virtual void func4() { cout << "Derived::func4" << endl; }
};

int main() {
    cout << "=== Virtual Function Table (vtable) ===" << endl;
    
    Base b;
    Derived d;
    Base* ptr = &d;
    
    cout << "\nSize of Base: " << sizeof(Base) << " bytes" << endl;
    cout << "Size of Derived: " << sizeof(Derived) << " bytes" << endl;
    cout << "Note: Each object has a vptr (virtual pointer) to vtable" << endl;
    
    cout << "\nCalling through base pointer (polymorphism):" << endl;
    ptr->func1();  // Calls Derived::func1
    ptr->func2();  // Calls Base::func2
    ptr->func3();  // Non-virtual, calls Base::func3
    
    cout << "\nCalling through derived object:" << endl;
    d.func1();  // Calls Derived::func1
    d.func2();  // Calls Base::func2
    d.func3();  // Calls Base::func3
    d.func4();  // Calls Derived::func4
    
    return 0;
}
```

---

## 4. **Abstract Classes and Pure Virtual Functions**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

// Abstract base class (interface)
class IAnimal {
public:
    // Pure virtual functions - must be implemented by derived classes
    virtual void speak() const = 0;
    virtual void move() const = 0;
    virtual string getName() const = 0;
    
    // Virtual destructor with default implementation
    virtual ~IAnimal() = default;
};

// Concrete class implementing the interface
class Dog : public IAnimal {
private:
    string name;
    
public:
    Dog(string n) : name(n) {}
    
    void speak() const override {
        cout << name << " says: Woof! Woof!" << endl;
    }
    
    void move() const override {
        cout << name << " runs on four legs" << endl;
    }
    
    string getName() const override {
        return name;
    }
};

class Bird : public IAnimal {
private:
    string name;
    
public:
    Bird(string n) : name(n) {}
    
    void speak() const override {
        cout << name << " chirps: Tweet! Tweet!" << endl;
    }
    
    void move() const override {
        cout << name << " flies in the sky" << endl;
    }
    
    string getName() const override {
        return name;
    }
};

class Fish : public IAnimal {
private:
    string name;
    
public:
    Fish(string n) : name(n) {}
    
    void speak() const override {
        cout << name << " says: ... (silence)" << endl;
    }
    
    void move() const override {
        cout << name << " swims in water" << endl;
    }
    
    string getName() const override {
        return name;
    }
};

int main() {
    cout << "=== Abstract Classes and Pure Virtual Functions ===" << endl;
    
    // IAnimal animal;  // Error! Cannot instantiate abstract class
    
    vector<unique_ptr<IAnimal>> animals;
    animals.push_back(make_unique<Dog>("Buddy"));
    animals.push_back(make_unique<Bird>("Tweety"));
    animals.push_back(make_unique<Fish>("Nemo"));
    
    cout << "Animals in the zoo:" << endl;
    for (const auto& animal : animals) {
        cout << "\n" << animal->getName() << ":" << endl;
        animal->speak();
        animal->move();
    }
    
    return 0;
}
```

---

## 5. **Polymorphism Benefits**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <cmath>
using namespace std;

// Without polymorphism (bad design)
class BadShape {
private:
    string type;
    double param1, param2;
    
public:
    BadShape(string t, double p1, double p2 = 0) : type(t), param1(p1), param2(p2) {}
    
    double area() const {
        if (type == "circle") {
            return M_PI * param1 * param1;
        } else if (type == "rectangle") {
            return param1 * param2;
        } else if (type == "triangle") {
            return 0.5 * param1 * param2;
        }
        return 0;
    }
    
    void draw() const {
        if (type == "circle") {
            cout << "Drawing circle radius=" << param1 << endl;
        } else if (type == "rectangle") {
            cout << "Drawing rectangle " << param1 << "x" << param2 << endl;
        } else if (type == "triangle") {
            cout << "Drawing triangle base=" << param1 << " height=" << param2 << endl;
        }
    }
};

// With polymorphism (good design)
class GoodShape {
public:
    virtual double area() const = 0;
    virtual void draw() const = 0;
    virtual ~GoodShape() = default;
};

class GoodCircle : public GoodShape {
private:
    double radius;
    
public:
    GoodCircle(double r) : radius(r) {}
    double area() const override { return M_PI * radius * radius; }
    void draw() const override { cout << "Circle radius=" << radius << endl; }
};

class GoodRectangle : public GoodShape {
private:
    double width, height;
    
public:
    GoodRectangle(double w, double h) : width(w), height(h) {}
    double area() const override { return width * height; }
    void draw() const override { cout << "Rectangle " << width << "x" << height << endl; }
};

class GoodTriangle : public GoodShape {
private:
    double base, height;
    
public:
    GoodTriangle(double b, double h) : base(b), height(h) {}
    double area() const override { return 0.5 * base * height; }
    void draw() const override { cout << "Triangle base=" << base << " height=" << height << endl; }
};

int main() {
    cout << "=== Polymorphism Benefits ===" << endl;
    
    cout << "\nWithout polymorphism (bad):" << endl;
    BadShape shapes[] = {
        BadShape("circle", 5),
        BadShape("rectangle", 4, 6),
        BadShape("triangle", 3, 4)
    };
    
    for (const auto& shape : shapes) {
        shape.draw();
        cout << "Area: " << shape.area() << endl;
    }
    
    cout << "\nWith polymorphism (good):" << endl;
    vector<unique_ptr<GoodShape>> goodShapes;
    goodShapes.push_back(make_unique<GoodCircle>(5));
    goodShapes.push_back(make_unique<GoodRectangle>(4, 6));
    goodShapes.push_back(make_unique<GoodTriangle>(3, 4));
    
    for (const auto& shape : goodShapes) {
        shape->draw();
        cout << "Area: " << shape->area() << endl;
    }
    
    cout << "\nBenefits of polymorphism:" << endl;
    cout << "✓ Open/Closed Principle - Open for extension, closed for modification" << endl;
    cout << "✓ No conditional statements (if/else or switch) for type checking" << endl;
    cout << "✓ New types can be added without modifying existing code" << endl;
    cout << "✓ Code is more maintainable and extensible" << endl;
    
    return 0;
}
```

---

## 📊 Polymorphism Summary

| Aspect | Description |
|--------|-------------|
| **Purpose** | Allow objects of different types to be treated uniformly |
| **Compile-time** | Resolved at compile time (overloading, templates) |
| **Run-time** | Resolved at runtime (virtual functions) |
| **Virtual Functions** | Enable dynamic dispatch |
| **Abstract Classes** | Define interfaces that derived classes must implement |
| **Benefits** | Extensibility, maintainability, code reuse |

---

## ✅ Best Practices

1. **Use virtual functions** for polymorphic behavior
2. **Make base destructors virtual** for proper cleanup
3. **Use `override` keyword** to explicitly mark overridden functions
4. **Use `final` keyword** to prevent further overriding
5. **Prefer pure virtual functions** for interfaces
6. **Use smart pointers** for polymorphic objects

---