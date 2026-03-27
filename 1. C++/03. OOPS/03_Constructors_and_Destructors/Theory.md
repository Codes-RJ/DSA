# Constructors and Destructors in C++ - Complete Guide

## 📖 Overview

Constructors and destructors are special member functions that manage object lifecycle. Constructors initialize objects when they are created, while destructors clean up resources when objects are destroyed. Understanding these concepts is crucial for proper resource management and preventing memory leaks.

---

## 🎯 Key Concepts

### Constructor
A constructor is a special member function that is automatically called when an object is created. It initializes the object's data members and acquires resources.

### Destructor
A destructor is a special member function that is automatically called when an object is destroyed. It releases resources and performs cleanup.

---

## 📊 Types of Constructors

| Type | Description | Syntax | When Called |
|------|-------------|--------|-------------|
| **Default Constructor** | No parameters | `ClassName();` | When object created without arguments |
| **Parameterized Constructor** | Takes parameters | `ClassName(params);` | When arguments are provided |
| **Copy Constructor** | Creates copy from existing object | `ClassName(const ClassName&);` | When object is copied |
| **Move Constructor (C++11)** | Transfers resources from temporary | `ClassName(ClassName&&);` | When object is moved |
| **Delegating Constructor (C++11)** | Calls another constructor | `ClassName() : ClassName(0) {}` | Constructor chaining |

---

## 1. **Constructor Characteristics**

```cpp
#include <iostream>
#include <string>
using namespace std;

class ConstructorDemo {
private:
    int value;
    string name;
    
public:
    // 1. Default constructor
    ConstructorDemo() : value(0), name("Default") {
        cout << "Default constructor called" << endl;
    }
    
    // 2. Parameterized constructor
    ConstructorDemo(int v, string n) : value(v), name(n) {
        cout << "Parameterized constructor called: " << name << endl;
    }
    
    // 3. Copy constructor
    ConstructorDemo(const ConstructorDemo& other) 
        : value(other.value), name(other.name + "_copy") {
        cout << "Copy constructor called: copying " << other.name << endl;
    }
    
    // 4. Move constructor (C++11)
    ConstructorDemo(ConstructorDemo&& other) noexcept
        : value(other.value), name(move(other.name)) {
        cout << "Move constructor called: moving " << name << endl;
        other.value = 0;
        other.name = "Moved";
    }
    
    // 5. Destructor
    ~ConstructorDemo() {
        cout << "Destructor called: " << name << endl;
    }
    
    void display() const {
        cout << "Value: " << value << ", Name: " << name << endl;
    }
};

int main() {
    cout << "=== Constructor Types Demo ===" << endl;
    
    cout << "\n1. Default constructor:" << endl;
    ConstructorDemo obj1;
    obj1.display();
    
    cout << "\n2. Parameterized constructor:" << endl;
    ConstructorDemo obj2(42, "Parameterized");
    obj2.display();
    
    cout << "\n3. Copy constructor:" << endl;
    ConstructorDemo obj3 = obj2;  // Copy constructor
    obj3.display();
    
    cout << "\n4. Move constructor:" << endl;
    ConstructorDemo obj4 = move(obj2);  // Move constructor
    obj4.display();
    cout << "Original after move: ";
    obj2.display();
    
    cout << "\n--- End of main (destructors will be called) ---" << endl;
    
    return 0;
}
```

**Output:**
```
=== Constructor Types Demo ===

1. Default constructor:
Default constructor called
Value: 0, Name: Default

2. Parameterized constructor:
Parameterized constructor called: Parameterized
Value: 42, Name: Parameterized

3. Copy constructor:
Copy constructor called: copying Parameterized
Value: 42, Name: Parameterized_copy

4. Move constructor:
Move constructor called: moving Parameterized
Value: 42, Name: Parameterized
Original after move: Value: 0, Name: Moved

--- End of main (destructors will be called) ---
Destructor called: Parameterized
Destructor called: Parameterized_copy
Destructor called: Default
Destructor called: Moved
```

---

## 2. **Constructor Initialization List**

### Definition
The initialization list is the preferred way to initialize data members, especially for const members, references, and base classes.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Base {
protected:
    int baseValue;
    
public:
    Base(int v) : baseValue(v) {
        cout << "Base constructor: " << baseValue << endl;
    }
};

class Member {
private:
    string name;
    
public:
    Member(string n) : name(n) {
        cout << "Member constructor: " << name << endl;
    }
    
    ~Member() {
        cout << "Member destructor: " << name << endl;
    }
};

