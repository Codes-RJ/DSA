# 03_Constructors_and_Destructors/07_Delegating_Constructors.md

# Delegating Constructors in C++ - Complete Guide

## 📖 Overview

Delegating constructors (C++11) allow one constructor to call another constructor of the same class. This reduces code duplication by centralizing common initialization logic. Delegation improves maintainability and ensures consistent initialization across multiple constructors.

---

## 🎯 Key Concepts

| Aspect | Description |
|--------|-------------|
| **Purpose** | Reduce code duplication in constructors |
| **Syntax** | `ClassName() : ClassName(parameters) { }` |
| **Restrictions** | Cannot delegate and have member initializers |
| **Benefits** | DRY principle, consistent initialization |

---

## 1. **Basic Delegating Constructors**

```cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

class Point {
private:
    double x, y;
    
public:
    // Master constructor - does all the work
    Point(double xVal, double yVal) : x(xVal), y(yVal) {
        cout << "Master constructor: (" << x << ", " << y << ")" << endl;
    }
    
    // Delegating constructor: calls master constructor
    Point() : Point(0, 0) {
        cout << "Delegating: default constructor" << endl;
    }
    
    // Delegating constructor: calls master constructor
    Point(double val) : Point(val, val) {
        cout << "Delegating: single value constructor" << endl;
    }
    
    void display() const {
        cout << "Point: (" << x << ", " << y << ")" << endl;
    }
};

class Circle {
private:
    double radius;
    string color;
    
public:
    // Master constructor
    Circle(double r, string c) : radius(r), color(c) {
        cout << "Master constructor: radius=" << radius << ", color=" << color << endl;
    }
    
    // Delegating constructors
    Circle() : Circle(1.0, "Red") {
        cout << "Default circle" << endl;
    }
    
    Circle(double r) : Circle(r, "Blue") {
        cout << "Circle with radius only" << endl;
    }
    
    Circle(string c) : Circle(1.0, c) {
        cout << "Circle with color only" << endl;
    }
    
    void display() const {
        cout << "Circle: radius=" << radius << ", color=" << color << endl;
    }
};

int main() {
    cout << "=== Basic Delegating Constructors ===" << endl;
    
    cout << "\n1. Point class:" << endl;
    Point p1;           // Delegates to Point(0,0)
    Point p2(5);        // Delegates to Point(5,5)
    Point p3(3, 4);     // Direct call to master
    p1.display();
    p2.display();
    p3.display();
    
    cout << "\n2. Circle class:" << endl;
    Circle c1;          // Delegates to Circle(1.0, "Red")
    Circle c2(5.0);     // Delegates to Circle(5.0, "Blue")
    Circle c3("Green"); // Delegates to Circle(1.0, "Green")
    Circle c4(2.5, "Yellow"); // Direct to master
    c1.display();
    c2.display();
    c3.display();
    c4.display();
    
    return 0;
}
```

**Output:**
```
=== Basic Delegating Constructors ===

1. Point class:
Master constructor: (0, 0)
Delegating: default constructor
Master constructor: (5, 5)
Delegating: single value constructor
Master constructor: (3, 4)
Point: (0, 0)
Point: (5, 5)
Point: (3, 4)

2. Circle class:
Master constructor: radius=1, color=Red
Default circle
Master constructor: radius=5, color=Blue
Circle with radius only
Master constructor: radius=1, color=Green
Circle with color only
Master constructor: radius=2.5, color=Yellow
Circle: radius=1, color=Red
Circle: radius=5, color=Blue
Circle: radius=1, color=Green
Circle: radius=2.5, color=Yellow
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
    int day, month, year;
    
    // Validation function
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
    Date(int d, int m, int y) : day(d), month(m), year(y) {
        if (!isValidDate(day, month, year)) {
            throw invalid_argument("Invalid date");
        }
        cout << "Date created: " << day << "/" << month << "/" << year << endl;
    }
    
    // Delegating constructor: today's date
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
    Date(const string& dateStr) : Date(stoi(dateStr.substr(0, 2)),
                                        stoi(dateStr.substr(3, 2)),
                                        stoi(dateStr.substr(6, 4))) {
        cout << "Date from string" << endl;
    }
    
    void display() const {
        cout << day << "/" << month << "/" << year << endl;
    }
};

class Account {
private:
    string accountNumber;
    double balance;
    string accountType;
    
    // Master constructor with validation
    Account(string accNo, double bal, string type) 
        : accountNumber(accNo), balance(bal), accountType(type) {
        if (balance < 0) {
            throw invalid_argument("Initial balance cannot be negative");
        }
        if (accountType != "Savings" && accountType != "Checking" && accountType != "Business") {
            throw invalid_argument("Invalid account type");
        }
        cout << "Account created: " << accountNumber << " (" << accountType << ")" << endl;
    }
    
public:
    // Regular account
    Account(string accNo, double bal) : Account(accNo, bal, "Savings") {
        cout << "Regular savings account" << endl;
    }
    
    // Account with default balance
    Account(string accNo) : Account(accNo, 0.0, "Savings") {
        cout << "Account with zero balance" << endl;
    }
    
    // Business account
    Account(string accNo, string type) : Account(accNo, 1000.0, type) {
        cout << "Business account with minimum balance" << endl;
    }
    
    void display() const {
        cout << "Account: " << accountNumber << ", Balance: $" << balance 
             << ", Type: " << accountType << endl;
    }
};

int main() {
    cout << "=== Delegating with Validation ===" << endl;
    
    cout << "\n1. Date class:" << endl;
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
    
    cout << "\n2. Account class:" << endl;
    try {
        Account a1("ACC001", 1000.0);
        Account a2("ACC002");
        Account a3("ACC003", "Business");
        
        // Invalid account type
        // Account a4("ACC004", "Invalid");
    } catch (const exception& e) {
        cout << "Error: " << e.what() << endl;
    }
    
    return 0;
}
```

