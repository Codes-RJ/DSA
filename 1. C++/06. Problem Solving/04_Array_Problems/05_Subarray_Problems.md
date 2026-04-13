# Subarray Problems

## Introduction
A subarray is a **contiguous** part of an array. Subarray problems are very common and often require clever optimization to avoid O(N²) or O(N³) brute-force solutions.

## 1. Kadane's Algorithm
Finds the maximum sum of a contiguous subarray in an array of integers.

**Concept**: At each step, either include the current element in the existing subarray or start a new subarray with the current element.
```cpp
int maxSubarraySum(vector<int>& arr) {
    int maxSoFar = arr[0], currentMax = arr[0];
    for (int i = 1; i < arr.size(); i++) {
        currentMax = max(arr[i], currentMax + arr[i]);
        maxSoFar = max(maxSoFar, currentMax);
    }
    return maxSoFar;
}
```
- **Complexity**: O(N) Time, O(1) Space.

## 2. Prefix Sum Technique
Precalculating the sum of all elements up to index `i`.
`P[i] = P[i-1] + arr[i]`
- Use case: Get `sum(arr[L...R])` in O(1) using `P[R] - P[L-1]`.
- Good for range sum queries.

## 3. Subarrays with Target Sum
Find number of subarrays whose sum is equal to `k`.
- **Strategy**: Use a Hash Map to store prefix sums.
- `current_sum - k = existing_prefix_sum` means there's a subarray ending at `current_index` with sum `k`.

## 4. Product-Based Problems
- **Max Product Subarray**: Similar to Kadane's but keep track of both `max_so_far` and `min_so_far` (because a large negative product can become positive if multiplied by another negative).

## 5. Sliding Window for Subarrays
Used when the subarray must meet certain conditions (e.g., maximum length with sum < k).

## Summary Table

| Problem | Method | Complexity |
|---------|--------|------------|
| Max Sum Subarray | Kadane's | O(N) |
| Range Sum Query | Prefix Sum | O(1) after O(N) |
| Subarray with Sum K | Hash Map + Prefix Sum | O(N) |
| Max Product Subarray | Two-Variable Kadane | O(N) |
| Find all Subarrays | Brute Force | O(N²) |

## Checklist
- [ ] Is it a **contiguous** subarray or a **non-contiguous** subsequence?
- [ ] Does it have negative numbers? (Changes Kadane's logic)
- [ ] Are multiple queries involved? (Consider Prefix Sums)
- [ ] Is a constant window size given? (Sliding Window)
---

## Next Step

- Go to [README.md](README.md) to continue.
