# Constructor Overloading in C++ - Complete Guide

## 📖 Overview

Constructor overloading allows a class to have multiple constructors with different parameter lists. This provides flexibility in object creation, allowing objects to be initialized in different ways. Constructor overloading is a form of compile-time polymorphism that enables multiple initialization patterns.

---

## 🎯 Key Concepts

| Aspect | Description |
|--------|-------------|
| **Purpose** | Provide multiple ways to initialize objects |
| **Rules** | Different parameter count, types, or order |
| **Resolution** | Compiler selects best match based on arguments |
| **Benefits** | Flexibility, convenience, backward compatibility |

---

## 1. **Basic Constructor Overloading**

```cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

class Rectangle {
private:
    double length;
    double width;
    
public:
    // Constructor 1: Default
    Rectangle() : length(1.0), width(1.0) {
        cout << "Default constructor: 1x1 rectangle" << endl;
    }
    
    // Constructor 2: Square (single parameter)
    Rectangle(double side) : length(side), width(side) {
        cout << "Square constructor: " << side << "x" << side << endl;
    }
    
    // Constructor 3: Rectangle (two parameters)
    Rectangle(double l, double w) : length(l), width(w) {
        cout << "Rectangle constructor: " << l << "x" << w << endl;
    }
    
    // Constructor 4: From string
    Rectangle(const string& dimensions) {
        size_t comma = dimensions.find(',');
        length = stod(dimensions.substr(0, comma));
        width = stod(dimensions.substr(comma + 1));
        cout << "String constructor: " << length << "x" << width << endl;
    }
    
    double area() const { return length * width; }
    double perimeter() const { return 2 * (length + width); }
    
    void display() const {
        cout << "Rectangle: " << length << " x " << width 
             << ", Area: " << area() << ", Perimeter: " << perimeter() << endl;
    }
};

int main() {
    cout << "=== Constructor Overloading Demo ===" << endl;
    
    cout << "\n1. Default constructor:" << endl;
    Rectangle r1;
    r1.display();
    
    cout << "\n2. Square constructor:" << endl;
    Rectangle r2(5);
    r2.display();
    
    cout << "\n3. Rectangle constructor:" << endl;
    Rectangle r3(4, 6);
    r3.display();
    
    cout << "\n4. String constructor:" << endl;
    Rectangle r4("7,3");
    r4.display();
    
    return 0;
}
```

**Output:**
```
=== Constructor Overloading Demo ===

1. Default constructor:
Default constructor: 1x1 rectangle
Rectangle: 1 x 1, Area: 1, Perimeter: 4

2. Square constructor:
Square constructor: 5x5
Rectangle: 5 x 5, Area: 25, Perimeter: 20

3. Rectangle constructor:
Rectangle constructor: 4x6
Rectangle: 4 x 6, Area: 24, Perimeter: 20

4. String constructor:
String constructor: 7x3
Rectangle: 7 x 3, Area: 21, Perimeter: 20
```

---

## 2. **Overloading with Different Parameter Types**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Date {
private:
    int day, month, year;
    
public:
    // Constructor 1: Day, month, year (integers)
    Date(int d, int m, int y) : day(d), month(m), year(y) {
        cout << "Date(int,int,int): " << day << "/" << month << "/" << year << endl;
    }
    
    // Constructor 2: Month, year (day defaults to 1)
    Date(int m, int y) : day(1), month(m), year(y) {
        cout << "Date(int,int): " << day << "/" << month << "/" << year << endl;
    }
    
    // Constructor 3: String format "dd/mm/yyyy"
    Date(const string& dateStr) {
        sscanf(dateStr.c_str(), "%d/%d/%d", &day, &month, &year);
        cout << "Date(string): " << day << "/" << month << "/" << year << endl;
    }
    
    // Constructor 4: Timestamp (time_t)
    Date(time_t timestamp) {
        struct tm* timeinfo = localtime(&timestamp);
        day = timeinfo->tm_mday;
        month = timeinfo->tm_mon + 1;
        year = timeinfo->tm_year + 1900;
        cout << "Date(time_t): " << day << "/" << month << "/" << year << endl;
    }
    
    void display() const {
        cout << day << "/" << month << "/" << year << endl;
    }
};

class Complex {
private:
    double real, imag;
    
public:
    // Constructor 1: Both real and imaginary
    Complex(double r, double i) : real(r), imag(i) {
        cout << "Complex(double,double): " << real << " + " << imag << "i" << endl;
    }
    
    // Constructor 2: Real only (imag = 0)
    Complex(double r) : real(r), imag(0) {
        cout << "Complex(double): " << real << " + 0i" << endl;
    }
    
