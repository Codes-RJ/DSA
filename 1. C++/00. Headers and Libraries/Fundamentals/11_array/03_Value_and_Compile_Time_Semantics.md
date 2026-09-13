# `std::array` Value and Compile-Time Semantics

## Size Is Part of the Type

`std::array<int, 3>` and `std::array<int, 4>` are different types. The extent must be a compile-time constant.

Use `std::vector` when the number of elements is selected at runtime. Use `std::array` when a fixed extent is part of the domain, such as RGB components or a bounded lookup table.

## Value Semantics

Unlike a built-in array, `std::array` can be returned, assigned, compared, and stored as a regular value. Copying an array copies all `N` elements.

```cpp
#include <array>

std::array<int, 3> coordinates() {
    return {4, 2, 7};
}

std::array<int, 3> left{1, 2, 3};
std::array<int, 3> right = left;
```

## Tuple Interface

```cpp
#include <tuple>

const auto [x, y, z] = coordinates();
static_assert(std::tuple_size_v<std::array<int, 3>> == 3U);
```

`std::get<I>(array)` uses a compile-time index. An out-of-range `I` is a compile-time error.

## Constant Evaluation

The exact set of operations usable in constant evaluation expands in newer standards. Keep a C++17 lesson within the C++17 guarantees and label any C++20 example explicitly.

## Next Step

Continue to [Complexity and Interoperability](04_Complexity_and_Interoperability.md).