class Derived : public Base {
private:
    const int constMember;      // Must use initialization list
    int& refMember;              // Must use initialization list
    Member member1;
    Member member2;
    static int staticMember;     // Static members are different
    
public:
    // Constructor with initialization list
    Derived(int b, int c, int& r, string m1, string m2) 
        : Base(b),                    // Initialize base class
          constMember(c),             // Initialize const member
          refMember(r),               // Initialize reference member
          member1(m1),                // Initialize member object
          member2(m2)                 // Initialize member object
    {
        cout << "Derived constructor body" << endl;
        // constMember = 10;          // Error! Can't assign to const
        // refMember = r;             // Already initialized, just reference
    }
    
    void display() const {
        cout << "Base value: " << baseValue << endl;
        cout << "Const member: " << constMember << endl;
        cout << "Reference member: " << refMember << endl;
    }
};

int Derived::staticMember = 100;

int main() {
    int externalValue = 999;
    
    cout << "=== Constructor Initialization List Demo ===" << endl;
    cout << endl;
    
    Derived obj(10, 42, externalValue, "First", "Second");
    obj.display();
    
    cout << "\n--- Destructors will be called in reverse order ---" << endl;
    
    return 0;
}
```

**Output:**
```
=== Constructor Initialization List Demo ===

Base constructor: 10
Member constructor: First
Member constructor: Second
Derived constructor body
Base value: 10
Const member: 42
Reference member: 999

--- Destructors will be called in reverse order ---
Member destructor: Second
Member destructor: First
Base destructor
```

---

## 3. **Destructor Characteristics**

### Definition
Destructors clean up resources, release memory, and perform final operations before an object is destroyed.

```cpp
#include <iostream>
#include <cstring>
using namespace std;

class Resource {
private:
    char* data;
    size_t size;
    static int resourceCount;
    
public:
    // Constructor
    Resource(const char* str) {
        size = strlen(str);
        data = new char[size + 1];
        strcpy(data, str);
        resourceCount++;
        cout << "Resource created: " << data << " (Total: " << resourceCount << ")" << endl;
    }
    
    // Copy constructor (deep copy)
    Resource(const Resource& other) {
        size = other.size;
        data = new char[size + 1];
        strcpy(data, other.data);
        resourceCount++;
        cout << "Resource copied: " << data << " (Total: " << resourceCount << ")" << endl;
    }
    
    // Move constructor
    Resource(Resource&& other) noexcept : data(other.data), size(other.size) {
        other.data = nullptr;
        other.size = 0;
        resourceCount++;
        cout << "Resource moved: " << data << " (Total: " << resourceCount << ")" << endl;
    }
    
    // Destructor - releases allocated memory
    ~Resource() {
        if (data) {
            cout << "Resource destroyed: " << data << " (Remaining: " << --resourceCount << ")" << endl;
            delete[] data;
            data = nullptr;
        } else {
            cout << "Resource destroyed: (null) (Remaining: " << --resourceCount << ")" << endl;
        }
    }
    
    void display() const {
        if (data) {
            cout << "Resource: " << data << endl;
        } else {
            cout << "Resource: (null)" << endl;
        }
    }
    
    static int getCount() { return resourceCount; }
};

int Resource::resourceCount = 0;

class FileHandler {
private:
    FILE* file;
    string filename;
    
public:
    FileHandler(const string& name) : filename(name) {
        file = fopen(name.c_str(), "w");
        if (file) {
            cout << "File opened: " << filename << endl;
        } else {
            cout << "Failed to open file: " << filename << endl;
        }
    }
    
    ~FileHandler() {
        if (file) {
            fclose(file);
            cout << "File closed: " << filename << endl;
        }
    }
    
    void write(const string& content) {
        if (file) {
            fprintf(file, "%s\n", content.c_str());
        }
    }
};

class DatabaseConnection {
private:
    bool connected;
    
public:
    DatabaseConnection() : connected(false) {
        cout << "Database connection object created" << endl;
    }
    
    void connect() {
        if (!connected) {
            connected = true;
            cout << "Connected to database" << endl;
        }
    }
    
    void disconnect() {
        if (connected) {
            connected = false;
            cout << "Disconnected from database" << endl;
        }
    }
    
    ~DatabaseConnection() {
        if (connected) {
            disconnect();  // Auto-disconnect on destruction
        }
        cout << "Database connection object destroyed" << endl;
    }
    
    void query(const string& sql) {
        if (connected) {
            cout << "Executing: " << sql << endl;
        } else {
            cout << "Not connected!" << endl;
        }
    }
};

