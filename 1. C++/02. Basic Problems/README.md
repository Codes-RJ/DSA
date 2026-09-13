# Basic Problem-Solving Foundations

> **Minimum standard:** C++17
>
> **Prerequisites:** Complete the core lessons in [`01. Basics`](../01.%20Basics/README.md), especially loops, functions, arrays, strings, and error handling.

This section turns language syntax into repeatable problem-solving habits. It is a bridge to data structures, not an encyclopedia of disconnected programs.

## Canonical Study Order

| Step | Section | Main outcome |
|---:|---|---|
| 1 | [Pattern exercises](Patterns/README.md) | Translate row/column relationships into predicates and output |
| 2 | [Searching](Search/README.md) | State preconditions, invariants, and search-space reduction |
| 3 | [Sorting](Sorting/README.md) | Compare stability, adaptiveness, storage, and asymptotic cost |

## Practice Loop

For each problem:

1. Restate the input, output, and invalid-input policy.
2. Work through a small example by hand.
3. Write the invariant or row/column rule before writing code.
4. Implement a function whose logic is separate from console I/O.
5. Test empty, one-element, duplicate, already-ordered, reverse-ordered, and extreme inputs where relevant.
6. State time complexity, auxiliary space, and any output-size lower bound.
7. Compare the result with a standard-library reference when one exists.

## Exit Criteria

You are ready for [Data Structures](../04.%20Data%20Structures/README.md) when you can:

- derive a nested-loop boundary instead of guessing it;
- implement linear and binary search with explicit preconditions;
- explain why comparison sorting has a worst-case lower bound of `Omega(N log N)`;
- distinguish stable from unstable sorting;
- test an implementation against `std::find`, `std::lower_bound`, or `std::sort`;
- diagnose an off-by-one error from a failing boundary case.

## Next Step

Begin with [Pattern Exercises](Patterns/README.md).
