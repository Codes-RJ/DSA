# Multilevel Inheritance in C++ - Complete Guide

## 📖 Overview

Multilevel inheritance is a chain of inheritance where a class inherits from a derived class, which itself inherits from another base class. This creates a hierarchical chain of relationships, forming a parent-child-grandchild structure.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Multilevel Inheritance** | Chain of inheritance: A → B → C |
| **Grandparent** | The top-most base class |
| **Parent** | Intermediate derived class |
| **Child** | Most derived class |
| **Properties** | Members are inherited through all levels |

---

## 1. **Basic Multilevel Inheritance**

```cpp
#include <iostream>
#include <string>
using namespace std;

// Grandparent class (Level 1)
class Vehicle {
protected:
    string brand;
    int year;
    
public:
    Vehicle(string b, int y) : brand(b), year(y) {
        cout << "Vehicle constructor: " << brand << endl;
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
    
    virtual ~Vehicle() {
        cout << "Vehicle destructor: " << brand << endl;
    }
};

// Parent class (Level 2) - inherits from Vehicle
class Car : public Vehicle {
protected:
    int doors;
    string fuelType;
    
public:
    Car(string b, int y, int d, string fuel) 
        : Vehicle(b, y), doors(d), fuelType(fuel) {
        cout << "  Car constructor: " << brand << endl;
    }
    
    void honk() {
        cout << brand << " car honks: Beep! Beep!" << endl;
    }
    
    void display() override {
        Vehicle::display();
        cout << "  Doors: " << doors << ", Fuel: " << fuelType << endl;
    }
    
    ~Car() override {
        cout << "  Car destructor: " << brand << endl;
    }
};

// Child class (Level 3) - inherits from Car
class ElectricCar : public Car {
private:
    int batteryCapacity;
    int chargeLevel;
    
public:
    ElectricCar(string b, int y, int d, int battery) 
        : Car(b, y, d, "Electric"), batteryCapacity(battery), chargeLevel(100) {
        cout << "    ElectricCar constructor: " << brand << endl;
    }
    
    void charge() {
        chargeLevel = 100;
        cout << brand << " electric car charging to 100%" << endl;
    }
    
    void display() override {
        Car::display();
        cout << "    Battery: " << batteryCapacity << " kWh, Charge: " << chargeLevel << "%" << endl;
    }
    
    void start() override {
        cout << brand << " electric car starting silently..." << endl;
    }
    
    ~ElectricCar() override {
        cout << "    ElectricCar destructor: " << brand << endl;
    }
};

int main() {
    cout << "=== Basic Multilevel Inheritance ===" << endl;
    
    cout << "\nCreating ElectricCar (Vehicle → Car → ElectricCar):" << endl;
    ElectricCar tesla("Tesla", 2024, 4, 75);
    
    cout << "\n=== Using Inherited Features ===" << endl;
    tesla.display();
    tesla.start();    // Overridden in ElectricCar
    tesla.honk();     // From Car
    tesla.charge();   // ElectricCar's own method
    tesla.stop();     // From Vehicle
    
    return 0;
}
```

**Output:**
```
=== Basic Multilevel Inheritance ===

Creating ElectricCar (Vehicle → Car → ElectricCar):
Vehicle constructor: Tesla
  Car constructor: Tesla
    ElectricCar constructor: Tesla

=== Using Inherited Features ===
Brand: Tesla, Year: 2024
  Doors: 4, Fuel: Electric
    Battery: 75 kWh, Charge: 100%
Tesla electric car starting silently...
Tesla car honks: Beep! Beep!
Tesla electric car charging to 100%
Tesla vehicle stopping...
    ElectricCar destructor: Tesla
  Car destructor: Tesla
Vehicle destructor: Tesla
```

---

## 2. **Member Access Through Levels**

