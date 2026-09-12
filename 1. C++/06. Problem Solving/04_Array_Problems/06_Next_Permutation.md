# Next Permutation in C++ - Lexicographical Inversion and Suffix Reversal

## 1. Introduction & Theoretical Foundations

A **permutation** of an array of integers is an arrangement of its elements into a sequence. The **lexicographical order** is the dictionary order based on the numerical value of elements.

The **Next Permutation** problem requires rearranging numbers into the lexicographically next greater permutation of numbers. If no such greater permutation is possible (the array is sorted in descending order), it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
The operation must be performed **in-place** using only **$O(1)$ constant extra memory** in **$O(N)$ linear time**.

```
Example Sequence:
[1, 2, 3]  ──►  [1, 3, 2]  ──►  [2, 1, 3]  ──►  [2, 3, 1]  ──►  [3, 1, 2]  ──►  [3, 2, 1]
                                                                                   │
                                                     Wraps around to:  ◄───────────┘
                                                       [1, 2, 3]
```

---

## 2. Mathematical 3-Step Invariant Algorithm

To transform a sequence to its immediate lexicographical successor, we must modify the array as far to the right as possible (retaining the longest common prefix):

```
Array: [ 1, 5, 8, 4, 7, 6, 5, 3, 1 ]
                      ▲  ─────────
                   pivot   decreasing suffix
```

### Step 1: Find the First Decreasing Element from the Right
Scan from right to left to find the first index $i$ such that:
$$\text{nums}[i] < \text{nums}[i + 1]$$
- The suffix to the right of $i$ ($\text{nums}[i + 1 \dots N - 1]$) is strictly in non-increasing order. No permutation of this suffix alone can produce a larger value.
- If no such $i$ exists (the entire array is monotonically decreasing), reverse the entire array to form the smallest permutation and terminate.

### Step 2: Find the Successor of $\text{nums}[i]$ in the Suffix
Scan from right to left to find the first element $\text{nums}[j]$ such that:
$$\text{nums}[j] > \text{nums}[i]$$
Swap $\text{nums}[i]$ and $\text{nums}[j]$.
- Since the suffix was sorted in descending order, $\text{nums}[j]$ is the smallest element in the suffix strictly greater than $\text{nums}[i]$.
- Swapping maintains the descending order of the suffix!

### Step 3: Reverse the Suffix
Reverse the suffix $\text{nums}[i + 1 \dots N - 1]$.
- Reversing a descending suffix converts it into an ascending suffix, minimizing its numerical value and guaranteeing that the new sequence is the **immediate next** permutation.

---

## 3. Production-Grade C++ Implementation

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

class PermutationUtils {
public:
    // Replicates std::next_permutation in O(N) time and O(1) space
    static bool nextPermutation(std::vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return false;

        // Step 1: Find largest index i such that nums[i] < nums[i + 1]
        int i = n - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }

        // If a valid pivot was found
        if (i >= 0) {
            // Step 2: Find largest index j such that nums[j] > nums[i]
            int j = n - 1;
            while (nums[j] <= nums[i]) {
                j--;
            }
            // Swap pivot with its successor
            std::swap(nums[i], nums[j]);
        }

        // Step 3: Reverse suffix starting at i + 1
        std::reverse(nums.begin() + i + 1, nums.end());

        // Returns false if wrapped around from last to first permutation
        return (i >= 0);
    }

    // Previous Permutation: The exact inverse transformation
    static bool prevPermutation(std::vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return false;

        int i = n - 2;
        while (i >= 0 && nums[i] <= nums[i + 1]) {
            i--;
        }

        if (i >= 0) {
            int j = n - 1;
            while (nums[j] >= nums[i]) {
                j--;
            }
            std::swap(nums[i], nums[j]);
        }

        std::reverse(nums.begin() + i + 1, nums.end());
        return (i >= 0);
    }
};
```

---

## 4. Complete Runnable Verification Suite

```cpp
#include <iostream>
#include <vector>

int main() {
    std::cout << "=====================================================" << std::endl;
    std::cout << "          NEXT PERMUTATION ALGORITHMIC SUITE         " << std::endl;
    std::cout << "=====================================================" << std::endl;

    // --- 1. Standard Step-by-Step Evolution ---
    std::cout << "\n[1] GENERATING ALL PERMUTATIONS OF {1, 2, 3}:" << std::endl;
    std::vector<int> seq = {1, 2, 3};
    int count = 1;
    do {
        std::cout << "  Permutation " << count++ << ": [ ";
        for (int v : seq) std::cout << v << " ";
        std::cout << "]" << std::endl;
    } while (PermutationUtils::nextPermutation(seq));

    // --- 2. Boundary Test: Last Permutation Wrap-Around ---
    std::cout << "\n[2] WRAP-AROUND OF DESCENDING ARRAY {3, 2, 1}:" << std::endl;
    std::vector<int> lastPerm = {3, 2, 1};
    bool hasNext = PermutationUtils::nextPermutation(lastPerm);
    std::cout << "  Input: [ 3, 2, 1 ] ──► Next: [ ";
    for (int v : lastPerm) std::cout << v << " ";
    std::cout << "] (Has next: " << (hasNext ? "true" : "false (wrapped)") << ")" << std::endl;

    // --- 3. Duplicate Handling ---
    std::cout << "\n[3] DUPLICATE ELEMENTS TEST {1, 1, 5}:" << std::endl;
    std::vector<int> dups = {1, 1, 5};
    PermutationUtils::nextPermutation(dups);
    std::cout << "  Input: [ 1, 1, 5 ] ──► Next: [ ";
    for (int v : dups) std::cout << v << " ";
    std::cout << "] (Expected: [ 1, 5, 1 ])" << std::endl;

    std::cout << "\n=====================================================" << std::endl;
    return 0;
}
```

---

## 5. Complexity Analysis Table

| Operation | Best Case Time | Average Case Time | Worst Case Time | Space Complexity |
| :--- | :--- | :--- | :--- | :--- |
| **Pivot Search** | $O(1)$ | $O(N)$ | $O(N)$ | $O(1)$ |
| **Successor Search** | $O(1)$ | $O(N)$ | $O(N)$ | $O(1)$ |
| **Suffix Reversal** | $O(1)$ | $O(N)$ | $O(N)$ | $O(1)$ |
| **Total `nextPermutation`** | $O(1)$ | $O(N)$ | $O(N)$ | $O(1)$ |

---

## 6. Common Pitfalls & Interview Traps

1. **Strict vs. Non-Strict Inequality in Pivot Scan**: Using `nums[i] > nums[i + 1]` instead of `nums[i] >= nums[i + 1]` fails on duplicate elements (e.g., `[1, 5, 1]` or `[2, 2, 1]`). Duplicates must be skipped.
2. **Successor Search Equality**: The successor must be strictly greater than the pivot: `nums[j] <= nums[i]` must continue scanning.
3. **Double Reversal Fallacy**: Attempting to sort the suffix with `std::sort` ($O(N \log N)$) instead of simple linear two-pointer reversal ($O(N)$). Because the suffix is guaranteed to be in descending order, reversing it in-place is strictly linear.

---

## Next Step

- Proceed to [07_Merge_Intervals.md](07_Merge_Intervals.md) to master range scheduling and interval intersection algorithms in C++.
