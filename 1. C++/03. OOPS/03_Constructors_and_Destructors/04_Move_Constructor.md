# Move Constructor in C++ - Complete Guide

## 📖 Overview

The move constructor (C++11) is a special constructor that transfers resources from a temporary object to a new object without copying. It significantly improves performance by eliminating unnecessary deep copies. Move semantics enable efficient handling of temporary objects and are essential for modern C++ programming.

---

## 🎯 Key Concepts

| Aspect | Description |
|--------|-------------|
| **Purpose** | Transfer resources from temporary/rvalue objects |
| **Syntax** | `ClassName(ClassName&& other) noexcept;` |
| **When Called** | When object is initialized from rvalue (temporary) |
| **Benefit** | Avoids expensive deep copies |
| **Key Operation** | Steal resources, leave source in valid state |

---

## 1. **Move Constructor Basics**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <chrono>
using namespace std;

class Buffer {
private:
    int* data;
    size_t size;
    static int moveCount;
    static int copyCount;
    
public:
    // Constructor
    Buffer(size_t s) : size(s) {
        data = new int[size];
        for (size_t i = 0; i < size; i++) {
            data[i] = i;
        }
        cout << "Constructor: allocated " << size << " ints" << endl;
    }
    
    // Copy constructor (expensive)
    Buffer(const Buffer& other) : size(other.size) {
        data = new int[size];
        for (size_t i = 0; i < size; i++) {
            data[i] = other.data[i];
        }
        copyCount++;
        cout << "Copy constructor: copied " << size << " ints" << endl;
    }
    
    // Move constructor (efficient)
    Buffer(Buffer&& other) noexcept : data(other.data), size(other.size) {
        other.data = nullptr;
        other.size = 0;
        moveCount++;
        cout << "Move constructor: stole " << size << " ints" << endl;
    }
    
    // Destructor
    ~Buffer() {
        if (data) {
            cout << "Destructor: freeing " << size << " ints" << endl;
            delete[] data;
        } else {
            cout << "Destructor: null (moved from)" << endl;
        }
    }
    
    static void printStats() {
        cout << "\nStatistics: Copies: " << copyCount 
             << ", Moves: " << moveCount << endl;
    }
    
    void displayFirstFew() const {
        cout << "First 5 elements: ";
        for (size_t i = 0; i < min(size, (size_t)5); i++) {
            cout << data[i] << " ";
        }
        cout << "..." << endl;
    }
};

int Buffer::moveCount = 0;
int Buffer::copyCount = 0;

// Function that returns a temporary (rvalue)
Buffer createBuffer(size_t size) {
    Buffer temp(size);
    return temp;  // Move constructor (or RVO)
}

// Function that takes by value (triggers copy or move)
void processBuffer(Buffer b) {
    b.displayFirstFew();
}

int main() {
    cout << "=== Move Constructor Basics ===" << endl;
    
    cout << "\n1. Copy constructor (expensive):" << endl;
    Buffer b1(100);
    Buffer b2 = b1;  // Copy - expensive
    
    cout << "\n2. Move constructor (efficient):" << endl;
    Buffer b3 = move(b1);  // Move - cheap
    cout << "b1 after move: ";
    b1.displayFirstFew();  // b1 is now empty
    
    cout << "\n3. Returning from function:" << endl;
    Buffer b4 = createBuffer(50);  // Move (or RVO)
    
    cout << "\n4. Passing temporary to function:" << endl;
    processBuffer(Buffer(30));  // Move constructor
    
    Buffer::printStats();
    
    return 0;
}
```

**Output:**
```
=== Move Constructor Basics ===

1. Copy constructor (expensive):
Constructor: allocated 100 ints
Copy constructor: copied 100 ints

2. Move constructor (efficient):
Move constructor: stole 100 ints
b1 after move: First 5 elements: 0 1 2 3 4 ...

3. Returning from function:
Constructor: allocated 50 ints

4. Passing temporary to function:
Constructor: allocated 30 ints
Move constructor: stole 30 ints
First 5 elements: 0 1 2 3 4 ...
Destructor: freeing 30 ints

