# 01_Basic_Bit_Operations.md

## Basic Bit Operations

### Overview

Bitwise operations work directly on the binary representation of integers at the bit level. These operations are fundamental to low-level programming, embedded systems, cryptography, and performance optimization. Understanding bitwise operators allows you to write more efficient code and solve problems that are difficult or impossible with arithmetic operations alone.

---

### 1. Binary Number System

Computers store all data as binary digits (bits), where each bit is either 0 or 1.

**Bit positions (for 8-bit integer):**

| Position | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|----------|---|---|---|---|---|---|---|---|
| Value | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

**Example: 42 in binary**

```
42 = 32 + 8 + 2 = 00101010

Positions: 7 6 5 4 3 2 1 0
Bits:      0 0 1 0 1 0 1 0
Values:   128 64 32 16 8 4 2 1
          0 +0 +32+0 +8+0+2+0 = 42
```

**Printing Binary Representation:**

```cpp
#include <iostream>
#include <bitset>
using namespace std;

void printBinary(int n) {
    for (int i = 31; i >= 0; i--) {
        cout << ((n >> i) & 1);
        if (i % 4 == 0 && i != 0) cout << " ";
    }
    cout << endl;
}

int main() {
    int n = 42;
    
    cout << "Decimal: " << n << endl;
    cout << "Binary:  ";
    printBinary(n);
    
    // Using bitset (C++11)
    cout << "Bitset:  " << bitset<8>(n) << endl;
    
    return 0;
}
```

**Output:**
```
Decimal: 42
Binary:  00000000 00000000 00000000 00101010
Bitset:  00101010
```

---

### 2. Bitwise AND (&)

The AND operator results in 1 only when both bits are 1.

**Truth Table:**

| a | b | a & b |
|---|---|-------|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**Properties:**
- `x & 0 = 0`
- `x & x = x`
- `x & y = y & x` (commutative)
- `(x & y) & z = x & (y & z)` (associative)

```cpp
#include <iostream>
#include <bitset>
using namespace std;

int main() {
    int a = 5;   // 0101
    int b = 3;   // 0011
    int result = a & b;  // 0001 = 1
    
    cout << "a = " << a << " (" << bitset<4>(a) << ")" << endl;
    cout << "b = " << b << " (" << bitset<4>(b) << ")" << endl;
    cout << "a & b = " << result << " (" << bitset<4>(result) << ")" << endl;
    
    // Use of AND: Check if a number is even
    int x = 10;
    if (x & 1) {
        cout << x << " is odd" << endl;
    } else {
        cout << x << " is even" << endl;
    }
    
    // Use of AND: Masking (extract lower 4 bits)
    int value = 0x3F;  // 63 = 00111111
    int masked = value & 0x0F;  // 00001111 = 15
    cout << "Masked value: " << masked << endl;
    
    return 0;
}
```

**Output:**
```
a = 5 (0101)
b = 3 (0011)
a & b = 1 (0001)
10 is even
Masked value: 15
```

---

### 3. Bitwise OR (|)

The OR operator results in 1 when at least one bit is 1.

**Truth Table:**

| a | b | a \| b |
|---|---|-------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

**Properties:**
- `x | 0 = x`
- `x | x = x`
- `x | y = y | x` (commutative)
- `(x | y) | z = x | (y | z)` (associative)

```cpp
#include <iostream>
#include <bitset>
using namespace std;

int main() {
    int a = 5;   // 0101
    int b = 3;   // 0011
    int result = a | b;  // 0111 = 7
    
    cout << "a = " << a << " (" << bitset<4>(a) << ")" << endl;
    cout << "b = " << b << " (" << bitset<4>(b) << ")" << endl;
    cout << "a | b = " << result << " (" << bitset<4>(result) << ")" << endl;
    
    // Use of OR: Set specific bits
    int flags = 0;
    flags |= (1 << 2);  // Set bit 2
    flags |= (1 << 5);  // Set bit 5
    cout << "Flags after setting bits 2 and 5: " << bitset<8>(flags) << endl;
    
    // Use of OR: Combine flags
    int READ = 1 << 0;   // 001
    int WRITE = 1 << 1;  // 010
    int EXEC = 1 << 2;   // 100
    
    int permissions = READ | WRITE;  // 011 = 3
    cout << "Permissions: " << bitset<3>(permissions) << endl;
    
    return 0;
}
```

**Output:**
```
a = 5 (0101)
b = 3 (0011)
a | b = 7 (0111)
Flags after setting bits 2 and 5: 00100100
Permissions: 011
```

---

### 4. Bitwise XOR (^)

The XOR operator results in 1 when the bits are different.

**Truth Table:**

| a | b | a ^ b |
|---|---|-------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

**Properties:**
- `x ^ 0 = x`
- `x ^ x = 0`
- `x ^ y = y ^ x` (commutative)
- `(x ^ y) ^ z = x ^ (y ^ z)` (associative)

