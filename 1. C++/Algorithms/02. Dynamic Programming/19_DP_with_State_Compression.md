# 19_DP_with_State_Compression.md

## DP with State Compression

### Definition

State compression is a technique used to reduce the memory requirements of DP by representing states more efficiently. This is different from bitmask DP (which is a form of state compression). Here we focus on compressing continuous states into discrete ones, reducing dimensions, or using mathematical transformations.

### Types of State Compression

| Type | Description | Example |
|------|-------------|---------|
| Coordinate Compression | Map large values to smaller indices | Graph nodes numbered 1 to 10^9 → 1 to 10^5 |
| Rolling Array | Keep only necessary previous rows | dp[i] depends only on dp[i-1] |
| Bitmask Compression | Represent sets as bits | TSP with 2^n states |
| Mathematical Compression | Use formulas to reduce dimensions | Prefix sums, difference arrays |
| HashMap Compression | Store only visited states | Sparse DP with map |

### 1. Coordinate Compression

**Problem:** When state values are large but sparse, map them to consecutive integers.

```cpp
// Example: Given points on a line, compress coordinates
vector<int> compress(vector<int>& arr) {
    vector<int> sorted = arr;
    sort(sorted.begin(), sorted.end());
    sorted.erase(unique(sorted.begin(), sorted.end()), sorted.end());
    
    vector<int> compressed(arr.size());
    for (int i = 0; i < arr.size(); i++) {
        compressed[i] = lower_bound(sorted.begin(), sorted.end(), arr[i]) - sorted.begin();
    }
    
    return compressed;
}

// Example usage in DP: Grid with large coordinates
int gridDPWithCompression(vector<pair<int, int>>& points) {
    // Points have coordinates up to 10^9 but only n points
    vector<int> xs, ys;
    for (auto& p : points) {
        xs.push_back(p.first);
        ys.push_back(p.second);
    }
    
    vector<int> compressedX = compress(xs);
    vector<int> compressedY = compress(ys);
    
    // Now use compressedX[i] and compressedY[i] which are in range [0, n-1]
    // DP array size becomes O(n²) instead of O(10^18)
    
    vector<vector<int>> dp(xs.size(), vector<int>(ys.size(), 0));
    // ... DP logic
    
    return dp.back().back();
}
```

### 2. Rolling Array (Space Compression)

**Problem:** When DP only needs previous few rows, not entire table.

```cpp
// Example: 0/1 Knapsack with 1D rolling array
int knapsackRolling(int W, vector<int>& weights, vector<int>& values) {
    vector<int> dp(W + 1, 0);
    
    for (int i = 0; i < weights.size(); i++) {
        for (int w = W; w >= weights[i]; w--) {
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i]);
        }
    }
    
    return dp[W];
}

// Example: 2D DP with 2 rows
int lcsRolling(string s1, string s2) {
    int m = s1.length(), n = s2.length();
    vector<int> dp(n + 1, 0);
    vector<int> prev(n + 1, 0);
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (s1[i-1] == s2[j-1]) {
                dp[j] = prev[j-1] + 1;
            } else {
                dp[j] = max(prev[j], dp[j-1]);
            }
        }
        swap(dp, prev);
    }
    
    return prev[n];
}

// Example: Fibonacci with O(1) space
int fibonacciRolling(int n) {
    if (n <= 1) return n;
    int a = 0, b = 1, c;
    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}
```

### 3. Difference Array Compression

**Problem:** When DP involves range updates, use difference array to compress operations.

```cpp
// Example: Range increment queries
vector<int> rangeUpdateCompression(vector<vector<int>>& queries, int n) {
    vector<int> diff(n + 2, 0);
    
    for (auto& q : queries) {
        int l = q[0], r = q[1], val = q[2];
        diff[l] += val;
        diff[r + 1] -= val;
    }
    
    vector<int> result(n);
    int curr = 0;
    for (int i = 0; i < n; i++) {
        curr += diff[i];
        result[i] = curr;
    }
    
    return result;
}
```

### 4. Prefix Sum Compression

**Problem:** When DP needs sum over ranges, use prefix sums to get O(1) queries.

```cpp
// Example: DP with range sum queries
vector<int> prefixSumDP(vector<int>& arr) {
    int n = arr.size();
    vector<int> prefix(n + 1, 0);
    
    for (int i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + arr[i];
    }
    
    // Now sum from l to r = prefix[r+1] - prefix[l]
    
    // Example DP: dp[i] = max(dp[j] + sum(j+1, i)) for j < i
    vector<int> dp(n, 0);
    for (int i = 0; i < n; i++) {
        dp[i] = arr[i];  // base
        for (int j = 0; j < i; j++) {
            int sum = prefix[i + 1] - prefix[j + 1];
            dp[i] = max(dp[i], dp[j] + sum);
        }
    }
    
    return dp;
}
```

### 5. HashMap Compression (Sparse DP)

**Problem:** When state space is large but only few states are reachable.