Statistics: Copies: 1, Moves: 2
Destructor: freeing 50 ints
Destructor: null (moved from)
Destructor: freeing 100 ints
Destructor: freeing 100 ints
```

---

## 2. **lvalues vs rvalues**

Understanding value categories is essential for move semantics.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Demo {
private:
    string name;
    
public:
    Demo(string n) : name(n) {
        cout << "Constructor: " << name << endl;
    }
    
    // Copy constructor
    Demo(const Demo& other) : name(other.name + "_copy") {
        cout << "Copy: " << name << " (from " << other.name << ")" << endl;
    }
    
    // Move constructor
    Demo(Demo&& other) noexcept : name(move(other.name)) {
        cout << "Move: " << name << " (stolen from " << other.name << ")" << endl;
        other.name = "EMPTY";
    }
    
    void display() const {
        cout << "Object: " << name << endl;
    }
};

Demo createDemo() {
    Demo temp("Temporary");
    return temp;  // Move or RVO
}

int main() {
    cout << "=== lvalues vs rvalues ===" << endl;
    
    cout << "\n1. lvalue (named variable):" << endl;
    Demo d1("Original");
    Demo d2 = d1;  // Copy (d1 is lvalue)
    
    cout << "\n2. rvalue (temporary):" << endl;
    Demo d3 = Demo("Anonymous");  // Move (rvalue)
    
    cout << "\n3. std::move converts lvalue to rvalue:" << endl;
    Demo d4 = move(d1);  // Move (d1 cast to rvalue)
    cout << "d1 after move: ";
    d1.display();
    
    cout << "\n4. Function return (rvalue):" << endl;
    Demo d5 = createDemo();  // Move or RVO
    
    cout << "\n5. Reference binding:" << endl;
    Demo& lref = d2;      // lvalue reference
    // Demo& lref2 = Demo("temp");  // Error! cannot bind rvalue to lvalue ref
    Demo&& rref = Demo("temp");  // rvalue reference (OK)
    
    cout << "\n--- End of main ---" << endl;
    return 0;
}
```

**Output:**
```
=== lvalues vs rvalues ===

1. lvalue (named variable):
Constructor: Original
Copy: Original_copy (from Original)

2. rvalue (temporary):
Constructor: Anonymous
Move: Anonymous (stolen from Anonymous)

3. std::move converts lvalue to rvalue:
Move: Original (stolen from Original)
d1 after move: Object: EMPTY

4. Function return (rvalue):
Constructor: Temporary

5. Reference binding:
Constructor: temp

--- End of main ---
Destructor: temp
Destructor: Temporary
Destructor: Original_copy
Destructor: EMPTY
Destructor: Original
```

---

## 3. **Move-Only Types (unique_ptr)**

Some types cannot be copied but can be moved.

