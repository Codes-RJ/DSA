# Cocktail Sort

## Overview
Cocktail Sort, also known as Bidirectional Bubble Sort or Shaker Sort, is a variation of bubble sort that sorts in both directions on each pass through the list. This bidirectional approach can be more efficient than standard bubble sort.

## Algorithm Description

### Theory
Cocktail Sort improves upon bubble sort by eliminating turtles (small values at the end) more quickly. It works by moving the largest element to the end in a forward pass and the smallest element to the beginning in a backward pass.

### Algorithm Steps
1. Initialize start and end pointers
2. Perform forward pass: bubble up largest element
3. Update end pointer
4. Perform backward pass: bubble down smallest element
5. Update start pointer
6. Repeat until no swaps occur

### Pseudocode
```
FUNCTION cocktailSort(array):
    swapped = true
    start = 0
    end = length(array) - 1
    
    WHILE swapped:
        swapped = false
        
        // Forward pass
        FOR i FROM start TO end - 1:
            IF array[i] > array[i + 1]:
                swap(array[i], array[i + 1])
                swapped = true
        
        IF NOT swapped:
            BREAK
        
        swapped = false
        end = end - 1
        
        // Backward pass
        FOR i FROM end - 1 DOWNTO start:
            IF array[i] > array[i + 1]:
                swap(array[i], array[i + 1])
                swapped = true
        
        start = start + 1
```

## Complexity Analysis

### Time Complexity
- **Best Case**: O(n) - Already sorted
- **Average Case**: O(n²)
- **Worst Case**: O(n²) - Reverse sorted

### Space Complexity
- **Space**: O(1) - In-place sorting

## Best Practices
- More efficient than bubble sort for partially sorted data
- Stable sorting algorithm
- Good for educational purposes
- Can be optimized with early termination

## When to Use
- Small datasets where bubble sort is too slow
- Educational settings to teach sorting concepts
- When bidirectional movement is beneficial
- Nearly sorted data

## Implementation Examples

### Example 1: Basic Cocktail Sort
```cpp
#include <iostream>
#include <vector>

class CocktailSort {
public:
    static void sort(std::vector<int>& arr) {
        bool swapped = true;
        int start = 0;
        int end = arr.size() - 1;
        
        while (swapped) {
            swapped = false;
            
            // Forward pass
            for (int i = start; i < end; i++) {
                if (arr[i] > arr[i + 1]) {
                    std::swap(arr[i], arr[i + 1]);
                    swapped = true;
                }
            }
            
            if (!swapped) {
                break;
            }
            
            swapped = false;
            end--;
            
            // Backward pass
            for (int i = end - 1; i >= start; i--) {
                if (arr[i] > arr[i + 1]) {
                    std::swap(arr[i], arr[i + 1]);
                    swapped = true;
                }
            }
            
            start++;
        }
    }
};
```

### Example 2: Optimized Cocktail Sort with Tracking
```cpp
#include <vector>

class OptimizedCocktailSort {
public:
    static void sort(std::vector<int>& arr) {
        if (arr.empty()) return;
        
        int start = 0;
        int end = arr.size() - 1;
        int newStart, newEnd;
        
        while (start < end) {
            newEnd = start;
            
            // Forward pass - find the last swap position
            for (int i = start; i < end; i++) {
                if (arr[i] > arr[i + 1]) {
                    std::swap(arr[i], arr[i + 1]);
                    newEnd = i;
                }
            }
            
            end = newEnd;
            if (start >= end) break;
            
            newStart = end;
            
            // Backward pass - find the first swap position
            for (int i = end; i > start; i--) {
                if (arr[i - 1] > arr[i]) {
                    std::swap(arr[i - 1], arr[i]);
                    newStart = i;
                }
            }
            
            start = newStart;
        }
    }
};
```

### Example 3: Generic Cocktail Sort Template
```cpp
#include <vector>
#include <algorithm>

template<typename T>
class CocktailSortGeneric {
public:
    static void sort(std::vector<T>& arr) {
        bool swapped = true;
        int start = 0;
        int end = arr.size() - 1;
        
        while (swapped) {
            swapped = false;
            
            // Forward pass
            for (int i = start; i < end; i++) {
                if (arr[i] > arr[i + 1]) {
                    std::swap(arr[i], arr[i + 1]);
                    swapped = true;
                }
            }
            
            if (!swapped) {
                break;
            }
            
            swapped = false;
            end--;
            
            // Backward pass
            for (int i = end - 1; i >= start; i--) {
                if (arr[i] > arr[i + 1]) {
                    std::swap(arr[i], arr[i + 1]);
                    swapped = true;
                }
            }
            
            start++;
        }
    }
};
```

