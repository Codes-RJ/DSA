# Low-Level Memory Topics

> **Minimum standard:** C++17
>
> **Prerequisite:** Understand RAII, the Rule of Zero, and [smart pointers](../../00.%20Headers%20and%20Libraries/Others/smart_pointers.md) first.

This section explains mechanisms needed for data-structure internals, allocators, pools, and systems code. It is not the default ownership model for application code.

## Study Order

1. [`new` and `delete`](01_New_and_Delete.md)
2. [Allocation for objects and arrays](02_New_Delete_for_Objects.md)
3. [Placement new](03_Placement_New.md)
4. [Memory pools](04_Memory_Pools.md)

## Safety Rules

- Prefer automatic storage and standard containers.
- Prefer the Rule of Zero.
- Use `std::unique_ptr` for unique ownership and `std::shared_ptr` only for genuinely shared lifetime.
- A raw pointer should normally be non-owning and have a documented lifetime.
- Pair every low-level construction operation with the correct destruction and deallocation operation.
- Test exceptional paths, alignment, double destruction, use-after-free, and leaks with sanitizers.

## Next Step

Continue to [Design Patterns](../12_Design_Patterns/README.md).
