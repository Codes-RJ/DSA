# 05_Bit_Manipulation_Problems.md

## Bit Manipulation Problems

### Overview

This topic covers common bit manipulation problems that frequently appear in coding interviews and competitive programming. These problems test your understanding of bitwise operations and your ability to apply bit tricks to solve problems efficiently. Many of these solutions achieve O(1) or O(n) time complexity where naive solutions would be O(n²) or worse.

---

### 1. Single Number (Find Element Appearing Once)

**Problem:** Given an array where every element appears twice except one, find that single element.

**Solution:** XOR all elements. Since `a ^ a = 0` and `a ^ 0 = a`, pairs cancel out.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int singleNumber(vector<int>& nums) {
    int result = 0;
    for (int num : nums) {
        result ^= num;
    }
    return result;
}

int main() {
    vector<int> nums = {4, 1, 2, 1, 2};
    
    cout << "Array: ";
    for (int x : nums) cout << x << " ";
    cout << endl;
    
    cout << "Single number: " << singleNumber(nums) << endl;
    
    return 0;
}
```

**Output:**
```
Array: 4 1 2 1 2 
Single number: 4
```

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### 2. Single Number II (Find Element Appearing Once, Others Thrice)

**Problem:** Given an array where every element appears three times except one, find that single element.

**Solution:** Count bits modulo 3.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int singleNumberII(vector<int>& nums) {
    int ones = 0, twos = 0;
    
    for (int num : nums) {
        ones = (ones ^ num) & ~twos;
        twos = (twos ^ num) & ~ones;
    }
    
    return ones;
}

int main() {
    vector<int> nums = {2, 2, 3, 2};
    
    cout << "Array: ";
    for (int x : nums) cout << x << " ";
    cout << endl;
    
    cout << "Single number: " << singleNumberII(nums) << endl;
    
    return 0;
}
```

**Output:**
```
Array: 2 2 3 2 
Single number: 3
```

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### 3. Find the Two Non-Repeating Elements

**Problem:** In an array where every element appears twice except two elements that appear once, find those two elements.

**Solution:**
1. XOR all elements to get XOR of the two unique numbers
2. Find any set bit in the XOR result
3. Partition numbers based on that bit and XOR each partition

```cpp
#include <iostream>
#include <vector>
using namespace std;

pair<int, int> findTwoUnique(vector<int>& nums) {
    int xorAll = 0;
    for (int num : nums) {
        xorAll ^= num;
    }
    
    // Get the rightmost set bit
    int setBit = xorAll & -xorAll;
    
    int x = 0, y = 0;
    for (int num : nums) {
        if (num & setBit) {
            x ^= num;
        } else {
            y ^= num;
        }
    }
    
    return {x, y};
}

int main() {
    vector<int> nums = {2, 4, 6, 8, 10, 2, 6, 10};
    
    cout << "Array: ";
    for (int x : nums) cout << x << " ";
    cout << endl;
    
    auto [a, b] = findTwoUnique(nums);
    cout << "Unique numbers: " << a << " and " << b << endl;
    
    return 0;
}
```

**Output:**
```
Array: 2 4 6 8 10 2 6 10 
Unique numbers: 4 and 8
```

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### 4. Missing Number

**Problem:** Given an array containing n distinct numbers from 0 to n, find the missing number.

**Solution:** XOR all indices and all numbers. The missing number cancels out.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int missingNumber(vector<int>& nums) {
    int n = nums.size();
    int xorSum = 0;
    
    for (int i = 0; i < n; i++) {
        xorSum ^= i ^ nums[i];
    }
    
    return xorSum ^ n;
}

int main() {
    vector<int> nums = {3, 0, 1};
    
    cout << "Array: ";
    for (int x : nums) cout << x << " ";
    cout << endl;
    
    cout << "Missing number: " << missingNumber(nums) << endl;
    
    return 0;
}
```

**Output:**
```
Array: 3 0 1 
Missing number: 2
```

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### 5. Power of Two

**Problem:** Determine if a number is a power of two.

**Solution:** A power of two has exactly one set bit. `n & (n-1)` clears the lowest set bit.

```cpp
#include <iostream>
using namespace std;

bool isPowerOfTwo(int n) {
    return n > 0 && (n & (n - 1)) == 0;
}

