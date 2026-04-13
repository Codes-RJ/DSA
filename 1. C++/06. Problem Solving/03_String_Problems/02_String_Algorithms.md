# String Algorithms

## Introduction
String algorithms are fundamental techniques for processing and manipulating strings efficiently. These algorithms are crucial for text processing, pattern matching, bioinformatics, and many other applications.

## String Processing Fundamentals

### String Properties
- **Length**: Number of characters in the string
- **Index**: Position of characters (0-based or 1-based)
- **Substring**: Continuous sequence of characters
- **Subsequence**: Not necessarily continuous sequence
- **Prefix**: Substring starting from beginning
- **Suffix**: Substring ending at the end

## Basic String Operations

### 1. String Utilities
```cpp
class StringAlgorithms {
public:
    // Check if string is palindrome
    static bool isPalindrome(const std::string& str) {
        int left = 0, right = str.length() - 1;
        while (left < right) {
            if (str[left] != str[right]) return false;
            left++;
            right--;
        }
        return true;
    }
    
    // Check if string is palindrome ignoring case and spaces
    static bool isPalindromeClean(const std::string& str) {
        int left = 0, right = str.length() - 1;
        while (left < right) {
            while (left < right && !std::isalnum(str[left])) left++;
            while (left < right && !std::isalnum(str[right])) right--;
            
            if (left < right && std::tolower(str[left]) != std::tolower(str[right])) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
    
    // Remove all duplicates from string
    static std::string removeDuplicates(const std::string& str) {
        std::string result;
        std::unordered_set<char> seen;
        
        for (char c : str) {
            if (seen.insert(c).second) {
                result += c;
            }
        }
        
        return result;
    }
    
    // Find first non-repeating character
    static char firstNonRepeating(const std::string& str) {
        std::unordered_map<char, int> count;
        
        // Count occurrences
        for (char c : str) {
            count[c]++;
        }
        
        // Find first non-repeating
        for (char c : str) {
            if (count[c] == 1) {
                return c;
            }
        }
        
        return '\0'; // No non-repeating character
    }
    
    // Reverse words in string
    static std::string reverseWords(const std::string& str) {
        std::vector<std::string> words;
        std::stringstream ss(str);
        std::string word;
        
        while (ss >> word) {
            words.push_back(word);
        }
        
        std::reverse(words.begin(), words.end());
        
        std::string result;
        for (int i = 0; i < words.size(); i++) {
            if (i > 0) result += " ";
            result += words[i];
        }
        
        return result;
    }
};
```

## Advanced String Algorithms

### 1. Z-Algorithm
```cpp
class ZAlgorithm {
public:
    // Compute Z-array for pattern matching
    static std::vector<int> computeZArray(const std::string& str) {
        int n = str.length();
        std::vector<int> Z(n, 0);
        
        int L = 0, R = 0;
        
        for (int i = 1; i < n; i++) {
            if (i > R) {
                L = R = i;
                while (R < n && str[R - L] == str[R]) {
                    R++;
                }
                Z[i] = R - L;
                R--;
            } else {
                int k = i - L;
                if (Z[k] < R - i + 1) {
                    Z[i] = Z[k];
                } else {
                    L = i;
                    while (R < n && str[R - L] == str[R]) {
                        R++;
                    }
                    Z[i] = R - L;
                    R--;
                }
            }
        }
        
        return Z;
    }
    
    // Pattern matching using Z-algorithm
    static std::vector<int> patternMatching(const std::string& text, 
                                           const std::string& pattern) {
        std::string combined = pattern + "$" + text;
        std::vector<int> Z = computeZArray(combined);
        std::vector<int> positions;
        
        for (int i = pattern.length() + 1; i < combined.length(); i++) {
            if (Z[i] == pattern.length()) {
                positions.push_back(i - pattern.length() - 1);
            }
        }
        
        return positions;
    }
};
```

