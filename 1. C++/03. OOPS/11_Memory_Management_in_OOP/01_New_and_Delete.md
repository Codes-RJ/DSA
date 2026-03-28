# 11_Memory_Management_in_OOP/01_New_and_Delete.md

# new and delete Operators in C++ - Complete Guide

## 📖 Overview

The `new` and `delete` operators are fundamental to dynamic memory management in C++. They allocate and deallocate memory on the heap, providing flexibility for objects whose size or lifetime cannot be determined at compile time. Understanding these operators is essential for proper resource management.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **new** | Allocates memory and constructs objects |
| **delete** | Destroys objects and deallocates memory |
| **new[]** | Allocates array of objects |
| **delete[]** | Deallocates array of objects |
| **Placement new** | Constructs object in pre-allocated memory |
| **nothrow new** | Returns nullptr on failure instead of throwing |

---

## 1. **Basic new and delete**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Simple {
private:
    int value;
    string name;
    
public:
    Simple(int v, string n) : value(v), name(n) {
        cout << "Simple constructor: " << name << " (" << value << ")" << endl;
    }
    
    ~Simple() {
        cout << "Simple destructor: " << name << endl;
    }
    
    void display() const {
        cout << "Value: " << value << ", Name: " << name << endl;
    }
};

int main() {
    cout << "=== Basic new and delete ===" << endl;
    
    cout << "\n1. Single object allocation:" << endl;
    int* pInt = new int(42);
    cout << "Allocated int: " << *pInt << endl;
    delete pInt;
    
    cout << "\n2. Object allocation:" << endl;
    Simple* pSimple = new Simple(100, "Dynamic");
    pSimple->display();
    delete pSimple;
    
    cout << "\n3. Array allocation:" << endl;
    int* pArray = new int[5];
    for (int i = 0; i < 5; i++) {
        pArray[i] = i * 10;
        cout << pArray[i] << " ";
    }
    cout << endl;
    delete[] pArray;
    
    cout << "\n4. Object array allocation:" << endl;
    Simple* pSimpleArray = new Simple[3]{
        Simple(1, "First"),
        Simple(2, "Second"),
        Simple(3, "Third")
    };
    
    for (int i = 0; i < 3; i++) {
        pSimpleArray[i].display();
    }
    delete[] pSimpleArray;
    
    return 0;
}
```

**Output:**
```
=== Basic new and delete ===

1. Single object allocation:
Allocated int: 42

2. Object allocation:
Simple constructor: Dynamic (100)
Value: 100, Name: Dynamic
Simple destructor: Dynamic

3. Array allocation:
0 10 20 30 40 

4. Object array allocation:
Simple constructor: First (1)
Simple constructor: Second (2)
Simple constructor: Third (3)
Value: 1, Name: First
Value: 2, Name: Second
Value: 3, Name: Third
Simple destructor: Third
Simple destructor: Second
Simple destructor: First
```

---

## 2. **new and delete with Inheritance**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Shape {
protected:
    string color;
    
public:
    Shape(string c) : color(c) {
        cout << "Shape constructor: " << color << endl;
    }
    
    virtual double area() const = 0;
    virtual void draw() const = 0;
    
    virtual ~Shape() {
        cout << "Shape destructor: " << color << endl;
    }
};

class Circle : public Shape {
private:
    double radius;
    
public:
    Circle(string c, double r) : Shape(c), radius(r) {
        cout << "  Circle constructor: radius=" << radius << endl;
    }
    
    double area() const override {
        return 3.14159 * radius * radius;
    }
    
    void draw() const override {
        cout << "Drawing " << color << " circle with radius " << radius << endl;
    }
    
    ~Circle() override {
        cout << "  Circle destructor: radius=" << radius << endl;
    }
};

class Rectangle : public Shape {
private:
    double width, height;
    
public:
    Rectangle(string c, double w, double h) : Shape(c), width(w), height(h) {
        cout << "  Rectangle constructor: " << width << "x" << height << endl;
    }
    
    double area() const override {
        return width * height;
    }
    
    void draw() const override {
        cout << "Drawing " << color << " rectangle " << width << "x" << height << endl;
    }
    
    ~Rectangle() override {
        cout << "  Rectangle destructor: " << width << "x" << height << endl;
    }
};

int main() {
    cout << "=== new and delete with Inheritance ===" << endl;
    
    cout << "\n1. Creating polymorphic objects:" << endl;
    Shape* shapes[3];
    
    shapes[0] = new Circle("Red", 5.0);
    shapes[1] = new Rectangle("Blue", 4.0, 6.0);
    shapes[2] = new Circle("Green", 3.0);
    
    cout << "\n2. Using polymorphic objects:" << endl;
    for (int i = 0; i < 3; i++) {
        shapes[i]->draw();
        cout << "Area: " << shapes[i]->area() << endl;
    }
    
    cout << "\n3. Deleting polymorphic objects:" << endl;
    for (int i = 0; i < 3; i++) {
        delete shapes[i];  // Virtual destructor ensures proper cleanup
    }
    
    return 0;
}
```

