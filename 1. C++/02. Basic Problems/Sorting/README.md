# Sorting Algorithms in C++

This directory contains comprehensive implementations of various sorting algorithms in C++, along with theoretical explanations, complexity analysis, and practical examples.

## Directory Structure

```
Sorting/
├── README.md                    # This file - Overview and guide
├── Sorting_Algorithms.md       # Complete reference with all algorithms
├── Bubble_Sort.md              # Bubble sort and its variants
├── Quick_Sort.md               # Quick sort with optimizations
└── [More algorithms to be added]
```

## Available Algorithms

### 1. Bubble Sort
- **File**: `Bubble_Sort.md`
- **Complexity**: O(n²) time, O(1) space
- **Best for**: Educational purposes, small datasets, nearly sorted data
- **Variants**: Basic, optimized, recursive, template, cocktail shaker

### 2. Quick Sort
- **File**: `Quick_Sort.md`
- **Complexity**: O(n log n) average, O(n²) worst, O(log n) space
- **Best for**: Large datasets, general-purpose sorting
- **Variants**: Lomuto/Hoare partition, randomized, iterative, hybrid

### 3. Selection Sort
- **File**: `Selection_Sort.md`
- **Complexity**: O(n²) time, O(1) space
- **Best for**: Small datasets, memory constraints
- **Variants**: Stable, bidirectional, template implementations

### 4. Insertion Sort
- **File**: `Insertion_Sort.md`
- **Complexity**: O(n²) average, O(n) best, O(1) space
- **Best for**: Small datasets, nearly sorted data, online sorting
- **Variants**: Binary, recursive, adaptive, performance optimized

### 5. Merge Sort
- **File**: `Merge_Sort.md`
- **Complexity**: O(n log n) time, O(n) space
- **Best for**: Stable sorting, external sorting, linked lists
- **Variants**: In-place, iterative, bottom-up, external sorting

### 6. Heap Sort
- **File**: `Heap_Sort.md`
- **Complexity**: O(n log n) time, O(1) space
- **Best for**: In-place sorting, priority queues
- **Variants**: Min/max heap, iterative, template implementations

### 7. Counting Sort
- **File**: `Counting_Sort.md`
- **Complexity**: O(n + k) time, O(k) space
- **Best for**: Integers with limited range
- **Variants**: Stable, characters, strings, optimized versions

### 8. Radix Sort
- **File**: `Radix_Sort.md`
- **Complexity**: O(d × (n + k)) time, O(n + k) space
- **Best for**: Fixed-size integers, strings
- **Variants**: Different bases, strings, LSD/MSD, negative numbers

### 9. Bucket Sort
- **File**: `Bucket_Sort.md`
- **Complexity**: O(n + k) average, O(n²) worst, O(n + k) space
- **Best for**: Uniformly distributed data, floating-point numbers
- **Variants**: Adaptive, dynamic, parallel, real-world applications

### 10. Shell Sort
- **File**: `Shell_Sort.md`
- **Complexity**: O(n^1.3) average, O(n²) worst, O(1) space
- **Best for**: Medium-sized arrays, in-place improvement
- **Variants**: Different gap sequences, adaptive, optimized

## Algorithm Comparison

| Algorithm | Best Time | Average Time | Worst Time | Space | Stable | In-Place |
|-----------|-----------|--------------|------------|-------|--------|----------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | ❌ | ✅ |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ | ❌ |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ | ✅ |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ | ✅ |
| Counting Sort | O(n + k) | O(n + k) | O(n + k) | O(k) | ✅ | ❌ |
| Radix Sort | O(d × (n + k)) | O(d × (n + k)) | O(d × (n + k)) | O(n + k) | ✅ | ❌ |
| Bucket Sort | O(n + k) | O(n + k) | O(n²) | O(n + k) | ✅ | ❌ |
| Shell Sort | O(n log n) | O(n^1.3) | O(n²) | O(1) | ❌ | ✅ |

## Choosing the Right Sorting Algorithm

### Decision Flow

1. **Is data nearly sorted?**
   - **Yes**: Insertion Sort or Bubble Sort
   - **No**: Continue to step 2

2. **Is stability required?**
   - **Yes**: Merge Sort, Counting Sort, Radix Sort, Bucket Sort
   - **No**: Quick Sort, Heap Sort, Shell Sort

3. **Is memory a constraint?**
   - **Yes**: In-place sorts (Heap Sort, Quick Sort, Shell Sort)
   - **No**: Merge Sort, Counting Sort, Radix Sort

4. **What is the data type?**
   - **Integers with limited range**: Counting Sort
   - **Integers with many digits**: Radix Sort
   - **Floating point**: Bucket Sort
   - **General**: Quick Sort, Merge Sort, Heap Sort

5. **How large is the dataset?**
   - **Small (< 50)**: Insertion Sort, Selection Sort, Bubble Sort
   - **Medium (50-1000)**: Shell Sort, Quick Sort
   - **Large (> 1000)**: Merge Sort, Quick Sort, Heap Sort

### Quick Reference

