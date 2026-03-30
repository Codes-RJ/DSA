# Virtual Inheritance in C++ - Complete Guide

## 📖 Overview

Virtual inheritance is a feature in C++ that solves the diamond problem by ensuring that only one copy of a base class is shared among all derived classes in an inheritance hierarchy. It is used when multiple inheritance paths lead to the same base class, preventing duplication and ambiguity.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Virtual Inheritance** | Ensures single shared copy of base class |
| **Diamond Problem** | Solved by virtual inheritance |
| **Constructor Order** | Virtual base constructed before non-virtual bases |
| **Memory Layout** | Single copy of virtual base shared by all |
| **Performance** | Slight overhead for virtual base pointer |

---

## 1. **Virtual Inheritance Syntax**

```cpp
#include <iostream>
#include <string>
using namespace std;

// Regular base class
class Animal {
protected:
    string name;
    int age;
    
public:
    Animal(string n, int a) : name(n), age(a) {
        cout << "Animal constructor: " << name << endl;
    }
    
    void eat() {
        cout << name << " is eating" << endl;
    }
    
    virtual void speak() {
        cout << name << " makes a sound" << endl;
    }
    
    virtual ~Animal() {
        cout << "Animal destructor: " << name << endl;
    }
};

// Virtual inheritance - Mammal virtually inherits from Animal
class Mammal : virtual public Animal {
public:
    Mammal(string n, int a) : Animal(n, a) {
        cout << "  Mammal constructor: " << name << endl;
    }
    
    void walk() {
        cout << name << " is walking" << endl;
    }
    
    ~Mammal() override {
        cout << "  Mammal destructor: " << name << endl;
    }
};

// Virtual inheritance - Bird virtually inherits from Animal
class Bird : virtual public Animal {
public:
    Bird(string n, int a) : Animal(n, a) {
        cout << "  Bird constructor: " << name << endl;
    }
    
    void fly() {
        cout << name << " is flying" << endl;
    }
    
    ~Bird() override {
        cout << "  Bird destructor: " << name << endl;
    }
};

// Bat inherits from both - only one Animal copy
class Bat : public Mammal, public Bird {
public:
    Bat(string n, int a) : Animal(n, a), Mammal(n, a), Bird(n, a) {
        cout << "    Bat constructor: " << name << endl;
    }
    
    void speak() override {
        cout << name << " makes ultrasonic sounds" << endl;
    }
    
    void display() {
        // No ambiguity - only one name
        cout << "Name: " << name << ", Age: " << age << endl;
    }
    
    ~Bat() override {
        cout << "    Bat destructor: " << name << endl;
    }
};

int main() {
    cout << "=== Virtual Inheritance Syntax ===" << endl;
    
    cout << "\nCreating Bat object:" << endl;
    Bat bat("Batman", 5);
    
    cout << "\nUsing inherited features:" << endl;
    bat.display();
    bat.eat();    // From Animal
    bat.walk();   // From Mammal
    bat.fly();    // From Bird
    bat.speak();  // Overridden
    
    cout << "\nOnly ONE Animal object created!" << endl;
    
    return 0;
}
```

**Output:**
```
=== Virtual Inheritance Syntax ===

Creating Bat object:
Animal constructor: Batman
  Mammal constructor: Batman
  Bird constructor: Batman
    Bat constructor: Batman

Using inherited features:
Name: Batman, Age: 5
Batman is eating
Batman is walking
Batman is flying
Batman makes ultrasonic sounds

Only ONE Animal object created!
    Bat destructor: Batman
  Bird destructor: Batman
  Mammal destructor: Batman
Animal destructor: Batman
```

---

## 2. **Constructor Order in Virtual Inheritance**

