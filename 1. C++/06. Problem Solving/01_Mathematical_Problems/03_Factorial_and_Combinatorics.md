# Factorial and Combinatorics

## Introduction
Factorial and combinatorics are foundational in calculating possibilities and permutations for various problem-solving tasks.

## Factorial (n!)
The factorial of a non-negative integer `n` is the product of all positive integers less than or equal to `n`.
`n! = n * (n-1) * (n-2) * ... * 1`

### C++ Implementation (Recursive)
```cpp
long long factorial(int n) {
    if (n == 0 || n == 1) return 1;
    return n * factorial(n - 1);
}
```

### C++ Implementation (Iterative)
```cpp
long long factorial(int n) {
    long long res = 1;
    for (int i = 2; i <= n; i++) res *= i;
    return res;
}
```

## Permutations (nPr)
Permutations refer to the arrangement of `r` objects from a set of `n` objects where the order matters.
`nPr = n! / (n - r)!`

## Combinations (nCr)
Combinations refer to the selection of `r` objects from a set of `n` objects where order does not matter.
`nCr = n! / (r! * (n - r)!)`

### Pascal's Triangle Property (Efficiency)
`nCr = (n-1)Cr + (n-1)C(r-1)`

### Efficient nCr Code
```cpp
long long nCr(int n, int r) {
    if (r > n) return 0;
    if (r == 0 || r == n) return 1;
    if (r > n / 2) r = n - r; // Symmetry property nCr = nC(n-r)

    long long res = 1;
    for (int i = 1; i <= r; i++) {
        res = res * (n - i + 1) / i;
    }
    return res;
}
```

## Key Topics
- **Pigeonhole Principle**: If `n` items are put into `m` containers and `n > m`, then at least one container must contain more than one item.
- **Catalan Numbers**: Sequence of natural numbers that occur in various counting problems (e.g., number of binary search trees with `n` nodes).
- **Inclusion-Exclusion Principle**: Calculating the size of the union of multiple sets.

## Time and Space Complexity
- **Iterative Factorial**: O(n) Time, O(1) Space.
- **nCr calculation**: O(r) Time, O(1) Space.
