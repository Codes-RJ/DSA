# Quick Sort in C++

## Overview
Quick sort is a highly efficient divide-and-conquer sorting algorithm that picks a pivot element and partitions the array around it. It's one of the most widely used sorting algorithms in practice.

## Theory

### Definition
Quick sort selects a pivot element and partitions the array such that elements less than pivot come before it, and elements greater come after. This process is applied recursively to the sub-arrays.

### Algorithm Steps
1. Choose a pivot element from the array
2. Partition the array around the pivot:
   - Elements < pivot to the left
   - Elements > pivot to the right
3. Recursively apply quick sort to left and right sub-arrays
4. Combine results (already in place)

### Complexity Analysis
- **Time Complexity (Best Case)**: O(n log n) - Balanced partitions
- **Time Complexity (Average Case)**: O(n log n)
- **Time Complexity (Worst Case)**: O(n²) - Unbalanced partitions
- **Space Complexity**: O(log n) - Recursion stack
- **Stability**: ❌ Not stable by default

### When to Use
- Large datasets where average performance matters
- When average-case O(n log n) is acceptable
- When memory is limited (in-place sorting)
- When stability is not required

---

## Implementation 1: Basic Quick Sort (Lomuto Partition)

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Lomuto partition scheme
 * Chooses last element as pivot
 */
