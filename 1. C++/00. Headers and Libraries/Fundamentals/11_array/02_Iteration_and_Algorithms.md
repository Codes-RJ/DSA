# `std::array` Iteration and Algorithms

`std::array` provides random-access iterators and works with standard algorithms.

```cpp
#include <algorithm>
#include <array>
#include <numeric>

std::array<int, 5> values{4, 1, 5, 1, 3};

std::sort(values.begin(), values.end());
const int total = std::accumulate(values.begin(), values.end(), 0);
const auto position = std::lower_bound(values.begin(), values.end(), 3);
```

## Iterator Forms

- `begin()` and `end()` for mutable forward traversal;
- `cbegin()` and `cend()` for const traversal;
- `rbegin()` and `rend()` for reverse traversal;
- range-based `for` for direct element iteration.

## Whole-Array Operations

```cpp
std::array<int, 4> left{1, 2, 3, 4};
std::array<int, 4> right{};

right.fill(7);
left.swap(right);
```

`fill` assigns every element and therefore takes `O(N)`. Swapping arrays exchanges corresponding elements and takes `O(N)`; it is not a constant-time pointer swap.

## Transforming to Another Array

```cpp
std::array<int, 4> input{1, 2, 3, 4};
std::array<int, 4> squared{};

std::transform(input.begin(), input.end(), squared.begin(),
               [](int value) { return value * value; });
```

Check overflow before multiplication when the accepted input range can exceed `int`.

## Next Step

Continue to [Value and Compile-Time Semantics](03_Value_and_Compile_Time_Semantics.md).