```cpp
#include <iostream>
#include <string>
using namespace std;

class GrandParent {
public:
    GrandParent() {
        cout << "GrandParent default constructor" << endl;
    }
    
    GrandParent(int x) {
        cout << "GrandParent constructor: " << x << endl;
    }
};

class Parent1 : virtual public GrandParent {
public:
    Parent1() : GrandParent() {
        cout << "  Parent1 constructor" << endl;
    }
    
    Parent1(int x) : GrandParent(x) {
        cout << "  Parent1 constructor: " << x << endl;
    }
};

class Parent2 : virtual public GrandParent {
public:
    Parent2() : GrandParent() {
        cout << "  Parent2 constructor" << endl;
    }
    
    Parent2(int x) : GrandParent(x) {
        cout << "  Parent2 constructor: " << x << endl;
    }
};

class Child : public Parent1, public Parent2 {
public:
    Child() : GrandParent(), Parent1(), Parent2() {
        cout << "    Child constructor" << endl;
    }
    
    Child(int x) : GrandParent(x), Parent1(x), Parent2(x) {
        cout << "    Child constructor: " << x << endl;
    }
    
    Child(int x1, int x2) : GrandParent(x1), Parent1(x1), Parent2(x2) {
        cout << "    Child constructor: Parent1=" << x1 << ", Parent2=" << x2 << endl;
    }
};

int main() {
    cout << "=== Constructor Order in Virtual Inheritance ===" << endl;
    
    cout << "\n1. Default construction:" << endl;
    Child c1;
    
    cout << "\n2. Same value for all:" << endl;
    Child c2(42);
    
    cout << "\n3. Different values for Parent1 and Parent2:" << endl;
    Child c3(100, 200);
    
    cout << "\nVirtual base constructor is called only ONCE by the most derived class!" << endl;
    cout << "The value from the most derived class constructor is used." << endl;
    
    return 0;
}
```

**Output:**
```
=== Constructor Order in Virtual Inheritance ===

1. Default construction:
GrandParent default constructor
  Parent1 constructor
  Parent2 constructor
    Child constructor

2. Same value for all:
GrandParent constructor: 42
  Parent1 constructor: 42
  Parent2 constructor: 42
    Child constructor: 42

3. Different values for Parent1 and Parent2:
GrandParent constructor: 100
  Parent1 constructor: 100
  Parent2 constructor: 200
    Child constructor: Parent1=100, Parent2=200

Virtual base constructor is called only ONCE by the most derived class!
The value from the most derived class constructor is used.
```

---

## 3. **Memory Layout Comparison**

```cpp
#include <iostream>
#include <string>
using namespace std;

// Non-virtual inheritance
class NonVirtualBase {
public:
    int baseData;
    NonVirtualBase() : baseData(0) {}
    virtual ~NonVirtualBase() {}
};

class NonVirtualDerived1 : public NonVirtualBase {
public:
    int data1;
    NonVirtualDerived1() : data1(1) {}
};

class NonVirtualDerived2 : public NonVirtualBase {
public:
    int data2;
    NonVirtualDerived2() : data2(2) {}
};

class NonVirtualDiamond : public NonVirtualDerived1, public NonVirtualDerived2 {
public:
    int diamondData;
    NonVirtualDiamond() : diamondData(3) {}
};

// Virtual inheritance
class VirtualBase {
public:
    int baseData;
    VirtualBase() : baseData(0) {}
    virtual ~VirtualBase() {}
};

class VirtualDerived1 : virtual public VirtualBase {
public:
    int data1;
    VirtualDerived1() : data1(1) {}
};

class VirtualDerived2 : virtual public VirtualBase {
public:
    int data2;
    VirtualDerived2() : data2(2) {}
};

class VirtualDiamond : public VirtualDerived1, public VirtualDerived2 {
public:
    int diamondData;
    VirtualDiamond() : diamondData(3) {}
};

int main() {
    cout << "=== Memory Layout Comparison ===" << endl;
    
    cout << "\n1. Non-virtual inheritance (multiple copies):" << endl;
    NonVirtualDiamond nvd;
    cout << "Size of NonVirtualBase: " << sizeof(NonVirtualBase) << " bytes" << endl;
    cout << "Size of NonVirtualDerived1: " << sizeof(NonVirtualDerived1) << " bytes" << endl;
    cout << "Size of NonVirtualDerived2: " << sizeof(NonVirtualDerived2) << " bytes" << endl;
    cout << "Size of NonVirtualDiamond: " << sizeof(NonVirtualDiamond) << " bytes" << endl;
    cout << "Note: Two copies of NonVirtualBase!" << endl;
    
    cout << "\n2. Virtual inheritance (single shared copy):" << endl;
    VirtualDiamond vd;
    cout << "Size of VirtualBase: " << sizeof(VirtualBase) << " bytes" << endl;
    cout << "Size of VirtualDerived1: " << sizeof(VirtualDerived1) << " bytes" << endl;
    cout << "Size of VirtualDerived2: " << sizeof(VirtualDerived2) << " bytes" << endl;
    cout << "Size of VirtualDiamond: " << sizeof(VirtualDiamond) << " bytes" << endl;
    cout << "Only one copy of VirtualBase (plus vptr overhead)!" << endl;
    
    cout << "\n3. Accessing members:" << endl;
    cout << "Non-virtual: nvd.NonVirtualDerived1::baseData = " 
         << nvd.NonVirtualDerived1::baseData << endl;
    cout << "Non-virtual: nvd.NonVirtualDerived2::baseData = " 
         << nvd.NonVirtualDerived2::baseData << endl;
    
    // Virtual diamond: no ambiguity
    cout << "Virtual: vd.baseData = " << vd.baseData << endl;
    
    return 0;
}
```

