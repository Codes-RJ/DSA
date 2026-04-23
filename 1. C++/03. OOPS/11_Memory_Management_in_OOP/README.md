# README.md

## Memory Management in OOP - Complete Guide

### Overview

Memory management is a critical aspect of C++ programming that involves allocating, using, and freeing memory. Unlike languages with garbage collection, C++ gives programmers direct control over memory, which enables high performance but also requires careful management to avoid leaks, dangling pointers, and undefined behavior. In object-oriented programming, memory management becomes especially important when dealing with dynamically allocated objects, polymorphic hierarchies, and resource ownership.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [01_New_and_Delete.md](01_New_and_Delete.md) | understand New and Delete Operators |
| 2. | [02_New_Delete_for_Objects.md](02_New_Delete_for_Objects.md) | understand New and Delete for Objects |
| 3. | [03_Placement_New.md](03_Placement_New.md) | understand Placement New |
| 4. | [04_Memory_Pools.md](04_Memory_Pools.md) | understand Memory Pools |
| 5. | [05_Smart_Pointers_Intro.md](05_Smart_Pointers_Intro.md) | understand Smart Pointers Introduction |
| 6. | [Theory.md](Theory.md) | understand Theoretical Foundations of Memory Management |

---

## 1. New and Delete Operators

This topic explains the fundamental operators for dynamic memory allocation and deallocation.

**File:** [01_New_and_Delete.md](01_New_and_Delete.md)

**What you will learn:**
- What is dynamic memory allocation
- The `new` operator for allocating memory
- The `delete` operator for freeing memory
- Memory leaks and how to prevent them
- Dangling pointers and null pointers
- `new` and `delete` for arrays
- `new(nothrow)` for non-throwing allocation

**Key Concepts:**

| Concept | Description | Example |
|---------|-------------|---------|
| **new** | Allocates memory on the heap | `int* p = new int;` |
| **delete** | Frees memory allocated with new | `delete p;` |
| **new[]** | Allocates array on the heap | `int* arr = new int[10];` |
| **delete[]** | Frees array allocated with new[] | `delete[] arr;` |
| **Memory Leak** | Memory not freed after use | Forgetting to delete |
| **Dangling Pointer** | Pointer to freed memory | Accessing after delete |

**Syntax:**
```cpp
#include <iostream>
using namespace std;

int main() {
    // Single variable allocation
    int* p = new int;
    *p = 42;
    cout << *p << endl;
    delete p;
    p = nullptr;  // Prevent dangling pointer
    
    // Allocation with initialization
    int* q = new int(100);
    cout << *q << endl;
    delete q;
    
    // Array allocation
    int* arr = new int[5];
    for (int i = 0; i < 5; i++) {
        arr[i] = i * 10;
    }
    delete[] arr;
    
    // Non-throwing new (returns nullptr on failure)
    int* large = new (nothrow) int[1000000000];
    if (large == nullptr) {
        cout << "Allocation failed" << endl;
    }
    delete[] large;
    
    return 0;
}
```

---

## 2. New and Delete for Objects

This topic explains how `new` and `delete` work with class objects, including constructor and destructor calls.

**File:** [02_New_Delete_for_Objects.md](02_New_Delete_for_Objects.md)

**What you will learn:**
- How `new` calls constructors
- How `delete` calls destructors
- Allocating and deallocating object arrays
- Object construction order
- Custom new/delete operators (overview)
- Placement new for objects (preview)

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **new for Objects** | Allocates memory AND calls constructor |
| **delete for Objects** | Calls destructor AND frees memory |
| **Object Array new** | Calls constructor for each element |
| **Object Array delete** | Calls destructor for each element |
| **Construction Order** | From first to last in array |
| **Destruction Order** | From last to first in array |

**Syntax:**
```cpp
#include <iostream>
using namespace std;

class Widget {
private:
    int id_;
    static int counter_;
    
public:
    Widget() : id_(++counter_) {
        cout << "Widget " << id_ << " constructed" << endl;
    }
    
    ~Widget() {
        cout << "Widget " << id_ << " destroyed" << endl;
    }
    
    int getId() const { return id_; }
};

int Widget::counter_ = 0;

int main() {
    // Single object
    Widget* w = new Widget();
    cout << "Widget ID: " << w->getId() << endl;
    delete w;
    
    // Array of objects
    Widget* arr = new Widget[3];
    delete[] arr;  // Destructors called in reverse order
    
    return 0;
}
```

**Output:**
```
Widget 1 constructed
Widget ID: 1
Widget 1 destroyed
Widget 2 constructed
Widget 3 constructed
Widget 4 constructed
Widget 4 destroyed
Widget 3 destroyed
Widget 2 destroyed
```

---

## 3. Placement New

This topic explains placement new, which allows constructing objects at pre-allocated memory locations.

**File:** [03_Placement_New.md](03_Placement_New.md)

