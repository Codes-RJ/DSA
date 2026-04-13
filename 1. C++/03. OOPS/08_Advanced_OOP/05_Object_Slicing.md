# Object Slicing in C++ - Complete Guide

## 📖 Overview

Object slicing occurs when a derived class object is assigned to a base class object, causing the derived-specific parts to be "sliced off" (discarded). This can lead to data loss, unexpected behavior, and subtle bugs. Understanding object slicing is crucial for writing correct polymorphic code.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Object Slicing** | Loss of derived class data when copying to base |
| **Slicing by Value** | Assigning derived to base by value |
| **Slicing in Containers** | Storing derived objects in base containers |
| **Prevention** | Use pointers or references instead of values |

---

## 1. **Basic Object Slicing**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Shape {
protected:
    string color;
    
public:
    Shape(string c = "White") : color(c) {
        cout << "Shape constructor: " << color << endl;
    }
    
    virtual void draw() const {
        cout << "Drawing " << color << " shape" << endl;
    }
    
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
    
    void draw() const override {
        cout << "Drawing " << color << " circle with radius " << radius << endl;
    }
    
    double getRadius() const { return radius; }
    
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
    
    void draw() const override {
        cout << "Drawing " << color << " rectangle " << width << "x" << height << endl;
    }
    
    double getArea() const { return width * height; }
    
    ~Rectangle() override {
        cout << "  Rectangle destructor: " << width << "x" << height << endl;
    }
};

int main() {
    cout << "=== Basic Object Slicing ===" << endl;
    
    cout << "\n1. Creating derived objects:" << endl;
    Circle circle("Red", 5.0);
    Rectangle rect("Blue", 4.0, 6.0);
    
    cout << "\n2. Assigning derived to base (slicing occurs!):" << endl;
    Shape shape1 = circle;   // Slicing! Circle part lost
    Shape shape2 = rect;     // Slicing! Rectangle part lost
    
    cout << "\n3. Calling draw (virtual functions work but data lost):" << endl;
    circle.draw();   // Full Circle draw
    rect.draw();     // Full Rectangle draw
    shape1.draw();   // Only Shape::draw() called - circle part lost
    shape2.draw();   // Only Shape::draw() called - rectangle part lost
    
    return 0;
}
```

**Output:**
```
=== Basic Object Slicing ===

1. Creating derived objects:
Shape constructor: Red
  Circle constructor: radius=5
Shape constructor: Blue
  Rectangle constructor: 4x6

2. Assigning derived to base (slicing occurs!):
Shape constructor: Red
Shape constructor: Blue

3. Calling draw (virtual functions work but data lost):
Drawing Red circle with radius 5
Drawing Blue rectangle 4x6
Drawing Red shape
Drawing Blue shape
  Circle destructor: radius=5
Shape destructor: Red
  Rectangle destructor: 4x6
Shape destructor: Blue
Shape destructor: Red
Shape destructor: Blue
```

---

## 2. **Slicing in Function Parameters**

```cpp
#include <iostream>
#include <string>
using namespace std;

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
    
    virtual ~Animal() {
        cout << "Animal destructor: " << name << endl;
    }
};

class Dog : public Animal {
private:
    string breed;
    
public:
    Dog(string n, string b) : Animal(n), breed(b) {
        cout << "  Dog constructor: " << breed << endl;
    }
    
    void speak() const override {
        cout << name << " barks: Woof!" << endl;
    }
    
    void wagTail() const {
        cout << name << " wags tail" << endl;
    }
    
    ~Dog() override {
        cout << "  Dog destructor: " << breed << endl;
    }
};

// Function taking base by value (slicing occurs!)
void processAnimalByValue(Animal a) {
    cout << "Processing animal by value: ";
    a.speak();  // Virtual call but data sliced!
}

// Function taking base by reference (no slicing)
void processAnimalByReference(const Animal& a) {
    cout << "Processing animal by reference: ";
    a.speak();  // Virtual call works correctly
}

// Function taking base by pointer (no slicing)
void processAnimalByPointer(const Animal* a) {
    cout << "Processing animal by pointer: ";
    a->speak();  // Virtual call works correctly
}