---

## 4. **Virtual Inheritance with Pure Virtual Functions**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

// Abstract base class (interface)
class Drawable {
public:
    virtual void draw() const = 0;
    virtual void setColor(const string& color) = 0;
    virtual ~Drawable() {}
};

// Abstract class with position
class Positioned : virtual public Drawable {
protected:
    int x, y;
    
public:
    Positioned(int xPos = 0, int yPos = 0) : x(xPos), y(yPos) {}
    
    virtual void move(int dx, int dy) {
        x += dx;
        y += dy;
    }
    
    virtual void setPosition(int xPos, int yPos) {
        x = xPos;
        y = yPos;
    }
    
    void getPosition(int& xPos, int& yPos) const {
        xPos = x;
        yPos = y;
    }
};

// Abstract class with size
class Sizable : virtual public Drawable {
protected:
    double width, height;
    
public:
    Sizable(double w = 0, double h = 0) : width(w), height(h) {}
    
    virtual void resize(double factor) {
        width *= factor;
        height *= factor;
    }
    
    virtual void setSize(double w, double h) {
        width = w;
        height = h;
    }
    
    double getWidth() const { return width; }
    double getHeight() const { return height; }
};

// Concrete class implementing multiple interfaces
class Rectangle : public Positioned, public Sizable {
private:
    string color;
    
public:
    Rectangle(int x, int y, double w, double h, string c) 
        : Drawable(), Positioned(x, y), Sizable(w, h), color(c) {
        cout << "Rectangle created at (" << x << "," << y 
             << ") size " << w << "x" << h << " color " << color << endl;
    }
    
    void draw() const override {
        cout << "Drawing " << color << " rectangle at (" << x << "," << y 
             << ") size " << width << "x" << height << endl;
    }
    
    void setColor(const string& c) override {
        color = c;
        cout << "Rectangle color changed to " << color << endl;
    }
    
    double area() const {
        return width * height;
    }
};

// Circle implementing same interfaces
class Circle : public Positioned, public Sizable {
private:
    string color;
    
public:
    Circle(int x, int y, double r, string c) 
        : Drawable(), Positioned(x, y), Sizable(r, r), color(c) {
        cout << "Circle created at (" << x << "," << y 
             << ") radius " << r << " color " << color << endl;
    }
    
    void draw() const override {
        cout << "Drawing " << color << " circle at (" << x << "," << y 
             << ") radius " << width << endl;
    }
    
    void setColor(const string& c) override {
        color = c;
        cout << "Circle color changed to " << color << endl;
    }
    
    double area() const {
        return 3.14159 * width * width;
    }
};

// Shape with additional text
class TextShape : public Positioned, public Sizable {
private:
    string text;
    string color;
    
public:
    TextShape(int x, int y, double w, double h, string t, string c)
        : Drawable(), Positioned(x, y), Sizable(w, h), text(t), color(c) {
        cout << "TextShape created: \"" << text << "\" at (" << x << "," << y 
             << ") size " << w << "x" << h << endl;
    }
    
    void draw() const override {
        cout << "Drawing text \"" << text << "\" in " << color 
             << " at (" << x << "," << y << ") size " << width << "x" << height << endl;
    }
    
    void setColor(const string& c) override {
        color = c;
        cout << "Text color changed to " << color << endl;
    }
    
    void setText(const string& t) {
        text = t;
        cout << "Text changed to \"" << text << "\"" << endl;
    }
};

