# Search Algorithms in C++

## Overview
This document provides comprehensive theoretical foundations for various search algorithms implemented in C++. From fundamental linear search to advanced searching techniques, each algorithm includes detailed explanations, complexity analysis, pseudocode, and best practices.

## 🎯 Importance of Search Algorithms

Search algorithms are fundamental to computer science and software development because:
- **Data Retrieval**: Essential for accessing information efficiently
- **Performance Impact**: Directly affects application responsiveness
- **Scalability**: Determines how systems handle growing datasets
- **User Experience**: Fast search capabilities improve user satisfaction
- **Resource Optimization**: Efficient algorithms save CPU time and memory

## 📊 Algorithm Classification

### 1. **Comparison-based Searching**
- Linear Search, Binary Search, Jump Search
- Time complexity bounded by Ω(log n) for sorted data

### 2. **Interpolation-based Searching**
- Interpolation Search, Exponential Search
- Exploit data distribution patterns

### 3. **Hash-based Searching**
- Direct addressing, collision resolution
- Average O(1) time complexity

### 4. **Tree-based Searching**
- Binary Search Trees, B-Trees, Tries
- Dynamic data structure support

### 5. **Pattern Matching**
- Sublist Search, String matching algorithms
- Specialized for sequence searching

---

## 🔍 Linear Search

### Theory
Linear search is the simplest searching algorithm that sequentially checks each element in a container until a match is found or the entire container has been searched.

### Algorithm Steps
1. Start from the first element
2. Compare current element with target
3. If match found, return index
4. If not, move to next element
5. Repeat until end or found

### Pseudocode
```
FUNCTION linearSearch(array, target):
    FOR i FROM 0 TO length(array) - 1:
        IF array[i] == target:
            RETURN i
    RETURN -1  // Not found
```

### Complexity Analysis
- **Time Complexity**: O(n) - Worst/average case
- **Space Complexity**: O(1) - No additional space
- **Best Case**: O(1) - Target at first position

### Best Practices
- Use for small datasets (< 100 elements)
- Ideal for unsorted data
- Consider sentinel optimization for large arrays
- Cache-friendly due to sequential access

### When to Use
- Unsorted or dynamically changing data
- Small datasets where overhead isn't justified
- When simplicity and reliability are prioritized
- Linked lists where random access is expensive

---

## 🔎 Binary Search

### Theory
Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing the search interval in half, achieving logarithmic time complexity.

### Mathematical Foundation
Binary search reduces the search space by half each iteration:
- After 1 comparison: n/2 elements remaining
- After 2 comparisons: n/4 elements remaining
- After k comparisons: n/2^k elements remaining
- When n/2^k = 1, we have k = log₂n comparisons

### Algorithm Steps
1. Ensure array is sorted (prerequisite)
2. Find the middle element: mid = left + (right - left) / 2
3. If middle element equals target, return mid
4. If target < middle element, search left half
5. If target > middle element, search right half
6. Repeat until found or search space exhausted

### Pseudocode
```
FUNCTION binarySearch(array, target):
    left = 0
    right = length(array) - 1
    
    WHILE left <= right:
        mid = left + (right - left) / 2  // Prevent overflow
        
        IF array[mid] == target:
            RETURN mid
        ELSE IF array[mid] < target:
            left = mid + 1
        ELSE:
            right = mid - 1
    
    RETURN -1  // Not found
```

### Complexity Analysis
- **Time Complexity**: O(log n) - All cases
- **Space Complexity**: O(1) iterative, O(log n) recursive
- **Best Case**: O(1) - Target at middle element

### Best Practices
- Always verify array is sorted before applying
- Use `left + (right - left) / 2` to prevent integer overflow
- Consider iterative version for production code
- Handle edge cases: empty array, single element

### Variants and Optimizations
- **Lower Bound**: First occurrence of target
- **Upper Bound**: Last occurrence of target
- **Binary Search on Answer**: For optimization problems
- **Exponential Search**: For unbounded arrays

### When to Use
- Large sorted datasets (> 1000 elements)
- Multiple searches on static sorted data
- When logarithmic performance is required
- Range queries and finding boundaries

### Implementation 1: Iterative Binary Search

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Iterative binary search on sorted array
 * Returns index of target if found, -1 otherwise
 */
