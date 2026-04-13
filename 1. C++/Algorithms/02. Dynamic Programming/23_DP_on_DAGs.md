# 23_DP_on_DAGs.md

## DP on DAGs (Directed Acyclic Graphs)

### Definition

A DAG is a directed graph with no cycles. DP on DAGs is straightforward because we can process nodes in topological order, ensuring that when we process a node, all its dependencies have already been processed.

### Key Property

In a DAG, there exists a topological ordering where for every directed edge u → v, u comes before v in the ordering.

### Why DP Works on DAGs

- No cycles means no circular dependencies
- Can process in topological order
- Each node's value depends only on its predecessors or successors
- Many graph problems become tractable on DAGs

### Topological Ordering Methods

```cpp
// DFS-based topological sort
void dfs(int u, vector<vector<int>>& adj, vector<bool>& visited, vector<int>& order) {
    visited[u] = true;
    for (int v : adj[u]) {
        if (!visited[v]) {
            dfs(v, adj, visited, order);
        }
    }
    order.push_back(u);
}

vector<int> topologicalSortDFS(vector<vector<int>>& adj, int n) {
    vector<bool> visited(n, false);
    vector<int> order;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, adj, visited, order);
        }
    }
    reverse(order.begin(), order.end());
    return order;
}

// Kahn's algorithm (BFS-based)
vector<int> topologicalSortKahn(vector<vector<int>>& adj, int n) {
    vector<int> indegree(n, 0);
    for (int u = 0; u < n; u++) {
        for (int v : adj[u]) {
            indegree[v]++;
        }
    }
    
    queue<int> q;
    for (int i = 0; i < n; i++) {
        if (indegree[i] == 0) {
            q.push(i);
        }
    }
    
    vector<int> order;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        order.push_back(u);
        for (int v : adj[u]) {
            indegree[v]--;
            if (indegree[v] == 0) {
                q.push(v);
            }
        }
    }
    
    return order;
}
```

### Classic DP on DAG Problems

#### 1. Longest Path in DAG

**Problem:** Find the longest path (maximum sum of weights) from source to any node.

```
State: dp[v] = longest distance from source to v
Transition: for each edge u → v with weight w: dp[v] = max(dp[v], dp[u] + w)
Order: topological
```

```cpp
int longestPathDAG(vector<vector<pair<int, int>>>& adj, int source, int n) {
    vector<int> topo = topologicalSortKahn(adj, n);
    vector<int> dist(n, INT_MIN);
    dist[source] = 0;
    
    for (int u : topo) {
        if (dist[u] == INT_MIN) continue;
        for (auto& [v, w] : adj[u]) {
            dist[v] = max(dist[v], dist[u] + w);
        }
    }
    
    int ans = 0;
    for (int i = 0; i < n; i++) {
        ans = max(ans, dist[i]);
    }
    return ans;
}
```

#### 2. Shortest Path in DAG

**Problem:** Find the shortest path from source to all nodes (can handle negative weights because no cycles).

```
State: dp[v] = shortest distance from source to v
Transition: for each edge u → v with weight w: dp[v] = min(dp[v], dp[u] + w)
Order: topological
```

```cpp
vector<int> shortestPathDAG(vector<vector<pair<int, int>>>& adj, int source, int n) {
    vector<int> topo = topologicalSortKahn(adj, n);
    vector<int> dist(n, INT_MAX);
    dist[source] = 0;
    
    for (int u : topo) {
        if (dist[u] == INT_MAX) continue;
        for (auto& [v, w] : adj[u]) {
            dist[v] = min(dist[v], dist[u] + w);
        }
    }
    
    return dist;
}
```

#### 3. Number of Paths in DAG

**Problem:** Count number of paths from source to destination.

```
State: dp[v] = number of paths from source to v
Base: dp[source] = 1
Transition: for each edge u → v: dp[v] += dp[u]
Order: topological
```

```cpp
int countPathsDAG(vector<vector<int>>& adj, int source, int dest, int n) {
    vector<int> topo = topologicalSortKahn(adj, n);
    vector<int> dp(n, 0);
    dp[source] = 1;
    
    for (int u : topo) {
        for (int v : adj[u]) {
            dp[v] += dp[u];
        }
    }
    
    return dp[dest];
}
```

#### 4. Longest Increasing Subsequence (as DAG)

**Problem:** LIS can be modeled as longest path in DAG where edge i → j exists if i < j and arr[i] < arr[j].

```cpp
int LISasDAG(vector<int>& arr) {
    int n = arr.size();
    vector<vector<int>> adj(n);
    
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] < arr[j]) {
                adj[i].push_back(j);
            }
        }
    }
    
    vector<int> topo = topologicalSortKahn(adj, n);
    vector<int> dp(n, 1);
    
    for (int i : topo) {
        for (int j : adj[i]) {
            dp[j] = max(dp[j], dp[i] + 1);
        }
    }
    
    return *max_element(dp.begin(), dp.end());
}
```

#### 5. Minimum Path Cost in Grid (as DAG)

**Problem:** Grid where you can only move right or down (forms a DAG).

```cpp
int minPathCostGrid(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    vector<vector<int>> dp(m, vector<int>(n, 0));
    dp[0][0] = grid[0][0];
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (i > 0) {
                dp[i][j] = min(dp[i][j], dp[i-1][j] + grid[i][j]);
            }
            if (j > 0) {
                dp[i][j] = min(dp[i][j], dp[i][j-1] + grid[i][j]);
            }
        }
    }
    
    return dp[m-1][n-1];
}
```

#### 6. Course Schedule (Prerequisite Chains)

**Problem:** Find minimum semesters to complete all courses given prerequisites.

