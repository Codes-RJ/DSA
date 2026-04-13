# README.md

## Types of Inheritance in C++ - Complete Guide

### Overview

Inheritance allows a class to acquire properties and behaviors from another class. Based on how many base classes are involved and how they are arranged, inheritance can be classified into five types: Single, Multiple, Multilevel, Hierarchical, and Hybrid. Understanding each type helps in designing appropriate class hierarchies for different programming scenarios.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [1_Single_Inheritance.md](1_Single_Inheritance.md) | understand Single Inheritance |
| 2. | [2_Multiple_Inheritance.md](2_Multiple_Inheritance.md) | understand Multiple Inheritance |
| 3. | [3_Multilevel_Inheritance.md](3_Multilevel_Inheritance.md) | understand Multilevel Inheritance |
| 4. | [4_Hierarchical_Inheritance.md](4_Hierarchical_Inheritance.md) | understand Hierarchical Inheritance |
| 5. | [5_Hybrid_Inheritance.md](5_Hybrid_Inheritance.md) | understand Hybrid Inheritance |

---

## 1. Single Inheritance

This topic explains the simplest form of inheritance where one derived class inherits from one base class.

**File:** [1_Single_Inheritance.md](1_Single_Inheritance.md)

**What you will learn:**
- Definition of single inheritance
- Syntax for single inheritance
- One base class, one derived class relationship
- Member inheritance in single inheritance
- When to use single inheritance
- Real-world examples of single inheritance

**Key Concepts:**
- **Base Class** - The parent class being inherited from
- **Derived Class** - The child class that inherits
- **One-to-One Relationship** - One base, one derived
- **Code Reusability** - Derived class reuses base class code
- **Extensibility** - Derived can add new members

**Visual Representation:**
```
    Base Class
        ↑
        │
    Derived Class
```

**Syntax:**
```cpp
class Base {
    // Base class members
};

class Derived : public Base {
    // Derived class members
};
```

**Example:**
```cpp
class Animal {
public:
    void eat() {
        cout << "Eating..." << endl;
    }
};

class Dog : public Animal {
public:
    void bark() {
        cout << "Barking..." << endl;
    }
};

// Usage
Dog d;
d.eat();   // From Animal
d.bark();  // From Dog
```

---

## 2. Multiple Inheritance

