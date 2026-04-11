# 15_Edit_Distance.md

## Edit Distance (Levenshtein Distance)

### Definition

Edit Distance is the minimum number of operations required to convert one string into another. The allowed operations are:

1. **Insert** a character
2. **Delete** a character
3. **Replace** a character

### Example

```
String A: "horse"
String B: "ros"

Operations:
horse → rose (replace 'h' with 'r')
rose → ros  (delete 'e')
Total: 2 operations
```

### Problem Statement

Given two strings word1 and word2, find the minimum number of operations to convert word1 to word2.

### Mathematical Formulation

```
Let dp[i][j] = minimum operations to convert word1[0..i-1] to word2[0..j-1]

Base cases:
dp[0][j] = j  (need to insert j characters)
dp[i][0] = i  (need to delete i characters)

Transition:
if word1[i-1] == word2[j-1]:
    dp[i][j] = dp[i-1][j-1]  (no operation needed)
else:
    dp[i][j] = 1 + min(
        dp[i-1][j],    // delete from word1
        dp[i][j-1],    // insert into word1
        dp[i-1][j-1]   // replace
    )

Answer: dp[m][n]
```

### Basic Implementation (2D)

```cpp
int minDistance(string word1, string word2) {
    int m = word1.length();
    int n = word2.length();
    
    vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
    
    // Base cases
    for (int i = 0; i <= m; i++) {
        dp[i][0] = i;
    }
    for (int j = 0; j <= n; j++) {
        dp[0][j] = j;
    }
    
    // Fill the table
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (word1[i-1] == word2[j-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = 1 + min({dp[i-1][j],     // delete
                                    dp[i][j-1],     // insert
                                    dp[i-1][j-1]}); // replace
            }
        }
    }
    
    return dp[m][n];
}
```

### Space Optimized Implementation (2 Rows)

Since dp[i][j] only depends on current row and previous row, we can optimize space to O(n).

```cpp
int minDistance(string word1, string word2) {
    int m = word1.length();
    int n = word2.length();
    
    // Ensure word2 is the shorter one for better space
    if (m < n) {
        swap(word1, word2);
        swap(m, n);
    }
    
    vector<int> dp(n+1, 0);
    vector<int> prev(n+1, 0);
    
    // Initialize first row
    for (int j = 0; j <= n; j++) {
        prev[j] = j;
    }
    
    for (int i = 1; i <= m; i++) {
        dp[0] = i;  // first column
        
        for (int j = 1; j <= n; j++) {
            if (word1[i-1] == word2[j-1]) {
                dp[j] = prev[j-1];
            } else {
                dp[j] = 1 + min({prev[j],     // delete
                                 dp[j-1],     // insert
                                 prev[j-1]}); // replace
            }
        }
        swap(dp, prev);
    }
    
    return prev[n];
}
```

### Even More Space Optimized (1 Row - Tricky)

We can use just one row if we store the diagonal value separately.

```cpp
int minDistance(string word1, string word2) {
    int m = word1.length();
    int n = word2.length();
    
    if (m < n) {
        swap(word1, word2);
        swap(m, n);
    }
    
    vector<int> dp(n+1);
    for (int j = 0; j <= n; j++) {
        dp[j] = j;
    }
    
    for (int i = 1; i <= m; i++) {
        int prevDiag = dp[0];  // dp[i-1][j-1]
        dp[0] = i;
        
        for (int j = 1; j <= n; j++) {
            int temp = dp[j];  // store for next diagonal
            if (word1[i-1] == word2[j-1]) {
                dp[j] = prevDiag;
            } else {
                dp[j] = 1 + min({dp[j],      // delete
                                 dp[j-1],    // insert
                                 prevDiag}); // replace
            }
            prevDiag = temp;
        }
    }
    
    return dp[n];
}
```

### Reconstructing the Operations

To get the actual sequence of operations, we trace back from dp[m][n].

