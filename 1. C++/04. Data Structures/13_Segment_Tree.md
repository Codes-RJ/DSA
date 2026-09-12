# Segment Tree in C++

## 📖 Overview

A **Segment Tree** is a versatile binary tree data structure used for storing information about intervals or segments of an array. It allows answering **range queries** (such as range sum, minimum, maximum, GCD) and performing **updates** in logarithmic time:

| Operation | Naive Array | Prefix Sum Array | Segment Tree |
|:---|:---|:---|:---|
| **Build Tree** | $O(N)$ | $O(N)$ | $O(N)$ |
| **Point Update** | $O(1)$ | $O(N)$ | $O(\log N)$ |
| **Range Query ($[L, R]$)** | $O(N)$ | $O(1)$ | $O(\log N)$ |
| **Range Update ($[L, R]$)** | $O(N)$ | $O(N)$ | $O(\log N)$ *(with Lazy Propagation)* |

---

## 🌲 Tree Structure & Array Representation

A Segment Tree for an array of size $N$ is represented using an array of size $4N$.
For a node at index $v$:
- Left child: $2v + 1$ (or $2v$ for 1-based indexing)
- Right child: $2v + 2$ (or $2v + 1$ for 1-based indexing)
- Leaves represent individual array elements $A[i]$.
- Internal nodes represent merged intervals.

```
                  [0...3] (Sum = 16)
                  /                \
          [0...1] (Sum = 4)      [2...3] (Sum = 12)
          /             \         /             \
      [0] (1)         [1] (3)   [2] (5)         [3] (7)
```

---

## 1. Segment Tree with Point Updates & Range Sum Queries

```cpp
#include <iostream>
#include <vector>

class SegmentTree {
private:
    int n_;
    std::vector<long long> tree_;

    void build(const std::vector<int>& arr, int node, int start, int end) {
        if (start == end) {
            tree_[node] = arr[start];
            return;
        }
        int mid = start + (end - start) / 2;
        build(arr, 2 * node + 1, start, mid);
        build(arr, 2 * node + 2, mid + 1, end);
        tree_[node] = tree_[2 * node + 1] + tree_[2 * node + 2];
    }

    void updatePoint(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree_[node] = val;
            return;
        }
        int mid = start + (end - start) / 2;
        if (idx <= mid) {
            updatePoint(2 * node + 1, start, mid, idx, val);
        } else {
            updatePoint(2 * node + 2, mid + 1, end, idx, val);
        }
        tree_[node] = tree_[2 * node + 1] + tree_[2 * node + 2];
    }

    long long queryRange(int node, int start, int end, int l, int r) const {
        // Range completely outside [start, end]
        if (r < start || end < l) {
            return 0;
        }
        // Range completely inside [start, end]
        if (l <= start && end <= r) {
            return tree_[node];
        }
        // Partial overlap
        int mid = start + (end - start) / 2;
        long long leftSum = queryRange(2 * node + 1, start, mid, l, r);
        long long rightSum = queryRange(2 * node + 2, mid + 1, end, l, r);
        return leftSum + rightSum;
    }

public:
    explicit SegmentTree(const std::vector<int>& arr) : n_(static_cast<int>(arr.size())) {
        tree_.assign(4 * n_, 0);
        if (n_ > 0) {
            build(arr, 0, 0, n_ - 1);
        }
    }

    // Point update: set arr[idx] = val in O(log N)
    void update(int idx, int val) {
        updatePoint(0, 0, n_ - 1, idx, val);
    }

    // Range sum query: sum of arr[l ... r] in O(log N)
    long long query(int l, int r) const {
        return queryRange(0, 0, n_ - 1, l, r);
    }
};
```

---

## 2. Lazy Propagation (Range Updates in $O(\log N)$)

### The Problem
Updating a range $[L, R]$ naively by calling point update for each element takes $O(M \log N)$, degrading to $O(N \log N)$.

### Key Insight
When an update covers an entire segment $[start, end]$ handled by node $v$, update $v$'s aggregate value immediately, record the pending update in a **`lazy`** array, and **do not update its children yet**. Postpone (defer) propagating the update to children until an operation actually visits those children.

