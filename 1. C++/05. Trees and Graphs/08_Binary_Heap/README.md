# Binary Heap

## 📖 Overview

A **Binary Heap** is a complete binary tree that satisfies the **heap-order property**. It is the most common and cache-friendly implementation of the **Priority Queue** abstract data type. Because a complete binary tree has no gaps (except possibly on the last level, filled from left to right), a binary heap can be stored compactly in a contiguous 1D array without any child or parent pointers.

Binary heaps are used extensively in:
- **Dijkstra's Shortest Path Algorithm** and **Prim's Minimum Spanning Tree** (using min-heaps for priority relaxation).
- **Heap Sort**: An optimal $O(N \log N)$ sorting algorithm requiring $O(1)$ auxiliary space.
- **Top-$K$ Elements / Median Finding**: Streaming algorithms for real-time order statistics.
- **Operating System Task Schedulers**: Prioritizing real-time processes against background threads.

---

## 🎯 Structural & Ordering Properties

### 1. Shape Property (Complete Binary Tree)
All levels of the tree are completely filled, except possibly the deepest level, which is filled from left to right.

### 2. Heap-Order Property
- **Min-Heap**: For every node $i$ other than the root:
  $$\text{Value}(\text{Parent}(i)) \le \text{Value}(i)$$
  The minimum element is always stored at the root.
- **Max-Heap**: For every node $i$ other than the root:
  $$\text{Value}(\text{Parent}(i)) \ge \text{Value}(i)$$
  The maximum element is always stored at the root.

```
          Min-Heap Tree View                     Array Representation (0-indexed)
                  [ 3 ]
                 /     \                          Index:   0   1   2   3   4   5
              [ 8 ]   [ 5 ]                      Value: [ 3 | 8 | 5 | 12| 15| 10]
             /    \    /
           [12]  [15][10]
```

---

## 🔢 Array Mapping Invariants (0-Based Indexing)

For an element at index $i$:
| Relationship | Index Formula | Bitwise Optimization |
| :--- | :--- | :--- |
| **Parent Index** | $\lfloor (i - 1) / 2 \rfloor$ | `(i - 1) >> 1` |
| **Left Child** | $2i + 1$ | `(i << 1) + 1` |
| **Right Child** | $2i + 2$ | `(i << 1) + 2` |
| **First Leaf Index** | $\lfloor N / 2 \rfloor$ | `n >> 1` |
| **Last Non-Leaf Index** | $\lfloor N / 2 \rfloor - 1$ | `(n >> 1) - 1` |

---

## ⚙️ Core Heap Operations

```
                   Sift-Up (Bubble-Up)                    Sift-Down (Bubble-Down)
                      Insert at End                          Extract Root
                            ↑                                     │
                 Compare with Parent                      Compare with Children
                            ↑                                     ↓
                    Swap until Valid                       Swap with Smaller/Larger
```

1. **Insert (`push`)**:
   - Append the new element to the end of the array ($O(1)$ amortized).
   - **Sift-Up (Bubble-Up)**: Compare with parent. If heap property is violated, swap with parent and repeat upwards until reaching root or a valid parent.
   - **Time Complexity**: $O(\log N)$.

2. **Extract Top (`pop`)**:
   - Copy root element to return it.
   - Replace the root with the last element in the array and decrement size.
   - **Sift-Down (Bubble-Down)**: Compare with children. Swap with the smaller child (in Min-Heap) or larger child (in Max-Heap). Repeat downwards until both children satisfy heap property or reaching a leaf.
   - **Time Complexity**: $O(\log N)$.

3. **Decrease Key (`decreaseKey`)**:
   - Update value at given index to a lower value.
   - Perform sift-up from that index.
   - **Time Complexity**: $O(\log N)$.

4. **Delete Key (`deleteKey`)**:
   - Decrease the key at index $i$ to $-\infty$ (sift-up to root).
   - Call `extractTop()`.
   - **Time Complexity**: $O(\log N)$.

---

## 📐 Mathematical Proof: Linear-Time Heap Construction ($O(N)$)

A naive approach to building a heap from an unsorted array of size $N$ is inserting elements one by one, which takes:
$$\sum_{i=1}^N O(\log i) = O(N \log N)$$

However, **Floyd's Algorithm (`buildHeap`)** constructs the heap in **$O(N)$** time by calling `siftDown` starting from the last non-leaf node down to the root:

```cpp
for (int i = (n / 2) - 1; i >= 0; i--) {
    siftDown(i);
}
```

### Proof:
- A complete binary tree with $N$ elements has height $H = \lfloor \log_2 N \rfloor$.
- At height $h$ (where leaves are at height 0, and root is at height $H$), there are at most $\lceil N / 2^{h+1} \rceil$ nodes.
- Calling `siftDown` on a node at height $h$ takes at most $O(h)$ swaps.
- The total work $S$ across all nodes is bounded by:
  $$S = \sum_{h=0}^H \left\lceil \frac{N}{2^{h+1}} \right\rceil O(h) \le O(N) \sum_{h=0}^\infty \frac{h}{2^{h+1}} = O(N) \cdot \frac{1}{2} \sum_{h=0}^\infty \frac{h}{2^h}$$

Let $A = \sum_{h=0}^\infty \frac{h}{2^h}$:
$$A = 0 + \frac{1}{2} + \frac{2}{4} + \frac{3}{8} + \frac{4}{16} + \dots$$
$$\frac{1}{2} A = 0 + \frac{1}{4} + \frac{2}{8} + \frac{3}{16} + \dots$$
Subtracting the two series:
$$A - \frac{1}{2} A = \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16} + \dots = 1$$
$$\frac{1}{2} A = 1 \implies A = 2$$

Substituting back:
$$S \le O(N) \cdot \frac{1}{2} \cdot 2 = O(N)$$

Therefore, `buildHeap` executes in strictly linear **$O(N)$** time! $\blacksquare$

---

## ⚖️ Heap vs. Binary Search Tree (BST)

| Dimension | Binary Heap | Self-Balancing BST (AVL / RBT) |
| :--- | :--- | :--- |
| **Order Property** | Partial order: Parent $\le$ Children | Full order: Left $<$ Node $<$ Right |
| **Underlying Memory** | Flat contiguous array (`std::vector`) | Pointers to individual heap allocations |
| **Cache Locality** | **Exceptional** (sequential array indices) | Poor (pointer-chasing across RAM) |
| **Find Min / Max** | **$O(1)$** | $O(\log N)$ |
| **Arbitrary Search** | $O(N)$ (must scan entire array) | **$O(\log N)$** |
| **Heap Construction** | **$O(N)$** (Floyd's algorithm) | $O(N \log N)$ |
| **In-Order Traversal** | Not sorted without sorting ($O(N \log N)$) | Sorted order in $O(N)$ |

---

## 📑 Directory Contents

- **`01_Binary_Heap.md`**: Complete production C++ implementation of `BinaryHeap<T, Compare>` providing:
  - Custom functors for Min-Heap (`std::less<T>`) and Max-Heap (`std::greater<T>`).
  - Floyd's linear-time constructor.
  - In-place Heap Sort algorithm.
  - Priority task scheduler application.
  - Comprehensive interactive test suite.
