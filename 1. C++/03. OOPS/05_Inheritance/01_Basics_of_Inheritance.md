# Basics of Inheritance in C++ - Complete Guide

## 📖 Overview

Inheritance is a core OOP concept that allows a class to acquire properties and behaviors from another class. The class that provides the members is called the **base class** (or parent class), and the class that inherits is called the **derived class** (or child class). Inheritance promotes code reuse and establishes hierarchical relationships.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Base Class** | The class being inherited from |
| **Derived Class** | The class that inherits from the base class |
| **`:` Symbol** | Used to specify inheritance |
| **Access Specifier** | `public`, `protected`, `private` - determines inheritance type |
| **Reusability** | Derived class reuses base class code |

---

## 1. **Basic Inheritance Syntax**

```cpp
#include <iostream>
#include <string>
using namespace std;

// Base class (Parent)
class Animal {
protected:
    string name;
    int age;
    
public:
    Animal(string n, int a) : name(n), age(a) {
        cout << "Animal constructor called for " << name << endl;
    }
    
    void eat() {
        cout << name << " is eating" << endl;
    }
    
    void sleep() {
        cout << name << " is sleeping" << endl;
    }
    
    void display() {
        cout << "Name: " << name << ", Age: " << age << endl;
    }
    
    virtual void sound() {
        cout << name << " makes a sound" << endl;
    }
};

// Derived class (Child) - inherits from Animal
class Dog : public Animal {
private:
    string breed;
    
public:
    Dog(string n, int a, string b) : Animal(n, a), breed(b) {
        cout << "Dog constructor called for " << name << endl;
    }
    
    // Additional member functions
    void bark() {
        cout << name << " says: Woof! Woof!" << endl;
    }
    
    void wagTail() {
        cout << name << " is wagging tail" << endl;
    }
    
    // Override base class function
    void sound() override {
        cout << name << " barks loudly!" << endl;
    }
    
    void display() {
        Animal::display();
        cout << "Breed: " << breed << endl;
    }
};

int main() {
    cout << "=== Basic Inheritance Demo ===" << endl;
    
    // Create derived class object
    Dog dog("Buddy", 3, "Golden Retriever");
    
    cout << "\n=== Using Inherited Methods ===" << endl;
    dog.eat();      // From Animal class
    dog.sleep();    // From Animal class
    dog.display();  // Overridden method
    dog.bark();     // Dog's own method
    dog.wagTail();  // Dog's own method
    dog.sound();    // Overridden method
    
    return 0;
}
```

**Output:**
```
=== Basic Inheritance Demo ===
Animal constructor called for Buddy
Dog constructor called for Buddy

=== Using Inherited Methods ===
Buddy is eating
Buddy is sleeping
Name: Buddy, Age: 3
Breed: Golden Retriever
Buddy says: Woof! Woof!
Buddy is wagging tail
Buddy barks loudly!
```

---

## 2. **Inheritance Terminology**

```cpp
#include <iostream>
#include <string>
using namespace std;

// Base class (Parent, Superclass)
class Vehicle {
protected:
    string brand;
    int year;
    
public:
    Vehicle(string b, int y) : brand(b), year(y) {
        cout << "Vehicle created: " << brand << endl;
    }
    
    void start() {
        cout << brand << " vehicle starting..." << endl;
    }
    
    void stop() {
        cout << brand << " vehicle stopping..." << endl;
    }
    
    virtual void display() {
        cout << "Brand: " << brand << ", Year: " << year << endl;
    }
};

// Derived class (Child, Subclass)
class Car : public Vehicle {
private:
    int doors;
    
public:
    Car(string b, int y, int d) : Vehicle(b, y), doors(d) {
        cout << "Car created: " << brand << endl;
    }
    
    void honk() {
        cout << brand << " car honks: Beep! Beep!" << endl;
    }
    
    void display() override {
        Vehicle::display();
        cout << "Doors: " << doors << endl;
    }
};

// Another derived class
class Motorcycle : public Vehicle {
private:
    bool hasSidecar;
    
public:
    Motorcycle(string b, int y, bool sidecar) : Vehicle(b, y), hasSidecar(sidecar) {
        cout << "Motorcycle created: " << brand << endl;
    }
    
    void wheelie() {
        cout << brand << " motorcycle doing a wheelie!" << endl;
    }
    
    void display() override {
        Vehicle::display();
        cout << "Sidecar: " << (hasSidecar ? "Yes" : "No") << endl;
    }
};

int main() {
    cout << "=== Inheritance Terminology ===" << endl;
    
    cout << "\nCreating Car (Derived from Vehicle):" << endl;
    Car car("Toyota", 2022, 4);
    
    cout << "\nCreating Motorcycle (Derived from Vehicle):" << endl;
    Motorcycle bike("Harley", 2021, false);
    
    cout << "\n=== Using Derived Classes ===" << endl;
    car.display();
    car.honk();
    car.start();
    
    cout << endl;
    
    bike.display();
    bike.wheelie();
    bike.start();
    
    return 0;
}
```

