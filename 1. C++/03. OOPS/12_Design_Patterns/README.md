# README.md

## Design Patterns in C++ - Complete Guide

### Overview

Design patterns are reusable solutions to common problems that occur in software design. They represent best practices evolved over time by experienced developers. Design patterns are not finished code but templates that can be applied to solve specific problems in different contexts. Understanding design patterns helps developers write more maintainable, flexible, and reusable code.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [01_Creational_Patterns/README.md](01_Creational_Patterns/README.md) | understand Creational Design Patterns |
| 2. | [02_Structural_Patterns/README.md](02_Structural_Patterns/README.md) | understand Structural Design Patterns |
| 3. | [03_Behavioral_Patterns/README.md](03_Behavioral_Patterns/README.md) | understand Behavioral Design Patterns |
| 4. | [Theory.md](Theory.md) | understand Theoretical Foundations of Design Patterns |

---

## 1. Creational Design Patterns

This topic explains patterns that deal with object creation mechanisms.

**File:** [01_Creational_Patterns/README.md](01_Creational_Patterns/README.md)

**What you will learn:**
- What are creational patterns
- Singleton pattern (single instance)
- Factory Method pattern (delegating instantiation)
- Abstract Factory pattern (families of products)
- Builder pattern (step-by-step construction)
- Prototype pattern (cloning objects)

**Key Concepts:**

| Pattern | Purpose | When to Use |
|---------|---------|-------------|
| **Singleton** | Ensure only one instance exists | Global configuration, logging |
| **Factory Method** | Define interface for creating objects | Subclasses decide which class to instantiate |
| **Abstract Factory** | Create families of related objects | Cross-platform UI components |
| **Builder** | Construct complex objects step by step | Objects with many optional parameters |
| **Prototype** | Create objects by cloning | Expensive creation, many similar objects |

**Patterns Covered:**

| # | Pattern | File |
| --- | --- | --- |
| 1. | Singleton | `01_Creational_Patterns/1_Singleton.md` |
| 2. | Factory Method | `01_Creational_Patterns/2_Factory_Method.md` |
| 3. | Abstract Factory | `01_Creational_Patterns/3_Abstract_Factory.md` |
| 4. | Builder | `01_Creational_Patterns/4_Builder.md` |
| 5. | Prototype | `01_Creational_Patterns/5_Prototype.md` |

---

## 2. Structural Design Patterns

This topic explains patterns that deal with class and object composition.

**File:** [02_Structural_Patterns/README.md](02_Structural_Patterns/README.md)

**What you will learn:**
- What are structural patterns
- Adapter pattern (interface conversion)
- Bridge pattern (abstraction from implementation)
- Composite pattern (tree structures)
- Decorator pattern (adding behavior dynamically)
- Facade pattern (simplifying complex subsystems)
- Flyweight pattern (sharing fine-grained objects)
- Proxy pattern (controlling access)

**Key Concepts:**

| Pattern | Purpose | When to Use |
|---------|---------|-------------|
| **Adapter** | Convert interface to expected interface | Integrating legacy code |
| **Bridge** | Separate abstraction from implementation | Multiple platform support |
| **Composite** | Compose objects into tree structures | Hierarchical data (filesystem) |
| **Decorator** | Add responsibilities dynamically | Adding features without subclassing |
| **Facade** | Provide simplified interface | Complex library or framework |
| **Flyweight** | Share objects to save memory | Many similar objects |
| **Proxy** | Control access to another object | Lazy loading, access control |

**Patterns Covered:**

| # | Pattern | File |
| --- | --- | --- |
| 1. | Adapter | `02_Structural_Patterns/Adapter.md` |
| 2. | Bridge | `02_Structural_Patterns/Bridge.md` |
| 3. | Composite | `02_Structural_Patterns/Composite.md` |
| 4. | Decorator | `02_Structural_Patterns/Decorator.md` |
| 5. | Facade | `02_Structural_Patterns/Facade.md` |
| 6. | Flyweight | `02_Structural_Patterns/Flyweight.md` |
| 7. | Proxy | `02_Structural_Patterns/Proxy.md` |

---

## 3. Behavioral Design Patterns

This topic explains patterns that deal with communication between objects.

**File:** [03_Behavioral_Patterns/README.md](03_Behavioral_Patterns/README.md)

**What you will learn:**
- What are behavioral patterns
- Chain of Responsibility pattern (request handling chain)
- Command pattern (request as object)
- Interpreter pattern (language grammar)
- Iterator pattern (sequential access)
- Mediator pattern (decoupled communication)
- Memento pattern (state capture)
- Observer pattern (notification mechanism)
- State pattern (behavior based on state)
- Strategy pattern (interchangeable algorithms)
- Template Method pattern (algorithm skeleton)
- Visitor pattern (operations on elements)

**Key Concepts:**

| Pattern | Purpose | When to Use |
|---------|---------|-------------|
| **Chain of Responsibility** | Pass request along chain | Multiple handlers, unknown receiver |
| **Command** | Encapsulate request as object | Undo/redo, queuing, logging |
| **Interpreter** | Define grammar and interpret | Simple languages, expression evaluation |
| **Iterator** | Access elements sequentially | Traversing collections |
| **Mediator** | Decouple communicating objects | Complex communications |
| **Memento** | Capture and restore state | Undo functionality |
| **Observer** | Notify dependents of changes | Event handling, publish-subscribe |
| **State** | Alter behavior when state changes | State machines |
| **Strategy** | Define interchangeable algorithms | Runtime algorithm selection |
| **Template Method** | Define algorithm skeleton | Common steps with variations |
| **Visitor** | Add operations to class hierarchy | Operations on many classes |

