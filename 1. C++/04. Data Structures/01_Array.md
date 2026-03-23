# Arrays in C++

## Overview
Arrays are the most fundamental data structure in C++ that store elements of the same data type in contiguous memory locations. They provide O(1) access time to elements using index-based addressing. C++ offers three types of arrays: C-style arrays, `std::array` (fixed-size), and `std::vector` (dynamic-size). This comprehensive guide covers all operations, functions, and advanced techniques for working with arrays.

## Key Characteristics
- **Contiguous Memory**: All elements are stored in consecutive memory locations
- **Fixed/Static Size**: Traditional arrays have fixed size determined at compile time
- **Zero-based Indexing**: First element is at index 0
- **Random Access**: Any element can be accessed directly using its index in O(1) time
- **Cache Friendly**: Contiguous memory layout improves cache performance

---

## 1. C-Style Arrays (Traditional Arrays)

### Theory
C-style arrays are inherited from the C programming language. They provide direct memory access but lack safety features. The size must be known at compile time, and there's no built-in bounds checking.

**Use Cases:**
- When working with legacy C code
- For embedded systems with memory constraints
- When maximum performance with minimal overhead is required
- For fixed-size data that won't change

**Limitations:**
- No size information stored with the array
- No bounds checking (dangerous)
- Cannot be copied or assigned directly
- Size must be compile-time constant

### All Functions and Operations

