# Runtime Polymorphism

> **Minimum standard:** C++17

## Study Order

1. [Virtual functions](01_Virtual_Functions.md)
2. [`override`](02_Override_Specifier.md)
3. [`final`](03_Final_Specifier.md)
4. [Pure virtual functions](04_Pure_Virtual_Functions.md)
5. [Abstract classes](../../07_Abstraction/01_Abstract_Classes.md) — canonical lesson
6. [Virtual-table model](06_Virtual_Table.md) — common implementation model, not a language-level layout guarantee
7. [Runtime type information](07_Run_Time_Type_Information.md)

## Central Contract

Runtime polymorphism requires a stable base-class interface, virtual dispatch, lifetime-safe access to the complete object, and normally a virtual destructor when deletion through the base is allowed. Prefer references or non-owning pointers for observation and smart pointers for ownership.

## Next Step

Continue to the canonical [Abstraction](../../07_Abstraction/README.md) section.
