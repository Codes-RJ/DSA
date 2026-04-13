# 20_Backtracking_vs_DP.md

## Backtracking vs Dynamic Programming

### Definition

Backtracking explores all possibilities recursively, pruning invalid branches. Dynamic Programming solves overlapping subproblems by storing results for reuse.

### Key Differences

| Aspect | Backtracking | Dynamic Programming |
|--------|--------------|---------------------|
| Subproblems | Independent (typically) | Overlapping |
| Storage | No memoization (usually) | Stores subproblem results |
| Exploration | Depth-first search | Systematic filling |
| Time Complexity | Exponential | Polynomial |
| Space Complexity | O(depth) | O(state space) |
| Optimality | Finds all solutions | Finds optimal (or count) |

### Visual Comparison

```
Backtracking (Fibonacci):
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2)
│   │   │   ├── fib(1)
│   │   │   └── fib(0)
│   │   └── fib(1)
│   └── fib(2)
│       ├── fib(1)
│       └── fib(0)
└── fib(3)
    ├── fib(2)
    │   ├── fib(1)
    │   └── fib(0)
    └── fib(1)

DP (Fibonacci):
dp[0]=0, dp[1]=1
dp[2]=dp[1]+dp[0]=1
dp[3]=dp[2]+dp[1]=2
dp[4]=dp[3]+dp[2]=3
dp[5]=dp[4]+dp[3]=5
```

### When to Use Backtracking

| Scenario | Example |
|----------|---------|
| Need all solutions | All permutations |
| Small search space | N-Queens n=8 |
| No overlapping subproblems | Generating subsets |
| Constraints can prune | Sudoku |

### When to Use DP

| Scenario | Example |
|----------|---------|
| Need optimal solution | Knapsack |
| Overlapping subproblems | Fibonacci |
| Count number of ways | Coin change |
| Large input size | LCS for long strings |

### Example: Fibonacci Numbers

| Approach | Time | Space | n=40 |
|----------|------|-------|------|
| Backtracking | O(φⁿ) | O(n) | ~1 sec |
| DP | O(n) | O(n) | Instant |

### Example: Subset Sum

| Approach | Time | Space | n=30, sum=1000 |
|----------|------|-------|----------------|
| Backtracking | O(2^n) | O(n) | May be slow |
| DP | O(n × sum) | O(sum) | Fast |

### Example: Longest Common Subsequence

| Approach | Time | Space | m=n=1000 |
|----------|------|-------|----------|
| Backtracking | O(2^(m+n)) | O(m+n) | Impossible |
| DP | O(m×n) | O(min(m,n)) | ~1 sec |

### Backtracking for DP Problems (Not Recommended)

```cpp
// Naive recursive Fibonacci (backtracking style)
int fibBacktrack(int n) {
    if (n <= 1) return n;
    return fibBacktrack(n-1) + fibBacktrack(n-2);
}
// Time: O(φⁿ), n=40 takes seconds

// DP Fibonacci
int fibDP(int n) {
    if (n <= 1) return n;
    int prev2 = 0, prev1 = 1, curr;
    for (int i = 2; i <= n; i++) {
        curr = prev1 + prev2;
        prev2 = prev1;
        prev1 = curr;
    }
    return curr;
}
// Time: O(n), n=10^7 is fine
```

### DP for Backtracking Problems (Often Not Possible)

```cpp
// N-Queens cannot be solved efficiently with DP
// State space is too large
// DP would need 2^n states which is still exponential
```

### When Both Work (But One is Better)

| Problem | Backtracking | DP | Winner |
|---------|--------------|-----|--------|
| Subset Sum | O(2^n) | O(n×sum) | DP for small sum |
| Coin Change (min coins) | O(2^n) | O(n×amount) | DP |
| Word Break | O(2^n) | O(n²) | DP |
| Palindrome Partitioning | O(2^n) | O(n²) | DP for min cuts |
| Combination Sum | O(2^n) | O(n×target) | DP for count |

### Combining Backtracking and DP (Memoization)

Memoization is backtracking + DP storage:

```cpp
// Memoized backtracking (top-down DP)
vector<int> memo;

int fibMemo(int n) {
    if (n <= 1) return n;
    if (memo[n] != -1) return memo[n];
    memo[n] = fibMemo(n-1) + fibMemo(n-2);
    return memo[n];
}
// Time: O(n), same as bottom-up DP
```

### Decision Guide

```
Does the problem have optimal substructure?
    │
    ├── No → Use Backtracking
    │
    └── Yes
        │
        Does it have overlapping subproblems?
            │
            ├── No → Use Divide and Conquer
            │
            └── Yes
                │
                Can you define a state with reasonable size?
                    │
                    ├── No → Use Backtracking
                    │
                    └── Yes → Use DP
```

### Performance Comparison Table

| Problem | n | Backtracking Time | DP Time | Backtracking Space | DP Space |
|---------|---|-------------------|---------|-------------------|----------|
| Fibonacci | 40 | ~1 sec | < 1 ms | O(n) | O(1) |
| Subset Sum | 30, sum=1000 | ~1 sec | < 10 ms | O(n) | O(sum) |
| Coin Change | 50, amount=1000 | ~1 min | < 10 ms | O(n) | O(amount) |
| N-Queens | 20 | ~10 sec | Not feasible | O(n) | O(2^n) |
| LCS | 1000 | Impossible | < 1 sec | O(m+n) | O(min(m,n)) |

### Practice Problems

1. Solve Fibonacci using both backtracking and DP, compare for n=40
2. Solve subset sum using both, compare for n=20, sum=100
3. Solve coin change (minimum coins) using both
4. Determine which problems are better suited for backtracking vs DP
5. Implement memoized backtracking for a problem
---

## Next Step

- Go to [Theory.md](Theory.md) to continue with Theory.