```cpp
#include <iostream>
#include <string>
using namespace std;

class GrandParent {
private:
    int privateGP = 1;
    
protected:
    int protectedGP = 2;
    
public:
    int publicGP = 3;
    
    void showGP() {
        cout << "GrandParent - Private: " << privateGP << endl;
        cout << "GrandParent - Protected: " << protectedGP << endl;
        cout << "GrandParent - Public: " << publicGP << endl;
    }
    
    int getPrivateGP() const { return privateGP; }
};

class Parent : public GrandParent {
public:
    void showParent() {
        // cout << privateGP << endl;      // Error! Private not accessible
        cout << "Parent - Protected: " << protectedGP << endl;  // OK
        cout << "Parent - Public: " << publicGP << endl;        // OK
        cout << "Parent - Private via getter: " << getPrivateGP() << endl;
    }
    
    void modifyParent() {
        protectedGP = 20;
        publicGP = 30;
        // privateGP = 10;  // Error! Cannot modify private
    }
};

class Child : public Parent {
public:
    void showChild() {
        // cout << privateGP << endl;      // Error! Not accessible
        cout << "Child - Protected: " << protectedGP << endl;    // OK (inherited)
        cout << "Child - Public: " << publicGP << endl;          // OK (inherited)
        cout << "Child - Private via getter: " << getPrivateGP() << endl;
    }
    
    void modifyChild() {
        protectedGP = 200;
        publicGP = 300;
    }
};

int main() {
    cout << "=== Member Access Through Levels ===" << endl;
    
    GrandParent gp;
    Parent parent;
    Child child;
    
    cout << "\n1. GrandParent accessing its members:" << endl;
    gp.showGP();
    
    cout << "\n2. Parent accessing inherited members:" << endl;
    parent.showParent();
    
    cout << "\n3. Child accessing inherited members:" << endl;
    child.showChild();
    
    cout << "\n4. Modifying at different levels:" << endl;
    parent.modifyParent();
    child.modifyChild();
    
    cout << "\n5. After modifications:" << endl;
    cout << "Parent view: ";
    parent.showParent();
    cout << "Child view: ";
    child.showChild();
    
    return 0;
}
```

---

## 3. **Constructor and Destructor Order**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Level1 {
private:
    string name;
    
public:
    Level1(string n) : name(n) {
        cout << "Level1 constructor: " << name << endl;
    }
    
    ~Level1() {
        cout << "Level1 destructor: " << name << endl;
    }
};

class Level2 : public Level1 {
private:
    string name;
    
public:
    Level2(string n1, string n2) : Level1(n1), name(n2) {
        cout << "  Level2 constructor: " << name << endl;
    }
    
    ~Level2() {
        cout << "  Level2 destructor: " << name << endl;
    }
};

class Level3 : public Level2 {
private:
    string name;
    
public:
    Level3(string n1, string n2, string n3) : Level2(n1, n2), name(n3) {
        cout << "    Level3 constructor: " << name << endl;
    }
    
    ~Level3() {
        cout << "    Level3 destructor: " << name << endl;
    }
};

class Level4 : public Level3 {
private:
    string name;
    
public:
    Level4(string n1, string n2, string n3, string n4) 
        : Level3(n1, n2, n3), name(n4) {
        cout << "      Level4 constructor: " << name << endl;
    }
    
    ~Level4() {
        cout << "      Level4 destructor: " << name << endl;
    }
};

int main() {
    cout << "=== Constructor/Destructor Order in Multilevel Inheritance ===" << endl;
    cout << "\nConstruction order: Top to Bottom (Level1 → Level2 → Level3 → Level4)" << endl;
    cout << "Destruction order: Bottom to Top (Level4 → Level3 → Level2 → Level1)\n" << endl;
    
    {
        Level4 obj("L1", "L2", "L3", "L4");
        cout << "\nObject created successfully" << endl;
    }  // Destructor called here
    
    return 0;
}
```

**Output:**
```
=== Constructor/Destructor Order in Multilevel Inheritance ===

Construction order: Top to Bottom (Level1 → Level2 → Level3 → Level4)
Destruction order: Bottom to Top (Level4 → Level3 → Level2 → Level1)

Level1 constructor: L1
  Level2 constructor: L2
    Level3 constructor: L3
      Level4 constructor: L4

Object created successfully
      Level4 destructor: L4
    Level3 destructor: L3
  Level2 destructor: L2
Level1 destructor: L1
```

---

## 4. **Method Overriding at Different Levels**

```cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

class Shape {
protected:
    string color;
    
public:
    Shape(string c) : color(c) {}
    
    virtual double area() const {
        return 0;
    }
    
    virtual void draw() const {
        cout << "Drawing a generic shape" << endl;
    }
    
    virtual void display() const {
        cout << "Shape color: " << color << endl;
    }
    
    virtual ~Shape() {}
};

class TwoDShape : public Shape {
protected:
    double perimeter;
    
public:
    TwoDShape(string c) : Shape(c), perimeter(0) {}
    
    virtual double perimeter() const {
        return perimeter;
    }
    
    void draw() const override {
        cout << "Drawing a 2D shape" << endl;
    }
    
    void display() const override {
        Shape::display();
        cout << "  Perimeter: " << perimeter << endl;
    }
};

