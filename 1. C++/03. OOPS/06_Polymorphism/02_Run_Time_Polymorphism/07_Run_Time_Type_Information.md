# Run-Time Type Information (RTTI) in C++ - Complete Guide

## 📖 Overview

Run-Time Type Information (RTTI) is a mechanism in C++ that allows the type of an object to be determined during program execution. RTTI is essential for safe downcasting, type identification, and implementing certain design patterns. It provides two main operators: `typeid` for type identification and `dynamic_cast` for safe downcasting.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **RTTI** | Run-Time Type Information mechanism |
| **typeid** | Operator to get type information at runtime |
| **dynamic_cast** | Safe downcasting with runtime type checking |
| **type_info** | Class containing information about a type |
| **Polymorphic Classes** | Classes with at least one virtual function |

---

## 1. **typeid Operator**

```cpp
#include <iostream>
#include <typeinfo>
#include <string>
using namespace std;

class Base {
public:
    virtual void func() {}
    virtual ~Base() {}
};

class Derived : public Base {
public:
    void derivedFunc() {}
};

class NonPolymorphic {
    // No virtual functions
};

int main() {
    cout << "=== typeid Operator ===" << endl;
    
    // Basic types
    cout << "\n1. Basic types:" << endl;
    cout << "typeid(int).name(): " << typeid(int).name() << endl;
    cout << "typeid(double).name(): " << typeid(double).name() << endl;
    cout << "typeid(string).name(): " << typeid(string).name() << endl;
    
    int x = 42;
    double y = 3.14;
    cout << "typeid(x).name(): " << typeid(x).name() << endl;
    cout << "typeid(y).name(): " << typeid(y).name() << endl;
    
    // Polymorphic types
    cout << "\n2. Polymorphic types:" << endl;
    Base b;
    Derived d;
    Base* ptr = &d;
    
    cout << "typeid(b).name(): " << typeid(b).name() << endl;
    cout << "typeid(d).name(): " << typeid(d).name() << endl;
    cout << "typeid(*ptr).name(): " << typeid(*ptr).name() << endl;
    cout << "ptr points to: " << typeid(*ptr).name() << endl;
    
    // Non-polymorphic types (static type)
    cout << "\n3. Non-polymorphic types:" << endl;
    NonPolymorphic np;
    NonPolymorphic* npptr = &np;
    cout << "typeid(np).name(): " << typeid(np).name() << endl;
    cout << "typeid(*npptr).name(): " << typeid(*npptr).name() << endl;
    
    // Comparing types
    cout << "\n4. Type comparison:" << endl;
    if (typeid(b) == typeid(d)) {
        cout << "b and d are same type" << endl;
    } else {
        cout << "b and d are different types" << endl;
    }
    
    if (typeid(*ptr) == typeid(d)) {
        cout << "*ptr and d are same type" << endl;
    }
    
    return 0;
}
```

**Output:**
```
=== typeid Operator ===

1. Basic types:
typeid(int).name(): i
typeid(double).name(): d
typeid(string).name(): NSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE
typeid(x).name(): i
typeid(y).name(): d

2. Polymorphic types:
typeid(b).name(): 4Base
typeid(d).name(): 7Derived
typeid(*ptr).name(): 7Derived
ptr points to: 7Derived

3. Non-polymorphic types:
typeid(np).name(): 16NonPolymorphic
typeid(*npptr).name(): 16NonPolymorphic

4. Type comparison:
b and d are different types
*ptr and d are same type
```

---

## 2. **dynamic_cast for Safe Downcasting**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

class Animal {
public:
    virtual void speak() const {
        cout << "Animal speaks" << endl;
    }
    virtual ~Animal() = default;
};

class Dog : public Animal {
public:
    void speak() const override {
        cout << "Dog barks: Woof!" << endl;
    }
    
    void wagTail() const {
        cout << "Dog wags tail" << endl;
    }
};

class Cat : public Animal {
public:
    void speak() const override {
        cout << "Cat meows: Meow!" << endl;
    }
    
    void purr() const {
        cout << "Cat purrs" << endl;
    }
};

class Bird : public Animal {
public:
    void speak() const override {
        cout << "Bird chirps: Tweet!" << endl;
    }
    
    void fly() const {
        cout << "Bird flies" << endl;
    }
};