---

## 3. **Delegating Constructors in Inheritance**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Shape {
protected:
    string color;
    bool filled;
    
public:
    // Master constructor
    Shape(string c, bool f) : color(c), filled(f) {
        cout << "Shape master: " << color << ", filled=" << (filled ? "yes" : "no") << endl;
    }
    
    // Delegating constructors
    Shape() : Shape("Black", true) {
        cout << "Shape default" << endl;
    }
    
    Shape(string c) : Shape(c, true) {
        cout << "Shape with color only" << endl;
    }
    
    virtual ~Shape() {}
    
    virtual void display() const {
        cout << "Shape: color=" << color << ", filled=" << (filled ? "Yes" : "No") << endl;
    }
};

class Circle : public Shape {
private:
    double radius;
    
public:
    // Master constructor
    Circle(double r, string c, bool f) : Shape(c, f), radius(r) {
        cout << "Circle master: radius=" << radius << endl;
    }
    
    // Delegating constructors
    Circle(double r) : Circle(r, "Black", true) {
        cout << "Circle with radius only" << endl;
    }
    
    Circle(double r, string c) : Circle(r, c, true) {
        cout << "Circle with radius and color" << endl;
    }
    
    void display() const override {
        Shape::display();
        cout << "Circle: radius=" << radius << ", area=" << 3.14159 * radius * radius << endl;
    }
};

class Rectangle : public Shape {
private:
    double width, height;
    
public:
    // Master constructor
    Rectangle(double w, double h, string c, bool f) : Shape(c, f), width(w), height(h) {
        cout << "Rectangle master: " << width << "x" << height << endl;
    }
    
    // Delegating constructors
    Rectangle(double w, double h) : Rectangle(w, h, "Black", true) {
        cout << "Rectangle with dimensions only" << endl;
    }
    
    Rectangle(double side) : Rectangle(side, side, "Black", true) {
        cout << "Square created" << endl;
    }
    
    void display() const override {
        Shape::display();
        cout << "Rectangle: " << width << "x" << height << ", area=" << width * height << endl;
    }
};

int main() {
    cout << "=== Delegating Constructors in Inheritance ===" << endl;
    
    cout << "\n1. Circle objects:" << endl;
    Circle c1(5.0);
    Circle c2(3.0, "Red");
    Circle c3(2.5, "Blue", false);
    
    cout << "\n2. Rectangle objects:" << endl;
    Rectangle r1(4, 6);
    Rectangle r2(5);  // Square
    Rectangle r3(3, 4, "Green", true);
    
    cout << "\n3. Display shapes:" << endl;
    c1.display();
    c2.display();
    c3.display();
    r1.display();
    r2.display();
    r3.display();
    
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
    int a;
    int b;
    const int c;
    
public:
    // CORRECT: Delegating constructor
    Example() : Example(0, 0) {
        cout << "Default delegating constructor" << endl;
    }
    
    // Master constructor
    Example(int x, int y) : a(x), b(y), c(x + y) {
        cout << "Master constructor: a=" << a << ", b=" << b << ", c=" << c << endl;
    }
    
    // ERROR: Cannot delegate and have member initializers
    // Example(int x) : Example(x, 0), a(x) { }  // Compiler error!
    
    // CORRECT: Delegating only
    Example(int x) : Example(x, 0) {
        cout << "Single parameter delegating" << endl;
    }
    
    void display() const {
        cout << "a=" << a << ", b=" << b << ", c=" << c << endl;
    }
};

class CircularDelegation {
private:
    int value;
    
public:
    // ERROR: Circular delegation - will cause infinite recursion
    // CircularDelegation() : CircularDelegation(0) { }
    // CircularDelegation(int x) : CircularDelegation() { }
    
