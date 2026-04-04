# Advanced String Problems

## High-Level Topics

### 1. Tries (Prefix Trees)
A tree structure used for fast prefix search and retrieval. Each node represents a character.
- **Insert**: O(L) where L is length.
- **Search**: O(L).
- **Space**: O(Alphabet_size * Num_nodes).

### 2. Suffix Arrays and Suffix Trees
Represent all suffixes of a string.
- Suffix tree: O(N) construction using Ukkonen's algorithm.
- Suffix array: O(N log N) or O(N) construction.
- Used for finding the longest repeated substring, longest common substring, etc.

### 3. Aho-Corasick Algorithm
Used for multi-pattern matching. It builds a Trie of the patterns and adds fail pointers (similar to KMP).
- **Complexity**: O(Length_of_Text + Sum_of_Patterns_Length).

### 4. Manacher's Algorithm
Finds the longest palindromic substring in **linear** time O(N).
- It overcomes the odd/even length problem by inserting dummy characters like `#`.

### 5. String Hashing
Representing a string as a unique number using polynomial hashing.
- `H = (s[0]*P^0 + s[1]*P^1 + ... + s[n-1]*P^(n-1)) % M`
- Good for O(1) substring comparison after O(N) preprocessing.

## Key Considerations
1. **Collisions in Hashing**: Always use a large prime `M` and possibly double hashing to reduce risk.
2. **Space Benchmarks**: Tries and suffix structures can take substantial memory for large alphabets or very long strings.
3. **Problem Type Identification**:
   - Multiple patterns? → Aho-Corasick or Suffix Tree.
   - Longest common substring? → Suffix Tree or Dynamic Programming.
   - Distinct substrings? → Suffix Array or Trie.

## Summary
Advanced string algorithms often bridge strings with tree structures or number theory (hashing) to solve problems that would otherwise be inefficient.
