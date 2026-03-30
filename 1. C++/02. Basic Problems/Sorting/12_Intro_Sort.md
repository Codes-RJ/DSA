# Intro Sort

## Overview
Intro Sort (Introspective Sort) is a hybrid sorting algorithm that combines quick sort, heap sort, and insertion sort to provide optimal performance with guaranteed O(n log n) worst-case complexity. It's the algorithm used in C++'s `std::sort`.

## Algorithm Description

### Theory
Intro Sort starts with quick sort but switches to heap sort when the recursion depth exceeds a certain threshold (typically 2 × log n). For small subarrays, it uses insertion sort for better performance.

### Mathematical Foundation
- Recursion depth limit: 2 × log n
- Switch threshold: prevents quick sort's O(n²) worst case
- Small array threshold: typically 16 elements for insertion sort
- Guaranteed O(n log n) complexity through hybrid approach

### Algorithm Steps
1. Start with quick sort
2. Monitor recursion depth
3. Switch to heap sort if depth > 2 × log n
4. Use insertion sort for small subarrays

### Pseudocode
```
FUNCTION introSort(array, maxDepth):
    n = length(array)
    
    IF n <= 16:
        insertionSort(array)
    ELSE IF maxDepth == 0:
        heapSort(array)
    ELSE:
        pivotIndex = partition(array)
        introSort(left part, maxDepth - 1)
        introSort(right part, maxDepth - 1)

FUNCTION introSortMain(array):
    maxDepth = 2 * floor(log2(length(array)))
    introSort(array, maxDepth)
```

## Complexity Analysis

### Time Complexity
- **Best Case**: O(n log n)
- **Average Case**: O(n log n)
- **Worst Case**: O(n log n) - Guaranteed

### Space Complexity
- **Space**: O(log n) - Recursion stack

## Best Practices
- Used in C++ STL sort implementation
- Guarantees worst-case performance
- Combines advantages of multiple algorithms
- Excellent general-purpose sorter

## When to Use
- General-purpose sorting
- When worst-case guarantee is required
- Large datasets
- Production systems

## Implementation Examples

### Example 1: Basic Intro Sort Implementation
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

class IntroSort {
private:
    static const int INSERTION_SORT_THRESHOLD = 16;
    
    static void insertionSort(std::vector<int>& arr, int left, int right) {
        for (int i = left + 1; i <= right; i++) {
            int key = arr[i];
            int j = i - 1;
            
            while (j >= left && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }
    
    static int partition(std::vector<int>& arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;
        
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                std::swap(arr[i], arr[j]);
            }
        }
        std::swap(arr[i + 1], arr[high]);
        return i + 1;
    }
    
    static void heapify(std::vector<int>& arr, int n, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        
        if (left < n && arr[left] > arr[largest])
            largest = left;
        
        if (right < n && arr[right] > arr[largest])
            largest = right;
        
        if (largest != i) {
            std::swap(arr[i], arr[largest]);
            heapify(arr, n, largest);
        }
    }
    
    static void heapSort(std::vector<int>& arr, int left, int right) {
        int n = right - left + 1;
        
        // Build heap
        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(arr, n, i);
        
        // Extract elements from heap
        for (int i = n - 1; i > 0; i--) {
            std::swap(arr[0], arr[i]);
            heapify(arr, i, 0);
        }
    }
    
    static void introSortUtil(std::vector<int>& arr, int left, int right, int depthLimit) {
        int size = right - left + 1;
        
        if (size <= INSERTION_SORT_THRESHOLD) {
            insertionSort(arr, left, right);
            return;
        }
        
        if (depthLimit == 0) {
            heapSort(arr, left, right);
            return;
        }
        
        int pivotIndex = partition(arr, left, right);
        introSortUtil(arr, left, pivotIndex - 1, depthLimit - 1);
        introSortUtil(arr, pivotIndex + 1, right, depthLimit - 1);
    }
    
    static int calculateDepthLimit(int n) {
        return 2 * static_cast<int>(std::log2(n));
    }
    
public:
    static void sort(std::vector<int>& arr) {
        if (arr.empty()) return;
        
        int depthLimit = calculateDepthLimit(arr.size());
        introSortUtil(arr, 0, arr.size() - 1, depthLimit);
    }
};
```

### Example 2: Optimized Intro Sort with Median-of-Three Pivot
```cpp
#include <vector>
#include <algorithm>

class OptimizedIntroSort {
private:
    static const int INSERTION_SORT_THRESHOLD = 16;
    
