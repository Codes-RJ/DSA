# 05_Inheritance/04_Constructor_and_Destructor_in_Inheritance.md

# Constructor and Destructor in Inheritance - Complete Guide

## 📖 Overview

Constructors and destructors in inheritance have specific rules and order of execution. When a derived class object is created, base class constructors are called before derived class constructors. When destroyed, destructors are called in reverse order. Understanding this order is crucial for proper resource initialization and cleanup.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Constructor Order** | Base → Member objects → Derived |
| **Destructor Order** | Derived → Member objects → Base |
| **Initialization List** | Used to call base class constructors |
| **Virtual Destructor** | Essential for polymorphic deletion |
| **Delegation** | Base class constructors can be called explicitly |

---

## 1. **Basic Constructor/Destructor Order**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Base {
private:
    string name;
    
public:
    Base(string n) : name(n) {
        cout << "Base constructor: " << name << endl;
    }
    
    ~Base() {
        cout << "Base destructor: " << name << endl;
    }
};

class Member1 {
private:
    string name;
    
public:
    Member1(string n) : name(n) {
        cout << "  Member1 constructor: " << name << endl;
    }
    
    ~Member1() {
        cout << "  Member1 destructor: " << name << endl;
    }
};

class Member2 {
private:
    string name;
    
public:
    Member2(string n) : name(n) {
        cout << "  Member2 constructor: " << name << endl;
    }
    
    ~Member2() {
        cout << "  Member2 destructor: " << name << endl;
    }
};

class Derived : public Base {
private:
    Member1 m1;
    Member2 m2;
    
public:
    Derived(string baseName, string m1Name, string m2Name) 
        : Base(baseName), m2(m2Name), m1(m1Name) {  // Order in list doesn't matter
        cout << "Derived constructor body" << endl;
    }
    
    ~Derived() {
        cout << "Derived destructor body" << endl;
    }
};

int main() {
    cout << "=== Constructor/Destructor Order ===" << endl;
    cout << "\nConstruction order:" << endl;
    cout << "1. Base class constructor" << endl;
    cout << "2. Member objects (in declaration order)" << endl;
    cout << "3. Derived class constructor body" << endl;
    cout << "\nDestruction order: REVERSE of construction\n" << endl;
    
    {
        Derived d("BaseObj", "Member1Obj", "Member2Obj");
        cout << "\nObject created successfully" << endl;
    }  // Destructor called here
    
    return 0;
}
```

**Output:**
```
=== Constructor/Destructor Order ===

Construction order:
1. Base class constructor
2. Member objects (in declaration order)
3. Derived class constructor body

Destruction order: REVERSE of construction

Base constructor: BaseObj
  Member1 constructor: Member1Obj
  Member2 constructor: Member2Obj
Derived constructor body

Object created successfully
Derived destructor body
  Member2 destructor: Member2Obj
  Member1 destructor: Member1Obj
