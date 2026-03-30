# Bitonic Sort

## Overview
Bitonic Sort is a parallel sorting algorithm that works particularly well on parallel architectures. It sorts by creating bitonic sequences (sequences that are first increasing then decreasing) and then merging them.

## Algorithm Description

### Theory
A bitonic sequence is a sequence that is first monotonically increasing and then monotonically decreasing, or vice versa. Bitonic Sort works by:
1. Creating bitonic sequences
2. Merging bitonic sequences to create sorted sequences

The algorithm is naturally parallelizable as comparisons can be performed simultaneously on non-overlapping elements.

### Mathematical Foundation
- Bitonic sequence: First increasing, then decreasing (or vice versa)
- Bitonic merge: Sorts a bitonic sequence in O(log n) time
- Network depth: O(log² n) for complete sorting
- Comparators: O(n log² n) total comparisons

### Algorithm Steps
1. Build bitonic sequences recursively
2. Perform bitonic merge to sort sequences
3. Use compare-exchange operations
4. Continue until sequence is sorted

### Pseudocode
```
FUNCTION bitonicSort(array, low, cnt, direction):
    IF cnt > 1:
        k = cnt / 2
        bitonicSort(array, low, k, 1)        // Sort in ascending order
        bitonicSort(array, low + k, k, 0)    // Sort in descending order
        bitonicMerge(array, low, cnt, direction)

FUNCTION bitonicMerge(array, low, cnt, direction):
    IF cnt > 1:
        k = cnt / 2
        FOR i FROM low TO low + k - 1:
            compareAndSwap(array, i, i + k, direction)
        bitonicMerge(array, low, k, direction)
        bitonicMerge(array, low + k, k, direction)

FUNCTION compareAndSwap(array, i, j, direction):
    IF (direction == 1 AND array[i] > array[j]) OR 
       (direction == 0 AND array[i] < array[j]):
        swap(array[i], array[j])
```

## Complexity Analysis

### Time Complexity
- **Best Case**: O(log² n)
- **Average Case**: O(log² n)
- **Worst Case**: O(log² n)

### Space Complexity
- **Space**: O(log n) - Recursion stack

## Best Practices
- Excellent for parallel processing
- Fixed comparison network
- Predictable performance
- Good for hardware implementation

## When to Use
- Parallel computing systems
- GPU implementations
- Hardware sorting networks
- Real-time systems with predictable timing

## Implementation Examples

### Example 1: Basic Bitonic Sort
```cpp
#include <iostream>
#include <vector>
#include <cmath>

class BitonicSort {
private:
    static void compareAndSwap(std::vector<int>& arr, int i, int j, bool direction) {
        if ((direction && arr[i] > arr[j]) || (!direction && arr[i] < arr[j])) {
            std::swap(arr[i], arr[j]);
        }
    }
    
    static void bitonicMerge(std::vector<int>& arr, int low, int cnt, bool direction) {
        if (cnt > 1) {
            int k = cnt / 2;
            for (int i = low; i < low + k; i++) {
                compareAndSwap(arr, i, i + k, direction);
            }
            bitonicMerge(arr, low, k, direction);
            bitonicMerge(arr, low + k, k, direction);
        }
    }
    
    static void bitonicSortRecursive(std::vector<int>& arr, int low, int cnt, bool direction) {
        if (cnt > 1) {
            int k = cnt / 2;
            bitonicSortRecursive(arr, low, k, true);   // Ascending
            bitonicSortRecursive(arr, low + k, k, false); // Descending
            bitonicMerge(arr, low, cnt, direction);
        }
    }
    
public:
    static void sort(std::vector<int>& arr) {
        int n = arr.size();
        // Ensure n is a power of 2 by padding if necessary
        int nextPowerOf2 = 1;
        while (nextPowerOf2 < n) {
            nextPowerOf2 *= 2;
        }
        
        if (nextPowerOf2 != n) {
            // Pad with maximum value
            int maxVal = n > 0 ? *std::max_element(arr.begin(), arr.end()) : 0;
            arr.resize(nextPowerOf2, maxVal + 1);
        }
        
        bitonicSortRecursive(arr, 0, arr.size(), true);
        
        // Remove padding
        arr.resize(n);
    }
};
```

