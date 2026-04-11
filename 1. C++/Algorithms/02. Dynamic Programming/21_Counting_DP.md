# 21_Counting_DP.md

## Counting DP

### Definition

Counting DP is a technique used to count the number of ways to achieve a certain configuration or satisfy certain constraints. Instead of finding maximum or minimum, we count possibilities.

### Key Difference

| Type | Goal | Operation |
|------|------|-----------|
| Optimization DP | Find best value | max(), min() |
| Counting DP | Count number of ways | sum() |

### Important Considerations

- Use modulo to prevent overflow (usually 10^9+7)
- Be careful with double counting
- Ensure base cases are correct
- Order of transitions matters (combinations vs permutations)

### Classic Counting DP Problems

#### 1. Number of Ways to Climb Stairs

**Problem:** Count ways to reach step n using 1 or 2 steps.

```cpp
int climbStairs(int n) {
    if (n <= 1) return 1;
    vector<int> dp(n + 1, 0);
    dp[0] = 1;
    dp[1] = 1;
    
    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    
    return dp[n];
}
```

#### 2. Number of Ways to Reach Bottom-Right (Unique Paths)

```cpp
int uniquePaths(int m, int n) {
    vector<vector<int>> dp(m, vector<int>(n, 1));
    
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = dp[i-1][j] + dp[i][j-1];
        }
    }
    
    return dp[m-1][n-1];
}
```

#### 3. Number of Ways to Make Change (Coin Change II)

**Problem:** Count number of combinations to make amount using given coins.

```cpp
int change(int amount, vector<int>& coins) {
    vector<int> dp(amount + 1, 0);
    dp[0] = 1;
    
    for (int coin : coins) {
        for (int a = coin; a <= amount; a++) {
            dp[a] += dp[a - coin];
        }
    }
    
    return dp[amount];
}
```

#### 4. Number of Ways to Partition Array into K Subsets with Equal Sum

```cpp
bool canPartitionKSubsets(vector<int>& nums, int k) {
    int total = accumulate(nums.begin(), nums.end(), 0);
    if (total % k != 0) return false;
    int target = total / k;
    
    sort(nums.begin(), nums.end(), greater<int>());
    vector<int> subsets(k, 0);
    
    function<bool(int)> dfs = [&](int index) {
        if (index == nums.size()) return true;
        
        for (int i = 0; i < k; i++) {
            if (subsets[i] + nums[index] <= target) {
                subsets[i] += nums[index];
                if (dfs(index + 1)) return true;
                subsets[i] -= nums[index];
            }
            if (subsets[i] == 0) break;
        }
        return false;
    };
    
    return dfs(0);
}
```

#### 5. Number of Ways to Decode String

```cpp
int numDecodings(string s) {
    int n = s.length();
    if (n == 0 || s[0] == '0') return 0;
    
    vector<int> dp(n + 1, 0);
    dp[0] = 1;
    dp[1] = 1;
    
    for (int i = 2; i <= n; i++) {
        int oneDigit = s[i-1] - '0';
        int twoDigits = (s[i-2] - '0') * 10 + oneDigit;
        
        if (oneDigit != 0) dp[i] += dp[i-1];
        if (twoDigits >= 10 && twoDigits <= 26) dp[i] += dp[i-2];
    }
    
    return dp[n];
}
```

#### 6. Number of Ways to Stay in Place

**Problem:** Count ways to stay at index 0 after exactly steps moves. Can move left, right, or stay.

```cpp
int numWays(int steps, int arrLen) {
    int maxPos = min(arrLen - 1, steps);
    vector<long long> dp(maxPos + 2, 0);
    vector<long long> next(maxPos + 2, 0);
    int MOD = 1e9 + 7;
    
    dp[0] = 1;
    
    for (int step = 0; step < steps; step++) {
        fill(next.begin(), next.end(), 0);
        for (int pos = 0; pos <= maxPos; pos++) {
            next[pos] = (next[pos] + dp[pos]) % MOD;  // stay
            if (pos > 0) next[pos] = (next[pos] + dp[pos-1]) % MOD;  // left
            if (pos < maxPos) next[pos] = (next[pos] + dp[pos+1]) % MOD;  // right
        }
        swap(dp, next);
    }
    
    return dp[0];
}
```

#### 7. Number of Ways to Form Target String

**Problem:** Count ways to form target by picking characters from multiple strings.

```cpp
int numWays(vector<string>& words, string target) {
    int n = words[0].length();
    int m = target.length();
    int MOD = 1e9 + 7;
    
    vector<vector<int>> freq(n, vector<int>(26, 0));
    for (string& word : words) {
        for (int i = 0; i < n; i++) {
            freq[i][word[i] - 'a']++;
        }
    }
    
    vector<vector<long long>> dp(m + 1, vector<long long>(n + 1, 0));
    dp[0][0] = 1;
    
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j < n; j++) {
            dp[i][j+1] = (dp[i][j+1] + dp[i][j]) % MOD;
            if (i < m) {
                dp[i+1][j+1] = (dp[i+1][j+1] + dp[i][j] * freq[j][target[i] - 'a']) % MOD;
            }
        }
    }
    
    return dp[m][n];
}
```