    // Constructor 3: No arguments (0 + 0i)
    Complex() : real(0), imag(0) {
        cout << "Complex(): 0 + 0i" << endl;
    }
    
    // Constructor 4: From polar coordinates
    static Complex fromPolar(double magnitude, double angle) {
        return Complex(magnitude * cos(angle), magnitude * sin(angle));
    }
    
    void display() const {
        cout << real << " + " << imag << "i" << endl;
    }
};

int main() {
    cout << "=== Constructor Overloading with Different Types ===" << endl;
    
    cout << "\n1. Date class:" << endl;
    Date d1(15, 3, 2024);           // int,int,int
    Date d2(5, 2024);                // int,int
    Date d3("25/12/2024");           // string
    time_t now = time(nullptr);
    Date d4(now);                    // time_t
    
    cout << "\n2. Complex class:" << endl;
    Complex c1(3, 4);                // double,double
    Complex c2(5);                   // double
    Complex c3;                      // default
    Complex c4 = Complex::fromPolar(5, 3.14159/4);  // static factory
    
    return 0;
}
```

---

## 3. **Overloading with Different Parameter Count**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Student {
private:
    string name;
    int rollNumber;
    double marks;
    string course;
    
public:
    // Constructor 1: All details
    Student(string n, int r, double m, string c) 
        : name(n), rollNumber(r), marks(m), course(c) {
        cout << "Student(full): " << name << endl;
    }
    
    // Constructor 2: Without course (default course)
    Student(string n, int r, double m) 
        : Student(n, r, m, "General") {  // Delegating constructor
        cout << "Student(no course): " << name << endl;
    }
    
    // Constructor 3: Without marks (marks = 0)
    Student(string n, int r) 
        : Student(n, r, 0.0, "General") {
        cout << "Student(no marks): " << name << endl;
    }
    
    // Constructor 4: Name only (default roll)
    Student(string n) 
        : Student(n, 0, 0.0, "General") {
        cout << "Student(name only): " << name << endl;
    }
    
    // Constructor 5: Default student
    Student() : Student("Unknown", 0, 0.0, "General") {
        cout << "Student(default): " << name << endl;
    }
    
    void display() const {
        cout << "Name: " << name << ", Roll: " << rollNumber 
             << ", Marks: " << marks << ", Course: " << course << endl;
    }
};

class Point {
private:
    double x, y, z;
    
public:
    // Constructor 1: 3D point
    Point(double x, double y, double z) : x(x), y(y), z(z) {
        cout << "3D Point: (" << x << ", " << y << ", " << z << ")" << endl;
    }
    
    // Constructor 2: 2D point (z=0)
    Point(double x, double y) : Point(x, y, 0) {
        cout << "2D Point: (" << x << ", " << y << ")" << endl;
    }
    
    // Constructor 3: 1D point (y=0, z=0)
    Point(double x) : Point(x, 0, 0) {
        cout << "1D Point: (" << x << ")" << endl;
    }
    
    // Constructor 4: Origin
    Point() : Point(0, 0, 0) {
        cout << "Origin Point" << endl;
    }
    
    double distance() const {
        return sqrt(x*x + y*y + z*z);
    }
    
    void display() const {
        cout << "(" << x << ", " << y << ", " << z << ") distance: " << distance() << endl;
    }
};

int main() {
    cout << "=== Constructor Overloading with Different Parameter Count ===" << endl;
    
    cout << "\n1. Student class:" << endl;
    Student s1("Alice", 101, 85.5, "CS");
    Student s2("Bob", 102, 78.0);
    Student s3("Charlie", 103);
    Student s4("Diana");
    Student s5;
    
    cout << "\n2. Point class:" << endl;
    Point p1(3, 4, 5);
    Point p2(3, 4);
    Point p3(5);
    Point p4;
    
    return 0;
}
```

---

## 4. **Ambiguity in Constructor Overloading**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Ambiguity {
private:
    int intValue;
    double doubleValue;
    string stringValue;
    
public:
    // Constructor 1: int
    Ambiguity(int i) : intValue(i), doubleValue(0), stringValue("int") {
        cout << "Int constructor: " << i << endl;
    }
    
    // Constructor 2: double
    Ambiguity(double d) : intValue(0), doubleValue(d), stringValue("double") {
        cout << "Double constructor: " << d << endl;
    }
    
    // Constructor 3: string
    Ambiguity(const string& s) : intValue(0), doubleValue(0), stringValue(s) {
        cout << "String constructor: " << s << endl;
    }
    
    // Constructor 4: int and double
    Ambiguity(int i, double d) : intValue(i), doubleValue(d), stringValue("int,double") {
        cout << "Int,Double constructor: " << i << ", " << d << endl;
    }
    
    void display() const {
        cout << "Value: " << stringValue << " (" << intValue << ", " << doubleValue << ")" << endl;
    }
};