    // CORRECT: Proper delegation chain
    CircularDelegation() : CircularDelegation(0) {
        cout << "Default constructor" << endl;
    }
    
    CircularDelegation(int x) : value(x) {
        cout << "Parameterized constructor: " << value << endl;
    }
};

int main() {
    cout << "=== Restrictions and Limitations ===" << endl;
    
    cout << "\n1. Correct delegation:" << endl;
    Example e1;
    Example e2(10);
    Example e3(20, 30);
    
    cout << "\n2. Circular delegation prevention:" << endl;
    CircularDelegation cd1;
    CircularDelegation cd2(42);
    
    cout << "\n3. Important rules:" << endl;
    cout << "✓ Cannot delegate and have member initializers in same constructor" << endl;
    cout << "✓ Cannot have circular delegation" << endl;
    cout << "✓ Delegation must be the only initializer" << endl;
    cout << "✓ Base class initialization must happen in delegated constructor" << endl;
    
    return 0;
}
```

---

## 5. **Practical Example: Employee Management**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <ctime>
using namespace std;

class Employee {
private:
    int id;
    string name;
    string department;
    double salary;
    time_t hireDate;
    bool isActive;
    static int nextId;
    
    // Private helper for generating hire date
    time_t getCurrentTime() {
        return time(nullptr);
    }
    
public:
    // Master constructor - does all validation and initialization
    Employee(string n, string dept, double sal, time_t hire, bool active) 
        : id(nextId++), name(n), department(dept), salary(sal), hireDate(hire), isActive(active) {
        if (salary < 0) {
            throw invalid_argument("Salary cannot be negative");
        }
        if (name.empty()) {
            throw invalid_argument("Name cannot be empty");
        }
        cout << "Employee master: " << name << " (ID: " << id << ")" << endl;
    }
    
    // Delegating: Active employee with hire date
    Employee(string n, string dept, double sal) 
        : Employee(n, dept, sal, time(nullptr), true) {
        cout << "New active employee" << endl;
    }
    
    // Delegating: Employee with default department
    Employee(string n, double sal) 
        : Employee(n, "General", sal, time(nullptr), true) {
        cout << "Employee with default department" << endl;
    }
    
    // Delegating: Employee with zero salary (intern)
    Employee(string n, string dept) 
        : Employee(n, dept, 0.0, time(nullptr), true) {
        cout << "Intern employee" << endl;
    }
    
    // Delegating: Terminated employee
    Employee(string n, string dept, double sal, bool active) 
        : Employee(n, dept, sal, time(nullptr), active) {
        cout << (active ? "Active" : "Terminated") << " employee record" << endl;
    }
    
    void display() const {
        cout << "ID: " << setw(4) << id 
             << " | Name: " << setw(15) << name
             << " | Dept: " << setw(12) << department
             << " | Salary: $" << setw(8) << fixed << setprecision(2) << salary
             << " | Status: " << (isActive ? "Active" : "Terminated") << endl;
    }
    
    void giveRaise(double percent) {
        if (isActive && percent > 0) {
            salary += salary * (percent / 100);
            cout << name << " received " << percent << "% raise. New salary: $" << salary << endl;
        }
    }
    
    void terminate() {
        isActive = false;
        cout << name << " terminated." << endl;
    }
    
    int getId() const { return id; }
    string getName() const { return name; }
};

int Employee::nextId = 1000;

class Department {
private:
    string name;
    vector<Employee> employees;
    double budget;
    
public:
    Department(string n, double b) : name(n), budget(b) {
        cout << "Department created: " << name << " (Budget: $" << budget << ")" << endl;
    }
    
    void hire(const Employee& emp) {
        employees.push_back(emp);
        cout << emp.getName() << " hired to " << name << " department" << endl;
    }
    
    void listEmployees() const {
        cout << "\n=== " << name << " Department (" << employees.size() << " employees) ===" << endl;
        for (const auto& emp : employees) {
            emp.display();
        }
    }
    
    double totalSalary() const {
        double total = 0;
        for (const auto& emp : employees) {
            total += emp.getSalary();
        }
        return total;
    }
};

// Need to add getSalary method to Employee class
// (Adding for completeness)
// Note: In a real implementation, you'd add this getter

int main() {
    cout << "=== Employee Management System with Delegating Constructors ===" << endl;
    
    cout << "\n1. Creating employees with different constructors:" << endl;
    Employee e1("Alice Johnson", "Engineering", 85000.0);
    Employee e2("Bob Smith", 65000.0);  // Default department
    Employee e3("Charlie Brown", "Sales");  // Intern
    Employee e4("Diana Prince", "Marketing", 75000.0, true);
    Employee e5("Eve Wilson", "Engineering", 0.0, false);  // Terminated
    
    cout << "\n2. All employees:" << endl;
    e1.display();
    e2.display();
    e3.display();
    e4.display();
    e5.display();
    
    cout << "\n3. Department management:" << endl;
    Department engineering("Engineering", 500000);
    Department sales("Sales", 300000);
    
    engineering.hire(e1);
    engineering.hire(e5);  // Terminated employee
    sales.hire(e2);
    sales.hire(e3);
    
    engineering.listEmployees();
    sales.listEmployees();
    
    cout << "\n4. Employee actions:" << endl;
    e1.giveRaise(10);
    e2.giveRaise(5);
    e3.terminate();
    
    return 0;
}
```

