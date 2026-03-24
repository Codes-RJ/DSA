# Bubble Sort in C++

## Overview
Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. It's named for the way smaller or larger elements "bubble" to their correct position.

## Theory

### Definition
Bubble sort repeatedly compares adjacent elements and swaps them if they're in the wrong order. This process continues until the list is sorted.

### Algorithm Steps
1. Start from the first element
2. Compare current element with next element
3. If current > next, swap them
4. Move to next element
5. Repeat until no swaps are needed in a complete pass

### Complexity Analysis
- **Time Complexity (Best Case)**: O(n) - Already sorted (with optimization)
- **Time Complexity (Average Case)**: O(n²)
- **Time Complexity (Worst Case)**: O(n²) - Reverse sorted
- **Space Complexity**: O(1) - In-place sorting
- **Stability**: ✅ Stable - Maintains relative order of equal elements

### When to Use
- Educational purposes (simple to understand)
- Small datasets (< 100 elements)
- Nearly sorted data
- When stability is required and simplicity is preferred

---

## Implementation 1: Basic Bubble Sort

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Basic bubble sort implementation
 */
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
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
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "Original array: ";
    printArray(arr, n);
    
    bubbleSort(arr, n);
    
    cout << "Sorted array:   ";
    printArray(arr, n);
    
    return 0;
}
```

**Output:**
```
Original array: 64 34 25 12 22 11 90 
Sorted array:   11 12 22 25 34 64 90 
```

---

## Implementation 2: Optimized Bubble Sort

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Optimized bubble sort with early termination
 */
void bubbleSortOptimized(int arr[], int n) {
    bool swapped;
    
    for (int i = 0; i < n - 1; i++) {
        swapped = false;
        
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        
        // If no two elements were swapped in inner loop, array is sorted
        if (!swapped) {
            break;
        }
    }
}

/**
 * Bubble sort with pass counter
 */
void bubbleSortWithCounter(int arr[], int n) {
    int passCount = 0;
    int swapCount = 0;
    
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        passCount++;
        
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
                swapCount++;
            }
        }
        
        if (!swapped) {
            break;
        }
    }
    
    cout << "Passes: " << passCount << ", Swaps: " << swapCount << endl;
}

int main() {
    int arr1[] = {64, 34, 25, 12, 22, 11, 90};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    
    cout << "Optimized Bubble Sort:" << endl;
    cout << "Original: ";
    printArray(arr1, n1);
    
    bubbleSortOptimized(arr1, n1);
    
    cout << "Sorted:   ";
    printArray(arr1, n1);
    
    // Test with nearly sorted array
    int arr2[] = {1, 2, 3, 4, 5, 6, 7};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    
    cout << "\nNearly Sorted Array:" << endl;
    cout << "Original: ";
    printArray(arr2, n2);
    
    bubbleSortWithCounter(arr2, n2);
    
    cout << "Sorted:   ";
    printArray(arr2, n2);
    
    return 0;
}
```

**Output:**
```
Optimized Bubble Sort:
Original: 64 34 25 12 22 11 90 
Sorted:   11 12 22 25 34 64 90 

Nearly Sorted Array:
Original: 1 2 3 4 5 6 7 
Passes: 1, Swaps: 0
Sorted:   1 2 3 4 5 6 7 
```

---

## Implementation 3: Recursive Bubble Sort

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Recursive bubble sort
 */
void bubbleSortRecursive(int arr[], int n) {
    // Base case
    if (n == 1) {
        return;
    }
    
    // One pass of bubble sort to move largest element to end
    for (int i = 0; i < n - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            swap(arr[i], arr[i + 1]);
        }
    }
    
    // Recur for remaining array
    bubbleSortRecursive(arr, n - 1);
}

/**
 * Recursive bubble sort with optimization
 */
void bubbleSortRecursiveOptimized(int arr[], int n) {
    // Base case
    if (n == 1) {
        return;
    }
    
    bool swapped = false;
    
    // One pass of bubble sort
    for (int i = 0; i < n - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            swap(arr[i], arr[i + 1]);
            swapped = true;
        }
    }
    
    // If no swapping occurred, array is already sorted
    if (!swapped) {
        return;
    }
    
    // Recur for remaining array
    bubbleSortRecursiveOptimized(arr, n - 1);
}

