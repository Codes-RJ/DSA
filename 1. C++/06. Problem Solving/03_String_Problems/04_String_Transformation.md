# String Transformations and Operations in C++

## 📖 Overview

String transformations form a cornerstone of competitive programming and text-processing interviews. Rather than relying on naive string allocations that trigger expensive memory churn, production-grade string transformations emphasize **in-place manipulation**, **two-pointer index tracking**, and **finite-state invariant maintenance**.

This guide provides rigorous analysis and production C++ implementations for the four canonical string transformation problems:
1. **In-Place Reverse Words in a Sentence** ($O(1)$ auxiliary space)
2. **In-Place String Compression (Run-Length Encoding)**
3. **Minimum Insertions to Form a Palindrome** (DP & LCS duality)
4. **Bidirectional Roman Numeral Conversion** (Greedy generation & subtractive parsing)

---

## 🔄 1. In-Place Word Reversal in a Sentence

Given a string $S$ containing words separated by spaces, reverse the order of words while trimming leading, trailing, and multiple consecutive spaces, utilizing **$O(1)$ auxiliary space**.

### The Two-Pass Reversal Invariant
```
Initial:         "  the   sky  is   blue  "
Step 1: Clean spaces & trim:
                 "the sky is blue"
Step 2: Reverse entire string:
                 "eulb si yks eht"
Step 3: Reverse each individual word:
                 "blue is sky the"
```

Why does this work?
- Reversing the entire string reverses the order of the words, but also reverses the letters within each word.
- Reversing each individual word restores its correct forward spelling while preserving the reversed word order.

---

## 🗜️ 2. In-Place String Compression (Run-Length Encoding)

Given an array of characters, compress it in-place using the following rules:
- Begin with an empty string `s`. For each group of consecutive repeating characters in `chars`:
  - If group length is 1, append the character.
  - Otherwise, append the character followed by the group's length as digits.
- The compressed string must be written directly back into the input array `chars`.

```
Input:   [ 'a', 'a', 'b', 'b', 'c', 'c', 'c' ]
Read:     ─── a:2 ───   ─── b:2 ───   ───── c:3 ─────
Write:   [ 'a', '2',   'b', '2',     'c', '3' ]  --> Returns new length 6
```

---

## 🪞 3. Minimum Insertions to Form a Palindrome

Given a string $S$, determine the minimum number of characters that must be inserted at any positions to make $S$ a palindrome.

### Mathematical Duality Theorem
> **Theorem**: The minimum insertions to transform $S$ of length $N$ into a palindrome is equal to:
> $$\text{Min Insertions} = N - \text{LPS}(S)$$
> where $\text{LPS}(S)$ is the **Longest Palindromic Subsequence** of $S$.

Equivalently, $\text{LPS}(S) = \text{LCS}(S, S^R)$, the Longest Common Subsequence of $S$ and its reversed counterpart $S^R$.
Any characters in $S$ that are already part of the longest palindromic subsequence can be kept; every character outside it requires exactly one matching inserted counterpart.

---

## 🏛️ 4. Bidirectional Roman Numeral Conversion

Roman numerals follow a strict additive and subtractive positional notation over seven symbols:
- `I` (1), `V` (5), `X` (10), `L` (50), `C` (100), `D` (500), `M` (1000).

```
Subtractive Combinations:
  IV = 4,   IX = 9
  XL = 40,  XC = 90
  CD = 400, CM = 900
```

1. **Integer to Roman (Greedy)**: Greedily subtract the largest possible value from a lookup table ordered in descending order.
2. **Roman to Integer (Lookahead)**: If the current symbol is strictly smaller than the next symbol ($s[i] < s[i+1]$), subtract $s[i]$; otherwise, add $s[i]$.

---

## 💻 Complete C++ Implementation

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cassert>
#include <unordered_map>

