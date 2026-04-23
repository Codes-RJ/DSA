# Theory.md

## OOP Best Practices - Theoretical Foundations

### Overview

Best practices are proven guidelines that help developers write high-quality code. They are not strict rules but recommendations based on decades of collective experience. Following best practices leads to code that is easier to understand, maintain, test, and extend. This document covers the theoretical foundations of OOP best practices, including the SOLID principles, design guidelines, and common anti-patterns.

---

### 1. SOLID Principles

SOLID is an acronym for five design principles that make software designs more understandable, flexible, and maintainable.

| Principle | Full Name | Core Idea |
|-----------|-----------|-----------|
| **S** | Single Responsibility | One class, one responsibility |
| **O** | Open/Closed | Open for extension, closed for modification |
| **L** | Liskov Substitution | Derived classes must be substitutable for base |
| **I** | Interface Segregation | Many specific interfaces > one general interface |
| **D** | Dependency Inversion | Depend on abstractions, not concretions |

---

### S - Single Responsibility Principle

**Definition:** A class should have only one reason to change.

**Violation Example:**
```cpp
class Employee {
public:
    void calculatePay() { }      // Payroll reason
    void saveToDatabase() { }    // Persistence reason
    void generateReport() { }    // Reporting reason
};
// Three reasons to change - violates SRP
```

**Corrected Example:**
```cpp
class Employee {
    // Employee data only
};

class PayrollCalculator {
    void calculatePay(const Employee& e);
};

class EmployeeRepository {
    void saveToDatabase(const Employee& e);
};

class ReportGenerator {
    void generateReport(const Employee& e);
};
```

**Benefits:**
- Easier to understand
- Easier to test
- Reduced coupling
- Changes affect only one class

---

### O - Open/Closed Principle

**Definition:** Software entities should be open for extension but closed for modification.

**Violation Example:**
```cpp
class Shape {
public:
    enum Type { CIRCLE, RECTANGLE };
    Type type;
};

class AreaCalculator {
public:
    double calculate(const Shape& shape) {
        if (shape.type == Shape::CIRCLE) {
            // Calculate circle area
        } else if (shape.type == Shape::RECTANGLE) {
            // Calculate rectangle area
        }
        // Adding new shape requires modifying this function
    }
};
```

**Corrected Example:**
```cpp
class Shape {
public:
    virtual double getArea() const = 0;
    virtual ~Shape() = default;
};

class Circle : public Shape {
    double radius_;
public:
    double getArea() const override { return 3.14 * radius_ * radius_; }
};

class Rectangle : public Shape {
    double width_, height_;
public:
    double getArea() const override { return width_ * height_; }
};

// Adding new shape: create new class, no modification needed
```

**Benefits:**
- New features added without changing existing code
- Reduced risk of introducing bugs
- Easier to extend

---

### L - Liskov Substitution Principle

**Definition:** If S is a subtype of T, then objects of type T may be replaced with objects of type S without altering the correctness of the program.

**Violation Example:**
```cpp
class Bird {
public:
    virtual void fly() { cout << "Flying" << endl; }
};

class Penguin : public Bird {
public:
    void fly() override {
        throw "Penguins can't fly";  // Violates LSP
    }
};

void makeBirdFly(Bird& b) {
    b.fly();  // Works for Bird, fails for Penguin
}
```

**Corrected Example:**
```cpp
class Bird {
public:
    virtual void move() = 0;
};

class FlyingBird : public Bird {
public:
    void move() override { fly(); }
    virtual void fly() = 0;
};

class SwimmingBird : public Bird {
public:
    void move() override { swim(); }
    virtual void swim() = 0;
};

class Sparrow : public FlyingBird {
    void fly() override { cout << "Sparrow flying" << endl; }
};

class Penguin : public SwimmingBird {
    void swim() override { cout << "Penguin swimming" << endl; }
};
```

**Benefits:**
- Predictable behavior
- Correct inheritance hierarchies
- Easier to reason about code

---

### I - Interface Segregation Principle

**Definition:** Clients should not be forced to depend on interfaces they do not use.

**Violation Example:**
```cpp
class IWorker {
public:
    virtual void work() = 0;
    virtual void eat() = 0;
    virtual void sleep() = 0;
};

class Robot : public IWorker {
public:
    void work() override { /* work */ }
    void eat() override { /* robot doesn't eat - forced to implement */ }
    void sleep() override { /* robot doesn't sleep - forced to implement */ }
};
```