int binarySearch(int arr[], int size, int target) {
    int left = 0;
    int right = size - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;  // Prevent overflow
        
        if (arr[mid] == target) {
            return mid;  // Target found
        }
        
        if (arr[mid] < target) {
            left = mid + 1;  // Search right half
        } else {
            right = mid - 1;  // Search left half
        }
    }
    
    return -1;  // Target not found
}

int main() {
    int arr[] = {10, 23, 45, 70, 89, 100, 123, 145};
    int size = sizeof(arr) / sizeof(arr[0]);
    int target = 70;
    
    int result = binarySearch(arr, size, target);
    
    if (result != -1) {
        cout << "Element " << target << " found at index: " << result << endl;
    } else {
        cout << "Element " << target << " not found in array" << endl;
    }
    
    return 0;
}
```

**Output:**
```
Element 70 found at index: 3
```

---

### Implementation 2: Recursive Binary Search

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Recursive binary search helper function
 */
int binarySearchRecursive(int arr[], int left, int right, int target) {
    if (left > right) {
        return -1;  // Base case: not found
    }
    
    int mid = left + (right - left) / 2;
    
    if (arr[mid] == target) {
        return mid;  // Base case: found
    }
    
    if (arr[mid] < target) {
        return binarySearchRecursive(arr, mid + 1, right, target);
    } else {
        return binarySearchRecursive(arr, left, mid - 1, target);
    }
}

/**
 * Wrapper function for recursive binary search
 */
int binarySearchRecursive(int arr[], int size, int target) {
    return binarySearchRecursive(arr, 0, size - 1, target);
}

int main() {
    int arr[] = {10, 23, 45, 70, 89, 100, 123, 145};
    int size = sizeof(arr) / sizeof(arr[0]);
    
    // Test cases
    int targets[] = {70, 10, 145, 99};
    
    for (int target : targets) {
        int result = binarySearchRecursive(arr, size, target);
        if (result != -1) {
            cout << "Element " << target << " found at index: " << result << endl;
        } else {
            cout << "Element " << target << " not found in array" << endl;
        }
    }
    
    return 0;
}
```

**Output:**
```
Element 70 found at index: 3
Element 10 found at index: 0
Element 145 found at index: 7
Element 99 not found in array
```

---

### Implementation 3: Binary Search on STL Containers

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/**
 * Binary search using std::binary_search
 * Returns true if element exists, false otherwise
 */
bool binarySearchExists(const vector<int>& vec, int target) {
    return binary_search(vec.begin(), vec.end(), target);
}

/**
 * Find position using lower_bound
 */
int binarySearchPosition(const vector<int>& vec, int target) {
    auto it = lower_bound(vec.begin(), vec.end(), target);
    
    if (it != vec.end() && *it == target) {
        return distance(vec.begin(), it);
    }
    
    return -1;
}

/**
 * Find first and last occurrence of element
 */
pair<int, int> binarySearchRange(const vector<int>& vec, int target) {
    auto lower = lower_bound(vec.begin(), vec.end(), target);
    auto upper = upper_bound(vec.begin(), vec.end(), target);
    
    if (lower != vec.end() && *lower == target) {
        int first = distance(vec.begin(), lower);
        int last = distance(vec.begin(), upper) - 1;
        return {first, last};
    }
    
    return {-1, -1};
}

int main() {
    vector<int> vec = {10, 23, 45, 70, 70, 70, 89, 100, 123, 145};
    
    // Test existence
    int target = 70;
    cout << "Does " << target << " exist? " 
         << (binarySearchExists(vec, target) ? "Yes" : "No") << endl;
    
    // Test position
    int pos = binarySearchPosition(vec, target);
    cout << "First occurrence of " << target << " at index: " << pos << endl;
    
    // Test range
    auto range = binarySearchRange(vec, target);
    if (range.first != -1) {
        cout << target << " appears from index " << range.first 
             << " to " << range.second << endl;
        cout << "Total occurrences: " << (range.second - range.first + 1) << endl;
    }
    
    // Test non-existent element
    int target2 = 99;
    cout << "\nDoes " << target2 << " exist? " 
         << (binarySearchExists(vec, target2) ? "Yes" : "No") << endl;
    
    return 0;
}
```

**Output:**
```
Does 70 exist? Yes
First occurrence of 70 at index: 3
70 appears from index 3 to 5
Total occurrences: 3

