# Virtual Table (vtable) in C++ - Complete Guide

## 📖 Overview

The virtual table (vtable) is the implementation mechanism behind run-time polymorphism in C++. It is a lookup table of function pointers that enables dynamic dispatch of virtual functions. Understanding vtables helps in understanding the performance characteristics and memory layout of polymorphic classes.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **vtable** | Virtual table containing pointers to virtual functions |
| **vptr** | Virtual pointer in each object pointing to its class's vtable |
| **Dynamic Dispatch** | Function call resolved at runtime using vtable |
| **Static Binding** | Function call resolved at compile time (non-virtual) |
| **vtable Layout** | Order of virtual function pointers in the table |

---

## 1. **Basic vtable Concept**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Base {
public:
    virtual void func1() {
        cout << "Base::func1()" << endl;
    }
    
    virtual void func2() {
        cout << "Base::func2()" << endl;
    }
    
    void func3() {
        cout << "Base::func3() (non-virtual)" << endl;
    }
    
    virtual ~Base() {
        cout << "Base destructor" << endl;
    }
};

class Derived : public Base {
public:
    void func1() override {
        cout << "Derived::func1()" << endl;
    }
    
    virtual void func4() {
        cout << "Derived::func4()" << endl;
    }
    
    ~Derived() override {
        cout << "Derived destructor" << endl;
    }
};

int main() {
    cout << "=== Basic vtable Concept ===" << endl;
    
    Base b;
    Derived d;
    Base* ptr = &d;
    
    cout << "\n1. Object sizes:" << endl;
    cout << "Size of Base: " << sizeof(Base) << " bytes" << endl;
    cout << "Size of Derived: " << sizeof(Derived) << " bytes" << endl;
    cout << "Note: Each object has a vptr (virtual pointer) - 8 bytes on 64-bit" << endl;
    
    cout << "\n2. Virtual function calls (dynamic dispatch):" << endl;
    ptr->func1();  // Calls Derived::func1() via vtable
    ptr->func2();  // Calls Base::func2() via vtable
    
    cout << "\n3. Non-virtual function call (static binding):" << endl;
    ptr->func3();  // Calls Base::func3() directly
    
    cout << "\n4. Direct calls (no vtable):" << endl;
    d.func1();     // Calls Derived::func1()
    d.func2();     // Calls Base::func2()
    d.func4();     // Calls Derived::func4()
    
    return 0;
}
```

**Output:**
```
=== Basic vtable Concept ===

1. Object sizes:
Size of Base: 8 bytes
Size of Derived: 8 bytes
Note: Each object has a vptr (virtual pointer) - 8 bytes on 64-bit

2. Virtual function calls (dynamic dispatch):
Derived::func1()
Base::func2()

3. Non-virtual function call (static binding):
Base::func3() (non-virtual)

4. Direct calls (no vtable):
Derived::func1()
Base::func2()
Derived::func4()
Derived destructor
Base destructor
Base destructor
```

---

## 2. **vtable Layout Visualization**

```cpp
#include <iostream>
#include <string>
using namespace std;

class GrandParent {
public:
    virtual void a() { cout << "GrandParent::a()" << endl; }
    virtual void b() { cout << "GrandParent::b()" << endl; }
    virtual ~GrandParent() {}
};

class Parent : public GrandParent {
public:
    void a() override { cout << "Parent::a()" << endl; }
    virtual void c() { cout << "Parent::c()" << endl; }
};

class Child : public Parent {
public:
    void b() override { cout << "Child::b()" << endl; }
    void c() override { cout << "Child::c()" << endl; }
    virtual void d() { cout << "Child::d()" << endl; }
};

