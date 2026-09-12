# Disjoint Set Union (Union-Find) in C++

## 📖 Overview

The **Disjoint Set Union (DSU)**—also known as **Union-Find**—is a specialized data structure that tracks a set of elements partitioned into a number of disjoint (non-overlapping) subsets.

It provides near-constant time operations to:
1. **Find**: Determine which subset a particular element belongs to (useful for determining if two elements are in the same subset).
2. **Union**: Merge two subsets into a single subset.

---

## ⚡ Core Optimizations & Complexity

### 1. Path Compression
During the `find(x)` operation, we make every traversed node point directly to the root. This flattens the tree structure, ensuring subsequent lookups take $O(1)$ time.

```
Before Compression:          After Compression:
       4                            4
      /                            /|\
     3                            1 2 3
    /
   2
  /
 1
```

### 2. Union by Rank / Union by Size
When merging two sets, always attach the root of the smaller/shallower tree to the root of the larger/deeper tree. This prevents skewed chains and guarantees that tree height remains at most $O(\log N)$.

### Complexity
Combining **Path Compression** with **Union by Rank/Size** yields an amortized time complexity of:
$$O(\alpha(N)) \text{ per operation}$$
where $\alpha(N)$ is the **Inverse Ackermann function**. For all practically conceivable inputs ($N \le 10^{600}$), $\alpha(N) \le 4$. Thus, operations are practically **$O(1)$**.

---

## 1. Canonical DSU Class Implementation

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

class DisjointSetUnion {
private:
    std::vector<int> parent_;
    std::vector<int> rank_;
    std::vector<int> size_;
    int numComponents_;

public:
    explicit DisjointSetUnion(int n) : numComponents_(n) {
        parent_.resize(n);
        std::iota(parent_.begin(), parent_.end(), 0); // parent[i] = i
        rank_.assign(n, 0);
        size_.assign(n, 1);
    }

    // Find representative with path compression: O(alpha(N))
    int find(int i) {
        if (parent_[i] == i) {
            return i;
        }
        return parent_[i] = find(parent_[i]); // Path compression
    }

    // Merge sets containing i and j using Union by Rank: O(alpha(N))
    bool uniteByRank(int i, int j) {
        int rootI = find(i);
        int rootJ = find(j);

        if (rootI == rootJ) {
            return false; // Already in the same set
        }

        // Attach tree with smaller rank to tree with larger rank
        if (rank_[rootI] < rank_[rootJ]) {
            parent_[rootI] = rootJ;
            size_[rootJ] += size_[rootI];
        } else if (rank_[rootI] > rank_[rootJ]) {
            parent_[rootJ] = rootI;
            size_[rootI] += size_[rootJ];
        } else {
            parent_[rootJ] = rootI;
            size_[rootI] += size_[rootJ];
            ++rank_[rootI];
        }

        --numComponents_;
        return true;
    }

    // Merge sets containing i and j using Union by Size: O(alpha(N))
    bool uniteBySize(int i, int j) {
        int rootI = find(i);
        int rootJ = find(j);

        if (rootI == rootJ) {
            return false;
        }

        if (size_[rootI] < size_[rootJ]) {
            std::swap(rootI, rootJ);
        }

        parent_[rootJ] = rootI;
        size_[rootI] += size_[rootJ];
        --numComponents_;
        return true;
    }

    // Check if i and j belong to the same component: O(alpha(N))
    bool connected(int i, int j) {
        return find(i) == find(j);
    }

    // Get number of distinct disjoint components: O(1)
    int countComponents() const noexcept {
        return numComponents_;
    }

    // Get size of the set containing element i: O(alpha(N))
    int getComponentSize(int i) {
        return size_[find(i)];
    }
};
```

---

## 2. Key Applications

### Application 1: Cycle Detection in Undirected Graph
An undirected graph contains a cycle if an edge connects two vertices that already share the same representative.

```cpp
bool hasCycleUndirected(int n, const std::vector<std::pair<int, int>>& edges) {
    DisjointSetUnion dsu(n);
    for (const auto& edge : edges) {
        int u = edge.first;
        int v = edge.second;
        if (!dsu.uniteByRank(u, v)) {
            return true; // Cycle detected: u and v are already connected
        }
    }
    return false;
}
```

### Application 2: Kruskal's Minimum Spanning Tree (MST)
Sort all edges in ascending order of weight. Add edges greedily to the spanning forest only if they do not create a cycle.

```cpp
struct Edge {
    int u, v, weight;
    bool operator<(const Edge& other) const {
        return weight < other.weight;
    }
};

std::pair<int, std::vector<Edge>> kruskalMST(int n, std::vector<Edge>& edges) {
    std::sort(edges.begin(), edges.end());
    DisjointSetUnion dsu(n);

    int totalWeight = 0;
    std::vector<Edge> mstEdges;

    for (const auto& edge : edges) {
        if (dsu.uniteByRank(edge.u, edge.v)) {
            totalWeight += edge.weight;
            mstEdges.push_back(edge);
            if (static_cast<int>(mstEdges.size()) == n - 1) {
                break; // Spanning tree complete
            }
        }
    }

    return {totalWeight, mstEdges};
}
```

---

## 💻 Driver & Comprehensive Verification

```cpp
#include <iostream>
#include <cassert>

int main() {
    std::cout << "========== 1. DSU BASIC OPERATIONS ==========\n";
    DisjointSetUnion dsu(5); // Elements: 0, 1, 2, 3, 4
    assert(dsu.countComponents() == 5);

    dsu.uniteByRank(0, 1);
    dsu.uniteByRank(2, 3);
    assert(dsu.connected(0, 1) == true);
    assert(dsu.connected(0, 2) == false);
    assert(dsu.countComponents() == 3);

    dsu.uniteByRank(1, 3);
    assert(dsu.connected(0, 2) == true); // 0-1-3-2 transitively connected
    assert(dsu.getComponentSize(0) == 4);
    assert(dsu.countComponents() == 2);

    std::cout << "\n========== 2. CYCLE DETECTION ==========\n";
    std::vector<std::pair<int, int>> acyclicEdges = {{0, 1}, {1, 2}, {2, 3}};
    assert(hasCycleUndirected(4, acyclicEdges) == false);

    std::vector<std::pair<int, int>> cyclicEdges = {{0, 1}, {1, 2}, {2, 0}};
    assert(hasCycleUndirected(3, cyclicEdges) == true);
    std::cout << "Cycle detection verified!\n";

    std::cout << "\n========== 3. KRUSKAL MST ==========\n";
    std::vector<Edge> graphEdges = {
        {0, 1, 10}, {0, 2, 6}, {0, 3, 5},
        {1, 3, 15}, {2, 3, 4}
    };
    auto mstResult = kruskalMST(4, graphEdges);
    int mstCost = mstResult.first;
    const auto& mstEdges = mstResult.second;
    std::cout << "MST Total Cost: " << mstCost << "\n";
    assert(mstCost == 19); // 2-3 (4), 0-3 (5), 0-1 (10)
    assert(mstEdges.size() == 3);

    std::cout << "\n✅ All DSU operations and applications verified successfully!\n";
    return 0;
}
```

---

## Next Step

- Go to [13_Segment_Tree.md](13_Segment_Tree.md) to understand the Segment Tree Data Structure.
