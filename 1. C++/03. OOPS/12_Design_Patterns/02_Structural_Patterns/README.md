# README.md

## Structural Design Patterns - Complete Guide

### Overview

Structural design patterns deal with class and object composition. They help ensure that when one part of a system changes, the entire system doesn't need to change. These patterns simplify the structure by identifying relationships and promoting code reusability and flexibility.

---

### Topics Covered

| # | Pattern | Purpose |
| --- | --- | --- |
| 1. | [Adapter.md](Adapter.md) | convert interface of a class into another interface clients expect |
| 2. | [Bridge.md](Bridge.md) | separate abstraction from implementation so both can vary independently |
| 3. | [Composite.md](Composite.md) | compose objects into tree structures to represent part-whole hierarchies |
| 4. | [Decorator.md](Decorator.md) | add responsibilities to objects dynamically |
| 5. | [Facade.md](Facade.md) | provide a unified interface to a set of interfaces in a subsystem |
| 6. | [Flyweight.md](Flyweight.md) | share objects to support large numbers of fine-grained objects efficiently |
| 7. | [Proxy.md](Proxy.md) | provide a surrogate or placeholder for another object to control access |

---

## 1. Adapter Pattern

This pattern converts the interface of a class into another interface that clients expect. It allows classes to work together that couldn't otherwise because of incompatible interfaces.

**File:** [Adapter.md](Adapter.md)

**What you will learn:**
- When to use Adapter (legacy code integration, third-party libraries)
- Class Adapter (using inheritance)
- Object Adapter (using composition)
- Two-way adapters
- Benefits (reusability, transparency)

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Target** | Interface that client expects |
| **Adaptee** | Existing interface that needs adapting |
| **Adapter** | Converts Adaptee to Target |
| **Client** | Uses Target interface |

**Structure (Object Adapter):**
```
    Client ──► Target
                 ▲
                 │
             Adapter
                 │
                 ▼
             Adaptee
```

---

## 2. Bridge Pattern

This pattern decouples an abstraction from its implementation so that the two can vary independently.

**File:** [Bridge.md](Bridge.md)

**What you will learn:**
- When to use Bridge (avoiding permanent binding, multiple dimensions)
- Abstraction and Implementor hierarchies
- Bridge vs Inheritance
- Benefits (extensibility, hiding implementation details)

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Abstraction** | Defines the abstract interface |
| **Refined Abstraction** | Extends the abstraction |
| **Implementor** | Defines the implementation interface |
| **Concrete Implementor** | Implements the Implementor |

**Structure:**
```
    Abstraction ◄─── RefinedAbstraction
         │
         │ has-a
         ▼
    Implementor ◄─── ConcreteImplementor
```

---

## 3. Composite Pattern

This pattern composes objects into tree structures to represent part-whole hierarchies. It lets clients treat individual objects and compositions uniformly.

**File:** [Composite.md](Composite.md)

**What you will learn:**
- When to use Composite (file systems, UI components)
- Leaf and Composite classes
- Uniform interface for primitive and composite objects
- Benefits (simplicity, flexibility)

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Component** | Declares interface for objects in composition |
| **Leaf** | Represents leaf objects (no children) |
| **Composite** | Defines behavior for components having children |
| **Client** | Manipulates objects through Component interface |

**Structure:**
```
    Client ──► Component
                ▲
                │
        ┌───────┴───────┐
        │               │
      Leaf          Composite ◄──► children
```

---

## 4. Decorator Pattern

This pattern attaches additional responsibilities to an object dynamically. It provides a flexible alternative to subclassing for extending functionality.

**File:** [Decorator.md](Decorator.md)

**What you will learn:**
- When to use Decorator (adding features dynamically)
- Decorator vs Inheritance
- Transparent nesting of decorators
- Benefits (flexibility, Open/Closed Principle)

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Component** | Defines interface for objects that can have responsibilities added |
| **Concrete Component** | Defines object to which additional responsibilities can be attached |
| **Decorator** | Maintains reference to Component and conforms to its interface |
| **Concrete Decorator** | Adds responsibilities to the component |

**Structure:**
```
    Component ◄─── ConcreteComponent
         ▲
         │
    Decorator ◄─── ConcreteDecorator
         │
         │ has-a
         ▼
    Component
```

---

## 5. Facade Pattern

This pattern provides a unified interface to a set of interfaces in a subsystem. It defines a higher-level interface that makes the subsystem easier to use.

**File:** [Facade.md](Facade.md)

