# Theory.md

## OOP Projects and Applications - Theoretical Foundations

### Overview

This document covers the theoretical foundations of OOP project design, architecture patterns, and practical guidelines for building real-world applications. It also provides detailed project ideas across various domains and difficulty levels to help you apply OOP concepts in practice.

---

### 1. Project Design Process

The software development process for OOP projects typically follows these phases:

| Phase | Description | Deliverables |
|-------|-------------|--------------|
| **Requirements Analysis** | Understand what the system should do | Requirements document |
| **Domain Modeling** | Identify classes and relationships | Class diagrams |
| **Architecture Design** | Define high-level structure | Architecture diagram |
| **Detailed Design** | Specify class interfaces | Detailed UML diagrams |
| **Implementation** | Write code | Source code |
| **Testing** | Verify correctness | Test reports |
| **Deployment** | Release software | Deployed application |
| **Maintenance** | Fix bugs, add features | Updated versions |

---

### 2. UML Diagrams for OOP Design

Unified Modeling Language (UML) provides standardized diagrams for visualizing OOP designs.

#### Class Diagram

Shows classes, attributes, methods, and relationships.

| Relationship | Symbol | Description | Example |
|--------------|--------|-------------|---------|
| **Inheritance** | `▷——` | Is-a relationship | `Dog ▷—— Animal` |
| **Association** | `——` | Uses relationship | `Student —— Course` |
| **Aggregation** | `◇——` | Has-a (weak) | `Car ◇—— Wheel` |
| **Composition** | `◆——` | Has-a (strong) | `House ◆—— Room` |
| **Dependency** | `- - - >` | Temporary usage | `Class uses another` |

**Class Diagram Example:**
```
┌─────────────────────────────┐
│          Animal             │
│  (abstract)                 │
├─────────────────────────────┤
│ # name: string              │
│ # age: int                  │
├─────────────────────────────┤
│ + makeSound(): void         │
│ + move(): void              │
└─────────────────────────────┘
            △
            │
    ┌───────┴─────────┐
    │                 │
┌───┴─────┐     ┌─────┴───┐
│  Dog    │     │   Cat   │
├─────────┤     ├─────────┤
│ - breed │     │ - color │
├─────────┤     ├─────────┤
│ + bark()│     │ + meow()│
└─────────┘     └─────────┘
```

#### Sequence Diagram

Shows interactions between objects over time.

```
┌────────┐     ┌──────────┐     ┌───────┐     ┌────────┐
│ Client │     │ Controller│     │ Model │     │  View  │
└───┬────┘     └─────┬────┘     └───┬───┘     └───┬────┘
    │                │              │             │
    │──request()────>│              │             │
    │                │──update()───>│             │
    │                │              │──notify()──>│
    │                │              │             │──display()
    │<──response()───│              │             │
```

---

### 3. Architecture Patterns

#### Model-View-Controller (MVC)

Separates application into three interconnected components.

| Component | Responsibility | OOP Concepts |
|-----------|----------------|--------------|
| **Model** | Data, business logic | Encapsulation |
| **View** | User interface | Observer |
| **Controller** | Input handling | Strategy |

```
┌─────────────────────────────────────────────────┐
│                    MVC                          │
│  ┌─────────┐    ┌──────────┐    ┌─────────┐    │
│  │  Model  │◄───│ Controller│───►│  View   │    │
│  └─────────┘    └──────────┘    └─────────┘    │
│       ▲                               │         │
│       └───────────────────────────────┘         │
│              (Observer pattern)                 │
└─────────────────────────────────────────────────┘
```

#### Layered Architecture

Organizes code into layers with dependencies flowing downward.

| Layer | Responsibility | Examples |
|-------|----------------|----------|
| **Presentation** | User interface | GUI, CLI, API |
| **Business Logic** | Domain rules | Services, validators |
| **Data Access** | Database operations | Repositories, DAOs |
| **Infrastructure** | Utilities | Logging, networking |

