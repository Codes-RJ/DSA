# Ternary Search

## Overview
Ternary search is a divide-and-conquer search algorithm that divides the search space into three parts instead of two. It's particularly useful for finding the minimum or maximum of unimodal functions.

## Algorithm Description

### Theory
Ternary search works by repeatedly dividing the search interval into three equal parts and eliminating two-thirds of the search space in each iteration. For discrete arrays, it uses two mid points to partition the array.

### Mathematical Foundation
For a function f(x) that is unimodal (has a single minimum or maximum), ternary search can efficiently find the extremum by comparing function values at two points.

### Algorithm Steps
1. Divide array into three parts using two mid points
2. Compare target with both mid points
3. Eliminate two-thirds of the array based on comparisons
4. Repeat until found or search space is exhausted

### Pseudocode
```
FUNCTION ternarySearch(array, target):
    left = 0
    right = length(array) - 1
    
    WHILE left <= right:
        third = (right - left) / 3
        mid1 = left + third
        mid2 = right - third
        
        IF array[mid1] == target:
            RETURN mid1
        ELSE IF array[mid2] == target:
            RETURN mid2
        ELSE IF target < array[mid1]:
            right = mid1 - 1
        ELSE IF target > array[mid2]:
            left = mid2 + 1
        ELSE:
            left = mid1 + 1
            right = mid2 - 1
    
    RETURN -1
```

## Complexity Analysis

### Time Complexity
- **Best Case**: O(1) - Target at first comparison
- **Average Case**: O(log₃ n) ≈ O(log n)
- **Worst Case**: O(log₃ n) ≈ O(log n)

### Space Complexity
- **Space**: O(1) - Iterative implementation
- **Space**: O(log n) - Recursive implementation

## Best Practices
- Useful for finding peaks in unimodal functions
- More comparisons per iteration than binary search
- Better for functions with single peak/valley
- Not generally better than binary search for simple searching

## When to Use
- Finding maximum/minimum in unimodal functions
- Optimization problems with single extremum
- When function evaluation is expensive
- Peak detection algorithms

## Variants

### 1. Discrete Ternary Search
For searching in sorted arrays.

### 2. Continuous Ternary Search
For finding extrema in continuous functions.

### 3. Recursive Ternary Search
Recursive implementation for cleaner code.

## Implementation Examples

### Example 1: Discrete Ternary Search
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int ternarySearch(const std::vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    
    while (left <= right) {
        int third = (right - left) / 3;
        int mid1 = left + third;
        int mid2 = right - third;
        
        if (arr[mid1] == target) {
            return mid1;
        }
        
        if (arr[mid2] == target) {
            return mid2;
        }
        
        if (target < arr[mid1]) {
            right = mid1 - 1;
        } else if (target > arr[mid2]) {
            left = mid2 + 1;
        } else {
            left = mid1 + 1;
            right = mid2 - 1;
        }
    }
    
    return -1;
}

// Recursive version
int ternarySearchRecursive(const std::vector<int>& arr, int left, int right, int target) {
    if (left > right) {
        return -1;
    }
    
    int third = (right - left) / 3;
    int mid1 = left + third;
    int mid2 = right - third;
    
    if (arr[mid1] == target) {
        return mid1;
    }
    
    if (arr[mid2] == target) {
        return mid2;
    }
    
    if (target < arr[mid1]) {
        return ternarySearchRecursive(arr, left, mid1 - 1, target);
    } else if (target > arr[mid2]) {
        return ternarySearchRecursive(arr, mid2 + 1, right, target);
    } else {
        return ternarySearchRecursive(arr, mid1 + 1, mid2 - 1, target);
    }
}
```

### Example 2: Continuous Ternary Search for Function Optimization
```cpp
#include <cmath>
#include <functional>

double ternarySearchContinuous(std::function<double(double)> func, 
                              double left, double right, double epsilon = 1e-9) {
    while (right - left > epsilon) {
        double third = (right - left) / 3.0;
        double mid1 = left + third;
        double mid2 = right - third;
        
        if (func(mid1) < func(mid2)) {  // Finding minimum
            right = mid2;
        } else {
            left = mid1;
        }
    }
    
    return (left + right) / 2.0;
}

// Example usage: Find minimum of f(x) = x^2 - 4x + 3
double exampleFunction(double x) {
    return x * x - 4 * x + 3;
}

// Find minimum in range [0, 5]
double minimum = ternarySearchContinuous(exampleFunction, 0.0, 5.0);
```

### Example 3: Finding Maximum in Unimodal Array
```cpp
int findPeakElement(const std::vector<int>& arr) {
    int left = 0;
    int right = arr.size() - 1;
    
    while (left < right) {
        int third = (right - left) / 3;
        int mid1 = left + third;
        int mid2 = right - third;
        
        if (arr[mid1] < arr[mid2]) {
            // Peak is in the right part
            left = mid1 + 1;
        } else {
            // Peak is in the left part
            right = mid2 - 1;
        }
    }
    
    return left;
}
```

## Testing and Verification

### Test Cases
1. **Target at various positions**: Beginning, middle, end
2. **Target not present**: Should return -1
3. **Single element array**: Edge case
4. **Two element array**: Small array handling
5. **Large arrays**: Performance verification

### Function Optimization Tests
1. **Quadratic functions**: Should find exact minimum/maximum
2. **Higher-order polynomials**: Test convergence
3. **Non-differentiable functions**: Test robustness

## Common Pitfalls
1. Incorrect mid point calculations
2. Infinite loop with improper termination conditions
3. Not handling edge cases properly
4. Confusion between discrete and continuous versions

## Optimization Tips
1. Use appropriate termination criteria for continuous version
2. Consider numerical precision issues
3. Cache function evaluations in continuous search
4. Use iterative version to avoid stack overflow

## Real-World Applications
- Function optimization
- Peak detection in signal processing
- Machine learning hyperparameter tuning
- Economic optimization problems
- Engineering design optimization

## Comparison with Binary Search

### Advantages
1. Better for unimodal function optimization
2. Can find extrema without derivatives
3. Useful in optimization problems

### Disadvantages
1. More comparisons per iteration for discrete search
2. Not better than binary search for simple searching
3. More complex implementation
4. Less intuitive than binary search

## Mathematical Properties
- Convergence rate: O(log₃ n)
- Guaranteed convergence for unimodal functions
- Requires function to be unimodal for continuous version

## Related Algorithms
- Binary Search
- Golden Section Search
- Gradient Descent
- Newton's Method

## References
- Numerical Recipes
- Optimization algorithms textbooks
- ACM computational resources

---

*This implementation provides a comprehensive guide to ternary search with both discrete and continuous applications.*
---

## Next Step

- Go to [08_Sublist_Search.md](08_Sublist_Search.md) to continue with Sublist Search.
