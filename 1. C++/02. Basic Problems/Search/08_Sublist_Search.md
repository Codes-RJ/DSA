# Sublist Search

## Overview
Sublist search is an algorithm used to find a pattern list (sublist) within a larger list. It's commonly used in pattern matching, string searching, and sequence detection applications.

## Algorithm Description

### Theory
Sublist search works by aligning the pattern with the main list and comparing elements one by one. If a mismatch occurs, the pattern is shifted by one position and the process repeats.

### Algorithm Steps
1. Align pattern with start of main list
2. Compare elements one by one
3. If mismatch, shift pattern by one position
4. Repeat until match found or end reached

### Pseudocode
```
FUNCTION sublistSearch(mainList, pattern):
    n = length(mainList)
    m = length(pattern)
    
    FOR i FROM 0 TO n - m:
        match = true
        FOR j FROM 0 TO m - 1:
            IF mainList[i + j] != pattern[j]:
                match = false
                BREAK
        
        IF match:
            RETURN i  // Pattern found at position i
    
    RETURN -1  // Pattern not found
```

## Complexity Analysis

### Time Complexity
- **Best Case**: O(n + m) - Pattern at beginning
- **Average Case**: O(n × m)
- **Worst Case**: O(n × m) - Pattern not found

### Space Complexity
- **Space**: O(1) - Constant extra space

## Best Practices
- Use KMP algorithm for better worst-case performance
- Consider Rabin-Karp for rolling hash approach
- Optimize for specific pattern characteristics
- Handle edge cases (empty pattern, pattern larger than text)

## When to Use
- Pattern matching in sequences
- Substring search in strings
- Finding motifs in biological sequences
- Plagiarism detection
- Image pattern recognition

## Variants

### 1. Basic Sublist Search
Simple implementation with sliding window approach.

### 2. KMP-based Sublist Search
Uses Knuth-Morris-Pratt algorithm for better performance.

### 3. Rabin-Karp Sublist Search
Uses hashing for efficient comparison.

### 4. Boyer-Moore Sublist Search
Uses bad character heuristic for optimization.

## Implementation Examples

### Example 1: Basic Sublist Search
```cpp
#include <iostream>
#include <vector>

int sublistSearch(const std::vector<int>& mainList, const std::vector<int>& pattern) {
    int n = mainList.size();
    int m = pattern.size();
    
    if (m == 0) return 0;  // Empty pattern matches at beginning
    if (n < m) return -1;  // Pattern larger than main list
    
    for (int i = 0; i <= n - m; i++) {
        bool match = true;
        
        for (int j = 0; j < m; j++) {
            if (mainList[i + j] != pattern[j]) {
                match = false;
                break;
            }
        }
        
        if (match) {
            return i;  // Pattern found at position i
        }
    }
    
    return -1;  // Pattern not found
}

// Template version for generic types
template<typename T>
int sublistSearchGeneric(const std::vector<T>& mainList, const std::vector<T>& pattern) {
    int n = mainList.size();
    int m = pattern.size();
    
    if (m == 0) return 0;
    if (n < m) return -1;
    
    for (int i = 0; i <= n - m; i++) {
        bool match = true;
        
        for (int j = 0; j < m; j++) {
            if (mainList[i + j] != pattern[j]) {
                match = false;
                break;
            }
        }
        
        if (match) {
            return i;
        }
    }
    
    return -1;
}
```

### Example 2: String Sublist Search
```cpp
#include <string>

int substringSearch(const std::string& text, const std::string& pattern) {
    int n = text.length();
    int m = pattern.length();
    
    if (m == 0) return 0;
    if (n < m) return -1;
    
    for (int i = 0; i <= n - m; i++) {
        bool match = true;
        
        for (int j = 0; j < m; j++) {
            if (text[i + j] != pattern[j]) {
                match = false;
                break;
            }
        }
        
        if (match) {
            return i;
        }
    }
    
    return -1;
}

// Find all occurrences
std::vector<int> findAllOccurrences(const std::string& text, const std::string& pattern) {
    std::vector<int> positions;
    int n = text.length();
    int m = pattern.length();
    
    if (m == 0 || n < m) return positions;
    
    for (int i = 0; i <= n - m; i++) {
        bool match = true;
        
        for (int j = 0; j < m; j++) {
            if (text[i + j] != pattern[j]) {
                match = false;
                break;
            }
        }
        
        if (match) {
            positions.push_back(i);
        }
    }
    
    return positions;
}
```

