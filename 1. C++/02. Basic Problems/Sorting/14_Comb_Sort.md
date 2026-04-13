# Comb Sort

## Overview
Comb Sort is an improvement over bubble sort that eliminates turtles (small values near the end) more efficiently. It uses a gap sequence that starts large and gradually shrinks, comparing elements that are far apart initially.

## Algorithm Description

### Theory
Comb Sort improves on bubble sort by introducing a gap between compared elements. The gap starts large and shrinks by a shrink factor (typically 1.3) until it reaches 1, at which point it performs a final bubble sort pass.

### Mathematical Foundation
- Initial gap: n/2 where n is array size
- Shrink factor: typically 1.3 (optimal value)
- Gap sequence: n/2, n/4, n/8, ..., 1
- Final pass: equivalent to bubble sort

### Algorithm Steps
1. Initialize gap = n/2, swapped = true
2. While gap > 1 or swapped:
   - Set gap = max(1, gap/shrink_factor)
   - Set swapped = false
   - Compare and swap elements gap apart
   - If any swap occurs, set swapped = true

### Pseudocode
```
FUNCTION combSort(array):
    gap = length(array)
    shrink = 1.3
    sorted = false
    
    WHILE NOT sorted:
        gap = floor(gap / shrink)
        IF gap <= 1:
            gap = 1
            sorted = true
        
        i = 0
        WHILE i + gap < length(array):
            IF array[i] > array[i + gap]:
                swap(array[i], array[i + gap])
                sorted = false
            i = i + 1
```

## Complexity Analysis

### Time Complexity
- **Best Case**: O(n log n)
- **Average Case**: O(n²/2^p) where p is number of passes
- **Worst Case**: O(n²)

### Space Complexity
- **Space**: O(1) - In-place sorting

## Best Practices
- Use shrink factor of 1.3 for optimal performance
- More efficient than bubble sort for most cases
- Simple to implement
- Good for medium-sized arrays

## When to Use
- Improvement over bubble sort
- Medium-sized datasets
- When simplicity is valued
- Educational purposes

## Implementation Examples

### Example 1: Basic Comb Sort
```cpp
#include <iostream>
#include <vector>
#include <cmath>

class CombSort {
public:
    static void sort(std::vector<int>& arr) {
        int n = arr.size();
        if (n <= 1) return;
        
        int gap = n;
        const double shrink = 1.3;
        bool sorted = false;
        
        while (!sorted) {
            gap = static_cast<int>(gap / shrink);
            if (gap <= 1) {
                gap = 1;
                sorted = true;
            }
            
            bool swapped = false;
            for (int i = 0; i + gap < n; i++) {
                if (arr[i] > arr[i + gap]) {
                    std::swap(arr[i], arr[i + gap]);
                    swapped = true;
                }
            }
            
            if (gap == 1 && swapped) {
                sorted = false;
            }
        }
    }
};
```

### Example 2: Optimized Comb Sort with Performance Tracking
```cpp
#include <vector>
#include <chrono>

class OptimizedCombSort {
private:
    int comparisons = 0;
    int swaps = 0;
    int passes = 0;
    
public:
    void sort(std::vector<int>& arr) {
        comparisons = 0;
        swaps = 0;
        passes = 0;
        
        int n = arr.size();
        if (n <= 1) return;
        
        int gap = n;
        const double shrink = 1.3;
        bool sorted = false;
        
        while (!sorted) {
            gap = static_cast<int>(gap / shrink);
            if (gap <= 1) {
                gap = 1;
                sorted = true;
            }
            
            passes++;
            bool swapped = false;
            for (int i = 0; i + gap < n; i++) {
                comparisons++;
                if (arr[i] > arr[i + gap]) {
                    std::swap(arr[i], arr[i + gap]);
                    swaps++;
                    swapped = true;
                }
            }
            
            if (gap == 1 && swapped) {
                sorted = false;
            }
        }
    }
    
    int getComparisons() const { return comparisons; }
    int getSwaps() const { return swaps; }
    int getPasses() const { return passes; }
};
```

### Example 3: Generic Comb Sort Template
```cpp
#include <vector>
#include <algorithm>

template<typename T>
class CombSortGeneric {
public:
    static void sort(std::vector<T>& arr) {
        int n = arr.size();
        if (n <= 1) return;
        
        int gap = n;
        const double shrink = 1.3;
        bool sorted = false;
        
        while (!sorted) {
            gap = static_cast<int>(gap / shrink);
            if (gap <= 1) {
                gap = 1;
                sorted = true;
            }
            
            bool swapped = false;
            for (int i = 0; i + gap < n; i++) {
                if (arr[i] > arr[i + gap]) {
                    std::swap(arr[i], arr[i + gap]);
                    swapped = true;
                }
            }
            
            if (gap == 1 && swapped) {
                sorted = false;
            }
        }
    }
};
```

