# Sorting Algorithms

## Overview

Sorting algorithms arrange elements in a specific order (ascending or descending). They are fundamental to computer science and are used extensively in various applications, from database systems to user interfaces.

## Sorting Algorithm Classification

### By Complexity
```text
O(n²) Algorithms (Simple):
- Bubble Sort
- Selection Sort
- Insertion Sort

O(n log n) Algorithms (Efficient):
- Merge Sort
- Quick Sort
- Heap Sort

Special Cases:
- Counting Sort: O(n + k) where k is range
- Radix Sort: O(d × (n + k)) where d is digits
- Bucket Sort: O(n + k) average case
```

### By Stability
```text
Stable Sorting (maintains relative order of equal elements):
- Bubble Sort
- Insertion Sort
- Merge Sort
- Counting Sort
- Radix Sort

Unstable Sorting (may change relative order):
- Selection Sort
- Quick Sort
- Heap Sort
```

### By Memory Usage
```text
In-place Sorting (O(1) extra space):
- Bubble Sort
- Selection Sort
- Insertion Sort
- Quick Sort
- Heap Sort

Not In-place (O(n) or more extra space):
- Merge Sort
- Counting Sort
- Radix Sort
- Bucket Sort
```

## Bubble Sort

### Algorithm Description
```text
Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps
them if they're in the wrong order. The pass through the list is repeated until the list
is sorted.

Characteristics:
- Time Complexity: O(n²)
- Space Complexity: O(1)
- Stable: Yes
- In-place: Yes
```

### Pseudocode
```text
ALGORITHM BubbleSort(A[0..n-1])
BEGIN
    FOR i ← 0 TO n-2 DO
        // Flag to detect if any swap occurred
        swapped ← false
        
        // Last i elements are already in place
        FOR j ← 0 TO n-i-2 DO
            IF A[j] > A[j+1] THEN
                SWAP A[j] and A[j+1]
                swapped ← true
            END IF
        END FOR
        
        // If no swaps occurred, array is sorted
        IF NOT swapped THEN
            BREAK
        END IF
    END FOR
END
```

### Implementation Examples
```python
# Python Implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Optimized version with early termination
def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
```

## Selection Sort

### Algorithm Description
```text
Selection Sort divides the input into sorted and unsorted regions. It repeatedly finds the
minimum element from the unsorted region and moves it to the end of the sorted region.

Characteristics:
- Time Complexity: O(n²)
- Space Complexity: O(1)
- Stable: No (can be made stable with modifications)
- In-place: Yes
```

### Pseudocode
```text
ALGORITHM SelectionSort(A[0..n-1])
BEGIN
    FOR i ← 0 TO n-2 DO
        // Find minimum element in unsorted portion
        min_index ← i
        FOR j ← i+1 TO n-1 DO
            IF A[j] < A[min_index] THEN
                min_index ← j
            END IF
        END FOR
        
        // Swap minimum element with element at position i
        IF min_index ≠ i THEN
            SWAP A[i] and A[min_index]
        END IF
    END FOR
END
```

### Implementation Examples
```python
# Python Implementation
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Stable version (using additional space)
def stable_selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Insert minimum element at correct position
        min_value = arr[min_index]
        while min_index > i:
            arr[min_index] = arr[min_index - 1]
            min_index -= 1
        arr[i] = min_value
    return arr
```

## Insertion Sort

### Algorithm Description
```text
Insertion Sort builds the final sorted array one item at a time. It iterates through the
input elements and inserts each element into its correct position in the sorted portion.

Characteristics:
- Time Complexity: O(n²) worst/average, O(n) best
- Space Complexity: O(1)
- Stable: Yes
- In-place: Yes
```

### Pseudocode
```text
ALGORITHM InsertionSort(A[0..n-1])
BEGIN
    FOR i ← 1 TO n-1 DO
        key ← A[i]
        j ← i - 1
        
        // Move elements greater than key one position ahead
        WHILE j ≥ 0 AND A[j] > key DO
            A[j+1] ← A[j]
            j ← j - 1
        END WHILE
        
        A[j+1] ← key
    END FOR
END
```

