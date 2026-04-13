# Advanced OOP in C++ - Complete Guide

## 📖 Overview

Advanced Object-Oriented Programming concepts extend beyond the four pillars of OOP. These features provide finer control over class design, memory management, and code organization. Understanding these advanced concepts enables creation of more sophisticated, efficient, and maintainable C++ applications.

---

## 🎯 Key Advanced Concepts

| Concept | Description |
|---------|-------------|
| **Friend Functions/Classes** | Granting access to private/protected members |
| **Mutable Keyword** | Allowing modification in const methods |
| **Explicit Keyword** | Preventing implicit conversions |
| **Virtual Base Class** | Solving diamond problem |
| **Object Slicing** | Loss of derived class data |
| **Covariant Return Types** | Returning more specific types |
| **Placement New** | Constructing objects in pre-allocated memory |
| **Type Conversion** | User-defined conversions |

---

## 1. **Friend Functions and Classes**

### Definition
Friend functions and classes can access private and protected members of another class, breaking encapsulation for specific use cases.

```cpp
#include <iostream>
#include <string>
using namespace std;

class BankAccount {
private:
    string accountNumber;
    double balance;
    string pin;
    
public:
    BankAccount(string acc, double bal, string p) 
        : accountNumber(acc), balance(bal), pin(p) {}
    
    // Friend function declaration
    friend void displayAccount(const BankAccount& acc);
    
    // Friend class declaration
    friend class Auditor;
    
    double getBalance() const { return balance; }
};

// Friend function definition - can access private members
void displayAccount(const BankAccount& acc) {
    cout << "Account: " << acc.accountNumber << endl;
    cout << "Balance: $" << acc.balance << endl;
    // cout << "PIN: " << acc.pin << endl;  // Could also access if needed
}

// Friend class - can access private members
class Auditor {
public:
    void audit(const BankAccount& acc) {
        cout << "Auditing account: " << acc.accountNumber << endl;
        cout << "Balance: $" << acc.balance << endl;
        
        // Can access pin for verification
        if (acc.pin.length() != 4) {
            cout << "Warning: PIN length issue!" << endl;
        }
    }
    
    void modifyBalance(BankAccount& acc, double newBalance) {
        // Friend class can even modify private members
        acc.balance = newBalance;
        cout << "Balance modified to: $" << acc.balance << endl;
    }
};

int main() {
    cout << "=== Friend Functions and Classes ===" << endl;
    
    BankAccount account("12345678", 1000.0, "1234");
    
    cout << "\n1. Friend function access:" << endl;
    displayAccount(account);
    
    cout << "\n2. Friend class access:" << endl;
    Auditor auditor;
    auditor.audit(account);
    auditor.modifyBalance(account, 1500.0);
    
    cout << "\n3. Regular member function (also works):" << endl;
    cout << "Balance: $" << account.getBalance() << endl;
    
    return 0;
}
```

---

## 2. **Mutable Keyword**

### Definition
`mutable` allows data members to be modified even in const member functions. Useful for caching, logging, and reference counting.

