# Pancake Sort

## Overview
Pancake Sort is a sorting algorithm that uses only the operation of flipping (reversing) prefixes of the array, similar to flipping a stack of pancakes with a spatula. It's the only sorting algorithm that uses this unique operation.

## Algorithm Description

### Theory
Pancake Sort works by repeatedly bringing the largest unsorted element to the front (through a flip), then moving it to its correct position at the end (through another flip). This process is repeated until the array is sorted.

### Algorithm Steps
1. Find the maximum element in the unsorted portion
2. Flip the array to bring the maximum to the front
3. Flip the unsorted portion to move the maximum to its correct position
4. Reduce the unsorted portion size by 1
5. Repeat until the array is sorted

### Pseudocode
```
FUNCTION pancakeSort(array):
    n = length(array)
    
    FOR currentSize FROM n DOWNTO 1:
        // Find index of maximum element in array[0...currentSize-1]
        maxIndex = findMaxIndex(array, currentSize)
        
        // If max is not at its correct position
        IF maxIndex != currentSize - 1:
            // If max is not at front, bring it to front
            IF maxIndex != 0:
                flip(array, maxIndex + 1)
            
            // Move max to its correct position
            flip(array, currentSize)

FUNCTION flip(array, k):
    // Reverse first k elements
    left = 0
    right = k - 1
    WHILE left < right:
        swap(array[left], array[right])
        left++
        right--
```

## Complexity Analysis

### Time Complexity
- **Best Case**: O(n) - Already sorted
- **Average Case**: O(n²)
- **Worst Case**: O(n²)

### Space Complexity
- **Space**: O(1) - In-place sorting

## Best Practices
- Unique flip operation makes it interesting for puzzles
- Educational value in understanding sorting concepts
- Useful for problems with restricted operations
- Simple to understand and implement

## When to Use
- Educational purposes
- Problems with flip/reverse operations only
- Algorithm puzzles and challenges
- Understanding sorting fundamentals

## Implementation Examples

### Example 1: Basic Pancake Sort
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

class PancakeSort {
private:
    static void flip(std::vector<int>& arr, int k) {
        // Reverse first k elements
        std::reverse(arr.begin(), arr.begin() + k);
    }
    
    static int findMaxIndex(const std::vector<int>& arr, int n) {
        int maxIndex = 0;
        for (int i = 1; i < n; i++) {
            if (arr[i] > arr[maxIndex]) {
                maxIndex = i;
            }
        }
        return maxIndex;
    }
    
public:
    static void sort(std::vector<int>& arr) {
        int n = arr.size();
        
        for (int currentSize = n; currentSize > 1; currentSize--) {
            // Find index of maximum element in array[0...currentSize-1]
            int maxIndex = findMaxIndex(arr, currentSize);
            
            // If max is not at its correct position
            if (maxIndex != currentSize - 1) {
                // If max is not at front, bring it to front
                if (maxIndex != 0) {
                    flip(arr, maxIndex + 1);
                }
                
                // Move max to its correct position
                flip(arr, currentSize);
            }
        }
    }
};
```

### Example 2: Pancake Sort with Flip Tracking
```cpp
#include <vector>
#include <algorithm>

class PancakeSortWithTracking {
private:
    std::vector<int> flipSequence;
    
    void flip(std::vector<int>& arr, int k) {
        std::reverse(arr.begin(), arr.begin() + k);
        flipSequence.push_back(k);
    }
    
    int findMaxIndex(const std::vector<int>& arr, int n) {
        int maxIndex = 0;
        for (int i = 1; i < n; i++) {
            if (arr[i] > arr[maxIndex]) {
                maxIndex = i;
            }
        }
        return maxIndex;
    }
    
public:
    void sort(std::vector<int>& arr) {
        flipSequence.clear();
        int n = arr.size();
        
        for (int currentSize = n; currentSize > 1; currentSize--) {
            int maxIndex = findMaxIndex(arr, currentSize);
            
            if (maxIndex != currentSize - 1) {
                if (maxIndex != 0) {
                    flip(arr, maxIndex + 1);
                }
                flip(arr, currentSize);
            }
        }
    }
    
    const std::vector<int>& getFlipSequence() const {
        return flipSequence;
    }
    
    void printFlipSequence() const {
        std::cout << "Flip sequence: ";
        for (int flip : flipSequence) {
            std::cout << flip << " ";
        }
        std::cout << std::endl;
    }
};
```

### Example 3: Optimized Pancake Sort
```cpp
#include <vector>
#include <algorithm>

class OptimizedPancakeSort {
private:
    void flip(std::vector<int>& arr, int k) {
        std::reverse(arr.begin(), arr.begin() + k);
    }
    
    int findMaxIndex(const std::vector<int>& arr, int n) {
        return std::max_element(arr.begin(), arr.begin() + n) - arr.begin();
    }
    
    bool isSorted(const std::vector<int>& arr, int n) {
        for (int i = 0; i < n - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                return false;
            }
        }
        return true;
    }
    
public:
    void sort(std::vector<int>& arr) {
        int n = arr.size();
        
        for (int currentSize = n; currentSize > 1; currentSize--) {
            // Early termination if already sorted
            if (isSorted(arr, currentSize)) {
                break;
            }
            
            int maxIndex = findMaxIndex(arr, currentSize);
            
            if (maxIndex != currentSize - 1) {
                if (maxIndex != 0) {
                    flip(arr, maxIndex + 1);
                }
                flip(arr, currentSize);
            }
        }
    }
};
```

### Example 4: Generic Pancake Sort Template
```cpp
#include <vector>
#include <algorithm>

