# Tim Sort

## Overview
Tim Sort is a hybrid stable sorting algorithm derived from merge sort and insertion sort, designed to perform well on real-world data. It's the default sorting algorithm in Python and Java.

## Algorithm Description

### Theory
Tim Sort exploits existing order in data by identifying natural runs (already sorted sequences) and merging them efficiently. It combines the speed of merge sort with the efficiency of insertion sort for small runs.

### Mathematical Foundation
- Natural runs: Existing sorted sequences in the data
- Run size: Typically 32-64 elements
- Merge invariants: Maintain balance between runs
- Galloping mode: Optimized merging for already-merged data

### Algorithm Steps
1. Identify natural runs in data
2. Sort small runs using insertion sort
3. Merge runs using merge sort
4. Maintain merge balance with invariants

### Pseudocode
```
FUNCTION timSort(array):
    n = length(array)
    MIN_RUN = 32
    
    // Sort individual runs using insertion sort
    FOR i FROM 0 TO n - 1 STEP MIN_RUN:
        insertionSort(array, i, min(i + MIN_RUN - 1, n - 1))
    
    // Merge runs
    FOR size FROM MIN_RUN; size < n; size *= 2:
        FOR left FROM 0 TO n - 1; left += 2 * size:
            mid = left + size - 1
            right = min(left + 2 * size - 1, n - 1)
            
            IF mid < right:
                merge(array, left, mid, right)
```

## Complexity Analysis

### Time Complexity
- **Best Case**: O(n) - Already sorted
- **Average Case**: O(n log n)
- **Worst Case**: O(n log n)

### Space Complexity
- **Space**: O(n) - For temporary arrays during merge

## Best Practices
- Excellent for real-world data with partial order
- Stable sorting algorithm
- Adaptive to existing order
- Optimized for partial sorting

## When to Use
- Real-world data with partial order
- When stability is required
- Large datasets
- General-purpose sorting

## Implementation Examples

### Example 1: Basic Tim Sort Implementation
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

class TimSort {
private:
    static const int MIN_MERGE = 32;
    
    static int minRunLength(int n) {
        int r = 0;
        while (n >= MIN_MERGE) {
            r |= (n & 1);
            n >>= 1;
        }
        return n + r;
    }
    
    static void insertionSort(std::vector<int>& arr, int left, int right) {
        for (int i = left + 1; i <= right; i++) {
            int temp = arr[i];
            int j = i - 1;
            
            while (j >= left && arr[j] > temp) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = temp;
        }
    }
    
    static void merge(std::vector<int>& arr, int l, int m, int r) {
        int len1 = m - l + 1, len2 = r - m;
        std::vector<int> left(len1), right(len2);
        
        for (int i = 0; i < len1; i++)
            left[i] = arr[l + i];
        for (int i = 0; i < len2; i++)
            right[i] = arr[m + 1 + i];
        
        int i = 0, j = 0, k = l;
        
        while (i < len1 && j < len2) {
            if (left[i] <= right[j]) {
                arr[k] = left[i];
                i++;
            } else {
                arr[k] = right[j];
                j++;
            }
            k++;
        }
        
        while (i < len1) {
            arr[k] = left[i];
            k++;
            i++;
        }
        
        while (j < len2) {
            arr[k] = right[j];
            k++;
            j++;
        }
    }
    
public:
    static void sort(std::vector<int>& arr) {
        int n = arr.size();
        int minRun = minRunLength(n);
        
        // Sort individual subarrays of size MIN_MERGE
        for (int i = 0; i < n; i += minRun) {
            insertionSort(arr, i, std::min((i + MIN_MERGE - 1), (n - 1)));
        }
        
        // Start merging from size MIN_MERGE
        for (int size = minRun; size < n; size = 2 * size) {
            for (int left = 0; left < n; left += 2 * size) {
                int mid = left + size - 1;
                int right = std::min((left + 2 * size - 1), (n - 1));
                
                if (mid < right) {
                    merge(arr, left, mid, right);
                }
            }
        }
    }
};
```

### Example 2: Tim Sort with Galloping Mode
```cpp
#include <vector>
#include <algorithm>

class TimSortAdvanced {
private:
    static const int MIN_MERGE = 32;
    static const int GALLOPING_THRESHOLD = 7;
    
    struct Run {
        int start;
        int length;
        
        Run(int s, int l) : start(s), length(l) {}
    };
    
    std::vector<Run> runs;
    
    int countRunAndMakeAscending(std::vector<int>& arr, int low, int high) {
        int runHi = low + 1;
        
        if (runHi == high) {
            return 1;
        }
        
        if (arr[runHi] < arr[low]) {
            // Descending run
            while (runHi < high && arr[runHi] < arr[runHi - 1]) {
                runHi++;
            }
            std::reverse(arr.begin() + low, arr.begin() + runHi);
        } else {
            // Ascending run
            while (runHi < high && arr[runHi] >= arr[runHi - 1]) {
                runHi++;
            }
        }
        
        return runHi - low;
    }
    
    void mergeCollapse(std::vector<int>& arr) {
        while (runs.size() > 1) {
            int n = runs.size() - 2;
            
            if (n > 0 && runs[n-1].length <= runs[n].length + runs[n+1].length) {
                if (runs[n-1].length < runs[n+1].length) {
                    n--;
                }
                mergeAt(arr, n);
            } else if (runs[n].length <= runs[n+1].length) {
                mergeAt(arr, n);
            } else {
                break;
            }
        }
    }
    
