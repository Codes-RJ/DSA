# README.md

## Constructors and Destructors in C++ - Complete Guide

### Overview

Constructors and destructors are special member functions in C++ that handle object initialization and cleanup. A constructor is automatically called when an object is created, initializing its data members. A destructor is automatically called when an object is destroyed, releasing any resources the object acquired. Understanding constructors and destructors is essential for proper resource management and preventing memory leaks.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [01_Default_Constructor.md](01_Default_Constructor.md) | understand Default Constructor |
| 2. | [02_Parameterized_Constructor.md](02_Parameterized_Constructor.md) | understand Parameterized Constructor |
| 3. | [03_Copy_Constructor.md](03_Copy_Constructor.md) | understand Copy Constructor |
| 4. | [04_Move_Constructor.md](04_Move_Constructor.md) | understand Move Constructor (C++11) |
| 5. | [05_Constructor_Overloading.md](05_Constructor_Overloading.md) | understand Constructor Overloading |
| 6. | [06_Constructor_Initialization_List.md](06_Constructor_Initialization_List.md) | understand Constructor Initialization List |
| 7. | [07_Delegating_Constructors.md](07_Delegating_Constructors.md) | understand Delegating Constructors (C++11) |
| 8. | [08_Destructor.md](08_Destructor.md) | understand Destructor |
| 9. | [09_Virtual_Destructor.md](09_Virtual_Destructor.md) | understand Virtual Destructor |
| 10. | [10_Rule_of_Three_Five_Zero.md](10_Rule_of_Three_Five_Zero.md) | understand Rule of Three, Five, and Zero |
| 11. | [Theory.md](Theory.md) | understand Theoretical Foundations |

---

## 1. Default Constructor

This topic explains the constructor that takes no arguments.

**File:** [01_Default_Constructor.md](01_Default_Constructor.md)

**What you will learn:**
- What is a default constructor
- Compiler-generated default constructor
- When default constructor is automatically called
- Defining custom default constructor
- Default constructor with default arguments
- `= default` and `= delete` syntax (C++11)

**Key Concepts:**
- **No Parameters** - Takes no arguments
- **Automatic Call** - Called when object created without arguments
- **Compiler-Generated** - Provided if no constructor is defined
- **Zero Initialization** - May leave members uninitialized
- **Default Keyword** - `ClassName() = default;`

**Syntax:**
```cpp
class Example {
public:
    // Default constructor
    Example() {
        // initialization code
    }
    
    // Or with default arguments (also acts as default)
    Example(int x = 0) {
        // initialization code
    }
};

// Usage
Example obj1;        // Calls default constructor
Example* obj2 = new Example();  // Calls default constructor
```

---

## 2. Parameterized Constructor

This topic explains constructors that take arguments to initialize objects with specific values.

**File:** [02_Parameterized_Constructor.md](02_Parameterized_Constructor.md)

**What you will learn:**
- Defining constructors with parameters
- Passing arguments to constructors
- Multiple parameterized constructors
- Calling parameterized constructors with different syntaxes
- Default arguments in parameterized constructors

**Key Concepts:**
- **Parameters** - Accepts one or more arguments
- **Explicit Call** - `ClassName obj(10, 20);`
- **Implicit Call** - `ClassName obj = ClassName(10, 20);`
- **Overloading** - Multiple parameterized constructors

**Syntax:**
```cpp
class Rectangle {
private:
    int width, height;
    
public:
    // Parameterized constructor
    Rectangle(int w, int h) {
        width = w;
        height = h;
    }
};

// Usage
Rectangle r1(10, 20);           // Direct initialization
Rectangle r2 = Rectangle(5, 5); // Copy initialization
Rectangle r3{15, 25};           // Uniform initialization (C++11)
```

---

## 3. Copy Constructor

This topic explains the constructor that creates a new object as a copy of an existing object.

**File:** [03_Copy_Constructor.md](03_Copy_Constructor.md)

**What you will learn:**
- What is a copy constructor
- Compiler-generated copy constructor (shallow copy)
- When copy constructor is called
- Defining custom copy constructor (deep copy)
- Copy constructor vs assignment operator
- Preventing copying (`= delete`)

**Key Concepts:**
- **Shallow Copy** - Copies pointer addresses (default)
- **Deep Copy** - Allocates new memory and copies data (custom)
- **Call Scenarios** - Pass by value, return by value, direct initialization
- **Signature** - `ClassName(const ClassName& other)`

