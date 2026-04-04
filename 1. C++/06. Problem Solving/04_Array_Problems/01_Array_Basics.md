# Array Basics in C++

## Introduction
An array is a collection of elements of the same type stored in contiguous memory locations. It's the most basic and frequently used data structure.

## C++ Array Types

### 1. Static Array (C-style)
Size is fixed at compile time and cannot be changed.
```cpp
int arr[5] = {1, 2, 3, 4, 5};
```

### 2. Standard Template Library (STL) `std::vector`
Dynamic array that can resize itself. This is the preferred way in modern C++.
```cpp
#include <vector>
std::vector<int> v = {1, 2, 3, 4, 5};
v.push_back(6); // Resizes automatically
```

### 3. `std::array` (C++11)
A thin wrapper around C-style arrays with STL-like functionality.
```cpp
#include <array>
std::array<int, 5> arr = {1, 2, 3, 4, 5};
```

## Common Operations

| Operation | Concept | Complexity |
|-----------|---------|------------|
| **Access** | `arr[i]` | O(1) |
| **Modify** | `arr[i] = val` | O(1) |
| **Search** | `find(arr, val)` | O(N) |
| **Insert** | `push_back` (vector) | O(1) amortized |
| **Delete** | `pop_back` (vector) | O(1) |
| **Sort** | `sort(v.begin(), v.end())` | O(N log N) |

## Memory Layout
In a 1D array of type `T`, the address of element `arr[i]` is:
`Address = Base_Address + i * sizeof(T)`

## Advantages
1. **Fast Access**: O(1) access for any element given its index.
2. **CPU Cache Friendly**: Contiguous storage improves spatial locality.
3. **Low Memory Overhead**: No extra pointers or metadata for basic arrays.

## Disadvantages
1. **Fixed Size**: Static arrays cannot grow. Dynamic arrays require reallocations eventually.
2. **Expensive Insert/Delete**: Adding or removing from the middle requires shifting O(N) elements.

## Summary Checklist
- [ ] Using `std::vector` for dynamic needs?
- [ ] Using `arr[i]` for O(1) access?
- [ ] Be aware of index-out-of-bounds errors.
- [ ] Using zero-indexing (0 to N-1).
- [ ] Considering 2D arrays for grid/matrix problems.
