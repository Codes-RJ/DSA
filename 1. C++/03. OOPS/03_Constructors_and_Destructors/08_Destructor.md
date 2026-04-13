# Destructor in C++ - Complete Guide

## 📖 Overview

A destructor is a special member function that is automatically called when an object goes out of scope or is explicitly deleted. Its primary purpose is to release resources acquired during the object's lifetime, preventing memory leaks and resource exhaustion. Understanding destructors is essential for proper resource management.

---

## 🎯 Key Concepts

| Aspect | Description |
|--------|-------------|
| **Purpose** | Release resources, clean up memory |
| **Syntax** | `~ClassName();` |
| **Name** | Tilde (~) followed by class name |
| **Parameters** | None |
| **Return Type** | None (no return value) |
| **Overloading** | Cannot be overloaded (only one destructor per class) |

---

## 1. **Basic Destructor**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Simple {
private:
    string name;
    static int count;
    
public:
    Simple(string n) : name(n) {
        count++;
        cout << "Constructor: " << name << " (Object #" << count << ")" << endl;
    }
    
    ~Simple() {
        cout << "Destructor: " << name << " (Object #" << count << ")" << endl;
        count--;
    }
    
    void display() const {
        cout << "Object: " << name << endl;
    }
};

int Simple::count = 0;

class Resource {
private:
    int* data;
    size_t size;
    
public:
    Resource(size_t s) : size(s) {
        data = new int[size];
        cout << "Resource allocated: " << size << " ints" << endl;
    }
    
    ~Resource() {
        delete[] data;
        cout << "Resource freed: " << size << " ints" << endl;
    }
};

int main() {
    cout << "=== Basic Destructor Demo ===" << endl;
    
    cout << "\n1. Simple class:" << endl;
    {
        Simple s1("First");
        Simple s2("Second");
        s1.display();
        s2.display();
    }  // Destructors called here
    
    cout << "\n2. Resource class:" << endl;
    {
        Resource r1(100);
        Resource r2(200);
    }  // Destructors called here
    
    cout << "\n--- End of main ---" << endl;
    return 0;
}
```

**Output:**
```
=== Basic Destructor Demo ===

