# README.md

## OOP Projects and Applications - Complete Guide

### Overview

This section provides practical projects and real-world applications that demonstrate the use of Object-Oriented Programming principles in C++. These projects help consolidate theoretical knowledge and develop practical skills. Each project applies multiple OOP concepts including encapsulation, inheritance, polymorphism, and abstraction.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [Theory.md](Theory.md) | understand OOP Project Design and Architecture |

---

## Theory.md

This topic covers project design principles, architecture patterns, and practical applications of OOP.

**File:** [Theory.md](Theory.md)

**What you will learn:**
- Project planning and design
- UML diagrams for OOP design
- Architecture patterns (MVC, layered architecture)
- Project structure and organization
- Testing OOP code
- Debugging techniques
- Performance optimization
- Code review practices

**Key Concepts:**

| Category | Topics |
|----------|--------|
| **Project Design** | Requirements analysis, Class diagrams, Sequence diagrams |
| **Architecture** | MVC, Layered architecture, Dependency injection |
| **Implementation** | Code organization, Header management, Build systems |
| **Testing** | Unit testing, Integration testing, Mock objects |
| **Debugging** | GDB, Valgrind, Sanitizers |
| **Optimization** | Profiling, Bottleneck identification |

---

### Sample Projects

#### Beginner Level Projects

| Project | Concepts Applied | Description |
|---------|-----------------|-------------|
| **Bank Account System** | Classes, Encapsulation, Constructors | Manage accounts, deposits, withdrawals |
| **Student Record System** | Classes, Arrays/Containers | Store and manage student information |
| **Library Management** | Classes, Inheritance, Polymorphism | Manage books, members, borrowing |
| **Employee Management** | Inheritance, Virtual Functions | Different employee types, payroll |
| **Shape Calculator** | Polymorphism, Abstract Classes | Calculate area/perimeter of shapes |

#### Intermediate Level Projects

| Project | Concepts Applied | Description |
|---------|-----------------|-------------|
| **Inventory System** | Templates, STL Containers | Product management, stock tracking |
| **Chat Application** | Networking, Multithreading | Real-time messaging between users |
| **Game Engine (2D)** | Composition, Polymorphism | Sprite, collision, input handling |
| **Database Wrapper** | RAII, Exception Handling | Safe database connection management |
| **Expression Evaluator** | Polymorphism, Composite | Parse and evaluate mathematical expressions |

#### Advanced Level Projects

| Project | Concepts Applied | Description |
|---------|-----------------|-------------|
| **HTTP Server** | Design Patterns, Networking | Multi-threaded web server |
| **Compiler Frontend** | Visitor Pattern, AST | Lexical and syntax analysis |
| **Graphics Engine** | Scene Graph, Memory Management | 3D rendering pipeline |
| **Distributed System** | RPC, Serialization | Multi-node communication |
| **Game Engine (3D)** | Component System, Resource Mgmt | Complete 3D game engine |

---

### Project Structure Template

```
project/
│
├── include/                    # Header files (.h)
│   ├── module1/
│   │   ├── ClassA.h
│   │   └── ClassB.h
│   └── module2/
│       └── ClassC.h
│
├── src/                        # Source files (.cpp)
│   ├── module1/
│   │   ├── ClassA.cpp
│   │   └── ClassB.cpp
│   └── module2/
│       └── ClassC.cpp
│
├── tests/                      # Unit tests
│   ├── test_ClassA.cpp
│   └── test_ClassB.cpp
│
├── docs/                       # Documentation
│   ├── design.md
│   └── api.md
│
├── CMakeLists.txt              # Build configuration
└── README.md                   # Project overview
```

---

### UML Diagrams for OOP Design

#### Class Diagram Example

```
┌─────────────────────────┐
│        Shape            │
├─────────────────────────┤
│ # color: string         │
├─────────────────────────┤
│ + getArea(): double     │
│ + draw(): void          │
└─────────────────────────┘
           ▲
           │
┌──────────┴──────────┐
│                     │
▼                     ▼
┌─────────────┐  ┌─────────────┐
│   Circle    │  │  Rectangle  │
├─────────────┤  ├─────────────┤
│ - radius    │  │ - width     │
│             │  │ - height    │
├─────────────┤  ├─────────────┤
│ + getArea() │  │ + getArea() │
└─────────────┘  └─────────────┘
```