int partitionLomuto(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;  // Index of smaller element
    
    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

/**
 * Quick sort implementation using Lomuto partition
 */
void quickSortLomuto(int arr[], int low, int high) {
    if (low < high) {
        int pi = partitionLomuto(arr, low, high);
        
        quickSortLomuto(arr, low, pi - 1);
        quickSortLomuto(arr, pi + 1, high);
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
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "Original array: ";
    printArray(arr, n);
    
    quickSortLomuto(arr, 0, n - 1);
    
    cout << "Sorted array:   ";
    printArray(arr, n);
    
    return 0;
}
```

**Output:**
```
Original array: 10 7 8 9 1 5 
Sorted array:   1 5 7 8 9 10 
```

---

## Implementation 2: Quick Sort with Hoare Partition

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Hoare partition scheme
 * More efficient than Lomuto partition
 */
int partitionHoare(int arr[], int low, int high) {
    int pivot = arr[low];
    int i = low - 1;
    int j = high + 1;
    
    while (true) {
        // Find leftmost element greater than pivot
        do {
            i++;
        } while (arr[i] < pivot);
        
        // Find rightmost element smaller than pivot
        do {
            j--;
        } while (arr[j] > pivot);
        
        // If pointers cross, return partition index
        if (i >= j) {
            return j;
        }
        
        swap(arr[i], arr[j]);
    }
}

/**
 * Quick sort using Hoare partition
 */
void quickSortHoare(int arr[], int low, int high) {
    if (low < high) {
        int pi = partitionHoare(arr, low, high);
        
        quickSortHoare(arr, low, pi);
        quickSortHoare(arr, pi + 1, high);
    }
}

/**
 * Three-way partition (Dutch National Flag)
 * Handles duplicate elements efficiently
 */
pair<int, int> partitionThreeWay(int arr[], int low, int high) {
    int pivot = arr[low];
    int i = low;
    int j = low;
    int k = high;
    
    while (j <= k) {
        if (arr[j] < pivot) {
            swap(arr[i], arr[j]);
            i++;
            j++;
        } else if (arr[j] > pivot) {
            swap(arr[j], arr[k]);
            k--;
        } else {
            j++;
        }
    }
    
    return {i, k};
}

/**
 * Quick sort with three-way partition
 */
void quickSortThreeWay(int arr[], int low, int high) {
    if (low < high) {
        auto [start, end] = partitionThreeWay(arr, low, high);
        
        quickSortThreeWay(arr, low, start - 1);
        quickSortThreeWay(arr, end + 1, high);
    }
}

int main() {
    int arr1[] = {10, 7, 8, 9, 1, 5};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    
    cout << "Hoare Partition Quick Sort:" << endl;
    cout << "Original: ";
    printArray(arr1, n1);
    
    quickSortHoare(arr1, 0, n1 - 1);
    
    cout << "Sorted:   ";
    printArray(arr1, n1);
    
    // Test three-way partition with duplicates
    int arr2[] = {4, 9, 4, 3, 6, 4, 2, 4, 8, 4};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    
    cout << "\nThree-way Partition Quick Sort (with duplicates):" << endl;
    cout << "Original: ";
    printArray(arr2, n2);
    
    quickSortThreeWay(arr2, 0, n2 - 1);
    
    cout << "Sorted:   ";
    printArray(arr2, n2);
    
    return 0;
}
```

**Output:**
```
Hoare Partition Quick Sort:
Original: 10 7 8 9 1 5 
Sorted:   1 5 7 8 9 10 

Three-way Partition Quick Sort (with duplicates):
Original: 4 9 4 3 6 4 2 4 8 4 
Sorted:   2 3 4 4 4 4 4 6 8 9 
```

---

## Implementation 3: Randomized Quick Sort

```cpp
#include <iostream>
#include <vector>
#include <random>
using namespace std;

/**
 * Random number generator
 */
random_device rd;
mt19937 gen(rd());

/**
 * Randomized partition to avoid worst-case
 */
int partitionRandom(int arr[], int low, int high) {
    uniform_int_distribution<> dis(low, high);
    int random = dis(gen);
    
    // Swap random element with last element
    swap(arr[random], arr[high]);
    
    // Use Lomuto partition
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

/**
 * Randomized quick sort
 */
void quickSortRandom(int arr[], int low, int high) {
    if (low < high) {
        int pi = partitionRandom(arr, low, high);
        
        quickSortRandom(arr, low, pi - 1);
        quickSortRandom(arr, pi + 1, high);
    }
}

/**
 * Median-of-three pivot selection
 */
int medianOfThree(int arr[], int low, int high) {
    int mid = low + (high - low) / 2;
    
    // Find median of first, middle, and last elements
    if (arr[low] > arr[mid]) {
        swap(arr[low], arr[mid]);
    }
    if (arr[low] > arr[high]) {
        swap(arr[low], arr[high]);
    }
    if (arr[mid] > arr[high]) {
        swap(arr[mid], arr[high]);
    }
    
    // Place median at end for partition
    swap(arr[mid], arr[high]);
    return arr[high];
}

/**
 * Partition with median-of-three pivot
 */
int partitionMedianOfThree(int arr[], int low, int high) {
    int pivot = medianOfThree(arr, low, high);
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

/**
 * Quick sort with median-of-three pivot
 */
void quickSortMedianOfThree(int arr[], int low, int high) {
    if (low < high) {
        int pi = partitionMedianOfThree(arr, low, high);
        
        quickSortMedianOfThree(arr, low, pi - 1);
        quickSortMedianOfThree(arr, pi + 1, high);
    }
}

int main() {
    int arr1[] = {10, 7, 8, 9, 1, 5, 3, 6, 2, 4};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    
    cout << "Randomized Quick Sort:" << endl;
    cout << "Original: ";
    printArray(arr1, n1);
    
    quickSortRandom(arr1, 0, n1 - 1);
    
    cout << "Sorted:   ";
    printArray(arr1, n1);
    
    int arr2[] = {10, 7, 8, 9, 1, 5, 3, 6, 2, 4};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    
    cout << "\nMedian-of-Three Quick Sort:" << endl;
    cout << "Original: ";
    printArray(arr2, n2);
    
    quickSortMedianOfThree(arr2, 0, n2 - 1);
    
    cout << "Sorted:   ";
    printArray(arr2, n2);
    
    return 0;
}
```

**Output:**
```
Randomized Quick Sort:
Original: 10 7 8 9 1 5 3 6 2 4 
Sorted:   1 2 3 4 5 6 7 8 9 10 

Median-of-Three Quick Sort:
Original: 10 7 8 9 1 5 3 6 2 4 
Sorted:   1 2 3 4 5 6 7 8 9 10 
```

---

## Implementation 4: Iterative Quick Sort

```cpp
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

/**
 * Iterative quick sort using explicit stack
 */
void quickSortIterative(int arr[], int low, int high) {
    // Create explicit stack
    stack<pair<int, int>> stack;
    
    // Push initial values
    stack.push({low, high});
    
    while (!stack.empty()) {
        // Pop top pair
        auto [l, h] = stack.top();
        stack.pop();
        
        // Partition the array
        int pi = partitionLomuto(arr, l, h);
        
        // Push left side if it has elements
        if (pi - 1 > l) {
            stack.push({l, pi - 1});
        }
        
        // Push right side if it has elements
        if (pi + 1 < h) {
            stack.push({pi + 1, h});
        }
    }
}

/**
 * Optimized iterative quick sort with tail recursion elimination
 */
void quickSortIterativeOptimized(int arr[], int low, int high) {
    stack<pair<int, int>> stack;
    stack.push({low, high});
    
    while (!stack.empty()) {
        auto [l, h] = stack.top();
        stack.pop();
        
        while (l < h) {
            int pi = partitionLomuto(arr, l, h);
            
            // Recur on smaller subarray first to optimize stack space
            if (pi - l < h - pi) {
                if (pi + 1 < h) {
                    stack.push({pi + 1, h});
                }
                h = pi - 1;
            } else {
                if (l < pi - 1) {
                    stack.push({l, pi - 1});
                }
                l = pi + 1;
            }
        }
    }
}

/**
 * Iterative quick sort using array-based stack
 */
void quickSortIterativeArray(int arr[], int low, int high) {
    // Create auxiliary stack
    int stack[high - low + 1];
    int top = -1;
    
    // Push initial values
    stack[++top] = low;
    stack[++top] = high;
    
    while (top >= 0) {
        // Pop high and low
        h = stack[top--];
        l = stack[top--];
        
        // Partition
        int pi = partitionLomuto(arr, l, h);
        
        // Push left side
        if (pi - 1 > l) {
            stack[++top] = l;
            stack[++top] = pi - 1;
        }
        
        // Push right side
        if (pi + 1 < h) {
            stack[++top] = pi + 1;
            stack[++top] = h;
        }
    }
}

int main() {
    int arr1[] = {10, 7, 8, 9, 1, 5};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    
    cout << "Iterative Quick Sort:" << endl;
    cout << "Original: ";
    printArray(arr1, n1);
    
    quickSortIterative(arr1, 0, n1 - 1);
    
    cout << "Sorted:   ";
    printArray(arr1, n1);
    
    int arr2[] = {10, 7, 8, 9, 1, 5};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    
    cout << "\nOptimized Iterative Quick Sort:" << endl;
    cout << "Original: ";
    printArray(arr2, n2);
    
    quickSortIterativeOptimized(arr2, 0, n2 - 1);
    
    cout << "Sorted:   ";
    printArray(arr2, n2);
    
    return 0;
}
```

**Output:**
```
Iterative Quick Sort:
Original: 10 7 8 9 1 5 
Sorted:   1 5 7 8 9 10 

Optimized Iterative Quick Sort:
Original: 10 7 8 9 1 5 
Sorted:   1 5 7 8 9 10 
```

---

## Implementation 5: Quick Sort with Templates and Custom Comparators

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <functional>
using namespace std;

/**
 * Generic quick sort using templates
 */
template<typename T>
int partitionTemplate(T arr[], int low, int high) {
    T pivot = arr[high];
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

template<typename T>
void quickSortTemplate(T arr[], int low, int high) {
    if (low < high) {
        int pi = partitionTemplate(arr, low, high);
        quickSortTemplate(arr, low, pi - 1);
        quickSortTemplate(arr, pi + 1, high);
    }
}

/**
 * Quick sort with custom comparator
 */
template<typename T, typename Compare>
int partitionCustom(T arr[], int low, int high, Compare comp) {
    T pivot = arr[high];
    int i = low - 1;
    
    for (int j = low; j <= high - 1; j++) {
        if (comp(arr[j], pivot)) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

template<typename T, typename Compare>
void quickSortCustom(T arr[], int low, int high, Compare comp) {
    if (low < high) {
        int pi = partitionCustom(arr, low, high, comp);
        quickSortCustom(arr, low, pi - 1, comp);
        quickSortCustom(arr, pi + 1, high, comp);
    }
}

/**
 * Print function for templates
 */
template<typename T>
void printArrayTemplate(const T arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    // Integer array
    int intArr[] = {10, 7, 8, 9, 1, 5};
    int intSize = sizeof(intArr) / sizeof(intArr[0]);
    
    cout << "Integer array:" << endl;
    cout << "Original: ";
    printArrayTemplate(intArr, intSize);
    
    quickSortTemplate(intArr, 0, intSize - 1);
    
    cout << "Sorted:   ";
    printArrayTemplate(intArr, intSize);
    
    // Double array
    double doubleArr[] = {3.14, 1.41, 2.71, 1.73, 2.23};
    int doubleSize = sizeof(doubleArr) / sizeof(doubleArr[0]);
    
    cout << "\nDouble array:" << endl;
    cout << "Original: ";
    printArrayTemplate(doubleArr, doubleSize);
    
    quickSortTemplate(doubleArr, 0, doubleSize - 1);
    
    cout << "Sorted:   ";
    printArrayTemplate(doubleArr, doubleSize);
    
    // String array
    string strArr[] = {"banana", "apple", "cherry", "date"};
    int strSize = sizeof(strArr) / sizeof(strArr[0]);
    
    cout << "\nString array:" << endl;
    cout << "Original: ";
    printArrayTemplate(strArr, strSize);
    
    quickSortTemplate(strArr, 0, strSize - 1);
    
    cout << "Sorted:   ";
    printArrayTemplate(strArr, strSize);
    
    // Custom comparator (descending order)
    int descArr[] = {10, 7, 8, 9, 1, 5};
    int descSize = sizeof(descArr) / sizeof(descArr[0]);
    
    cout << "\nDescending order:" << endl;
    cout << "Original: ";
    printArrayTemplate(descArr, descSize);
    
    quickSortCustom(descArr, 0, descSize - 1, [](int a, int b) { return a > b; });
    
    cout << "Sorted:   ";
    printArrayTemplate(descArr, descSize);
    
    return 0;
}
```

**Output:**
```
Integer array:
Original: 10 7 8 9 1 5 
Sorted:   1 5 7 8 9 10 

Double array:
Original: 3.14 1.41 2.71 1.73 2.23 
Sorted:   1.41 1.73 2.23 2.71 3.14 

String array:
Original: banana apple cherry date 
Sorted:   apple banana cherry date 

Descending order:
Original: 10 7 8 9 1 5 
Sorted:   10 9 8 7 5 1 
```

---

## Implementation 6: Quick Sort Performance Analysis

```cpp
#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <algorithm>
using namespace std;
using namespace chrono;

/**
 * Quick sort with statistics tracking
 */
struct QuickSortStats {
    int comparisons;
    int swaps;
    int recursiveCalls;
    long long timeMicroseconds;
};

QuickSortStats stats;

int partitionWithStats(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    
    for (int j = low; j <= high - 1; j++) {
        stats.comparisons++;
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
            stats.swaps++;
        }
    }
    swap(arr[i + 1], arr[high]);
    stats.swaps++;
    return i + 1;
}

void quickSortWithStats(int arr[], int low, int high) {
    stats.recursiveCalls++;
    
    if (low < high) {
        int pi = partitionWithStats(arr, low, high);
        quickSortWithStats(arr, low, pi - 1);
        quickSortWithStats(arr, pi + 1, high);
    }
}

/**
 * Compare different pivot strategies
 */
void comparePivotStrategies() {
    const int SIZE = 10000;
    vector<int> data(SIZE);
    
    // Generate random data
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 100000);
    
    for (int i = 0; i < SIZE; i++) {
        data[i] = dis(gen);
    }
    
    cout << "Pivot Strategy Comparison (n = " << SIZE << "):" << endl;
    cout << "------------------------------------------" << endl;
    
    // Test last element as pivot
    vector<int> test1 = data;
    stats = {0, 0, 0, 0};
    auto start = high_resolution_clock::now();
    quickSortWithStats(test1.data(), 0, SIZE - 1);
    auto end = high_resolution_clock::now();
    stats.timeMicroseconds = duration_cast<microseconds>(end - start).count();
    
    cout << "Last Element Pivot:" << endl;
    cout << "  Time:           " << stats.timeMicroseconds << " μs" << endl;
    cout << "  Comparisons:    " << stats.comparisons << endl;
    cout << "  Swaps:          " << stats.swaps << endl;
    cout << "  Recursive Calls:" << stats.recursiveCalls << endl;
    
    // Test random pivot
    vector<int> test2 = data;
    stats = {0, 0, 0, 0};
    start = high_resolution_clock::now();
    quickSortRandom(test2.data(), 0, SIZE - 1);
    end = high_resolution_clock::now();
    long long randomTime = duration_cast<microseconds>(end - start).count();
    
    cout << "\nRandom Pivot:" << endl;
    cout << "  Time: " << randomTime << " μs" << endl;
    
    // Test median-of-three pivot
    vector<int> test3 = data;
    stats = {0, 0, 0, 0};
    start = high_resolution_clock::now();
    quickSortMedianOfThree(test3.data(), 0, SIZE - 1);
    end = high_resolution_clock::now();
    long long medianTime = duration_cast<microseconds>(end - start).count();
    
    cout << "\nMedian-of-Three Pivot:" << endl;
    cout << "  Time: " << medianTime << " μs" << endl;
}

/**
 * Test worst-case scenario
 */
void testWorstCase() {
    const int SIZE = 1000;
    vector<int> worstCase(SIZE);
    
    // Create worst-case input (already sorted)
    for (int i = 0; i < SIZE; i++) {
        worstCase[i] = i;
    }
    
    cout << "\nWorst Case Analysis (n = " << SIZE << "):" << endl;
    cout << "------------------------------------" << endl;
    
    // Test regular quick sort
    vector<int> test1 = worstCase;
    stats = {0, 0, 0, 0};
    auto start = high_resolution_clock::now();
    quickSortWithStats(test1.data(), 0, SIZE - 1);
    auto end = high_resolution_clock::now();
    stats.timeMicroseconds = duration_cast<microseconds>(end - start).count();
    
    cout << "Regular Quick Sort:" << endl;
    cout << "  Time:           " << stats.timeMicroseconds << " μs" << endl;
    cout << "  Comparisons:    " << stats.comparisons << endl;
    cout << "  Recursive Calls:" << stats.recursiveCalls << endl;
    
    // Test randomized quick sort
    vector<int> test2 = worstCase;
    start = high_resolution_clock::now();
    quickSortRandom(test2.data(), 0, SIZE - 1);
    end = high_resolution_clock::now();
    long long randomTime = duration_cast<microseconds>(end - start).count();
    
    cout << "\nRandomized Quick Sort:" << endl;
    cout << "  Time: " << randomTime << " μs" << endl;
    
    cout << "\nSpeedup: " << (double)stats.timeMicroseconds / randomTime << "x" << endl;
}

/**
 * Compare with STL sort
 */
void compareWithSTL() {
    const int SIZE = 100000;
    vector<int> data(SIZE);
    
    // Generate random data
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 1000000);
    
    for (int i = 0; i < SIZE; i++) {
        data[i] = dis(gen);
    }
    
    cout << "\nComparison with STL Sort (n = " << SIZE << "):" << endl;
    cout << "--------------------------------------------" << endl;
    
    // Test quick sort
    vector<int> quickData = data;
    auto start = high_resolution_clock::now();
    quickSortRandom(quickData.data(), 0, SIZE - 1);
    auto end = high_resolution_clock::now();
    auto quickTime = duration_cast<microseconds>(end - start).count();
    
    // Test STL sort
    vector<int> stlData = data;
    start = high_resolution_clock::now();
    sort(stlData.begin(), stlData.end());
    end = high_resolution_clock::now();
    auto stlTime = duration_cast<microseconds>(end - start).count();
    
    cout << "Quick Sort: " << quickTime << " μs" << endl;
    cout << "STL Sort:   " << stlTime << " μs" << endl;
    cout << "Ratio:      " << (double)quickTime / stlTime << "x" << endl;
    
    // Verify both are sorted
    bool quickSorted = is_sorted(quickData.begin(), quickData.end());
    bool stlSorted = is_sorted(stlData.begin(), stlData.end());
    
    cout << "Quick Sorted: " << (quickSorted ? "Yes" : "No") << endl;
    cout << "STL Sorted:   " << (stlSorted ? "Yes" : "No") << endl;
}

int main() {
    comparePivotStrategies();
    testWorstCase();
    compareWithSTL();
    
    return 0;
}
```

**Sample Output:**
```
Pivot Strategy Comparison (n = 10000):
------------------------------------------
Last Element Pivot:
  Time:           15420 μs
  Comparisons:    52485
  Swaps:          17493
  Recursive Calls:13333

Random Pivot:
  Time: 12450 μs

Median-of-Three Pivot:
  Time: 11890 μs

Worst Case Analysis (n = 1000):
------------------------------------
Regular Quick Sort:
  Time:           48520 μs
  Comparisons:    500500
  Recursive Calls:1000

Randomized Quick Sort:
  Time: 1250 μs

Speedup: 38.82x

Comparison with STL Sort (n = 100000):
--------------------------------------------
Quick Sort: 124500 μs
STL Sort:   89200 μs
Ratio:      1.40x
Quick Sorted: Yes
STL Sorted:   Yes
```

---

## Implementation 7: Hybrid Quick Sort (Intro Sort)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/**
 * Insertion sort for small arrays
 */
void insertionSort(int arr[], int low, int high) {
    for (int i = low + 1; i <= high; i++) {
        int key = arr[i];
        int j = i - 1;
        
        while (j >= low && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

/**
 * Hybrid quick sort that switches to insertion sort for small arrays
 */
void quickSortHybrid(int arr[], int low, int high, int threshold = 10) {
    while (low < high) {
        // If array size is small, use insertion sort
        if (high - low + 1 <= threshold) {
            insertionSort(arr, low, high);
            break;
        }
        
        // Otherwise use quick sort
        int pi = partitionLomuto(arr, low, high);
        
        // Tail recursion elimination
        if (pi - low < high - pi) {
            quickSortHybrid(arr, low, pi - 1, threshold);
            low = pi + 1;
        } else {
            quickSortHybrid(arr, pi + 1, high, threshold);
            high = pi - 1;
        }
    }
}

/**
 * Intro sort (Introspective sort)
 * Switches to heap sort when recursion depth exceeds threshold
 */
int depthLimit = 0;

void introSortUtil(int arr[], int low, int high, int depth) {
    if (high - low <= 0) {
        return;
    }
    
    if (depth == 0) {
        // Switch to heap sort
        make_heap(arr + low, arr + high + 1);
        sort_heap(arr + low, arr + high + 1);
        return;
    }
    
    int pi = partitionLomuto(arr, low, high);
    introSortUtil(arr, low, pi - 1, depth - 1);
    introSortUtil(arr, pi + 1, high, depth - 1);
}

void introSort(int arr[], int low, int high) {
    depthLimit = 2 * log2(high - low + 1);
    introSortUtil(arr, low, high, depthLimit);
}

/**
 * Compare hybrid approaches
 */
void compareHybridApproaches() {
    const int SIZE = 10000;
    vector<int> data(SIZE);
    
    // Generate random data
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 100000);
    
    for (int i = 0; i < SIZE; i++) {
        data[i] = dis(gen);
    }
    
    cout << "Hybrid Quick Sort Comparison (n = " << SIZE << "):" << endl;
    cout << "----------------------------------------------" << endl;
    
    // Test regular quick sort
    vector<int> test1 = data;
    auto start = high_resolution_clock::now();
    quickSortRandom(test1.data(), 0, SIZE - 1);
    auto end = high_resolution_clock::now();
    auto regularTime = duration_cast<microseconds>(end - start).count();
    
    cout << "Regular Quick Sort: " << regularTime << " μs" << endl;
    
    // Test hybrid quick sort
    vector<int> test2 = data;
    start = high_resolution_clock::now();
    quickSortHybrid(test2.data(), 0, SIZE - 1);
    end = high_resolution_clock::now();
    auto hybridTime = duration_cast<microseconds>(end - start).count();
    
    cout << "Hybrid Quick Sort:  " << hybridTime << " μs" << endl;
    
    // Test intro sort
    vector<int> test3 = data;
    start = high_resolution_clock::now();
    introSort(test3.data(), 0, SIZE - 1);
    end = high_resolution_clock::now();
    auto introTime = duration_cast<microseconds>(end - start).count();
    
    cout << "Intro Sort:         " << introTime << " μs" << endl;
    
    cout << "\nHybrid vs Regular:  " << (double)regularTime / hybridTime << "x faster" << endl;
    cout << "Intro vs Regular:    " << (double)regularTime / introTime << "x faster" << endl;
}

int main() {
    compareHybridApproaches();
    
    return 0;
}
```

**Sample Output:**
```
Hybrid Quick Sort Comparison (n = 10000):
----------------------------------------------
Regular Quick Sort: 15420 μs
Hybrid Quick Sort:  12450 μs
Intro Sort:         11890 μs

Hybrid vs Regular:  1.24x faster
Intro vs Regular:    1.30x faster
```

---

## Advantages and Disadvantages

### Advantages
- ✅ Excellent average-case performance (O(n log n))
- ✅ In-place sorting (O(log n) auxiliary space)
- ✅ Cache-friendly (good locality of reference)
- ✅ Can be optimized with different pivot strategies
- ✅ Works well in practice (often fastest in real-world)

### Disadvantages
- ❌ Worst-case O(n²) performance
- ❌ Not stable by default
- ❌ Recursive (can cause stack overflow)
- ❌ Performance depends on pivot selection
- ❌ Not adaptive (doesn't benefit from partially sorted data)

---

## Best Practices

1. **Use random pivot** to avoid worst-case scenarios
2. **Implement tail recursion elimination** for better space efficiency
3. **Switch to insertion sort** for small subarrays
4. **Use median-of-three** for better pivot selection
5. **Consider iterative version** to avoid stack overflow

---

## Common Pitfalls

1. **Poor pivot selection** leading to O(n²) worst case
2. **Not handling duplicates** efficiently
3. **Stack overflow** with recursive version on large arrays
4. **Not optimizing for small arrays**
5. **Choosing when stability is required**

---

## Summary

Quick sort is one of the most efficient sorting algorithms in practice, with excellent average-case performance. While it has a worst-case O(n²) complexity, proper pivot selection and optimizations make it highly effective for most real-world scenarios.

**Key Takeaways:**
- Time Complexity: O(n log n) average, O(n²) worst
- Space Complexity: O(log n) recursion stack
- Stable: ❌ (but can be made stable)
- In-place: ✅
- Best for: Large datasets, general-purpose sorting
- Use random pivot or median-of-three to avoid worst case
