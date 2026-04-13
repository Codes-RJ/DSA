# 10_DP_on_Grids.md

## DP on Grids

### Definition

Grid DP involves problems where you navigate a 2D grid (matrix) from one corner to another, typically moving only right and down. Each cell may have costs, values, or obstacles.

### Key Concept

The state is usually the cell position (i, j). The transition comes from the top cell (i-1, j) and left cell (i, j-1). The order of computation is row-major (top to bottom, left to right).

### Classic Grid DP Problems

#### 1. Unique Paths

**Problem:** Number of ways to reach bottom-right corner of m x n grid moving only right or down.

```
State: dp[i][j] = ways to reach cell (i, j)
Base: dp[0][j] = 1 for all j, dp[i][0] = 1 for all i
Transition: dp[i][j] = dp[i-1][j] + dp[i][j-1]
Answer: dp[m-1][n-1]
```

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

**Space optimized (1D array):**

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

#### 2. Unique Paths II (with Obstacles)

**Problem:** Grid has obstacles (1 represents obstacle, 0 represents empty). Count paths.

```
State: dp[i][j] = ways to reach cell (i, j)
Base: dp[0][0] = 1 if grid[0][0] == 0 else 0
Transition: 
    if grid[i][j] == 1: dp[i][j] = 0
    else: dp[i][j] = dp[i-1][j] + dp[i][j-1]
Answer: dp[m-1][n-1]
```

```cpp
int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
    int m = obstacleGrid.size();
    int n = obstacleGrid[0].size();
    
    if (obstacleGrid[0][0] == 1) return 0;
    
    vector<vector<int>> dp(m, vector<int>(n, 0));
    dp[0][0] = 1;
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (obstacleGrid[i][j] == 1) {
                dp[i][j] = 0;
            } else {
                if (i > 0) dp[i][j] += dp[i-1][j];
                if (j > 0) dp[i][j] += dp[i][j-1];
            }
        }
    }
    
    return dp[m-1][n-1];
}
```

#### 3. Minimum Path Sum

**Problem:** Find path from top-left to bottom-right with minimum sum.

```
State: dp[i][j] = minimum sum to reach cell (i, j)
Base: dp[0][0] = grid[0][0]
Transition: dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
Answer: dp[m-1][n-1]
```

```cpp
int minPathSum(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<int>> dp(m, vector<int>(n, 0));
    
    dp[0][0] = grid[0][0];
    
    for (int i = 1; i < m; i++) {
        dp[i][0] = dp[i-1][0] + grid[i][0];
    }
    for (int j = 1; j < n; j++) {
        dp[0][j] = dp[0][j-1] + grid[0][j];
    }
    
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]);
        }
    }
    
    return dp[m-1][n-1];
}
```

**Space optimized (1D array):**

```cpp
int minPathSum(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<int> dp(n, 0);
    
    dp[0] = grid[0][0];
    for (int j = 1; j < n; j++) {
        dp[j] = dp[j-1] + grid[0][j];
    }
    
    for (int i = 1; i < m; i++) {
        dp[0] = dp[0] + grid[i][0];
        for (int j = 1; j < n; j++) {
            dp[j] = grid[i][j] + min(dp[j], dp[j-1]);
        }
    }
    
    return dp[n-1];
}
```

#### 4. Maximum Path Sum in Grid (with negative numbers)

**Problem:** Find path from top-left to bottom-right with maximum sum.

```
Same as minimum path sum but use max instead of min.
```

```cpp
int maxPathSum(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<int>> dp(m, vector<int>(n, 0));
    
    dp[0][0] = grid[0][0];
    
    for (int i = 1; i < m; i++) {
        dp[i][0] = dp[i-1][0] + grid[i][0];
    }
    for (int j = 1; j < n; j++) {
        dp[0][j] = dp[0][j-1] + grid[0][j];
    }
    
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = grid[i][j] + max(dp[i-1][j], dp[i][j-1]);
        }
    }
    
    return dp[m-1][n-1];
}
```

#### 5. Dungeon Game

**Problem:** Find minimum initial health to reach bottom-right. Health decreases by dungeon values (negative = damage, positive = heal). Health must stay positive.

```
State: dp[i][j] = minimum health needed to reach bottom-right from (i, j)
Base: dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
Transition: dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
Answer: dp[0][0]
```

```cpp
int calculateMinimumHP(vector<vector<int>>& dungeon) {
    int m = dungeon.size();
    int n = dungeon[0].size();
    vector<vector<int>> dp(m, vector<int>(n, 0));
    
    dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1]);
    
    for (int i = m-2; i >= 0; i--) {
        dp[i][n-1] = max(1, dp[i+1][n-1] - dungeon[i][n-1]);
    }
    for (int j = n-2; j >= 0; j--) {
        dp[m-1][j] = max(1, dp[m-1][j+1] - dungeon[m-1][j]);
    }
    
    for (int i = m-2; i >= 0; i--) {
        for (int j = n-2; j >= 0; j--) {
            int need = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j];
            dp[i][j] = max(1, need);
        }
    }
    
    return dp[0][0];
}
```

