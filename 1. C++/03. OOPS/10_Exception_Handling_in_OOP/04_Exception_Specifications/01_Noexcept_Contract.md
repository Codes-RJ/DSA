# `noexcept` as a Contract

## Meaning

```cpp
void close() noexcept;
void parse();
void update() noexcept(false);
```

If an exception escapes `close`, the runtime calls `std::terminate`. Callers cannot recover with an outer `catch`. Apply `noexcept` only after auditing the complete implementation.

## Compile-Time Query

```cpp
#include <utility>
#include <vector>

static_assert(noexcept(std::declval<std::vector<int>&>().size()));
static_assert(!noexcept(std::declval<std::vector<int>&>().push_back(1)));
```

The operand of the `noexcept` operator is unevaluated. The result is a constant expression describing whether the expression is declared non-throwing; it does not prove that an incorrect implementation will never terminate.

## Function Types

Since C++17, exception specifications are part of function types. A pointer to a potentially throwing function cannot be converted to a pointer that promises non-throwing behavior.

```cpp
using Task = void (*)();
using SafeTask = void (*)() noexcept;

void safe_task() noexcept {}
void ordinary_task() {}

SafeTask safe = safe_task;
Task either = safe_task;
// SafeTask invalid = ordinary_task;
```

## Virtual Overrides

An override must not weaken the base contract:

```cpp
struct Base {
    virtual void reset() noexcept = 0;
    virtual void refresh() = 0;
    virtual ~Base() = default;
};

struct Derived final : Base {
    void reset() noexcept override {}
    void refresh() noexcept override {}
};
```

An override may strengthen a potentially throwing base operation by declaring itself `noexcept`.

## Historical Note

Dynamic exception specifications such as `throw(Type)` are removed from modern C++. `throw()` was historically used for a non-throwing promise; use `noexcept` in current code.

## Next Step

Continue to [Conditional `noexcept`](02_Conditional_Noexcept.md).