class StringTransformation {
public:
    // -------------------------------------------------------------
    // Problem 1: In-Place Word Reversal with Space Normalization
    // -------------------------------------------------------------
    static std::string reverseWords(std::string s) {
        int n = static_cast<int>(s.length());
        int writeIdx = 0;
        int readIdx = 0;

        // Step 1: Remove redundant spaces in-place
        while (readIdx < n) {
            // Skip leading spaces
            while (readIdx < n && s[readIdx] == ' ') readIdx++;
            if (readIdx >= n) break;

            // Add single space between words
            if (writeIdx > 0) s[writeIdx++] = ' ';

            // Copy word
            while (readIdx < n && s[readIdx] != ' ') {
                s[writeIdx++] = s[readIdx++];
            }
        }
        s.resize(writeIdx);
        n = writeIdx;

        // Step 2: Reverse entire string
        std::reverse(s.begin(), s.end());

        // Step 3: Reverse each individual word
        int start = 0;
        for (int end = 0; end <= n; end++) {
            if (end == n || s[end] == ' ') {
                std::reverse(s.begin() + start, s.begin() + end);
                start = end + 1;
            }
        }

        return s;
    }

    // -------------------------------------------------------------
    // Problem 2: In-Place Run-Length Compression
    // -------------------------------------------------------------
    static int compress(std::vector<char>& chars) {
        int n = static_cast<int>(chars.size());
        int writeIdx = 0;
        int readIdx = 0;

        while (readIdx < n) {
            char currentChar = chars[readIdx];
            int count = 0;

            // Count contiguous occurrences
            while (readIdx < n && chars[readIdx] == currentChar) {
                readIdx++;
                count++;
            }

            // Write character
            chars[writeIdx++] = currentChar;

            // Write count if greater than 1
            if (count > 1) {
                std::string countStr = std::to_string(count);
                for (char digit : countStr) {
                    chars[writeIdx++] = digit;
                }
            }
        }

        chars.resize(writeIdx);
        return writeIdx;
    }

    // -------------------------------------------------------------
    // Problem 3: Minimum Insertions to Form Palindrome (DP)
    // -------------------------------------------------------------
    static int minInsertionsForPalindrome(const std::string& s) {
        int n = static_cast<int>(s.length());
        if (n <= 1) return 0;

        // dp[i][j] stores min insertions needed to make s[i..j] a palindrome
        std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));

        // Substrings of length len
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;
                if (s[i] == s[j]) {
                    dp[i][j] = dp[i + 1][j - 1];
                } else {
                    dp[i][j] = 1 + std::min(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }

        return dp[0][n - 1];
    }

    // -------------------------------------------------------------
    // Problem 4A: Integer to Roman Numeral (Greedy)
    // -------------------------------------------------------------
    static std::string intToRoman(int num) {
        const std::pair<int, const char*> romanTable[] = {
            {1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"},
            {100, "C"},  {90, "XC"},  {50, "L"},  {40, "XL"},
            {10, "X"},   {9, "IX"},   {5, "V"},   {4, "IV"},
            {1, "I"}
        };

        std::string result = "";
        for (const auto& entry : romanTable) {
            while (num >= entry.first) {
                result += entry.second;
                num -= entry.first;
            }
        }
        return result;
    }

    // -------------------------------------------------------------
    // Problem 4B: Roman Numeral to Integer (Lookahead)
    // -------------------------------------------------------------
    static int romanToInt(const std::string& s) {
        auto valueOf = [](char c) -> int {
            switch (c) {
                case 'I': return 1;
                case 'V': return 5;
                case 'X': return 10;
                case 'L': return 50;
                case 'C': return 100;
                case 'D': return 500;
                case 'M': return 1000;
                default: return 0;
            }
        };

        int total = 0;
        int n = static_cast<int>(s.length());

        for (int i = 0; i < n; i++) {
            int currentVal = valueOf(s[i]);
            if (i + 1 < n && currentVal < valueOf(s[i + 1])) {
                // Subtractive combination (e.g. IV = 4)
                total -= currentVal;
            } else {
                total += currentVal;
            }
        }

        return total;
    }
};

