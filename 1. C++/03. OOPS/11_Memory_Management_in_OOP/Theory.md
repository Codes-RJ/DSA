# Memory Management in OOP - Complete Guide

## 📖 Overview

Memory management is a critical aspect of C++ programming that directly affects performance, stability, and correctness. In Object-Oriented Programming, understanding how objects are allocated, used, and destroyed is essential. C++ provides both automatic and manual memory management, giving developers fine-grained control over resource usage.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Stack Allocation** | Automatic memory management, fast, limited size |
| **Heap Allocation** | Manual memory management, flexible, larger size |
| **RAII** | Resource Acquisition Is Initialization |
| **Smart Pointers** | Automatic memory management for heap objects |
| **Memory Leaks** | Failure to deallocate memory |
| **Dangling Pointers** | Pointers to already deallocated memory |

---

## 📊 Memory Allocation Types

| Type | Allocation | Deallocation | Speed | Size | Lifetime |
|------|------------|--------------|-------|------|----------|
| **Stack** | Automatic | Automatic | Fast | Limited | Scope-based |
| **Heap** | Manual (`new`) | Manual (`delete`) | Slower | Large | Programmer-controlled |
| **Static** | Program start | Program end | Fast | Fixed | Program lifetime |
| **Thread Local** | Thread start | Thread end | Fast | Limited | Thread lifetime |

---

## 1. **Stack vs Heap Memory**

```cpp
#include <iostream>
#include <string>
#include <chrono>
using namespace std;

class BigObject {
private:
    int data[1000];
    
public:
    BigObject() {
        for (int i = 0; i < 1000; i++) data[i] = i;
    }
    
    void process() {
        // Simulate processing
        for (int i = 0; i < 1000; i++) data[i] *= 2;
    }
};

void stackAllocation() {
    BigObject obj;  // Allocated on stack
    obj.process();  // Automatic cleanup when function returns
}

void heapAllocation() {
    BigObject* obj = new BigObject();  // Allocated on heap
    obj->process();
    delete obj;  // Must manually deallocate
}

int main() {
    cout << "=== Stack vs Heap Memory ===" << endl;
    
    cout << "\n1. Stack allocation (automatic):" << endl;
    stackAllocation();  // Object automatically destroyed
    
    cout << "\n2. Heap allocation (manual):" << endl;
    heapAllocation();   // Must call delete
    
    cout << "\n3. Stack overflow risk:" << endl;
    cout << "   Large arrays on stack can cause overflow" << endl;
    
    cout << "\n4. Heap fragmentation risk:" << endl;
    cout << "   Frequent allocation/deallocation can fragment heap" << endl;
    
    cout << "\n5. Performance comparison:" << endl;
    const int ITERATIONS = 1000000;
    
    auto start = chrono::high_resolution_clock::now();
    for (int i = 0; i < ITERATIONS; i++) {
        int x = 42;  // Stack allocation
    }
    auto end = chrono::high_resolution_clock::now();
    auto stackTime = chrono::duration_cast<chrono::microseconds>(end - start).count();
    
    start = chrono::high_resolution_clock::now();
    for (int i = 0; i < ITERATIONS; i++) {
        int* x = new int(42);  // Heap allocation
        delete x;
    }
    end = chrono::high_resolution_clock::now();
    auto heapTime = chrono::duration_cast<chrono::microseconds>(end - start).count();
    
    cout << "Stack allocation: " << stackTime << " μs" << endl;
    cout << "Heap allocation: " << heapTime << " μs" << endl;
    cout << "Heap is " << (heapTime / stackTime) << "x slower" << endl;
    
    return 0;
}
```

---

## 2. **Memory Leaks and Dangling Pointers**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Resource {
private:
    string name;
    int* data;
    
public:
    Resource(string n) : name(n) {
        data = new int[100];
        cout << "Resource created: " << name << endl;
    }
    
    ~Resource() {
        delete[] data;
        cout << "Resource destroyed: " << name << endl;
    }
    
    void use() {
        cout << "Using resource: " << name << endl;
    }
};

