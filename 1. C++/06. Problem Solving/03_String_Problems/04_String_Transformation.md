# String Transformations and Operations

## Introduction
String transformations involve modifying a string to achieve a specific target or perform a specific task like reversing, rotating, or rearranging.

## Common Operations

### 1. Reverse a String
In C++, use `std::reverse(s.begin(), s.end());`.
- **Complexity**: O(N) Time, O(1) Space.

### 2. String Rotation
Rotate string `s` by `k` characters to the left.
- **Trick**: Concatenate `s + s`. The rotated string will be a substring of size `N` starting at index `k`.
- **Manual Trick**:
  1. Reverse `s[0...k-1]`
  2. Reverse `s[k...N-1]`
  3. Reverse the entire string `s[0...N-1]`
- **Complexity**: O(N) Time, O(1) Space.

### 3. Case Conversion
Modify ASCII values.
- `tolower(char)` and `toupper(char)` from `<cctype>`.
- Or bitwise: `c |= 32` for lowercase, `c &= ~32` for uppercase.

### 4. Permutations and Anagrams
- **Check Anagram**: Sort both strings and compare OR use a frequency array (`hash map`).
- **Generate Permutations**: Use `std::next_permutation(s.begin(), s.end());`.

## Problem Types

### 1. Palindrome Check
- **Basic**: Check if `s` is equal to its reverse.
- **Optimized**: Use two pointers starting from ends and move inward.
```cpp
bool isPalindrome(string s) {
    int l = 0, r = s.length() - 1;
    while (l < r) {
        if (s[l++] != s[r--]) return false;
    }
    return true;
}
```

### 2. Word Reversal
Reverse words in a sentence but not the letters themselves.
- **Strategy**: Reverse each word individually, then reverse the entire sentence.

### 3. Longest Palindromic Substring
- **Brute Force**: O(N³)
- **Expand around Center**: O(N²)
- **Manacher's Algorithm**: O(N)

## Key Concepts
- **ASCII and Encoding**: Understanding that characters are integers under the hood.
- **Two-Pointers**: Essential for palindromes, reversals, and specific rearrangements.
- **Frequency Arrays**: Great for anagram and character-counting problems.
---

## Next Step

- Go to [05_Advanced_String_Problems.md](05_Advanced_String_Problems.md) to continue with Advanced String Problems.