**Corrected Example:**
```cpp
class IWorkable {
public:
    virtual void work() = 0;
};

class IEatable {
public:
    virtual void eat() = 0;
};

class ISleepable {
public:
    virtual void sleep() = 0;
};

class Human : public IWorkable, public IEatable, public ISleepable {
public:
    void work() override { /* work */ }
    void eat() override { /* eat */ }
    void sleep() override { /* sleep */ }
};

class Robot : public IWorkable {
public:
    void work() override { /* work */ }
    // No need to implement eat() or sleep()
};
```

**Benefits:**
- Smaller, focused interfaces
- Clients only depend on what they use
- Easier to implement and test

---

### D - Dependency Inversion Principle

**Definition:** High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.

**Violation Example:**
```cpp
class EmailSender {
public:
    void send(const string& message) { /* send email */ }
};

class NotificationService {
    EmailSender sender_;  // Depends on concrete class
public:
    void notify(const string& msg) {
        sender_.send(msg);
    }
};
```

**Corrected Example:**
```cpp
class IMessageSender {
public:
    virtual void send(const string& message) = 0;
    virtual ~IMessageSender() = default;
};

class EmailSender : public IMessageSender {
public:
    void send(const string& message) override { /* send email */ }
};

class SMSSender : public IMessageSender {
public:
    void send(const string& message) override { /* send SMS */ }
};

class NotificationService {
    IMessageSender& sender_;  // Depends on abstraction
public:
    NotificationService(IMessageSender& s) : sender_(s) { }
    
    void notify(const string& msg) {
        sender_.send(msg);
    }
};
```

**Benefits:**
- Loose coupling
- Easier to test (mocking)
- Easier to change implementations

---

### 2. Class Design Guidelines

| Guideline | Description |
|-----------|-------------|
| **Cohesion** | A class should have high cohesion (closely related members) |
| **Coupling** | Minimize coupling between classes |
| **Encapsulation** | Hide internal state, expose only necessary interface |
| **Information Hiding** | Design decisions that may change should be hidden |
| **Minimal Interface** | Expose only what clients need |

**High Cohesion Example:**
```cpp
// Good - high cohesion (all related to bank account)
class BankAccount {
    string accountNumber_;
    double balance_;
public:
    void deposit(double amount);
    void withdraw(double amount);
    double getBalance() const;
};

// Bad - low cohesion (unrelated responsibilities)
class Utility {
    string accountNumber_;
    double temperature_;
    string filename_;
public:
    void deposit(double amount);
    void setTemperature(double temp);
    void readFile();
};
```

---

### 3. Inheritance Guidelines

| Guideline | Description |
|-----------|-------------|
| **Favor Composition** | Prefer composition over inheritance when possible |
| **Is-a Relationship** | Only inherit when a true is-a relationship exists |
| **Shallow Hierarchies** | Keep inheritance hierarchies shallow |
| **Abstract Base Classes** | Use abstract classes for interfaces |
| **Final Classes** | Mark classes final when appropriate |

**Composition vs Inheritance:**
```cpp
// Inheritance (is-a)
class Car : public Vehicle { };

// Composition (has-a)
class Car {
    Engine engine_;      // Car has an engine
    Wheels wheels_;      // Car has wheels
    // Delegates to components
};
```

---

### 4. Polymorphism Guidelines

| Guideline | Description |
|-----------|-------------|
| **Override Keyword** | Always use `override` when overriding virtual functions |
| **Final Keyword** | Use `final` to prevent further overriding |
| **Virtual Destructors** | Base classes must have virtual destructors |
| **Prefer Interfaces** | Program to interfaces, not implementations |

---

### 5. Memory Management Guidelines

| Guideline | Description |
|-----------|-------------|
| **RAII** | Use Resource Acquisition Is Initialization |
| **Smart Pointers** | Prefer `unique_ptr`, `shared_ptr`, `weak_ptr` over raw pointers |
| **Rule of Zero** | Let compiler generate special members when possible |
| **Rule of Five** | Implement all five special members when managing resources |

**Rule of Zero:**
```cpp
// No special members needed - compiler generates them correctly
class Person {
    string name_;    // string manages its own memory
    vector<int> ids_; // vector manages its own memory
public:
    Person(string name, vector<int> ids) : name_(name), ids_(ids) { }
    // No destructor, copy, move needed
};
```

