# Search Algorithms in C++

This directory contains comprehensive implementations of various search algorithms in C++, along with theoretical explanations, complexity analysis, and practical examples.

## Directory Structure

```
Search/
├── README.md                    # This file - Overview and guide
├── Search_Algorithms.md         # Complete reference with all algorithms
├── Linear_Search.md            # Linear search with detailed implementations
├── Binary_Search.md            # Binary search and its variants
├── Jump_Search.md              # Jump search algorithm
├── Interpolation_Search.md     # Interpolation search for uniform data
└── [More algorithms to be added]
```

## Available Algorithms

### 1. Linear Search
- **File**: `Linear_Search.md`
- **Complexity**: O(n) time, O(1) space
- **Best for**: Small datasets, unsorted data
- **Variants**: Basic, recursive, sentinel, STL-style, linked list

### 2. Binary Search
- **File**: `Binary_Search.md`
- **Complexity**: O(log n) time, O(1) space
- **Best for**: Large sorted datasets
- **Variants**: Iterative, recursive, STL containers, templates, matrix search

### 3. Jump Search
- **File**: `Jump_Search.md`
- **Complexity**: O(√n) time, O(1) space
- **Best for**: Medium-sized sorted arrays
- **Variants**: Custom block size, vector implementation, performance comparison

### 4. Interpolation Search
- **File**: `Interpolation_Search.md`
- **Complexity**: O(log log n) average, O(n) worst
- **Best for**: Uniformly distributed data
- **Variants**: Template version, floating-point support, error handling

## Algorithm Comparison

| Algorithm | Time Complexity | Space | Data Required | Best Use Case |
|-----------|----------------|-------|---------------|--------------|
| Linear Search | O(n) | O(1) | Unsorted | Small datasets, unsorted data |
| Binary Search | O(log n) | O(1) | Sorted | Large sorted datasets |
| Jump Search | O(√n) | O(1) | Sorted | Medium-sized arrays |
| Interpolation Search | O(log log n) avg, O(n) worst | O(1) | Sorted, Uniform | Uniformly distributed data |
| Hash Table Search | O(1) avg, O(n) worst | O(n) | Any | Frequent lookups |

## Choosing the Right Algorithm

### Decision Flow

1. **Is your data sorted?**
   - **No**: Use Linear Search or build a Hash Table
   - **Yes**: Continue to step 2

2. **How large is your dataset?**
   - **Small (< 100)**: Linear Search is fine
   - **Medium (100-10,000)**: Jump Search or Binary Search
   - **Large (> 10,000)**: Binary Search or Interpolation Search

3. **Is data uniformly distributed?**
   - **Yes**: Interpolation Search (fastest)
   - **No**: Binary Search (reliable)

4. **How frequent are searches?**
   - **Rare**: Simple search is fine
   - **Frequent**: Consider Hash Table or maintain sorted data

## Quick Reference

### Linear Search
```cpp
int linearSearch(int arr[], int size, int target) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}
```

### Binary Search
```cpp
int binarySearch(int arr[], int size, int target) {
    int left = 0, right = size - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
```

### Jump Search
```cpp
int jumpSearch(int arr[], int size, int target) {
    int step = sqrt(size), prev = 0;
    while (arr[min(step, size)-1] < target) {
        prev = step;
        step += sqrt(size);
    }
    for (int i = prev; i < min(step, size); i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}
```

### Interpolation Search
```cpp
int interpolationSearch(int arr[], int size, int target) {
    int left = 0, right = size - 1;
    while (left <= right && target >= arr[left] && target <= arr[right]) {
        int pos = left + ((target - arr[left]) * (right - left)) / (arr[right] - arr[left]);
        if (arr[pos] == target) return pos;
        if (arr[pos] < target) left = pos + 1;
        else right = pos - 1;
    }
    return -1;
}
```

## Performance Tips

1. **Use STL algorithms**: `std::find`, `std::binary_search`, `std::lower_bound`
2. **Prefer hash tables** for frequent lookups
3. **Consider cache locality** - Linear search can be faster for small datasets
4. **Profile your code** - Theoretical complexity isn't everything
5. **Handle edge cases**: Empty arrays, single elements, duplicates

## Common Pitfalls to Avoid

1. **Using binary search on unsorted data**
2. **Integer overflow** in mid/position calculation
3. **Off-by-one errors** in loop conditions
4. **Not handling duplicates** correctly
5. **Wrong algorithm choice** for data distribution

## Best Practices

1. **Always validate input** - Check for empty arrays, null pointers
2. **Use appropriate return values** - -1 for not found, index for found
3. **Consider const correctness** - Use const references when possible
4. **Document assumptions** - State if data must be sorted
5. **Write unit tests** - Test edge cases and typical scenarios

## Advanced Topics

### Multi-dimensional Search
- Binary search in 2D matrices
- Search in tree structures
- Graph search algorithms

### Parallel Search
- Multi-threaded linear search
- Parallel binary search
- GPU-accelerated search

### Optimized Variants
- Exponential search
- Fibonacci search
- Ternary search
- Probabilistic search

## Testing Your Implementation

```cpp
#include <cassert>
#include <vector>

void testSearchAlgorithm(auto searchFunc) {
    std::vector<int> arr = {10, 20, 30, 40, 50};
    
    // Test existing elements
    assert(searchFunc(arr, 30) == 2);
    assert(searchFunc(arr, 10) == 0);
    assert(searchFunc(arr, 50) == 4);
    
    // Test non-existing element
    assert(searchFunc(arr, 35) == -1);
    
    // Test empty array
    std::vector<int> empty;
    assert(searchFunc(empty, 10) == -1);
    
    // Test single element
    std::vector<int> single = {42};
    assert(searchFunc(single, 42) == 0);
    assert(searchFunc(single, 10) == -1);
}
```

## Contributing

When adding new search algorithms:

1. Follow the existing documentation format
2. Include complexity analysis
3. Provide multiple implementation variants
4. Add performance comparisons
5. Include test cases and edge cases
6. Document when to use the algorithm

## Resources

- [GeeksforGeeks - Searching Algorithms](https://www.geeksforgeeks.org/searching-algorithms/)
- [CPPReference - Algorithms](https://en.cppreference.com/w/cpp/algorithm)
- [Introduction to Algorithms (CLRS)](https://en.wikipedia.org/wiki/Introduction_to_Algorithms)

## Quick Start

1. **Begin with Linear Search** - Simple and works everywhere
2. **Move to Binary Search** - Most common for sorted data
3. **Explore specialized searches** - Jump, Interpolation for specific cases
4. **Practice with problems** - Implement variations and optimizations

Happy searching! 🚀