```cpp
#include <iostream>
#include <cstring>      // For C-string functions
#include <algorithm>    // For std::sort, std::find, etc.
#include <iterator>     // For std::begin, std::end

void demonstrateCStyleArrays() {
    std::cout << "\n========== C-STYLE ARRAYS ==========\n";
    
    // ==================== DECLARATION & INITIALIZATION ====================
    std::cout << "\n--- Declaration & Initialization ---\n";
    
    // Single-dimensional arrays
    int arr1[5];                                    // Declaration only (uninitialized)
    int arr2[5] = {1, 2, 3, 4, 5};                 // Full initialization
    int arr3[] = {10, 20, 30, 40};                  // Size deduced (4 elements)
    int arr4[5] = {1, 2, 3};                        // Partial initialization (rest = 0)
    int arr5[5] = {0};                              // All elements initialized to 0
    
    // Multi-dimensional arrays
    int matrix1[3][3];                              // 3x3 uninitialized
    int matrix2[3][3] = {                           // Full initialization
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    int matrix3[][3] = {{1, 2}, {3, 4}, {5, 6}};   // Partial initialization (rest = 0)
    int matrix4[3][3] = {0};                        // All zeros
    
    // Character arrays (strings)
    char str1[] = "Hello";                          // Size 6 (includes null terminator)
    char str2[10] = "World";                       // Size 10, "World\0" followed by zeros
    char str3[5] = {'A', 'B', 'C', 'D', '\0'};     // Explicit null termination
    
    // ==================== ACCESSING ELEMENTS ====================
    std::cout << "\n--- Accessing Elements ---\n";
    
    std::cout << "arr2[2]: " << arr2[2] << "\n";
    std::cout << "matrix2[1][1]: " << matrix2[1][1] << "\n";
    std::cout << "str1[0]: " << str1[0] << "\n";
    std::cout << "str1 (as C-string): " << str1 << "\n";
    
    // Pointer arithmetic
    int* ptr = arr2;
    std::cout << "Pointer arithmetic: *(ptr + 2) = " << *(ptr + 2) << "\n";
    std::cout << "Pointer difference: " << (ptr + 4) - ptr << "\n";
    
    // ==================== SIZE INFORMATION ====================
    std::cout << "\n--- Size Information ---\n";
    
    size_t total_bytes = sizeof(arr2);
    size_t element_bytes = sizeof(arr2[0]);
    size_t length = sizeof(arr2) / sizeof(arr2[0]);
    
    std::cout << "Total bytes: " << total_bytes << "\n";
    std::cout << "Element bytes: " << element_bytes << "\n";
    std::cout << "Number of elements: " << length << "\n";
    
    // String length (excluding null terminator)
    std::cout << "String length: " << strlen(str1) << "\n";
    
    // ==================== MODIFYING ELEMENTS ====================
    std::cout << "\n--- Modifying Elements ---\n";
    
    arr2[2] = 100;
    std::cout << "After modification arr2[2] = " << arr2[2] << "\n";
    
    matrix2[1][1] = 99;
    std::cout << "After modification matrix2[1][1] = " << matrix2[1][1] << "\n";
    
    // ==================== COPYING ARRAYS ====================
    std::cout << "\n--- Copying Arrays ---\n";
    
    int source[] = {1, 2, 3, 4, 5};
    int dest[5];
    
    // Manual copy
    for (int i = 0; i < 5; i++) {
        dest[i] = source[i];
    }
    
    // Using memcpy
    int dest2[5];
    memcpy(dest2, source, sizeof(source));
    
    // Using std::copy (requires <algorithm>)
    int dest3[5];
    std::copy(std::begin(source), std::end(source), dest3);
    
    std::cout << "Copied array: ";
    for (int i = 0; i < 5; i++) {
        std::cout << dest3[i] << " ";
    }
    std::cout << "\n";
    
    // ==================== COMPARING ARRAYS ====================
    std::cout << "\n--- Comparing Arrays ---\n";
    
    int arrA[] = {1, 2, 3, 4, 5};
    int arrB[] = {1, 2, 3, 4, 5};
    
    // Manual comparison
    bool equal = true;
    for (int i = 0; i < 5; i++) {
        if (arrA[i] != arrB[i]) {
            equal = false;
            break;
        }
    }
    std::cout << "Arrays equal (manual): " << (equal ? "Yes" : "No") << "\n";
    
    // Using memcmp
    bool mem_equal = (memcmp(arrA, arrB, sizeof(arrA)) == 0);
    std::cout << "Arrays equal (memcmp): " << (mem_equal ? "Yes" : "No") << "\n";
    
    // ==================== SEARCHING ====================
    std::cout << "\n--- Searching ---\n";
    
    int search_arr[] = {10, 20, 30, 40, 50};
    int target = 30;
    
    // Linear search
    int found_index = -1;
    for (int i = 0; i < 5; i++) {
        if (search_arr[i] == target) {
            found_index = i;
            break;
        }
    }
    std::cout << "Element " << target << " found at index: " << found_index << "\n";
    
    // Using std::find
    auto it = std::find(std::begin(search_arr), std::end(search_arr), target);
    if (it != std::end(search_arr)) {
        std::cout << "Using std::find - found at index: " << (it - search_arr) << "\n";
    }
    
    // ==================== SORTING ====================
    std::cout << "\n--- Sorting ---\n";
    
    int sort_arr[] = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    int size = sizeof(sort_arr) / sizeof(sort_arr[0]);
    
    // Using std::sort
    std::sort(std::begin(sort_arr), std::end(sort_arr));
    std::cout << "Sorted ascending: ";
    for (int x : sort_arr) std::cout << x << " ";
    std::cout << "\n";
    
    // Sorting in descending order
    std::sort(std::begin(sort_arr), std::end(sort_arr), std::greater<int>());
    std::cout << "Sorted descending: ";
    for (int x : sort_arr) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== REVERSING ====================
    std::cout << "\n--- Reversing ---\n";
    
    int rev_arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int rev_size = sizeof(rev_arr) / sizeof(rev_arr[0]);
    
    // Manual reversal
    for (int i = 0; i < rev_size / 2; i++) {
        std::swap(rev_arr[i], rev_arr[rev_size - 1 - i]);
    }
    std::cout << "Manually reversed: ";
    for (int x : rev_arr) std::cout << x << " ";
    std::cout << "\n";
    
    // Using std::reverse
    int rev_arr2[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    std::reverse(std::begin(rev_arr2), std::end(rev_arr2));
    std::cout << "Using std::reverse: ";
    for (int x : rev_arr2) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== FILLING ====================
    std::cout << "\n--- Filling ---\n";
    
    int fill_arr[10];
    
    // Manual fill
    for (int i = 0; i < 10; i++) {
        fill_arr[i] = 42;
    }
    
    // Using memset (for byte-level filling)
    int fill_arr2[10];
    memset(fill_arr2, 0, sizeof(fill_arr2));     // Fill with 0
    
    // Using std::fill
    int fill_arr3[10];
    std::fill(std::begin(fill_arr3), std::end(fill_arr3), 99);
    std::cout << "std::fill result: ";
    for (int x : fill_arr3) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== ROTATION ====================
    std::cout << "\n--- Rotation ---\n";
    
    int rot_arr[] = {1, 2, 3, 4, 5, 6, 7, 8};
    int rot_size = sizeof(rot_arr) / sizeof(rot_arr[0]);
    
    // Using std::rotate
    std::rotate(std::begin(rot_arr), std::begin(rot_arr) + 2, std::end(rot_arr));
    std::cout << "After rotate left by 2: ";
    for (int x : rot_arr) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== PARTITIONING ====================
    std::cout << "\n--- Partitioning ---\n";
    
    int part_arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    // Partition: even numbers first, odd numbers second
    auto partition_point = std::partition(
        std::begin(part_arr), 
        std::end(part_arr), 
        [](int x) { return x % 2 == 0; }
    );
    
    std::cout << "Partitioned (evens first): ";
    for (int x : part_arr) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== UNIQUE ELEMENTS ====================
    std::cout << "\n--- Removing Duplicates ---\n";
    
    int dup_arr[] = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5};
    int dup_size = sizeof(dup_arr) / sizeof(dup_arr[0]);
    
    // Sort first
    std::sort(std::begin(dup_arr), std::end(dup_arr));
    
    // Get unique elements
    auto last = std::unique(std::begin(dup_arr), std::end(dup_arr));
    
    std::cout << "After unique (first " << (last - dup_arr) << " elements): ";
    for (int* p = dup_arr; p != last; ++p) {
        std::cout << *p << " ";
    }
    std::cout << "\n";
    
    // ==================== SET OPERATIONS ====================
    std::cout << "\n--- Set Operations (on sorted arrays) ---\n";
    
    int set1[] = {1, 2, 3, 4, 5};
    int set2[] = {4, 5, 6, 7, 8};
    int result[10];
    
    // Union
    auto union_end = std::set_union(
        std::begin(set1), std::end(set1),
        std::begin(set2), std::end(set2),
        result
    );
    std::cout << "Union: ";
    for (int* p = result; p != union_end; ++p) std::cout << *p << " ";
    std::cout << "\n";
    
    // Intersection
    auto inter_end = std::set_intersection(
        std::begin(set1), std::end(set1),
        std::begin(set2), std::end(set2),
        result
    );
    std::cout << "Intersection: ";
    for (int* p = result; p != inter_end; ++p) std::cout << *p << " ";
    std::cout << "\n";
    
    // Difference (set1 - set2)
    auto diff_end = std::set_difference(
        std::begin(set1), std::end(set1),
        std::begin(set2), std::end(set2),
        result
    );
    std::cout << "Difference (set1 - set2): ";
    for (int* p = result; p != diff_end; ++p) std::cout << *p << " ";
    std::cout << "\n";
    
    // ==================== MIN/MAX ELEMENTS ====================
    std::cout << "\n--- Min/Max Elements ---\n";
    
    int minmax_arr[] = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    // Manual min/max
    int min_val = minmax_arr[0];
    int max_val = minmax_arr[0];
    for (int x : minmax_arr) {
        if (x < min_val) min_val = x;
        if (x > max_val) max_val = x;
    }
    std::cout << "Min (manual): " << min_val << ", Max (manual): " << max_val << "\n";
    
    // Using std::min_element and std::max_element
    auto min_it = std::min_element(std::begin(minmax_arr), std::end(minmax_arr));
    auto max_it = std::max_element(std::begin(minmax_arr), std::end(minmax_arr));
    std::cout << "Min (algorithm): " << *min_it << ", Max (algorithm): " << *max_it << "\n";
    
    // ==================== SUMMATION & ACCUMULATION ====================
    std::cout << "\n--- Summation & Accumulation ---\n";
    
    int sum_arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    // Manual sum
    int sum = 0;
    for (int x : sum_arr) sum += x;
    std::cout << "Sum (manual): " << sum << "\n";
    
    // Using std::accumulate (requires <numeric>)
    #include <numeric>
    int acc_sum = std::accumulate(std::begin(sum_arr), std::end(sum_arr), 0);
    std::cout << "Sum (accumulate): " << acc_sum << "\n";
    
    // ==================== ADJACENT DIFFERENCES ====================
    std::cout << "\n--- Adjacent Differences ---\n";
    
    int diff_arr[] = {1, 3, 6, 10, 15, 21, 28, 36, 45, 55};
    int adj_diff[9];
    
    std::adjacent_difference(
        std::begin(diff_arr), std::end(diff_arr),
        std::begin(adj_diff)
    );
    
    std::cout << "Original: ";
    for (int x : diff_arr) std::cout << x << " ";
    std::cout << "\nDifferences: ";
    for (int x : adj_diff) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== TRANSFORMATION ====================
    std::cout << "\n--- Transformation ---\n";
    
    int transform_arr[] = {1, 2, 3, 4, 5};
    int transformed[5];
    
    // Square each element
    std::transform(
        std::begin(transform_arr), std::end(transform_arr),
        std::begin(transformed),
        [](int x) { return x * x; }
    );
    
    std::cout << "Original: ";
    for (int x : transform_arr) std::cout << x << " ";
    std::cout << "\nSquared: ";
    for (int x : transformed) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== BINARY SEARCH (on sorted arrays) ====================
    std::cout << "\n--- Binary Search ---\n";
    
    int binary_arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    // Using std::binary_search
    bool found = std::binary_search(std::begin(binary_arr), std::end(binary_arr), 7);
    std::cout << "Element 7 found: " << (found ? "Yes" : "No") << "\n";
    
    // Using std::lower_bound (returns first position where element could be inserted)
    auto lb = std::lower_bound(std::begin(binary_arr), std::end(binary_arr), 7);
    if (lb != std::end(binary_arr) && *lb == 7) {
        std::cout << "Element 7 found at index: " << (lb - binary_arr) << "\n";
    }
    
    // ==================== COUNTING ELEMENTS ====================
    std::cout << "\n--- Counting Elements ---\n";
    
    int count_arr[] = {1, 2, 3, 2, 4, 2, 5, 2, 6, 2};
    
    // Manual count
    int manual_count = 0;
    for (int x : count_arr) {
        if (x == 2) manual_count++;
    }
    std::cout << "Manual count of 2: " << manual_count << "\n";
    
    // Using std::count
    int algo_count = std::count(std::begin(count_arr), std::end(count_arr), 2);
    std::cout << "std::count of 2: " << algo_count << "\n";
    
    // Count with condition
    int cond_count = std::count_if(
        std::begin(count_arr), std::end(count_arr),
        [](int x) { return x > 3; }
    );
    std::cout << "Count of elements > 3: " << cond_count << "\n";
    
    // ==================== REPLACING ELEMENTS ====================
    std::cout << "\n--- Replacing Elements ---\n";
    
    int replace_arr[] = {1, 2, 3, 2, 4, 2, 5, 2, 6};
    
    // Replace all 2 with 99
    std::replace(
        std::begin(replace_arr), std::end(replace_arr),
        2, 99
    );
    
    std::cout << "After replace (2 -> 99): ";
    for (int x : replace_arr) std::cout << x << " ";
    std::cout << "\n";
    
    // Replace based on condition
    int replace_if_arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    std::replace_if(
        std::begin(replace_if_arr), std::end(replace_if_arr),
        [](int x) { return x % 2 == 0; },
        0
    );
    
    std::cout << "After replace_if (even -> 0): ";
    for (int x : replace_if_arr) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== REMOVING ELEMENTS (LOGICAL) ====================
    std::cout << "\n--- Removing Elements (Logical) ---\n";
    
    int remove_arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int remove_size = sizeof(remove_arr) / sizeof(remove_arr[0]);
    
    // Remove all odd numbers (logical removal)
    auto new_end = std::remove_if(
        std::begin(remove_arr), std::end(remove_arr),
        [](int x) { return x % 2 != 0; }
    );
    
    std::cout << "After remove_if (odd numbers removed): ";
    for (int* p = remove_arr; p != new_end; ++p) {
        std::cout << *p << " ";
    }
    std::cout << "\n";
    std::cout << "Note: Array still has size " << remove_size << ", but logical size is " 
              << (new_end - remove_arr) << "\n";
}
```

