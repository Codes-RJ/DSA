# 02_Bit_Tricks.md

## Common Bit Tricks

### Overview

Bit tricks are clever techniques that use bitwise operations to solve problems efficiently. These tricks often replace loops or complex arithmetic with single bitwise operations, dramatically improving performance. Mastering these tricks is essential for competitive programming, low-level optimization, and technical interviews.

---

### 1. Check if Number is Power of Two

A number is a power of two if it has exactly one bit set.

**Trick:** `n & (n - 1) == 0` (for n > 0)

**Explanation:** Subtracting 1 from a power of two flips all bits after the set bit.

```
n     = 16 = 10000
n-1   = 15 = 01111
n & (n-1) = 00000 = 0
```

```cpp
#include <iostream>
using namespace std;

bool isPowerOfTwo(int n) {
    return n > 0 && (n & (n - 1)) == 0;
}

int main() {
    cout << "Power of two check:" << endl;
    
    for (int i = 1; i <= 20; i++) {
        if (isPowerOfTwo(i)) {
            cout << i << " is a power of two" << endl;
        }
    }
    
    // Test edge cases
    cout << "\n0 is power of two? " << (isPowerOfTwo(0) ? "Yes" : "No") << endl;
    cout << "1 is power of two? " << (isPowerOfTwo(1) ? "Yes" : "No") << endl;
    cout << "1024 is power of two? " << (isPowerOfTwo(1024) ? "Yes" : "No") << endl;
    
    return 0;
}
```

**Output:**
```
Power of two check:
1 is a power of two
2 is a power of two
4 is a power of two
8 is a power of two
16 is a power of two

0 is power of two? No
1 is power of two? Yes
1024 is power of two? Yes
```

---

### 2. Count Set Bits (Brian Kernighan's Algorithm)

Brian Kernighan's algorithm iteratively clears the lowest set bit until the number becomes zero.

**Trick:** `n = n & (n - 1)` clears the lowest set bit.

```cpp
#include <iostream>
using namespace std;

// Brian Kernighan's algorithm
int countSetBits(int n) {
    int count = 0;
    while (n) {
        n &= (n - 1);  // Clear lowest set bit
        count++;
    }
    return count;
}

// Alternative: Built-in function (if available)
int countSetBitsBuiltin(int n) {
    return __builtin_popcount(n);  // GCC/Clang only
}

// For long long
int countSetBitsLong(long long n) {
    return __builtin_popcountll(n);
}

int main() {
    cout << "Set bits count (Brian Kernighan):" << endl;
    
    int numbers[] = {0, 1, 2, 3, 5, 7, 8, 15, 16, 255, 1023};
    
    for (int n : numbers) {
        cout << n << " (binary: ";
        for (int i = 7; i >= 0; i--) {
            cout << ((n >> i) & 1);
        }
        cout << ") has " << countSetBits(n) << " set bits" << endl;
    }
    
    return 0;
}
```

**Output:**
```
Set bits count (Brian Kernighan):
0 (binary: 00000000) has 0 set bits
1 (binary: 00000001) has 1 set bits
2 (binary: 00000010) has 1 set bits
3 (binary: 00000011) has 2 set bits
5 (binary: 00000101) has 2 set bits
7 (binary: 00000111) has 3 set bits
8 (binary: 00001000) has 1 set bits
15 (binary: 00001111) has 4 set bits
16 (binary: 00010000) has 1 set bits
255 (binary: 11111111) has 8 set bits
1023 (binary: 11111111) has 10 set bits
```

---

### 3. Isolate Lowest Set Bit

The expression `x & -x` isolates the lowest set bit.

**Explanation:** In two's complement, `-x = ~x + 1`. ANDing with original isolates the lowest set bit.

```cpp
#include <iostream>
#include <bitset>
using namespace std;

int lowestSetBit(int n) {
    return n & -n;
}

int main() {
    cout << "Isolating lowest set bit:" << endl;
    
    int numbers[] = {6, 10, 12, 14, 20, 40, 48};
    
    for (int n : numbers) {
        int lowest = lowestSetBit(n);
        cout << n << " (" << bitset<8>(n) << ") -> ";
        cout << "lowest set bit = " << lowest;
        cout << " (" << bitset<8>(lowest) << ")" << endl;
    }
    
    return 0;
}
```

**Output:**
```
Isolating lowest set bit:
6 (00000110) -> lowest set bit = 2 (00000010)
10 (00001010) -> lowest set bit = 2 (00000010)
12 (00001100) -> lowest set bit = 4 (00000100)
14 (00001110) -> lowest set bit = 2 (00000010)
20 (00010100) -> lowest set bit = 4 (00000100)
40 (00101000) -> lowest set bit = 8 (00001000)
48 (00110000) -> lowest set bit = 16 (00010000)
```

---

### 4. Clear Lowest Set Bit

The expression `n & (n - 1)` clears the lowest set bit.

