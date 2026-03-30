# new and delete for Objects - Complete Guide

## 📖 Overview

When working with objects in C++, `new` and `delete` operators handle dynamic object allocation and deallocation. Understanding how these operators work with constructors, destructors, and inheritance is crucial for proper object lifecycle management. This guide covers object-specific allocation patterns, object arrays, and best practices.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Object Allocation** | `new` allocates memory and calls constructor |
| **Object Deallocation** | `delete` calls destructor and frees memory |
| **Object Arrays** | `new[]` allocates array of objects |
| **Constructor Calls** | Called automatically after allocation |
| **Destructor Calls** | Called automatically before deallocation |

---

## 1. **Single Object Allocation**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Employee {
private:
    string name;
    int id;
    double salary;
    static int nextId;
    
public:
    Employee(string n, double sal) : name(n), id(nextId++), salary(sal) {
        cout << "Employee constructor: " << name << " (ID: " << id << ")" << endl;
    }
    
    ~Employee() {
        cout << "Employee destructor: " << name << " (ID: " << id << ")" << endl;
    }
    
    void display() const {
        cout << "ID: " << id << ", Name: " << name << ", Salary: $" << salary << endl;
    }
    
    void giveRaise(double percent) {
        salary += salary * (percent / 100);
    }
};

int Employee::nextId = 1000;

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
    
    void use() {
        cout << "Using resource" << endl;
    }
};

int main() {
    cout << "=== Single Object Allocation ===" << endl;
    
    cout << "\n1. Stack allocation (automatic):" << endl;
    Employee e1("Alice", 75000);
    e1.display();
    
    cout << "\n2. Heap allocation (manual):" << endl;
    Employee* e2 = new Employee("Bob", 85000);
    e2->display();
    delete e2;  // Must delete
    
    cout << "\n3. Multiple heap objects:" << endl;
    Employee* e3 = new Employee("Charlie", 65000);
    Employee* e4 = new Employee("Diana", 95000);
    
    e3->display();
    e4->display();
    
    delete e3;
    delete e4;
    
    cout << "\n4. Resource allocation in constructor:" << endl;
    Resource* res = new Resource(1000);
    res->use();
    delete res;  // Destructor frees resource
    
    return 0;
}
```

**Output:**
```
=== Single Object Allocation ===

1. Stack allocation (automatic):
Employee constructor: Alice (ID: 1000)
ID: 1000, Name: Alice, Salary: $75000
Employee destructor: Alice (ID: 1000)

2. Heap allocation (manual):
Employee constructor: Bob (ID: 1001)
ID: 1001, Name: Bob, Salary: $85000
Employee destructor: Bob (ID: 1001)

3. Multiple heap objects:
Employee constructor: Charlie (ID: 1002)
Employee constructor: Diana (ID: 1003)
ID: 1002, Name: Charlie, Salary: $65000
ID: 1003, Name: Diana, Salary: $95000
Employee destructor: Diana (ID: 1003)
Employee destructor: Charlie (ID: 1002)

4. Resource allocation in constructor:
Resource allocated: 1000 ints
Using resource
Resource freed: 1000 ints
```

---

## 2. **Object Arrays**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Student {
private:
    string name;
    int rollNumber;
    static int nextRoll;
    
public:
    Student() : name("Unknown"), rollNumber(nextRoll++) {
        cout << "Student default constructor: " << name << " (Roll: " << rollNumber << ")" << endl;
    }
    
    Student(string n) : name(n), rollNumber(nextRoll++) {
        cout << "Student parameterized: " << name << " (Roll: " << rollNumber << ")" << endl;
    }
    
    ~Student() {
        cout << "Student destructor: " << name << " (Roll: " << rollNumber << ")" << endl;
    }
    
    void display() const {
        cout << "Roll: " << rollNumber << ", Name: " << name << endl;
    }
};

int Student::nextRoll = 1001;

int main() {
    cout << "=== Object Arrays ===" << endl;
    
    cout << "\n1. Array of objects (default constructor):" << endl;
    Student* students1 = new Student[3];  // Calls default constructor 3 times
    for (int i = 0; i < 3; i++) {
        students1[i].display();
    }
    delete[] students1;
    
    cout << "\n2. Array with initializer list:" << endl;
    Student* students2 = new Student[3]{
        Student("Alice"),
        Student("Bob"),
        Student("Charlie")
    };
    for (int i = 0; i < 3; i++) {
        students2[i].display();
    }
    delete[] students2;
    
    cout << "\n3. 2D array of objects:" << endl;
    Student** matrix = new Student*[2];
    for (int i = 0; i < 2; i++) {
        matrix[i] = new Student[3];
    }
    
    // Use the 2D array
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            matrix[i][j].display();
        }
    }
    
    // Cleanup in reverse order
    for (int i = 0; i < 2; i++) {
        delete[] matrix[i];
    }
    delete[] matrix;
    
    return 0;
}
```

---

## 3. **new and delete with Inheritance**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Base {
protected:
    string name;
    
