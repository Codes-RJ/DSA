# Delegating Constructors in C++ - Complete Guide

## 📖 Overview

Delegating constructors (C++11) allow one constructor to call another constructor of the same class. This feature reduces code duplication by centralizing common initialization logic. Delegation makes constructors more maintainable and ensures consistent initialization across multiple constructors.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Delegating Constructor** | Constructor that calls another constructor |
| **Target Constructor** | Constructor that performs the actual initialization |
| **Initialization List** | Where delegation occurs |
| **Delegation Chain** | Multiple constructors delegating to one master |

---

## 1. **Basic Delegating Constructors**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Point {
private:
    int x_, y_;
    
public:
    // Master constructor (target)
    Point(int x, int y) : x_(x), y_(y) {
        cout << "Master constructor: (" << x_ << ", " << y_ << ")" << endl;
    }
    
    // Delegating constructor: default
    Point() : Point(0, 0) {
        cout << "Delegating: default constructor" << endl;
    }
    
    // Delegating constructor: single value (makes it a line on x-axis)
    Point(int x) : Point(x, 0) {
        cout << "Delegating: single value constructor" << endl;
    }
    
    void display() const {
        cout << "Point: (" << x_ << ", " << y_ << ")" << endl;
    }
};

class Rectangle {
private:
    double width_, height_;
    
public:
    // Master constructor
    Rectangle(double w, double h) : width_(w), height_(h) {
        cout << "Master constructor: " << width_ << "x" << height_ << endl;
    }
    
    // Delegating: square
    Rectangle(double side) : Rectangle(side, side) {
        cout << "Delegating: square constructor" << endl;
    }
    
    // Delegating: default
    Rectangle() : Rectangle(1.0, 1.0) {
        cout << "Delegating: default constructor" << endl;
    }
    
    double area() const {
        return width_ * height_;
    }
    
    void display() const {
        cout << "Rectangle: " << width_ << "x" << height_ << ", Area: " << area() << endl;
    }
};

int main() {
    cout << "=== Basic Delegating Constructors ===" << endl;
    
    cout << "\n1. Point class:" << endl;
    Point p1;           // Delegates to Point(0,0)
    Point p2(5);        // Delegates to Point(5,0)
    Point p3(3, 4);     // Direct call to master
    
    p1.display();
    p2.display();
    p3.display();
    
    cout << "\n2. Rectangle class:" << endl;
    Rectangle r1;           // Delegates to Rectangle(1,1)
    Rectangle r2(5);        // Delegates to Rectangle(5,5)
    Rectangle r3(4, 6);     // Direct call to master
    
    r1.display();
    r2.display();
    r3.display();
    
    return 0;
}
```

**Output:**
```
=== Basic Delegating Constructors ===

1. Point class:
Master constructor: (0, 0)
Delegating: default constructor
Master constructor: (5, 0)
Delegating: single value constructor
Master constructor: (3, 4)
Point: (0, 0)
Point: (5, 0)
Point: (3, 4)

2. Rectangle class:
Master constructor: 1x1
Delegating: default constructor
Master constructor: 5x5
Delegating: square constructor
Master constructor: 4x6
Rectangle: 1x1, Area: 1
Rectangle: 5x5, Area: 25
Rectangle: 4x6, Area: 24
```

---

## 2. **Delegating with Validation**

```cpp
#include <iostream>
#include <string>
#include <stdexcept>
using namespace std;

class Date {
private:
    int day_, month_, year_;
    
    // Validation logic
    bool isValidDate(int d, int m, int y) {
        if (y < 1900 || y > 2100) return false;
        if (m < 1 || m > 12) return false;
        
        int daysInMonth[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        
        // Leap year check
        if (m == 2 && ((y % 4 == 0 && y % 100 != 0) || (y % 400 == 0))) {
            daysInMonth[1] = 29;
        }
        
        return (d >= 1 && d <= daysInMonth[m - 1]);
    }
    
public:
    // Master constructor with validation
    Date(int d, int m, int y) : day_(d), month_(m), year_(y) {
        if (!isValidDate(day_, month_, year_)) {
            throw invalid_argument("Invalid date");
        }
        cout << "Date created: " << day_ << "/" << month_ << "/" << year_ << endl;
    }
    
    // Delegating: today's date (default)
    Date() : Date(1, 1, 2000) {
        cout << "Default date (needs update)" << endl;
    }
    
    // Delegating: month and year only (day = 1)
    Date(int m, int y) : Date(1, m, y) {
        cout << "Date from month and year" << endl;
    }
    
    // Delegating: year only (Jan 1)
    Date(int y) : Date(1, 1, y) {
        cout << "Date from year only" << endl;
    }
    
    // Delegating: from string "dd/mm/yyyy"
    Date(const string& dateStr) : Date(
        stoi(dateStr.substr(0, 2)),
        stoi(dateStr.substr(3, 2)),
        stoi(dateStr.substr(6, 4))) {
        cout << "Date from string" << endl;
    }
    
    void display() const {
        cout << day_ << "/" << month_ << "/" << year_ << endl;
    }
};

class Employee {
private:
    int id_;
    string name_;
    double salary_;
    string department_;
    static int nextId_;
    
public:
    // Master constructor
    Employee(string name, double salary, string dept) 
        : id_(nextId_++), name_(name), salary_(salary), department_(dept) {
        if (salary < 0) throw invalid_argument("Salary cannot be negative");
        cout << "Employee created: " << name_ << " (ID: " << id_ << ")" << endl;
    }
    