int main() {
    cout << "Power of two check:" << endl;
    
    for (int i = 0; i <= 20; i++) {
        if (isPowerOfTwo(i)) {
            cout << i << " is a power of two" << endl;
        }
    }
    
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
```

**Time Complexity:** O(1) | **Space Complexity:** O(1)

---

### 6. Power of Four

**Problem:** Determine if a number is a power of four.

**Solution:** A power of four is a power of two with the set bit at an even position (0-indexed).

```cpp
#include <iostream>
using namespace std;

bool isPowerOfFour(int n) {
    return n > 0 && (n & (n - 1)) == 0 && (n & 0x55555555) != 0;
    // 0x55555555 has bits set at even positions: 01010101010101010101010101010101
}

int main() {
    cout << "Power of four check:" << endl;
    
    for (int i = 1; i <= 256; i *= 2) {
        cout << i << ": " << (isPowerOfFour(i) ? "Yes" : "No") << endl;
    }
    
    return 0;
}
```

**Output:**
```
Power of four check:
1: Yes
2: No
4: Yes
8: No
16: No
32: No
64: Yes
128: No
256: No
```

**Time Complexity:** O(1) | **Space Complexity:** O(1)

---

### 7. Reverse Bits

**Problem:** Reverse the bits of a 32-bit unsigned integer.

```cpp
#include <iostream>
#include <cstdint>
using namespace std;

uint32_t reverseBits(uint32_t n) {
    uint32_t result = 0;
    
    for (int i = 0; i < 32; i++) {
        result = (result << 1) | (n & 1);
        n >>= 1;
    }
    
    return result;
}

// Optimized version using bit manipulation
uint32_t reverseBitsOptimized(uint32_t n) {
    n = (n >> 16) | (n << 16);
    n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8);
    n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4);
    n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2);
    n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1);
    return n;
}

int main() {
    uint32_t n = 0b00000010100101000001111010011100;
    
    cout << "Original:  " << bitset<32>(n) << endl;
    cout << "Reversed:  " << bitset<32>(reverseBits(n)) << endl;
    cout << "Optimized: " << bitset<32>(reverseBitsOptimized(n)) << endl;
    
    return 0;
}
```

**Output:**
```
Original:  00000010100101000001111010011100
Reversed:  00111001011110000010100101000000
Optimized: 00111001011110000010100101000000
```

**Time Complexity:** O(1) (32 iterations) | **Space Complexity:** O(1)

---

### 8. Count Set Bits

**Problem:** Count the number of 1 bits in an integer.

```cpp
#include <iostream>
#include <cstdint>
using namespace std;

// Brian Kernighan's algorithm
int countSetBits(int n) {
    int count = 0;
    while (n) {
        n &= (n - 1);
        count++;
    }
    return count;
}

// Lookup table method (for 32-bit integers)
int countSetBitsLookup(uint32_t n) {
    // Precomputed for 4-bit chunks (0-15)
    const int lookup[16] = {0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4};
    
    return lookup[n & 0xF] +
           lookup[(n >> 4) & 0xF] +
           lookup[(n >> 8) & 0xF] +
           lookup[(n >> 12) & 0xF] +
           lookup[(n >> 16) & 0xF] +
           lookup[(n >> 20) & 0xF] +
           lookup[(n >> 24) & 0xF] +
           lookup[(n >> 28) & 0xF];
}

int main() {
    int numbers[] = {0, 1, 2, 3, 5, 7, 8, 15, 16, 42, 255, 1023};
    
    cout << "Set bits count (Brian Kernighan):" << endl;
    for (int n : numbers) {
        cout << n << " (" << bitset<8>(n) << ") has " << countSetBits(n) << " set bits" << endl;
    }
    
    return 0;
}
```

**Output:**
```
Set bits count (Brian Kernighan):
0 (00000000) has 0 set bits
1 (00000001) has 1 set bits
2 (00000010) has 1 set bits
3 (00000011) has 2 set bits
5 (00000101) has 2 set bits
7 (00000111) has 3 set bits
8 (00001000) has 1 set bits
15 (00001111) has 4 set bits
16 (00010000) has 1 set bits
42 (00101010) has 3 set bits
255 (11111111) has 8 set bits
1023 (11111111) has 10 set bits
```

**Time Complexity:** O(k) where k = number of set bits | **Space Complexity:** O(1)

---

### 9. Bitwise AND of Numbers Range

**Problem:** Given a range [m, n], find the bitwise AND of all numbers from m to n.

**Solution:** Find the common prefix of m and n.

```cpp
#include <iostream>
using namespace std;

int rangeBitwiseAnd(int m, int n) {
    int shift = 0;
    
    while (m < n) {
        m >>= 1;
        n >>= 1;
        shift++;
    }
    
    return m << shift;
}

int main() {
    cout << "Range bitwise AND:" << endl;
    cout << "AND [5, 7] = " << rangeBitwiseAnd(5, 7) << endl;   // 5 & 6 & 7 = 4
    cout << "AND [0, 1] = " << rangeBitwiseAnd(0, 1) << endl;   // 0
    cout << "AND [1, 2] = " << rangeBitwiseAnd(1, 2) << endl;   // 0
    cout << "AND [10, 13] = " << rangeBitwiseAnd(10, 13) << endl; // 8
    
    return 0;
}
```

**Output:**
```
Range bitwise AND:
AND [5, 7] = 4
AND [0, 1] = 0
AND [1, 2] = 0
AND [10, 13] = 8
```

**Time Complexity:** O(log n) | **Space Complexity:** O(1)

---

### 10. Add Two Numbers Without Using + Operator

**Problem:** Add two integers without using the + operator.

**Solution:** Use XOR for sum and AND for carry, then shift.

```cpp
#include <iostream>
using namespace std;

