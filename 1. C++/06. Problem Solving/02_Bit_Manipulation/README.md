# README.md

## Bit Manipulation - Complete Guide

### Overview

Bit manipulation involves working directly with the binary representation of numbers. It is a powerful technique for solving problems efficiently, often reducing time complexity from O(n) to O(1) or from O(n²) to O(n). Bit manipulation is essential for competitive programming, embedded systems, cryptography, and performance-critical applications.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [01_Basic_Bit_Operations.md](01_Basic_Bit_Operations.md) | understand Basic Bit Operations |
| 2. | [02_Bit_Tricks.md](02_Bit_Tricks.md) | understand Common Bit Tricks |
| 3. | [03_Bit_Masks.md](03_Bit_Masks.md) | understand Bit Masks and Subset Generation |
| 4. | [04_Binary_Representation.md](04_Binary_Representation.md) | understand Binary Representation |
| 5. | [05_Bit_Manipulation_Problems.md](05_Bit_Manipulation_Problems.md) | understand Bit Manipulation Problems |
| 6. | [README.md](README.md) | understand Bit Manipulation Overview |

---

## 1. Basic Bit Operations

This topic covers fundamental bitwise operators and their usage.

**File:** [01_Basic_Bit_Operations.md](01_Basic_Bit_Operations.md)

**What you will learn:**
- Bitwise AND (&)
- Bitwise OR (|)
- Bitwise XOR (^)
- Bitwise NOT (~)
- Left shift (<<)
- Right shift (>>)
- Operator precedence and examples

**Key Concepts:**

| Operator | Symbol | Description | Example |
|----------|--------|-------------|---------|
| **AND** | `&` | 1 if both bits are 1 | `5 & 3 = 1` (101 & 011 = 001) |
| **OR** | `\|` | 1 if at least one bit is 1 | `5 \| 3 = 7` (101 \| 011 = 111) |
| **XOR** | `^` | 1 if bits are different | `5 ^ 3 = 6` (101 ^ 011 = 110) |
| **NOT** | `~` | Flips all bits | `~5 = -6` (flips all 32 bits) |
| **Left Shift** | `<<` | Shifts bits left (multiply by 2) | `5 << 1 = 10` |
| **Right Shift** | `>>` | Shifts bits right (divide by 2) | `5 >> 1 = 2` |

**Syntax:**
```cpp
int a = 5;  // 101
int b = 3;  // 011

int andResult = a & b;    // 001 = 1
int orResult = a | b;     // 111 = 7
int xorResult = a ^ b;    // 110 = 6
int notResult = ~a;       // ...11111010 = -6
int leftShift = a << 1;   // 1010 = 10
int rightShift = a >> 1;  // 10 = 2
```

---

## 2. Common Bit Tricks

This topic covers common bit manipulation tricks and optimizations.

**File:** [02_Bit_Tricks.md](02_Bit_Tricks.md)