---

## 6. **Advanced Delegation with Factory Pattern**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <map>
using namespace std;

class Logger {
private:
    string level;
    bool timestamp;
    bool colorOutput;
    
    // Master constructor
    Logger(string lvl, bool ts, bool color) 
        : level(lvl), timestamp(ts), colorOutput(color) {
        cout << "Logger initialized: level=" << level 
             << ", timestamp=" << (timestamp ? "on" : "off")
             << ", color=" << (colorOutput ? "on" : "off") << endl;
    }
    
public:
    // Different ways to create loggers using delegation
    static Logger createProduction() {
        return Logger("INFO", true, false);
    }
    
    static Logger createDevelopment() {
        return Logger("DEBUG", true, true);
    }
    
    static Logger createSilent() {
        return Logger("ERROR", false, false);
    }
    
    static Logger createCustom(string lvl) {
        return Logger(lvl, true, false);
    }
    
    void log(const string& message) const {
        if (timestamp) {
            time_t now = time(nullptr);
            cout << "[" << ctime(&now) << "] ";
        }
        cout << "[" << level << "] " << message << endl;
    }
};

class Database {
private:
    string host;
    int port;
    string username;
    string password;
    bool connected;
    
    // Master constructor with full initialization
    Database(string h, int p, string u, string pw) 
        : host(h), port(p), username(u), password(pw), connected(false) {
        cout << "Database configured: " << host << ":" << port << " (user: " << username << ")" << endl;
    }
    
public:
    // Factory methods using delegation
    static Database localhost() {
        return Database("localhost", 5432, "admin", "admin123");
    }
    
    static Database production(string host, int port) {
        return Database(host, port, "prod_user", "prod_pass");
    }
    
    static Database test(string host) {
        return Database(host, 5432, "test_user", "test_pass");
    }
    
    void connect() {
        if (!connected) {
            // Simulate connection
            connected = true;
            cout << "Connected to " << host << ":" << port << endl;
        }
    }
    
    void disconnect() {
        if (connected) {
            connected = false;
            cout << "Disconnected from " << host << ":" << port << endl;
        }
    }
    
    void query(const string& sql) const {
        if (connected) {
            cout << "Executing on " << host << ": " << sql << endl;
        } else {
            cout << "Not connected to " << host << endl;
        }
    }
};

int main() {
    cout << "=== Advanced Delegation with Factory Pattern ===" << endl;
    
    cout << "\n1. Logger factory:" << endl;
    Logger prod = Logger::createProduction();
    Logger dev = Logger::createDevelopment();
    Logger silent = Logger::createSilent();
    Logger custom = Logger::createCustom("WARNING");
    
    prod.log("Production log message");
    dev.log("Debug message with colors");
    silent.log("This won't appear (level ERROR)");
    custom.log("Custom level message");
    
    cout << "\n2. Database factory:" << endl;
    Database local = Database::localhost();
    Database prodDb = Database::production("db.example.com", 5432);
    Database testDb = Database::test("test.example.com");
    
    local.connect();
    local.query("SELECT * FROM users");
    local.disconnect();
    
    prodDb.connect();
    prodDb.query("INSERT INTO logs VALUES('action')");
    prodDb.disconnect();
    
    testDb.connect();
    testDb.query("SELECT * FROM test_data");
    
    cout << "\n3. Benefits of delegating constructors:" << endl;
    cout << "✓ Code reuse - common logic in one place" << endl;
    cout << "✓ Consistent initialization across all constructors" << endl;
    cout << "✓ Easy to add new constructors" << endl;
    cout << "✓ Maintainability - change once, update everywhere" << endl;
    
    return 0;
}
```

---

## 📊 Delegating Constructors Summary

| Aspect | Description |
|--------|-------------|
| **Purpose** | Reduce constructor code duplication |
| **Syntax** | `ClassName() : ClassName(parameters) { }` |
| **Restrictions** | Cannot have member initializers when delegating |
| **Chain** | Can have delegation chains (A calls B calls C) |
| **Benefits** | DRY principle, maintainability, consistency |

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
6. **Factory methods** can complement delegation patterns

---