Does 99 exist? No
```

---

## 🚀 Jump Search

### Theory
Jump search is an algorithm for searching in sorted arrays. It jumps ahead by fixed steps and then performs linear search within the block, providing a balance between linear and binary search.

### Mathematical Foundation
Optimal block size = √n:
- Number of jumps = √n
- Linear search within block = √n
- Total comparisons = 2√n = O(√n)

### Algorithm Steps
1. Calculate optimal block size: step = √n
2. Jump ahead by block size until current element >= target
3. Perform linear search in the previous block
4. Return index if found, -1 otherwise

### Pseudocode
```
FUNCTION jumpSearch(array, target):
    n = length(array)
    step = sqrt(n)
    prev = 0
    
    // Find the block where element may be present
    WHILE array[min(step, n) - 1] < target:
        prev = step
        step = step + sqrt(n)
        IF prev >= n:
            RETURN -1
    
    // Linear search in the identified block
    WHILE array[prev] < target:
        prev = prev + 1
        IF prev == min(step, n):
            RETURN -1
    
    // Check if element is found
    IF array[prev] == target:
        RETURN prev
    
    RETURN -1
```

### Complexity Analysis
- **Time Complexity**: O(√n) - Optimal block size
- **Space Complexity**: O(1)
- **Best Case**: O(1) - Target at first jump point

### Best Practices
- Use optimal block size √n for best performance
- Better than linear search for medium-sized arrays
- Simpler than binary search but slower
- Good compromise between simplicity and efficiency

---

## 📈 Interpolation Search

### Theory
Interpolation search is an improved variant of binary search for uniformly distributed sorted arrays. It estimates the position of the target value using interpolation formula.

### Mathematical Foundation
Position estimation using linear interpolation:
```
pos = left + ((target - arr[left]) * (right - left)) / (arr[right] - arr[left])
```

For uniformly distributed data, this provides better than logarithmic performance.

### Algorithm Steps
1. Check if target is within array bounds
2. Calculate estimated position using interpolation formula
3. Compare array[pos] with target
4. Adjust search range based on comparison
5. Repeat until found or range is exhausted

### Pseudocode
```
FUNCTION interpolationSearch(array, target):
    left = 0
    right = length(array) - 1
    
    WHILE left <= right AND target >= array[left] AND target <= array[right]:
        IF left == right:
            IF array[left] == target:
                RETURN left
            RETURN -1
        
        // Calculate position using interpolation formula
        pos = left + ((target - array[left]) * (right - left)) / (array[right] - array[left])
        
        IF array[pos] == target:
            RETURN pos
        ELSE IF array[pos] < target:
            left = pos + 1
        ELSE:
            right = pos - 1
    
    RETURN -1
```

### Complexity Analysis
- **Best Case**: O(log log n) - Perfectly uniform distribution
- **Average Case**: O(log log n) - Uniform distribution
- **Worst Case**: O(n) - Non-uniform distribution
- **Space Complexity**: O(1)

### Best Practices
- Only use with uniformly distributed sorted data
- Performance degrades significantly with skewed distributions
- Excellent for numeric sequences with constant differences
- Validate data distribution before using

---

## ⚡ Exponential Search

### Theory
Exponential search is useful for unbounded or infinite arrays. It works by finding a range containing the target and then performing binary search within that range.

### Algorithm Steps
1. Check if first element is the target
2. Find range by doubling index until array[i] >= target
3. Perform binary search between i/2 and min(i, n-1)

### Pseudocode
```
FUNCTION exponentialSearch(array, target):
    n = length(array)
    
    // Check if first element is the target
    IF array[0] == target:
        RETURN 0
    
    // Find range for binary search
    i = 1
    WHILE i < n AND array[i] <= target:
        i = i * 2
    
    // Perform binary search in found range
    RETURN binarySearch(array, i/2, min(i, n-1), target)
