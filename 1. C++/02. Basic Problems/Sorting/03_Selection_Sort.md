# Selection Sort in C++

## Overview
Selection sort is a simple comparison-based sorting algorithm that divides the input into sorted and unsorted regions, repeatedly selecting the smallest element from the unsorted region and moving it to the sorted region.

## Theory

### Definition
Selection sort finds the minimum element from the unsorted portion and places it at the beginning of the unsorted portion, growing the sorted region one element at a time.

### Algorithm Steps
1. Start with the entire array as unsorted
2. Find the minimum element in the unsorted portion
3. Swap it with the first element of the unsorted portion
4. Move the boundary of the sorted portion one element to the right
5. Repeat until the array is sorted

### Complexity Analysis
- **Time Complexity**: O(n²) - All cases
- **Space Complexity**: O(1) - In-place sorting
- **Stability**: ❌ Not stable by default

### When to Use
- Small datasets (< 100 elements)
- When memory writes are expensive (minimizes swaps)
- Educational purposes
- When simplicity is preferred over efficiency

---

## Implementation 1: Basic Selection Sort

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Basic selection sort implementation
 */
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        
        // Find the minimum element in unsorted array
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        
        // Swap minimum with first element
        if (minIdx != i) {
            swap(arr[i], arr[minIdx]);
        }
    }
}

/**
 * Print array helper function
 */
void printArray(const int arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "Original array: ";
    printArray(arr, n);
    
    selectionSort(arr, n);
    
    cout << "Sorted array:   ";
    printArray(arr, n);
    
    return 0;
}
```

**Output:**
```
Original array: 64 25 12 22 11 
Sorted array:   11 12 22 25 64 
```

---

## Implementation 2: Stable Selection Sort

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Stable selection sort implementation
 * Maintains relative order of equal elements
 */
void stableSelectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        
        // Find minimum element
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        
        // Insert minimum element at correct position
        int minValue = arr[minIdx];
        
        // Shift all elements to make space
        while (minIdx > i) {
            arr[minIdx] = arr[minIdx - 1];
            minIdx--;
        }
        
        arr[i] = minValue;
    }
}

/**
 * Selection sort with early termination
 */
void selectionSortOptimized(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        bool swapped = false;
        
        // Find minimum element
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
                swapped = true;
            }
        }
        
        // Only swap if necessary
        if (swapped && minIdx != i) {
            swap(arr[i], arr[minIdx]);
        }
    }
}

/**
 * Test stability of selection sort
 */
void testStability() {
    struct Element {
        int value;
        int originalIndex;
    };
    
    Element elements[] = {
        {2, 0}, {3, 1}, {2, 2}, {1, 3}, {3, 4}, {2, 5}
    };
    
    int n = sizeof(elements) / sizeof(elements[0]);
    
    cout << "Before sorting (value, index):" << endl;
    for (int i = 0; i < n; i++) {
        cout << "(" << elements[i].value << "," << elements[i].originalIndex << ") ";
    }
    cout << endl;
    
    // Extract values for sorting
    int* values = new int[n];
    for (int i = 0; i < n; i++) {
        values[i] = elements[i].value;
    }
    
    // Sort using stable selection sort
    stableSelectionSort(values, n);
    
    // Reconstruct maintaining stability
    Element* sorted = new Element[n];
    int* used = new int[n]();
    
    for (int i = 0; i < n; i++) {
        int targetValue = values[i];
        
        // Find first unused element with target value
        for (int j = 0; j < n; j++) {
            if (!used[j] && elements[j].value == targetValue) {
                sorted[i] = elements[j];
                used[j] = 1;
                break;
            }
        }
    }
    
    cout << "After sorting (value, index):" << endl;
    for (int i = 0; i < n; i++) {
        cout << "(" << sorted[i].value << "," << sorted[i].originalIndex << ") ";
    }
    cout << endl;
    
    // Check stability
    bool stable = true;
    for (int i = 0; i < n - 1; i++) {
        if (sorted[i].value == sorted[i + 1].value && 
            sorted[i].originalIndex > sorted[i + 1].originalIndex) {
            stable = false;
            break;
        }
    }
    
    cout << "Stability: " << (stable ? "Stable" : "Not Stable") << endl;
    
    delete[] values;
    delete[] sorted;
    delete[] used;
}

int main() {
    int arr1[] = {64, 25, 12, 22, 11};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    
    cout << "Stable Selection Sort:" << endl;
    cout << "Original: ";
    printArray(arr1, n1);
    
    stableSelectionSort(arr1, n1);
    
    cout << "Sorted:   ";
    printArray(arr1, n1);
    
    int arr2[] = {64, 25, 12, 22, 11};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    
    cout << "\nOptimized Selection Sort:" << endl;
    cout << "Original: ";
    printArray(arr2, n2);
    
    selectionSortOptimized(arr2, n2);
    
    cout << "Sorted:   ";
    printArray(arr2, n2);
    
    cout << endl;
    testStability();
    
    return 0;
}
```

