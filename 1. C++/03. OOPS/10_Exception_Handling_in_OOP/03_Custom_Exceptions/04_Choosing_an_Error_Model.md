# Choosing an Error Model

Exceptions are one way to report failure, not a universal replacement for preconditions, optional values, status codes, or result types.

## Decision Table

| Situation | Typical model |
|---|---|
| Programmer violated a documented precondition | Assertion during development, contract documentation, or exception at a checked public boundary |
| Lookup may routinely miss | Iterator, pointer, or `std::optional` |
| Constructor cannot establish its invariant | Exception |
| Deep operation cannot recover locally | Exception propagated to an owning boundary |
| Every call site must branch on an expected outcome | Status/result value |
| Operating-system error with a portable category | `std::error_code` or `std::system_error` |
| C ABI or exception-disabled boundary | Explicit status code and output value |

## Error Codes and Exceptions

`std::error_code` is a value. It can be stored, compared, and returned without stack unwinding. `std::system_error` is an exception that carries an `error_code`.

Use an enum-based domain code only when its values form a stable contract. Pair it with a category or custom exception when callers require both machine-readable classification and exception propagation.

## Optional Is Not an Error Message

`std::optional<T>` communicates either a `T` or no value. It is effective for an ordinary absence but does not explain multiple failure causes. Do not encode detailed failures as arbitrary sentinel values inside `T`.

## C++23 `std::expected`

`std::expected<T, E>` represents either a value or an error and makes the branch explicit in the type. It is a C++23 extension in this curriculum and must not appear as an unexplained dependency in C++17 core lessons.

## Boundary Rule

Choose one model for a public abstraction and translate lower-level mechanisms at its boundary. Avoid forcing callers to handle a mixture of exceptions, sentinel values, assertions, and error codes for closely related operations.

## Next Step

Continue to [Testing and Exercises](05_Testing_and_Exercises.md).
