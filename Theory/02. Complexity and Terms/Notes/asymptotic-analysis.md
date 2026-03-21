# Asymptotic Analysis

Asymptotic analysis focuses on growth rate, not exact runtime in seconds.

## Why It Matters

Two correct solutions can behave very differently for large inputs.

## Complexity Classes

- `O(1)`: constant work
- `O(log n)`: repeatedly halves the search space
- `O(n)`: scans input once
- `O(n log n)`: typical efficient comparison sorting
- `O(n^2)`: nested loops over the same input

## Best, Average, Worst Case

- best case: most favorable input
- average case: expected behavior
- worst case: maximum cost among valid inputs

## Interview Rule

If constraints allow only around `10^5` or `10^6` operations, an `O(n^2)` solution is usually too slow.