int main() {
    cout << "=== Virtual Inheritance with Pure Virtual Functions ===" << endl;
    
    cout << "\n1. Creating shapes:" << endl;
    Rectangle rect(10, 20, 100, 50, "Red");
    Circle circle(30, 40, 25, "Blue");
    TextShape text(50, 60, 200, 30, "Hello World", "Green");
    
    cout << "\n2. Using polymorphic container:" << endl;
    vector<unique_ptr<Drawable>> shapes;
    shapes.push_back(make_unique<Rectangle>(rect));
    shapes.push_back(make_unique<Circle>(circle));
    shapes.push_back(make_unique<TextShape>(text));
    
    for (const auto& shape : shapes) {
        shape->draw();
    }
    
    cout << "\n3. Using Positioned interface:" << endl;
    Positioned* positioned = &rect;
    positioned->move(5, 10);
    cout << "After move: ";
    rect.draw();
    
    cout << "\n4. Using Sizable interface:" << endl;
    Sizable* sizable = &circle;
    sizable->resize(2.0);
    cout << "After resize: ";
    circle.draw();
    
    cout << "\n5. Multiple inheritance benefits:" << endl;
    cout << "Rectangle area: " << rect.area() << endl;
    cout << "Circle area: " << circle.area() << endl;
    
    return 0;
}
```

---

## 5. **Practical Example: Database Access Layer**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <memory>
using namespace std;

// Base interface for all data sources
class DataSource {
protected:
    string connectionString;
    bool connected;
    
public:
    DataSource(string conn) : connectionString(conn), connected(false) {}
    
    virtual bool connect() = 0;
    virtual void disconnect() = 0;
    virtual bool executeQuery(const string& query) = 0;
    virtual vector<string> fetchResults() = 0;
    
    bool isConnected() const { return connected; }
    virtual ~DataSource() {}
};

// Transaction support interface
class Transactional {
public:
    virtual bool beginTransaction() = 0;
    virtual bool commit() = 0;
    virtual bool rollback() = 0;
    virtual ~Transactional() {}
};

// Caching support interface
class Cachable {
public:
    virtual void enableCache(bool enable) = 0;
    virtual void clearCache() = 0;
    virtual bool isCacheEnabled() const = 0;
    virtual ~Cachable() {}
};

// MySQL Database - implements multiple interfaces
class MySQLDatabase : public DataSource, public Transactional, public Cachable {
private:
    bool inTransaction;
    bool cacheEnabled;
    vector<string> cache;
    
public:
    MySQLDatabase(string conn) : DataSource(conn), inTransaction(false), cacheEnabled(false) {
        cout << "MySQLDatabase created: " << connectionString << endl;
    }
    
    bool connect() override {
        cout << "Connecting to MySQL: " << connectionString << endl;
        connected = true;
        return true;
    }
    
    void disconnect() override {
        if (connected) {
            cout << "Disconnecting from MySQL" << endl;
            connected = false;
        }
    }
    
    bool executeQuery(const string& query) override {
        if (!connected) return false;
        
        cout << "MySQL executing: " << query << endl;
        
        // Simulate caching
        if (cacheEnabled) {
            cache.push_back(query);
        }
        return true;
    }
    
    vector<string> fetchResults() override {
        vector<string> results = {"row1", "row2", "row3"};
        cout << "MySQL returning " << results.size() << " rows" << endl;
        return results;
    }
    
    // Transactional implementation
    bool beginTransaction() override {
        if (!connected || inTransaction) return false;
        inTransaction = true;
        cout << "MySQL transaction started" << endl;
        return true;
    }
    
    bool commit() override {
        if (!connected || !inTransaction) return false;
        inTransaction = false;
        cout << "MySQL transaction committed" << endl;
        return true;
    }
    
    bool rollback() override {
        if (!connected || !inTransaction) return false;
        inTransaction = false;
        cout << "MySQL transaction rolled back" << endl;
        return true;
    }
    
    // Cachable implementation
    void enableCache(bool enable) override {
        cacheEnabled = enable;
        cout << "MySQL cache " << (enable ? "enabled" : "disabled") << endl;
        if (!enable) clearCache();
    }
    
    void clearCache() override {
        cache.clear();
        cout << "MySQL cache cleared" << endl;
    }
    
    bool isCacheEnabled() const override {
        return cacheEnabled;
    }
};

// PostgreSQL Database - similar implementation
class PostgreSQLDatabase : public DataSource, public Transactional {
public:
    PostgreSQLDatabase(string conn) : DataSource(conn) {
        cout << "PostgreSQLDatabase created: " << connectionString << endl;
    }
    
    bool connect() override {
        cout << "Connecting to PostgreSQL: " << connectionString << endl;
        connected = true;
        return true;
    }
    
    void disconnect() override {
        if (connected) {
            cout << "Disconnecting from PostgreSQL" << endl;
            connected = false;
        }
    }
    
    bool executeQuery(const string& query) override {
        if (!connected) return false;
        cout << "PostgreSQL executing: " << query << endl;
        return true;
    }
    
    vector<string> fetchResults() override {
        vector<string> results = {"postgres_row1", "postgres_row2"};
        cout << "PostgreSQL returning " << results.size() << " rows" << endl;
        return results;
    }
    
    bool beginTransaction() override {
        if (!connected) return false;
        cout << "PostgreSQL transaction started" << endl;
        return true;
    }
    
    bool commit() override {
        if (!connected) return false;
        cout << "PostgreSQL transaction committed" << endl;
        return true;
    }
    
    bool rollback() override {
        if (!connected) return false;
        cout << "PostgreSQL transaction rolled back" << endl;
        return true;
    }
};

// Database manager using multiple interfaces
class DatabaseManager {
private:
    unique_ptr<DataSource> dataSource;
    
public:
    DatabaseManager(DataSource* ds) : dataSource(ds) {}
    
    void executeWithTransaction(const string& query1, const string& query2) {
        // Check if data source supports transactions
        Transactional* tx = dynamic_cast<Transactional*>(dataSource.get());
        
        if (tx) {
            tx->beginTransaction();
            dataSource->executeQuery(query1);
            dataSource->executeQuery(query2);
            tx->commit();
        } else {
            dataSource->executeQuery(query1);
            dataSource->executeQuery(query2);
        }
    }
    
    void enableCaching(bool enable) {
        Cachable* cache = dynamic_cast<Cachable*>(dataSource.get());
        if (cache) {
            cache->enableCache(enable);
        } else {
            cout << "Caching not supported" << endl;
        }
    }
    
    void query(const string& q) {
        dataSource->executeQuery(q);
        auto results = dataSource->fetchResults();
        for (const auto& row : results) {
            cout << "  " << row << endl;
        }
    }
};

int main() {
    cout << "=== Database Access Layer with Virtual Inheritance ===" << endl;
    
    cout << "\n1. MySQL Database (supports all features):" << endl;
    DatabaseManager mysql(new MySQLDatabase("mysql://localhost:3306/mydb"));
    mysql.connect();
    mysql.enableCaching(true);
    mysql.executeWithTransaction("UPDATE users SET active=1", "INSERT INTO logs VALUES('update')");
    mysql.query("SELECT * FROM users");
    
    cout << "\n2. PostgreSQL Database (supports transactions only):" << endl;
    DatabaseManager pg(new PostgreSQLDatabase("postgresql://localhost:5432/mydb"));
    pg.connect();
    pg.enableCaching(false);  // Not supported
    pg.executeWithTransaction("UPDATE products SET price=99", "INSERT INTO audit VALUES('update')");
    pg.query("SELECT * FROM products");
    
    return 0;
}
```

