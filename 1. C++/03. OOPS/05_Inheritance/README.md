# README.md

## Inheritance in C++ - Complete Guide

### Overview

Inheritance is one of the four fundamental pillars of Object-Oriented Programming. It allows a class (derived class) to inherit properties and behaviors from another class (base class). Inheritance promotes code reusability, establishes relationships between classes, and enables polymorphism. Understanding inheritance is essential for creating hierarchical class structures and reducing code duplication.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [01_Basics_of_Inheritance.md](01_Basics_of_Inheritance.md) | understand Basics of Inheritance |
| 2. | [02_Types_of_Inheritance/README.md](02_Types_of_Inheritance/README.md) | understand Types of Inheritance |
| 3. | [03_Access_Specifiers_in_Inheritance.md](03_Access_Specifiers_in_Inheritance.md) | understand Access Specifiers in Inheritance |
| 4. | [04_Constructor_and_Destructor_in_Inheritance.md](04_Constructor_and_Destructor_in_Inheritance.md) | understand Constructor and Destructor in Inheritance |
| 5. | [05_Diamond_Problem.md](05_Diamond_Problem.md) | understand Diamond Problem |
| 6. | [06_Virtual_Inheritance.md](06_Virtual_Inheritance.md) | understand Virtual Inheritance |
| 7. | [07_Is-A_vs_Has-A_Relationship.md](07_Is-A_vs_Has-A_Relationship.md) | understand Is-A vs Has-A Relationship |
| 8. | [Theory.md](Theory.md) | understand Theoretical Foundations of Inheritance |

---

## 1. Basics of Inheritance

This topic explains the fundamental concepts of inheritance in C++.

**File:** [01_Basics_of_Inheritance.md](01_Basics_of_Inheritance.md)

**What you will learn:**
- What is inheritance and why it is used
- Base class (parent/super class) and derived class (child/sub class)
- Syntax of inheritance
- Code reusability through inheritance
- Member inheritance (which members are inherited)
- Types of inheritance (single, multiple, multilevel, hierarchical, hybrid)

**Key Concepts:**
- **Base Class** - The class being inherited from
- **Derived Class** - The class that inherits from base class
- **Reusability** - Derived class can use base class members
- **Extensibility** - Derived class can add new members
- **Syntax** - `class Derived : access_specifier Base`

**Syntax:**
```cpp
// Base class (Parent)
class Animal {
public:
    void eat() {
        cout << "Eating..." << endl;
    }
    void sleep() {
        cout << "Sleeping..." << endl;
    }
};

// Derived class (Child) - inherits from Animal
class Dog : public Animal {
public:
    void bark() {
        cout << "Barking..." << endl;
    }
};

// Usage
int main() {
    Dog d;
    d.eat();    // Inherited from Animal
    d.sleep();  // Inherited from Animal
    d.bark();   // Dog's own method
    return 0;
}
```

---

## 2. Types of Inheritance

This topic explains the different forms of inheritance in C++.

**File:** [02_Types_of_Inheritance/README.md](02_Types_of_Inheritance/README.md)

**What you will learn:**

| Type | Description | Example |
|------|-------------|---------|
| **Single Inheritance** | One derived class inherits from one base class | `class B : public A` |
| **Multiple Inheritance** | One derived class inherits from multiple base classes | `class C : public A, public B` |
| **Multilevel Inheritance** | A class inherits from a derived class | `class B : public A, class C : public B` |
| **Hierarchical Inheritance** | Multiple derived classes inherit from one base class | `class B : public A, class C : public A` |
| **Hybrid Inheritance** | Combination of multiple and multilevel inheritance | `class D : public B, public C` |

**Key Concepts:**
- **Single** - Simplest form, one base, one derived
- **Multiple** - Derived inherits from two or more bases (C++ specific)
- **Multilevel** - Chain of inheritance
- **Hierarchical** - One base, many derived classes
- **Hybrid** - Complex combinations (can cause diamond problem)

