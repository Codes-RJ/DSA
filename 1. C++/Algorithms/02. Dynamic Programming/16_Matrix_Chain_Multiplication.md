# 16_Matrix_Chain_Multiplication.md

## Matrix Chain Multiplication

### Definition

Given a sequence of matrices, find the most efficient way to multiply them together. The goal is to minimize the total number of scalar multiplications.

### Problem Statement

You are given an array `dims` where matrix i has dimensions `dims[i-1] x dims[i]`. Find the minimum number of scalar multiplications needed to multiply all matrices.

### Example

```
Matrices: A1 (10 x 20), A2 (20 x 30), A3 (30 x 40)

Order 1: (A1 x A2) x A3
- Multiply A1 x A2: 10 x 20 x 30 = 6000 multiplications
- Multiply (result) x A3: 10 x 30 x 40 = 12000 multiplications
- Total: 18000

Order 2: A1 x (A2 x A3)
- Multiply A2 x A3: 20 x 30 x 40 = 24000 multiplications
- Multiply A1 x (result): 10 x 20 x 40 = 8000 multiplications
- Total: 32000

Minimum: 18000
```

### Mathematical Formulation

```
Let dims be array where dims[i-1] x dims[i] is dimension of matrix i (1-indexed)
Let dp[i][j] = minimum multiplications to multiply matrices i through j

Base case:
dp[i][i] = 0 (single matrix, no multiplication needed)

Transition:
dp[i][j] = min over k from i to j-1 of (
    dp[i][k] + dp[k+1][j] + (dims[i-1] * dims[k] * dims[j])
)

Answer: dp[1][n]
```

### Basic Implementation (O(n³))

```cpp
int matrixChainMultiplication(vector<int>& dims) {
    int n = dims.size() - 1;  // number of matrices
    vector<vector<int>> dp(n+1, vector<int>(n+1, 0));
    
    // length of chain
    for (int len = 2; len <= n; len++) {
        for (int i = 1; i <= n - len + 1; i++) {
            int j = i + len - 1;
            dp[i][j] = INT_MAX;
            
            for (int k = i; k < j; k++) {
                int cost = dp[i][k] + dp[k+1][j] + (dims[i-1] * dims[k] * dims[j]);
                dp[i][j] = min(dp[i][j], cost);
            }
        }
    }
    
    return dp[1][n];
}
```

### Reconstructing the Parenthesization

To get the actual order of multiplication, we store the split point `k` for each `dp[i][j]`.

```cpp
vector<vector<int>> split;  // to store the split point

int matrixChainMultiplicationWithSplit(vector<int>& dims) {
    int n = dims.size() - 1;
    vector<vector<int>> dp(n+1, vector<int>(n+1, 0));
    split.assign(n+1, vector<int>(n+1, 0));
    
    for (int len = 2; len <= n; len++) {
        for (int i = 1; i <= n - len + 1; i++) {
            int j = i + len - 1;
            dp[i][j] = INT_MAX;
            
            for (int k = i; k < j; k++) {
                int cost = dp[i][k] + dp[k+1][j] + (dims[i-1] * dims[k] * dims[j]);
                if (cost < dp[i][j]) {
                    dp[i][j] = cost;
                    split[i][j] = k;
                }
            }
        }
    }
    
    return dp[1][n];
}

string printParenthesization(int i, int j) {
    if (i == j) {
        return "A" + to_string(i);
    }
    return "(" + printParenthesization(i, split[i][j]) + 
           " x " + printParenthesization(split[i][j] + 1, j) + ")";
}
```

### Example Walkthrough

```
dims = [10, 20, 30, 40]
n = 3 matrices

dp table:

len = 2:
i=1, j=2: k=1 → cost = 0 + 0 + (10*20*30) = 6000
i=2, j=3: k=2 → cost = 0 + 0 + (20*30*40) = 24000

len = 3:
i=1, j=3:
  k=1: dp[1][1] + dp[2][3] + (10*20*40) = 0 + 24000 + 8000 = 32000
  k=2: dp[1][2] + dp[3][3] + (10*30*40) = 6000 + 0 + 12000 = 18000
  min = 18000

Result: 18000
```

### Variations of Matrix Chain Multiplication

#### 1. Printing the Parenthesization

Already shown above.

#### 2. Matrix Chain Multiplication for Boolean Parenthesization

**Problem:** Given a boolean expression and operators (AND, OR, XOR), find number of ways to parenthesize to get True.

```
Let T[i][j] = ways to get True for expression i to j
Let F[i][j] = ways to get False for expression i to j

For each operator between k and k+1:
- For AND: T += T[i][k] * T[k+1][j]
- For OR:  T += total[i][k] * total[k+1][j] - F[i][k] * F[k+1][j]
- For XOR: T += T[i][k] * F[k+1][j] + F[i][k] * T[k+1][j]
```

