# Exponential Search

## Overview
Exponential search is an algorithm for searching in sorted, unbounded, or infinite arrays. It works by finding a range containing the target and then performing binary search within that range.

## Algorithm Description

### Theory
Exponential search first checks if the first element is the target. If not, it finds a range by repeatedly doubling the index until the element at that index is greater than or equal to the target. Then it performs binary search within the identified range.

### Algorithm Steps
1. Check if first element is the target
2. Initialize i = 1 and repeatedly double i while arr[i] ≤ target
3. Perform binary search between i/2 and min(i, n-1)

### Pseudocode
```
FUNCTION exponentialSearch(array, target):
    n = length(array)
    
    // Check if first element is the target
    IF array[0] == target:
        RETURN 0
    
    // Find range for binary search
    i = 1
    WHILE i < n AND array[i] <= target:
        i = i * 2
    
    // Perform binary search in found range
    RETURN binarySearch(array, i/2, min(i, n-1), target)
```

## Complexity Analysis

### Time Complexity
- **Best Case**: O(1) - Target at first position
- **Average Case**: O(log n)
- **Worst Case**: O(log n)

### Space Complexity
- **Space**: O(1) - Iterative implementation
- **Space**: O(log n) - Recursive binary search

## Best Practices
- Ideal for unbounded or infinite sorted arrays
- Useful when array size is unknown
- More efficient than binary search for targets near beginning
- Combined with binary search for optimal performance

## When to Use
- Unbounded or infinite sorted arrays
- When array size is unknown
- Search operations near the beginning of large arrays
- Streaming data scenarios

## Variants

### 1. Basic Exponential Search
Standard implementation with range finding followed by binary search.

### 2. Recursive Exponential Search
Recursive implementation for cleaner code.

### 3. Modified Exponential Search
Optimized for specific data distributions.

## Implementation Examples

### Example 1: Basic Exponential Search
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int binarySearch(const std::vector<int>& arr, int left, int right, int target) {
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}

int exponentialSearch(const std::vector<int>& arr, int target) {
    int n = arr.size();
    
    if (n == 0) return -1;
    
    // Check if first element is the target
    if (arr[0] == target) {
        return 0;
    }
    
    // Find range for binary search
    int i = 1;
    while (i < n && arr[i] <= target) {
        i *= 2;
    }
    
    // Perform binary search in found range
    return binarySearch(arr, i / 2, std::min(i, n - 1), target);
}
```

### Example 2: Exponential Search for Unbounded Arrays
```cpp
int exponentialSearchUnbounded(const std::vector<int>& arr, int target) {
    // Assume array is conceptually infinite
    if (arr[0] == target) return 0;
    
    int i = 1;
    while (arr[i] <= target) {
        i *= 2;
    }
    
    return binarySearch(arr, i / 2, i, target);
}
```

## Testing and Verification

### Test Cases
1. **Target at beginning**: Should return index 0
2. **Target at end**: Should find efficiently
3. **Target in middle**: Should work correctly
4. **Target not present**: Should return -1
5. **Single element array**: Should handle edge case

### Performance Comparison
- Exponential search vs binary search for different target positions
- Efficiency for unbounded vs bounded arrays

## Common Pitfalls
1. Not handling empty arrays
2. Integer overflow when doubling index
3. Not checking array bounds
4. Incorrect range calculation for binary search

## Optimization Tips
1. Use iterative binary search to avoid stack overflow
2. Add bounds checking for safety
3. Consider cache performance for large arrays
4. Use appropriate data types for large indices

## Real-World Applications
- Searching in streaming data
- Infinite data structures
- File system searches
- Database index searches
- Network packet analysis

## Related Algorithms
- Binary Search
- Interpolation Search
- Jump Search
- Fibonacci Search

## References
- Introduction to Algorithms (CLRS)
- Algorithm Design Manual
- Online algorithm resources

---

*This implementation provides a comprehensive guide to exponential search with practical examples and best practices.*
---

## Next Step

- Go to [06_Fibonacci_Search.md](06_Fibonacci_Search.md) to continue with Fibonacci Search.