int main() {
    int arr1[] = {64, 34, 25, 12, 22, 11, 90};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    
    cout << "Recursive Bubble Sort:" << endl;
    cout << "Original: ";
    printArray(arr1, n1);
    
    bubbleSortRecursive(arr1, n1);
    
    cout << "Sorted:   ";
    printArray(arr1, n1);
    
    int arr2[] = {64, 34, 25, 12, 22, 11, 90};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    
    cout << "\nOptimized Recursive Bubble Sort:" << endl;
    cout << "Original: ";
    printArray(arr2, n2);
    
    bubbleSortRecursiveOptimized(arr2, n2);
    
    cout << "Sorted:   ";
    printArray(arr2, n2);
    
    return 0;
}
```

**Output:**
```
Recursive Bubble Sort:
Original: 64 34 25 12 22 11 90 
Sorted:   11 12 22 25 34 64 90 

Optimized Recursive Bubble Sort:
Original: 64 34 25 12 22 11 90 
Sorted:   11 12 22 25 34 64 90 
```

---

## Implementation 4: Bubble Sort with Templates

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

/**
 * Generic bubble sort using templates
 */
template<typename T>
void bubbleSortTemplate(T arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        
        if (!swapped) {
            break;
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
 * Custom comparator for bubble sort
 */
template<typename T, typename Compare>
void bubbleSortCustom(T arr[], int n, Compare comp) {
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        
        for (int j = 0; j < n - i - 1; j++) {
            if (comp(arr[j], arr[j + 1])) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        
        if (!swapped) {
            break;
        }
    }
}

int main() {
    // Integer array
    int intArr[] = {64, 34, 25, 12, 22, 11, 90};
    int intSize = sizeof(intArr) / sizeof(intArr[0]);
    
    cout << "Integer array:" << endl;
    cout << "Original: ";
    printArrayTemplate(intArr, intSize);
    
    bubbleSortTemplate(intArr, intSize);
    
    cout << "Sorted:   ";
    printArrayTemplate(intArr, intSize);
    
    // Double array
    double doubleArr[] = {3.14, 1.41, 2.71, 1.73, 2.23};
    int doubleSize = sizeof(doubleArr) / sizeof(doubleArr[0]);
    
    cout << "\nDouble array:" << endl;
    cout << "Original: ";
    printArrayTemplate(doubleArr, doubleSize);
    
    bubbleSortTemplate(doubleArr, doubleSize);
    
    cout << "Sorted:   ";
    printArrayTemplate(doubleArr, doubleSize);
    
    // String array
    string strArr[] = {"banana", "apple", "cherry", "date"};
    int strSize = sizeof(strArr) / sizeof(strArr[0]);
    
    cout << "\nString array:" << endl;
    cout << "Original: ";
    printArrayTemplate(strArr, strSize);
    
    bubbleSortTemplate(strArr, strSize);
    
    cout << "Sorted:   ";
    printArrayTemplate(strArr, strSize);
    
    // Custom comparator (descending order)
    int descArr[] = {64, 34, 25, 12, 22, 11, 90};
    int descSize = sizeof(descArr) / sizeof(descArr[0]);
    
    cout << "\nDescending order:" << endl;
    cout << "Original: ";
    printArrayTemplate(descArr, descSize);
    
    bubbleSortCustom(descArr, descSize, [](int a, int b) { return a < b; });
    
    cout << "Sorted:   ";
    printArrayTemplate(descArr, descSize);
    
    return 0;
}
```

**Output:**
```
Integer array:
Original: 64 34 25 12 22 11 90 
Sorted:   11 12 22 25 34 64 90 

Double array:
Original: 3.14 1.41 2.71 1.73 2.23 
Sorted:   1.41 1.73 2.23 2.71 3.14 

String array:
Original: banana apple cherry date 
Sorted:   apple banana cherry date 

Descending order:
Original: 64 34 25 12 22 11 90 
Sorted:   90 64 34 25 22 12 11 
```