---

## 2. std::array (Modern C++ Fixed-Size Array)

### Theory
`std::array` (introduced in C++11) is a modern wrapper around C-style arrays that provides STL container interface while maintaining the performance of fixed-size arrays. It knows its size, provides bounds checking with `.at()`, and works with STL algorithms.

**Advantages:**
- Knows its size (`.size()` method)
- Bounds checking with `.at()` (throws exception)
- Works with STL algorithms
- No memory overhead compared to C-style arrays
- Supports iterators and range-based for loops
- Copyable and assignable
- Provides tuple interface for structured bindings

**When to Use:**
- When you need a fixed-size array with STL interface
- When you want bounds checking in debug mode
- When you need to pass array size information
- When working with STL algorithms on fixed-size data

### All Functions and Operations

```cpp
#include <iostream>
#include <array>
#include <algorithm>
#include <numeric>
#include <tuple>

void demonstrateStdArray() {
    std::cout << "\n========== STD::ARRAY ==========\n";
    
    // ==================== DECLARATION & INITIALIZATION ====================
    std::cout << "\n--- Declaration & Initialization ---\n";
    
    // Various initialization methods
    std::array<int, 5> arr1;                           // Uninitialized
    std::array<int, 5> arr2 = {1, 2, 3, 4, 5};        // Initializer list
    std::array<int, 5> arr3 = {1, 2, 3};              // Partial initialization (rest = 0)
    std::array<int, 5> arr4{1, 2, 3, 4, 5};           // Uniform initialization
    std::array<int, 5> arr5 = arr2;                   // Copy construction
    
    // 2D std::array
    std::array<std::array<int, 3>, 3> matrix = {{
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    }};
    
    // ==================== ACCESSING ELEMENTS ====================
    std::cout << "\n--- Accessing Elements ---\n";
    
    // Using operator[]
    std::cout << "arr2[2]: " << arr2[2] << "\n";
    
    // Using .at() (with bounds checking)
    try {
        std::cout << "arr2.at(2): " << arr2.at(2) << "\n";
        // std::cout << arr2.at(10) << "\n";        // Throws std::out_of_range
    } catch (const std::out_of_range& e) {
        std::cout << "Out of range: " << e.what() << "\n";
    }
    
    // Using .front() and .back()
    std::cout << "Front: " << arr2.front() << "\n";
    std::cout << "Back: " << arr2.back() << "\n";
    
    // Using .data() (C-style pointer)
    int* data_ptr = arr2.data();
    std::cout << "Data pointer access: " << data_ptr[0] << "\n";
    
    // Structured binding (C++17)
    auto [a, b, c, d, e] = arr2;
    std::cout << "Structured binding: " << a << ", " << b << ", " << c << ", " << d << ", " << e << "\n";
    
    // ==================== SIZE INFORMATION ====================
    std::cout << "\n--- Size Information ---\n";
    
    std::cout << "Size: " << arr2.size() << "\n";
    std::cout << "Max size: " << arr2.max_size() << "\n";
    std::cout << "Empty? " << (arr2.empty() ? "Yes" : "No") << "\n";
    std::cout << "Element size: " << sizeof(arr2[0]) << "\n";
    std::cout << "Total size: " << sizeof(arr2) << "\n";
    
    // ==================== MODIFYING ELEMENTS ====================
    std::cout << "\n--- Modifying Elements ---\n";
    
    arr2[2] = 100;
    std::cout << "After modification arr2[2] = " << arr2[2] << "\n";
    
    // Using .fill() - fill entire array with value
    arr2.fill(0);
    std::cout << "After fill with 0: ";
    for (int x : arr2) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== COPYING ====================
    std::cout << "\n--- Copying ---\n";
    
    std::array<int, 5> source = {1, 2, 3, 4, 5};
    std::array<int, 5> dest;
    
    // Copy assignment
    dest = source;
    std::cout << "After copy assignment: ";
    for (int x : dest) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== SWAPPING ====================
    std::cout << "\n--- Swapping ---\n";
    
    std::array<int, 5> arrA = {1, 2, 3, 4, 5};
    std::array<int, 5> arrB = {10, 20, 30, 40, 50};
    
    arrA.swap(arrB);
    std::cout << "After swap - arrA: ";
    for (int x : arrA) std::cout << x << " ";
    std::cout << "\nAfter swap - arrB: ";
    for (int x : arrB) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== COMPARISON ====================
    std::cout << "\n--- Comparison ---\n";
    
    std::array<int, 5> comp1 = {1, 2, 3, 4, 5};
    std::array<int, 5> comp2 = {1, 2, 3, 4, 5};
    std::array<int, 5> comp3 = {1, 2, 3, 4, 6};
    
    std::cout << "comp1 == comp2: " << (comp1 == comp2 ? "Yes" : "No") << "\n";
    std::cout << "comp1 == comp3: " << (comp1 == comp3 ? "Yes" : "No") << "\n";
    std::cout << "comp1 < comp3: " << (comp1 < comp3 ? "Yes" : "No") << "\n";
    
    // ==================== ITERATORS ====================
    std::cout << "\n--- Iterators ---\n";
    
    std::array<int, 5> iter_arr = {10, 20, 30, 40, 50};
    
    // Regular iterators
    std::cout << "Using iterators: ";
    for (auto it = iter_arr.begin(); it != iter_arr.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    // Const iterators
    std::cout << "Using const iterators: ";
    for (auto it = iter_arr.cbegin(); it != iter_arr.cend(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    // Reverse iterators
    std::cout << "Reverse order: ";
    for (auto it = iter_arr.rbegin(); it != iter_arr.rend(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    // Range-based for loop
    std::cout << "Range-based for: ";
    for (const auto& elem : iter_arr) {
        std::cout << elem << " ";
    }
    std::cout << "\n";
    
    // ==================== ALGORITHMS WITH STD::ARRAY ====================
    std::cout << "\n--- Algorithms ---\n";
    
    std::array<int, 10> algo_arr = {5, 2, 8, 1, 9, 3, 7, 4, 6, 10};
    
    // Sorting
    std::sort(algo_arr.begin(), algo_arr.end());
    std::cout << "Sorted: ";
    for (int x : algo_arr) std::cout << x << " ";
    std::cout << "\n";
    
    // Reverse
    std::reverse(algo_arr.begin(), algo_arr.end());
    std::cout << "Reversed: ";
    for (int x : algo_arr) std::cout << x << " ";
    std::cout << "\n";
    
    // Find
    auto found = std::find(algo_arr.begin(), algo_arr.end(), 5);
    if (found != algo_arr.end()) {
        std::cout << "Found 5 at position: " << (found - algo_arr.begin()) << "\n";
    }
    
    // Count
    int count = std::count(algo_arr.begin(), algo_arr.end(), 5);
    std::cout << "Count of 5: " << count << "\n";
    
    // Accumulate (sum)
    int sum = std::accumulate(algo_arr.begin(), algo_arr.end(), 0);
    std::cout << "Sum: " << sum << "\n";
    
    // Min and max
    auto min_it = std::min_element(algo_arr.begin(), algo_arr.end());
    auto max_it = std::max_element(algo_arr.begin(), algo_arr.end());
    std::cout << "Min: " << *min_it << ", Max: " << *max_it << "\n";
    
    // Transform
    std::array<int, 5> square_arr;
    std::array<int, 5> orig_arr = {1, 2, 3, 4, 5};
    std::transform(orig_arr.begin(), orig_arr.end(), square_arr.begin(),
                   [](int x) { return x * x; });
    std::cout << "Squares: ";
    for (int x : square_arr) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== TUPLE INTERFACE (C++11+) ====================
    std::cout << "\n--- Tuple Interface ---\n";
    
    std::array<std::string, 3> names = {"Alice", "Bob", "Charlie"};
    
    // Get by index (compile-time)
    std::cout << "First name: " << std::get<0>(names) << "\n";
    std::cout << "Second name: " << std::get<1>(names) << "\n";
    
    // Get tuple size
    std::cout << "Tuple size: " << std::tuple_size<decltype(names)>::value << "\n";
    
    // Get element type
    using ElementType = std::tuple_element<0, decltype(names)>::type;
    std::cout << "Element type: " << typeid(ElementType).name() << "\n";
    
    // ==================== STRUCTURED BINDINGS (C++17) ====================
    std::cout << "\n--- Structured Bindings ---\n";
    
    std::array<int, 4> nums = {100, 200, 300, 400};
    auto [w, x, y, z] = nums;
    std::cout << "Structured binding: " << w << ", " << x << ", " << y << ", " << z << "\n";
}
```

