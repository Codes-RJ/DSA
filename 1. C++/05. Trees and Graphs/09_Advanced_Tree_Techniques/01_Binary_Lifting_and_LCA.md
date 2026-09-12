# Binary Lifting and Lowest Common Ancestor (LCA)

## 📖 Overview

The **Lowest Common Ancestor (LCA)** of two nodes $u$ and $v$ in a rooted tree is the deepest node that is an ancestor of both $u$ and $v$. Finding the LCA is a fundamental primitive in tree algorithms, used for:
- Computing shortest path distances between any two tree nodes.
- Finding minimum or maximum edge weights along a tree path.
- Resolving network routing and phylogenetic tree queries.

While a naive traversal takes $O(N)$ time per query, **Binary Lifting** is a dynamic programming technique based on powers of two that answers each LCA query in **$O(\log N)$** time after an **$O(N \log N)$** offline preprocessing phase.

---

## 🎯 Binary Lifting Principle

Every positive integer $D$ has a unique representation in binary:
$$D = \sum_{i=0}^{\lfloor \log_2 D \rfloor} b_i \cdot 2^i, \quad b_i \in \{0, 1\}$$

Therefore, walking $D$ steps up from node $u$ towards the root does not require $D$ sequential parent traversals. Instead, we can break the journey into at most $\log_2 D$ jumps, where each jump length is a power of two ($1, 2, 4, 8, \dots, 2^k$).

```
                      Node: u
                        │  (jump 2^0 = 1)
                     up[u][0]
                        │  (jump 2^1 = 2)
                     up[u][1] = up[ up[u][0] ][0]
                        │  (jump 2^2 = 4)
                     up[u][2] = up[ up[u][1] ][1]
                        │
                     up[u][k] = up[ up[u][k-1] ][k-1]
```

### Dynamic Programming Recurrence
Let $\text{up}[u][k]$ denote the $2^k$-th ancestor of node $u$:
$$\text{up}[u][0] = \text{parent}[u]$$
$$\text{up}[u][k] = \text{up}\Big[\text{up}[u][k-1]\Big][k-1]$$

Meaning: To jump $2^k$ steps up from $u$, first jump $2^{k-1}$ steps to reach intermediate node $w = \text{up}[u][k-1]$, and then from $w$ jump another $2^{k-1}$ steps ($2^{k-1} + 2^{k-1} = 2^k$).

---

## 🔍 The LCA Query Algorithm

Given two nodes $u$ and $v$:

```
Step 1: Equalize Depths                      Step 2: Synchronous Lifting
        (u deeper than v)                         (jump up if ancestors differ)

             o (Root)                                      o (Root)
             │                                             │
             v                                           LCA(u,v)
            / \                                           /     \
           .   .                                         o       o
          /     \                                       / \     / \
         o       o                                     u   .   .   v  (same depth)
        /
       u  (jump up by depth difference)
```

1. **Equalize Depths**:
   - Without loss of generality, assume $\text{depth}[u] \ge \text{depth}[v]$.
   - Let $\Delta = \text{depth}[u] - \text{depth}[v]$.
   - For each bit $k$ where $\Delta$ has a 1 ($(\Delta \gg k) \ \& \ 1$), lift $u$ to $\text{up}[u][k]$.
   - Now, $\text{depth}[u] = \text{depth}[v]$.

2. **Check for Direct Ancestor**:
   - If $u == v$, then $v$ was an ancestor of $u$. Return $u$.

3. **Synchronous Binary Lifting**:
   - Iterate $k$ from $\text{LOG} - 1$ down to $0$:
     - If $\text{up}[u][k] \neq \text{up}[v][k]$, then the LCA lies strictly above this $2^k$ jump.
     - Therefore, both $u$ and $v$ safely jump up: $u = \text{up}[u][k]$ and $v = \text{up}[v][k]$.
     - If $\text{up}[u][k] == \text{up}[v][k]$, the jump overshoots the LCA or lands on it; we do not jump, but test smaller powers of two.

4. **Final Step**:
   - At the end of the loop, $u$ and $v$ are immediate children of the LCA.
   - Return $\text{up}[u][0]$ (the parent of $u$).

---

## 📏 Path Aggregates & Distance

Once $\text{LCA}(u, v)$ is known:
1. **Tree Distance**:
   $$\text{dist}(u, v) = \text{depth}[u] + \text{depth}[v] - 2 \cdot \text{depth}[\text{LCA}(u, v)]$$

2. **Path Aggregation (e.g., Maximum Edge Weight)**:
   - Augment the table with $\text{maxWeight}[u][k]$, storing the maximum edge weight on the path from $u$ to its $2^k$-th ancestor:
     $$\text{maxWeight}[u][k] = \max\Big(\text{maxWeight}[u][k-1], \;\; \text{maxWeight}[\text{up}[u][k-1]][k-1]\Big)$$
   - During depth equalization and synchronous lifting, aggregate the maximum edge weights.

---

## 💻 Complete C++ Implementation

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cassert>
#include <iomanip>

