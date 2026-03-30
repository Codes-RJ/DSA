# Virtual Destructor in C++ - Complete Guide

## 📖 Overview

A virtual destructor ensures that when a derived object is deleted through a base class pointer, the correct destructor chain is called. Without a virtual destructor, only the base class destructor executes, leading to resource leaks and undefined behavior. Virtual destructors are essential for polymorphic class hierarchies.

---

## 🎯 Key Concepts

| Aspect | Description |
|--------|-------------|
| **Purpose** | Ensure proper cleanup in polymorphic hierarchies |
| **Syntax** | `virtual ~ClassName();` |
| **When Needed** | When class has virtual functions (polymorphic) |
| **Cost** | Adds vptr (virtual pointer) overhead |
| **Rule** | If class has virtual functions, make destructor virtual |

---

## 1. **Problem: Non-Virtual Destructor**

```cpp
#include <iostream>
#include <string>
#include <memory>
using namespace std;

// Base class with non-virtual destructor (WRONG!)
class BaseWrong {
private:
    int* baseData;
    
public:
    BaseWrong() {
        baseData = new int(42);
        cout << "BaseWrong constructor: allocated " << *baseData << endl;
    }
    
    // Non-virtual destructor - PROBLEM!
    ~BaseWrong() {
        cout << "BaseWrong destructor: freeing " << *baseData << endl;
        delete baseData;
    }
    
    virtual void display() const {
        cout << "BaseWrong: value=" << *baseData << endl;
    }
};

class DerivedWrong : public BaseWrong {
private:
    int* derivedData;
    
public:
    DerivedWrong() : BaseWrong() {
        derivedData = new int(100);
        cout << "DerivedWrong constructor: allocated " << *derivedData << endl;
    }
    
    ~DerivedWrong() {
        cout << "DerivedWrong destructor: freeing " << *derivedData << endl;
        delete derivedData;
    }
    
    void display() const override {
        BaseWrong::display();
        cout << "DerivedWrong: extra=" << *derivedData << endl;
    }
};

// Base class with virtual destructor (CORRECT!)
class BaseCorrect {
private:
    int* baseData;
    
public:
    BaseCorrect() {
        baseData = new int(42);
        cout << "BaseCorrect constructor: allocated " << *baseData << endl;
    }
    
    // Virtual destructor - CORRECT!
    virtual ~BaseCorrect() {
        cout << "BaseCorrect destructor: freeing " << *baseData << endl;
        delete baseData;
    }
    
    virtual void display() const {
        cout << "BaseCorrect: value=" << *baseData << endl;
    }
};

class DerivedCorrect : public BaseCorrect {
private:
    int* derivedData;
    
public:
    DerivedCorrect() : BaseCorrect() {
        derivedData = new int(100);
        cout << "DerivedCorrect constructor: allocated " << *derivedData << endl;
    }
    
    ~DerivedCorrect() override {
        cout << "DerivedCorrect destructor: freeing " << *derivedData << endl;
        delete derivedData;
    }
    
    void display() const override {
        BaseCorrect::display();
        cout << "DerivedCorrect: extra=" << *derivedData << endl;
    }
};

int main() {
    cout << "=== Non-Virtual Destructor Problem ===" << endl;
    
    cout << "\n1. CORRECT: Deleting derived object through base pointer:" << endl;
    cout << "   (Will call both destructors)" << endl;
    BaseCorrect* ptr1 = new DerivedCorrect();
    delete ptr1;  // Both destructors called correctly
    
    cout << "\n2. INCORRECT: Non-virtual destructor - MEMORY LEAK!" << endl;
    cout << "   (Only base destructor called, derived destructor skipped)" << endl;
    BaseWrong* ptr2 = new DerivedWrong();
    delete ptr2;  // Only BaseWrong destructor called! Memory leak!
    
    cout << "\n3. Demonstrating the leak:" << endl;
    cout << "   DerivedWrong destructor never called!" << endl;
    cout << "   derivedData memory is leaked!" << endl;
    
    cout << "\nRule: Always make destructor virtual in polymorphic base classes!" << endl;
    
    return 0;
}
```

**Output:**
```
=== Non-Virtual Destructor Problem ===

1. CORRECT: Deleting derived object through base pointer:
   (Will call both destructors)
BaseCorrect constructor: allocated 42
DerivedCorrect constructor: allocated 100
DerivedCorrect destructor: freeing 100
BaseCorrect destructor: freeing 42

2. INCORRECT: Non-virtual destructor - MEMORY LEAK!
   (Only base destructor called, derived destructor skipped)
BaseWrong constructor: allocated 42
DerivedWrong constructor: allocated 100
BaseWrong destructor: freeing 42

3. Demonstrating the leak:
   DerivedWrong destructor never called!
   derivedData memory is leaked!

Rule: Always make destructor virtual in polymorphic base classes!
```

