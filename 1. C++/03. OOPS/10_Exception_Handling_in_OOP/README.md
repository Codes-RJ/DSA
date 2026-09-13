# Exceptions and RAII

> **Minimum standard:** C++17
>
> **Prerequisites:** Functions, stack lifetime, classes, inheritance, ownership, constructors, and destructors.

Exceptions report failures that cannot be handled where they are detected. RAII keeps invariants and resource ownership safe while the stack unwinds.

## Study Order

| Step | Lesson | Main outcome |
|---:|---|---|
| 1 | [Exception model](Theory.md) | Explain propagation, unwinding, handlers, and failure boundaries |
| 2 | [`try`, `catch`, and `throw`](01_Try_Catch_Throw.md) | Throw by value, catch by reference, and rethrow correctly |
| 3 | [Standard exception types](02_Standard_Exceptions.md) | Select an existing standard category before inventing one |
| 4 | [Custom exception types](03_Custom_Exceptions/README.md) | Design shallow domain categories and owned context |
| 5 | [Exception specifications](04_Exception_Specifications/README.md) | Distinguish `noexcept` from safety guarantees |
| 6 | [RAII](05_RAII.md) | Tie resource lifetime to object lifetime and prefer the Rule of Zero |

## Required Design Rules

1. Use exceptions for exceptional failures, not normal loop or lookup control flow.
2. Acquire each resource into an RAII object immediately.
3. Keep destructors non-throwing.
4. Catch only where code can recover, translate abstractions, or report one final diagnostic.
5. State the post-failure invariant and exception guarantee of mutating operations.
6. Preserve lower-level causes when translating at an abstraction boundary.
7. Audit every branch before promising `noexcept`.

## Exit Criteria

You can explain stack unwinding, choose a standard or custom failure type, implement prepare and commit for the strong guarantee, build a Rule-of-Zero resource owner, and identify a false `noexcept` promise.

## Next Step

Proceed to [Design Patterns](../12_Design_Patterns/README.md). Study [Low-Level Memory Topics](../11_Memory_Management_in_OOP/README.md) only when allocation internals are needed.
