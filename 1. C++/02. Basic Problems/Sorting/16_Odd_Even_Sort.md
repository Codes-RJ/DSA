# Odd-Even Sort

## Overview
Odd-Even Sort, also known as Brick Sort, is a parallel sorting algorithm that works by repeatedly comparing and swapping adjacent elements in alternating odd and even phases. It's particularly useful for parallel processing environments.

## Algorithm Description

### Theory
Odd-Even Sort performs two phases in each iteration:
1. **Odd Phase**: Compare and swap elements at odd indices (1,3,5,...) with their next element
2. **Even Phase**: Compare and swap elements at even indices (0,2,4,...) with their next element

This alternating pattern allows for parallel execution of non-overlapping comparisons.

### Algorithm Steps
1. Initialize sorted = false
2. While not sorted:
   - Set sorted = true
   - Perform odd phase: compare (1,2), (3,4), (5,6),...
   - Perform even phase: compare (0,1), (2,3), (4,5),...
   - If any swap occurs, set sorted = false

### Pseudocode
```
FUNCTION oddEvenSort(array):
    sorted = false
    
    WHILE NOT sorted:
        sorted = true
        
        // Odd phase
        FOR i FROM 1 TO length(array) - 2 STEP 2:
            IF array[i] > array[i + 1]:
                swap(array[i], array[i + 1])
                sorted = false
        
        // Even phase
        FOR i FROM 0 TO length(array) - 2 STEP 2:
            IF array[i] > array[i + 1]:
                swap(array[i], array[i + 1])
                sorted = false
```

## Complexity Analysis

### Time Complexity
- **Best Case**: O(n) - Already sorted
- **Average Case**: O(n²)
- **Worst Case**: O(n²) - Reverse sorted

### Space Complexity
- **Space**: O(1) - In-place sorting

## Best Practices
- Excellent for parallel processing
- Simple to implement
- Good for educational purposes
- Naturally parallelizable

## When to Use
- Parallel processing environments
- Multi-core systems
- Teaching parallel algorithms
- Situations where parallel execution is beneficial

## Implementation Examples

### Example 1: Basic Odd-Even Sort
```cpp
#include <iostream>
#include <vector>

class OddEvenSort {
public:
    static void sort(std::vector<int>& arr) {
        bool sorted = false;
        
        while (!sorted) {
            sorted = true;
            
            // Odd phase
            for (int i = 1; i < arr.size() - 1; i += 2) {
                if (arr[i] > arr[i + 1]) {
                    std::swap(arr[i], arr[i + 1]);
                    sorted = false;
                }
            }
            
            // Even phase
            for (int i = 0; i < arr.size() - 1; i += 2) {
                if (arr[i] > arr[i + 1]) {
                    std::swap(arr[i], arr[i + 1]);
                    sorted = false;
                }
            }
        }
    }
};
```

### Example 2: Optimized Odd-Even Sort with Early Termination
```cpp
#include <vector>

class OptimizedOddEvenSort {
private:
    int comparisons = 0;
    int swaps = 0;
    int phases = 0;
    
public:
    void sort(std::vector<int>& arr) {
        comparisons = 0;
        swaps = 0;
        phases = 0;
        
        bool sorted = false;
        
        while (!sorted) {
            sorted = true;
            phases++;
            
            // Odd phase
            for (int i = 1; i < arr.size() - 1; i += 2) {
                comparisons++;
                if (arr[i] > arr[i + 1]) {
                    std::swap(arr[i], arr[i + 1]);
                    swaps++;
                    sorted = false;
                }
            }
            
            // Even phase
            for (int i = 0; i < arr.size() - 1; i += 2) {
                comparisons++;
                if (arr[i] > arr[i + 1]) {
                    std::swap(arr[i], arr[i + 1]);
                    swaps++;
                    sorted = false;
                }
            }
        }
    }
    
    int getComparisons() const { return comparisons; }
    int getSwaps() const { return swaps; }
    int getPhases() const { return phases; }
};
```