---

## 3. std::vector (Dynamic Array) - Complete Guide

### Theory
`std::vector` is a dynamic array that can grow and shrink automatically. It manages memory allocation internally and provides amortized O(1) insertion at the end. Elements are stored contiguously, making it cache-friendly and compatible with C-style APIs via `.data()`.

**Key Features:**
- Dynamic size that changes at runtime
- Automatic memory management (allocates and deallocates)
- Contiguous storage for cache efficiency
- Amortized O(1) push_back and pop_back
- O(1) random access
- Works with STL algorithms
- Provides capacity management

**Memory Management:**
- Capacity grows exponentially (typically doubles) when needed
- `.reserve()` pre-allocates memory to avoid reallocations
- `.shrink_to_fit()` reduces capacity to match size
- Reallocation invalidates iterators

**When to Use:**
- Default choice for most sequence container needs
- When you need dynamic sizing
- When random access is important
- When you need to pass data to C APIs
- When you frequently add/remove at the end

### All Functions and Operations

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <iterator>

void demonstrateVector() {
    std::cout << "\n========== STD::VECTOR ==========\n";
    
    // ==================== DECLARATION & INITIALIZATION ====================
    std::cout << "\n--- Declaration & Initialization ---\n";
    
    // Various initialization methods
    std::vector<int> vec1;                                      // Empty vector
    std::vector<int> vec2(10);                                  // 10 elements, value-initialized (0)
    std::vector<int> vec3(10, 42);                              // 10 elements, all 42
    std::vector<int> vec4 = {1, 2, 3, 4, 5};                   // Initializer list (C++11)
    std::vector<int> vec5(vec4);                                // Copy constructor
    std::vector<int> vec6(std::move(vec5));                     // Move constructor (C++11)
    std::vector<int> vec7(vec4.begin(), vec4.end());            // Iterator range constructor
    
    // Using assign()
    std::vector<int> assign_vec;
    assign_vec.assign(5, 100);                                  // 5 elements, all 100
    assign_vec.assign({1, 2, 3, 4, 5});                         // From initializer list
    assign_vec.assign(vec4.begin(), vec4.end());                // From iterator range
    
    // 2D vector
    std::vector<std::vector<int>> matrix1(3, std::vector<int>(4, 0));  // 3x4, all 0
    std::vector<std::vector<int>> matrix2 = {                     // Jagged array
        {1, 2, 3},
        {4, 5},
        {6, 7, 8, 9}
    };
    
    // ==================== ACCESSING ELEMENTS ====================
    std::cout << "\n--- Accessing Elements ---\n";
    
    std::vector<int> access_vec = {10, 20, 30, 40, 50};
    
    // Using operator[]
    std::cout << "access_vec[2]: " << access_vec[2] << "\n";
    
    // Using .at() (with bounds checking)
    try {
        std::cout << "access_vec.at(2): " << access_vec.at(2) << "\n";
        // std::cout << access_vec.at(10) << "\n";              // Throws std::out_of_range
    } catch (const std::out_of_range& e) {
        std::cout << "Out of range: " << e.what() << "\n";
    }
    
    // Using .front() and .back()
    std::cout << "Front: " << access_vec.front() << "\n";
    std::cout << "Back: " << access_vec.back() << "\n";
    
    // Using .data() (C-style pointer)
    int* data_ptr = access_vec.data();
    std::cout << "Data pointer access: " << data_ptr[0] << "\n";
    
    // ==================== SIZE & CAPACITY ====================
    std::cout << "\n--- Size & Capacity ---\n";
    
    std::vector<int> cap_vec;
    std::cout << "Initial - Size: " << cap_vec.size() << ", Capacity: " << cap_vec.capacity() << "\n";
    
    for (int i = 0; i < 20; i++) {
        cap_vec.push_back(i);
        std::cout << "After push " << i << " - Size: " << cap_vec.size() 
                  << ", Capacity: " << cap_vec.capacity() << "\n";
    }
    
    // Size and capacity functions
    std::cout << "Size: " << cap_vec.size() << "\n";
    std::cout << "Capacity: " << cap_vec.capacity() << "\n";
    std::cout << "Max size: " << cap_vec.max_size() << "\n";
    std::cout << "Empty? " << (cap_vec.empty() ? "Yes" : "No") << "\n";
    
    // Reserve capacity
    cap_vec.reserve(100);
    std::cout << "After reserve(100) - Capacity: " << cap_vec.capacity() << "\n";
    
    // Shrink to fit
    cap_vec.shrink_to_fit();
    std::cout << "After shrink_to_fit - Capacity: " << cap_vec.capacity() << "\n";
    
    // ==================== ADDING ELEMENTS ====================
    std::cout << "\n--- Adding Elements ---\n";
    
    std::vector<int> add_vec;
    
    // push_back - add to end
    add_vec.push_back(10);
    add_vec.push_back(20);
    add_vec.push_back(30);
    std::cout << "After push_back: ";
    for (int x : add_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // emplace_back (C++11) - constructs in place (more efficient)
    add_vec.emplace_back(40);
    std::cout << "After emplace_back: ";
    for (int x : add_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // insert at position
    auto it = add_vec.begin() + 2;
    add_vec.insert(it, 25);
    std::cout << "After insert at position 2: ";
    for (int x : add_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // insert multiple copies
    add_vec.insert(add_vec.begin(), 3, 5);                  // Insert 3 copies of 5 at beginning
    std::cout << "After insert 3 copies of 5: ";
    for (int x : add_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // insert from initializer list
    add_vec.insert(add_vec.end(), {100, 200, 300});
    std::cout << "After insert from initializer list: ";
    for (int x : add_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // insert from iterator range
    std::vector<int> source = {1000, 2000, 3000};
    add_vec.insert(add_vec.begin(), source.begin(), source.end());
    std::cout << "After insert from range: ";
    for (int x : add_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // emplace (C++11) - construct in place at position
    add_vec.emplace(add_vec.begin() + 2, 999);
    std::cout << "After emplace at position 2: ";
    for (int x : add_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== REMOVING ELEMENTS ====================
    std::cout << "\n--- Removing Elements ---\n";
    
    std::vector<int> remove_vec = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    // pop_back - remove last element
    remove_vec.pop_back();
    std::cout << "After pop_back: ";
    for (int x : remove_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // erase at position
    remove_vec.erase(remove_vec.begin() + 2);
    std::cout << "After erase at index 2: ";
    for (int x : remove_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // erase range
    remove_vec.erase(remove_vec.begin() + 1, remove_vec.begin() + 3);
    std::cout << "After erase range [1, 3): ";
    for (int x : remove_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // clear - remove all elements
    remove_vec.clear();
    std::cout << "After clear - Size: " << remove_vec.size() << "\n";
    
    // ==================== ALGORITHMS WITH VECTOR ====================
    std::cout << "\n--- Algorithms ---\n";
    
    std::vector<int> algo_vec = {5, 2, 8, 1, 9, 3, 7, 4, 6, 10};
    
    // Sorting
    std::sort(algo_vec.begin(), algo_vec.end());
    std::cout << "Sorted: ";
    for (int x : algo_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // Sorting descending
    std::sort(algo_vec.begin(), algo_vec.end(), std::greater<int>());
    std::cout << "Sorted descending: ";
    for (int x : algo_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // Reverse
    std::reverse(algo_vec.begin(), algo_vec.end());
    std::cout << "Reversed: ";
    for (int x : algo_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // Find
    auto found = std::find(algo_vec.begin(), algo_vec.end(), 5);
    if (found != algo_vec.end()) {
        std::cout << "Found 5 at index: " << (found - algo_vec.begin()) << "\n";
    }
    
    // Count
    int count = std::count(algo_vec.begin(), algo_vec.end(), 5);
    std::cout << "Count of 5: " << count << "\n";
    
    // Count with condition
    int odd_count = std::count_if(algo_vec.begin(), algo_vec.end(), 
                                   [](int x) { return x % 2 != 0; });
    std::cout << "Count of odd numbers: " << odd_count << "\n";
    
    // Accumulate (sum)
    int sum = std::accumulate(algo_vec.begin(), algo_vec.end(), 0);
    std::cout << "Sum: " << sum << "\n";
    
    // Min and max
    auto min_it = std::min_element(algo_vec.begin(), algo_vec.end());
    auto max_it = std::max_element(algo_vec.begin(), algo_vec.end());
    std::cout << "Min: " << *min_it << ", Max: " << *max_it << "\n";
    
    // Transform
    std::vector<int> squares(algo_vec.size());
    std::transform(algo_vec.begin(), algo_vec.end(), squares.begin(),
                   [](int x) { return x * x; });
    std::cout << "Squares: ";
    for (int x : squares) std::cout << x << " ";
    std::cout << "\n";
    
    // Remove elements (logical removal)
    std::vector<int> remove_odd = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    auto new_end = std::remove_if(remove_odd.begin(), remove_odd.end(),
                                   [](int x) { return x % 2 != 0; });
    remove_odd.erase(new_end, remove_odd.end());
    std::cout << "After removing odd numbers: ";
    for (int x : remove_odd) std::cout << x << " ";
    std::cout << "\n";
    
    // Unique (remove consecutive duplicates)
    std::vector<int> dup_vec = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5};
    auto last = std::unique(dup_vec.begin(), dup_vec.end());
    dup_vec.erase(last, dup_vec.end());
    std::cout << "After removing duplicates: ";
    for (int x : dup_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== ITERATORS ====================
    std::cout << "\n--- Iterators ---\n";
    
    std::vector<int> iter_vec = {10, 20, 30, 40, 50};
    
    // Regular iterators
    std::cout << "Using iterators: ";
    for (auto it = iter_vec.begin(); it != iter_vec.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    // Const iterators
    std::cout << "Using const iterators: ";
    for (auto it = iter_vec.cbegin(); it != iter_vec.cend(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    // Reverse iterators
    std::cout << "Reverse order: ";
    for (auto it = iter_vec.rbegin(); it != iter_vec.rend(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    // Range-based for loop
    std::cout << "Range-based for: ";
    for (const auto& elem : iter_vec) {
        std::cout << elem << " ";
    }
    std::cout << "\n";
    
    // ==================== MEMORY MANAGEMENT ====================
    std::cout << "\n--- Memory Management ---\n";
    
    std::vector<int> mem_vec;
    
    // Reserve space
    mem_vec.reserve(1000);
    std::cout << "After reserve(1000) - Capacity: " << mem_vec.capacity() << "\n";
    
    // Add many elements
    for (int i = 0; i < 500; i++) {
        mem_vec.push_back(i);
    }
    std::cout << "After 500 push_backs - Size: " << mem_vec.size() 
              << ", Capacity: " << mem_vec.capacity() << "\n";
    
    // Shrink to fit
    mem_vec.shrink_to_fit();
    std::cout << "After shrink_to_fit - Capacity: " << mem_vec.capacity() << "\n";
    
    // ==================== COMPARISON ====================
    std::cout << "\n--- Comparison ---\n";
    
    std::vector<int> comp1 = {1, 2, 3, 4, 5};
    std::vector<int> comp2 = {1, 2, 3, 4, 5};
    std::vector<int> comp3 = {1, 2, 3, 4, 6};
    
    std::cout << "comp1 == comp2: " << (comp1 == comp2 ? "Yes" : "No") << "\n";
    std::cout << "comp1 == comp3: " << (comp1 == comp3 ? "Yes" : "No") << "\n";
    std::cout << "comp1 < comp3: " << (comp1 < comp3 ? "Yes" : "No") << "\n";
    
    // ==================== SWAPPING ====================
    std::cout << "\n--- Swapping ---\n";
    
    std::vector<int> swap1 = {1, 2, 3};
    std::vector<int> swap2 = {10, 20, 30, 40, 50};
    
    swap1.swap(swap2);
    std::cout << "After swap - swap1: ";
    for (int x : swap1) std::cout << x << " ";
    std::cout << "\nAfter swap - swap2: ";
    for (int x : swap2) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== RESIZING ====================
    std::cout << "\n--- Resizing ---\n";
    
    std::vector<int> resize_vec = {1, 2, 3, 4, 5};
    
    resize_vec.resize(10);
    std::cout << "After resize(10): ";
    for (int x : resize_vec) std::cout << x << " ";
    std::cout << "\n";
    
    resize_vec.resize(3);
    std::cout << "After resize(3): ";
    for (int x : resize_vec) std::cout << x << " ";
    std::cout << "\n";
    
    resize_vec.resize(7, 99);
    std::cout << "After resize(7, 99): ";
    for (int x : resize_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== 2D VECTOR OPERATIONS ====================
    std::cout << "\n--- 2D Vector Operations ---\n";
    
    // Create 3x4 matrix
    std::vector<std::vector<int>> mat(3, std::vector<int>(4, 0));
    
    // Fill with values
    int val = 1;
    for (size_t i = 0; i < mat.size(); i++) {
        for (size_t j = 0; j < mat[i].size(); j++) {
            mat[i][j] = val++;
        }
    }
    
    std::cout << "2D Matrix:\n";
    for (const auto& row : mat) {
        for (int elem : row) {
            std::cout << elem << " ";
        }
        std::cout << "\n";
    }
    
    // ==================== EMPlACE VS PUSH (Performance) ====================
    std::cout << "\n--- Emplace vs Push (Performance) ---\n";
    
    struct Person {
        std::string name;
        int age;
        Person(std::string n, int a) : name(std::move(n)), age(a) {}
    };
    
    std::vector<Person> persons;
    
    // push_back - creates temporary then moves/copies
    persons.push_back(Person("Alice", 25));
    
    // emplace_back - constructs in place (more efficient)
    persons.emplace_back("Bob", 30);
    
    std::cout << "Persons: " << persons[0].name << ", " << persons[1].name << "\n";
}
```

---

## Performance Summary

| Operation | C-style Array | std::array | std::vector |
|-----------|---------------|------------|-------------|
| Access | O(1) | O(1) | O(1) |
| Insert at End | O(1)* | N/A | O(1) amortized |
| Insert at Beginning | O(n) | O(n) | O(n) |
| Insert at Middle | O(n) | O(n) | O(n) |
| Delete at End | O(1)* | N/A | O(1) |
| Delete at Beginning | O(n) | O(n) | O(n) |
| Delete at Middle | O(n) | O(n) | O(n) |
| Search (unsorted) | O(n) | O(n) | O(n) |
| Memory Overhead | None | None | Some (capacity) |
| Bounds Checking | No | .at() only | .at() only |
| Size Information | Manual | .size() | .size() |

*Requires manual size tracking for C-style arrays

---

## Best Practices

1. **Prefer `std::vector` as default** - It's the most versatile and safe
2. **Use `.reserve()` when size is known** - Prevents multiple reallocations
3. **Use `.at()` for bounds checking** - Safer than `[]` operator in debug code
4. **Use `const auto&` in range loops** - Avoids unnecessary copying
5. **Initialize vectors with size when possible** - Avoids multiple reallocations
6. **Use `.data()` for C API compatibility** - Provides pointer to underlying array
7. **Consider `std::array` for fixed-size data** - Better than C-style arrays
8. **Be aware of iterator invalidation** - Reallocation invalidates all iterators
9. **Use `emplace_back()` over `push_back()`** - More efficient for complex objects
10. **Use `shrink_to_fit()` after large removals** - Reduces memory footprint

---

## Common Pitfalls

1. **Out-of-bounds access** - Use `.at()` or bounds checking
2. **Iterator invalidation** - Insert/erase can invalidate iterators
3. **Copy overhead** - Pass by reference or use move semantics
4. **Memory reallocation** - Causes all iterators to become invalid
5. **Using `[]` when element might not exist** - Use `.at()` for safety
6. **Forgetting to `#include <vector>`** - Common compilation error
7. **Using vector of bool** - Specialized implementation, use vector<char> for speed
8. **Not reserving capacity** - Can cause multiple reallocations
9. **Using vector for frequent insertions at front** - Use `std::deque` instead
10. **Assuming contiguous memory for all containers** - Only vector and array guarantee this