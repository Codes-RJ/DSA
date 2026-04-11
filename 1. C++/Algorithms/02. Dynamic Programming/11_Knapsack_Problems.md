# 11_Knapsack_Problems.md

## Knapsack Problems

### Definition

Knapsack problems are a family of optimization problems where you have a set of items, each with a weight and a value, and a knapsack with a weight capacity. The goal is to maximize the total value without exceeding the capacity.

### Types of Knapsack Problems

| Type | Description | Item Usage |
|------|-------------|-------------|
| 0/1 Knapsack | Each item can be taken at most once | 0 or 1 time |
| Unbounded Knapsack | Each item can be taken unlimited times | 0, 1, 2, ... |
| Bounded Knapsack | Each item has a maximum count | 0 to count[i] times |
| Fractional Knapsack | Items can be broken (Greedy, not DP) | Any fraction |

### 1. 0/1 Knapsack

**Problem:** Given n items with weights w[i] and values v[i], and capacity W. Maximize value. Each item can be taken at most once.

```
State: dp[i][c] = maximum value using first i items with capacity c
Base: dp[0][c] = 0 for all c
Transition:
    if c >= w[i-1]:
        dp[i][c] = max(dp[i-1][c], dp[i-1][c - w[i-1]] + v[i-1])
    else:
        dp[i][c] = dp[i-1][c]
Answer: dp[n][W]
```

**2D Implementation:**

```cpp
int knapsack01(int W, vector<int>& weights, vector<int>& values) {
    int n = weights.size();
    vector<vector<int>> dp(n+1, vector<int>(W+1, 0));
    
    for (int i = 1; i <= n; i++) {
        for (int c = 0; c <= W; c++) {
            if (c >= weights[i-1]) {
                dp[i][c] = max(dp[i-1][c], 
                               dp[i-1][c - weights[i-1]] + values[i-1]);
            } else {
                dp[i][c] = dp[i-1][c];
            }
        }
    }
    
    return dp[n][W];
}
```

**Space Optimized (1D array - reverse loop):**

```cpp
int knapsack01(int W, vector<int>& weights, vector<int>& values) {
    int n = weights.size();
    vector<int> dp(W+1, 0);
    
    for (int i = 0; i < n; i++) {
        for (int c = W; c >= weights[i]; c--) {
            dp[c] = max(dp[c], dp[c - weights[i]] + values[i]);
        }
    }
    
    return dp[W];
}
```

**Why reverse loop?** To prevent using the same item multiple times. Going backwards ensures dp[c - weights[i]] is from the previous iteration (i-1).

### 2. Unbounded Knapsack (Complete Knapsack)

**Problem:** Each item can be taken unlimited times.

```
State: dp[c] = maximum value with capacity c
Base: dp[0] = 0
Transition: dp[c] = max(dp[c], dp[c - w[i]] + v[i]) for each item
Answer: dp[W]
```

**Implementation (forward loop):**

```cpp
int unboundedKnapsack(int W, vector<int>& weights, vector<int>& values) {
    int n = weights.size();
    vector<int> dp(W+1, 0);
    
    for (int c = 0; c <= W; c++) {
        for (int i = 0; i < n; i++) {
            if (c >= weights[i]) {
                dp[c] = max(dp[c], dp[c - weights[i]] + values[i]);
            }
        }
    }
    
    return dp[W];
}
```

**Alternative (item loop first - forward):**

```cpp
int unboundedKnapsack(int W, vector<int>& weights, vector<int>& values) {
    int n = weights.size();
    vector<int> dp(W+1, 0);
    
    for (int i = 0; i < n; i++) {
        for (int c = weights[i]; c <= W; c++) {
            dp[c] = max(dp[c], dp[c - weights[i]] + values[i]);
        }
    }
    
    return dp[W];
}
```

**Why forward loop?** Forward loop allows the same item to be used multiple times because dp[c - weights[i]] may already include the current item.

### 3. Bounded Knapsack

**Problem:** Each item i has a maximum count of count[i].

**Approach 1: Convert to 0/1 by duplication**

Break each item into count[i] copies. Time: O(W * sum(count))

**Approach 2: Binary splitting**

Split count[i] into powers of 2. Example: count = 13 becomes 1, 2, 4, 6. Time: O(W * sum(log(count)))

**Approach 3: Monotone queue optimization**

Most efficient but complex.

**Binary splitting implementation:**

```cpp
int boundedKnapsack(int W, vector<int>& weights, vector<int>& values, vector<int>& counts) {
    int n = weights.size();
    vector<int> dp(W+1, 0);
    
    for (int i = 0; i < n; i++) {
        int remaining = counts[i];
        int k = 1;
        
        while (remaining > 0) {
            int take = min(k, remaining);
            int w = weights[i] * take;
            int v = values[i] * take;
            
            for (int c = W; c >= w; c--) {
                dp[c] = max(dp[c], dp[c - w] + v);
            }
            
            remaining -= take;
            k <<= 1;
        }
    }
    
    return dp[W];
}
```

### 4. Subset Sum Problem (Special 0/1 Knapsack)

**Problem:** Is there a subset with sum exactly equal to target? (Values = weights)

```
State: dp[s] = true if sum s is achievable
Base: dp[0] = true
Transition: dp[s] = dp[s] or dp[s - w[i]]
Answer: dp[target]
```

