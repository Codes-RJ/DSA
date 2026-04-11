# 20_DP_on_Intervals.md

## DP on Intervals

### Definition

Interval DP is a technique where the state represents a contiguous subarray or substring from index i to j. The solution is built by combining solutions of smaller intervals.

### Key Concept

The state is typically `dp[i][j]` representing the optimal solution for the interval from i to j. We compute intervals in increasing order of length.

### General Template

```
for length = 1 to n:
    for i = 0 to n - length:
        j = i + length - 1
        dp[i][j] = initial value
        for k = i to j-1:
            dp[i][j] = max/min(dp[i][j], dp[i][k] + dp[k+1][j] + cost(i, j, k))
```

### Classic Interval DP Problems

#### 1. Matrix Chain Multiplication

Already covered in file 16.

#### 2. Burst Balloons

**Problem:** Given balloons with coins, bursting balloon i gives coins = nums[i-1] * nums[i] * nums[i+1]. Find maximum coins after bursting all balloons.

```
State: dp[i][j] = max coins from bursting balloons i to j
Transition: dp[i][j] = max over k of (dp[i][k-1] + dp[k+1][j] + nums[i-1] * nums[k] * nums[j+1])
Answer: dp[1][n]
```

```cpp
int maxCoins(vector<int>& nums) {
    int n = nums.size();
    vector<int> arr(n + 2, 1);
    for (int i = 1; i <= n; i++) {
        arr[i] = nums[i-1];
    }
    
    vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));
    
    for (int len = 1; len <= n; len++) {
        for (int i = 1; i <= n - len + 1; i++) {
            int j = i + len - 1;
            for (int k = i; k <= j; k++) {
                int coins = dp[i][k-1] + dp[k+1][j] + arr[i-1] * arr[k] * arr[j+1];
                dp[i][j] = max(dp[i][j], coins);
            }
        }
    }
    
    return dp[1][n];
}
```

#### 3. Stone Game

**Problem:** Two players take turns picking stones from either end. Each player wants to maximize their sum. Find maximum score the first player can achieve.

```
State: dp[i][j] = maximum score difference (first player - second player) for piles i to j
Transition: dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
Answer: (total + dp[0][n-1]) / 2 (first player's score)
```

```cpp
bool stoneGame(vector<int>& piles) {
    int n = piles.size();
    vector<vector<int>> dp(n, vector<int>(n, 0));
    
    for (int i = 0; i < n; i++) {
        dp[i][i] = piles[i];
    }
    
    for (int len = 2; len <= n; len++) {
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1]);
        }
    }
    
    return dp[0][n-1] > 0;
}
```

#### 4. Palindrome Partitioning (Minimum Cuts)

**Problem:** Partition string into palindromes with minimum cuts.

```
State: isPal[i][j] = true if s[i..j] is palindrome
       dp[i] = min cuts for s[0..i]
Transition: if isPal[j][i] then dp[i] = min(dp[i], dp[j-1] + 1)
Answer: dp[n-1]
```