### Example 4: Comb Sort with Custom Shrink Factor
```cpp
#include <vector>

class CombSortCustomShrink {
private:
    double shrinkFactor;
    
public:
    CombSortCustomShrink(double shrink = 1.3) : shrinkFactor(shrink) {}
    
    void sort(std::vector<int>& arr) {
        int n = arr.size();
        if (n <= 1) return;
        
        int gap = n;
        bool sorted = false;
        
        while (!sorted) {
            gap = static_cast<int>(gap / shrinkFactor);
            if (gap <= 1) {
                gap = 1;
                sorted = true;
            }
            
            bool swapped = false;
            for (int i = 0; i + gap < n; i++) {
                if (arr[i] > arr[i + gap]) {
                    std::swap(arr[i], arr[i + gap]);
                    swapped = true;
                }
            }
            
            if (gap == 1 && swapped) {
                sorted = false;
            }
        }
    }
    
    void setShrinkFactor(double shrink) {
        shrinkFactor = shrink;
    }
};
```

### Example 5: Comb Sort with Custom Comparator
```cpp
#include <vector>
#include <functional>

template<typename T, typename Compare = std::less<T>>
class CombSortCustom {
private:
    Compare comp;
    
public:
    CombSortCustom(Compare c = Compare()) : comp(c) {}
    
    void sort(std::vector<T>& arr) {
        int n = arr.size();
        if (n <= 1) return;
        
        int gap = n;
        const double shrink = 1.3;
        bool sorted = false;
        
        while (!sorted) {
            gap = static_cast<int>(gap / shrink);
            if (gap <= 1) {
                gap = 1;
                sorted = true;
            }
            
            bool swapped = false;
            for (int i = 0; i + gap < n; i++) {
                if (comp(arr[i + gap], arr[i])) {  // arr[i] > arr[i + gap]
                    std::swap(arr[i], arr[i + gap]);
                    swapped = true;
                }
            }
            
            if (gap == 1 && swapped) {
                sorted = false;
            }
        }
    }
};
```

### Example 6: Comb Sort with Gap Sequence Analysis
```cpp
#include <vector>
#include <iostream>

class CombSortAnalysis {
private:
    std::vector<int> gapSequence;
    
public:
    void sort(std::vector<int>& arr) {
        int n = arr.size();
        if (n <= 1) return;
        
        gapSequence.clear();
        int gap = n;
        const double shrink = 1.3;
        bool sorted = false;
        
        while (!sorted) {
            gap = static_cast<int>(gap / shrink);
            if (gap <= 1) {
                gap = 1;
                sorted = true;
            }
            
            gapSequence.push_back(gap);
            
            bool swapped = false;
            for (int i = 0; i + gap < n; i++) {
                if (arr[i] > arr[i + gap]) {
                    std::swap(arr[i], arr[i + gap]);
                    swapped = true;
                }
            }
            
            if (gap == 1 && swapped) {
                sorted = false;
            }
        }
    }
    
    const std::vector<int>& getGapSequence() const {
        return gapSequence;
    }
    
    void printGapSequence() const {
        std::cout << "Gap sequence: ";
        for (int gap : gapSequence) {
            std::cout << gap << " ";
        }
        std::cout << std::endl;
    }
};
```

## Testing and Verification

### Test Cases
1. **Already sorted array**: Should complete efficiently
2. **Reverse sorted array**: Should handle worst case
3. **Random array**: Should sort correctly
4. **Array with duplicates**: Should handle correctly
5. **Small arrays**: Should work efficiently

### Performance Tests
1. **Comparison with bubble sort**: Should be more efficient
2. **Different shrink factors**: Performance analysis
3. **Gap sequence analysis**: Study gap reduction
4. **Large dataset performance**: Scalability testing

## Common Pitfalls
1. Using wrong shrink factor
2. Integer division issues in gap calculation
3. Not handling final bubble sort pass correctly
4. Infinite loop if sorted condition is wrong

## Optimization Tips
1. Use optimal shrink factor of 1.3
2. Track gap sequence for analysis
3. Optimize for specific data patterns
4. Consider cache performance

## Real-World Applications
- Educational sorting demonstrations
- Medium-sized dataset sorting
- Situations where bubble sort is too slow
- Embedded systems with limited memory
- Teaching algorithm optimization

## Advantages
- More efficient than bubble sort
- Simple to implement
- Good performance on average
- Eliminates turtles quickly

## Disadvantages
- Still O(n²) worst-case complexity
- Not suitable for very large datasets
- Performance depends on shrink factor
- Outperformed by advanced algorithms

## Shrink Factor Analysis

### Optimal Shrink Factor
- Research suggests 1.3 is optimal
- Values between 1.2 and 1.5 work well
- Too small: too many comparisons
- Too large: insufficient gap reduction

### Different Shrink Factors
- 1.3: Standard optimal value
- 1.25: More conservative approach
- 1.4: More aggressive gap reduction
- 2.0: Equivalent to shell sort with certain gaps

## Related Algorithms
- Bubble Sort
- Shell Sort
- Gnome Sort
- Cocktail Sort

## References
- Comb Sort research papers
- Algorithm optimization studies
- Sorting algorithm comparisons
- Educational computer science resources

---

*This implementation provides a comprehensive guide to Comb Sort with gap-based optimization and performance analysis.*

---

## Next Step

- Go to [15_Gnome_Sort.md](15_Gnome_Sort.md) to continue with Gnome Sort.