int main() {
    cout << "=== dynamic_cast for Safe Downcasting ===" << endl;
    
    vector<unique_ptr<Animal>> animals;
    animals.push_back(make_unique<Dog>());
    animals.push_back(make_unique<Cat>());
    animals.push_back(make_unique<Bird>());
    
    cout << "\n1. Using dynamic_cast to access derived-specific methods:" << endl;
    for (auto& animal : animals) {
        animal->speak();  // Polymorphic call
        
        // Safe downcasting
        if (Dog* dog = dynamic_cast<Dog*>(animal.get())) {
            dog->wagTail();
        } else if (Cat* cat = dynamic_cast<Cat*>(animal.get())) {
            cat->purr();
        } else if (Bird* bird = dynamic_cast<Bird*>(animal.get())) {
            bird->fly();
        }
        cout << endl;
    }
    
    cout << "\n2. dynamic_cast with references (throws exception):" << endl;
    try {
        Dog dog;
        Animal& animalRef = dog;
        Dog& dogRef = dynamic_cast<Dog&>(animalRef);
        dogRef.wagTail();
        
        Cat& catRef = dynamic_cast<Cat&>(animalRef);  // Will throw
    } catch (const bad_cast& e) {
        cout << "Bad cast: " << e.what() << endl;
    }
    
    return 0;
}
```

**Output:**
```
=== dynamic_cast for Safe Downcasting ===

1. Using dynamic_cast to access derived-specific methods:
Dog barks: Woof!
Dog wags tail

Cat meows: Meow!
Cat purrs

Bird chirps: Tweet!
Bird flies

2. dynamic_cast with references (throws exception):
Dog wags tail
Bad cast: std::bad_cast
```

---

## 3. **dynamic_cast vs static_cast**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Base {
public:
    virtual void show() {
        cout << "Base::show()" << endl;
    }
    virtual ~Base() = default;
};

class Derived : public Base {
public:
    void show() override {
        cout << "Derived::show()" << endl;
    }
    
    void derivedOnly() {
        cout << "Derived::derivedOnly()" << endl;
    }
};

class Unrelated {
public:
    void unrelated() {
        cout << "Unrelated::unrelated()" << endl;
    }
};

int main() {
    cout << "=== dynamic_cast vs static_cast ===" << endl;
    
    Derived d;
    Base* basePtr = &d;
    
    cout << "\n1. Upcast (always safe):" << endl;
    Base* b = static_cast<Base*>(&d);     // OK - always safe
    Base* b2 = dynamic_cast<Base*>(&d);   // OK - always safe
    
    cout << "\n2. Downcast (needs runtime check):" << endl;
    
    // static_cast - no runtime check (dangerous!)
    Derived* d1 = static_cast<Derived*>(basePtr);
    d1->derivedOnly();  // Works, but unsafe if type is wrong
    
    // dynamic_cast - runtime check (safe)
    Derived* d2 = dynamic_cast<Derived*>(basePtr);
    if (d2) {
        d2->derivedOnly();
    }
    
    cout << "\n3. Wrong type casting:" << endl;
    Base base;
    Base* basePtr2 = &base;
    
    // static_cast - dangerous (no check)
    Derived* d3 = static_cast<Derived*>(basePtr2);
    // d3->derivedOnly();  // Undefined behavior!
    
    // dynamic_cast - safe (returns nullptr)
    Derived* d4 = dynamic_cast<Derived*>(basePtr2);
    if (d4) {
        d4->derivedOnly();
    } else {
        cout << "dynamic_cast failed - returned nullptr" << endl;
    }
    
    cout << "\n4. Casting between unrelated types:" << endl;
    Unrelated* u = reinterpret_cast<Unrelated*>(basePtr);  // reinterpret_cast only
    // u->unrelated();  // Dangerous!
    
    cout << "\n5. When to use each:" << endl;
    cout << "   static_cast:   Upcast, well-defined conversions" << endl;
    cout << "   dynamic_cast:  Safe downcast for polymorphic types" << endl;
    cout << "   reinterpret_cast: Low-level casting (avoid)" << endl;
    cout << "   const_cast:    Remove const (avoid)" << endl;
    
    return 0;
}
```

---

## 4. **type_info Class**

