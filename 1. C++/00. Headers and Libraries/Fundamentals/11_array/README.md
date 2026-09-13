# `std::array`: Fixed-Size Contiguous Storage

> **Header:** `<array>`
>
> **Minimum standard:** C++17
>
> **Prerequisites:** built-in arrays, templates, iterators, value initialization, and contiguous storage.

`std::array<T, N>` wraps exactly `N` elements in a regular value type. Its size is part of its type and cannot change at runtime.

## Study Order

1. [Construction and access](01_Construction_and_Access.md)
2. [Iteration and algorithms](02_Iteration_and_Algorithms.md)
3. [Value semantics and compile-time use](03_Value_and_Compile_Time_Semantics.md)
4. [Complexity and interoperability](04_Complexity_and_Interoperability.md)
5. [Applied patterns and exercises](05_Applied_Patterns.md)

## Choose `std::array` When

- the element count is known at compile time;
- contiguous storage and zero dynamic allocation are wanted;
- the collection should be copied, returned, or compared as one value;
- standard iterator-based algorithms should work directly.

Use `std::vector` for a runtime-sized or growable sequence, and use `std::span` in a C++20 interface that observes contiguous storage without owning it.

## Core Invariants

- `size()` is always `N`;
- elements occupy contiguous storage;
- there is no capacity separate from size;
- no insertion, erasure, or reallocation operation exists;
- `std::array<T, 0>` is valid, but `front()` and `back()` are not valid on it.

## Next Step

Begin with [Construction and Access](01_Construction_and_Access.md).
