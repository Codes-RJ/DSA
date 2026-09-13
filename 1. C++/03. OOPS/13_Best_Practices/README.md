# OOP Design Practices

> **Minimum standard:** C++17

## Study Order

1. [Class-design theory](Theory.md) — cohesion, coupling, SOLID heuristics, exception safety, and maintainability.
2. [Pimpl idiom](01_Pimpl_Idiom.md) — an optional implementation-boundary technique for stable interfaces and reduced compile dependencies.

## Working Rules

- Prefer value semantics and the Rule of Zero.
- Keep a class responsible for one coherent invariant.
- Prefer composition; use public inheritance only for substitutable types.
- Make ownership and lifetime visible in types and documentation.
- Keep public interfaces small, const-correct, and difficult to misuse.
- Do not use a design pattern or Pimpl without a concrete maintenance benefit.
- Test behavior at public boundaries instead of coupling tests to private representation.
- State the exception guarantee of mutating operations when failure matters.

## Next Step

Continue to [Modern C++ Language Features](../14_Modern_Cpp_OOP_Features/README.md) and then [Projects](../15_Projects_and_Applications/README.md).
