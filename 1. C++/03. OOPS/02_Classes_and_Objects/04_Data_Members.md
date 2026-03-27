# 02_Classes_and_Objects/04_Data_Members.md

# Data Members in C++ - Complete Guide

## 📖 Overview

Data members (also called member variables, attributes, or fields) are variables declared within a class that hold the state of an object. They define what data an object stores and can be of various types including primitive types, objects of other classes, pointers, references, and static members.

---

## 🎯 Types of Data Members

| Type | Storage | Lifetime | Access | Purpose |
|------|---------|----------|--------|---------|
| **Instance Variables** | Per object | Object lifetime | Via object | Store object-specific data |
| **Static Variables** | Class-wide | Program lifetime | Via class or object | Shared across all objects |
| **Const Members** | Per object | Object lifetime | Read-only | Constant values per object |
| **Reference Members** | Per object | Object lifetime | Must be initialized | Aliasing other variables |
| **Mutable Members** | Per object | Object lifetime | Can modify in const methods | Cache, logging, etc. |

---

## 1. **Instance Variables (Non-static Data Members)**

### Definition
Instance variables are unique to each object. Each object gets its own copy of these variables.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Student {
private:
    // Instance variables - each Student object has its own
    string name;
    int rollNumber;
    float marks;
    char grade;
    
public:
    Student(string n, int r, float m) {
        name = n;
        rollNumber = r;
        marks = m;
        
        // Calculate grade based on marks
        if (marks >= 90) grade = 'A';
        else if (marks >= 80) grade = 'B';
        else if (marks >= 70) grade = 'C';
        else if (marks >= 60) grade = 'D';
        else grade = 'F';
    }
    
    void display() {
        cout << "Name: " << name << endl;
        cout << "Roll No: " << rollNumber << endl;
        cout << "Marks: " << marks << endl;
        cout << "Grade: " << grade << endl;
    }
};

int main() {
    // Each object has its own copy of data members
    Student s1("Alice", 101, 95.5);
    Student s2("Bob", 102, 78.0);
    Student s3("Charlie", 103, 82.5);
    
    cout << "Student 1:" << endl;
    s1.display();
    
    cout << "\nStudent 2:" << endl;
    s2.display();
    
    cout << "\nStudent 3:" << endl;
    s3.display();
    
    return 0;
}
```

**Output:**
```
Student 1:
Name: Alice
Roll No: 101
Marks: 95.5
Grade: A

Student 2:
Name: Bob
Roll No: 102
Marks: 78
Grade: C

Student 3:
Name: Charlie
Roll No: 103
Marks: 82.5
Grade: B
```

---

## 2. **Static Data Members**

### Definition
Static data members belong to the class itself, not to individual objects. They are shared across all objects and exist even before any object is created.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Employee {
private:
    string name;
    int id;
    static int nextId;      // Static data member - shared by all objects
    
public:
    Employee(string n) : name(n) {
        id = ++nextId;       // Assign unique ID from shared counter
        cout << "Employee " << name << " created with ID: " << id << endl;
    }
    
    ~Employee() {
        cout << "Employee " << name << " (ID: " << id << ") destroyed" << endl;
    }
    
    void display() {
        cout << "ID: " << id << ", Name: " << name << endl;
    }
    
    static int getNextId() {
        return nextId;       // Static function can access static data
    }
};

// Definition and initialization of static member
int Employee::nextId = 1000;

int main() {
    cout << "Initial nextId: " << Employee::getNextId() << endl;
    
    Employee e1("Alice");
    Employee e2("Bob");
    Employee e3("Charlie");
    
    cout << "\nAfter creating employees, nextId: " << Employee::getNextId() << endl;
    
    cout << "\nEmployee details:" << endl;
    e1.display();
    e2.display();
    e3.display();
    
    return 0;
}
```

**Output:**
```
Initial nextId: 1000
Employee Alice created with ID: 1001
Employee Bob created with ID: 1002
Employee Charlie created with ID: 1003

After creating employees, nextId: 1004

Employee details:
ID: 1001, Name: Alice
ID: 1002, Name: Bob
ID: 1003, Name: Charlie
Employee Charlie (ID: 1003) destroyed
Employee Bob (ID: 1002) destroyed
Employee Alice (ID: 1001) destroyed
```

