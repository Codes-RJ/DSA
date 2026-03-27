# 03_Constructors_and_Destructors/02_Parameterized_Constructor.md

# Parameterized Constructor in C++ - Complete Guide

## 📖 Overview

A parameterized constructor is a constructor that accepts arguments to initialize an object with specific values. Unlike the default constructor, it allows creating objects with custom initial states. Parameterized constructors enable flexible object creation and are essential for proper initialization.

---

## 🎯 Key Concepts

| Aspect | Description |
|--------|-------------|
| **Purpose** | Initialize objects with specific values |
| **Syntax** | `ClassName(parameters) { }` |
| **Parameters** | Can have any number of parameters |
| **Overloading** | Multiple parameterized constructors possible |
| **Initialization** | Use initialization list for efficiency |

---

## 1. **Basic Parameterized Constructor**

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
    // Parameterized constructor
    Rectangle(double l, double w) {
        length = l;
        width = w;
        cout << "Rectangle created: " << length << " x " << width << endl;
    }
    
    double area() const {
        return length * width;
    }
    
    double perimeter() const {
        return 2 * (length + width);
    }
    
    void display() const {
        cout << "Rectangle: " << length << " x " << width 
             << ", Area: " << area() << ", Perimeter: " << perimeter() << endl;
    }
};

class Circle {
private:
    double radius;
    string color;
    
public:
    // Parameterized constructor with multiple parameters
    Circle(double r, string c) : radius(r), color(c) {
        cout << "Circle created: radius=" << radius << ", color=" << color << endl;
    }
    
    double area() const {
        return 3.14159 * radius * radius;
    }
    
    double circumference() const {
        return 2 * 3.14159 * radius;
    }
    
    void display() const {
        cout << "Circle: radius=" << radius << ", color=" << color 
             << ", Area: " << area() << ", Circumference: " << circumference() << endl;
    }
};

class Employee {
private:
    int id;
    string name;
    double salary;
    
public:
    // Parameterized constructor
    Employee(int i, string n, double s) {
        id = i;
        name = n;
        salary = s;
        cout << "Employee created: " << name << " (ID: " << id << ")" << endl;
    }
    
    void display() const {
        cout << "ID: " << id << ", Name: " << name << ", Salary: $" << salary << endl;
    }
    
    void giveRaise(double percent) {
        salary += salary * (percent / 100);
    }
};

int main() {
    cout << "=== Parameterized Constructor Examples ===" << endl;
    
    cout << "\n1. Rectangle:" << endl;
    Rectangle rect(10, 5);
    rect.display();
    
    cout << "\n2. Circle:" << endl;
    Circle circle(7.5, "Red");
    circle.display();
    
    cout << "\n3. Employee:" << endl;
    Employee emp(1001, "Alice Johnson", 75000);
    emp.display();
    emp.giveRaise(10);
    cout << "After 10% raise: ";
    emp.display();
    
    return 0;
}
```

**Output:**
```
=== Parameterized Constructor Examples ===

1. Rectangle:
Rectangle created: 10 x 5
Rectangle: 10 x 5, Area: 50, Perimeter: 30

2. Circle:
Circle created: radius=7.5, color=Red
Circle: radius=7.5, color=Red, Area: 176.714, Circumference: 47.1239

