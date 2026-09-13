# C++ Programming Language

> 🗺️ **Master Curriculum Architecture**: Access the **[Master DSA Curriculum Map](MASTER_DSA_MAP.md)** for the syllabus breakdown, prerequisite graph, complexity cheat sheet, and pattern-matching matrix across the major modules.

> 🎓 **Student Path**: Follow the canonical [C++ and DSA Learning Path](LEARNING_PATH.md) for the precise study order, prerequisites, and exit criteria. Use the directory numbering for navigation, not as the learning sequence.

## Overview

C++ is a high-level, general-purpose programming language created as an extension of the C programming language. It was developed by Bjarne Stroustrup at Bell Labs starting in 1979 and officially released in 1985. C++ combines the low-level capabilities of C with object-oriented programming features, making it a powerful and versatile language for system programming, game development, competitive programming, and large-scale applications.

## History

- **1979**: Bjarne Stroustrup begins work on "C with Classes" at Bell Labs
- **1983**: Renamed to C++ (the ++ operator signifies increment/enhancement)
- **1985**: First commercial release of C++
- **1998**: ISO/IEC 14882:1998 (C++98) - First standardized version
- **2003**: Minor revision (C++03)
- **2011**: Major revision (C++11) - Added lambda functions, auto keyword, smart pointers
- **2014**: C++14 - Further improvements and features
- **2017**: C++17 - File system library, parallel algorithms
- **2020**: C++20 - Concepts, ranges, coroutines, modules
- **2023**: C++23 - Current published language standard; availability varies by compiler and standard-library implementation

## Key Features and Perks

### Performance Advantages
- **Compiled Language**: Direct compilation to machine code for maximum performance
- **Resource Management**: RAII (Resource Acquisition Is Initialization) ties resources to object lifetimes and reduces manual cleanup
- **Zero-Overhead Principle**: Well-designed abstractions aim not to impose costs beyond an equivalent lower-level implementation, although this is not an unconditional guarantee
- **Low-Level Extensions**: Many compilers support non-standard facilities such as inline assembly for target-specific work

### Rich Standard Library
- **STL (Standard Template Library)**: Comprehensive data structures and algorithms
- **Containers**: vector, list, deque, map, set, unordered_map, unordered_set
- **Algorithms**: sort, search, heap operations, numeric algorithms
- **Iterators**: Unified interface for accessing container elements

### Object-Oriented Programming
- **Classes and Objects**: Encapsulation, inheritance, polymorphism
- **Templates**: Generic programming for type-safe code reuse
- **Exception Handling**: Robust error management
- **Multiple Inheritance**: Complex inheritance hierarchies

### Modern Features (C++11 and later)
- **Smart Pointers**: unique_ptr, shared_ptr, weak_ptr for automatic memory management
- **Lambda Expressions**: Anonymous functions for functional programming
- **Auto Keyword**: Type inference for cleaner code
- **Range-based for loops**: Simplified iteration
- **Move Semantics**: Efficient resource transfer

## Common Use Cases