### Example 4: Cocktail Sort with Custom Comparator
```cpp
#include <vector>
#include <functional>

template<typename T, typename Compare = std::less<T>>
class CocktailSortCustom {
private:
    Compare comp;
    
public:
    CocktailSortCustom(Compare c = Compare()) : comp(c) {}
    
    void sort(std::vector<T>& arr) {
        bool swapped = true;
        int start = 0;
        int end = arr.size() - 1;
        
        while (swapped) {
            swapped = false;
            
            // Forward pass
            for (int i = start; i < end; i++) {
                if (comp(arr[i + 1], arr[i])) {  // arr[i] > arr[i + 1]
                    std::swap(arr[i], arr[i + 1]);
                    swapped = true;
                }
            }
            
            if (!swapped) {
                break;
            }
            
            swapped = false;
            end--;
            
            // Backward pass
            for (int i = end - 1; i >= start; i--) {
                if (comp(arr[i + 1], arr[i])) {  // arr[i] > arr[i + 1]
                    std::swap(arr[i], arr[i + 1]);
                    swapped = true;
                }
            }
            
            start++;
        }
    }
};
```

### Example 5: Cocktail Sort with Performance Metrics
```cpp
#include <vector>
#include <chrono>

class CocktailSortWithMetrics {
private:
    int comparisons = 0;
    int swaps = 0;
    int passes = 0;
    
public:
    void sort(std::vector<int>& arr) {
        comparisons = 0;
        swaps = 0;
        passes = 0;
        
        bool swapped = true;
        int start = 0;
        int end = arr.size() - 1;
        
        while (swapped) {
            swapped = false;
            passes++;
            
            // Forward pass
            for (int i = start; i < end; i++) {
                comparisons++;
                if (arr[i] > arr[i + 1]) {
                    std::swap(arr[i], arr[i + 1]);
                    swaps++;
                    swapped = true;
                }
            }
            
            if (!swapped) {
                break;
            }
            
            swapped = false;
            end--;
            
            // Backward pass
            for (int i = end - 1; i >= start; i--) {
                comparisons++;
                if (arr[i] > arr[i + 1]) {
                    std::swap(arr[i], arr[i + 1]);
                    swaps++;
                    swapped = true;
                }
            }
            
            start++;
        }
    }
    
    int getComparisons() const { return comparisons; }
    int getSwaps() const { return swaps; }
    int getPasses() const { return passes; }
};
```

## Testing and Verification

### Test Cases
1. **Already sorted array**: Should complete in one pass
2. **Reverse sorted array**: Should perform maximum swaps
3. **Random array**: Should sort correctly
4. **Single element**: Should handle edge case
5. **Empty array**: Should handle gracefully

### Performance Tests
1. **Comparison with bubble sort**: Should be more efficient
2. **Partially sorted data**: Should perform well
3. **Small vs large arrays**: Performance characteristics
4. **Stability test**: Verify stable sorting

## Common Pitfalls
1. Off-by-one errors in loop bounds
2. Not updating start/end pointers correctly
3. Infinite loop if swap detection is incorrect
4. Not handling empty arrays properly

## Optimization Tips
1. Track last swap positions to reduce range
2. Use early termination when no swaps occur
3. Optimize for specific data patterns
4. Consider cache performance

## Real-World Applications
- Educational purposes
- Small dataset sorting
- Real-time systems with small data
- Embedded systems with limited memory
- Teaching bidirectional algorithms

## Advantages
- More efficient than bubble sort
- Stable sorting algorithm
- Good for nearly sorted data
- Simple to understand and implement

## Disadvantages
- Still O(n²) time complexity
- Not suitable for large datasets
- More complex than bubble sort
- Outperformed by more advanced algorithms

## Comparison with Bubble Sort

### Advantages over Bubble Sort
1. Eliminates turtles faster
2. Better for partially sorted data
3. Fewer passes needed on average
4. Bidirectional movement

### When to choose Cocktail Sort over Bubble Sort
- When data is nearly sorted
- When small elements are at the end
- When bidirectional movement is beneficial
- For educational purposes

## Related Algorithms
- Bubble Sort
- Odd-Even Sort
- Gnome Sort
- Comb Sort

## References
- Sorting algorithm textbooks
- Algorithm visualization resources
- Educational computer science materials

---

*This implementation provides a comprehensive guide to Cocktail Sort with bidirectional sorting capabilities and optimization strategies.*

---

## Next Step

- Go to [14_Comb_Sort.md](14_Comb_Sort.md) to continue with Comb Sort.
