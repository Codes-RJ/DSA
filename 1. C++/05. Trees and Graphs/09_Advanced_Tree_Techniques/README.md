# Advanced Tree Techniques

## 📖 Overview

Trees are hierarchical, acyclic connected graphs. While basic tree algorithms (such as DFS, BFS, and tree traversals) operate in $O(N)$ time per query, advanced competitive programming and large-scale graph databases require answering dynamic queries—such as finding the **Lowest Common Ancestor (LCA)**, computing path aggregates, or updating entire subtrees—in **$O(\log N)$** or **$O(1)$** time after offline precomputation.

This module covers two foundational advanced tree techniques:
1. **Binary Lifting & LCA**: Dynamic programming over powers of two to answer $k$-th ancestor queries, lowest common ancestors, and path aggregates in $O(\log N)$ time per query.
2. **Euler Tour Technique & Tree Flattening**: Mapping hierarchical subtrees into contiguous 1D array ranges using DFS entry and exit timestamps, enabling standard 1D range query data structures (Segment Trees, Fenwick Trees) to answer dynamic subtree updates and queries in $O(\log N)$ time.

---

## 🗺️ Algorithmic Comparison Matrix

| Technique | Preprocessing Time | Preprocessing Space | Query Types Supported | Query Time |
| :--- | :--- | :--- | :--- | :--- |
| **Naive DFS / BFS** | $O(1)$ | $O(N)$ recursion | Single path traversal, subtree sum | $O(N)$ per query |
| **Binary Lifting** | $O(N \log N)$ | $O(N \log N)$ | $k$-th Ancestor, LCA, Path Max/Min/Sum, Tree Distance | **$O(\log N)$** |
| **Euler Tour + Segment Tree** | $O(N)$ | $O(N)$ | Subtree Sum, Subtree Range Update, Ancestor Testing | **$O(\log N)$** (Queries), **$O(1)$** (Ancestor check) |
| **Tarjan's Offline LCA** | $O(N \cdot \alpha(N) + Q)$ | $O(N + Q)$ | Batch LCA queries offline via Disjoint Set Union | **$O(1)$** amortized per query |
| **Heavy-Light Decomposition (HLD)** | $O(N)$ | $O(N)$ | Arbitrary Path Updates & Path Range Queries | **$O(\log^2 N)$** |

---

## 🎯 Topic Roadmap

```
                          ┌──────────────────────────┐
                          │ Advanced Tree Techniques │
                          └────────────┬─────────────┘
                                       │
            ┌──────────────────────────┴──────────────────────────┐
            │                                                     │
   ┌────────┴─────────┐                                  ┌────────┴─────────┐
   │  Binary Lifting  │                                  │    Euler Tour    │
   │      & LCA       │                                  │ Tree Flattening  │
   └────────┬─────────┘                                  └────────┬─────────┘
            │                                                     │
   ├── Powers of 2 Table [u][2^k]                        ├── Entry / Exit Timestamps (tin/tout)
   ├── k-th Ancestor in O(log N)                         ├── Subtree -> Contiguous 1D Range
   ├── LCA in O(log N)                                   ├── O(1) Ancestor Inclusion Check
   ├── Path Min / Max Aggregation                        └── Segment Tree Subtree Range Queries
   └── Tree Path Distance Formula
```

---

## 📑 Directory Contents

- **`01_Binary_Lifting_and_LCA.md`**:
  - Theory of sparse tables on trees (`up[u][k]` DP state).
  - Depth-equalization and synchronized logarithmic jumping.
  - Path weight aggregation (maximum edge weight between any two nodes).
  - Distance formula: $\text{dist}(u, v) = \text{depth}[u] + \text{depth}[v] - 2 \cdot \text{depth}[\text{LCA}(u, v)]$.
  - Complete, production C++ class `TreeLCA` with interactive test harness.

- **`02_Euler_Tour_Tree_Flattening.md`**:
  - Theory of Euler Tour flattening with DFS discovery (`tin`) and finish (`tout`) timestamps.
  - Theorem: Subtree containment maps 1-to-1 with interval $[tin[u], tout[u]]$.
  - $O(1)$ Ancestry query rule: $u$ is ancestor of $v \iff tin[u] \le tin[v] \text{ and } tout[u] \ge tout[v]$.
  - Complete integration of Euler Tour with a 1D Segment Tree to solve dynamic subtree point-updates and range-sum queries in $O(\log N)$.
