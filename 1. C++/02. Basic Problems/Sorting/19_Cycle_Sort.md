# Cycle Sort

## Overview
Cycle Sort is an in-place sorting algorithm that minimizes the number of write operations. It's particularly useful when write operations are expensive, such as with EEPROM or flash memory.

## Algorithm Description

### Theory
Cycle Sort works by finding cycles in the permutation of elements and rotating them to place each element in its correct position. Each cycle requires exactly (cycle length - 1) writes, making it optimal for minimizing writes.

### Algorithm Steps
1. For each element, find its correct position in the sorted array
2. If the element is already in correct position, continue
3. Otherwise, place it in its correct position and continue the cycle
4. Repeat until all elements are in their correct positions

### Pseudocode
```
FUNCTION cycleSort(array):
    n = length(array)
    
    FOR cycleStart FROM 0 TO n - 2:
        item = array[cycleStart]
        
        // Find position where we put the item
        pos = cycleStart
        FOR i FROM cycleStart + 1 TO n - 1:
            IF array[i] < item:
                pos++
        
        // If item is already in correct position
        IF pos == cycleStart:
            CONTINUE
        
        // Skip duplicate elements
        WHILE item == array[pos]:
            pos++
        
        // Put the item to its right position
        IF pos != cycleStart:
            swap(item, array[pos])
        
        // Rotate the rest of the cycle
        WHILE pos != cycleStart:
            pos = cycleStart
            FOR i FROM cycleStart + 1 TO n - 1:
                IF array[i] < item:
                    pos++
            
            WHILE item == array[pos]:
                pos++
            
            IF item != array[pos]:
                swap(item, array[pos])
```

## Complexity Analysis

### Time Complexity
- **Best Case**: O(n²)
- **Average Case**: O(n²)
- **Worst Case**: O(n²)

### Space Complexity
- **Space**: O(1) - In-place sorting

### Write Operations
- **Minimum writes**: O(n) - When array is already sorted
- **Maximum writes**: O(n²) - When array is reverse sorted

## Best Practices
- Excellent for minimizing write operations
- In-place sorting algorithm
- Not stable by default
- Useful for expensive write operations

## When to Use
- EEPROM/flash memory where writes are expensive
- Situations minimizing data movement is critical
- Embedded systems with limited write cycles
- When write operations are costly

## Implementation Examples

### Example 1: Basic Cycle Sort
```cpp
#include <iostream>
#include <vector>

class CycleSort {
public:
    static void sort(std::vector<int>& arr) {
        int n = arr.size();
        
        for (int cycleStart = 0; cycleStart < n - 1; cycleStart++) {
            int item = arr[cycleStart];
            
            // Find position where we put the item
            int pos = cycleStart;
            for (int i = cycleStart + 1; i < n; i++) {
                if (arr[i] < item) {
                    pos++;
                }
            }
            
            // If item is already in correct position
            if (pos == cycleStart) {
                continue;
            }
            
            // Skip duplicate elements
            while (item == arr[pos]) {
                pos++;
            }
            
            // Put the item to its right position
            if (pos != cycleStart) {
                std::swap(item, arr[pos]);
            }
            
            // Rotate the rest of the cycle
            while (pos != cycleStart) {
                pos = cycleStart;
                for (int i = cycleStart + 1; i < n; i++) {
                    if (arr[i] < item) {
                        pos++;
                    }
                }
                
                while (item == arr[pos]) {
                    pos++;
                }
                
                if (item != arr[pos]) {
                    std::swap(item, arr[pos]);
                }
            }
        }
    }
};
```

### Example 2: Cycle Sort with Write Tracking
```cpp
#include <vector>
#include <iostream>

class CycleSortWithTracking {
private:
    int writes = 0;
    int cycles = 0;
    int comparisons = 0;
    
public:
    void sort(std::vector<int>& arr) {
        writes = 0;
        cycles = 0;
        comparisons = 0;
        
        int n = arr.size();
        
        for (int cycleStart = 0; cycleStart < n - 1; cycleStart++) {
            int item = arr[cycleStart];
            
            // Find position where we put the item
            int pos = cycleStart;
            for (int i = cycleStart + 1; i < n; i++) {
                comparisons++;
                if (arr[i] < item) {
                    pos++;
                }
            }
            
            // If item is already in correct position
            if (pos == cycleStart) {
                continue;
            }
            
            cycles++;
            
            // Skip duplicate elements
            while (item == arr[pos]) {
                pos++;
            }
            
            // Put the item to its right position
            if (pos != cycleStart) {
                std::swap(item, arr[pos]);
                writes++;
            }
            
            // Rotate the rest of the cycle
            while (pos != cycleStart) {
                pos = cycleStart;
                for (int i = cycleStart + 1; i < n; i++) {
                    comparisons++;
                    if (arr[i] < item) {
                        pos++;
                    }
                }
                
                while (item == arr[pos]) {
                    pos++;
                }
                
                if (item != arr[pos]) {
                    std::swap(item, arr[pos]);
                    writes++;
                }
            }
        }
        
        std::cout << "Cycle Sort Analysis:\n";
        std::cout << "Writes: " << writes << "\n";
        std::cout << "Cycles: " << cycles << "\n";
        std::cout << "Comparisons: " << comparisons << "\n";
        std::cout << "Writes per element: " << static_cast<double>(writes) / n << "\n";
    }
};
```