3. Employee:
Employee created: Alice Johnson (ID: 1001)
ID: 1001, Name: Alice Johnson, Salary: $75000
After 10% raise: ID: 1001, Name: Alice Johnson, Salary: $82500
```

---

## 2. **Constructor Overloading**

Multiple constructors with different parameters can coexist.

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Date {
private:
    int day, month, year;
    
public:
    // Constructor 1: Full date
    Date(int d, int m, int y) : day(d), month(m), year(y) {
        cout << "Date: " << day << "/" << month << "/" << year << endl;
    }
    
    // Constructor 2: Month and year only (day defaults to 1)
    Date(int m, int y) : day(1), month(m), year(y) {
        cout << "Date: " << day << "/" << month << "/" << year << endl;
    }
    
    // Constructor 3: Year only (defaults to Jan 1)
    Date(int y) : day(1), month(1), year(y) {
        cout << "Date: " << day << "/" << month << "/" << year << endl;
    }
    
    void display() const {
        cout << day << "/" << month << "/" << year << endl;
    }
};

class Student {
private:
    string name;
    int rollNumber;
    double marks;
    string course;
    
public:
    // Constructor 1: All parameters
    Student(string n, int r, double m, string c) 
        : name(n), rollNumber(r), marks(m), course(c) {
        cout << "Student (full): " << name << endl;
    }
    
    // Constructor 2: Name, roll, marks only (course default)
    Student(string n, int r, double m) 
        : name(n), rollNumber(r), marks(m), course("General") {
        cout << "Student (basic): " << name << endl;
    }
    
    // Constructor 3: Name and roll only (marks default 0, course default)
    Student(string n, int r) 
        : name(n), rollNumber(r), marks(0.0), course("General") {
        cout << "Student (minimal): " << name << endl;
    }
    
    void display() const {
        cout << "Name: " << name << ", Roll: " << rollNumber 
             << ", Marks: " << marks << ", Course: " << course << endl;
    }
};

class Vector3D {
private:
    double x, y, z;
    
public:
    // Constructor 1: All components
    Vector3D(double xVal, double yVal, double zVal) : x(xVal), y(yVal), z(zVal) {
        cout << "Vector: (" << x << ", " << y << ", " << z << ")" << endl;
    }
    
    // Constructor 2: 2D vector (z=0)
    Vector3D(double xVal, double yVal) : x(xVal), y(yVal), z(0) {
        cout << "Vector: (" << x << ", " << y << ", " << z << ")" << endl;
    }
    
    // Constructor 3: Single component (vector along x-axis)
    Vector3D(double xVal) : x(xVal), y(0), z(0) {
        cout << "Vector: (" << x << ", " << y << ", " << z << ")" << endl;
    }
    
    // Constructor 4: Default vector (zero)
    Vector3D() : x(0), y(0), z(0) {
        cout << "Vector: Zero vector" << endl;
    }
    
    double magnitude() const {
        return sqrt(x*x + y*y + z*z);
    }
    
    void display() const {
        cout << "(" << x << ", " << y << ", " << z << ") magnitude: " << magnitude() << endl;
    }
};

int main() {
    cout << "=== Constructor Overloading Examples ===" << endl;
    
    cout << "\n1. Date class:" << endl;
    Date d1(15, 3, 2024);     // Full date
    Date d2(5, 2024);          // Month and year only
    Date d3(2024);             // Year only
    
    cout << "\n2. Student class:" << endl;
    Student s1("Alice", 101, 85.5, "Computer Science");
    Student s2("Bob", 102, 78.0);
    Student s3("Charlie", 103);
    s1.display();
    s2.display();
    s3.display();
    
    cout << "\n3. Vector3D class:" << endl;
    Vector3D v1(3, 4, 5);
    Vector3D v2(3, 4);
    Vector3D v3(5);
    Vector3D v4;
    v1.display();
    v2.display();
    v3.display();
    v4.display();
    
    return 0;
}
```

**Output:**
```
=== Constructor Overloading Examples ===

1. Date class:
Date: 15/3/2024
Date: 1/5/2024
Date: 1/1/2024

2. Student class:
Student (full): Alice
Student (basic): Bob
Student (minimal): Charlie
Name: Alice, Roll: 101, Marks: 85.5, Course: Computer Science
Name: Bob, Roll: 102, Marks: 78, Course: General
Name: Charlie, Roll: 103, Marks: 0, Course: General

3. Vector3D class:
Vector: (3, 4, 5)
Vector: (3, 4, 0)
Vector: (5, 0, 0)
Vector: Zero vector
(3, 4, 5) magnitude: 7.07107
(3, 4, 0) magnitude: 5
(5, 0, 0) magnitude: 5
(0, 0, 0) magnitude: 0
```

---

## 3. **Parameterized Constructor with Initialization List**

