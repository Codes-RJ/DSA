# 10_Median_of_Two_Sorted_Arrays.md

## Median of Two Sorted Arrays

### Definition

Given two sorted arrays of size m and n, find the median of the combined sorted array without actually merging them.

### Problem Statement

Input:
- Sorted array nums1 of size m
- Sorted array nums2 of size n

Output:
- Median of the combined array

### Key Insight

If we partition both arrays such that all elements on the left side are less than all elements on the right side, the median is the max of left side (if total length odd) or average of max left and min right (if even).

### Visual Representation

```
Combined sorted array of size m+n:

Left Part               | Right Part
[..., ..., ...]         | [..., ..., ...]
Size = (m+n+1)/2        | Size = (m+n)/2

We need:
max(left part) ≤ min(right part)
```

### Divide and Conquer Approach (Binary Search)

```
Step 1: Ensure nums1 is the smaller array (m ≤ n)
Step 2: Binary search on the partition point in nums1
Step 3: Partition in nums2 is determined by total left size
Step 4: Check if max(left) ≤ min(right)
Step 5: Adjust partition based on comparison
```

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    int m = nums1.size();
    int n = nums2.size();
    
    // Ensure nums1 is the smaller array
    if (m > n) {
        return findMedianSortedArrays(nums2, nums1);
    }
    
    int left = 0;
    int right = m;
    int totalLeft = (m + n + 1) / 2;
    
    while (left <= right) {
        int partition1 = left + (right - left) / 2;
        int partition2 = totalLeft - partition1;
        
        int maxLeft1 = (partition1 == 0) ? INT_MIN : nums1[partition1 - 1];
        int minRight1 = (partition1 == m) ? INT_MAX : nums1[partition1];
        
        int maxLeft2 = (partition2 == 0) ? INT_MIN : nums2[partition2 - 1];
        int minRight2 = (partition2 == n) ? INT_MAX : nums2[partition2];
        
        if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
            // Found correct partition
            if ((m + n) % 2 == 0) {
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0;
            } else {
                return max(maxLeft1, maxLeft2);
            }
        } else if (maxLeft1 > minRight2) {
            // Move partition1 left
            right = partition1 - 1;
        } else {
            // Move partition1 right
            left = partition1 + 1;
        }
    }
    
    return 0.0;  // Should not reach here
}

int main() {
    vector<int> nums1 = {1, 3};
    vector<int> nums2 = {2};
    
    double median = findMedianSortedArrays(nums1, nums2);
    cout << "Median: " << median << endl;
    
    return 0;
}
```

### Example Walkthrough

```
Example 1:
nums1 = [1, 3], nums2 = [2]
m = 2, n = 1, totalLeft = (3+1)/2 = 2

Binary search on nums1 (size 2):
left=0, right=2

partition1 = 1, partition2 = 2-1 = 1
maxLeft1 = 1, minRight1 = 3
maxLeft2 = 2, minRight2 = INT_MAX
Check: maxLeft1(1) ≤ minRight2(INF) ✓, maxLeft2(2) ≤ minRight1(3) ✓
(m+n) odd → median = max(1, 2) = 2

Result: 2

Example 2:
nums1 = [1, 2], nums2 = [3, 4]
m = 2, n = 2, totalLeft = (4+1)/2 = 2

partition1 = 1, partition2 = 2-1 = 1
maxLeft1 = 1, minRight1 = 2
maxLeft2 = 3, minRight2 = 4
Check: maxLeft1(1) ≤ minRight2(4) ✓, maxLeft2(3) ≤ minRight1(2)? No → move right
left = 2, right = 2

partition1 = 2, partition2 = 2-2 = 0
maxLeft1 = 2, minRight1 = INF
maxLeft2 = INT_MIN, minRight2 = 3
Check: maxLeft1(2) ≤ minRight2(3) ✓, maxLeft2(-INF) ≤ minRight1(INF) ✓
(m+n) even → median = (max(2, -INF) + min(INF, 3))/2 = (2+3)/2 = 2.5

Result: 2.5
```

### Visual Partition Explanation

```
nums1: [1, 2, 3, 4, 5]
nums2: [6, 7, 8, 9, 10]

Combined sorted: [1,2,3,4,5,6,7,8,9,10]
Median = (5+6)/2 = 5.5

Partition:
nums1 left: [1,2,3,4]  |  nums1 right: [5]
nums2 left: [6]         |  nums2 right: [7,8,9,10]

Left side combined: [1,2,3,4,6] (size 5)
Right side combined: [5,7,8,9,10] (size 5)

maxLeft = max(4,6) = 6
minRight = min(5,7) = 5
Wait, this violates maxLeft ≤ minRight (6 > 5) → need adjustment.
Correct partition would be different.
```

### Time Complexity

| Operation | Complexity |
|-----------|------------|
| Binary search on smaller array | O(log(min(m, n))) |
| Total | O(log(min(m, n))) |

### Space Complexity

O(1) extra space

### Alternative: Merge Until Median (O(m+n))

```cpp
double findMedianMerge(vector<int>& nums1, vector<int>& nums2) {
    int m = nums1.size(), n = nums2.size();
    int total = m + n;
    int i = 0, j = 0;
    int prev = 0, curr = 0;
    
    for (int count = 0; count <= total / 2; count++) {
        prev = curr;
        if (i < m && (j >= n || nums1[i] < nums2[j])) {
            curr = nums1[i++];
        } else {
            curr = nums2[j++];
        }
    }
    
    if (total % 2 == 0) {
        return (prev + curr) / 2.0;
    } else {
        return curr;
    }
}
```

### Comparison of Approaches

| Approach | Time Complexity | Space Complexity | When to Use |
|----------|----------------|------------------|-------------|
| Merge until median | O(m+n) | O(1) | Small arrays |
| Binary search | O(log(min(m,n))) | O(1) | Large arrays |
| Brute force (merge all) | O(m+n) | O(m+n) | Not recommended |

### Edge Cases

| Case | Handling |
|------|----------|
| One array empty | Median of the other array |
| Both arrays empty | Undefined (not valid input) |
| All elements same | Works correctly |
| Very large numbers | Use long long for sums |

### Practice Problems

1. Find median of two sorted arrays
2. Find kth element of two sorted arrays
3. Find median of k sorted arrays
4. Find median of two sorted arrays of different sizes
5. Find median of two sorted arrays with duplicates
---

## Next Step

- Go to [11_Inversion_Count.md](11_Inversion_Count.md) to continue with Inversion Count.
