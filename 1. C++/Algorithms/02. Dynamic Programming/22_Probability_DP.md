# 22_Probability_DP.md

## Probability DP

### Definition

Probability DP is a technique used to calculate probabilities or expected values of certain events in stochastic processes. The state represents the current situation, and transitions represent probabilistic outcomes.

### Key Concepts

| Term | Description |
|------|-------------|
| Probability | Likelihood of an event (0 to 1) |
| Expected Value | Weighted average of all possible outcomes |
| Conditional Probability | Probability given some condition |
| Random Variable | Variable whose values depend on random events |

### Important Formulas

```
Expected Value: E[X] = sum(p(i) * value(i))

Linearity of Expectation: E[X + Y] = E[X] + E[Y]

Total Probability: P(A) = sum(P(A|B_i) * P(B_i))

Geometric Distribution: E[trials until success] = 1/p
```

### Classic Probability DP Problems

#### 1. Dice Throw Probability

**Problem:** Find probability of getting sum S when throwing n dice.

```
State: dp[n][s] = probability of sum s with n dice
Transition: dp[n][s] = (1/6) * sum(dp[n-1][s-k]) for k=1 to 6
```

```cpp
double diceProbability(int n, int target) {
    vector<vector<double>> dp(n + 1, vector<double>(target + 1, 0));
    dp[0][0] = 1.0;
    
    for (int i = 1; i <= n; i++) {
        for (int s = 1; s <= target; s++) {
            for (int k = 1; k <= 6; k++) {
                if (s >= k) {
                    dp[i][s] += dp[i-1][s-k] / 6.0;
                }
            }
        }
    }
    
    return dp[n][target];
}
```

#### 2. Knight Probability on Chessboard

**Problem:** Probability that knight stays on board after k moves.

```
State: dp[k][i][j] = probability of being at (i,j) after k moves
Transition: dp[k][i][j] = sum(dp[k-1][ni][nj] / 8) for all valid knight moves
```

```cpp
double knightProbability(int n, int k, int row, int column) {
    vector<vector<double>> dp(n, vector<double>(n, 0));
    dp[row][column] = 1.0;
    
    int dirs[8][2] = {{-2,-1}, {-2,1}, {-1,-2}, {-1,2},
                      {1,-2}, {1,2}, {2,-1}, {2,1}};
    
    for (int move = 0; move < k; move++) {
        vector<vector<double>> next(n, vector<double>(n, 0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dp[i][j] > 0) {
                    for (auto& d : dirs) {
                        int ni = i + d[0];
                        int nj = j + d[1];
                        if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
                            next[ni][nj] += dp[i][j] / 8.0;
                        }
                    }
                }
            }
        }
        dp = next;
    }
    
    double ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            ans += dp[i][j];
        }
    }
    
    return ans;
}
```

#### 3. Soup Servings

**Problem:** Two types of soup. Each operation reduces amounts. Find probability that soup A runs out first.

```cpp
double soupServings(int n) {
    if (n >= 4800) return 1.0;  // optimization for large n
    
    n = (n + 24) / 25;  // scale down (each operation removes 25ml)
    vector<vector<double>> dp(n + 1, vector<double>(n + 1, 0));
    
    function<double(int, int)> solve = [&](int a, int b) {
        if (a <= 0 && b <= 0) return 0.5;
        if (a <= 0) return 1.0;
        if (b <= 0) return 0.0;
        if (dp[a][b] > 0) return dp[a][b];
        
        dp[a][b] = 0.25 * (solve(a-4, b) + solve(a-3, b-1) + 
                           solve(a-2, b-2) + solve(a-1, b-3));
        return dp[a][b];
    };
    
    return solve(n, n);
}
```

#### 4. Probability of Winning a Game

**Problem:** Two players. Player A wins point with probability p. First to win 2 points wins game. Find probability A wins.

```
State: dp[i][j] = probability A wins when A has i points, B has j points
```

```cpp
double probabilityWin(double p) {
    vector<vector<double>> dp(3, vector<double>(3, 0));
    
    // Base cases
    dp[2][0] = dp[2][1] = 1.0;
    dp[0][2] = dp[1][2] = 0.0;
    
    for (int i = 2; i >= 0; i--) {
        for (int j = 2; j >= 0; j--) {
            if (i == 2 || j == 2) continue;
            dp[i][j] = p * dp[i+1][j] + (1-p) * dp[i][j+1];
        }
    }
    
    return dp[0][0];
}
```

#### 5. Frog Jump Probability

**Problem:** Frog starts at position 0. At each step, it jumps 1, 2, or 3 units with equal probability. Find probability of landing exactly on position n.

```cpp
double frogProbability(int n) {
    vector<double> dp(n + 4, 0);
    dp[0] = 1.0;
    
    for (int i = 0; i <= n; i++) {
        for (int jump = 1; jump <= 3; jump++) {
            if (i + jump <= n) {
                dp[i + jump] += dp[i] / 3.0;
            }
        }
    }
    
    return dp[n];
}
```

#### 6. Expected Value of Dice Rolls

**Problem:** Expected number of rolls to get sum >= target.