public:
    Base(string n) : name(n) {
        cout << "Base constructor: " << name << endl;
    }
    
    virtual void speak() const {
        cout << name << " makes a sound" << endl;
    }
    
    virtual ~Base() {
        cout << "Base destructor: " << name << endl;
    }
};

class Dog : public Base {
private:
    string breed;
    
public:
    Dog(string n, string b) : Base(n), breed(b) {
        cout << "  Dog constructor: " << breed << endl;
    }
    
    void speak() const override {
        cout << name << " barks: Woof! (" << breed << ")" << endl;
    }
    
    ~Dog() override {
        cout << "  Dog destructor: " << breed << endl;
    }
};

class Cat : public Base {
public:
    Cat(string n) : Base(n) {
        cout << "  Cat constructor" << endl;
    }
    
    void speak() const override {
        cout << name << " meows: Meow!" << endl;
    }
    
    ~Cat() override {
        cout << "  Cat destructor" << endl;
    }
};

int main() {
    cout << "=== new and delete with Inheritance ===" << endl;
    
    cout << "\n1. Allocating derived objects as base pointers:" << endl;
    Base* animals[3];
    
    animals[0] = new Dog("Buddy", "Golden Retriever");
    animals[1] = new Cat("Whiskers");
    animals[2] = new Dog("Max", "German Shepherd");
    
    cout << "\n2. Polymorphic calls:" << endl;
    for (int i = 0; i < 3; i++) {
        animals[i]->speak();
    }
    
    cout << "\n3. Deleting through base pointers (virtual destructor):" << endl;
    for (int i = 0; i < 3; i++) {
        delete animals[i];  // Virtual destructor ensures proper cleanup
    }
    
    cout << "\n4. Array of base pointers:" << endl;
    Base** zoo = new Base*[2];
    zoo[0] = new Dog("Rex", "Beagle");
    zoo[1] = new Cat("Luna");
    
    for (int i = 0; i < 2; i++) {
        zoo[i]->speak();
        delete zoo[i];
    }
    delete[] zoo;
    
    return 0;
}
```

---

## 4. **Object Pools with new/delete**

```cpp
#include <iostream>
#include <string>
#include <stack>
#include <vector>
using namespace std;

class Particle {
private:
    float x, y, z;
    float vx, vy, vz;
    bool active;
    static int totalCreated;
    static int totalDestroyed;
    
public:
    Particle() : x(0), y(0), z(0), vx(0), vy(0), vz(0), active(true) {
        totalCreated++;
        cout << "Particle created (total: " << totalCreated << ")" << endl;
    }
    
    ~Particle() {
        totalDestroyed++;
        cout << "Particle destroyed (remaining: " << (totalCreated - totalDestroyed) << ")" << endl;
    }
    
    void update(float dt) {
        if (active) {
            x += vx * dt;
            y += vy * dt;
            z += vz * dt;
        }
    }
    
    void setVelocity(float vxVal, float vyVal, float vzVal) {
        vx = vxVal;
        vy = vyVal;
        vz = vzVal;
    }
    
    void activate(float xPos, float yPos, float zPos) {
        x = xPos;
        y = yPos;
        z = zPos;
        active = true;
    }
    
    void deactivate() {
        active = false;
    }
    
    void display() const {
        if (active) {
            cout << "Particle at (" << x << ", " << y << ", " << z << ")" << endl;
        }
    }
    
    static int getCreated() { return totalCreated; }
    static int getDestroyed() { return totalDestroyed; }
};

int Particle::totalCreated = 0;
int Particle::totalDestroyed = 0;

class ParticlePool {
private:
    vector<Particle*> pool;
    stack<Particle*> available;
    
public:
    ParticlePool(int size) {
        for (int i = 0; i < size; i++) {
            Particle* p = new Particle();
            pool.push_back(p);
            available.push(p);
        }
        cout << "Pool created with " << size << " particles" << endl;
    }
    
    ~ParticlePool() {
        for (auto p : pool) {
            delete p;
        }
        cout << "Pool destroyed" << endl;
    }
    
    Particle* acquire() {
        if (available.empty()) {
            cout << "No particles available!" << endl;
            return nullptr;
        }
        Particle* p = available.top();
        available.pop();
        p->activate(0, 0, 0);
        return p;
    }
    
    void release(Particle* p) {
        p->deactivate();
        available.push(p);
    }
    
    size_t availableCount() const {
        return available.size();
    }
};