template<typename T>
class PancakeSortGeneric {
private:
    static void flip(std::vector<T>& arr, int k) {
        std::reverse(arr.begin(), arr.begin() + k);
    }
    
    static int findMaxIndex(const std::vector<T>& arr, int n) {
        return std::max_element(arr.begin(), arr.begin() + n) - arr.begin();
    }
    
public:
    static void sort(std::vector<T>& arr) {
        int n = arr.size();
        
        for (int currentSize = n; currentSize > 1; currentSize--) {
            int maxIndex = findMaxIndex(arr, currentSize);
            
            if (maxIndex != currentSize - 1) {
                if (maxIndex != 0) {
                    flip(arr, maxIndex + 1);
                }
                flip(arr, currentSize);
            }
        }
    }
};
```

### Example 5: Pancake Sort with Custom Comparator
```cpp
#include <vector>
#include <algorithm>
#include <functional>

template<typename T, typename Compare = std::less<T>>
class PancakeSortCustom {
private:
    Compare comp;
    
    void flip(std::vector<T>& arr, int k) {
        std::reverse(arr.begin(), arr.begin() + k);
    }
    
    int findMaxIndex(const std::vector<T>& arr, int n) {
        int maxIndex = 0;
        for (int i = 1; i < n; i++) {
            if (comp(arr[maxIndex], arr[i])) {  // arr[i] > arr[maxIndex]
                maxIndex = i;
            }
        }
        return maxIndex;
    }
    
public:
    PancakeSortCustom(Compare c = Compare()) : comp(c) {}
    
    void sort(std::vector<T>& arr) {
        int n = arr.size();
        
        for (int currentSize = n; currentSize > 1; currentSize--) {
            int maxIndex = findMaxIndex(arr, currentSize);
            
            if (maxIndex != currentSize - 1) {
                if (maxIndex != 0) {
                    flip(arr, maxIndex + 1);
                }
                flip(arr, currentSize);
            }
        }
    }
};
```

### Example 6: Pancake Sort with Performance Analysis
```cpp
#include <vector>
#include <algorithm>
#include <chrono>
#include <iostream>

class PancakeSortAnalyzer {
private:
    int flips = 0;
    int comparisons = 0;
    int maxSearches = 0;
    
    void flip(std::vector<int>& arr, int k) {
        std::reverse(arr.begin(), arr.begin() + k);
        flips++;
    }
    
    int findMaxIndex(const std::vector<int>& arr, int n) {
        maxSearches++;
        int maxIndex = 0;
        for (int i = 1; i < n; i++) {
            comparisons++;
            if (arr[i] > arr[maxIndex]) {
                maxIndex = i;
            }
        }
        return maxIndex;
    }
    
public:
    void sort(std::vector<int>& arr) {
        flips = 0;
        comparisons = 0;
        maxSearches = 0;
        
        auto startTime = std::chrono::high_resolution_clock::now();
        
        int n = arr.size();
        for (int currentSize = n; currentSize > 1; currentSize--) {
            int maxIndex = findMaxIndex(arr, currentSize);
            
            if (maxIndex != currentSize - 1) {
                if (maxIndex != 0) {
                    flip(arr, maxIndex + 1);
                }
                flip(arr, currentSize);
            }
        }
        
        auto endTime = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(
            endTime - startTime);
        
        std::cout << "Pancake Sort Analysis:\n";
        std::cout << "Time: " << duration.count() << " microseconds\n";
        std::cout << "Flips: " << flips << "\n";
        std::cout << "Comparisons: " << comparisons << "\n";
        std::cout << "Max searches: " << maxSearches << "\n";
        std::cout << "Average flips per element: " << static_cast<double>(flips) / n << "\n";
    }
};
```

## Testing and Verification

### Test Cases
1. **Already sorted array**: Should use minimal flips
2. **Reverse sorted array**: Should use maximum flips
3. **Random array**: Should sort correctly
4. **Single element**: Should handle edge case
5. **Empty array**: Should handle gracefully

### Performance Tests
1. **Flip count analysis**: Verify optimal flip usage
2. **Comparison with other sorts**: Relative performance
3. **Worst-case scenarios**: Reverse sorted arrays
4. **Best-case scenarios**: Already sorted arrays

## Common Pitfalls
1. Incorrect flip implementation
2. Off-by-one errors in max index calculation
3. Not handling edge cases properly
4. Inefficient max element search

## Optimization Tips
1. Use early termination for sorted portions
2. Optimize max element search
3. Consider cache performance in flip operations
4. Use efficient reverse operations

## Real-World Applications
- Algorithm puzzles and challenges
- Educational purposes
- Problems with restricted operations
- Robotics (stack manipulation)
- DNA sequence analysis

## Advantages
- Unique flip operation
- Simple to understand
- Educational value
- Works with restricted operations

## Disadvantages
- O(n²) time complexity
- Not practical for large datasets
- Limited real-world applications
- Outperformed by conventional sorts

## Mathematical Properties

### Maximum Number of Flips
- Worst case: 2n - 3 flips
- Best case: 0 flips (already sorted)
- Average case: approximately 1.5n flips

### Burnt Pancake Problem
- Variation where pancakes are burnt on one side
- Requires additional constraints
- More complex algorithm needed

## Related Algorithms
- Reversal Sort
- Sorting by reversals
- Genome rearrangement algorithms
- Permutation sorting

## References
- Algorithm puzzles and challenges
- Computational geometry literature
- Permutation group theory
- Educational computer science resources

---

*This implementation provides a comprehensive guide to Pancake Sort with its unique flip-based approach and educational value.*
