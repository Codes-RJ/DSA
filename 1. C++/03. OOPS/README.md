# Object-Oriented and Generic Programming in C++

> **Role in the curriculum:** Classes, object lifetime, resource ownership, runtime and static polymorphism, abstraction, generic programming, and selected design techniques.

## Prerequisites

- Complete [`01. Basics`](../01.%20Basics/README.md).
- Understand references, pointers, `const`, functions, scope, and automatic versus dynamic storage.
- Learn the essential [`string`](../00.%20Headers%20and%20Libraries/Fundamentals/03_string.md), [`vector`](../00.%20Headers%20and%20Libraries/Fundamentals/02_vector.md), and [`memory`](../00.%20Headers%20and%20Libraries/Fundamentals/22_memory.md) facilities.

## Canonical Study Order

| Step | Section | Main outcome |
|---:|---|---|
| 1 | [Introduction](01_Introduction/README.md) | Explain objects, responsibilities, and when OOP is useful |
| 2 | [Classes and Objects](02_Classes_and_Objects/README.md) | Define small value-oriented classes with clear invariants |
| 3 | [Constructors and Destructors](03_Constructors_and_Destructors/README.md) | Control initialization, cleanup, copy, and move behavior |
| 4 | [Encapsulation](04_Encapsulation/README.md) | Protect invariants through a minimal public interface |
| 5 | [Inheritance](05_Inheritance/README.md) | Use public inheritance only for valid substitutability |
| 6 | [Polymorphism](06_Polymorphism/README.md) | Compare overloading, templates, and virtual dispatch |
| 7 | [Abstraction](07_Abstraction/README.md) | Design interfaces and separate policy from implementation |
| 8 | [Advanced Class Mechanics](08_Advanced_OOP/README.md) | Understand conversions, slicing, virtual bases, and friends |
| 9 | [Templates and Generic Programming](09_Templates_and_Generic_Programming/README.md) | Write reusable algorithms and types with compile-time constraints |
| 10 | [Exception Handling and RAII](10_Exception_Handling_in_OOP/README.md) | Maintain invariants and resource safety when operations fail |
| 11 | [Low-Level Memory Topics](11_Memory_Management_in_OOP/README.md) | Study manual allocation and placement only after RAII |
| 12 | [Design Patterns](12_Design_Patterns/README.md) | Apply selected patterns when simpler composition is insufficient |
| 13 | [Best Practices](13_Best_Practices/README.md) | Design maintainable interfaces and implementation boundaries |
| 14 | [Modern Language Features](14_Modern_Cpp_OOP_Features/README.md) | Use version-labeled C++17/20 features |
| 15 | [Projects](15_Projects_and_Applications/README.md) | Integrate classes, ownership, testing, and build structure |

## Canonical Cross-Section Topics

These subjects previously had multiple full tutorials. Use one canonical source:

- [Smart pointers](../00.%20Headers%20and%20Libraries/Others/smart_pointers.md)
- [Move semantics and value categories](../00.%20Headers%20and%20Libraries/Others/move_semantics.md)
- [Lambda expressions](../00.%20Headers%20and%20Libraries/Others/lambda_expressions.md)
- [Delegating constructors](03_Constructors_and_Destructors/07_Delegating_Constructors.md)
- [Placement new](11_Memory_Management_in_OOP/03_Placement_New.md)
- [Abstract classes](07_Abstraction/01_Abstract_Classes.md)
- [Templates and generic programming](09_Templates_and_Generic_Programming/README.md)
- [Design patterns](12_Design_Patterns/README.md)

## Design Rules Used by This Path

1. Prefer value semantics and the Rule of Zero.
2. Use composition by default; introduce inheritance only when substitution is valid.
3. Make ownership explicit and keep raw owning pointers out of application-level examples.
4. Give every class a documented invariant.
5. Keep interfaces small and const-correct.
6. Distinguish runtime polymorphism from templates and overload resolution.
7. Treat patterns as trade-offs, not mandatory architecture.
8. Do not mark operations `noexcept` without accounting for every operation in the body.

## Supporting References

- [`00_Glossary.md`](00_Glossary.md)
- [`00_References.md`](00_References.md)
- Repository-wide [`LEARNING_PATH.md`](../LEARNING_PATH.md)
- Audit and cleanup roadmap: [`REPORT.md`](../REPORT.md)

## Exit Criteria

You are ready for project work when you can:

- implement a value type using the Rule of Zero;
- explain construction and destruction order;
- identify slicing and unsafe downcasts;
- design and test an abstract interface;
- choose between templates and virtual dispatch;
- describe strong, basic, and no-throw exception guarantees;
- use smart pointers without cycles or ambiguous ownership;
- justify a design pattern against a simpler alternative.

## Next Step

Continue to [Data Structures](../04.%20Data%20Structures/README.md) or follow the repository-wide [learning path](../LEARNING_PATH.md).
