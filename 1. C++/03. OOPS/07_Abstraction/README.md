# README.md

## Abstraction in C++ - Complete Guide

### Overview

Abstraction is one of the four fundamental pillars of Object-Oriented Programming (along with Encapsulation, Inheritance, and Polymorphism). Abstraction means hiding complex implementation details and showing only the essential features of an object. It focuses on what an object does rather than how it does it. In C++, abstraction is achieved primarily through abstract classes and interfaces.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [01_Abstract_Classes.md](01_Abstract_Classes.md) | understand Abstract Classes |
| 2. | [02_Interfaces_in_Cpp.md](02_Interfaces_in_Cpp.md) | understand Interfaces in C++ |
| 3. | [03_Abstract_vs_Concrete.md](03_Abstract_vs_Concrete.md) | understand Abstract vs Concrete Classes |
| 4. | [04_Design_Patterns_Intro.md](04_Design_Patterns_Intro.md) | understand Design Patterns Introduction |
| 5. | [Theory.md](Theory.md) | understand Theoretical Foundations of Abstraction |

---

## 1. Abstract Classes

This topic explains abstract classes that cannot be instantiated and serve as blueprints for derived classes.

**File:** [01_Abstract_Classes.md](01_Abstract_Classes.md)

**What you will learn:**
- What is an abstract class
- How to create abstract classes using pure virtual functions
- Properties of abstract classes (cannot be instantiated)
- Abstract classes can have constructors and data members
- Abstract classes can have implemented member functions
- Derived classes must override all pure virtual functions to become concrete

**Key Concepts:**

| Concept | Description | Example |
|---------|-------------|---------|
| **Pure Virtual Function** | Function with `= 0` syntax, no implementation in base | `virtual void draw() = 0;` |
| **Abstract Class** | Class with at least one pure virtual function | `class Shape { };` |
| **No Instantiation** | Cannot create objects of abstract class | `Shape s;` // Error |
| **Pointer/Reference** | Can have pointers/references to abstract class | `Shape* ptr;` |

**Syntax:**
```cpp
#include <iostream>
using namespace std;

// Abstract class
class Animal {
protected:
    string name_;
    int age_;
    
public:
    Animal(string name, int age) : name_(name), age_(age) {
        cout << "Animal constructor" << endl;
    }
    
    // Pure virtual functions (must be overridden)
    virtual void makeSound() = 0;
    virtual void move() = 0;
    
    // Regular member function (inherited as is)
    void display() const {
        cout << "Name: " << name_ << ", Age: " << age_ << endl;
    }
    
    virtual ~Animal() {
        cout << "Animal destructor" << endl;
    }
};

// Concrete class - must override all pure virtual functions
class Dog : public Animal {
private:
    string breed_;
    
public:
    Dog(string name, int age, string breed) 
        : Animal(name, age), breed_(breed) {
        cout << "Dog constructor" << endl;
    }
    
    void makeSound() override {
        cout << name_ << " says: Woof! Woof!" << endl;
    }
    
    void move() override {
        cout << name_ << " is running" << endl;
    }
    
    ~Dog() {
        cout << "Dog destructor" << endl;
    }
};

class Cat : public Animal {
public:
    Cat(string name, int age) : Animal(name, age) {
        cout << "Cat constructor" << endl;
    }
    
    void makeSound() override {
        cout << name_ << " says: Meow! Meow!" << endl;
    }
    
    void move() override {
        cout << name_ << " is walking silently" << endl;
    }
    
    ~Cat() {
        cout << "Cat destructor" << endl;
    }
};

int main() {
    // Cannot create Animal object
    // Animal a("Generic", 5);  // Error!
    
    // Can create pointers and references to abstract class
    Animal* animals[2];
    
    animals[0] = new Dog("Buddy", 3, "Golden Retriever");
    animals[1] = new Cat("Whiskers", 2);
    
    for (int i = 0; i < 2; i++) {
        animals[i]->display();
        animals[i]->makeSound();
        animals[i]->move();
        cout << "---" << endl;
    }
    
    for (int i = 0; i < 2; i++) {
        delete animals[i];
    }
    
    return 0;
}
```