#### 8. Number of Ways to Distribute N Candies to K Children

**Problem:** Count ways to distribute n identical candies to k distinct children with each child getting at least 1 candy.

```cpp
int distributeCandies(int n, int k) {
    // Stars and bars: C(n-1, k-1)
    if (n < k) return 0;
    
    vector<vector<long long>> C(n + 1, vector<long long>(k + 1, 0));
    int MOD = 1e9 + 7;
    
    for (int i = 0; i <= n; i++) {
        C[i][0] = 1;
        for (int j = 1; j <= min(i, k); j++) {
            C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD;
        }
    }
    
    return C[n-1][k-1];
}
```

#### 9. Number of Ways to Color N x M Grid

**Problem:** Count ways to color grid with 3 colors such that no two adjacent cells have same color.

```cpp
int colorGrid(int n, int m) {
    int MOD = 1e9 + 7;
    
    // Generate all valid rows (no adjacent same color)
    vector<int> validRows;
    for (int mask = 0; mask < (1 << (2 * m)); mask++) {
        vector<int> colors(m);
        bool valid = true;
        for (int i = 0; i < m; i++) {
            colors[i] = (mask >> (2 * i)) & 3;
            if (i > 0 && colors[i] == colors[i-1]) {
                valid = false;
                break;
            }
        }
        if (valid) validRows.push_back(mask);
    }
    
    // Check if two rows are compatible
    int r = validRows.size();
    vector<vector<bool>> compatible(r, vector<bool>(r, false));
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < r; j++) {
            vector<int> row1(m), row2(m);
            for (int k = 0; k < m; k++) {
                row1[k] = (validRows[i] >> (2 * k)) & 3;
                row2[k] = (validRows[j] >> (2 * k)) & 3;
                if (row1[k] == row2[k]) {
                    compatible[i][j] = false;
                    break;
                }
                compatible[i][j] = true;
            }
        }
    }
    
    // DP
    vector<long long> dp(r, 1);
    for (int row = 1; row < n; row++) {
        vector<long long> next(r, 0);
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < r; j++) {
                if (compatible[i][j]) {
                    next[j] = (next[j] + dp[i]) % MOD;
                }
            }
        }
        dp = next;
    }
    
    long long ans = 0;
    for (int i = 0; i < r; i++) {
        ans = (ans + dp[i]) % MOD;
    }
    
    return ans;
}
```

#### 10. Number of Ways to Arrange Balls in Boxes

**Problem:** Count ways to arrange n distinct balls into k identical boxes.

This is Stirling numbers of the second kind.

```cpp
int stirlingNumber(int n, int k) {
    int MOD = 1e9 + 7;
    vector<vector<long long>> S(n + 1, vector<long long>(k + 1, 0));
    S[0][0] = 1;
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= min(i, k); j++) {
            S[i][j] = (S[i-1][j-1] + j * S[i-1][j]) % MOD;
        }
    }
    
    return S[n][k];
}
```

#### 11. Number of Ways to Parenthesize Expression (Catalan Numbers)

**Problem:** Count number of ways to parenthesize n matrices.

Catalan number: C_n = (1/(n+1)) * C(2n, n)

```cpp
int catalanNumber(int n) {
    int MOD = 1e9 + 7;
    vector<long long> dp(n + 1, 0);
    dp[0] = 1;
    
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) {
            dp[i] = (dp[i] + dp[j] * dp[i - 1 - j]) % MOD;
        }
    }
    
    return dp[n];
}
```

### Counting DP Patterns Summary

| Problem Type | DP State | Transition |
|--------------|----------|------------|
| Linear Counting | dp[i] | dp[i] = sum(dp[i - step]) |
| Grid Counting | dp[i][j] | dp[i][j] = dp[i-1][j] + dp[i][j-1] |
| Coin Change (Combinations) | dp[amount] | dp[a] += dp[a - coin] (coin outer) |
| Coin Change (Permutations) | dp[amount] | dp[a] += dp[a - coin] (amount outer) |
| Partition Counting | dp[n][k] | dp[i][j] = dp[i-1][j-1] + j*dp[i-1][j] |
| Catalan Numbers | dp[n] | dp[i] = sum(dp[j] * dp[i-1-j]) |

### Modulo Operations

When counting large numbers, always use modulo:

```cpp
const int MOD = 1e9 + 7;

dp[i] = (dp[i] + dp[i-1]) % MOD;
dp[i] = (dp[i] + dp[i-2]) % MOD;
```

### Common Mistakes in Counting DP

1. Forgetting modulo operations
2. Double counting due to order (combinations vs permutations)
3. Incorrect base cases (dp[0] = 0 vs dp[0] = 1)
4. Integer overflow before modulo
5. Not handling large numbers with long long