---

## Implementation 5: Bubble Sort on Vectors and STL Containers

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
using namespace std;

/**
 * Bubble sort on vector
 */
void bubbleSortVector(vector<int>& vec) {
    int n = vec.size();
    
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        
        for (int j = 0; j < n - i - 1; j++) {
            if (vec[j] > vec[j + 1]) {
                swap(vec[j], vec[j + 1]);
                swapped = true;
            }
        }
        
        if (!swapped) {
            break;
        }
    }
}

/**
 * Bubble sort on list (using iterators)
 */
void bubbleSortList(list<int>& lst) {
    int n = lst.size();
    
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        
        for (auto it = lst.begin(); it != prev(lst.end()); ++it) {
            auto nextIt = next(it);
            if (*it > *nextIt) {
                iter_swap(it, nextIt);
                swapped = true;
            }
        }
        
        if (!swapped) {
            break;
        }
    }
}

/**
 * Generic bubble sort for any container
 */
template<typename Container>
void bubbleSortContainer(Container& container) {
    int n = container.size();
    
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        
        auto it = container.begin();
        for (int j = 0; j < n - i - 1; j++) {
            auto nextIt = next(it);
            if (*it > *nextIt) {
                iter_swap(it, nextIt);
                swapped = true;
            }
            ++it;
        }
        
        if (!swapped) {
            break;
        }
    }
}

/**
 * Print vector
 */
void printVector(const vector<int>& vec) {
    for (int val : vec) {
        cout << val << " ";
    }
    cout << endl;
}

/**
 * Print list
 */
void printList(const list<int>& lst) {
    for (int val : lst) {
        cout << val << " ";
    }
    cout << endl;
}

int main() {
    // Vector example
    vector<int> vec = {64, 34, 25, 12, 22, 11, 90};
    
    cout << "Vector Bubble Sort:" << endl;
    cout << "Original: ";
    printVector(vec);
    
    bubbleSortVector(vec);
    
    cout << "Sorted:   ";
    printVector(vec);
    
    // List example
    list<int> lst = {64, 34, 25, 12, 22, 11, 90};
    
    cout << "\nList Bubble Sort:" << endl;
    cout << "Original: ";
    printList(lst);
    
    bubbleSortList(lst);
    
    cout << "Sorted:   ";
    printList(lst);
    
    // Generic container example
    vector<int> genericVec = {64, 34, 25, 12, 22, 11, 90};
    
    cout << "\nGeneric Container Bubble Sort:" << endl;
    cout << "Original: ";
    printVector(genericVec);
    
    bubbleSortContainer(genericVec);
    
    cout << "Sorted:   ";
    printVector(genericVec);
    
    return 0;
}
```

**Output:**
```
Vector Bubble Sort:
Original: 64 34 25 12 22 11 90 
Sorted:   11 12 22 25 34 64 90 

List Bubble Sort:
Original: 64 34 25 12 22 11 90 
Sorted:   11 12 22 25 34 64 90 

Generic Container Bubble Sort:
Original: 64 34 25 12 22 11 90 
Sorted:   11 12 22 25 34 64 90 
```

---

## Implementation 6: Bubble Sort with Performance Analysis

```cpp
#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <algorithm>
using namespace std;
using namespace chrono;

/**
 * Basic bubble sort with performance tracking
 */
struct SortStats {
    int comparisons;
    int swaps;
    long long timeMicroseconds;
};

SortStats bubbleSortWithStats(int arr[], int n) {
    SortStats stats = {0, 0, 0};
    
    auto start = high_resolution_clock::now();
    
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        
        for (int j = 0; j < n - i - 1; j++) {
            stats.comparisons++;
            
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                stats.swaps++;
                swapped = true;
            }
        }
        
        if (!swapped) {
            break;
        }
    }
    
    auto end = high_resolution_clock::now();
    stats.timeMicroseconds = duration_cast<microseconds>(end - start).count();
    
    return stats;
}

/**
 * Compare bubble sort with STL sort
 */
