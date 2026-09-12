# Euler Tour Technique and Tree Flattening

## 📖 Overview

The **Euler Tour Technique (ETT)**, also known as **Tree Flattening**, is a method of linearizing a hierarchical tree structure into a one-dimensional array using Depth-First Search (DFS) discovery and exit timestamps. 

By mapping the 2D tree hierarchy into a 1D sequence, the entire subtree of any node $u$ becomes a **contiguous subarray** $[tin[u], tout[u]]$. This fundamental transformation allows standard 1D range-query data structures—such as **Segment Trees** and **Fenwick Trees (Binary Indexed Trees)**—to perform dynamic updates and queries on subtrees in **$O(\log N)$** time.

---

## 🎯 Theoretical Foundation

### 1. DFS Timestamps (`tin` and `tout`)
During a single DFS traversal starting from the root:
- Maintain a global discrete logical clock `timer`.
- When entering node $u$, record the discovery timestamp: $tin[u] = \text{++timer}$.
- Recursively visit all unvisited children of $u$.
- When leaving node $u$ after all its descendants have been processed, record the exit timestamp: $tout[u] = \text{timer}$.

```
                Tree View                           Flattened 1D Time Axis
                    1                               timer:  1   2   3   4   5   6   7   8
                  /   \                             Node:  [1 | 2 | 4 | 5 | 3 | 6 | 7 | 8]
                 2     3                                    └─── Subtree of 1 ────────────┘
                / \     \                                   └── Subtree 2 ──┘
               4   5     6                                          │
                        / \                                      tin[2]=2, tout[2]=4
                       7   8
```

### 2. The Subtree Containment Theorem
> **Theorem**: Node $v$ belongs to the subtree rooted at node $u$ if and only if:
> $$tin[u] \le tin[v] \le tout[u]$$

**Proof:**
- By the Parenthesis Theorem of Depth-First Search, the interval $[tin[v], tout[v]]$ for any descendant $v$ is strictly nested inside the interval $[tin[u], tout[u]]$ of its ancestor $u$.
- If $v$ is in $u$'s subtree, DFS must visit $v$ after entering $u$ ($tin[u] \le tin[v]$) and must finish $v$ before leaving $u$ ($tout[v] \le tout[u]$).
- Conversely, if $v$ is not in $u$'s subtree, the intervals $[tin[u], tout[u]]$ and $[tin[v], tout[v]]$ are completely disjoint. $\blacksquare$

---

## ⚡ Key Applications

### 1. $O(1)$ Ancestor Verification
We can determine whether node $u$ is an ancestor of node $v$ in strict **$O(1)$** time without traversing any pointers:
```cpp
bool isAncestor(int u, int v) const {
    return tin[u] <= tin[v] && tout[u] >= tout[v];
}
```

### 2. Subtree Queries via 1D Data Structures
Because the nodes of $u$'s subtree correspond to the contiguous indices from $tin[u]$ to $tout[u]$ in the flattened array:
- **Subtree Sum**: $\sum_{v \in \text{subtree}(u)} \text{value}(v) = \text{RangeSum}(tin[u], tout[u])$.
- **Subtree Point Update**: Updating $\text{value}(u)$ is simply a point update at index $tin[u]$.
- **Subtree Range Update**: Adding $X$ to all nodes in $u$'s subtree is a range update over $[tin[u], tout[u]]$ in a Segment Tree with Lazy Propagation.

---

## 💻 Complete C++ Implementation