**Syntax:**
```cpp
class String {
private:
    char* data;
    
public:
    // Copy constructor (deep copy)
    String(const String& other) {
        data = new char[strlen(other.data) + 1];
        strcpy(data, other.data);
    }
};

// When copy constructor is called
String s1("Hello");
String s2 = s1;      // Copy constructor
String s3(s1);       // Copy constructor
void func(String s); // Copy constructor called when passing by value
```

---

## 4. Move Constructor

This topic explains the move constructor (C++11) that transfers resources from a temporary object.

**File:** [04_Move_Constructor.md](04_Move_Constructor.md)

**What you will learn:**
- What is move semantics (C++11)
- Move constructor vs copy constructor
- When move constructor is called
- Defining move constructor
- `std::move` function
- Benefits of move semantics (performance)

**Key Concepts:**
- **Resource Transfer** - Steals resources instead of copying
- **Temporary Objects** - Rvalues (results of expressions)
- **Signature** - `ClassName(ClassName&& other) noexcept`
- **Nullifying Source** - Source object left in valid but unspecified state

**Syntax:**
```cpp
class String {
private:
    char* data;
    
public:
    // Move constructor
    String(String&& other) noexcept : data(other.data) {
        other.data = nullptr;  // Source no longer owns resource
    }
};

// When move constructor is called
String s1("Hello");
String s2 = std::move(s1);  // Move constructor
String s3 = String("Temp");  // Move constructor (temporary)
```

---

## 5. Constructor Overloading

This topic explains having multiple constructors with different parameter lists.

**File:** [05_Constructor_Overloading.md](05_Constructor_Overloading.md)

**What you will learn:**
- Defining multiple constructors in a class
- How compiler selects the correct constructor
- Overloading rules and ambiguity
- Constructor with default arguments vs overloading
- Best practices for constructor overloading

**Key Concepts:**
- **Multiple Constructors** - Same name, different parameters
- **Overload Resolution** - Compiler matches arguments to parameters
- **Ambiguity** - Occurs when multiple constructors match
- **Delegation** - One constructor calling another

**Syntax:**
```cpp
class Date {
private:
    int day, month, year;
    
public:
    Date() : day(1), month(1), year(2000) {}           // Default
    Date(int d, int m, int y) : day(d), month(m), year(y) {}  // Parameterized
    Date(int d, int m) : day(d), month(m), year(2000) {}      // Partial
};

// Usage
Date d1;              // Calls default
Date d2(15, 8, 2024); // Calls parameterized
Date d3(15, 8);       // Calls partial
```

---

## 6. Constructor Initialization List

This topic explains the initialization list syntax for initializing data members before constructor body executes.

**File:** [06_Constructor_Initialization_List.md](06_Constructor_Initialization_List.md)

**What you will learn:**
- Syntax of member initializer list
- Why initialization list is preferred over assignment in body
- Initializing const and reference members
- Initializing base class constructors
- Order of initialization

**Key Concepts:**
- **Before Body** - Initialization occurs before constructor body
- **Syntax** - `: member1(value1), member2(value2)`
- **Required For** - Const members, reference members, base classes
- **Order** - Initialization order follows declaration order, not list order

**Syntax:**
```cpp
class Student {
private:
    const int id_;        // const member
    string& nameRef_;     // reference member
    string name_;
    int age_;
    
public:
    // Initialization list (required for const and reference)
    Student(int id, string& name, int age) 
        : id_(id),          // const member initialization
          nameRef_(name),   // reference initialization
          name_(name),      // regular member
          age_(age) {}      // regular member
};
```

---

## 7. Delegating Constructors

This topic explains C++11 feature where one constructor can call another constructor of the same class.

**File:** [07_Delegating_Constructors.md](07_Delegating_Constructors.md)

**What you will learn:**
- What are delegating constructors (C++11)
- Syntax for constructor delegation
- Benefits (reducing code duplication)
- Delegation chains
- Restrictions and limitations

**Key Concepts:**
- **Delegation** - One constructor calls another
- **Syntax** - `: ClassName(args)` in initialization list
- **Single Delegation** - Can delegate to only one constructor
- **No Mixed Initialization** - Cannot delegate and initialize members directly

