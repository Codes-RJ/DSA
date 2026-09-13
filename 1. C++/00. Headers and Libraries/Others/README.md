# Supporting C++ Library and Tooling Guides

> **Role in the curriculum:** Focused references for language facilities, ownership, diagnostics, performance, concurrency, and library features that support later DSA work.

## Recommended Order

| Step | Guide | Main outcome |
|---:|---|---|
| 1 | [Best practices](best_practices.md) | Apply safe defaults, RAII, and clear interface design |
| 2 | [STL container selection](stl_containers.md) | Choose a standard container from required operations and invalidation rules |
| 3 | [Move semantics](move_semantics.md) | Understand value categories and efficient ownership transfer |
| 4 | [Smart pointers](smart_pointers.md) | Express unique, shared, and observing lifetime relationships |
| 5 | [Lambda expressions](lambda_expressions.md) | Supply local behavior to algorithms and callbacks |
| 6 | [Debugging](debugging.md) | Reproduce, isolate, inspect, and prevent defects |
| 7 | [Optimization](optimization.md) | Measure before changing code and reason about real bottlenecks |

## Specialized References

- [Concurrency overview](concurrency.md)
- [Multithreading](multithreading.md)
- [Filesystem](filesystem.md)
- [Regular expressions](regular_expressions.md)
- [Miscellaneous utilities](miscellaneous.md)

## Canonical Ownership

Some earlier pages in this folder duplicated full subjects. Those copies were removed. Use these canonical locations instead:

- [Templates and Generic Programming](../../03.%20OOPS/09_Templates_and_Generic_Programming/README.md)
- [Design Patterns](../../03.%20OOPS/12_Design_Patterns/README.md)
- [Low-Level Memory Topics](../../03.%20OOPS/11_Memory_Management_in_OOP/README.md)
- [Fundamental standard-library headers](../Fundamentals/README.md)

## How to Use These Pages

Read the recommended-order pages alongside the core language path. Treat the specialized pages as just-in-time references. For every example, note its minimum language standard, compile it with warnings enabled, and prefer a standard-library facility over a custom replacement unless implementing the mechanism is itself the exercise.

## Next Step

Return to [Headers and Libraries](../README.md) or continue along the repository-wide [learning path](../../LEARNING_PATH.md).