**Syntax:**
```cpp
// Single Inheritance
class Derived : public Base {};

// Multiple Inheritance
class Derived : public Base1, public Base2 {};

// Multilevel Inheritance
class Child : public Parent {};
class GrandChild : public Child {};

// Hierarchical Inheritance
class Dog : public Animal {};
class Cat : public Animal {};
```

---

## 3. Access Specifiers in Inheritance

This topic explains how access specifiers affect member visibility in derived classes.

**File:** [03_Access_Specifiers_in_Inheritance.md](03_Access_Specifiers_in_Inheritance.md)

**What you will learn:**
- How `public`, `protected`, and `private` inheritance affect member visibility
- Access levels in base class vs derived class
- When to use each inheritance type
- Member access table for different inheritance modes

**Key Concepts:**

| Base Member Access | public Inheritance | protected Inheritance | private Inheritance |
|--------------------|--------------------|----------------------|---------------------|
| **public** | public in derived | protected in derived | private in derived |
| **protected** | protected in derived | protected in derived | private in derived |
| **private** | not inherited | not inherited | not inherited |

**Syntax:**
```cpp
class Base {
public:
    int pub;
protected:
    int prot;
private:
    int priv;
};

// Public inheritance (most common)
class PublicDerived : public Base {
    // pub remains public
    // prot remains protected
    // priv is not accessible
};

// Protected inheritance
class ProtectedDerived : protected Base {
    // pub becomes protected
    // prot remains protected
    // priv is not accessible
};

// Private inheritance
class PrivateDerived : private Base {
    // pub becomes private
    // prot becomes private
    // priv is not accessible
};
```

---

## 4. Constructor and Destructor in Inheritance

This topic explains the order of constructor and destructor calls in inheritance.

**File:** [04_Constructor_and_Destructor_in_Inheritance.md](04_Constructor_and_Destructor_in_Inheritance.md)

**What you will learn:**
- Order of constructor execution (base → derived)
- Order of destructor execution (derived → base)
- Passing arguments to base class constructor
- Constructor initialization list with base class
- Virtual destructors in inheritance hierarchy

**Key Concepts:**
- **Construction Order** - Base class constructor executes first, then derived
- **Destruction Order** - Derived destructor executes first, then base
- **Base Initialization** - Use initialization list to call base constructor
- **Virtual Destructor** - Required for proper cleanup via base pointer

**Syntax:**
```cpp
class Base {
public:
    Base(int x) {
        cout << "Base constructor: " << x << endl;
    }
    ~Base() {
        cout << "Base destructor" << endl;
    }
};

class Derived : public Base {
public:
    // Call base constructor via initialization list
    Derived(int x, int y) : Base(x) {
        cout << "Derived constructor: " << y << endl;
    }
    ~Derived() {
        cout << "Derived destructor" << endl;
    }
};

// Output when creating Derived object:
// Base constructor: 10
// Derived constructor: 20
// Derived destructor
// Base destructor
```

---

## 5. Diamond Problem

This topic explains the ambiguity that arises in multiple inheritance with a common ancestor.

**File:** [05_Diamond_Problem.md](05_Diamond_Problem.md)

**What you will learn:**
- What is the diamond problem
- How it occurs in multiple inheritance
- Ambiguity in member access
- Ambiguity in constructor calls
- Visual representation of the diamond hierarchy

**Key Concepts:**
- **Diamond Shape** - Class D inherits from B and C, which both inherit from A
- **Ambiguity** - Which A member should D inherit?
- **Duplicate Members** - Two copies of A's members in D
- **Constructor Confusion** - Which path to initialize A?

**Visual Representation:**
```
      A
     / \
    B   C
     \ /
      D
```

**Problem Code:**
```cpp
class A {
public:
    int value;
};

class B : public A {};
class C : public A {};

class D : public B, public C {
public:
    void show() {
        // Ambiguous: which value? B::value or C::value?
        // cout << value;  // Error!
        
        cout << B::value;  // OK - explicit
        cout << C::value;  // OK - explicit
    }
};
```

---

## 6. Virtual Inheritance

This topic explains how to solve the diamond problem using virtual inheritance.