class Ambiguous {
public:
    // Ambiguous overloads
    Ambiguous(int i) { cout << "Int constructor" << endl; }
    Ambiguous(double d) { cout << "Double constructor" << endl; }
    
    // This would cause ambiguity with int version
    // Ambiguous(long l) { cout << "Long constructor" << endl; }
    
    // This would cause ambiguity with double version
    // Ambiguous(float f) { cout << "Float constructor" << endl; }
};

int main() {
    cout << "=== Ambiguity in Constructor Overloading ===" << endl;
    
    cout << "\n1. Resolving ambiguity:" << endl;
    Ambiguity a1(10);           // int
    Ambiguity a2(10.5);         // double
    Ambiguity a3("Hello");      // string
    Ambiguity a4(10, 20.5);     // int, double
    
    cout << "\n2. Problematic cases:" << endl;
    // Ambiguity a5(10.0f);      // float -> ambiguous between int and double?
    // Ambiguity a6('A');         // char -> could be int or double
    // Ambiguity a7(true);        // bool -> could be int or double
    
    cout << "\n3. Best practices to avoid ambiguity:" << endl;
    cout << "✓ Use explicit constructor for single-parameter constructors" << endl;
    cout << "✓ Avoid overloading with types that have implicit conversions" << endl;
    cout << "✓ Use factory methods instead of ambiguous overloads" << endl;
    
    // Using explicit conversion to resolve ambiguity
    Ambiguity a8(static_cast<int>(10.0f));
    Ambiguity a9(static_cast<double>('A'));
    
    return 0;
}
```

---

## 5. **Constructor Overloading with Default Arguments**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Logger {
private:
    string prefix;
    int level;
    bool timestamp;
    
public:
    // Constructor with all defaults
    Logger(string p = "INFO", int l = 1, bool ts = true) 
        : prefix(p), level(l), timestamp(ts) {
        cout << "Logger created: " << prefix << " (level=" << level << ", timestamp=" << timestamp << ")" << endl;
    }
    
    void log(const string& message) const {
        if (timestamp) {
            cout << "[TIME] ";
        }
        cout << "[" << prefix << "] " << message << endl;
    }
};

class Config {
private:
    string host;
    int port;
    string protocol;
    int timeout;
    
public:
    // Constructor with default arguments
    Config(string h = "localhost", int p = 8080, string prot = "http", int t = 30)
        : host(h), port(p), protocol(prot), timeout(t) {
        cout << "Config created: " << host << ":" << port << " (" << protocol << ", timeout=" << timeout << ")" << endl;
    }
    
    void display() const {
        cout << "Host: " << host << ", Port: " << port << ", Protocol: " << protocol << ", Timeout: " << timeout << endl;
    }
};

int main() {
    cout << "=== Constructor Overloading with Default Arguments ===" << endl;
    
    cout << "\n1. Logger class:" << endl;
    Logger l1;                    // All defaults
    Logger l2("DEBUG");           // Custom prefix
    Logger l3("ERROR", 2);        // Custom prefix and level
    Logger l4("WARN", 1, false);  // All custom
    
    l1.log("System started");
    l2.log("Debug message");
    l3.log("Error occurred");
    l4.log("Warning message");
    
    cout << "\n2. Config class:" << endl;
    Config c1;                    // All defaults
    Config c2("192.168.1.100");   // Custom host
    Config c3("example.com", 443); // Custom host and port
    Config c4("api.example.com", 8443, "https", 60); // All custom
    
    cout << "\nNote: Default arguments can replace multiple overloaded constructors" << endl;
    cout << "But be careful: cannot combine default arguments with overloaded constructors that would cause ambiguity" << endl;
    
    return 0;
}
```

---

## 6. **Practical Example: Employee Management System**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
using namespace std;

class Employee {
private:
    int id;
    string name;
    string department;
    double salary;
    bool isActive;
    static int nextId;
    
public:
    // Constructor 1: Full details
    Employee(string n, string dept, double sal) 
        : id(nextId++), name(n), department(dept), salary(sal), isActive(true) {
        cout << "Employee created: " << name << " (ID: " << id << ")" << endl;
    }
    
    // Constructor 2: Name and department only (salary default 0)
    Employee(string n, string dept) 
        : Employee(n, dept, 0.0) {
        cout << "Employee (no salary): " << name << endl;
    }
    
    // Constructor 3: Name only (default department "General", salary 0)
    Employee(string n) 
        : Employee(n, "General", 0.0) {
        cout << "Employee (name only): " << name << endl;
    }
    