    // Delegating: default department
    Employee(string name, double salary) : Employee(name, salary, "General") {
        cout << "Employee with default department" << endl;
    }
    
    // Delegating: zero salary (intern)
    Employee(string name, string dept) : Employee(name, 0.0, dept) {
        cout << "Intern employee" << endl;
    }
    
    // Delegating: name only
    Employee(string name) : Employee(name, 0.0, "General") {
        cout << "Employee with minimal info" << endl;
    }
    
    void display() const {
        cout << "ID: " << id_ << ", Name: " << name_ 
             << ", Salary: $" << salary_ << ", Dept: " << department_ << endl;
    }
};

int Employee::nextId_ = 1000;

int main() {
    cout << "=== Delegating with Validation ===" << endl;
    
    cout << "\n1. Date class with validation:" << endl;
    try {
        Date d1(15, 3, 2024);
        Date d2(5, 2024);
        Date d3(2024);
        Date d4("25/12/2024");
        
        // Invalid date - will throw exception
        // Date d5(31, 2, 2024);
    } catch (const exception& e) {
        cout << "Error: " << e.what() << endl;
    }
    
    cout << "\n2. Employee class:" << endl;
    Employee e1("Alice Johnson", 75000, "Engineering");
    Employee e2("Bob Smith", 65000);
    Employee e3("Charlie Brown", "Sales");
    Employee e4("Diana Prince");
    
    e1.display();
    e2.display();
    e3.display();
    e4.display();
    
    return 0;
}
```

---

## 3. **Delegation Chains**

```cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

class Circle {
private:
    double radius_;
    string color_;
    
public:
    // Master constructor (most parameters)
    Circle(double radius, string color) : radius_(radius), color_(color) {
        cout << "Master constructor: radius=" << radius_ << ", color=" << color_ << endl;
    }
    
    // Delegates to master
    Circle(double radius) : Circle(radius, "Black") {
        cout << "Delegating: radius only" << endl;
    }
    
    // Delegates to radius constructor
    Circle() : Circle(1.0) {
        cout << "Delegating: default constructor" << endl;
    }
    
    // Delegates to master with default radius
    Circle(string color) : Circle(1.0, color) {
        cout << "Delegating: color only" << endl;
    }
    
    double area() const {
        return M_PI * radius_ * radius_;
    }
    
    void display() const {
        cout << "Circle: radius=" << radius_ << ", color=" << color_ 
             << ", area=" << area() << endl;
    }
};

class Logger {
private:
    string prefix_;
    int level_;
    bool timestamp_;
    
public:
    // Ultimate master constructor
    Logger(string prefix, int level, bool timestamp) 
        : prefix_(prefix), level_(level), timestamp_(timestamp) {
        cout << "Master logger created: " << prefix_ << " (level=" << level_ << ")" << endl;
    }
    
    // Delegates to master
    Logger(string prefix, int level) : Logger(prefix, level, true) {
        cout << "Delegating: prefix and level" << endl;
    }
    
    // Delegates to prefix/level constructor
    Logger(string prefix) : Logger(prefix, 1) {
        cout << "Delegating: prefix only" << endl;
    }
    
    // Delegates to prefix constructor
    Logger() : Logger("INFO") {
        cout << "Delegating: default logger" << endl;
    }
    