class Circle : public TwoDShape {
private:
    double radius;
    
public:
    Circle(string c, double r) : TwoDShape(c), radius(r) {
        perimeter = 2 * M_PI * radius;
    }
    
    double area() const override {
        return M_PI * radius * radius;
    }
    
    void draw() const override {
        cout << "Drawing a " << color << " circle with radius " << radius << endl;
    }
    
    void display() const override {
        TwoDShape::display();
        cout << "  Radius: " << radius << ", Area: " << area() << endl;
    }
};

class Rectangle : public TwoDShape {
private:
    double width, height;
    
public:
    Rectangle(string c, double w, double h) : TwoDShape(c), width(w), height(h) {
        perimeter = 2 * (width + height);
    }
    
    double area() const override {
        return width * height;
    }
    
    void draw() const override {
        cout << "Drawing a " << color << " rectangle " << width << "x" << height << endl;
    }
    
    void display() const override {
        TwoDShape::display();
        cout << "  Dimensions: " << width << "x" << height << ", Area: " << area() << endl;
    }
};

int main() {
    cout << "=== Method Overriding at Different Levels ===" << endl;
    
    cout << "\nCreating shapes:" << endl;
    Circle circle("Red", 5.0);
    Rectangle rect("Blue", 4.0, 6.0);
    
    cout << "\nCalling methods at different levels:" << endl;
    cout << "\n--- Circle ---" << endl;
    circle.display();
    circle.draw();
    cout << "Area: " << circle.area() << endl;
    cout << "Perimeter: " << circle.perimeter() << endl;
    
    cout << "\n--- Rectangle ---" << endl;
    rect.display();
    rect.draw();
    cout << "Area: " << rect.area() << endl;
    cout << "Perimeter: " << rect.perimeter() << endl;
    
    cout << "\nPolymorphic behavior through base pointers:" << endl;
    Shape* shapes[] = {&circle, &rect};
    for (auto shape : shapes) {
        shape->draw();      // Calls appropriate draw()
        shape->display();   // Calls appropriate display()
    }
    
    return 0;
}
```

---

## 5. **Practical Example: Employee Hierarchy**

```cpp
#include <iostream>
#include <string>
#include <iomanip>
#include <vector>
using namespace std;

// Level 1: Person
class Person {
protected:
    string name;
    int age;
    string email;
    
public:
    Person(string n, int a, string e) : name(n), age(a), email(e) {
        cout << "Person created: " << name << endl;
    }
    
    virtual void work() const {
        cout << name << " is working" << endl;
    }
    
    virtual void display() const {
        cout << "Name: " << name << ", Age: " << age << ", Email: " << email << endl;
    }
    
    virtual ~Person() {
        cout << "Person destroyed: " << name << endl;
    }
};

// Level 2: Employee (inherits from Person)
class Employee : public Person {
protected:
    int employeeId;
    double salary;
    static int nextId;
    
public:
    Employee(string n, int a, string e, double sal) 
        : Person(n, a, e), salary(sal) {
        employeeId = nextId++;
        cout << "  Employee created: ID=" << employeeId << endl;
    }
    
    void work() const override {
        cout << name << " (Employee) is performing assigned tasks" << endl;
    }
    
    void display() const override {
        Person::display();
        cout << "  ID: " << employeeId << ", Salary: $" << fixed << setprecision(2) << salary << endl;
    }
    
    double getSalary() const { return salary; }
    void giveRaise(double percent) {
        salary += salary * (percent / 100);
        cout << name << " received " << percent << "% raise. New salary: $" << salary << endl;
    }
    
    ~Employee() override {
        cout << "  Employee destroyed: " << name << endl;
    }
};

int Employee::nextId = 1000;

// Level 3: Manager (inherits from Employee)
class Manager : public Employee {
private:
    int teamSize;
    vector<string> teamMembers;
    double bonus;
    
public:
    Manager(string n, int a, string e, double sal, int size) 
        : Employee(n, a, e, sal), teamSize(size), bonus(0) {
        cout << "    Manager created: Leading " << teamSize << " people" << endl;
    }
    
    void work() const override {
        cout << name << " (Manager) is managing team of " << teamSize << " people" << endl;
    }
    
    void addTeamMember(const string& member) {
        teamMembers.push_back(member);
        cout << member << " added to " << name << "'s team" << endl;
    }
    
    void setBonus(double b) {
        bonus = b;
        cout << name << " received bonus of $" << bonus << endl;
    }
    
    double calculateTotalCompensation() const {
        return salary + bonus;
    }
    
