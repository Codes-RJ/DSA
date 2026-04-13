# 13_Longest_Common_Subsequence.md

## Longest Common Subsequence (LCS)

### Definition

Given two strings (or sequences), a subsequence is a sequence that appears in the same relative order but not necessarily contiguous. The Longest Common Subsequence (LCS) is the longest subsequence that appears in both strings.

### Example

```
String A: "ABCDGH"
String B: "AEDFHR"

LCS: "ADH" (length 3)

Explanation:
A B C D G H
A E D F H R
- A - D - H
```

### Problem Statement

Find the length of the longest subsequence common to two strings.

### Mathematical Formulation

```
Let dp[i][j] = length of LCS of A[0..i-1] and B[0..j-1]

Base cases:
dp[0][j] = 0 for all j (empty string with any string)
dp[i][0] = 0 for all i

Transition:
if A[i-1] == B[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

Answer: dp[m][n]
```

### Basic Implementation (2D)

```cpp
int longestCommonSubsequence(string text1, string text2) {
    int m = text1.length();
    int n = text2.length();
    
    vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (text1[i-1] == text2[j-1]) {
                dp[i][j] = dp[i-1][j-1] + 1;
            } else {
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    
    return dp[m][n];
}
```

### Space Optimized Implementation (2 Rows)

Since dp[i][j] only depends on current row and previous row, we can optimize space to O(min(m, n)).

```cpp
int longestCommonSubsequence(string text1, string text2) {
    int m = text1.length();
    int n = text2.length();
    
    // Ensure m is the smaller dimension for better space
    if (m < n) {
        swap(text1, text2);
        swap(m, n);
    }
    
    vector<int> dp(n+1, 0);
    vector<int> prev(n+1, 0);
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (text1[i-1] == text2[j-1]) {
                dp[j] = prev[j-1] + 1;
            } else {
                dp[j] = max(prev[j], dp[j-1]);
            }
        }
        swap(dp, prev);
    }
    
    return prev[n];
}
```

### Reconstructing the LCS String

To get the actual subsequence, not just the length, we trace back from dp[m][n].

```cpp
string getLCS(string text1, string text2) {
    int m = text1.length();
    int n = text2.length();
    
    vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (text1[i-1] == text2[j-1]) {
                dp[i][j] = dp[i-1][j-1] + 1;
            } else {
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    
    // Reconstruct
    string lcs = "";
    int i = m, j = n;
    
    while (i > 0 && j > 0) {
        if (text1[i-1] == text2[j-1]) {
            lcs = text1[i-1] + lcs;
            i--;
            j--;
        } else if (dp[i-1][j] > dp[i][j-1]) {
            i--;
        } else {
            j--;
        }
    }
    
    return lcs;
}
```

### Variations of LCS

#### 1. Longest Common Substring (Contiguous)

**Difference:** Substring must be contiguous, unlike subsequence.

```
State: dp[i][j] = length of longest common SUFFIX ending at i, j
Transition:
    if A[i] == B[j]:
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

#### 2. Shortest Common Supersequence (SCS)

**Problem:** Find the shortest string that contains both strings as subsequences.

```
SCS length = m + n - LCS length

To reconstruct:
- Take common characters once from LCS
- Add remaining characters from both strings
```

```cpp
string shortestCommonSupersequence(string str1, string str2) {
    int m = str1.length(), n = str2.length();
    vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (str1[i-1] == str2[j-1]) {
                dp[i][j] = dp[i-1][j-1] + 1;
            } else {
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    
    // Reconstruct SCS
    string result = "";
    int i = m, j = n;
    
    while (i > 0 && j > 0) {
        if (str1[i-1] == str2[j-1]) {
            result = str1[i-1] + result;
            i--;
            j--;
        } else if (dp[i-1][j] > dp[i][j-1]) {
            result = str1[i-1] + result;
            i--;
        } else {
            result = str2[j-1] + result;
            j--;
        }
    }
    
    while (i > 0) {
        result = str1[i-1] + result;
        i--;
    }
    while (j > 0) {
        result = str2[j-1] + result;
        j--;
    }
    
    return result;
}
```

#### 3. Longest Palindromic Subsequence (LPS)

**Problem:** Find the longest subsequence that is a palindrome.

**Method:** Reverse the string and find LCS with original.

```
LPS(s) = LCS(s, reverse(s))
```

```cpp
int longestPalindromeSubseq(string s) {
    string rev = s;
    reverse(rev.begin(), rev.end());
    return longestCommonSubsequence(s, rev);
}
```

#### 4. Minimum Insertions to Make String Palindrome

**Problem:** Minimum insertions to make a string palindrome.

```
Answer = n - LPS(s)
```

```cpp
int minInsertionsToPalindrome(string s) {
    return s.length() - longestPalindromeSubseq(s);
}
```

#### 5. Minimum Deletions to Make String Palindrome

**Problem:** Minimum deletions to make a string palindrome.

```
Answer = n - LPS(s)
```

```cpp
int minDeletionsToPalindrome(string s) {
    return s.length() - longestPalindromeSubseq(s);
}
```

#### 6. Longest Common Increasing Subsequence

**Problem:** Find the longest subsequence that is both common and increasing.

This is more complex and usually solved with O(n² log n) or O(n³) DP.

#### 7. Edit Distance (Closely Related)

LCS is closely related to edit distance where only insertions and deletions are allowed (no replacements).

```
Edit Distance (with only insert/delete) = m + n - 2 * LCS
```

### LCS with Multiple Strings

**Problem:** Find LCS of k strings (k > 2).

This becomes exponential and is often solved with DP state dp[i1][i2][...][ik] which is O(n^k).

### Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Basic 2D DP | O(m × n) | O(m × n) |
| Space Optimized | O(m × n) | O(min(m, n)) |
| Recursive with Memo | O(m × n) | O(m × n) + stack |
---

## Next Step

- Go to [14_Longest_Increasing_Subsequence.md](14_Longest_Increasing_Subsequence.md) to continue with Longest Increasing Subsequence.