---

## 2. **When to Use Virtual Destructors**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Interface/Abstract class - MUST have virtual destructor
class IShape {
public:
    virtual double area() const = 0;
    virtual void draw() const = 0;
    
    // Virtual destructor essential for interface
    virtual ~IShape() {
        cout << "IShape destructor" << endl;
    }
};

class Circle : public IShape {
private:
    double radius;
    int* cache;  // Some resource
    
public:
    Circle(double r) : radius(r) {
        cache = new int(42);
        cout << "Circle created: radius=" << radius << endl;
    }
    
    ~Circle() override {
        cout << "Circle destroyed: radius=" << radius << endl;
        delete cache;
    }
    
    double area() const override {
        return 3.14159 * radius * radius;
    }
    
    void draw() const override {
        cout << "Drawing circle with radius " << radius << endl;
    }
};

// Base class with virtual functions - needs virtual destructor
class Animal {
protected:
    string name;
    
public:
    Animal(string n) : name(n) {
        cout << "Animal constructor: " << name << endl;
    }
    
    virtual void speak() const {
        cout << name << " makes a sound" << endl;
    }
    
    // Virtual destructor because class has virtual functions
    virtual ~Animal() {
        cout << "Animal destructor: " << name << endl;
    }
};

class Dog : public Animal {
private:
    int* toyCount;  // Resource
    
public:
    Dog(string n) : Animal(n) {
        toyCount = new int(5);
        cout << "Dog constructor: " << name << " has " << *toyCount << " toys" << endl;
    }
    
    ~Dog() override {
        cout << "Dog destructor: " << name << " deleting toys" << endl;
        delete toyCount;
    }
    
    void speak() const override {
        cout << name << " barks: Woof!" << endl;
    }
};

// Class with no virtual functions - virtual destructor optional
class Point {
private:
    int x, y;
    
public:
    Point(int xVal, int yVal) : x(xVal), y(yVal) {
        cout << "Point created: (" << x << ", " << y << ")" << endl;
    }
    
    // No virtual functions, virtual destructor not needed
    ~Point() {
        cout << "Point destroyed: (" << x << ", " << y << ")" << endl;
    }
    
    void display() const {
        cout << "(" << x << ", " << y << ")" << endl;
    }
};

int main() {
    cout << "=== When to Use Virtual Destructors ===" << endl;
    
    cout << "\n1. Interface/Abstract class - MUST have virtual destructor:" << endl;
    IShape* shape = new Circle(5.0);
    shape->draw();
    cout << "Area: " << shape->area() << endl;
    delete shape;  // Correct cleanup
    
    cout << "\n2. Class with virtual functions - SHOULD have virtual destructor:" << endl;
    Animal* animal = new Dog("Buddy");
    animal->speak();
    delete animal;  // Correct cleanup
    
    cout << "\n3. Class with no virtual functions - virtual destructor optional:" << endl;
    Point* point = new Point(10, 20);
    point->display();
    delete point;  // No virtual dispatch needed
    
    cout << "\nRule: If class has virtual functions, make destructor virtual!" << endl;
    
    return 0;
}
```

---

## 3. **Virtual Destructor in Inheritance Chains**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class GrandParent {
protected:
    string* grandData;
    
public:
    GrandParent() {
        grandData = new string("GrandParent Resource");
        cout << "GrandParent constructor: " << *grandData << endl;
    }
    
    virtual ~GrandParent() {
        cout << "GrandParent destructor: deleting " << *grandData << endl;
        delete grandData;
    }
    
    virtual void show() const {
        cout << "GrandParent: " << *grandData << endl;
    }
};

class Parent : public GrandParent {
protected:
    string* parentData;
    
public:
    Parent() : GrandParent() {
        parentData = new string("Parent Resource");
        cout << "Parent constructor: " << *parentData << endl;
    }
    
    virtual ~Parent() override {
        cout << "Parent destructor: deleting " << *parentData << endl;
        delete parentData;
    }
    
    void show() const override {
        GrandParent::show();
        cout << "Parent: " << *parentData << endl;
    }
};

class Child : public Parent {
private:
    string* childData;
    
public:
    Child() : Parent() {
        childData = new string("Child Resource");
        cout << "Child constructor: " << *childData << endl;
    }
    
    ~Child() override {
        cout << "Child destructor: deleting " << *childData << endl;
        delete childData;
    }
    
    void show() const override {
        Parent::show();
        cout << "Child: " << *childData << endl;
    }
};

int main() {
    cout << "=== Virtual Destructor in Inheritance Chains ===" << endl;
    
    cout << "\n1. Deleting Child through GrandParent pointer:" << endl;
    GrandParent* obj1 = new Child();
    obj1->show();
    delete obj1;  // Full chain of destructors called
    
    cout << "\n2. Deleting Child through Parent pointer:" << endl;
    Parent* obj2 = new Child();
    obj2->show();
    delete obj2;  // Full chain of destructors called
    
    cout << "\n3. Deleting directly (stack object):" << endl;
    {
        Child obj3;
        obj3.show();
    }  // Destructors called in reverse order automatically
    
    cout << "\n4. Vector of polymorphic objects:" << endl;
    {
        vector<GrandParent*> objects;
        objects.push_back(new GrandParent());
        objects.push_back(new Parent());
        objects.push_back(new Child());
        
        for (auto obj : objects) {
            obj->show();
            delete obj;  // Each deletion calls correct destructor chain
        }
    }
    
    cout << "\nNote: Virtual destructor ensures complete cleanup in deep hierarchies!" << endl;
    
    return 0;
}
```