---

## 2. Interfaces in C++

This topic explains how to create and use interfaces (pure abstract classes) in C++.

**File:** [02_Interfaces_in_Cpp.md](02_Interfaces_in_Cpp.md)

**What you will learn:**
- What is an interface in OOP
- How C++ implements interfaces (pure abstract classes)
- Interface with only pure virtual functions (no data members)
- Multiple interface inheritance
- Interface vs Abstract Class
- When to use interfaces

**Key Concepts:**

| Concept | Description | Example |
|---------|-------------|---------|
| **Interface** | Class with only pure virtual functions | No data members, no implementations |
| **Pure Abstract Class** | Another name for interface in C++ | All functions are `= 0` |
| **Multiple Interface Inheritance** | Class can implement multiple interfaces | `class C : public I1, public I2` |
| **Contract** | Interface defines what a class must do | Not how it does it |

**Syntax:**
```cpp
#include <iostream>
using namespace std;

// Interface 1 - Drawable
class IDrawable {
public:
    virtual void draw() = 0;
    virtual void setColor(string color) = 0;
    virtual ~IDrawable() { }
};

// Interface 2 - Resizable
class IResizable {
public:
    virtual void resize(double factor) = 0;
    virtual void resetSize() = 0;
    virtual ~IResizable() { }
};

// Interface 3 - Serializable
class ISerializable {
public:
    virtual string serialize() const = 0;
    virtual void deserialize(const string& data) = 0;
    virtual ~ISerializable() { }
};

// Class implementing multiple interfaces
class Shape : public IDrawable, public IResizable, public ISerializable {
private:
    string color_;
    double size_;
    string shapeType_;
    
public:
    Shape(string type, string color, double size)
        : shapeType_(type), color_(color), size_(size) { }
    
    // IDrawable implementation
    void draw() override {
        cout << "Drawing " << color_ << " " << shapeType_ << endl;
    }
    
    void setColor(string color) override {
        color_ = color;
        cout << "Color changed to " << color_ << endl;
    }
    
    // IResizable implementation
    void resize(double factor) override {
        size_ *= factor;
        cout << "Resized to " << size_ << endl;
    }
    
    void resetSize() override {
        size_ = 1.0;
        cout << "Size reset to 1.0" << endl;
    }
    
    // ISerializable implementation
    string serialize() const override {
        return shapeType_ + "|" + color_ + "|" + to_string(size_);
    }
    
    void deserialize(const string& data) override {
        // Parse data (simplified)
        cout << "Deserializing: " << data << endl;
    }
};

// Function using interface
void processDrawable(IDrawable* d) {
    d->draw();
    d->setColor("blue");
    d->draw();
}

int main() {
    Shape s("Circle", "red", 2.5);
    
    s.draw();
    s.resize(1.5);
    s.setColor("green");
    
    cout << "Serialized: " << s.serialize() << endl;
    
    processDrawable(&s);
    
    return 0;
}
```

---

## 3. Abstract vs Concrete Classes

This topic explains the differences between abstract and concrete classes and when to use each.

**File:** [03_Abstract_vs_Concrete.md](03_Abstract_vs_Concrete.md)

**What you will learn:**
- Definition of concrete classes
- Differences between abstract and concrete classes
- When to use abstract classes
- When to use concrete classes
- Partial abstraction (some pure virtual, some implemented)
- Converting between abstract and concrete

**Key Concepts:**

| Aspect | Abstract Class | Concrete Class |
|--------|----------------|----------------|
| **Instantiation** | Cannot create objects | Can create objects |
| **Pure Virtual Functions** | Has at least one | Has none |
| **Purpose** | Base class for inheritance | Standalone or leaf class |
| **Completeness** | Incomplete definition | Complete definition |
| **Use Case** | Define interface/contract | Implement specific behavior |