```cpp
#include <iostream>
#include <vector>
#include <cassert>
#include <iomanip>
#include <string>

// ---------------------------------------------------------------------
// 1. Classical 1D Segment Tree with Point Update & Range Sum Query
// ---------------------------------------------------------------------
class SegmentTree {
private:
    int n;
    std::vector<long long> tree;

    void build(const std::vector<long long>& arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = arr[start];
            return;
        }
        int mid = start + (end - start) / 2;
        build(arr, 2 * node, start, mid);
        build(arr, 2 * node + 1, mid + 1, end);
        tree[node] = tree[2 * node] + tree[2 * node + 1];
    }

    void update(int node, int start, int end, int idx, long long val) {
        if (start == end) {
            tree[node] += val;
            return;
        }
        int mid = start + (end - start) / 2;
        if (idx <= mid) {
            update(2 * node, start, mid, idx, val);
        } else {
            update(2 * node + 1, mid + 1, end, idx, val);
        }
        tree[node] = tree[2 * node] + tree[2 * node + 1];
    }

    long long query(int node, int start, int end, int l, int r) const {
        if (r < start || end < l) return 0; // Out of bounds
        if (l <= start && end <= r) return tree[node]; // Total overlap

        int mid = start + (end - start) / 2;
        long long leftSum = query(2 * node, start, mid, l, r);
        long long rightSum = query(2 * node + 1, mid + 1, end, l, r);
        return leftSum + rightSum;
    }

public:
    SegmentTree(int size) : n(size), tree(4 * size + 4, 0) {}

    void init(const std::vector<long long>& arr) {
        build(arr, 1, 1, n);
    }

    void add(int idx, long long delta) {
        update(1, 1, n, idx, delta);
    }

    long long rangeSum(int l, int r) const {
        if (l > r) return 0;
        return query(1, 1, n, l, r);
    }
};

// ---------------------------------------------------------------------
// 2. Euler Tour Tree with Subtree Query Engine
// ---------------------------------------------------------------------
class EulerTourTree {
private:
    int n;
    int root;
    int timer;
    std::vector<std::vector<int>> adj;
    std::vector<long long> nodeValues;
    std::vector<int> tin;
    std::vector<int> tout;
    std::vector<int> flatNodeAtTime; // flatNodeAtTime[t] = node whose tin is t
    SegmentTree segTree;

    void dfs(int u, int p) {
        tin[u] = ++timer;
        flatNodeAtTime[timer] = u;

        for (int v : adj[u]) {
            if (v != p) {
                dfs(v, u);
            }
        }
        tout[u] = timer;
    }

public:
    EulerTourTree(int numNodes, int treeRoot = 1)
        : n(numNodes), root(treeRoot), timer(0),
          adj(n + 1), nodeValues(n + 1, 0),
          tin(n + 1, 0), tout(n + 1, 0),
          flatNodeAtTime(n + 1, 0),
          segTree(numNodes) {}

    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    void setNodeValue(int u, long long val) {
        nodeValues[u] = val;
    }

    void build() {
        timer = 0;
        dfs(root, 0);

        // Map initial node values onto flattened 1D time array
        std::vector<long long> flatArray(n + 1, 0);
        for (int u = 1; u <= n; u++) {
            flatArray[tin[u]] = nodeValues[u];
        }
        segTree.init(flatArray);
    }

    // O(1) Ancestor Check
    bool isAncestor(int u, int v) const {
        return tin[u] <= tin[v] && tout[u] >= tout[v];
    }

    // O(log N) Dynamic Point Update: Add delta to value of node u
    void updateNode(int u, long long delta) {
        nodeValues[u] += delta;
        segTree.add(tin[u], delta);
    }

    // O(log N) Subtree Sum Query: Returns sum of values in subtree of u
    long long querySubtreeSum(int u) const {
        return segTree.rangeSum(tin[u], tout[u]);
    }

    // Accessors for diagnostics
    int getTin(int u) const { return tin[u]; }
    int getTout(int u) const { return tout[u]; }
    long long getNodeValue(int u) const { return nodeValues[u]; }

    void printFlattenedTour() const {
        std::cout << "Flattened Euler Tour Array (Indices 1 to " << n << "):\n";
        std::cout << "  Time:  ";
        for (int t = 1; t <= n; t++) std::cout << std::setw(4) << t;
        std::cout << "\n  Node:  ";
        for (int t = 1; t <= n; t++) std::cout << std::setw(4) << flatNodeAtTime[t];
        std::cout << "\n  Value: ";
        for (int t = 1; t <= n; t++) std::cout << std::setw(4) << nodeValues[flatNodeAtTime[t]];
        std::cout << "\n\n";
    }
};

int main() {
    std::cout << "=== Euler Tour Tree Flattening Comprehensive Test Harness ===\n\n";

    /*
         Tree Structure:
                   1 (Val: 10)
                 /   \
          (20)  2     3  (30)
               / \     \
        (40)  4   5     6  (60)
            (50)       / \
                (70)  7   8  (80)
    */

    const int NUM_NODES = 8;
    EulerTourTree ett(NUM_NODES, 1);

    ett.addEdge(1, 2);
    ett.addEdge(1, 3);
    ett.addEdge(2, 4);
    ett.addEdge(2, 5);
    ett.addEdge(3, 6);
    ett.addEdge(6, 7);
    ett.addEdge(6, 8);

    ett.setNodeValue(1, 10);
    ett.setNodeValue(2, 20);
    ett.setNodeValue(3, 30);
    ett.setNodeValue(4, 40);
    ett.setNodeValue(5, 50);
    ett.setNodeValue(6, 60);
    ett.setNodeValue(7, 70);
    ett.setNodeValue(8, 80);

    ett.build();

    std::cout << "--- 1. Subtree Intervals [tin, tout] ---\n";
    for (int i = 1; i <= NUM_NODES; i++) {
        std::cout << "  Node " << i << ": tin=" << ett.getTin(i) 
                  << ", tout=" << ett.getTout(i) 
                  << ", Subtree Size=" << (ett.getTout(i) - ett.getTin(i) + 1) << "\n";
    }
    std::cout << "\n";

    ett.printFlattenedTour();

    std::cout << "--- 2. O(1) Ancestor Tests ---\n";
    std::cout << "  Is 1 ancestor of 7? " << (ett.isAncestor(1, 7) ? "YES (True)" : "NO") << "\n";
    std::cout << "  Is 3 ancestor of 7? " << (ett.isAncestor(3, 7) ? "YES (True)" : "NO") << "\n";
    std::cout << "  Is 2 ancestor of 7? " << (ett.isAncestor(2, 7) ? "YES" : "NO (Correct)") << "\n";
    std::cout << "  Is 6 ancestor of 6? " << (ett.isAncestor(6, 6) ? "YES (True)" : "NO") << "\n";
    assert(ett.isAncestor(1, 7) == true);
    assert(ett.isAncestor(3, 7) == true);
    assert(ett.isAncestor(2, 7) == false);
    assert(ett.isAncestor(6, 6) == true);
    std::cout << "  All Ancestor Invariants: PASSED\n\n";

    std::cout << "--- 3. Subtree Sum Queries ---\n";
    // Subtree of 4: {4} = 40
    std::cout << "  Subtree sum of Node 4 [Expected: 40]: " << ett.querySubtreeSum(4) << "\n";
    assert(ett.querySubtreeSum(4) == 40);

    // Subtree of 2: {2, 4, 5} = 20 + 40 + 50 = 110
    std::cout << "  Subtree sum of Node 2 [Expected: 110]: " << ett.querySubtreeSum(2) << "\n";
    assert(ett.querySubtreeSum(2) == 110);

    // Subtree of 6: {6, 7, 8} = 60 + 70 + 80 = 210
    std::cout << "  Subtree sum of Node 6 [Expected: 210]: " << ett.querySubtreeSum(6) << "\n";
    assert(ett.querySubtreeSum(6) == 210);

    // Subtree of 3: {3, 6, 7, 8} = 30 + 210 = 240
    std::cout << "  Subtree sum of Node 3 [Expected: 240]: " << ett.querySubtreeSum(3) << "\n";
    assert(ett.querySubtreeSum(3) == 240);

    // Total Tree (Subtree of 1): 10 + 110 + 240 = 360
    std::cout << "  Total tree sum (Subtree of 1) [Expected: 360]: " << ett.querySubtreeSum(1) << "\n";
    assert(ett.querySubtreeSum(1) == 360);
    std::cout << "  All Subtree Sum Queries: PASSED\n\n";

    std::cout << "--- 4. Dynamic Point Updates & Re-queries ---\n";
    std::cout << "  Adding +25 to Node 5 (originally 50)...\n";
    ett.updateNode(5, 25);

    std::cout << "  New Subtree sum of Node 2 [Expected: 135]: " << ett.querySubtreeSum(2) << "\n";
    assert(ett.querySubtreeSum(2) == 135);

    std::cout << "  New Total tree sum [Expected: 385]: " << ett.querySubtreeSum(1) << "\n";
    assert(ett.querySubtreeSum(1) == 385);

    std::cout << "  Adding +100 to Root Node 1...\n";
    ett.updateNode(1, 100);
    std::cout << "  New Total tree sum [Expected: 485]: " << ett.querySubtreeSum(1) << "\n";
    assert(ett.querySubtreeSum(1) == 485);

    // Subtree of 2 should be completely unchanged by root modification
    std::cout << "  Subtree sum of Node 2 [Still 135]: " << ett.querySubtreeSum(2) << "\n";
    assert(ett.querySubtreeSum(2) == 135);

    std::cout << "\n=== All Euler Tour Tree Tests Completed Successfully! ===\n";
    return 0;
}
```