```cpp
#include <iostream>
#include <typeinfo>
#include <string>
#include <cxxabi.h>  // For demangling (GCC)
using namespace std;

class Shape {
public:
    virtual void draw() = 0;
    virtual ~Shape() = default;
};

class Circle : public Shape {
public:
    void draw() override { cout << "Drawing Circle" << endl; }
};

class Rectangle : public Shape {
public:
    void draw() override { cout << "Drawing Rectangle" << endl; }
};

// Helper to demangle type name (GCC/Clang)
string demangle(const char* name) {
    int status;
    char* demangled = abi::__cxa_demangle(name, nullptr, nullptr, &status);
    string result = (status == 0) ? demangled : name;
    free(demangled);
    return result;
}

int main() {
    cout << "=== type_info Class ===" << endl;
    
    Circle c;
    Rectangle r;
    Shape* shapes[] = {&c, &r};
    
    cout << "\n1. Basic type_info usage:" << endl;
    const type_info& t1 = typeid(c);
    const type_info& t2 = typeid(r);
    
    cout << "Type of c: " << demangle(t1.name()) << endl;
    cout << "Type of r: " << demangle(t2.name()) << endl;
    cout << "Are they same? " << (t1 == t2 ? "Yes" : "No") << endl;
    
    cout << "\n2. type_info in polymorphic container:" << endl;
    for (auto shape : shapes) {
        const type_info& ti = typeid(*shape);
        cout << "Shape type: " << demangle(ti.name()) << endl;
        if (ti == typeid(Circle)) {
            cout << "  -> It's a Circle!" << endl;
        } else if (ti == typeid(Rectangle)) {
            cout << "  -> It's a Rectangle!" << endl;
        }
    }
    
    cout << "\n3. type_info methods:" << endl;
    const type_info& ti = typeid(Circle);
    cout << "name(): " << demangle(ti.name()) << endl;
    cout << "hash_code(): " << ti.hash_code() << endl;
    cout << "before(Rectangle): " << (ti.before(typeid(Rectangle)) ? "Yes" : "No") << endl;
    
    cout << "\n4. type_info cannot be copied:" << endl;
    // type_info ti2 = ti;  // Error! Copy constructor deleted
    const type_info& ti2 = typeid(Circle);  // Reference only
    
    return 0;
}
```

---

## 5. **Performance Considerations**

```cpp
#include <iostream>
#include <chrono>
#include <vector>
#include <memory>
using namespace std;
using namespace chrono;

class Base {
public:
    virtual void process() = 0;
    virtual ~Base() = default;
};

class DerivedA : public Base {
public:
    void process() override {
        // Do nothing
    }
    
    void specificA() {}
};

class DerivedB : public Base {
public:
    void process() override {
        // Do nothing
    }
    
    void specificB() {}
};

int main() {
    cout << "=== Performance Considerations ===" << endl;
    
    const int ITERATIONS = 10000000;
    DerivedA da;
    DerivedB db;
    Base* ptrs[2] = {&da, &db};
    
    // Test 1: Virtual function call (no RTTI)
    auto start = high_resolution_clock::now();
    for (int i = 0; i < ITERATIONS; i++) {
        ptrs[i % 2]->process();
    }
    auto end = high_resolution_clock::now();
    auto virtualTime = duration_cast<milliseconds>(end - start).count();
    
    // Test 2: dynamic_cast + virtual call
    start = high_resolution_clock::now();
    for (int i = 0; i < ITERATIONS; i++) {
        Base* ptr = ptrs[i % 2];
        if (DerivedA* d = dynamic_cast<DerivedA*>(ptr)) {
            d->process();
        } else if (DerivedB* d = dynamic_cast<DerivedB*>(ptr)) {
            d->process();
        }
    }
    end = high_resolution_clock::now();
    auto dynamicCastTime = duration_cast<milliseconds>(end - start).count();
    
    // Test 3: typeid check + virtual call
    start = high_resolution_clock::now();
    for (int i = 0; i < ITERATIONS; i++) {
        Base* ptr = ptrs[i % 2];
        if (typeid(*ptr) == typeid(DerivedA)) {
            static_cast<DerivedA*>(ptr)->process();
        } else if (typeid(*ptr) == typeid(DerivedB)) {
            static_cast<DerivedB*>(ptr)->process();
        }
    }
    end = high_resolution_clock::now();
    auto typeidTime = duration_cast<milliseconds>(end - start).count();
    
    cout << "\nPerformance for " << ITERATIONS << " iterations:" << endl;
    cout << "Virtual function only:     " << virtualTime << " ms" << endl;
    cout << "dynamic_cast + virtual:    " << dynamicCastTime << " ms" << endl;
    cout << "typeid + static_cast:      " << typeidTime << " ms" << endl;
    
    cout << "\nRTTI Cost Analysis:" << endl;
    cout << "  dynamic_cast:    Additional type check (2-3x slower)" << endl;
    cout << "  typeid:          Fast (similar to virtual call)" << endl;
    cout << "  Recommendation:  Use virtual functions when possible" << endl;
    cout << "                   Use RTTI only when necessary" << endl;
    
    return 0;
}
```