```cpp
int minSemesters(int n, vector<vector<int>>& prerequisites) {
    vector<vector<int>> adj(n);
    vector<int> indegree(n, 0);
    
    for (auto& preq : prerequisites) {
        int u = preq[1], v = preq[0];  // u must be taken before v
        adj[u].push_back(v);
        indegree[v]++;
    }
    
    queue<int> q;
    for (int i = 0; i < n; i++) {
        if (indegree[i] == 0) {
            q.push(i);
        }
    }
    
    vector<int> semester(n, 0);
    int maxSemester = 0;
    
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        maxSemester = max(maxSemester, semester[u]);
        
        for (int v : adj[u]) {
            indegree[v]--;
            semester[v] = max(semester[v], semester[u] + 1);
            if (indegree[v] == 0) {
                q.push(v);
            }
        }
    }
    
    return maxSemester + 1;
}
```

#### 7. Maximum Score from DAG (Job Scheduling)

**Problem:** Each node has a value. Find maximum sum path in DAG.

```cpp
int maxSumPathDAG(vector<vector<int>>& adj, vector<int>& values, int n) {
    vector<int> topo = topologicalSortKahn(adj, n);
    vector<int> dp = values;  // dp[v] = max sum ending at v
    
    for (int u : topo) {
        for (int v : adj[u]) {
            dp[v] = max(dp[v], dp[u] + values[v]);
        }
    }
    
    return *max_element(dp.begin(), dp.end());
}
```

#### 8. Number of Ways to Reach Destination with Time Constraint

**Problem:** Count paths from source to destination that take exactly K time.

```
State: dp[t][v] = number of ways to reach v at time t
Transition: for each edge u → v with time w: dp[t][v] += dp[t-w][u]
```

```cpp
int countPathsWithTime(int n, vector<vector<int>>& edges, int source, int dest, int K) {
    vector<vector<pair<int, int>>> adj(n);
    for (auto& e : edges) {
        int u = e[0], v = e[1], w = e[2];
        adj[u].push_back({v, w});
    }
    
    vector<vector<int>> dp(K + 1, vector<int>(n, 0));
    dp[0][source] = 1;
    
    for (int t = 1; t <= K; t++) {
        for (int u = 0; u < n; u++) {
            if (dp[t-1][u] == 0) continue;
            for (auto& [v, w] : adj[u]) {
                if (t - 1 + w <= K) {
                    dp[t - 1 + w][v] += dp[t-1][u];
                }
            }
        }
    }
    
    int ans = 0;
    for (int t = 0; t <= K; t++) {
        ans += dp[t][dest];
    }
    
    return ans;
}
```

#### 9. Minimum Number of Coins (Coin Change as DAG)

**Problem:** States are amounts from 0 to target. Edge from amount a to a+coin exists.

```cpp
int minCoinsDAG(vector<int>& coins, int target) {
    vector<vector<int>> adj(target + 1);
    
    for (int a = 0; a < target; a++) {
        for (int coin : coins) {
            if (a + coin <= target) {
                adj[a].push_back(a + coin);
            }
        }
    }
    
    vector<int> dp(target + 1, INT_MAX);
    dp[0] = 0;
    
    for (int a = 0; a <= target; a++) {
        if (dp[a] == INT_MAX) continue;
        for (int next : adj[a]) {
            dp[next] = min(dp[next], dp[a] + 1);
        }
    }
    
    return dp[target];
}
```

#### 10. Maximum Profit from Tasks with Dependencies

**Problem:** Each task takes time and gives profit. Tasks have dependencies. Find maximum profit with deadline.

```cpp
struct Task {
    int time, profit;
    vector<int> dependencies;
};

int maxProfitWithDependencies(vector<Task>& tasks, int deadline, int n) {
    // Build DAG
    vector<vector<int>> adj(n);
    for (int i = 0; i < n; i++) {
        for (int dep : tasks[i].dependencies) {
            adj[dep].push_back(i);
        }
    }
    
    vector<int> topo = topologicalSortKahn(adj, n);
    
    // dp[t][i] = max profit ending at task i at time t
    vector<vector<int>> dp(deadline + 1, vector<int>(n, -1e9));
    
    for (int i = 0; i < n; i++) {
        if (tasks[i].dependencies.empty()) {
            if (tasks[i].time <= deadline) {
                dp[tasks[i].time][i] = tasks[i].profit;
            }
        }
    }
    
    for (int t = 0; t <= deadline; t++) {
        for (int u : topo) {
            if (dp[t][u] < 0) continue;
            for (int v : adj[u]) {
                int newTime = t + tasks[v].time;
                if (newTime <= deadline) {
                    dp[newTime][v] = max(dp[newTime][v], dp[t][u] + tasks[v].profit);
                }
            }
        }
    }
    
    int ans = 0;
    for (int t = 0; t <= deadline; t++) {
        for (int i = 0; i < n; i++) {
            ans = max(ans, dp[t][i]);
        }
    }
    
    return ans;
}
```

### DAG DP Summary

| Problem | DP State | Transition | Time Complexity |
|---------|----------|------------|-----------------|
| Longest Path | dist[v] | max(dist[u] + w) | O(V + E) |
| Shortest Path | dist[v] | min(dist[u] + w) | O(V + E) |
| Count Paths | dp[v] | sum(dp[u]) | O(V + E) |
| Max Sum Path | dp[v] | max(dp[u] + val[v]) | O(V + E) |
| Time-Constrained | dp[t][v] | sum(dp[t-w][u]) | O(T × E) |
---

## Next Step

- Go to [24_Optimization_Techniques.md](24_Optimization_Techniques.md) to continue with Optimization Techniques.
