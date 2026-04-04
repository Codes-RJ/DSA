# String Problems

## Overview
String problems are fundamental in computer science and appear frequently in programming contests, technical interviews, and real-world applications. This section covers string manipulation techniques, algorithms, and problem-solving strategies.

## Topics Covered

### 1. String Basics (`01_String_Basics.md`)
- String representation and operations
- Character classification and conversion
- String comparison and searching
- Memory management for strings
- Common string pitfalls

### 2. String Algorithms (`02_String_Algorithms.md`)
- String matching algorithms
- Pattern searching techniques
- String hashing
- Suffix arrays and trees
- String transformation algorithms

### 3. Pattern Matching (`03_Pattern_Matching.md`)
- Naive pattern matching
- Knuth-Morris-Pratt (KMP) algorithm
- Rabin-Karp algorithm
- Boyer-Moore algorithm
- Z-algorithm

### 4. String Transformation (`04_String_Transformation.md`)
- String reversal and rotation
- Palindrome checking and generation
- Anagram detection and generation
- String compression and decompression
- Edit distance operations

### 5. Advanced String Problems (`05_Advanced_String_Problems.md`)
- Longest common subsequence
- Longest palindromic substring
- String permutation problems
- Regular expression matching
- Advanced string DP problems

## Key Concepts

### String Properties
- **Length**: Number of characters in the string
- **Index**: Position of characters (0-based or 1-based)
- **Substring**: Continuous sequence of characters
- **Subsequence**: Not necessarily continuous sequence
- **Prefix**: Substring starting from beginning
- **Suffix**: Substring ending at the end

### String Operations
- **Concatenation**: Joining two strings
- **Comparison**: Lexicographical ordering
- **Searching**: Finding patterns within strings
- **Modification**: Insert, delete, replace operations
- **Transformation**: Changing string properties

## Basic String Operations

### 1. String Utilities
```cpp
class StringUtils {
public:
    // Check if string is empty
    static bool isEmpty(const std::string& str) {
        return str.empty();
    }
    
    // Get string length
    static size_t length(const std::string& str) {
        return str.length();
    }
    
    // Convert to uppercase
    static std::string toUpper(const std::string& str) {
        std::string result = str;
        std::transform(result.begin(), result.end(), result.begin(), ::toupper);
        return result;
    }
    
    // Convert to lowercase
    static std::string toLower(const std::string& str) {
        std::string result = str;
        std::transform(result.begin(), result.end(), result.begin(), ::tolower);
        return result;
    }
    
    // Reverse string
    static std::string reverse(const std::string& str) {
        std::string result = str;
        std::reverse(result.begin(), result.end());
        return result;
    }
    
    // Check if character is alphabetic
    static bool isAlpha(char c) {
        return std::isalpha(c);
    }
    
    // Check if character is numeric
    static bool isDigit(char c) {
        return std::isdigit(c);
    }
    
    // Check if character is alphanumeric
    static bool isAlphaNumeric(char c) {
        return std::isalnum(c);
    }
    
    // Remove whitespace from both ends
    static std::string trim(const std::string& str) {
        size_t start = str.find_first_not_of(" \t\n\r");
        if (start == std::string::npos) return "";
        
        size_t end = str.find_last_not_of(" \t\n\r");
        return str.substr(start, end - start + 1);
    }
};
```

### 2. String Searching
```cpp
class StringSearch {
public:
    // Find all occurrences of a pattern
    static std::vector<int> findAllOccurrences(const std::string& text, 
                                              const std::string& pattern) {
        std::vector<int> positions;
        if (pattern.empty()) return positions;
        
        size_t pos = text.find(pattern);
        while (pos != std::string::npos) {
            positions.push_back(pos);
            pos = text.find(pattern, pos + 1);
        }
        
        return positions;
    }
    
    // Count occurrences of a pattern
    static int countOccurrences(const std::string& text, 
                               const std::string& pattern) {
        if (pattern.empty()) return 0;
        
        int count = 0;
        size_t pos = text.find(pattern);
        while (pos != std::string::npos) {
            count++;
            pos = text.find(pattern, pos + 1);
        }
        
        return count;
    }
    
    // Check if string contains pattern
    static bool contains(const std::string& text, const std::string& pattern) {
        return text.find(pattern) != std::string::npos;
    }
    
    // Check if string starts with pattern
    static bool startsWith(const std::string& text, const std::string& pattern) {
        if (pattern.length() > text.length()) return false;
        return text.substr(0, pattern.length()) == pattern;
    }
    
    // Check if string ends with pattern
    static bool endsWith(const std::string& text, const std::string& pattern) {
        if (pattern.length() > text.length()) return false;
        return text.substr(text.length() - pattern.length()) == pattern;
    }
};
```

## Pattern Matching Algorithms