```cpp
#include <iostream>
#include <string>
#include <chrono>
using namespace std;

class ExpensiveCalculator {
private:
    int value;
    mutable int cacheHits;      // Can be modified in const methods
    mutable double cachedResult; // Can be modified in const methods
    mutable bool cacheValid;     // Can be modified in const methods
    mutable chrono::steady_clock::time_point lastAccess;
    
    double expensiveCalculation() const {
        // Simulate expensive calculation
        this_thread::sleep_for(chrono::milliseconds(100));
        return value * value * 3.14159;
    }
    
public:
    ExpensiveCalculator(int v) : value(v), cacheHits(0), cacheValid(false) {}
    
    double getResult() const {
        lastAccess = chrono::steady_clock::now();
        
        if (!cacheValid) {
            cachedResult = expensiveCalculation();
            cacheValid = true;
        } else {
            cacheHits++;
        }
        return cachedResult;
    }
    
    int getCacheHits() const { return cacheHits; }
    
    void setValue(int v) {
        value = v;
        cacheValid = false;  // Invalidate cache
    }
};

class Logger {
private:
    string name;
    mutable int logCount;      // Mutable for logging in const methods
    
public:
    Logger(string n) : name(n), logCount(0) {}
    
    void log(const string& message) const {
        // Can modify mutable even in const method
        logCount++;
        cout << "[" << name << "] " << message << " (log #" << logCount << ")" << endl;
    }
    
    int getLogCount() const { return logCount; }
};

int main() {
    cout << "=== Mutable Keyword ===" << endl;
    
    cout << "\n1. ExpensiveCalculator with caching:" << endl;
    const ExpensiveCalculator calc(10);  // const object
    
    cout << "First calculation: " << calc.getResult() << endl;
    cout << "Second calculation: " << calc.getResult() << endl;
    cout << "Third calculation: " << calc.getResult() << endl;
    cout << "Cache hits: " << calc.getCacheHits() << endl;
    
    cout << "\n2. Logger with mutable counter:" << endl;
    const Logger logger("System");
    
    logger.log("Application started");
    logger.log("User logged in");
    logger.log("Processing data");
    cout << "Total logs: " << logger.getLogCount() << endl;
    
    return 0;
}
```

---

## 3. **Explicit Keyword**

### Definition
`explicit` prevents implicit conversions that could lead to unintended behavior. Should be used for single-argument constructors.

```cpp
#include <iostream>
#include <string>
using namespace std;

class String {
private:
    string data;
    
public:
    // Implicit conversion constructor (dangerous)
    String(const char* str) : data(str) {
        cout << "Implicit conversion: " << str << endl;
    }
    
    void display() const {
        cout << data << endl;
    }
};

class SafeString {
private:
    string data;
    
public:
    // Explicit constructor - prevents implicit conversion
    explicit SafeString(const char* str) : data(str) {
        cout << "Explicit constructor: " << str << endl;
    }
    
    void display() const {
        cout << data << endl;
    }
};

void printString(const String& s) {
    s.display();
}

void printSafeString(const SafeString& s) {
    s.display();
}

class Number {
private:
    int value;
    
public:
    // Explicit constructor
    explicit Number(int v) : value(v) {}
    
    int getValue() const { return value; }
};

int main() {
    cout << "=== Explicit Keyword ===" << endl;
    
    cout << "\n1. Implicit conversion (dangerous):" << endl;
    String s1 = "Hello";        // Implicit conversion!
    String s2("World");          // Explicit
    printString("Direct");       // Implicit conversion in function call!
    s1.display();
    
    cout << "\n2. Explicit constructor (safe):" << endl;
    SafeString s3("Hello");      // OK
    // SafeString s4 = "World";  // Error! Implicit conversion prevented
    // printSafeString("Direct"); // Error! Implicit conversion prevented
    printSafeString(SafeString("Direct")); // OK - explicit
    s3.display();
    
    cout << "\n3. Number class:" << endl;
    Number n1(42);               // OK
    // Number n2 = 100;          // Error! Explicit constructor
    cout << "Value: " << n1.getValue() << endl;
    
    return 0;
}
```

---

## 4. **Virtual Base Class**

### Definition
Virtual base classes solve the diamond problem by ensuring only one copy of a base class is inherited.

