# Object Creation in C++ - Complete Guide

## 📖 Overview

Object creation is the process of instantiating a class to create an object in memory. In C++, objects can be created in different ways: on the stack (automatic storage), on the heap (dynamic storage), or as global/static objects. Understanding object creation is crucial for proper memory management and program design.

---

## 🎯 Types of Object Creation

### 1. **Stack Allocation (Automatic Storage)**

Objects created on the stack have automatic lifetime - they are automatically destroyed when they go out of scope.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Student {
private:
    string name;
    int age;
    
public:
    Student(string n, int a) : name(n), age(a) {
        cout << "Constructor called for " << name << endl;
    }
    
    ~Student() {
        cout << "Destructor called for " << name << endl;
    }
    
    void display() {
        cout << name << " is " << age << " years old" << endl;
    }
};

int main() {
    cout << "Creating objects on stack..." << endl;
    
    // Direct object creation (stack)
    Student s1("Alice", 20);
    Student s2("Bob", 22);
    Student s3("Charlie", 21);
    
    s1.display();
    s2.display();
    s3.display();
    
    cout << "Exiting main - objects will be destroyed..." << endl;
    return 0;
}
```

**Output:**
```
Creating objects on stack...
Constructor called for Alice
Constructor called for Bob
Constructor called for Charlie
Alice is 20 years old
Bob is 22 years old
Charlie is 21 years old
Exiting main - objects will be destroyed...
Destructor called for Charlie
Destructor called for Bob
Destructor called for Alice
```

---

### 2. **Heap Allocation (Dynamic Storage)**

Objects created on the heap must be manually allocated with `new` and deallocated with `delete`. They persist until explicitly destroyed.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Product {
private:
    string name;
    double price;
    
public:
    Product(string n, double p) : name(n), price(p) {
        cout << "Product created: " << name << endl;
    }
    
    ~Product() {
        cout << "Product destroyed: " << name << endl;
    }
    
    void display() {
        cout << name << " - $" << price << endl;
    }
};

int main() {
    cout << "Creating objects on heap..." << endl;
    
    // Single object allocation
    Product* p1 = new Product("Laptop", 999.99);
    Product* p2 = new Product("Mouse", 29.99);
    Product* p3 = new Product("Keyboard", 79.99);
    
    p1->display();
    p2->display();
    p3->display();
    
    // Must manually delete heap objects
    delete p1;
    delete p2;
    delete p3;
    
    cout << "Objects deleted manually" << endl;
    
    return 0;
}
```

**Output:**
```
Creating objects on heap...
Product created: Laptop
Product created: Mouse
Product created: Keyboard
Laptop - $999.99
Mouse - $29.99
Keyboard - $79.99
Product destroyed: Laptop
Product destroyed: Mouse
Product destroyed: Keyboard
Objects deleted manually
```

---

## 📝 Different Object Creation Methods

### 3. **Array of Objects**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Employee {
private:
    string name;
    int id;
    
public:
    Employee() : name("Unknown"), id(0) {
        cout << "Default constructor" << endl;
    }
    
    Employee(string n, int i) : name(n), id(i) {
        cout << "Parameterized constructor: " << name << endl;
    }
    
    ~Employee() {
        cout << "Destructor: " << name << endl;
    }
    
    void display() {
        cout << "ID: " << id << ", Name: " << name << endl;
    }
};