Initialization lists are more efficient than assignment in the constructor body.

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Base {
private:
    int value;
    
public:
    Base(int v) : value(v) {
        cout << "Base constructor: " << value << endl;
    }
};

class Member {
private:
    string name;
    
public:
    Member(string n) : name(n) {
        cout << "Member constructor: " << name << endl;
    }
};

class Complex {
private:
    const int id;           // Must use initialization list
    string& nameRef;        // Must use initialization list
    Base base;              // Must use initialization list
    Member member;          // Must use initialization list
    static int counter;     // Static - not in initialization list
    
public:
    // Constructor with initialization list (MORE EFFICIENT)
    Complex(int i, string& n, int baseVal, string memberName) 
        : id(i),                    // Initialize const member
          nameRef(n),               // Initialize reference member
          base(baseVal),            // Initialize base class
          member(memberName)        // Initialize member object
    {
        counter++;
        cout << "Complex constructor body" << endl;
    }
    
    // Alternative: Assignment in body (LESS EFFICIENT)
    /*
    Complex(int i, string& n, int baseVal, string memberName) {
        id = i;                     // Error! const can't be assigned
        nameRef = n;                // Reference already initialized
        base = Base(baseVal);       // Base already default constructed
        member = Member(memberName); // Member already default constructed
    }
    */
    
    void display() const {
        cout << "ID: " << id << ", Name Ref: " << nameRef << endl;
    }
    
    static int getCount() { return counter; }
};

int Complex::counter = 0;

class Book {
private:
    string title;
    string author;
    int pages;
    double price;
    
public:
    // Using initialization list for all members
    Book(string t, string a, int p, double pr) 
        : title(t), author(a), pages(p), price(pr) {
        cout << "Book created: " << title << endl;
    }
    
    // Initialization list with default values
    Book(string t, string a) 
        : title(t), author(a), pages(0), price(0.0) {
        cout << "Book (basic): " << title << endl;
    }
    
    void display() const {
        cout << "'" << title << "' by " << author 
             << ", " << pages << " pages, $" << price << endl;
    }
};

int main() {
    cout << "=== Parameterized Constructor with Initialization List ===" << endl;
    
    string externalName = "External Reference";
    
    cout << "\n1. Complex class with const and reference members:" << endl;
    Complex c(100, externalName, 42, "Member Object");
    c.display();
    cout << "Complex instances: " << Complex::getCount() << endl;
    
    cout << "\n2. Book class:" << endl;
    Book b1("The C++ Programming Language", "Bjarne Stroustrup", 1368, 89.99);
    Book b2("Effective Modern C++", "Scott Meyers");
    b1.display();
    b2.display();
    
    cout << "\n3. Efficiency note:" << endl;
    cout << "Initialization list initializes members directly." << endl;
    cout << "Assignment in body first default-constructs, then assigns." << endl;
    cout << "Use initialization list for const, reference, and object members." << endl;
    
    return 0;
}
```

**Output:**
```
=== Parameterized Constructor with Initialization List ===

1. Complex class with const and reference members:
Base constructor: 42
Member constructor: Member Object
Complex constructor body
ID: 100, Name Ref: External Reference
Complex instances: 1

2. Book class:
Book created: The C++ Programming Language
Book (basic): Effective Modern C++
'The C++ Programming Language' by Bjarne Stroustrup, 1368 pages, $89.99
'Effective Modern C++' by Scott Meyers, 0 pages, $0