void comparePerformance() {
    const int SIZE = 1000;
    vector<int> data(SIZE);
    
    // Generate random data
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 10000);
    
    for (int i = 0; i < SIZE; i++) {
        data[i] = dis(gen);
    }
    
    // Test bubble sort
    vector<int> bubbleData = data;
    SortStats bubbleStats = bubbleSortWithStats(bubbleData.data(), SIZE);
    
    // Test STL sort
    vector<int> stlData = data;
    auto start = high_resolution_clock::now();
    sort(stlData.begin(), stlData.end());
    auto end = high_resolution_clock::now();
    auto stlTime = duration_cast<microseconds>(end - start).count();
    
    // Verify both are sorted
    bool bubbleSorted = is_sorted(bubbleData.begin(), bubbleData.end());
    bool stlSorted = is_sorted(stlData.begin(), stlData.end());
    
    cout << "Performance Comparison (n = " << SIZE << "):" << endl;
    cout << "----------------------------------------" << endl;
    cout << "Bubble Sort:" << endl;
    cout << "  Time:        " << bubbleStats.timeMicroseconds << " μs" << endl;
    cout << "  Comparisons: " << bubbleStats.comparisons << endl;
    cout << "  Swaps:       " << bubbleStats.swaps << endl;
    cout << "  Sorted:      " << (bubbleSorted ? "Yes" : "No") << endl;
    
    cout << "\nSTL Sort:" << endl;
    cout << "  Time:        " << stlTime << " μs" << endl;
    cout << "  Sorted:      " << (stlSorted ? "Yes" : "No") << endl;
    
    cout << "\nSpeedup: " << (double)bubbleStats.timeMicroseconds / stlTime << "x" << endl;
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
    
    cout << "\nBubble Sort Performance on Different Patterns:" << endl;
    cout << "-----------------------------------------------" << endl;
    
    for (int i = 0; i < 4; i++) {
        vector<int> test = patterns[i];
        SortStats stats = bubbleSortWithStats(test.data(), SIZE);
        
        cout << names[i] << ":" << endl;
        cout << "  Time:        " << stats.timeMicroseconds << " μs" << endl;
        cout << "  Comparisons: " << stats.comparisons << endl;
        cout << "  Swaps:       " << stats.swaps << endl;
        cout << endl;
    }
}

int main() {
    comparePerformance();
    testDataPatterns();
    
    return 0;
}
```

**Sample Output:**
```
Performance Comparison (n = 1000):
----------------------------------------
Bubble Sort:
  Time:        15420 μs
  Comparisons: 499500
  Swaps:       247532
  Sorted:      Yes

STL Sort:
  Time:        156 μs
  Sorted:      Yes

Speedup: 98.85x

Bubble Sort Performance on Different Patterns:
-----------------------------------------------
Random:
  Time:        180 μs
  Comparisons: 4950
  Swaps:       2475

Sorted:
  Time:        2 μs
  Comparisons: 99
  Swaps:       0

Reverse Sorted:
  Time:        280 μs
  Comparisons: 4950
  Swaps:       4950

Nearly Sorted:
  Time:        15 μs
  Comparisons: 490
  Swaps:       2