```
┌─────────────────────┐
│   Presentation      │
│       Layer         │
└─────────┬───────────┘
          │ depends on
          ▼
┌─────────────────────┐
│   Business Logic    │
│       Layer         │
└─────────┬───────────┘
          │ depends on
          ▼
┌─────────────────────┐
│   Data Access       │
│       Layer         │
└─────────┬───────────┘
          │ depends on
          ▼
┌─────────────────────┐
│   Infrastructure    │
│       Layer         │
└─────────────────────┘
```

---

### 4. Project Ideas by Domain

#### Beginner Projects (1-2 weeks)

| Project | Description | OOP Concepts | Features |
|---------|-------------|--------------|----------|
| **Bank Account System** | Manage bank accounts | Classes, Encapsulation | Create accounts, deposit, withdraw, transfer |
| **Student Record System** | Store student data | Classes, Containers | Add, remove, search, display students |
| **Library Management** | Manage books and members | Classes, Inheritance | Borrow, return, search, fine calculation |
| **Shape Calculator** | Calculate area/perimeter | Polymorphism, Abstract classes | Multiple shapes, virtual functions |
| **To-Do List** | Task management | Classes, Composition | Add, complete, delete, save/load tasks |
| **Contact Manager** | Store contacts | Classes, STL containers | Add, edit, delete, search, group contacts |
| **Simple Calculator** | Arithmetic operations | Classes, Operator overloading | Basic math, memory functions |
| **Quiz Game** | Multiple choice questions | Classes, Polymorphism | Questions, scoring, leaderboard |

#### Intermediate Projects (2-4 weeks)

| Project | Description | OOP Concepts | Features |
|---------|-------------|--------------|----------|
| **Inventory System** | Product management | Templates, STL | Stock tracking, reorder alerts, reports |
| **Chat Application** | Real-time messaging | Networking, Multithreading | Multiple clients, private chat, file transfer |
| **Expression Evaluator** | Parse math expressions | Composite pattern, Recursion | Variables, functions, precedence |
| **Chess Game** | Two-player chess | Inheritance, Polymorphism | Piece movement, check/checkmate, castling |
| **File Explorer** | Browse filesystem | Composite pattern | Tree view, file operations, search |
| **Calendar App** | Event management | Observer pattern | Recurring events, reminders, sharing |
| **Drawing App** | Vector graphics | Composite, Command | Shapes, undo/redo, save/load |
| **Music Player** | Audio playback | State pattern | Playlist, shuffle, repeat, equalizer |

#### Advanced Projects (1-2 months)

| Project | Description | OOP Concepts | Features |
|---------|-------------|--------------|----------|
| **HTTP Server** | Web server | Design patterns, Networking | Multiple clients, routing, static files |
| **Database Engine** | Simple relational DB | B-trees, Transactions | SQL parsing, indexing, ACID |
| **Game Engine (2D)** | 2D game framework | Component system | Sprites, collision, input handling |
| **Compiler Frontend** | Language parser | Visitor pattern | Lexing, parsing, AST, type checking |
| **Stock Trading System** | Real-time trading | Observer, Strategy | Market data, order matching, risk management |
| **Distributed Cache** | Key-value store | Consistency protocols | Replication, sharding, failover |
| **Machine Learning Framework** | Neural networks | Templates, Polymorphism | Layers, activation, backpropagation |
| **Virtual Machine** | Bytecode interpreter | Visitor, Strategy | Instruction set, memory management |

---

### 5. Beginner Project: Bank Account System

**Requirements:**
- Create different account types (Savings, Checking)
- Deposit and withdraw money
- Calculate interest for savings accounts
- Transaction history
- Transfer between accounts