3. Efficiency note:
Initialization list initializes members directly.
Assignment in body first default-constructs, then assigns.
Use initialization list for const, reference, and object members.
```

---

## 4. **Default Arguments in Parameterized Constructors**

Constructors can have default arguments, combining the benefits of default and parameterized constructors.

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Timer {
private:
    int hours;
    int minutes;
    int seconds;
    
public:
    // Constructor with default arguments
    Timer(int h = 0, int m = 0, int s = 0) 
        : hours(h), minutes(m), seconds(s) {
        cout << "Timer created: " << *this << endl;
    }
    
    friend ostream& operator<<(ostream& os, const Timer& t) {
        os << t.hours << ":" << t.minutes << ":" << t.seconds;
        return os;
    }
};

class Product {
private:
    int id;
    string name;
    double price;
    int quantity;
    
public:
    // Constructor with default arguments
    Product(int i = 0, string n = "Unknown", double p = 0.0, int q = 0)
        : id(i), name(n), price(p), quantity(q) {
        cout << "Product: " << name << " (ID: " << id << ")" << endl;
    }
    
    void display() const {
        cout << "ID: " << id << ", Name: " << name 
             << ", Price: $" << price << ", Stock: " << quantity << endl;
    }
};

class Point {
private:
    double x, y;
    
public:
    // Constructor with default arguments
    Point(double xVal = 0.0, double yVal = 0.0) : x(xVal), y(yVal) {
        cout << "Point: (" << x << ", " << y << ")" << endl;
    }
    
    double distance() const {
        return sqrt(x*x + y*y);
    }
    
    void display() const {
        cout << "(" << x << ", " << y << ") distance: " << distance() << endl;
    }
};

int main() {
    cout << "=== Default Arguments in Constructors ===" << endl;
    
    cout << "\n1. Timer class:" << endl;
    Timer t1;                    // All defaults
    Timer t2(10);                // Hours only
    Timer t3(10, 30);            // Hours and minutes
    Timer t4(10, 30, 45);        // All specified
    
    cout << "\n2. Product class:" << endl;
    Product p1;                  // All defaults
    Product p2(101);             // ID only
    Product p3(102, "Laptop");   // ID and name
    Product p4(103, "Mouse", 29.99);  // ID, name, price
    Product p5(104, "Keyboard", 79.99, 50);  // All specified
    p1.display();
    p2.display();
    p3.display();
    p4.display();
    p5.display();
    
    cout << "\n3. Point class:" << endl;
    Point pt1;                   // (0,0)
    Point pt2(3);                // (3,0)
    Point pt3(3, 4);             // (3,4)
    pt1.display();
    pt2.display();
    pt3.display();
    
    cout << "\n4. Note about ambiguity:" << endl;
    cout << "Default arguments can cause ambiguity with overloaded constructors." << endl;
    cout << "Avoid combining default arguments with overloaded constructors." << endl;
    
    return 0;
}
```

**Output:**
```
=== Default Arguments in Constructors ===

1. Timer class:
Timer created: 0:0:0
Timer created: 10:0:0
Timer created: 10:30:0
Timer created: 10:30:45

2. Product class:
Product: Unknown (ID: 0)
Product: Unknown (ID: 101)
Product: Laptop (ID: 102)
Product: Mouse (ID: 103)
Product: Keyboard (ID: 104)
ID: 0, Name: Unknown, Price: $0, Stock: 0
ID: 101, Name: Unknown, Price: $0, Stock: 0
ID: 102, Name: Laptop, Price: $0, Stock: 0
ID: 103, Name: Mouse, Price: $29.99, Stock: 0
ID: 104, Name: Keyboard, Price: $79.99, Stock: 50

3. Point class:
Point: (0, 0)
Point: (3, 0)
Point: (3, 4)
(0, 0) distance: 0
(3, 0) distance: 3
(3, 4) distance: 5

4. Note about ambiguity:
Default arguments can cause ambiguity with overloaded constructors.
Avoid combining default arguments with overloaded constructors.
```

---

## 5. **explicit Keyword for Single-Parameter Constructors**

Prevents implicit conversions that can lead to unexpected behavior.