```cpp
// Example: DP with large coordinates but sparse transitions
int sparseDP(unordered_map<int, int>& transitions, int target) {
    unordered_map<int, int> dp;
    dp[0] = 1;
    
    for (int step = 0; step < 10; step++) {
        unordered_map<int, int> next;
        for (auto& [state, count] : dp) {
            if (transitions.count(state)) {
                next[transitions[state]] += count;
            }
        }
        dp = move(next);
    }
    
    return dp[target];
}

// Example: DP on tree with large values but only n nodes
int treeDPWithHashMap(vector<vector<int>>& tree, int root) {
    unordered_map<int, unordered_map<int, int>> dp;
    
    function<void(int, int)> dfs = [&](int u, int parent) {
        dp[u][0] = 0;
        dp[u][1] = 1;
        
        for (int v : tree[u]) {
            if (v == parent) continue;
            dfs(v, u);
            
            unordered_map<int, int> newState;
            for (auto& [stateU, valU] : dp[u]) {
                for (auto& [stateV, valV] : dp[v]) {
                    if ((stateU & stateV) == 0) {
                        newState[stateU | stateV] = max(newState[stateU | stateV], valU + valV);
                    }
                }
            }
            dp[u] = move(newState);
        }
    };
    
    dfs(root, -1);
    
    int ans = 0;
    for (auto& [state, val] : dp[root]) {
        ans = max(ans, val);
    }
    return ans;
}
```

### 6. Mathematical State Compression

**Problem:** When state can be represented by a formula rather than a table.

```cpp
// Example: Arithmetic progression sum
long long arithmeticSum(long long a, long long d, long long n) {
    return n * (2 * a + (n - 1) * d) / 2;
}

// Example: DP for counting ways to climb stairs with 1,2,3 steps
// Instead of dp array, use matrix exponentiation
vector<vector<long long>> matMul(vector<vector<long long>>& a, vector<vector<long long>>& b) {
    int n = a.size();
    vector<vector<long long>> res(n, vector<long long>(n, 0));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                res[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    return res;
}

vector<vector<long long>> matPow(vector<vector<long long>>& mat, int exp) {
    int n = mat.size();
    vector<vector<long long>> res(n, vector<long long>(n, 0));
    for (int i = 0; i < n; i++) res[i][i] = 1;
    
    while (exp > 0) {
        if (exp & 1) res = matMul(res, mat);
        mat = matMul(mat, mat);
        exp >>= 1;
    }
    return res;
}

int climbStairsMatrix(int n) {
    if (n <= 1) return 1;
    vector<vector<long long>> mat = {{1, 1, 1}, {1, 0, 0}, {0, 1, 0}};
    vector<vector<long long>> res = matPow(mat, n - 2);
    return res[0][0] + res[0][1] + res[0][2];
}
```

### 7. Meet-in-the-Middle Compression

**Problem:** When 2^n is too large, split into two halves of size n/2 each.

```cpp
// Example: Subset sum with n up to 40 (2^40 too large)
vector<long long> generateSubsets(vector<int>& arr, int start, int end) {
    int len = end - start;
    vector<long long> sums;
    for (int mask = 0; mask < (1 << len); mask++) {
        long long sum = 0;
        for (int i = 0; i < len; i++) {
            if (mask & (1 << i)) {
                sum += arr[start + i];
            }
        }
        sums.push_back(sum);
    }
    return sums;
}

int countSubsetsWithSumMeetInMiddle(vector<int>& arr, int target) {
    int n = arr.size();
    int mid = n / 2;
    
    vector<long long> left = generateSubsets(arr, 0, mid);
    vector<long long> right = generateSubsets(arr, mid, n);
    
    sort(right.begin(), right.end());
    
    int count = 0;
    for (long long sum : left) {
        count += upper_bound(right.begin(), right.end(), target - sum) -
                 lower_bound(right.begin(), right.end(), target - sum);
    }
    
    return count;
}
```

### 8. Bitmask Compression for Permutations

**Problem:** Represent permutation as Lehmer code or factorial number system.

```cpp
// Convert permutation to Lehmer code (compressed representation)
vector<int> permutationToLehmer(vector<int>& perm) {
    int n = perm.size();
    vector<int> lehmer(n);
    
    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int j = i + 1; j < n; j++) {
            if (perm[j] < perm[i]) count++;
        }
        lehmer[i] = count;
    }
    
    return lehmer;
}

// Convert Lehmer code to permutation
vector<int> lehmerToPermutation(vector<int>& lehmer) {
    int n = lehmer.size();
    vector<int> perm;
    vector<int> available(n);
    for (int i = 0; i < n; i++) available[i] = i;
    
    for (int i = 0; i < n; i++) {
        perm.push_back(available[lehmer[i]]);
        available.erase(available.begin() + lehmer[i]);
    }
    
    return perm;
}
```

### Compression Techniques Summary

| Technique | Space Reduction | Time Complexity | Use Case |
|-----------|----------------|-----------------|----------|
| Coordinate Compression | O(N) to O(n) | O(n log n) | Large sparse coordinates |
| Rolling Array | O(N×M) to O(M) | Same | Sequential dependencies |
| Difference Array | O(N) to O(N) | O(1) per query | Range updates |
| Prefix Sum | O(N) to O(N) | O(1) per query | Range queries |
| HashMap | O(N×M) to O(K) | O(K) | Sparse reachable states |
| Meet-in-Middle | O(2^n) to O(2^(n/2)) | O(2^(n/2)) | n ≤ 40 |
| Matrix Exponentiation | O(n) to O(log n) | O(k³ log n) | Linear recurrences |
---

## Next Step

- Go to [20_DP_on_Intervals.md](20_DP_on_Intervals.md) to continue with DP on Intervals.
