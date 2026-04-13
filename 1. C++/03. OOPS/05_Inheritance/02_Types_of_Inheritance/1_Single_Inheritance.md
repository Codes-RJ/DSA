# Single Inheritance in C++ - Complete Guide

## 📖 Overview

Single inheritance is the simplest form of inheritance where a derived class inherits from exactly one base class. This creates a direct parent-child relationship and forms the foundation for more complex inheritance hierarchies.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Single Inheritance** | One derived class inherits from one base class |
| **Parent Class** | The class being inherited from (Base) |
| **Child Class** | The class that inherits (Derived) |
| **Relationship** | "is-a" relationship (e.g., Dog is an Animal) |

---

## 1. **Basic Single Inheritance**

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
        cout << "Animal constructor: " << name << endl;
    }
    
    void eat() {
        cout << name << " is eating" << endl;
    }
    
    void sleep() {
        cout << name << " is sleeping" << endl;
    }
    
    virtual void sound() {
        cout << name << " makes a sound" << endl;
    }
    
    void display() {
        cout << "Name: " << name << ", Age: " << age << endl;
    }
    
    virtual ~Animal() {
        cout << "Animal destructor: " << name << endl;
    }
};

// Derived class (Child) - Single inheritance
class Dog : public Animal {
private:
    string breed;
    
public:
    Dog(string n, int a, string b) : Animal(n, a), breed(b) {
        cout << "  Dog constructor: " << name << endl;
    }
    
    // Additional functionality
    void bark() {
        cout << name << " says: Woof! Woof!" << endl;
    }
    
    void wagTail() {
        cout << name << " is wagging tail" << endl;
    }
    
    // Override base class method
    void sound() override {
        cout << name << " barks loudly!" << endl;
    }
    
    void display() {
        Animal::display();
        cout << "  Breed: " << breed << endl;
    }
    
    ~Dog() override {
        cout << "Dog destructor: " << name << endl;
    }
};

int main() {
    cout << "=== Single Inheritance Demo ===" << endl;
    
    cout << "\nCreating Dog object:" << endl;
    Dog dog("Buddy", 3, "Golden Retriever");
    
    cout << "\n=== Using Inherited Methods ===" << endl;
    dog.display();
    dog.eat();      // From Animal
    dog.sleep();    // From Animal
    dog.sound();    // Overridden
    dog.bark();     // Dog's own method
    dog.wagTail();  // Dog's own method
    
    return 0;
}
```

**Output:**
```
=== Single Inheritance Demo ===

Creating Dog object:
Animal constructor: Buddy
  Dog constructor: Buddy

=== Using Inherited Methods ===
Name: Buddy, Age: 3
  Breed: Golden Retriever
Buddy is eating
Buddy is sleeping
Buddy barks loudly!
Buddy says: Woof! Woof!
Buddy is wagging tail
Dog destructor: Buddy
Animal destructor: Buddy
```

---

## 2. **Single Inheritance with Different Access Specifiers**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Base {
private:
    int privateVar = 1;
    
protected:
    int protectedVar = 2;
    
public:
    int publicVar = 3;
    
    void showBase() {
        cout << "Private: " << privateVar << endl;
        cout << "Protected: " << protectedVar << endl;
        cout << "Public: " << publicVar << endl;
    }
    
    int getPrivate() const { return privateVar; }
    void setPrivate(int val) { privateVar = val; }
};

// Public Inheritance
class PublicDerived : public Base {
public:
    void show() {
        // cout << privateVar << endl;  // Error! Private not accessible
        cout << "Protected: " << protectedVar << endl;  // OK - becomes protected
        cout << "Public: " << publicVar << endl;        // OK - remains public
        cout << "Private via getter: " << getPrivate() << endl;
    }
    
    void modify() {
        protectedVar = 20;    // OK - can modify protected
        publicVar = 30;       // OK - can modify public
        setPrivate(10);       // Modify private via setter
    }
};

// Protected Inheritance
class ProtectedDerived : protected Base {
public:
    void show() {
        cout << "Protected: " << protectedVar << endl;  // OK
        cout << "Public: " << publicVar << endl;        // OK - becomes protected
    }
};

// Private Inheritance
class PrivateDerived : private Base {
public:
    void show() {
        cout << "Protected: " << protectedVar << endl;  // OK
        cout << "Public: " << publicVar << endl;        // OK - becomes private
    }
};

int main() {
    cout << "=== Single Inheritance with Access Specifiers ===" << endl;
    
    cout << "\n1. Public Inheritance:" << endl;
    PublicDerived pub;
    pub.modify();
    pub.show();
    pub.publicVar = 100;     // OK - public
    
    cout << "\n2. Protected Inheritance:" << endl;
    ProtectedDerived prot;
    prot.show();
    // prot.publicVar = 100;  // Error! Now protected
    
    cout << "\n3. Private Inheritance:" << endl;
    PrivateDerived priv;
    priv.show();
    // priv.publicVar = 100;  // Error! Now private
    
    return 0;
}
```