**What you will learn:**
- What is placement new
- Syntax for placement new (`new (address) Type(args)`)
- Separating allocation from construction
- Manual destructor calls for placement new
- Alignment requirements
- Memory pools and custom allocators

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Placement New** | Constructs object at specific memory address |
| **No Allocation** | Only constructs, does not allocate |
| **Manual Destruction** | Must call destructor explicitly |
| **Alignment** | Memory must be properly aligned for type |
| **Use Cases** | Memory pools, shared memory, embedded systems |

**Syntax:**
```cpp
#include <iostream>
#include <new>
using namespace std;

class Widget {
private:
    int x_;
    double y_;
    
public:
    Widget(int x, double y) : x_(x), y_(y) {
        cout << "Widget constructed" << endl;
    }
    
    ~Widget() {
        cout << "Widget destroyed" << endl;
    }
    
    void display() const {
        cout << "x=" << x_ << ", y=" << y_ << endl;
    }
};

int main() {
    // Raw memory buffer
    char buffer[sizeof(Widget)];
    
    // Construct Widget in the buffer
    Widget* w = new (buffer) Widget(42, 3.14);
    
    w->display();
    
    // Manual destructor call
    w->~Widget();
    
    // Buffer memory is automatically freed (stack)
    
    return 0;
}
```

---

## 4. Memory Pools

This topic explains memory pools for efficient allocation of many small objects.

**File:** [04_Memory_Pools.md](04_Memory_Pools.md)

**What you will learn:**
- What are memory pools
- Why memory pools are used (performance, fragmentation)
- Implementing a simple memory pool
- Fixed-size allocators
- Object pooling pattern
- When to use memory pools

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Memory Pool** | Pre-allocated block of memory for objects of fixed size |
| **Object Pool** | Reuses objects instead of allocating/freeing |
| **Fragmentation Reduction** | Eliminates external fragmentation |
| **Performance Improvement** | Faster than general-purpose allocator |
| **Predictable Allocation** | O(1) allocation and deallocation |

**Syntax:**
```cpp
#include <iostream>
#include <vector>
#include <cstddef>
using namespace std;

class MemoryPool {
private:
    struct Block {
        Block* next_;
    };
    
    Block* freeList_;
    vector<char> memory_;
    size_t blockSize_;
    
public:
    MemoryPool(size_t blockSize, size_t poolSize) 
        : blockSize_(blockSize), freeList_(nullptr) {
        
        memory_.resize(blockSize * poolSize);
        
        // Build free list
        char* ptr = memory_.data();
        for (size_t i = 0; i < poolSize; i++) {
            Block* block = reinterpret_cast<Block*>(ptr);
            block->next_ = freeList_;
            freeList_ = block;
            ptr += blockSize_;
        }
    }
    
    void* allocate() {
        if (freeList_ == nullptr) {
            throw bad_alloc();
        }
        void* result = freeList_;
        freeList_ = freeList_->next_;
        return result;
    }
    
    void deallocate(void* ptr) {
        Block* block = static_cast<Block*>(ptr);
        block->next_ = freeList_;
        freeList_ = block;
    }
    
    size_t getBlockSize() const { return blockSize_; }
};

// Object that uses custom allocator
class PooledObject {
private:
    int data_;
    static MemoryPool pool_;
    
public:
    static void* operator new(size_t size) {
        if (size != sizeof(PooledObject)) {
            return ::operator new(size);
        }
        return pool_.allocate();
    }
    
    static void operator delete(void* ptr, size_t size) {
        if (size != sizeof(PooledObject)) {
            ::operator delete(ptr);
            return;
        }
        pool_.deallocate(ptr);
    }
    
    PooledObject(int data) : data_(data) { }
};

MemoryPool PooledObject::pool_(sizeof(PooledObject), 100);

int main() {
    vector<PooledObject*> objects;
    
    for (int i = 0; i < 50; i++) {
        objects.push_back(new PooledObject(i));
    }
    
    for (auto obj : objects) {
        delete obj;
    }
    
    return 0;
}
```

---

## 5. Smart Pointers Introduction

This topic introduces smart pointers as RAII wrappers for dynamic memory management.

**File:** [05_Smart_Pointers_Intro.md](05_Smart_Pointers_Intro.md)

**What you will learn:**
- Problems with raw pointers (leaks, dangling pointers)
- What are smart pointers
- `std::unique_ptr` for exclusive ownership
- `std::shared_ptr` for shared ownership
- `std::weak_ptr` for breaking cycles
- `std::auto_ptr` (deprecated)
- Smart pointer best practices

**Key Concepts:**

| Smart Pointer | Ownership Model | Use Case |
|---------------|-----------------|----------|
| **unique_ptr** | Exclusive ownership | Single owner, no copying |
| **shared_ptr** | Shared ownership | Multiple owners, reference counting |
| **weak_ptr** | Non-owning observer | Breaking cycles, caching |
| **auto_ptr** | Transfer ownership | Deprecated, use unique_ptr |

