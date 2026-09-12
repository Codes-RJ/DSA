# Container With Most Water in C++ - Two-Pointer Convergence & Invariant Proof

## 1. Introduction & Theoretical Foundations

The **Container With Most Water** problem is an interview classic that exemplifies the power of **two-pointer greedy convergence**. Given an integer array `height` of length $N$, each index $i$ represents a vertical line drawn at coordinate $(i, \text{height}[i])$ extending down to $(i, 0)$.

Find two lines that together with the x-axis form a container such that the container contains the most water.

```
       Height Map: [1, 8, 6, 2, 5, 4, 8, 3, 7]
       
         8 |     █               █
         7 |     █ ~ ~ ~ ~ ~ ~ ~ █ ~ ~ ~ █   ◄── Optimal Container (Area = 49)
         6 |     █ █             █       █
         5 |     █ █     █       █       █
         4 |     █ █     █ █     █       █
         3 |     █ █     █ █     █ █     █
         2 |     █ █ █   █ █     █ █     █
         1 |   █ █ █ █   █ █     █ █     █
         0 └───┴─█─┴─█─█─█─█─█─█─█─█─█─█─█───
               0 1 2 3 4 5 6 7 8
```

---

## 2. Mathematical Formulation & Optimality Proof

The volume of water between lines at indices $L$ and $R$ ($L < R$) is governed by the container formula:
$$\text{Area}(L, R) = (R - L) \times \min(\text{height}[L], \, \text{height}[R])$$

A naive brute-force algorithm tests all $\frac{N(N - 1)}{2} = O(N^2)$ pairs.

### Proof of Two-Pointer Convergence ($O(N)$ Time)
Initialize pointers at the maximal width: `L = 0` and `R = N - 1`.

Suppose without loss of generality that $\text{height}[L] \le \text{height}[R]$:
1. The height of water trapped between $L$ and $R$ is $\text{height}[L]$.
2. For any interior index $k$ such that $L < k < R$:
   - The width $(k - L)$ is strictly less than $(R - L)$.
   - The height $\min(\text{height}[L], \text{height}[k])$ cannot exceed $\text{height}[L]$.
   - Therefore:
$$\text{Area}(L, k) = (k - L) \times \min(\text{height}[L], \text{height}[k]) \le (k - L) \times \text{height}[L] < (R - L) \times \text{height}[L] = \text{Area}(L, R)$$

**Deduction:** No container formed by pairing $L$ with any interior index $k$ can ever surpass $\text{Area}(L, R)$.
Thus, index $L$ is **completely exhausted** and can be eliminated from future consideration. We safely increment `L++` without missing the global maximum!

Similarly, if $\text{height}[R] < \text{height}[L]$, we decrement `R--`.

---

## 3. Production-Grade C++ Implementation

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

struct ContainerResult {
    int maxArea;
    int leftIndex;
    int rightIndex;
};

class MostWaterContainer {
public:
    // O(N) Time, O(1) Auxiliary Space
    static ContainerResult maxArea(const std::vector<int>& height) {
        int n = height.size();
        if (n < 2) return {0, -1, -1};

        int left = 0;
        int right = n - 1;
        int maxWater = 0;
        int bestL = 0, bestR = n - 1;

        while (left < right) {
            int width = right - left;
            int hL = height[left];
            int hR = height[right];
            int currentWater = width * std::min(hL, hR);

            if (currentWater > maxWater) {
                maxWater = currentWater;
                bestL = left;
                bestR = right;
            }

            // Always discard the shorter line
            if (hL <= hR) {
                left++;
            } else {
                right--;
            }
        }

        return {maxWater, bestL, bestR};
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
    std::cout << "       CONTAINER WITH MOST WATER ALGORITHMIC SUITE   " << std::endl;
    std::cout << "=====================================================" << std::endl;

    // --- 1. Standard Case ---
    std::cout << "\n[1] STANDARD ELEVATION {1, 8, 6, 2, 5, 4, 8, 3, 7}:" << std::endl;
    std::vector<int> height1 = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    auto res1 = MostWaterContainer::maxArea(height1);
    std::cout << "  Max Water: " << res1.maxArea << " units between indices "
              << res1.leftIndex << " (height=" << height1[res1.leftIndex] << ") and "
              << res1.rightIndex << " (height=" << height1[res1.rightIndex] << ")" << std::endl;
    std::cout << "  Expected: 49 (Width 7 * Height 7)" << std::endl;

    // --- 2. Equal Heights ---
    std::cout << "\n[2] EQUAL HEIGHTS {1, 1}:" << std::endl;
    std::vector<int> height2 = {1, 1};
    auto res2 = MostWaterContainer::maxArea(height2);
    std::cout << "  Max Water: " << res2.maxArea << " (Expected: 1)" << std::endl;

    // --- 3. Decreasing Heights ---
    std::cout << "\n[3] MONOTONIC DECREASING {4, 3, 2, 1, 4}:" << std::endl;
    std::vector<int> height3 = {4, 3, 2, 1, 4};
    auto res3 = MostWaterContainer::maxArea(height3);
    std::cout << "  Max Water: " << res3.maxArea << " (Expected: 16 via outer boundaries)" << std::endl;

    std::cout << "\n=====================================================" << std::endl;
    return 0;
}
```

---

## 5. Complexity Analysis Table

| Method | Time Complexity | Auxiliary Space | Operations per Step |
| :--- | :--- | :--- | :--- |
| **Brute Force** | $O(N^2)$ | $O(1)$ | $\frac{N(N-1)}{2}$ area calculations |
| **Two-Pointer Convergence** | $O(N)$ | $O(1)$ | Exactly $N - 1$ steps |

---

## 6. Common Pitfalls & Interview Traps

1. **Moving the Taller Pointer**: If you move the pointer with the taller line, the width shrinks by $1$ and the new height can at most be equal to the shorter line, guaranteeing that the area can only decrease or stay the same. **Always advance the shorter line.**
2. **Strict Equality Tie-Breaking**: When `height[L] == height[R]`, moving either pointer (or both) is mathematically correct because neither can be paired with any interior line to beat the current width with that height.
3. **Confusion with Trapping Rain Water**: Container With Most Water finds the single maximal rectangle between two lines without intermediate obstacles. Trapping Rain Water computes the cumulative sum of puddle basins trapped between all bars.

---

## Next Step

- Proceed to [09_Product_Except_Self.md](09_Product_Except_Self.md) to explore prefix and suffix product accumulators without division.