int main() {
    std::cout << "=== String Transformations Comprehensive Test Harness ===\n\n";

    std::cout << "--- 1. Testing Reverse Words in a Sentence ---\n";
    std::string s1 = "  the   sky  is   blue  ";
    std::string rev1 = StringTransformation::reverseWords(s1);
    std::cout << "  Input:    \"" << s1 << "\"\n";
    std::cout << "  Reversed: \"" << rev1 << "\"\n";
    assert(rev1 == "blue is sky the");

    std::string s2 = "a good   example";
    std::string rev2 = StringTransformation::reverseWords(s2);
    std::cout << "  Input:    \"" << s2 << "\"\n";
    std::cout << "  Reversed: \"" << rev2 << "\"\n";
    assert(rev2 == "example good a");
    std::cout << "  Word Reversal: ALL PASSED\n\n";

    std::cout << "--- 2. Testing In-Place Run-Length Compression ---\n";
    std::vector<char> chars1 = {'a', 'a', 'b', 'b', 'c', 'c', 'c'};
    int newLen1 = StringTransformation::compress(chars1);
    std::cout << "  Compressed result: \"";
    for (char c : chars1) std::cout << c;
    std::cout << "\" (New length: " << newLen1 << ")\n";
    assert(newLen1 == 6);

    std::vector<char> chars2 = {'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'};
    int newLen2 = StringTransformation::compress(chars2);
    std::cout << "  Compressed result: \"";
    for (char c : chars2) std::cout << c;
    std::cout << "\" (New length: " << newLen2 << ")\n";
    assert(newLen2 == 4); // "ab12"
    std::cout << "  Run-Length Compression: ALL PASSED\n\n";

    std::cout << "--- 3. Testing Minimum Insertions for Palindrome ---\n";
    std::string pal1 = "zzazz";
    assert(StringTransformation::minInsertionsForPalindrome(pal1) == 0); // Already palindrome

    std::string pal2 = "mbadm";
    // Can become "mbdadbm" by inserting 'd' and 'b' -> 2 insertions
    int minIns2 = StringTransformation::minInsertionsForPalindrome(pal2);
    std::cout << "  Min insertions for \"mbadm\": " << minIns2 << " (Expected: 2)\n";
    assert(minIns2 == 2);

    std::string pal3 = "leetcode";
    int minIns3 = StringTransformation::minInsertionsForPalindrome(pal3);
    std::cout << "  Min insertions for \"leetcode\": " << minIns3 << " (Expected: 5)\n";
    assert(minIns3 == 5);
    std::cout << "  Palindrome Insertions: ALL PASSED\n\n";

    std::cout << "--- 4. Testing Bidirectional Roman Numeral Conversion ---\n";
    std::vector<int> numbers = {3, 4, 9, 58, 1994, 2026};
    for (int num : numbers) {
        std::string roman = StringTransformation::intToRoman(num);
        int parsedBack = StringTransformation::romanToInt(roman);
        std::cout << "  " << num << " => " << roman << " => " << parsedBack << "\n";
        assert(parsedBack == num);
    }
    std::cout << "  Bidirectional Roman Conversion: ALL PASSED\n\n";

    std::cout << "=== All String Transformations Tests Completed Successfully! ===\n";
    return 0;
}
```

---

## 📊 Complexity Analysis

| Problem | Time Complexity | Auxiliary Space | Optimal Strategy |
| :--- | :--- | :--- | :--- |
| **Reverse Words** | $O(N)$ | $O(1)$ | Trim spaces + Reverse string + Reverse words |
| **Run-Length Compression** | $O(N)$ | $O(1)$ | Two-pointer read and write heads |
| **Min Palindrome Insertions**| $O(N^2)$ | $O(N^2)$ or $O(N)$ | Dynamic Programming ($N - \text{LPS}(S)$) |
| **Integer to Roman** | $O(1)$ | $O(1)$ | Greedy value subtraction lookup table |
| **Roman to Integer** | $O(N)$ | $O(1)$ | Lookahead subtractive neighbor comparison |
