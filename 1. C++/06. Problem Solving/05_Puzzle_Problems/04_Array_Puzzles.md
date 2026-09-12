# Array Puzzles in C++ - Boundary Invariants, Monotonic Structures, and Partitioning

## 1. Introduction & Theoretical Foundations

**Array puzzles** require sophisticated index manipulation, boundary tracking, and pointer coordination without auxiliary memory allocations. These problems often transform $O(N^2)$ or $O(N^3)$ brute-force simulations into optimal $O(N)$ or $O(\log N)$ algorithms through mathematical invariants and monotonic properties.

This module provides comprehensive theoretical foundations and production-ready C++ implementations for the 3 most critical array puzzles:
1. **2D Spiral Matrix Traversal & Generation** (4-Boundary Pointer Invariant)
2. **Trapping Rain Water** (Two-Pointer $O(1)$ Space and Monotonic Stack Approaches)
3. **Median of Two Sorted Arrays** ($O(\log(\min(M, N)))$ Binary Search Partitioning)

---

## 2. Puzzle 1: 2D Spiral Matrix Traversal & Generation

### Problem Statement
1. **Spiral Traversal**: Given an $M \times N$ matrix, return all elements in spiral order starting from $(0, 0)$ clockwise.
2. **Spiral Generation**: Given an integer $N$, generate an $N \times N$ matrix filled with elements from $1$ to $N^2$ in spiral order.

```
       top  ──►  1  ──►  2  ──►  3
                                 │
                                 ▼
                 8  ──►  9       4
                 ▲               │
                 │               ▼
    bottom  ──►  7  ◄──  6  ◄──  5
                 ▲               ▲
                 │               │
                left           right
```

### Boundary Contraction Invariant
We maintain four boundaries: `top = 0`, `bottom = M - 1`, `left = 0`, `right = N - 1`.
Each iteration executes 4 directional sweeps, contracting the respective boundary:
1. **Left $\to$ Right** along row `top`: `top++`
2. **Top $\to$ Bottom** along column `right`: `right--`
3. **Right $\to$ Left** along row `bottom`: `bottom--` *(Requires guard `top <= bottom`)*
4. **Bottom $\to$ Top** along column `left`: `left++` *(Requires guard `left <= right`)*

### C++ Implementation: Spiral Traversal and Generation

```cpp
#include <iostream>
#include <vector>
#include <iomanip>

class SpiralMatrix {
public:
    // Traversal: O(M * N) time, O(1) auxiliary space
    static std::vector<int> spiralOrder(const std::vector<std::vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return {};
        
        int rows = matrix.size();
        int cols = matrix[0].size();
        std::vector<int> result;
        result.reserve(rows * cols);

        int top = 0, bottom = rows - 1;
        int left = 0, right = cols - 1;

        while (top <= bottom && left <= right) {
            // Sweep 1: Left to Right
            for (int c = left; c <= right; ++c) {
                result.push_back(matrix[top][c]);
            }
            top++;

            // Sweep 2: Top to Bottom
            for (int r = top; r <= bottom; ++r) {
                result.push_back(matrix[r][right]);
            }
            right--;

            // Sweep 3: Right to Left (Guard against single-row overlap)
            if (top <= bottom) {
                for (int c = right; c >= left; --c) {
                    result.push_back(matrix[bottom][c]);
                }
                bottom--;
            }

            // Sweep 4: Bottom to Top (Guard against single-column overlap)
            if (left <= right) {
                for (int r = bottom; r >= top; --r) {
                    result.push_back(matrix[r][left]);
                }
                left++;
            }
        }
        return result;
    }

    // Generation: O(N^2) time, O(1) auxiliary space (excluding result matrix)
    static std::vector<std::vector<int>> generateMatrix(int n) {
        std::vector<std::vector<int>> matrix(n, std::vector<int>(n, 0));
        int top = 0, bottom = n - 1;
        int left = 0, right = n - 1;
        int val = 1;

        while (top <= bottom && left <= right) {
            for (int c = left; c <= right; ++c) matrix[top][c] = val++;
            top++;

            for (int r = top; r <= bottom; ++r) matrix[r][right] = val++;
            right--;

            if (top <= bottom) {
                for (int c = right; c >= left; --c) matrix[bottom][c] = val++;
                bottom--;
            }

            if (left <= right) {
                for (int r = bottom; r >= top; --r) matrix[r][left] = val++;
                left++;
            }
        }
        return matrix;
    }
};
```

---

## 3. Puzzle 2: Trapping Rain Water

### Problem Statement
Given $N$ non-negative integers representing an elevation map where the width of each bar is $1$, compute how much water it can trap after raining.

