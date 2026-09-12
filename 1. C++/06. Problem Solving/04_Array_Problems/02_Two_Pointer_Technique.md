# Two-Pointer Technique in C++ - Masterclass in Multi-Pointer Navigation

## 📖 Overview

The **Two-Pointer Technique** is one of the most versatile algorithmic paradigms in computer science. By coordinating two or more pointers across contiguous sequences (arrays, strings, or linked lists), we can eliminate nested iterative loops, reducing time complexities from brute-force **$O(N^2)$** down to **$O(N)$** or **$O(N \log N)$** with **$O(1)$ auxiliary memory**.

---

## 🎯 The Four Foundational Two-Pointer Archetypes

```
  Archetype 1: Convergent (Opposite Ends)     Archetype 2: Fast & Slow (Same Direction)
       left ───>             <─── right            slow ──>  fast ──────>
      [  1,   2,   4,   7,  11,  15  ]            [  0,   0,   1,   1,   2,   3  ]

  Archetype 3: Dual Sequence (Two Arrays)      Archetype 4: 3-Way Partitioning (Dutch Flag)
       p1 ───>                                     low ──>  mid ──>          <── high
      [  2,   5,   8,  12  ]                      [  0,   0,   1,   1,   2,   2  ]
       p2 ───>
      [  1,   3,   7,  10  ]
```

### 1. Convergent Pointers (Opposite Ends Inward)
- Pointers start at indices `0` and `N - 1` and move toward each other.
- Requires monotonicity (typically sorted input).
- **Canonical Use Cases**: 2-Sum, 3-Sum, Container With Most Water, Palindrome verification, Trapping Rain Water.

