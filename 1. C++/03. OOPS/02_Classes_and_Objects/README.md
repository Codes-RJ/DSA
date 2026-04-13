# README.md

## Classes and Objects in C++ - Complete Guide

### Overview

Classes and objects are the fundamental building blocks of Object-Oriented Programming in C++. A class is a user-defined data type that acts as a blueprint for creating objects. An object is an instance of a class that contains actual data and can execute the functions defined within the class. Understanding classes and objects is essential for mastering OOP in C++.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [01_Class_Declaration.md](01_Class_Declaration.md) | understand Class Declaration |
| 2. | [02_Object_Creation.md](02_Object_Creation.md) | understand Object Creation |
| 3. | [03_Access_Specifiers.md](03_Access_Specifiers.md) | understand Access Specifiers (public, private, protected) |
| 4. | [04_Data_Members.md](04_Data_Members.md) | understand Data Members (Attributes) |
| 5. | [05_Member_Functions.md](05_Member_Functions.md) | understand Member Functions (Methods) |
| 6. | [06_Static_Members.md](06_Static_Members.md) | understand Static Members |
| 7. | [07_Const_Members.md](07_Const_Members.md) | understand Const Members |
| 8. | [08_Inline_Functions.md](08_Inline_Functions.md) | understand Inline Functions in Classes |
| 9. | [09_Nested_Classes.md](09_Nested_Classes.md) | understand Nested Classes |
| 10. | [Theory.md](Theory.md) | understand Theoretical Foundations of Classes and Objects |

---

## 1. Class Declaration

This topic explains how to declare a class in C++ and the syntax involved.

**File:** [01_Class_Declaration.md](01_Class_Declaration.md)

**What you will learn:**
- Syntax of class declaration
- Class naming conventions (PascalCase)
- Class body and terminating semicolon
- Difference between class and struct in C++
- Forward declaration of classes
- Class scope and visibility

**Key Concepts:**
- **Class Keyword** - `class ClassName { };`
- **Class Body** - Enclosed in curly braces `{}`
- **Terminating Semicolon** - Mandatory after class definition
- **Member Section** - Divided into public, private, protected
- **Class vs Struct** - Struct members are public by default; class members are private by default

**Syntax:**
```cpp
class ClassName {
private:
    // Private members (data and functions)
    
public:
    // Public members (data and functions)
    
protected:
    // Protected members (for inheritance)
};
```

---

## 2. Object Creation

This topic explains how to create objects (instances) from a class.

**File:** [02_Object_Creation.md](02_Object_Creation.md)

**What you will learn:**
- Creating objects on stack (automatic storage)
- Creating objects on heap (dynamic storage using `new`)
- Creating arrays of objects
- Object lifecycle (creation to destruction)
- Object memory layout
- Multiple objects of the same class

**Key Concepts:**
- **Stack Object** - `ClassName obj;`
- **Heap Object** - `ClassName* obj = new ClassName();`
- **Object Array** - `ClassName arr[10];`
- **Dynamic Array** - `ClassName* arr = new ClassName[10];`
- **Object Pointer** - `ClassName* ptr = &obj;`
- **Deleting Heap Objects** - `delete obj;` or `delete[] arr;`

**Syntax:**
```cpp
// Stack allocation
ClassName obj1;

// Heap allocation
ClassName* obj2 = new ClassName();

// Array of objects
ClassName objArray[5];

// Dynamic array
ClassName* dynArray = new ClassName[10];
```

---

## 3. Access Specifiers

This topic explains the three access specifiers in C++ that control member visibility.

**File:** [03_Access_Specifiers.md](03_Access_Specifiers.md)

**What you will learn:**
- `public` - Accessible from anywhere
- `private` - Accessible only within the class
- `protected` - Accessible within class and derived classes
- Default access (private for class, public for struct)
- When to use each access specifier
- Access control in inheritance

**Key Concepts:**

| Specifier | Same Class | Derived Class | Outside Class |
|-----------|------------|---------------|---------------|
| **public** | Yes | Yes | Yes |
| **protected** | Yes | Yes | No |
| **private** | Yes | No | No |

**Syntax:**
```cpp
class Example {
private:
    int privateVar;     // Only accessible inside Example
    
protected:
    int protectedVar;   // Accessible in Example and derived classes
    
public:
    int publicVar;      // Accessible anywhere
    
    void publicMethod() {
        privateVar = 10;  // OK - inside class
    }
};
```

---

## 4. Data Members

This topic explains the attributes (variables) that hold the state of an object.

**File:** [04_Data_Members.md](04_Data_Members.md)