int main() {
    // Array of objects on stack
    cout << "Stack array of objects:" << endl;
    Employee empStack[3] = {
        Employee("Alice", 101),
        Employee("Bob", 102),
        Employee("Charlie", 103)
    };
    
    for (int i = 0; i < 3; i++) {
        empStack[i].display();
    }
    
    cout << "\nHeap array of objects:" << endl;
    // Array of objects on heap
    Employee* empHeap = new Employee[3];
    
    empHeap[0] = Employee("David", 201);
    empHeap[1] = Employee("Eve", 202);
    empHeap[2] = Employee("Frank", 203);
    
    for (int i = 0; i < 3; i++) {
        empHeap[i].display();
    }
    
    // Must delete array on heap
    delete[] empHeap;
    
    return 0;
}
```

---

### 4. **Dynamic Object with Different Initialization Methods**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Circle {
private:
    double radius;
    static int count;
    
public:
    // Default constructor
    Circle() : radius(0) {
        count++;
        cout << "Default Circle created (count: " << count << ")" << endl;
    }
    
    // Parameterized constructor
    Circle(double r) : radius(r) {
        count++;
        cout << "Circle created with radius " << radius << " (count: " << count << ")" << endl;
    }
    
    // Copy constructor
    Circle(const Circle& other) : radius(other.radius) {
        count++;
        cout << "Circle copied (radius " << radius << ", count: " << count << ")" << endl;
    }
    
    // Destructor
    ~Circle() {
        cout << "Circle destroyed (radius " << radius << ", count: " << count << ")" << endl;
        count--;
    }
    
    double area() const {
        return 3.14159 * radius * radius;
    }
    
    static int getCount() { return count; }
};

int Circle::count = 0;

int main() {
    cout << "=== Different Object Creation Methods ===\n" << endl;
    
    // Method 1: Stack allocation
    cout << "1. Stack allocation:" << endl;
    Circle c1(5.0);
    cout << "Area: " << c1.area() << endl;
    cout << "Total circles: " << Circle::getCount() << endl;
    
    // Method 2: Heap allocation
    cout << "\n2. Heap allocation:" << endl;
    Circle* c2 = new Circle(10.0);
    cout << "Area: " << c2->area() << endl;
    delete c2;
    
    // Method 3: Array of objects
    cout << "\n3. Array of objects:" << endl;
    Circle circles[2] = {Circle(2.0), Circle(3.0)};
    
    // Method 4: Copy constructor
    cout << "\n4. Copy constructor:" << endl;
    Circle c3 = c1;
    cout << "Area of copy: " << c3.area() << endl;
    
    // Method 5: Dynamic array
    cout << "\n5. Dynamic array:" << endl;
    Circle* circleArray = new Circle[3];
    delete[] circleArray;
    
    cout << "\nFinal circle count: " << Circle::getCount() << endl;
    
    return 0;
}
```

---

## 🔧 The `new` and `delete` Operators

### `new` Operator Variations

```cpp
#include <iostream>
using namespace std;

class Widget {
private:
    int id;
    string name;
    
public:
    Widget() : id(0), name("Default") {
        cout << "Default constructor" << endl;
    }
    
    Widget(int i, string n) : id(i), name(n) {
        cout << "Parameterized constructor: " << name << endl;
    }
    
    ~Widget() {
        cout << "Destructor: " << name << endl;
    }
    
    void display() {
        cout << "Widget " << id << ": " << name << endl;
    }
    
    // Placement new operator
    static void* operator new(size_t size, void* ptr) {
        cout << "Placement new called" << endl;
        return ptr;
    }
};

int main() {
    // 1. Basic new
    Widget* w1 = new Widget(1, "Basic");
    w1->display();
    delete w1;
    
    // 2. new with no initialization
    Widget* w2 = new Widget;  // Default constructor
    w2->display();
    delete w2;
    
    // 3. new array
    Widget* wArray = new Widget[3];
    delete[] wArray;
    
    // 4. Placement new (construct object in pre-allocated memory)
    char* buffer = new char[sizeof(Widget)];
    Widget* w3 = new(buffer) Widget(2, "Placement");
    w3->display();
    w3->~Widget();  // Must call destructor manually
    delete[] buffer;
    
    // 5. Nothrow new (returns nullptr on failure)
    Widget* w4 = new(nothrow) Widget(3, "Nothrow");
    if (w4) {
        w4->display();
        delete w4;
    }
    
    return 0;
}
```

---

## 🏗️ Object Lifecycle

