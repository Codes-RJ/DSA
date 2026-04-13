# README.md

## C++ Basics - Complete Guide

### Overview

This section covers the fundamental concepts of C++ programming. These topics form the foundation for writing any C++ program and are essential before moving to advanced topics like object-oriented programming, data structures, and algorithms.

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [01_Variables_Keywords_and_Operators.md](01_Variables_Keywords_and_Operators.md) | understand Variables Keywords and Operators |
| 2. | [02_Conditional_Statements.md](02_Conditional_Statements.md) | understand Conditional Statements |
| 3. | [03_Loops_and_Iteration.md](03_Loops_and_Iteration.md) | understand Loops and Iteration |
| 4. | [04_Functions_and_Scope.md](04_Functions_and_Scope.md) | understand Functions and Scope |
| 5. | [05_Arrays_and_Strings.md](05_Arrays_and_Strings.md) | understand Arrays and Strings |
| 6. | [06_Pointers_and_Memory_Management.md](06_Pointers_and_Memory_Management.md) | understand Pointers and Memory Management |
| 7. | [07_Error_Handling.md](07_Error%20Handling.md) | understand Error Handling |

---

### 1. Variables, Keywords, and Operators

**What you will learn:**
- What are variables and how to declare them
- Basic data types (int, float, double, char, bool)
- Constants and literals
- C++ keywords (reserved words)
- Arithmetic, relational, logical, and bitwise operators
- Operator precedence and associativity
- Type conversion (implicit and explicit)

**Key Concepts:**
- Variable naming conventions
- Scope of variables
- Integer, floating-point, and character operations
- Short-circuit evaluation in logical operators

---

### 2. Conditional Statements

**What you will learn:**
- if, if-else, and if-else-if ladder
- Nested conditional statements
- Switch-case statements
- Ternary operator (?:)
- When to use which conditional statement

**Key Concepts:**
- Decision making in programs
- Comparing values and expressions
- Fall-through behavior in switch
- Best practices for readability

---

### 3. Loops and Iteration

**What you will learn:**
- for loop (basic and range-based)
- while loop
- do-while loop
- Nested loops
- Break and continue statements
- Infinite loops and how to avoid them

**Key Concepts:**
- Loop initialization, condition, and increment
- Pre-test vs post-test loops
- Loop control statements
- Performance considerations

---

### 4. Functions and Scope

**What you will learn:**
- Function declaration (prototype) and definition
- Function parameters and return types
- Pass by value, pass by reference
- Default arguments
- Function overloading
- Inline functions
- Scope rules (local, global, block scope)

**Key Concepts:**
- Reusability and modularity
- Call stack and function calls
- Lifetime of variables
- Best practices for function design

---

### 5. Arrays and Strings

**What you will learn:**
- One-dimensional and multi-dimensional arrays
- Array initialization and access
- C-style strings (character arrays)
- String functions (strlen, strcpy, strcat, strcmp)
- C++ string class (std::string)
- String operations and manipulation

**Key Concepts:**
- Array indexing (0-based)
- Bounds checking (no automatic bounds check)
- Difference between C-style and C++ strings
- String concatenation, comparison, and searching

---

### 6. Pointers and Memory Management

**What you will learn:**
- What are pointers and addresses
- Pointer declaration and initialization
- Dereferencing pointers
- Pointer arithmetic
- Pointers and arrays
- Pointers to pointers
- Dynamic memory allocation (new and delete)
- Null pointers and dangling pointers

**Key Concepts:**
- Memory addresses and pointer variables
- Relationship between pointers and arrays
- Dynamic vs static memory allocation
- Memory leaks and how to prevent them

---

### 7. Error Handling

**What you will learn:**
- Types of errors (compile-time, runtime, logical)
- Assertions (assert macro)
- Exception handling basics (try, catch, throw)
- Standard exception classes
- Error codes and return values

**Key Concepts:**
- Debugging techniques
- When to use exceptions vs error codes
- Exception safety

---

### Prerequisites

Before starting this section, you should have:

- A C++ compiler installed (g++, clang++, or Visual Studio)
- A text editor or IDE (VS Code, Code::Blocks, CLion, or Dev-C++)
- Basic understanding of how to compile and run a C++ program

---

### Sample Program Structure

```cpp
#include <iostream>
using namespace std;

int main() {
    // Variable declaration
    int number = 10;
    
    // Conditional statement
    if (number > 0) {
        cout << "Positive number" << endl;
    }
    
    // Loop
    for (int i = 0; i < 5; i++) {
        cout << i << " ";
    }
    cout << endl;
    
    // Function call
    int result = add(5, 3);
    
    return 0;
}
```

---

### Learning Path

```
Level 1: Getting Started
├── Variables and Data Types
├── Basic Input/Output (cin, cout)
└── Operators

Level 2: Control Flow
├── Conditional Statements (if, switch)
└── Loops (for, while, do-while)

Level 3: Modular Programming
├── Functions
├── Scope and Lifetime
└── Function Overloading

Level 4: Data Structures Basics
├── Arrays
├── Strings
└── Multi-dimensional Arrays

Level 5: Memory Management
├── Pointers
├── Dynamic Allocation
└── Pointer Arithmetic

Level 6: Error Handling
├── Types of Errors
├── Assertions
└── Exception Basics
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Using uninitialized variables | Always initialize variables |
| Array index out of bounds | Check bounds before access |
| Forgetting semicolon (;) | Remember statements end with ; |
| Using = instead of == in conditions | = is assignment, == is comparison |
| Infinite loops | Ensure loop condition eventually becomes false |
| Memory leaks | Always delete dynamically allocated memory |
| Dangling pointers | Set pointer to nullptr after delete |

---

### Practice Problems

After completing this section, you should be able to:

1. Write a program to swap two numbers
2. Find whether a number is prime or not
3. Print Fibonacci series up to n terms
4. Find factorial of a number using function
5. Reverse a string
6. Find the largest element in an array
7. Calculate sum of array elements using pointers
8. Handle division by zero using exception handling

---

### Next Steps

- Go to [01_Variables_Keywords_and_Operators.md](01_Variables_Keywords_and_Operators.md) to understand C++ Variables and Keywords.