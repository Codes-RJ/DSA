# README.md

## Run-Time Polymorphism in C++ - Complete Guide

### Overview

Run-time polymorphism, also known as dynamic polymorphism or late binding, is a type of polymorphism where the function to be called is determined at runtime rather than at compile time. It is achieved through virtual functions and function overriding. Run-time polymorphism allows a base class pointer or reference to call derived class functions, enabling flexible and extensible designs.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [01_Virtual_Functions.md](01_Virtual_Functions.md) | understand Virtual Functions |
| 2. | [02_Override_Specifier.md](02_Override_Specifier.md) | understand Override Specifier (C++11) |
| 3. | [03_Final_Specifier.md](03_Final_Specifier.md) | understand Final Specifier (C++11) |
| 4. | [04_Pure_Virtual_Functions.md](04_Pure_Virtual_Functions.md) | understand Pure Virtual Functions |
| 5. | [05_Abstract_Classes.md](05_Abstract_Classes.md) | understand Abstract Classes |
| 6. | [06_Virtual_Table.md](06_Virtual_Table.md) | understand Virtual Table (VTable) Mechanism |
| 7. | [07_Run_Time_Type_Information.md](07_Run_Time_Type_Information.md) | understand Run-Time Type Information (RTTI) |

---

## 1. Virtual Functions

This topic explains the core concept of virtual functions that enables run-time polymorphism.

**File:** [01_Virtual_Functions.md](01_Virtual_Functions.md)

**What you will learn:**
- What are virtual functions
- How virtual functions enable dynamic dispatch
- Syntax for declaring virtual functions
- Virtual function overriding rules
- Virtual functions in inheritance hierarchies
- Virtual destructors and their importance
- Limitations of virtual functions

**Key Concepts:**

| Concept | Description | Example |
|---------|-------------|---------|
| **Virtual Keyword** | Marks a function for dynamic dispatch | `virtual void draw()` |
| **Function Overriding** | Derived class provides its own implementation | `void draw() override` |
| **Dynamic Dispatch** | Function call resolved at runtime | Based on actual object type |
| **Virtual Destructor** | Ensures proper cleanup of derived objects | `virtual ~Base()` |
| **VTable** | Table of function pointers for virtual functions | Created by compiler |

**Syntax:**
```cpp
#include <iostream>
using namespace std;

class Base {
public:
    // Virtual function
    virtual void show() {
        cout << "Base::show()" << endl;
    }
    
    // Non-virtual function
    void display() {
        cout << "Base::display()" << endl;
    }
    
    // Virtual destructor (important!)
    virtual ~Base() {
        cout << "Base destructor" << endl;
    }
};

class Derived : public Base {
public:
    // Overriding virtual function
    void show() override {
        cout << "Derived::show()" << endl;
    }
    
    // Hiding non-virtual function (not overriding)
    void display() {
        cout << "Derived::display()" << endl;
    }
    
    ~Derived() {
        cout << "Derived destructor" << endl;
    }
};

int main() {
    Base* ptr = new Derived();
    
    ptr->show();     // Calls Derived::show() (virtual - dynamic dispatch)
    ptr->display();  // Calls Base::display() (non-virtual - static binding)
    
    delete ptr;      // Calls both destructors (virtual destructor)
    
    return 0;
}
```

**Output:**
```
Derived::show()
Base::display()
Derived destructor
Base destructor
```

---

## 2. Override Specifier

This topic explains the override specifier introduced in C++11 to prevent accidental errors when overriding virtual functions.

**File:** [02_Override_Specifier.md](02_Override_Specifier.md)

**What you will learn:**
- What is the override specifier (C++11)
- Why override is useful (catches signature mismatches)
- Syntax for using override
- Common mistakes caught by override
- Best practices for using override

**Key Concepts:**
- **Override Keyword** - Explicitly marks a function as overriding a virtual function
- **Compile-Time Check** - Compiler verifies base class has matching virtual function
- **Error Prevention** - Catches typos and signature mismatches
- **Code Clarity** - Makes intent explicit to readers