### Complete Object Lifecycle Example

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Resource {
private:
    string name;
    int* data;
    size_t size;
    
public:
    // Constructor
    Resource(string n, size_t s) : name(n), size(s) {
        cout << "Constructor: " << name << " allocating " << size << " bytes" << endl;
        data = new int[size];
        for (size_t i = 0; i < size; i++) {
            data[i] = i;
        }
    }
    
    // Copy constructor (deep copy)
    Resource(const Resource& other) : name(other.name + "_copy"), size(other.size) {
        cout << "Copy constructor: copying " << other.name << endl;
        data = new int[size];
        for (size_t i = 0; i < size; i++) {
            data[i] = other.data[i];
        }
    }
    
    // Move constructor (C++11)
    Resource(Resource&& other) noexcept 
        : name(move(other.name)), data(other.data), size(other.size) {
        cout << "Move constructor: moving " << name << endl;
        other.data = nullptr;
        other.size = 0;
    }
    
    // Destructor
    ~Resource() {
        cout << "Destructor: " << name << " freeing " << size << " bytes" << endl;
        delete[] data;
        data = nullptr;
    }
    
    // Copy assignment
    Resource& operator=(const Resource& other) {
        cout << "Copy assignment: " << name << " = " << other.name << endl;
        if (this != &other) {
            delete[] data;
            size = other.size;
            data = new int[size];
            for (size_t i = 0; i < size; i++) {
                data[i] = other.data[i];
            }
            name = other.name + "_assigned";
        }
        return *this;
    }
    
    // Move assignment
    Resource& operator=(Resource&& other) noexcept {
        cout << "Move assignment: " << name << " = " << other.name << endl;
        if (this != &other) {
            delete[] data;
            data = other.data;
            size = other.size;
            name = move(other.name);
            other.data = nullptr;
            other.size = 0;
        }
        return *this;
    }
    
    void display() {
        cout << "Resource: " << name << " (size: " << size << ")" << endl;
    }
};

Resource createResource() {
    Resource temp("Temporary", 100);
    return temp;  // Move or copy elision
}

int main() {
    cout << "=== Object Lifecycle Demonstration ===\n" << endl;
    
    // 1. Stack object
    cout << "1. Creating stack object:" << endl;
    Resource r1("StackResource", 10);
    r1.display();
    
    // 2. Heap object
    cout << "\n2. Creating heap object:" << endl;
    Resource* r2 = new Resource("HeapResource", 20);
    r2->display();
    
    // 3. Copy constructor
    cout << "\n3. Copy constructor:" << endl;
    Resource r3 = r1;  // Copy constructor
    r3.display();
    
    // 4. Copy assignment
    cout << "\n4. Copy assignment:" << endl;
    Resource r4("Empty", 0);
    r4 = r1;  // Copy assignment
    r4.display();
    
    // 5. Move constructor (C++11)
    cout << "\n5. Move constructor:" << endl;
    Resource r5 = move(r1);  // Move constructor
    r5.display();
    cout << "Original after move: ";
    r1.display();  // Now empty
    
    // 6. Function returning object
    cout << "\n6. Function returning object:" << endl;
    Resource r6 = createResource();  // Move or copy elision
    r6.display();
    
    // 7. Vector of objects
    cout << "\n7. Vector of objects:" << endl;
    vector<Resource> resources;
    resources.push_back(Resource("Vector1", 5));
    resources.push_back(Resource("Vector2", 6));
    resources.emplace_back("Vector3", 7);
    
    // 8. Cleanup
    cout << "\n8. Cleaning up:" << endl;
    delete r2;  // Manual cleanup
    cout << "Exiting scope - stack objects will be destroyed..." << endl;
    
    return 0;
}
```

---

## 📊 Comparison of Object Creation Methods

| Method | Syntax | Storage | Lifetime | When to Use |
|--------|--------|---------|----------|-------------|
| **Stack** | `ClassName obj;` | Stack | Automatic (scope) | Small objects, short lifetime |
| **Heap** | `new ClassName()` | Heap | Manual (until delete) | Large objects, dynamic lifetime |
| **Array (Stack)** | `ClassName arr[10];` | Stack | Automatic | Fixed-size collections |
| **Array (Heap)** | `new ClassName[10]` | Heap | Manual | Dynamic-size collections |
| **Global** | `ClassName obj;` (outside main) | Data segment | Program lifetime | Shared resources |
| **Static** | `static ClassName obj;` | Data segment | Program lifetime | Persistent state |

---

## 🎯 Object Creation Guidelines

### When to Use Stack Allocation
```cpp
void function() {
    // ✓ Good: Small objects with short lifetime
    Point p(10, 20);
    string name = "Alice";
    vector<int> numbers = {1, 2, 3};
    
    // ✓ Good: When object size is known at compile time
    int arr[100];
    
    // ✓ Good: When scope is limited
    // Object automatically destroyed when function ends
}
```

### When to Use Heap Allocation
```cpp
void function() {
    // ✓ Good: Large objects
    BigData* data = new BigData(1000000);
    
    // ✓ Good: When object needs to outlive the function
    Widget* createWidget() {
        return new Widget();  // Returns pointer to persistent object
    }
    
    // ✓ Good: When size is unknown at compile time
    int* dynamicArray = new int[size];
    
    // ✓ Good: For polymorphic objects
    Shape* shape = new Circle(5.0);
    
    // Must remember to delete
    delete data;
    delete shape;
    delete[] dynamicArray;
}
```

---

## 🚀 Modern C++: Smart Pointers

```cpp
#include <memory>
#include <iostream>
using namespace std;

