# Find the Duplicate Number in C++ - Floyd's Cycle Detection on Array Indices

## 1. Introduction & Theoretical Foundations

The **Find the Duplicate Number** problem states:
Given an array of integers `nums` containing $N + 1$ integers where each integer is between $1$ and $N$ inclusive, prove that at least one duplicate number must exist, and find this duplicate number.

### Strict Constraints:
1. You **must not modify the array** (read-only).
2. You must use only **$O(1)$ constant extra memory**.
3. Your runtime complexity must be **$O(N)$ linear time**.

```
Input Array (N = 4, Size = 5):
Index: [ 0, 1, 2, 3, 4 ]
Value: [ 1, 3, 4, 2, 2 ]

Mapped Directed Graph:
0 ──► 1 ──► 3 ──► 2 ◄──┐
                  │    │  (Cycle between 2 and 4!)
                  ▼    │  Cycle entrance is 2 (the duplicate!)
                  4 ───┘
```

---

## 2. Theoretical Reduction: Array as a Functional Graph

Because every value $\text{nums}[i] \in [1, N]$, we can view the array as a **directed functional graph** where each index $i$ has a single directed edge pointing to node $\text{nums}[i]$:
$$i \longrightarrow \text{nums}[i]$$

### Key Mathematical Invariants:
1. **The Pigeonhole Principle**: Distributing $N + 1$ integers into $N$ distinct values ($1$ to $N$) guarantees by the Pigeonhole Principle that at least one value is duplicated.
2. **Multiple Predecessors**: If a value $D$ is duplicated, at least two distinct indices point to node $D$.
3. **Index 0 is Never Pointed To**: Because all array values are $\ge 1$, no element points to index $0$.
4. **Guaranteed Cycle Entrance**: Starting from index $0$ and walking the path $0 \to \text{nums}[0] \to \text{nums}[\text{nums}[0]] \dots$ forms a path shaped like the letter $\rho$ (rho). The entrance to the cycle is precisely the duplicate value $D$!

---

## 3. Mathematical Proof of Floyd's Tortoise and Hare

Let:
- $F$ be the distance from index $0$ to the cycle entrance.
- $C$ be the circumference (length) of the cycle.
- $a$ be the distance from the cycle entrance to the collision point of the two pointers.

```
0 ────────► [ Entrance D ] ──────► [ Collision ]
   dist = F          ▲                   │
                     └───────────────────┘
                           dist = C - a
```

1. In Phase 1:
   - `slow` travels distance: $d_{\text{slow}} = F + a$.
   - `fast` travels distance: $d_{\text{fast}} = F + n \cdot C + a$ for some integer $n \ge 1$.
   - Because `fast` moves at twice the speed of `slow`:
$$2 \cdot d_{\text{slow}} = d_{\text{fast}} \implies 2(F + a) = F + n \cdot C + a$$
$$F + a = n \cdot C \implies F = n \cdot C - a = (n - 1)C + (C - a)$$

2. In Phase 2:
   - Reset `slow = 0` while keeping `fast` at the collision point.
   - Advance both pointers **one step at a time**.
   - After `slow` travels distance $F$, it reaches the cycle entrance $D$.
   - Simultaneously, `fast` travels distance $(n - 1)C + (C - a)$ from the collision point, which lands `fast` **at the exact same cycle entrance $D$**!

---

## 4. Production-Grade C++ Implementation

```cpp
#include <iostream>
#include <vector>

class DuplicateFinder {
public:
    // O(N) Time, O(1) Auxiliary Space, Read-Only Array
    static int findDuplicate(const std::vector<int>& nums) {
        if (nums.size() <= 1) return -1;

        // Phase 1: Detect intersection within the cycle
        int slow = nums[0];
        int fast = nums[0];

        do {
            slow = nums[slow];           // 1 step
            fast = nums[nums[fast]];     // 2 steps
        } while (slow != fast);

        // Phase 2: Locate the entrance to the cycle
        slow = nums[0]; // Reset slow to start
        while (slow != fast) {
            slow = nums[slow]; // 1 step
            fast = nums[fast]; // 1 step
        }

        return slow; // The cycle entrance is the duplicate element
    }
};
```

---

## 5. Complete Runnable Verification Suite

```cpp
#include <iostream>
#include <vector>

int main() {
    std::cout << "=====================================================" << std::endl;
    std::cout << "       FIND THE DUPLICATE NUMBER ALGORITHMIC SUITE   " << std::endl;
    std::cout << "=====================================================" << std::endl;

    // --- 1. Standard Case with Duplicate 2 ---
    std::cout << "\n[1] STANDARD ARRAY {1, 3, 4, 2, 2}:" << std::endl;
    std::vector<int> nums1 = {1, 3, 4, 2, 2};
    int dup1 = DuplicateFinder::findDuplicate(nums1);
    std::cout << "  Found Duplicate: " << dup1 << " (Expected: 2)" << std::endl;

    // --- 2. Multiple Duplicates of the Same Number ---
    std::cout << "\n[2] MULTIPLE COPIES OF SAME VALUE {3, 1, 3, 4, 2}:" << std::endl;
    std::vector<int> nums2 = {3, 1, 3, 4, 2};
    int dup2 = DuplicateFinder::findDuplicate(nums2);
    std::cout << "  Found Duplicate: " << dup2 << " (Expected: 3)" << std::endl;

    // --- 3. Duplicate Appears Three Times ---
    std::cout << "\n[3] TRIPLE OCCURRENCE {2, 2, 2, 2, 2}:" << std::endl;
    std::vector<int> nums3 = {2, 2, 2, 2, 2};
    int dup3 = DuplicateFinder::findDuplicate(nums3);
    std::cout << "  Found Duplicate: " << dup3 << " (Expected: 2)" << std::endl;

    std::cout << "\n=====================================================" << std::endl;
    return 0;
}
```

---

## 6. Complexity Analysis Table

| Method | Time Complexity | Auxiliary Space | Modifies Input? | Meets Constraints? |
| :--- | :--- | :--- | :--- | :--- |
| **Sorting** | $O(N \log N)$ | $O(1)$ or $O(N)$ | Yes | No (Modifies array) |
| **Hash Set** | $O(N)$ | $O(N)$ | No | No (Exceeds $O(1)$ space) |
| **Index Negation** | $O(N)$ | $O(1)$ | Yes | No (Modifies array) |
| **Binary Search on Values** | $O(N \log N)$ | $O(1)$ | No | Yes, but sub-optimal |
| **Floyd's Tortoise & Hare** | $O(N)$ | $O(1)$ | No | **Yes (Optimal)** |

---

## 7. Common Pitfalls & Interview Traps

1. **Array Modification via Negation**: Marking visited elements by negating `nums[abs(nums[i])]` is a common interview approach, but it **violates the read-only constraint** of concurrent or immutable data streams.
2. **Incorrect Phase 2 Reset**: In Phase 2, resetting `slow = 0` instead of `slow = nums[0]` causes an off-by-one pointer alignment because Phase 1 started at `nums[0]`.
3. **Out-of-Bounds Assumption**: Floyd's algorithm works only because values are guaranteed to be in $[1, N]$. If values could be $0$ or larger than $N$, index dereferencing would throw segmentation faults.

---

## Next Step

- Proceed to [README.md](README.md) for the complete Array Problems overview.