### Static Data Member Characteristics

```cpp
class Counter {
private:
    static int count;        // Declared in class
    
public:
    Counter() { count++; }
    ~Counter() { count--; }
    
    static int getCount() { return count; }
};

// Must be defined outside the class
int Counter::count = 0;      // Definition and initialization

int main() {
    cout << "Count: " << Counter::getCount() << endl;  // 0
    
    Counter c1, c2, c3;
    cout << "Count after 3 objects: " << Counter::getCount() << endl;  // 3
    
    {
        Counter c4, c5;
        cout << "Count inside block: " << Counter::getCount() << endl;  // 5
    }
    
    cout << "Count after block: " << Counter::getCount() << endl;  // 3
    
    return 0;
}
```

---

## 3. **Const Data Members**

### Definition
Const data members cannot be modified after initialization. They must be initialized using the constructor initialization list.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Book {
private:
    const string isbn;        // Const data member
    const int edition;        // Const data member
    string title;
    string author;
    
public:
    // Must use initialization list for const members
    Book(string i, int e, string t, string a) 
        : isbn(i), edition(e), title(t), author(a) {
        // isbn = i;      // Error! Can't assign to const in body
        // edition = e;   // Error! Can't assign to const in body
    }
    
    void display() const {
        cout << "ISBN: " << isbn << endl;
        cout << "Edition: " << edition << endl;
        cout << "Title: " << title << endl;
        cout << "Author: " << author << endl;
    }
    
    // Getter methods - const members can be read
    string getISBN() const { return isbn; }
    int getEdition() const { return edition; }
};

int main() {
    Book book("978-0-321-99278-9", 5, "C++ Primer", "Lippman");
    book.display();
    
    // Cannot modify const members
    // book.isbn = "123";    // Error! isbn is const
    // book.edition = 6;     // Error! edition is const
    
    return 0;
}
```

---

## 4. **Reference Data Members**

### Definition
Reference data members must be initialized when the object is created and cannot be reassigned. They are useful for aliasing external variables.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Config {
private:
    string& configFile;      // Reference data member
    int& port;               // Reference data member
    
public:
    // Must initialize references in initialization list
    Config(string& file, int& p) : configFile(file), port(p) {}
    
    void display() {
        cout << "Config file: " << configFile << endl;
        cout << "Port: " << port << endl;
    }
    
    void updateConfig(string& newFile) {
        // configFile = newFile;  // This changes the referenced variable, not the reference itself
    }
};

class Wrapper {
private:
    int& ref;                // Reference member
    
public:
    Wrapper(int& r) : ref(r) {}
    
    int getValue() const { return ref; }
    void setValue(int val) { ref = val; }  // Modifies referenced variable
};

int main() {
    string filename = "config.ini";
    int serverPort = 8080;
    
    Config config(filename, serverPort);
    config.display();
    
    // Change the original variables
    filename = "production.ini";
    serverPort = 9090;
    
    cout << "\nAfter changing original variables:" << endl;
    config.display();  // References reflect the changes
    
    // Reference members
    int value = 42;
    Wrapper wrapper(value);
    cout << "\nWrapper value: " << wrapper.getValue() << endl;
    
    wrapper.setValue(100);
    cout << "After wrapper.setValue: " << value << endl;  // Original variable changed
    
    return 0;
}
```

**Output:**
```
Config file: config.ini
Port: 8080

After changing original variables:
Config file: production.ini
Port: 9090

Wrapper value: 42
After wrapper.setValue: 100
```

---

## 5. **Mutable Data Members**