---

## 4. **Abstract Base Class with Virtual Destructor**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <vector>
using namespace std;

// Abstract base class with pure virtual destructor
class Resource {
public:
    // Pure virtual destructor - class becomes abstract
    virtual ~Resource() = 0;
    
    virtual void use() const = 0;
    virtual string getType() const = 0;
};

// Pure virtual destructor must have a body
Resource::~Resource() {
    cout << "Resource base destructor" << endl;
}

class FileResource : public Resource {
private:
    string filename;
    FILE* file;
    
public:
    FileResource(const string& name) : filename(name) {
        file = fopen(name.c_str(), "w");
        cout << "FileResource created: " << filename << endl;
    }
    
    ~FileResource() override {
        if (file) {
            fclose(file);
            cout << "FileResource closed: " << filename << endl;
        }
        cout << "FileResource destructor" << endl;
    }
    
    void use() const override {
        if (file) {
            cout << "Using file: " << filename << endl;
        }
    }
    
    string getType() const override {
        return "FileResource";
    }
};

class MemoryResource : public Resource {
private:
    int* data;
    size_t size;
    
public:
    MemoryResource(size_t s) : size(s) {
        data = new int[size];
        cout << "MemoryResource allocated: " << size << " ints" << endl;
    }
    
    ~MemoryResource() override {
        delete[] data;
        cout << "MemoryResource freed: " << size << " ints" << endl;
        cout << "MemoryResource destructor" << endl;
    }
    
    void use() const override {
        cout << "Using memory block of " << size << " ints" << endl;
    }
    
    string getType() const override {
        return "MemoryResource";
    }
};

class NetworkResource : public Resource {
private:
    string host;
    int port;
    bool connected;
    
public:
    NetworkResource(string h, int p) : host(h), port(p), connected(false) {
        cout << "NetworkResource created: " << host << ":" << port << endl;
    }
    
    ~NetworkResource() override {
        if (connected) {
            cout << "NetworkResource disconnecting..." << endl;
        }
        cout << "NetworkResource destructor" << endl;
    }
    
    void use() const override {
        cout << "Using network connection to " << host << ":" << port << endl;
    }
    
    void connect() {
        connected = true;
        cout << "Connected to " << host << ":" << port << endl;
    }
    
    string getType() const override {
        return "NetworkResource";
    }
};

class ResourceManager {
private:
    vector<unique_ptr<Resource>> resources;
    
public:
    void add(Resource* res) {
        resources.emplace_back(res);
    }
    
    void useAll() const {
        for (const auto& res : resources) {
            cout << "Type: " << res->getType() << " - ";
            res->use();
        }
    }
    
    // No need for explicit cleanup - unique_ptr handles it
};

int main() {
    cout << "=== Abstract Base Class with Virtual Destructor ===" << endl;
    
    cout << "\n1. Creating resources:" << endl;
    ResourceManager manager;
    manager.add(new FileResource("data.txt"));
    manager.add(new MemoryResource(1000));
    manager.add(new NetworkResource("api.example.com", 8080));
    
    cout << "\n2. Using resources polymorphically:" << endl;
    manager.useAll();
    
    cout << "\n3. Resources will be automatically cleaned up:" << endl;
    cout << "   (ResourceManager destructor calls unique_ptr destructors)" << endl;
    
    cout << "\n4. Abstract class with pure virtual destructor:" << endl;
    cout << "   ✓ Cannot instantiate Resource directly" << endl;
    cout << "   ✓ Forces derived classes to implement destructor" << endl;
    cout << "   ✓ Ensures proper cleanup through base pointers" << endl;
    
    return 0;
}
```

---

## 5. **Performance Considerations**

```cpp
#include <iostream>
#include <chrono>
#include <vector>
using namespace std;
using namespace chrono;