---

## 6. **Practical Example: Object Serialization**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <memory>
#include <typeinfo>
#include <cxxabi.h>
using namespace std;

// Demangle function for readable type names
string demangle(const char* name) {
    int status;
    char* demangled = abi::__cxa_demangle(name, nullptr, nullptr, &status);
    string result = (status == 0) ? demangled : name;
    free(demangled);
    return result;
}

// Base serializable class
class Serializable {
public:
    virtual void serialize(ostream& os) const = 0;
    virtual void deserialize(istream& is) = 0;
    virtual string getTypeName() const = 0;
    virtual ~Serializable() = default;
};

class Person : public Serializable {
private:
    string name;
    int age;
    string email;
    
public:
    Person() : name(""), age(0), email("") {}
    Person(string n, int a, string e) : name(n), age(a), email(e) {}
    
    void serialize(ostream& os) const override {
        os << "Person|" << name << "|" << age << "|" << email << endl;
    }
    
    void deserialize(istream& is) override {
        string line;
        getline(is, line);
        // Parse: Person|name|age|email
        size_t pos1 = line.find('|');
        size_t pos2 = line.find('|', pos1 + 1);
        size_t pos3 = line.find('|', pos2 + 1);
        
        name = line.substr(pos1 + 1, pos2 - pos1 - 1);
        age = stoi(line.substr(pos2 + 1, pos3 - pos2 - 1));
        email = line.substr(pos3 + 1);
    }
    
    string getTypeName() const override {
        return "Person";
    }
    
    void display() const {
        cout << "Person: " << name << ", " << age << ", " << email << endl;
    }
};

class Employee : public Serializable {
private:
    string name;
    int employeeId;
    double salary;
    string department;
    
public:
    Employee() : name(""), employeeId(0), salary(0), department("") {}
    Employee(string n, int id, double s, string dept) 
        : name(n), employeeId(id), salary(s), department(dept) {}
    
    void serialize(ostream& os) const override {
        os << "Employee|" << name << "|" << employeeId << "|" 
           << salary << "|" << department << endl;
    }
    
    void deserialize(istream& is) override {
        string line;
        getline(is, line);
        // Parse: Employee|name|id|salary|department
        size_t pos1 = line.find('|');
        size_t pos2 = line.find('|', pos1 + 1);
        size_t pos3 = line.find('|', pos2 + 1);
        size_t pos4 = line.find('|', pos3 + 1);
        
        name = line.substr(pos1 + 1, pos2 - pos1 - 1);
        employeeId = stoi(line.substr(pos2 + 1, pos3 - pos2 - 1));
        salary = stod(line.substr(pos3 + 1, pos4 - pos3 - 1));
        department = line.substr(pos4 + 1);
    }
    
    string getTypeName() const override {
        return "Employee";
    }
    
    void display() const {
        cout << "Employee: " << name << ", ID: " << employeeId 
             << ", Salary: $" << salary << ", Dept: " << department << endl;
    }
};

class SerializationManager {
private:
    map<string, function<unique_ptr<Serializable>()>> factories;
    
public:
    void registerType(const string& typeName, function<unique_ptr<Serializable>()> factory) {
        factories[typeName] = factory;
    }
    
    void saveToFile(const string& filename, const vector<unique_ptr<Serializable>>& objects) {
        ofstream file(filename);
        for (const auto& obj : objects) {
            obj->serialize(file);
        }
        file.close();
        cout << "Saved " << objects.size() << " objects to " << filename << endl;
    }
    
