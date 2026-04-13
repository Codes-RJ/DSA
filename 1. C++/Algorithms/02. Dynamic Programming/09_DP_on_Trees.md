# 09_DP_on_Trees.md

## DP on Trees

### Definition

Tree DP involves solving dynamic programming problems on tree structures. The DP is typically performed using DFS (Depth First Search) where we compute answers for children first and then combine them for the parent.

### Key Concept

In tree DP, the state is usually defined at a node. The transition combines information from all children. The order is post-order (process children before parent).

### Classic Tree DP Problems

#### 1. Tree Diameter (Longest Path Between Two Nodes)

**Problem:** Find the longest path between any two nodes in a tree.

```
State: 
    depth[u] = longest path from u to any leaf in its subtree
    diameter = max(diameter, depth[child1] + depth[child2] + 2)
```

```cpp
int diameter = 0;

int dfs(int u, int parent, vector<vector<int>>& adj) {
    int maxDepth1 = 0, maxDepth2 = 0;
    
    for (int v : adj[u]) {
        if (v == parent) continue;
        int childDepth = dfs(v, u, adj);
        
        if (childDepth > maxDepth1) {
            maxDepth2 = maxDepth1;
            maxDepth1 = childDepth;
        } else if (childDepth > maxDepth2) {
            maxDepth2 = childDepth;
        }
    }
    
    diameter = max(diameter, maxDepth1 + maxDepth2);
    return maxDepth1 + 1;
}

// Call: dfs(root, -1, adj)
// Answer: diameter
```

#### 2. Maximum Sum Path in a Tree

**Problem:** Find the path with maximum sum (node values can be negative).

```
State: 
    maxPathFrom[u] = maximum sum path from u to any node in its subtree
    ans = max(ans, maxPathFrom[u], maxPathFrom[child1] + maxPathFrom[child2] + val[u])
```

```cpp
int ans = INT_MIN;

int dfs(int u, int parent, vector<vector<int>>& adj, vector<int>& val) {
    int maxPathFromU = val[u];
    int maxChild1 = 0, maxChild2 = 0;
    
    for (int v : adj[u]) {
        if (v == parent) continue;
        int childPath = dfs(v, u, adj, val);
        
        if (childPath > maxChild1) {
            maxChild2 = maxChild1;
            maxChild1 = childPath;
        } else if (childPath > maxChild2) {
            maxChild2 = childPath;
        }
    }
    
    // Path that goes through u
    ans = max(ans, val[u] + maxChild1 + maxChild2);
    // Path that starts at u and goes down
    ans = max(ans, val[u] + maxChild1);
    // Just u alone
    ans = max(ans, val[u]);
    
    return val[u] + maxChild1;
}
```

#### 3. Tree DP - Maximum Independent Set

**Problem:** Largest set of nodes with no adjacent nodes selected.

```
State:
    dp[u][0] = max independent set in subtree when u is NOT selected
    dp[u][1] = max independent set in subtree when u IS selected

Transition:
    dp[u][0] = sum over children of max(dp[v][0], dp[v][1])
    dp[u][1] = 1 + sum over children of dp[v][0]
```

```cpp
vector<vector<int>> dp;

void dfs(int u, int parent, vector<vector<int>>& adj) {
    dp[u][0] = 0;
    dp[u][1] = 1;
    
    for (int v : adj[u]) {
        if (v == parent) continue;
        dfs(v, u, adj);
        dp[u][0] += max(dp[v][0], dp[v][1]);
        dp[u][1] += dp[v][0];
    }
}

// Initialize dp with size n x 2
// Call: dfs(root, -1, adj)
// Answer: max(dp[root][0], dp[root][1])
```

#### 4. Tree DP - Minimum Vertex Cover

**Problem:** Smallest set of nodes such that every edge has at least one endpoint in the set.

```
State:
    dp[u][0] = min vertex cover in subtree when u is NOT selected
    dp[u][1] = min vertex cover in subtree when u IS selected

Transition:
    dp[u][0] = sum over children of dp[v][1]  (if u not selected, all children must be selected)
    dp[u][1] = 1 + sum over children of min(dp[v][0], dp[v][1])
```

```cpp
vector<vector<int>> dp;

void dfs(int u, int parent, vector<vector<int>>& adj) {
    dp[u][0] = 0;
    dp[u][1] = 1;
    
    for (int v : adj[u]) {
        if (v == parent) continue;
        dfs(v, u, adj);
        dp[u][0] += dp[v][1];
        dp[u][1] += min(dp[v][0], dp[v][1]);
    }
}

// Answer: min(dp[root][0], dp[root][1])
```

#### 5. Tree DP - Tree Coloring (No Two Adjacent Same Color)

**Problem:** Color the tree with k colors such that no two adjacent nodes have same color. Count number of ways.