### Example 3: Generic Cycle Sort Template
```cpp
#include <vector>
#include <algorithm>

template<typename T>
class CycleSortGeneric {
public:
    static void sort(std::vector<T>& arr) {
        int n = arr.size();
        
        for (int cycleStart = 0; cycleStart < n - 1; cycleStart++) {
            T item = arr[cycleStart];
            
            // Find position where we put the item
            int pos = cycleStart;
            for (int i = cycleStart + 1; i < n; i++) {
                if (arr[i] < item) {
                    pos++;
                }
            }
            
            // If item is already in correct position
            if (pos == cycleStart) {
                continue;
            }
            
            // Skip duplicate elements
            while (item == arr[pos]) {
                pos++;
            }
            
            // Put the item to its right position
            if (pos != cycleStart) {
                std::swap(item, arr[pos]);
            }
            
            // Rotate the rest of the cycle
            while (pos != cycleStart) {
                pos = cycleStart;
                for (int i = cycleStart + 1; i < n; i++) {
                    if (arr[i] < item) {
                        pos++;
                    }
                }
                
                while (item == arr[pos]) {
                    pos++;
                }
                
                if (item != arr[pos]) {
                    std::swap(item, arr[pos]);
                }
            }
        }
    }
};
```

### Example 4: Cycle Sort with Custom Comparator
```cpp
#include <vector>
#include <functional>

template<typename T, typename Compare = std::less<T>>
class CycleSortCustom {
private:
    Compare comp;
    
public:
    CycleSortCustom(Compare c = Compare()) : comp(c) {}
    
    void sort(std::vector<T>& arr) {
        int n = arr.size();
        
        for (int cycleStart = 0; cycleStart < n - 1; cycleStart++) {
            T item = arr[cycleStart];
            
            // Find position where we put the item
            int pos = cycleStart;
            for (int i = cycleStart + 1; i < n; i++) {
                if (comp(arr[i], item)) {  // arr[i] < item
                    pos++;
                }
            }
            
            // If item is already in correct position
            if (pos == cycleStart) {
                continue;
            }
            
            // Skip duplicate elements
            while (!comp(item, arr[pos]) && !comp(arr[pos], item)) {  // item == arr[pos]
                pos++;
            }
            
            // Put the item to its right position
            if (pos != cycleStart) {
                std::swap(item, arr[pos]);
            }
            
            // Rotate the rest of the cycle
            while (pos != cycleStart) {
                pos = cycleStart;
                for (int i = cycleStart + 1; i < n; i++) {
                    if (comp(arr[i], item)) {  // arr[i] < item
                        pos++;
                    }
                }
                
                while (!comp(item, arr[pos]) && !comp(arr[pos], item)) {  // item == arr[pos]
                    pos++;
                }
                
                if (item != arr[pos]) {
                    std::swap(item, arr[pos]);
                }
            }
        }
    }
};
```

### Example 5: Stable Cycle Sort
```cpp
#include <vector>
#include <utility>

class StableCycleSort {
private:
    struct Element {
        int value;
        int originalIndex;
        
        Element(int v, int idx) : value(v), originalIndex(idx) {}
        
        bool operator<(const Element& other) const {
            if (value != other.value) {
                return value < other.value;
            }
            return originalIndex < other.originalIndex;
        }
    };
    
public:
    void sort(std::vector<int>& arr) {
        int n = arr.size();
        std::vector<Element> elements;
        elements.reserve(n);
        
        for (int i = 0; i < n; i++) {
            elements.emplace_back(arr[i], i);
        }
        
        for (int cycleStart = 0; cycleStart < n - 1; cycleStart++) {
            Element item = elements[cycleStart];
            
            // Find position where we put the item
            int pos = cycleStart;
            for (int i = cycleStart + 1; i < n; i++) {
                if (elements[i] < item) {
                    pos++;
                }
            }
            
            // If item is already in correct position
            if (pos == cycleStart) {
                continue;
            }
            
            // Skip duplicate elements
            while (item.value == elements[pos].value && 
                   item.originalIndex == elements[pos].originalIndex) {
                pos++;
            }
            
            // Put the item to its right position
            if (pos != cycleStart) {
                std::swap(item, elements[pos]);
            }
            
            // Rotate the rest of the cycle
            while (pos != cycleStart) {
                pos = cycleStart;
                for (int i = cycleStart + 1; i < n; i++) {
                    if (elements[i] < item) {
                        pos++;
                    }
                }
                
                while (item.value == elements[pos].value && 
                       item.originalIndex == elements[pos].originalIndex) {
                    pos++;
                }
                
                if (item.value != elements[pos].value || 
                    item.originalIndex != elements[pos].originalIndex) {
                    std::swap(item, elements[pos]);
                }
            }
        }
        
        // Copy back to original array
        for (int i = 0; i < n; i++) {
            arr[i] = elements[i].value;
        }
    }
};
```