**Syntax:**
```cpp
#include <iostream>
using namespace std;

// Abstract class (partial abstraction)
class Logger {
public:
    // Pure virtual - must be overridden
    virtual void log(const string& message) = 0;
    
    // Implemented - can be used as is
    void setLogLevel(int level) {
        logLevel_ = level;
    }
    
    int getLogLevel() const {
        return logLevel_;
    }
    
    virtual ~Logger() { }
    
protected:
    int logLevel_ = 1;
};

// Concrete class - implements all pure virtual functions
class FileLogger : public Logger {
private:
    string filename_;
    
public:
    FileLogger(const string& file) : filename_(file) { }
    
    void log(const string& message) override {
        cout << "Writing to file " << filename_ << ": " << message << endl;
    }
};

// Concrete class - another implementation
class ConsoleLogger : public Logger {
public:
    void log(const string& message) override {
        cout << "[Console] " << message << endl;
    }
};

// Partially abstract class (still abstract)
class NetworkLogger : public Logger {
    // log() not overridden - class remains abstract
public:
    void setServerAddress(const string& addr) {
        serverAddress_ = addr;
    }
    
private:
    string serverAddress_;
};

// Concrete class derived from partially abstract class
class UDPLogger : public NetworkLogger {
public:
    void log(const string& message) override {
        cout << "Sending via UDP: " << message << endl;
    }
};

int main() {
    // Cannot create abstract class object
    // Logger l;  // Error!
    
    // Can create concrete class objects
    FileLogger fileLog("app.log");
    ConsoleLogger consoleLog;
    
    fileLog.setLogLevel(2);
    fileLog.log("Application started");
    
    consoleLog.log("User logged in");
    
    // Polymorphic usage
    Logger* loggers[] = { &fileLog, &consoleLog };
    for (Logger* log : loggers) {
        log->log("Heartbeat");
    }
    
    return 0;
}
```

---

## 4. Design Patterns Introduction

This topic introduces design patterns and how abstraction enables them.

**File:** [04_Design_Patterns_Intro.md](04_Design_Patterns_Intro.md)

**What you will learn:**
- What are design patterns
- How abstraction enables design patterns
- Common design patterns using abstraction
- Strategy Pattern
- Template Method Pattern
- Factory Pattern
- Observer Pattern

**Key Concepts:**

| Pattern | Description | How Abstraction Helps |
|---------|-------------|----------------------|
| **Strategy Pattern** | Encapsulates interchangeable algorithms | Abstract strategy interface |
| **Template Method** | Defines algorithm skeleton in base class | Abstract methods for steps |
| **Factory Pattern** | Creates objects without specifying concrete class | Returns abstract product |
| **Observer Pattern** | Notifies dependents of state changes | Abstract observer interface |

**Syntax - Strategy Pattern Example:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

// Abstract strategy interface
class ISortStrategy {
public:
    virtual void sort(vector<int>& data) = 0;
    virtual ~ISortStrategy() { }
};

// Concrete strategy 1
class BubbleSort : public ISortStrategy {
public:
    void sort(vector<int>& data) override {
        cout << "Using Bubble Sort" << endl;
        int n = data.size();
        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < n-i-1; j++) {
                if (data[j] > data[j+1]) {
                    swap(data[j], data[j+1]);
                }
            }
        }
    }
};

// Concrete strategy 2
class QuickSort : public ISortStrategy {
private:
    void quickSort(vector<int>& data, int left, int right) {
        if (left >= right) return;
        int pivot = data[right];
        int i = left - 1;
        for (int j = left; j < right; j++) {
            if (data[j] <= pivot) {
                i++;
                swap(data[i], data[j]);
            }
        }
        swap(data[i+1], data[right]);
        quickSort(data, left, i);
        quickSort(data, i+2, right);
    }
    
public:
    void sort(vector<int>& data) override {
        cout << "Using Quick Sort" << endl;
        quickSort(data, 0, data.size() - 1);
    }
};