**File:** [06_Virtual_Inheritance.md](06_Virtual_Inheritance.md)

**What you will learn:**
- What is virtual inheritance
- How virtual inheritance solves the diamond problem
- Syntax for virtual inheritance
- Single copy of base class members
- Constructor call order with virtual inheritance

**Key Concepts:**
- **Virtual Keyword** - `class B : virtual public A`
- **Single Copy** - Only one copy of base class members
- **Direct Initialization** - Most derived class initializes virtual base
- **Constructor Order** - Virtual base constructed before non-virtual bases

**Syntax:**
```cpp
class A {
public:
    int value;
    A() { cout << "A constructor" << endl; }
};

// Virtual inheritance
class B : virtual public A {};
class C : virtual public A {};

class D : public B, public C {
public:
    D() : A() {  // D directly initializes A
        cout << "D constructor" << endl;
    }
    void show() {
        cout << value;  // No ambiguity - single copy
    }
};
```

---

## 7. Is-A vs Has-A Relationship

This topic explains the difference between inheritance (is-a) and composition (has-a).

**File:** [07_Is-A_vs_Has-A_Relationship.md](07_Is-A_vs_Has-A_Relationship.md)

**What you will learn:**
- What is Is-A relationship (inheritance)
- What is Has-A relationship (composition/aggregation)
- When to use inheritance vs composition
- Code examples of both relationships
- Design guidelines for choosing between them

**Key Concepts:**

| Relationship | Type | Description | Example |
|--------------|------|-------------|---------|
| **Is-A** | Inheritance | Derived class is a type of base class | Dog is an Animal |
| **Has-A** | Composition | Class contains another class as member | Car has an Engine |

**Syntax:**
```cpp
// Is-A relationship (Inheritance)
class Animal { };
class Dog : public Animal { };  // Dog IS-A Animal

// Has-A relationship (Composition)
class Engine {
    void start() { }
};

class Car {
private:
    Engine engine_;  // Car HAS-A Engine
public:
    void start() {
        engine_.start();  // Delegation
    }
};

// When to use:
// Is-A: when there is a natural hierarchical relationship
// Has-A: when one class contains or uses another class
```

---

## 8. Theoretical Foundations

This topic covers the theoretical concepts behind inheritance.

**File:** [Theory.md](Theory.md)

**What you will learn:**
- Subtyping vs subclassing
- Liskov Substitution Principle (LSP)
- Open/Closed Principle (OCP)
- Inheritance vs composition debate
- Favor composition over inheritance
- Code reuse mechanisms

**Key Concepts:**

| Principle | Description |
|-----------|-------------|
| **Liskov Substitution** | Derived class must be substitutable for base class |
| **Open/Closed** | Classes open for extension, closed for modification |
| **Favor Composition** | Prefer composition over inheritance when possible |
| **Code Reuse** | Inheritance provides reuse, but creates tight coupling |

**Liskov Substitution Example:**
```cpp
class Bird {
public:
    virtual void fly() { cout << "Flying" << endl; }
};

// Violates LSP - Penguin cannot fly
class Penguin : public Bird {
    void fly() override {
        // Penguins don't fly - violates LSP
        throw "Cannot fly";
    }
};

// Better approach - redesign hierarchy
class FlyingBird : public Bird { };
class Penguin : public Bird { };  // No fly method
```

---

### Prerequisites

Before starting this section, you should have completed:

- [01. Basics](../../01.%20Basics/README.md) - Classes, objects, pointers
- [02_Classes_and_Objects/README.md](../02_Classes_and_Objects/README.md) - Class basics
- [03_Constructors_and_Destructors/README.md](../03_Constructors_and_Destructors/README.md) - Object lifecycle
- [04_Encapsulation/README.md](../04_Encapsulation/README.md) - Access control

---

### Sample Inheritance Example