int main() {
    cout << "=== Object Pools with new/delete ===" << endl;
    
    ParticlePool pool(5);
    
    cout << "\n1. Acquiring particles:" << endl;
    vector<Particle*> active;
    for (int i = 0; i < 5; i++) {
        Particle* p = pool.acquire();
        if (p) {
            p->setVelocity(i * 1.0f, 0, 0);
            active.push_back(p);
        }
    }
    
    cout << "\n2. Trying to acquire beyond pool size:" << endl;
    Particle* extra = pool.acquire();
    if (!extra) cout << "No particle available" << endl;
    
    cout << "\n3. Updating particles:" << endl;
    for (int i = 0; i < 3; i++) {
        cout << "Frame " << i << ":" << endl;
        for (auto p : active) {
            p->update(0.1f);
            p->display();
        }
    }
    
    cout << "\n4. Releasing particles:" << endl;
    for (auto p : active) {
        pool.release(p);
    }
    cout << "Available: " << pool.availableCount() << endl;
    
    cout << "\n5. Statistics:" << endl;
    cout << "Total particles created: " << Particle::getCreated() << endl;
    cout << "Total particles destroyed: " << Particle::getDestroyed() << endl;
    cout << "Pool reused objects, no new allocations after initial creation" << endl;
    
    return 0;
}
```

---

## 5. **Exception Safety with new/delete**

```cpp
#include <iostream>
#include <string>
#include <stdexcept>
#include <memory>
using namespace std;

class Logger {
private:
    string name;
    
public:
    Logger(string n) : name(n) {
        cout << "Logger created: " << name << endl;
    }
    
    ~Logger() {
        cout << "Logger destroyed: " << name << endl;
    }
    
    void log(const string& msg) {
        cout << "[" << name << "] " << msg << endl;
    }
};

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

class Database {
public:
    Database(const string& conn) {
        cout << "Database connected to " << conn << endl;
        if (conn.empty()) {
            throw runtime_error("Invalid connection string");
        }
    }
    
    ~Database() {
        cout << "Database disconnected" << endl;
    }
    
    void query(const string& sql) {
        cout << "Executing: " << sql << endl;
    }
};

// Bad: Manual management (exception unsafe)
void badFunction() {
    Resource* r = new Resource(1000);
    Database* db = new Database("localhost");
    
    r->use();
    db->query("SELECT * FROM users");
    
    delete db;
    delete r;
    // If constructor throws, resources leak!
}

// Good: RAII (exception safe)
void goodFunction() {
    Resource r(1000);
    Database db("localhost");
    
    // No manual cleanup needed
}

// Better: Smart pointers
void smartFunction() {
    auto r = make_unique<Resource>(1000);
    auto db = make_unique<Database>("localhost");
    
    // Automatic cleanup
}

int main() {
    cout << "=== Exception Safety with new/delete ===" << endl;
    
    cout << "\n1. Safe function with RAII:" << endl;
    try {
        goodFunction();
    } catch (const exception& e) {
        cout << "Caught: " << e.what() << endl;
    }
    
    cout << "\n2. Safe function with smart pointers:" << endl;
    try {
        smartFunction();
    } catch (const exception& e) {
        cout << "Caught: " << e.what() << endl;
    }
    
    cout << "\n3. Unsafe function (commented out):" << endl;
    cout << "   // badFunction();  // Would leak on exception" << endl;
    
    cout << "\n4. Exception safety guidelines:" << endl;
    cout << "   ✓ Use RAII (Resource Acquisition Is Initialization)" << endl;
    cout << "   ✓ Use smart pointers instead of raw new/delete" << endl;
    cout << "   ✓ Never use raw new/delete in exception-prone code" << endl;
    cout << "   ✓ Follow Rule of Zero/Three/Five" << endl;
    
    return 0;
}
```

---

## 📊 Object Allocation Summary

| Allocation Type | Syntax | Constructor | Destructor | When to Use |
|-----------------|--------|-------------|------------|-------------|
| **Stack** | `Class obj;` | Automatic | Automatic | Small objects, short lifetime |
| **Heap (single)** | `new Class()` | Manual | Manual | Polymorphic objects, long lifetime |
| **Heap (array)** | `new Class[n]` | Manual | Manual | Arrays of objects |
| **Object Pool** | Custom | Managed | Managed | Frequent allocation/deallocation |

---

## ✅ Best Practices

1. **Prefer stack allocation** when possible
2. **Use smart pointers** instead of raw new/delete
3. **Always match new with delete**, new[] with delete[]
4. **Use virtual destructors** for polymorphic base classes
5. **Never mix new/delete types** (new with delete[], etc.)
6. **Consider object pools** for frequently created/destroyed objects
7. **Use RAII** to manage resources automatically

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Mismatched new/delete** | Undefined behavior | Use new[] with delete[] |
| **Missing virtual destructor** | Incomplete cleanup | Make base destructor virtual |
| **Double delete** | Undefined behavior | Use smart pointers |
| **Forgetting delete** | Memory leak | Use RAII/smart pointers |
| **Exception in constructor** | Resource leak | Use RAII for members |

---

## ✅ Key Takeaways

1. **new** allocates memory and calls constructor
2. **delete** calls destructor and frees memory
3. **Virtual destructors** ensure proper cleanup in hierarchies
4. **Object pools** reuse objects to reduce allocation overhead
5. **RAII** is essential for exception safety
6. **Smart pointers** are preferred over raw pointers

---