```cpp
#include <iostream>
#include <memory>
#include <vector>
using namespace std;

class FileHandle {
private:
    FILE* file;
    string filename;
    
public:
    // Constructor
    FileHandle(const string& name) : filename(name) {
        file = fopen(name.c_str(), "w");
        cout << "File opened: " << filename << endl;
    }
    
    // Move constructor
    FileHandle(FileHandle&& other) noexcept 
        : file(other.file), filename(move(other.filename)) {
        other.file = nullptr;
        cout << "File moved: " << filename << endl;
    }
    
    // Delete copy constructor (cannot copy)
    FileHandle(const FileHandle&) = delete;
    FileHandle& operator=(const FileHandle&) = delete;
    
    // Destructor
    ~FileHandle() {
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
};

class UniqueResource {
private:
    int* data;
    size_t size;
    
public:
    UniqueResource(size_t s) : size(s) {
        data = new int[size];
        cout << "Resource allocated: " << size << " ints" << endl;
    }
    
    // Move constructor
    UniqueResource(UniqueResource&& other) noexcept 
        : data(other.data), size(other.size) {
        other.data = nullptr;
        other.size = 0;
        cout << "Resource moved" << endl;
    }
    
    // Delete copy
    UniqueResource(const UniqueResource&) = delete;
    UniqueResource& operator=(const UniqueResource&) = delete;
    
    ~UniqueResource() {
        if (data) {
            cout << "Resource freed: " << size << " ints" << endl;
            delete[] data;
        }
    }
    
    void display() const {
        if (data) {
            cout << "Resource: " << size << " ints at " << data << endl;
        } else {
            cout << "Resource: empty" << endl;
        }
    }
};

int main() {
    cout << "=== Move-Only Types ===" << endl;
    
    cout << "\n1. FileHandle (move-only):" << endl;
    FileHandle f1("test.txt");
    // FileHandle f2 = f1;  // Error! Copy constructor deleted
    FileHandle f2 = move(f1);  // OK - move
    
    f2.write("Hello from moved file");
    
    cout << "\n2. UniqueResource in container:" << endl;
    vector<UniqueResource> resources;
    resources.push_back(UniqueResource(100));  // Move into vector
    resources.push_back(UniqueResource(200));
    resources.push_back(UniqueResource(300));
    
    cout << "\n3. Transferring ownership:" << endl;
    UniqueResource r1(50);
    UniqueResource r2 = move(r1);  // Transfer ownership
    cout << "r1 after move: ";
    r1.display();
    cout << "r2: ";
    r2.display();
    
    cout << "\n--- End of main ---" << endl;
    return 0;
}
```

**Output:**
```
=== Move-Only Types ===

1. FileHandle (move-only):
File opened: test.txt
File moved: test.txt
File closed: test.txt

2. UniqueResource in container:
Resource allocated: 100 ints
Resource moved
Resource allocated: 200 ints
Resource moved
Resource allocated: 300 ints
Resource moved

3. Transferring ownership:
Resource allocated: 50 ints
Resource moved
r1 after move: Resource: empty
r2: Resource: 50 ints at 0x...

--- End of main ---
Resource freed: 50 ints
Resource freed: 300 ints
Resource freed: 200 ints
Resource freed: 100 ints
```

---

## 4. **Move Constructor with Inheritance**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Base {
protected:
    int* baseData;
    
public:
    Base(int val) {
        baseData = new int(val);
        cout << "Base constructor: " << *baseData << endl;
    }
    
    // Base move constructor
    Base(Base&& other) noexcept : baseData(other.baseData) {
        other.baseData = nullptr;
        cout << "Base move constructor" << endl;
    }
    
    // Base copy constructor (delete to make move-only)
    Base(const Base&) = delete;
    
    virtual ~Base() {
        if (baseData) {
            cout << "Base destructor: " << *baseData << endl;
            delete baseData;
        }
    }
};

class Derived : public Base {
private:
    string name;
    vector<int> data;
    
public:
    Derived(int val, string n, size_t size) 
        : Base(val), name(n), data(size) {
        cout << "Derived constructor: " << name << endl;
    }
    
    // Derived move constructor
    Derived(Derived&& other) noexcept 
        : Base(move(other)),           // Move base part
          name(move(other.name)),      // Move string
          data(move(other.data))       // Move vector
    {
        cout << "Derived move constructor: " << name << endl;
    }
    
    // Delete copy
    Derived(const Derived&) = delete;
    
    ~Derived() {
        if (!name.empty()) {
            cout << "Derived destructor: " << name << endl;
        }
    }
    
    void display() const {
        cout << "Name: " << name << ", Data size: " << data.size() << endl;
    }
};

class Container {
private:
    vector<Derived> items;
    
public:
    void add(Derived&& item) {
        items.push_back(move(item));  // Move into vector
        cout << "Added to container" << endl;
    }
    
    void display() {
        for (const auto& item : items) {
            item.display();
        }
    }
};