```cpp
#include <iostream>
#include <string>
using namespace std;

// Base class
class Employee {
protected:
    string name_;
    int id_;
    double salary_;
    
public:
    Employee(string name, int id, double salary)
        : name_(name), id_(id), salary_(salary) {
        cout << "Employee constructor: " << name_ << endl;
    }
    
    virtual ~Employee() {
        cout << "Employee destructor: " << name_ << endl;
    }
    
    virtual double calculateBonus() const {
        return salary_ * 0.05;  // 5% bonus
    }
    
    virtual void display() const {
        cout << "Name: " << name_ << ", ID: " << id_;
        cout << ", Salary: " << salary_ << endl;
    }
    
    double getSalary() const { return salary_; }
};

// Derived class - Manager
class Manager : public Employee {
private:
    int teamSize_;
    
public:
    Manager(string name, int id, double salary, int teamSize)
        : Employee(name, id, salary), teamSize_(teamSize) {
        cout << "Manager constructor: " << name_ << endl;
    }
    
    ~Manager() {
        cout << "Manager destructor: " << name_ << endl;
    }
    
    double calculateBonus() const override {
        return salary_ * 0.10 + teamSize_ * 500;  // 10% + 500 per team member
    }
    
    void display() const override {
        Employee::display();
        cout << "Team Size: " << teamSize_ << endl;
    }
};

// Derived class - Intern
class Intern : public Employee {
private:
    int duration_;  // in months
    
public:
    Intern(string name, int id, double salary, int duration)
        : Employee(name, id, salary), duration_(duration) {
        cout << "Intern constructor: " << name_ << endl;
    }
    
    ~Intern() {
        cout << "Intern destructor: " << name_ << endl;
    }
    
    double calculateBonus() const override {
        return salary_ * 0.02;  // 2% bonus
    }
};

// Polymorphic function
void printBonus(const Employee& emp) {
    cout << "Bonus: " << emp.calculateBonus() << endl;
}

int main() {
    cout << "=== Creating Employees ===" << endl;
    
    Manager mgr("Alice", 1001, 50000, 5);
    Intern intern("Bob", 1002, 20000, 6);
    
    cout << "\n=== Employee Details ===" << endl;
    mgr.display();
    printBonus(mgr);
    
    intern.display();
    printBonus(intern);
    
    // Polymorphic container
    cout << "\n=== Polymorphism with Pointers ===" << endl;
    Employee* employees[] = { &mgr, &intern };
    
    for (Employee* emp : employees) {
        emp->display();
        cout << "Bonus: " << emp->calculateBonus() << endl;
    }
    
    cout << "\n=== Destruction Order ===" << endl;
    return 0;
}
```

---

### Learning Path

```
Level 1: Basic Inheritance
├── Basics of Inheritance
├── Types of Inheritance
└── Access Specifiers

Level 2: Object Lifecycle
├── Constructors in Inheritance
├── Destructors in Inheritance
└── Virtual Destructors

Level 3: Advanced Inheritance
├── Diamond Problem
├── Virtual Inheritance
└── Multiple Inheritance

Level 4: Design with Inheritance
├── Is-A vs Has-A
├── Liskov Substitution Principle
└── Favor Composition over Inheritance
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Using inheritance when composition is better | Evaluate Is-A vs Has-A relationship |
| Forgetting virtual destructor in base class | Always make base destructor virtual |
| Not calling base constructor in initialization list | Explicitly call base constructor |
| Diamond problem without virtual inheritance | Use virtual inheritance |
| Violating Liskov Substitution Principle | Ensure derived class can substitute base |
| Overriding non-virtual functions | Make functions virtual if intended to override |

---

### Practice Questions

After completing this section, you should be able to:

1. Explain what inheritance is and why it is used
2. List and describe the five types of inheritance
3. Explain the difference between public, protected, and private inheritance
4. Describe the order of constructor and destructor calls in inheritance
5. Explain the diamond problem and how to solve it
6. Differentiate between Is-A and Has-A relationships
7. Explain the Liskov Substitution Principle
8. Implement a class hierarchy using inheritance

---

### Next Steps

- Go to [01_Basics_of_Inheritance.md](01_Basics_of_Inheritance.md) to understand Basics of Inheritance.