**Syntax:**
```cpp
class Rectangle {
private:
    int width, height;
    
public:
    // Target constructor
    Rectangle(int w, int h) : width(w), height(h) {}
    
    // Delegating constructors
    Rectangle() : Rectangle(0, 0) {}           // Delegates to target
    Rectangle(int side) : Rectangle(side, side) {}  // Delegates to target
    Rectangle(int w) : Rectangle(w, w) {}      // Also delegates
};

// Usage
Rectangle r1;        // Delegates to Rectangle(0,0)
Rectangle r2(10);    // Delegates to Rectangle(10,10)
Rectangle r3(5, 7);  // Direct call
```

---

## 8. Destructor

This topic explains the special member function that cleans up resources when an object is destroyed.

**File:** [08_Destructor.md](08_Destructor.md)

**What you will learn:**
- What is a destructor
- When destructor is automatically called
- Compiler-generated destructor
- Defining custom destructor for cleanup
- Destructor order in inheritance and composition
- Destructor best practices

**Key Concepts:**
- **No Parameters** - Cannot take arguments
- **No Overloading** - Only one destructor per class
- **Automatic Call** - Called when object goes out of scope or `delete`
- **Cleanup** - Release memory, close files, release locks

**Syntax:**
```cpp
class Resource {
private:
    int* data;
    FILE* file;
    
public:
    Resource(int size) {
        data = new int[size];
        file = fopen("data.txt", "w");
    }
    
    // Destructor
    ~Resource() {
        delete[] data;     // Release heap memory
        fclose(file);      // Close file
    }
};

// Destructor called automatically when:
{
    Resource r(100);  // Constructor called
}   // Destructor called here (out of scope)
```

---

## 9. Virtual Destructor

This topic explains why base class destructor should be virtual when using polymorphism.

**File:** [09_Virtual_Destructor.md](09_Virtual_Destructor.md)

**What you will learn:**
- Problem of non-virtual destructor in base class
- Memory leaks with polymorphism
- Virtual destructor syntax
- When to use virtual destructor
- Performance considerations

**Key Concepts:**
- **Base Class Destructor** - Should be virtual if class has virtual functions
- **Proper Cleanup** - Ensures derived destructor is called
- **Undefined Behavior** - Deleting derived object via base pointer without virtual destructor
- **Vtable** - Virtual destructor adds vtable overhead

**Syntax:**
```cpp
class Base {
public:
    Base() { cout << "Base constructor" << endl; }
    virtual ~Base() { cout << "Base destructor" << endl; }  // Virtual
    virtual void display() { cout << "Base" << endl; }
};

class Derived : public Base {
private:
    int* data;
public:
    Derived() : Base(), data(new int[100]) { cout << "Derived constructor" << endl; }
    ~Derived() { delete[] data; cout << "Derived destructor" << endl; }
};

// Without virtual destructor, this would leak memory
Base* ptr = new Derived();
delete ptr;  // Calls both destructors (if virtual)
```

---

## 10. Rule of Three, Five, and Zero

This topic explains the modern C++ guidelines for special member functions.

**File:** [10_Rule_of_Three_Five_Zero.md](10_Rule_of_Three_Five_Zero.md)

**What you will learn:**
- Rule of Three (C++98) - Destructor, Copy Constructor, Copy Assignment
- Rule of Five (C++11) - Adds Move Constructor, Move Assignment
- Rule of Zero - Let compiler generate all special members
- When to follow each rule
- `= default` and `= delete` syntax

**Key Concepts:**

| Rule | Members | Use Case |
|------|---------|----------|
| **Rule of Three** | Destructor, Copy Constructor, Copy Assignment | Managing resources (raw pointers) |
| **Rule of Five** | + Move Constructor, Move Assignment | Modern C++ resource management |
| **Rule of Zero** | None (use RAII containers) | Prefer composition over manual resource management |

**Syntax:**
```cpp
// Rule of Five (manual resource management)
class Resource {
private:
    int* data;
public:
    ~Resource() { delete[] data; }
    Resource(const Resource& other);  // Copy constructor
    Resource& operator=(const Resource& other);  // Copy assignment
    Resource(Resource&& other) noexcept;  // Move constructor
    Resource& operator=(Resource&& other) noexcept;  // Move assignment
};

// Rule of Zero (use RAII containers)
class Person {
private:
    string name_;      // string manages its own memory
    vector<int> ids_;  // vector manages its own memory
public:
    // No destructor, copy, move needed - compiler generates correctly
};
```

