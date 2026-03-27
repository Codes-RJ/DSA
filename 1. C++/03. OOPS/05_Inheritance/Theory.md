# 05_Inheritance/Theory.md

# Inheritance in C++ - Complete Guide

## 📖 Overview

Inheritance is a fundamental concept in Object-Oriented Programming that allows a class (derived class) to acquire properties and behaviors from another class (base class). It enables code reuse, establishes hierarchical relationships, and forms the foundation for polymorphism. Inheritance models "is-a" relationships in real-world systems.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Base Class** | Parent class that provides members to derived classes |
| **Derived Class** | Child class that inherits from base class |
| **Inheritance** | Mechanism to create new classes from existing ones |
| **Reusability** | Base class code is reused across multiple derived classes |
| **Hierarchy** | Creates relationships between classes |

---

## 📊 Types of Inheritance

| Type | Description | Relationship |
|------|-------------|--------------|
| **Single Inheritance** | One derived class inherits from one base class | A → B |
| **Multiple Inheritance** | One derived class inherits from multiple base classes | A, B → C |
| **Multilevel Inheritance** | Chain of inheritance | A → B → C |
| **Hierarchical Inheritance** | Multiple derived classes from one base | A → B, A → C |
| **Hybrid Inheritance** | Combination of multiple inheritance types | Complex relationships |

---

## 1. **Single Inheritance**

The simplest form where a derived class inherits from a single base class.

```cpp
#include <iostream>
#include <string>
using namespace std;

// Base class
class Animal {
protected:
    string name;
    int age;
    
public:
    Animal(string n, int a) : name(n), age(a) {
        cout << "Animal constructor: " << name << endl;
    }
    
    void eat() {
        cout << name << " is eating" << endl;
    }
    
    void sleep() {
        cout << name << " is sleeping" << endl;
    }
    
    virtual void sound() {
        cout << name << " makes a sound" << endl;
    }
    
    void display() {
        cout << "Name: " << name << ", Age: " << age << endl;
    }
};

// Derived class
class Dog : public Animal {
private:
    string breed;
    
public:
    Dog(string n, int a, string b) : Animal(n, a), breed(b) {
        cout << "Dog constructor: " << name << endl;
    }
    
    // Additional functionality
    void bark() {
        cout << name << " says: Woof! Woof!" << endl;
    }
    
    void wagTail() {
        cout << name << " is wagging tail" << endl;
    }
    
    // Override base class method
    void sound() override {
        cout << name << " barks loudly" << endl;
    }
    
    void display() {
        Animal::display();
        cout << "Breed: " << breed << endl;
    }
};

int main() {
    cout << "=== Single Inheritance ===" << endl;
    
    Dog dog("Buddy", 3, "Golden Retriever");
    
    dog.display();
    dog.eat();      // Inherited from Animal
    dog.sleep();    // Inherited from Animal
    dog.bark();     // Dog's own method
    dog.wagTail();  // Dog's own method
    dog.sound();    // Overridden method
    
    return 0;
}
```

**Output:**
```
=== Single Inheritance ===
Animal constructor: Buddy
Dog constructor: Buddy
Name: Buddy, Age: 3
Breed: Golden Retriever
Buddy is eating
Buddy is sleeping
Buddy says: Woof! Woof!
Buddy is wagging tail
Buddy barks loudly
```

---

## 2. **Multilevel Inheritance**

A chain of inheritance where a class inherits from another derived class.

```cpp
#include <iostream>
#include <string>
using namespace std;

// Base class
class Vehicle {
protected:
    string brand;
    int year;
    
public:
    Vehicle(string b, int y) : brand(b), year(y) {
        cout << "Vehicle constructor: " << brand << endl;
    }
    
    void start() {
        cout << brand << " vehicle starting..." << endl;
    }
    
    void stop() {
        cout << brand << " vehicle stopping..." << endl;
    }
    
    virtual void display() {
        cout << "Brand: " << brand << ", Year: " << year << endl;
    }
};

// Derived class 1
class Car : public Vehicle {
protected:
    int doors;
    
public:
    Car(string b, int y, int d) : Vehicle(b, y), doors(d) {
        cout << "Car constructor: " << brand << endl;
    }
    
    void honk() {
        cout << brand << " car honks: Beep! Beep!" << endl;
    }
    
    void display() override {
        Vehicle::display();
        cout << "Doors: " << doors << endl;
    }
};

// Derived class 2 (from Car)
class ElectricCar : public Car {
private:
    int batteryCapacity;
    
public:
    ElectricCar(string b, int y, int d, int battery) 
        : Car(b, y, d), batteryCapacity(battery) {
        cout << "ElectricCar constructor: " << brand << endl;
    }
    
    void charge() {
        cout << brand << " electric car charging..." << endl;
    }
    
    void display() override {
        Car::display();
        cout << "Battery: " << batteryCapacity << " kWh" << endl;
    }
    
    // Override start method
    void start() override {
        cout << brand << " electric car starting silently..." << endl;
    }
};

int main() {
    cout << "=== Multilevel Inheritance ===" << endl;
    
    ElectricCar tesla("Tesla", 2024, 4, 75);
    
    tesla.display();
    tesla.start();    // Overridden method
    tesla.honk();     // From Car
    tesla.charge();   // ElectricCar's own method
    tesla.stop();     // From Vehicle
    
    return 0;
}
```

