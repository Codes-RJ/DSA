# Minimum Cost to Connect Sticks: Greedy Huffman Merge Trees & Dual-Queue Optimization

## 1. Executive Overview & Theoretical Foundations

The **Minimum Cost to Connect Sticks** (also known as the *Optimal Merge Pattern* or *Rope Splicing Problem*) is a classical greedy optimization challenge:
Given $N$ sticks of arbitrary lengths, any two sticks of lengths $x$ and $y$ can be connected into a single stick of length $(x + y)$ at an incurred computational or physical cost equal to $(x + y)$. This process is repeated until exactly one contiguous stick remains. The objective is to determine the minimum cumulative cost required to merge all $N$ sticks.

### Mathematical Formulation
When sticks are merged, the process forms a **strictly binary merge tree** where:
- Each initial stick length $L_i$ corresponds to a leaf node in the tree.
- The depth of leaf $i$ in the merge tree is denoted by $d_i$ (number of merges stick $i$ participates in).
- The total cumulative merge cost is mathematically identical to the weighted external path length:
  $$\text{Total Cost} = \sum_{i=1}^{N} L_i \cdot d_i$$

```
                          CUMULATIVE MERGE TREE
                              [ Total Cost ]
                                 (Cost: 29)
                                   /    \
                                [6]     (15)  <── Cost: 15
                                       /    \
                                     [4]    (9)  <── Cost: 9
                                           /   \
                                         [2]   [3] <── Cost: 5

           Total Incurred Cost = 5 + 9 + 15 = 29
           Leaf-depth formula: 2*(3) + 3*(3) + 4*(2) + 6*(1) = 6 + 9 + 8 + 6 = 29
```

---

## 2. Formal Exchange Argument Proof of Optimality

**Theorem**: An optimal stick merge sequence always pairs the two globally smallest available stick lengths first.

*Proof by Contradiction (Exchange Argument)*:
1. Suppose an optimal merge tree $T^*$ exists where the two smallest elements $x$ and $y$ are not placed as siblings at the maximum depth of the tree.
2. Let $a$ and $b$ be two sibling leaves at the maximum depth $d_{max}$ in $T^*$, with $a \ge x$ and $b \ge y$.
3. Since $d_{max} \ge d_x$ and $d_{max} \ge d_y$, swapping $x$ with $a$ and $y$ with $b$ modifies the total cost by:
   $$\Delta \text{Cost} = (x \cdot d_{max} + a \cdot d_x) - (x \cdot d_x + a \cdot d_{max}) = (x - a)(d_{max} - d_x)$$
4. Because $x \le a$ and $d_{max} \ge d_x$, both $(x - a) \le 0$ and $(d_{max} - d_x) \ge 0$.
5. Therefore, $\Delta \text{Cost} \le 0$. The swap cannot increase the total cost.
6. Performing this exchange yields an alternative tree $T'$ whose cost is less than or equal to $T^*$, with $x$ and $y$ as deepest siblings. Repeating this inductively proves the greedy choice property. $\blacksquare$

---

## 3. Production-Grade C++ Implementation Suite

This implementation provides both the standard **Min-Heap ($O(N \log N)$)** method and the advanced **Dual-Queue Linear-Time ($O(N)$)** method:

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cassert>
#include <climits>

class StickConnector {
public:
    // -------------------------------------------------------------------------
    // Method 1: Classical Min-Heap (Priority Queue)
    // Time Complexity:  O(N log N)
    // Auxiliary Space:  O(N) heap elements
    // -------------------------------------------------------------------------
    static long long connectSticksMinHeap(std::vector<int> sticks) {
        if (sticks.size() <= 1) return 0;

        std::priority_queue<long long, std::vector<long long>, std::greater<long long>> minHeap;
        for (int len : sticks) {
            minHeap.push(len);
        }

        long long totalCost = 0;
        while (minHeap.size() > 1) {
            long long stick1 = minHeap.top();
            minHeap.pop();
            long long stick2 = minHeap.top();
            minHeap.pop();

            long long mergedStick = stick1 + stick2;
            totalCost += mergedStick;
            minHeap.push(mergedStick);
        }
        return totalCost;
    }

    // -------------------------------------------------------------------------
    // Method 2: Dual-Queue Linear Time Algorithm (Huffman's Two-Queue Technique)
    // Invariant: If initial sticks are sorted, merged sums are strictly non-decreasing!
    // Time Complexity:  O(N log N) to sort, or O(N) if already presorted!
    // Auxiliary Space:  O(N) for the merged queue
    // -------------------------------------------------------------------------
    static long long connectSticksDualQueue(std::vector<int> sticks) {
        if (sticks.size() <= 1) return 0;

        std::sort(sticks.begin(), sticks.end());

        std::queue<long long> q1; // Stores original sorted sticks
        std::queue<long long> q2; // Stores newly merged sticks (automatically sorted)

        for (int s : sticks) {
            q1.push(s);
        }

        // Helper lambda to extract the minimum of the two queue heads
        auto extractMin = [&]() -> long long {
            if (q1.empty()) {
                long long val = q2.front();
                q2.pop();
                return val;
            }
            if (q2.empty()) {
                long long val = q1.front();
                q1.pop();
                return val;
            }
            if (q1.front() <= q2.front()) {
                long long val = q1.front();
                q1.pop();
                return val;
            } else {
                long long val = q2.front();
                q2.pop();
                return val;
            }
        };

        long long totalCost = 0;
        int mergesNeeded = sticks.size() - 1;

        for (int i = 0; i < mergesNeeded; ++i) {
            long long stick1 = extractMin();
            long long stick2 = extractMin();

            long long merged = stick1 + stick2;
            totalCost += merged;
            q2.push(merged);
        }
        return totalCost;
    }