### Implementation Examples
```python
# Python Implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    return arr

# Binary Insertion Sort (uses binary search for insertion position)
def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        
        # Find insertion position using binary search
        left, right = 0, i - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > key:
                right = mid - 1
            else:
                left = mid + 1
        
        # Shift elements to make room for key
        for j in range(i, left, -1):
            arr[j] = arr[j - 1]
        
        arr[left] = key
    return arr
```

## Merge Sort

### Algorithm Description
```text
Merge Sort is a divide-and-conquer algorithm that divides the array into two halves,
recursively sorts them, and then merges the sorted halves.

Characteristics:
- Time Complexity: O(n log n)
- Space Complexity: O(n)
- Stable: Yes
- In-place: No (requires additional space)
```

### Pseudocode
```text
ALGORITHM MergeSort(A[0..n-1])
BEGIN
    IF n ≤ 1 THEN
        RETURN A  // Already sorted
    END IF
    
    // Divide array into two halves
    mid ← n / 2
    left ← MergeSort(A[0..mid-1])
    right ← MergeSort(A[mid..n-1])
    
    // Merge sorted halves
    RETURN Merge(left, right)
END

ALGORITHM Merge(left[0..m-1], right[0..n-1])
BEGIN
    result ← new array of size m + n
    i ← 0  // Index for left array
    j ← 0  // Index for right array
    k ← 0  // Index for result array
    
    // Merge elements from left and right arrays
    WHILE i < m AND j < n DO
        IF left[i] ≤ right[j] THEN
            result[k] ← left[i]
            i ← i + 1
        ELSE
            result[k] ← right[j]
            j ← j + 1
        END IF
        k ← k + 1
    END WHILE
    
    // Copy remaining elements from left array
    WHILE i < m DO
        result[k] ← left[i]
        i ← i + 1
        k ← k + 1
    END WHILE
    
    // Copy remaining elements from right array
    WHILE j < n DO
        result[k] ← right[j]
        j ← j + 1
        k ← k + 1
    END WHILE
    
    RETURN result
END
```

### Implementation Examples
```python
# Python Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# In-place merge sort (more complex)
def merge_sort_inplace(arr):
    if len(arr) <= 1:
        return arr
    
    temp = [0] * len(arr)
    merge_sort_helper(arr, temp, 0, len(arr) - 1)
    return arr

def merge_sort_helper(arr, temp, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort_helper(arr, temp, left, mid)
        merge_sort_helper(arr, temp, mid + 1, right)
        merge_inplace(arr, temp, left, mid, right)

def merge_inplace(arr, temp, left, mid, right):
    i, j, k = left, mid + 1, left
    
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    
    for i in range(left, right + 1):
        arr[i] = temp[i]
```

## Quick Sort

### Algorithm Description
```text
Quick Sort is a divide-and-conquer algorithm that picks a pivot element and partitions
the array around the pivot, then recursively sorts the sub-arrays.

Characteristics:
- Time Complexity: O(n log n) average, O(n²) worst
- Space Complexity: O(log n) recursive stack
- Stable: No
- In-place: Yes
```

### Pseudocode
```text
ALGORITHM QuickSort(A[low..high])
BEGIN
    IF low < high THEN
        // Partition the array and get pivot index
        pivot_index ← Partition(A, low, high)
        
        // Recursively sort elements before and after pivot
        QuickSort(A, low, pivot_index - 1)
        QuickSort(A, pivot_index + 1, high)
    END IF
END

ALGORITHM Partition(A[low..high])
BEGIN
    pivot ← A[high]  // Choose last element as pivot
    i ← low - 1      // Index of smaller element
    
    FOR j ← low TO high-1 DO
        IF A[j] ≤ pivot THEN
            i ← i + 1
            SWAP A[i] and A[j]
        END IF
    END FOR
    
    SWAP A[i+1] and A[high]
    RETURN i + 1  // Pivot index
END
```