    // Constructor 4: Default employee
    Employee() 
        : Employee("Unknown", "General", 0.0) {
        cout << "Default employee created" << endl;
    }
    
    // Constructor 5: From CSV string
    Employee(const string& csv) {
        size_t pos1 = csv.find(',');
        size_t pos2 = csv.find(',', pos1 + 1);
        size_t pos3 = csv.find(',', pos2 + 1);
        
        name = csv.substr(0, pos1);
        department = csv.substr(pos1 + 1, pos2 - pos1 - 1);
        salary = stod(csv.substr(pos2 + 1, pos3 - pos2 - 1));
        isActive = csv.substr(pos3 + 1) == "1";
        id = nextId++;
        
        cout << "Employee from CSV: " << name << " (ID: " << id << ")" << endl;
    }
    
    void display() const {
        cout << "ID: " << setw(4) << id 
             << ", Name: " << setw(15) << name
             << ", Dept: " << setw(12) << department
             << ", Salary: $" << setw(8) << fixed << setprecision(2) << salary
             << ", Active: " << (isActive ? "Yes" : "No") << endl;
    }
    
    void giveRaise(double percent) {
        if (isActive && percent > 0) {
            salary += salary * (percent / 100);
            cout << name << " received " << percent << "% raise. New salary: $" << salary << endl;
        }
    }
    
    void terminate() {
        isActive = false;
        cout << name << " has been terminated." << endl;
    }
    
    int getID() const { return id; }
    string getName() const { return name; }
};

int Employee::nextId = 1000;

class Department {
private:
    string name;
    vector<Employee> employees;
    
public:
    Department(string n) : name(n) {}
    
    void hire(Employee e) {
        employees.push_back(e);
        cout << "Hired to " << name << " department" << endl;
    }
    
    void listEmployees() const {
        cout << "\n=== " << name << " Department ===" << endl;
        for (const auto& emp : employees) {
            emp.display();
        }
    }
};

int main() {
    cout << "=== Employee Management System ===" << endl;
    
    cout << "\n1. Creating employees with different constructors:" << endl;
    Employee e1("Alice Johnson", "Engineering", 85000);
    Employee e2("Bob Smith", "Sales");
    Employee e3("Charlie Brown");
    Employee e4;
    Employee e5("Diana Prince,Marketing,75000,1");
    
    cout << "\n2. Employee roster:" << endl;
    e1.display();
    e2.display();
    e3.display();
    e4.display();
    e5.display();
    
    cout << "\n3. Department management:" << endl;
    Department engineering("Engineering");
    Department sales("Sales");
    
    engineering.hire(e1);
    engineering.hire(e5);
    sales.hire(e2);
    sales.hire(e3);
    
    engineering.listEmployees();
    sales.listEmployees();
    
    cout << "\n4. Employee actions:" << endl;
    e1.giveRaise(10);
    e2.terminate();
    
    return 0;
}
```

---

## 📊 Constructor Overloading Summary

| Aspect | Description |
|--------|-------------|
| **Purpose** | Multiple initialization options |
| **Resolution** | Compiler selects best match based on arguments |
| **Ambiguity** | Can occur with implicit conversions |
| **Default Arguments** | Alternative to multiple overloads |
| **Delegation** | Constructors can call other constructors (C++11) |

---

## ✅ Best Practices

1. **Use delegating constructors** to avoid code duplication (C++11)
2. **Be explicit** with single-argument constructors to prevent implicit conversions
3. **Avoid ambiguity** by not overloading with types that have implicit conversions
4. **Consider default arguments** instead of multiple overloads when appropriate
5. **Document constructor behavior** clearly for users
6. **Order constructors** from most specific to most general

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Ambiguity** | Compiler can't choose | Use explicit casts or factory methods |
| **Default arguments with overloads** | Ambiguous calls | Avoid combining both |
| **Implicit conversions** | Unexpected constructor called | Use `explicit` keyword |
| **Delegation cycles** | Infinite recursion | Ensure no circular delegation |
| **Order of initialization** | Dependencies matter | Follow declaration order |

---

## ✅ Key Takeaways

1. **Constructor overloading** provides flexibility in object creation
2. **Resolution** is based on argument count, types, and order
3. **Delegating constructors** (C++11) reduce code duplication
4. **Default arguments** can replace some overloaded constructors
5. **`explicit`** prevents unwanted implicit conversions
6. **Ambiguity** must be avoided for compilable code

---
---

## Next Step

- Go to [06_Constructor_Initialization_List.md](06_Constructor_Initialization_List.md) to continue with Constructor Initialization List.