---

## 3. **Multiple Inheritance**

A derived class inherits from multiple base classes (C++ specific).

```cpp
#include <iostream>
#include <string>
using namespace std;

class Printer {
public:
    void print(const string& content) {
        cout << "Printing: " << content << endl;
    }
    
    void calibrate() {
        cout << "Printer calibrating..." << endl;
    }
};

class Scanner {
public:
    void scan() {
        cout << "Scanning document..." << endl;
    }
    
    void calibrate() {
        cout << "Scanner calibrating..." << endl;
    }
};

// Multiple inheritance
class MultiFunctionPrinter : public Printer, public Scanner {
public:
    void copy() {
        cout << "Copying document..." << endl;
    }
    
    // Resolve ambiguity for calibrate
    void calibrate() {
        Printer::calibrate();  // Call Printer's version
        Scanner::calibrate();  // Call Scanner's version
        cout << "Multi-function device calibrated" << endl;
    }
};

class Worker {
protected:
    string name;
    
public:
    Worker(string n) : name(n) {}
    virtual void work() = 0;
};

class Developer : virtual public Worker {
public:
    Developer(string n) : Worker(n) {}
    void work() override {
        cout << name << " is writing code" << endl;
    }
};

class Manager : virtual public Worker {
public:
    Manager(string n) : Worker(n) {}
    void work() override {
        cout << name << " is managing team" << endl;
    }
};

// Diamond problem solution using virtual inheritance
class TechLead : public Developer, public Manager {
public:
    TechLead(string n) : Worker(n), Developer(n), Manager(n) {}
    
    void work() override {
        Developer::work();
        Manager::work();
        cout << "TechLead is leading technical decisions" << endl;
    }
};

int main() {
    cout << "=== Multiple Inheritance ===" << endl;
    
    MultiFunctionPrinter mfp;
    mfp.print("Hello World");
    mfp.scan();
    mfp.copy();
    mfp.calibrate();  // Resolved ambiguity
    
    cout << "\n=== Virtual Inheritance (Diamond Problem) ===" << endl;
    TechLead lead("Alice");
    lead.work();
    
    return 0;
}
```

---

## 4. **Hierarchical Inheritance**

Multiple derived classes inherit from a single base class.

```cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

// Base class
class Shape {
protected:
    string color;
    
public:
    Shape(string c) : color(c) {}
    
    virtual double area() const = 0;
    virtual double perimeter() const = 0;
    
    void setColor(string c) { color = c; }
    string getColor() const { return color; }
    
    virtual void display() const {
        cout << "Shape color: " << color << endl;
    }
};

// Derived class 1
class Circle : public Shape {
private:
    double radius;
    
public:
    Circle(string c, double r) : Shape(c), radius(r) {}
    
    double area() const override {
        return M_PI * radius * radius;
    }
    
    double perimeter() const override {
        return 2 * M_PI * radius;
    }
    
    void display() const override {
        Shape::display();
        cout << "Circle: radius=" << radius 
             << ", area=" << area() 
             << ", circumference=" << perimeter() << endl;
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
    
    double perimeter() const override {
        return 2 * (width + height);
    }
    
    void display() const override {
        Shape::display();
        cout << "Rectangle: " << width << "x" << height 
             << ", area=" << area() 
             << ", perimeter=" << perimeter() << endl;
    }
};

// Derived class 3
class Triangle : public Shape {
private:
    double side1, side2, side3;
    
public:
    Triangle(string c, double s1, double s2, double s3) 
        : Shape(c), side1(s1), side2(s2), side3(s3) {}
    
    double area() const override {
        double s = (side1 + side2 + side3) / 2;
        return sqrt(s * (s - side1) * (s - side2) * (s - side3));
    }
    
    double perimeter() const override {
        return side1 + side2 + side3;
    }
    
    void display() const override {
        Shape::display();
        cout << "Triangle: sides=" << side1 << "," << side2 << "," << side3
             << ", area=" << area() 
             << ", perimeter=" << perimeter() << endl;
    }
};

int main() {
    cout << "=== Hierarchical Inheritance ===" << endl;
    
    Circle circle("Red", 5.0);
    Rectangle rectangle("Blue", 4.0, 6.0);
    Triangle triangle("Green", 3.0, 4.0, 5.0);
    
    cout << "\nShapes:" << endl;
    circle.display();
    rectangle.display();
    triangle.display();
    
    cout << "\nPolymorphic behavior:" << endl;
    Shape* shapes[] = {&circle, &rectangle, &triangle};
    
    for (auto shape : shapes) {
        cout << "Area: " << shape->area() << ", Perimeter: " << shape->perimeter() << endl;
    }
    
    return 0;
}
```