---

## 📊 Complexity Analysis

| Phase / Operation | Time Complexity | Space Complexity | Notes |
| :--- | :--- | :--- | :--- |
| **DFS Tree Flattening** | $O(N)$ | $O(N)$ | Single traversal populating `tin`/`tout` |
| **Segment Tree Build** | $O(N)$ | $O(N)$ | Linear bottom-up construction |
| **$O(1)$ Ancestor Check** | $O(1)$ | $O(1)$ | Boundary check on $[tin, tout]$ |
| **Point Node Update** | $O(\log N)$ | $O(1)$ | Point update at `tin[u]` |
| **Subtree Range Sum** | $O(\log N)$ | $O(1)$ | Query over $[tin[u], tout[u]]$ |
| **Subtree Range Update** | $O(\log N)$ | $O(1)$ | Supported via Segment Tree Lazy Propagation |

---

## 💡 Practical Insights & Comparison with HLD

1. **Subtree vs Path Operations**:
   - **Euler Tour Technique (ETT)** is the optimal choice when operations target **subtrees** (e.g., "add $V$ to all nodes in subtree of $u$", "find maximum value in subtree of $u$"). A single range $[tin[u], tout[u]]$ captures the entire subtree.
   - **Heavy-Light Decomposition (HLD)** is needed when operations target **paths** between two arbitrary nodes (e.g., "add $V$ to all nodes on the simple path from $u$ to $v$"). HLD decomposes paths into at most $O(\log N)$ heavy segments, answering path queries in $O(\log^2 N)$.
2. **Fenwick Tree Alternative**:
   - If only point updates and range sums are needed (without range updates or range max/min), replacing the Segment Tree with a **Fenwick Tree (Binary Indexed Tree)** reduces memory usage to $N \times 8$ bytes and provides smaller constant factor execution speeds.
