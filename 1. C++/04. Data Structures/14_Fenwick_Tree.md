# Fenwick Tree (Binary Indexed Tree) in C++

## 📖 Overview

A **Fenwick Tree** (also known as a **Binary Indexed Tree**, or **BIT**) is an exceptionally compact and fast data structure designed by Peter Fenwick in 1994. It efficiently calculates prefix sums and updates elements in an array in **$O(\log N)$ time** using only **$O(N)$ auxiliary space**.

Compared to a Segment Tree, a Fenwick Tree:
- Requires only $N$ space (vs. $4N$ for a Segment Tree)
- Requires only 10–15 lines of code
- Has much smaller constant factors in execution speed and cache usage

---

## ⚡ The Mathematics: Lowest Set Bit (`i & -i`)

A Fenwick Tree utilizes the two's complement binary representation of indices. 
For any integer `i`, the expression `i & (-i)` extracts the **Lowest Significant Set Bit (LSB)**:

| $i$ (Decimal) | $i$ (Binary) | $-i$ (Two's Complement) | `i & (-i)` | Range Covered $(i - \text{LSB}(i), i]$ |
|:---|:---|:---|:---|:---|
| 1 | `0001` | `1111` | `0001` (1) | $(0, 1] \rightarrow A[1]$ |
| 2 | `0010` | `1110` | `0010` (2) | $(0, 2] \rightarrow A[1] + A[2]$ |
| 3 | `0011` | `1101` | `0001` (1) | $(2, 3] \rightarrow A[3]$ |
| 4 | `0100` | `1100` | `0100` (4) | $(0, 4] \rightarrow A[1] + \dots + A[4]$ |
| 5 | `0101` | `1011` | `0001` (1) | $(4, 5] \rightarrow A[5]$ |
| 6 | `0110` | `1010` | `0010` (2) | $(4, 6] \rightarrow A[5] + A[6]$ |
| 7 | `0111` | `1001` | `0001` (1) | $(6, 7] \rightarrow A[7]$ |
| 8 | `1000` | `1000` | `1000` (8) | $(0, 8] \rightarrow A[1] + \dots + A[8]$ |

- **To compute prefix sum**: Accumulate `tree[i]` and strip the lowest set bit: `i -= i & (-i)`.
- **To update an element**: Add `delta` to `tree[i]` and add the lowest set bit: `i += i & (-i)`.

---

## 1. 1D Fenwick Tree Implementation (Point Update, Range Query)

```cpp
#include <iostream>
#include <vector>

class FenwickTree {
private:
    int n_;
    std::vector<long long> tree_;

public:
    // 1-based indexing internally
    explicit FenwickTree(int n) : n_(n), tree_(n + 1, 0) {}

    explicit FenwickTree(const std::vector<int>& arr) : n_(static_cast<int>(arr.size())), tree_(n_ + 1, 0) {
        for (int i = 0; i < n_; ++i) {
            add(i + 1, arr[i]);
        }
    }

    // Add delta to index idx (1-based): O(log N)
    void add(int idx, long long delta) {
        for (; idx <= n_; idx += idx & (-idx)) {
            tree_[idx] += delta;
        }
    }

    // Query prefix sum from 1 to idx (1-based): O(log N)
    long long queryPrefix(int idx) const {
        long long sum = 0;
        for (; idx > 0; idx -= idx & (-idx)) {
            sum += tree_[idx];
        }
        return sum;
    }

    // Query range sum [l, r] (1-based): O(log N)
    long long queryRange(int l, int r) const {
        if (l > r) return 0;
        return queryPrefix(r) - queryPrefix(l - 1);
    }
};
```

---

## 2. Range Update and Point Query (Difference Array BIT)

If the problem requires **updating an entire range $[L, R]$** and **querying single points**, we can maintain a Fenwick Tree over the **difference array** $D[i] = A[i] - A[i-1]$:
- Range update $[L, R]$ with `val`: `add(L, val)` and `add(R + 1, -val)`.
- Point query at index `k`: `queryPrefix(k)` returns the exact value of $A[k]$.

```cpp
class RangeUpdateFenwickTree {
private:
    FenwickTree bit_;

public:
    explicit RangeUpdateFenwickTree(int n) : bit_(n) {}

    // Add val to every element in range [l, r] (1-based) in O(log N)
    void updateRange(int l, int r, long long val) {
        bit_.add(l, val);
        bit_.add(r + 1, -val);
    }

    // Query value at point idx (1-based) in O(log N)
    long long queryPoint(int idx) const {
        return bit_.queryPrefix(idx);
    }
};
```

---

## 3. 2D Fenwick Tree (Matrix Range Sum Queries)

Extending the binary indexing across both row and column coordinates enables $O(\log N \log M)$ point updates and 2D subgrid sum queries.

```cpp
class FenwickTree2D {
private:
    int rows_, cols_;
    std::vector<std::vector<long long>> tree_;

public:
    FenwickTree2D(int rows, int cols)
        : rows_(rows), cols_(cols), tree_(rows + 1, std::vector<long long>(cols + 1, 0)) {}

    // Add delta at (r, c) (1-based)
    void add(int r, int c, long long delta) {
        for (int i = r; i <= rows_; i += i & (-i)) {
            for (int j = c; j <= cols_; j += j & (-j)) {
                tree_[i][j] += delta;
            }
        }
    }

    // Query 2D prefix sum of rectangle (1, 1) to (r, c)
    long long queryPrefix(int r, int c) const {
        long long sum = 0;
        for (int i = r; i > 0; i -= i & (-i)) {
            for (int j = c; j > 0; j -= j & (-j)) {
                sum += tree_[i][j];
            }
        }
        return sum;
    }

    // Query submatrix sum from (r1, c1) to (r2, c2)
    long long querySubgrid(int r1, int c1, int r2, int c2) const {
        return queryPrefix(r2, c2) 
             - queryPrefix(r1 - 1, c2) 
             - queryPrefix(r2, c1 - 1) 
             + queryPrefix(r1 - 1, c1 - 1);
    }
};
```

---

## 4. Fenwick Tree vs. Segment Tree

| Dimension | Fenwick Tree | Segment Tree |
|:---|:---|:---|
| **Auxiliary Memory** | $N$ words | $4N$ words |
| **Implementation Length** | ~15 lines | ~60–80 lines |
| **Speed / Constant Factor** | Extremely fast (cache-friendly) | Slightly slower overhead |
| **Supported Operations** | Invertible operations (Sum, XOR) | Any associative operation (Min, Max, GCD, Matrix mult) |
| **Range Updates** | Simple with difference array | Powerful with Lazy Propagation |

---

## 💻 Driver & Comprehensive Verification

```cpp
#include <iostream>
#include <cassert>

int main() {
    std::cout << "========== 1. 1D FENWICK TREE ==========\n";
    std::vector<int> arr = {2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9};
    FenwickTree ft(arr);

    // Sum from index 1 to 5: 2 + 1 + 1 + 3 + 2 = 9
    assert(ft.queryPrefix(5) == 9);
    // Range sum from 3 to 6: 1 + 3 + 2 + 3 = 9
    assert(ft.queryRange(3, 6) == 9);

    ft.add(3, 6); // Add 6 to index 3
    assert(ft.queryRange(3, 6) == 15);
    std::cout << "1D Fenwick Tree verified!\n";

    std::cout << "\n========== 2. RANGE UPDATE POINT QUERY ==========\n";
    RangeUpdateFenwickTree ruf(10);
    ruf.updateRange(2, 6, 5); // Add 5 to elements at indices [2..6]
    assert(ruf.queryPoint(1) == 0);
    assert(ruf.queryPoint(3) == 5);
    assert(ruf.queryPoint(6) == 5);
    assert(ruf.queryPoint(7) == 0);
    std::cout << "Range update point query verified!\n";

    std::cout << "\n========== 3. 2D FENWICK TREE ==========\n";
    FenwickTree2D ft2d(4, 4);
    ft2d.add(1, 1, 10);
    ft2d.add(2, 2, 20);
    ft2d.add(3, 3, 30);
    // Subgrid from (1, 1) to (2, 2) includes (1, 1)=10 and (2, 2)=20
    assert(ft2d.querySubgrid(1, 1, 2, 2) == 30);
    assert(ft2d.querySubgrid(1, 1, 4, 4) == 60);
    std::cout << "2D Fenwick Tree verified!\n";

    std::cout << "\n✅ All Fenwick Tree implementations verified successfully!\n";
    return 0;
}
```

---

## Next Step

- Go to [README.md](README.md) to continue exploring Data Structures.