### 2. Prefix Function (KMP Preprocessing)
```cpp
class PrefixFunction {
public:
    // Compute prefix function (also known as failure function)
    static std::vector<int> computePrefixFunction(const std::string& pattern) {
        int m = pattern.length();
        std::vector<int> pi(m, 0);
        
        for (int i = 1; i < m; i++) {
            int j = pi[i - 1];
            
            while (j > 0 && pattern[i] != pattern[j]) {
                j = pi[j - 1];
            }
            
            if (pattern[i] == pattern[j]) {
                j++;
            }
            
            pi[i] = j;
        }
        
        return pi;
    }
    
    // Find all occurrences using prefix function
    static std::vector<int> findAllOccurrences(const std::string& text, 
                                              const std::string& pattern) {
        std::vector<int> pi = computePrefixFunction(pattern);
        std::vector<int> positions;
        
        int j = 0; // index in pattern
        for (int i = 0; i < text.length(); i++) {
            while (j > 0 && text[i] != pattern[j]) {
                j = pi[j - 1];
            }
            
            if (text[i] == pattern[j]) {
                j++;
            }
            
            if (j == pattern.length()) {
                positions.push_back(i - pattern.length() + 1);
                j = pi[j - 1];
            }
        }
        
        return positions;
    }
};
```

### 3. Suffix Array
```cpp
class SuffixArray {
public:
    // Build suffix array using O(n log²n) algorithm
    static std::vector<int> buildSuffixArray(const std::string& str) {
        int n = str.length();
        std::vector<int> suffixArray(n);
        std::vector<int> rank(n, 0);
        
        // Initialize suffix array and rank
        for (int i = 0; i < n; i++) {
            suffixArray[i] = i;
            rank[i] = str[i];
        }
        
        // Sort suffixes based on first 2^k characters
        for (int k = 1; k < n; k *= 2) {
            // Comparator for sorting
            auto compare = [k, &rank, n](int a, int b) {
                if (rank[a] != rank[b]) {
                    return rank[a] < rank[b];
                }
                
                int rankA = (a + k < n) ? rank[a + k] : -1;
                int rankB = (b + k < n) ? rank[b + k] : -1;
                
                return rankA < rankB;
            };
            
            std::sort(suffixArray.begin(), suffixArray.end(), compare);
            
            // Update ranks
            std::vector<int> newRank(n);
            newRank[suffixArray[0]] = 0;
            
            for (int i = 1; i < n; i++) {
                newRank[suffixArray[i]] = newRank[suffixArray[i - 1]];
                
                if (compare(suffixArray[i - 1], suffixArray[i])) {
                    newRank[suffixArray[i]]++;
                }
            }
            
            rank = newRank;
        }
        
        return suffixArray;
    }
    
    // Build LCP (Longest Common Prefix) array
    static std::vector<int> buildLCPArray(const std::string& str, 
                                          const std::vector<int>& suffixArray) {
        int n = str.length();
        std::vector<int> rank(n, 0);
        std::vector<int> lcp(n - 1, 0);
        
        // Build rank array
        for (int i = 0; i < n; i++) {
            rank[suffixArray[i]] = i;
        }
        
        int h = 0;
        for (int i = 0; i < n; i++) {
            if (rank[i] > 0) {
                int j = suffixArray[rank[i] - 1];
                
                while (i + h < n && j + h < n && str[i + h] == str[j + h]) {
                    h++;
                }
                
                lcp[rank[i] - 1] = h;
                
                if (h > 0) {
                    h--;
                }
            }
        }
        
        return lcp;
    }
};
```

## String Transformation Algorithms