// Class with non-virtual destructor (no vtable overhead)
class NonVirtual {
private:
    int data;
    
public:
    NonVirtual(int d) : data(d) {}
    ~NonVirtual() {}  // Non-virtual
    void process() { data++; }
};

// Class with virtual destructor (vtable overhead)
class VirtualBase {
public:
    virtual ~VirtualBase() {}  // Virtual destructor
    virtual void process() = 0;
};

class VirtualDerived : public VirtualBase {
private:
    int data;
    
public:
    VirtualDerived(int d) : data(d) {}
    ~VirtualDerived() override {}
    void process() override { data++; }
};

// Class with virtual functions and virtual destructor
class Polymorphic {
private:
    int data;
    
public:
    Polymorphic(int d) : data(d) {}
    virtual ~Polymorphic() {}  // Virtual destructor
    virtual void process() { data++; }
};

class DerivedPolymorphic : public Polymorphic {
public:
    DerivedPolymorphic(int d) : Polymorphic(d) {}
    ~DerivedPolymorphic() override {}
    void process() override { Polymorphic::process(); }
};

int main() {
    cout << "=== Performance Considerations ===" << endl;
    
    cout << "\n1. Object size comparison:" << endl;
    cout << "NonVirtual size: " << sizeof(NonVirtual) << " bytes" << endl;
    cout << "VirtualBase size: " << sizeof(VirtualBase) << " bytes" << endl;
    cout << "Polymorphic size: " << sizeof(Polymorphic) << " bytes" << endl;
    cout << "Note: Virtual destructor adds vptr (8 bytes on 64-bit)" << endl;
    
    cout << "\n2. When to use virtual destructor:" << endl;
    cout << "✓ REQUIRED: Class has virtual functions" << endl;
    cout << "✓ REQUIRED: Class is intended as base class" << endl;
    cout << "✓ REQUIRED: Deleting derived through base pointer" << endl;
    cout << "✗ NOT NEEDED: Class has no virtual functions" << endl;
    cout << "✗ NOT NEEDED: Class is final/sealed" << endl;
    
    cout << "\n3. Performance impact:" << endl;
    cout << "• Virtual destructor adds vptr (memory overhead)" << endl;
    cout << "• Virtual dispatch adds slight runtime overhead" << endl;
    cout << "• Cost is minimal compared to benefits" << endl;
    cout << "• Modern CPUs handle virtual dispatch efficiently" << endl;
    
    cout << "\n4. Best practice:" << endl;
    cout << "If a class has ANY virtual functions, make destructor virtual!" << endl;
    cout << "If class is not intended for inheritance, no need for virtual destructor" << endl;
    
    return 0;
}
```

---

## 6. **Practical Example: Plugin System**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <map>
using namespace std;

// Plugin interface - MUST have virtual destructor
class IPlugin {
protected:
    string name;
    string version;
    
public:
    IPlugin(string n, string v) : name(n), version(v) {
        cout << "Plugin base: " << name << " v" << version << endl;
    }
    
    virtual ~IPlugin() {
        cout << "Plugin destroyed: " << name << endl;
    }
    
    virtual void initialize() = 0;
    virtual void execute() = 0;
    virtual void shutdown() = 0;
    
    string getName() const { return name; }
    string getVersion() const { return version; }
};

// Concrete plugin 1
class LoggerPlugin : public IPlugin {
private:
    FILE* logFile;
    bool active;
    
public:
    LoggerPlugin() : IPlugin("Logger", "1.0"), logFile(nullptr), active(false) {
        cout << "  LoggerPlugin constructed" << endl;
    }
    
    ~LoggerPlugin() override {
        if (logFile) {
            fclose(logFile);
        }
        cout << "  LoggerPlugin destroyed" << endl;
    }
    
    void initialize() override {
        logFile = fopen("plugin.log", "w");
        active = true;
        cout << "  LoggerPlugin initialized" << endl;
    }
    
    void execute() override {
        if (active && logFile) {
            fprintf(logFile, "Log entry at %ld\n", time(nullptr));
            cout << "  LoggerPlugin: wrote log entry" << endl;
        }
    }
    
    void shutdown() override {
        if (logFile) {
            fclose(logFile);
            logFile = nullptr;
        }
        active = false;
        cout << "  LoggerPlugin shutdown" << endl;
    }
};

// Concrete plugin 2
class DataProcessorPlugin : public IPlugin {
private:
    int* data;
    size_t size;
    bool initialized;
    
public:
    DataProcessorPlugin() : IPlugin("DataProcessor", "2.1"), data(nullptr), size(0), initialized(false) {
        cout << "  DataProcessorPlugin constructed" << endl;
    }
    
    ~DataProcessorPlugin() override {
        if (data) {
            delete[] data;
        }
        cout << "  DataProcessorPlugin destroyed" << endl;
    }
    
    void initialize() override {
        size = 1000;
        data = new int[size];
        initialized = true;
        cout << "  DataProcessorPlugin initialized (allocated " << size << " ints)" << endl;
    }
    
    void execute() override {
        if (initialized) {
            for (size_t i = 0; i < size; i++) {
                data[i] = i;
            }
            cout << "  DataProcessorPlugin: processed " << size << " elements" << endl;
        }
    }
    
    void shutdown() override {
        if (data) {
            delete[] data;
            data = nullptr;
        }
        initialized = false;
        cout << "  DataProcessorPlugin shutdown" << endl;
    }
};

// Plugin manager
class PluginManager {
private:
    vector<unique_ptr<IPlugin>> plugins;
    map<string, IPlugin*> pluginMap;
    
public:
    void loadPlugin(IPlugin* plugin) {
        plugins.emplace_back(plugin);
        pluginMap[plugin->getName()] = plugin;
        cout << "Loaded plugin: " << plugin->getName() << endl;
    }
    
    void initializeAll() {
        for (auto& plugin : plugins) {
            plugin->initialize();
        }
    }
    
    void executeAll() {
        for (auto& plugin : plugins) {
            plugin->execute();
        }
    }
    
    void shutdownAll() {
        for (auto& plugin : plugins) {
            plugin->shutdown();
        }
    }
    
    IPlugin* getPlugin(const string& name) {
        auto it = pluginMap.find(name);
        if (it != pluginMap.end()) {
            return it->second;
        }
        return nullptr;
    }
    
    // No explicit cleanup needed - unique_ptr handles it
};

int main() {
    cout << "=== Plugin System with Virtual Destructor ===" << endl;
    
    cout << "\n1. Loading plugins:" << endl;
    PluginManager manager;
    manager.loadPlugin(new LoggerPlugin());
    manager.loadPlugin(new DataProcessorPlugin());
    
    cout << "\n2. Initializing plugins:" << endl;
    manager.initializeAll();
    
    cout << "\n3. Executing plugins:" << endl;
    manager.executeAll();
    
    cout << "\n4. Shutting down plugins:" << endl;
    manager.shutdownAll();
    
    cout << "\n5. Plugins will be automatically destroyed:" << endl;
    cout << "   (PluginManager destructor calls unique_ptr destructors)" << endl;
    
    cout << "\nKey Takeaway: Virtual destructor ensures proper cleanup";
    cout << " when deleting through base interface!" << endl;
    
    return 0;
}
```