---

## 5. **Inheritance Access Specifiers**

How different inheritance types affect member accessibility.

```cpp
#include <iostream>
using namespace std;

class Base {
private:
    int privateVar = 1;
protected:
    int protectedVar = 2;
public:
    int publicVar = 3;
    
    void showBase() {
        cout << "Private: " << privateVar << endl;
        cout << "Protected: " << protectedVar << endl;
        cout << "Public: " << publicVar << endl;
    }
};

// Public Inheritance
class PublicDerived : public Base {
public:
    void show() {
        // cout << privateVar << endl;  // Error: private not accessible
        cout << "Protected: " << protectedVar << endl;  // OK - becomes protected
        cout << "Public: " << publicVar << endl;        // OK - remains public
    }
};

// Protected Inheritance
class ProtectedDerived : protected Base {
public:
    void show() {
        cout << "Protected: " << protectedVar << endl;  // OK
        cout << "Public: " << publicVar << endl;        // OK - becomes protected
    }
};

// Private Inheritance
class PrivateDerived : private Base {
public:
    void show() {
        cout << "Protected: " << protectedVar << endl;  // OK
        cout << "Public: " << publicVar << endl;        // OK - becomes private
    }
};

int main() {
    cout << "=== Inheritance Access Specifiers ===" << endl;
    
    PublicDerived pub;
    pub.show();
    pub.publicVar = 100;    // OK - public
    
    ProtectedDerived prot;
    prot.show();
    // prot.publicVar = 100;  // Error! becomes protected
    
    PrivateDerived priv;
    priv.show();
    // priv.publicVar = 100;  // Error! becomes private
    
    return 0;
}
```

---

## 6. **Constructor and Destructor Order in Inheritance**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Base {
private:
    string name;
    
public:
    Base(string n) : name(n) {
        cout << "Base constructor: " << name << endl;
    }
    
    ~Base() {
        cout << "Base destructor: " << name << endl;
    }
};

class Member {
private:
    string name;
    
public:
    Member(string n) : name(n) {
        cout << "  Member constructor: " << name << endl;
    }
    
    ~Member() {
        cout << "  Member destructor: " << name << endl;
    }
};

class Derived : public Base {
private:
    Member m1;
    Member m2;
    
public:
    Derived(string baseName, string m1Name, string m2Name) 
        : Base(baseName), m2(m2Name), m1(m1Name) {  // Order: Base, then m1, then m2
        cout << "Derived constructor body" << endl;
    }
    
    ~Derived() {
        cout << "Derived destructor body" << endl;
    }
};

int main() {
    cout << "=== Constructor/Destructor Order ===" << endl;
    cout << "\nConstruction order:" << endl;
    cout << "1. Base class constructor" << endl;
    cout << "2. Member objects (in declaration order)" << endl;
    cout << "3. Derived class constructor body" << endl;
    
    cout << "\nDestruction order: REVERSE of construction\n" << endl;
    
    {
        Derived d("BaseObj", "Member1", "Member2");
        cout << "\nObject created successfully" << endl;
    }  // Destructor called here
    
    return 0;
}
```

---

## 📊 Inheritance Summary

| Aspect | Description |
|--------|-------------|
| **Purpose** | Code reuse, hierarchical relationships, polymorphism |
| **Syntax** | `class Derived : access_specifier Base` |
| **Access** | Public, protected, private inheritance |
| **Order** | Base → Members → Derived (construction) |
| **Virtual** | Virtual inheritance solves diamond problem |

---

## ✅ Best Practices

1. **Use public inheritance for "is-a" relationships**
2. **Use protected/private inheritance for "implemented-in-terms-of"**
3. **Make base class destructor virtual** for polymorphic classes
4. **Use virtual inheritance** to solve diamond problem
5. **Follow Liskov Substitution Principle** - derived class should be substitutable for base
6. **Prefer composition over inheritance** when relationship is "has-a" not "is-a"

---