**Patterns Covered:**

| # | Pattern | File |
| --- | --- | --- |
| 1. | Command | `03_Behavioral_Patterns/Command.md` |
| 2. | Observer | `03_Behavioral_Patterns/Observer.md` |
| 3. | State | `03_Behavioral_Patterns/State.md` |
| 4. | Strategy | `03_Behavioral_Patterns/Strategy.md` |

---

## 4. Theoretical Foundations

This topic covers the theoretical concepts behind design patterns.

**File:** [Theory.md](Theory.md)

**What you will learn:**
- History of design patterns (Gang of Four)
- Pattern classification (creational, structural, behavioral)
- Benefits and drawbacks of using patterns
- Pattern language and relationships
- Anti-patterns (common mistakes)
- Pattern selection guidelines

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Gang of Four (GoF)** | Authors of "Design Patterns: Elements of Reusable Object-Oriented Software" |
| **Pattern Language** | Collection of patterns that work together |
| **Anti-Pattern** | Common but ineffective solution |
| **Pattern Classification** | Categorization by purpose and scope |
| **Pattern Relationships** | How patterns complement or conflict |

---

### Design Patterns Classification

```
Design Patterns
│
├── Creational Patterns
│   ├── Singleton
│   ├── Factory Method
│   ├── Abstract Factory
│   ├── Builder
│   └── Prototype
│
├── Structural Patterns
│   ├── Adapter
│   ├── Bridge
│   ├── Composite
│   ├── Decorator
│   ├── Facade
│   ├── Flyweight
│   └── Proxy
│
└── Behavioral Patterns
    ├── Chain of Responsibility
    ├── Command
    ├── Interpreter
    ├── Iterator
    ├── Mediator
    ├── Memento
    ├── Observer
    ├── State
    ├── Strategy
    ├── Template Method
    └── Visitor
```

---

### Prerequisites

Before starting this section, you should have completed:

- [01. Basics](../../01.%20Basics/README.md) - Functions, classes
- [02_Classes_and_Objects/README.md](../02_Classes_and_Objects/README.md) - Class basics
- [05_Inheritance/README.md](../05_Inheritance/README.md) - Inheritance
- [06_Polymorphism/README.md](../06_Polymorphism/README.md) - Virtual functions
- [09_Templates_and_Generic_Programming/README.md](../09_Templates_and_Generic_Programming/README.md) - Templates

---

### Sample Pattern Implementation (Singleton)

```cpp
#include <iostream>
#include <memory>
#include <mutex>
using namespace std;

class Singleton {
private:
    static unique_ptr<Singleton> instance_;
    static mutex mtx_;
    int data_;
    
    // Private constructor
    Singleton() : data_(0) {
        cout << "Singleton created" << endl;
    }
    
public:
    // Delete copy and move
    Singleton(const Singleton&) = delete;
    Singleton& operator=(const Singleton&) = delete;
    
    static Singleton* getInstance() {
        lock_guard<mutex> lock(mtx_);
        if (!instance_) {
            instance_ = unique_ptr<Singleton>(new Singleton());
        }
        return instance_.get();
    }
    
    void setData(int data) { data_ = data; }
    int getData() const { return data_; }
};

unique_ptr<Singleton> Singleton::instance_ = nullptr;
mutex Singleton::mtx_;

int main() {
    Singleton* s1 = Singleton::getInstance();
    Singleton* s2 = Singleton::getInstance();
    
    s1->setData(42);
    
    cout << "s1 data: " << s1->getData() << endl;
    cout << "s2 data: " << s2->getData() << endl;
    cout << "Same instance: " << (s1 == s2) << endl;
    
    return 0;
}
```

---

### Learning Path

```
Level 1: Introduction
├── What are Design Patterns?
├── Why Use Design Patterns?
└── Pattern Classification

Level 2: Creational Patterns
├── Singleton
├── Factory Method
├── Abstract Factory
├── Builder
└── Prototype

Level 3: Structural Patterns
├── Adapter
├── Bridge
├── Composite
├── Decorator
├── Facade
├── Flyweight
└── Proxy

Level 4: Behavioral Patterns
├── Command
├── Observer
├── State
├── Strategy
└── Others

Level 5: Advanced Topics
├── Pattern Relationships
├── Anti-Patterns
└── Pattern Selection
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Overusing patterns | Use only when needed |
| Applying pattern blindly | Understand the problem first |
| Ignoring language features | C++ has unique capabilities |
| Singleton overuse | Consider alternatives (dependency injection) |
| Premature pattern application | Refactor into patterns when needed |

---

### Practice Questions

After completing this section, you should be able to:

1. Explain what design patterns are and why they are useful
2. List the three categories of design patterns
3. Implement a thread-safe Singleton pattern
4. Explain when to use Factory Method vs Abstract Factory
5. Implement a Decorator pattern for adding features
6. Explain the Observer pattern for event handling
7. Choose appropriate patterns for given scenarios
8. Recognize anti-patterns in existing code

---

### Next Steps

- Go to [Theory.md](Theory.md) to understand basics of the module.