### Example 2: Iterative Bitonic Sort
```cpp
#include <vector>
#include <algorithm>

class IterativeBitonicSort {
public:
    static void sort(std::vector<int>& arr) {
        int n = arr.size();
        
        // Ensure n is a power of 2
        int nextPowerOf2 = 1;
        while (nextPowerOf2 < n) {
            nextPowerOf2 *= 2;
        }
        
        if (nextPowerOf2 != n) {
            int maxVal = n > 0 ? *std::max_element(arr.begin(), arr.end()) : 0;
            arr.resize(nextPowerOf2, maxVal + 1);
        }
        
        for (int size = 2; size <= n; size *= 2) {
            bool direction = (size == n);
            
            for (int stride = size / 2; stride > 0; stride /= 2) {
                for (int i = 0; i < n; i++) {
                    int partner = i ^ stride;
                    
                    if (partner > i) {
                        bool compareDirection = ((i & size) == 0);
                        
                        if (compareDirection && arr[i] > arr[partner]) {
                            std::swap(arr[i], arr[partner]);
                        } else if (!compareDirection && arr[i] < arr[partner]) {
                            std::swap(arr[i], arr[partner]);
                        }
                    }
                }
            }
        }
        
        // Remove padding
        arr.resize(n);
    }
};
```

### Example 3: Generic Bitonic Sort Template
```cpp
#include <vector>
#include <algorithm>

template<typename T>
class BitonicSortGeneric {
private:
    static void compareAndSwap(std::vector<T>& arr, int i, int j, bool direction) {
        if ((direction && arr[i] > arr[j]) || (!direction && arr[i] < arr[j])) {
            std::swap(arr[i], arr[j]);
        }
    }
    
    static void bitonicMerge(std::vector<T>& arr, int low, int cnt, bool direction) {
        if (cnt > 1) {
            int k = cnt / 2;
            for (int i = low; i < low + k; i++) {
                compareAndSwap(arr, i, i + k, direction);
            }
            bitonicMerge(arr, low, k, direction);
            bitonicMerge(arr, low + k, k, direction);
        }
    }
    
    static void bitonicSortRecursive(std::vector<T>& arr, int low, int cnt, bool direction) {
        if (cnt > 1) {
            int k = cnt / 2;
            bitonicSortRecursive(arr, low, k, true);
            bitonicSortRecursive(arr, low + k, k, false);
            bitonicMerge(arr, low, cnt, direction);
        }
    }
    
public:
    static void sort(std::vector<T>& arr) {
        int n = arr.size();
        int nextPowerOf2 = 1;
        while (nextPowerOf2 < n) {
            nextPowerOf2 *= 2;
        }
        
        if (nextPowerOf2 != n) {
            T maxVal = n > 0 ? *std::max_element(arr.begin(), arr.end()) : T();
            arr.resize(nextPowerOf2, maxVal);
        }
        
        bitonicSortRecursive(arr, 0, arr.size(), true);
        arr.resize(n);
    }
};
```

### Example 4: Bitonic Sort with Custom Comparator
```cpp
#include <vector>
#include <functional>

template<typename T, typename Compare = std::less<T>>
class BitonicSortCustom {
private:
    Compare comp;
    
    void compareAndSwap(std::vector<T>& arr, int i, int j, bool direction) {
        if ((direction && comp(arr[j], arr[i])) || (!direction && comp(arr[i], arr[j]))) {
            std::swap(arr[i], arr[j]);
        }
    }
    
    void bitonicMerge(std::vector<T>& arr, int low, int cnt, bool direction) {
        if (cnt > 1) {
            int k = cnt / 2;
            for (int i = low; i < low + k; i++) {
                compareAndSwap(arr, i, i + k, direction);
            }
            bitonicMerge(arr, low, k, direction);
            bitonicMerge(arr, low + k, k, direction);
        }
    }
    
    void bitonicSortRecursive(std::vector<T>& arr, int low, int cnt, bool direction) {
        if (cnt > 1) {
            int k = cnt / 2;
            bitonicSortRecursive(arr, low, k, true);
            bitonicSortRecursive(arr, low + k, k, false);
            bitonicMerge(arr, low, cnt, direction);
        }
    }
    
public:
    BitonicSortCustom(Compare c = Compare()) : comp(c) {}
    
    void sort(std::vector<T>& arr) {
        int n = arr.size();
        int nextPowerOf2 = 1;
        while (nextPowerOf2 < n) {
            nextPowerOf2 *= 2;
        }
        
        if (nextPowerOf2 != n) {
            T maxVal = n > 0 ? *std::max_element(arr.begin(), arr.end(), comp) : T();
            arr.resize(nextPowerOf2, maxVal);
        }
        
        bitonicSortRecursive(arr, 0, arr.size(), true);
        arr.resize(n);
    }
};
```

