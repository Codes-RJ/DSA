# Series and Summations

## Introduction
Problems often require calculating the sum of a sequence of numbers (Arithmetic Progression, Geometric Progression, etc.).

## Arithmetic Progression (AP)
A sequence where the difference between any two consecutive terms is constant.
`Sum = n/2 * (2a + (n-1)d)` or `Sum = n/2 * (first + last)`

## Geometric Progression (GP)
A sequence where each term after the first is found by multiplying the previous term by a fixed, non-zero number called the common ratio.
`Sum = a(r^n - 1) / (r - 1)` for `r > 1`
`Sum = a(1 - r^n) / (1 - r)` for `r < 1`

## Common Summations
1. **First n natural numbers**: `n(n+1) / 2`
2. **First n squares**: `n(n+1)(2n+1) / 6`
3. **First n cubes**: `[n(n+1) / 2]^2`
4. **Sum of even numbers up to 2n**: `n(n+1)`
5. **Sum of odd numbers up to 2n-1**: `n^2`

## Harmonic Series
The sum of reciprocal of integers: `1 + 1/2 + 1/3 + ... + 1/n ≈ ln(n) + γ` (where γ is Euler's constant).
- Grows very slowly (logarithmically).

## Fibonacci Series
`F(n) = F(n-1) + F(n-2)` with `F(0) = 0`, `F(1) = 1`.
- **Closed-form (Binet's Formula)**: `F(n) = (φ^n - ψ^n) / √5` where φ is the golden ratio.
- **Sum of first n Fibonacci**: `Sum(F_i) = F(n+2) - 1`.

## Time and Space Complexity
- Formulas are O(1) Time and Space.
- Iterative calculation is O(n) Time.
- Matrix Exponentiation for Fibonacci/Linear Recurrences is O(log n) Time.
---

## Next Step

- Go to [README.md](README.md) to continue.