---

## 📊 Virtual Destructor Summary

| Aspect | Description |
|--------|-------------|
| **Purpose** | Proper cleanup in polymorphic hierarchies |
| **When Needed** | Class has virtual functions |
| **Cost** | vptr overhead (8 bytes on 64-bit) |
| **Rule** | If any virtual function → virtual destructor |
| **Pure Virtual** | Makes class abstract (must have body) |

---

## ✅ Best Practices

1. **Make destructor virtual** for any class with virtual functions
2. **Pure virtual destructor** can make class abstract
3. **Always provide body** for pure virtual destructor
4. **Use `override`** keyword in derived classes (C++11)
5. **Smart pointers** handle virtual destructors automatically
6. **Consider performance** but prioritize correctness

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Missing virtual destructor** | Memory leak in polymorphism | Always add virtual destructor |
| **Pure virtual without body** | Linker error | Provide empty body: `{}` |
| **Virtual destructor in final class** | Unnecessary overhead | Not needed if class is final |
| **Forgetting override** | Hard to maintain | Use `override` keyword |

---

## ✅ Key Takeaways

1. **Virtual destructor** ensures complete cleanup in polymorphism
2. **Required** when class has virtual functions
3. **Pure virtual destructor** makes class abstract
4. **Must have body** even when pure virtual
5. **Smart pointers** handle virtual destructors automatically
6. **Rule of Thumb**: If any virtual function → virtual destructor

---