---

## 3. **Constructor and Destructor Order**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Base {
private:
    string name;
    
public:
    Base(string n) : name(n) {
        cout << "Base constructor: " << name << endl;
    }
    
    ~Base() {
        cout << "Base destructor: " << name << endl;
    }
    
    void show() {
        cout << "Base: " << name << endl;
    }
};

class Member {
private:
    string name;
    
public:
    Member(string n) : name(n) {
        cout << "  Member constructor: " << name << endl;
    }
    
    ~Member() {
        cout << "  Member destructor: " << name << endl;
    }
};

class Derived : public Base {
private:
    Member m1;
    Member m2;
    
public:
    Derived(string baseName, string m1Name, string m2Name) 
        : Base(baseName), m2(m2Name), m1(m1Name) {  // Order in list doesn't matter
        cout << "Derived constructor body" << endl;
    }
    
    ~Derived() {
        cout << "Derived destructor body" << endl;
    }
};

int main() {
    cout << "=== Constructor/Destructor Order in Single Inheritance ===" << endl;
    cout << "\nConstruction order:" << endl;
    cout << "1. Base class constructor" << endl;
    cout << "2. Member objects (in declaration order)" << endl;
    cout << "3. Derived class constructor body" << endl;
    cout << "\nDestruction order: REVERSE of construction\n" << endl;
    
    {
        Derived d("BaseObj", "Member1", "Member2");
        cout << "\nObject created successfully" << endl;
    }  // Destructor called here
    
    return 0;
}
```

**Output:**
```
=== Constructor/Destructor Order in Single Inheritance ===

Construction order:
1. Base class constructor
2. Member objects (in declaration order)
3. Derived class constructor body

Destruction order: REVERSE of construction

Base constructor: BaseObj
  Member constructor: Member1
  Member constructor: Member2
Derived constructor body

Object created successfully
Derived destructor body
  Member destructor: Member2
  Member destructor: Member1
Base destructor: BaseObj
```

---

## 4. **Practical Example: Vehicle Hierarchy**

```cpp
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

class Vehicle {
protected:
    string brand;
    string model;
    int year;
    double mileage;
    
public:
    Vehicle(string b, string m, int y) 
        : brand(b), model(m), year(y), mileage(0) {
        cout << "Vehicle created: " << brand << " " << model << endl;
    }
    
    virtual ~Vehicle() {
        cout << "Vehicle destroyed: " << brand << " " << model << endl;
    }
    
    void drive(double distance) {
        mileage += distance;
        cout << "Driven " << distance << " km. Total mileage: " << mileage << " km" << endl;
    }
    
    virtual void display() const {
        cout << brand << " " << model << " (" << year << ") - " 
             << fixed << setprecision(1) << mileage << " km" << endl;
    }
    
    virtual double calculateMaintenanceCost() const {
        return mileage * 0.1;  // Base calculation
    }
    
    string getBrand() const { return brand; }
    string getModel() const { return model; }
};

class Car : public Vehicle {
private:
    int doors;
    string fuelType;
    
public:
    Car(string b, string m, int y, int d, string fuel) 
        : Vehicle(b, m, y), doors(d), fuelType(fuel) {
        cout << "  Car created: " << doors << "-door, " << fuelType << endl;
    }
    
    ~Car() override {
        cout << "  Car destroyed" << endl;
    }
    
    void honk() {
        cout << brand << " " << model << " honks: Beep! Beep!" << endl;
    }
    
    void display() const override {
        Vehicle::display();
        cout << "  " << doors << " doors, " << fuelType << " fuel" << endl;
    }
    
    double calculateMaintenanceCost() const override {
        // Cars have higher maintenance cost
        return Vehicle::calculateMaintenanceCost() + 200;
    }
};