    void mergeAt(std::vector<int>& arr, int i) {
        int base1 = runs[i].start;
        int len1 = runs[i].length;
        int base2 = runs[i+1].start;
        int len2 = runs[i+1].length;
        
        runs[i].length = len1 + len2;
        
        if (i + 2 < runs.size()) {
            runs[i+1] = runs[i+2];
            runs.pop_back();
        } else {
            runs.pop_back();
        }
        
        merge(arr, base1, base1 + len1 - 1, base2 + len2 - 1);
    }
    
    void merge(std::vector<int>& arr, int lo, int mid, int hi) {
        std::vector<int> temp(arr.begin() + lo, arr.begin() + hi + 1);
        int i = 0, j = mid - lo + 1, k = lo;
        
        while (i <= mid - lo && j <= hi - lo) {
            if (temp[i] <= temp[j]) {
                arr[k++] = temp[i++];
            } else {
                arr[k++] = temp[j++];
            }
        }
        
        while (i <= mid - lo) {
            arr[k++] = temp[i++];
        }
    }
    
public:
    void sort(std::vector<int>& arr) {
        int n = arr.size();
        int minRun = MIN_MERGE;
        
        for (int i = 0; i < n; ) {
            int runLen = countRunAndMakeAscending(arr, i, n);
            
            if (runLen < minRun) {
                int force = std::min(n, i + minRun);
                int insertionSort(arr, i, force - 1);
                runLen = force - i;
            }
            
            runs.emplace_back(i, runLen);
            i += runLen;
            mergeCollapse(arr);
        }
        
        // Merge remaining runs
        while (runs.size() > 1) {
            mergeAt(arr, runs.size() - 2);
        }
    }
    
private:
    void insertionSort(std::vector<int>& arr, int left, int right) {
        for (int i = left + 1; i <= right; i++) {
            int temp = arr[i];
            int j = i - 1;
            
            while (j >= left && arr[j] > temp) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = temp;
        }
    }
};
```

### Example 3: Generic Tim Sort Template
```cpp
template<typename T>
class TimSortGeneric {
private:
    static const int MIN_MERGE = 32;
    
    static int minRunLength(int n) {
        int r = 0;
        while (n >= MIN_MERGE) {
            r |= (n & 1);
            n >>= 1;
        }
        return n + r;
    }
    
    static void insertionSort(std::vector<T>& arr, int left, int right) {
        for (int i = left + 1; i <= right; i++) {
            T temp = arr[i];
            int j = i - 1;
            
            while (j >= left && arr[j] > temp) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = temp;
        }
    }
    
    static void merge(std::vector<T>& arr, int l, int m, int r) {
        int len1 = m - l + 1, len2 = r - m;
        std::vector<T> left(len1), right(len2);
        
        for (int i = 0; i < len1; i++)
            left[i] = arr[l + i];
        for (int i = 0; i < len2; i++)
            right[i] = arr[m + 1 + i];
        
        int i = 0, j = 0, k = l;
        
        while (i < len1 && j < len2) {
            if (left[i] <= right[j]) {
                arr[k] = left[i];
                i++;
            } else {
                arr[k] = right[j];
                j++;
            }
            k++;
        }
        
        while (i < len1) {
            arr[k] = left[i];
            k++;
            i++;
        }
        
        while (j < len2) {
            arr[k] = right[j];
            k++;
            j++;
        }
    }
    
public:
    static void sort(std::vector<T>& arr) {
        int n = arr.size();
        int minRun = minRunLength(n);
        
        // Sort individual subarrays
        for (int i = 0; i < n; i += minRun) {
            insertionSort(arr, i, std::min((i + MIN_MERGE - 1), (n - 1)));
        }
        
        // Start merging
        for (int size = minRun; size < n; size = 2 * size) {
            for (int left = 0; left < n; left += 2 * size) {
                int mid = left + size - 1;
                int right = std::min((left + 2 * size - 1), (n - 1));
                
                if (mid < right) {
                    merge(arr, left, mid, right);
                }
            }
        }
    }
};
```

## Testing and Verification

### Test Cases
1. **Already sorted data**: Should perform in O(n)
2. **Reverse sorted data**: Should handle efficiently
3. **Partially sorted data**: Should exploit existing order
4. **Random data**: Should perform as well as merge sort
5. **Duplicate elements**: Should maintain stability

### Performance Tests
1. **Adaptive behavior**: Compare with merge sort on partially sorted data
2. **Stability verification**: Ensure stable sorting
3. **Memory usage**: Verify O(n) space complexity
4. **Large datasets**: Test scalability

## Common Pitfalls
1. Incorrect run identification
2. Improper merge invariants
3. Memory management issues
4. Not handling edge cases properly

## Optimization Tips
1. Optimize run size based on cache size
2. Implement galloping mode for better merge performance
3. Use SIMD operations for merge operations
4. Optimize for specific data distributions

## Real-World Applications
- Python's built-in sort
- Java's Arrays.sort() for objects
- Real-world data processing
- Database sorting operations
- Data analysis pipelines

## Advantages
- Adaptive to existing order
- Stable sorting
- Good performance on real-world data
- Optimized for partial sorting

## Disadvantages
- Higher memory usage than in-place sorts
- More complex implementation
- Slightly slower than quicksort on random data

## Related Algorithms
- Merge Sort
- Insertion Sort
- Natural Merge Sort
- Adaptive algorithms

## References
- Python's timsort implementation
- TimSort original paper by Tim Peters
- Adaptive sorting algorithms research

---

*This implementation provides a comprehensive guide to Tim Sort with adaptive sorting capabilities and real-world optimizations.*
---

## Next Step

- Go to [12_Intro_Sort.md](12_Intro_Sort.md) to continue with Intro Sort.