#### Sequence Diagram Example

```
Client          Controller          Model           View
  │                 │                 │              │
  │──request()─────>│                 │              │
  │                 │──process()─────>│              │
  │                 │                 │──update()───>│
  │                 │                 │              │──display()
  │                 │<──return────────│              │
  │<──response()────│                 │              │
```

---

### Build Systems

| Build System | Description | Best For |
|--------------|-------------|----------|
| **Make** | Traditional, simple | Small projects |
| **CMake** | Cross-platform, industry standard | Medium to large projects |
| **Meson** | Modern, fast | Large projects |
| **Bazel** | Google's build system | Very large, multi-language |

**CMake Example:**
```cmake
cmake_minimum_required(VERSION 3.10)
project(MyProject)

set(CMAKE_CXX_STANDARD 17)

# Library
add_library(MyLib src/ClassA.cpp src/ClassB.cpp)
target_include_directories(MyLib PUBLIC include)

# Executable
add_executable(MyApp src/main.cpp)
target_link_libraries(MyApp MyLib)

# Tests
enable_testing()
add_executable(MyTests tests/test_ClassA.cpp)
target_link_libraries(MyTests MyLib)
add_test(NAME MyTests COMMAND MyTests)
```

---

### Testing OOP Code

#### Unit Testing Frameworks

| Framework | Description | Syntax Style |
|-----------|-------------|--------------|
| **Google Test** | Most popular | xUnit |
| **Catch2** | Header-only, expressive | BDD |
| **Doctest** | Lightweight, fast | BDD |
| **Boost.Test** | Mature, feature-rich | xUnit |

**Google Test Example:**
```cpp
#include <gtest/gtest.h>
#include "BankAccount.h"

class BankAccountTest : public ::testing::Test {
protected:
    void SetUp() override {
        account = new BankAccount(1000);
    }
    
    void TearDown() override {
        delete account;
    }
    
    BankAccount* account;
};

TEST_F(BankAccountTest, DepositIncreasesBalance) {
    account->deposit(500);
    EXPECT_EQ(account->getBalance(), 1500);
}

TEST_F(BankAccountTest, WithdrawDecreasesBalance) {
    account->withdraw(300);
    EXPECT_EQ(account->getBalance(), 700);
}
```

#### Mock Objects

```cpp
#include <gmock/gmock.h>

class MockDatabase : public IDatabase {
public:
    MOCK_METHOD(bool, connect, (const string&), (override));
    MOCK_METHOD(bool, query, (const string&), (override));
    MOCK_METHOD(void, disconnect, (), (override));
};

TEST(UserServiceTest, LoginSuccess) {
    MockDatabase mockDb;
    EXPECT_CALL(mockDb, connect("localhost"))
        .Times(1)
        .WillOnce(Return(true));
    EXPECT_CALL(mockDb, query("SELECT * FROM users"))
        .Times(1)
        .WillOnce(Return(true));
    
    UserService service(&mockDb);
    EXPECT_TRUE(service.login("user", "pass"));
}
```

---

### Debugging Tools

| Tool | Purpose | Usage |
|------|---------|-------|
| **GDB** | Debugger | `gdb ./program` |
| **LLDB** | LLVM debugger | `lldb ./program` |
| **Valgrind** | Memory leak detection | `valgrind ./program` |
| **Address Sanitizer** | Memory error detection | `-fsanitize=address` |
| **Undefined Behavior Sanitizer** | UB detection | `-fsanitize=undefined` |

**GDB Commands:**
```bash
break ClassName::methodName   # Set breakpoint
run                           # Start program
next                          # Step over
step                          # Step into
print variable                # Print value
backtrace                     # Show call stack
continue                      # Continue execution
```

---

### Performance Optimization

#### Profiling Tools

| Tool | Purpose | Platform |
|------|---------|----------|
| **perf** | CPU profiling | Linux |
| **Valgrind (Callgrind)** | Call graph analysis | Linux |
| **Intel VTune** | Advanced profiling | Windows/Linux |
| **Instruments** | Profiling | macOS |