// Memory leak example
void memoryLeak() {
    Resource* leak = new Resource("Leaky");  // Never deleted
    leak->use();
    // Missing delete leak; -> memory leak!
}

// Correct management
void correctManagement() {
    Resource* res = new Resource("Correct");
    res->use();
    delete res;  // Proper cleanup
}

// Dangling pointer example
int* createDanglingPointer() {
    int x = 42;  // Stack variable
    return &x;   // Returns pointer to stack memory - DANGEROUS!
}

int* createValidPointer() {
    int* ptr = new int(42);  // Heap allocation
    return ptr;              // Valid - caller must delete
}

int main() {
    cout << "=== Memory Leaks and Dangling Pointers ===" << endl;
    
    cout << "\n1. Memory leak:" << endl;
    memoryLeak();  // Memory leaked!
    
    cout << "\n2. Correct management:" << endl;
    correctManagement();
    
    cout << "\n3. Dangling pointer (stack):" << endl;
    int* dangling = createDanglingPointer();
    cout << "Dangling pointer value: " << *dangling << " (may be garbage!)" << endl;
    
    cout << "\n4. Valid pointer (heap):" << endl;
    int* valid = createValidPointer();
    cout << "Valid pointer value: " << *valid << endl;
    delete valid;
    
    cout << "\n5. Double delete (undefined behavior):" << endl;
    int* ptr = new int(10);
    delete ptr;
    // delete ptr;  // Undefined behavior - double delete
    
    return 0;
}
```

---

## 3. **RAII (Resource Acquisition Is Initialization)**

```cpp
#include <iostream>
#include <fstream>
#include <mutex>
#include <thread>
#include <vector>
using namespace std;

// RAII for file handling
class FileHandler {
private:
    FILE* file;
    string filename;
    
public:
    FileHandler(const string& name, const string& mode) : filename(name) {
        file = fopen(name.c_str(), mode.c_str());
        if (!file) {
            throw runtime_error("Cannot open file: " + name);
        }
        cout << "File opened: " << name << endl;
    }
    
    ~FileHandler() {
        if (file) {
            fclose(file);
            cout << "File closed: " << filename << endl;
        }
    }
    
    void write(const string& data) {
        if (file) {
            fprintf(file, "%s\n", data.c_str());
        }
    }
    
    // Prevent copying
    FileHandler(const FileHandler&) = delete;
    FileHandler& operator=(const FileHandler&) = delete;
};

// RAII for mutex locking
class MutexGuard {
private:
    mutex& mtx;
    
public:
    explicit MutexGuard(mutex& m) : mtx(m) {
        mtx.lock();
        cout << "Mutex locked" << endl;
    }
    
    ~MutexGuard() {
        mtx.unlock();
        cout << "Mutex unlocked" << endl;
    }
    
    // Prevent copying
    MutexGuard(const MutexGuard&) = delete;
    MutexGuard& operator=(const MutexGuard&) = delete;
};

class Counter {
private:
    int value;
    mutex mtx;
    
public:
    Counter() : value(0) {}
    
    void increment() {
        MutexGuard lock(mtx);  // RAII lock
        value++;  // Automatically unlocked on exit
    }
    
    int getValue() const {
        MutexGuard lock(mtx);
        return value;
    }
};

void worker(Counter& counter, int iterations) {
    for (int i = 0; i < iterations; i++) {
        counter.increment();
    }
}

int main() {
    cout << "=== RAII (Resource Acquisition Is Initialization) ===" << endl;
    
    cout << "\n1. File handling with RAII:" << endl;
    try {
        FileHandler file("test.txt", "w");
        file.write("Line 1");
        file.write("Line 2");
        // No need to close - destructor handles it
    } catch (const exception& e) {
        cout << "Error: " << e.what() << endl;
    }
    
    cout << "\n2. Mutex with RAII:" << endl;
    Counter counter;
    const int THREADS = 4;
    const int ITERATIONS = 100000;
    vector<thread> threads;
    
    for (int i = 0; i < THREADS; i++) {
        threads.emplace_back(worker, ref(counter), ITERATIONS);
    }
    
    for (auto& t : threads) {
        t.join();
    }
    
    cout << "Final count: " << counter.getValue() << endl;
    cout << "Expected: " << (THREADS * ITERATIONS) << endl;
    
    return 0;
}
```

---

## 4. **Smart Pointers Overview**

```cpp
#include <iostream>
#include <memory>
#include <vector>
#include <string>
using namespace std;