class ModernObject {
public:
    ModernObject(string name) {
        cout << "Created: " << name << endl;
    }
    
    ~ModernObject() {
        cout << "Destroyed" << endl;
    }
};

int main() {
    cout << "=== Modern C++ Object Creation ===\n" << endl;
    
    // unique_ptr - exclusive ownership
    cout << "1. unique_ptr:" << endl;
    unique_ptr<ModernObject> uptr = make_unique<ModernObject>("Unique");
    // Automatically destroyed when uptr goes out of scope
    
    // shared_ptr - shared ownership
    cout << "\n2. shared_ptr:" << endl;
    shared_ptr<ModernObject> sptr1 = make_shared<ModernObject>("Shared");
    {
        shared_ptr<ModernObject> sptr2 = sptr1;  // Shared ownership
        cout << "Reference count: " << sptr1.use_count() << endl;
    }
    cout << "Reference count: " << sptr1.use_count() << endl;
    
    // weak_ptr - non-owning observer
    cout << "\n3. weak_ptr:" << endl;
    weak_ptr<ModernObject> wptr = sptr1;
    if (auto spt = wptr.lock()) {
        cout << "Object still exists" << endl;
    }
    
    cout << "\nExiting..." << endl;
    return 0;
}
```

---

## 📚 Object Creation Best Practices

### 1. **Prefer Stack Allocation When Possible**
```cpp
// ✓ Good
string name = "Alice";
vector<int> numbers;

// ✗ Avoid when not necessary
string* name = new string("Alice");
vector<int>* numbers = new vector<int>();
```

### 2. **Use RAII (Resource Acquisition Is Initialization)**
```cpp
class FileHandler {
private:
    FILE* file;
    
public:
    FileHandler(const char* filename) {
        file = fopen(filename, "r");
        if (!file) throw runtime_error("Cannot open file");
    }
    
    ~FileHandler() {
        if (file) fclose(file);
    }
    
    // Prevent copying
    FileHandler(const FileHandler&) = delete;
    FileHandler& operator=(const FileHandler&) = delete;
};
```

### 3. **Initialize All Members**
```cpp
class Widget {
private:
    int a;      // Will be initialized in constructor
    int b;      // Will be initialized in constructor
    string c;   // Will be initialized in constructor
    
public:
    // ✓ Good: Use initialization list
    Widget(int x, int y, string z) : a(x), b(y), c(z) {}
    
    // ✗ Avoid: Assignment in body
    // Widget(int x, int y, string z) {
    //     a = x;  // Less efficient
    //     b = y;
    //     c = z;
    // }
};
```

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Memory Leak** | Forgetting to delete heap objects | Use smart pointers or RAII |
| **Double Delete** | Deleting same object twice | Set pointers to nullptr after delete |
| **Dangling Pointer** | Using object after deletion | Use smart pointers or clear references |
| **Stack Overflow** | Creating huge objects on stack | Use heap allocation for large objects |
| **Slicing** | Assigning derived to base object | Use pointers/references for polymorphism |

---

## ✅ Key Takeaways

1. **Stack objects**: Automatic lifetime, faster, preferred when possible
2. **Heap objects**: Manual lifetime, necessary for dynamic size and polymorphism
3. **`new`/`delete`**: Allocate/deallocate heap memory; must be paired
4. **`new[]`/`delete[]`**: For arrays of objects
5. **Smart pointers**: Modern C++ alternative for automatic memory management
6. **RAII**: Resource acquisition is initialization pattern
7. **Object lifecycle**: Constructor → use → destructor

---