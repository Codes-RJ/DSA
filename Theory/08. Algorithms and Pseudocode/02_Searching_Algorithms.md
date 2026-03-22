# Searching Algorithms

## Overview

Searching algorithms are designed to retrieve information stored within some data structure, or calculated in the search space of a problem domain. Understanding different searching techniques is crucial for efficient data retrieval and problem-solving.

## Linear Search

### Algorithm Description
```text
Linear search sequentially checks each element in the data structure until the target
is found or the end is reached.

Characteristics:
- Works on unsorted data
- Simple to implement
- Guaranteed to find the element if it exists
- Time complexity: O(n)
- Space complexity: O(1)
```

### Pseudocode
```text
ALGORITHM LinearSearch(A[0..n-1], target)
BEGIN
    FOR i ← 0 TO n-1 DO
        IF A[i] = target THEN
            RETURN i  // Found at index i
        END IF
    END FOR
    
    RETURN -1  // Not found
END
```

### Implementation Examples
```python
# Python Implementation
def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

# C++ Implementation
int linearSearch(const vector<int>& arr, int target) {
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}

# Java Implementation
int linearSearch(int[] arr, int target) {
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}
```

### Variations and Optimizations
```text
1. Sentinel Linear Search:
   - Add target value at the end as sentinel
   - Eliminates boundary check in loop
   - Slightly faster in practice

2. Transposition Search:
   - Move found element one position forward
   - Frequently accessed items bubble to front
   - Useful for non-uniform access patterns

3. Move-to-Front Search:
   - Move found element to front
   - Optimal for repeated searches
   - Adapts to access patterns
```

## Binary Search

### Algorithm Description
```text
Binary search works on sorted arrays by repeatedly dividing the search interval in half.
If the target value is less than the middle element, search the left half; otherwise,
search the right half.

Characteristics:
- Requires sorted data
- Much faster than linear search
- Time complexity: O(log n)
- Space complexity: O(1) iterative, O(log n) recursive
```

### Pseudocode (Iterative)
```text
ALGORITHM BinarySearch(A[0..n-1], target)
BEGIN
    left ← 0
    right ← n-1
    
    WHILE left ≤ right DO
        mid ← left + (right - left) / 2  // Avoid overflow
        
        IF A[mid] = target THEN
            RETURN mid
        ELSE IF A[mid] < target THEN
            left ← mid + 1
        ELSE
            right ← mid - 1
        END IF
    END WHILE
    
    RETURN -1  // Not found
END
```

### Pseudocode (Recursive)
```text
ALGORITHM BinarySearchRecursive(A[left..right], target)
BEGIN
    IF left > right THEN
        RETURN -1
    END IF
    
    mid ← left + (right - left) / 2
    
    IF A[mid] = target THEN
        RETURN mid
    ELSE IF A[mid] < target THEN
        RETURN BinarySearchRecursive(A[mid+1..right], target)
    ELSE
        RETURN BinarySearchRecursive(A[left..mid-1], target)
    END IF
END
```

### Implementation Examples
```python
# Python Implementation (Iterative)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Python Implementation (Recursive)
def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
```

### Binary Search Variations
```text
1. Lower Bound (First Occurrence):
   - Find first index where element ≥ target
   - Useful for finding first occurrence in sorted array with duplicates

2. Upper Bound (Last Occurrence):
   - Find first index where element > target
   - Useful for finding last occurrence in sorted array with duplicates

3. Binary Search on Answer:
   - Search in solution space instead of data space
   - Used for optimization problems
```

### Lower and Upper Bound Pseudocode
```text
ALGORITHM LowerBound(A[0..n-1], target)
BEGIN
    left ← 0
    right ← n
    
    WHILE left < right DO
        mid ← left + (right - left) / 2
        
        IF A[mid] < target THEN
            left ← mid + 1
        ELSE
            right ← mid
        END IF
    END WHILE
    
    RETURN left
END

ALGORITHM UpperBound(A[0..n-1], target)
BEGIN
    left ← 0
    right ← n
    
    WHILE left < right DO
        mid ← left + (right - left) / 2
        
        IF A[mid] ≤ target THEN
            left ← mid + 1
        ELSE
            right ← mid
        END IF
    END WHILE
    
    RETURN left
END
```