    static void insertionSort(std::vector<int>& arr, int left, int right) {
        for (int i = left + 1; i <= right; i++) {
            int key = arr[i];
            int j = i - 1;
            
            while (j >= left && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }
    
    // Median-of-three pivot selection
    static int medianOfThree(std::vector<int>& arr, int left, int right) {
        int mid = left + (right - left) / 2;
        
        // Sort left, mid, right
        if (arr[left] > arr[mid])
            std::swap(arr[left], arr[mid]);
        if (arr[left] > arr[right])
            std::swap(arr[left], arr[right]);
        if (arr[mid] > arr[right])
            std::swap(arr[mid], arr[right]);
        
        // Place pivot at right-1
        std::swap(arr[mid], arr[right - 1]);
        return right - 1;
    }
    
    static int partition(std::vector<int>& arr, int left, int right) {
        int pivotIndex = medianOfThree(arr, left, right);
        int pivot = arr[pivotIndex];
        int i = left;
        int j = right - 1;
        
        while (true) {
            while (arr[++i] < pivot);
            while (arr[--j] > pivot);
            
            if (i < j) {
                std::swap(arr[i], arr[j]);
            } else {
                break;
            }
        }
        
        // Restore pivot
        std::swap(arr[i], arr[right - 1]);
        return i;
    }
    
    static void heapify(std::vector<int>& arr, int n, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        
        if (left < n && arr[left] > arr[largest])
            largest = left;
        
        if (right < n && arr[right] > arr[largest])
            largest = right;
        
        if (largest != i) {
            std::swap(arr[i], arr[largest]);
            heapify(arr, n, largest);
        }
    }
    
    static void heapSort(std::vector<int>& arr, int left, int right) {
        int n = right - left + 1;
        
        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(arr, n, i);
        
        for (int i = n - 1; i > 0; i--) {
            std::swap(arr[0], arr[i]);
            heapify(arr, i, 0);
        }
    }
    
    static void introSortUtil(std::vector<int>& arr, int left, int right, int depthLimit) {
        int size = right - left + 1;
        
        if (size <= INSERTION_SORT_THRESHOLD) {
            insertionSort(arr, left, right);
            return;
        }
        
        if (depthLimit == 0) {
            heapSort(arr, left, right);
            return;
        }
        
        int pivotIndex = partition(arr, left, right);
        introSortUtil(arr, left, pivotIndex - 1, depthLimit - 1);
        introSortUtil(arr, pivotIndex + 1, right, depthLimit - 1);
    }
    
public:
    static void sort(std::vector<int>& arr) {
        if (arr.size() <= 1) return;
        
        int depthLimit = 2 * static_cast<int>(std::log2(arr.size()));
        introSortUtil(arr, 0, arr.size() - 1, depthLimit);
    }
};
```

### Example 3: Generic Intro Sort Template
```cpp
#include <vector>
#include <algorithm>
#include <cmath>

template<typename T>
class IntroSortGeneric {
private:
    static const int INSERTION_SORT_THRESHOLD = 16;
    
    static void insertionSort(std::vector<T>& arr, int left, int right) {
        for (int i = left + 1; i <= right; i++) {
            T key = arr[i];
            int j = i - 1;
            
            while (j >= left && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }
    
    static int partition(std::vector<T>& arr, int low, int high) {
        T pivot = arr[high];
        int i = low - 1;
        
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                std::swap(arr[i], arr[j]);
            }
        }
        std::swap(arr[i + 1], arr[high]);
        return i + 1;
    }
    
    static void heapify(std::vector<T>& arr, int n, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        
        if (left < n && arr[left] > arr[largest])
            largest = left;
        
        if (right < n && arr[right] > arr[largest])
            largest = right;
        
        if (largest != i) {
            std::swap(arr[i], arr[largest]);
            heapify(arr, n, largest);
        }
    }
    
    static void heapSort(std::vector<T>& arr, int left, int right) {
        int n = right - left + 1;
        
        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(arr, n, i);
        
        for (int i = n - 1; i > 0; i--) {
            std::swap(arr[0], arr[i]);
            heapify(arr, i, 0);
        }
    }
    
    static void introSortUtil(std::vector<T>& arr, int left, int right, int depthLimit) {
        int size = right - left + 1;
        
        if (size <= INSERTION_SORT_THRESHOLD) {
            insertionSort(arr, left, right);
            return;
        }
        
        if (depthLimit == 0) {
            heapSort(arr, left, right);
            return;
        }
        
        int pivotIndex = partition(arr, left, right);
        introSortUtil(arr, left, pivotIndex - 1, depthLimit - 1);
        introSortUtil(arr, pivotIndex + 1, right, depthLimit - 1);
    }
    
    static int calculateDepthLimit(int n) {
        return 2 * static_cast<int>(std::log2(n));
    }
    
public:
    static void sort(std::vector<T>& arr) {
        if (arr.size() <= 1) return;
        
        int depthLimit = calculateDepthLimit(arr.size());
        introSortUtil(arr, 0, arr.size() - 1, depthLimit);
    }
};
```

### Example 4: Intro Sort with Custom Comparator
```cpp
#include <vector>
#include <functional>

template<typename T, typename Compare = std::less<T>>
class IntroSortCustom {
private:
    static const int INSERTION_SORT_THRESHOLD = 16;
    
    Compare comp;
    
    void insertionSort(std::vector<T>& arr, int left, int right) {
        for (int i = left + 1; i <= right; i++) {
            T key = arr[i];
            int j = i - 1;
            
            while (j >= left && comp(key, arr[j])) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }
    
    int partition(std::vector<T>& arr, int low, int high) {
        T pivot = arr[high];
        int i = low - 1;
        
        for (int j = low; j < high; j++) {
            if (!comp(pivot, arr[j])) {  // arr[j] <= pivot
                i++;
                std::swap(arr[i], arr[j]);
            }
        }
        std::swap(arr[i + 1], arr[high]);
        return i + 1;
    }
    
    void heapify(std::vector<T>& arr, int n, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        
        if (left < n && comp(arr[largest], arr[left]))
            largest = left;
        
        if (right < n && comp(arr[largest], arr[right]))
            largest = right;
        
        if (largest != i) {
            std::swap(arr[i], arr[largest]);
            heapify(arr, n, largest);
        }
    }
    
    void heapSort(std::vector<T>& arr, int left, int right) {
        int n = right - left + 1;
        
        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(arr, n, i);
        
        for (int i = n - 1; i > 0; i--) {
            std::swap(arr[0], arr[i]);
            heapify(arr, i, 0);
        }
    }
    
    void introSortUtil(std::vector<T>& arr, int left, int right, int depthLimit) {
        int size = right - left + 1;
        
        if (size <= INSERTION_SORT_THRESHOLD) {
            insertionSort(arr, left, right);
            return;
        }
        
        if (depthLimit == 0) {
            heapSort(arr, left, right);
            return;
        }
        
        int pivotIndex = partition(arr, left, right);
        introSortUtil(arr, left, pivotIndex - 1, depthLimit - 1);
        introSortUtil(arr, pivotIndex + 1, right, depthLimit - 1);
    }
    
    int calculateDepthLimit(int n) {
        return 2 * static_cast<int>(std::log2(n));
    }
    
public:
    IntroSortCustom(Compare c = Compare()) : comp(c) {}
    
    void sort(std::vector<T>& arr) {
        if (arr.size() <= 1) return;
        
        int depthLimit = calculateDepthLimit(arr.size());
        introSortUtil(arr, 0, arr.size() - 1, depthLimit);
    }
};
```

## Testing and Verification

### Test Cases
1. **Random data**: Should perform as well as quick sort
2. **Sorted data**: Should handle efficiently
3. **Reverse sorted data**: Should switch to heap sort
4. **Small arrays**: Should use insertion sort
5. **Duplicate elements**: Should handle correctly

### Performance Tests
1. **Worst-case scenarios**: Verify O(n log n) guarantee
2. **Depth limit testing**: Ensure proper algorithm switching
3. **Comparison with std::sort**: Should be comparable
4. **Memory usage**: Verify O(log n) space complexity

## Common Pitfalls
1. Incorrect depth limit calculation
2. Improper pivot selection
3. Not handling small arrays efficiently
4. Memory leaks in recursive implementation

## Optimization Tips
1. Use median-of-three pivot selection
2. Optimize insertion sort threshold
3. Consider iterative implementation to avoid stack overflow
4. Use SIMD operations where possible

## Real-World Applications
- C++ Standard Library (std::sort)
- Production sorting systems
- Database management systems
- Scientific computing applications
- Game development engines

## Advantages
- Guaranteed O(n log n) performance
- Combines strengths of multiple algorithms
- Excellent average-case performance
- Widely tested and optimized

## Disadvantages
- More complex implementation
- Slightly higher constant factors
- Not stable by default
- Requires careful parameter tuning

## Related Algorithms
- Quick Sort
- Heap Sort
- Insertion Sort
- Tim Sort
- Merge Sort

## References
- C++ Standard Library implementation
- Musser's Introspective Sorting paper
- Algorithm Design Manual
- Introduction to Algorithms (CLRS)

---

*This implementation provides a comprehensive guide to Intro Sort with guaranteed worst-case performance and hybrid optimization strategies.*