### Example 5: Bitonic Sort with Performance Analysis
```cpp
#include <vector>
#include <chrono>
#include <iostream>

class BitonicSortAnalyzer {
private:
    int comparisons = 0;
    int swaps = 0;
    int mergeOperations = 0;
    
    void compareAndSwap(std::vector<int>& arr, int i, int j, bool direction) {
        comparisons++;
        if ((direction && arr[i] > arr[j]) || (!direction && arr[i] < arr[j])) {
            std::swap(arr[i], arr[j]);
            swaps++;
        }
    }
    
    void bitonicMerge(std::vector<int>& arr, int low, int cnt, bool direction) {
        if (cnt > 1) {
            mergeOperations++;
            int k = cnt / 2;
            for (int i = low; i < low + k; i++) {
                compareAndSwap(arr, i, i + k, direction);
            }
            bitonicMerge(arr, low, k, direction);
            bitonicMerge(arr, low + k, k, direction);
        }
    }
    
    void bitonicSortRecursive(std::vector<int>& arr, int low, int cnt, bool direction) {
        if (cnt > 1) {
            int k = cnt / 2;
            bitonicSortRecursive(arr, low, k, true);
            bitonicSortRecursive(arr, low + k, k, false);
            bitonicMerge(arr, low, cnt, direction);
        }
    }
    
public:
    void sort(std::vector<int>& arr) {
        comparisons = 0;
        swaps = 0;
        mergeOperations = 0;
        
        int n = arr.size();
        int nextPowerOf2 = 1;
        while (nextPowerOf2 < n) {
            nextPowerOf2 *= 2;
        }
        
        if (nextPowerOf2 != n) {
            int maxVal = n > 0 ? *std::max_element(arr.begin(), arr.end()) : 0;
            arr.resize(nextPowerOf2, maxVal + 1);
        }
        
        auto startTime = std::chrono::high_resolution_clock::now();
        bitonicSortRecursive(arr, 0, arr.size(), true);
        auto endTime = std::chrono::high_resolution_clock::now();
        
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(
            endTime - startTime);
        
        std::cout << "Bitonic Sort Analysis:\n";
        std::cout << "Time: " << duration.count() << " microseconds\n";
        std::cout << "Comparisons: " << comparisons << "\n";
        std::cout << "Swaps: " << swaps << "\n";
        std::cout << "Merge Operations: " << mergeOperations << "\n";
        
        arr.resize(n);
    }
};
```

## Testing and Verification

### Test Cases
1. **Power of 2 size arrays**: Optimal performance
2. **Non-power of 2 size**: Should handle padding correctly
3. **Already sorted array**: Should maintain order
4. **Reverse sorted array**: Should sort correctly
5. **Random array**: Should sort correctly

### Performance Tests
1. **Parallel vs sequential**: Performance comparison
2. **Different array sizes**: Scalability analysis
3. **Comparison with other parallel sorts**: Relative performance
4. **Network depth analysis**: Verify O(log² n) complexity

## Common Pitfalls
1. Not handling non-power-of-2 array sizes
2. Incorrect bitonic merge implementation
3. Wrong direction handling in compare-swap
4. Stack overflow with deep recursion

## Optimization Tips
1. Use iterative implementation to avoid recursion
2. Optimize for specific hardware architectures
3. Use SIMD operations for compare-swap operations
4. Consider cache performance in implementation

## Real-World Applications
- Parallel computing systems
- GPU sorting implementations
- Hardware sorting networks
- Real-time signal processing
- Database parallel sorting

## Advantages
- Naturally parallelizable
- Fixed comparison network
- Predictable performance
- Good for hardware implementation

## Disadvantages
- Requires power-of-2 array size (or padding)
- More comparisons than some other algorithms
- Complex implementation
- Not cache-friendly for large arrays

## Parallel Processing Benefits

### Network Properties
- Fixed depth sorting network
- Deterministic comparison pattern
- No data dependencies in parallel stages
- Suitable for hardware implementation

### GPU Implementation
- Excellent fit for GPU architecture
- Can utilize thousands of threads
- Memory access patterns are predictable
- High throughput for large datasets

## Related Algorithms
- Odd-Even Merge Sort
- Batcher's Odd-Even Merge Network
- Parallel sorting networks
- Merge Sort

## References
- Parallel Computer Architecture
- Sorting Networks (Knuth)
- GPU Computing documentation
- Parallel Algorithm Design

---

*This implementation provides a comprehensive guide to Bitonic Sort with parallel processing capabilities and hardware optimization strategies.*