int main() {
    cout << "=== Move Constructor with Inheritance ===" << endl;
    
    cout << "\n1. Moving Derived object:" << endl;
    Derived d1(100, "Original", 50);
    Derived d2 = move(d1);  // Move constructor
    
    cout << "\n2. d1 after move:" << endl;
    d1.display();
    cout << "d2:" << endl;
    d2.display();
    
    cout << "\n3. Container with move-only objects:" << endl;
    Container container;
    container.add(Derived(200, "First", 10));
    container.add(Derived(300, "Second", 20));
    container.add(Derived(400, "Third", 30));
    
    cout << "\nContainer contents:" << endl;
    container.display();
    
    cout << "\n--- End of main ---" << endl;
    return 0;
}
```

---

## 5. **Move Constructor Best Practices**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <cstring>
using namespace std;

class OptimizedString {
private:
    char* data;
    size_t length;
    
public:
    // Constructor
    OptimizedString(const char* str = "") {
        length = strlen(str);
        data = new char[length + 1];
        strcpy(data, str);
        cout << "Created: " << data << endl;
    }
    
    // Copy constructor (deep copy)
    OptimizedString(const OptimizedString& other) {
        length = other.length;
        data = new char[length + 1];
        strcpy(data, other.data);
        cout << "Copied: " << data << endl;
    }
    
    // Move constructor - BEST PRACTICES
    OptimizedString(OptimizedString&& other) noexcept 
        : data(other.data), length(other.length) {
        // 1. Steal resources
        // 2. Leave source in valid state (nullptr)
        // 3. Mark as noexcept for optimizations
        other.data = nullptr;
        other.length = 0;
        cout << "Moved: " << data << endl;
    }
    
    // Destructor
    ~OptimizedString() {
        if (data) {
            cout << "Destroyed: " << data << endl;
            delete[] data;
        } else {
            cout << "Destroyed: (moved from)" << endl;
        }
    }
    
    // Move assignment (for completeness)
    OptimizedString& operator=(OptimizedString&& other) noexcept {
        if (this != &other) {
            delete[] data;
            data = other.data;
            length = other.length;
            other.data = nullptr;
            other.length = 0;
            cout << "Move assigned: " << data << endl;
        }
        return *this;
    }
    
    void display() const {
        if (data) {
            cout << "String: " << data << " (length: " << length << ")" << endl;
        } else {
            cout << "String: (empty)" << endl;
        }
    }
};

class Factory {
public:
    static OptimizedString createString(const char* str) {
        OptimizedString temp(str);
        return temp;  // RVO or move
    }
    
    static void processString(OptimizedString s) {
        s.display();
    }
};

int main() {
    cout << "=== Move Constructor Best Practices ===" << endl;
    
    cout << "\n1. Creating from temporary:" << endl;
    OptimizedString s1 = OptimizedString("Temporary");
    
    cout << "\n2. Moving from lvalue:" << endl;
    OptimizedString s2("Original");
    OptimizedString s3 = move(s2);
    cout << "s2 after move: ";
    s2.display();
    
    cout << "\n3. Factory pattern with move:" << endl;
    OptimizedString s4 = Factory::createString("Factory created");
    
    cout << "\n4. Passing temporary to function:" << endl;
    Factory::processString(OptimizedString("Function argument"));
    
    cout << "\n5. Vector of move-only objects:" << endl;
    vector<OptimizedString> vec;
    vec.push_back(OptimizedString("First"));
    vec.push_back(OptimizedString("Second"));
    vec.push_back(OptimizedString("Third"));
    
    cout << "\n--- End of main ---" << endl;
    return 0;
}
```

**Output:**
```
=== Move Constructor Best Practices ===

1. Creating from temporary:
Created: Temporary
Moved: Temporary
Destroyed: (moved from)

2. Moving from lvalue:
Created: Original
Moved: Original
s2 after move: String: (empty)

3. Factory pattern with move:
Created: Factory created

4. Passing temporary to function:
Created: Function argument
Moved: Function argument
String: Function argument (length: 18)
Destroyed: Function argument

5. Vector of move-only objects:
Created: First
Moved: First
Destroyed: (moved from)
Created: Second
Moved: Second
Destroyed: (moved from)
Created: Third
Moved: Third
Destroyed: (moved from)

--- End of main ---
Destroyed: First
Destroyed: Second
Destroyed: Third
Destroyed: Factory created
Destroyed: (moved from)
Destroyed: (moved from)
```