```cpp
int countWaysToGetTrue(string expr) {
    int n = expr.length();
    vector<vector<int>> T(n, vector<int>(n, 0));
    vector<vector<int>> F(n, vector<int>(n, 0));
    
    for (int i = 0; i < n; i += 2) {
        T[i][i] = (expr[i] == 'T') ? 1 : 0;
        F[i][i] = (expr[i] == 'F') ? 1 : 0;
    }
    
    for (int len = 2; len < n; len += 2) {
        for (int i = 0; i < n - len; i += 2) {
            int j = i + len;
            for (int k = i + 1; k < j; k += 2) {
                char op = expr[k];
                int totalLeft = T[i][k-1] + F[i][k-1];
                int totalRight = T[k+1][j] + F[k+1][j];
                
                if (op == '&') {
                    T[i][j] += T[i][k-1] * T[k+1][j];
                    F[i][j] += (totalLeft * totalRight) - (T[i][k-1] * T[k+1][j]);
                }
                else if (op == '|') {
                    F[i][j] += F[i][k-1] * F[k+1][j];
                    T[i][j] += (totalLeft * totalRight) - (F[i][k-1] * F[k+1][j]);
                }
                else if (op == '^') {
                    T[i][j] += T[i][k-1] * F[k+1][j] + F[i][k-1] * T[k+1][j];
                    F[i][j] += T[i][k-1] * T[k+1][j] + F[i][k-1] * F[k+1][j];
                }
            }
        }
    }
    
    return T[0][n-1];
}
```

#### 3. Minimum Cost to Cut a Stick

**Problem:** Given a stick of length n and cuts array, find minimum cost to make all cuts. Cost = length of stick being cut.

This is similar to matrix chain multiplication.

```cpp
int minCostToCutStick(int n, vector<int>& cuts) {
    cuts.push_back(0);
    cuts.push_back(n);
    sort(cuts.begin(), cuts.end());
    
    int m = cuts.size();
    vector<vector<int>> dp(m, vector<int>(m, 0));
    
    for (int len = 2; len < m; len++) {
        for (int i = 0; i < m - len; i++) {
            int j = i + len;
            dp[i][j] = INT_MAX;
            for (int k = i + 1; k < j; k++) {
                dp[i][j] = min(dp[i][j], 
                               dp[i][k] + dp[k][j] + (cuts[j] - cuts[i]));
            }
        }
    }
    
    return dp[0][m-1];
}
```

#### 4. Optimal Binary Search Tree (OBST)

**Problem:** Given keys and their frequencies, build a BST with minimum search cost.

```cpp
int optimalBST(vector<int>& keys, vector<int>& freq) {
    int n = keys.size();
    vector<vector<int>> dp(n, vector<int>(n, 0));
    vector<vector<int>> sum(n, vector<int>(n, 0));
    
    // Compute prefix sums for quick range sum
    for (int i = 0; i < n; i++) {
        sum[i][i] = freq[i];
        for (int j = i + 1; j < n; j++) {
            sum[i][j] = sum[i][j-1] + freq[j];
        }
    }
    
    for (int i = 0; i < n; i++) {
        dp[i][i] = freq[i];
    }
    
    for (int len = 2; len <= n; len++) {
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            dp[i][j] = INT_MAX;
            
            for (int r = i; r <= j; r++) {
                int left = (r > i) ? dp[i][r-1] : 0;
                int right = (r < j) ? dp[r+1][j] : 0;
                int cost = left + right + sum[i][j];
                dp[i][j] = min(dp[i][j], cost);
            }
        }
    }
    
    return dp[0][n-1];
}
```

#### 5. Egg Dropping Problem

**Problem:** Find minimum number of attempts to find critical floor from which egg breaks.

```cpp
int eggDrop(int eggs, int floors) {
    vector<vector<int>> dp(eggs+1, vector<int>(floors+1, 0));
    
    for (int i = 1; i <= eggs; i++) {
        dp[i][0] = 0;
        dp[i][1] = 1;
    }
    for (int j = 1; j <= floors; j++) {
        dp[1][j] = j;
    }
    
    for (int i = 2; i <= eggs; i++) {
        for (int j = 2; j <= floors; j++) {
            dp[i][j] = INT_MAX;
            for (int k = 1; k <= j; k++) {
                int attempts = 1 + max(dp[i-1][k-1], dp[i][j-k]);
                dp[i][j] = min(dp[i][j], attempts);
            }
        }
    }
    
    return dp[eggs][floors];
}
```

### Complexity Analysis

| Problem | Time Complexity | Space Complexity |
|---------|----------------|------------------|
| Matrix Chain Multiplication | O(n³) | O(n²) |
| Boolean Parenthesization | O(n³) | O(n²) |
| Cut Stick | O(m³) | O(m²) |
| Optimal BST | O(n³) | O(n²) |
| Egg Dropping (Naive) | O(eggs × floors²) | O(eggs × floors) |