```
       Elevation Map: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
       
         3 |                       █
         2 |             █ ~ ~ ~ ~ █ █ ~ █
         1 |     █ ~ ~ █ █ ~ █ ~ █ █ █ █ █
         0 └───┴─█─┴─█─█─█─█─█─█─█─█─█─█─█───
                 0 1 0 2 1 0 1 3 2 1 2 1
                       Total trapped = 6 units
```

### Mathematical Formulation
The volume of water trapped above any bar at index $i$ is determined strictly by the minimum of the highest bar to its left and the highest bar to its right:
$$\text{Water}[i] = \max\Big(0, \, \min\big(\max_{0 \le j \le i} H[j], \; \max_{i \le j < N} H[j]\big) - H[i]\Big)$$

### Technique A: Two Pointers ($O(N)$ Time, $O(1)$ Space)
Instead of precomputing prefix and suffix max arrays:
- Maintain two pointers `left = 0` and `right = N - 1`, and their respective running maximums `leftMax` and `rightMax`.
- If `leftMax < rightMax`, we know with certainty that the water level at `left` is bounded by `leftMax`, regardless of any intermediate bars. We process `left` and advance `left++`.
- Otherwise, the water level at `right` is bounded by `rightMax`. We process `right` and advance `right--`.

### Technique B: Monotonic Stack ($O(N)$ Time, $O(N)$ Space)
- Maintain a decreasing monotonic stack of indices.
- When encountering a bar taller than the stack top, we have found a right boundary. We pop the bounded bottom, compute the trapped horizontal layer bounded by the new stack top (left boundary) and the current bar (right boundary).

### C++ Implementation: Trapping Rain Water (Both Methods)

```cpp
#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

class RainWaterTrapping {
public:
    // Method 1: Two Pointers - O(N) time, O(1) space (Optimal)
    static int trapTwoPointers(const std::vector<int>& height) {
        int n = height.size();
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

    // Method 2: Monotonic Stack - O(N) time, O(N) space
    static int trapMonotonicStack(const std::vector<int>& height) {
        int n = height.size();
        std::stack<int> st; // Stores indices of decreasing heights
        int totalWater = 0;

        for (int i = 0; i < n; ++i) {
            while (!st.empty() && height[i] > height[st.top()]) {
                int bottomIdx = st.top();
                st.pop();

                if (st.empty()) break; // No left boundary

                int leftIdx = st.top();
                int boundedHeight = std::min(height[leftIdx], height[i]) - height[bottomIdx];
                int distance = i - leftIdx - 1;

                totalWater += boundedHeight * distance;
            }
            st.push(i);
        }
        return totalWater;
    }
};
```

---

## 4. Puzzle 3: Median of Two Sorted Arrays

### Problem Statement
Given two sorted arrays `nums1` and `nums2` of sizes $M$ and $N$, return the median of the combined sorted array in **$O(\log(\min(M, N)))$ time complexity**.

### Binary Search on Partitions
Let the combined size be $M + N$. We partition `nums1` at index $i$ and `nums2` at index $j$ such that:
$$i + j = \frac{M + N + 1}{2}$$
This ensures the left partition contains exactly half of all elements.

```
       nums1:  [  x1,  x2  |  x3,  x4,  x5  ]    (partition at i)
       nums2:  [  y1,  y2, y3  |  y4  ]          (partition at j)
               ◄── Left ──► ◄── Right ──►
```

The partition is valid if and only if:
$$\max(\text{left}_1) \le \min(\text{right}_2) \quad \text{and} \quad \max(\text{left}_2) \le \min(\text{right}_1)$$

- If $\max(\text{left}_1) > \min(\text{right}_2)$, $i$ is too far right $\implies \text{high} = i - 1$.
- If $\max(\text{left}_2) > \min(\text{right}_1)$, $i$ is too far left $\implies \text{low} = i + 1$.

Once partitioned:
- If $(M + N)$ is odd: $\text{Median} = \max(\max(\text{left}_1), \max(\text{left}_2))$.
- If $(M + N)$ is even: $\text{Median} = \frac{\max(\text{left}_1, \text{left}_2) + \min(\text{right}_1, \text{right}_2)}{2.0}$.

### C++ Implementation: Median of Two Sorted Arrays

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