### 1. Knuth-Morris-Pratt (KMP) Algorithm
```cpp
class KMP {
private:
    // Build LPS (Longest Prefix Suffix) array
    static std::vector<int> buildLPS(const std::string& pattern) {
        int m = pattern.length();
        std::vector<int> lps(m, 0);
        
        int len = 0; // Length of previous longest prefix suffix
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
    
public:
    // Search pattern using KMP
    static std::vector<int> search(const std::string& text, 
                                  const std::string& pattern) {
        std::vector<int> positions;
        if (pattern.empty()) return positions;
        
        std::vector<int> lps = buildLPS(pattern);
        int n = text.length();
        int m = pattern.length();
        
        int i = 0; // Index for text
        int j = 0; // Index for pattern
        
        while (i < n) {
            if (pattern[j] == text[i]) {
                i++;
                j++;
            }
            
            if (j == m) {
                positions.push_back(i - j);
                j = lps[j - 1];
            } else if (i < n && pattern[j] != text[i]) {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        
        return positions;
    }
};
```

### 2. Rabin-Karp Algorithm
```cpp
class RabinKarp {
private:
    static const int MOD = 1e9 + 7;
    static const int BASE = 256;
    
public:
    // Search pattern using Rabin-Karp
    static std::vector<int> search(const std::string& text, 
                                  const std::string& pattern) {
        std::vector<int> positions;
        if (pattern.empty() || pattern.length() > text.length()) {
            return positions;
        }
        
        int n = text.length();
        int m = pattern.length();
        
        // Calculate hash of pattern and first window of text
        long long patternHash = 0;
        long long textHash = 0;
        long long power = 1; // BASE^(m-1) % MOD
        
        for (int i = 0; i < m; i++) {
            patternHash = (patternHash * BASE + pattern[i]) % MOD;
            textHash = (textHash * BASE + text[i]) % MOD;
            
            if (i < m - 1) {
                power = (power * BASE) % MOD;
            }
        }
        
        // Slide the pattern over text
        for (int i = 0; i <= n - m; i++) {
            if (patternHash == textHash) {
                // Check character by character
                if (text.substr(i, m) == pattern) {
                    positions.push_back(i);
                }
            }
            
            // Calculate hash for next window
            if (i < n - m) {
                textHash = (textHash - text[i] * power) % MOD;
                textHash = (textHash * BASE + text[i + m]) % MOD;
                
                if (textHash < 0) {
                    textHash += MOD;
                }
            }
        }
        
        return positions;
    }
};
```

## String Transformation Problems

### 1. Palindrome Operations
```cpp
class PalindromeOperations {
public:
    // Check if string is palindrome
    static bool isPalindrome(const std::string& str) {
        int left = 0;
        int right = str.length() - 1;
        
        while (left < right) {
            if (str[left] != str[right]) {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
    }
    
    // Check if string is palindrome ignoring case and non-alphanumeric
    static bool isPalindromeClean(const std::string& str) {
        int left = 0;
        int right = str.length() - 1;
        
        while (left < right) {
            // Skip non-alphanumeric characters
            while (left < right && !std::isalnum(str[left])) left++;
            while (left < right && !std::isalnum(str[right])) right--;
            
            if (left < right) {
                if (std::tolower(str[left]) != std::tolower(str[right])) {
                    return false;
                }
                left++;
                right--;
            }
        }
        
        return true;
    }
    
    // Find longest palindromic substring
    static std::string longestPalindromeSubstring(const std::string& str) {
        if (str.empty()) return "";
        
        int start = 0;
        int maxLen = 1;
        
        for (int i = 0; i < str.length(); i++) {
            // Odd length palindrome
            expandAroundCenter(str, i, i, start, maxLen);
            // Even length palindrome
            expandAroundCenter(str, i, i + 1, start, maxLen);
        }
        
        return str.substr(start, maxLen);
    }
    
    // Minimum insertions to make palindrome
    static int minInsertionsToPalindrome(const std::string& str) {
        return str.length() - longestPalindromeSubsequence(str);
    }
    
private:
    static void expandAroundCenter(const std::string& str, int left, int right,
                                  int& start, int& maxLen) {
        while (left >= 0 && right < str.length() && str[left] == str[right]) {
            int currentLen = right - left + 1;
            if (currentLen > maxLen) {
                start = left;
                maxLen = currentLen;
            }
            left--;
            right++;
        }
    }
    
    static int longestPalindromeSubsequence(const std::string& str) {
        std::string rev = str;
        std::reverse(rev.begin(), rev.end());
        
        int n = str.length();
        std::vector<std::vector<int>> dp(n + 1, std::vector<int>(n + 1, 0));
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (str[i - 1] == rev[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = std::max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        
        return dp[n][n];
    }
};
```

