# 08_DP_on_Strings.md

## DP on Strings

### Definition

String DP problems involve finding optimal patterns, matching, or transformations between strings. These problems often use 2D DP where dimensions represent positions in one or two strings.

### Common String DP Problems

#### 1. Longest Common Subsequence (LCS)

Already covered in 2D DP section.

#### 2. Longest Common Substring

**Problem:** Find the longest contiguous substring common to both strings.

```
State: dp[i][j] = length of longest common suffix of s1[0..i-1] and s2[0..j-1]
Base: dp[0][j] = 0, dp[i][0] = 0
Transition:
    if s1[i-1] == s2[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1
    else:
        dp[i][j] = 0
Answer: max over all dp[i][j]
```

```cpp
int longestCommonSubstring(string s1, string s2) {
    int m = s1.length(), n = s2.length();
    vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
    int ans = 0;
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (s1[i-1] == s2[j-1]) {
                dp[i][j] = dp[i-1][j-1] + 1;
                ans = max(ans, dp[i][j]);
            }
        }
    }
    
    return ans;
}
```

#### 3. Shortest Common Supersequence (SCS)

**Problem:** Find the shortest string that has both given strings as subsequences.

```
State: dp[i][j] = length of SCS of s1[0..i-1] and s2[0..j-1]
Base: dp[0][j] = j, dp[i][0] = i
Transition:
    if s1[i-1] == s2[j-1]:
        dp[i][j] = 1 + dp[i-1][j-1]
    else:
        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
```

```cpp
int shortestCommonSupersequenceLength(string s1, string s2) {
    int m = s1.length(), n = s2.length();
    vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
    
    for (int i = 0; i <= m; i++) dp[i][0] = i;
    for (int j = 0; j <= n; j++) dp[0][j] = j;
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (s1[i-1] == s2[j-1]) {
                dp[i][j] = 1 + dp[i-1][j-1];
            } else {
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    
    return dp[m][n];
}
```

#### 4. Edit Distance (Levenshtein Distance)

Already covered in 2D DP section.

#### 5. Regular Expression Matching

**Problem:** Implement regex matching with '.' (any char) and '*' (zero or more of previous).

```
State: dp[i][j] = true if s[0..i-1] matches p[0..j-1]
Base: dp[0][0] = true
Transition:
    if p[j-1] == '*':
        dp[i][j] = dp[i][j-2] OR (match(s[i-1], p[j-2]) AND dp[i-1][j])
    else:
        dp[i][j] = match(s[i-1], p[j-1]) AND dp[i-1][j-1]
```

```cpp
bool isMatch(string s, string p) {
    int m = s.length(), n = p.length();
    vector<vector<bool>> dp(m+1, vector<bool>(n+1, false));
    dp[0][0] = true;
    
    // Handle patterns like a*, a*b*, a*b*c*
    for (int j = 2; j <= n; j++) {
        if (p[j-1] == '*') {
            dp[0][j] = dp[0][j-2];
        }
    }
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (p[j-1] == '*') {
                dp[i][j] = dp[i][j-2];
                if (p[j-2] == '.' || p[j-2] == s[i-1]) {
                    dp[i][j] = dp[i][j] || dp[i-1][j];
                }
            } else if (p[j-1] == '.' || p[j-1] == s[i-1]) {
                dp[i][j] = dp[i-1][j-1];
            }
        }
    }
    
    return dp[m][n];
}
```

#### 6. Wildcard Matching

**Problem:** Implement wildcard matching with '?' (any single char) and '*' (any sequence).

```
State: dp[i][j] = true if s[0..i-1] matches p[0..j-1]
Base: dp[0][0] = true
Transition:
    if p[j-1] == '*':
        dp[i][j] = dp[i][j-1] OR dp[i-1][j]
    else:
        dp[i][j] = (p[j-1] == '?' OR p[j-1] == s[i-1]) AND dp[i-1][j-1]
```

```cpp
bool isMatchWildcard(string s, string p) {
    int m = s.length(), n = p.length();
    vector<vector<bool>> dp(m+1, vector<bool>(n+1, false));
    dp[0][0] = true;
    
    for (int j = 1; j <= n; j++) {
        if (p[j-1] == '*') {
            dp[0][j] = dp[0][j-1];
        }
    }
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (p[j-1] == '*') {
                dp[i][j] = dp[i][j-1] || dp[i-1][j];
            } else if (p[j-1] == '?' || p[j-1] == s[i-1]) {
                dp[i][j] = dp[i-1][j-1];
            }
        }
    }
    
    return dp[m][n];
}
```