### Example 3: Generic Odd-Even Sort Template
```cpp
#include <vector>

template<typename T>
class OddEvenSortGeneric {
public:
    static void sort(std::vector<T>& arr) {
        bool sorted = false;
        
        while (!sorted) {
            sorted = true;
            
            // Odd phase
            for (int i = 1; i < arr.size() - 1; i += 2) {
                if (arr[i] > arr[i + 1]) {
                    std::swap(arr[i], arr[i + 1]);
                    sorted = false;
                }
            }
            
            // Even phase
            for (int i = 0; i < arr.size() - 1; i += 2) {
                if (arr[i] > arr[i + 1]) {
                    std::swap(arr[i], arr[i + 1]);
                    sorted = false;
                }
            }
        }
    }
};
```

### Example 4: Parallel Odd-Even Sort (Conceptual)
```cpp
#include <vector>
#include <thread>
#include <mutex>

class ParallelOddEvenSort {
private:
    std::mutex mtx;
    
    void oddPhase(std::vector<int>& arr, int start, int end, bool& swapped) {
        for (int i = start; i < end && i < arr.size() - 1; i += 2) {
            std::lock_guard<std::mutex> lock(mtx);
            if (arr[i] > arr[i + 1]) {
                std::swap(arr[i], arr[i + 1]);
                swapped = true;
            }
        }
    }
    
    void evenPhase(std::vector<int>& arr, int start, int end, bool& swapped) {
        for (int i = start; i < end && i < arr.size() - 1; i += 2) {
            std::lock_guard<std::mutex> lock(mtx);
            if (arr[i] > arr[i + 1]) {
                std::swap(arr[i], arr[i + 1]);
                swapped = true;
            }
        }
    }
    
public:
    void sort(std::vector<int>& arr, int numThreads = 4) {
        bool sorted = false;
        
        while (!sorted) {
            sorted = true;
            bool swapped = false;
            
            std::vector<std::thread> threads;
            int chunkSize = arr.size() / numThreads;
            
            // Parallel odd phase
            for (int i = 0; i < numThreads; i++) {
                int start = 1 + i * chunkSize;
                int end = (i == numThreads - 1) ? arr.size() : start + chunkSize;
                threads.emplace_back(&ParallelOddEvenSort::oddPhase, 
                                   this, std::ref(arr), start, end, std::ref(swapped));
            }
            
            for (auto& thread : threads) {
                thread.join();
            }
            
            threads.clear();
            
            // Parallel even phase
            for (int i = 0; i < numThreads; i++) {
                int start = i * chunkSize;
                int end = (i == numThreads - 1) ? arr.size() : start + chunkSize;
                threads.emplace_back(&ParallelOddEvenSort::evenPhase, 
                                   this, std::ref(arr), start, end, std::ref(swapped));
            }
            
            for (auto& thread : threads) {
                thread.join();
            }
            
            if (swapped) {
                sorted = false;
            }
        }
    }
};
```

### Example 5: Odd-Even Sort with Custom Comparator
```cpp
#include <vector>
#include <functional>

template<typename T, typename Compare = std::less<T>>
class OddEvenSortCustom {
private:
    Compare comp;
    
public:
    OddEvenSortCustom(Compare c = Compare()) : comp(c) {}
    
    void sort(std::vector<T>& arr) {
        bool sorted = false;
        
        while (!sorted) {
            sorted = true;
            
            // Odd phase
            for (int i = 1; i < arr.size() - 1; i += 2) {
                if (comp(arr[i + 1], arr[i])) {  // arr[i] > arr[i + 1]
                    std::swap(arr[i], arr[i + 1]);
                    sorted = false;
                }
            }
            
            // Even phase
            for (int i = 0; i < arr.size() - 1; i += 2) {
                if (comp(arr[i + 1], arr[i])) {  // arr[i] > arr[i + 1]
                    std::swap(arr[i], arr[i + 1]);
                    sorted = false;
                }
            }
        }
    }
};
```

