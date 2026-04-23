# README.md

## Behavioral Design Patterns - Complete Guide

### Overview

Behavioral design patterns deal with communication between objects, how they interact, and how responsibility is distributed. They focus on algorithms and the assignment of responsibilities between objects, making complex communication manageable and promoting loose coupling.

---

### Topics Covered

| # | Pattern | Purpose |
| --- | --- | --- |
| 1. | [Command.md](Command.md) | encapsulate a request as an object, allowing parameterization and queuing |
| 2. | [Observer.md](Observer.md) | define a one-to-many dependency so that when one object changes state, all dependents are notified |
| 3. | [State.md](State.md) | allow an object to alter its behavior when its internal state changes |
| 4. | [Strategy.md](Strategy.md) | define a family of algorithms, encapsulate each one, and make them interchangeable |

---

## 1. Command Pattern

This pattern encapsulates a request as an object, thereby allowing for parameterization of clients with different requests, queuing of requests, and logging of operations. It also supports undoable operations.

**File:** [Command.md](Command.md)

**What you will learn:**
- When to use Command (undo/redo, transaction systems, GUI buttons)
- Command, Receiver, Invoker, and Client roles
- Macro commands (composite commands)
- Undo/redo implementation
- Benefits (decoupling, extensibility)

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Command** | Declares interface for executing operations |
| **Concrete Command** | Implements execute method, binds receiver to action |
| **Receiver** | Knows how to perform the actual operation |
| **Invoker** | Asks command to carry out request |
| **Client** | Creates concrete commands and sets receivers |

**Structure:**
```
    Client ──► Invoker
                │
                │ stores
                ▼
    Client ──► Command
                ▲
                │
        ┌───────┴───────┐
        │               │
    CommandA        CommandB
        │               │
        ▼               ▼
    ReceiverA       ReceiverB
```

---

## 2. Observer Pattern

This pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

**File:** [Observer.md](Observer.md)

**What you will learn:**
- When to use Observer (event handling, publish-subscribe, model-view-controller)
- Subject and Observer roles
- Push vs Pull models
- Loose coupling between subject and observers
- Benefits (reusability, maintainability)

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Subject** | Knows its observers, provides interface for attaching/detaching |
| **Concrete Subject** | Stores state of interest, notifies observers when state changes |
| **Observer** | Defines interface for updating observing objects |
| **Concrete Observer** | Maintains reference to subject, implements update interface |

**Structure:**
```
    Subject ◄─── ConcreteSubject
        │
        │ notifies
        ▼
    Observer ◄─── ConcreteObserver
        ▲
        │
        └── references Subject
```

---

## 3. State Pattern

This pattern allows an object to alter its behavior when its internal state changes. The object will appear to change its class.

**File:** [State.md](State.md)

**What you will learn:**
- When to use State (state machines, workflow systems)
- Context and State roles
- State transitions
- State vs Strategy pattern
- Benefits (localizes state-specific behavior, simplifies context)

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Context** | Defines interface of interest to clients, maintains current state |
| **State** | Defines interface for encapsulating behavior associated with state |
| **Concrete State** | Implements behavior associated with a state of context |

**Structure:**
```
    Context ◄─── State
        │           ▲
        │           │
        └── has-a ──┘
        │
        ▼
    ┌───────────────────────┐
    │  ConcreteStateA  │  ConcreteStateB  │
    └───────────────────────┘
```

---

## 4. Strategy Pattern

This pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. It lets the algorithm vary independently from clients that use it.

**File:** [Strategy.md](Strategy.md)

**What you will learn:**
- When to use Strategy (multiple algorithms for same task)
- Context and Strategy roles
- Strategy vs State pattern
- Benefits (Open/Closed Principle, eliminates conditional statements)

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Context** | Maintains reference to strategy object |
| **Strategy** | Declares interface common to all supported algorithms |
| **Concrete Strategy** | Implements algorithm using Strategy interface |

**Structure:**
```
    Context ◄─── Strategy
        │           ▲
        │           │
        └── has-a ──┘
        │
        ▼
    ┌───────────────────────┐
    │ ConcreteStrategyA │ ConcreteStrategyB │
    └───────────────────────┘
```

---

### Behavioral Patterns Comparison

| Pattern | Problem Solved | Key Mechanism | Complexity |
|---------|----------------|---------------|------------|
| **Command** | Encapsulate request as object | Request object | Medium |
| **Observer** | Notify dependents of state changes | Subscription model | Low |
| **State** | Change behavior with internal state | State objects | Medium |
| **Strategy** | Interchangeable algorithms | Algorithm objects | Low |

---

### State vs Strategy Pattern

| Aspect | State Pattern | Strategy Pattern |
|--------|---------------|------------------|
| **Purpose** | Behavior changes with state | Algorithm selection |
| **State/Strategy Knows** | May know about other states | Usually independent |
| **Context Changes** | State typically changes | Strategy set by client |
| **Relationship** | State is part of context | Strategy is injected |

---

### Command vs Strategy Pattern

| Aspect | Command Pattern | Strategy Pattern |
|--------|-----------------|------------------|
| **Purpose** | Encapsulate request as object | Encapsulate algorithm |
| **Execution** | Typically one-time | Reusable across calls |
| **State** | May store parameters | Usually stateless |
| **Undo/Redo** | Supports | Not typically |

---

### When to Use Which Pattern

| Scenario | Recommended Pattern |
|----------|---------------------|
| Need to parameterize objects with an operation | Command |
| Need to queue, log, or undo operations | Command |
| One object needs to notify multiple others | Observer |
| Decouple subject from observers | Observer |
| Object behavior depends on its state | State |
| Many conditional statements for state transitions | State |
| Multiple algorithms for the same task | Strategy |
| Need to switch algorithms at runtime | Strategy |

---

### Prerequisites

Before starting this section, you should have completed:

- [02_Classes_and_Objects/README.md](../../02_Classes_and_Objects/README.md) - Class basics
- [05_Inheritance/README.md](../../05_Inheritance/README.md) - Inheritance
- [06_Polymorphism/README.md](../../06_Polymorphism/README.md) - Virtual functions

---

### Learning Path

```
Level 1: Communication Patterns
├── Observer
└── Command

Level 2: Behavior Variation Patterns
├── Strategy
└── State

Level 3: Pattern Selection
├── State vs Strategy
├── Command vs Strategy
└── Pattern Combinations
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Observer causing memory leaks | Use weak pointers for observer references |
| Too many observers affecting performance | Batch notifications, use pull model |
| State pattern for simple state machines | Use enum and switch for simple cases |
| Strategy creating many small classes | Balance flexibility and complexity |
| Command for simple operations | Direct method call may suffice |

---

### Practice Questions

After completing this section, you should be able to:

1. Implement a Command pattern for undo/redo functionality
2. Create an Observer pattern for event notification system
3. Use State pattern for a traffic light system
4. Implement Strategy pattern for different sorting algorithms
5. Differentiate between State and Strategy patterns
6. Choose appropriate behavioral pattern for given scenarios

---

### Next Steps

- Go to [Command.md](Command.md) to understand Command Pattern.