### 2. Fast & Slow Pointers (Same Direction, Staggered Speed)
- Both pointers begin at the start, advancing at different rates or under distinct conditional predicates.
- **Canonical Use Cases**: In-place duplicate removal, cycle detection (Floyd's algorithm), middle of linked list.

### 3. Dual Sequence Pointers
- Pointer `p1` traverses array $A$, while pointer `p2` traverses array $B$.
- **Canonical Use Cases**: Merging sorted arrays, interval intersections, finding common elements.

### 4. 3-Way Partitioning (Dutch National Flag)
- Three pointers (`low`, `mid`, `high`) partition an array into three discrete segments ($< \text{pivot}$, $== \text{pivot}$, $> \text{pivot}$).
- **Canonical Use Cases**: QuickSort pivot partitioning, 0-1-2 color sorting.

---

## 📐 Mathematical Invariant: Trapping Rain Water

Given an elevation map where width of each bar is 1, compute how much water it can trap after raining.

```
                      Elevation Profile & Trapped Water
          3 │                  █
          2 │          █ ~ ~ ~ █ █ ~ █
          1 │      █ ~ █ █ ~ █ █ █ █ █ █
          0 └──────┴───┴─┴───┴─┴─┴─┴─┴─┴───
            Index: 0 1 2 3 4 5 6 7 8 9 10
```

### The Invariant
At index $i$, the height of trapped water is:
$$\text{Water}[i] = \max(0, \; \min(\text{leftMax}[i], \; \text{rightMax}[i]) - \text{height}[i])$$

In the two-pointer approach:
- Maintain `left` at 0, `right` at $N-1$, with tracking variables `leftMax = height[left]` and `rightMax = height[right]`.
- If `height[left] <= height[right]`:
  - We know for certainty that `leftMax <= height[right] <= rightMax`.
  - Therefore, the bottleneck at `left` is determined strictly by `leftMax`, regardless of any taller bars further to the right!
  - We safely process `left`, add `leftMax - height[left]`, and advance `left++`.
- Symmetrically, if `height[right] < height[left]`:
  - The bottleneck at `right` is strictly `rightMax`. Process `right` and decrement `right--`.
- This executes in strictly **$O(N)$ time** and **$O(1)$ auxiliary space**.

---

## 💻 Complete C++ Implementation

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
#include <iomanip>

class TwoPointerMasterclass {
public:
    // -------------------------------------------------------------
    // Problem 1: 3-Sum (Finding all unique triplets summing to 0)
    // -------------------------------------------------------------
    static std::vector<std::vector<int>> threeSum(std::vector<int> nums) {
        std::vector<std::vector<int>> result;
        int n = static_cast<int>(nums.size());
        if (n < 3) return result;

        // Step 1: Sort to enable monotonic two-pointer convergence
        std::sort(nums.begin(), nums.end());

        for (int i = 0; i < n - 2; i++) {
            // Prune duplicate outer values
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            // Early exit: if smallest element is > 0, sum cannot be 0
            if (nums[i] > 0) break;

            int left = i + 1;
            int right = n - 1;
            int target = -nums[i];

            while (left < right) {
                int sum = nums[left] + nums[right];
                if (sum == target) {
                    result.push_back({nums[i], nums[left], nums[right]});

                    // Skip duplicate inner values
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;

                    left++;
                    right--;
                } else if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return result;
    }

    // -------------------------------------------------------------
    // Problem 2: Dutch National Flag (3-Way In-Place Partitioning)
    // -------------------------------------------------------------
    static void sortColors(std::vector<int>& nums) {
        int low = 0;
        int mid = 0;
        int high = static_cast<int>(nums.size()) - 1;

        /*
           Invariants:
           - nums[0 .. low-1]  == 0 (Red)
           - nums[low .. mid-1] == 1 (White)
           - nums[mid .. high]  == Unexamined
           - nums[high+1 .. N-1]== 2 (Blue)
        */
        while (mid <= high) {
            if (nums[mid] == 0) {
                std::swap(nums[low], nums[mid]);
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else { // nums[mid] == 2
                std::swap(nums[mid], nums[high]);
                high--; // Do not advance mid! New element at mid must be re-evaluated
            }
        }
    }

    // -------------------------------------------------------------
    // Problem 3: Trapping Rain Water (Two-Pointer O(1) Space)
    // -------------------------------------------------------------
    static int trapRainWater(const std::vector<int>& height) {
        int n = static_cast<int>(height.size());
        if (n <= 2) return 0;

        int left = 0, right = n - 1;
        int leftMax = 0, rightMax = 0;
        int totalWater = 0;

        while (left < right) {
            if (height[left] <= height[right]) {
                if (height[left] >= leftMax) {
                    leftMax = height[left];
                } else {
                    totalWater += leftMax - height[left];
                }
                left++;
            } else {
                if (height[right] >= rightMax) {
                    rightMax = height[right];
                } else {
                    totalWater += rightMax - height[right];
                }
                right--;
            }
        }

        return totalWater;
    }

    // -------------------------------------------------------------
    // Problem 4: Remove Duplicates from Sorted Array (Fast & Slow)
    // -------------------------------------------------------------
    static int removeDuplicates(std::vector<int>& nums) {
        if (nums.empty()) return 0;
        int slow = 0;

        for (int fast = 1; fast < static_cast<int>(nums.size()); fast++) {
            if (nums[fast] != nums[slow]) {
                slow++;
                nums[slow] = nums[fast];
            }
        }

        return slow + 1;
    }
};

int main() {
    std::cout << "=== Two-Pointer Technique Comprehensive Test Harness ===\n\n";

    std::cout << "--- 1. Testing 3-Sum with Duplicate Pruning ---\n";
    std::vector<int> nums1 = {-1, 0, 1, 2, -1, -4};
    auto triplets = TwoPointerMasterclass::threeSum(nums1);
    std::cout << "  Input: [-1, 0, 1, 2, -1, -4]\n";
    std::cout << "  Triplets summing to 0:\n";
    for (const auto& trip : triplets) {
        std::cout << "    [ " << trip[0] << ", " << trip[1] << ", " << trip[2] << " ]\n";
    }
    assert(triplets.size() == 2);
    std::cout << "  3-Sum: PASSED\n\n";

    std::cout << "--- 2. Testing Dutch National Flag Partitioning ---\n";
    std::vector<int> colors = {2, 0, 2, 1, 1, 0};
    std::cout << "  Before sort: [ 2, 0, 2, 1, 1, 0 ]\n";
    TwoPointerMasterclass::sortColors(colors);
    std::cout << "  After sort:  [ ";
    for (int c : colors) std::cout << c << " ";
    std::cout << "]\n";
    assert((colors == std::vector<int>{0, 0, 1, 1, 2, 2}));
    std::cout << "  Dutch National Flag: PASSED\n\n";

    std::cout << "--- 3. Testing Trapping Rain Water (Two-Pointer Invariant) ---\n";
    std::vector<int> elevationMap = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    int waterTrapped = TwoPointerMasterclass::trapRainWater(elevationMap);
    std::cout << "  Elevation Map: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]\n";
    std::cout << "  Trapped Water Units: " << waterTrapped << " (Expected: 6)\n";
    assert(waterTrapped == 6);
    std::cout << "  Trapping Rain Water: PASSED\n\n";

    std::cout << "--- 4. Testing Fast & Slow Pointer In-Place Deduplication ---\n";
    std::vector<int> sortedArr = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    int uniqueCount = TwoPointerMasterclass::removeDuplicates(sortedArr);
    std::cout << "  Unique elements count: " << uniqueCount << "\n";
    std::cout << "  Array prefix: [ ";
    for (int i = 0; i < uniqueCount; i++) std::cout << sortedArr[i] << " ";
    std::cout << "]\n";
    assert(uniqueCount == 5);
    std::cout << "  In-Place Deduplication: PASSED\n\n";

    std::cout << "=== All Two-Pointer Masterclass Tests Completed Successfully! ===\n";
    return 0;
}
```

---

## 📊 Complexity Comparison Matrix

| Pattern / Problem | Time Complexity | Auxiliary Space | Prerequisite |
| :--- | :--- | :--- | :--- |
| **2-Sum (Sorted)** | $O(N)$ | $O(1)$ | Array must be sorted |
| **3-Sum** | $O(N^2)$ | $O(1)$ auxiliary | Array must be sorted ($O(N \log N)$) |
| **Dutch National Flag** | $O(N)$ (Single pass) | $O(1)$ | Three distinct target keys |
| **Trapping Rain Water** | $O(N)$ | $O(1)$ | Works on arbitrary elevation arrays |
| **Remove Duplicates** | $O(N)$ | $O(1)$ | Array must be sorted |

---

## 💡 Practical Interview Insights & Gotchas

1. **Duplicate Elimination in 3-Sum**:
   - Always skip duplicate values on the outer loop (`if (i > 0 && nums[i] == nums[i - 1]) continue;`) AND inside the while loop after finding a match.
2. **Dutch Flag High Pointer Swap**:
   - When swapping `nums[mid]` with `nums[high]`, do **not** increment `mid`. The element swapped from `high` has not yet been inspected and could be a 0, 1, or 2.
3. **Trapping Rain Water Equivalence**:
   - While monotonic stacks require $O(N)$ auxiliary memory, the two-pointer approach achieves the exact same result in $O(1)$ space by exploiting global peak dominance.