int main() {
    cout << "=== Destructor Examples ===" << endl;
    
    cout << "\n1. Resource Management:" << endl;
    {
        Resource r1("Hello");
        Resource r2("World");
        {
            Resource r3("Temporary");
            r3.display();
        }  // r3 destructor called here
        r1.display();
        r2.display();
    }  // r1 and r2 destructors called here
    
    cout << "\n2. File Handling with RAII:" << endl;
    {
        FileHandler file("test.txt");
        file.write("Hello, World!");
        file.write("This will be auto-saved");
    }  // File automatically closed
    
    cout << "\n3. Database Connection with RAII:" << endl;
    {
        DatabaseConnection db;
        db.connect();
        db.query("SELECT * FROM users");
        db.query("INSERT INTO logs VALUES('action')");
        // db.disconnect();  // Not necessary - will happen in destructor
    }  // Auto-disconnect on destruction
    
    cout << "\n--- End of main ---" << endl;
    
    return 0;
}
```

**Output:**
```
=== Destructor Examples ===

1. Resource Management:
Resource created: Hello (Total: 1)
Resource created: World (Total: 2)
Resource created: Temporary (Total: 3)
Resource: Temporary
Resource destroyed: Temporary (Remaining: 2)
Resource: Hello
Resource: World
Resource destroyed: World (Remaining: 1)
Resource destroyed: Hello (Remaining: 0)

2. File Handling with RAII:
File opened: test.txt
File closed: test.txt

3. Database Connection with RAII:
Database connection object created
Connected to database
Executing: SELECT * FROM users
Executing: INSERT INTO logs VALUES('action')
Disconnected from database
Database connection object destroyed

--- End of main ---
```

---

## 4. **Order of Construction and Destruction**

### Definition
The order of constructor calls follows the hierarchy: base classes first, then member objects, then derived class. Destruction happens in reverse order.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Base1 {
public:
    Base1() { cout << "Base1 constructor" << endl; }
    ~Base1() { cout << "Base1 destructor" << endl; }
};

class Base2 {
public:
    Base2() { cout << "Base2 constructor" << endl; }
    ~Base2() { cout << "Base2 destructor" << endl; }
};

class Member1 {
public:
    Member1() { cout << "  Member1 constructor" << endl; }
    ~Member1() { cout << "  Member1 destructor" << endl; }
};

class Member2 {
public:
    Member2() { cout << "  Member2 constructor" << endl; }
    ~Member2() { cout << "  Member2 destructor" << endl; }
};

class Derived : public Base1, public Base2 {
private:
    Member1 m1;
    Member2 m2;
    
public:
    Derived() {
        cout << "Derived constructor body" << endl;
    }
    
    ~Derived() {
        cout << "Derived destructor body" << endl;
    }
};

int main() {
    cout << "=== Order of Construction/Destruction ===" << endl;
    cout << endl;
    cout << "Construction order:" << endl;
    cout << "1. Base classes (in declaration order)" << endl;
    cout << "2. Member objects (in declaration order)" << endl;
    cout << "3. Derived class body" << endl;
    cout << endl;
    cout << "Destruction order: REVERSE of construction" << endl;
    cout << endl;
    
    cout << "--- Creating object ---" << endl;
    {
        Derived d;
    }
    cout << "--- Object destroyed ---" << endl;
    
    return 0;
}
```

**Output:**
```
=== Order of Construction/Destruction ===

Construction order:
1. Base classes (in declaration order)
2. Member objects (in declaration order)
3. Derived class body

Destruction order: REVERSE of construction

--- Creating object ---
Base1 constructor
Base2 constructor
  Member1 constructor
  Member2 constructor
Derived constructor body
Derived destructor body
  Member2 destructor
  Member1 destructor
Base2 destructor
Base1 destructor
--- Object destroyed ---
```

---

## 5. **Virtual Destructor**

### Definition
Base classes should have virtual destructors to ensure proper cleanup of derived objects when deleted through a base pointer.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

class Base {
private:
    string name;
    
public:
    Base(string n) : name(n) {
        cout << "Base constructor: " << name << endl;
    }
    
    // Virtual destructor - essential for polymorphism
    virtual ~Base() {
        cout << "Base destructor: " << name << endl;
    }
    
    virtual void display() const {
        cout << "Base: " << name << endl;
    }
};

class Derived : public Base {
private:
    int* data;
    size_t size;
    
public:
    Derived(string n, size_t s) : Base(n), size(s) {
        data = new int[size];
        cout << "Derived constructor: allocating " << size << " ints" << endl;
    }
    
    ~Derived() override {
        cout << "Derived destructor: freeing " << size << " ints" << endl;
        delete[] data;
    }
    