**What you will learn:**
- Checking if number is power of two
- Counting set bits (Brian Kernighan's algorithm)
- Isolating lowest set bit
- Clearing lowest set bit
- Swapping numbers without temporary variable
- Checking if bits are alternating

**Key Tricks:**

| Trick | Expression | Description |
|-------|------------|-------------|
| **Power of Two** | `n & (n-1) == 0` | True if n is power of two |
| **Lowest Set Bit** | `n & -n` | Isolates lowest set bit |
| **Clear Lowest Set Bit** | `n & (n-1)` | Removes lowest set bit |
| **Set bit** | `n \| (1 << k)` | Sets kth bit to 1 |
| **Clear bit** | `n & ~(1 << k)` | Sets kth bit to 0 |
| **Toggle bit** | `n ^ (1 << k)` | Flips kth bit |
| **Check bit** | `(n >> k) & 1` | Gets kth bit value |

**Syntax:**
```cpp
// Count set bits (Brian Kernighan)
int countSetBits(int n) {
    int count = 0;
    while (n) {
        n &= (n - 1);  // Clear lowest set bit
        count++;
    }
    return count;
}

// Check power of two
bool isPowerOfTwo(int n) {
    return n > 0 && (n & (n - 1)) == 0;
}

// Swap without temporary variable
void swap(int& a, int& b) {
    a ^= b;
    b ^= a;
    a ^= b;
}
```

---

## 3. Bit Masks

This topic covers using bit masks to represent sets and subsets.

**File:** [03_Bit_Masks.md](03_Bit_Masks.md)

**What you will learn:**
- Representing sets using bit masks
- Subset generation using bit masks
- Set operations (union, intersection, complement)
- Checking membership
- Iterating over subsets
- Dynamic programming with bit masks

**Key Concepts:**

| Operation | Expression | Description |
|-----------|------------|-------------|
| **Add element** | `mask \| (1 << i)` | Add i to set |
| **Remove element** | `mask & ~(1 << i)` | Remove i from set |
| **Check element** | `(mask >> i) & 1` | Check if i is in set |
| **Union** | `maskA \| maskB` | Union of two sets |
| **Intersection** | `maskA & maskB` | Intersection of two sets |
| **Complement** | `~mask` | Complement of set |

**Syntax:**
```cpp
// Generate all subsets of an array of n elements
vector<vector<int>> generateSubsets(vector<int>& arr) {
    int n = arr.size();
    vector<vector<int>> subsets;
    
    for (int mask = 0; mask < (1 << n); mask++) {
        vector<int> subset;
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) {
                subset.push_back(arr[i]);
            }
        }
        subsets.push_back(subset);
    }
    return subsets;
}

// Iterate over all submasks of a mask
int mask = 13;  // 1101
for (int sub = mask; sub; sub = (sub - 1) & mask) {
    // Process submask
}
```

---

## 4. Binary Representation

This topic covers converting numbers to binary and understanding signed representations.

**File:** [04_Binary_Representation.md](04_Binary_Representation.md)

**What you will learn:**
- Binary, octal, hexadecimal representation
- Two's complement (signed integers)
- Binary to decimal conversion
- Decimal to binary conversion
- Printing binary representation
- Endianness

**Key Concepts:**

| Representation | Base | Digits | Example |
|----------------|------|--------|---------|
| **Binary** | 2 | 0,1 | 1010₂ = 10 |
| **Octal** | 8 | 0-7 | 12₈ = 10 |
| **Hexadecimal** | 16 | 0-9,A-F | A₁₆ = 10 |

**Syntax:**
```cpp
// Print binary representation
void printBinary(int n) {
    for (int i = 31; i >= 0; i--) {
        cout << ((n >> i) & 1);
        if (i % 4 == 0) cout << " ";
    }
    cout << endl;
}

// Binary string to integer
int binaryToInt(string binary) {
    int result = 0;
    for (char c : binary) {
        result = (result << 1) | (c - '0');
    }
    return result;
}
```

---

## 5. Bit Manipulation Problems

This topic covers common interview and competitive programming problems.

**File:** [05_Bit_Manipulation_Problems.md](05_Bit_Manipulation_Problems.md)

**What you will learn:**
- Single number (find element that appears once)
- Find missing number
- Count bits in a range
- Reverse bits of a number
- Find the two non-repeating elements
- Add two numbers without using + operator

**Key Problems:**

| Problem | Solution Approach | Complexity |
|---------|-------------------|------------|
| **Single Number** | XOR all elements | O(n) |
| **Missing Number** | XOR with indices | O(n) |
| **Power of Two** | `n & (n-1) == 0` | O(1) |
| **Count Set Bits** | Brian Kernighan | O(k) |
| **Reverse Bits** | Bit by bit reversal | O(32) |

**Syntax:**
```cpp
// Single number (find element appearing once)
int singleNumber(vector<int>& nums) {
    int result = 0;
    for (int num : nums) {
        result ^= num;
    }
    return result;
}

// Add two numbers without + operator
int add(int a, int b) {
    while (b != 0) {
        int carry = a & b;
        a = a ^ b;
        b = carry << 1;
    }
    return a;
}

// Reverse bits of a 32-bit integer
uint32_t reverseBits(uint32_t n) {
    uint32_t result = 0;
    for (int i = 0; i < 32; i++) {
        result = (result << 1) | (n & 1);
        n >>= 1;
    }
    return result;
}
```

---

### Bit Manipulation Cheat Sheet

| Operation | Expression | Example (n=5, k=2) |
|-----------|------------|-------------------|
| Set kth bit | `n \| (1 << k)` | 5 | (1<<2) = 5 | 4 = 7 (111) |
| Clear kth bit | `n & ~(1 << k)` | 5 & ~4 = 5 & 3 = 1 (001) |
| Toggle kth bit | `n ^ (1 << k)` | 5 ^ 4 = 1 (001) |
| Check kth bit | `(n >> k) & 1` | (5>>2)&1 = 1&1 = 1 |
| Is power of two | `n & (n-1) == 0` | 4 & 3 = 0 → true |
| Lowest set bit | `n & -n` | 6 (110) & -6 (010) = 2 (010) |
| Clear lowest set bit | `n & (n-1)` | 6 & 5 = 4 (100) |

---

### Complexity Summary

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Basic bitwise | O(1) | O(1) |
| Count set bits (Brian Kernighan) | O(k) where k = number of set bits | O(1) |
| Reverse bits | O(32) = O(1) | O(1) |
| Subset generation | O(2ⁿ × n) | O(2ⁿ × n) |

---

### Prerequisites

Before starting this section, you should have completed:

- [01. Basics](../../01.%20Basics/README.md) - Binary numbers, operators

---

### Sample Bit Manipulation Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Problem: Find the only number that appears once in an array
int singleNumber(vector<int>& nums) {
    int result = 0;
    for (int num : nums) {
        result ^= num;
    }
    return result;
}

// Problem: Check if a number is a power of two
bool isPowerOfTwo(int n) {
    return n > 0 && (n & (n - 1)) == 0;
}

// Problem: Count the number of set bits
int countSetBits(int n) {
    int count = 0;
    while (n) {
        n &= (n - 1);
        count++;
    }
    return count;
}

int main() {
    vector<int> nums = {4, 1, 2, 1, 2};
    cout << "Single number: " << singleNumber(nums) << endl;
    
    cout << "Is 16 power of two? " << (isPowerOfTwo(16) ? "Yes" : "No") << endl;
    cout << "Is 18 power of two? " << (isPowerOfTwo(18) ? "Yes" : "No") << endl;
    
    cout << "Set bits in 13: " << countSetBits(13) << endl;
    
    return 0;
}
```

**Output:**
```
Single number: 4
Is 16 power of two? Yes
Is 18 power of two? No
Set bits in 13: 3
```

---

### Learning Path

```
Level 1: Basic Operations
├── Bitwise Operators
├── Shift Operators
└── Basic Bit Tricks

Level 2: Common Tricks
├── Power of Two Check
├── Count Set Bits
├── Isolate/Remove Lowest Bit
└── Swap without Temporary

Level 3: Bit Masks
├── Set Representation
├── Subset Generation
└── Submask Iteration

Level 4: Problem Solving
├── Single Number
├── Missing Number
├── Add without + Operator
└── Bit Manipulation Problems
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Shift beyond bit width | Limit shift to < 32 for int, < 64 for long long |
| Negative right shift behavior | Use unsigned for bit operations |
| XOR confusion | Understand XOR properties (a^a=0, a^0=a) |
| Operator precedence | Use parentheses: `(n & (n-1)) == 0` |
| Sign extension on right shift | Use `>>` for unsigned |

---

### Practice Questions

1. Check if a number is a power of two
2. Count the number of set bits in an integer
3. Find the only number that appears once in an array
4. Swap two numbers without using a temporary variable
5. Generate all subsets using bit masks
6. Reverse the bits of a 32-bit integer
7. Add two integers without using + operator
8. Find the missing number in an array of 0..n
9. Find the two non-repeating elements in an array
10. Check if a number has alternating bits

---

### Next Steps

- Go to [01_Basic_Bit_Operations.md](01_Basic_Bit_Operations.md) to understand Basic Bit Operations.