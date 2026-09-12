# Subarray Problems in C++ - Kadane, Prefix Sum Hash Maps, and Sliding Invariants

## 1. Introduction & Theoretical Foundations

A **subarray** is defined as a contiguous slice of an array: $\text{arr}[i \dots j]$ where $0 \le i \le j < N$. Because an array of size $N$ has $\frac{N(N+1)}{2} = O(N^2)$ distinct contiguous subarrays, evaluating all subarrays by brute-force requires $O(N^3)$ or $O(N^2)$ time.

Efficient subarray algorithms reduce these operations to **linear $O(N)$ time** using four foundational paradigms:
1. **Dynamic Programming with Local Invariants** (Kadane's Algorithm)
2. **Dual Extremum Tracking** (Maximum Product Subarray)
3. **Prefix Sum Inversion via Hash Maps** (Subarrays with target sum $K$)
4. **Complementary Inversion** (Maximum Circular Subarray Sum)

---

## 2. Problem 1: Maximum Subarray Sum (Kadane's Algorithm)

### Mathematical Formulation
Let $dp[i]$ be the maximum subarray sum ending strictly at index $i$:
$$dp[i] = \max(\text{arr}[i], \, dp[i - 1] + \text{arr}[i])$$
The global maximum is:
$$\text{MaxSum} = \max_{0 \le i < N} dp[i]$$

Since $dp[i]$ depends solely on $dp[i-1]$, space compresses from $O(N)$ to $O(1)$.

```
Array:        [ -2,   1,  -3,   4,  -1,   2,   1,  -5,   4 ]
dp[i]:          -2    1   -2    4    3    5    6    1    5
MaxSoFar:       -2    1    1    4    4    5    6    6    6  (Max = 6: [4, -1, 2, 1])
```

### C++ Implementation with Subarray Boundary Tracking

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

struct SubarrayResult {
    int maxSum;
    int startIndex;
    int endIndex;
};

class KadaneAlgorithm {
public:
    static SubarrayResult findMaxSubarray(const std::vector<int>& arr) {
        if (arr.empty()) return {0, -1, -1};

        int maxSoFar = arr[0];
        int currentMax = arr[0];
        int start = 0, end = 0, tempStart = 0;

        for (size_t i = 1; i < arr.size(); ++i) {
            if (arr[i] > currentMax + arr[i]) {
                currentMax = arr[i];
                tempStart = i; // Reset subarray start
            } else {
                currentMax += arr[i];
            }

            if (currentMax > maxSoFar) {
                maxSoFar = currentMax;
                start = tempStart;
                end = i;
            }
        }
        return {maxSoFar, start, end};
    }
};
```

---

## 3. Problem 2: Maximum Product Subarray

### The Negative Flips Problem
Unlike addition where negative numbers merely decrease the sum, multiplying by a negative number can turn a very large negative product into a massive positive product!

Thus, at each step $i$, we must maintain **both**:
- $maxProd[i]$: the maximum product of a subarray ending at $i$.
- $minProd[i]$: the minimum (most negative) product of a subarray ending at $i$.

When $\text{arr}[i] < 0$, the maximum and minimum candidates swap roles!

$$maxProd = \max(\text{arr}[i], \, \max(prevMax \times \text{arr}[i], \, prevMin \times \text{arr}[i]))$$
$$minProd = \min(\text{arr}[i], \, \min(prevMax \times \text{arr}[i], \, prevMin \times \text{arr}[i]))$$

### C++ Implementation: Maximum Product Subarray

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

class MaxProductSubarray {
public:
    static int maxProduct(const std::vector<int>& nums) {
        if (nums.empty()) return 0;

        int globalMax = nums[0];
        int currentMax = nums[0];
        int currentMin = nums[0];

        for (size_t i = 1; i < nums.size(); ++i) {
            int val = nums[i];

            if (val < 0) {
                std::swap(currentMax, currentMin);
            }

            currentMax = std::max(val, currentMax * val);
            currentMin = std::min(val, currentMin * val);

            globalMax = std::max(globalMax, currentMax);
        }
        return globalMax;
    }
};
```

---

## 4. Problem 3: Subarray Sum Equals $K$ (Prefix Hash Map)

### Mathematical Formulation
Let $P[i] = \sum_{j=0}^{i} \text{arr}[j]$ be the running prefix sum:
$$\text{Sum}(\text{arr}[i \dots j]) = P[j] - P[i - 1] = K \implies P[i - 1] = P[j] - K$$

As we iterate with $j$, any previously encountered prefix sum equal to $P[j] - K$ marks the start of a valid subarray ending at $j$. By storing prefix sum frequencies in an `std::unordered_map`, we count all qualifying subarrays in **$O(N)$ time**.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

class SubarraySumK {
public:
    static int subarraySum(const std::vector<int>& nums, int k) {
        std::unordered_map<int, int> prefixFreq;
        prefixFreq[0] = 1; // Base case: empty prefix has sum 0

        int runningSum = 0;
        int count = 0;

        for (int num : nums) {
            runningSum += num;
            int target = runningSum - k;

            if (prefixFreq.count(target)) {
                count += prefixFreq[target];
            }
            prefixFreq[runningSum]++;
        }
        return count;
    }
};
```

---

## 5. Problem 4: Maximum Circular Subarray Sum

### The Circular Wraparound Invariant
In a circular array of size $N$, a maximum subarray can either:
1. **Case A (Non-wrapping)**: Resides entirely within the standard array bounds. (Solved via standard Kadane's).
2. **Case B (Wrapping)**: Wraps around the boundary from end back to start.
   - The remaining elements between the wrapped ends form a **contiguous non-wrapping minimum subarray**!
   - Therefore:
$$\text{CircularMax} = \text{TotalSum} - \text{MinSubarraySum}$$

**Critical Edge Case:** If all elements are negative, $\text{TotalSum} == \text{MinSubarraySum}$, which would yield $0$ (an empty subarray). If all numbers are negative, the answer must simply be the non-wrapping $\text{MaxSubarraySum}$.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

class CircularSubarray {
public:
    static int maxSubarraySumCircular(const std::vector<int>& nums) {
        int totalSum = 0;
        int maxKadane = nums[0], currMax = 0;
        int minKadane = nums[0], currMin = 0;

        for (int x : nums) {
            totalSum += x;

            currMax = std::max(x, currMax + x);
            maxKadane = std::max(maxKadane, currMax);

            currMin = std::min(x, currMin + x);
            minKadane = std::min(minKadane, currMin);
        }

        // Edge case: all negative numbers
        if (maxKadane < 0) {
            return maxKadane;
        }

        return std::max(maxKadane, totalSum - minKadane);
    }
};
```

---

## 6. Complete Runnable Verification Suite

```cpp
#include <iostream>
#include <vector>

int main() {
    std::cout << "=====================================================" << std::endl;
    std::cout << "          SUBARRAY PROBLEMS ALGORITHMIC SUITE        " << std::endl;
    std::cout << "=====================================================" << std::endl;

    // --- 1. Kadane's Algorithm with Index Tracking ---
    std::cout << "\n[1] KADANE'S MAXIMUM SUBARRAY SUM:" << std::endl;
    std::vector<int> arr1 = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    auto res1 = KadaneAlgorithm::findMaxSubarray(arr1);
    std::cout << "  Max Sum: " << res1.maxSum << " from index " 
              << res1.startIndex << " to " << res1.endIndex << " (Subarray: ";
    for (int i = res1.startIndex; i <= res1.endIndex; ++i) {
        std::cout << arr1[i] << (i < res1.endIndex ? ", " : "");
    }
    std::cout << ")" << std::endl;

    // --- 2. Maximum Product Subarray ---
    std::cout << "\n[2] MAXIMUM PRODUCT SUBARRAY:" << std::endl;
    std::vector<int> arr2 = {2, 3, -2, 4, -1};
    int maxProd = MaxProductSubarray::maxProduct(arr2);
    std::cout << "  Array: {2, 3, -2, 4, -1}" << std::endl;
    std::cout << "  Max Product: " << maxProd << " (Expected: 48 via {2, 3, -2, 4, -1})" << std::endl;

    // --- 3. Subarray Sum Equals K ---
    std::cout << "\n[3] SUBARRAY SUM EQUALS K (k = 7):" << std::endl;
    std::vector<int> arr3 = {3, 4, 7, 2, -3, 1, 4, 2};
    int countK = SubarraySumK::subarraySum(arr3, 7);
    std::cout << "  Total subarrays with sum 7: " << countK << std::endl;

    // --- 4. Maximum Circular Subarray Sum ---
    std::cout << "\n[4] MAXIMUM CIRCULAR SUBARRAY SUM:" << std::endl;
    std::vector<int> arr4 = {5, -3, 5};
    int circMax = CircularSubarray::maxSubarraySumCircular(arr4);
    std::cout << "  Array: {5, -3, 5}" << std::endl;
    std::cout << "  Max Circular Sum: " << circMax << " (Expected: 10 via wrapped 5 + 5)" << std::endl;

    std::cout << "\n=====================================================" << std::endl;
    return 0;
}
```

---

## 7. Complexity Analysis Table

| Subarray Problem | Algorithm Technique | Time Complexity | Auxiliary Space | Key Invariant |
| :--- | :--- | :--- | :--- | :--- |
| **Max Subarray Sum** | Kadane's Local Max | $O(N)$ | $O(1)$ | $dp[i] = \max(\text{arr}[i], dp[i-1] + \text{arr}[i])$ |
| **Max Product Subarray** | Dual Min/Max Tracking | $O(N)$ | $O(1)$ | Negative multiplier swaps min and max |
| **Subarray Sum Equals $K$** | Prefix Sum Frequency Map | $O(N)$ | $O(N)$ | $P[j] - P[i-1] = K \implies P[i-1] = P[j] - K$ |
| **Circular Subarray Sum** | Complementary Min Kadane | $O(N)$ | $O(1)$ | $\max(\text{MaxKadane}, \, \text{TotalSum} - \text{MinKadane})$ |

---

## 8. Common Pitfalls & Interview Traps

1. **Kadane Resetting to 0 Instead of Current Element**: Initializing `maxSoFar = 0` or resetting `currentMax = 0` produces incorrect results when all array elements are negative (e.g., `{-5, -2, -8}` returns `0` instead of `-2`).
2. **Subarray Sum $K$ Base Case Missing**: Failing to initialize `prefixFreq[0] = 1` misses all valid subarrays that start at index $0$.
3. **Circular Subarray All-Negative Edge Case**: If all numbers are negative, $\text{TotalSum} == \text{MinKadane}$, so $\text{TotalSum} - \text{MinKadane} == 0$, which falsely returns $0$ instead of the single least-negative element.

---

## Next Step

- Proceed to [06_Next_Permutation.md](06_Next_Permutation.md) to master lexicographical sequence transformations in C++.