### Implementation Examples
```python
# Python Implementation
def quick_sort(arr):
    def quick_sort_helper(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            quick_sort_helper(arr, low, pivot_index - 1)
            quick_sort_helper(arr, pivot_index + 1, high)
    
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr

# Randomized Quick Sort (better average case)
def randomized_quick_sort(arr):
    import random
    
    def quick_sort_helper(arr, low, high):
        if low < high:
            pivot_index = randomized_partition(arr, low, high)
            quick_sort_helper(arr, low, pivot_index - 1)
            quick_sort_helper(arr, pivot_index + 1, high)
    
    def randomized_partition(arr, low, high):
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        return partition(arr, low, high)
    
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr

# Three-way Quick Sort (better for duplicates)
def three_way_quick_sort(arr):
    def quick_sort_helper(arr, low, high):
        if low < high:
            lt, gt = three_way_partition(arr, low, high)
            quick_sort_helper(arr, low, lt - 1)
            quick_sort_helper(arr, gt + 1, high)
    
    def three_way_partition(arr, low, high):
        pivot = arr[low]
        lt = low      # Elements < pivot
        i = low + 1   # Elements = pivot
        gt = high     # Elements > pivot
        
        while i <= gt:
            if arr[i] < pivot:
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
            else:
                i += 1
        
        return lt, gt
    
    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr
```

## Heap Sort

### Algorithm Description
```text
Heap Sort uses a binary heap data structure to sort elements. It first builds a max-heap
from the input data, then repeatedly extracts the maximum element and rebuilds the heap.

Characteristics:
- Time Complexity: O(n log n)
- Space Complexity: O(1)
- Stable: No
- In-place: Yes
```

### Pseudocode
```text
ALGORITHM HeapSort(A[0..n-1])
BEGIN
    // Build max heap
    FOR i ← n/2 - 1 DOWNTO 0 DO
        Heapify(A, n, i)
    END FOR
    
    // Extract elements one by one
    FOR i ← n-1 DOWNTO 1 DO
        // Move current root to end
        SWAP A[0] and A[i]
        
        // Call heapify on reduced heap
        Heapify(A, i, 0)
    END FOR
END

ALGORITHM Heapify(A[0..n-1], heap_size, root)
BEGIN
    largest ← root
    left ← 2 * root + 1
    right ← 2 * root + 2
    
    // If left child is larger than root
    IF left < heap_size AND A[left] > A[largest] THEN
        largest ← left
    END IF
    
    // If right child is larger than largest so far
    IF right < heap_size AND A[right] > A[largest] THEN
        largest ← right
    END IF
    
    // If largest is not root
    IF largest ≠ root THEN
        SWAP A[root] and A[largest]
        Heapify(A, heap_size, largest)
    END IF
END
```

### Implementation Examples
```python
# Python Implementation
def heap_sort(arr):
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, heap_size, root):
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2
    
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, heap_size, largest)

# Using Python's heapq module (min-heap)
def heap_sort_using_heapq(arr):
    import heapq
    
    # Create a max-heap by inverting values
    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)
    
    sorted_arr = []
    while max_heap:
        sorted_arr.append(-heapq.heappop(max_heap))
    
    return sorted_arr
```

## Counting Sort

### Algorithm Description
```text
Counting Sort is a non-comparison-based sorting algorithm that works by counting the
number of occurrences of each distinct element in the input array.

Characteristics:
- Time Complexity: O(n + k) where k is range of elements
- Space Complexity: O(k)
- Stable: Yes
- In-place: No
```

### Pseudocode
```text
ALGORITHM CountingSort(A[0..n-1], k)
BEGIN
    // Create count array to store count of each element
    count ← new array of size k+1 initialized to 0
    
    // Store count of each element
    FOR i ← 0 TO n-1 DO
        count[A[i]] ← count[A[i]] + 1
    END FOR
    
    // Modify count array to contain positions
    FOR i ← 1 TO k DO
        count[i] ← count[i] + count[i-1]
    END FOR
    
    // Build output array
    output ← new array of size n
    FOR i ← n-1 DOWNTO 0 DO
        output[count[A[i]] - 1] ← A[i]
        count[A[i]] ← count[A[i]] - 1
    END FOR
    
    RETURN output
END
```