int main() {
    cout << "=== vtable Layout Visualization ===" << endl;
    
    GrandParent gp;
    Parent p;
    Child c;
    
    cout << "\n1. Object sizes:" << endl;
    cout << "GrandParent: " << sizeof(GrandParent) << " bytes" << endl;
    cout << "Parent: " << sizeof(Parent) << " bytes" << endl;
    cout << "Child: " << sizeof(Child) << " bytes" << endl;
    
    cout << "\n2. vtable layout for GrandParent:" << endl;
    cout << "   [0] -> GrandParent::a()" << endl;
    cout << "   [1] -> GrandParent::b()" << endl;
    cout << "   [2] -> GrandParent::~GrandParent()" << endl;
    
    cout << "\n3. vtable layout for Parent:" << endl;
    cout << "   [0] -> Parent::a()      (overridden)" << endl;
    cout << "   [1] -> GrandParent::b() (inherited)" << endl;
    cout << "   [2] -> Parent::~Parent()" << endl;
    cout << "   [3] -> Parent::c()      (new virtual function)" << endl;
    
    cout << "\n4. vtable layout for Child:" << endl;
    cout << "   [0] -> Parent::a()      (inherited override)" << endl;
    cout << "   [1] -> Child::b()       (overridden)" << endl;
    cout << "   [2] -> Child::~Child()" << endl;
    cout << "   [3] -> Child::c()       (overridden)" << endl;
    cout << "   [4] -> Child::d()       (new virtual function)" << endl;
    
    cout << "\n5. Dynamic dispatch demonstration:" << endl;
    GrandParent* ptr = &c;
    ptr->a();  // Calls Child::a() (via Parent's override)
    ptr->b();  // Calls Child::b()
    
    return 0;
}
```

---

## 3. **Multiple Inheritance vtable**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Base1 {
public:
    virtual void f1() { cout << "Base1::f1()" << endl; }
    virtual void f2() { cout << "Base1::f2()" << endl; }
    virtual ~Base1() {}
};

class Base2 {
public:
    virtual void g1() { cout << "Base2::g1()" << endl; }
    virtual void g2() { cout << "Base2::g2()" << endl; }
    virtual ~Base2() {}
};

class Derived : public Base1, public Base2 {
public:
    void f1() override { cout << "Derived::f1()" << endl; }
    void g2() override { cout << "Derived::g2()" << endl; }
    virtual void h1() { cout << "Derived::h1()" << endl; }
};

int main() {
    cout << "=== Multiple Inheritance vtable ===" << endl;
    
    Derived d;
    Base1* b1 = &d;
    Base2* b2 = &d;
    
    cout << "\n1. Object size:" << endl;
    cout << "Size of Derived: " << sizeof(Derived) << " bytes" << endl;
    cout << "Note: Multiple vtables for multiple base classes" << endl;
    
    cout << "\n2. Calling through Base1 pointer:" << endl;
    b1->f1();  // Derived::f1()
    b1->f2();  // Base1::f2()
    
    cout << "\n3. Calling through Base2 pointer:" << endl;
    b2->g1();  // Base2::g1()
    b2->g2();  // Derived::g2()
    
    cout << "\n4. Address of objects:" << endl;
    cout << "Derived object address: " << &d << endl;
    cout << "As Base1: " << b1 << endl;
    cout << "As Base2: " << b2 << endl;
    cout << "Note: Different addresses for different base class views" << endl;
    
    return 0;
}
```

---

## 4. **Virtual Inheritance vtable**

```cpp
#include <iostream>
#include <string>
using namespace std;

class GrandParent {
public:
    virtual void a() { cout << "GrandParent::a()" << endl; }
    virtual void b() { cout << "GrandParent::b()" << endl; }
    virtual ~GrandParent() {}
};

class Parent1 : virtual public GrandParent {
public:
    virtual void c() { cout << "Parent1::c()" << endl; }
};

class Parent2 : virtual public GrandParent {
public:
    virtual void d() { cout << "Parent2::d()" << endl; }
};

class Child : public Parent1, public Parent2 {
public:
    void a() override { cout << "Child::a()" << endl; }
    virtual void e() { cout << "Child::e()" << endl; }
};

int main() {
    cout << "=== Virtual Inheritance vtable ===" << endl;
    
    Child c;
    GrandParent* gp = &c;
    Parent1* p1 = &c;
    Parent2* p2 = &c;
    
    cout << "\n1. Object sizes:" << endl;
    cout << "GrandParent: " << sizeof(GrandParent) << " bytes" << endl;
    cout << "Parent1: " << sizeof(Parent1) << " bytes" << endl;
    cout << "Parent2: " << sizeof(Parent2) << " bytes" << endl;
    cout << "Child: " << sizeof(Child) << " bytes" << endl;
    cout << "Note: Virtual inheritance adds extra pointers" << endl;
    
    cout << "\n2. Virtual function calls:" << endl;
    gp->a();  // Child::a()
    gp->b();  // GrandParent::b()
    
    cout << "\n3. Calls through Parent1:" << endl;
    p1->a();  // Child::a()
    p1->c();  // Parent1::c()
    
    cout << "\n4. Calls through Parent2:" << endl;
    p2->a();  // Child::a()
    p2->d();  // Parent2::d()
    
    return 0;
}
```