---

## 📊 Virtual Inheritance Summary

| Aspect | Without Virtual | With Virtual |
|--------|-----------------|--------------|
| **Base Copies** | Multiple copies | Single shared copy |
| **Constructor Order** | Multiple base calls | Single base call |
| **Memory** | Larger | Smaller (but with vptr overhead) |
| **Ambiguity** | Requires scope resolution | No ambiguity |
| **Performance** | Slightly faster | Slightly slower (vptr indirection) |

---

## ✅ Best Practices

1. **Use virtual inheritance** to solve diamond problem
2. **Call virtual base constructor** from most derived class
3. **Use interfaces** (pure virtual classes) with virtual inheritance
4. **Avoid deep hierarchies** with virtual inheritance
5. **Document virtual inheritance** clearly
6. **Consider performance** overhead of virtual inheritance

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Not calling virtual base constructor** | Default constructor used | Explicitly call in most derived |
| **Multiple initialization** | Confusion | Virtual base initialized once |
| **Casting issues** | Downcast complexity | Use dynamic_cast |
| **Memory overhead** | Larger object size | Acceptable trade-off |
| **Complex debugging** | Hard to trace | Keep hierarchies simple |

---

## ✅ Key Takeaways

1. **Virtual inheritance** ensures single shared copy of base class
2. **Constructor order**: Virtual base → Non-virtual bases → Derived
3. **Virtual base constructor** called from most derived class
4. **Solves diamond problem** elegantly
5. **Memory layout** includes vptr for virtual base access
6. **Used for interfaces** and multiple inheritance hierarchies
7. **Performance overhead** minimal compared to correctness

---