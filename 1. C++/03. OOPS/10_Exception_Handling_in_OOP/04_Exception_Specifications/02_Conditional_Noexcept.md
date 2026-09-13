# Conditional `noexcept` in Generic Code

## Constant-Expression Requirement

The expression inside a `noexcept(...)` specification must be a contextually converted constant expression of type `bool`. Runtime parameters cannot change a function's exception specification.

Invalid idea:

```cpp
// Invalid: should_throw is a runtime parameter.
// void run(bool should_throw) noexcept(!should_throw);
```

A compile-time parameter can select distinct function specializations:

```cpp
#include <stdexcept>

template <bool ShouldThrow>
void run() noexcept(!ShouldThrow) {
    if constexpr (ShouldThrow) {
        throw std::runtime_error("requested failure");
    }
}

static_assert(noexcept(run<false>()));
static_assert(!noexcept(run<true>()));
```

## Mirror the Exact Operation

Generic wrappers should derive their specification from the expression they actually execute:

```cpp
#include <utility>

template <class T>
void exchange(T& left, T& right)
    noexcept(noexcept(std::swap(left, right))) {
    std::swap(left, right);
}
```

If a wrapper deliberately uses an unqualified swap for argument-dependent lookup, ensure its queried expression models that same call. A helper can keep that logic readable.

## Traits Versus Expressions

Traits such as `std::is_nothrow_move_constructible_v<T>` are useful when construction is exactly the operation being promised. They are not sufficient for a wrapper that also allocates, logs, invokes callbacks, or mutates another container.

For example, `std::vector<T>::push_back` may allocate even when moving `T` is non-throwing. A wrapper around it generally cannot be conditionally `noexcept` based only on `T`'s move constructor.

## Design Rule

Use conditional `noexcept` when generic code exposes the same exception behavior as a well-defined underlying operation. Do not add complicated specifications to ordinary code merely to make it look optimized.

## Next Step

Continue to [Exception-Safety Guarantees](03_Exception_Safety_Guarantees.md).
