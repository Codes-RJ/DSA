# Bit Manipulation Problems: From Basic to Expert

## Introduction
Bit manipulation problems often have "magical" $O(1)$ or $O(N)$ solutions that bypass traditional loops and conditions. This guide covers the most common patterns and advanced challenges.

---

## 1. The Unique Element Saga

### Problem: Find the only non-repeating element (Others repeat twice)
**Solution**: XOR all elements. Since $x \oplus x = 0$ and $x \oplus 0 = x$.
```cpp
int findSingle(vector<int>& arr) {
    int res = 0;
    for (int x : arr) res ^= x;
    return res;
}
```

### Problem: Find TWO non-repeating elements (Others repeat twice)
**Solution**:
1. XOR all $\to$ result is $X \oplus Y$.
2. Find the rightmost set bit in $X \oplus Y$. This bit must be different in $X$ and $Y$.
3. Divide elements into two groups based on this bit and XOR each group.
```cpp
pair<int, int> findTwoSingles(vector<int>& arr) {
    int xorSum = 0;
    for (int x : arr) xorSum ^= x;
    
    int rightmostBit = xorSum & -xorSum; // Isolates the rightmost set bit
    int x = 0, y = 0;
    for (int num : arr) {
        if (num & rightmostBit) x ^= num;
        else y ^= num;
    }
    return {x, y};
}
```

### Problem: Find the single element (Others repeat THRICE)
**Solution**: Sum the bits at each position. If a bit sum is not divisible by 3, that bit belongs to the single element.
```cpp
int findSingleThrice(vector<int>& arr) {
    int result = 0;
    for (int i = 0; i < 32; i++) {
        int sum = 0;
        for (int x : arr) {
            if (x & (1 << i)) sum++;
        }
        if (sum % 3 != 0) result |= (1 << i);
    }
    return result;
}
```

---

## 2. Power Set Generation (Subsets)
Generate all $2^n$ subsets of a set using bitmasks.
```cpp
void generateSubsets(vector<int>& set) {
    int n = set.size();
    for (int i = 0; i < (1 << n); i++) {
        cout << "{ ";
        for (int j = 0; j < n; j++) {
            if (i & (1 << j)) cout << set[j] << " ";
        }
        cout << "}" << endl;
    }
}
```

---

## 3. Advanced Bit Tricks

### Maximum XOR Subarray
Given an array, find the maximum XOR sum of any contiguous subarray.
- **Strategy**: Similar to 1D prefix sum. Use a **Trie** to store prefix XORs and find the best match for each element.

### Gray Code Generation
A sequence of $2^n$ binary strings where two successive values differ in only one bit position.
- **Formula**: $G(i) = i \oplus (i >> 1)$.
```cpp
vector<int> generateGrayCode(int n) {
    vector<int> res;
    for (int i = 0; i < (1 << n); i++) {
        res.push_back(i ^ (i >> 1));
    }
    return res;
}
```

---

## 4. Exceptions and Pitfalls

1. **Signed Shifts**: Shifting a negative integer (`-5 >> 1`) is "Implementation Defined" in C++ before C++20. Modern C++ uses arithmetic shift (preserves sign), but be careful.
2. **Overflow**: `1 << 31` overflows a signed 32-bit `int`. Use `1LL << 31` for safety.
3. **Precedence**: `n & 1 == 0` is evaluated as `n & (1 == 0)`. **Always use parentheses** for bitwise operations: `(n & 1) == 0`.
4. **Large Bitsets**: If you need to manipulate thousands of bits, use `std::bitset` or `vector<bool>`.

---

## 5. Complexity Table

| Problem | Time | Space | Note |
|---------|------|-------|------|
| Single element (2x) | $O(N)$ | $O(1)$ | Pure XOR |
| Two single elements | $O(N)$ | $O(1)$ | Split by bit |
| Single element (3x) | $O(32N)$ | $O(1)$ | Bit counting |
| Power set | $O(N \cdot 2^N)$ | $O(1)$ | Exponential |
| Max XOR Subarray | $O(N)$ | $O(N)$ | Requires Trie |

---

## Final Checklist
- [ ] Wrapped bitwise operations in parentheses?
- [ ] Used `long long` for shifts $>30$?
- [ ] Accounted for negative numbers (Two's complement)?
- [ ] Considered `__builtin_popcount` for counting bits?
---

## Next Step

- Go to [README.md](README.md) to continue.