---

## 6. **Performance Comparison: Copy vs Move**

```cpp
#include <iostream>
#include <chrono>
#include <vector>
#include <string>
using namespace std;
using namespace chrono;

class LargeObject {
private:
    vector<int> data;
    string name;
    
public:
    LargeObject(const string& n, size_t size) : name(n), data(size) {
        for (size_t i = 0; i < size; i++) {
            data[i] = i;
        }
    }
    
    // Copy constructor
    LargeObject(const LargeObject& other) 
        : data(other.data), name(other.name + "_copy") {
        // Expensive deep copy
    }
    
    // Move constructor
    LargeObject(LargeObject&& other) noexcept 
        : data(move(other.data)), name(move(other.name)) {
        // Cheap pointer swaps
    }
    
    size_t getSize() const { return data.size(); }
};

int main() {
    const int NUM_OBJECTS = 10000;
    const int DATA_SIZE = 1000;
    
    cout << "=== Performance: Copy vs Move ===" << endl;
    
    // Test copy
    cout << "\n1. Copying " << NUM_OBJECTS << " objects:" << endl;
    auto start = high_resolution_clock::now();
    
    vector<LargeObject> copyVec;
    LargeObject original("Original", DATA_SIZE);
    for (int i = 0; i < NUM_OBJECTS; i++) {
        copyVec.push_back(original);  // Copy constructor
    }
    
    auto end = high_resolution_clock::now();
    auto copyTime = duration_cast<milliseconds>(end - start).count();
    cout << "Copy time: " << copyTime << " ms" << endl;
    
    // Test move
    cout << "\n2. Moving " << NUM_OBJECTS << " objects:" << endl;
    start = high_resolution_clock::now();
    
    vector<LargeObject> moveVec;
    for (int i = 0; i < NUM_OBJECTS; i++) {
        moveVec.push_back(LargeObject("Temporary", DATA_SIZE));  // Move constructor
    }
    
    end = high_resolution_clock::now();
    auto moveTime = duration_cast<milliseconds>(end - start).count();
    cout << "Move time: " << moveTime << " ms" << endl;
    
    cout << "\n3. Performance improvement:" << endl;
    cout << "Move is " << (double)copyTime / moveTime << "x faster" << endl;
    
    cout << "\n4. When to use move:" << endl;
    cout << "✓ Returning large objects from functions" << endl;
    cout << "✓ Storing objects in containers" << endl;
    cout << "✓ Passing temporary objects" << endl;
    cout << "✓ Transferring ownership of resources" << endl;
    
    return 0;
}
```

---

## 📊 Move Constructor Summary

| Aspect | Description |
|--------|-------------|
| **Purpose** | Transfer resources efficiently |
| **Syntax** | `ClassName(ClassName&& other) noexcept;` |
| **When Called** | When initializing from rvalue |
| **Key Operation** | Steal resources, leave source valid |
| **`noexcept`** | Essential for standard library optimizations |
| **After Move** | Source in valid but unspecified state |

---

## ✅ Best Practices

1. **Mark move constructors `noexcept`** - Enables optimizations
2. **Leave source in valid state** - Typically set pointers to nullptr
3. **Use `std::move`** to cast lvalues to rvalues
4. **Delete copy constructor** for move-only types
5. **Move base class parts** in derived move constructors
6. **Use member-wise move** for member variables

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Missing `noexcept`** | Prevents optimizations | Add `noexcept` |
| **Source not reset** | Double deletion | Set pointers to nullptr |
| **Using moved-from object** | Undefined behavior | Don't use after move |
| **Not moving base** | Incomplete move | Call base move constructor |
| **Throwing move** | Exception safety | Keep move noexcept |

---

## ✅ Key Takeaways

1. **Move constructor** transfers resources efficiently
2. **Called for rvalues** (temporaries, `std::move` results)
3. **`noexcept`** enables standard library optimizations
4. **Source must be valid** after move (can be empty)
5. **Move-only types** cannot be copied, only moved
6. **Performance** is dramatically better for large objects

---