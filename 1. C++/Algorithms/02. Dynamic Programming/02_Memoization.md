# 02_Memoization.md

## Memoization (Top-Down DP)

### Definition

Memoization is a technique where you store the results of expensive function calls and return the cached result when the same inputs occur again. It is a top-down approach because you start from the main problem and recursively break it down.

### How Memoization Works

Step 1: Create a cache (array, hash map, dictionary)

Step 2: Before computing a subproblem, check if it exists in cache

Step 3: If yes, return cached value

Step 4: If no, compute it recursively

Step 5: Store the result in cache before returning

### Visual Representation

```
Problem(n)
    │
    ├── Check cache[n]
    │       │
    │       ├── Found → Return immediately
    │       │
    │       └── Not found → Compute
    │
    └── Compute:
            │
            ├── Solve subproblems
            ├── Store result in cache[n]
            └── Return result
```

### Memoization for Fibonacci

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<long long> memo(100, -1);

long long fib(int n) {
    if (n <= 1) return n;
    if (memo[n] != -1) return memo[n];
    memo[n] = fib(n-1) + fib(n-2);
    return memo[n];
}

int main() {
    cout << fib(50) << endl;
    return 0;
}
```

### Memoization for Factorial

```cpp
vector<long long> factMemo(100, -1);

long long factorial(int n) {
    if (n <= 1) return 1;
    if (factMemo[n] != -1) return factMemo[n];
    factMemo[n] = n * factorial(n-1);
    return factMemo[n];
}
```

### Memoization for Climbing Stairs

**Problem:** You can climb 1 or 2 steps at a time. Find number of ways to reach step n.

```cpp
vector<int> climbMemo(100, -1);

int climbStairs(int n) {
    if (n < 0) return 0;
    if (n == 0) return 1;
    if (climbMemo[n] != -1) return climbMemo[n];
    climbMemo[n] = climbStairs(n-1) + climbStairs(n-2);
    return climbMemo[n];
}
```

### Cache Data Structures

| Use Case | Cache Structure |
|----------|-----------------|
| Single integer parameter | 1D array |
| Two integer parameters | 2D array |
| String parameter | unordered_map<string, int> |
| Complex state | map or custom hash |

### Memoization with Map (for sparse states)

```cpp
#include <unordered_map>

unordered_map<int, long long> memo;

long long fib(int n) {
    if (n <= 1) return n;
    if (memo.count(n)) return memo[n];
    memo[n] = fib(n-1) + fib(n-2);
    return memo[n];
}
```

### Advantages of Memoization

1. Intuitive to implement (follows recursion structure)
2. Solves only the subproblems that are actually needed
3. No need to determine the order of computation
4. Easy to add to existing recursive solution

### Disadvantages of Memoization

1. Recursion overhead (function calls)
2. Risk of stack overflow for deep recursion
3. Slightly slower than tabulation due to function calls
4. Memory for recursion stack in addition to cache

### When to Use Memoization

- When the recursive formulation is natural
- When not all subproblems need to be solved
- When the state space is sparse
- When you already have a working recursive solution

### Memoization Template

```cpp
// Step 1: Define cache
vector<vector<int>> memo;

// Step 2: Initialize cache with -1 (or 0, or INT_MIN)
memo.assign(n, vector<int>(m, -1));

// Step 3: Write recursive function with memoization
int solve(int i, int j) {
    // Base case
    if (i == 0 && j == 0) return 1;
    
    // Check cache
    if (memo[i][j] != -1) return memo[i][j];
    
    // Compute and store
    int result = // transition using solve(i-1, j), solve(i, j-1), etc.
    memo[i][j] = result;
    return result;
}
```

### Common Mistakes in Memoization

1. Forgetting to store result in cache before returning
2. Using wrong cache size (off-by-one errors)
3. Not resetting cache between test cases
4. Using cache for problems without overlapping subproblems
5. Not handling invalid states in cache check

---
---

## Next Step

- Go to [03_Tabulation.md](03_Tabulation.md) to continue with Tabulation.