class Motorcycle : public Vehicle {
private:
    bool hasSidecar;
    int engineCC;
    
public:
    Motorcycle(string b, string m, int y, int cc, bool sidecar) 
        : Vehicle(b, m, y), engineCC(cc), hasSidecar(sidecar) {
        cout << "  Motorcycle created: " << engineCC << "cc" << endl;
    }
    
    ~Motorcycle() override {
        cout << "  Motorcycle destroyed" << endl;
    }
    
    void wheelie() {
        cout << brand << " " << model << " doing a wheelie!" << endl;
    }
    
    void display() const override {
        Vehicle::display();
        cout << "  " << engineCC << "cc, Sidecar: " << (hasSidecar ? "Yes" : "No") << endl;
    }
    
    double calculateMaintenanceCost() const override {
        // Motorcycles have lower maintenance cost
        return Vehicle::calculateMaintenanceCost() + 100;
    }
};

class Truck : public Vehicle {
private:
    double loadCapacity;
    int axles;
    
public:
    Truck(string b, string m, int y, double capacity, int ax) 
        : Vehicle(b, m, y), loadCapacity(capacity), axles(ax) {
        cout << "  Truck created: " << loadCapacity << " tons, " << axles << " axles" << endl;
    }
    
    ~Truck() override {
        cout << "  Truck destroyed" << endl;
    }
    
    void loadCargo(double weight) {
        cout << "Loading " << weight << " tons into " << brand << " " << model << endl;
    }
    
    void display() const override {
        Vehicle::display();
        cout << "  Capacity: " << loadCapacity << " tons, " << axles << " axles" << endl;
    }
    
    double calculateMaintenanceCost() const override {
        // Trucks have highest maintenance cost
        return Vehicle::calculateMaintenanceCost() + 500;
    }
};

int main() {
    cout << "=== Vehicle Hierarchy with Single Inheritance ===" << endl;
    
    cout << "\n1. Creating vehicles:" << endl;
    Car car("Toyota", "Camry", 2022, 4, "Petrol");
    Motorcycle bike("Harley", "Sportster", 2021, 1200, false);
    Truck truck("Volvo", "FH16", 2023, 25.0, 3);
    
    cout << "\n2. Driving vehicles:" << endl;
    car.drive(150);
    bike.drive(80);
    truck.drive(300);
    
    cout << "\n3. Vehicle-specific actions:" << endl;
    car.honk();
    bike.wheelie();
    truck.loadCargo(15);
    
    cout << "\n4. Displaying details:" << endl;
    car.display();
    cout << endl;
    bike.display();
    cout << endl;
    truck.display();
    
    cout << "\n5. Maintenance costs:" << endl;
    cout << "Car maintenance: $" << car.calculateMaintenanceCost() << endl;
    cout << "Motorcycle maintenance: $" << bike.calculateMaintenanceCost() << endl;
    cout << "Truck maintenance: $" << truck.calculateMaintenanceCost() << endl;
    
    return 0;
}
```

---

## 📊 Single Inheritance Summary

| Aspect | Description |
|--------|-------------|
| **Syntax** | `class Derived : public Base` |
| **Relationships** | One base, one derived |
| **Member Access** | Derived inherits all but private members |
| **Constructor Order** | Base → Derived |
| **Destructor Order** | Derived → Base |
| **Use Case** | "is-a" relationships |

---

## ✅ Best Practices

1. **Use public inheritance** for "is-a" relationships
2. **Make base destructor virtual** for polymorphic classes
3. **Initialize base class** in derived constructor initialization list
4. **Use protected** for members that derived classes need
5. **Follow Liskov Substitution Principle**

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Slicing** | Assigning derived to base loses data | Use pointers/references |
| **Missing virtual destructor** | Memory leak | Make base destructor virtual |
| **Incorrect constructor call** | Base not initialized | Use initialization list |
| **Accessing private members** | Compiler error | Use protected or getters/setters |

---

## ✅ Key Takeaways

1. **Single inheritance** creates a direct parent-child relationship
2. **Derived class** inherits all non-private members
3. **Constructor** calls base constructor first
4. **Virtual functions** enable polymorphic behavior
5. **Public inheritance** models "is-a" relationships
6. **Protected members** are accessible in derived classes

---
---

## Next Step

- Go to [2_Multiple_Inheritance.md](2_Multiple_Inheritance.md) to continue with Multiple Inheritance.