class TreeLCA {
public:
    struct Edge {
        int to;
        int weight;
    };

private:
    int n;
    int logN;
    int root;
    std::vector<std::vector<Edge>> adj;
    std::vector<int> depth;
    std::vector<std::vector<int>> up;        // up[u][k] = 2^k-th ancestor of u
    std::vector<std::vector<int>> maxEdge;   // maxEdge[u][k] = max weight from u to 2^k-th ancestor

    void dfs(int u, int p, int d, int edgeWeight) {
        depth[u] = d;
        up[u][0] = p;
        maxEdge[u][0] = edgeWeight;

        // Populate binary lifting sparse table for node u
        for (int k = 1; k < logN; k++) {
            int mid = up[u][k - 1];
            up[u][k] = up[mid][k - 1];
            maxEdge[u][k] = std::max(maxEdge[u][k - 1], maxEdge[mid][k - 1]);
        }

        for (const auto& edge : adj[u]) {
            if (edge.to != p) {
                dfs(edge.to, u, d + 1, edge.weight);
            }
        }
    }

public:
    TreeLCA(int numNodes, int treeRoot = 1) : n(numNodes), root(treeRoot) {
        logN = static_cast<int>(std::ceil(std::log2(std::max(2, n)))) + 1;
        adj.resize(n + 1);
        depth.assign(n + 1, 0);
        up.assign(n + 1, std::vector<int>(logN, treeRoot));
        maxEdge.assign(n + 1, std::vector<int>(logN, 0));
    }

    void addEdge(int u, int v, int weight = 1) {
        adj[u].push_back({v, weight});
        adj[v].push_back({u, weight});
    }

    void preprocess() {
        dfs(root, root, 0, 0);
    }

    // Query k-th ancestor of node u (returns -1 if depth < k)
    int getKthAncestor(int u, int k) const {
        if (depth[u] < k) return -1;

        for (int i = 0; i < logN; i++) {
            if ((k >> i) & 1) {
                u = up[u][i];
            }
        }
        return u;
    }

    // Query Lowest Common Ancestor of u and v in O(log N)
    int getLCA(int u, int v) const {
        // Step 1: Ensure u is deeper than or equal to v
        if (depth[u] < depth[v]) {
            std::swap(u, v);
        }

        // Step 2: Lift u to the same depth as v
        int diff = depth[u] - depth[v];
        for (int k = 0; k < logN; k++) {
            if ((diff >> k) & 1) {
                u = up[u][k];
            }
        }

        if (u == v) return u;

        // Step 3: Synchronous lifting
        for (int k = logN - 1; k >= 0; k--) {
            if (up[u][k] != up[v][k]) {
                u = up[u][k];
                v = up[v][k];
            }
        }

        // Step 4: Parent of u is the LCA
        return up[u][0];
    }

    // Query tree distance (number of edges or path sum) between u and v
    int getDistance(int u, int v) const {
        int lca = getLCA(u, v);
        return depth[u] + depth[v] - 2 * depth[lca];
    }

    // Query maximum edge weight along the simple path between u and v
    int getMaxEdgeOnPath(int u, int v) const {
        if (u == v) return 0;

        int maxWeight = 0;

        // Ensure u is deeper than v
        if (depth[u] < depth[v]) {
            std::swap(u, v);
        }

        // Lift u to same depth as v, aggregating max edge weight
        int diff = depth[u] - depth[v];
        for (int k = 0; k < logN; k++) {
            if ((diff >> k) & 1) {
                maxWeight = std::max(maxWeight, maxEdge[u][k]);
                u = up[u][k];
            }
        }

        if (u == v) return maxWeight;

        // Synchronously lift both nodes
        for (int k = logN - 1; k >= 0; k--) {
            if (up[u][k] != up[v][k]) {
                maxWeight = std::max(maxWeight, maxEdge[u][k]);
                maxWeight = std::max(maxWeight, maxEdge[v][k]);
                u = up[u][k];
                v = up[v][k];
            }
        }

        // Add last edges connecting to LCA
        maxWeight = std::max(maxWeight, maxEdge[u][0]);
        maxWeight = std::max(maxWeight, maxEdge[v][0]);

        return maxWeight;
    }

    int getDepth(int u) const { return depth[u]; }
};