Base destructor: BaseObj
```

---

## 2. **Constructor Parameters in Inheritance**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Vehicle {
protected:
    string brand;
    int year;
    
public:
    Vehicle(string b, int y) : brand(b), year(y) {
        cout << "Vehicle constructor: " << brand << " (" << year << ")" << endl;
    }
    
    ~Vehicle() {
        cout << "Vehicle destructor: " << brand << endl;
    }
    
    void display() {
        cout << "Brand: " << brand << ", Year: " << year << endl;
    }
};

class Car : public Vehicle {
private:
    int doors;
    string fuelType;
    
public:
    Car(string b, int y, int d, string fuel) 
        : Vehicle(b, y), doors(d), fuelType(fuel) {
        cout << "  Car constructor: " << doors << " doors, " << fuelType << endl;
    }
    
    ~Car() {
        cout << "  Car destructor: " << brand << endl;
    }
    
    void display() {
        Vehicle::display();
        cout << "  Doors: " << doors << ", Fuel: " << fuelType << endl;
    }
};

class ElectricCar : public Car {
private:
    int batteryCapacity;
    int range;
    
public:
    ElectricCar(string b, int y, int d, int battery, int r) 
        : Car(b, y, d, "Electric"), batteryCapacity(battery), range(r) {
        cout << "    ElectricCar constructor: " << batteryCapacity << "kWh, " << range << "km" << endl;
    }
    
    ~ElectricCar() {
        cout << "    ElectricCar destructor: " << brand << endl;
    }
    
    void display() {
        Car::display();
        cout << "    Battery: " << batteryCapacity << "kWh, Range: " << range << "km" << endl;
    }
};

int main() {
    cout << "=== Constructor Parameters in Inheritance ===" << endl;
    
    cout << "\nCreating ElectricCar:" << endl;
    ElectricCar tesla("Tesla", 2024, 4, 75, 500);
    
    cout << "\nDisplaying:" << endl;
    tesla.display();
    
    cout << "\nDestruction order (reverse of construction):" << endl;
    
    return 0;
}
```

**Output:**
```
=== Constructor Parameters in Inheritance ===

Creating ElectricCar:
Vehicle constructor: Tesla (2024)
  Car constructor: 4 doors, Electric
    ElectricCar constructor: 75kWh, 500km

Displaying:
Brand: Tesla, Year: 2024
  Doors: 4, Fuel: Electric
    Battery: 75kWh, Range: 500km

Destruction order (reverse of construction):
    ElectricCar destructor: Tesla
  Car destructor: Tesla
Vehicle destructor: Tesla
```

---

## 3. **Virtual Destructor in Inheritance**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

// Base class with non-virtual destructor (WRONG for polymorphism)
class NonVirtualBase {
public:
    NonVirtualBase() {
        cout << "NonVirtualBase constructor" << endl;
    }
    
    ~NonVirtualBase() {
        cout << "NonVirtualBase destructor" << endl;
    }
    
    virtual void speak() {
        cout << "Base speaking" << endl;
    }
};

class NonVirtualDerived : public NonVirtualBase {
private:
    int* data;
    
public:
    NonVirtualDerived() : data(new int(42)) {
        cout << "NonVirtualDerived constructor: allocated " << *data << endl;
    }
    
    ~NonVirtualDerived() {
        cout << "NonVirtualDerived destructor: deleting " << *data << endl;
        delete data;
    }
    
    void speak() override {
        cout << "Derived speaking" << endl;
    }
};

// Base class with virtual destructor (CORRECT)
class VirtualBase {
public:
    VirtualBase() {
        cout << "VirtualBase constructor" << endl;
    }
    
    virtual ~VirtualBase() {
        cout << "VirtualBase destructor" << endl;
    }
    
    virtual void speak() {
        cout << "VirtualBase speaking" << endl;
    }
};

class VirtualDerived : public VirtualBase {
private:
    int* data;
    
public:
    VirtualDerived() : data(new int(42)) {
        cout << "VirtualDerived constructor: allocated " << *data << endl;
    }
    
    ~VirtualDerived() override {
        cout << "VirtualDerived destructor: deleting " << *data << endl;
        delete data;
    }
    
    void speak() override {
        cout << "VirtualDerived speaking" << endl;
    }
};