```
State: dp[u][c] = number of ways to color subtree of u with color c

Transition:
    dp[u][c] = product over children of (sum over color != c of dp[v][color])
```

```cpp
vector<vector<long long>> dp;
int k;
long long MOD = 1e9 + 7;

void dfs(int u, int parent, vector<vector<int>>& adj) {
    for (int c = 0; c < k; c++) {
        dp[u][c] = 1;
    }
    
    for (int v : adj[u]) {
        if (v == parent) continue;
        dfs(v, u, adj);
        
        for (int c = 0; c < k; c++) {
            long long sum = 0;
            for (int other = 0; other < k; other++) {
                if (other != c) {
                    sum = (sum + dp[v][other]) % MOD;
                }
            }
            dp[u][c] = (dp[u][c] * sum) % MOD;
        }
    }
}

// Answer: sum over c of dp[root][c]
```

#### 6. Tree DP - Distance Sum

**Problem:** For each node, find sum of distances to all other nodes.

```
Step 1: First DFS to compute subtree sizes and initial sum for root
Step 2: Second DFS (rerooting) to compute for all nodes

State:
    size[u] = number of nodes in subtree of u
    dp[u] = sum of distances from u to all nodes in its subtree
    ans[u] = sum of distances from u to all nodes in the tree

Transition for rerooting:
    ans[v] = ans[u] + (n - 2*size[v])
```

```cpp
vector<int> size;
vector<long long> dp, ans;
int n;

void dfs1(int u, int parent, vector<vector<int>>& adj) {
    size[u] = 1;
    dp[u] = 0;
    
    for (int v : adj[u]) {
        if (v == parent) continue;
        dfs1(v, u, adj);
        size[u] += size[v];
        dp[u] += dp[v] + size[v];
    }
}

void dfs2(int u, int parent, vector<vector<int>>& adj) {
    for (int v : adj[u]) {
        if (v == parent) continue;
        ans[v] = ans[u] + (n - 2 * size[v]);
        dfs2(v, u, adj);
    }
}

// Call: dfs1(root, -1, adj)
// ans[root] = dp[root]
// dfs2(root, -1, adj)
// Final answer: ans array
```

#### 7. Tree DP - Longest Path in a Tree (For Each Node)

**Problem:** For each node, find the longest path starting from that node.

```
State:
    down1[u] = longest path from u going down to leaf
    down2[u] = second longest path from u going down to leaf
    up[u] = longest path from u going upward (through parent)
```

```cpp
vector<int> down1, down2, up;

void dfsDown(int u, int parent, vector<vector<int>>& adj) {
    down1[u] = 0;
    down2[u] = 0;
    
    for (int v : adj[u]) {
        if (v == parent) continue;
        dfsDown(v, u, adj);
        int cand = down1[v] + 1;
        
        if (cand > down1[u]) {
            down2[u] = down1[u];
            down1[u] = cand;
        } else if (cand > down2[u]) {
            down2[u] = cand;
        }
    }
}

void dfsUp(int u, int parent, vector<vector<int>>& adj) {
    for (int v : adj[u]) {
        if (v == parent) continue;
        
        if (down1[u] == down1[v] + 1) {
            up[v] = max(up[u], down2[u]) + 1;
        } else {
            up[v] = max(up[u], down1[u]) + 1;
        }
        
        dfsUp(v, u, adj);
    }
}

// Call: dfsDown(root, -1, adj)
// up[root] = 0
// dfsUp(root, -1, adj)
// For each node u, longest path from u = max(down1[u], up[u])
```

### Tree DP Patterns Summary

| Problem | State Definition | Transition |
|---------|-----------------|------------|
| Diameter | depth[u] | max(depth[c1] + depth[c2]) |
| Max Independent Set | dp[u][0/1] | sum over children |
| Min Vertex Cover | dp[u][0/1] | sum over children |
| Tree Coloring | dp[u][c] | product over children |
| Distance Sum | size[u], dp[u] | rerooting formula |
| Longest Path from Node | down1[u], down2[u], up[u] | DFS + rerooting |

### Practice Problems for Tree DP

| Problem | Description |
|---------|-------------|
| Tree Diameter | Find longest path between any two nodes |
| Tree Distance Sum | Sum of distances from each node |
| Maximum Independent Set | Largest set with no adjacent nodes |
| Minimum Vertex Cover | Smallest set covering all edges |
| Tree Coloring | Count valid colorings |
| Binary Tree Cameras | Minimum cameras to monitor tree |
| House Robber III | Tree version of house robber |
| Longest Path in Tree | For each node, longest path from it |

---
---

## Next Step

- Go to [10_DP_on_Grids.md](10_DP_on_Grids.md) to continue with DP on Grids.
