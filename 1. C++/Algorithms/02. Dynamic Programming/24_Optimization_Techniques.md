# 24_Optimization_Techniques.md

## Optimization Techniques for Dynamic Programming

### Definition

DP optimization techniques are used to reduce the time or space complexity of DP solutions, often from O(n³) to O(n²) or from O(n²) to O(n log n).

### When to Use Optimizations

| Technique | Time Reduction | Space Reduction | Use Case |
|-----------|---------------|-----------------|----------|
| Rolling Array | No change | O(n²) → O(n) | When only previous rows needed |
| Convex Hull Trick | O(n²) → O(n log n) | No change | dp[i] = min(mⱼ×xᵢ + cⱼ) |
| Divide and Conquer DP | O(k×n²) → O(k×n log n) | No change | dp[i][j] = min(dp[i-1][k] + C(k+1, j)) |
| Knuth Optimization | O(n³) → O(n²) | No change | Quadrangle inequality holds |
| Monotone Queue | O(n²) → O(n) | No change | Sliding window maximum/minimum |
| Knapsack Optimization | O(n×W) → O(n×W) | O(W) → O(W) | Unbounded knapsack |
| SOS DP | O(3ⁿ) → O(n×2ⁿ) | No change | Sum over subsets |

---

### 1. Rolling Array (Space Optimization)

**Concept:** When dp[i] depends only on a fixed number of previous states, store only those states.

**Before (O(n²) space):**
```cpp
vector<vector<int>> dp(n, vector<int>(m, 0));
```

**After (O(m) space):**
```cpp
vector<int> dp(m, 0);
vector<int> prev(m, 0);
```

**Example - LCS Space Optimization:**
```cpp
int lcs(string s1, string s2) {
    int m = s1.length(), n = s2.length();
    if (m < n) {
        swap(s1, s2);
        swap(m, n);
    }
    
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
```

---

### 2. Convex Hull Trick (CHT)

**Concept:** Optimize DP of the form:
```
dp[i] = min over j < i of (dp[j] + a[j] * x[i] + b[j])
```
where a[j] and b[j] come from previous states.

**Requirements:** Slopes (a[j]) are monotonic and x[i] is monotonic.

**Example - Minimum cost to partition array:**
```cpp
struct Line {
    long long m, b;  // y = m*x + b
    long long eval(long long x) { return m * x + b; }
};

bool isBad(Line l1, Line l2, Line l3) {
    // Check if l2 is unnecessary
    return (l3.b - l1.b) * (l1.m - l2.m) <= (l2.b - l1.b) * (l1.m - l3.m);
}

vector<Line> hull;

void addLine(long long m, long long b) {
    Line newLine = {m, b};
    while (hull.size() >= 2 && isBad(hull[hull.size()-2], hull.back(), newLine)) {
        hull.pop_back();
    }
    hull.push_back(newLine);
}

long long query(long long x) {
    // For monotonic x, maintain pointer
    static int ptr = 0;
    while (ptr + 1 < hull.size() && hull[ptr].eval(x) >= hull[ptr+1].eval(x)) {
        ptr++;
    }
    return hull[ptr].eval(x);
}
```

---

### 3. Divide and Conquer DP Optimization

**Concept:** Optimize DP of the form:
```
dp[i][j] = min over k < j of (dp[i-1][k] + C(k+1, j))
```
where the optimal split point for dp[i][j] is between opt[i][j-1] and opt[i][j+1].

**Condition:** Quadrangle inequality and monotonicity of opt.

**Template:**
```cpp
vector<vector<long long>> dp(K+1, vector<long long>(N+1, INF));
vector<vector<int>> opt(K+1, vector<int>(N+1, 0));

void compute(int i, int l, int r, int optL, int optR) {
    if (l > r) return;
    int mid = (l + r) / 2;
    
    int bestK = optL;
    dp[i][mid] = INF;
    
    for (int k = optL; k <= min(optR, mid-1); k++) {
        long long val = dp[i-1][k] + cost(k+1, mid);
        if (val < dp[i][mid]) {
            dp[i][mid] = val;
            bestK = k;
        }
    }
    
    opt[i][mid] = bestK;
    compute(i, l, mid-1, optL, bestK);
    compute(i, mid+1, r, bestK, optR);
}
```