#### 6. Triangle (Minimum Path Sum in Triangle)

**Problem:** Given a triangle array, find minimum path sum from top to bottom.

```
State: dp[i][j] = minimum sum to reach cell (i, j)
Base: dp[0][0] = triangle[0][0]
Transition: dp[i][j] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j])
Answer: min(dp[n-1][j]) for all j
```

```cpp
int minimumTotal(vector<vector<int>>& triangle) {
    int n = triangle.size();
    vector<int> dp(n, 0);
    
    dp[0] = triangle[0][0];
    
    for (int i = 1; i < n; i++) {
        vector<int> curr(i+1, 0);
        curr[0] = dp[0] + triangle[i][0];
        curr[i] = dp[i-1] + triangle[i][i];
        
        for (int j = 1; j < i; j++) {
            curr[j] = triangle[i][j] + min(dp[j-1], dp[j]);
        }
        
        dp = curr;
    }
    
    return *min_element(dp.begin(), dp.end());
}
```

#### 7. Maximal Square

**Problem:** Find the largest square containing only 1's in a binary matrix.

```
State: dp[i][j] = side length of largest square ending at (i, j)
Base: dp[i][j] = grid[i][j] for first row and first column
Transition: 
    if grid[i][j] == 1:
        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    else:
        dp[i][j] = 0
Answer: max(dp[i][j]) ^ 2 (area)
```

```cpp
int maximalSquare(vector<vector<char>>& matrix) {
    int m = matrix.size();
    int n = matrix[0].size();
    vector<vector<int>> dp(m, vector<int>(n, 0));
    int maxSide = 0;
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (matrix[i][j] == '1') {
                if (i == 0 || j == 0) {
                    dp[i][j] = 1;
                } else {
                    dp[i][j] = 1 + min(dp[i-1][j], min(dp[i][j-1], dp[i-1][j-1]));
                }
                maxSide = max(maxSide, dp[i][j]);
            }
        }
    }
    
    return maxSide * maxSide;
}
```

#### 8. Number of Paths with Exactly k Coins

**Problem:** Count paths from top-left to bottom-right collecting exactly k coins.

```
State: dp[i][j][c] = number of ways to reach (i, j) with exactly c coins
Base: dp[0][0][grid[0][0]] = 1
Transition: dp[i][j][c] = dp[i-1][j][c - grid[i][j]] + dp[i][j-1][c - grid[i][j]]
Answer: dp[m-1][n-1][k]
```

#### 9. Cherry Pickup

**Problem:** Collect maximum cherries going from top-left to bottom-right and back.

```
State: dp[r1][c1][r2] = max cherries collected with person1 at (r1, c1) and person2 at (r2, c2)
where c2 = r1 + c1 - r2 (since both move same number of steps)
```

```cpp
int cherryPickup(vector<vector<int>>& grid) {
    int n = grid.size();
    vector<vector<vector<int>>> dp(n, vector<vector<int>>(n, vector<int>(n, INT_MIN)));
    
    dp[0][0][0] = grid[0][0];
    
    for (int r1 = 0; r1 < n; r1++) {
        for (int c1 = 0; c1 < n; c1++) {
            for (int r2 = 0; r2 < n; r2++) {
                int c2 = r1 + c1 - r2;
                if (c2 < 0 || c2 >= n) continue;
                if (grid[r1][c1] == -1 || grid[r2][c2] == -1) continue;
                
                int best = dp[r1][c1][r2];
                if (r1 > 0 && r2 > 0) best = max(best, dp[r1-1][c1][r2-1]);
                if (r1 > 0 && c2 > 0) best = max(best, dp[r1-1][c1][r2]);
                if (c1 > 0 && r2 > 0) best = max(best, dp[r1][c1-1][r2-1]);
                if (c1 > 0 && c2 > 0) best = max(best, dp[r1][c1-1][r2]);
                
                if (best < 0) continue;
                
                int cherries = grid[r1][c1];
                if (r1 != r2 || c1 != c2) {
                    cherries += grid[r2][c2];
                }
                
                dp[r1][c1][r2] = best + cherries;
            }
        }
    }
    
    return max(0, dp[n-1][n-1][n-1]);
}
```

### Grid DP Patterns Summary

| Problem | State | Direction | Transition |
|---------|-------|-----------|------------|
| Unique Paths | dp[i][j] | Top-left to bottom-right | dp[i-1][j] + dp[i][j-1] |
| Min Path Sum | dp[i][j] | Top-left to bottom-right | grid[i][j] + min(up, left) |
| Dungeon Game | dp[i][j] | Bottom-right to top-left | max(1, min(down, right) - grid[i][j]) |
| Maximal Square | dp[i][j] | Top-left to bottom-right | 1 + min(up, left, diagonal) |
| Triangle | dp[i][j] | Top to bottom | triangle[i][j] + min(prev[j-1], prev[j]) |
---

## Next Step

- Go to [11_Knapsack_Problems.md](11_Knapsack_Problems.md) to continue with Knapsack Problems.