### Definition
`mutable` data members can be modified even in const member functions. Useful for caching, logging, or reference counting.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Logger {
private:
    string name;
    mutable int accessCount;    // Can be modified in const methods
    mutable time_t lastAccess;  // Can be modified in const methods
    
public:
    Logger(string n) : name(n), accessCount(0), lastAccess(0) {}
    
    // Const method - but can modify mutable members
    void log(const string& message) const {
        accessCount++;           // ✓ Allowed - mutable
        lastAccess = time(nullptr); // ✓ Allowed - mutable
        
        cout << "[" << name << "] " << message << endl;
        cout << "  (Access #" << accessCount << ")" << endl;
    }
    
    int getAccessCount() const {
        return accessCount;      // Reading mutable is fine
    }
    
    time_t getLastAccess() const {
        return lastAccess;
    }
};

class Cache {
private:
    mutable bool dirty;          // Mutable for caching
    int cachedValue;
    int originalValue;
    
public:
    Cache(int val) : originalValue(val), cachedValue(val), dirty(false) {}
    
    int getValue() const {
        if (dirty) {
            // Recalculate cache (even though method is const)
            cachedValue = originalValue * 2;
            dirty = false;
        }
        return cachedValue;
    }
    
    void setValue(int val) {
        originalValue = val;
        dirty = true;            // Mark cache as dirty
    }
};

int main() {
    Logger logger("System");
    
    logger.log("Starting up");
    logger.log("Processing data");
    logger.log("Shutting down");
    
    cout << "Total accesses: " << logger.getAccessCount() << endl;
    
    // Cache example
    Cache cache(10);
    cout << "Cached value: " << cache.getValue() << endl;  // 20
    cache.setValue(20);
    cout << "Cached value after update: " << cache.getValue() << endl;  // 40
    
    return 0;
}
```

---

## 6. **Pointer Data Members**

### Definition
Pointer data members store addresses of other objects. They enable dynamic memory allocation and polymorphism.

```cpp
#include <iostream>
#include <cstring>
using namespace std;

class String {
private:
    char* data;          // Pointer to dynamically allocated array
    size_t length;
    
public:
    // Constructor
    String(const char* str) {
        length = strlen(str);
        data = new char[length + 1];
        strcpy(data, str);
        cout << "Created: " << data << endl;
    }
    
    // Copy constructor (deep copy)
    String(const String& other) {
        length = other.length;
        data = new char[length + 1];
        strcpy(data, other.data);
        cout << "Copied: " << data << endl;
    }
    
    // Destructor
    ~String() {
        cout << "Destroying: " << data << endl;
        delete[] data;
    }
    
    void display() const {
        cout << "String: " << data << " (length: " << length << ")" << endl;
    }
    
    void toUpper() {
        for (size_t i = 0; i < length; i++) {
            data[i] = toupper(data[i]);
        }
    }
};

class LinkedList {
private:
    struct Node {
        int data;
        Node* next;
        
        Node(int val) : data(val), next(nullptr) {}
    };
    
    Node* head;          // Pointer to first node
    
public:
    LinkedList() : head(nullptr) {}
    
    ~LinkedList() {
        Node* current = head;
        while (current) {
            Node* next = current->next;
            delete current;
            current = next;
        }
    }
    
    void insert(int value) {
        Node* newNode = new Node(value);
        newNode->next = head;
        head = newNode;
    }
    
    void display() {
        Node* current = head;
        while (current) {
            cout << current->data << " -> ";
            current = current->next;
        }
        cout << "NULL" << endl;
    }
};

int main() {
    // String class with pointer member
    String s1("Hello");
    String s2 = s1;  // Deep copy
    
    s1.display();
    s2.display();
    
    s1.toUpper();
    cout << "After s1.toUpper():" << endl;
    s1.display();
    s2.display();  // s2 unchanged (deep copy)
    
    // LinkedList with pointer members
    LinkedList list;
    list.insert(10);
    list.insert(20);
    list.insert(30);
    list.display();
    
    return 0;
}
```

---

## 7. **Initialization of Data Members**

### Different Initialization Methods

```cpp
#include <iostream>
#include <string>
using namespace std;

class Widget {
private:
    // 1. In-class initialization (C++11)
    int id = 0;                     // Default value
    string name = "Default";
    static int counter;             // Static - must be defined outside
    