#### 7. Longest Palindromic Substring

**Problem:** Find the longest contiguous substring that is a palindrome.

```
State: dp[i][j] = true if s[i..j] is palindrome
Base: dp[i][i] = true, dp[i][i+1] = (s[i] == s[i+1])
Transition: dp[i][j] = (s[i] == s[j]) AND dp[i+1][j-1]
```

```cpp
string longestPalindrome(string s) {
    int n = s.length();
    vector<vector<bool>> dp(n, vector<bool>(n, false));
    int start = 0, maxLen = 1;
    
    // All single characters are palindromes
    for (int i = 0; i < n; i++) {
        dp[i][i] = true;
    }
    
    // Check for length 2
    for (int i = 0; i < n-1; i++) {
        if (s[i] == s[i+1]) {
            dp[i][i+1] = true;
            start = i;
            maxLen = 2;
        }
    }
    
    // Check for length >= 3
    for (int len = 3; len <= n; len++) {
        for (int i = 0; i <= n-len; i++) {
            int j = i + len - 1;
            if (s[i] == s[j] && dp[i+1][j-1]) {
                dp[i][j] = true;
                start = i;
                maxLen = len;
            }
        }
    }
    
    return s.substr(start, maxLen);
}
```

#### 8. Distinct Subsequences

**Problem:** Count distinct subsequences of s that equal t.

```
State: dp[i][j] = number of distinct subsequences of s[0..i-1] that equal t[0..j-1]
Base: dp[i][0] = 1 for all i
Transition:
    if s[i-1] == t[j-1]:
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    else:
        dp[i][j] = dp[i-1][j]
```

```cpp
int numDistinct(string s, string t) {
    int m = s.length(), n = t.length();
    vector<vector<long long>> dp(m+1, vector<long long>(n+1, 0));
    
    for (int i = 0; i <= m; i++) {
        dp[i][0] = 1;
    }
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            dp[i][j] = dp[i-1][j];
            if (s[i-1] == t[j-1]) {
                dp[i][j] += dp[i-1][j-1];
            }
        }
    }
    
    return dp[m][n];
}
```

#### 9. Minimum Insertion Steps to Make String Palindrome

**Problem:** Minimum insertions to make a string palindrome.

```
This equals length of string minus length of longest palindromic subsequence.
```

```cpp
int minInsertions(string s) {
    int n = s.length();
    return n - longestPalindromeSubseq(s);
}
```

#### 10. Interleaving String

**Problem:** Check if s3 is formed by interleaving s1 and s2.

```
State: dp[i][j] = true if s3[0..i+j-1] is interleaving of s1[0..i-1] and s2[0..j-1]
Base: dp[0][0] = true
Transition:
    if i > 0 and s1[i-1] == s3[i+j-1]:
        dp[i][j] = dp[i][j] or dp[i-1][j]
    if j > 0 and s2[j-1] == s3[i+j-1]:
        dp[i][j] = dp[i][j] or dp[i][j-1]
```

```cpp
bool isInterleave(string s1, string s2, string s3) {
    int m = s1.length(), n = s2.length();
    if (m + n != s3.length()) return false;
    
    vector<vector<bool>> dp(m+1, vector<bool>(n+1, false));
    dp[0][0] = true;
    
    for (int i = 1; i <= m; i++) {
        dp[i][0] = dp[i-1][0] && (s1[i-1] == s3[i-1]);
    }
    for (int j = 1; j <= n; j++) {
        dp[0][j] = dp[0][j-1] && (s2[j-1] == s3[j-1]);
    }
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (s1[i-1] == s3[i+j-1]) {
                dp[i][j] = dp[i][j] || dp[i-1][j];
            }
            if (s2[j-1] == s3[i+j-1]) {
                dp[i][j] = dp[i][j] || dp[i][j-1];
            }
        }
    }
    
    return dp[m][n];
}
```

### Summary Table

| Problem | Time Complexity | Space Complexity |
|---------|----------------|------------------|
| LCS | O(m × n) | O(min(m, n)) |
| Longest Common Substring | O(m × n) | O(m × n) |
| Edit Distance | O(m × n) | O(min(m, n)) |
| Regular Expression Matching | O(m × n) | O(m × n) |
| Wildcard Matching | O(m × n) | O(m × n) |
| Longest Palindromic Substring | O(n²) | O(n²) |
| Distinct Subsequences | O(m × n) | O(m × n) |
| Interleaving String | O(m × n) | O(m × n) |
