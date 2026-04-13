# Number Puzzles

## Introduction
Number puzzles focus on the properties of integers, arithmetic, and mathematical induction.

## 1. Tower of Hanoi
**Question**: Move a stack of `n` disks from one rod to another using a third rod, following specific rules (only one disk at a time, no larger disk on a smaller disk).
- **Solution**: Recursive. `Move(n) = 2^n - 1` steps.

## 2. Josephus Problem
**Question**: People stand in a circle. Every `k`-th person is eliminated until only one survives.
- **Solution**: 
  `J(n, k) = (J(n-1, k) + k) % n` with `J(1, k) = 0`.

## 3. Missing Number in Range [1, N]
**Question**: An array contains `n-1` distinct integers in range `[1, n]`.
- **Solution 1 (Sum)**: `Expected_Sum(n*(n+1) / 2) - Actual_Sum`.
- **Solution 2 (XOR)**: `XOR(1...n) ^ XOR(arr_elements)`.

## 4. Water Jug Problem
**Question**: Measure exactly `d` liters of water using two jugs of capacity `m` and `n`.
- **Solution**: Possible only if `d % gcd(m, n) == 0`.

## 5. Happy Number
**Question**: Replace a number with the sum of squares of its digits repeatdly. If you reach 1, it is happy.
- **Solution**: Use cycle detection (Floyd's Tortoise and Hare) to avoid infinite loops.

## Core Topics
- **Prime Properties**: Generating primes (Sieve of Eratosthenes).
- **Digit Manipulation**: Reversing, sum of digits, Palindrome numbers.
- **Factorial Trailing Zeros**: Count multiples of 5, 25, 125, etc.
- **Divisibility Rules**: Sum of digits (for 3 and 9), last 2 digits (for 4).

## Summary
Number puzzles are effective for building mathematical intuition and performance optimizing through algebraic shortcuts.
---

## Next Step

- Go to [04_Array_Puzzles.md](04_Array_Puzzles.md) to continue with Array Puzzles.