    // 2. Const/Reference must use initialization list
    const int version;
    int& ref;
    
public:
    // 3. Constructor initialization list (preferred)
    Widget(int ver, int& r) : version(ver), ref(r) {
        // Member initialization happens before constructor body
        id = 100;                   // Assignment, not initialization
    }
    
    // 4. Delegating constructor (C++11)
    Widget() : Widget(1, version) {}  // Delegate to parameterized constructor
    
    void display() {
        cout << "ID: " << id << endl;
        cout << "Name: " << name << endl;
        cout << "Version: " << version << endl;
        cout << "Reference: " << ref << endl;
    }
};

int Widget::counter = 0;

class Complex {
private:
    double real;
    double imag;
    
public:
    // Member initializer list is more efficient
    Complex(double r = 0, double i = 0) : real(r), imag(i) {}
    
    // Order of initialization follows declaration order, not initializer list order
    Complex(int a, int b) : imag(b), real(a) {  // real initialized before imag
        // This works, but order is real then imag
    }
    
    void display() {
        cout << real << " + " << imag << "i" << endl;
    }
};

int main() {
    int value = 42;
    Widget w1(5, value);
    w1.display();
    
    Complex c1(3, 4);
    c1.display();
    
    return 0;
}
```

---

## 📊 Data Member Summary

| Type | Declaration | Initialization | Access | Use Case |
|------|-------------|----------------|--------|----------|
| **Instance** | `int x;` | Constructor | Per object | Object state |
| **Static** | `static int x;` | Outside class | Shared | Counters, constants |
| **Const** | `const int x;` | Initialization list | Read-only | Fixed per object |
| **Reference** | `int& x;` | Initialization list | Via reference | Aliasing |
| **Mutable** | `mutable int x;` | Constructor | Modifiable in const | Caching, logging |
| **Pointer** | `int* x;` | Constructor | Dynamic | Dynamic allocation |

---

## ✅ Best Practices

### 1. **Initialize All Data Members**
```cpp
class Good {
private:
    int a = 0;        // ✓ In-class initializer (C++11)
    int b;            // Must initialize in constructor
    
public:
    Good() : b(0) {}  // ✓ Initialize in initialization list
};

class Bad {
private:
    int a;            // ✗ Uninitialized
    int b;            // ✗ Uninitialized
    
public:
    Bad() {}          // ✗ Members have indeterminate values
};
```

### 2. **Use In-class Initializers for Defaults**
```cpp
class Employee {
private:
    string name = "Unknown";     // ✓ Default value
    int id = 0;                  // ✓ Default value
    double salary = 0.0;         // ✓ Default value
    
public:
    Employee(string n, int i, double s) 
        : name(n), id(i), salary(s) {}  // Override defaults
    
    Employee() = default;  // Use defaults
};
```

### 3. **Order Members by Size (Optimization)**
```cpp
class Optimized {
    double d;      // 8 bytes
    int i;         // 4 bytes
    char c;        // 1 byte
    // Padding: 3 bytes
};  // Total: 16 bytes

class LessOptimized {
    char c;        // 1 byte
    // Padding: 7 bytes
    double d;      // 8 bytes
    int i;         // 4 bytes
    // Padding: 4 bytes
};  // Total: 24 bytes
```

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Uninitialized members** | Indeterminate values | Initialize in class or constructor |
| **Static member not defined** | Linker error | Define static member in .cpp file |
| **Const/Reference not initialized** | Compiler error | Use initialization list |
| **Copying pointer members** | Shallow copy | Implement deep copy |
| **Order of initialization** | Dependency issues | Follow declaration order |

---

## ✅ Key Takeaways

1. **Instance variables**: Per-object storage, accessed via object
2. **Static members**: Class-wide storage, shared across objects
3. **Const members**: Must be initialized in initialization list
4. **Reference members**: Must be initialized, cannot be reassigned
5. **Mutable members**: Can be modified in const functions
6. **Pointer members**: Enable dynamic allocation and polymorphism
7. **Initialization**: Use initialization list over assignment in constructor body

---