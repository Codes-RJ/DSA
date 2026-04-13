# 01_Introduction_to_DP.md

## Introduction to Dynamic Programming

### What is Dynamic Programming?

Dynamic Programming (DP) is a method for solving complex problems by breaking them down into simpler subproblems, solving each subproblem only once, and storing the results for future use.

The term "Dynamic Programming" was coined by Richard Bellman in the 1950s. "Programming" here means planning or decision-making, not computer programming.

### Core Idea

If you have solved a subproblem before, reuse the answer. Do not solve it again.

This is the opposite of naive recursion, where the same subproblem may be solved hundreds or thousands of times.

### Real-World Analogy

**Memoization (remembering):** Imagine you are doing a complex calculation. Every time you get a result, you write it on a sticky note. Before doing the same calculation again, you check your sticky notes. If the answer is there, you use it immediately.

**Tabulation (filling a table):** Imagine you are filling a spreadsheet. You start with the first row (base values). Then each new cell is calculated using previous cells that are already filled.

### When is DP Used?

DP is used when a problem has two key properties:

| Property | Explanation |
|----------|-------------|
| Overlapping Subproblems | The same smaller problem appears many times |
| Optimal Substructure | The best solution to the big problem uses the best solutions to smaller problems |

### Simple Example: Fibonacci Numbers

**Problem:** Find the nth Fibonacci number where:
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) for n ≥ 2

**Naive Recursive Approach:**

```
function fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

**Why this is bad:** For fib(5), the recursion tree looks like this:

```
                    fib(5)
                   /      \
              fib(4)        fib(3)
             /    \        /    \
         fib(3)  fib(2)  fib(2) fib(1)
        /    \   /    \   /    \
    fib(2) fib(1) fib(1) fib(0) ...
    /    \
fib(1) fib(0)
```

Notice fib(3) is calculated twice. fib(2) is calculated three times. For large n, this becomes exponential: O(2^n).

**DP Approach:** Store results of subproblems. Time complexity becomes O(n).

### Two Approaches in DP

| Approach | Direction | Implementation | Also Known As |
|----------|-----------|----------------|----------------|
| Top-Down | Main problem → Base case | Recursion + Caching | Memoization |
| Bottom-Up | Base case → Main problem | Iteration + Table | Tabulation |

### Top-Down (Memoization) Example

Fibonacci using Top-Down DP:

```
int memo[100];  // initialize with -1

int fib(int n):
    if n <= 1:
        return n
    if memo[n] != -1:
        return memo[n]
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
```

### Bottom-Up (Tabulation) Example

Fibonacci using Bottom-Up DP:

```
int fib(int n):
    if n <= 1:
        return n
    int dp[n+1]
    dp[0] = 0
    dp[1] = 1
    for i = 2 to n:
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

### Space Optimized Fibonacci

Since we only need the last two values:

```
int fib(int n):
    if n <= 1:
        return n
    int prev2 = 0
    int prev1 = 1
    int curr
    for i = 2 to n:
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return curr
```

### Characteristics of DP Problems

**Common keywords that suggest DP:**

- "minimum", "maximum", "shortest", "longest"
- "number of ways", "count"
- "optimal", "best", "worst"
- "can you", "is it possible"
- "subset", "sequence", "string", "grid", "tree"

### DP vs Other Techniques

| Technique | Approach | Overlapping Subproblems | Optimal Substructure |
|-----------|----------|------------------------|---------------------|
| Recursion | Divide and conquer | No | Not required |
| Memoization | Store results | Yes | Yes |
| Tabulation | Build table | Yes | Yes |
| Greedy | Local optimal | No | Yes |
| Backtracking | Try all options | No | Not required |

### When DP is NOT the Answer

1. No overlapping subproblems → Use divide and conquer
2. Greedy works → Use greedy (simpler and faster)
3. Constraints are very small → Use brute force
4. Constraints are huge → Use mathematical formula if exists
5. Problem requires all solutions → Use backtracking
---

## Next Step

- Go to [02_Memoization.md](02_Memoization.md) to continue with Memoization.