```cpp
#include <iostream>
#include <bitset>
using namespace std;

int clearLowestSetBit(int n) {
    return n & (n - 1);
}

int main() {
    cout << "Clearing lowest set bit:" << endl;
    
    int n = 42;  // 00101010
    
    while (n) {
        cout << n << " (" << bitset<8>(n) << ") -> ";
        n = clearLowestSetBit(n);
        cout << "cleared -> " << n << " (" << bitset<8>(n) << ")" << endl;
    }
    
    return 0;
}
```

**Output:**
```
Clearing lowest set bit:
42 (00101010) -> cleared -> 40 (00101000)
40 (00101000) -> cleared -> 32 (00100000)
32 (00100000) -> cleared -> 0 (00000000)
```

---

### 5. Get Position of Lowest Set Bit

Find the index (0-based) of the lowest set bit.

```cpp
#include <iostream>
using namespace std;

int getLowestSetBitPosition(int n) {
    if (n == 0) return -1;
    return __builtin_ctz(n);  // Count trailing zeros (GCC/Clang)
}

// Manual implementation
int lowestSetBitPositionManual(int n) {
    if (n == 0) return -1;
    int pos = 0;
    while ((n & 1) == 0) {
        n >>= 1;
        pos++;
    }
    return pos;
}

int main() {
    cout << "Position of lowest set bit (0-indexed):" << endl;
    
    int numbers[] = {1, 2, 4, 8, 16, 6, 10, 12, 14};
    
    for (int n : numbers) {
        int pos = lowestSetBitPositionManual(n);
        cout << n << " -> lowest set bit at position " << pos << endl;
    }
    
    return 0;
}
```

**Output:**
```
Position of lowest set bit (0-indexed):
1 -> lowest set bit at position 0
2 -> lowest set bit at position 1
4 -> lowest set bit at position 2
8 -> lowest set bit at position 3
16 -> lowest set bit at position 4
6 -> lowest set bit at position 1
10 -> lowest set bit at position 1
12 -> lowest set bit at position 2
14 -> lowest set bit at position 1
```

---

### 6. Check if Two Numbers Have Opposite Signs

The XOR of two numbers is negative if they have opposite signs.

**Trick:** `(x ^ y) < 0`

```cpp
#include <iostream>
using namespace std;

bool haveOppositeSigns(int x, int y) {
    return (x ^ y) < 0;
}

int main() {
    cout << "Check opposite signs:" << endl;
    
    cout << "5 and 10: " << (haveOppositeSigns(5, 10) ? "Opposite" : "Same") << endl;
    cout << "5 and -10: " << (haveOppositeSigns(5, -10) ? "Opposite" : "Same") << endl;
    cout << "-5 and 10: " << (haveOppositeSigns(-5, 10) ? "Opposite" : "Same") << endl;
    cout << "-5 and -10: " << (haveOppositeSigns(-5, -10) ? "Opposite" : "Same") << endl;
    cout << "0 and 5: " << (haveOppositeSigns(0, 5) ? "Opposite" : "Same") << endl;
    
    return 0;
}
```

**Output:**
```
Check opposite signs:
5 and 10: Same
5 and -10: Opposite
-5 and 10: Opposite
-5 and -10: Same
0 and 5: Same
```

---

### 7. Compute Absolute Value Without Branching

Absolute value without using conditionals.

**Trick:** `(x ^ (x >> 31)) - (x >> 31)` for 32-bit integers

```cpp
#include <iostream>
using namespace std;

int absValue(int x) {
    int mask = x >> 31;
    return (x ^ mask) - mask;
}

int main() {
    cout << "Absolute value (branchless):" << endl;
    
    int numbers[] = {5, -5, 0, 10, -10, -100, 100};
    
    for (int n : numbers) {
        cout << "abs(" << n << ") = " << absValue(n) << endl;
    }
    
    return 0;
}
```

**Output:**
```
Absolute value (branchless):
abs(5) = 5
abs(-5) = 5
abs(0) = 0
abs(10) = 10
abs(-10) = 10
abs(-100) = 100
abs(100) = 100
```

---

### 8. Swap Two Numbers Without Temporary Variable

Using XOR to swap values without a temporary variable.

```cpp
#include <iostream>
using namespace std;

void swapXOR(int& a, int& b) {
    if (&a != &b) {  // Avoid self-swap
        a ^= b;
        b ^= a;
        a ^= b;
    }
}

int main() {
    cout << "Swapping using XOR:" << endl;
    
    int x = 5, y = 10;
    cout << "Before: x = " << x << ", y = " << y << endl;
    
    swapXOR(x, y);
    cout << "After:  x = " << x << ", y = " << y << endl;
    
    // Self-swap (no change)
    swapXOR(x, x);
    cout << "Self-swap: x = " << x << endl;
    
    return 0;
}
```

**Output:**
```
Swapping using XOR:
Before: x = 5, y = 10
After:  x = 10, y = 5
Self-swap: x = 10
```

---

### 9. Check if Number is Odd or Even

The least significant bit indicates parity.