```cpp
vector<string> getEditOperations(string word1, string word2) {
    int m = word1.length();
    int n = word2.length();
    
    vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
    
    for (int i = 0; i <= m; i++) dp[i][0] = i;
    for (int j = 0; j <= n; j++) dp[0][j] = j;
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (word1[i-1] == word2[j-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = 1 + min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]});
            }
        }
    }
    
    // Reconstruct
    vector<string> operations;
    int i = m, j = n;
    
    while (i > 0 || j > 0) {
        if (i > 0 && j > 0 && word1[i-1] == word2[j-1]) {
            operations.push_back("keep '" + string(1, word1[i-1]) + "'");
            i--; j--;
        }
        else if (i > 0 && j > 0 && dp[i][j] == dp[i-1][j-1] + 1) {
            operations.push_back("replace '" + string(1, word1[i-1]) + 
                                 "' with '" + string(1, word2[j-1]) + "'");
            i--; j--;
        }
        else if (i > 0 && dp[i][j] == dp[i-1][j] + 1) {
            operations.push_back("delete '" + string(1, word1[i-1]) + "'");
            i--;
        }
        else if (j > 0 && dp[i][j] == dp[i][j-1] + 1) {
            operations.push_back("insert '" + string(1, word2[j-1]) + "'");
            j--;
        }
    }
    
    reverse(operations.begin(), operations.end());
    return operations;
}
```

### Variations of Edit Distance

#### 1. Edit Distance with Different Costs

Each operation can have different costs.

```cpp
int minDistanceWithCosts(string word1, string word2, 
                         int insertCost, int deleteCost, int replaceCost) {
    int m = word1.length();
    int n = word2.length();
    
    vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
    
    for (int i = 0; i <= m; i++) dp[i][0] = i * deleteCost;
    for (int j = 0; j <= n; j++) dp[0][j] = j * insertCost;
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (word1[i-1] == word2[j-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = min({
                    dp[i-1][j] + deleteCost,
                    dp[i][j-1] + insertCost,
                    dp[i-1][j-1] + replaceCost
                });
            }
        }
    }
    
    return dp[m][n];
}
```

#### 2. Minimum Edit Distance with Only Insert and Delete

```
This is equivalent to: m + n - 2 * LCS(word1, word2)
```

#### 3. One Edit Distance

**Problem:** Check if two strings are exactly one edit away.

```cpp
bool isOneEditDistance(string s, string t) {
    int m = s.length();
    int n = t.length();
    
    if (abs(m - n) > 1) return false;
    
    if (m == n) {
        int diff = 0;
        for (int i = 0; i < m; i++) {
            if (s[i] != t[i]) diff++;
            if (diff > 1) return false;
        }
        return diff == 1;
    }
    
    // One string is longer by 1
    if (m > n) swap(s, t);
    
    for (int i = 0; i < s.length(); i++) {
        if (s[i] != t[i]) {
            return s.substr(i) == t.substr(i+1);
        }
    }
    
    return true;
}
```

#### 4. Damerau-Levenshtein Distance

Includes an additional operation: **transposition** (swap two adjacent characters).

```
Allowed operations: insert, delete, replace, swap
```

```cpp
int damerauLevenshteinDistance(string a, string b) {
    int m = a.length();
    int n = b.length();
    vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
    
    for (int i = 0; i <= m; i++) dp[i][0] = i;
    for (int j = 0; j <= n; j++) dp[0][j] = j;
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            int cost = (a[i-1] == b[j-1]) ? 0 : 1;
            dp[i][j] = min({
                dp[i-1][j] + 1,     // delete
                dp[i][j-1] + 1,     // insert
                dp[i-1][j-1] + cost // replace
            });
            
            // Transposition
            if (i > 1 && j > 1 && a[i-1] == b[j-2] && a[i-2] == b[j-1]) {
                dp[i][j] = min(dp[i][j], dp[i-2][j-2] + 1);
            }
        }
    }
    
    return dp[m][n];
}
```

### Applications of Edit Distance

| Application | Description |
|-------------|-------------|
| Spell Checking | Suggest corrections for misspelled words |
| DNA Sequence Alignment | Find similarity between DNA sequences |
| Plagiarism Detection | Compare documents for similarity |
| Natural Language Processing | Measure string similarity |
| Version Control | Show differences between file versions |

### Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Basic 2D DP | O(m × n) | O(m × n) |
| 2-Row Optimization | O(m × n) | O(n) |
| 1-Row Optimization | O(m × n) | O(n) |
| Recursive with Memo | O(m × n) | O(m × n) + stack |