| Scenario | Recommended Algorithm |
|----------|----------------------|
| Small array (< 50) | Insertion Sort |
| Nearly sorted | Insertion Sort, Bubble Sort |
| Stability required | Merge Sort, Counting Sort |
| Memory constrained | Heap Sort, Quick Sort |
| Average performance critical | Quick Sort (with random pivot) |
| Worst-case guarantee needed | Heap Sort, Merge Sort |
| Integers, small range | Counting Sort |
| Integers, large range | Radix Sort |
| Floating point, uniform | Bucket Sort |
| General purpose | Quick Sort or std::sort |

## Quick Reference Implementations

### Bubble Sort
```cpp
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break;
    }
}
```

### Quick Sort
```cpp
int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
```

### Merge Sort
```cpp
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    int L[n1], R[n2];
    
    for (int i = 0; i < n1; i++) L[i] = arr[left + i];
    for (int j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];
    
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}
```

## Performance Tips

1. **Use STL algorithms** - `std::sort`, `std::stable_sort`, `std::partial_sort`
2. **Choose based on data characteristics** - Size, distribution, type
3. **Consider hybrid approaches** - Quick sort + insertion sort
4. **Profile before optimizing** - Measure actual performance
5. **Handle edge cases** - Empty arrays, single elements, duplicates
6. **Use appropriate pivot selection** - Random, median-of-three

## Common Pitfalls to Avoid

1. **Using O(n²) algorithms on large datasets**
2. **Not considering stability requirements**
3. **Ignoring space complexity constraints**
4. **Poor pivot selection in quick sort**
5. **Not testing with edge cases**
6. **Choosing based on best-case instead of average-case**

## Best Practices

1. **Always validate input** - Check for empty arrays, null pointers
2. **Use appropriate return values** - Consider error handling
3. **Consider const correctness** - Use const references when possible
4. **Document assumptions** - State if data must be sorted
5. **Write unit tests** - Test edge cases and typical scenarios
6. **Use templates** for generic implementations
7. **Optimize for the common case** - Most frequent data patterns

## Advanced Topics

### Hybrid Algorithms
- **Intro Sort**: Quick sort + Heap sort + Insertion sort
- **Tim Sort**: Merge sort + Insertion sort (used in Python)
- **Block Sort**: Merge sort variant with better cache performance

### Parallel Sorting
- **Parallel Quick Sort**: Multi-threaded partitioning
- **Parallel Merge Sort**: Divide and conquer with threads
- **Sample Sort**: Parallel version of bucket sort

### External Sorting
- **External Merge Sort**: For data that doesn't fit in memory
- **Replacement Selection**: For generating initial runs

### Stable In-Place Sorting
- **Block Merge Sort**: O(1) space stable merge sort
- **Grail Sort**: Stable in-place sorting

## Testing Your Implementation

```cpp
#include <cassert>
#include <vector>
#include <algorithm>

void testSortingAlgorithm(auto sortFunc) {
    // Test empty array
    std::vector<int> empty;
    sortFunc(empty.data(), 0, empty.size() - 1);
    assert(empty.empty());
    
    // Test single element
    std::vector<int> single = {42};
    sortFunc(single.data(), 0, single.size() - 1);
    assert(single == std::vector<int>{42});
    
    // Test sorted array
    std::vector<int> sorted = {1, 2, 3, 4, 5};
    std::vector<int> sortedCopy = sorted;
    sortFunc(sorted.data(), 0, sorted.size() - 1);
    assert(sorted == sortedCopy);
    
    // Test reverse sorted
    std::vector<int> reverse = {5, 4, 3, 2, 1};
    sortFunc(reverse.data(), 0, reverse.size() - 1);
    assert(reverse == sortedCopy);
    
    // Test random array
    std::vector<int> random = {3, 1, 4, 1, 5, 9, 2, 6};
    std::vector<int> randomSorted = random;
    std::sort(randomSorted.begin(), randomSorted.end());
    sortFunc(random.data(), 0, random.size() - 1);
    assert(random == randomSorted);
    
    // Test with duplicates
    std::vector<int> duplicates = {2, 3, 2, 1, 3, 1, 2};
    std::vector<int> dupSorted = duplicates;
    std::sort(dupSorted.begin(), dupSorted.end());
    sortFunc(duplicates.data(), 0, duplicates.size() - 1);
    assert(duplicates == dupSorted);
}
```

## Contributing

When adding new sorting algorithms:

1. Follow the existing documentation format
2. Include complexity analysis
3. Provide multiple implementation variants
4. Add performance comparisons
5. Include test cases and edge cases
6. Document when to use the algorithm
7. Consider stability and space complexity

## Resources

- [GeeksforGeeks - Sorting Algorithms](https://www.geeksforgeeks.org/sorting-algorithms/)
- [CPPReference - Algorithms](https://en.cppreference.com/w/cpp/algorithm)
- [Introduction to Algorithms (CLRS)](https://en.wikipedia.org/wiki/Introduction_to_Algorithms)
- [The Art of Computer Programming - Volume 3](https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming)

## Quick Start

1. **Begin with Bubble Sort** - Simple and educational
2. **Move to Insertion Sort** - Good for nearly sorted data
3. **Learn Quick Sort** - Most practical algorithm
4. **Explore Merge Sort** - When stability is needed
5. **Study advanced algorithms** - For specific use cases

Happy sorting! 🚀