```cpp
#include <iostream>
#include <bitset>
using namespace std;

int main() {
    int a = 5;   // 0101
    int b = 3;   // 0011
    int result = a ^ b;  // 0110 = 6
    
    cout << "a = " << a << " (" << bitset<4>(a) << ")" << endl;
    cout << "b = " << b << " (" << bitset<4>(b) << ")" << endl;
    cout << "a ^ b = " << result << " (" << bitset<4>(result) << ")" << endl;
    
    // Property: x ^ x = 0
    int x = 42;
    cout << "x ^ x = " << (x ^ x) << endl;
    
    // Property: x ^ 0 = x
    cout << "x ^ 0 = " << (x ^ 0) << endl;
    
    // Use of XOR: Toggle bits
    int flags = 0b1010;
    flags ^= (1 << 1);  // Toggle bit 1: 1010 ^ 0010 = 1000
    cout << "After toggling bit 1: " << bitset<4>(flags) << endl;
    flags ^= (1 << 1);  // Toggle again: 1000 ^ 0010 = 1010
    cout << "After toggling again: " << bitset<4>(flags) << endl;
    
    return 0;
}
```

**Output:**
```
a = 5 (0101)
b = 3 (0011)
a ^ b = 6 (0110)
x ^ x = 0
x ^ 0 = 42
After toggling bit 1: 1000
After toggling again: 1010
```

---

### 5. Bitwise NOT (~)

The NOT operator flips all bits (0 becomes 1, 1 becomes 0).

**Truth Table:**

| a | ~a |
|---|----|
| 0 | 1 |
| 1 | 0 |

**Important:** For signed integers, NOT produces two's complement negative value.

```cpp
#include <iostream>
#include <bitset>
using namespace std;

int main() {
    int a = 5;   // ...0101
    int result = ~a;  // ...1010 (which is -6 in two's complement)
    
    cout << "a = " << a << " (" << bitset<8>(a) << ")" << endl;
    cout << "~a = " << result << " (" << bitset<8>(result) << ")" << endl;
    
    // Property: ~(~x) = x
    cout << "~(~5) = " << (~(~a)) << endl;
    
    // Use of NOT: Clear bits
    int value = 0b1111;  // 15
    int cleared = value & ~0b0011;  // Clear lowest 2 bits: 1111 & 1100 = 1100
    cout << "Cleared lower 2 bits: " << bitset<4>(cleared) << endl;
    
    // Alternative: Create mask using NOT
    int mask = ~0;  // All bits set to 1
    cout << "All bits set: " << bitset<8>(mask) << endl;
    
    return 0;
}
```

**Output:**
```
a = 5 (00000101)
~a = -6 (11111010)
~(~5) = 5
Cleared lower 2 bits: 1100
All bits set: 11111111
```

---

### 6. Left Shift (<<)

The left shift operator shifts bits to the left by the specified number of positions. Vacated bits are filled with 0.

**Effect:** `x << y` is equivalent to `x × 2ʸ`

```cpp
#include <iostream>
#include <bitset>
using namespace std;

int main() {
    int x = 5;  // 0101
    
    cout << "x = " << x << " (" << bitset<8>(x) << ")" << endl;
    
    for (int i = 1; i <= 3; i++) {
        int shifted = x << i;
        cout << "x << " << i << " = " << shifted;
        cout << " (" << bitset<8>(shifted) << ") = " << x << " × 2^" << i << endl;
    }
    
    // Use of left shift: Create powers of two
    cout << "\nPowers of two:" << endl;
    for (int i = 0; i < 8; i++) {
        cout << "2^" << i << " = " << (1 << i) << " (" << bitset<8>(1 << i) << ")" << endl;
    }
    
    // Use of left shift: Set specific bit
    int flags = 0;
    flags |= (1 << 3);  // Set bit 3
    flags |= (1 << 7);  // Set bit 7
    cout << "\nFlags with bits 3 and 7 set: " << bitset<8>(flags) << endl;
    
    return 0;
}
```

**Output:**
```
x = 5 (00000101)
x << 1 = 10 (00001010) = 5 × 2^1
x << 2 = 20 (00010100) = 5 × 2^2
x << 3 = 40 (00101000) = 5 × 2^3

Powers of two:
2^0 = 1 (00000001)
2^1 = 2 (00000010)
2^2 = 4 (00000100)
2^3 = 8 (00001000)
2^4 = 16 (00010000)
2^5 = 32 (00100000)
2^6 = 64 (01000000)
2^7 = 128 (10000000)

Flags with bits 3 and 7 set: 10001000
```

---

### 7. Right Shift (>>)

The right shift operator shifts bits to the right by the specified number of positions.

**For unsigned integers:** Vacated bits are filled with 0.

**Effect:** `x >> y` is equivalent to `x / 2ʸ` (integer division)