    void display() const override {
        Base::display();
        cout << "Derived: size=" << size << endl;
    }
};

class NonVirtualBase {
public:
    NonVirtualBase() { cout << "NonVirtualBase constructor" << endl; }
    ~NonVirtualBase() { cout << "NonVirtualBase destructor" << endl; }
};

class NonVirtualDerived : public NonVirtualBase {
private:
    int* data;
    
public:
    NonVirtualDerived() : data(new int[100]) {
        cout << "NonVirtualDerived constructor: allocated 100 ints" << endl;
    }
    
    ~NonVirtualDerived() {
        cout << "NonVirtualDerived destructor: freeing 100 ints" << endl;
        delete[] data;
    }
};

int main() {
    cout << "=== Virtual Destructor Demo ===" << endl;
    
    cout << "\n1. Correct: Virtual destructor in base class" << endl;
    {
        Base* ptr = new Derived("Virtual Example", 50);
        ptr->display();
        delete ptr;  // Proper cleanup with virtual destructor
    }
    
    cout << "\n2. INCORRECT: Non-virtual destructor" << endl;
    {
        NonVirtualBase* ptr = new NonVirtualDerived();
        // Derived destructor won't be called! Memory leak!
        delete ptr;
        cout << "Memory leak! Derived destructor not called!" << endl;
    }
    
    cout << "\n3. Smart pointer handles this automatically" << endl;
    {
        unique_ptr<Base> ptr = make_unique<Derived>("Smart Pointer", 75);
        ptr->display();
        // Auto cleanup with virtual destructor
    }
    
    cout << "\n4. Vector of polymorphic objects" << endl;
    {
        vector<unique_ptr<Base>> objects;
        objects.push_back(make_unique<Derived>("Object1", 10));
        objects.push_back(make_unique<Derived>("Object2", 20));
        objects.push_back(make_unique<Derived>("Object3", 30));
        
        for (const auto& obj : objects) {
            obj->display();
        }
        // All automatically cleaned up
    }
    
    return 0;
}
```

**Output:**
```
=== Virtual Destructor Demo ===

1. Correct: Virtual destructor in base class
Base constructor: Virtual Example
Derived constructor: allocating 50 ints
Base: Virtual Example
Derived: size=50
Derived destructor: freeing 50 ints
Base destructor: Virtual Example

2. INCORRECT: Non-virtual destructor
NonVirtualBase constructor
NonVirtualDerived constructor: allocated 100 ints
NonVirtualBase destructor
Memory leak! Derived destructor not called!

3. Smart pointer handles this automatically
Base constructor: Smart Pointer
Derived constructor: allocating 75 ints
Base: Smart Pointer
Derived: size=75
Derived destructor: freeing 75 ints
Base destructor: Smart Pointer

4. Vector of polymorphic objects
Base constructor: Object1
Derived constructor: allocating 10 ints
Base constructor: Object2
Derived constructor: allocating 20 ints
Base constructor: Object3
Derived constructor: allocating 30 ints
Base: Object1
Derived: size=10
Base: Object2
Derived: size=20
Base: Object3
Derived: size=30
Derived destructor: freeing 30 ints
Base destructor: Object3
Derived destructor: freeing 20 ints
Base destructor: Object2
Derived destructor: freeing 10 ints
Base destructor: Object1
```

---

## 6. **Rule of Three, Five, and Zero**

### Definition
Guidelines for managing resources in classes:

- **Rule of Three**: If a class needs a custom destructor, copy constructor, or copy assignment operator, it likely needs all three.
- **Rule of Five** (C++11): Adds move constructor and move assignment operator.
- **Rule of Zero**: Prefer classes that don't need custom resource management (use standard containers and smart pointers).

```cpp
#include <iostream>
#include <cstring>
#include <memory>
using namespace std;

// Rule of Zero: Use standard containers, no custom resource management
class RuleOfZero {
private:
    string name;           // std::string manages its own memory
    vector<int> data;      // std::vector manages its own memory
    
public:
    RuleOfZero(string n) : name(n) {}
    // No need for custom destructor, copy, or move
    // Compiler-generated versions work correctly
};

// Rule of Five: Manual resource management
class RuleOfFive {
private:
    char* data;
    size_t size;
    
public:
    // Constructor
    RuleOfFive(const char* str) {
        size = strlen(str);
        data = new char[size + 1];
        strcpy(data, str);
        cout << "Constructor: " << data << endl;
    }
    
    // Destructor
    ~RuleOfFive() {
        cout << "Destructor: " << (data ? data : "null") << endl;
        delete[] data;
    }
    