```cpp
#include <iostream>
#include <string>
using namespace std;

class String {
private:
    char* data;
    size_t length;
    
public:
    // Implicit conversion constructor (can be dangerous)
    String(const char* str) {
        length = strlen(str);
        data = new char[length + 1];
        strcpy(data, str);
        cout << "Implicit conversion: " << data << endl;
    }
    
    ~String() {
        delete[] data;
    }
    
    void display() const {
        cout << data << endl;
    }
};

class SafeString {
private:
    char* data;
    size_t length;
    
public:
    // Explicit constructor - prevents implicit conversion
    explicit SafeString(const char* str) {
        length = strlen(str);
        data = new char[length + 1];
        strcpy(data, str);
        cout << "Explicit constructor: " << data << endl;
    }
    
    ~SafeString() {
        delete[] data;
    }
    
    void display() const {
        cout << data << endl;
    }
};

class Number {
private:
    int value;
    
public:
    // Explicit constructor
    explicit Number(int v) : value(v) {
        cout << "Number: " << value << endl;
    }
    
    int getValue() const { return value; }
};

void printString(const String& s) {
    s.display();
}

void printSafeString(const SafeString& s) {
    s.display();
}

void processNumber(const Number& n) {
    cout << "Processing number: " << n.getValue() << endl;
}

int main() {
    cout << "=== explicit Keyword for Single-Parameter Constructors ===" << endl;
    
    cout << "\n1. Implicit conversion (DANGEROUS):" << endl;
    String s1 = "Hello";        // Implicit conversion! const char* -> String
    printString("World");       // Implicit conversion in function call
    s1.display();
    
    cout << "\n2. Explicit constructor (SAFE):" << endl;
    SafeString s2("Hello");      // OK - explicit call
    // SafeString s3 = "World";  // Error! Cannot implicitly convert
    // printSafeString("World"); // Error! Cannot implicitly convert
    s2.display();
    
    cout << "\n3. Number class:" << endl;
    Number n1(42);               // OK - explicit call
    // Number n2 = 100;          // Error! Implicit conversion prevented
    // processNumber(50);        // Error! Implicit conversion prevented
    processNumber(Number(50));   // OK - explicit conversion
    cout << "Number value: " << n1.getValue() << endl;
    
    cout << "\n4. When to use explicit:" << endl;
    cout << "✓ Single-argument constructors" << endl;
    cout << "✓ Constructors that shouldn't be used for implicit conversion" << endl;
    cout << "✓ To prevent unintended type conversions" << endl;
    
    return 0;
}
```

**Output:**
```
=== explicit Keyword for Single-Parameter Constructors ===

1. Implicit conversion (DANGEROUS):
Implicit conversion: Hello
Implicit conversion: World
Hello

2. Explicit constructor (SAFE):
Explicit constructor: Hello
Hello

3. Number class:
Number: 42
Processing number: 50
Number value: 42

4. When to use explicit:
✓ Single-argument constructors
✓ Constructors that shouldn't be used for implicit conversion
✓ To prevent unintended type conversions
```

---

## 6. **Practical Example: Bank Account System**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
using namespace std;

class BankAccount {
private:
    string accountNumber;
    string accountHolder;
    double balance;
    string accountType;
    static int accountCounter;
    
public:
    // Parameterized constructor with default arguments
    BankAccount(string holder, double initialBalance = 0.0, string type = "Savings") 
        : accountHolder(holder), balance(initialBalance), accountType(type) {
        accountNumber = generateAccountNumber();
        cout << "Account created: " << accountNumber << " for " << accountHolder << endl;
    }
    
    // Constructor with account type only
    BankAccount(string holder, string type) 
        : BankAccount(holder, 0.0, type) {  // Delegating constructor
    }
    
    string generateAccountNumber() {
        accountCounter++;
        return "ACC" + to_string(accountCounter);
    }
    
    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            cout << "Deposited: $" << fixed << setprecision(2) << amount << endl;
        }
    }
    
    bool withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            cout << "Withdrawn: $" << fixed << setprecision(2) << amount << endl;
            return true;
        }
        cout << "Insufficient funds!" << endl;
        return false;
    }
    
    void display() const {
        cout << "\n=== Account Details ===" << endl;
        cout << "Account Number: " << accountNumber << endl;
        cout << "Account Holder: " << accountHolder << endl;
        cout << "Account Type: " << accountType << endl;
        cout << "Balance: $" << fixed << setprecision(2) << balance << endl;
    }
    
    double getBalance() const { return balance; }
    string getAccountNumber() const { return accountNumber; }
};

int BankAccount::accountCounter = 1000;