    // -------------------------------------------------------------------------
    // Method 3: K-Way Stick Connecting (K-Ary Huffman Merge Tree)
    // Merges K sticks simultaneously at each step
    // -------------------------------------------------------------------------
    static long long connectSticksKWay(std::vector<int> sticks, int k) {
        if (sticks.size() <= 1 || k <= 1) return 0;

        std::priority_queue<long long, std::vector<long long>, std::greater<long long>> minHeap;
        for (int s : sticks) {
            minHeap.push(s);
        }

        // Dummy zero-length sticks to ensure the last merge has exactly K items:
        // (N - 1) % (K - 1) != 0 means the root would have fewer than K branches
        while ((minHeap.size() - 1) % (k - 1) != 0) {
            minHeap.push(0);
        }

        long long totalCost = 0;
        while (minHeap.size() > 1) {
            long long merged = 0;
            for (int i = 0; i < k && !minHeap.empty(); ++i) {
                merged += minHeap.top();
                minHeap.pop();
            }
            totalCost += merged;
            minHeap.push(merged);
        }
        return totalCost;
    }
};

int main() {
    std::cout << "==============================================================\n";
    std::cout << "        MINIMUM COST TO CONNECT STICKS TEST SUITE             \n";
    std::cout << "==============================================================\n";

    // Test Case 1: Standard example [2, 4, 3, 6]
    // 2 + 3 = 5 (Cost: 5)   -> remaining [4, 5, 6]
    // 4 + 5 = 9 (Cost: 14)  -> remaining [6, 9]
    // 6 + 9 = 15 (Cost: 29) -> total: 29
    std::vector<int> sticks1 = {2, 4, 3, 6};
    long long cost1_heap = StickConnector::connectSticksMinHeap(sticks1);
    long long cost1_dual = StickConnector::connectSticksDualQueue(sticks1);
    assert(cost1_heap == 29);
    assert(cost1_dual == 29);
    std::cout << ">> Test Case 1 [2, 4, 3, 6]: Passed (Cost = 29)\n";

    // Test Case 2: Already sorted array [1, 8, 35]
    // 1 + 8 = 9 (Cost: 9)  -> remaining [9, 35]
    // 9 + 35 = 44 (Cost: 53)
    std::vector<int> sticks2 = {1, 8, 35};
    assert(StickConnector::connectSticksMinHeap(sticks2) == 53);
    assert(StickConnector::connectSticksDualQueue(sticks2) == 53);
    std::cout << ">> Test Case 2 [1, 8, 35]: Passed (Cost = 53)\n";

    // Test Case 3: All identical sticks [5, 5, 5, 5]
    // (5+5) = 10, (5+5) = 10, (10+10) = 20 -> Cost: 10 + 10 + 20 = 40
    std::vector<int> sticks3 = {5, 5, 5, 5};
    assert(StickConnector::connectSticksMinHeap(sticks3) == 40);
    assert(StickConnector::connectSticksDualQueue(sticks3) == 40);
    std::cout << ">> Test Case 3 [5, 5, 5, 5]: Passed (Cost = 40)\n";

    // Test Case 4: K-Way merge with K = 3 on [2, 4, 3, 6, 1]
    // Sticks = 5. (5-1) % (3-1) = 4 % 2 = 0 (perfect fit)
    // 1 + 2 + 3 = 6 (Cost: 6) -> sticks become [4, 6, 6]
    // 4 + 6 + 6 = 16 (Cost: 6 + 16 = 22)
    std::vector<int> sticks4 = {2, 4, 3, 6, 1};
    long long costKWay = StickConnector::connectSticksKWay(sticks4, 3);
    assert(costKWay == 22);
    std::cout << ">> Test Case 4 (3-Way Merge): Passed (Cost = 22)\n";

    std::cout << "\n=== All Stick Connecting Tests Successfully Verified! ===\n";
    return 0;
}
```

---

## 4. Algorithmic Complexity Comparison

| Method | Best Time | Average Time | Worst Time | Auxiliary Space | Precondition |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Min-Heap (Priority Queue)** | $O(N \log N)$ | $O(N \log N)$ | $O(N \log N)$ | $O(N)$ | Unordered sticks |
| **Dual-Queue (Huffman 2-Q)** | $O(N)$ | $O(N)$ | $O(N)$ | $O(N)$ | Presorted input |
| **Dual-Queue (with Sort)** | $O(N \log N)$ | $O(N \log N)$ | $O(N \log N)$ | $O(N)$ | Unordered sticks |
| **$K$-Way Merge Heap** | $O(N \log_K N)$ | $O(N \log_K N)$ | $O(N \log_K N)$ | $O(N)$ | Unordered sticks |

---

## 5. Key Invariants & Competitive Programming Pitfalls

1. **Integer Overflow on Sum Accumulation**:
   - For $N = 10^5$ sticks with lengths up to $10^4$, the cumulative merge cost easily exceeds $2^{31} - 1$ ($2 \times 10^9$).
   - Always use 64-bit `long long` for both the accumulator variable and the intermediate merge sums.
2. **Boundary Condition ($N \le 1$)**:
   - If $N = 0$ or $N = 1$, zero merges occur, so the total cost is strictly `0`.
3. **$K$-Ary Huffman Padding Invariant**:
   - For $K$-way merges, if $(N - 1) \not\equiv 0 \pmod{K - 1}$, dummy nodes with weight `0` must be prepended so the tree remains full at all internal nodes.

---

## Next Step

- Proceed to [14_Gas_Station_Problem.md](14_Gas_Station_Problem.md) to explore cyclic greedy invariant tracking and running balance proofs.