---

## 11. Theoretical Foundations

This topic covers the theoretical concepts behind constructors and destructors.

**File:** [Theory.md](Theory.md)

**What you will learn:**
- Object lifetime management
- RAII (Resource Acquisition Is Initialization) idiom
- Constructor failure handling
- Exception safety in constructors
- Memory allocation and object construction phases
- Construction and destruction order in inheritance

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **RAII** | Resource acquisition in constructor, release in destructor |
| **Two-Phase Construction** | Memory allocation then object construction |
| **Construction Order** | Base → Members → Derived |
| **Destruction Order** | Derived → Members → Base (reverse of construction) |
| **Strong Exception Safety** | Constructor should not leak resources on exception |

---

### Prerequisites

Before starting this section, you should have completed:

- [01. Basics](../../01.%20Basics/README.md) - Pointers, dynamic memory
- [02_Classes_and_Objects/README.md](../02_Classes_and_Objects/README.md) - Basic class concepts
- [01_Introduction/README.md](../01_Introduction/README.md) - OOP fundamentals

---

### Sample Class with Constructors and Destructor

```cpp
#include <iostream>
#include <cstring>
using namespace std;

class String {
private:
    char* data_;
    size_t length_;
    
public:
    // Default constructor
    String() : data_(nullptr), length_(0) {
        data_ = new char[1];
        data_[0] = '\0';
        cout << "Default constructor" << endl;
    }
    
    // Parameterized constructor
    String(const char* str) : length_(strlen(str)) {
        data_ = new char[length_ + 1];
        strcpy(data_, str);
        cout << "Parameterized constructor: " << data_ << endl;
    }
    
    // Copy constructor (deep copy)
    String(const String& other) : length_(other.length_) {
        data_ = new char[length_ + 1];
        strcpy(data_, other.data_);
        cout << "Copy constructor: " << data_ << endl;
    }
    
    // Move constructor (C++11)
    String(String&& other) noexcept : data_(other.data_), length_(other.length_) {
        other.data_ = nullptr;
        other.length_ = 0;
        cout << "Move constructor" << endl;
    }
    
    // Destructor
    ~String() {
        delete[] data_;
        cout << "Destructor" << endl;
    }
    
    void display() const {
        if (data_) {
            cout << data_ << endl;
        }
    }
};

int main() {
    String s1("Hello");           // Parameterized constructor
    String s2(s1);                // Copy constructor
    String s3(move(s1));          // Move constructor
    String s4;                    // Default constructor
    
    s2.display();
    s3.display();
    
    return 0;
}
```

---

### Learning Path

```
Level 1: Basic Constructors
├── Default Constructor
├── Parameterized Constructor
└── Constructor Overloading

Level 2: Copy and Move
├── Copy Constructor
├── Move Constructor (C++11)
└── Copy vs Move Semantics

Level 3: Constructor Techniques
├── Initialization List
├── Delegating Constructors (C++11)
└── Constructor Best Practices

Level 4: Destructors
├── Destructor Basics
├── Virtual Destructor
└── RAII Idiom

Level 5: Modern C++ Guidelines
├── Rule of Three
├── Rule of Five
└── Rule of Zero
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Forgetting to delete memory in destructor | Always pair `new` with `delete` in destructor |
| Shallow copy with pointer members | Implement deep copy in copy constructor |
| Not making base destructor virtual | Add `virtual ~Base() = default;` |
| Using assignment instead of initialization list | Use initialization list for const/ref members |
| Throwing exceptions from destructor | Destructors should be `noexcept` |
| Double deletion (shallow copy) | Set pointer to `nullptr` after move/deletion |

---

### Practice Questions

After completing this section, you should be able to:

1. Write a class with default, parameterized, and copy constructors
2. Explain the difference between shallow copy and deep copy
3. Implement a move constructor for a resource-managing class
4. Explain when a virtual destructor is needed
5. Describe the Rule of Three and Rule of Five
6. Use initialization list correctly for const and reference members
7. Implement delegating constructors to reduce code duplication
8. Explain RAII and why destructors are important for resource management

---

### Next Steps

- Go to [01_Default_Constructor.md](01_Default_Constructor.md) to understand Default Constructor.