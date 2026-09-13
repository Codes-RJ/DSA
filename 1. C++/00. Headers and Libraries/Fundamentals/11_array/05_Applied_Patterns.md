# `std::array` Applied Patterns

## Lookup Table

```cpp
#include <array>
#include <string_view>

constexpr std::array<std::string_view, 7> weekday_names{
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"};
```

Validate a runtime index before using it. A fixed lookup table is effective when every valid key maps to a dense integer range.

## Fixed-Extent Matrix

```cpp
template <class T, std::size_t Rows, std::size_t Columns>
using Matrix = std::array<std::array<T, Columns>, Rows>;

Matrix<int, 2, 3> matrix{{
    {{1, 2, 3}},
    {{4, 5, 6}},
}};
```

Rows remain contiguous individually, but do not pass a nested array to an API that assumes one flat `T*` range without proving the required representation and bounds.

## Exercises

1. Implement dot product for two arrays of the same compile-time size.
2. Rotate a fixed array left without allocating another dynamic container.
3. Build a compile-time table of squares for a small bounded domain.
4. Compare passing an array by value, by const reference, and through a pointer/count interface.
5. Test `std::array<int, 0>` without calling an element-access operation.

## Exit Criteria

You can distinguish `std::array` from a built-in array and `std::vector`, explain why size is part of the type, choose checked access at an input boundary, and state that swapping two arrays is linear in their extent.

## Next Step

Continue to [`std::deque`](../12_deque.md).