**What you will learn:**
- Declaring data members inside a class
- Initializing data members (constructors, default values)
- Accessing data members via objects
- Data member naming conventions (often with trailing underscore)
- Constant data members
- Reference data members
- Data member types (built-in, user-defined, pointers)

**Key Concepts:**
- **Instance Variables** - Each object has its own copy
- **Class Variables** - Shared across all objects (static members)
- **Member Initialization** - Using constructors or in-class initializers (C++11)
- **Access Methods** - Getters and setters for private data

**Syntax:**
```cpp
class Student {
private:
    string name_;       // trailing underscore convention
    int age_;
    static int count_;  // static data member (shared)
    
public:
    Student(string name, int age) : name_(name), age_(age) {}
    
    string getName() const { return name_; }
    void setName(string name) { name_ = name; }
};
```

---

## 5. Member Functions

This topic explains the methods (functions) that define the behavior of an object.

**File:** [05_Member_Functions.md](05_Member_Functions.md)

**What you will learn:**
- Defining member functions inside the class
- Defining member functions outside the class (using scope resolution `::`)
- Calling member functions on objects
- Const member functions
- Member function overloading
- Default arguments in member functions
- Returning `*this` from member functions

**Key Concepts:**
- **Inside Definition** - Function body inside class
- **Outside Definition** - `returnType ClassName::functionName() { }`
- **Const Member Function** - `void func() const { }` (cannot modify object)
- **This Pointer** - Implicit pointer to current object
- **Chaining** - Returning `*this` for method chaining

**Syntax:**
```cpp
class Calculator {
private:
    int value_;
    
public:
    // Inside definition
    void setValue(int v) { value_ = v; }
    
    // Outside definition (declaration inside, definition outside)
    int getValue() const;
    
    // Method chaining
    Calculator& add(int x) {
        value_ += x;
        return *this;
    }
};

// Outside definition
int Calculator::getValue() const {
    return value_;
}
```

---

## 6. Static Members

This topic explains static data members and static member functions that belong to the class rather than individual objects.

**File:** [06_Static_Members.md](06_Static_Members.md)

**What you will learn:**
- Static data members (shared across all objects)
- Static member functions (can be called without an object)
- Initialization of static data members (outside class definition)
- Accessing static members (using class name or object)
- Use cases for static members (counters, singleton pattern)
- Static vs non-static members

**Key Concepts:**
- **Shared Storage** - One copy for all objects
- **Class-Level Access** - No `this` pointer in static functions
- **External Initialization** - Must be defined outside class
- **Access Syntax** - `ClassName::staticMember`

**Syntax:**
```cpp
class Counter {
private:
    static int totalCount_;  // Declaration
    
public:
    Counter() { totalCount_++; }
    ~Counter() { totalCount_--; }
    
    static int getCount() { return totalCount_; }
};

// Definition and initialization outside class
int Counter::totalCount_ = 0;

// Usage
int main() {
    cout << Counter::getCount() << endl;  // 0
    Counter c1, c2;
    cout << Counter::getCount() << endl;  // 2
}
```

---

## 7. Const Members

This topic explains constant data members and constant member functions.

**File:** [07_Const_Members.md](07_Const_Members.md)

**What you will learn:**
- Constant data members (initialized in constructor initializer list)
- Constant member functions (cannot modify object)
- Constant objects (can only call const member functions)
- Mutable keyword (allows modification in const functions)
- When to use const correctness

**Key Concepts:**
- **Const Data Member** - Value cannot change after initialization
- **Const Member Function** - Guarantees not to modify object
- **Const Object** - Object cannot be modified
- **Const Correctness** - Marking functions const when they don't modify

**Syntax:**
```cpp
class Rectangle {
private:
    const int width_;   // const data member
    const int height_;
    mutable int accessCount_;  // can be modified in const functions
    
public:
    Rectangle(int w, int h) : width_(w), height_(h), accessCount_(0) {}
    
    int getArea() const {  // const member function
        accessCount_++;    // allowed because mutable
        return width_ * height_;
    }
};

const Rectangle r(10, 20);  // const object
int area = r.getArea();     // OK - getArea is const
```

---

## 8. Inline Functions in Classes

This topic explains inline functions and their use within classes.

**File:** [08_Inline_Functions.md](08_Inline_Functions.md)

**What you will learn:**
- What are inline functions
- Member functions defined inside class are implicitly inline
- Explicit inline keyword for functions defined outside
- Benefits of inline (reduced function call overhead)
- When to use and when to avoid inline
- Inline vs macros

**Key Concepts:**
- **Implicit Inline** - Functions defined inside class body
- **Explicit Inline** - Using `inline` keyword for outside definitions
- **Compiler Decision** - `inline` is a request, not a command
- **Header Files** - Inline functions are defined in headers