### Example 3: KMP-based Sublist Search
```cpp
#include <vector>

std::vector<int> computeLPSArray(const std::vector<int>& pattern) {
    int m = pattern.size();
    std::vector<int> lps(m, 0);
    int len = 0;
    int i = 1;
    
    while (i < m) {
        if (pattern[i] == pattern[len]) {
            len++;
            lps[i] = len;
            i++;
        } else {
            if (len != 0) {
                len = lps[len - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }
    
    return lps;
}

int sublistSearchKMP(const std::vector<int>& mainList, const std::vector<int>& pattern) {
    int n = mainList.size();
    int m = pattern.size();
    
    if (m == 0) return 0;
    if (n < m) return -1;
    
    std::vector<int> lps = computeLPSArray(pattern);
    
    int i = 0;  // Index for mainList
    int j = 0;  // Index for pattern
    
    while (i < n) {
        if (mainList[i] == pattern[j]) {
            i++;
            j++;
            
            if (j == m) {
                return i - j;  // Pattern found
            }
        } else {
            if (j != 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
    }
    
    return -1;
}
```

### Example 4: Rabin-Karp Sublist Search
```cpp
#include <vector>
#include <cmath>

int sublistSearchRabinKarp(const std::vector<int>& mainList, const std::vector<int>& pattern) {
    int n = mainList.size();
    int m = pattern.size();
    
    if (m == 0) return 0;
    if (n < m) return -1;
    
    const int prime = 101;  // A prime number for hashing
    const int base = 256;   // Base for hashing
    
    // Compute hash of pattern and first window of mainList
    long long patternHash = 0;
    long long windowHash = 0;
    long long h = 1;  // base^(m-1) % prime
    
    for (int i = 0; i < m - 1; i++) {
        h = (h * base) % prime;
    }
    
    // Calculate initial hash values
    for (int i = 0; i < m; i++) {
        patternHash = (base * patternHash + pattern[i]) % prime;
        windowHash = (base * windowHash + mainList[i]) % prime;
    }
    
    // Slide the pattern over mainList
    for (int i = 0; i <= n - m; i++) {
        // Check hash values
        if (patternHash == windowHash) {
            // If hash matches, check characters one by one
            bool match = true;
            for (int j = 0; j < m; j++) {
                if (mainList[i + j] != pattern[j]) {
                    match = false;
                    break;
                }
            }
            if (match) {
                return i;
            }
        }
        
        // Calculate hash for next window
        if (i < n - m) {
            windowHash = (base * (windowHash - mainList[i] * h) + mainList[i + m]) % prime;
            if (windowHash < 0) {
                windowHash += prime;
            }
        }
    }
    
    return -1;
}
```

## Testing and Verification

### Test Cases
1. **Pattern at beginning**: Should return index 0
2. **Pattern at end**: Should find correctly
3. **Pattern in middle**: Should return correct index
4. **Pattern not present**: Should return -1
5. **Empty pattern**: Should return 0
6. **Pattern larger than text**: Should return -1
7. **Multiple occurrences**: Should find first occurrence

### Performance Tests
1. **Large datasets**: Test scalability
2. **Pattern characteristics**: Test with different pattern types
3. **Algorithm comparison**: Compare with KMP, Rabin-Karp

## Common Pitfalls
1. Not handling edge cases (empty pattern, pattern larger than text)
2. Off-by-one errors in loop bounds
3. Inefficient character-by-character comparison
4. Not using appropriate algorithms for specific cases

## Optimization Tips
1. Use KMP for patterns with repeated prefixes
2. Use Rabin-Karp for large alphabets
3. Use Boyer-Moore for long patterns
4. Consider preprocessing for multiple searches

## Real-World Applications
- Text editors (find functionality)
- DNA sequence analysis
- Plagiarism detection
- Spam filtering
- Bioinformatics
- Information retrieval

## Advanced Topics

### Multiple Pattern Search
- Aho-Corasick algorithm
- Trie-based approaches
- Suffix trees and arrays

### Approximate Pattern Matching
- Edit distance-based matching
- Fuzzy string matching
- Dynamic programming approaches

### Parallel Pattern Matching
- Multi-threaded implementations
- GPU-accelerated search
- Distributed pattern matching

## Related Algorithms
- Knuth-Morris-Pratt (KMP)
- Rabin-Karp
- Boyer-Moore
- Aho-Corasick
- Suffix Tree

## References
- Introduction to Algorithms (CLRS)
- String Algorithms (Maxime Crochemore)
- Pattern Matching in Strings

---

*This implementation provides a comprehensive guide to sublist search with various optimization strategies and real-world applications.*
---

## Next Step

- Go to [09_Hash_Search.md](09_Hash_Search.md) to continue with Hash Search.