1. Simple class:
Constructor: First (Object #1)
Constructor: Second (Object #2)
Object: First
Object: Second
Destructor: Second (Object #2)
Destructor: First (Object #1)

2. Resource class:
Resource allocated: 100 ints
Resource allocated: 200 ints
Resource freed: 200 ints
Resource freed: 100 ints

--- End of main ---
```

---

## 2. **Destructor Order (Stack Unwinding)**

```cpp
#include <iostream>
#include <string>
using namespace std;

class OrderDemo {
private:
    string name;
    static int depth;
    
public:
    OrderDemo(string n) : name(n) {
        depth++;
        cout << string(depth * 2, ' ') << "Constructor: " << name << " (depth=" << depth << ")" << endl;
    }
    
    ~OrderDemo() {
        cout << string(depth * 2, ' ') << "Destructor: " << name << " (depth=" << depth << ")" << endl;
        depth--;
    }
};

int OrderDemo::depth = 0;

class Base {
public:
    Base() { cout << "  Base constructor" << endl; }
    ~Base() { cout << "  Base destructor" << endl; }
};

class Member {
public:
    Member() { cout << "    Member constructor" << endl; }
    ~Member() { cout << "    Member destructor" << endl; }
};

class Derived : public Base {
private:
    Member m;
    
public:
    Derived() { cout << "  Derived constructor" << endl; }
    ~Derived() { cout << "  Derived destructor" << endl; }
};

int main() {
    cout << "=== Destructor Order (Stack Unwinding) ===" << endl;
    
    cout << "\n1. Multiple objects in nested scopes:" << endl;
    {
        OrderDemo a("A");
        {
            OrderDemo b("B");
            {
                OrderDemo c("C");
            }  // c destructed here
        }  // b destructed here
    }  // a destructed here
    
    cout << "\n2. Inheritance and composition order:" << endl;
    {
        Derived d;
    }  // Destructors called in reverse order
    
    cout << "\nDestruction order is always REVERSE of construction order!" << endl;
    
    return 0;
}
```

**Output:**
```
=== Destructor Order (Stack Unwinding) ===

1. Multiple objects in nested scopes:
  Constructor: A (depth=1)
    Constructor: B (depth=2)
      Constructor: C (depth=3)
      Destructor: C (depth=3)
    Destructor: B (depth=2)
  Destructor: A (depth=1)

2. Inheritance and composition order:
  Base constructor
    Member constructor
  Derived constructor
  Derived destructor
    Member destructor
  Base destructor

Destruction order is always REVERSE of construction order!
```

---

## 3. **Dynamic Memory Management**

```cpp
#include <iostream>
#include <cstring>
using namespace std;

class String {
private:
    char* data;
    size_t length;
    
public:
    // Constructor
    String(const char* str = "") {
        length = strlen(str);
        data = new char[length + 1];
        strcpy(data, str);
        cout << "Created: \"" << data << "\" (length=" << length << ")" << endl;
    }
    
    // Copy constructor (deep copy)
    String(const String& other) {
        length = other.length;
        data = new char[length + 1];
        strcpy(data, other.data);
        cout << "Copied: \"" << data << "\"" << endl;
    }
    
    // Destructor
    ~String() {
        if (data) {
            cout << "Destroyed: \"" << data << "\"" << endl;
            delete[] data;
            data = nullptr;
        }
    }
    
    void display() const {
        cout << "String: \"" << data << "\" (length=" << length << ")" << endl;
    }
    
    void setChar(size_t index, char c) {
        if (index < length) {
            data[index] = c;
        }
    }
};

class Array {
private:
    int* data;
    size_t size;
    
public:
    Array(size_t s) : size(s) {
        data = new int[size];
        for (size_t i = 0; i < size; i++) {
            data[i] = i;
        }
        cout << "Array created: " << size << " elements" << endl;
    }
    
    ~Array() {
        cout << "Array destroyed: " << size << " elements" << endl;
        delete[] data;
    }
    
    void display() const {
        cout << "Array: ";
        for (size_t i = 0; i < size; i++) {
            cout << data[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    cout << "=== Dynamic Memory Management ===" << endl;
    
    cout << "\n1. String class with dynamic memory:" << endl;
    String s1("Hello");
    String s2 = s1;  // Copy constructor - deep copy
    s1.display();
    s2.display();
    
    cout << "\n2. Modifying original:" << endl;
    s1.setChar(0, 'J');
    cout << "s1 after modification: ";
    s1.display();
    cout << "s2 unchanged: ";
    s2.display();
    
    cout << "\n3. Array class:" << endl;
    {
        Array a1(10);
        Array a2(20);
        a1.display();
        a2.display();
    }  // Destructors called here
    
    cout << "\n--- End of main ---" << endl;
    return 0;
}
```

---

## 4. **Destructor and Exception Safety**

```cpp
#include <iostream>
#include <string>
#include <stdexcept>
using namespace std;

class FileHandler {
private:
    string filename;
    FILE* file;
    
public:
    FileHandler(const string& name) : filename(name), file(nullptr) {
        file = fopen(name.c_str(), "w");
        if (!file) {
            throw runtime_error("Cannot open file: " + name);
        }
        cout << "File opened: " << filename << endl;
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
};

class DatabaseConnection {
private:
    string connectionString;
    bool connected;
    
public:
    DatabaseConnection(const string& conn) : connectionString(conn), connected(false) {
        // Simulate connection
        connected = true;
        cout << "Database connected: " << connectionString << endl;
    }
    
    ~DatabaseConnection() {
        if (connected) {
            cout << "Database disconnected: " << connectionString << endl;
        }
    }
    
    void query(const string& sql) {
        if (!connected) {
            throw runtime_error("Not connected to database");
        }
        cout << "Executing: " << sql << endl;
    }
};

class Transaction {
private:
    bool active;
    
public:
    Transaction() : active(true) {
        cout << "Transaction started" << endl;
    }
    
    ~Transaction() {
        if (active) {
            cout << "Transaction rolled back (destructor cleanup)" << endl;
        }
    }
    
    void commit() {
        if (active) {
            cout << "Transaction committed" << endl;
            active = false;
        }
    }
    
    void rollback() {
        if (active) {
            cout << "Transaction rolled back" << endl;
            active = false;
        }
    }
};

void riskyOperation(bool shouldThrow) {
    FileHandler file("data.txt");
    DatabaseConnection db("localhost:5432");
    Transaction tx;
    
    file.write("Starting operation");
    db.query("BEGIN");
    
    if (shouldThrow) {
        throw runtime_error("Operation failed!");
    }
    
    db.query("COMMIT");
    tx.commit();
    file.write("Operation completed");
}

int main() {
    cout << "=== Destructor and Exception Safety ===" << endl;
    
    cout << "\n1. Successful operation (no exception):" << endl;
    try {
        riskyOperation(false);
    } catch (const exception& e) {
        cout << "Caught: " << e.what() << endl;
    }
    
    cout << "\n2. Failed operation (exception thrown):" << endl;
    try {
        riskyOperation(true);
    } catch (const exception& e) {
        cout << "Caught: " << e.what() << endl;
    }
    
    cout << "\nRAII ensures resources are released even when exceptions occur!" << endl;
    
    return 0;
}
```

---

## 5. **Virtual Destructor**

```cpp
#include <iostream>
#include <vector>
#include <memory>
using namespace std;

class Base {
private:
    int* data;
    
public:
    Base() {
        data = new int(42);
        cout << "Base constructor: allocated " << *data << endl;
    }
    
    // Non-virtual destructor - PROBLEM!
    ~Base() {
        cout << "Base destructor: freeing " << *data << endl;
        delete data;
    }
};

class Derived : public Base {
private:
    int* moreData;
    
public:
    Derived() : Base() {
        moreData = new int(100);
        cout << "Derived constructor: allocated " << *moreData << endl;
    }
    
    ~Derived() {
        cout << "Derived destructor: freeing " << *moreData << endl;
        delete moreData;
    }
};

class VirtualBase {
private:
    int* data;
    
public:
    VirtualBase() {
        data = new int(42);
        cout << "VirtualBase constructor: allocated " << *data << endl;
    }
    
    // Virtual destructor - CORRECT!
    virtual ~VirtualBase() {
        cout << "VirtualBase destructor: freeing " << *data << endl;
        delete data;
    }
};

class VirtualDerived : public VirtualBase {
private:
    int* moreData;
    
public:
    VirtualDerived() : VirtualBase() {
        moreData = new int(100);
        cout << "VirtualDerived constructor: allocated " << *moreData << endl;
    }
    
    ~VirtualDerived() override {
        cout << "VirtualDerived destructor: freeing " << *moreData << endl;
        delete moreData;
    }
};

int main() {
    cout << "=== Virtual Destructor Demo ===" << endl;
    
    cout << "\n1. INCORRECT: Non-virtual destructor (memory leak!):" << endl;
    Base* ptr1 = new Derived();
    delete ptr1;  // Only Base destructor called! Derived destructor skipped!
    cout << "Memory leak! Derived destructor not called!" << endl;
    
    cout << "\n2. CORRECT: Virtual destructor:" << endl;
    VirtualBase* ptr2 = new VirtualDerived();
    delete ptr2;  // Both destructors called correctly
    
    cout << "\n3. Smart pointers automatically handle this:" << endl;
    {
        unique_ptr<VirtualBase> ptr3 = make_unique<VirtualDerived>();
        // Automatically calls correct destructor
    }
    
    cout << "\nRule: Always make base class destructor virtual!" << endl;
    
    return 0;
}
```

---

## 6. **Practical Example: Smart Pointer Simulation**

```cpp
#include <iostream>
#include <cassert>
using namespace std;

template<typename T>
class SimpleSmartPtr {
private:
    T* ptr;
    int* refCount;
    
public:
    // Constructor
    SimpleSmartPtr(T* p = nullptr) : ptr(p) {
        refCount = new int(1);
        cout << "SmartPtr created, refCount=" << *refCount << endl;
    }
    
    // Copy constructor
    SimpleSmartPtr(const SimpleSmartPtr& other) : ptr(other.ptr), refCount(other.refCount) {
        (*refCount)++;
        cout << "SmartPtr copied, refCount=" << *refCount << endl;
    }
    
    // Destructor
    ~SimpleSmartPtr() {
        (*refCount)--;
        cout << "SmartPtr destroyed, refCount=" << *refCount << endl;
        
        if (*refCount == 0) {
            cout << "Deleting resource" << endl;
            delete ptr;
            delete refCount;
        }
    }
    
    T* operator->() { return ptr; }
    T& operator*() { return *ptr; }
};

class Resource {
private:
    string name;
    static int count;
    
public:
    Resource(string n) : name(n) {
        count++;
        cout << "Resource created: " << name << " (total=" << count << ")" << endl;
    }
    
    ~Resource() {
        cout << "Resource destroyed: " << name << " (remaining=" << --count << ")" << endl;
    }
    
    void use() {
        cout << "Using resource: " << name << endl;
    }
};

int Resource::count = 0;

class Connection {
private:
    int id;
    bool connected;
    static int nextId;
    
public:
    Connection() : id(nextId++), connected(false) {
        cout << "Connection object created (ID=" << id << ")" << endl;
    }
    
    ~Connection() {
        if (connected) {
            disconnect();
        }
        cout << "Connection object destroyed (ID=" << id << ")" << endl;
    }
    
    void connect() {
        if (!connected) {
            connected = true;
            cout << "Connection " << id << " established" << endl;
        }
    }
    
    void disconnect() {
        if (connected) {
            connected = false;
            cout << "Connection " << id << " closed" << endl;
        }
    }
    
    void send(const string& data) {
        if (connected) {
            cout << "Connection " << id << " sending: " << data << endl;
        }
    }
};

int Connection::nextId = 1;

int main() {
    cout << "=== Practical Example: Smart Pointer Simulation ===" << endl;
    
    cout << "\n1. SimpleSmartPtr with Resource:" << endl;
    {
        SimpleSmartPtr<Resource> ptr1(new Resource("Resource1"));
        {
            SimpleSmartPtr<Resource> ptr2 = ptr1;  // Copy - refCount increases
            ptr2->use();
        }  // ptr2 destroyed - refCount decreases
        ptr1->use();
    }  // ptr1 destroyed - refCount becomes 0, resource deleted
    
    cout << "\n2. Connection management with destructor cleanup:" << endl;
    {
        Connection conn1;
        conn1.connect();
        conn1.send("Hello");
        
        {
            Connection conn2;
            conn2.connect();
            conn2.send("World");
        }  // conn2 destructor automatically disconnects
        
        conn1.send("Goodbye");
    }  // conn1 destructor automatically disconnects
    
    return 0;
}
```

---

## 📊 Destructor Summary

| Aspect | Description |
|--------|-------------|
| **Purpose** | Release resources, clean up |
| **Name** | `~ClassName()` |
| **Parameters** | None |
| **Overloading** | Not allowed (only one) |
| **Order** | Reverse of construction |
| **Virtual** | Essential for polymorphic base classes |

---

## ✅ Best Practices

1. **Always release resources** acquired in constructor
2. **Make destructors virtual** for polymorphic base classes
3. **Follow RAII** (Resource Acquisition Is Initialization)
4. **Never throw exceptions** from destructors
5. **Set pointers to nullptr** after deletion
6. **Use smart pointers** instead of manual resource management

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Non-virtual destructor** | Memory leak in polymorphism | Make base destructor virtual |
| **Throwing in destructor** | Program termination | Log errors, don't throw |
| **Double deletion** | Undefined behavior | Set pointers to nullptr |
| **Forgetting to delete** | Memory leak | Use RAII, smart pointers |
| **Accessing deleted objects** | Use-after-free | Clear references after delete |

---

## ✅ Key Takeaways

1. **Destructors** clean up resources automatically
2. **Called in reverse order** of construction
3. **RAII** ensures resources are released
4. **Virtual destructors** essential for polymorphism
5. **Never throw** from destructors
6. **Smart pointers** automate resource management

---
---

## Next Step

- Go to [09_Virtual_Destructor.md](09_Virtual_Destructor.md) to continue with Virtual Destructor.