    void display() const override {
        Employee::display();
        cout << "  Team Size: " << teamSize << ", Bonus: $" << bonus << endl;
        cout << "  Total Compensation: $" << calculateTotalCompensation() << endl;
        if (!teamMembers.empty()) {
            cout << "  Team Members: ";
            for (const auto& m : teamMembers) cout << m << " ";
            cout << endl;
        }
    }
    
    ~Manager() override {
        cout << "    Manager destroyed: " << name << endl;
    }
};

// Level 4: Director (inherits from Manager)
class Director : public Manager {
private:
    int departmentCount;
    double stockOptions;
    
public:
    Director(string n, int a, string e, double sal, int teamSize, int deptCount, double stocks) 
        : Manager(n, a, e, sal, teamSize), departmentCount(deptCount), stockOptions(stocks) {
        cout << "      Director created: Overseeing " << departmentCount << " departments" << endl;
    }
    
    void work() const override {
        cout << name << " (Director) is setting strategic direction for " 
             << departmentCount << " departments" << endl;
    }
    
    double calculateTotalCompensation() const {
        return Manager::calculateTotalCompensation() + stockOptions;
    }
    
    void display() const override {
        Manager::display();
        cout << "  Departments: " << departmentCount << ", Stock Options: $" << stockOptions << endl;
    }
    
    ~Director() override {
        cout << "      Director destroyed: " << name << endl;
    }
};

int main() {
    cout << "=== Employee Hierarchy (Multilevel Inheritance) ===" << endl;
    
    cout << "\n1. Creating hierarchy:" << endl;
    Person p("John Public", 30, "john@email.com");
    Employee e("Alice Smith", 25, "alice@company.com", 60000);
    Manager m("Bob Johnson", 40, "bob@company.com", 90000, 5);
    Director d("Carol Williams", 50, "carol@company.com", 150000, 8, 3, 50000);
    
    cout << "\n2. Working behaviors:" << endl;
    p.work();
    e.work();
    m.work();
    d.work();
    
    cout << "\n3. Manager actions:" << endl;
    m.addTeamMember("Alice");
    m.addTeamMember("Bob");
    m.setBonus(10000);
    
    cout << "\n4. Director actions:" << endl;
    d.addTeamMember("Manager1");
    d.addTeamMember("Manager2");
    d.setBonus(25000);
    
    cout << "\n5. Displaying all:" << endl;
    cout << "\n--- Person ---" << endl;
    p.display();
    cout << "\n--- Employee ---" << endl;
    e.display();
    cout << "\n--- Manager ---" << endl;
    m.display();
    cout << "\n--- Director ---" << endl;
    d.display();
    
    cout << "\n6. Polymorphic container:" << endl;
    vector<Person*> people = {&p, &e, &m, &d};
    for (auto person : people) {
        person->work();  // Polymorphic behavior
    }
    
    return 0;
}
```

---

## 📊 Multilevel Inheritance Summary

| Aspect | Description |
|--------|-------------|
| **Syntax** | `class C : public B { }; class B : public A { };` |
| **Depth** | Unlimited levels |
| **Property Flow** | Properties flow downward through all levels |
| **Constructor Order** | Top-most base → ... → Most derived |
| **Destructor Order** | Most derived → ... → Top-most base |
| **Method Overriding** | Can override at any level |

---

## ✅ Best Practices

1. **Keep hierarchy depth reasonable** - Deep hierarchies become complex
2. **Follow IS-A relationship** - Each level should represent a valid IS-A relationship
3. **Use virtual functions** for polymorphic behavior
4. **Make base destructors virtual** for proper cleanup
5. **Avoid unnecessary levels** - Only add levels that add meaningful functionality

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Too deep hierarchy** | Complexity, maintenance issues | Limit depth, use composition |
| **Violating IS-A** | Semantic errors | Ensure each level is truly a specialization |
| **Incorrect constructor initialization** | Missing base initialization | Initialize all base classes |
| **Method hiding** | Unexpected behavior | Use `override` keyword |

---

## ✅ Key Takeaways

1. **Multilevel inheritance** creates a chain of specialization
2. **Properties** are inherited through all levels
3. **Constructor order** is top-down (base to derived)
4. **Destructor order** is bottom-up (derived to base)
5. **Method overriding** can occur at any level
6. **Polymorphism** works across all levels
7. **Virtual destructors** ensure proper cleanup

---
---

## Next Step

- Go to [4_Hierarchical_Inheritance.md](4_Hierarchical_Inheritance.md) to continue with Hierarchical Inheritance.
