# Binary Representation

## Introduction
Binary representation is the way data is stored in computers using only two digits: 0 and 1. Understanding how integers are represented is crucial for low-level programming and bitwise manipulation.

## Integer Representations

### 1. Unsigned Representation
Straightforward binary where each bit represents a power of 2.
- Range for `n` bits: `0 to 2^n - 1`.

### 2. Two's Complement (Signed)
The most common way to represent signed integers.
- The leading bit is the **sign bit** (1 for negative, 0 for positive).
- **Calculation for -x**: Invert all bits of `x` and add 1.
- Range for `n` bits: `-2^(n-1) to 2^(n-1) - 1`.

## Bit Ordering

### 1. Big Endian
The most significant byte is stored at the lowest memory address.

### 2. Little Endian
The least significant byte is stored at the lowest memory address (X86 architecture standard).

## C++ Tools for Binary

### 1. `std::bitset`
Convenient way to print and manipulate bit sequences as strings of 0s and 1s.
```cpp
#include <bitset>
#include <iostream>

int main() {
    std::bitset<8> b(42); 
    std::cout << b; // prints "00101010"
    return 0;
}
```

### 2. Built-in Compiler Intrinsics (GCC)
- `__builtin_popcount(x)`: Number of set bits.
- `__builtin_clz(x)`: Number of leading zeros.
- `__builtin_ctz(x)`: Number of trailing zeros.
- `__builtin_ffs(x)`: Index of first set bit.

## Decimal to Binary (Manual Method)
Keep dividing the number by 2 and recording the remainder. The bits are recorded in reverse order of discovery.

## Binary to Decimal
Sum the powers of 2 for every bit that is 1.
`Sum = Σ (bit_i * 2^i)`

## Space and Time Efficiency
Computers process binary data natively. Converting to binary for operations (shifts, masks) can reduce complex operations (multiplication, modulo) to simple, fast instructions.
---

## Next Step

- Go to [05_Bit_Manipulation_Problems.md](05_Bit_Manipulation_Problems.md) to continue with Bit Manipulation Problems.
