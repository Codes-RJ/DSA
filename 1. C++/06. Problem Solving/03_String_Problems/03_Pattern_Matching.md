# Pattern Matching Algorithms

## Introduction
Pattern matching is the task of finding one or more occurrences of a "pattern" string within a "text" string.

## Common Algorithms

### 1. Brute Force (Naive)
Check all possible positions where the pattern could start.
- **Time Complexity**: O(N * M)
- **Space** : O(1)

### 2. Knuth-Morris-Pratt (KMP)
Uses a **prefix function** (also called π table or LPS array) to avoid unnecessary comparisons. When a mismatch occurs, it uses the prefix information to "jump" ahead.
- **Time Complexity**: O(N + M)
- **Space Complexity**: O(M)

### 3. Rabin-Karp
Uses **rolling hashing** to find the pattern. If two strings have the same hash value, they are potentially the same. It calculates the hash of the next window in O(1) time.
- **Time Complexity**: O(N + M) (average), O(N * M) (worst case due to collisions)
- **Space Complexity**: O(1)

### 4. Z-Algorithm
Builds a **Z-array** where `Z[i]` is the length of the longest substring starting from `text[i]` which is also a prefix of `text`.
- **Time Complexity**: O(N + M)
- **Space Complexity**: O(N + M)

### 5. Boyer-Moore
Uses two heuristics (bad character and good suffix rule) to skip sections of the text. It's often very fast in practice.
- **Complexity**: O(N/M) best case, O(N * M) worst case.

## Summary Checklist
- [ ] Needs O(N+M) performance? → KMP or Z
- [ ] Many patterns to search? → Aho-Corasick
- [ ] Pattern changes frequently? → Rolling Hash (Rabin-Karp)
- [ ] Real-world fast search? → Boyer-Moore or KMP

## Comparison Table

| Algorithm | Preprocessing | Search Time | Notes |
|-----------|---------------|-------------|-------|
| **Naive** | None | O(N*M) | Slow, but no overhead |
| **KMP** | O(M) | O(N) | Solid, reliable |
| **Rabin-Karp** | O(M) | O(N) (avg) | Good for multiple patterns |
| **Z-Algorithm** | O(N+M) | O(1) (after construction) | Versatile for prefixes |
| **Boyer-Moore** | O(M + Σ) | O(N/M) - O(N*M) | Standard for `ctrl + f` |
---

## Next Step

- Go to [04_String_Transformation.md](04_String_Transformation.md) to continue with String Transformation.