**Rule of Five:**
```cpp
// Managing a resource - implement all five
class ResourceHandle {
    int* data_;
public:
    ResourceHandle() : data_(new int[100]) { }
    ~ResourceHandle() { delete[] data_; }
    ResourceHandle(const ResourceHandle& other);     // copy ctor
    ResourceHandle& operator=(const ResourceHandle& other); // copy assign
    ResourceHandle(ResourceHandle&& other) noexcept; // move ctor
    ResourceHandle& operator=(ResourceHandle&& other) noexcept; // move assign
};
```

---

### 6. Error Handling Guidelines

| Guideline | Description |
|-----------|-------------|
| **Throw by value, catch by const reference** | Avoids slicing, no copy overhead |
| **Use standard exceptions** | Consistent hierarchy |
| **Don't throw from destructors** | Can cause `terminate()` |
| **Be specific in catch** | Catch what you can handle |
| **Noexcept when appropriate** | Enables optimizations |

---

### 7. Naming Conventions

| Element | Convention | Good Example | Bad Example |
|---------|------------|--------------|--------------|
| **Classes** | PascalCase | `FileManager` | `file_manager` |
| **Functions** | PascalCase or camelCase | `ReadFile`, `readFile` | `read_file` |
| **Variables** | snake_case or camelCase | `student_count` | `studentCount` |
| **Constants** | UPPER_SNAKE_CASE | `MAX_SIZE` | `maxSize` |
| **Private Members** | trailing underscore | `size_` | `m_size` |
| **Global** | avoid, or g_ prefix | `g_counter` | `counter` |

---

### 8. Code Organization

| Guideline | Description |
|-----------|-------------|
| **One Class Per File** | Match file name to class name |
| **Header Guards** | `#pragma once` or include guards |
| **Include What You Use** | Avoid transitive includes |
| **Forward Declarations** | Use to reduce dependencies |
| **Separation** | Headers for declarations, source files for definitions |

---

### 9. Documentation Guidelines

| Guideline | Description |
|-----------|-------------|
| **Self-Documenting Code** | Use meaningful names |
| **Comment Why, Not What** | Explain intent |
| **Document Public Interfaces** | Parameters, return, exceptions |
| **Keep Comments Updated** | Outdated comments are harmful |

---

### 10. Common Anti-Patterns

| Anti-Pattern | Description | Solution |
|--------------|-------------|----------|
| **God Object** | One class knows/does everything | Split into smaller classes |
| **Singleton Overuse** | Global state everywhere | Dependency injection |
| **Premature Optimization** | Optimizing without evidence | Write clear code first |
| **Copy-Paste Programming** | Duplicating code | Extract common functionality |
| **Magic Numbers** | Unexplained constants | Named constants |
| **Deep Inheritance** | Overly complex hierarchies | Favor composition |
| **Golden Hammer** | Using same pattern everywhere | Learn multiple patterns |
| **Spaghetti Code** | Unstructured, tangled code | Apply structural patterns |

---

### 11. Code Smells to Watch For

| Code Smell | Description | Possible Refactoring |
|------------|-------------|---------------------|
| **Long Method** | Method does too much | Extract smaller methods |
| **Large Class** | Class has too many responsibilities | Split into multiple classes |
| **Long Parameter List** | Too many parameters | Introduce parameter object |
| **Duplicate Code** | Same code in multiple places | Extract common method |
| **Switch/Cascade Statements** | Many conditionals | Use polymorphism |
| **Temporary Field** | Field used only sometimes | Extract to separate class |

---

### 12. Testing Guidelines

| Guideline | Description |
|-----------|-------------|
| **Test One Thing** | Each test should verify one behavior |
| **Isolated Tests** | Tests should not depend on each other |
| **Fast Tests** | Unit tests should run quickly |
| **Readable Tests** | Tests should be easy to understand |
| **Mock Dependencies** | Use mocks for external dependencies |

---

### Key Takeaways

1. **SOLID principles** are the foundation of good OOP design
2. **Single Responsibility** leads to focused, maintainable classes
3. **Open/Closed** enables extension without modification
4. **Liskov Substitution** ensures correct inheritance hierarchies
5. **Interface Segregation** prevents bloated interfaces
6. **Dependency Inversion** reduces coupling
7. **Favor composition over inheritance** for flexibility
8. **RAII** is essential for resource management
9. **Follow naming conventions** for consistency
10. **Avoid anti-patterns** to prevent common mistakes

---

### Next Steps

- Go to [14_Modern_Cpp_OOP_Features](../14_Modern_Cpp_OOP_Features/README.md) to understand real-life OOP modern concepts.