## Jump Search

### Algorithm Description
```text
Jump search works by jumping ahead by fixed steps and then performing linear search
in the backward direction when the target is surpassed.

Characteristics:
- Requires sorted data
- Better than linear search, worse than binary search
- Optimal when jumping to next block is expensive
- Time complexity: O(√n)
- Space complexity: O(1)
```

### Pseudocode
```text
ALGORITHM JumpSearch(A[0..n-1], target)
BEGIN
    step ← √n
    prev ← 0
    
    // Find the block where element could be
    WHILE A[min(step, n)-1] < target DO
        prev ← step
        step ← step + √n
        IF prev ≥ n THEN
            RETURN -1  // Not found
        END IF
    END WHILE
    
    // Linear search in identified block
    FOR i ← prev TO min(step, n)-1 DO
        IF A[i] = target THEN
            RETURN i
        END IF
    END FOR
    
    RETURN -1  // Not found
END
```

### Implementation Example
```python
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    # Find the block where element could be
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Linear search in identified block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    
    return -1
```

## Interpolation Search

### Algorithm Description
```text
Interpolation search is an improved variant of binary search for uniformly distributed
sorted arrays. It estimates the position based on the target value's relative position
between the first and last elements.

Characteristics:
- Requires sorted and uniformly distributed data
- Faster than binary search for uniform distributions
- Time complexity: O(log log n) average, O(n) worst
- Space complexity: O(1)
```

### Pseudocode
```text
ALGORITHM InterpolationSearch(A[0..n-1], target)
BEGIN
    left ← 0
    right ← n-1
    
    WHILE left ≤ right AND target ≥ A[left] AND target ≤ A[right] DO
        // Estimate position
        pos ← left + ((target - A[left]) * (right - left)) / (A[right] - A[left])
        
        IF A[pos] = target THEN
            RETURN pos
        ELSE IF A[pos] < target THEN
            left ← pos + 1
        ELSE
            right ← pos - 1
        END IF
    END WHILE
    
    RETURN -1  // Not found
END
```

### Implementation Example
```python
def interpolation_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right and target >= arr[left] and target <= arr[right]:
        if left == right:
            return left if arr[left] == target else -1
        
        # Estimate position
        pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    
    return -1
```

## Exponential Search

### Algorithm Description
```text
Exponential search finds the range where the target might be present by exponentially
increasing the search interval, then performs binary search in that range.

Characteristics:
- Requires sorted data
- Useful for infinite or unbounded sorted arrays
- Time complexity: O(log n)
- Space complexity: O(1)
```

### Pseudocode
```text
ALGORITHM ExponentialSearch(A[0..n-1], target)
BEGIN
    IF n = 1 THEN
        RETURN 0 IF A[0] = target ELSE -1
    END IF
    
    i ← 1
    WHILE i < n AND A[i] ≤ target DO
        i ← i * 2
    END WHILE
    
    // Binary search in found range
    left ← i / 2
    right ← min(i, n-1)
    
    RETURN BinarySearch(A[left..right], target)
END
```

### Implementation Example
```python
def exponential_search(arr, target):
    n = len(arr)
    
    if n == 0:
        return -1
    
    if arr[0] == target:
        return 0
    
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    
    # Binary search in found range
    left, right = i // 2, min(i, n - 1)
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

## Fibonacci Search

### Algorithm Description
```text
Fibonacci search divides the array into unequal parts using Fibonacci numbers.
It's similar to binary search but uses Fibonacci indices to divide the search space.