```cpp
#include <iostream>
using namespace std;

bool isEven(int n) {
    return (n & 1) == 0;
}

bool isOdd(int n) {
    return (n & 1) != 0;
}

int main() {
    cout << "Parity check using bitwise AND:" << endl;
    
    for (int i = 0; i <= 10; i++) {
        cout << i << " is " << (isEven(i) ? "even" : "odd") << endl;
    }
    
    return 0;
}
```

**Output:**
```
Parity check using bitwise AND:
0 is even
1 is odd
2 is even
3 is odd
4 is even
5 is odd
6 is even
7 is odd
8 is even
9 is odd
10 is even
```

---

### 10. Turn Off the Rightmost 1 Bit

Clearing the lowest set bit (same as Brian Kernighan).

```cpp
#include <iostream>
#include <bitset>
using namespace std;

int turnOffLowestSetBit(int n) {
    return n & (n - 1);
}

int main() {
    int n = 42;  // 00101010
    
    cout << "Turning off rightmost 1 bit repeatedly:" << endl;
    
    while (n) {
        cout << n << " (" << bitset<8>(n) << ")" << endl;
        n = turnOffLowestSetBit(n);
    }
    cout << "0 (00000000)" << endl;
    
    return 0;
}
```

---

### 11. Turn On the Rightmost 0 Bit

Setting the lowest zero bit to 1.

**Trick:** `n | (n + 1)`

```cpp
#include <iostream>
#include <bitset>
using namespace std;

int turnOnLowestZeroBit(int n) {
    return n | (n + 1);
}

int main() {
    int numbers[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    cout << "Turning on rightmost 0 bit:" << endl;
    
    for (int n : numbers) {
        int result = turnOnLowestZeroBit(n);
        cout << n << " (" << bitset<8>(n) << ") -> ";
        cout << result << " (" << bitset<8>(result) << ")" << endl;
    }
    
    return 0;
}
```

**Output:**
```
Turning on rightmost 0 bit:
0 (00000000) -> 1 (00000001)
1 (00000001) -> 3 (00000011)
2 (00000010) -> 3 (00000011)
3 (00000011) -> 7 (00000111)
4 (00000100) -> 5 (00000101)
5 (00000101) -> 7 (00000111)
6 (00000110) -> 7 (00000111)
7 (00000111) -> 15 (00001111)
8 (00001000) -> 9 (00001001)
9 (00001001) -> 11 (00001011)
10 (00001010) -> 11 (00001011)
```

---

### 12. Check if Two Numbers are Equal Without Comparison

Using XOR to check equality.

```cpp
#include <iostream>
using namespace std;

bool areEqual(int a, int b) {
    return (a ^ b) == 0;
}

int main() {
    cout << "Equality check using XOR:" << endl;
    
    cout << "5 and 5: " << (areEqual(5, 5) ? "Equal" : "Not equal") << endl;
    cout << "5 and 10: " << (areEqual(5, 10) ? "Equal" : "Not equal") << endl;
    cout << "10 and 10: " << (areEqual(10, 10) ? "Equal" : "Not equal") << endl;
    
    return 0;
}
```

---

### Bit Tricks Cheat Sheet

| Trick | Expression | Description |
|-------|------------|-------------|
| Power of two | `n & (n-1) == 0` | Check if n is power of two |
| Lowest set bit | `n & -n` | Isolate lowest set bit |
| Clear lowest set bit | `n & (n-1)` | Remove lowest set bit |
| Count set bits | `while(n) { n &= n-1; count++; }` | Brian Kernighan's algorithm |
| Opposite signs | `(x ^ y) < 0` | Check if signs are opposite |
| Absolute value | `(x ^ (x>>31)) - (x>>31)` | Compute abs without branch |
| Swap with XOR | `a ^= b; b ^= a; a ^= b;` | Swap without temp |
| Odd/Even | `n & 1` | Check parity |
| Turn on lowest zero bit | `n \| (n+1)` | Set lowest 0 to 1 |
| Turn off lowest one bit | `n & (n-1)` | Set lowest 1 to 0 |
| Equality without comparison | `(a ^ b) == 0` | Check equality using XOR |

---

### Key Takeaways

1. **`n & (n-1)`** clears the lowest set bit
2. **`n & -n`** isolates the lowest set bit
3. **`(n & (n-1)) == 0`** checks if n is a power of two
4. **`x ^ y < 0`** checks if x and y have opposite signs
5. **XOR swap** works without a temporary variable
6. **Brian Kernighan's algorithm** counts set bits efficiently
7. **Bit tricks** often replace loops with single operations

---

### Practice Questions

1. Write a function to count set bits using Brian Kernighan's algorithm
2. Check if a number is a power of two without using any loops
3. Find the position of the lowest set bit
4. Swap two numbers without using a temporary variable
5. Compute the absolute value without using conditionals
6. Turn off the lowest set bit of a number
7. Turn on the lowest zero bit of a number
8. Check if two numbers have opposite signs

---

### Next Steps

- Go to [03_Bit_Masks.md](03_Bit_Masks.md) for Bit Masks.