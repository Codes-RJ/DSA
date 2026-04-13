# 03_Tabulation.md

## Tabulation (Bottom-Up DP)

### Definition

Tabulation is a bottom-up approach where you solve all smaller subproblems first and use their results to build solutions for larger subproblems. You fill a table (usually an array) in a specific order until you reach the original problem.

### How Tabulation Works

Step 1: Create a table (array) to store results for all subproblems

Step 2: Initialize base cases in the table

Step 3: Iterate through states in the correct order

Step 4: Use previously computed values to compute current state

Step 5: Answer is in the last cell (or a specific cell)

### Visual Representation

```
Table of size n (for 1D DP):

Index:   0   1   2   3   4   5
        ┌───┬───┬───┬───┬───┬───┐
        │ B │ B │   │   │   │ A │
        └───┴───┴───┴───┴───┴───┘
          ↑   ↑               ↑
          │   │               │
      Base cases         Answer

Order of computation: left to right (usually)
```

### Tabulation for Fibonacci

```cpp
int fib(int n) {
    if (n <= 1) return n;
    
    int dp[n+1];
    dp[0] = 0;
    dp[1] = 1;
    
    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    
    return dp[n];
}
```

### Tabulation for Climbing Stairs

```cpp
int climbStairs(int n) {
    if (n == 0) return 1;
    if (n == 1) return 1;
    
    int dp[n+1];
    dp[0] = 1;
    dp[1] = 1;
    
    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    
    return dp[n];
}
```

### Tabulation for 2D DP (Unique Paths)

**Problem:** Number of ways to reach bottom-right corner of m x n grid moving only right or down.

```cpp
int uniquePaths(int m, int n) {
    int dp[m][n];
    
    // Base cases: first row and first column
    for (int i = 0; i < m; i++) {
        dp[i][0] = 1;
    }
    for (int j = 0; j < n; j++) {
        dp[0][j] = 1;
    }
    
    // Fill the table
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = dp[i-1][j] + dp[i][j-1];
        }
    }
    
    return dp[m-1][n-1];
}
```

### Determining the Order of Computation

The key challenge in tabulation is computing states in the correct order.

**Rule:** A state can only depend on states that have been computed earlier.

| Problem | Dependencies | Order |
|---------|--------------|-------|
| Fibonacci | dp[i] depends on dp[i-1], dp[i-2] | i from 2 to n |
| Unique Paths | dp[i][j] depends on dp[i-1][j], dp[i][j-1] | i from 1 to m, j from 1 to n |
| LCS | dp[i][j] depends on dp[i-1][j], dp[i][j-1], dp[i-1][j-1] | i from 1 to m, j from 1 to n |
| Knapsack | dp[i][w] depends on dp[i-1][w], dp[i-1][w-wt[i]] | i from 1 to n, w from 0 to W |

### Advantages of Tabulation

1. No recursion (no stack overflow risk)
2. Faster than memoization (no function call overhead)
3. Easier to optimize space (rolling arrays)
4. Predictable memory usage
5. Better for problems where all subproblems must be solved

### Disadvantages of Tabulation

1. May solve unnecessary subproblems
2. Requires knowing the correct order of computation
3. Less intuitive for complex state transitions
4. Harder to implement for irregular state spaces

### When to Use Tabulation

- When all subproblems need to be solved anyway
- When recursion depth might be too large
- When you need maximum performance
- When you want to optimize memory usage
- When the transition order is clear

### Space Optimization with Rolling Arrays

When dp[i] depends only on previous few rows, we can reduce space.

**Fibonacci optimization (O(1) space):**

```cpp
int fib(int n) {
    if (n <= 1) return n;
    int prev2 = 0, prev1 = 1, curr;
    for (int i = 2; i <= n; i++) {
        curr = prev1 + prev2;
        prev2 = prev1;
        prev1 = curr;
    }
    return curr;
}
```

**Unique Paths optimization (O(n) space):**

```cpp
int uniquePaths(int m, int n) {
    vector<int> dp(n, 1);
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[j] = dp[j] + dp[j-1];
        }
    }
    return dp[n-1];
}
```

### Tabulation Template

```cpp
// Step 1: Create table
vector<vector<int>> dp(m+1, vector<int>(n+1, 0));

// Step 2: Initialize base cases
dp[0][0] = baseValue;

// Step 3: Fill table in correct order
for (int i = 0; i <= m; i++) {
    for (int j = 0; j <= n; j++) {
        if (i == 0 && j == 0) continue;
        // transition using dp[i-1][j], dp[i][j-1], etc.
    }
}

// Step 4: Return answer
return dp[m][n];
```

### Memoization vs Tabulation Summary

| Aspect | Memoization | Tabulation |
|--------|-------------|------------|
| Approach | Top-down | Bottom-up |
| Implementation | Recursive | Iterative |
| Subproblems solved | Only needed | All |
| Space | Cache + stack | Table only |
| Stack overflow risk | Yes | No |
| Speed | Slower | Faster |
| Ease of coding | Easier | Harder |
---

## Next Step

- Go to [04_1D_DP.md](04_1D_DP.md) to continue with 1D DP.