Characteristics:
- Requires sorted data
- No division operation (uses addition/subtraction)
- Time complexity: O(log n)
- Space complexity: O(1)
```

### Pseudocode
```text
ALGORITHM FibonacciSearch(A[0..n-1], target)
BEGIN
    // Initialize fibonacci numbers
    fibM2 ← 0
    fibM1 ← 1
    fibM ← fibM1 + fibM2
    
    // Find smallest fibonacci number >= n
    WHILE fibM < n DO
        fibM2 ← fibM1
        fibM1 ← fibM
        fibM ← fibM1 + fibM2
    END WHILE
    
    offset ← -1
    
    WHILE fibM > 1 DO
        i ← min(offset + fibM2, n-1)
        
        IF A[i] < target THEN
            fibM ← fibM1
            fibM1 ← fibM2
            fibM2 ← fibM - fibM1
            offset ← i
        ELSE IF A[i] > target THEN
            fibM ← fibM2
            fibM1 ← fibM1 - fibM2
            fibM2 ← fibM - fibM1
        ELSE
            RETURN i
        END IF
    END WHILE
    
    // Check last element
    IF fibM1 AND offset + 1 < n AND A[offset + 1] = target THEN
        RETURN offset + 1
    END IF
    
    RETURN -1  // Not found
END
```

## Searching in Data Structures

### Linked List Search
```text
Linear Search in Linked List:
- Can only use linear search
- Time complexity: O(n)
- Space complexity: O(1)

Pseudocode:
ALGORITHM LinkedListSearch(head, target)
BEGIN
    current ← head
    position ← 0
    
    WHILE current ≠ null DO
        IF current.data = target THEN
            RETURN position
        END IF
        current ← current.next
        position ← position + 1
    END WHILE
    
    RETURN -1  // Not found
END
```

### Binary Search Tree Search
```text
BST Search:
- Average case: O(log n)
- Worst case (skewed tree): O(n)
- Space complexity: O(1) iterative, O(h) recursive

Pseudocode:
ALGORITHM BSTSearch(root, target)
BEGIN
    current ← root
    
    WHILE current ≠ null DO
        IF current.value = target THEN
            RETURN current
        ELSE IF target < current.value THEN
            current ← current.left
        ELSE
            current ← current.right
        END IF
    END WHILE
    
    RETURN null  // Not found
END
```

### Hash Table Search
```text
Hash Table Search:
- Average case: O(1)
- Worst case (all collisions): O(n)
- Space complexity: O(n)

Pseudocode:
ALGORITHM HashSearch(table, target, size)
BEGIN
    index ← hash(target) % size
    
    // Handle collisions with chaining
    current ← table[index]
    
    WHILE current ≠ null DO
        IF current.key = target THEN
            RETURN current.value
        END IF
        current ← current.next
    END WHILE
    
    RETURN null  // Not found
END
```

## Multi-dimensional Search

### 2D Array Search
```text
Search in 2D Matrix (row-wise and column-wise sorted):

Pseudocode:
ALGORITHM Search2DMatrix(matrix[0..m-1][0..n-1], target)
BEGIN
    row ← 0
    col ← n-1
    
    WHILE row < m AND col ≥ 0 DO
        IF matrix[row][col] = target THEN
            RETURN (row, col)
        ELSE IF matrix[row][col] > target THEN
            col ← col - 1
        ELSE
            row ← row + 1
        END IF
    END WHILE
    
    RETURN null  // Not found
END

Time Complexity: O(m + n)
Space Complexity: O(1)
```

### Range Queries
```text
Range Search in BST:
- Find all elements in range [low, high]
- Time complexity: O(k + h) where k is result size, h is height

Pseudocode:
ALGORITHM RangeSearch(root, low, high, result)
BEGIN
    IF root = null THEN
        RETURN
    END IF
    
    // If current node is in range, add to result
    IF root.value ≥ low AND root.value ≤ high THEN
        ADD root.value TO result
    END IF
    
    // Search left subtree if current value > low
    IF root.value > low THEN
        RangeSearch(root.left, low, high, result)
    END IF
    
    // Search right subtree if current value < high
    IF root.value < high THEN
        RangeSearch(root.right, low, high, result)
    END IF