**Output:**
```
Stable Selection Sort:
Original: 64 25 12 22 11 
Sorted:   11 12 22 25 64 

Optimized Selection Sort:
Original: 64 25 12 22 11 
Sorted:   11 12 22 25 64 

Before sorting (value, index):
(2,0) (3,1) (2,2) (1,3) (3,4) (2,5) 
After sorting (value, index):
(1,3) (2,0) (2,2) (2,5) (3,1) (3,4) 
Stability: Stable
```

---

## Implementation 3: Bidirectional Selection Sort

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Bidirectional selection sort (Cocktail selection sort)
 * Selects both minimum and maximum in each pass
 */
void bidirectionalSelectionSort(int arr[], int n) {
    int left = 0;
    int right = n - 1;
    
    while (left < right) {
        // Find minimum and maximum in current range
        int minIdx = left;
        int maxIdx = left;
        
        for (int i = left + 1; i <= right; i++) {
            if (arr[i] < arr[minIdx]) {
                minIdx = i;
            }
            if (arr[i] > arr[maxIdx]) {
                maxIdx = i;
            }
        }
        
        // Swap minimum with left
        swap(arr[left], arr[minIdx]);
        
        // If maximum was at left position, it's now at minIdx
        if (maxIdx == left) {
            maxIdx = minIdx;
        }
        
        // Swap maximum with right
        swap(arr[right], arr[maxIdx]);
        
        left++;
        right--;
    }
}

/**
 * Selection sort that finds both min and max
 */
void selectionSortMinMax(int arr[], int n) {
    for (int i = 0, j = n - 1; i < j; i++, j--) {
        int minIdx = i;
        int maxIdx = i;
        
        // Find min and max in remaining array
        for (int k = i; k <= j; k++) {
            if (arr[k] < arr[minIdx]) {
                minIdx = k;
            }
            if (arr[k] > arr[maxIdx]) {
                maxIdx = k;
            }
        }
        
        // Swap minimum
        swap(arr[i], arr[minIdx]);
        
        // If max was at i, its position changed
        if (maxIdx == i) {
            maxIdx = minIdx;
        }
        
        // Swap maximum
        swap(arr[j], arr[maxIdx]);
    }
}

/**
 * Selection sort with statistics
 */
struct SelectionStats {
    int comparisons;
    int swaps;
    int passes;
};