int main() {
    cout << "=== Slicing in Function Parameters ===" << endl;
    
    Dog dog("Buddy", "Golden Retriever");
    
    cout << "\n1. Pass by value (slicing occurs):" << endl;
    processAnimalByValue(dog);
    
    cout << "\n2. Pass by reference (no slicing):" << endl;
    processAnimalByReference(dog);
    
    cout << "\n3. Pass by pointer (no slicing):" << endl;
    processAnimalByPointer(&dog);
    
    cout << "\n4. Direct call (no slicing):" << endl;
    dog.speak();
    dog.wagTail();
    
    return 0;
}
```

---

## 3. **Slicing in Containers**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

class Employee {
protected:
    string name;
    int id;
    
public:
    Employee(string n, int i) : name(n), id(i) {}
    
    virtual double calculateSalary() const {
        return 0;
    }
    
    virtual void display() const {
        cout << "Name: " << name << ", ID: " << id << endl;
    }
    
    virtual ~Employee() = default;
};

class Developer : public Employee {
private:
    double baseSalary;
    int projectsCompleted;
    
public:
    Developer(string n, int i, double salary, int projects) 
        : Employee(n, i), baseSalary(salary), projectsCompleted(projects) {}
    
    double calculateSalary() const override {
        return baseSalary + (projectsCompleted * 1000);
    }
    
    void display() const override {
        Employee::display();
        cout << "  Developer: $" << calculateSalary() << endl;
    }
};

class Manager : public Employee {
private:
    double baseSalary;
    int teamSize;
    double bonus;
    
public:
    Manager(string n, int i, double salary, int team, double b) 
        : Employee(n, i), baseSalary(salary), teamSize(team), bonus(b) {}
    
    double calculateSalary() const override {
        return baseSalary + bonus;
    }
    
    void display() const override {
        Employee::display();
        cout << "  Manager: $" << calculateSalary() << " (Team: " << teamSize << ")" << endl;
    }
};

int main() {
    cout << "=== Slicing in Containers ===" << endl;
    
    Developer dev("Alice", 1001, 75000, 5);
    Manager mgr("Bob", 1002, 90000, 8, 15000);
    
    cout << "\n1. Vector of objects (SLICING!):" << endl;
    vector<Employee> employees;  // Stores Employee objects, not derived
    
    employees.push_back(dev);    // Slicing occurs!
    employees.push_back(mgr);    // Slicing occurs!
    
    for (const auto& e : employees) {
        e.display();  // Only Employee::display() called
    }
    
    cout << "\n2. Vector of pointers (NO SLICING):" << endl;
    vector<Employee*> empPtrs;
    
    empPtrs.push_back(&dev);
    empPtrs.push_back(&mgr);
    
    for (const auto& e : empPtrs) {
        e->display();  // Virtual call works correctly
    }
    
    cout << "\n3. Vector of smart pointers (NO SLICING):" << endl;
    vector<unique_ptr<Employee>> empSmart;
    
    empSmart.push_back(make_unique<Developer>("Charlie", 1003, 80000, 3));
    empSmart.push_back(make_unique<Manager>("Diana", 1004, 95000, 5, 12000));
    
    for (const auto& e : empSmart) {
        e->display();  // Virtual call works correctly
    }
    
    return 0;
}
```

---

## 4. **Slicing in Return Values**

```cpp
#include <iostream>
#include <string>
#include <memory>
using namespace std;

class Product {
protected:
    string name;
    double price;
    
public:
    Product(string n, double p) : name(n), price(p) {}
    
    virtual string getDescription() const {
        return name + " - $" + to_string(price);
    }
    
    virtual ~Product() = default;
};

class Electronics : public Product {
private:
    string brand;
    int warrantyMonths;
    
public:
    Electronics(string n, double p, string b, int w) 
        : Product(n, p), brand(b), warrantyMonths(w) {}
    
    string getDescription() const override {
        return Product::getDescription() + " (" + brand + ", " + 
               to_string(warrantyMonths) + " months warranty)";
    }
};

class Book : public Product {
private:
    string author;
    int pages;
    
public:
    Book(string n, double p, string a, int pg) 
        : Product(n, p), author(a), pages(pg) {}
    
    string getDescription() const override {
        return Product::getDescription() + " by " + author + 
               " (" + to_string(pages) + " pages)";
    }
};

// BAD: Returns by value - slicing occurs!
Product createProductBad(const string& type, const string& name, double price) {
    if (type == "electronics") {
        Electronics e(name, price, "Samsung", 24);
        return e;  // Slicing! Electronics part lost
    } else {
        Book b(name, price, "Unknown", 200);
        return b;  // Slicing! Book part lost
    }
}

// GOOD: Returns pointer - no slicing
Product* createProductGood(const string& type, const string& name, double price) {
    if (type == "electronics") {
        return new Electronics(name, price, "Samsung", 24);
    } else {
        return new Book(name, price, "Unknown", 200);
    }
}

// GOOD: Returns smart pointer - no slicing
unique_ptr<Product> createProductSmart(const string& type, const string& name, double price) {
    if (type == "electronics") {
        return make_unique<Electronics>(name, price, "Samsung", 24);
    } else {
        return make_unique<Book>(name, price, "Unknown", 200);
    }
}

int main() {
    cout << "=== Slicing in Return Values ===" << endl;
    
    cout << "\n1. Returning by value (SLICING):" << endl;
    Product p1 = createProductBad("electronics", "Smart TV", 999.99);
    Product p2 = createProductBad("book", "C++ Primer", 89.99);
    
    cout << "Product 1: " << p1.getDescription() << endl;  // Only Product part
    cout << "Product 2: " << p2.getDescription() << endl;  // Only Product part
    
    cout << "\n2. Returning by pointer (NO SLICING):" << endl;
    Product* p3 = createProductGood("electronics", "Smart TV", 999.99);
    Product* p4 = createProductGood("book", "C++ Primer", 89.99);
    
    cout << "Product 3: " << p3->getDescription() << endl;  // Full description
    cout << "Product 4: " << p4->getDescription() << endl;  // Full description
    
    delete p3;
    delete p4;
    
    cout << "\n3. Returning by smart pointer (NO SLICING):" << endl;
    auto p5 = createProductSmart("electronics", "Smart TV", 999.99);
    auto p6 = createProductSmart("book", "C++ Primer", 89.99);
    
    cout << "Product 5: " << p5->getDescription() << endl;  // Full description
    cout << "Product 6: " << p6->getDescription() << endl;  // Full description
    
    return 0;
}
```