class MedianSortedArrays {
public:
    static double findMedianSortedArrays(const std::vector<int>& nums1, 
                                         const std::vector<int>& nums2) {
        // Ensure binary search is performed on the smaller array for O(log(min(M, N)))
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int m = nums1.size();
        int n = nums2.size();
        int low = 0, high = m;

        while (low <= high) {
            int partitionX = low + (high - low) / 2;
            int partitionY = (m + n + 1) / 2 - partitionX;

            // Handle partition boundaries with +/- infinity
            int maxLeftX = (partitionX == 0) ? INT_MIN : nums1[partitionX - 1];
            int minRightX = (partitionX == m) ? INT_MAX : nums1[partitionX];

            int maxLeftY = (partitionY == 0) ? INT_MIN : nums2[partitionY - 1];
            int minRightY = (partitionY == n) ? INT_MAX : nums2[partitionY];

            if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
                // Correct partition found
                if ((m + n) % 2 != 0) {
                    return std::max(maxLeftX, maxLeftY);
                } else {
                    return (std::max(maxLeftX, maxLeftY) + std::min(minRightX, minRightY)) / 2.0;
                }
            } else if (maxLeftX > minRightY) {
                high = partitionX - 1; // Move left in nums1
            } else {
                low = partitionX + 1;  // Move right in nums1
            }
        }
        throw std::invalid_argument("Input arrays are not sorted.");
    }
};
```

---

## 5. Complete Runnable Verification Suite

```cpp
#include <iostream>
#include <vector>
#include <iomanip>

int main() {
    std::cout << "=====================================================" << std::endl;
    std::cout << "            ARRAY PUZZLES ALGORITHMIC SUITE          " << std::endl;
    std::cout << "=====================================================" << std::endl;

    // --- 1. Spiral Matrix Traversal ---
    std::cout << "\n[1] SPIRAL MATRIX TRAVERSAL (3x4 Matrix):" << std::endl;
    std::vector<std::vector<int>> matrix = {
        { 1,  2,  3,  4},
        { 5,  6,  7,  8},
        { 9, 10, 11, 12}
    };
    auto spiralResult = SpiralMatrix::spiralOrder(matrix);
    std::cout << "  Spiral output: ";
    for (int v : spiralResult) std::cout << v << " ";
    std::cout << std::endl;

    // --- 2. Trapping Rain Water ---
    std::cout << "\n[2] TRAPPING RAIN WATER:" << std::endl;
    std::vector<int> elevation = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    int water2P = RainWaterTrapping::trapTwoPointers(elevation);
    int waterStack = RainWaterTrapping::trapMonotonicStack(elevation);
    std::cout << "  Trapped Water (Two Pointers):   " << water2P << " units" << std::endl;
    std::cout << "  Trapped Water (Monotonic Stack): " << waterStack << " units" << std::endl;

    // --- 3. Median of Two Sorted Arrays ---
    std::cout << "\n[3] MEDIAN OF TWO SORTED ARRAYS:" << std::endl;
    std::vector<int> arr1 = {1, 3, 8};
    std::vector<int> arr2 = {7, 9, 10, 11};
    double median = MedianSortedArrays::findMedianSortedArrays(arr1, arr2);
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "  arr1 = {1, 3, 8}, arr2 = {7, 9, 10, 11}" << std::endl;
    std::cout << "  Combined Median: " << median << " (Expected: 8.00)" << std::endl;

    std::cout << "\n=====================================================" << std::endl;
    return 0;
}
```

---

## 6. Complexity Analysis Table

| Array Puzzle | Algorithm Technique | Time Complexity | Auxiliary Space | Key Invariant |
| :--- | :--- | :--- | :--- | :--- |
| **Spiral Traversal** | 4-Boundary Pointers | $O(M \cdot N)$ | $O(1)$ | $top \le bottom$ & $left \le right$ |
| **Spiral Generation** | In-place Boundary Sweep | $O(N^2)$ | $O(1)$ | Concentric perimeter filling |
| **Trapping Rain (2-Ptr)** | Two-Pointer Max Track | $O(N)$ | $O(1)$ | Water level bounded by $\min(L_{max}, R_{max})$ |
| **Trapping Rain (Stack)** | Monotonic Stack | $O(N)$ | $O(N)$ | Horizontal layer calculation |
| **Median Sorted Arrays** | Binary Search Partition | $O(\log(\min(M, N)))$ | $O(1)$ | $L_{max1} \le R_{min2}$ and $L_{max2} \le R_{min1}$ |

---

## 7. Common Pitfalls & Interview Traps

1. **Spiral Traversal Rectangular Overlap**: In non-square matrices (e.g., $1 \times N$ or $M \times 1$), failing to check `if (top <= bottom)` before Sweep 3 causes elements in the single row to be printed twice (once left-to-right, and again right-to-left).
2. **Rain Water Negative Volume**: Failing to take $\max(0, \text{bound} - \text{height}[i])$ can cause negative water additions if height exceeds the boundary.
3. **Median Search Array Sizing**: Performing binary search on the larger array results in $O(\log(\max(M, N)))$ time and can cause the partition index in the other array to become negative or exceed bounds. Always ensure `nums1.size() <= nums2.size()`.

---

## Next Step

- Proceed to [05_Recreational_Problems.md](05_Recreational_Problems.md) to explore the Knight's Tour, Gale-Shapley Stable Marriage, and Magic Squares in C++.
