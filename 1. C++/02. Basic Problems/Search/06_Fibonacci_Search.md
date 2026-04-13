# Fibonacci Search

## Overview
Fibonacci search is a comparison-based search algorithm that uses Fibonacci numbers to divide the array into sections. It's similar to binary search but avoids division operations, making it useful in systems where division is expensive.

## Algorithm Description

### Theory
Fibonacci search uses the Fibonacci sequence to create partition points in the array. The algorithm finds the smallest Fibonacci number greater than or equal to the array size and uses it to divide the search space.

### Mathematical Foundation
The Fibonacci sequence is defined as:
- F(0) = 0, F(1) = 1
- F(n) = F(n-1) + F(n-2) for n > 1

This creates natural partition points that efficiently divide the search space.

### Algorithm Steps
1. Generate Fibonacci numbers until F(k) ≥ n
2. Compare target with element at index F(k-2)
3. Adjust range based on comparison
4. Update Fibonacci numbers accordingly
5. Repeat until found or exhausted

### Pseudocode
```
FUNCTION fibonacciSearch(array, target):
    n = length(array)
    
    // Initialize Fibonacci numbers
    fibM2 = 0    // (k-2)th Fibonacci
    fibM1 = 1    // (k-1)th Fibonacci
    fibM = fibM2 + fibM1  // kth Fibonacci
    
    // Find smallest Fibonacci >= n
    WHILE fibM < n:
        fibM2 = fibM1
        fibM1 = fibM
        fibM = fibM2 + fibM1
    
    // Mark the eliminated range
    offset = -1
    
    WHILE fibM > 1:
        i = min(offset + fibM2, n - 1)
        
        IF array[i] < target:
            fibM = fibM1
            fibM1 = fibM2
            fibM2 = fibM - fibM1
            offset = i
        ELSE IF array[i] > target:
            fibM = fibM2
            fibM1 = fibM1 - fibM2
            fibM2 = fibM - fibM1
        ELSE:
            RETURN i
    
    // Check for last element
    IF fibM1 AND offset + 1 < n AND array[offset + 1] == target:
        RETURN offset + 1
    
    RETURN -1
```

## Complexity Analysis

### Time Complexity
- **Best Case**: O(1) - Target at first comparison
- **Average Case**: O(log n)
- **Worst Case**: O(log n)

### Space Complexity
- **Space**: O(1) - Only stores Fibonacci numbers

## Best Practices
- Use when division operations are expensive
- Suitable for embedded systems with limited arithmetic
- Provides similar performance to binary search
- Cache-friendly access pattern

## When to Use
- Systems where division is expensive
- Embedded systems with limited computational resources
- When cache performance is important
- Memory-constrained environments

## Variants

### 1. Standard Fibonacci Search
Basic implementation using Fibonacci sequence for partitioning.

### 2. Recursive Fibonacci Search
Recursive implementation for cleaner code structure.

### 3. Optimized Fibonacci Search
Optimized version with reduced calculations.

## Implementation Examples

### Example 1: Basic Fibonacci Search
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int fibonacciSearch(const std::vector<int>& arr, int target) {
    int n = arr.size();
    
    // Initialize Fibonacci numbers
    int fibM2 = 0;    // (k-2)th Fibonacci
    int fibM1 = 1;    // (k-1)th Fibonacci
    int fibM = fibM2 + fibM1;  // kth Fibonacci
    
    // Find smallest Fibonacci >= n
    while (fibM < n) {
        fibM2 = fibM1;
        fibM1 = fibM;
        fibM = fibM2 + fibM1;
    }
    
    // Mark the eliminated range
    int offset = -1;
    
    while (fibM > 1) {
        int i = std::min(offset + fibM2, n - 1);
        
        if (arr[i] < target) {
            fibM = fibM1;
            fibM1 = fibM2;
            fibM2 = fibM - fibM1;
            offset = i;
        } else if (arr[i] > target) {
            fibM = fibM2;
            fibM1 = fibM1 - fibM2;
            fibM2 = fibM - fibM1;
        } else {
            return i;
        }
    }
    
    // Check for last element
    if (fibM1 && offset + 1 < n && arr[offset + 1] == target) {
        return offset + 1;
    }
    
    return -1;
}
```

### Example 2: Fibonacci Search with Custom Comparator
```cpp
template<typename T, typename Compare>
int fibonacciSearch(const std::vector<T>& arr, const T& target, Compare comp) {
    int n = arr.size();
    
    int fibM2 = 0, fibM1 = 1, fibM = fibM2 + fibM1;
    
    while (fibM < n) {
        fibM2 = fibM1;
        fibM1 = fibM;
        fibM = fibM2 + fibM1;
    }
    
    int offset = -1;
    
    while (fibM > 1) {
        int i = std::min(offset + fibM2, n - 1);
        
        if (comp(arr[i], target)) {  // arr[i] < target
            fibM = fibM1;
            fibM1 = fibM2;
            fibM2 = fibM - fibM1;
            offset = i;
        } else if (comp(target, arr[i])) {  // target < arr[i]
            fibM = fibM2;
            fibM1 = fibM1 - fibM2;
            fibM2 = fibM - fibM1;
        } else {
            return i;
        }
    }
    
    if (fibM1 && offset + 1 < n && !comp(arr[offset + 1], target) && !comp(target, arr[offset + 1])) {
        return offset + 1;
    }
    
    return -1;
}
```

## Testing and Verification

### Test Cases
1. **Target at various positions**: Test beginning, middle, end
2. **Target not present**: Should return -1
3. **Single element array**: Edge case handling
4. **Empty array**: Should handle gracefully
5. **Large arrays**: Performance verification

### Performance Comparison
- Compare with binary search on various datasets
- Measure cache performance differences
- Test on systems with different division costs

## Common Pitfalls
1. Incorrect Fibonacci number generation
2. Off-by-one errors in index calculations
3. Not handling edge cases (empty array, single element)
4. Integer overflow with large arrays

## Optimization Tips
1. Pre-compute Fibonacci numbers for repeated searches
2. Use iterative approach to avoid stack overhead
3. Optimize for specific data sizes
4. Consider cache line boundaries

## Real-World Applications
- Embedded systems with limited FPU
- Database indexing systems
- File system searches
- Memory-constrained devices
- Real-time systems with predictable performance

## Advantages over Binary Search
1. No division operations
2. Better cache performance in some cases
3. Predictable memory access pattern
4. Suitable for hardware without division support

## Disadvantages
1. More complex implementation
2. Slightly more comparisons in some cases
3. Less intuitive than binary search
4. Requires Fibonacci number generation

## Related Algorithms
- Binary Search
- Golden Section Search
- Interpolation Search
- Exponential Search

## References
- The Art of Computer Programming (Donald Knuth)
- Introduction to Algorithms (CLRS)
- Fibonacci search optimization papers

---

*This implementation provides a comprehensive guide to Fibonacci search with practical examples and performance considerations.*
---

## Next Step

- Go to [07_Ternary_Search.md](07_Ternary_Search.md) to continue with Ternary Search.