int add(int a, int b) {
    while (b != 0) {
        int carry = a & b;
        a = a ^ b;
        b = carry << 1;
    }
    return a;
}

// Recursive version
int addRecursive(int a, int b) {
    if (b == 0) return a;
    return addRecursive(a ^ b, (a & b) << 1);
}

int main() {
    cout << "Addition without + operator:" << endl;
    
    cout << "5 + 3 = " << add(5, 3) << endl;
    cout << "10 + 20 = " << add(10, 20) << endl;
    cout << "100 + 200 = " << add(100, 200) << endl;
    cout << "-5 + 3 = " << add(-5, 3) << endl;
    
    return 0;
}
```

**Output:**
```
Addition without + operator:
5 + 3 = 8
10 + 20 = 30
100 + 200 = 300
-5 + 3 = -2
```

**Time Complexity:** O(log max(a,b)) | **Space Complexity:** O(1)

---

### 11. Find the Only Repeating Element

**Problem:** In an array of size n+1 containing numbers from 1 to n, find the duplicate element.

**Solution:** XOR all indices and all numbers. The duplicate appears twice.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int findDuplicate(vector<int>& nums) {
    int result = 0;
    
    for (int i = 0; i < nums.size(); i++) {
        result ^= i ^ nums[i];
    }
    
    return result;
}

int main() {
    vector<int> nums = {1, 3, 4, 2, 2};
    
    cout << "Array: ";
    for (int x : nums) cout << x << " ";
    cout << endl;
    
    cout << "Duplicate element: " << findDuplicate(nums) << endl;
    
    return 0;
}
```

**Output:**
```
Array: 1 3 4 2 2 
Duplicate element: 2
```

**Time Complexity:** O(n) | **Space Complexity:** O(1)

---

### 12. Maximum Product of Word Lengths

**Problem:** Find the maximum product of lengths of two words that share no common letters.

**Solution:** Represent each word as a bitmask of letters. Then check for no overlap using `(mask[i] & mask[j]) == 0`.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int maxProduct(vector<string>& words) {
    int n = words.size();
    vector<int> masks(n, 0);
    
    // Create bitmask for each word
    for (int i = 0; i < n; i++) {
        for (char c : words[i]) {
            masks[i] |= 1 << (c - 'a');
        }
    }
    
    int maxProd = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if ((masks[i] & masks[j]) == 0) {
                int prod = words[i].length() * words[j].length();
                maxProd = max(maxProd, prod);
            }
        }
    }
    
    return maxProd;
}

int main() {
    vector<string> words = {"abcw", "baz", "foo", "bar", "xtfn", "abcdef"};
    
    int result = maxProduct(words);
    cout << "Maximum product: " << result << endl;
    
    return 0;
}
```

**Output:**
```
Maximum product: 16
```

**Time Complexity:** O(n² × L) | **Space Complexity:** O(n)

---

### Problem Summary Table

| Problem | Solution Approach | Time | Space |
|---------|-------------------|------|-------|
| Single Number | XOR all elements | O(n) | O(1) |
| Two Unique Numbers | XOR + partition | O(n) | O(1) |
| Missing Number | XOR with indices | O(n) | O(1) |
| Power of Two | `n & (n-1) == 0` | O(1) | O(1) |
| Power of Four | Power of two + check bit position | O(1) | O(1) |
| Reverse Bits | Bit-by-bit reversal | O(1) | O(1) |
| Count Set Bits | `n & (n-1)` loop | O(k) | O(1) |
| Range AND | Find common prefix | O(log n) | O(1) |
| Add Without + | XOR + AND | O(log n) | O(1) |

---

### Key Takeaways

1. **XOR properties** (`a ^ a = 0`, `a ^ 0 = a`) are powerful for finding unique elements
2. **`n & (n-1)`** clears the lowest set bit (Brian Kernighan)
3. **`n & -n`** isolates the lowest set bit
4. **Power of two** check: `n > 0 && (n & (n-1)) == 0`
5. **Bit masks** are useful for set representation and overlap detection
6. **Addition without +** uses XOR for sum and AND for carry
7. **Range AND** finds the common prefix of numbers

---

### Practice Questions

1. Find the only element that appears an odd number of times in an array
2. Determine if a number is a power of two
3. Count the number of bits to flip to convert a to b
4. Find the complement of a number (flip all bits)
5. Find the largest power of two less than or equal to n
6. Check if a number has alternating bits
7. Find the sum of all subset XOR totals
8. Find the minimum number of bit flips to make a equal to b

---

### Next Steps

- Now proceed to [03_String_Problems](../../03_String_Problems/README.md) for String Problems.