**Syntax:**
```cpp
class Base {
public:
    virtual void func1(int x) {
        cout << "Base::func1" << endl;
    }
    
    virtual void func2() const {
        cout << "Base::func2" << endl;
    }
    
    virtual void func3() {
        cout << "Base::func3" << endl;
    }
};

class Derived : public Base {
public:
    // Correct override
    void func1(int x) override {
        cout << "Derived::func1" << endl;
    }
    
    // Correct override with const
    void func2() const override {
        cout << "Derived::func2" << endl;
    }
    
    // WRONG - missing const - compiler error
    // void func2() override { }  // Error!
    
    // WRONG - different parameter type - compiler error
    // void func1(double x) override { }  // Error!
    
    // WRONG - no matching virtual function in base
    // void func4() override { }  // Error!
};
```

**Common Errors Caught by Override:**
```cpp
class Base {
public:
    virtual void process(int x) const;
    virtual void handle(double d);
    virtual void execute();
};

class Derived : public Base {
public:
    // Error: missing const
    // void process(int x) override { }
    
    // Error: wrong parameter type
    // void handle(int d) override { }
    
    // Error: wrong return type (if not covariant)
    // int execute() override { return 0; }
    
    // Correct versions:
    void process(int x) const override { }
    void handle(double d) override { }
    void execute() override { }
};
```

---

## 3. Final Specifier

This topic explains the final specifier introduced in C++11 to prevent further overriding or inheritance.

**File:** [03_Final_Specifier.md](03_Final_Specifier.md)

**What you will learn:**
- What is the final specifier (C++11)
- Using final to prevent function overriding
- Using final to prevent class inheritance
- When to use final
- Benefits of final (optimization, design clarity)

**Key Concepts:**

| Usage | Syntax | Effect |
|-------|--------|--------|
| **Final Function** | `virtual void func() final;` | Cannot be overridden in derived classes |
| **Final Class** | `class ClassName final { };` | Cannot be inherited from |

**Syntax - Final Function:**
```cpp
class Base {
public:
    virtual void func1() {
        cout << "Base::func1" << endl;
    }
    
    virtual void func2() final {
        cout << "Base::func2 - cannot be overridden" << endl;
    }
};

class Derived : public Base {
public:
    void func1() override {
        cout << "Derived::func1" << endl;  // OK
    }
    
    // Error: cannot override final function
    // void func2() override { }  // Compiler error!
};
```

**Syntax - Final Class:**
```cpp
// This class cannot be inherited from
class FinalClass final {
public:
    void display() {
        cout << "This class is final" << endl;
    }
};

// Error: cannot inherit from final class
// class DerivedClass : public FinalClass { };  // Compiler error!

// Normal class that can be inherited
class NormalClass {
public:
    virtual void show() {
        cout << "NormalClass" << endl;
    }
};

class DerivedNormal : public NormalClass {
public:
    void show() override {
        cout << "DerivedNormal" << endl;
    }
};
```

---

## 4. Pure Virtual Functions

This topic explains pure virtual functions that have no implementation in the base class.

**File:** [04_Pure_Virtual_Functions.md](04_Pure_Virtual_Functions.md)

**What you will learn:**
- What are pure virtual functions
- Syntax for pure virtual functions (`= 0`)
- Why pure virtual functions are used
- Classes with pure virtual functions become abstract
- Pure virtual functions can have bodies (rare)
- When to use pure virtual functions

**Key Concepts:**
- **Pure Virtual** - Function with `= 0` syntax
- **No Implementation** - Base class provides no default implementation
- **Forced Override** - Derived classes must override (unless they become abstract)
- **Interface Definition** - Defines what derived classes must implement

**Syntax:**
```cpp
class Shape {
public:
    // Pure virtual function
    virtual double getArea() = 0;
    
    // Pure virtual function (can have body - rare but possible)
    virtual void draw() = 0;
    
    // Non-virtual function with implementation
    void display() {
        cout << "Shape display" << endl;
    }
    
    virtual ~Shape() { }
};

// Pure virtual function can have a body (rare)
void Shape::draw() {
    cout << "Default drawing" << endl;
}

class Circle : public Shape {
private:
    double radius_;
    
public:
    Circle(double r) : radius_(r) { }
    
    // Must override pure virtual functions
    double getArea() override {
        return 3.14159 * radius_ * radius_;
    }
    
    void draw() override {
        Shape::draw();  // Can call base implementation
        cout << "Drawing Circle" << endl;
    }
};

class Rectangle : public Shape {
private:
    double length_, width_;
    
public:
    Rectangle(double l, double w) : length_(l), width_(w) { }
    
    double getArea() override {
        return length_ * width_;
    }
    
    void draw() override {
        cout << "Drawing Rectangle" << endl;
    }
};

// Cannot create object of Shape - it's abstract
// Shape s;  // Error!

int main() {
    Shape* shapes[2];
    shapes[0] = new Circle(5);
    shapes[1] = new Rectangle(4, 6);
    
    for (int i = 0; i < 2; i++) {
        cout << "Area: " << shapes[i]->getArea() << endl;
        shapes[i]->draw();
    }
    
    for (int i = 0; i < 2; i++) {
        delete shapes[i];
    }
    
    return 0;
}
```