---

### 4. Knuth Optimization

**Concept:** For DP of the form:
```
dp[i][j] = min over i < k < j of (dp[i][k] + dp[k][j] + C[i][j])
```
if opt[i][j-1] ≤ opt[i][j] ≤ opt[i+1][j] (monotonicity).

**Time Complexity:** O(n²) instead of O(n³).

**Example - Matrix Chain Multiplication with Knuth Optimization:**
```cpp
int matrixChainKnuth(vector<int>& dims) {
    int n = dims.size() - 1;
    vector<vector<int>> dp(n+1, vector<int>(n+1, 0));
    vector<vector<int>> opt(n+1, vector<int>(n+1, 0));
    
    for (int i = 1; i <= n; i++) {
        opt[i][i] = i;
    }
    
    for (int len = 2; len <= n; len++) {
        for (int i = 1; i <= n - len + 1; i++) {
            int j = i + len - 1;
            dp[i][j] = INT_MAX;
            
            for (int k = opt[i][j-1]; k <= opt[i+1][j]; k++) {
                int cost = dp[i][k] + dp[k+1][j] + dims[i-1] * dims[k] * dims[j];
                if (cost < dp[i][j]) {
                    dp[i][j] = cost;
                    opt[i][j] = k;
                }
            }
        }
    }
    
    return dp[1][n];
}
```

---

### 5. Monotone Queue Optimization (Sliding Window)

**Concept:** Optimize DP of the form:
```
dp[i] = min over j in window of (dp[j] + cost(j, i))
```
where the window slides as i increases.

**Example - Sliding Window Maximum:**
```cpp
vector<int> slidingWindowMax(vector<int>& arr, int k) {
    deque<int> dq;
    vector<int> result;
    
    for (int i = 0; i < arr.size(); i++) {
        // Remove out of window
        while (!dq.empty() && dq.front() <= i - k) {
            dq.pop_front();
        }
        
        // Remove smaller elements
        while (!dq.empty() && arr[dq.back()] <= arr[i]) {
            dq.pop_back();
        }
        
        dq.push_back(i);
        
        if (i >= k - 1) {
            result.push_back(arr[dq.front()]);
        }
    }
    
    return result;
}
```

**Example - DP with Sliding Window Minimum:**
```cpp
int dpWithSlidingWindow(vector<int>& arr, int k) {
    int n = arr.size();
    vector<int> dp(n, 0);
    deque<int> dq;
    
    for (int i = 0; i < n; i++) {
        // dp[i] = min(dp[j]) + arr[i] for j in [i-k, i-1]
        while (!dq.empty() && dq.front() < i - k) {
            dq.pop_front();
        }
        
        if (!dq.empty()) {
            dp[i] = dp[dq.front()] + arr[i];
        } else {
            dp[i] = arr[i];
        }
        
        while (!dq.empty() && dp[dq.back()] >= dp[i]) {
            dq.pop_back();
        }
        dq.push_back(i);
    }
    
    return dp[n-1];
}
```

---

### 6. Knapsack Optimization (Unbounded)

**Concept:** For unbounded knapsack, we can optimize using monotone queue for bounded knapsack.

**Unbounded Knapsack (already O(n×W)):**
```cpp
int unboundedKnapsack(int W, vector<int>& weights, vector<int>& values) {
    vector<int> dp(W + 1, 0);
    for (int i = 0; i < weights.size(); i++) {
        for (int w = weights[i]; w <= W; w++) {
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i]);
        }
    }
    return dp[W];
}
```