### Implementation Examples
```python
# Python Implementation
def counting_sort(arr):
    if not arr:
        return arr
    
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1
    
    # Create count array
    count = [0] * range_val
    
    # Store count of each element
    for num in arr:
        count[num - min_val] += 1
    
    # Modify count array to contain positions
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Build output array
    output = [0] * len(arr)
    for num in reversed(arr):
        count[num - min_val] -= 1
        output[count[num - min_val]] = num
    
    return output

# Counting sort for characters
def counting_sort_chars(arr):
    if not arr:
        return arr
    
    # For ASCII characters
    range_val = 256
    count = [0] * range_val
    
    # Store count of each character
    for char in arr:
        count[ord(char)] += 1
    
    # Modify count array to contain positions
    for i in range(1, range_val):
        count[i] += count[i - 1]
    
    # Build output array
    output = [''] * len(arr)
    for char in reversed(arr):
        count[ord(char)] -= 1
        output[count[ord(char)]] = char
    
    return output
```

## Radix Sort

### Algorithm Description
```text
Radix Sort sorts numbers by processing individual digits. It sorts the numbers digit by
digit, starting from the least significant digit to the most significant digit.

Characteristics:
- Time Complexity: O(d × (n + k)) where d is digits, k is range
- Space Complexity: O(n + k)
- Stable: Yes
- In-place: No
```

### Pseudocode
```text
ALGORITHM RadixSort(A[0..n-1], d)
BEGIN
    FOR i ← 1 TO d DO  // For each digit position
        // Use counting sort as stable sort on digit i
        A ← CountingSortByDigit(A, i)
    END FOR
    
    RETURN A
END

ALGORITHM CountingSortByDigit(A[0..n-1], digit_position)
BEGIN
    count ← new array of size 10 initialized to 0  // Digits 0-9
    
    // Store count of each digit
    FOR i ← 0 TO n-1 DO
        digit ← GetDigit(A[i], digit_position)
        count[digit] ← count[digit] + 1
    END FOR
    
    // Modify count array to contain positions
    FOR i ← 1 TO 9 DO
        count[i] ← count[i] + count[i-1]
    END FOR
    
    // Build output array
    output ← new array of size n
    FOR i ← n-1 DOWNTO 0 DO
        digit ← GetDigit(A[i], digit_position)
        output[count[digit] - 1] ← A[i]
        count[digit] ← count[digit] - 1
    END FOR
    
    RETURN output
END
```

### Implementation Examples
```python
# Python Implementation
def radix_sort(arr):
    if not arr:
        return arr
    
    # Find maximum number to know number of digits
    max_val = max(arr)
    
    # Do counting sort for every digit
    exp = 1
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
    
    return arr

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Digits 0-9
    
    # Store count of occurrences
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    # Change count[i] to contain actual position
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    # Copy output array to arr
    for i in range(n):
        arr[i] = output[i]

# Radix sort for strings
def radix_sort_strings(arr):
    if not arr:
        return arr
    
    # Find maximum string length
    max_len = max(len(s) for s in arr)
    
    # Do counting sort for each character position
    for pos in range(max_len - 1, -1, -1):
        counting_sort_by_char(arr, pos)
    
    return arr

def counting_sort_by_char(arr, pos):
    n = len(arr)
    output = [0] * n
    count = [0] * 256  # ASCII characters
    
    # Store count of occurrences
    for i in range(n):
        if pos < len(arr[i]):
            index = ord(arr[i][pos])
        else:
            index = 0  # Treat empty position as character 0
        count[index] += 1
    
    # Change count[i] to contain actual position
    for i in range(1, 256):
        count[i] += count[i - 1]
    
    # Build output array
    for i in range(n - 1, -1, -1):
        if pos < len(arr[i]):
            index = ord(arr[i][pos])
        else:
            index = 0
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    # Copy output array to arr
    for i in range(n):
        arr[i] = output[i]
```

## Bucket Sort

