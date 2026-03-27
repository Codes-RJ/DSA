# 02_Classes_and_Objects/Theory.md

# Classes and Objects in C++ - Theory Guide

## 📖 Overview

Classes and objects form the foundation of Object-Oriented Programming in C++. A **class** is a user-defined data type that serves as a blueprint for creating objects. An **object** is an instance of a class that occupies memory and has its own state (data members) and behavior (member functions). Understanding classes and objects is essential for mastering OOP in C++.

---

## 🎯 Core Concepts

### 1. **Class Definition**

A class is a blueprint that defines:
- **Data members**: Variables that store the state
- **Member functions**: Functions that define behavior
- **Access specifiers**: Control visibility of members

```cpp
class ClassName {
private:
    // Private data members (encapsulation)
    int privateData;
    
protected:
    // Protected members (accessible to derived classes)
    int protectedData;
    
public:
    // Public interface
    ClassName();           // Constructor
    ~ClassName();          // Destructor
    void publicMethod();   // Member function
};
```

---

### 2. **Object Creation**

Objects can be created in two ways:

#### a) Stack Allocation (Automatic Storage)
```cpp
ClassName obj;           // Default constructor
ClassName obj2(10, 20);  // Parameterized constructor
ClassName obj3 = obj2;   // Copy constructor
```

#### b) Heap Allocation (Dynamic Storage)
```cpp
ClassName* ptr = new ClassName();    // Allocate on heap
delete ptr;                          // Manual deallocation
```

---

### 3. **Memory Layout of Objects**

When an object is created, memory is allocated for its data members. Member functions are stored separately and shared across all objects.

```
Object in Memory:
┌─────────────────────┐
│   Data Member 1     │  ← Unique to each object
├─────────────────────┤
│   Data Member 2     │  ← Unique to each object
├─────────────────────┤
│   Data Member 3     │  ← Unique to each object
└─────────────────────┘

Member functions (shared):
┌─────────────────────┐
│   Function 1        │  ← Shared by all objects
├─────────────────────┤
│   Function 2        │  ← Shared by all objects
└─────────────────────┘
```

---

## 📊 Class Components Breakdown

### Data Members

| Type | Storage | Lifetime | Access |
|------|---------|----------|--------|
| **Instance variables** | Per object | Object lifetime | Via object reference |
| **Static variables** | Class-wide | Program lifetime | Via class name or object |
| **Const members** | Per object | Object lifetime | Cannot be modified after initialization |
| **Reference members** | Per object | Object lifetime | Must be initialized in constructor |

### Member Functions

| Type | Description | Call Syntax |
|------|-------------|-------------|
| **Instance methods** | Operate on specific objects | `obj.method()` |
| **Static methods** | Belong to class, not objects | `ClassName::method()` |
| **Const methods** | Promise not to modify object | `obj.constMethod()` |
| **Inline methods** | Expanded at compile time | Defined inside class |
| **Virtual methods** | Support polymorphism | `obj.virtualMethod()` |

---

## 🔧 Access Specifiers Deep Dive

### Public
- Members accessible from anywhere
- Defines the interface of the class
- Should be used for methods, not data (encapsulation)

### Private
- Members accessible only within the class
- Used for data hiding
- Can be accessed via public getters/setters

### Protected
- Members accessible within class and derived classes
- Used for inheritance hierarchies
- Balances encapsulation and extensibility

```cpp
class Example {
private:
    int secret;           // Only accessible within Example
  
protected:
    int familySecret;     // Accessible in Example and derived classes
  
public:
    int publicInfo;       // Accessible everywhere
  
    void setSecret(int s) { secret = s; }  // Public interface
    int getSecret() { return secret; }     // Public interface
};
```

---

## 📐 The `this` Pointer

Every non-static member function has an implicit `this` pointer that points to the current object.

```cpp
class Counter {
private:
    int value;
    
public:
    Counter& increment() {
        this->value++;    // Explicit use of this
        return *this;     // Return reference to current object
    }
    
    void setValue(int value) {
        this->value = value;  // Resolves name conflict
    }
};
```