### 2. Anagram Operations
```cpp
class AnagramOperations {
public:
    // Check if two strings are anagrams
    static bool areAnagrams(const std::string& str1, const std::string& str2) {
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
    
    // Group anagrams together
    static std::vector<std::vector<std::string>> groupAnagrams(
        const std::vector<std::string>& words) {
        std::unordered_map<std::string, std::vector<std::string>> groups;
        
        for (const std::string& word : words) {
            std::string key = word;
            std::sort(key.begin(), key.end());
            groups[key].push_back(word);
        }
        
        std::vector<std::vector<std::string>> result;
        for (auto& pair : groups) {
            result.push_back(pair.second);
        }
        
        return result;
    }
    
    // Find all anagrams of a pattern in a string
    static std::vector<int> findAnagrams(const std::string& text, 
                                        const std::string& pattern) {
        std::vector<int> result;
        if (pattern.length() > text.length()) return result;
        
        std::vector<int> patternCount(256, 0);
        std::vector<int> textCount(256, 0);
        
        int m = pattern.length();
        
        // Initialize frequency arrays
        for (int i = 0; i < m; i++) {
            patternCount[pattern[i]]++;
            textCount[text[i]]++;
        }
        
        // Slide through text
        for (int i = m; i < text.length(); i++) {
            if (patternCount == textCount) {
                result.push_back(i - m);
            }
            
            // Remove current character and add next character
            textCount[text[i - m]]--;
            textCount[text[i]]++;
        }
        
        // Check last window
        if (patternCount == textCount) {
            result.push_back(text.length() - m);
        }
        
        return result;
    }
};
```

## Advanced String Problems

### 1. Edit Distance
```cpp
class EditDistance {
public:
    // Levenshtein distance (insert, delete, replace)
    static int levenshteinDistance(const std::string& str1, 
                                  const std::string& str2) {
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
    
    // Check if strings are one edit apart
    static bool isOneEditApart(const std::string& str1, const std::string& str2) {
        int m = str1.length();
        int n = str2.length();
        
        if (abs(m - n) > 1) return false;
        
        int i = 0, j = 0;
        int edits = 0;
        
        while (i < m && j < n) {
            if (str1[i] != str2[j]) {
                if (edits == 1) return false;
                
                if (m > n) {
                    i++; // Delete from str1
                } else if (n > m) {
                    j++; // Insert to str1
                } else {
                    i++; j++; // Replace
                }
                
                edits++;
            } else {
                i++; j++;
            }
        }
        
        // Handle remaining characters
        if (i < m || j < n) edits++;
        
        return edits == 1;
    }
};
```

### 2. Longest Common Subsequence
```cpp
class LongestCommonSubsequence {
public:
    // Find length of LCS
    static int length(const std::string& str1, const std::string& str2) {
        int m = str1.length();
        int n = str2.length();
        
        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (str1[i - 1] == str2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = std::max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        
        return dp[m][n];
    }
    
    // Find LCS string
    static std::string find(const std::string& str1, const std::string& str2) {
        int m = str1.length();
        int n = str2.length();
        
        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));
        
        // Fill DP table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (str1[i - 1] == str2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = std::max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        
        // Reconstruct LCS
        std::string lcs;
        int i = m, j = n;
        
        while (i > 0 && j > 0) {
            if (str1[i - 1] == str2[j - 1]) {
                lcs.push_back(str1[i - 1]);
                i--; j--;
            } else if (dp[i - 1][j] > dp[i][j - 1]) {
                i--;
            } else {
                j--;
            }
        }
        
        std::reverse(lcs.begin(), lcs.end());
        return lcs;
    }
};
```

## String Compression

### 1. Run-Length Encoding
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
                compressed += std::to_string(count);
                count = 1;
            }
        }
        
        // Add last character
        compressed += str.back();
        compressed += std::to_string(count);
        
        return compressed.length() < str.length() ? compressed : str;
    }
    
    // Run-length decoding
    static std::string decompressRLE(const std::string& str) {
        std::string decompressed;
        
        for (int i = 0; i < str.length(); i += 2) {
            if (i + 1 < str.length()) {
                char c = str[i];
                int count = str[i + 1] - '0';
                decompressed.append(count, c);
            }
        }
        
        return decompressed;
    }
};
```

## Performance Analysis

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Naive Search | O(nm) | O(1) |
| KMP | O(n + m) | O(m) |
| Rabin-Karp | O(n + m) | O(1) |
| Edit Distance | O(nm) | O(nm) |
| LCS | O(nm) | O(nm) |
| Palindrome Check | O(n) | O(1) |

## Best Practices

1. **Use String Views**: For read-only operations to avoid copies
2. **Reserve Memory**: Pre-allocate when size is known
3. **Avoid Unnecessary Copies**: Use const references
4. **Choose Right Algorithm**: Consider string length and pattern complexity
5. **Handle Unicode**: Use appropriate libraries for international text

## Common Pitfalls

1. **Off-by-One Errors**: Be careful with indices
2. **Memory Leaks**: Manage dynamic allocation properly
3. **Null Terminators**: C-style strings require null termination
4. **Encoding Issues**: Consider character encoding
5. **Performance**: String operations can be expensive

## Summary

String problems require understanding of various algorithms and techniques. Mastering these concepts enables efficient text processing, pattern matching, and string manipulation essential for many applications in computer science.