// Context class using abstraction
class DataProcessor {
private:
    ISortStrategy* strategy_;
    
public:
    DataProcessor(ISortStrategy* strategy) : strategy_(strategy) { }
    
    void setStrategy(ISortStrategy* strategy) {
        strategy_ = strategy;
    }
    
    void process(vector<int>& data) {
        cout << "Processing data..." << endl;
        strategy_->sort(data);
        cout << "Data sorted" << endl;
    }
};

int main() {
    vector<int> data = {64, 34, 25, 12, 22, 11, 90};
    
    BubbleSort bubble;
    QuickSort quick;
    
    DataProcessor processor(&bubble);
    processor.process(data);
    
    data = {64, 34, 25, 12, 22, 11, 90};
    processor.setStrategy(&quick);
    processor.process(data);
    
    return 0;
}
```

---

## 5. Theoretical Foundations

This topic covers the theoretical concepts behind abstraction.

**File:** [Theory.md](Theory.md)

**What you will learn:**
- History of abstraction in programming
- Levels of abstraction (machine, assembly, high-level, OOP)
- Abstraction vs Encapsulation
- Interface segregation principle
- Dependency inversion principle
- Design by contract

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Abstraction** | Hiding implementation details, exposing essential features |
| **Encapsulation** | Bundling data and methods, hiding internal state |
| **Interface Segregation** | Many specific interfaces are better than one general interface |
| **Dependency Inversion** | Depend on abstractions, not concretions |
| **Design by Contract** | Specify preconditions, postconditions, invariants |

**Abstraction vs Encapsulation:**
```cpp
// Both abstraction and encapsulation working together
class BankAccount {
private:
    double balance_;        // Encapsulation - hidden data
    
public:
    void deposit(double amount) {  // Abstraction - simple interface
        if (amount > 0) {
            balance_ += amount;
        }
    }
    
    bool withdraw(double amount) {  // Abstraction - simple interface
        if (amount > 0 && amount <= balance_) {
            balance_ -= amount;
            return true;
        }
        return false;
    }
    
    double getBalance() const { return balance_; }  // Abstraction
};
```

---

### Abstraction Summary

| Feature | Description | Key Syntax |
|---------|-------------|------------|
| **Abstract Class** | Class with pure virtual functions | `virtual void func() = 0;` |
| **Interface** | Class with only pure virtual functions | All functions `= 0` |
| **Concrete Class** | Class with no pure virtual functions | Implements all virtual functions |
| **Pure Virtual Function** | Function without implementation | `= 0` syntax |

---

### Prerequisites

Before starting this section, you should have completed:

- [01. Basics](../../01.%20Basics/README.md) - Functions, classes
- [02_Classes_and_Objects/README.md](../02_Classes_and_Objects/README.md) - Class basics
- [05_Inheritance/README.md](../05_Inheritance/README.md) - Inheritance
- [06_Polymorphism/README.md](../06_Polymorphism/README.md) - Virtual functions

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Trying to instantiate abstract class | Use concrete derived class instead |
| Forgetting to override all pure virtual functions | Override all or derived class remains abstract |
| Using abstract class when interface is sufficient | Use pure abstract class for interfaces |
| Putting implementation in interface | Interfaces should have only pure virtual functions |
| Not using virtual destructor in abstract class | Always add virtual destructor |

---

### Practice Questions

After completing this section, you should be able to:

1. Define abstraction and explain its importance in OOP
2. Differentiate between abstraction and encapsulation
3. Create an abstract class with pure virtual functions
4. Create an interface (pure abstract class) in C++
5. Explain when to use abstract classes vs concrete classes
6. Implement multiple interfaces in a single class
7. Explain how abstraction enables design patterns
8. Apply the Dependency Inversion Principle using abstraction

---

### Next Steps

- Go to [Theory.md](Theory.md) to understand the basics of the content to come.