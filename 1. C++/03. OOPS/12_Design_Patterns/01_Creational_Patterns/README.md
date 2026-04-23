# README.md

## Creational Design Patterns - Complete Guide

### Overview

Creational design patterns deal with object creation mechanisms. They abstract the instantiation process, making a system independent of how its objects are created, composed, and represented. These patterns give flexibility in deciding which objects need to be created for a given case, and how they are created.

---

### Topics Covered

| # | Pattern | Purpose |
| --- | --- | --- |
| 1. | [1_Singleton.md](1_Singleton.md) | ensure only one instance of a class exists |
| 2. | [2_Factory_Method.md](2_Factory_Method.md) | define interface for creating objects, subclasses decide which class to instantiate |
| 3. | [3_Abstract_Factory.md](3_Abstract_Factory.md) | create families of related or dependent objects |
| 4. | [4_Builder.md](4_Builder.md) | construct complex objects step by step |
| 5. | [5_Prototype.md](5_Prototype.md) | create new objects by cloning existing ones |

---

## 1. Singleton Pattern

This pattern ensures a class has only one instance and provides a global point of access to it.

**File:** [1_Singleton.md](1_Singleton.md)

**What you will learn:**
- When to use Singleton (logging, configuration, connection pools)
- Thread-safe Singleton implementation
- Meyers Singleton (C++11 and later)
- Double-checked locking
- Problems with Singleton (testing, hiding dependencies)

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Private Constructor** | Prevents external instantiation |
| **Static Instance** | Holds the single instance |
| **Static Access Method** | Global access point |
| **Thread Safety** | Must handle concurrent access |
| **Lazy Initialization** | Create only when needed |

**Basic Implementation:**
```cpp
class Singleton {
private:
    static Singleton* instance_;
    Singleton() { }  // Private constructor
    
public:
    static Singleton* getInstance() {
        if (instance_ == nullptr) {
            instance_ = new Singleton();
        }
        return instance_;
    }
    
    Singleton(const Singleton&) = delete;
    Singleton& operator=(const Singleton&) = delete;
};
```

---

## 2. Factory Method Pattern

This pattern defines an interface for creating an object but lets subclasses decide which class to instantiate.

**File:** [2_Factory_Method.md](2_Factory_Method.md)

**What you will learn:**
- When to use Factory Method
- Creator and Product hierarchies
- Parameterized factory methods
- Factory Method vs Simple Factory
- Benefits (loose coupling, Open/Closed Principle)

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Product** | The interface of objects created |
| **Concrete Product** | Specific implementation |
| **Creator** | Declares factory method |
| **Concrete Creator** | Implements factory method |

**Structure:**
```
        Creator                    Product
      (abstract)                  (interface)
           │                           │
           │ factoryMethod()           │
           ▼                           ▼
    ConcreteCreator            ConcreteProduct
           │                           │
           └────────── creates ────────┘
```

---

## 3. Abstract Factory Pattern

This pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes.

**File:** [3_Abstract_Factory.md](3_Abstract_Factory.md)

**What you will learn:**
- When to use Abstract Factory (cross-platform UI, theme switching)
- Factory interfaces and implementations
- Product families
- Abstract Factory vs Factory Method
- Benefits (consistency, flexibility)

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Abstract Factory** | Interface for creating product families |
| **Concrete Factory** | Implements creation for a specific family |
| **Abstract Product** | Interface for a product type |
| **Concrete Product** | Implementation for a specific family |

**Structure:**
```
    AbstractFactory                    AbstractProductA
           │                                  │
           ▼                                  ▼
    ConcreteFactory1                 ConcreteProductA1
           │                                  │
           └────────── creates ───────────────┘

    AbstractFactory                    AbstractProductB
           │                                  │
           ▼                                  ▼
    ConcreteFactory2                 ConcreteProductB2
           │                                  │
           └────────── creates ───────────────┘
```

---

## 4. Builder Pattern

This pattern separates the construction of a complex object from its representation, allowing the same construction process to create different representations.