---

## 3. **new with Exceptions (nothrow)**

```cpp
#include <iostream>
#include <new>
#include <cstdlib>
using namespace std;

class LargeObject {
private:
    char data[1024 * 1024];  // 1 MB
    
public:
    LargeObject() {
        cout << "LargeObject created" << endl;
    }
    
    ~LargeObject() {
        cout << "LargeObject destroyed" << endl;
    }
};

void handleAllocationFailure() {
    cerr << "Memory allocation failed!" << endl;
    exit(1);
}

int main() {
    cout << "=== new with Exceptions ===" << endl;
    
    cout << "\n1. Standard new (throws bad_alloc on failure):" << endl;
    try {
        // This may throw if memory is exhausted
        int* p = new int[1000000000];
        delete[] p;
        cout << "Allocation successful" << endl;
    } catch (const bad_alloc& e) {
        cout << "Allocation failed: " << e.what() << endl;
    }
    
    cout << "\n2. nothrow new (returns nullptr on failure):" << endl;
    int* p2 = new(nothrow) int[1000000000];
    if (p2 == nullptr) {
        cout << "Allocation failed (returned nullptr)" << endl;
    } else {
        delete[] p2;
        cout << "Allocation successful" << endl;
    }
    
    cout << "\n3. Custom new handler:" << endl;
    // Set custom new handler
    set_new_handler(handleAllocationFailure);
    
    // This will call handler on failure
    // int* p3 = new int[1000000000];
    // delete[] p3;
    
    // Reset new handler
    set_new_handler(nullptr);
    
    cout << "\n4. Placement new (no allocation, just construction):" << endl;
    char buffer[sizeof(LargeObject)];
    LargeObject* obj = new(buffer) LargeObject();
    obj->~LargeObject();  // Must call destructor manually
    
    return 0;
}
```

---

## 4. **new and delete Overloading**

```cpp
#include <iostream>
#include <cstdlib>
#include <new>
using namespace std;

class Tracked {
private:
    static int allocationCount;
    static int deallocationCount;
    int id;
    
public:
    Tracked() : id(++allocationCount) {
        cout << "Tracked " << id << " constructed" << endl;
    }
    
    ~Tracked() {
        cout << "Tracked " << id << " destroyed" << endl;
    }
    
    // Overloaded new operator
    static void* operator new(size_t size) {
        cout << "Custom new: allocating " << size << " bytes" << endl;
        allocationCount++;
        void* ptr = malloc(size);
        if (!ptr) throw bad_alloc();
        return ptr;
    }
    
    // Overloaded delete operator
    static void operator delete(void* ptr) {
        cout << "Custom delete: freeing memory" << endl;
        deallocationCount++;
        free(ptr);
    }
    
    // Overloaded new[] for arrays
    static void* operator new[](size_t size) {
        cout << "Custom new[]: allocating " << size << " bytes for array" << endl;
        return malloc(size);
    }
    
    // Overloaded delete[] for arrays
    static void operator delete[](void* ptr) {
        cout << "Custom delete[]: freeing array memory" << endl;
        free(ptr);
    }
    
    static void printStats() {
        cout << "Allocations: " << allocationCount 
             << ", Deallocations: " << deallocationCount << endl;
    }
};

int Tracked::allocationCount = 0;
int Tracked::deallocationCount = 0;

class Pool {
private:
    static const int POOL_SIZE = 1024;
    static char pool[POOL_SIZE];
    static bool used;
    
public:
    static void* operator new(size_t size) {
        if (!used && size <= POOL_SIZE) {
            used = true;
            cout << "Pool allocation: using static pool" << endl;
            return pool;
        }
        cout << "Pool allocation: falling back to heap" << endl;
        return ::operator new(size);
    }
    
    static void operator delete(void* ptr) {
        if (ptr == pool) {
            cout << "Pool deallocation: resetting pool" << endl;
            used = false;
        } else {
            cout << "Pool deallocation: freeing heap memory" << endl;
            ::operator delete(ptr);
        }
    }
    
    void display() {
        cout << "Pool object" << endl;
    }
};

char Pool::pool[POOL_SIZE];
bool Pool::used = false;

int main() {
    cout << "=== new and delete Overloading ===" << endl;
    
    cout << "\n1. Custom new/delete for Tracked:" << endl;
    Tracked* t1 = new Tracked();
    Tracked* t2 = new Tracked();
    delete t1;
    delete t2;
    Tracked::printStats();
    
    cout << "\n2. Array allocation with custom new[]/delete[]:" << endl;
    Tracked* tArray = new Tracked[3];
    delete[] tArray;
    
    cout << "\n3. Pool allocation:" << endl;
    Pool* p1 = new Pool();
    p1->display();
    delete p1;
    
    Pool* p2 = new Pool();  // Reuses the pool
    delete p2;
    
    return 0;
}
```