---

## 3. **Accessing Base Class Members**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Base {
private:
    int privateVar = 1;      // Not accessible in derived class
    
protected:
    int protectedVar = 2;    // Accessible in derived class
    
public:
    int publicVar = 3;       // Accessible everywhere
    
    // Public method to access private member
    int getPrivate() const {
        return privateVar;
    }
    
    void setPrivate(int val) {
        privateVar = val;
    }
    
    void showBase() {
        cout << "Private: " << privateVar << endl;
        cout << "Protected: " << protectedVar << endl;
        cout << "Public: " << publicVar << endl;
    }
};

class Derived : public Base {
public:
    void accessBaseMembers() {
        // cout << privateVar << endl;  // Error! Private not accessible
        
        cout << "Protected member: " << protectedVar << endl;  // OK
        cout << "Public member: " << publicVar << endl;        // OK
        
        // Access private via public methods
        cout << "Private via getter: " << getPrivate() << endl;
        
        // Modify protected and public
        protectedVar = 20;
        publicVar = 30;
        
        // Modify private via setter
        setPrivate(10);
    }
    
    void showDerived() {
        cout << "\nDerived Class View:" << endl;
        cout << "Protected: " << protectedVar << endl;
        cout << "Public: " << publicVar << endl;
        cout << "Private via getter: " << getPrivate() << endl;
    }
};

int main() {
    cout << "=== Accessing Base Class Members ===" << endl;
    
    Base base;
    Derived derived;
    
    cout << "\nBase class accessing its own members:" << endl;
    base.showBase();
    
    cout << "\nDerived class accessing base members:" << endl;
    derived.accessBaseMembers();
    derived.showDerived();
    
    cout << "\nExternal access (main function):" << endl;
    // cout << derived.protectedVar;  // Error! Protected not accessible externally
    cout << "Public member: " << derived.publicVar << endl;  // OK
    
    return 0;
}
```

---

## 4. **Inheritance and Member Functions**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Shape {
protected:
    string color;
    
public:
    Shape(string c) : color(c) {
        cout << "Shape constructor: " << color << endl;
    }
    
    // Non-virtual function - will be statically bound
    void identify() {
        cout << "This is a shape" << endl;
    }
    
    // Virtual function - can be overridden
    virtual void draw() {
        cout << "Drawing a generic shape" << endl;
    }
    
    // Pure virtual function - must be overridden
    virtual double area() const = 0;
    
    virtual ~Shape() {
        cout << "Shape destructor: " << color << endl;
    }
    
    string getColor() const { return color; }
};

class Circle : public Shape {
private:
    double radius;
    
public:
    Circle(string c, double r) : Shape(c), radius(r) {
        cout << "Circle constructor: radius=" << radius << endl;
    }
    
    // Override virtual function
    void draw() override {
        cout << "Drawing a " << color << " circle" << endl;
    }
    
    // Must implement pure virtual function
    double area() const override {
        return 3.14159 * radius * radius;
    }
    
    // Additional function
    void circumference() {
        cout << "Circumference: " << 2 * 3.14159 * radius << endl;
    }
    
    ~Circle() override {
        cout << "Circle destructor: radius=" << radius << endl;
    }
};

class Rectangle : public Shape {
private:
    double width, height;
    
public:
    Rectangle(string c, double w, double h) : Shape(c), width(w), height(h) {
        cout << "Rectangle constructor: " << width << "x" << height << endl;
    }
    
    void draw() override {
        cout << "Drawing a " << color << " rectangle" << endl;
    }
    
    double area() const override {
        return width * height;
    }
    
    ~Rectangle() override {
        cout << "Rectangle destructor: " << width << "x" << height << endl;
    }
};

int main() {
    cout << "=== Inheritance and Member Functions ===" << endl;
    
    cout << "\nCreating Circle object:" << endl;
    Circle circle("Red", 5.0);
    
    cout << "\nCalling member functions:" << endl;
    circle.identify();      // From Shape
    circle.draw();          // Overridden
    cout << "Area: " << circle.area() << endl;
    circle.circumference(); // Circle's own method
    
    cout << "\nCreating Rectangle object:" << endl;
    Rectangle rect("Blue", 4.0, 6.0);
    
    cout << "\nPolymorphic behavior:" << endl;
    Shape* shapes[] = {&circle, &rect};
    
    for (auto shape : shapes) {
        shape->draw();      // Calls appropriate derived class method
        cout << "Area: " << shape->area() << endl;
    }
    
    return 0;
}
```