**Bounded Knapsack with Monotone Queue (O(n×W)):**
```cpp
int boundedKnapsack(int W, vector<int>& weights, vector<int>& values, vector<int>& counts) {
    int n = weights.size();
    vector<int> dp(W + 1, 0);
    vector<int> newdp(W + 1, 0);
    
    for (int i = 0; i < n; i++) {
        for (int r = 0; r < weights[i]; r++) {
            deque<int> dq;
            for (int k = 0; r + k * weights[i] <= W; k++) {
                int w = r + k * weights[i];
                int val = dp[w] - k * values[i];
                
                while (!dq.empty() && dq.back() <= val) {
                    dq.pop_back();
                }
                dq.push_back(val);
                
                while (!dq.empty() && k - counts[i] > 0 && dq.front() == dp[r + (k - counts[i] - 1) * weights[i]] - (k - counts[i] - 1) * values[i]) {
                    dq.pop_front();
                }
                
                newdp[w] = dq.front() + k * values[i];
            }
        }
        dp = newdp;
    }
    
    return dp[W];
}
```

---

### 7. SOS DP (Sum Over Subsets)

**Concept:** Compute sum over all subsets of a mask efficiently.

**Problem:** For each mask, compute F[mask] = sum over sub ⊆ mask of A[sub].

**Naive:** O(3ⁿ)

**SOS DP:** O(n × 2ⁿ)

```cpp
vector<int> sosDP(vector<int>& A, int n) {
    vector<int> F = A;
    
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

**Application - Subset Sum Queries:**
```cpp
// Preprocess to answer: sum of A[sub] for all sub ⊆ mask
vector<int> preprocessSOS(vector<int>& A, int n) {
    return sosDP(A, n);
}

// Answer query in O(1)
int query(int mask, vector<int>& F) {
    return F[mask];
}
```

---

### 8. Divide and Conquer on Trees (Centroid Decomposition)

**Concept:** Break tree into smaller parts using centroids to achieve O(n log n) complexity.

```cpp
vector<bool> removed;
vector<int> subtreeSize;

int getSubtreeSize(int u, int p, vector<vector<int>>& adj) {
    subtreeSize[u] = 1;
    for (int v : adj[u]) {
        if (v != p && !removed[v]) {
            subtreeSize[u] += getSubtreeSize(v, u, adj);
        }
    }
    return subtreeSize[u];
}

int findCentroid(int u, int p, int totalSize, vector<vector<int>>& adj) {
    for (int v : adj[u]) {
        if (v != p && !removed[v] && subtreeSize[v] > totalSize / 2) {
            return findCentroid(v, u, totalSize, adj);
        }
    }
    return u;
}

void solveSubtree(int centroid, vector<vector<int>>& adj) {
    // Solve problems for paths passing through centroid
    // Then recursively solve for each component
    
    removed[centroid] = true;
    for (int v : adj[centroid]) {
        if (!removed[v]) {
            int totalSize = getSubtreeSize(v, -1, adj);
            int newCentroid = findCentroid(v, -1, totalSize, adj);
            solveSubtree(newCentroid, adj);
        }
    }
}
```

---

### Optimization Techniques Summary

| Technique | Original Complexity | Optimized Complexity | Condition |
|-----------|--------------------|---------------------|-----------|
| Rolling Array | O(n×m) time, O(n×m) space | O(n×m) time, O(m) space | Only previous rows needed |
| Convex Hull Trick | O(n²) | O(n log n) | Monotonic slopes and queries |
| Divide and Conquer DP | O(k×n²) | O(k×n log n) | Quadrangle inequality |
| Knuth Optimization | O(n³) | O(n²) | Quadrangle inequality |
| Monotone Queue | O(n×k) | O(n) | Sliding window |
| SOS DP | O(3ⁿ) | O(n×2ⁿ) | Sum over subsets |
| Centroid Decomposition | O(n²) | O(n log n) | Tree problems |

---
---

## Next Step

- Go to [Theory.md](Theory.md) to continue with Theory.