**Syntax:**
```cpp
#include <iostream>
#include <memory>
using namespace std;

class Widget {
private:
    int id_;
    
public:
    Widget(int id) : id_(id) {
        cout << "Widget " << id_ << " created" << endl;
    }
    
    ~Widget() {
        cout << "Widget " << id_ << " destroyed" << endl;
    }
    
    void process() {
        cout << "Processing Widget " << id_ << endl;
    }
};

int main() {
    // unique_ptr - exclusive ownership
    unique_ptr<Widget> u1 = make_unique<Widget>(1);
    // unique_ptr<Widget> u2 = u1;  // Error - cannot copy
    unique_ptr<Widget> u2 = move(u1);  // OK - transfer ownership
    
    // shared_ptr - shared ownership
    shared_ptr<Widget> s1 = make_shared<Widget>(2);
    shared_ptr<Widget> s2 = s1;  // OK - shared ownership
    cout << "Reference count: " << s1.use_count() << endl;
    
    // weak_ptr - non-owning observer
    weak_ptr<Widget> w = s1;
    if (auto sp = w.lock()) {
        sp->process();
    }
    
    return 0;
}
```

---

## 6. Theoretical Foundations

This topic covers the theoretical concepts behind memory management.

**File:** [Theory.md](Theory.md)

**What you will learn:**
- Memory hierarchy (stack, heap, static storage)
- Allocation strategies (first-fit, best-fit, buddy allocator)
- Memory fragmentation (external, internal)
- Garbage collection algorithms
- RAII philosophy
- Ownership semantics
- Memory management in C++ vs other languages

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Stack Allocation** | Automatic, fast, fixed size, LIFO |
| **Heap Allocation** | Manual, slower, flexible, arbitrary size |
| **Static Storage** | Program lifetime, fixed size |
| **Fragmentation** | Inability to use free memory due to splitting |
| **RAII** | Resource Acquisition Is Initialization |
| **Ownership** | Responsibility for releasing memory |

---

### Prerequisites

Before starting this section, you should have completed:

- [01. Basics](../../01.%20Basics/README.md) - Pointers, references, dynamic memory
- [02_Classes_and_Objects/README.md](../02_Classes_and_Objects/README.md) - Class basics
- [03_Constructors_and_Destructors/README.md](../03_Constructors_and_Destructors/README.md) - Object lifecycle
- [10_Exception_Handling_in_OOP/README.md](../10_Exception_Handling_in_OOP/README.md) - RAII concepts

---

### Sample Memory Management Code

```cpp
#include <iostream>
#include <memory>
#include <vector>
using namespace std;

class Resource {
private:
    string name_;
    
public:
    Resource(const string& name) : name_(name) {
        cout << "Resource " << name_ << " acquired" << endl;
    }
    
    ~Resource() {
        cout << "Resource " << name_ << " released" << endl;
    }
    
    void use() const {
        cout << "Using resource " << name_ << endl;
    }
};

// RAII container
class ResourceContainer {
private:
    unique_ptr<Resource> resource_;
    
public:
    ResourceContainer(const string& name) 
        : resource_(make_unique<Resource>(name)) { }
    
    void use() const {
        resource_->use();
    }
};

int main() {
    // Stack allocation (automatic)
    int stackVar = 42;
    
    // Heap allocation (manual - avoid)
    int* rawPtr = new int(100);
    delete rawPtr;
    
    // Smart pointer (preferred)
    unique_ptr<int> smartPtr = make_unique<int>(200);
    
    // RAII container
    ResourceContainer container("MyResource");
    container.use();
    
    // Vector manages its memory automatically
    vector<int> vec = {1, 2, 3, 4, 5};
    
    return 0;
}
```

---

### Learning Path

```
Level 1: Basic Memory Management
├── New and Delete
├── New and Delete for Objects
└── Array Allocation

Level 2: Advanced Allocation
├── Placement New
├── Memory Pools
└── Custom Allocators

Level 3: Smart Pointers
├── Unique Pointer
├── Shared Pointer
└── Weak Pointer

Level 4: RAII and Ownership
├── RAII Philosophy
├── Ownership Semantics
└── Rule of Three/Five/Zero
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Forgetting to delete | Use smart pointers |
| Double deletion | Set pointers to nullptr after delete |
| Dangling pointers | Use references or smart pointers |
| Memory leaks | Use RAII for all resources |
| Mismatched new/delete | new[] must use delete[] |
| Throwing from destructor | Destructors should be noexcept |

---

### Practice Questions

After completing this section, you should be able to:

1. Allocate and deallocate memory using `new` and `delete`
2. Use `new[]` and `delete[]` for arrays
3. Implement placement new for custom memory pools
4. Create a simple memory pool allocator
5. Use `unique_ptr` for exclusive ownership
6. Use `shared_ptr` for shared ownership
7. Break reference cycles with `weak_ptr`
8. Explain RAII and its importance in exception safety

---

### Next Steps

- Go to [Theory.md](Theory.md) to understand the basics.