```cpp
#include <iostream>
#include <string>
using namespace std;

// Virtual base class
class Person {
protected:
    string name;
    int age;
    
public:
    Person(string n, int a) : name(n), age(a) {
        cout << "Person constructor: " << name << endl;
    }
    
    void display() const {
        cout << "Name: " << name << ", Age: " << age << endl;
    }
};

// Virtual inheritance
class Employee : virtual public Person {
protected:
    int employeeId;
    
public:
    Employee(string n, int a, int id) : Person(n, a), employeeId(id) {
        cout << "  Employee constructor: ID=" << employeeId << endl;
    }
    
    void work() const {
        cout << name << " is working" << endl;
    }
};

// Virtual inheritance
class Student : virtual public Person {
protected:
    int studentId;
    string major;
    
public:
    Student(string n, int a, int sid, string m) : Person(n, a), studentId(sid), major(m) {
        cout << "  Student constructor: ID=" << studentId << endl;
    }
    
    void study() const {
        cout << name << " is studying " << major << endl;
    }
};

// Multiple inheritance with virtual base
class WorkingStudent : public Employee, public Student {
public:
    WorkingStudent(string n, int a, int eid, int sid, string m) 
        : Person(n, a), Employee(n, a, eid), Student(n, a, sid, m) {
        cout << "    WorkingStudent constructor" << endl;
    }
    
    void display() const {
        Person::display();
        cout << "  Employee ID: " << employeeId << endl;
        cout << "  Student ID: " << studentId << ", Major: " << major << endl;
    }
};

int main() {
    cout << "=== Virtual Base Class ===" << endl;
    
    cout << "\nCreating WorkingStudent (single Person instance):" << endl;
    WorkingStudent ws("Alice", 25, 1001, 2001, "Computer Science");
    
    cout << "\nDisplay:" << endl;
    ws.display();
    
    cout << "\nActions:" << endl;
    ws.work();
    ws.study();
    
    cout << "\nWithout virtual inheritance, Person would appear twice!" << endl;
    
    return 0;
}
```

---

## 5. **Object Slicing**

### Definition
Object slicing occurs when a derived class object is assigned to a base class object, losing derived class data.

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Shape {
protected:
    string color;
    
public:
    Shape(string c) : color(c) {}
    
    virtual void draw() const {
        cout << "Drawing " << color << " shape" << endl;
    }
    
    virtual ~Shape() {}
};

class Circle : public Shape {
private:
    double radius;
    
public:
    Circle(string c, double r) : Shape(c), radius(r) {}
    
    void draw() const override {
        cout << "Drawing " << color << " circle with radius " << radius << endl;
    }
    
    void setRadius(double r) { radius = r; }
};

class Rectangle : public Shape {
private:
    double width, height;
    
public:
    Rectangle(string c, double w, double h) : Shape(c), width(w), height(h) {}
    
    void draw() const override {
        cout << "Drawing " << color << " rectangle " << width << "x" << height << endl;
    }
};

int main() {
    cout << "=== Object Slicing ===" << endl;
    
    Circle circle("Red", 5.0);
    Rectangle rect("Blue", 4.0, 6.0);
    
    cout << "\n1. Original objects:" << endl;
    circle.draw();
    rect.draw();
    
    cout << "\n2. Slicing (assigning derived to base):" << endl;
    Shape shape1 = circle;      // Slicing occurs!
    Shape shape2 = rect;        // Slicing occurs!
    shape1.draw();              // Only base part remains
    shape2.draw();
    
    cout << "\n3. Using pointers (no slicing):" << endl;
    Shape* ptr1 = &circle;
    Shape* ptr2 = &rect;
    ptr1->draw();               // Virtual call works
    ptr2->draw();
    
    cout << "\n4. Using references (no slicing):" << endl;
    Shape& ref1 = circle;
    Shape& ref2 = rect;
    ref1.draw();                // Virtual call works
    ref2.draw();
    
    cout << "\n5. Vector of pointers (correct):" << endl;
    vector<Shape*> shapes;
    shapes.push_back(&circle);
    shapes.push_back(&rect);
    for (auto shape : shapes) {
        shape->draw();          // Correct polymorphic behavior
    }
    
    cout << "\n6. Vector of objects (slicing):" << endl;
    vector<Shape> slicedShapes;
    slicedShapes.push_back(circle);  // Slicing!
    slicedShapes.push_back(rect);    // Slicing!
    for (auto shape : slicedShapes) {
        shape.draw();          // Only base class draw called
    }
    
    return 0;
}
```

---

## 6. **Covariant Return Types**

### Definition
Covariant return types allow overriding functions to return a more specific type than the base class.

```cpp
#include <iostream>
#include <string>
#include <memory>
using namespace std;