### 1. String Distance Metrics
```cpp
class StringDistance {
public:
    // Hamming distance (for strings of equal length)
    static int hammingDistance(const std::string& str1, const std::string& str2) {
        if (str1.length() != str2.length()) {
            return -1; // Undefined for different lengths
        }
        
        int distance = 0;
        for (int i = 0; i < str1.length(); i++) {
            if (str1[i] != str2[i]) {
                distance++;
            }
        }
        
        return distance;
    }
    
    // Levenshtein distance (edit distance)
    static int levenshteinDistance(const std::string& str1, const std::string& str2) {
        int m = str1.length();
        int n = str2.length();
        
        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1));
        
        // Initialize base cases
        for (int i = 0; i <= m; i++) dp[i][0] = i;
        for (int j = 0; j <= n; j++) dp[0][j] = j;
        
        // Fill DP table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (str1[i - 1] == str2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = 1 + std::min({
                        dp[i - 1][j],     // Delete
                        dp[i][j - 1],     // Insert
                        dp[i - 1][j - 1]  // Replace
                    });
                }
            }
        }
        
        return dp[m][n];
    }
    
    // Damerau-Levenshtein distance (includes transposition)
    static int damerauLevenshteinDistance(const std::string& str1, const std::string& str2) {
        int m = str1.length();
        int n = str2.length();
        
        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1));
        
        for (int i = 0; i <= m; i++) dp[i][0] = i;
        for (int j = 0; j <= n; j++) dp[0][j] = j;
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                int cost = (str1[i - 1] == str2[j - 1]) ? 0 : 1;
                
                dp[i][j] = std::min({
                    dp[i - 1][j] + 1,        // Deletion
                    dp[i][j - 1] + 1,        // Insertion
                    dp[i - 1][j - 1] + cost  // Substitution
                });
                
                // Transposition
                if (i > 1 && j > 1 && str1[i - 1] == str2[j - 2] && str1[i - 2] == str2[j - 1]) {
                    dp[i][j] = std::min(dp[i][j], dp[i - 2][j - 2] + cost);
                }
            }
        }
        
        return dp[m][n];
    }
};
```

### 2. String Compression
```cpp
class StringCompression {
public:
    // Run-length encoding
    static std::string compressRLE(const std::string& str) {
        if (str.empty()) return "";
        
        std::string compressed;
        int count = 1;
        
        for (int i = 1; i < str.length(); i++) {
            if (str[i] == str[i - 1]) {
                count++;
            } else {
                compressed += str[i - 1];
                if (count > 1) {
                    compressed += std::to_string(count);
                }
                count = 1;
            }
        }
        
        // Add last character
        compressed += str.back();
        if (count > 1) {
            compressed += std::to_string(count);
        }
        
        return compressed.length() < str.length() ? compressed : str;
    }
    
    // Decompress RLE
    static std::string decompressRLE(const std::string& str) {
        std::string decompressed;
        
        for (int i = 0; i < str.length(); i++) {
            char c = str[i];
            decompressed += c;
            
            // Check if next character is a digit
            if (i + 1 < str.length() && std::isdigit(str[i + 1])) {
                int count = 0;
                i++;
                while (i < str.length() && std::isdigit(str[i])) {
                    count = count * 10 + (str[i] - '0');
                    i++;
                }
                i--; // Adjust for loop increment
                
                if (count > 1) {
                    decompressed.append(count - 1, c);
                }
            }
        }
        
        return decompressed;
    }
};
```

## String Searching and Matching

### 1. Advanced Pattern Matching
```cpp
class AdvancedPatternMatching {
public:
    // Find all occurrences of multiple patterns
    static std::unordered_map<std::string, std::vector<int>> multiPatternSearch(
        const std::string& text, const std::vector<std::string>& patterns) {
        
        std::unordered_map<std::string, std::vector<int>> results;
        
        for (const std::string& pattern : patterns) {
            auto positions = KMP::search(text, pattern);
            results[pattern] = positions;
        }
        
        return results;
    }
    
    // Find longest repeated substring
    static std::string longestRepeatedSubstring(const std::string& str) {
        if (str.empty()) return "";
        
        auto suffixArray = SuffixArray::buildSuffixArray(str);
        auto lcpArray = SuffixArray::buildLCPArray(str, suffixArray);
        
        int maxLCP = 0;
        int maxIndex = 0;
        
        for (int i = 0; i < lcpArray.size(); i++) {
            if (lcpArray[i] > maxLCP) {
                maxLCP = lcpArray[i];
                maxIndex = i;
            }
        }
        
        if (maxLCP == 0) return "";
        
        return str.substr(suffixArray[maxIndex], maxLCP);
    }
    
    // Find longest common substring between two strings
    static std::string longestCommonSubstring(const std::string& str1, 
                                             const std::string& str2) {
        std::string combined = str1 + "#" + str2;
        auto suffixArray = SuffixArray::buildSuffixArray(combined);
        auto lcpArray = SuffixArray::buildLCPArray(combined, suffixArray);
        
        int maxLCP = 0;
        int maxIndex = 0;
        int separatorPos = str1.length();
        
        for (int i = 0; i < lcpArray.size(); i++) {
            int pos1 = suffixArray[i];
            int pos2 = suffixArray[i + 1];
            
            // Check if suffixes are from different strings
            if ((pos1 < separatorPos) != (pos2 < separatorPos)) {
                if (lcpArray[i] > maxLCP) {
                    maxLCP = lcpArray[i];
                    maxIndex = i;
                }
            }
        }
        
        if (maxLCP == 0) return "";
        
        int startPos = suffixArray[maxIndex];
        return combined.substr(startPos, maxLCP);
    }
};
```