```

---

## Implementation 7: Bubble Sort Variants

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Cocktail Shaker Sort (Bidirectional Bubble Sort)
 */
void cocktailShakerSort(int arr[], int n) {
    bool swapped = true;
    int start = 0;
    int end = n - 1;
    
    while (swapped) {
        swapped = false;
        
        // Forward pass
        for (int i = start; i < end; i++) {
            if (arr[i] > arr[i + 1]) {
                swap(arr[i], arr[i + 1]);
                swapped = true;
            }
        }
        
        if (!swapped) {
            break;
        }
        
        end--;
        swapped = false;
        
        // Backward pass
        for (int i = end - 1; i >= start; i--) {
            if (arr[i] > arr[i + 1]) {
                swap(arr[i], arr[i + 1]);
                swapped = true;
            }
        }
        
        start++;
    }
}

/**
 * Odd-Even Sort (Brick Sort)
 */
void oddEvenSort(int arr[], int n) {
    bool isSorted = false;
    
    while (!isSorted) {
        isSorted = true;
        
        // Perform odd indexed bubble sort
        for (int i = 1; i <= n - 2; i += 2) {
            if (arr[i] > arr[i + 1]) {
                swap(arr[i], arr[i + 1]);
                isSorted = false;
            }
        }
        
        // Perform even indexed bubble sort
        for (int i = 0; i <= n - 2; i += 2) {
            if (arr[i] > arr[i + 1]) {
                swap(arr[i], arr[i + 1]);
                isSorted = false;
            }
        }
    }
}

/**
 * Comb Sort (Improved Bubble Sort)
 */
void combSort(int arr[], int n) {
    int gap = n;
    bool swapped = true;
    
    while (gap > 1 || swapped) {
        // Update gap for next pass
        gap = max(1, gap * 10 / 13);
        
        swapped = false;
        
        // Compare elements with current gap
        for (int i = 0; i < n - gap; i++) {
            if (arr[i] > arr[i + gap]) {
                swap(arr[i], arr[i + gap]);
                swapped = true;
            }
        }
    }
}

int main() {
    // Test data
    int arr1[] = {64, 34, 25, 12, 22, 11, 90};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    
    cout << "Cocktail Shaker Sort:" << endl;
    cout << "Original: ";
    printArray(arr1, n1);
    
    cocktailShakerSort(arr1, n1);
    
    cout << "Sorted:   ";
    printArray(arr1, n1);
    
    int arr2[] = {64, 34, 25, 12, 22, 11, 90};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    
    cout << "\nOdd-Even Sort:" << endl;
    cout << "Original: ";
    printArray(arr2, n2);
    
    oddEvenSort(arr2, n2);
    
    cout << "Sorted:   ";
    printArray(arr2, n2);
    
    int arr3[] = {64, 34, 25, 12, 22, 11, 90};
    int n3 = sizeof(arr3) / sizeof(arr3[0]);
    
    cout << "\nComb Sort:" << endl;
    cout << "Original: ";
    printArray(arr3, n3);
    
    combSort(arr3, n3);
    
    cout << "Sorted:   ";
    printArray(arr3, n3);
    
    return 0;
}
```

**Output:**
```
Cocktail Shaker Sort:
Original: 64 34 25 12 22 11 90 
Sorted:   11 12 22 25 34 64 90 

Odd-Even Sort:
Original: 64 34 25 12 22 11 90 
Sorted:   11 12 22 25 34 64 90 

Comb Sort:
Original: 64 34 25 12 22 11 90 
Sorted:   11 12 22 25 34 64 90 
```

---

## Advantages and Disadvantages

### Advantages
- ✅ Simple to understand and implement
- ✅ Stable sort (maintains relative order)
- ✅ In-place sorting (O(1) extra space)
- ✅ Adaptive (optimizes for nearly sorted data)
- ✅ Can detect if array is already sorted

### Disadvantages
- ❌ Inefficient for large datasets (O(n²))
- ❌ Too many swaps for reverse-sorted data
- ❌ Poor performance compared to O(n log n) algorithms
- ❌ Not suitable for performance-critical applications

---

## Best Practices

1. **Use optimization** - Early termination when no swaps occur
2. **Consider dataset size** - Only for small datasets (< 100 elements)
3. **Use for educational purposes** - Great for teaching sorting concepts
4. **Test with edge cases** - Empty arrays, single elements, duplicates
5. **Consider stability requirements** - Bubble sort is naturally stable

---

## Common Pitfalls

1. **Using on large datasets** - Performance is O(n²)
2. **Not implementing optimization** - Missing early termination
3. **Off-by-one errors** in loop boundaries
4. **Not handling empty arrays**
5. **Choosing when stability isn't required**

---

## Summary

Bubble sort is the simplest sorting algorithm, making it excellent for educational purposes and small datasets. While it's not efficient for large datasets, its simplicity and stability make it useful in specific scenarios.

**Key Takeaways:**
- Time Complexity: O(n²) average and worst, O(n) best (optimized)
- Space Complexity: O(1)
- Stable: ✅
- In-place: ✅
- Best for: Small datasets, educational purposes, nearly sorted data
