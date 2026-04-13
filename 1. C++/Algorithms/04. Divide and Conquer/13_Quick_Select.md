# 13_Quick_Select.md

## Quick Select (Kth Smallest Element)

### Definition

Quick Select is a divide-and-conquer algorithm to find the kth smallest (or largest) element in an unsorted array. It is similar to Quick Sort but only recurses into one partition instead of both.

### Problem Statement

Input:
- An unsorted array arr
- An integer k (1-indexed, 1 ≤ k ≤ n)

Output:
- The kth smallest element in the array

### Algorithm Steps

```
Step 1: Choose a pivot element (like in Quick Sort)
Step 2: Partition the array around the pivot
        All elements < pivot go left
        All elements > pivot go right
Step 3: After partition, pivot is at its correct sorted position (pivotIndex)
Step 4: If pivotIndex == k-1, return pivot
Step 5: If pivotIndex > k-1, recurse on left side
Step 6: If pivotIndex < k-1, recurse on right side (search for (k - pivotIndex - 1)th element)
```

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>
using namespace std;

int partition(vector<int>& arr, int left, int right) {
    // Choose rightmost element as pivot
    int pivot = arr[right];
    int i = left - 1;
    
    for (int j = left; j < right; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    
    swap(arr[i + 1], arr[right]);
    return i + 1;
}

int partitionRandom(vector<int>& arr, int left, int right) {
    // Random pivot to avoid worst case
    int random = left + rand() % (right - left + 1);
    swap(arr[random], arr[right]);
    return partition(arr, left, right);
}

int quickSelect(vector<int>& arr, int left, int right, int k) {
    if (left == right) {
        return arr[left];
    }
    
    int pivotIndex = partitionRandom(arr, left, right);
    
    if (pivotIndex == k) {
        return arr[pivotIndex];
    } else if (pivotIndex > k) {
        return quickSelect(arr, left, pivotIndex - 1, k);
    } else {
        return quickSelect(arr, pivotIndex + 1, right, k);
    }
}

int findKthSmallest(vector<int>& arr, int k) {
    // k is 1-indexed, convert to 0-index
    return quickSelect(arr, 0, arr.size() - 1, k - 1);
}

int main() {
    srand(time(NULL));
    
    vector<int> arr = {7, 10, 4, 3, 20, 15};
    int k = 3;
    
    int result = findKthSmallest(arr, k);
    
    cout << "The " << k << "rd smallest element is: " << result << endl;
    
    return 0;
}
```

### Example Walkthrough

```
Array: [7, 10, 4, 3, 20, 15]
Find 3rd smallest (k=3, 0-indexed k=2)

Step 1: Choose random pivot (say index 3, value 3)
Partition around 3:
    [3, 7, 10, 4, 20, 15]  (pivot at index 0)
pivotIndex = 0, k=2 → pivotIndex < k → search right side

Step 2: Search right side [7, 10, 4, 20, 15] for (k - 0 - 1 = 1)th element
Choose pivot (say index 2, value 4)
Partition around 4:
    [4, 7, 10, 20, 15]  (pivot at index 0 of subarray)
pivotIndex = 0, k=1 → pivotIndex < k → search right side

Step 3: Search right side [7, 10, 20, 15] for (1 - 0 - 1 = 0)th element
Choose pivot (say index 0, value 7)
Partition around 7:
    [7, 10, 20, 15]  (pivot at index 0)
pivotIndex = 0, k=0 → found!

Result: 7

Sorted array: [3, 4, 7, 10, 15, 20]
3rd smallest is 7 ✓
```

### Kth Largest Element

To find kth largest, either:
1. Find (n - k + 1)th smallest
2. Modify partition to put larger elements on left

```cpp
int partitionForLargest(vector<int>& arr, int left, int right) {
    int pivot = arr[right];
    int i = left - 1;
    
    for (int j = left; j < right; j++) {
        if (arr[j] >= pivot) {  // Note: >= for largest
            i++;
            swap(arr[i], arr[j]);
        }
    }
    
    swap(arr[i + 1], arr[right]);
    return i + 1;
}

int quickSelectLargest(vector<int>& arr, int left, int right, int k) {
    if (left == right) {
        return arr[left];
    }
    
    int pivotIndex = partitionForLargest(arr, left, right);
    
    if (pivotIndex == k) {
        return arr[pivotIndex];
    } else if (pivotIndex > k) {
        return quickSelectLargest(arr, left, pivotIndex - 1, k);
    } else {
        return quickSelectLargest(arr, pivotIndex + 1, right, k);
    }
}

int findKthLargest(vector<int>& arr, int k) {
    return quickSelectLargest(arr, 0, arr.size() - 1, k - 1);
}
```

### Time Complexity

| Case | Time Complexity | Explanation |
|------|----------------|-------------|
| Best | O(n) | Pivot is median each time |
| Average | O(n) | T(n) = T(n/2) + O(n) |
| Worst | O(n²) | Pivot is smallest or largest each time |

### Space Complexity

O(log n) for recursion stack (average case)
O(n) for recursion stack (worst case)

### Iterative Quick Select

```cpp
int quickSelectIterative(vector<int>& arr, int k) {
    int left = 0;
    int right = arr.size() - 1;
    
    while (left <= right) {
        int pivotIndex = partitionRandom(arr, left, right);
        
        if (pivotIndex == k) {
            return arr[pivotIndex];
        } else if (pivotIndex > k) {
            right = pivotIndex - 1;
        } else {
            left = pivotIndex + 1;
        }
    }
    
    return -1;
}
```

### Quick Select vs Sorting

| Approach | Time Complexity | Space Complexity | When to Use |
|----------|----------------|------------------|-------------|
| Sort and index | O(n log n) | O(1) (in-place sort) | Need sorted array anyway |
| Quick Select | O(n) average | O(log n) | Only need kth element |
| Min-Heap | O(n log k) | O(k) | Streaming data |
| Max-Heap | O(n log n) | O(n) | Not recommended |

### Comparison with Other Methods

| Method | Time | Space | Pros | Cons |
|--------|------|-------|------|------|
| Quick Select | O(n) avg | O(log n) | In-place, fast | Worst-case O(n²) |
| Sorting | O(n log n) | O(1) | Simple | Slower for large n |
| Heap | O(n log k) | O(k) | Good for streaming | Extra space |
| nth_element (C++) | O(n) avg | O(log n) | STL implementation | Not available in all languages |

### Applications

| Application | Description |
|-------------|-------------|
| Median finding | k = n/2 |
| Order statistics | Find any percentile |
| Outlier detection | Find extreme values |
| Data analysis | Find quantiles |

### Practice Problems

1. Find kth smallest element in array
2. Find kth largest element in array
3. Find median of unsorted array
4. Find k closest elements to a given value
5. Find k smallest elements (not just the kth)
6. Find kth smallest in two sorted arrays
---

## Next Step

- Go to [14_Convex_Hull.md](14_Convex_Hull.md) to continue with Convex Hull.