### 2. String Permutations
```cpp
class StringPermutations {
public:
    // Generate all permutations of a string
    static std::vector<std::string> generatePermutations(const std::string& str) {
        std::vector<std::string> permutations;
        std::string current = str;
        
        std::sort(current.begin(), current.end());
        do {
            permutations.push_back(current);
        } while (std::next_permutation(current.begin(), current.end()));
        
        return permutations;
    }
    
    // Check if two strings are permutations of each other
    static bool arePermutations(const std::string& str1, const std::string& str2) {
        if (str1.length() != str2.length()) return false;
        
        std::vector<int> count(256, 0);
        
        for (char c : str1) {
            count[c]++;
        }
        
        for (char c : str2) {
            count[c]--;
        }
        
        return std::all_of(count.begin(), count.end(), 
                          [](int x) { return x == 0; });
    }
    
    // Find k-th permutation of string
    static std::string kthPermutation(const std::string& str, int k) {
        std::string sorted = str;
        std::sort(sorted.begin(), sorted.end());
        
        int n = sorted.length();
        std::vector<int> factorial(n + 1);
        factorial[0] = 1;
        
        for (int i = 1; i <= n; i++) {
            factorial[i] = factorial[i - 1] * i;
        }
        
        if (k >= factorial[n]) {
            return ""; // k is out of range
        }
        
        std::string result;
        std::vector<bool> used(n, false);
        
        for (int i = 0; i < n; i++) {
            int remaining = n - i - 1;
            
            for (int j = 0; j < n; j++) {
                if (!used[j]) {
                    if (factorial[remaining] <= k) {
                        k -= factorial[remaining];
                    } else {
                        result += sorted[j];
                        used[j] = true;
                        break;
                    }
                }
            }
        }
        
        return result;
    }
};
```

## Performance Analysis

### Time Complexity
| Algorithm | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| Naive String Search | O(nm) | O(1) |
| KMP Algorithm | O(n + m) | O(m) |
| Rabin-Karp | O(n + m) | O(1) |
| Z-Algorithm | O(n + m) | O(n + m) |
| Suffix Array | O(n log²n) | O(n) |
| Edit Distance | O(nm) | O(nm) |
| String Compression | O(n) | O(n) |

## Best Practices

### 1. Algorithm Selection
- Use **KMP** for single pattern matching
- Use **Rabin-Karp** for multiple pattern matching
- Use **Suffix Array** for complex string problems
- Use **Z-Algorithm** for pattern matching with preprocessing

### 2. Implementation Tips
- Handle edge cases (empty strings, single characters)
- Consider Unicode and character encoding
- Use appropriate data structures for efficiency
- Optimize for space when working with large strings

### 3. Performance Optimization
- Preprocess patterns when using multiple queries
- Use rolling hashes for large-scale pattern matching
- Consider memory locality for string operations
- Use built-in string functions when available

## Applications

### 1. Text Processing
- Document search and indexing
- Text editors and word processors
- Spell checkers and grammar checkers
- Plagiarism detection

### 2. Bioinformatics
- DNA sequence analysis
- Protein structure prediction
- Genome assembly
- Sequence alignment

### 3. Information Retrieval
- Search engines
- Text mining
- Natural language processing
- Data compression

## Summary

String algorithms are essential for efficient text processing and pattern matching. Understanding various string processing techniques, from basic operations to advanced algorithms like suffix arrays, enables solving complex problems in text processing, bioinformatics, and information retrieval. Mastering these algorithms is crucial for competitive programming and real-world applications involving string manipulation.
---

## Next Step

- Go to [03_Pattern_Matching.md](03_Pattern_Matching.md) to continue with Pattern Matching.
