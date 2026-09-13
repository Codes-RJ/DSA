# `std::array` Construction and Access

## Initialization

```cpp
#include <array>

std::array<int, 4> uninitialized;     // Fundamental elements have indeterminate values.
std::array<int, 4> zeroed{};          // All elements are value-initialized.
std::array<int, 4> values{2, 4, 6, 8};
```

Prefer brace initialization. Missing initializers value-initialize the remaining elements.

In C++17, template argument deduction can infer the element type and size when the elements share a suitable type:

```cpp
std::array inferred{1, 2, 3};
```

## Access

| Operation | Behavior | Bounds check |
|---|---|---|
| `values[index]` | Element at index | No |
| `values.at(index)` | Element at index | Throws `std::out_of_range` |
| `front()` | First element | Requires non-empty array |
| `back()` | Last element | Requires non-empty array |
| `data()` | Pointer to contiguous storage | Does not transfer ownership |

```cpp
values.at(1) = 10;
const int first = values.front();
int* storage = values.data();
```

Use `at` at checked input boundaries. Use `operator[]` when the algorithm already proves the index is valid.

## Zero-Length Arrays

`std::array<int, 0>` has `begin() == end()` and `size() == 0`. The return value of `data()` is not a pointer that may be dereferenced. Calling `front()`, `back()`, or indexing an element violates their preconditions.

## Next Step

Continue to [Iteration and Algorithms](02_Iteration_and_Algorithms.md).
