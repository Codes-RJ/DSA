# Bit Masks and Bit Manipulation

## Introduction
A bitmask is a string of bits (usually an integer) used to select or modify specific bits in another integer. It's an efficient way to represent and process collections of flags.

## Core Concepts

### 1. Representation of Sets
A set of elements `{0, 1, 2, ..., n-1}` can be represented by a bitmask where the `i-th` bit is 1 if the `i-th` element is in the set, and 0 otherwise.

### 2. Operations with Bitmasks

| Operation | Concept | Formula |
|-----------|---------|---------|
| **Intersection** | Both sets contain element | `mask1 & mask2` |
| **Union** | Either set contains element | `mask1 \| mask2` |
| **Difference** | `mask1` excluding `mask2` | `mask1 & (~mask2)` |
| **Check Element** | Is `i`-th bit 1? | `(mask >> i) & 1` |
| **Add Element** | Set `i`-th bit to 1 | `mask \| (1 << i)` |
| **Remove Element** | Set `i`-th bit to 0 | `mask & ~(1 << i)` |
| **Toggle Element** | Invert `i`-th bit | `mask ^ (1 << i)` |

## Examples

### Checking if a subset
```cpp
// if mask1 is a subset of mask2
if ((mask1 & mask2) == mask1) {
    // True
}
```

### Iterating through all submasks of a mask
```cpp
for (int submask = mask; submask > 0; submask = (submask - 1) & mask) {
    // Process submask
}
```

### Iterating through all possible masks (Brute Force Subsets)
```cpp
for (int i = 0; i < (1 << n); i++) {
    // Represents a subset out of 2^n possibilities
}
```

## Why use Bitmasks?
1. **Extremely Fast**: Bitwise operations are translated directly to CPU instructions.
2. **Minimal Space**: Uses a single integer to store up to 32 or 64 boolean flags.
3. **Easy Parallelism**: Operates on all 32/64 bits simultaneously.

## Applications
- Solving NP-hard problems like Traveling Salesman Problem (DP with Bitmask).
- Game states (e.g., Chess piece positions).
- Data compression and protocols.
- Graph theory (representing adjacency matrices within bits for very small graphs).
