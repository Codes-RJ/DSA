# Custom Exception Types

> **Minimum standard:** C++17
>
> **Prerequisites:** [`try`, `catch`, and `throw`](../01_Try_Catch_Throw.md), [standard exceptions](../02_Standard_Exceptions.md), RAII, inheritance, and object lifetime.

Create a custom exception type only when callers need a stable, domain-specific failure category or structured diagnostic data. A different message alone is not sufficient reason to add a type.

## Study Order

1. [Choosing and defining a custom type](01_Defining_a_Custom_Exception.md)
2. [Designing an exception hierarchy](02_Hierarchy_Design.md)
3. [Adding context and nested exceptions](03_Context_and_Nesting.md)
4. [Exceptions, error codes, and result types](04_Choosing_an_Error_Model.md)
5. [Testing and design exercises](05_Testing_and_Exercises.md)

## Core Rules

- Derive application exception types from an appropriate `std::exception` subtype.
- Store owned diagnostic data; do not retain dangling views or pointers.
- Keep construction and `what()` non-throwing in ordinary use.
- Catch by `const` reference and order handlers from most specific to most general.
- Throw by value; do not allocate the exception object manually.
- Do not use exceptions for expected branching or routine lookup misses.
- Document the abstraction-level failures a public operation can report.

## Next Step

Begin with [Defining a Custom Exception](01_Defining_a_Custom_Exception.md).
