# 14_Palindrome_Partitioning.md

## Palindrome Partitioning

### Definition

Given a string, partition it into substrings such that every substring is a palindrome. Return all possible palindrome partitioning.

### Problem Statement

Input:
- A string s

Output:
- All possible ways to partition s into palindromic substrings

### Visual Example

```
Input: "aab"

Output:
["a", "a", "b"]
["aa", "b"]
```

### Backtracking Approach

```
Step 1: Start with empty partition
Step 2: For each possible substring starting at current index
Step 3: Check if substring is palindrome
Step 4: If yes, add to current partition and recurse
Step 5: When end of string reached, record partition
Step 6: Backtrack by removing last substring
```

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isPalindrome(string& s, int start, int end) {
    while (start < end) {
        if (s[start] != s[end]) {
            return false;
        }
        start++;
        end--;
    }
    return true;
}

void partition(string& s, int start, vector<string>& current, vector<vector<string>>& result) {
    // Base case: reached end of string
    if (start == s.length()) {
        result.push_back(current);
        return;
    }
    
    for (int end = start; end < s.length(); end++) {
        if (isPalindrome(s, start, end)) {
            // Add current palindrome substring
            current.push_back(s.substr(start, end - start + 1));
            
            // Recurse for remaining string
            partition(s, end + 1, current, result);
            
            // Backtrack
            current.pop_back();
        }
    }
}

vector<vector<string>> partition(string s) {
    vector<vector<string>> result;
    vector<string> current;
    partition(s, 0, current, result);
    return result;
}

int main() {
    string s = "aab";
    vector<vector<string>> result = partition(s);
    
    cout << "All palindrome partitions of \"" << s << "\":" << endl;
    for (auto& part : result) {
        cout << "[ ";
        for (string& str : part) {
            cout << "\"" << str << "\" ";
        }
        cout << "]" << endl;
    }
    
    return 0;
}
```

### Example Walkthrough (s = "aab")

```
Start: start=0, current=[]

end=0: substring "a" is palindrome
    current=["a"], recurse start=1
    
    start=1:
        end=1: substring "a" is palindrome
            current=["a","a"], recurse start=2
            
            start=2:
                end=2: substring "b" is palindrome
                    current=["a","a","b"], recurse start=3
                    
                    start=3 == n → record ["a","a","b"]
                    backtrack: remove "b"
                end=3: out of bounds
            backtrack: remove "a"
        
        end=2: substring "ab" is not palindrome → skip
        
        end=3: out of bounds
    backtrack: remove "a"

end=1: substring "aa" is palindrome
    current=["aa"], recurse start=2
    
    start=2:
        end=2: substring "b" is palindrome
            current=["aa","b"], recurse start=3
            
            start=3 == n → record ["aa","b"]
            backtrack: remove "b"
    backtrack: remove "aa"

end=2: substring "aab" is not palindrome → skip

Result: [["a","a","b"], ["aa","b"]]
```

### Recursion Tree

```
                                    "aab"
                                    │
                ┌───────────────────┼───────────────────┐
                │                   │                   │
              "a"                  "aa"                "aab"
                │                   │                   │
              "ab"                  "b"                (invalid)
                │                   │
            ┌───┴───┐               │
           "a"     "b"             [ ]
            │       │
           "b"     [ ]
            │
           [ ]
```

### Optimized with DP Precomputation

Precompute palindrome table to avoid repeated checks.

```cpp
vector<vector<string>> partitionOptimized(string s) {
    int n = s.length();
    
    // Precompute palindrome table
    vector<vector<bool>> isPal(n, vector<bool>(n, false));
    
    for (int i = 0; i < n; i++) {
        isPal[i][i] = true;
    }
    
    for (int len = 2; len <= n; len++) {
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            if (s[i] == s[j]) {
                isPal[i][j] = (len == 2) || isPal[i+1][j-1];
            }
        }
    }
    
    vector<vector<string>> result;
    vector<string> current;
    
    function<void(int)> backtrack = [&](int start) {
        if (start == n) {
            result.push_back(current);
            return;
        }
        
        for (int end = start; end < n; end++) {
            if (isPal[start][end]) {
                current.push_back(s.substr(start, end - start + 1));
                backtrack(end + 1);
                current.pop_back();
            }
        }
    };
    
    backtrack(0);
    return result;
}
```

### Minimum Cuts for Palindrome Partitioning

Find the minimum cuts needed to partition string into palindromic substrings.

```cpp
int minCut(string s) {
    int n = s.length();
    
    // Precompute palindrome table
    vector<vector<bool>> isPal(n, vector<bool>(n, false));
    
    for (int i = 0; i < n; i++) {
        isPal[i][i] = true;
    }
    
    for (int len = 2; len <= n; len++) {
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            if (s[i] == s[j]) {
                isPal[i][j] = (len == 2) || isPal[i+1][j-1];
            }
        }
    }
    
    // DP for minimum cuts
    vector<int> dp(n, INT_MAX);
    
    for (int i = 0; i < n; i++) {
        if (isPal[0][i]) {
            dp[i] = 0;
        } else {
            for (int j = 0; j < i; j++) {
                if (isPal[j+1][i]) {
                    dp[i] = min(dp[i], dp[j] + 1);
                }
            }
        }
    }
    
    return dp[n-1];
}
```

### Number of Palindrome Partitions

| String | Number of Partitions |
|--------|---------------------|
| "a" | 1 |
| "aa" | 2 |
| "ab" | 1 |
| "aab" | 2 |
| "aaa" | 4 |
| "aba" | 2 |
| "abcba" | 4 |

### Time Complexity

| Complexity | Value |
|------------|-------|
| Without DP | O(n × 2^n) |
| With DP precomputation | O(n² + number of partitions) |

### Space Complexity

O(n²) for palindrome table + O(n) for recursion

### Variations

#### 1. Palindrome Partitioning with K Substrings

Partition into exactly k palindromic substrings.

#### 2. Longest Palindromic Substring

Find the longest palindrome within the string (not partitioning).

#### 3. Palindrome Partitioning with Distinct Substrings

Count partitions where all substrings are distinct.

### Practice Problems

1. Return all palindrome partitions of a string
2. Find the minimum cuts needed for palindrome partitioning
3. Count the number of palindrome partitions
4. Find the longest palindrome substring
5. Check if a string can be partitioned into k palindromic substrings