int main() {
    std::cout << "=== Binary Lifting & LCA Comprehensive Test Harness ===\n\n";

    /*
         Tree Structure with Edge Weights:
                   1 (Root, depth 0)
                 /   \
           (4)  /     \ (7)
               2       3
             /   \      \
       (2)  /     \ (5)  \ (1)
           4       5      6
          /       / \
    (8)  /   (3) /   \ (6)
        7       8     9
    */

    const int NUM_NODES = 9;
    TreeLCA tree(NUM_NODES, 1);

    tree.addEdge(1, 2, 4);
    tree.addEdge(1, 3, 7);
    tree.addEdge(2, 4, 2);
    tree.addEdge(2, 5, 5);
    tree.addEdge(3, 6, 1);
    tree.addEdge(4, 7, 8);
    tree.addEdge(5, 8, 3);
    tree.addEdge(5, 9, 6);

    tree.preprocess();

    std::cout << "--- 1. Depths of All Nodes ---\n";
    for (int i = 1; i <= NUM_NODES; i++) {
        std::cout << "  Node " << i << ": Depth = " << tree.getDepth(i) << "\n";
    }
    std::cout << "\n";

    std::cout << "--- 2. K-th Ancestor Queries ---\n";
    std::cout << "  2nd ancestor of Node 7 (should be 2): " << tree.getKthAncestor(7, 2) << "\n";
    std::cout << "  3rd ancestor of Node 8 (should be 1): " << tree.getKthAncestor(8, 3) << "\n";
    std::cout << "  1st ancestor of Node 1 (Root, should be 1 or clamped): " << tree.getKthAncestor(1, 1) << "\n";
    std::cout << "  5th ancestor of Node 4 (exceeds depth, returns -1): " << tree.getKthAncestor(4, 5) << "\n\n";

    std::cout << "--- 3. Lowest Common Ancestor (LCA) Queries ---\n";
    struct LCATest { int u, v, expected; };
    std::vector<LCATest> tests = {
        {7, 8, 2},  // Siblings' children
        {8, 9, 5},  // Immediate siblings
        {7, 4, 4},  // Direct ancestor
        {7, 6, 1},  // Cross-branch via root
        {3, 6, 3},  // Parent-child
        {9, 9, 9}   // Self
    };

    for (const auto& t : tests) {
        int lca = tree.getLCA(t.u, t.v);
        std::cout << "  LCA(" << t.u << ", " << t.v << ") = " << lca 
                  << " [Expected: " << t.expected << "] => " 
                  << (lca == t.expected ? "PASSED" : "FAILED") << "\n";
        assert(lca == t.expected);
    }
    std::cout << "\n";

    std::cout << "--- 4. Tree Distance Queries ---\n";
    std::cout << "  Distance between Node 7 and Node 8 (7-4-2-5-8 = 4 edges): " 
              << tree.getDistance(7, 8) << "\n";
    std::cout << "  Distance between Node 7 and Node 6 (7-4-2-1-3-6 = 5 edges): " 
              << tree.getDistance(7, 6) << "\n";
    std::cout << "  Distance between Node 1 and Node 9 (1-2-5-9 = 3 edges): " 
              << tree.getDistance(1, 9) << "\n\n";

    std::cout << "--- 5. Maximum Edge Weight on Tree Path ---\n";
    // Path 7 -> 8: 7-(8)-4-(2)-2-(5)-5-(3)-8 => Max edge weight is 8
    std::cout << "  Max edge weight on path (7, 8) [Expected: 8]: " << tree.getMaxEdgeOnPath(7, 8) << "\n";
    assert(tree.getMaxEdgeOnPath(7, 8) == 8);

    // Path 8 -> 9: 8-(3)-5-(6)-9 => Max edge weight is 6
    std::cout << "  Max edge weight on path (8, 9) [Expected: 6]: " << tree.getMaxEdgeOnPath(8, 9) << "\n";
    assert(tree.getMaxEdgeOnPath(8, 9) == 6);

    // Path 2 -> 6: 2-(4)-1-(7)-3-(1)-6 => Max edge weight is 7
    std::cout << "  Max edge weight on path (2, 6) [Expected: 7]: " << tree.getMaxEdgeOnPath(2, 6) << "\n";
    assert(tree.getMaxEdgeOnPath(2, 6) == 7);

    std::cout << "\n=== All Binary Lifting & LCA Tests Completed Successfully! ===\n";
    return 0;
}
```

---

## 📊 Complexity Analysis

| Phase / Operation | Time Complexity | Auxiliary Space |
| :--- | :--- | :--- |
| **DFS Traversal & Depth Setup** | $O(N)$ | $O(N)$ (recursion stack) |
| **Binary Lifting Precomputation** | $O(N \log N)$ | $O(N \log N)$ (`up` and `maxEdge` tables) |
| **$k$-th Ancestor Query** | $O(\log N)$ | $O(1)$ |
| **LCA Query** | $O(\log N)$ | $O(1)$ |
| **Tree Distance Query** | $O(\log N)$ | $O(1)$ |
| **Path Aggregate (Min/Max/Sum)** | $O(\log N)$ | $O(1)$ |

---

## 💡 Practical Engineering Insights

1. **Table Dimensioning**:
   - Set $\text{LOG} = \lfloor \log_2 N \rfloor + 1$. For $N \le 2 \times 10^5$, $\log_2(200000) \approx 17.6$, so $\text{LOG} = 19$ or $20$ is more than sufficient.
2. **Root Clamping Trick**:
   - By setting $\text{up}[\text{root}][k] = \text{root}$ for all $k$, any jump that overshoots above the root safely lands on the root without throwing out-of-bounds exceptions.
3. **Memory Optimization**:
   - If only basic LCA and distance queries are needed without path weights, omit the `maxEdge` table. The storage requirement drops to $N \times \text{LOG} \times 4$ bytes (e.g., $\approx 15 \text{ MB}$ for $N = 2 \times 10^5$).