1. **System Programming**: Operating systems, device drivers
2. **Game Development**: Unreal Engine, Unity (C# with C++ backend)
3. **High-Frequency Trading**: Low-latency financial applications
4. **Scientific Computing**: Numerical simulations, data analysis
5. **Embedded Systems**: IoT devices, automotive software
6. **Competitive Programming**: Preferred language for programming contests
7. **Desktop Applications**: Adobe products, Microsoft Office components

## Advantages

### Performance
- **Execution Speed**: Among the fastest high-level languages
- **Memory Control**: Precise control over memory allocation/deallocation
- **Cache Performance**: Optimized data layout and access patterns

### Ecosystem
- **Large Community**: Extensive libraries and frameworks
- **Source Portability**: Standards-conforming source can often be rebuilt across platforms, subject to operating-system, compiler, library, and ABI differences
- **Industry Adoption**: Widely used in performance-critical applications
- **Job Market**: High demand for C++ developers in specialized fields

### Compatibility
- **C Interoperability**: C++ can call C interfaces through compatible declarations, but C++ is not a strict superset of every version of C
- **Binary Interoperability**: ABI compatibility is platform- and toolchain-specific; the C++ language standard does not define one universal ABI

## Disadvantages and Quirks

### Complexity
- **Steep Learning Curve**: Complex syntax and numerous features
- **Manual Memory Management**: Prone to memory leaks and dangling pointers
- **Header Dependencies**: Long compilation times for large projects
- **Behavioral Categories**: C++ distinguishes undefined, unspecified, and implementation-defined behavior; unsafe operations may invoke undefined behavior

### Development Challenges
- **Verbose Syntax**: Requires more code than modern languages
- **Build Systems**: Complex compilation and linking processes
- **Debugging Difficulty**: Memory errors can be hard to trace
- **Platform-Specific Code**: Sometimes requires conditional compilation

### Safety Issues
- **Buffer Overflows**: No automatic bounds checking
- **Memory Corruption**: Pointer errors can cause crashes
- **Type Safety**: C-style casting can bypass type system
- **Exception Safety**: Code without RAII or well-defined exception guarantees can leak resources or leave objects in invalid states

## C++ for DSA Learning

### Why C++ is Excellent for Data Structures and Algorithms

1. **Performance Analysis**: See actual time complexity differences
2. **Memory Understanding**: Learn how data structures use memory
3. **STL Implementation**: Study professional-quality implementations
4. **Pointer Mastery**: Deep understanding of references and memory
5. **Template Programming**: Learn generic algorithm design

### Key DSA Concepts in C++
- **Pointers and References**: Foundation for linked structures
- **Dynamic Memory Allocation**: Essential for flexible data structures
- **Template Metaprogramming**: Compile-time algorithm optimization
- **STL Containers**: Production-ready data structure implementations
- **Algorithm Library**: Standardized algorithm implementations

## Best Practices

1. **Use Modern C++**: Prefer C++11/14/17/20 features over legacy C-style code
2. **RAII Principle**: Always manage resources with object lifetimes
3. **Smart Pointers**: Prefer smart pointers over raw pointers
4. **STL Algorithms**: Use standard algorithms instead of manual implementations
5. **Const Correctness**: Use const for safety and clarity
6. **Exception Safety**: Write exception-safe code
7. **Move Semantics**: Use move operations for efficiency

## Learning Path

1. **Basic Syntax**: Variables, control flow, functions
2. **Object-Oriented Programming**: Classes, inheritance, polymorphism
3. **Memory Management**: Pointers, references, smart pointers
4. **STL Mastery**: Containers, iterators, algorithms
5. **Template Programming**: Generic programming techniques
6. **Advanced Features**: Concurrency, move semantics, concepts

## Repository Structure

```
1. C++/
├── README.md
├── 00. Headers and Libraries/     # STL and standard library coverage
│   ├── README.md
│   ├── Fundamentals/              # Core STL headers (iostream, vector, etc.)
│   └── Others/                    # Advanced topics (concurrency, debugging, etc.)
├── 01. Basics/                    # Fundamental C++ concepts
│   ├── README.md
│   ├── Variables, Keywords and Operators
│   ├── Conditional Statements
│   ├── Loops and Iterations
│   ├── Functions and Scopes
│   ├── Arrays and Strings
│   ├── Pointers and Memory Management
│   └── Error Handling
├── 02. Basic Problems/            # Foundational algorithm problems
│   ├── README.md
│   ├── Search Algorithms/         # Linear, binary, and advanced search
│   ├── Sorting Algorithms/        # All major sorting techniques
│   └── Pattern Making             # Pattern programming exercises
├── 03. OOPS/                      # Object-Oriented Programming
│   ├── README.md
│   ├── Introduction/
│   ├── Classes and Objects/
│   ├── Constructors and Destructors/
│   ├── Encapsulation/
│   ├── Inheritance/
│   ├── Polymorphism/
│   ├── Abstraction/
│   ├── Advance OOP/
│   ├── Templates and Generic Programming/
│   ├── Exception Handling/
│   ├── Memory Management/
│   ├── Design Patterns/
│   ├── Best Practices/
│   ├── Modern C++ Features/
│   ├── Projects and Applications/
│   ├── Glossary
│   ├── Index
│   └── References
├── 04. Data Structures/           # Standard containers and selected custom structures
│   ├── README.md
│   ├── Theory.md
│   ├── Array
│   ├── String
│   ├── Sequence Container
│   ├── Containers Adapters
│   ├── Associative Containers
│   ├── Unassociative Containers
│   ├── Utility
│   └── Specialized Containers/
├── 05. Trees and Graphs/          # Tree and graph data structures
│   ├── README.md
│   ├── Binary Trees/              # Tree fundamentals and operations
│   ├── BST/                       # Binary Search Trees
│   ├── AVL Trees/                 # Self-balancing trees
│   ├── Graph Representations/     # Graph storage and basic algorithms
│   ├── Tree Transversals
│   └── Basic Graph Algorithms
├── 06. Problem Solving/           # Essential problem-solving techniques
│   ├── README.md
│   ├── Mathematical Problems/     # Number theory, combinatorics
│   ├── Bit Manipulation/          # Bitwise operations and tricks
│   ├── String Problems/           # String algorithms and processing
│   ├── Array Problems/            # Array manipulation techniques
│   └── Puzzle Problems/           # Logical and mathematical puzzles
└── Algorithms/                    # Advanced algorithms (framework provided)
│   ├── README.md
    ├── Graph Algorithms/
    ├── Dynamic Programming/
    ├── Greedy Algorithms/
    ├── Divide and Conquer/
    └── Backtracking/
```

## 🗺️ Master Curriculum Architecture

For a broader syllabus map covering prerequisites, complexity summaries, and problem-solving archetypes, see the:
👉 **[Master DSA Curriculum Map](MASTER_DSA_MAP.md)**

## Section Status

All sections contain substantial study material, but the examples are currently undergoing technical review and automated extraction. Until a lesson is backed by a compiled and tested source file, treat its code as illustrative rather than production-ready.

Start with the [toolchain guide](TOOLCHAIN.md), follow the [standards policy](STANDARDS.md), and use the [verified example suite](examples/README.md) to check your environment. The suite builds through CMake and is tested on GCC, Clang, MSVC, and a sanitizer configuration in CI.

- **00. Headers and Libraries**: Broad standard-library and supporting-topic reference material
- **01. Basics**: Core syntax, control flow, functions, arrays, pointers, and error handling
- **02. Basic Problems**: Search, sorting, and pattern-programming material
- **03. OOPS**: Object-oriented programming, object lifetime, templates, exceptions, design patterns, and related modern C++ features
- **04. Data Structures**: ADT design and custom structures, including linked lists, Trie, DSU, Segment Tree, and Fenwick Tree; standard containers have one canonical home under Headers and Libraries
- **05. Trees and Graphs**: Classical trees, traversals, representations, heaps, and selected advanced tree techniques
- **06. Problem Solving**: Mathematical, bit, string, array, and puzzle-oriented examples
- **Algorithms**: Graph algorithms, dynamic programming, greedy methods, divide and conquer, and backtracking

## Key Features of This Repository

### Broad Coverage
- **435 Markdown files** after the first duplicate-topic consolidation pass
- **Theory and mathematical foundations** across the major algorithm families, with verification status documented in [REPORT.md](REPORT.md)
- **Practical examples** with real-world applications
- **Performance discussions** for many data structures and algorithms

### Learning-Focused Design
- **Progressive difficulty** from basics to advanced topics
- **Multiple implementations** (recursive, iterative, optimized)
- **Edge case handling** and error management
- **Best practices** and modern C++ standards

### Practical Applications
- **Competitive programming** templates and techniques
- **Interview preparation** problems and solutions
- **Real-world examples** and use cases
- **Performance optimization** strategies

## Getting Started

### For Beginners
1. Start with **01. Basics** to learn C++ fundamentals
2. Move to **02. Basic Problems** for algorithm practice
3. Study **03. OOPS** for object-oriented concepts
4. Explore **04. Data Structures** for essential data structures

### For Intermediate Learners
1. Master **05. Trees and Graphs** for advanced data structures
2. Practice **06. Problem Solving** for competitive programming
3. Study **00. Headers and Libraries** for STL mastery
4. Implement algorithms in the **Algorithms** section

### For Advanced Users
1. Review the verification findings in [REPORT.md](REPORT.md)
2. Compile and test canonical examples before optimizing them
3. Study advanced problem-solving techniques after completing their prerequisites
4. Use explicit C++17, C++20, or C++23 labels when extending the material

## Conclusion

C++ remains a dominant language in performance-critical applications and competitive programming. While it has a steeper learning curve than modern languages, its combination of low-level control and high-level abstractions makes it an excellent choice for learning data structures and algorithms. 

This repository provides a broad path from basic C++ syntax to advanced problem-solving techniques. It is an evolving study compendium rather than an exhaustive definition of C++ or DSA; see [REPORT.md](REPORT.md) for its current verification status and improvement roadmap.

## Next Step

- Go to [01_Basics](01.%20Basics/README.md) to continue understanding Basics of Programming in C++.