class Widget {
private:
    string name;
    int id;
    static int nextId;
    
public:
    Widget(string n) : name(n), id(nextId++) {
        cout << "Widget created: " << name << " (ID: " << id << ")" << endl;
    }
    
    ~Widget() {
        cout << "Widget destroyed: " << name << " (ID: " << id << ")" << endl;
    }
    
    void doSomething() {
        cout << "Widget " << name << " doing something" << endl;
    }
    
    int getId() const { return id; }
    string getName() const { return name; }
};

int Widget::nextId = 1;

// unique_ptr - exclusive ownership
void uniquePtrExample() {
    cout << "\n--- unique_ptr (exclusive ownership) ---" << endl;
    unique_ptr<Widget> u1 = make_unique<Widget>("Unique1");
    unique_ptr<Widget> u2 = make_unique<Widget>("Unique2");
    
    u1->doSomething();
    
    // Transfer ownership
    unique_ptr<Widget> u3 = move(u1);
    if (!u1) cout << "u1 is now empty" << endl;
    u3->doSomething();
    
    // Cannot copy
    // unique_ptr<Widget> u4 = u2;  // Error!
}

// shared_ptr - shared ownership
void sharedPtrExample() {
    cout << "\n--- shared_ptr (shared ownership) ---" << endl;
    shared_ptr<Widget> s1 = make_shared<Widget>("Shared1");
    {
        shared_ptr<Widget> s2 = s1;  // Reference count: 2
        shared_ptr<Widget> s3 = s2;  // Reference count: 3
        cout << "Reference count: " << s1.use_count() << endl;
        s2->doSomething();
    }  // s2 and s3 destroyed, count becomes 1
    cout << "Reference count: " << s1.use_count() << endl;
    s1->doSomething();
}

// weak_ptr - non-owning observer
void weakPtrExample() {
    cout << "\n--- weak_ptr (non-owning observer) ---" << endl;
    shared_ptr<Widget> s = make_shared<Widget>("Shared");
    weak_ptr<Widget> w = s;
    
    cout << "Reference count: " << s.use_count() << endl;
    
    if (auto locked = w.lock()) {
        locked->doSomething();
        cout << "Weak pointer valid" << endl;
    }
    
    s.reset();  // Destroy the object
    
    if (auto locked = w.lock()) {
        locked->doSomething();
    } else {
        cout << "Weak pointer expired" << endl;
    }
}

// Container of smart pointers
void containerExample() {
    cout << "\n--- Container of smart pointers ---" << endl;
    vector<unique_ptr<Widget>> widgets;
    widgets.push_back(make_unique<Widget>("A"));
    widgets.push_back(make_unique<Widget>("B"));
    widgets.push_back(make_unique<Widget>("C"));
    
    for (auto& w : widgets) {
        w->doSomething();
    }
    // All automatically destroyed when vector goes out of scope
}

int main() {
    cout << "=== Smart Pointers Overview ===" << endl;
    
    uniquePtrExample();
    sharedPtrExample();
    weakPtrExample();
    containerExample();
    
    cout << "\nAll memory automatically managed!" << endl;
    
    return 0;
}
```

---

## 5. **Memory Management Best Practices**

```cpp
#include <iostream>
#include <memory>
#include <vector>
#include <string>
using namespace std;

// Good: Rule of Zero - use RAII types
class GoodClass {
private:
    string name;              // std::string manages memory
    vector<int> data;         // std::vector manages memory
    unique_ptr<int> ptr;      // smart pointer manages memory
    
public:
    GoodClass(string n) : name(n) {
        ptr = make_unique<int>(42);
    }
    // No destructor, copy, move needed - Rule of Zero
};