```cpp
bool subsetSum(vector<int>& nums, int target) {
    vector<bool> dp(target+1, false);
    dp[0] = true;
    
    for (int num : nums) {
        for (int s = target; s >= num; s--) {
            dp[s] = dp[s] || dp[s - num];
        }
    }
    
    return dp[target];
}
```

### 5. Partition Equal Subset Sum

**Problem:** Can the array be partitioned into two subsets with equal sum?

```
total = sum(nums)
if total is odd: return false
target = total / 2
return subsetSum(nums, target)
```

### 6. Minimum Subset Sum Difference

**Problem:** Partition into two subsets with minimum absolute difference.

```
Find all achievable sums using subset sum
Answer = min over s of abs(total - 2*s) where dp[s] is true
```

```cpp
int minSubsetSumDiff(vector<int>& nums) {
    int total = accumulate(nums.begin(), nums.end(), 0);
    vector<bool> dp(total+1, false);
    dp[0] = true;
    
    for (int num : nums) {
        for (int s = total; s >= num; s--) {
            dp[s] = dp[s] || dp[s - num];
        }
    }
    
    int ans = total;
    for (int s = 0; s <= total; s++) {
        if (dp[s]) {
            ans = min(ans, abs(total - 2*s));
        }
    }
    
    return ans;
}
```

### 7. Count of Subsets with Given Sum

**Problem:** Count number of subsets that sum to target.

```
State: dp[s] = number of ways to achieve sum s
Base: dp[0] = 1
Transition: dp[s] += dp[s - num]
Answer: dp[target]
```

```cpp
int countSubsetsWithSum(vector<int>& nums, int target) {
    vector<int> dp(target+1, 0);
    dp[0] = 1;
    
    for (int num : nums) {
        for (int s = target; s >= num; s--) {
            dp[s] += dp[s - num];
        }
    }
    
    return dp[target];
}
```

### 8. Target Sum

**Problem:** Assign + or - to each number to reach target sum.

```
Let P be sum of positive numbers, N be sum of negative numbers
P - N = target
P + N = total
2P = target + total
P = (target + total) / 2

So it becomes count subsets with sum = (target + total)/2
```

```cpp
int findTargetSumWays(vector<int>& nums, int target) {
    int total = accumulate(nums.begin(), nums.end(), 0);
    if (abs(target) > total) return 0;
    if ((target + total) % 2 != 0) return 0;
    int subsetSum = (target + total) / 2;
    return countSubsetsWithSum(nums, subsetSum);
}
```

### 9. Coin Change (Minimum Coins)

**Problem:** Find minimum number of coins to make amount. Unlimited coins.

```
State: dp[a] = minimum coins to make amount a
Base: dp[0] = 0, dp[a] = INF for a > 0
Transition: dp[a] = min(dp[a], dp[a - coin] + 1)
Answer: dp[amount] if not INF
```

```cpp
int coinChangeMin(vector<int>& coins, int amount) {
    vector<int> dp(amount+1, INT_MAX);
    dp[0] = 0;
    
    for (int a = 1; a <= amount; a++) {
        for (int coin : coins) {
            if (a >= coin && dp[a-coin] != INT_MAX) {
                dp[a] = min(dp[a], dp[a-coin] + 1);
            }
        }
    }
    
    return dp[amount] == INT_MAX ? -1 : dp[amount];
}
```

### 10. Coin Change (Number of Ways)

**Problem:** Count number of ways to make amount using unlimited coins.

```
State: dp[a] = number of ways to make amount a
Base: dp[0] = 1
Transition: dp[a] += dp[a - coin]
Answer: dp[amount]
```

```cpp
int coinChangeWays(vector<int>& coins, int amount) {
    vector<int> dp(amount+1, 0);
    dp[0] = 1;
    
    for (int coin : coins) {
        for (int a = coin; a <= amount; a++) {
            dp[a] += dp[a - coin];
        }
    }
    
    return dp[amount];
}
```

**Note:** The order of loops matters. Coin loop outside, amount loop inside gives combinations (order doesn't matter). Amount loop outside, coin loop inside gives permutations (order matters).

### 11. Combination Sum IV (Permutations)

**Problem:** Count number of sequences that sum to target. Order matters.

```cpp
int combinationSum4(vector<int>& nums, int target) {
    vector<unsigned int> dp(target+1, 0);
    dp[0] = 1;
    
    for (int a = 1; a <= target; a++) {
        for (int num : nums) {
            if (a >= num) {
                dp[a] += dp[a - num];
            }
        }
    }
    
    return dp[target];
}
```

### Knapsack Problems Summary

| Problem | Type | Loop Order | Space Optimization |
|---------|------|------------|-------------------|
| 0/1 Knapsack | Max value | Item outside, capacity reverse | 1D reverse |
| Unbounded Knapsack | Max value | Capacity forward or item forward | 1D forward |
| Subset Sum | Existence | Item outside, capacity reverse | 1D reverse |
| Count Subsets | Count | Item outside, capacity reverse | 1D reverse |
| Coin Change (Min) | Min coins | Capacity forward, coin inside | 1D forward |
| Coin Change (Ways) | Count ways | Coin outside, capacity forward | 1D forward |
| Target Sum | Count ways | Convert to subset sum | 1D reverse |