int main() {
    cout << "=== Virtual Destructor in Inheritance ===" << endl;
    
    cout << "\n1. INCORRECT: Non-virtual destructor (Memory leak!):" << endl;
    NonVirtualBase* ptr1 = new NonVirtualDerived();
    ptr1->speak();
    delete ptr1;  // Only NonVirtualBase destructor called!
    cout << "Memory leak! Derived destructor not called!" << endl;
    
    cout << "\n2. CORRECT: Virtual destructor:" << endl;
    VirtualBase* ptr2 = new VirtualDerived();
    ptr2->speak();
    delete ptr2;  // Both destructors called correctly
    
    cout << "\n3. Smart pointer handles this automatically:" << endl;
    {
        unique_ptr<VirtualBase> ptr3 = make_unique<VirtualDerived>();
        ptr3->speak();
    }  // Auto cleanup with virtual destructor
    
    cout << "\nRule: Always make base class destructor virtual!" << endl;
    
    return 0;
}
```

---

## 4. **Multiple Inheritance Constructor/Destructor Order**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Base1 {
private:
    string name;
    
public:
    Base1(string n) : name(n) {
        cout << "Base1 constructor: " << name << endl;
    }
    
    ~Base1() {
        cout << "Base1 destructor: " << name << endl;
    }
};

class Base2 {
private:
    string name;
    
public:
    Base2(string n) : name(n) {
        cout << "Base2 constructor: " << name << endl;
    }
    
    ~Base2() {
        cout << "Base2 destructor: " << name << endl;
    }
};

class MemberA {
private:
    string name;
    
public:
    MemberA(string n) : name(n) {
        cout << "  MemberA constructor: " << name << endl;
    }
    
    ~MemberA() {
        cout << "  MemberA destructor: " << name << endl;
    }
};

class MemberB {
private:
    string name;
    
public:
    MemberB(string n) : name(n) {
        cout << "  MemberB constructor: " << name << endl;
    }
    
    ~MemberB() {
        cout << "  MemberB destructor: " << name << endl;
    }
};

class Derived : public Base1, public Base2 {
private:
    MemberA ma;
    MemberB mb;
    
public:
    Derived(string b1Name, string b2Name, string maName, string mbName) 
        : Base1(b1Name), Base2(b2Name), mb(mbName), ma(maName) {
        cout << "Derived constructor body" << endl;
    }
    
    ~Derived() {
        cout << "Derived destructor body" << endl;
    }
};

int main() {
    cout << "=== Multiple Inheritance Constructor/Destructor Order ===" << endl;
    cout << "\nConstruction order:" << endl;
    cout << "1. Base classes (in declaration order)" << endl;
    cout << "2. Member objects (in declaration order)" << endl;
    cout << "3. Derived class constructor body" << endl;
    cout << "\nDestruction order: REVERSE of construction\n" << endl;
    
    {
        Derived d("Base1Obj", "Base2Obj", "MemberAObj", "MemberBObj");
        cout << "\nObject created successfully" << endl;
    }
    
    return 0;
}
```

**Output:**
```
=== Multiple Inheritance Constructor/Destructor Order ===

Construction order:
1. Base classes (in declaration order)
2. Member objects (in declaration order)
3. Derived class constructor body

Destruction order: REVERSE of construction

Base1 constructor: Base1Obj
Base2 constructor: Base2Obj
  MemberA constructor: MemberAObj
  MemberB constructor: MemberBObj
Derived constructor body

Object created successfully
Derived destructor body
  MemberB destructor: MemberBObj
  MemberA destructor: MemberAObj
Base2 destructor: Base2Obj
Base1 destructor: Base1Obj
```

---

## 5. **Virtual Inheritance Constructor Order**