#### Optimization Strategies

| Strategy | Description | Impact |
|----------|-------------|--------|
| **Avoid unnecessary copies** | Use references, move semantics | High |
| **Reserve container capacity** | `vector::reserve()` | Medium |
| **Use const references** | For function parameters | Medium |
| **Inline small functions** | In header or `inline` | Low |
| **Profile before optimizing** | Identify real bottlenecks | Critical |

---

### Code Review Checklist

| Category | Items to Check |
|----------|----------------|
| **Design** | SOLID principles, proper abstractions, minimal coupling |
| **Readability** | Meaningful names, consistent formatting, comments |
| **Correctness** | Edge cases, error handling, resource management |
| **Performance** | Unnecessary copies, algorithm complexity |
| **Testing** | Unit tests cover edge cases, test names clear |
| **Memory** | No leaks, proper ownership, RAII |

---

### Project Ideas by Domain

#### Desktop Applications

| Application | Concepts | Difficulty |
|-------------|----------|------------|
| Text Editor | MVC, Observer | Intermediate |
| Image Viewer | Composite, Factory | Intermediate |
| Music Player | State, Command | Intermediate |
| PDF Reader | Visitor, Proxy | Advanced |

#### Business Applications

| Application | Concepts | Difficulty |
|-------------|----------|------------|
| Inventory System | Singleton, Factory | Beginner |
| Payroll System | Strategy, Template | Intermediate |
| CRM System | Observer, Mediator | Advanced |
| ERP System | Abstract Factory, Bridge | Advanced |

#### Games

| Game | Concepts | Difficulty |
|------|----------|------------|
| Snake | Component, State | Beginner |
| Tetris | Composite, Command | Intermediate |
| Platformer | Component, Observer | Intermediate |
| RPG | Factory, Strategy | Advanced |

#### Embedded/Systems

| Application | Concepts | Difficulty |
|-------------|----------|------------|
| Device Driver | Bridge, Adapter | Advanced |
| Protocol Stack | Chain of Responsibility | Advanced |
| File System | Composite, Visitor | Advanced |
| Memory Allocator | Singleton, Pool | Advanced |

---

### Prerequisites

Before starting this section, you should have completed:

- [01. Basics](../../01.%20Basics/README.md) - C++ fundamentals
- [02_Classes_and_Objects/README.md](../02_Classes_and_Objects/README.md) - Class basics
- [03_Constructors_and_Destructors/README.md](../03_Constructors_and_Destructors/README.md) - Object lifecycle
- [05_Inheritance/README.md](../05_Inheritance/README.md) - Inheritance
- [06_Polymorphism/README.md](../06_Polymorphism/README.md) - Polymorphism
- [12_Design_Patterns/README.md](../12_Design_Patterns/README.md) - Design patterns

---

### Learning Path

```
Level 1: Small Projects
├── Bank Account System
├── Student Record System
└── Library Management

Level 2: Medium Projects
├── Inventory System
├── Chat Application
└── Expression Evaluator

Level 3: Large Projects
├── HTTP Server
├── Game Engine
└── Compiler Frontend

Level 4: Professional Development
├── Open Source Contribution
├── Portfolio Building
└── Code Review Participation
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Starting without design | Create UML diagrams first |
| Ignoring error handling | Use exceptions or error codes consistently |
| No version control | Use Git from day one |
| Skipping tests | Write tests alongside code |
| Premature optimization | Profile first, optimize second |
| Poor documentation | Document public interfaces |

---

### Practice Questions

After completing this section, you should be able to:

1. Design a class hierarchy for a given problem
2. Create UML diagrams for a system design
3. Implement a complete OOP project from requirements
4. Write unit tests for OOP code
5. Debug memory issues using Valgrind
6. Optimize performance using profiling tools
7. Conduct a code review for OOP code

---

### Next Steps

- Go to [Theory.md](Theory.md) to understand OOP Project Design and Architecture.
- Then start with a beginner-level project of your choice.
- Gradually move to intermediate and advanced projects.