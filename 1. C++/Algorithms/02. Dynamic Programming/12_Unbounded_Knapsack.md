# 12_Unbounded_Knapsack.md

## Unbounded Knapsack (Complete Knapsack)

### Definition

In the unbounded knapsack problem, each item can be taken an unlimited number of times. This is also called the complete knapsack problem.

### Problem Statement

Given:
- n items, each with weight w[i] and value v[i]
- A knapsack with capacity W
- Unlimited copies of each item

Goal: Maximize total value without exceeding capacity W.

### Mathematical Formulation

```
Let dp[c] = maximum value achievable with capacity c

dp[0] = 0
dp[c] = max( dp[c], dp[c - w[i]] + v[i] ) for all i where w[i] <= c

Answer = dp[W]
```

### Difference from 0/1 Knapsack

| Aspect | 0/1 Knapsack | Unbounded Knapsack |
|--------|--------------|---------------------|
| Item usage | 0 or 1 time | 0, 1, 2, ... times |
| DP loop direction | Reverse (W to w[i]) | Forward (w[i] to W) |
| Why? | Prevents reuse | Allows reuse |

### Basic Implementation

```cpp
int unboundedKnapsack(int W, vector<int>& weights, vector<int>& values) {
    int n = weights.size();
    vector<int> dp(W + 1, 0);
    
    for (int c = 1; c <= W; c++) {
        for (int i = 0; i < n; i++) {
            if (c >= weights[i]) {
                dp[c] = max(dp[c], dp[c - weights[i]] + values[i]);
            }
        }
    }
    
    return dp[W];
}
```

### Alternative Implementation (Item Loop First)

```cpp
int unboundedKnapsack(int W, vector<int>& weights, vector<int>& values) {
    int n = weights.size();
    vector<int> dp(W + 1, 0);
    
    for (int i = 0; i < n; i++) {
        for (int c = weights[i]; c <= W; c++) {
            dp[c] = max(dp[c], dp[c - weights[i]] + values[i]);
        }
    }
    
    return dp[W];
}
```

### Why Forward Loop Works

In 0/1 knapsack, we loop backwards to prevent reusing the same item:

```
for (int c = W; c >= w[i]; c--) {
    dp[c] = max(dp[c], dp[c - w[i]] + v[i]);
}
```

In unbounded knapsack, we want to allow reuse, so we loop forwards:

```
for (int c = w[i]; c <= W; c++) {
    dp[c] = max(dp[c], dp[c - w[i]] + v[i]);
}
```

When looping forward, dp[c - w[i]] may have already been updated with the same item in the current iteration, allowing multiple uses.

### Example Walkthrough

**Input:**
- W = 5
- Item: weight = 2, value = 3

**Forward loop (Unbounded):**

```
Start: dp = [0, 0, 0, 0, 0, 0]

c = 2: dp[2] = max(0, dp[0] + 3) = 3
c = 3: dp[3] = max(0, dp[1] + 3) = 0
c = 4: dp[4] = max(0, dp[2] + 3) = 3 + 3 = 6
c = 5: dp[5] = max(0, dp[3] + 3) = 0

Result: dp[5] = 0 (can't make exactly 5)
```

But if we had multiple items, the forward loop allows using the same item multiple times.

### Classic Problems Using Unbounded Knapsack

#### 1. Coin Change (Minimum Coins)

**Problem:** Find minimum number of coins to make a given amount. Unlimited coins.

```
State: dp[a] = minimum coins to make amount a
Base: dp[0] = 0, dp[a] = INF for a > 0
Transition: dp[a] = min(dp[a], dp[a - coin] + 1)
Answer: dp[amount] if not INF
```

```cpp
int coinChange(vector<int>& coins, int amount) {
    vector<int> dp(amount + 1, INT_MAX);
    dp[0] = 0;
    
    for (int a = 1; a <= amount; a++) {
        for (int coin : coins) {
            if (a >= coin && dp[a - coin] != INT_MAX) {
                dp[a] = min(dp[a], dp[a - coin] + 1);
            }
        }
    }
    
    return dp[amount] == INT_MAX ? -1 : dp[amount];
}
```

#### 2. Coin Change (Number of Ways - Combinations)

**Problem:** Count number of combinations (order doesn't matter) to make amount.

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

#### 3. Maximum Value with Weight Constraint

**Problem:** Fill a knapsack with unlimited items to maximize value.

```cpp
int maxValue(int W, vector<int>& weights, vector<int>& values) {
    vector<int> dp(W + 1, 0);
    
    for (int i = 0; i < weights.size(); i++) {
        for (int c = weights[i]; c <= W; c++) {
            dp[c] = max(dp[c], dp[c - weights[i]] + values[i]);
        }
    }
    
    return dp[W];
}
```

#### 4. Rod Cutting Problem

**Problem:** Given a rod of length n and prices for each length, find maximum revenue by cutting the rod.

This is exactly unbounded knapsack where:
- Length = weight
- Price = value
- Rod length = capacity

```cpp
int rodCutting(int n, vector<int>& prices) {
    // prices[i] is price for length i+1
    vector<int> dp(n + 1, 0);
    
    for (int len = 1; len <= n; len++) {
        for (int cut = 1; cut <= len; cut++) {
            dp[len] = max(dp[len], dp[len - cut] + prices[cut - 1]);
        }
    }
    
    return dp[n];
}
```

#### 5. Perfect Squares

**Problem:** Find the least number of perfect squares that sum to n.

```
This is coin change where coins are perfect squares.
```

```cpp
int numSquares(int n) {
    vector<int> dp(n + 1, INT_MAX);
    dp[0] = 0;
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j * j <= i; j++) {
            dp[i] = min(dp[i], dp[i - j*j] + 1);
        }
    }
    
    return dp[n];
}
```

#### 6. Combination Sum (Unlimited Use)

**Problem:** Find all combinations that sum to target. (Usually solved with backtracking, but counting uses DP.)

```cpp
int combinationSumCount(vector<int>& candidates, int target) {
    vector<int> dp(target + 1, 0);
    dp[0] = 1;
    
    for (int t = 1; t <= target; t++) {
        for (int num : candidates) {
            if (t >= num) {
                dp[t] += dp[t - num];
            }
        }
    }
    
    return dp[target];
}
```

### Comparison Table

| Problem Type | Transition | Loop Order | Initialization |
|--------------|------------|------------|----------------|
| Max Value | max(dp[c], dp[c-w] + v) | forward | dp[0] = 0 |
| Min Coins | min(dp[c], dp[c-w] + 1) | forward | dp[0] = 0, others INF |
| Number of Ways (Combinations) | dp[c] += dp[c-w] | coin outer, capacity inner | dp[0] = 1 |
| Number of Ways (Permutations) | dp[c] += dp[c-w] | capacity outer, coin inner | dp[0] = 1 |

### Unbounded vs 0/1 Summary

| Aspect | 0/1 Knapsack | Unbounded Knapsack |
|--------|--------------|---------------------|
| Item limit | 1 per item | Unlimited |
| DP array | 1D or 2D | 1D |
| Loop direction | Reverse (W to w) | Forward (w to W) |
| Time complexity | O(n × W) | O(n × W) |
| Space complexity | O(W) | O(W) |
---

## Next Step

- Go to [13_Longest_Common_Subsequence.md](13_Longest_Common_Subsequence.md) to continue with Longest Common Subsequence.