class Transaction {
private:
    string fromAccount;
    string toAccount;
    double amount;
    string timestamp;
    
public:
    // Parameterized constructor
    Transaction(string from, string to, double amt) 
        : fromAccount(from), toAccount(to), amount(amt) {
        // In real system, would set timestamp
        cout << "Transaction created: " << from << " -> " << to << " $" << amount << endl;
    }
    
    void display() const {
        cout << fromAccount << " -> " << toAccount << ": $" << amount << endl;
    }
};

int main() {
    cout << "=== Bank Account System ===" << endl;
    
    // Creating accounts with different constructors
    BankAccount acc1("Alice Johnson", 1000.00);
    BankAccount acc2("Bob Smith", 500.00, "Checking");
    BankAccount acc3("Charlie Brown");  // Default balance 0, type Savings
    
    acc1.display();
    acc2.display();
    acc3.display();
    
    cout << "\n=== Transactions ===" << endl;
    acc1.deposit(250);
    acc1.withdraw(100);
    acc2.withdraw(600);  // Should fail
    
    Transaction t1(acc1.getAccountNumber(), acc2.getAccountNumber(), 300);
    
    cout << "\n=== Final Balances ===" << endl;
    acc1.display();
    acc2.display();
    acc3.display();
    
    return 0;
}
```

**Output:**
```
=== Bank Account System ===
Account created: ACC1001 for Alice Johnson
Account created: ACC1002 for Bob Smith
Account created: ACC1003 for Charlie Brown

=== Account Details ===
Account Number: ACC1001
Account Holder: Alice Johnson
Account Type: Savings
Balance: $1000.00

=== Account Details ===
Account Number: ACC1002
Account Holder: Bob Smith
Account Type: Checking
Balance: $500.00

=== Account Details ===
Account Number: ACC1003
Account Holder: Charlie Brown
Account Type: Savings
Balance: $0.00

=== Transactions ===
Deposited: $250.00
Withdrawn: $100.00
Insufficient funds!
Transaction created: ACC1001 -> ACC1002 $300

=== Final Balances ===

=== Account Details ===
Account Number: ACC1001
Account Holder: Alice Johnson
Account Type: Savings
Balance: $1150.00

=== Account Details ===
Account Number: ACC1002
Account Holder: Bob Smith
Account Type: Checking
Balance: $500.00

=== Account Details ===
Account Number: ACC1003
Account Holder: Charlie Brown
Account Type: Savings
Balance: $0.00
```

---

## 📊 Parameterized Constructor Summary

| Aspect | Description |
|--------|-------------|
| **Purpose** | Initialize objects with specific values |
| **Parameters** | Can have 0 to N parameters |
| **Overloading** | Multiple constructors with different parameters |
| **Default Arguments** | Can combine with parameter defaults |
| **Initialization List** | More efficient than assignment in body |
| **explicit** | Prevents implicit conversions for single-arg constructors |
| **Delegation** | Can call other constructors (C++11) |

---

## ✅ Best Practices

1. **Use initialization lists** for better performance
2. **Mark single-argument constructors as `explicit`** to prevent implicit conversions
3. **Use default arguments** to reduce constructor overloads
4. **Validate parameters** in constructor body when needed
5. **Prefer initialization list over assignment** for non-trivial types
6. **Use delegating constructors** (C++11) to avoid code duplication

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Implicit conversion** | Unexpected behavior | Use `explicit` keyword |
| **Ambiguous overloads** | Compiler error | Avoid combining default args with overloads |
| **Order of initialization** | Dependency issues | Follow declaration order |
| **Parameter name shadowing** | Confusion | Use `this->` or different names |
| **Missing validation** | Invalid state | Validate parameters in constructor |

---

## ✅ Key Takeaways

1. **Parameterized constructors** enable customized object initialization
2. **Overloading** provides multiple ways to create objects
3. **Initialization lists** are more efficient than assignment
4. **Default arguments** reduce the need for multiple constructors
5. **`explicit`** prevents dangerous implicit conversions
6. **Delegating constructors** reduce code duplication

---