### Algorithm Description
```text
Bucket Sort distributes elements into several buckets, sorts each bucket individually,
and then concatenates the buckets.

Characteristics:
- Time Complexity: O(n + k) average, O(n²) worst
- Space Complexity: O(n + k)
- Stable: Yes
- In-place: No
```

### Pseudocode
```text
ALGORITHM BucketSort(A[0..n-1], k)
BEGIN
    // Create k empty buckets
    buckets ← new array of k empty lists
    
    // Put array elements in different buckets
    FOR i ← 0 TO n-1 DO
        bucket_index ← floor(k * A[i])
        APPEND A[i] TO buckets[bucket_index]
    END FOR
    
    // Sort individual buckets
    FOR i ← 0 TO k-1 DO
        Sort(buckets[i])  // Usually using insertion sort
    END FOR
    
    // Concatenate all buckets
    result ← empty list
    FOR i ← 0 TO k-1 DO
        result ← result + buckets[i]
    END FOR
    
    RETURN result
END
```

### Implementation Examples
```python
# Python Implementation
def bucket_sort(arr, num_buckets=10):
    if not arr:
        return arr
    
    # Find minimum and maximum values
    min_val = min(arr)
    max_val = max(arr)
    
    # Create buckets
    buckets = [[] for _ in range(num_buckets)]
    
    # Distribute input array values into buckets
    for num in arr:
        if max_val == min_val:
            bucket_index = 0
        else:
            bucket_index = int((num - min_val) / (max_val - min_val) * (num_buckets - 1))
        buckets[bucket_index].append(num)
    
    # Sort individual buckets and concatenate
    result = []
    for bucket in buckets:
        if bucket:
            # Use insertion sort for small buckets
            insertion_sort(bucket)
            result.extend(bucket)
    
    return result

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Bucket sort for floating-point numbers in [0, 1)
def bucket_sort_floats(arr):
    if not arr:
        return arr
    
    # Create n buckets
    n = len(arr)
    buckets = [[] for _ in range(n)]
    
    # Distribute elements into buckets
    for num in arr:
        bucket_index = int(num * n)  # 0 <= num < 1
        if bucket_index == n:
            bucket_index = n - 1
        buckets[bucket_index].append(num)
    
    # Sort individual buckets and concatenate
    result = []
    for bucket in buckets:
        bucket.sort()  # Use built-in sort for simplicity
        result.extend(bucket)
    
    return result
```

## Special Sorting Algorithms

### Shell Sort
```text
Shell Sort is an optimization of insertion sort that allows the exchange of items
far apart. It works by sorting elements far apart from each other and progressively
reducing the gap between elements.

Characteristics:
- Time Complexity: O(n^1.5) average, O(n²) worst
- Space Complexity: O(1)
- Stable: No
- In-place: Yes
```

```python
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            arr[j] = temp
        
        gap //= 2
    
    return arr
```

### Tim Sort
```text
Tim Sort is a hybrid sorting algorithm derived from merge sort and insertion sort.
It's designed to perform well on many kinds of real-world data.

Characteristics:
- Time Complexity: O(n log n) worst, O(n) best
- Space Complexity: O(n)
- Stable: Yes
- In-place: No
```

```python
# Simplified Tim Sort (Python's built-in sort uses Tim Sort)
def tim_sort(arr):
    # This is a simplified version
    # Real Tim Sort is much more complex
    MIN_MERGE = 32
    
    def insertion_sort(arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            
            arr[j + 1] = key
    
    def merge(arr, l, m, r):
        left = arr[l:m + 1]
        right = arr[m + 1:r + 1]
        
        i = j = 0
        k = l
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    
    n = len(arr)
    
    # Sort individual subarrays of size MIN_MERGE
    for start in range(0, n, MIN_MERGE):
        end = min(start + MIN_MERGE - 1, n - 1)
        insertion_sort(arr, start, end)
    
    # Merge subarrays
    size = MIN_MERGE
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size - 1
            right = min((left + 2 * size - 1), n - 1)
            
            if mid < right:
                merge(arr, left, mid, right)
        
        size *= 2
    
    return arr
```