class Animal {
public:
    virtual Animal* clone() const {
        cout << "Animal::clone()" << endl;
        return new Animal(*this);
    }
    
    virtual void speak() const {
        cout << "Animal speaks" << endl;
    }
    
    virtual ~Animal() {}
};

class Dog : public Animal {
public:
    // Covariant return type: Dog* instead of Animal*
    Dog* clone() const override {
        cout << "Dog::clone()" << endl;
        return new Dog(*this);
    }
    
    void speak() const override {
        cout << "Dog barks: Woof!" << endl;
    }
    
    void wagTail() const {
        cout << "Dog wags tail" << endl;
    }
};

class Cat : public Animal {
public:
    // Covariant return type: Cat* instead of Animal*
    Cat* clone() const override {
        cout << "Cat::clone()" << endl;
        return new Cat(*this);
    }
    
    void speak() const override {
        cout << "Cat meows: Meow!" << endl;
    }
    
    void purr() const {
        cout << "Cat purrs" << endl;
    }
};

class AnimalFactory {
public:
    virtual Animal* createAnimal() = 0;
    virtual ~AnimalFactory() {}
};

class DogFactory : public AnimalFactory {
public:
    // Covariant return type: Dog* instead of Animal*
    Dog* createAnimal() override {
        return new Dog();
    }
};

class CatFactory : public AnimalFactory {
public:
    // Covariant return type: Cat* instead of Animal*
    Cat* createAnimal() override {
        return new Cat();
    }
};

int main() {
    cout << "=== Covariant Return Types ===" << endl;
    
    cout << "\n1. Clone with covariant returns:" << endl;
    Dog dog;
    Animal* animalPtr = &dog;
    
    Animal* clone1 = animalPtr->clone();  // Returns Animal*
    Dog* clone2 = dog.clone();             // Returns Dog* (covariant)
    
    clone1->speak();
    clone2->speak();
    clone2->wagTail();  // Can call Dog-specific method
    
    delete clone1;
    delete clone2;
    
    cout << "\n2. Factory with covariant returns:" << endl;
    DogFactory dogFactory;
    CatFactory catFactory;
    
    Dog* dog1 = dogFactory.createAnimal();  // Returns Dog*
    Cat* cat1 = catFactory.createAnimal();  // Returns Cat*
    
    dog1->speak();
    dog1->wagTail();
    cat1->speak();
    cat1->purr();
    
    delete dog1;
    delete cat1;
    
    cout << "\nCovariant return types enable:" << endl;
    cout << "  ✓ More specific return types in overrides" << endl;
    cout << "  ✓ No need for downcasting" << endl;
    cout << "  ✓ Type-safe factory methods" << endl;
    
    return 0;
}
```

---

## 📊 Advanced OOP Summary

| Concept | Purpose | Key Feature |
|---------|---------|-------------|
| **Friend** | Grant access | Breaks encapsulation for specific cases |
| **Mutable** | Modify in const | Caching, logging in const methods |
| **Explicit** | Prevent conversion | Single-arg constructors |
| **Virtual Base** | Diamond solution | Single copy of base class |
| **Object Slicing** | Warning | Use pointers/references |
| **Covariant Return** | Specific return | Type-safe overrides |

---

## ✅ Best Practices

1. **Use friend sparingly** - Breaks encapsulation
2. **Use mutable for caching** - Not for regular data
3. **Mark single-arg constructors explicit** - Prevent implicit conversions
4. **Use virtual inheritance** for diamond problem
5. **Avoid object slicing** - Use pointers/references
6. **Use covariant returns** for factory methods

---
---

## Next Step

- Go to [README.md](README.md) to continue.