```cpp
#include <iostream>
#include <bitset>
using namespace std;

int main() {
    int x = 40;  // 101000
    unsigned int ux = 40;
    
    cout << "x = " << x << " (" << bitset<8>(x) << ")" << endl;
    
    for (int i = 1; i <= 3; i++) {
        int shifted = x >> i;
        cout << "x >> " << i << " = " << shifted;
        cout << " (" << bitset<8>(shifted) << ") = " << x << " / 2^" << i << endl;
    }
    
    // Right shift for negative numbers (implementation-defined for signed)
    int negative = -40;
    cout << "\nNegative number: " << negative << " (" << bitset<8>(negative) << ")" << endl;
    cout << "-40 >> 1 = " << (negative >> 1) << " (implementation-defined)" << endl;
    
    // Unsigned right shift (always logical shift)
    cout << "\nUnsigned right shift:" << endl;
    unsigned int u = 40;
    for (int i = 1; i <= 3; i++) {
        cout << "u >> " << i << " = " << (u >> i) << endl;
    }
    
    // Use of right shift: Extract bits
    int value = 0b10101010;  // 170
    int lower4 = value & 0x0F;  // Extract lower 4 bits
    int upper4 = (value >> 4) & 0x0F;  // Extract upper 4 bits
    cout << "\nOriginal: " << bitset<8>(value) << endl;
    cout << "Lower 4 bits: " << bitset<4>(lower4) << endl;
    cout << "Upper 4 bits: " << bitset<4>(upper4) << endl;
    
    return 0;
}
```

**Output:**
```
x = 40 (00101000)
x >> 1 = 20 (00010100) = 40 / 2^1
x >> 2 = 10 (00001010) = 40 / 2^2
x >> 3 = 5 (00000101) = 40 / 2^3

Negative number: -40 (11011000)
-40 >> 1 = -20 (implementation-defined)

Unsigned right shift:
u >> 1 = 20
u >> 2 = 10
u >> 3 = 5

Original: 10101010
Lower 4 bits: 1010
Upper 4 bits: 1010
```

---

### 8. Operator Precedence and Examples

Bitwise operators have lower precedence than arithmetic operators.

**Precedence (from highest to lowest):**
1. `~` (bitwise NOT)
2. `<<` `>>` (shift)
3. `&` (bitwise AND)
4. `^` (bitwise XOR)
5. `|` (bitwise OR)

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 5, b = 3, c = 2;
    
    // IMPORTANT: Use parentheses to make precedence clear
    
    // Without parentheses (unclear)
    int result1 = a & b | c;  // (a & b) | c = (1) | 2 = 3
    cout << "a & b | c = " << result1 << endl;
    
    // With parentheses (clear)
    int result2 = (a & b) | c;
    cout << "(a & b) | c = " << result2 << endl;
    
    // Shift precedence
    int result3 = a << 1 + 2;  // a << (1+2) = 5 << 3 = 40
    int result4 = (a << 1) + 2;  // (5<<1) + 2 = 10 + 2 = 12
    cout << "a << 1 + 2 = " << result3 << " (uses addition first!)" << endl;
    cout << "(a << 1) + 2 = " << result4 << endl;
    
    // Complex expression
    int x = 0b1100;  // 12
    int y = 0b1010;  // 10
    int z = 0b0110;  // 6
    
    int complex = (x & y) | (z ^ y) >> 1;
    // (1100 & 1010) = 1000 (8)
    // (0110 ^ 1010) = 1100 (12) >> 1 = 0110 (6)
    // 1000 (8) | 0110 (6) = 1110 (14)
    cout << "(x & y) | (z ^ y) >> 1 = " << complex << endl;
    
    return 0;
}
```

**Output:**
```
a & b | c = 3
(a & b) | c = 3
a << 1 + 2 = 40 (uses addition first!)
(a << 1) + 2 = 12
(x & y) | (z ^ y) >> 1 = 14
```

---

### Key Takeaways

1. **AND (&)** - Used for masking, checking even/odd
2. **OR (|)** - Used for setting bits, combining flags
3. **XOR (^)** - Used for toggling bits, finding unique elements
4. **NOT (~)** - Used for inverting bits, creating masks
5. **Left Shift (<<)** - Used for multiplying by powers of two, creating bit masks
6. **Right Shift (>>)** - Used for dividing by powers of two, extracting bits
7. **Always use parentheses** when combining bitwise operations with arithmetic

---

### Practice Questions

1. Write a function to check if a number is even using bitwise AND
2. Set the 5th bit (0-indexed) of a number to 1
3. Clear the 3rd bit of a number to 0
4. Toggle the 2nd bit of a number
5. Check if the 4th bit of a number is set
6. Compute 2^10 using left shift
7. Extract the lower 8 bits of a 32-bit integer
8. Swap two numbers without a temporary variable using XOR

---

### Next Steps

- Go to [02_Bit_Tricks.md](02_Bit_Tricks.md) for Common Bit Tricks.