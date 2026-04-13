# 17_DP_with_Bitmasks.md

## DP with Bitmasks

### Definition

Bitmask DP is a technique where we use a binary number (bitmask) to represent a set of items. Each bit represents whether an element is included (1) or not (0). This is useful for problems with small n (typically n ≤ 20).

### Why Bitmask DP

When n is small (≤ 20), we can represent all subsets of items using a bitmask from 0 to 2^n - 1. This allows us to solve problems like:

- Traveling Salesman Problem (TSP)
- Assigning tasks to workers
- Set cover problems
- Hamiltonian path/cycle

### Bitmask Basics

| Operation | Code | Description |
|-----------|------|-------------|
| Check if bit i is set | `(mask >> i) & 1` | Returns 1 if set |
| Set bit i | `mask \| (1 << i)` | Turns bit i to 1 |
| Clear bit i | `mask & ~(1 << i)` | Turns bit i to 0 |
| Toggle bit i | `mask ^ (1 << i)` | Flips bit i |
| Get lowest set bit | `mask & -mask` | Isolates lowest 1 |
| Count set bits | `__builtin_popcount(mask)` | Number of 1's |
| All bits set | `(1 << n) - 1` | All n bits are 1 |

### Classic Problem: Traveling Salesman Problem (TSP)

**Problem:** Given n cities and distances between them, find the shortest path that visits each city exactly once and returns to the starting city.

```
State: dp[mask][i] = minimum distance to visit all cities in mask, ending at city i

Base: dp[1 << i][i] = distance from start to i (assuming start is city 0)

Transition: dp[mask][i] = min over j in mask of (dp[mask ^ (1<<i)][j] + dist[j][i])

Answer: min over i of (dp[(1<<n)-1][i] + dist[i][0])
```

```cpp
int tsp(vector<vector<int>>& dist) {
    int n = dist.size();
    int fullMask = (1 << n) - 1;
    
    // dp[mask][i] = min distance to visit mask ending at i
    vector<vector<int>> dp(1 << n, vector<int>(n, INT_MAX));
    
    // Start from city 0
    dp[1 << 0][0] = 0;
    
    for (int mask = 1; mask <= fullMask; mask++) {
        for (int i = 0; i < n; i++) {
            if (dp[mask][i] == INT_MAX) continue;
            
            // Try going to next city j
            for (int j = 0; j < n; j++) {
                if (mask & (1 << j)) continue;  // j already visited
                int newMask = mask | (1 << j);
                dp[newMask][j] = min(dp[newMask][j], 
                                     dp[mask][i] + dist[i][j]);
            }
        }
    }
    
    // Return to start
    int ans = INT_MAX;
    for (int i = 0; i < n; i++) {
        if (dp[fullMask][i] != INT_MAX) {
            ans = min(ans, dp[fullMask][i] + dist[i][0]);
        }
    }
    
    return ans;
}
```

### Problem 2: Assigning Tasks to Workers

**Problem:** There are n tasks and n workers. Each worker has a cost for each task. Assign each task to exactly one worker to minimize total cost.

```
State: dp[mask] = minimum cost to assign tasks represented by mask
mask bit i = 1 means task i has been assigned

Transition: dp[mask] = min over i where bit i is set of 
            (dp[mask ^ (1<<i)] + cost[workerCount][i])

workerCount = number of set bits in mask (which worker is assigned)
```

```cpp
int assignTasks(vector<vector<int>>& cost) {
    int n = cost.size();
    vector<int> dp(1 << n, INT_MAX);
    dp[0] = 0;
    
    for (int mask = 0; mask < (1 << n); mask++) {
        int worker = __builtin_popcount(mask);  // current worker to assign
        
        for (int task = 0; task < n; task++) {
            if (!(mask & (1 << task))) {  // task not assigned
                int newMask = mask | (1 << task);
                dp[newMask] = min(dp[newMask], 
                                  dp[mask] + cost[worker][task]);
            }
        }
    }
    
    return dp[(1 << n) - 1];
}
```

### Problem 3: Hamiltonian Path

**Problem:** Find a path that visits each vertex exactly once (not necessarily returning to start).

```
State: dp[mask][i] = true if there is a path visiting mask ending at i

Transition: dp[mask][i] = OR over j in mask of (dp[mask ^ (1<<i)][j] AND edge[j][i])
```

```cpp
bool hasHamiltonianPath(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<vector<bool>> dp(1 << n, vector<bool>(n, false));
    
    // Start from any node
    for (int i = 0; i < n; i++) {
        dp[1 << i][i] = true;
    }
    
    for (int mask = 1; mask < (1 << n); mask++) {
        for (int i = 0; i < n; i++) {
            if (!dp[mask][i]) continue;
            
            for (int j = 0; j < n; j++) {
                if (mask & (1 << j)) continue;  // j already visited
                if (graph[i][j]) {
                    dp[mask | (1 << j)][j] = true;
                }
            }
        }
    }
    
    int fullMask = (1 << n) - 1;
    for (int i = 0; i < n; i++) {
        if (dp[fullMask][i]) return true;
    }
    return false;
}
```

### Problem 4: Hamiltonian Cycle

Similar to TSP but for existence (unweighted graph).