---

## 5. **Memory Allocation Strategies**

```cpp
#include <iostream>
#include <vector>
#include <chrono>
#include <memory>
using namespace std;
using namespace chrono;

class TestObject {
public:
    int data[100];
    TestObject() {
        for (int i = 0; i < 100; i++) data[i] = i;
    }
};

void testIndividualAllocations(int count) {
    vector<TestObject*> objects;
    for (int i = 0; i < count; i++) {
        objects.push_back(new TestObject());
    }
    for (auto obj : objects) {
        delete obj;
    }
}

void testBulkAllocation(int count) {
    TestObject* objects = new TestObject[count];
    delete[] objects;
}

void testSmartPointers(int count) {
    vector<unique_ptr<TestObject>> objects;
    for (int i = 0; i < count; i++) {
        objects.push_back(make_unique<TestObject>());
    }
}

int main() {
    cout << "=== Memory Allocation Strategies ===" << endl;
    
    const int COUNT = 100000;
    
    cout << "\n1. Individual allocations (new/delete):" << endl;
    auto start = high_resolution_clock::now();
    testIndividualAllocations(COUNT);
    auto end = high_resolution_clock::now();
    auto individualTime = duration_cast<milliseconds>(end - start).count();
    cout << "Time: " << individualTime << " ms" << endl;
    
    cout << "\n2. Bulk allocation (new[]/delete[]):" << endl;
    start = high_resolution_clock::now();
    testBulkAllocation(COUNT);
    end = high_resolution_clock::now();
    auto bulkTime = duration_cast<milliseconds>(end - start).count();
    cout << "Time: " << bulkTime << " ms" << endl;
    
    cout << "\n3. Smart pointers (unique_ptr):" << endl;
    start = high_resolution_clock::now();
    testSmartPointers(COUNT);
    end = high_resolution_clock::now();
    auto smartTime = duration_cast<milliseconds>(end - start).count();
    cout << "Time: " << smartTime << " ms" << endl;
    
    cout << "\n4. Allocation strategies comparison:" << endl;
    cout << "   Individual: " << individualTime << " ms" << endl;
    cout << "   Bulk: " << bulkTime << " ms" << endl;
    cout << "   Smart: " << smartTime << " ms" << endl;
    cout << "   Bulk is " << (individualTime / bulkTime) << "x faster" << endl;
    
    cout << "\n5. Best practices:" << endl;
    cout << "   ✓ Use bulk allocation for arrays" << endl;
    cout << "   ✓ Use smart pointers for individual objects" << endl;
    cout << "   ✓ Avoid raw new/delete in modern C++" << endl;
    cout << "   ✓ Consider custom allocators for performance-critical code" << endl;
    
    return 0;
}
```

---

## 📊 new and delete Summary

| Operator | Purpose | Array Version | Exception Behavior |
|----------|---------|---------------|-------------------|
| **new** | Single object | `new[]` | Throws `bad_alloc` |
| **delete** | Single object | `delete[]` | No-throw |
| **nothrow new** | Single object | `new(nothrow)[]` | Returns nullptr |
| **placement new** | Construction only | N/A | N/A |

---

## ✅ Best Practices

1. **Always match new with delete**, new[] with delete[]
2. **Use smart pointers** instead of raw new/delete
3. **Check for allocation failure** when using nothrow new
4. **Never delete twice** (undefined behavior)
5. **Use virtual destructors** for polymorphic base classes
6. **Consider custom allocators** for performance-critical code

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Mismatched new/delete** | Undefined behavior | Use new[] with delete[] |
| **Double delete** | Undefined behavior | Set pointers to nullptr after delete |
| **Forgetting delete** | Memory leak | Use smart pointers |
| **Deleting void*** | Undefined behavior | Ensure correct type |
| **Deleting const pointer** | Undefined behavior | Remove const before delete |

---

## ✅ Key Takeaways

1. **new** allocates and constructs
2. **delete** destroys and deallocates
3. **new[]/delete[]** for arrays
4. **nothrow** returns nullptr on failure
5. **Placement new** constructs in existing memory
6. **Custom new/delete** for special allocation strategies
7. **Smart pointers** are preferred in modern C++

---