```cpp
#include <iostream>
#include <string>
using namespace std;

class GrandParent {
public:
    GrandParent() {
        cout << "GrandParent constructor" << endl;
    }
    
    GrandParent(int x) {
        cout << "GrandParent parameterized: " << x << endl;
    }
    
    ~GrandParent() {
        cout << "GrandParent destructor" << endl;
    }
};

class Parent1 : virtual public GrandParent {
public:
    Parent1() : GrandParent() {
        cout << "  Parent1 constructor" << endl;
    }
    
    Parent1(int x) : GrandParent(x) {
        cout << "  Parent1 parameterized: " << x << endl;
    }
};

class Parent2 : virtual public GrandParent {
public:
    Parent2() : GrandParent() {
        cout << "  Parent2 constructor" << endl;
    }
    
    Parent2(int x) : GrandParent(x) {
        cout << "  Parent2 parameterized: " << x << endl;
    }
};

class Child : public Parent1, public Parent2 {
public:
    Child() : GrandParent(), Parent1(), Parent2() {
        cout << "    Child constructor" << endl;
    }
    
    Child(int x) : GrandParent(x), Parent1(x), Parent2(x) {
        cout << "    Child parameterized: " << x << endl;
    }
    
    ~Child() {
        cout << "    Child destructor" << endl;
    }
};

int main() {
    cout << "=== Virtual Inheritance Constructor Order ===" << endl;
    
    cout << "\n1. Default construction:" << endl;
    Child c1;
    
    cout << "\n2. Parameterized construction:" << endl;
    Child c2(42);
    
    cout << "\nConstructor order with virtual inheritance:" << endl;
    cout << "1. Virtual base class (only once!)" << endl;
    cout << "2. Non-virtual base classes (in order)" << endl;
    cout << "3. Member objects" << endl;
    cout << "4. Derived class" << endl;
    
    return 0;
}
```

**Output:**
```
=== Virtual Inheritance Constructor Order ===

1. Default construction:
GrandParent constructor
  Parent1 constructor
  Parent2 constructor
    Child constructor

2. Parameterized construction:
GrandParent parameterized: 42
  Parent1 parameterized: 42
  Parent2 parameterized: 42
    Child parameterized: 42

Constructor order with virtual inheritance:
1. Virtual base class (only once!)
2. Non-virtual base classes (in order)
3. Member objects
4. Derived class
    Child destructor
  Parent2 destructor
  Parent1 destructor
GrandParent destructor
    Child destructor
  Parent2 destructor
  Parent1 destructor
GrandParent destructor
```

---

## 6. **Practical Example: Resource Management Hierarchy**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

// Base resource manager
class Resource {
protected:
    string name;
    bool acquired;
    
public:
    Resource(string n) : name(n), acquired(false) {
        cout << "Resource created: " << name << endl;
    }
    
    virtual void acquire() {
        acquired = true;
        cout << "  Acquired: " << name << endl;
    }
    
    virtual void release() {
        if (acquired) {
            acquired = false;
            cout << "  Released: " << name << endl;
        }
    }
    
    virtual ~Resource() {
        release();
        cout << "Resource destroyed: " << name << endl;
    }
    
    bool isAcquired() const { return acquired; }
    string getName() const { return name; }
};

// File resource
class FileResource : public Resource {
private:
    string filename;
    FILE* file;
    
public:
    FileResource(string n, string fname) : Resource(n), filename(fname), file(nullptr) {
        cout << "  FileResource created: " << filename << endl;
    }
    
    void acquire() override {
        if (!acquired) {
            file = fopen(filename.c_str(), "w");
            if (file) {
                Resource::acquire();
                cout << "    File opened: " << filename << endl;
            }
        }
    }
    
    void release() override {
        if (acquired && file) {
            fclose(file);
            file = nullptr;
            cout << "    File closed: " << filename << endl;
        }
        Resource::release();
    }
    
    void write(const string& data) {
        if (acquired && file) {
            fprintf(file, "%s\n", data.c_str());
            cout << "    Written to file: " << data << endl;
        }
    }
    
    ~FileResource() override {
        cout << "  FileResource destroyed: " << filename << endl;
    }
};

// Database connection resource
class DBResource : public Resource {
private:
    string connectionString;
    bool connected;
    
public:
    DBResource(string n, string conn) : Resource(n), connectionString(conn), connected(false) {
        cout << "  DBResource created: " << connectionString << endl;
    }
    
    void acquire() override {
        if (!acquired) {
            // Simulate connection
            connected = true;
            Resource::acquire();
            cout << "    DB Connected: " << connectionString << endl;
        }
    }
    
    void release() override {
        if (acquired && connected) {
            connected = false;
            cout << "    DB Disconnected: " << connectionString << endl;
        }
        Resource::release();
    }
    