```

### Complexity Analysis
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)
- **Best Case**: O(1) - Target at first position

### Best Practices
- Ideal for unbounded or infinite sorted arrays
- Useful when array size is unknown
- More efficient than binary search for targets near beginning
- Combined with binary search for optimal performance

---

## 🌀 Fibonacci Search

### Theory
Fibonacci search is similar to binary search but uses Fibonacci numbers to divide the array, avoiding division operations.

### Mathematical Foundation
Uses Fibonacci sequence to create partition points:
- F(k-2) and F(k-1) create the search intervals
- Eliminates need for division operations
- Useful in systems where division is expensive

### Algorithm Steps
1. Generate Fibonacci numbers until F(k) >= n
2. Compare target with element at index F(k-2)
3. Adjust range based on comparison
4. Update Fibonacci numbers accordingly
5. Repeat until found or exhausted

### Pseudocode
```
FUNCTION fibonacciSearch(array, target):
    n = length(array)
    
    // Initialize Fibonacci numbers
    fibM2 = 0    // (k-2)th Fibonacci
    fibM1 = 1    // (k-1)th Fibonacci
    fibM = fibM2 + fibM1  // kth Fibonacci
    
    // Find smallest Fibonacci >= n
    WHILE fibM < n:
        fibM2 = fibM1
        fibM1 = fibM
        fibM = fibM2 + fibM1
    
    // Mark the eliminated range
    offset = -1
    
    WHILE fibM > 1:
        i = min(offset + fibM2, n - 1)
        
        IF array[i] < target:
            fibM = fibM1
            fibM1 = fibM2
            fibM2 = fibM - fibM1
            offset = i
        ELSE IF array[i] > target:
            fibM = fibM2
            fibM1 = fibM1 - fibM2
            fibM2 = fibM - fibM1
        ELSE:
            RETURN i
    
    // Check for last element
    IF fibM1 AND offset + 1 < n AND array[offset + 1] == target:
        RETURN offset + 1
    
    RETURN -1
```

### Complexity Analysis
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)
- **Best Case**: O(1)

### Best Practices
- Use when division operations are expensive
- Suitable for embedded systems with limited arithmetic
- Provides similar performance to binary search
- Cache-friendly access pattern

---

## 🔺 Ternary Search

### Theory
Ternary search divides the array into three parts instead of two, useful for unimodal functions and finding peaks in sorted arrays.

### Algorithm Steps
1. Divide array into three parts using two mid points
2. Compare target with both mid points
3. Eliminate two-thirds of the array based on comparisons
4. Repeat until found

### Pseudocode
```
FUNCTION ternarySearch(array, target):
    left = 0
    right = length(array) - 1
    
    WHILE left <= right:
        third = (right - left) / 3
        mid1 = left + third
        mid2 = right - third
        
        IF array[mid1] == target:
            RETURN mid1
        ELSE IF array[mid2] == target:
            RETURN mid2
        ELSE IF target < array[mid1]:
            right = mid1 - 1
        ELSE IF target > array[mid2]:
            left = mid2 + 1
        ELSE:
            left = mid1 + 1
            right = mid2 - 1
    
    RETURN -1
```

### Complexity Analysis
- **Time Complexity**: O(log₃ n) ≈ O(log n)
- **Space Complexity**: O(1)
- **Best Case**: O(1)

### Best Practices
- Useful for finding peaks in unimodal functions
- More comparisons per iteration than binary search
- Better for functions with single peak/valley
- Not generally better than binary search for simple searching

---

## 🎯 Hash Table Search

### Theory
Hash tables provide O(1) average time complexity for search operations using key-value pairs and hash functions.

### Mathematical Foundation
Hash function: h(key) → index
Collision resolution strategies:
- **Chaining**: Linked lists at each bucket
- **Open Addressing**: Probing sequences

### Algorithm Steps
1. Compute hash of target key
2. Access bucket at computed index
3. Handle collisions if necessary
4. Search within bucket for exact match

### Pseudocode
```
FUNCTION hashSearch(hashTable, key):
    index = hashFunction(key)
    
    // Handle collisions (chaining example)
    current = hashTable[index]
    WHILE current != null:
        IF current.key == key:
            RETURN current.value
        current = current.next
    
    RETURN null  // Not found
```

### Complexity Analysis
- **Average Case**: O(1) - Good hash function, low load factor
- **Worst Case**: O(n) - All elements hash to same bucket
- **Space Complexity**: O(n)

### Best Practices
- Choose appropriate hash function for data distribution
- Maintain load factor < 0.75 for performance
- Handle collisions efficiently
- Consider rehashing when table grows

---

## 🌳 Tree Search (BST)

### Theory
Binary Search Trees provide dynamic searching with O(log n) average time complexity, supporting insertions and deletions.

### Mathematical Foundation
BST property: left subtree < node < right subtree
Height determines performance: balanced = O(log n), unbalanced = O(n)

### Algorithm Steps
1. Start at root
2. Compare target with current node
3. If equal, return node
4. If target < node, search left subtree
5. If target > node, search right subtree

### Pseudocode
```
FUNCTION bstSearch(root, target):
    current = root
    
    WHILE current != null:
        IF target == current.value:
            RETURN current
        ELSE IF target < current.value:
            current = current.left
        ELSE:
            current = current.right
    
    RETURN null  // Not found