---

## 5. **Preventing Slicing with Copy and Move**

```cpp
#include <iostream>
#include <string>
#include <memory>
using namespace std;

class Base {
protected:
    int value;
    
public:
    Base(int v = 0) : value(v) {}
    
    virtual Base* clone() const {
        return new Base(value);
    }
    
    virtual void display() const {
        cout << "Base value: " << value << endl;
    }
    
    virtual ~Base() = default;
};

class Derived : public Base {
private:
    int extra;
    
public:
    Derived(int v, int e) : Base(v), extra(e) {}
    
    // Covariant return type - returns Derived*
    Derived* clone() const override {
        return new Derived(value, extra);
    }
    
    void display() const override {
        cout << "Derived: value=" << value << ", extra=" << extra << endl;
    }
};

class SafeContainer {
private:
    Base* data;
    
public:
    SafeContainer(const Base& obj) {
        data = obj.clone();  // No slicing! Uses clone
    }
    
    SafeContainer(const SafeContainer& other) {
        data = other.data->clone();
    }
    
    ~SafeContainer() {
        delete data;
    }
    
    void display() const {
        data->display();
    }
};

int main() {
    cout << "=== Preventing Slicing with Clone ===" << endl;
    
    Derived d(10, 20);
    Base b(5);
    
    cout << "\n1. Direct assignment (slicing):" << endl;
    Base b2 = d;      // Slicing!
    b2.display();     // Only Base part
    
    cout << "\n2. Using clone (no slicing):" << endl;
    Base* b3 = d.clone();
    b3->display();    // Full Derived
    delete b3;
    
    cout << "\n3. Using safe container (no slicing):" << endl;
    SafeContainer sc1(d);
    SafeContainer sc2(b);
    
    sc1.display();    // Full Derived
    sc2.display();    // Base
    
    cout << "\n4. Copy of safe container (no slicing):" << endl;
    SafeContainer sc3 = sc1;
    sc3.display();    // Full Derived
    
    return 0;
}
```

---

## 📊 Object Slicing Summary

| Scenario | Slicing? | Explanation |
|----------|----------|-------------|
| **Derived to Base assignment** | ✓ Yes | Derived parts discarded |
| **Pass by value** | ✓ Yes | Copy of base only |
| **Pass by reference** | ✗ No | Reference maintains type |
| **Pass by pointer** | ✗ No | Pointer maintains type |
| **Vector of objects** | ✓ Yes | Container holds base objects |
| **Vector of pointers** | ✗ No | Pointers maintain type |
| **Return by value** | ✓ Yes | Copy of base only |
| **Return by pointer** | ✗ No | Pointer maintains type |
| **Clone pattern** | ✗ No | Virtual copy method |

---

## ✅ Best Practices

1. **Use pointers or references** for polymorphic objects
2. **Avoid storing derived objects** in base containers by value
3. **Use smart pointers** for automatic memory management
4. **Implement clone pattern** when copying is needed
5. **Mark copy constructors deleted** for polymorphic classes
6. **Use virtual functions** instead of type checking

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Passing by value** | Slicing occurs | Use reference or pointer |
| **Storing in vector** | Slicing occurs | Store pointers or smart pointers |
| **Returning by value** | Slicing occurs | Return pointer or smart pointer |
| **Assignment** | Slicing occurs | Use clone pattern |
| **Copy constructor** | Slicing in copies | Delete or implement properly |

---

## ✅ Key Takeaways

1. **Object slicing** discards derived class data
2. **Occurs when** assigning derived to base by value
3. **Occurs when** passing/returning by value
4. **Occurs when** storing in base containers
5. **Prevent by** using pointers/references
6. **Prevent by** using smart pointers
7. **Prevent by** implementing clone pattern

---
---

## Next Step

- Go to [06_Covariant_Return_Types.md](06_Covariant_Return_Types.md) to continue with Covariant Return Types.