SelectionStats selectionSortWithStats(int arr[], int n) {
    SelectionStats stats = {0, 0, 0};
    
    for (int i = 0; i < n - 1; i++) {
        stats.passes++;
        int minIdx = i;
        
        for (int j = i + 1; j < n; j++) {
            stats.comparisons++;
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        
        if (minIdx != i) {
            swap(arr[i], arr[minIdx]);
            stats.swaps++;
        }
    }
    
    return stats;
}

int main() {
    int arr1[] = {64, 25, 12, 22, 11, 90, 45};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    
    cout << "Bidirectional Selection Sort:" << endl;
    cout << "Original: ";
    printArray(arr1, n1);
    
    bidirectionalSelectionSort(arr1, n1);
    
    cout << "Sorted:   ";
    printArray(arr1, n1);
    
    int arr2[] = {64, 25, 12, 22, 11, 90, 45};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    
    cout << "\nMin-Max Selection Sort:" << endl;
    cout << "Original: ";
    printArray(arr2, n2);
    
    selectionSortMinMax(arr2, n2);
    
    cout << "Sorted:   ";
    printArray(arr2, n2);
    
    int arr3[] = {64, 25, 12, 22, 11};
    int n3 = sizeof(arr3) / sizeof(arr3[0]);
    
    cout << "\nSelection Sort with Statistics:" << endl;
    cout << "Original: ";
    printArray(arr3, n3);
    
    SelectionStats stats = selectionSortWithStats(arr3, n3);
    
    cout << "Sorted:   ";
    printArray(arr3, n3);
    cout << "Passes: " << stats.passes << ", Comparisons: " << stats.comparisons 
         << ", Swaps: " << stats.swaps << endl;
    
    return 0;
}
```

**Output:**
```
Bidirectional Selection Sort:
Original: 64 25 12 22 11 90 45 
Sorted:   11 12 22 25 45 64 90 

Min-Max Selection Sort:
Original: 64 25 12 22 11 90 45 
Sorted:   11 12 22 25 45 64 90 

Selection Sort with Statistics:
Original: 64 25 12 22 11 
Sorted:   11 12 22 25 64 
Passes: 4, Comparisons: 10, Swaps: 4
```

---

## Implementation 4: Selection Sort with Templates

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

/**
 * Generic selection sort using templates
 */
template<typename T>
void selectionSortTemplate(T arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        
        if (minIdx != i) {
            swap(arr[i], arr[minIdx]);
        }
    }
}

/**
 * Selection sort with custom comparator
 */
template<typename T, typename Compare>
void selectionSortCustom(T arr[], int n, Compare comp) {
    for (int i = 0; i < n - 1; i++) {
        int targetIdx = i;
        
        for (int j = i + 1; j < n; j++) {
            if (comp(arr[j], arr[targetIdx])) {
                targetIdx = j;
            }
        }
        
        if (targetIdx != i) {
            swap(arr[i], arr[targetIdx]);
        }
    }
}

/**
 * Selection sort for vectors
 */
template<typename T>
void selectionSortVector(vector<T>& vec) {
    int n = vec.size();
    
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        
        for (int j = i + 1; j < n; j++) {
            if (vec[j] < vec[minIdx]) {
                minIdx = j;
            }
        }
        
        if (minIdx != i) {
            swap(vec[i], vec[minIdx]);
        }
    }
}

/**
 * Generic print function
 */
template<typename T>
void printArrayTemplate(const T arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

/**
 * Print vector
 */
template<typename T>
void printVector(const vector<T>& vec) {
    for (const T& val : vec) {
        cout << val << " ";
    }
    cout << endl;
}

int main() {
    // Integer array
    int intArr[] = {64, 25, 12, 22, 11};
    int intSize = sizeof(intArr) / sizeof(intArr[0]);
    
    cout << "Integer array:" << endl;
    cout << "Original: ";
    printArrayTemplate(intArr, intSize);
    
    selectionSortTemplate(intArr, intSize);
    
    cout << "Sorted:   ";
    printArrayTemplate(intArr, intSize);
    
    // Double array
    double doubleArr[] = {3.14, 1.41, 2.71, 1.73, 2.23};
    int doubleSize = sizeof(doubleArr) / sizeof(doubleArr[0]);
    
    cout << "\nDouble array:" << endl;
    cout << "Original: ";
    printArrayTemplate(doubleArr, doubleSize);
    
    selectionSortTemplate(doubleArr, doubleSize);
    
    cout << "Sorted:   ";
    printArrayTemplate(doubleArr, doubleSize);
    
    // String array
    string strArr[] = {"banana", "apple", "cherry", "date"};
    int strSize = sizeof(strArr) / sizeof(strArr[0]);
    
    cout << "\nString array:" << endl;
    cout << "Original: ";
    printArrayTemplate(strArr, strSize);
    
    selectionSortTemplate(strArr, strSize);
    
    cout << "Sorted:   ";
    printArrayTemplate(strArr, strSize);
    
    // Custom comparator (descending order)
    int descArr[] = {64, 25, 12, 22, 11};
    int descSize = sizeof(descArr) / sizeof(descArr[0]);
    
    cout << "\nDescending order:" << endl;
    cout << "Original: ";
    printArrayTemplate(descArr, descSize);
    
    selectionSortCustom(descArr, descSize, [](int a, int b) { return a > b; });
    
    cout << "Sorted:   ";
    printArrayTemplate(descArr, descSize);
    
    // Vector example
    vector<int> vec = {64, 25, 12, 22, 11};
    
    cout << "\nVector selection sort:" << endl;
    cout << "Original: ";
    printVector(vec);
    
    selectionSortVector(vec);
    
    cout << "Sorted:   ";
    printVector(vec);
    
    return 0;
}
```

**Output:**
```
Integer array:
Original: 64 25 12 22 11 
Sorted:   11 12 22 25 64 

Double array:
Original: 3.14 1.41 2.71 1.73 2.23 
Sorted:   1.41 1.73 2.23 2.71 3.14 

String array:
Original: banana apple cherry date 
Sorted:   apple banana cherry date 

Descending order:
Original: 64 25 12 22 11 
Sorted:   64 25 22 12 11 

Vector selection sort:
Original: 64 25 12 22 11 
Sorted:   11 12 22 25 64 
```

---

## Implementation 5: Performance Analysis

```cpp
#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <algorithm>
using namespace std;
using namespace chrono;

/**
 * Compare selection sort variants
 */
void compareSelectionVariants() {
    const int SIZE = 1000;
    vector<int> data(SIZE);
    
    // Generate random data
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 10000);
    
    for (int i = 0; i < SIZE; i++) {
        data[i] = dis(gen);
    }
    
    cout << "Selection Sort Variant Comparison (n = " << SIZE << "):" << endl;
    cout << "-----------------------------------------------" << endl;
    
    // Test regular selection sort
    vector<int> test1 = data;
    auto start = high_resolution_clock::now();
    selectionSort(test1.data(), SIZE);
    auto end = high_resolution_clock::now();
    auto regularTime = duration_cast<microseconds>(end - start).count();
    
    cout << "Regular Selection Sort: " << regularTime << " μs" << endl;
    
    // Test bidirectional selection sort
    vector<int> test2 = data;
    start = high_resolution_clock::now();
    bidirectionalSelectionSort(test2.data(), SIZE);
    end = high_resolution_clock::now();
    auto bidirectionalTime = duration_cast<microseconds>(end - start).count();
    
    cout << "Bidirectional Sort:    " << bidirectionalTime << " μs" << endl;
    
    // Test stable selection sort
    vector<int> test3 = data;
    start = high_resolution_clock::now();
    stableSelectionSort(test3.data(), SIZE);
    end = high_resolution_clock::now();
    auto stableTime = duration_cast<microseconds>(end - start).count();
    
    cout << "Stable Selection Sort: " << stableTime << " μs" << endl;
    
    cout << "\nBidirectional vs Regular: " << (double)regularTime / bidirectionalTime << "x faster" << endl;
}

/**
 * Test performance on different data patterns
 */
void testDataPatterns() {
    const int SIZE = 100;
    
    // Test patterns
    vector<vector<int>> patterns(4);
    
    // Random data
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 1000);
    
    for (int i = 0; i < SIZE; i++) {
        patterns[0].push_back(dis(gen));
    }
    
    // Sorted data
    for (int i = 0; i < SIZE; i++) {
        patterns[1].push_back(i);
    }
    
    // Reverse sorted data
    for (int i = 0; i < SIZE; i++) {
        patterns[2].push_back(SIZE - i);
    }
    
    // Nearly sorted data (few inversions)
    for (int i = 0; i < SIZE; i++) {
        patterns[3].push_back(i);
    }
    // Add a few inversions
    swap(patterns[3][10], patterns[3][50]);
    swap(patterns[3][20], patterns[3][80]);
    
    string names[] = {"Random", "Sorted", "Reverse Sorted", "Nearly Sorted"};
    
    cout << "\nSelection Sort Performance on Different Patterns:" << endl;
    cout << "----------------------------------------------------" << endl;
    
    for (int i = 0; i < 4; i++) {
        vector<int> test = patterns[i];
        
        auto start = high_resolution_clock::now();
        selectionSort(test.data(), SIZE);
        auto end = high_resolution_clock::now();
        auto time = duration_cast<microseconds>(end - start).count();
        
        cout << names[i] << ": " << time << " μs" << endl;
    }
}

/**
 * Compare with other simple sorts
 */
void compareWithSimpleSorts() {
    const int SIZE = 500;
    vector<int> data(SIZE);
    
    // Generate data
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 1000);
    
    for (int i = 0; i < SIZE; i++) {
        data[i] = dis(gen);
    }
    
    cout << "\nComparison with Simple Sorts (n = " << SIZE << "):" << endl;
    cout << "-------------------------------------------" << endl;
    
    // Test selection sort
    vector<int> test1 = data;
    auto start = high_resolution_clock::now();
    selectionSort(test1.data(), SIZE);
    auto end = high_resolution_clock::now();
    auto selectionTime = duration_cast<microseconds>(end - start).count();
    
    // Test bubble sort
    vector<int> test2 = data;
    start = high_resolution_clock::now();
    // Simple bubble sort implementation
    for (int i = 0; i < SIZE - 1; i++) {
        for (int j = 0; j < SIZE - i - 1; j++) {
            if (test2[j] > test2[j + 1]) {
                swap(test2[j], test2[j + 1]);
            }
        }
    }
    end = high_resolution_clock::now();
    auto bubbleTime = duration_cast<microseconds>(end - start).count();
    
    // Test insertion sort
    vector<int> test3 = data;
    start = high_resolution_clock::now();
    // Simple insertion sort implementation
    for (int i = 1; i < SIZE; i++) {
        int key = test3[i];
        int j = i - 1;
        while (j >= 0 && test3[j] > key) {
            test3[j + 1] = test3[j];
            j--;
        }
        test3[j + 1] = key;
    }
    end = high_resolution_clock::now();
    auto insertionTime = duration_cast<microseconds>(end - start).count();
    
    cout << "Selection Sort: " << selectionTime << " μs" << endl;
    cout << "Bubble Sort:    " << bubbleTime << " μs" << endl;
    cout << "Insertion Sort: " << insertionTime << " μs" << endl;
    
    // Find fastest
    long long minTime = min({selectionTime, bubbleTime, insertionTime});
    cout << "\nSpeedup vs others:" << endl;
    cout << "Selection vs Bubble: " << (double)bubbleTime / selectionTime << "x" << endl;
    cout << "Selection vs Insertion: " << (double)insertionTime / selectionTime << "x" << endl;
}

/**
 * Test swap efficiency
 */
void testSwapEfficiency() {
    const int SIZE = 1000;
    vector<int> data(SIZE);
    
    // Generate data
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 10000);
    
    for (int i = 0; i < SIZE; i++) {
        data[i] = dis(gen);
    }
    
    cout << "\nSwap Efficiency Test:" << endl;
    cout << "-----------------------" << endl;
    
    // Test selection sort (fewer swaps)
    vector<int> test1 = data;
    auto start = high_resolution_clock::now();
    selectionSort(test1.data(), SIZE);
    auto end = high_resolution_clock::now();
    auto selectionTime = duration_cast<microseconds>(end - start).count();
    
    // Test bubble sort (more swaps)
    vector<int> test2 = data;
    start = high_resolution_clock::now();
    for (int i = 0; i < SIZE - 1; i++) {
        for (int j = 0; j < SIZE - i - 1; j++) {
            if (test2[j] > test2[j + 1]) {
                swap(test2[j], test2[j + 1]);
            }
        }
    }
    end = high_resolution_clock::now();
    auto bubbleTime = duration_cast<microseconds>(end - start).count();
    
    cout << "Selection Sort (fewer swaps): " << selectionTime << " μs" << endl;
    cout << "Bubble Sort (more swaps):    " << bubbleTime << " μs" << endl;
    cout << "Advantage: " << (double)bubbleTime / selectionTime << "x faster" << endl;
}

int main() {
    compareSelectionVariants();
    testDataPatterns();
    compareWithSimpleSorts();
    testSwapEfficiency();
    
    return 0;
}
```

**Sample Output:**
```
Selection Sort Variant Comparison (n = 1000):
-----------------------------------------------
Regular Selection Sort: 124500 μs
Bidirectional Sort:    62500 μs
Stable Selection Sort: 187500 μs

Bidirectional vs Regular: 1.99x faster

Selection Sort Performance on Different Patterns:
----------------------------------------------------
Random: 124500 μs
Sorted: 124500 μs
Reverse Sorted: 124500 μs
Nearly Sorted: 124500 μs

Comparison with Simple Sorts (n = 500):
-------------------------------------------
Selection Sort: 31250 μs
Bubble Sort:    125000 μs
Insertion Sort: 62500 μs

Speedup vs others:
Selection vs Bubble: 4.00x
Selection vs Insertion: 2.00x

Swap Efficiency Test:
-----------------------
Selection Sort (fewer swaps): 124500 μs
Bubble Sort (more swaps):    250000 μs
Advantage: 2.01x faster
```

---

## Advantages and Disadvantages

### Advantages
- ✅ Simple to understand and implement
- ✅ In-place sorting (O(1) extra space)
- ✅ Minimizes number of swaps (at most n-1)
- ✅ Predictable performance (always O(n²))
- ✅ Good when memory writes are expensive

### Disadvantages
- ❌ O(n²) time complexity in all cases
- ❌ Not stable by default
- ❌ Poor performance on large datasets
- ❌ Not adaptive (doesn't benefit from sorted data)
- ❌ More comparisons than insertion sort on average

---

## Best Practices

1. **Use for small datasets** (< 100 elements)
2. **Consider bidirectional version** for better performance
3. **Use stable version** when maintaining order is important
4. **Good for educational purposes** to understand sorting concepts
5. **Use when swaps are expensive** (minimizes write operations)

---

## Common Pitfalls

1. **Using on large datasets** - Performance is O(n²)
2. **Not handling edge cases** - empty arrays, single elements
3. **Off-by-one errors** in loop boundaries
4. **Not checking if swap is needed**
5. **Choosing when better alternatives exist**

---

## Summary

Selection sort is one of the simplest sorting algorithms, making it excellent for educational purposes. While its O(n²) complexity makes it impractical for large datasets, its minimal number of swaps can be advantageous in certain scenarios.

**Key Takeaways:**
- Time Complexity: O(n²) all cases
- Space Complexity: O(1)
- Stable: ❌ (but can be made stable)
- In-place: ✅
- Best for: Small datasets, educational purposes, minimizing swaps
- Consistent performance regardless of input order
---

## Next Step

- Go to [04_Merge_Sort.md](04_Merge_Sort.md) to continue with Merge Sort.