```

### Complexity Analysis
- **Average Case**: O(log n) - Balanced tree
- **Worst Case**: O(n) - Skewed tree
- **Space Complexity**: O(1) iterative, O(log n) recursive

### Best Practices
- Use self-balancing trees (AVL, Red-Black) for guaranteed performance
- Consider B-Trees for disk-based storage
- Implement proper balancing strategies
- Handle duplicate values consistently

---

## 🧩 Sublist Search

### Theory
Sublist search finds a pattern list within a larger list, useful for pattern matching and sequence detection.

### Algorithm Steps
1. Align pattern with start of main list
2. Compare elements one by one
3. If mismatch, shift pattern by one position
4. Repeat until match found or end reached

### Pseudocode
```
FUNCTION sublistSearch(mainList, pattern):
    n = length(mainList)
    m = length(pattern)
    
    FOR i FROM 0 TO n - m:
        match = true
        FOR j FROM 0 TO m - 1:
            IF mainList[i + j] != pattern[j]:
                match = false
                BREAK
        
        IF match:
            RETURN i  // Pattern found at position i
    
    RETURN -1  // Pattern not found
```

### Complexity Analysis
- **Average Case**: O(n + m)
- **Worst Case**: O(n × m)
- **Space Complexity**: O(1)

### Best Practices
- Use KMP algorithm for better worst-case performance
- Consider Rabin-Karp for rolling hash approach
- Optimize for specific pattern characteristics
- Handle edge cases (empty pattern, pattern larger than text)

---

## 📋 Comprehensive Algorithm Comparison

### Decision Matrix

| Algorithm | Data Type | Sorted | Size Range | Stability | Memory | Best Use Case |
|-----------|-----------|--------|------------|-----------|---------|---------------|
| Linear | Any | No | Small (<100) | N/A | O(1) | Unsorted data |
| Binary | Comparable | Yes | Large (>1000) | N/A | O(1) | Static sorted data |
| Jump | Comparable | Yes | Medium (100-10000) | N/A | O(1) | Simple alternative to binary |
| Interpolation | Numeric | Yes | Large, uniform | N/A | O(1) | Uniformly distributed |
| Exponential | Comparable | Yes | Unknown/Infinite | N/A | O(1) | Unbounded arrays |
| Fibonacci | Comparable | Yes | Large | N/A | O(1) | Division-optimized |
| Ternary | Comparable | Yes | Large | N/A | O(1) | Unimodal functions |
| Hash | Hashable | No | Any | N/A | O(n) | Frequent lookups |
| BST | Comparable | Self-sorting | Dynamic | N/A | O(n) | Dynamic data |
| Sublist | Sequence | No | Pattern matching | N/A | O(1) | Pattern detection |

### Performance Guidelines

1. **Small datasets (< 100)**: Linear search is often fastest due to cache efficiency
2. **Medium datasets (100-10000)**: Binary search or jump search
3. **Large datasets (> 10000)**: Binary search, hash tables, or balanced trees
4. **Static data**: Binary search on pre-sorted arrays
5. **Dynamic data**: Hash tables or balanced BSTs
6. **Uniform distribution**: Interpolation search outperforms binary
7. **Frequent insertions/deletions**: Hash tables or balanced trees
8. **Memory constraints**: In-place algorithms (binary, jump, linear)

---

## 🚀 Advanced Topics and Optimizations

### 1. **Hybrid Approaches**
- Interpolation + Binary for non-uniform data
- Jump + Linear for cache optimization
- Hash + Tree for collision resolution

### 2. **Parallel Search**
- Multi-threaded linear search
- Parallel binary search
- Distributed hash tables

### 3. **Cache-Optimized Search**
- Block search for better cache utilization
- Prefetching strategies
- SIMD optimizations

### 4. **Probabilistic Search**
- Bloom filters for membership testing
- Skip lists for probabilistic balancing
- Locality-sensitive hashing

### 5. **External Memory Search**
- B-Trees for disk-based storage
- Buffer tree techniques
- External memory binary search

---

## 🎯 Best Practices Summary

### General Guidelines
1. **Profile before optimizing**: Measure actual performance
2. **Consider data characteristics**: Size, distribution, update frequency
3. **Handle edge cases**: Empty inputs, single elements, duplicates
4. **Validate assumptions**: Ensure preconditions are met
5. **Document trade-offs**: Space vs time, simplicity vs performance

### Implementation Tips
1. **Use appropriate data structures**: Arrays, vectors, trees, hash tables
2. **Optimize for common case**: Most frequent access patterns
3. **Consider memory hierarchy**: Cache, RAM, disk
4. **Implement robust error handling**: Invalid inputs, overflow
5. **Write comprehensive tests**: Edge cases, performance benchmarks

### When to Choose Which Algorithm

**Choose Linear Search when:**
- Dataset is small (< 100 elements)
- Data is unsorted and sorting is expensive
- Simplicity and reliability are priorities
- Cache performance is critical

**Choose Binary Search when:**
- Data is sorted or can be sorted once
- Multiple searches will be performed
- Logarithmic performance is required
- Memory usage must be minimal

**Choose Hash Table when:**
- Average O(1) performance is needed
- Data is dynamic with frequent updates
- Keys can be effectively hashed
- Memory overhead is acceptable

**Choose Balanced Tree when:**
- Data must remain sorted
- Range queries are needed
- Memory is constrained (compared to hash tables)
- Ordered traversal is required

---

*This comprehensive guide provides the theoretical foundation for understanding and implementing search algorithms effectively in C++. The choice of algorithm depends on your specific requirements, data characteristics, and performance constraints.*

---

## Algorithm Comparison Summary

| Algorithm | Time Complexity | Space Complexity | Best For | Requires Sorted |
|-----------|----------------|------------------|----------|-----------------|
| Linear Search | O(n) | O(1) | Small/unsorted data | ❌ No |
| Binary Search | O(log n) | O(1) | Large sorted data | ✅ Yes |
| Jump Search | O(√n) | O(1) | Medium sorted arrays | ✅ Yes |
| Interpolation Search | O(log log n) | O(1) | Uniform distributed data | ✅ Yes |
| Exponential Search | O(log n) | O(1) | Unbounded arrays | ✅ Yes |
| Fibonacci Search | O(log n) | O(1) | Educational purposes | ✅ Yes |
| Ternary Search | O(log n) | O(1) | Unimodal functions | ✅ Yes |
| Hash Table Search | O(1) avg, O(n) worst | O(n) | Frequent lookups | ❌ No |
| BST Search | O(log n) avg, O(n) worst | O(n) | Dynamic data | ❌ No |

---

## Choosing the Right Search Algorithm

### Decision Guide

1. **Is your data sorted?**
   - **No**: Use Linear Search or Hash Table
   - **Yes**: Consider Binary Search or its variants

2. **How large is your dataset?**
   - **Small (< 100)**: Linear Search is fine
   - **Medium (100-10,000)**: Binary Search if sorted
   - **Large (> 10,000)**: Binary Search or Hash Table

3. **How frequent are searches?**
   - **Rare**: Simple Linear Search
   - **Frequent**: Build Hash Table or maintain sorted data

4. **Is data uniformly distributed?**
   - **Yes**: Interpolation Search
   - **No**: Binary Search

5. **Do you need dynamic insertions/deletions?**
   - **Yes**: BST or Hash Table
   - **No**: Array with Binary Search

---

## Best Practices

1. **Use STL algorithms** - `std::find`, `std::binary_search`, `std::lower_bound`
2. **Prefer hash tables** for frequent lookups
3. **Keep data sorted** if you need fast searches
4. **Consider cache locality** - Linear search can be faster for small datasets
5. **Profile your code** - Theoretical complexity isn't everything
6. **Handle edge cases** - Empty arrays, single elements, duplicates

---

## Common Pitfalls

1. **Using binary search on unsorted data** - Will give incorrect results
2. **Not handling integer overflow** in mid calculation
3. **Ignoring worst-case scenarios** in hash tables
4. **Not checking bounds** in array access
5. **Using wrong algorithm for data distribution**

---

## Conclusion

Search algorithms are fundamental to computer science, and choosing the right one can significantly impact performance. Consider your data characteristics, access patterns, and performance requirements when selecting a search algorithm.

**Key Takeaways:**
- Linear search for small/unsorted data
- Binary search for sorted data
- Hash tables for O(1) average lookups
- Specialized searches for specific distributions
- Always consider the trade-offs between time and space complexity
---

## Next Step

- Go to [Linear Search](./01_Linear_Search.md) to continue.