```
State: E[s] = expected rolls needed when current sum is s
E[s] = 1 + (1/6) * sum(E[s+k]) for k=1 to 6
Base: E[s] = 0 for s >= target
```

```cpp
double expectedRolls(int target) {
    vector<double> E(target + 7, 0);
    
    for (int s = target - 1; s >= 0; s--) {
        double sum = 0;
        for (int k = 1; k <= 6; k++) {
            sum += E[s + k];
        }
        E[s] = 1 + sum / 6.0;
    }
    
    return E[0];
}
```

#### 7. Expected Value of Random Walk

**Problem:** Random walk on number line from 0 to n. At each step, move left with probability p, right with probability 1-p. Find expected steps to reach 0 or n.

```
State: E[i] = expected steps from position i
E[0] = 0, E[n] = 0
E[i] = 1 + p*E[i-1] + (1-p)*E[i+1]
```

```cpp
double expectedRandomWalk(int n, double p) {
    if (p == 0.5) {
        // Expected steps = i * (n - i)
        return i * (n - i);
    }
    
    vector<double> E(n + 1, 0);
    double q = 1 - p;
    
    // Solve using linear equations
    // E[i] - p*E[i-1] - q*E[i+1] = 1
    // This gives a system of equations
    
    // Alternative: closed form
    // For p != 0.5, E[i] = (i/(q-p)) - (n/(q-p)) * (1 - (q/p)^i) / (1 - (q/p)^n)
    
    return i / (q - p) - (n / (q - p)) * 
           (1 - pow(q/p, i)) / (1 - pow(q/p, n));
}
```

#### 8. Expected Value of Geometric Distribution

**Problem:** Probability of success = p. Expected number of trials until first success.

```cpp
double expectedTrials(double p) {
    return 1.0 / p;
}
```

#### 9. Probability of Reaching Target in Maze

**Problem:** Grid with obstacles. Probability of reaching target moving randomly.

```cpp
double probabilityReachingTarget(vector<vector<int>>& grid, int steps) {
    int m = grid.size(), n = grid[0].size();
    vector<vector<double>> dp(m, vector<double>(n, 0));
    
    // Assume target is bottom-right
    dp[m-1][n-1] = 1.0;
    int dirs[4][2] = {{-1,0}, {1,0}, {0,-1}, {0,1}};
    
    for (int step = 0; step < steps; step++) {
        vector<vector<double>> next(m, vector<double>(n, 0));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) continue;
                
                int validMoves = 0;
                for (auto& d : dirs) {
                    int ni = i + d[0], nj = j + d[1];
                    if (ni >= 0 && ni < m && nj >= 0 && nj < n && grid[ni][nj] == 0) {
                        validMoves++;
                    }
                }
                
                if (validMoves == 0) {
                    next[i][j] += dp[i][j];
                } else {
                    for (auto& d : dirs) {
                        int ni = i + d[0], nj = j + d[1];
                        if (ni >= 0 && ni < m && nj >= 0 && nj < n && grid[ni][nj] == 0) {
                            next[ni][nj] += dp[i][j] / validMoves;
                        }
                    }
                }
            }
        }
        dp = next;
    }
    
    return dp[0][0];
}
```

#### 10. Probability of Generating String

**Problem:** Type random characters. Find probability of generating target string within k attempts.

```cpp
double probabilityGenerateString(string target, vector<double>& charProbs, int k) {
    int n = target.length();
    vector<double> dp(k + 1, 0);
    dp[0] = 1.0;
    
    // Probability of typing correct character at each position
    double correctProb = 1.0;
    for (char c : target) {
        correctProb *= charProbs[c - 'a'];
    }
    double wrongProb = 1.0 - correctProb;
    
    for (int attempt = 1; attempt <= k; attempt++) {
        dp[attempt] = dp[attempt-1] * wrongProb;
        if (attempt >= n) {
            dp[attempt] += correctProb;
        }
    }
    
    return dp[k];
}
```

### Expected Value DP Template

```cpp
// For expected value, we often work backwards from base cases
vector<double> E(n, 0);
// Base cases: E[terminal] = 0

for (int i = n-1; i >= 0; i--) {
    double sum = 0;
    for (int transition : transitions) {
        sum += E[nextState] * probability;
    }
    E[i] = 1 + sum;  // +1 for current step
}
```

### Probability DP Template

```cpp
// For probability, we work forwards from starting state
vector<double> dp(n, 0);
dp[start] = 1.0;

for (int step = 0; step < maxSteps; step++) {
    vector<double> next(n, 0);
    for (int i = 0; i < n; i++) {
        for (int transition : transitions) {
            next[nextState] += dp[i] * probability;
        }
    }
    dp = next;
}
```

### Common Pitfalls

1. Not normalizing probabilities (sum should be 1)
2. Forgetting to add +1 for current step in expected value
3. Not handling absorbing states correctly
4. Floating point precision issues
5. Infinite loops in expected value (solving linear equations)
---

## Next Step

- Go to [23_DP_on_DAGs.md](23_DP_on_DAGs.md) to continue with DP on DAGs.