**Uses of `this`:**
- Distinguish between parameter and member with same name
- Return reference to current object for method chaining
- Pass current object to other functions
- In overloaded operators

---

## 🏗️ Class Organization Best Practices

### 1. **Separation of Interface and Implementation**

```cpp
// header.h - Interface
class Calculator {
public:
    void add(int a, int b);
    int getResult() const;
    
private:
    int result;
};

// implementation.cpp - Implementation
void Calculator::add(int a, int b) {
    result = a + b;  // Implementation hidden from users
}

int Calculator::getResult() const {
    return result;
}
```

### 2. **Const Correctness**

```cpp
class String {
private:
    char* data;
    int length;
    
public:
    // Const methods promise not to modify object
    int getLength() const { return length; }
    char getChar(int index) const { return data[index]; }
    
    // Non-const methods can modify
    void setChar(int index, char c) { data[index] = c; }
};
```

### 3. **Initialization vs Assignment**

```cpp
class Student {
private:
    const int id;        // Must be initialized, not assigned
    string& name;        // Reference must be initialized
    int age;
    
public:
    // Constructor initialization list (correct)
    Student(int i, string& n, int a) : id(i), name(n), age(a) {}
    
    // Assignment in body (wrong for const and references)
    // Student(int i, string& n, int a) {
    //     id = i;      // Error! Can't assign to const
    //     name = n;    // Error! Can't assign to reference
    //     age = a;
    // }
};
```

---

## 📊 Size of Objects

The size of an object depends on:
- Size of all non-static data members
- Padding for alignment
- Virtual function table pointer (if any)

```cpp
#include <iostream>
using namespace std;

class Empty { };                    // Size: 1 byte (C++ guarantees unique addresses)

class Simple {
    int a;                          // 4 bytes
    char b;                         // 1 byte + 3 padding
};                                  // Total: 8 bytes

class WithVirtual {
    int a;
    virtual void func() { }         // Adds vptr (8 bytes on 64-bit)
};                                  // Total: 16 bytes (int + vptr + padding)

int main() {
    cout << "Size of Empty: " << sizeof(Empty) << endl;        // 1
    cout << "Size of Simple: " << sizeof(Simple) << endl;      // 8
    cout << "Size of WithVirtual: " << sizeof(WithVirtual) << endl; // 16
    return 0;
}
```

---

## 🔄 Object Lifetime

### Creation
1. Memory allocated
2. Constructor called
3. Object initialized

### Destruction
1. Destructor called
2. Memory deallocated

```cpp
class Resource {
public:
    Resource() {
        cout << "Resource acquired" << endl;
        // Acquire resources
    }
    
    ~Resource() {
        cout << "Resource released" << endl;
        // Release resources
    }
};

void function() {
    Resource r;              // Constructor called
    // ... use resource
}                            // Destructor called automatically
```

---

## 📚 Summary Table

| Concept | Description | Example |
|---------|-------------|---------|
| **Class** | Blueprint for objects | `class Car { ... };` |
| **Object** | Instance of class | `Car myCar;` |
| **Data Member** | Variable in class | `int speed;` |
| **Member Function** | Function in class | `void accelerate();` |
| **Constructor** | Initializes object | `Car() { speed = 0; }` |
| **Destructor** | Cleans up object | `~Car() { }` |
| **`this` Pointer** | Points to current object | `this->speed` |
| **Access Specifier** | Controls visibility | `public:`, `private:` |

---

## ✅ Key Takeaways

1. **Class**: Blueprint defining structure and behavior
2. **Object**: Actual instance with memory
3. **Data Members**: Store object state
4. **Member Functions**: Define object behavior
5. **Access Specifiers**: Control visibility (public, private, protected)
6. **`this` Pointer**: Refers to current object
7. **Const Correctness**: Mark methods that don't modify object
8. **Initialization List**: Preferred way to initialize members

---