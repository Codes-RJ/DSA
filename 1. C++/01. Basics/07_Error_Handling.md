# Error Handling Fundamentals

> **Role in the path:** Required C++ bridge
>
> **Prerequisites:** Functions, references, strings, and basic classes
>
> **Scope:** Learn enough error handling to write honest, testable DSA code. Resource safety, custom exception hierarchies, exception guarantees, and advanced `noexcept` design belong to the [Exceptions and RAII module](../03.%20OOPS/10_Exception_Handling_in_OOP/README.md).

Algorithms are easier to reason about when their input contract is explicit. Before choosing an error mechanism, decide whether a result is ordinary, invalid input is a caller bug, or an operation genuinely failed.

## 1. Start with the Contract

Consider binary search. “Target not found” is a normal result, so it should not throw. An invalid search range is a violated precondition and should be rejected or prevented by the interface.

| Situation | Prefer | Example |
|---|---|---|
| Normal absence | Sentinel or `std::optional` | Target is not in an array |
| Invalid argument | Validation, then `std::invalid_argument` when recovery is possible | Negative graph vertex count |
| Valid argument outside an allowed range | `std::out_of_range` | Vertex index is not in `[0, n)` |
| Operation failure | A relevant standard exception | Parsing malformed input |
| Programmer invariant is false | Assertion during development | Heap size disagrees with storage |

Do not use exceptions as a replacement for an ordinary `if` statement or as loop control.

## 2. A Normal “Not Found” Result

```cpp
#include <cstddef>
#include <optional>
#include <vector>

std::optional<std::size_t> findFirst(
    const std::vector<int>& values,
    int target) {
    for (std::size_t index = 0; index < values.size(); ++index) {
        if (values[index] == target) {
            return index;
        }
    }
    return std::nullopt;
}
```

Absence is part of the function's normal domain, so the return type communicates it directly.

## 3. `throw`, `try`, and `catch`

Use an exception when the current function cannot produce its promised result and its caller may be able to recover.

```cpp
#include <iostream>
#include <stdexcept>
#include <vector>

int checkedVertexValue(const std::vector<int>& values, int vertex) {
    if (vertex < 0 || vertex >= static_cast<int>(values.size())) {
        throw std::out_of_range("vertex index is outside the graph");
    }
    return values[static_cast<std::size_t>(vertex)];
}

int main() {
    const std::vector<int> distance{0, 4, 9};

    try {
        std::cout << checkedVertexValue(distance, 5) << '\n';
    } catch (const std::out_of_range& error) {
        std::cerr << "Input error: " << error.what() << '\n';
    }
}
```

The control flow is:

1. `throw` creates an exception object.
2. The runtime searches outward for a matching handler.
3. Local objects on exited scopes are destroyed during stack unwinding.
4. The selected `catch` block handles or reports the failure.

## 4. Rules That Prevent Common Bugs

- Throw objects by value: `throw std::invalid_argument("message");`.
- Catch polymorphic exceptions by `const` reference: `catch (const std::exception& error)`.
- Put specific handlers before general handlers.
- Catch only where you can recover, add meaningful context, or produce the program's final diagnostic.
- Use `throw;` to preserve the active exception when rethrowing. `throw error;` can slice it.
- Never leave an empty `catch` block.
- Do not throw raw strings or integers in normal C++ code; standard exception types compose better.

## 5. Choose a Standard Exception

The most useful beginner categories are:

| Type | Meaning |
|---|---|
| `std::invalid_argument` | The argument's value is not acceptable |
| `std::out_of_range` | A valid kind of value is outside the supported range |
| `std::overflow_error` | A mathematical result cannot be represented |
| `std::runtime_error` | A runtime failure has no more precise standard category |

Prefer a precise existing category. Design custom types only when callers need a domain-specific recovery policy or structured context; that is covered in [Custom Exception Types](../03.%20OOPS/10_Exception_Handling_in_OOP/03_Custom_Exceptions/README.md).

## 6. Assertions Are Different

An assertion documents a condition that should be impossible if the program is correct. It is not a user-input handler.

```cpp
#include <cassert>
#include <vector>

int heapRoot(const std::vector<int>& heap) {
    assert(!heap.empty());
    return heap.front();
}
```

If an empty heap can legitimately arrive from outside the function, represent that possibility in the return type or validate and report it. Do not rely on an assertion for recoverable input.

## 7. What `noexcept` Actually Promises

`noexcept` is a contract: if an exception escapes the function, the program calls `std::terminate`. It is not proof that every statement in the body is safe.

```cpp
#include <utility>

template <typename T>
void exchangeValues(T& left, T& right)
    noexcept(noexcept(std::swap(left, right))) {
    std::swap(left, right);
}
```

The condition checks the exact operation performed. At this stage, use `noexcept` only when the entire call path is intentionally non-throwing. Study the full contract in [`noexcept` as a Contract](../03.%20OOPS/10_Exception_Handling_in_OOP/04_Exception_Specifications/01_Noexcept_Contract.md).

## 8. DSA Error-Handling Checklist

Before submitting or publishing an implementation, ask:

- What inputs are valid?
- Is “not found” a normal result?
- Can an index be negative or exceed the container size?
- Can arithmetic overflow the chosen numeric type?
- Does the function mutate data before it discovers invalid input?
- Does the interface communicate failure without ambiguous magic values?
- Are tests present for empty, one-element, boundary, and invalid inputs?

Online-judge functions normally receive inputs that satisfy the problem statement. Keep their hot algorithmic path simple. In reusable library code, validate public boundaries and state the contract in the lesson.

## Practice

1. Rewrite a linear search that returns `-1` to return `std::optional<std::size_t>`.
2. Add vertex-range validation to a graph's public `addEdge` method.
3. Write `checkedMidpoint(int left, int right)` and decide which preconditions it should enforce.
4. Explain why “queue is empty” may be either normal absence or misuse depending on the API.
5. Test every failure branch without inspecting console text as the only assertion.

## Exit Check

You are ready to continue when you can:

- distinguish normal absence, invalid input, invariant failure, and runtime failure;
- choose between a return value, `std::optional`, assertion, or exception;
- throw by value and catch by `const` reference;
- explain stack unwinding at a high level; and
- explain why `noexcept` is a promise with termination consequences.

## Next Step

Continue to [Basic Problems](../02.%20Basic%20Problems/README.md). Return to the full [Exceptions and RAII module](../03.%20OOPS/10_Exception_Handling_in_OOP/README.md) after learning classes, constructors, destructors, and ownership.