**Class Design:**
```
    ┌─────────────────────────────────────────────────┐
    │                   BankAccount                   │
    │                (abstract class)                 │
    ├─────────────────────────────────────────────────┤
    │ # accountNumber: string                         │
    │ # balance: double                               │
    │ # transactions: vector<Transaction>             │
    ├─────────────────────────────────────────────────┤
    │ + deposit(amount: double): void                 │
    │ + withdraw(amount: double): bool                │
    │ + getBalance(): double                          │
    │ + getTransactionHistory(): vector<Transaction>  │
    │ + calculateInterest(): double (pure virtual)    │
    └─────────────────────────────────────────────────┘
                           △
                           │
        ┌──────────────────┴─────────────────────┐
        │                                        │
┌───────┴──────────────┐                 ┌───────┴──────────────┐
│ SavingsAccount       │                 │ CheckingAccount      │
├──────────────────────┤                 ├──────────────────────┤
│ - interestRate       │                 │ - overdraftFee       │
├──────────────────────┤                 ├──────────────────────┤
│ + calculateInterest()│                 │ + calculateInterest()│
│ + addInterest()      │                 │ + applyOverdraftFee()│
└──────────────────────┘                 └──────────────────────┘
```

---

### 6. Intermediate Project: Inventory System

**Requirements:**
- Product categories (Electronics, Clothing, Food)
- Stock tracking with minimum thresholds
- Supplier management
- Purchase orders and sales
- Reports (low stock, sales by category)

**Class Design:**
```
┌─────────────────────────────────────────────────┐
│                    Product                      │
│                (abstract class)                 │
├─────────────────────────────────────────────────┤
│ # id: int                                       │
│ # name: string                                  │
│ # price: double                                 │
│ # quantity: int                                 │
│ # reorderLevel: int                             │
├─────────────────────────────────────────────────┤
│ + sell(quantity: int): bool                     │
│ + restock(quantity: int): void                  │
│ + isLowStock(): bool                            │
│ + getCategory(): string (pure virtual)          │
└─────────────────────────────────────────────────┘
                         △
                         │
        ┌────────────────┼────────────────┐
        │                │                │
┌───────┴───────┐ ┌───────┴───────┐ ┌───────┴───────┐
│  Electronics  │ │   Clothing    │ │     Food      │
├───────────────┤ ├───────────────┤ ├───────────────┤
│ - warranty    │ │ - size        │ │ - expiryDate  │
│ - brand       │ │ - material    │ │ - isPerishable│
└───────────────┘ └───────────────┘ └───────────────┘

┌─────────────────────────────────────────────────┐
│                 InventoryManager                 │
├─────────────────────────────────────────────────┤
│ - products: map<int, Product*>                  │
│ - suppliers: vector<Supplier>                   │
│ - orders: vector<Order>                         │
├─────────────────────────────────────────────────┤
│ + addProduct(): void                            │
│ + removeProduct(): void                         │
│ + generateLowStockReport(): void                │
│ + generateSalesReport(): void                   │
└─────────────────────────────────────────────────┘
```

---

### 7. Advanced Project: HTTP Server

**Requirements:**
- Handle multiple client connections
- Parse HTTP requests (GET, POST)
- Serve static files
- Routing and handlers
- Logging and error handling

**Class Design:**
```
┌─────────────────────────────────────────────────┐
│                   HTTPServer                    │
├─────────────────────────────────────────────────┤
│ - port: int                                     │
│ - socket: int                                   │
│ - running: bool                                 │
│ - router: Router                                │
├─────────────────────────────────────────────────┤
│ + start(): void                                 │
│ + stop(): void                                  │
│ + acceptConnections(): void                     │
└─────────────────────────────────────────────────┘
                         │
                         │ contains
                         ▼
┌─────────────────────────────────────────────────┐
│                    Router                       │
├─────────────────────────────────────────────────┤
│ - routes: map<string, Handler*>                 │
├─────────────────────────────────────────────────┤
│ + addRoute(path: string, handler: Handler*): void│
│ + route(request: Request): Response             │
└─────────────────────────────────────────────────┘
                         │
                         │ contains
                         ▼
┌─────────────────────────────────────────────────┐
│                    Handler                      │
│                (abstract class)                 │
├─────────────────────────────────────────────────┤
│ + handle(request: Request): Response (pure)     │
└─────────────────────────────────────────────────┘
                          △
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
┌───────┴───────┐ ┌───────┴───────┐ ┌───────┴───────┐
│ StaticHandler │ │  RESTHandler  │ │  AuthHandler  │
├───────────────┤ ├───────────────┤ ├───────────────┤
│ - basePath    │ │ - dbConnection│ │ - jwtSecret   │
└───────────────┘ └───────────────┘ └───────────────┘
```