```cpp
class LazySegmentTree {
private:
    int n_;
    std::vector<long long> tree_;
    std::vector<long long> lazy_;

    void build(const std::vector<int>& arr, int node, int start, int end) {
        if (start == end) {
            tree_[node] = arr[start];
            return;
        }
        int mid = start + (end - start) / 2;
        build(arr, 2 * node + 1, start, mid);
        build(arr, 2 * node + 2, mid + 1, end);
        tree_[node] = tree_[2 * node + 1] + tree_[2 * node + 2];
    }

    // Push pending lazy updates down to children
    void pushDown(int node, int start, int end) {
        if (lazy_[node] != 0) {
            int mid = start + (end - start) / 2;

            // Apply to left child
            tree_[2 * node + 1] += (mid - start + 1) * lazy_[node];
            lazy_[2 * node + 1] += lazy_[node];

            // Apply to right child
            tree_[2 * node + 2] += (end - mid) * lazy_[node];
            lazy_[2 * node + 2] += lazy_[node];

            lazy_[node] = 0; // Clear parent's lazy tag
        }
    }

    void updateRangeInternal(int node, int start, int end, int l, int r, long long val) {
        if (r < start || end < l) return; // Outside

        if (l <= start && end <= r) {
            // Segment fully inside update range
            tree_[node] += (end - start + 1) * val;
            lazy_[node] += val;
            return;
        }

        pushDown(node, start, end);
        int mid = start + (end - start) / 2;
        updateRangeInternal(2 * node + 1, start, mid, l, r, val);
        updateRangeInternal(2 * node + 2, mid + 1, end, l, r, val);
        tree_[node] = tree_[2 * node + 1] + tree_[2 * node + 2];
    }

    long long queryRangeInternal(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return 0;

        if (l <= start && end <= r) {
            return tree_[node];
        }

        pushDown(node, start, end);
        int mid = start + (end - start) / 2;
        return queryRangeInternal(2 * node + 1, start, mid, l, r) +
               queryRangeInternal(2 * node + 2, mid + 1, end, l, r);
    }

public:
    explicit LazySegmentTree(const std::vector<int>& arr) : n_(static_cast<int>(arr.size())) {
        tree_.assign(4 * n_, 0);
        lazy_.assign(4 * n_, 0);
        if (n_ > 0) {
            build(arr, 0, 0, n_ - 1);
        }
    }

    // Add val to every element in arr[l ... r] in O(log N)
    void updateRange(int l, int r, long long val) {
        updateRangeInternal(0, 0, n_ - 1, l, r, val);
    }

    // Query sum of arr[l ... r] in O(log N)
    long long query(int l, int r) {
        return queryRangeInternal(0, 0, n_ - 1, l, r);
    }
};
```

---

## 💻 Driver & Comprehensive Verification

```cpp
#include <iostream>
#include <cassert>

int main() {
    std::vector<int> arr = {1, 3, 5, 7, 9, 11};
    // Indices:             0  1  2  3  4   5

    std::cout << "========== 1. BASIC SEGMENT TREE ==========\n";
    SegmentTree st(arr);
    assert(st.query(1, 3) == (3 + 5 + 7)); // 15
    assert(st.query(0, 5) == 36);

    st.update(1, 10); // arr[1] = 10 -> arr = {1, 10, 5, 7, 9, 11}
    assert(st.query(1, 3) == (10 + 5 + 7)); // 22
    assert(st.query(0, 5) == 43);
    std::cout << "Point update and range queries verified!\n";

    std::cout << "\n========== 2. LAZY PROPAGATION ==========\n";
    LazySegmentTree lst(arr);
    // Add 10 to range [1, 4] -> arr = {1, 13, 15, 17, 19, 11}
    lst.updateRange(1, 4, 10);

    assert(lst.query(1, 4) == (13 + 15 + 17 + 19)); // 64
    assert(lst.query(0, 1) == (1 + 13));             // 14
    assert(lst.query(0, 5) == (36 + 4 * 10));        // 76
    std::cout << "Lazy propagation range updates verified!\n";

    std::cout << "\n✅ All Segment Tree operations verified successfully!\n";
    return 0;
}
```

---

## Next Step

- Go to [14_Fenwick_Tree.md](14_Fenwick_Tree.md) to understand the Fenwick Tree (Binary Indexed Tree).