// Bad: Manual memory management
class BadClass {
private:
    char* name;
    int* data;
    size_t size;
    
public:
    BadClass(const char* n, size_t s) : size(s) {
        name = new char[strlen(n) + 1];
        strcpy(name, n);
        data = new int[size];
    }
    
    // Need destructor, copy constructor, copy assignment
    ~BadClass() {
        delete[] name;
        delete[] data;
    }
    
    // Copy constructor (Rule of Three)
    BadClass(const BadClass& other) : size(other.size) {
        name = new char[strlen(other.name) + 1];
        strcpy(name, other.name);
        data = new int[size];
        memcpy(data, other.data, size * sizeof(int));
    }
    
    // Copy assignment (Rule of Three)
    BadClass& operator=(const BadClass& other) {
        if (this != &other) {
            delete[] name;
            delete[] data;
            size = other.size;
            name = new char[strlen(other.name) + 1];
            strcpy(name, other.name);
            data = new int[size];
            memcpy(data, other.data, size * sizeof(int));
        }
        return *this;
    }
};

// Good: Using factory functions
class Resource {
private:
    Resource() {}  // Private constructor
    
public:
    static unique_ptr<Resource> create() {
        return make_unique<Resource>();
    }
    
    void use() {
        cout << "Using resource" << endl;
    }
};

// Good: Custom deleter
void customDeleter(int* p) {
    cout << "Custom deleting: " << *p << endl;
    delete p;
}

int main() {
    cout << "=== Memory Management Best Practices ===" << endl;
    
    cout << "\n1. Rule of Zero (preferred):" << endl;
    GoodClass good("Good");
    // No manual cleanup needed
    
    cout << "\n2. Rule of Three (when necessary):" << endl;
    BadClass bad("Bad", 100);
    BadClass bad2 = bad;  // Copy constructor
    
    cout << "\n3. Factory pattern with smart pointers:" << endl;
    auto res = Resource::create();
    res->use();
    
    cout << "\n4. Custom deleter:" << endl;
    unique_ptr<int, void(*)(int*)> custom(new int(42), customDeleter);
    // Automatically calls custom deleter
    
    cout << "\n5. Memory allocation strategies:" << endl;
    cout << "   ✓ Prefer stack allocation when possible" << endl;
    cout << "   ✓ Use smart pointers for heap allocation" << endl;
    cout << "   ✓ Avoid raw pointers for ownership" << endl;
    cout << "   ✓ Follow RAII principle" << endl;
    cout << "   ✓ Apply Rule of Zero/Three/Five" << endl;
    
    return 0;
}
```

---

## 📊 Memory Management Summary

| Aspect | Stack | Heap | Static |
|--------|-------|------|--------|
| **Allocation Speed** | Fast | Slower | Fast |
| **Size** | Limited (MB) | Large (GB) | Fixed |
| **Lifetime** | Scope-based | Programmer-controlled | Program lifetime |
| **Management** | Automatic | Manual/RAII | Automatic |
| **Fragmentation** | None | Possible | None |

---

## ✅ Best Practices

1. **Prefer stack allocation** when possible (faster, automatic)
2. **Use RAII** for all resource management
3. **Use smart pointers** for heap allocation
4. **Follow Rule of Zero** - use RAII types
5. **Follow Rule of Three/Five** when managing resources manually
6. **Avoid raw pointers** for ownership
7. **Never use raw `new`/`delete`** in modern C++ (except in low-level code)

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Memory leak** | Forgetting to delete | Use smart pointers |
| **Double delete** | Deleting same pointer twice | Use smart pointers |
| **Dangling pointer** | Using deleted memory | Use smart pointers |
| **Buffer overflow** | Writing beyond array bounds | Use std::vector |
| **Stack overflow** | Large stack allocation | Use heap for large objects |

---
---

## Next Step

- Go to [README.md](README.md) to continue.