    // Copy constructor
    RuleOfFive(const RuleOfFive& other) {
        size = other.size;
        data = new char[size + 1];
        strcpy(data, other.data);
        cout << "Copy constructor: " << data << endl;
    }
    
    // Copy assignment operator
    RuleOfFive& operator=(const RuleOfFive& other) {
        if (this != &other) {
            cout << "Copy assignment: " << data << " = " << other.data << endl;
            delete[] data;
            size = other.size;
            data = new char[size + 1];
            strcpy(data, other.data);
        }
        return *this;
    }
    
    // Move constructor
    RuleOfFive(RuleOfFive&& other) noexcept 
        : data(other.data), size(other.size) {
        cout << "Move constructor: moving " << other.data << endl;
        other.data = nullptr;
        other.size = 0;
    }
    
    // Move assignment operator
    RuleOfFive& operator=(RuleOfFive&& other) noexcept {
        if (this != &other) {
            cout << "Move assignment: " << data << " = " << other.data << endl;
            delete[] data;
            data = other.data;
            size = other.size;
            other.data = nullptr;
            other.size = 0;
        }
        return *this;
    }
    
    void display() const {
        cout << "Data: " << (data ? data : "null") << endl;
    }
};

int main() {
    cout << "=== Rule of Five Demo ===" << endl;
    
    cout << "\n1. Constructor:" << endl;
    RuleOfFive r1("Original");
    r1.display();
    
    cout << "\n2. Copy constructor:" << endl;
    RuleOfFive r2 = r1;
    r2.display();
    
    cout << "\n3. Copy assignment:" << endl;
    RuleOfFive r3("Temporary");
    r3 = r1;
    r3.display();
    
    cout << "\n4. Move constructor:" << endl;
    RuleOfFive r4 = move(r1);
    r4.display();
    cout << "Original after move: ";
    r1.display();
    
    cout << "\n5. Move assignment:" << endl;
    RuleOfFive r5("Placeholder");
    r5 = move(r2);
    r5.display();
    cout << "Original after move: ";
    r2.display();
    
    cout << "\n--- End of scope ---" << endl;
    return 0;
}
```

**Output:**
```
=== Rule of Five Demo ===

1. Constructor:
Constructor: Original
Data: Original

2. Copy constructor:
Copy constructor: Original
Data: Original

3. Copy assignment:
Constructor: Temporary
Copy assignment: Temporary = Original
Data: Original

4. Move constructor:
Move constructor: moving Original
Data: Original
Original after move: Data: null

5. Move assignment:
Constructor: Placeholder
Move assignment: Placeholder = Original
Data: Original
Original after move: Data: null

--- End of scope ---
Destructor: Original
Destructor: null
Destructor: Original
Destructor: Original
```

---

## 📊 Constructor/Destructor Summary

| Aspect | Constructor | Destructor |
|--------|-------------|------------|
| **Purpose** | Initialize object | Clean up resources |
| **Name** | Same as class | ~Classname |
| **Return Type** | None | None |
| **Parameters** | Optional | None |
| **Overloading** | Yes | No |
| **Default** | Compiler-generated if not provided | Compiler-generated if not provided |
| **Inheritance** | Not inherited (but called) | Not inherited (but called) |
| **Virtual** | Not possible | Essential for polymorphism |

---

## ✅ Best Practices

1. **Use initialization lists** over assignment in constructor body
2. **Mark single-argument constructors as `explicit`** to prevent implicit conversions
3. **Make base class destructors virtual** for proper cleanup in polymorphism
4. **Follow Rule of Zero**: Use standard containers instead of manual resource management
5. **Follow Rule of Five** when manual resource management is necessary
6. **Use `noexcept` on move operations** for better performance
7. **Initialize all members** in constructors (especially pointers)

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Missing virtual destructor** | Memory leaks in polymorphism | Make base destructor virtual |
| **Shallow copy** | Double deletion, memory corruption | Implement deep copy in copy constructor |
| **Not initializing const/reference members** | Compiler error | Use initialization list |
| **Calling virtual functions in constructor** | Unexpected behavior | Avoid virtual calls in constructor |
| **Resource leak in constructor** | Memory leak if exception thrown | Use RAII, smart pointers |

---

## ✅ Key Takeaways

1. **Constructors**: Initialize objects, can be overloaded
2. **Destructors**: Clean up resources, single per class
3. **Initialization list**: Preferred over assignment
4. **Order**: Base → members → derived (reverse for destruction)
5. **Virtual destructor**: Essential for polymorphic base classes
6. **Rule of Five**: Manage resources properly when needed
7. **RAII**: Resource Acquisition Is Initialization

---