### Example 6: Cycle Sort for Minimizing Writes
```cpp
#include <vector>
#include <iostream>

class WriteOptimizedCycleSort {
private:
    int writeCount = 0;
    
    void writeWithCount(std::vector<int>& arr, int index, int value) {
        if (arr[index] != value) {
            arr[index] = value;
            writeCount++;
        }
    }
    
public:
    void sort(std::vector<int>& arr) {
        writeCount = 0;
        int n = arr.size();
        
        for (int cycleStart = 0; cycleStart < n - 1; cycleStart++) {
            int item = arr[cycleStart];
            
            // Find position where we put the item
            int pos = cycleStart;
            for (int i = cycleStart + 1; i < n; i++) {
                if (arr[i] < item) {
                    pos++;
                }
            }
            
            // If item is already in correct position
            if (pos == cycleStart) {
                continue;
            }
            
            // Skip duplicate elements
            while (item == arr[pos]) {
                pos++;
            }
            
            // Put the item to its right position
            if (pos != cycleStart) {
                std::swap(item, arr[pos]);
                writeWithCount(arr, pos, item);
            }
            
            // Rotate the rest of the cycle
            while (pos != cycleStart) {
                pos = cycleStart;
                for (int i = cycleStart + 1; i < n; i++) {
                    if (arr[i] < item) {
                        pos++;
                    }
                }
                
                while (item == arr[pos]) {
                    pos++;
                }
                
                if (item != arr[pos]) {
                    std::swap(item, arr[pos]);
                    writeWithCount(arr, pos, item);
                }
            }
        }
        
        std::cout << "Total writes: " << writeCount << std::endl;
        std::cout << "Writes per element: " << static_cast<double>(writeCount) / n << std::endl;
    }
};
```

## Testing and Verification

### Test Cases
1. **Already sorted array**: Minimum writes
2. **Reverse sorted array**: Maximum writes
3. **Random array**: Normal operation
4. **Array with duplicates**: Should handle correctly
5. **Single element**: Should handle edge case

### Performance Tests
1. **Write count analysis**: Verify minimal writes
2. **Comparison with other sorts**: Relative performance
3. **Memory write efficiency**: Test on expensive write scenarios
4. **Stability test**: Verify stable behavior

## Common Pitfalls
1. Incorrect cycle detection
2. Not handling duplicate elements properly
3. Infinite loops in cycle rotation
4. Off-by-one errors in position calculation

## Optimization Tips
1. Optimize for specific data patterns
2. Use efficient swap operations
3. Consider cache performance
4. Implement early termination for sorted portions

## Real-World Applications
- EEPROM/flash memory programming
- Embedded systems with limited write cycles
- Database systems with expensive writes
- Situations minimizing data movement is critical
- Memory-constrained environments

## Advantages
- Minimizes write operations
- In-place sorting algorithm
- Optimal for expensive write operations
- Deterministic write count

## Disadvantages
- O(n²) time complexity
- Not stable by default
- Complex implementation
- Limited real-world applications

## Mathematical Properties

### Write Operation Analysis
- Minimum writes: n - 1 (already sorted)
- Maximum writes: n² - 1 (reverse sorted)
- Average writes: approximately n(n-1)/2

### Cycle Properties
- Each cycle requires (length - 1) writes
- Total number of cycles varies based on permutation
- Optimal for minimizing writes

## Related Algorithms
- Selection Sort (similar concept)
- Permutation sorting
- In-place sorting algorithms
- Memory-efficient sorts

## References
- Algorithm design textbooks
- Memory-efficient sorting research
- Embedded systems programming
- Database optimization literature

---

*This implementation provides a comprehensive guide to Cycle Sort with focus on minimizing write operations and applications in memory-constrained environments.*

---

## Next Step

- Go to [20_Bogo_Sort.md](20_Bogo_Sort.md) to continue with Bogo Sort.