---

## 5. Abstract Classes

This topic explains abstract classes that cannot be instantiated and serve as interfaces.

**File:** [05_Abstract_Classes.md](05_Abstract_Classes.md)

**What you will learn:**
- What are abstract classes
- How to create abstract classes (at least one pure virtual function)
- Cannot create objects of abstract classes
- Can create pointers and references to abstract classes
- Abstract classes as interfaces
- Concrete derived classes

**Key Concepts:**
- **Abstract Class** - Class with at least one pure virtual function
- **No Instantiation** - Cannot create objects
- **Interface** - Defines contract for derived classes
- **Concrete Class** - Derived class that overrides all pure virtual functions

**Syntax:**
```cpp
// Abstract class (interface)
class Drawable {
public:
    virtual void draw() = 0;
    virtual void setColor(string color) = 0;
    virtual ~Drawable() { }
};

// Another abstract class
class Resizable {
public:
    virtual void resize(double factor) = 0;
    virtual ~Resizable() { }
};

// Concrete class implementing multiple interfaces
class Shape : public Drawable, public Resizable {
private:
    string color_;
    double size_;
    
public:
    void draw() override {
        cout << "Drawing shape with color " << color_ << endl;
    }
    
    void setColor(string color) override {
        color_ = color;
    }
    
    void resize(double factor) override {
        size_ *= factor;
        cout << "Resized to " << size_ << endl;
    }
};

// Partially abstract class (still abstract)
class PartialAbstract : public Drawable {
public:
    void setColor(string color) override {
        cout << "Color set to " << color << endl;
    }
    // draw() is still pure virtual - class remains abstract
};

int main() {
    // Cannot create object of abstract class
    // Drawable d;  // Error!
    
    // Can create pointer to abstract class
    Drawable* ptr = new Shape();
    ptr->draw();
    
    delete ptr;
    
    return 0;
}
```

---

## 6. Virtual Table Mechanism

This topic explains the internal implementation of virtual functions using virtual tables.

**File:** [06_Virtual_Table.md](06_Virtual_Table.md)

**What you will learn:**
- What is Virtual Table (VTable)
- What is Virtual Pointer (VPtr)
- How virtual functions are implemented internally
- Memory layout of objects with virtual functions
- Performance implications of virtual functions
- Multiple inheritance and VTables

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **VTable** | Per-class table of function pointers for virtual functions |
| **VPtr** | Per-object pointer pointing to the class's VTable |
| **Static Binding** | Function call resolved at compile time (no VTable) |
| **Dynamic Binding** | Function call resolved at runtime (via VTable) |

**Memory Layout:**
```
Object without virtual functions:
┌────────────┐
│   data     │
└────────────┘

Object with virtual functions:
┌────────────┐
│   vptr     │ ──→ Class VTable
├────────────┤     ┌──────────────┐
│   data     │     │ func1 ptr    │ ──→ actual func1
└────────────┘     ├──────────────┤
                   │ func2 ptr    │ ──→ actual func2
                   └──────────────┘
```

**Example Demonstrating VTable:**
```cpp
#include <iostream>
using namespace std;

class Base {
public:
    virtual void func1() { cout << "Base::func1" << endl; }
    virtual void func2() { cout << "Base::func2" << endl; }
    void func3() { cout << "Base::func3" << endl; }
};

class Derived : public Base {
public:
    void func1() override { cout << "Derived::func1" << endl; }
    virtual void func4() { cout << "Derived::func4" << endl; }
};

int main() {
    Base* b = new Base();
    Base* d = new Derived();
    
    // Virtual function calls (via VTable)
    b->func1();  // Calls Base::func1
    d->func1();  // Calls Derived::func1 (via VTable)
    
    // Non-virtual function call (compile time)
    b->func3();  // Calls Base::func3
    d->func3();  // Calls Base::func3 (not overridden)
    
    delete b;
    delete d;
    
    return 0;
}
```

---

## 7. Run-Time Type Information (RTTI)