### Example 6: Odd-Even Sort with Performance Analysis
```cpp
#include <vector>
#include <chrono>
#include <iostream>

class OddEvenSortAnalyzer {
private:
    std::vector<double> phaseTimes;
    std::vector<bool> phaseSwapped;
    
public:
    void sort(std::vector<int>& arr) {
        phaseTimes.clear();
        phaseSwapped.clear();
        
        bool sorted = false;
        int phase = 0;
        
        while (!sorted) {
            sorted = true;
            auto phaseStart = std::chrono::high_resolution_clock::now();
            bool phaseSwappedLocal = false;
            
            // Odd phase
            for (int i = 1; i < arr.size() - 1; i += 2) {
                if (arr[i] > arr[i + 1]) {
                    std::swap(arr[i], arr[i + 1]);
                    sorted = false;
                    phaseSwappedLocal = true;
                }
            }
            
            // Even phase
            for (int i = 0; i < arr.size() - 1; i += 2) {
                if (arr[i] > arr[i + 1]) {
                    std::swap(arr[i], arr[i + 1]);
                    sorted = false;
                    phaseSwappedLocal = true;
                }
            }
            
            auto phaseEnd = std::chrono::high_resolution_clock::now();
            auto duration = std::chrono::duration_cast<std::chrono::microseconds>(
                phaseEnd - phaseStart);
            
            phaseTimes.push_back(duration.count() / 1000.0);  // Convert to milliseconds
            phaseSwapped.push_back(phaseSwappedLocal);
            phase++;
        }
    }
    
    void printAnalysis() const {
        std::cout << "Phase Analysis:\n";
        for (size_t i = 0; i < phaseTimes.size(); i++) {
            std::cout << "Phase " << i + 1 << ": " 
                      << phaseTimes[i] << "ms, "
                      << "Swapped: " << (phaseSwapped[i] ? "Yes" : "No") << std::endl;
        }
    }
    
    double getTotalTime() const {
        double total = 0.0;
        for (double time : phaseTimes) {
            total += time;
        }
        return total;
    }
};
```

## Testing and Verification

### Test Cases
1. **Already sorted array**: Should complete in one phase
2. **Reverse sorted array**: Should handle worst case
3. **Random array**: Should sort correctly
4. **Even/odd sized arrays**: Should handle both
5. **Single element**: Should handle edge case

### Performance Tests
1. **Parallel vs sequential**: Performance comparison
2. **Thread scaling**: Performance with different thread counts
3. **Data size scaling**: Performance on different array sizes
4. **Comparison with bubble sort**: Relative performance

## Common Pitfalls
1. Incorrect phase ordering
2. Off-by-one errors in index calculations
3. Race conditions in parallel implementation
4. Not handling array bounds properly

## Optimization Tips
1. Use parallel processing for large datasets
2. Optimize thread allocation based on data size
3. Consider SIMD operations for comparisons
4. Use efficient synchronization mechanisms

## Real-World Applications
- Parallel computing systems
- Multi-core processors
- GPU computing
- Distributed systems
- Teaching parallel algorithms

## Advantages
- Naturally parallelizable
- Simple to understand
- Good for parallel architectures
- Deterministic behavior

## Disadvantages
- O(n²) time complexity
- Not efficient for sequential execution
- Requires synchronization in parallel versions
- Outperformed by advanced parallel algorithms

## Parallel Processing Benefits

### Natural Parallelization
- Odd and even phases can be parallelized
- Non-overlapping comparisons can run simultaneously
- Scales well with multiple cores
- Suitable for GPU implementation

### Synchronization Considerations
- Need proper locking mechanisms
- Avoid race conditions
- Balance between parallelism and synchronization overhead
- Consider lock-free implementations

## Related Algorithms
- Bubble Sort
- Cocktail Sort
- Brick Sort (alternative name)
- Parallel sorting algorithms

## References
- Parallel algorithm textbooks
- Multi-core programming resources
- GPU computing documentation
- Distributed systems literature

---

*This implementation provides a comprehensive guide to Odd-Even Sort with parallel processing capabilities and performance optimization strategies.*

---

## Next Step

- Go to [17_Bitonic_Sort.md](17_Bitonic_Sort.md) to continue with Bitonic Sort.