---

## 5. **Protected vs Private Inheritance**

```cpp
#include <iostream>
using namespace std;

class Base {
protected:
    int protectedData = 10;
public:
    int publicData = 20;
    
    void showBase() {
        cout << "Base: protected=" << protectedData << ", public=" << publicData << endl;
    }
};

// Public Inheritance
class PublicDerived : public Base {
public:
    void show() {
        // protectedData is protected in derived
        protectedData = 100;
        publicData = 200;
        cout << "PublicDerived: protected=" << protectedData 
             << ", public=" << publicData << endl;
    }
};

// Protected Inheritance
class ProtectedDerived : protected Base {
public:
    void show() {
        // Both become protected in derived
        protectedData = 300;
        publicData = 400;
        cout << "ProtectedDerived: protected=" << protectedData 
             << ", public=" << publicData << endl;
    }
};

// Private Inheritance
class PrivateDerived : private Base {
public:
    void show() {
        // Both become private in derived
        protectedData = 500;
        publicData = 600;
        cout << "PrivateDerived: protected=" << protectedData 
             << ", public=" << publicData << endl;
    }
};

int main() {
    cout << "=== Protected vs Private Inheritance ===" << endl;
    
    PublicDerived pub;
    pub.show();
    pub.publicData = 700;    // OK - public
    // pub.protectedData = 800; // Error - protected
    
    ProtectedDerived prot;
    prot.show();
    // prot.publicData = 900;   // Error - now protected
    // prot.protectedData = 1000; // Error - protected
    
    PrivateDerived priv;
    priv.show();
    // priv.publicData = 1100;   // Error - now private
    // priv.protectedData = 1200; // Error - private
    
    cout << "\nBase class can still be accessed directly:" << endl;
    Base base;
    base.publicData = 1300;
    base.showBase();
    
    return 0;
}
```

---

## 6. **Practical Example: Employee Hierarchy**