This topic explains RTTI features that allow type identification at runtime.

**File:** [07_Run_Time_Type_Information.md](07_Run_Time_Type_Information.md)

**What you will learn:**
- What is Run-Time Type Information (RTTI)
- `typeid` operator for getting type information
- `dynamic_cast` for safe downcasting
- When to use RTTI (and when to avoid)
- Performance considerations

**Key Concepts:**

| Feature | Description | Use Case |
|---------|-------------|----------|
| **typeid** | Returns type information at runtime | Type comparison, logging |
| **dynamic_cast** | Safe downcasting with runtime check | Converting base to derived pointer |
| **type_info** | Class containing type information | Obtaining type names |

**Syntax:**
```cpp
#include <iostream>
#include <typeinfo>
using namespace std;

class Base {
public:
    virtual ~Base() { }  // Required for RTTI
};

class Derived1 : public Base { };
class Derived2 : public Base { };

void identifyType(Base* ptr) {
    // Using typeid
    if (typeid(*ptr) == typeid(Derived1)) {
        cout << "It's a Derived1 object" << endl;
    }
    else if (typeid(*ptr) == typeid(Derived2)) {
        cout << "It's a Derived2 object" << endl;
    }
    else if (typeid(*ptr) == typeid(Base)) {
        cout << "It's a Base object" << endl;
    }
    
    // Get type name
    cout << "Type name: " << typeid(*ptr).name() << endl;
    
    // Using dynamic_cast for downcasting
    Derived1* d1 = dynamic_cast<Derived1*>(ptr);
    if (d1) {
        cout << "Successfully cast to Derived1" << endl;
    }
    
    Derived2* d2 = dynamic_cast<Derived2*>(ptr);
    if (d2) {
        cout << "Successfully cast to Derived2" << endl;
    }
}

int main() {
    Base* b = new Base();
    Derived1* d1 = new Derived1();
    Derived2* d2 = new Derived2();
    
    cout << "=== Identifying Base ===" << endl;
    identifyType(b);
    
    cout << "\n=== Identifying Derived1 ===" << endl;
    identifyType(d1);
    
    cout << "\n=== Identifying Derived2 ===" << endl;
    identifyType(d2);
    
    delete b;
    delete d1;
    delete d2;
    
    return 0;
}
```

---

### Run-Time Polymorphism Summary

| Feature | Purpose | Key Keyword |
|---------|---------|-------------|
| **Virtual Functions** | Enable dynamic dispatch | `virtual` |
| **Override** | Catch signature errors | `override` |
| **Final** | Prevent overriding/inheritance | `final` |
| **Pure Virtual** | Create abstract classes | `= 0` |
| **Abstract Class** | Define interfaces | (pure virtual functions) |
| **VTable** | Internal mechanism | (compiler-generated) |
| **RTTI** | Runtime type identification | `typeid`, `dynamic_cast` |

---

### Prerequisites

Before starting this section, you should have completed:

- [01. Basics](../../../01.%20Basics/README.md) - Pointers, references
- [02_Classes_and_Objects/README.md](../../02_Classes_and_Objects/README.md) - Class basics
- [05_Inheritance/README.md](../../05_Inheritance/README.md) - Inheritance concepts
- [01_Compile_Time_Polymorphism/README.md](../01_Compile_Time_Polymorphism/README.md) - Overloading basics

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Forgetting `virtual` keyword in base class | Mark functions as `virtual` for dynamic dispatch |
| Not using `override` specifier | Use `override` to catch signature errors |
| Non-virtual destructor in base class | Always make base destructor `virtual` |
| Calling virtual function in constructor/destructor | Avoid - doesn't work as expected (static binding) |
| Object slicing | Use pointers or references, not pass by value |
| Excessive use of RTTI | Prefer virtual functions over RTTI |
| `dynamic_cast` on non-polymorphic type | Base class must have at least one virtual function |

---

### Practice Questions

After completing this section, you should be able to:

1. Define virtual functions and explain their purpose
2. Differentiate between virtual and non-virtual functions
3. Explain why base class destructor should be virtual
4. Use the `override` specifier and explain its benefits
5. Use the `final` specifier for functions and classes
6. Create abstract classes using pure virtual functions
7. Explain the VTable and VPtr mechanism
8. Use `typeid` and `dynamic_cast` for runtime type identification

---

### Next Steps

- Go to [01_Virtual_Functions.md](01_Virtual_Functions.md) to understand Virtual Functions.