    void log(const string& message) {
        if (timestamp_) {
            cout << "[TIME] ";
        }
        cout << "[" << prefix_ << "] " << message << endl;
    }
};

int main() {
    cout << "=== Delegation Chains ===" << endl;
    
    cout << "\n1. Circle delegation chain:" << endl;
    Circle c1;                  // Default → radius → master
    Circle c2("Red");           // Color → master
    Circle c3(5.0);             // Radius → master
    Circle c4(7.0, "Blue");     // Master directly
    
    c1.display();
    c2.display();
    c3.display();
    c4.display();
    
    cout << "\n2. Logger delegation chain:" << endl;
    Logger l1;                  // Default → prefix → level → master
    Logger l2("DEBUG");         // Prefix → level → master
    Logger l3("WARN", 2);       // Level → master
    Logger l4("ERROR", 3, false); // Master directly
    
    l1.log("System started");
    l2.log("Debug message");
    l3.log("Warning message");
    l4.log("Error occurred");
    
    return 0;
}
```

---

## 4. **Restrictions and Limitations**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Example {
private:
    int a_;
    int b_;
    const int c_;
    int& ref_;
    
public:
    // CORRECT: Delegating constructor
    Example() : Example(0, 0, 0, a_) {  // 'a_' used as reference
        cout << "Default delegating constructor" << endl;
    }
    
    // Master constructor
    Example(int a, int b, int c, int& r) : a_(a), b_(b), c_(c), ref_(r) {
        cout << "Master constructor: a=" << a_ << ", b=" << b_ 
             << ", c=" << c_ << ", ref=" << ref_ << endl;
    }
    
    // ERROR: Cannot delegate and have member initializers
    // Example(int x) : Example(x, 0, 0, a_), a_(x) { }  // Error!
    
    // CORRECT: Delegating only
    Example(int x) : Example(x, 0, 0, a_) {
        cout << "Single parameter delegating" << endl;
    }
    
    void display() const {
        cout << "a=" << a_ << ", b=" << b_ << ", c=" << c_ << ", ref=" << ref_ << endl;
    }
};

class CircularDelegation {
private:
    int value_;
    
public:
    // ERROR: Circular delegation - will cause infinite recursion
    // CircularDelegation() : CircularDelegation(0) { }
    // CircularDelegation(int x) : CircularDelegation() { }
    
    // CORRECT: Proper delegation chain
    CircularDelegation() : CircularDelegation(0) {
        cout << "Default constructor" << endl;
    }
    
    CircularDelegation(int x) : value_(x) {
        cout << "Parameterized constructor: " << value_ << endl;
    }
};

class Base {
public:
    Base(int x) {
        cout << "Base constructor: " << x << endl;
    }
};

class Derived : public Base {
public:
    // Cannot delegate to another constructor in same class AND call base
    // Derived() : Derived(0), Base(0) { }  // Error! Cannot delegate and initialize base
    
    // Correct: Delegate to another constructor that calls base
    Derived() : Derived(0) {
        cout << "Derived default constructor" << endl;
    }
    
    Derived(int x) : Base(x) {
        cout << "Derived parameterized constructor: " << x << endl;
    }
};

int main() {
    cout << "=== Restrictions and Limitations ===" << endl;
    
    cout << "\n1. Correct delegation:" << endl;
    Example e1;
    Example e2(42);
    e1.display();
    e2.display();
    
    cout << "\n2. Circular delegation prevention:" << endl;
    CircularDelegation cd1;
    CircularDelegation cd2(100);
    
    cout << "\n3. Delegation with inheritance:" << endl;
    Derived d1;
    Derived d2(50);
    
    cout << "\nImportant rules:" << endl;
    cout << "  ✓ Cannot delegate and have member initializers" << endl;
    cout << "  ✓ Cannot have circular delegation" << endl;
    cout << "  ✓ Delegation must be the only initializer" << endl;
    cout << "  ✓ Base class initialization must be in delegated constructor" << endl;
    
    return 0;
}
```

---

## 5. **Practical Example: Database Connection**

```cpp
#include <iostream>
#include <string>
#include <stdexcept>
#include <memory>
using namespace std;

class DatabaseConnection {
private:
    string host_;
    int port_;
    string database_;
    string username_;
    string password_;
    bool connected_;
    
    void validate() {
        if (host_.empty()) throw invalid_argument("Host cannot be empty");
        if (port_ <= 0 || port_ > 65535) throw invalid_argument("Invalid port");
        if (database_.empty()) throw invalid_argument("Database name cannot be empty");
    }
    
public:
    // Master constructor
    DatabaseConnection(string host, int port, string database, 
                       string username, string password) 
        : host_(host), port_(port), database_(database), 
          username_(username), password_(password), connected_(false) {
        validate();
        cout << "Database connection configured: " << host_ << ":" << port_ 
             << "/" << database_ << endl;
    }
    
    // Delegating: default port (3306)
    DatabaseConnection(string host, string database, string username, string password)
        : DatabaseConnection(host, 3306, database, username, password) {
        cout << "Using default port" << endl;
    }
    
    // Delegating: no authentication
    DatabaseConnection(string host, int port, string database)
        : DatabaseConnection(host, port, database, "guest", "") {
        cout << "Using guest authentication" << endl;
    }
    
    // Delegating: localhost with default port
    DatabaseConnection(string database, string username, string password)
        : DatabaseConnection("localhost", database, username, password) {
        cout << "Using localhost" << endl;
    }
    
    // Delegating: localhost, default port, no auth
    DatabaseConnection(string database)
        : DatabaseConnection("localhost", 3306, database, "guest", "") {
        cout << "Using minimal configuration" << endl;
    }
    
    void connect() {
        if (!connected_) {
            cout << "Connecting to " << host_ << ":" << port_ 
                 << "/" << database_ << " as " << username_ << endl;
            connected_ = true;
        }
    }
    
    void disconnect() {
        if (connected_) {
            cout << "Disconnected from database" << endl;
            connected_ = false;
        }
    }
    
    void query(const string& sql) {
        if (connected_) {
            cout << "Executing: " << sql << endl;
        } else {
            cout << "Not connected!" << endl;
        }
    }
};

class ConnectionPool {
private:
    DatabaseConnection connections_[3];
    int current_;
    
public:
    // Delegating constructors for pool initialization
    ConnectionPool() : ConnectionPool("pool_db") {}
    
    ConnectionPool(string database) : ConnectionPool(database, "pool_user", "pool_pass") {}
    
    ConnectionPool(string database, string user, string pass) 
        : connections_{
            DatabaseConnection(database, user, pass),
            DatabaseConnection(database, user, pass),
            DatabaseConnection(database, user, pass)
        }, current_(0) {
        cout << "Connection pool created with 3 connections to " << database << endl;
    }
    
    DatabaseConnection& getConnection() {
        current_ = (current_ + 1) % 3;
        return connections_[current_];
    }
};

int main() {
    cout << "=== Practical Example: Database Connection ===" << endl;
    
    cout << "\n1. Different connection configurations:" << endl;
    DatabaseConnection prod("prod.example.com", 5432, "production", "admin", "secret");
    DatabaseConnection dev("localhost", "development", "dev_user", "dev_pass");
    DatabaseConnection test("test.db", "test_user", "test_pass");
    DatabaseConnection local("local.db");
    
    prod.connect();
    dev.connect();
    test.connect();
    local.connect();
    
    cout << "\n2. Using connections:" << endl;
    prod.query("SELECT * FROM users");
    dev.query("INSERT INTO logs VALUES('test')");
    
    cout << "\n3. Connection pool:" << endl;
    ConnectionPool pool("app_db");
    
    auto& conn1 = pool.getConnection();
    auto& conn2 = pool.getConnection();
    auto& conn3 = pool.getConnection();
    auto& conn4 = pool.getConnection();  // Cycles back
    
    conn1.connect();
    conn1.query("SELECT * FROM products");
    
    return 0;
}
```

---

## 📊 Delegating Constructors Summary

| Feature | Description |
|---------|-------------|
| **Syntax** | `ClassName() : ClassName(args) { }` |
| **Purpose** | Reduce code duplication |
| **Target** | Constructor that does actual initialization |
| **Chain** | Multiple constructors can delegate to one master |
| **Restriction** | Cannot have member initializers when delegating |

---

## ✅ Best Practices

1. **Use delegating constructors** to avoid code duplication
2. **Make master constructor** the most parameterized one
3. **Keep validation in master constructor** only
4. **Avoid circular delegation** (infinite recursion)
5. **Document delegation chains** for clarity
6. **Use factory methods** alongside delegation for complex creation

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Circular delegation** | Infinite recursion | Ensure delegation chain terminates |
| **Member initializers with delegation** | Compiler error | Delegate only, no member initializers |
| **Delegation in base class** | Base initialized multiple times | Let delegated constructor handle base |
| **Logic duplication** | Validation in multiple places | Put all validation in master constructor |

---

## ✅ Key Takeaways

1. **Delegating constructors** call other constructors in same class
2. **Master constructor** contains common initialization logic
3. **Cannot mix** delegation with member initializers
4. **Avoid circular delegation** (A → B → A)
5. **C++11 feature** - improves code maintainability
6. **Validation centralized** in master constructor
7. **Reduces code duplication** significantly

---
---

## Next Step

- Go to [08_Inheriting_Constructors.md](08_Inheriting_Constructors.md) to continue with Inheriting Constructors.