```cpp
bool hasHamiltonianCycle(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<vector<bool>> dp(1 << n, vector<bool>(n, false));
    
    // Start from node 0
    dp[1 << 0][0] = true;
    
    for (int mask = 1; mask < (1 << n); mask++) {
        for (int i = 0; i < n; i++) {
            if (!dp[mask][i]) continue;
            
            for (int j = 0; j < n; j++) {
                if (mask & (1 << j)) continue;
                if (graph[i][j]) {
                    dp[mask | (1 << j)][j] = true;
                }
            }
        }
    }
    
    int fullMask = (1 << n) - 1;
    for (int i = 0; i < n; i++) {
        if (dp[fullMask][i] && graph[i][0]) return true;
    }
    return false;
}
```

### Problem 5: Set Cover

**Problem:** Given a universe of elements and subsets, find the minimum number of subsets that cover all elements.

```
State: dp[mask] = minimum subsets needed to cover mask
mask bit i = 1 means element i is covered

Transition: for each subset with its own subMask:
    dp[mask | subMask] = min(dp[mask | subMask], dp[mask] + 1)
```

```cpp
int setCover(int n, vector<int>& subsets) {
    // subsets[i] is a bitmask representing which elements subset i covers
    vector<int> dp(1 << n, INT_MAX);
    dp[0] = 0;
    
    for (int mask = 0; mask < (1 << n); mask++) {
        if (dp[mask] == INT_MAX) continue;
        
        for (int subMask : subsets) {
            int newMask = mask | subMask;
            dp[newMask] = min(dp[newMask], dp[mask] + 1);
        }
    }
    
    return dp[(1 << n) - 1];
}
```

### Problem 6: Minimum Cost to Partition Array

**Problem:** Partition array into k subsets with minimum cost.

```cpp
int minCostPartition(vector<int>& arr, int k) {
    int n = arr.size();
    vector<int> cost(1 << n, 0);
    
    // Precompute cost for each subset
    for (int mask = 1; mask < (1 << n); mask++) {
        int sum = 0;
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) {
                sum += arr[i];
            }
        }
        cost[mask] = sum * sum;  // example cost function
    }
    
    // dp[mask][c] = min cost to partition mask into c subsets
    vector<vector<int>> dp(1 << n, vector<int>(k + 1, INT_MAX));
    dp[0][0] = 0;
    
    for (int mask = 0; mask < (1 << n); mask++) {
        for (int c = 0; c < k; c++) {
            if (dp[mask][c] == INT_MAX) continue;
            
            int remaining = ((1 << n) - 1) ^ mask;
            // iterate over submasks of remaining
            for (int sub = remaining; sub; sub = (sub - 1) & remaining) {
                dp[mask | sub][c + 1] = min(dp[mask | sub][c + 1], 
                                             dp[mask][c] + cost[sub]);
            }
        }
    }
    
    return dp[(1 << n) - 1][k];
}
```

### Problem 7: SOS DP (Sum Over Subsets)

**Problem:** For each mask, compute sum over all submasks.

```
F[mask] = sum over sub of A[sub] where sub is submask of mask
```

```cpp
vector<int> sosDP(vector<int>& A, int n) {
    vector<int> F = A;  // copy
    
    for (int i = 0; i < n; i++) {
        for (int mask = 0; mask < (1 << n); mask++) {
            if (mask & (1 << i)) {
                F[mask] += F[mask ^ (1 << i)];
            }
        }
    }
    
    return F;
}
```

### Problem 8: Counting Subsets with Given Sum

**Problem:** Count number of subsets with sum = target (n ≤ 20).

```cpp
int countSubsetsWithSum(vector<int>& nums, int target) {
    int n = nums.size();
    unordered_map<int, int> firstHalf, secondHalf;
    
    int half = n / 2;
    
    // Generate all subsets of first half
    for (int mask = 0; mask < (1 << half); mask++) {
        int sum = 0;
        for (int i = 0; i < half; i++) {
            if (mask & (1 << i)) sum += nums[i];
        }
        firstHalf[sum]++;
    }
    
    // Generate all subsets of second half
    int secondSize = n - half;
    for (int mask = 0; mask < (1 << secondSize); mask++) {
        int sum = 0;
        for (int i = 0; i < secondSize; i++) {
            if (mask & (1 << i)) sum += nums[half + i];
        }
        secondHalf[sum]++;
    }
    
    // Combine
    int ans = 0;
    for (auto& [sum, count] : firstHalf) {
        if (secondHalf.count(target - sum)) {
            ans += count * secondHalf[target - sum];
        }
    }
    
    return ans;
}
```

### Complexity Summary

| Problem | States | Transition | Time Complexity |
|---------|--------|------------|-----------------|
| TSP | 2^n × n | O(n) | O(2^n × n²) |
| Task Assignment | 2^n | O(n) | O(2^n × n) |
| Hamiltonian Path | 2^n × n | O(n) | O(2^n × n²) |
| Set Cover | 2^n | O(number of subsets) | O(2^n × m) |
| SOS DP | 2^n | O(n) | O(n × 2^n) |
---

## Next Step

- Go to [18_Digit_DP.md](18_Digit_DP.md) to continue with Digit DP.