This topic explains where a derived class inherits from two or more base classes. This is a unique feature of C++ (not available in languages like Java and C#).

**File:** [2_Multiple_Inheritance.md](2_Multiple_Inheritance.md)

**What you will learn:**
- Definition of multiple inheritance
- Syntax for multiple inheritance
- Inheriting from multiple base classes
- Ambiguity resolution (diamond problem introduction)
- When to use multiple inheritance
- Real-world examples of multiple inheritance

**Key Concepts:**
- **Multiple Bases** - Derived inherits from two or more base classes
- **Ambiguity** - Same member name in multiple bases causes conflict
- **Scope Resolution** - Use `Base::member` to resolve ambiguity
- **C++ Specific** - Not all OOP languages support this

**Visual Representation:**
```
    Base1      Base2
       ↑         ↑
        \       /
         \     /
          \   /
        Derived Class
```

**Syntax:**
```cpp
class Base1 {
    // Base1 members
};

class Base2 {
    // Base2 members
};

class Derived : public Base1, public Base2 {
    // Derived members
};
```

**Example:**
```cpp
class Printer {
public:
    void print() {
        cout << "Printing..." << endl;
    }
};

class Scanner {
public:
    void scan() {
        cout << "Scanning..." << endl;
    }
};

class AllInOne : public Printer, public Scanner {
public:
    void fax() {
        cout << "Faxing..." << endl;
    }
};

// Usage
AllInOne device;
device.print();  // From Printer
device.scan();   // From Scanner
device.fax();    // From AllInOne
```

---

## 3. Multilevel Inheritance

This topic explains where a class inherits from a derived class, creating a chain of inheritance.

**File:** [3_Multilevel_Inheritance.md](3_Multilevel_Inheritance.md)

**What you will learn:**
- Definition of multilevel inheritance
- Chain of inheritance (grandparent → parent → child)
- Constructor and destructor order
- Member inheritance through multiple levels
- When to use multilevel inheritance
- Real-world examples (Vehicle → Car → SportsCar)

**Key Concepts:**
- **Inheritance Chain** - Derived class becomes base for another class
- **Levels** - Can have any number of levels
- **Member Propagation** - Members inherited through all levels
- **Constructor Order** - Top to bottom (base to most derived)

**Visual Representation:**
```
    GrandParent Class
          ↑
          │
     Parent Class
          ↑
          │
     Child Class
```

**Syntax:**
```cpp
class GrandParent {
    // GrandParent members
};

class Parent : public GrandParent {
    // Parent members (includes GrandParent)
};

class Child : public Parent {
    // Child members (includes GrandParent and Parent)
};
```

**Example:**
```cpp
class Vehicle {
public:
    void start() {
        cout << "Vehicle started" << endl;
    }
};

class Car : public Vehicle {
public:
    void drive() {
        cout << "Car driving" << endl;
    }
};

class SportsCar : public Car {
public:
    void turboBoost() {
        cout << "Turbo boost activated" << endl;
    }
};

// Usage
SportsCar sc;
sc.start();      // From Vehicle
sc.drive();      // From Car
sc.turboBoost(); // From SportsCar
```

---

## 4. Hierarchical Inheritance

This topic explains where multiple derived classes inherit from a single base class.

**File:** [4_Hierarchical_Inheritance.md](4_Hierarchical_Inheritance.md)

**What you will learn:**
- Definition of hierarchical inheritance
- One base class, multiple derived classes
- Code reuse across multiple derived classes
- Common functionality in base class
- Specific functionality in derived classes
- Real-world examples (Animal → Dog, Cat, Cow)

**Key Concepts:**
- **One-to-Many** - One base, many derived classes
- **Common Interface** - Base defines common behavior
- **Specialization** - Each derived adds specific behavior
- **Code Reuse** - Common code written once in base

**Visual Representation:**
```
              Base Class
            ↑     ↑     ↑
            │     │     │
            │     │     │
        Derived1 Derived2 Derived3
```

**Syntax:**
```cpp
class Base {
    // Common members
};

class Derived1 : public Base {
    // Specific members for Derived1
};

class Derived2 : public Base {
    // Specific members for Derived2
};

class Derived3 : public Base {
    // Specific members for Derived3
};
```

**Example:**
```cpp
class Shape {
protected:
    double area_;
public:
    virtual void calculateArea() = 0;
    double getArea() const { return area_; }
};

class Circle : public Shape {
private:
    double radius_;
public:
    Circle(double r) : radius_(r) {}
    void calculateArea() override {
        area_ = 3.14159 * radius_ * radius_;
    }
};

class Rectangle : public Shape {
private:
    double length_, width_;
public:
    Rectangle(double l, double w) : length_(l), width_(w) {}
    void calculateArea() override {
        area_ = length_ * width_;
    }
};

class Triangle : public Shape {
private:
    double base_, height_;
public:
    Triangle(double b, double h) : base_(b), height_(h) {}
    void calculateArea() override {
        area_ = 0.5 * base_ * height_;
    }
};
```

---

## 5. Hybrid Inheritance

This topic explains the combination of multiple and multilevel inheritance, which can lead to the diamond problem.

**File:** [5_Hybrid_Inheritance.md](5_Hybrid_Inheritance.md)

**What you will learn:**
- Definition of hybrid inheritance
- Combination of two or more inheritance types
- Diamond problem introduction
- Ambiguity in hybrid inheritance
- Virtual inheritance as solution
- When to use hybrid inheritance

**Key Concepts:**
- **Combination** - Mix of multiple and multilevel inheritance
- **Diamond Problem** - Ambiguity when same base appears multiple times
- **Virtual Inheritance** - Solution to diamond problem
- **Complex Hierarchy** - Can become difficult to manage

**Visual Representation (Diamond):**
```
        Base Class
         ↑     ↑
         │     │
        B      C
         ↑     ↑
          \   /
           \ /
        Derived Class
```

**Syntax:**
```cpp
class Base {
public:
    int value;
};

class B : public Base { };   // or virtual public Base
class C : public Base { };   // or virtual public Base

class Derived : public B, public C {
    // Ambiguity: which value?
};
```

**Example (Without Virtual Inheritance - Problem):**
```cpp
class Person {
protected:
    string name_;
public:
    Person(string name) : name_(name) {}
    void display() { cout << "Person: " << name_ << endl; }
};

class Employee : public Person {
public:
    Employee(string name) : Person(name) {}
    void work() { cout << name_ << " is working" << endl; }
};

class Student : public Person {
public:
    Student(string name) : Person(name) {}
    void study() { cout << name_ << " is studying" << endl; }
};

// Hybrid: WorkingStudent inherits from both Employee and Student
class WorkingStudent : public Employee, public Student {
public:
    // Problem: Person constructor called twice
    WorkingStudent(string name) : Employee(name), Student(name) {}
    // Ambiguity: which name_? Employee::name_ or Student::name_?
};

// Solution: Use virtual inheritance
class Employee : virtual public Person { };
class Student : virtual public Person { };
class WorkingStudent : public Employee, public Student {
    WorkingStudent(string name) : Person(name), Employee(name), Student(name) {}
};
```

---

### Types of Inheritance Comparison Table

| Type | Base Classes | Derived Classes | Complexity | Diamond Problem Risk |
|------|--------------|-----------------|------------|---------------------|
| **Single** | 1 | 1 | Low | No |
| **Multiple** | 2 or more | 1 | Medium | Yes (with common base) |
| **Multilevel** | 1 per level | 1 per level | Low | No |
| **Hierarchical** | 1 | Many | Low | No |
| **Hybrid** | Multiple | Multiple | High | Yes |

---

### When to Use Each Type

| Type | Best Used For |
|------|----------------|
| **Single** | Simple hierarchical relationships, basic code reuse |
| **Multiple** | Combining orthogonal functionalities (e.g., Printable, Serializable) |
| **Multilevel** | Deep specialization chains (e.g., Vehicle → Car → ElectricCar) |
| **Hierarchical** | Creating family of related classes (e.g., different shapes) |
| **Hybrid** | Complex real-world relationships (e.g., Person → Employee and Student) |

---

### Prerequisites

Before starting this section, you should have completed:

- [01_Basics_of_Inheritance.md](../01_Basics_of_Inheritance.md) - Basic inheritance concepts
- [03_Access_Specifiers_in_Inheritance.md](../03_Access_Specifiers_in_Inheritance.md) - Access control
- [04_Constructor_and_Destructor_in_Inheritance.md](../04_Constructor_and_Destructor_in_Inheritance.md) - Object lifecycle

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Multiple inheritance without necessity | Prefer composition or single inheritance |
| Diamond problem without virtual inheritance | Use virtual inheritance for common base |
| Constructor ambiguity in multiple inheritance | Explicitly call all base constructors |
| Overcomplicating hierarchy | Keep inheritance trees simple and shallow |
| Ignoring constructor/destructor order | Understand execution order for each type |

---

### Practice Questions

After completing this section, you should be able to:

1. List and describe the five types of inheritance
2. Write code for each type of inheritance
3. Explain the diamond problem and which inheritance types cause it
4. Describe when to use multiple inheritance vs composition
5. Draw inheritance diagrams for each type
6. Identify the inheritance type from a given class hierarchy
7. Explain the constructor order in multilevel inheritance
8. Implement virtual inheritance to solve the diamond problem

---

### Next Steps

- Go to [1_Single_Inheritance.md](1_Single_Inheritance.md) to understand Single Inheritance.