**File:** [4_Builder.md](4_Builder.md)

**What you will learn:**
- When to use Builder (complex objects, many optional parameters)
- Director and Builder roles
- Fluent interfaces (method chaining)
- Builder vs Factory
- Benefits (step-by-step construction, reuse)

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Director** | Controls construction process |
| **Builder** | Abstract interface for building parts |
| **Concrete Builder** | Implements specific construction |
| **Product** | The complex object being built |

**Structure:**
```
    Director ──► Builder
                    │
            ┌───────┼───────┐
            ▼       ▼       ▼
      BuilderA  BuilderB  BuilderC
            │       │       │
            ▼       ▼       ▼
         ProductA ProductB ProductC
```

---

## 5. Prototype Pattern

This pattern creates new objects by cloning existing ones, avoiding the cost of creating objects from scratch.

**File:** [5_Prototype.md](5_Prototype.md)

**What you will learn:**
- When to use Prototype (expensive creation, many similar objects)
- Shallow vs deep copy
- Clone method implementation
- Prototype registry
- Benefits (performance, dynamic configuration)

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Prototype** | Interface declaring clone method |
| **Concrete Prototype** | Implements cloning for itself |
| **Clone Method** | Creates copy of the object |
| **Prototype Registry** | Stores and retrieves prototypes |

**Structure:**
```
    Client ──► Prototype
                 │
                 │ clone()
                 ▼
            ┌────────────┐
            │ Concrete   │
            │ Prototype  │
            └────────────┘
                 │
                 │ clone()
                 ▼
            ┌────────────┐
            │   Copy     │
            │ of object  │
            └────────────┘
```

---

### Creational Patterns Comparison

| Pattern | Problem Solved | Key Feature | Complexity |
|---------|----------------|-------------|------------|
| **Singleton** | Single instance | One instance global access | Low |
| **Factory Method** | Which subclass to create | Inheritance-based creation | Low |
| **Abstract Factory** | Families of objects | Composition-based creation | Medium |
| **Builder** | Complex object construction | Step-by-step building | Medium |
| **Prototype** | Costly creation | Cloning existing objects | Low |

---

### When to Use Which Pattern

| Scenario | Recommended Pattern |
|----------|---------------------|
| Need exactly one instance | Singleton |
| Class can't predict which subclass to create | Factory Method |
| Need families of related objects | Abstract Factory |
| Object has many optional parameters | Builder |
| Creating objects is expensive | Prototype |
| Want to avoid subclassing for creation | Prototype |

---

### Prerequisites

Before starting this section, you should have completed:

- [02_Classes_and_Objects/README.md](../../02_Classes_and_Objects/README.md) - Class basics
- [05_Inheritance/README.md](../../05_Inheritance/README.md) - Inheritance
- [06_Polymorphism/README.md](../../06_Polymorphism/README.md) - Virtual functions

---

### Learning Path

```
Level 1: Basic Creational Patterns
├── Singleton
└── Factory Method

Level 2: Advanced Creational Patterns
├── Abstract Factory
├── Builder
└── Prototype

Level 3: Pattern Selection
├── Comparing Patterns
├── Pattern Combinations
└── Anti-Patterns to Avoid
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Singleton overuse | Consider dependency injection |
| Factory Method for simple creation | Simple constructor may suffice |
| Abstract Factory when not needed | Adds unnecessary complexity |
| Builder for simple objects | Constructor or factory is simpler |
| Prototype with shallow copy | Implement deep copy for complex objects |

---

### Practice Questions

After completing this section, you should be able to:

1. Implement a thread-safe Singleton pattern
2. Explain when to use Factory Method vs Abstract Factory
3. Create a Builder for a complex object with many parameters
4. Implement Prototype with deep copy
5. Choose appropriate creational pattern for given scenarios
6. Identify Singleton anti-patterns in existing code

---

### Next Steps

- Go to [1_Singleton.md](1_Singleton.md) to understand Singleton Pattern.