**Syntax:**
```cpp
class Math {
public:
    // Implicitly inline (defined inside class)
    int square(int x) { return x * x; }
    
    // Explicitly inline (defined outside)
    int cube(int x);
};

// Explicit inline definition
inline int Math::cube(int x) {
    return x * x * x;
}
```

---

## 9. Nested Classes

This topic explains classes defined inside other classes.

**File:** [09_Nested_Classes.md](09_Nested_Classes.md)

**What you will learn:**
- Defining a class inside another class
- Access rules for nested classes
- Scope and visibility of nested classes
- When to use nested classes (helper classes, iterators)
- Nested class vs separate class

**Key Concepts:**
- **Inner Class** - Defined within outer class scope
- **Access** - Can access outer class's static members
- **No Special Access** - Cannot access non-static members without an instance
- **Visibility** - Access controlled by outer class access specifier

**Syntax:**
```cpp
class Outer {
private:
    static int staticValue_;
    int instanceValue_;
    
public:
    class Inner {
    public:
        void display() {
            cout << staticValue_;  // OK - static member
            // cout << instanceValue_;  // Error - non-static
        }
    };
    
    Inner getInner() { return Inner(); }
};

int Outer::staticValue_ = 42;
```

---

## 10. Theoretical Foundations

This topic covers the theoretical concepts behind classes and objects.

**File:** [Theory.md](Theory.md)

**What you will learn:**
- Object-oriented analysis and design
- UML class diagrams
- Relationship between classes (association, aggregation, composition)
- Encapsulation theory
- Information hiding principles
- Object lifetime and memory management theory

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Association** | "Uses-a" relationship (Teacher teaches Student) |
| **Aggregation** | "Has-a" relationship (weak ownership) |
| **Composition** | "Part-of" relationship (strong ownership) |
| **Dependency** | One class uses another (temporary) |
| **UML Notation** | Standard diagrams for class design |

---

### Prerequisites

Before starting this section, you should have completed:

- [01. Basics](../../01.%20Basics/README.md) - Variables, functions, pointers
- [01_Introduction/README.md](../01_Introduction/README.md) - Basic OOP concepts

---

### Sample Class Definition

```cpp
#include <iostream>
#include <string>
using namespace std;

class Student {
private:
    string name_;
    int age_;
    static int totalStudents_;
    
public:
    // Constructor
    Student(string name, int age) : name_(name), age_(age) {
        totalStudents_++;
    }
    
    // Destructor
    ~Student() {
        totalStudents_--;
    }
    
    // Const member functions (getters)
    string getName() const { return name_; }
    int getAge() const { return age_; }
    
    // Non-const member function (setter)
    void setAge(int age) { age_ = age; }
    
    // Static member function
    static int getTotalStudents() { return totalStudents_; }
    
    // Member function defined outside
    void display();
};

// Static member definition
int Student::totalStudents_ = 0;

// Member function definition outside class
void Student::display() {
    cout << name_ << " (" << age_ << ")" << endl;
}

int main() {
    Student s1("Alice", 20);
    Student s2("Bob", 22);
    
    s1.display();
    s2.display();
    
    cout << "Total students: " << Student::getTotalStudents() << endl;
    
    return 0;
}
```

---

### Learning Path

```
Level 1: Basic Class Structure
├── Class Declaration
├── Object Creation
└── Access Specifiers

Level 2: Class Components
├── Data Members
├── Member Functions
└── Constructors and Destructors (next folder)

Level 3: Advanced Class Features
├── Static Members
├── Const Members
└── Inline Functions

Level 4: Class Relationships
├── Nested Classes
├── Friend Functions (Advanced OOP)
└── Class Design Patterns
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Forgetting semicolon after class definition | Always add `;` after closing `}` |
| Making all data members public | Use private by default, expose only what's needed |
| Confusing class with object | Class = blueprint, Object = instance |
| Accessing private members from outside | Use public getters/setters |
| Forgetting to define static members outside class | Define `Type Class::member = value;` in .cpp |
| Modifying object in const member function | Use `mutable` for exceptions or redesign |
| Memory leaks with heap objects | Always `delete` objects created with `new` |

---

### Practice Questions

After completing this section, you should be able to:

1. Declare a class with private and public members
2. Create objects on stack and heap
3. Explain the difference between public, private, and protected
4. Write a class with static data member and static function
5. Create a const member function and explain its purpose
6. Define a member function inside and outside the class
7. Create a nested class and access it from outer class
8. Explain the difference between class and struct in C++

---

### Next Steps

- Go to [01_Class_Declaration.md](01_Class_Declaration.md) to understand Class Declaration.