```cpp
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

class Employee {
protected:
    int id;
    string name;
    double baseSalary;
    static int nextId;
    
public:
    Employee(string n, double salary) : name(n), baseSalary(salary) {
        id = nextId++;
        cout << "Employee created: " << name << " (ID: " << id << ")" << endl;
    }
    
    virtual ~Employee() {
        cout << "Employee destroyed: " << name << endl;
    }
    
    virtual double calculateSalary() const {
        return baseSalary;
    }
    
    virtual void display() const {
        cout << "ID: " << id << ", Name: " << name 
             << ", Base Salary: $" << fixed << setprecision(2) << baseSalary << endl;
    }
    
    int getId() const { return id; }
    string getName() const { return name; }
};

int Employee::nextId = 1000;

class Manager : public Employee {
private:
    double bonus;
    int teamSize;
    
public:
    Manager(string n, double salary, double b, int team) 
        : Employee(n, salary), bonus(b), teamSize(team) {
        cout << "  Manager created: " << name << " (Team size: " << teamSize << ")" << endl;
    }
    
    double calculateSalary() const override {
        return baseSalary + bonus;
    }
    
    void display() const override {
        Employee::display();
        cout << "  Bonus: $" << bonus << ", Team Size: " << teamSize 
             << ", Total: $" << calculateSalary() << endl;
    }
    
    void addBonus(double amount) {
        bonus += amount;
        cout << name << " received bonus of $" << amount << endl;
    }
};

class Developer : public Employee {
private:
    string programmingLanguage;
    int projectsCompleted;
    
public:
    Developer(string n, double salary, string lang, int projects) 
        : Employee(n, salary), programmingLanguage(lang), projectsCompleted(projects) {
        cout << "  Developer created: " << name << " (" << lang << ")" << endl;
    }
    
    double calculateSalary() const override {
        // Developers get bonus based on projects
        return baseSalary + (projectsCompleted * 1000);
    }
    
    void display() const override {
        Employee::display();
        cout << "  Language: " << programmingLanguage << ", Projects: " << projectsCompleted
             << ", Total: $" << calculateSalary() << endl;
    }
    
    void completeProject() {
        projectsCompleted++;
        cout << name << " completed a project! Now " << projectsCompleted << " projects" << endl;
    }
};

class Intern : public Employee {
private:
    int hoursWorked;
    double hourlyRate;
    
public:
    Intern(string n, double rate, int hours) 
        : Employee(n, 0), hourlyRate(rate), hoursWorked(hours) {
        cout << "  Intern created: " << name << " ($" << rate << "/hour)" << endl;
    }
    
    double calculateSalary() const override {
        return hoursWorked * hourlyRate;
    }
    
    void display() const override {
        cout << "ID: " << id << ", Name: " << name 
             << ", Hours: " << hoursWorked << ", Rate: $" << hourlyRate
             << ", Total: $" << calculateSalary() << endl;
    }
    
    void addHours(int hours) {
        hoursWorked += hours;
        cout << name << " worked " << hours << " more hours. Total: " << hoursWorked << endl;
    }
};

int main() {
    cout << "=== Employee Hierarchy ===" << endl;
    
    cout << "\n1. Creating employees:" << endl;
    Manager alice("Alice Johnson", 85000, 15000, 5);
    Developer bob("Bob Smith", 75000, "C++", 3);
    Intern charlie("Charlie Brown", 20, 80);
    
    cout << "\n2. Displaying employee details:" << endl;
    alice.display();
    cout << endl;
    bob.display();
    cout << endl;
    charlie.display();
    
    cout << "\n3. Employee actions:" << endl;
    alice.addBonus(5000);
    bob.completeProject();
    charlie.addHours(40);
    
    cout << "\n4. Updated salaries:" << endl;
    cout << "Alice's salary: $" << alice.calculateSalary() << endl;
    cout << "Bob's salary: $" << bob.calculateSalary() << endl;
    cout << "Charlie's salary: $" << charlie.calculateSalary() << endl;
    
    cout << "\n5. Polymorphic container:" << endl;
    Employee* employees[] = {&alice, &bob, &charlie};
    
    for (auto emp : employees) {
        emp->display();
        cout << endl;
    }
    
    return 0;
}
```

---

## 📊 Inheritance Basics Summary

| Aspect | Description |
|--------|-------------|
| **Syntax** | `class Derived : public Base` |
| **Base Class** | Class being inherited from |
| **Derived Class** | Class that inherits |
| **Access** | Public, protected, private inheritance |
| **Member Access** | Derived can access public and protected members |
| **Constructor Order** | Base → Derived |
| **Destructor Order** | Derived → Base |

---

## ✅ Best Practices

1. **Use public inheritance** for "is-a" relationships
2. **Make base class destructor virtual** for polymorphic classes
3. **Initialize base class** in derived constructor initialization list
4. **Use protected** for members that derived classes need
5. **Prefer composition** over inheritance when relationship is "has-a"
6. **Follow Liskov Substitution Principle** - derived should be substitutable for base

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Missing virtual destructor** | Memory leak in polymorphism | Make base destructor virtual |
| **Slicing** | Assigning derived to base loses derived data | Use pointers/references |
| **Incorrect constructor call** | Base not initialized | Use initialization list |
| **Overriding non-virtual** | Unexpected behavior | Mark overridden methods virtual |

---

## ✅ Key Takeaways

1. **Inheritance** allows code reuse and hierarchical relationships
2. **Derived class** inherits all members except private
3. **Constructor** calls base constructor first
4. **Destructor** calls derived destructor first, then base
5. **Public inheritance** models "is-a" relationships
6. **Protected members** are accessible in derived classes
7. **Virtual functions** enable polymorphic behavior

---
---

## Next Step

- Go to [Types of Inheritance](./02_Types_of_Inheritance/README.md) to understand different types of Inheritance.