---

### 8. Testing Strategies for OOP Projects

| Test Level | Description | Tools |
|------------|-------------|-------|
| **Unit Testing** | Test individual classes/methods | Google Test, Catch2 |
| **Integration Testing** | Test class interactions | Google Test, custom |
| **System Testing** | Test entire application | Manual, scripts |
| **Regression Testing** | Ensure no new bugs | Automated test suite |

**Test Pyramid:**
```
           +
          / \
         /   \
        /     \
       /       \
      /         \
     /Integration\
    /    Tests    \
   /_______________\
  /                 \
 /    Unit Tests     \
/_____________________\
```

---

### 9. Documentation Guidelines

| Document | Purpose | Audience |
|----------|---------|----------|
| **README.md** | Project overview, setup | All users |
| **API Documentation** | Class and function interfaces | Developers |
| **Design Document** | Architecture and decisions | Maintainers |
| **User Manual** | How to use the application | End users |

**API Documentation Example:**
```cpp
/**
 * @brief Calculates the area of a circle.
 * 
 * This function computes the area using the formula π * r².
 * 
 * @param radius The radius of the circle (must be non-negative).
 * @return double The area of the circle.
 * @throws std::invalid_argument if radius is negative.
 * 
 * @example
 * double area = calculateCircleArea(5.0);
 */
double calculateCircleArea(double radius);
```

---

### 10. Version Control Best Practices

| Practice | Description |
|----------|-------------|
| **Commit often** | Small, focused commits |
| **Meaningful messages** | Explain why, not just what |
| **Feature branches** | Develop features in branches |
| **Pull requests** | Code review before merging |
| **Tags for releases** | Mark versioned releases |

**Git Branch Strategy:**
```
main
  │
  ├── develop
  │     │
  │     ├── feature/auth
  │     ├── feature/api
  │     └── feature/ui
  │
  └── release/v1.0
```

---

### 11. Project Evaluation Criteria

| Criteria | Weight | What to Evaluate |
|----------|--------|------------------|
| **Correctness** | 30% | Features work as expected |
| **Code Quality** | 25% | Readability, naming, comments |
| **OOP Design** | 20% | Proper use of OOP principles |
| **Testing** | 15% | Test coverage, edge cases |
| **Documentation** | 10% | README, API docs, comments |

---

### 12. Portfolio Building Tips

| Tip | Description |
|-----|-------------|
| **Start small** | Complete small projects fully |
| **Document your work** | Write good READMEs |
| **Use version control** | Show Git history |
| **Write tests** | Demonstrate testing skills |
| **Showcase best work** | Quality over quantity |
| **Explain decisions** | Include design rationale |
| **Deploy if possible** | Show working application |

---

### Key Takeaways

1. **Project design** should start with requirements and UML diagrams
2. **Architecture patterns** (MVC, Layered) provide proven structures
3. **Project difficulty** should match your skill level (beginner → intermediate → advanced)
4. **Testing** is essential for reliable software
5. **Documentation** helps users and maintainers
6. **Version control** is mandatory for any project
7. **Portfolio** demonstrates your skills to employers

---

### Next Steps

- Move to [Data Structures](/1.%20C++/04.%20Data%20Structures/README.md) now.