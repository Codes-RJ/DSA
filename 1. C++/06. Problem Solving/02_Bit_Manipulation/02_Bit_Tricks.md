# Bit Manipulation Tricks

## Introduction
Bit manipulation allows us to perform operations at a very low level, directly on bits, leading to extremely fast and memory-efficient algorithms.

## Common Operations

### 1. Parity Check (Odd/Even)
- `(n & 1)` is 1 if `n` is odd, 0 if even.

### 2. Multiply and Divide by 2
- `n << 1` → Multiply by 2.
- `n >> 1` → Divide by 2.

### 3. Swap Two Numbers (Without Temporary Variable)
```cpp
a ^= b;
b ^= a;
a ^= b;
```

### 4. Check if Power of Two
A power of two has only one bit set.
- `(n > 0) && (n & (n - 1)) == 0` is true if `n` is a power of 2.

### 5. Clear the Last Set Bit
- `n & (n - 1)` removes the least significant bit that is 1.

### 6. Extract the Lowest Set Bit
- `n & (-n)` isolating the rightmost 1-bit.

### 7. Absolute Value (Without Conditonal)
```cpp
int sign = n >> (sizeof(int) * 8 - 1);
int abs_n = (n + sign) ^ sign;
```

### 8. Lowercase to Uppercase and Vice-Versa
- **Upper to Lower**: `char lower = upper | 32;` (or `' '`)
- **Lower to Upper**: `char upper = lower & ~32;` (or `'_'`)

## Key Tips
- Bitwise operations have lower precedence than arithmetic/comparison ones. **Always use parentheses**.
- Use `1LL << n` for bit shifts involving `long long` integers.
- Built-in functions like `__builtin_popcount(n)` in GCC are optimized for counting set bits.

## Applications
- Competitive programming (performance optimization).
- Graphics and compression.
- State machines.
- Memory-efficient data structures.
