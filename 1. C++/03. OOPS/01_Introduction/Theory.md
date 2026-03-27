# Object-Oriented Programming (OOP) - Introduction

## 📖 Overview

Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around **objects** rather than functions and logic. An object is a self-contained entity that contains both **data** (attributes) and **methods** (behaviors) that operate on that data. OOP aims to implement real-world entities like inheritance, hiding, and polymorphism in programming.

## 🎯 Core Principles of OOP

Object-Oriented Programming is built on four fundamental principles:

### 1. **Encapsulation**
- Bundling data and methods that operate on that data within a single unit (class)
- Hiding internal state and requiring all interaction to be performed through an object's methods
- Protects data integrity and prevents unauthorized access

### 2. **Abstraction**
- Hiding complex implementation details and showing only essential features
- Providing a simple interface while hiding the complexity behind it
- Reduces complexity and isolates impact of changes

### 3. **Inheritance**
- Creating new classes (derived) based on existing classes (base)
- Reusing code and establishing hierarchical relationships
- Enables polymorphism and code reuse

### 4. **Polymorphism**
- Ability of objects to take multiple forms
- Same interface, different implementations
- Compile-time (function overloading) and run-time (virtual functions)

---

## 🔄 Procedural vs Object-Oriented Programming

| Aspect | Procedural Programming | Object-Oriented Programming |
|--------|------------------------|----------------------------|
| **Approach** | Top-down | Bottom-up |
| **Focus** | Functions and procedures | Objects and classes |
| **Data** | Data moves freely between functions | Data is encapsulated within objects |
| **Reusability** | Limited through functions | High through inheritance and composition |
| **Security** | Low (data is exposed) | High (data hiding) |
| **Modularity** | Function-based | Class-based |
| **Real-world mapping** | Difficult | Natural |
| **Maintenance** | Harder for large programs | Easier due to modularity |
| **Examples** | C, Pascal, FORTRAN | C++, Java, Python, C# |

---

## 💡 Benefits of Object-Oriented Programming

### 1. **Code Reusability**
- Inheritance allows reuse of existing code
- Reduces development time and effort
- Promotes DRY (Don't Repeat Yourself) principle

### 2. **Modularity**
- Classes are independent modules
- Easier to debug and maintain
- Changes in one class don't affect others

### 3. **Data Security**
- Encapsulation protects data from unauthorized access
- Controlled access through methods
- Prevents accidental data corruption

### 4. **Scalability**
- Easy to extend existing functionality
- New features can be added without breaking existing code
- Suitable for large, complex applications

### 5. **Maintainability**
- Organized code structure
- Easier to understand and modify
- Reduced complexity through abstraction

### 6. **Real-World Modeling**
- Natural representation of real-world entities
- Makes problem-solving more intuitive
- Better communication between developers and domain experts

---

## 📚 Basic OOP Terminology

| Term | Definition | Example |
|------|------------|---------|
| **Class** | Blueprint or template for creating objects | `class Car { ... };` |
| **Object** | Instance of a class | `Car myCar;` |
| **Attribute** | Data member/variable that holds object state | `string color;` |
| **Method** | Function that defines object behavior | `void startEngine();` |
| **Constructor** | Special method called when object is created | `Car();` |
| **Destructor** | Special method called when object is destroyed | `~Car();` |
| **Interface** | Set of methods that define behavior | Pure virtual functions |
| **Message** | Request to an object to execute a method | `myCar.startEngine();` |

---

## 🏗️ Structure of a C++ Class

```cpp
class ClassName {
private:
    // Data members (attributes)
    int dataMember;
    
public:
    // Constructor
    ClassName() {
        // Initialization code
    }
    
    // Member functions (methods)
    void memberFunction() {
        // Function body
    }
    
    // Destructor
    ~ClassName() {
        // Cleanup code
    }
};
```

---

## 🌍 Real-World Example: A Car Object

```cpp
#include <iostream>
#include <string>
using namespace std;

class Car {
private:
    string brand;
    string model;
    int year;
    int speed;
    
public:
    // Constructor
    Car(string b, string m, int y) {
        brand = b;
        model = m;
        year = y;
        speed = 0;
    }
    
    // Methods
    void accelerate(int amount) {
        speed += amount;
        cout << brand << " " << model << " accelerated to " << speed << " km/h" << endl;
    }
    
    void brake(int amount) {
        speed = max(0, speed - amount);
        cout << brand << " " << model << " slowed to " << speed << " km/h" << endl;
    }
    
    void displayInfo() {
        cout << "Car: " << brand << " " << model << " (" << year << ")" << endl;
        cout << "Current speed: " << speed << " km/h" << endl;
    }
};

int main() {
    // Creating objects (instances)
    Car myCar("Toyota", "Camry", 2022);
    Car yourCar("Honda", "Civic", 2021);
    
    // Interacting with objects
    myCar.displayInfo();
    myCar.accelerate(50);
    myCar.brake(20);
    
    yourCar.displayInfo();
    yourCar.accelerate(30);
    
    return 0;
}
```

**Output:**
```
Car: Toyota Camry (2022)
Current speed: 0 km/h
Toyota Camry accelerated to 50 km/h
Toyota Camry slowed to 30 km/h
Car: Honda Civic (2021)
Current speed: 0 km/h
Honda Civic accelerated to 30 km/h
```

---

## ⚡ Advantages and Disadvantages

### Advantages
- ✅ **Reusability**: Inheritance allows code reuse
- ✅ **Flexibility**: Polymorphism enables flexible code
- ✅ **Maintainability**: Encapsulation isolates changes
- ✅ **Security**: Data hiding protects information
- ✅ **Scalability**: Easy to add new features
- ✅ **Real-world mapping**: Intuitive design

### Disadvantages
- ❌ **Complexity**: Steeper learning curve
- ❌ **Size**: Larger program size
- ❌ **Speed**: Slightly slower than procedural (due to overhead)
- ❌ **Design effort**: Requires more upfront design
- ❌ **Over-engineering**: Can lead to unnecessary complexity

---

## 📊 When to Use OOP

| Use OOP When... | Avoid OOP When... |
|-----------------|-------------------|
| Building large, complex systems | Building small, simple programs |
| Need code reusability | Performance is critical |
| Working in a team | Memory is extremely limited |
| Long-term maintenance required | Problem is naturally procedural |
| Modeling real-world entities | Low-level system programming |
| Building frameworks or libraries | Simple scripts or utilities |

---

## ✅ Key Takeaways

1. OOP is a programming paradigm based on objects containing data and methods
2. Four pillars: Encapsulation, Abstraction, Inheritance, Polymorphism
3. Benefits: Reusability, modularity, security, scalability, maintainability
4. Classes are blueprints; objects are instances
5. OOP models real-world entities naturally
6. C++ supports OOP with classes, inheritance, polymorphism, and encapsulation

---