    void query(const string& sql) {
        if (acquired && connected) {
            cout << "    Executing: " << sql << endl;
        }
    }
    
    ~DBResource() override {
        cout << "  DBResource destroyed: " << connectionString << endl;
    }
};

// Composite resource manager
class ResourceManager : public Resource {
private:
    vector<unique_ptr<Resource>> resources;
    
public:
    ResourceManager(string n) : Resource(n) {
        cout << "  ResourceManager created" << endl;
    }
    
    void addResource(Resource* res) {
        resources.emplace_back(res);
    }
    
    void acquire() override {
        if (!acquired) {
            Resource::acquire();
            for (auto& res : resources) {
                res->acquire();
            }
            cout << "    All resources acquired" << endl;
        }
    }
    
    void release() override {
        if (acquired) {
            for (auto it = resources.rbegin(); it != resources.rend(); ++it) {
                (*it)->release();
            }
            Resource::release();
            cout << "    All resources released" << endl;
        }
    }
    
    ~ResourceManager() override {
        cout << "  ResourceManager destroyed" << endl;
    }
};

int main() {
    cout << "=== Resource Management Hierarchy ===" << endl;
    
    cout << "\n1. Creating individual resources:" << endl;
    {
        FileResource file("FileRes", "test.txt");
        DBResource db("DBRes", "postgresql://localhost/db");
        
        file.acquire();
        db.acquire();
        
        file.write("Hello World");
        db.query("SELECT * FROM users");
        
        // Resources automatically released when out of scope
    }
    
    cout << "\n2. Creating composite resource manager:" << endl;
    {
        ResourceManager manager("Manager");
        manager.addResource(new FileResource("File1", "log1.txt"));
        manager.addResource(new FileResource("File2", "log2.txt"));
        manager.addResource(new DBResource("DB1", "postgresql://localhost/app"));
        
        manager.acquire();
        
        // All resources acquired automatically
        cout << "\nManager acquired, resources ready" << endl;
        
        // Resources released automatically when manager goes out of scope
    }
    
    cout << "\nNotice the destruction order (reverse of construction):" << endl;
    cout << "Resources → Manager → Base" << endl;
    
    return 0;
}
```

---

## 📊 Constructor/Destructor Order Summary

| Inheritance Type | Constructor Order | Destructor Order |
|------------------|-------------------|------------------|
| **Single** | Base → Derived | Derived → Base |
| **Multiple** | Bases (in declaration) → Derived | Derived → Bases (reverse) |
| **Multilevel** | Grandparent → Parent → Child | Child → Parent → Grandparent |
| **Virtual** | Virtual base → Non-virtual bases → Derived | Derived → Non-virtual → Virtual |

---

## ✅ Best Practices

1. **Always initialize base classes** in derived constructor initialization list
2. **Make base destructor virtual** for polymorphic classes
3. **Follow RAII** for resource management
4. **Use smart pointers** to manage dynamic resources
5. **Be aware of initialization order** when dependencies exist
6. **Document constructor requirements** in base classes

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Missing base constructor call** | Compiler error | Call base constructor in init list |
| **Non-virtual destructor** | Memory leak in polymorphism | Make base destructor virtual |
| **Wrong initialization order** | Dependency issues | Follow declaration order |
| **Calling virtual functions in constructor** | Unexpected behavior | Avoid virtual calls in constructor |
| **Resource leak in constructor** | Exception safety | Use RAII, smart pointers |

---

## ✅ Key Takeaways

1. **Constructor order**: Base → Members → Derived
2. **Destructor order**: Derived → Members → Base
3. **Virtual destructor**: Essential for polymorphic base classes
4. **Initialization list**: Required for base class constructor calls
5. **RAII**: Resources acquired in constructor, released in destructor
6. **Multiple inheritance**: Base classes in declaration order
7. **Virtual inheritance**: Virtual base constructed first

---