    vector<unique_ptr<Serializable>> loadFromFile(const string& filename) {
        vector<unique_ptr<Serializable>> objects;
        ifstream file(filename);
        string line;
        
        while (getline(file, line)) {
            size_t pos = line.find('|');
            string typeName = line.substr(0, pos);
            
            auto it = factories.find(typeName);
            if (it != factories.end()) {
                auto obj = it->second();
                // Put the line back for deserialization
                stringstream ss(line);
                obj->deserialize(ss);
                objects.push_back(move(obj));
            }
        }
        
        file.close();
        cout << "Loaded " << objects.size() << " objects from " << filename << endl;
        return objects;
    }
};

int main() {
    cout << "=== Object Serialization with RTTI ===" << endl;
    
    SerializationManager manager;
    
    // Register factory functions using RTTI
    manager.registerType("Person", []() { return make_unique<Person>(); });
    manager.registerType("Employee", []() { return make_unique<Employee>(); });
    
    // Create objects
    vector<unique_ptr<Serializable>> objects;
    objects.push_back(make_unique<Person>("Alice Johnson", 30, "alice@email.com"));
    objects.push_back(make_unique<Employee>("Bob Smith", 1001, 75000, "Engineering"));
    objects.push_back(make_unique<Person>("Charlie Brown", 25, "charlie@email.com"));
    objects.push_back(make_unique<Employee>("Diana Prince", 1002, 85000, "Sales"));
    
    cout << "\n1. Original objects:" << endl;
    for (const auto& obj : objects) {
        cout << "  Type: " << demangle(typeid(*obj).name()) << endl;
        if (auto p = dynamic_cast<Person*>(obj.get())) {
            p->display();
        } else if (auto e = dynamic_cast<Employee*>(obj.get())) {
            e->display();
        }
    }
    
    // Save to file
    cout << "\n2. Saving objects:" << endl;
    manager.saveToFile("data.txt", objects);
    
    // Load from file
    cout << "\n3. Loading objects:" << endl;
    auto loadedObjects = manager.loadFromFile("data.txt");
    
    // Display loaded objects
    cout << "\n4. Loaded objects:" << endl;
    for (const auto& obj : loadedObjects) {
        cout << "  Type: " << demangle(typeid(*obj).name()) << endl;
        if (auto p = dynamic_cast<Person*>(obj.get())) {
            p->display();
        } else if (auto e = dynamic_cast<Employee*>(obj.get())) {
            e->display();
        }
    }
    
    return 0;
}
```

---

## 📊 RTTI Summary

| Feature | Description | Cost |
|---------|-------------|------|
| **typeid** | Get type information | Fast (similar to virtual call) |
| **dynamic_cast** | Safe downcasting | Moderate (type check overhead) |
| **type_info** | Type information class | Small |
| **Polymorphic Required** | RTTI works only for polymorphic types | - |
| **Memory Overhead** | vtable includes type_info pointer | Small |

---

## ✅ Best Practices

1. **Use virtual functions** when possible instead of RTTI
2. **Use `dynamic_cast`** for safe downcasting
3. **Check `dynamic_cast` result** (nullptr for pointers, catch for references)
4. **Avoid RTTI in performance-critical code**
5. **Disable RTTI** (`-fno-rtti`) for embedded systems to save space
6. **Use `typeid` for debugging and logging**

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Using on non-polymorphic types** | Static type only | Ensure class has virtual functions |
| **Not checking dynamic_cast result** | Undefined behavior | Always check pointer result |
| **Catching bad_cast by value** | Object slicing | Catch by reference |
| **Performance overhead** | Slowdown | Use virtual functions instead |
| **RTTI disabled** | Linker errors | Enable RTTI or avoid it |

---

## ✅ Key Takeaways

1. **RTTI** enables runtime type identification in C++
2. **typeid** returns type information at runtime
3. **dynamic_cast** provides safe downcasting
4. **Requires polymorphic types** (classes with virtual functions)
5. **Performance overhead** exists (use judiciously)
6. **Alternatives**: virtual functions, double dispatch, visitor pattern
7. **Useful for** serialization, debugging, generic containers

---