---

## 5. **Performance Implications**

```cpp
#include <iostream>
#include <chrono>
#include <vector>
#include <memory>
using namespace std;
using namespace chrono;

class Base {
public:
    virtual void virtualFunc() {
        // Do nothing
    }
    
    void nonVirtualFunc() {
        // Do nothing
    }
    
    virtual ~Base() = default;
};

class Derived : public Base {
public:
    void virtualFunc() override {
        // Do nothing
    }
};

int main() {
    cout << "=== Performance Implications ===" << endl;
    
    const int ITERATIONS = 100000000;
    Base base;
    Derived derived;
    Base* ptr = &derived;
    
    // Test non-virtual function call
    auto start = high_resolution_clock::now();
    for (int i = 0; i < ITERATIONS; i++) {
        base.nonVirtualFunc();
    }
    auto end = high_resolution_clock::now();
    auto nonVirtualTime = duration_cast<milliseconds>(end - start).count();
    
    // Test virtual function call (static binding)
    start = high_resolution_clock::now();
    for (int i = 0; i < ITERATIONS; i++) {
        derived.virtualFunc();
    }
    end = high_resolution_clock::now();
    auto staticVirtualTime = duration_cast<milliseconds>(end - start).count();
    
    // Test virtual function call (dynamic dispatch)
    start = high_resolution_clock::now();
    for (int i = 0; i < ITERATIONS; i++) {
        ptr->virtualFunc();
    }
    end = high_resolution_clock::now();
    auto dynamicVirtualTime = duration_cast<milliseconds>(end - start).count();
    
    cout << "\nPerformance for " << ITERATIONS << " iterations:" << endl;
    cout << "Non-virtual function:    " << nonVirtualTime << " ms" << endl;
    cout << "Virtual (static binding): " << staticVirtualTime << " ms" << endl;
    cout << "Virtual (dynamic):       " << dynamicVirtualTime << " ms" << endl;
    
    cout << "\nOverhead of virtual dispatch:" << endl;
    cout << "  vtable lookup: 1-2 extra memory accesses" << endl;
    cout << "  Indirect call: prevents inlining" << endl;
    cout << "  Branch prediction: may be less accurate" << endl;
    
    cout << "\nMemory overhead:" << endl;
    cout << "  Each polymorphic object: +8 bytes (vptr)" << endl;
    cout << "  Each class: +1 vtable (shared across objects)" << endl;
    
    return 0;
}
```

---

## 6. **Practical Example: Plugin System with vtables**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <map>
using namespace std;

// Plugin interface - vtables enable polymorphism
class IPlugin {
protected:
    string name;
    string version;
    
public:
    IPlugin(string n, string v) : name(n), version(v) {}
    
    // Virtual functions - will be in vtable
    virtual bool initialize() = 0;
    virtual void execute() = 0;
    virtual void shutdown() = 0;
    virtual string getDescription() const = 0;
    
    // Non-virtual functions - not in vtable
    string getName() const { return name; }
    string getVersion() const { return version; }
    
    virtual ~IPlugin() = default;
};

// Logger plugin
class LoggerPlugin : public IPlugin {
private:
    bool active;
    int logCount;
    
public:
    LoggerPlugin() : IPlugin("Logger", "1.0"), active(false), logCount(0) {}
    
    bool initialize() override {
        active = true;
        cout << "  LoggerPlugin::initialize() via vtable" << endl;
        return true;
    }
    
    void execute() override {
        if (active) {
            logCount++;
            cout << "  LoggerPlugin::execute() - log #" << logCount << endl;
        }
    }
    
    void shutdown() override {
        if (active) {
            cout << "  LoggerPlugin::shutdown() - " << logCount << " logs written" << endl;
            active = false;
        }
    }
    
    string getDescription() const override {
        return "Logs messages to console";
    }
};

// Data processor plugin
class DataProcessor : public IPlugin {
private:
    int processedCount;
    
public:
    DataProcessor() : IPlugin("DataProcessor", "2.1"), processedCount(0) {}
    
    bool initialize() override {
        cout << "  DataProcessor::initialize() via vtable" << endl;
        return true;
    }
    