```cpp
int minCut(string s) {
    int n = s.length();
    vector<vector<bool>> isPal(n, vector<bool>(n, false));
    
    // Precompute palindromes
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

#### 5. Longest Palindromic Substring (Interval DP)

```cpp
string longestPalindrome(string s) {
    int n = s.length();
    vector<vector<bool>> dp(n, vector<bool>(n, false));
    int start = 0, maxLen = 1;
    
    for (int i = 0; i < n; i++) {
        dp[i][i] = true;
    }
    
    for (int i = 0; i < n-1; i++) {
        if (s[i] == s[i+1]) {
            dp[i][i+1] = true;
            start = i;
            maxLen = 2;
        }
    }
    
    for (int len = 3; len <= n; len++) {
        for (int i = 0; i <= n - len; i++) {
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

#### 6. Minimum Cost to Merge Stones

**Problem:** Merge piles into one pile with cost = sum of piles merged. Find minimum total cost.

```
State: dp[i][j] = min cost to merge piles i to j
Transition: dp[i][j] = min over k of (dp[i][k] + dp[k+1][j] + sum[i][j])
Answer: dp[0][n-1]
```

```cpp
int minCostToMergeStones(vector<int>& stones) {
    int n = stones.size();
    vector<int> prefix(n + 1, 0);
    for (int i = 0; i < n; i++) {
        prefix[i+1] = prefix[i] + stones[i];
    }
    
    vector<vector<int>> dp(n, vector<int>(n, 0));
    
    for (int len = 2; len <= n; len++) {
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            dp[i][j] = INT_MAX;
            int sum = prefix[j+1] - prefix[i];
            for (int k = i; k < j; k++) {
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + sum);
            }
        }
    }
    
    return dp[0][n-1];
}
```

#### 7. Optimal Binary Search Tree

Already covered in file 16.

#### 8. Remove Boxes

**Problem:** Remove boxes to get points. Removing k boxes of same color gives k*k points.

```
State: dp[i][j][k] = max points from boxes i to j with k boxes of same color as boxes[i] attached to the left
Transition: 
    - Remove boxes[i] with attached boxes: dp[i+1][j][0] + (k+1)*(k+1)
    - Merge with same color later: find m where boxes[i] == boxes[m] and merge
```

```cpp
int removeBoxes(vector<int>& boxes) {
    int n = boxes.size();
    vector<vector<vector<int>>> dp(n, vector<vector<int>>(n, vector<int>(n, 0)));
    
    function<int(int, int, int)> dfs = [&](int i, int j, int k) {
        if (i > j) return 0;
        if (dp[i][j][k] > 0) return dp[i][j][k];
        
        // Remove boxes[i] with its attached k boxes
        int res = dfs(i + 1, j, 0) + (k + 1) * (k + 1);
        
        // Try to merge with same color later
        for (int m = i + 1; m <= j; m++) {
            if (boxes[m] == boxes[i]) {
                res = max(res, dfs(i + 1, m - 1, 0) + dfs(m, j, k + 1));
            }
        }
        
        dp[i][j][k] = res;
        return res;
    };
    
    return dfs(0, n - 1, 0);
}
```

#### 9. Predict the Winner

**Problem:** Two players pick from either end. Predict if first player can win.

```cpp
bool predictTheWinner(vector<int>& nums) {
    int n = nums.size();
    vector<vector<int>> dp(n, vector<int>(n, 0));
    
    for (int i = 0; i < n; i++) {
        dp[i][i] = nums[i];
    }
    
    for (int len = 2; len <= n; len++) {
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1]);
        }
    }
    
    return dp[0][n-1] >= 0;
}
```

#### 10. Strange Printer

**Problem:** Printer can print same character multiple times. Find minimum turns to print string.

```
State: dp[i][j] = min turns to print s[i..j]
Transition: 
    - dp[i][j] = dp[i+1][j] + 1
    - for k where s[i] == s[k]: dp[i][j] = min(dp[i][j], dp[i+1][k-1] + dp[k][j])
```

```cpp
int strangePrinter(string s) {
    int n = s.length();
    vector<vector<int>> dp(n, vector<int>(n, 0));
    
    for (int i = 0; i < n; i++) {
        dp[i][i] = 1;
    }
    
    for (int len = 2; len <= n; len++) {
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            dp[i][j] = dp[i+1][j] + 1;
            
            for (int k = i + 1; k <= j; k++) {
                if (s[i] == s[k]) {
                    dp[i][j] = min(dp[i][j], dp[i+1][k-1] + dp[k][j]);
                }
            }
        }
    }
    
    return dp[0][n-1];
}
```

### Interval DP Patterns Summary

| Problem | State | Transition Complexity |
|---------|-------|----------------------|
| Matrix Chain | dp[i][j] | O(n) per state |
| Burst Balloons | dp[i][j] | O(n) per state |
| Stone Game | dp[i][j] | O(1) per state |
| Palindrome Partitioning | dp[i] + isPal | O(1) per state after precompute |
| Merge Stones | dp[i][j] | O(n) per state |
| Remove Boxes | dp[i][j][k] | O(n) per state |
| Strange Printer | dp[i][j] | O(n) per state |