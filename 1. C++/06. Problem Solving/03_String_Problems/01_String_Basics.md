# String Basics in C++

## Introduction
A string is a sequence of characters. In C++, there are two ways to represent strings:
1. **C-Style Strings**: Arrays of `char` ending with a null character `\0`.
2. **`std::string`**: A dynamic class that manages strings more easily.

## `std::string` Basics

### Initialization
```cpp
#include <string>
std::string s1 = "Hello";
std::string s2("World");
std::string s3(5, 'c'); // "ccccc"
```

### Common Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `size()` / `length()` | Number of characters | `s.size()` → 5 |
| `substr(pos, len)` | Extract substring | `s.substr(1, 3)` |
| `find("str")` | Find position of first occurrence | `s.find("el")` |
| `append("str")` | Concatenate to end | `s.append("!!!")` |
| `push_back('c')` | Add single character to end | `s.push_back('!')` |
| `empty()` | Check if string is empty | `s.empty()` |

## Iteration and Indexing
Strings support direct indexing like arrays:
```cpp
for (int i = 0; i < s.size(); i++) cout << s[i];
for (char c : s) cout << c;
```

## Comparisons
Unlike C-style strings (which need `strcmp`), `std::string` can be compared using standard operators like `==`, `!=`, `<`, `>`, `!=`.

## Conversions
### String to Number
- `stoi(s)`: String to int.
- `stol(s)`: String to long.
- `stod(s)`: String to double.

### Number to String
- `std::to_string(42)` → "42".

## Space and Time Complexity
- `std::string` operations (size, indexing) are O(1).
- Concatenation is generally O(N).
- Comparing strings is O(min(N1, N2)).
- Searching for substrings is O(N*M) or more efficient with better algorithms.

## Prerequisites
Understanding strings is essential for most coding problems involving text processing, data parsing, and user interactions.
---

## Next Step

- Go to [02_String_Algorithms.md](02_String_Algorithms.md) to continue with String Algorithms.