END
```

## Search Algorithm Comparison

### Performance Comparison Table
```text
| Algorithm | Time Complexity | Space | Sorted Required | Best For |
|-----------|-----------------|-------|----------------|----------|
| Linear | O(n) | O(1) | No | Small/unsorted data |
| Binary | O(log n) | O(1) | Yes | Large sorted arrays |
| Jump | O(√n) | O(1) | Yes | Expensive jumping |
| Interpolation | O(log log n) | O(1) | Yes | Uniform distribution |
| Exponential | O(log n) | O(1) | Yes | Unbounded arrays |
| Fibonacci | O(log n) | O(1) | Yes | No division operation |
| Hash Table | O(1) avg | O(n) | No | Fast lookups |
| BST | O(log n) avg | O(1) | No | Dynamic data |
```

### Choosing the Right Algorithm
```text
Decision Factors:
1. Data Size:
   - Small (< 100): Linear search is fine
   - Medium (100-1000): Binary search if sorted
   - Large (> 1000): Binary search or hash table

2. Data Characteristics:
   - Unsorted: Linear search or sort first
   - Sorted: Binary search, jump search
   - Uniform distribution: Interpolation search
   - Dynamic: BST or hash table

3. Access Patterns:
   - Single search: Linear search might be sufficient
   - Multiple searches: Sort once, use binary search
   - Frequent insertions/deletions: BST or hash table

4. Memory Constraints:
   - Limited memory: In-place algorithms
   - Abundant memory: Hash table for O(1) lookups
```

## Search Algorithm Optimizations

### 1. Early Termination
```text
Optimization: Stop search as soon as target is found
Benefit: Reduces average case time
Implementation: Return immediately when found
```

### 2. Adaptive Search
```text
Optimization: Adapt search strategy based on data distribution
Benefit: Better performance on non-uniform data
Example: Interpolation search for clustered data
```

### 3. Parallel Search
```text
Optimization: Divide search space among multiple processors
Benefit: Faster execution on multi-core systems
Implementation: Divide array into chunks, search in parallel
```

### 4. Cache-Friendly Search
```text
Optimization: Organize data to improve cache utilization
Benefit: Better performance due to fewer cache misses
Example: Search in row-major order for 2D arrays
```

## Common Search Problems and Solutions

### 1. Find First Occurrence
```text
Problem: Find first occurrence of target in sorted array with duplicates
Solution: Modified binary search (lower bound)
Time: O(log n)
```

### 2. Find Kth Smallest Element
```text
Problem: Find kth smallest element in unsorted array
Solution: Quickselect algorithm
Time: O(n) average, O(n²) worst
```

### 3. Search in Rotated Sorted Array
```text
Problem: Search in array sorted then rotated
Solution: Modified binary search
Time: O(log n)
```

### 4. Search in Matrix
```text
Problem: Search target in 2D matrix with sorted rows and columns
Solution: Start from top-right or bottom-left corner
Time: O(m + n)
```

## Best Practices

### Algorithm Selection
1. **Analyze Data**: Understand size, distribution, and organization
2. **Consider Constraints**: Time, space, and access pattern requirements
3. **Test Performance**: Benchmark with realistic data
4. **Handle Edge Cases**: Empty data, single element, duplicates

### Implementation Tips
1. **Use Built-in Functions**: When available and appropriate
2. **Validate Inputs**: Check for null/empty inputs
3. **Return Meaningful Results**: Index, boolean, or actual data
4. **Document Assumptions**: Sorted order, data types, constraints

### Optimization Guidelines
1. **Profile First**: Identify actual bottlenecks
2. **Consider Trade-offs**: Time vs space vs complexity
3. **Test Edge Cases**: Boundary conditions and error cases
4. **Maintain Readability**: Don't over-optimize prematurely

## Conclusion

Searching algorithms are fundamental to computer science and programming. Understanding different search techniques, their characteristics, and when to use each one is crucial for efficient data retrieval. From simple linear search to sophisticated binary search variants and specialized algorithms for specific data structures, each has its place in the programmer's toolkit. The choice of search algorithm depends on data characteristics, size, organization, and specific requirements of the application. Mastering these algorithms enables developers to write efficient, optimized code for data retrieval tasks across various domains and problem types.