    void execute() override {
        processedCount++;
        cout << "  DataProcessor::execute() - processed " << processedCount << " items" << endl;
    }
    
    void shutdown() override {
        cout << "  DataProcessor::shutdown() - total " << processedCount << " items" << endl;
    }
    
    string getDescription() const override {
        return "Processes data streams";
    }
};

// Security plugin
class SecurityPlugin : public IPlugin {
private:
    bool armed;
    
public:
    SecurityPlugin() : IPlugin("Security", "1.5"), armed(false) {}
    
    bool initialize() override {
        armed = true;
        cout << "  SecurityPlugin::initialize() via vtable" << endl;
        return true;
    }
    
    void execute() override {
        if (armed) {
            cout << "  SecurityPlugin::execute() - security check performed" << endl;
        }
    }
    
    void shutdown() override {
        if (armed) {
            cout << "  SecurityPlugin::shutdown() - system disarmed" << endl;
            armed = false;
        }
    }
    
    string getDescription() const override {
        return "Provides security monitoring";
    }
};

class PluginManager {
private:
    vector<unique_ptr<IPlugin>> plugins;
    map<string, IPlugin*> pluginMap;
    
public:
    void registerPlugin(IPlugin* plugin) {
        plugins.emplace_back(plugin);
        pluginMap[plugin->getName()] = plugin;
        cout << "Registered: " << plugin->getName() << " v" << plugin->getVersion() << endl;
    }
    
    void initializeAll() {
        cout << "\n=== Initializing Plugins (vtable dispatch) ===" << endl;
        for (auto& plugin : plugins) {
            plugin->initialize();  // vtable call
        }
    }
    
    void executeAll() {
        cout << "\n=== Executing Plugins (vtable dispatch) ===" << endl;
        for (auto& plugin : plugins) {
            plugin->execute();  // vtable call
        }
    }
    
    void shutdownAll() {
        cout << "\n=== Shutting Down Plugins (vtable dispatch) ===" << endl;
        for (auto& plugin : plugins) {
            plugin->shutdown();  // vtable call
        }
    }
    
    void showInfo() const {
        cout << "\n=== Plugin Information ===" << endl;
        for (const auto& plugin : plugins) {
            // Non-virtual calls - no vtable overhead
            cout << "  " << plugin->getName() << " v" << plugin->getVersion() << endl;
            cout << "    " << plugin->getDescription() << endl;
        }
    }
};

int main() {
    cout << "=== Plugin System with vtables ===" << endl;
    cout << "\nUnderstanding how vtables enable plugins:" << endl;
    cout << "  - IPlugin defines virtual functions in vtable" << endl;
    cout << "  - Each plugin provides its own implementation" << endl;
    cout << "  - PluginManager calls via base class pointers" << endl;
    cout << "  - vtable ensures correct function is called" << endl;
    
    PluginManager manager;
    
    cout << "\n1. Registering plugins:" << endl;
    manager.registerPlugin(new LoggerPlugin());
    manager.registerPlugin(new DataProcessor());
    manager.registerPlugin(new SecurityPlugin());
    
    manager.showInfo();
    
    cout << "\n2. Plugin lifecycle (vtable in action):" << endl;
    manager.initializeAll();
    manager.executeAll();
    manager.executeAll();  // Second execution
    manager.shutdownAll();
    
    return 0;
}
```

---

## 📊 vtable Summary

| Aspect | Description |
|--------|-------------|
| **vtable** | Table of function pointers for virtual functions |
| **vptr** | Pointer in each object pointing to its class's vtable |
| **Memory Overhead** | +8 bytes per object (vptr) + one vtable per class |
| **Performance** | Indirect call (1-2 extra memory accesses) |
| **Multiple Inheritance** | Multiple vtables (one per base class) |
| **Virtual Inheritance** | Additional pointers for shared base |

---

## ✅ Key Takeaways

1. **vtable** is the implementation mechanism for virtual functions
2. **vptr** in each object points to the class's vtable
3. **Dynamic dispatch**: object->vptr[index]()
4. **Memory overhead**: vptr per object, vtable per class
5. **Performance**: Indirect call prevents inlining
6. **Multiple inheritance**: Multiple vtables
7. **Virtual inheritance**: Additional pointer overhead

---
---

## Next Step

- Go to [07_Run_Time_Type_Information.md](07_Run_Time_Type_Information.md) to continue with Run Time Type Information.