**What you will learn:**
- When to use Facade (complex subsystems, libraries)
- Facade vs other patterns
- Benefits (simplicity, decoupling, layering)

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Facade** | Provides simplified interface to subsystem |
| **Subsystem Classes** | Implement subsystem functionality |
| **Client** | Uses Facade instead of subsystem directly |

**Structure:**
```
    Client ──► Facade
                │
                │ delegates to
                ▼
    ┌───────────────────────┐
    │    Subsystem Classes   │
    └───────────────────────┘
```

---

## 6. Flyweight Pattern

This pattern uses sharing to support large numbers of fine-grained objects efficiently.

**File:** [Flyweight.md](Flyweight.md)

**What you will learn:**
- When to use Flyweight (many similar objects, memory constraints)
- Intrinsic vs Extrinsic state
- Flyweight factory for object reuse
- Benefits (memory savings, performance)

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Flyweight** | Declares interface for flyweight objects |
| **Concrete Flyweight** | Stores intrinsic state and implements interface |
| **Unshared Concrete Flyweight** | Not shared, has extrinsic state |
| **Flyweight Factory** | Creates and manages flyweight objects |

**Structure:**
```
    Client ──► FlyweightFactory
                    │
                    │ creates/manages
                    ▼
    Client ◄─── Flyweight (shared)
                    ▲
                    │
              ConcreteFlyweight
```

---

## 7. Proxy Pattern

This pattern provides a surrogate or placeholder for another object to control access to it.

**File:** [Proxy.md](Proxy.md)

**What you will learn:**
- When to use Proxy (lazy loading, access control, logging)
- Types of Proxy (virtual, protection, remote, logging)
- Proxy vs Decorator
- Benefits (control, optimization)

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Subject** | Defines common interface for RealSubject and Proxy |
| **RealSubject** | The real object that proxy represents |
| **Proxy** | Maintains reference to RealSubject and controls access |

**Structure:**
```
    Client ──► Subject
                ▲
                │
        ┌───────┴───────┐
        │               │
      Proxy         RealSubject
        │               │
        └──► controls ──┘
```

---

### Structural Patterns Comparison

| Pattern | Problem Solved | Key Mechanism | Complexity |
|---------|----------------|---------------|------------|
| **Adapter** | Incompatible interfaces | Wrapping | Low |
| **Bridge** | Multiple dimensions of variation | Decoupling abstraction | Medium |
| **Composite** | Part-whole hierarchies | Tree structure | Medium |
| **Decorator** | Adding responsibilities dynamically | Wrapping (nesting) | Medium |
| **Facade** | Complex subsystem interface | Simplification | Low |
| **Flyweight** | Memory efficiency | Sharing | Medium |
| **Proxy** | Access control | Indirection | Low |

---

### When to Use Which Pattern

| Scenario | Recommended Pattern |
|----------|---------------------|
| Need to use existing class with different interface | Adapter |
| Abstraction and implementation may vary independently | Bridge |
| Need to represent part-whole hierarchies | Composite |
| Need to add responsibilities dynamically | Decorator |
| Want to simplify complex subsystem | Facade |
| Many similar objects causing memory issues | Flyweight |
| Need to control access to an object | Proxy |

---

### Prerequisites

Before starting this section, you should have completed:

- [02_Classes_and_Objects/README.md](../../02_Classes_and_Objects/README.md) - Class basics
- [05_Inheritance/README.md](../../05_Inheritance/README.md) - Inheritance
- [06_Polymorphism/README.md](../../06_Polymorphism/README.md) - Virtual functions

---

### Learning Path

```
Level 1: Wrapper Patterns
├── Adapter
├── Decorator
└── Proxy

Level 2: Structure Simplification
├── Facade
└── Composite

Level 3: Decoupling and Optimization
├── Bridge
└── Flyweight

Level 4: Pattern Selection
├── Comparing Patterns
└── Pattern Combinations
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Using Adapter when you can change the interface | Change the source if possible |
| Decorator creating too many small objects | Balance flexibility and complexity |
| Composite for simple, non-hierarchical data | Overkill for flat structures |
| Facade hiding too much functionality | Keep essential access available |
| Flyweight for unique objects | Only beneficial for many similar objects |
| Proxy when direct access is fine | Don't add unnecessary indirection |

---

### Practice Questions

After completing this section, you should be able to:

1. Implement an Adapter to make legacy code work with new interface
2. Use Bridge to separate UI abstraction from platform implementation
3. Create a Composite structure for a file system
4. Add features dynamically using Decorator
5. Simplify a complex subsystem with Facade
6. Optimize memory using Flyweight for repeated objects
7. Implement a Virtual Proxy for lazy loading

---

### Next Steps

- Go to [Adapter.md](Adapter.md) to understand Adapter Pattern.