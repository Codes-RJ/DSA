# Exception Specifications and Safety Guarantees

> **Minimum standard:** C++17
>
> **Prerequisites:** exceptions, RAII, move semantics, templates, and type traits.

Modern C++ uses `noexcept` to state that an exception will not escape a function. If one does escape, the program calls `std::terminate`; `noexcept` does not silently catch the exception.

## Study Order

1. [`noexcept` as a contract](01_Noexcept_Contract.md)
2. [Conditional `noexcept` in generic code](02_Conditional_Noexcept.md)
3. [Basic, strong, and non-throwing guarantees](03_Exception_Safety_Guarantees.md)
4. [Move, swap, destructors, and containers](04_Move_Swap_and_Destructors.md)
5. [Auditing and testing non-throwing code](05_Auditing_and_Testing.md)

## Central Distinctions

- `noexcept` is a function-type and termination contract.
- The `noexcept(expression)` operator is a compile-time query and does not evaluate its operand.
- An exception-safety guarantee describes observable state after failure.
- A function can provide the strong guarantee while still being allowed to throw.
- A function marked `noexcept` can still contain throwing operations only if it prevents every exception from escaping.

## Next Step

Begin with [`noexcept` as a Contract](01_Noexcept_Contract.md).