## Sorting Algorithm Comparison

### Performance Comparison
```text
| Algorithm | Best | Average | Worst | Space | Stable | In-place |
|-----------|------|---------|--------|-------|--------|----------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | No | Yes |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Yes |
| Heap | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Yes |
| Counting | O(n + k) | O(n + k) | O(n + k) | O(k) | Yes | No |
| Radix | O(d(n + k)) | O(d(n + k)) | O(d(n + k)) | O(n + k) | Yes | No |
| Bucket | O(n + k) | O(n + k) | O(n²) | O(n + k) | Yes | No |
| Shell | O(n log n) | O(n^1.5) | O(n²) | O(1) | No | Yes |
| Tim | O(n) | O(n log n) | O(n log n) | O(n) | Yes | No |
```

### When to Use Each Algorithm

```text
Bubble Sort:
- Educational purposes
- Small datasets (n < 100)
- Nearly sorted data

Selection Sort:
- Memory writes are expensive
- Small datasets
- When minimizing swaps is important

Insertion Sort:
- Small datasets (n < 1000)
- Nearly sorted data
- Online sorting (data arrives incrementally)

Merge Sort:
- Large datasets
- External sorting (data doesn't fit in memory)
- When stability is required

Quick Sort:
- Large datasets
- Average case performance is important
- In-place sorting is required

Heap Sort:
- When worst-case performance must be guaranteed
- In-place sorting with O(1) space
- Priority queue applications

Counting Sort:
- Integers in a small range
- When O(n) time is required
- Stability is important

Radix Sort:
- Large datasets of integers or strings
- When comparison-based sorting is too slow
- Fixed-length keys

Bucket Sort:
- Uniformly distributed data
- Floating-point numbers in [0, 1)
- When data can be evenly distributed

Shell Sort:
- Medium datasets
- When insertion sort is too slow but quick sort is overkill
- Memory-constrained environments

Tim Sort:
- Real-world data with existing order
- When adaptive performance is beneficial
- Python's default sorting algorithm
```

## Sorting Algorithm Applications

### 1. Database Systems
```text
- Merge Sort: External sorting for large datasets
- Quick Sort: In-memory sorting for query results
- Heap Sort: Priority queue operations
```

### 2. Graphics and Multimedia
```text
- Radix Sort: Sorting pixels by color values
- Counting Sort: Histogram operations
- Bucket Sort: Z-buffer sorting
```

### 3. Operating Systems
```text
- Quick Sort: Process scheduling
- Heap Sort: Memory management
- Insertion Sort: Small system tables
```

### 4. Web Applications
```text
- Tim Sort: JavaScript array sorting
- Merge Sort: Sorting large datasets
- Quick Sort: Real-time data processing
```

## Best Practices

### Algorithm Selection
1. **Consider Data Size**: Choose based on input size
2. **Analyze Data Characteristics**: Distribution, order, range
3. **Evaluate Constraints**: Time, space, stability requirements
4. **Test with Real Data**: Benchmark with actual datasets

### Implementation Tips
1. **Use Built-in Functions**: When available and appropriate
2. **Handle Edge Cases**: Empty arrays, single elements, duplicates
3. **Optimize for Common Cases**: Most frequent input patterns
4. **Consider Memory Usage**: In-place vs extra space requirements

### Performance Optimization
1. **Profile First**: Identify actual bottlenecks
2. **Use Hybrid Approaches**: Combine algorithms for better performance
3. **Leverage Hardware**: Cache-friendly implementations
4. **Parallelize When Possible**: Multi-threaded sorting for large datasets

## Conclusion

Sorting algorithms are fundamental to computer science and programming. Understanding different sorting techniques, their characteristics, and when to use each one is crucial for efficient data organization. From simple O(n²) algorithms suitable for small datasets to sophisticated O(n log n) algorithms for large-scale applications, each has its place in the programmer's toolkit. The choice of sorting algorithm depends on data characteristics, size, memory constraints, and specific application requirements. Mastering these algorithms enables developers to write efficient, optimized code for data organization tasks across various domains and problem types.
