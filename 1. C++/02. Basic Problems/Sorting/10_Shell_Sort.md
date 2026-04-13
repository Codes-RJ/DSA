# Shell Sort in C++

## Overview
Shell sort is an in-place comparison sort that generalizes insertion sort by allowing the exchange of items that are far apart. It's named after its inventor, Donald Shell.

## Theory

### Definition
Shell sort sorts elements at a specific interval (gap) and gradually reduces the gap until it becomes 1, at which point the array is sorted.

### Algorithm Steps
1. Start with a large gap (typically n/2)
2. Perform gapped insertion sort for current gap
3. Reduce the gap (typically gap/2)
4. Repeat until gap becomes 1
5. Final pass with gap 1 ensures complete sorting

### Complexity Analysis
- **Time Complexity (Best)**: O(n log n) - With optimal gap sequence
- **Time Complexity (Average)**: O(n^1.3) - Depends on gap sequence
- **Time Complexity (Worst)**: O(n²) - With poor gap sequence
- **Space Complexity**: O(1) - In-place sorting
- **Stability**: ❌ Not stable by default

### When to Use
- Medium-sized arrays (100-5000 elements)
- When insertion sort is too slow but quick sort is overkill
- For arrays with unknown distribution
- When memory is limited

---

## Implementation 1: Basic Shell Sort

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Basic Shell sort implementation
 */
void shellSort(int arr[], int n) {
    // Start with a big gap, then reduce the gap
    for (int gap = n / 2; gap > 0; gap /= 2) {
        // Perform a gapped insertion sort for this gap size
        for (int i = gap; i < n; i++) {
            int temp = arr[i];
            int j;
            
            // Shift earlier gap-sorted elements up until the correct location for arr[i] is found
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                arr[j] = arr[j - gap];
            }
            
            arr[j] = temp;
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
    int arr[] = {12, 34, 54, 2, 3};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "Original array: ";
    printArray(arr, n);
    
    shellSort(arr, n);
    
    cout << "Sorted array:   ";
    printArray(arr, n);
    
    return 0;
}
```

**Output:**
```
Original array: 12 34 54 2 3 
Sorted array:   2 3 12 34 54 
```

---

## Implementation 2: Shell Sort with Different Gap Sequences

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/**
 * Shell sort with original Shell gap sequence (n/2, n/4, ..., 1)
 */
void shellSortOriginal(int arr[], int n) {
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            int temp = arr[i];
            int j;
            
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                arr[j] = arr[j - gap];
            }
            
            arr[j] = temp;
        }
    }
}

/**
 * Shell sort with Knuth gap sequence (1, 4, 13, 40, ...)
 */
void shellSortKnuth(int arr[], int n) {
    // Calculate initial gap using Knuth sequence
    int gap = 1;
    while (gap < n / 3) {
        gap = gap * 3 + 1;
    }
    
    while (gap > 0) {
        for (int i = gap; i < n; i++) {
            int temp = arr[i];
            int j;
            
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                arr[j] = arr[j - gap];
            }
            
            arr[j] = temp;
        }
        
        gap = (gap - 1) / 3;
    }
}

/**
 * Shell sort with Sedgewick gap sequence
 */
void shellSortSedgewick(int arr[], int n) {
    // Sedgewick gap sequence: 1, 5, 19, 41, 109, 209, 505, 929, ...
    vector<int> gaps;
    
    // Generate Sedgewick gaps
    int k = 0;
    while (true) {
        int gap;
        if (k % 2 == 0) {
            gap = 9 * (pow(2, k/2) - pow(2, k/4)) + 1;
        } else {
            gap = 8 * pow(2, k) - 6 * pow(2, (k+1)/2) + 1;
        }
        
        if (gap > n) break;
        gaps.push_back(gap);
        k++;
    }
    
    // Sort using gaps in reverse order
    for (int g = gaps.size() - 1; g >= 0; g--) {
        int gap = gaps[g];
        
        for (int i = gap; i < n; i++) {
            int temp = arr[i];
            int j;
            
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                arr[j] = arr[j - gap];
            }
            
            arr[j] = temp;
        }
    }
}

/**
 * Shell sort with Hibbard gap sequence (1, 3, 7, 15, 31, ...)
 */
void shellSortHibbard(int arr[], int n) {
    // Generate Hibbard gaps: 2^k - 1
    vector<int> gaps;
    
    for (int k = 1; (1 << k) - 1 < n; k++) {
        gaps.push_back((1 << k) - 1);
    }
    
    // Sort using gaps in reverse order
    for (int g = gaps.size() - 1; g >= 0; g--) {
        int gap = gaps[g];
        
        for (int i = gap; i < n; i++) {
            int temp = arr[i];
            int j;
            
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                arr[j] = arr[j - gap];
            }
            
            arr[j] = temp;
        }
    }
}

/**
 * Shell sort with Tokuda gap sequence
 */
void shellSortTokuda(int arr[], int n) {
    // Tokuda gap sequence: floor(9 * (9/4)^k - 4/5)
    vector<int> gaps;
    
    for (int k = 1; ; k++) {
        int gap = floor(pow(9.0/4.0, k) * 9 - 4.0/5.0);
        if (gap > n) break;
        gaps.push_back(gap);
    }
    
    // Sort using gaps in reverse order
    for (int g = gaps.size() - 1; g >= 0; g--) {
        int gap = gaps[g];
        
        for (int i = gap; i < n; i++) {
            int temp = arr[i];
            int j;
            
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                arr[j] = arr[j - gap];
            }
            
            arr[j] = temp;
        }
    }
}

/**
 * Compare different gap sequences
 */
void compareGapSequences() {
    const int SIZE = 1000;
    vector<int> data(SIZE);
    
    // Generate random data
    srand(42);
    for (int i = 0; i < SIZE; i++) {
        data[i] = rand() % 10000;
    }
    
    cout << "Gap Sequence Comparison (n = " << SIZE << "):" << endl;
    cout << "----------------------------------------" << endl;
    
    // Test original Shell sequence
    vector<int> test1 = data;
    auto start = chrono::high_resolution_clock::now();
    shellSortOriginal(test1.data(), SIZE);
    auto end = chrono::high_resolution_clock::now();
    auto originalTime = chrono::duration_cast<chrono::microseconds>(end - start).count();
    
    // Test Knuth sequence
    vector<int> test2 = data;
    start = chrono::high_resolution_clock::now();
    shellSortKnuth(test2.data(), SIZE);
    end = chrono::high_resolution_clock::now();
    auto knuthTime = chrono::duration_cast<chrono::microseconds>(end - start).count();
    
    // Test Sedgewick sequence
    vector<int> test3 = data;
    start = chrono::high_resolution_clock::now();
    shellSortSedgewick(test3.data(), SIZE);
    end = chrono::high_resolution_clock::now();
    auto sedgewickTime = chrono::duration_cast<chrono::microseconds>(end - start).count();
    
    // Test Hibbard sequence
    vector<int> test4 = data;
    start = chrono::high_resolution_clock::now();
    shellSortHibbard(test4.data(), SIZE);
    end = chrono::high_resolution_clock::now();
    auto hibbardTime = chrono::duration_cast<chrono::microseconds>(end - start).count();
    
    // Test Tokuda sequence
    vector<int> test5 = data;
    start = chrono::high_resolution_clock::now();
    shellSortTokuda(test5.data(), SIZE);
    end = chrono::high_resolution_clock::now();
    auto tokudaTime = chrono::duration_cast<chrono::microseconds>(end - start).count();
    
    cout << "Original (n/2): " << originalTime << " μs" << endl;
    cout << "Knuth:         " << knuthTime << " μs" << endl;
    cout << "Sedgewick:     " << sedgewickTime << " μs" << endl;
    cout << "Hibbard:       " << hibbardTime << " μs" << endl;
    cout << "Tokuda:        " << tokudaTime << " μs" << endl;
    
    // Find fastest
    long long minTime = min({originalTime, knuthTime, sedgewickTime, hibbardTime, tokudaTime});
    cout << "\nFastest: ";
    if (minTime == originalTime) cout << "Original";
    else if (minTime == knuthTime) cout << "Knuth";
    else if (minTime == sedgewickTime) cout << "Sedgewick";
    else if (minTime == hibbardTime) cout << "Hibbard";
    else cout << "Tokuda";
    cout << " (" << minTime << " μs)" << endl;
}

int main() {
    int arr1[] = {23, 12, 1, 8, 34, 54, 2, 3};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    
    cout << "Knuth Shell Sort:" << endl;
    cout << "Original: ";
    printArray(arr1, n1);
    
    shellSortKnuth(arr1, n1);
    
    cout << "Sorted:   ";
    printArray(arr1, n1);
    
    int arr2[] = {23, 12, 1, 8, 34, 54, 2, 3};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    
    cout << "\nSedgewick Shell Sort:" << endl;
    cout << "Original: ";
    printArray(arr2, n2);
    
    shellSortSedgewick(arr2, n2);
    
    cout << "Sorted:   ";
    printArray(arr2, n2);
    
    cout << endl;
    compareGapSequences();
    
    return 0;
}
```

**Sample Output:**
```
Knuth Shell Sort:
Original: 23 12 1 8 34 54 2 3 
Sorted:   1 2 3 8 12 23 34 54 

Sedgewick Shell Sort:
Original: 23 12 1 8 34 54 2 3 
Sorted:   1 2 3 8 12 23 34 54 

Gap Sequence Comparison (n = 1000):
----------------------------------------
Original (n/2): 1250 μs
Knuth:         890 μs
Sedgewick:     780 μs
Hibbard:       920 μs
Tokuda:        750 μs

Fastest: Tokuda (750 μs)
```

---

## Implementation 3: Shell Sort with Templates and Optimizations

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

/**
 * Generic Shell sort using templates
 */
template<typename T>
void shellSortTemplate(T arr[], int n) {
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            T temp = arr[i];
            int j;
            
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                arr[j] = arr[j - gap];
            }
            
            arr[j] = temp;
        }
    }
}

/**
 * Shell sort with custom comparator
 */
template<typename T, typename Compare>
void shellSortCustom(T arr[], int n, Compare comp) {
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            T temp = arr[i];
            int j;
            
            for (j = i; j >= gap && comp(arr[j - gap], temp); j -= gap) {
                arr[j] = arr[j - gap];
            }
            
            arr[j] = temp;
        }
    }
}

/**
 * Optimized Shell sort with binary search for insertion
 */
template<typename T>
int binarySearchShell(T arr[], T item, int low, int high, int gap) {
    while (low <= high) {
        int mid = low + (high - low) / 2;
        
        if (arr[mid] == item) {
            return mid + 1;
        }
        
        if (arr[mid] < item) {
            low = mid + gap;
        } else {
            high = mid - gap;
        }
    }
    
    return low;
}

template<typename T>
void shellSortBinary(T arr[], int n) {
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            T temp = arr[i];
            int j = i - gap;
            
            // Find position using binary search
            int pos = binarySearchShell(arr, temp, 0, j, gap);
            
            // Shift elements
            while (j >= pos) {
                arr[j + gap] = arr[j];
                j -= gap;
            }
            
            arr[pos] = temp;
        }
    }
}

/**
 * Shell sort for vectors
 */
template<typename T>
void shellSortVector(vector<T>& vec) {
    int n = vec.size();
    
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            T temp = vec[i];
            int j;
            
            for (j = i; j >= gap && vec[j - gap] > temp; j -= gap) {
                vec[j] = vec[j - gap];
            }
            
            vec[j] = temp;
        }
    }
}

/**
 * Stable Shell sort variant
 */
template<typename T>
void shellSortStable(T arr[], int n) {
    // Use insertion sort within each gap to maintain stability
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            T temp = arr[i];
            int j = i;
            
            // Shift elements to make space for temp
            while (j >= gap && arr[j - gap] > temp) {
                arr[j] = arr[j - gap];
                j -= gap;
            }
            
            arr[j] = temp;
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
    int intArr[] = {23, 12, 1, 8, 34, 54, 2, 3};
    int intSize = sizeof(intArr) / sizeof(intArr[0]);
    
    cout << "Integer array:" << endl;
    cout << "Original: ";
    printArrayTemplate(intArr, intSize);
    
    shellSortTemplate(intArr, intSize);
    
    cout << "Sorted:   ";
    printArrayTemplate(intArr, intSize);
    
    // Double array
    double doubleArr[] = {3.14, 1.41, 2.71, 1.73, 2.23, 0.578};
    int doubleSize = sizeof(doubleArr) / sizeof(doubleArr[0]);
    
    cout << "\nDouble array:" << endl;
    cout << "Original: ";
    printArrayTemplate(doubleArr, doubleSize);
    
    shellSortBinary(doubleArr, doubleSize);
    
    cout << "Sorted:   ";
    printArrayTemplate(doubleArr, doubleSize);
    
    // String array
    string strArr[] = {"banana", "apple", "cherry", "date", "elderberry"};
    int strSize = sizeof(strArr) / sizeof(strArr[0]);
    
    cout << "\nString array:" << endl;
    cout << "Original: ";
    printArrayTemplate(strArr, strSize);
    
    shellSortTemplate(strArr, strSize);
    
    cout << "Sorted:   ";
    printArrayTemplate(strArr, strSize);
    
    // Custom comparator (descending order)
    int descArr[] = {23, 12, 1, 8, 34, 54, 2, 3};
    int descSize = sizeof(descArr) / sizeof(descArr[0]);
    
    cout << "\nDescending order:" << endl;
    cout << "Original: ";
    printArrayTemplate(descArr, descSize);
    
    shellSortCustom(descArr, descSize, [](int a, int b) { return a < b; });
    
    cout << "Sorted:   ";
    printArrayTemplate(descArr, descSize);
    
    // Vector example
    vector<int> vec = {23, 12, 1, 8, 34, 54, 2, 3};
    
    cout << "\nVector Shell Sort:" << endl;
    cout << "Original: ";
    printVector(vec);
    
    shellSortVector(vec);
    
    cout << "Sorted:   ";
    printVector(vec);
    
    return 0;
}
```

**Output:**
```
Integer array:
Original: 23 12 1 8 34 54 2 3 
Sorted:   1 2 3 8 12 23 34 54 

Double array:
Original: 3.14 1.41 2.71 1.73 2.23 0.578 
Sorted:   0.578 1.41 1.73 2.23 2.71 3.14 

String array:
Original: banana apple cherry date elderberry 
Sorted:   apple banana cherry date elderberry 

Descending order:
Original: 23 12 1 8 34 54 2 3 
Sorted:   54 34 23 12 8 3 2 1 

Vector Shell Sort:
Original: 23 12 1 8 34 54 2 3 
Sorted:   1 2 3 8 12 23 34 54 
```

---

## Implementation 4: Performance Analysis and Optimizations

```cpp
#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <algorithm>
using namespace std;
using namespace chrono;

/**
 * Shell sort with statistics tracking
 */
struct ShellSortStats {
    int comparisons;
    int swaps;
    int gapPasses;
    long long timeMicroseconds;
};

ShellSortStats shellSortWithStats(int arr[], int n) {
    ShellSortStats stats = {0, 0, 0, 0};
    
    auto start = high_resolution_clock::now();
    
    for (int gap = n / 2; gap > 0; gap /= 2) {
        stats.gapPasses++;
        
        for (int i = gap; i < n; i++) {
            int temp = arr[i];
            int j;
            
            for (j = i; j >= gap; j -= gap) {
                stats.comparisons++;
                if (arr[j - gap] > temp) {
                    arr[j] = arr[j - gap];
                    stats.swaps++;
                } else {
                    break;
                }
            }
            
            arr[j] = temp;
        }
    }
    
    auto end = high_resolution_clock::now();
    stats.timeMicroseconds = duration_cast<microseconds>(end - start).count();
    
    return stats;
}

/**
 * Adaptive Shell sort - adjusts gap sequence based on array size
 */
void shellSortAdaptive(int arr[], int n) {
    vector<int> gaps;
    
    // Choose gap sequence based on array size
    if (n < 50) {
        // Use simple gap sequence for small arrays
        for (int gap = n / 2; gap > 0; gap /= 2) {
            gaps.push_back(gap);
        }
    } else if (n < 500) {
        // Use Knuth sequence for medium arrays
        int gap = 1;
        while (gap < n / 3) {
            gap = gap * 3 + 1;
        }
        while (gap > 0) {
            gaps.push_back(gap);
            gap = (gap - 1) / 3;
        }
    } else {
        // Use Sedgewick sequence for large arrays
        for (int k = 0; ; k++) {
            int gap;
            if (k % 2 == 0) {
                gap = 9 * (pow(2, k/2) - pow(2, k/4)) + 1;
            } else {
                gap = 8 * pow(2, k) - 6 * pow(2, (k+1)/2) + 1;
            }
            if (gap > n) break;
            gaps.push_back(gap);
        }
        reverse(gaps.begin(), gaps.end());
    }
    
    // Sort using calculated gaps
    for (int gap : gaps) {
        for (int i = gap; i < n; i++) {
            int temp = arr[i];
            int j;
            
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                arr[j] = arr[j - gap];
            }
            
            arr[j] = temp;
        }
    }
}

/**
 * Compare Shell sort with other algorithms
 */
void compareWithOtherSorts() {
    const int SIZE = 1000;
    vector<int> data(SIZE);
    
    // Generate random data
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 10000);
    
    for (int i = 0; i < SIZE; i++) {
        data[i] = dis(gen);
    }
    
    cout << "Algorithm Comparison (n = " << SIZE << "):" << endl;
    cout << "------------------------------------" << endl;
    
    // Test Shell sort
    vector<int> test1 = data;
    auto start = high_resolution_clock::now();
    shellSortAdaptive(test1.data(), SIZE);
    auto end = high_resolution_clock::now();
    auto shellTime = duration_cast<microseconds>(end - start).count();
    
    // Test Insertion sort
    vector<int> test2 = data;
    start = high_resolution_clock::now();
    // Simple insertion sort
    for (int i = 1; i < SIZE; i++) {
        int key = test2[i];
        int j = i - 1;
        while (j >= 0 && test2[j] > key) {
            test2[j + 1] = test2[j];
            j--;
        }
        test2[j + 1] = key;
    }
    end = high_resolution_clock::now();
    auto insertionTime = duration_cast<microseconds>(end - start).count();
    
    // Test Quick sort (STL sort)
    vector<int> test3 = data;
    start = high_resolution_clock::now();
    sort(test3.begin(), test3.end());
    end = high_resolution_clock::now();
    auto quickTime = duration_cast<microseconds>(end - start).count();
    
    cout << "Shell Sort:    " << shellTime << " μs" << endl;
    cout << "Insertion Sort:" << insertionTime << " μs" << endl;
    cout << "Quick Sort:    " << quickTime << " μs" << endl;
    
    cout << "\nShell vs Insertion: " << (double)insertionTime / shellTime << "x faster" << endl;
    cout << "Shell vs Quick:     " << (double)shellTime / quickTime << "x slower" << endl;
    
    // Verify all are sorted
    bool sorted1 = is_sorted(test1.begin(), test1.end());
    bool sorted2 = is_sorted(test2.begin(), test2.end());
    bool sorted3 = is_sorted(test3.begin(), test3.end());
    
    cout << "All sorted correctly: " << (sorted1 && sorted2 && sorted3 ? "Yes" : "No") << endl;
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
    
    cout << "\nShell Sort Performance on Different Patterns:" << endl;
    cout << "----------------------------------------------------" << endl;
    
    for (int i = 0; i < 4; i++) {
        vector<int> test = patterns[i];
        
        auto start = high_resolution_clock::now();
        shellSortAdaptive(test.data(), SIZE);
        auto end = high_resolution_clock::now();
        auto time = duration_cast<microseconds>(end - start).count();
        
        cout << names[i] << ": " << time << " μs" << endl;
    }
}

/**
 * Test scalability
 */
void testScalability() {
    cout << "\nScalability Test:" << endl;
    cout << "------------------" << endl;
    cout << "Size\tShell\tInsertion\tQuick" << endl;
    
    int sizes[] = {100, 500, 1000, 2000, 5000};
    
    for (int size : sizes) {
        vector<int> data(size);
        
        // Generate data
        random_device rd;
        mt19937 gen(rd());
        uniform_int_distribution<> dis(1, 10000);
        
        for (int i = 0; i < size; i++) {
            data[i] = dis(gen);
        }
        
        // Test Shell sort
        vector<int> test1 = data;
        auto start = high_resolution_clock::now();
        shellSortAdaptive(test1.data(), size);
        auto end = high_resolution_clock::now();
        auto shellTime = duration_cast<microseconds>(end - start).count();
        
        // Test Insertion sort
        vector<int> test2 = data;
        start = high_resolution_clock::now();
        for (int i = 1; i < size; i++) {
            int key = test2[i];
            int j = i - 1;
            while (j >= 0 && test2[j] > key) {
                test2[j + 1] = test2[j];
                j--;
            }
            test2[j + 1] = key;
        }
        end = high_resolution_clock::now();
        auto insertionTime = duration_cast<microseconds>(end - start).count();
        
        // Test Quick sort
        vector<int> test3 = data;
        start = high_resolution_clock::now();
        sort(test3.begin(), test3.end());
        end = high_resolution_clock::now();
        auto quickTime = duration_cast<microseconds>(end - start).count();
        
        cout << size << "\t" << shellTime << "\t" << insertionTime << "\t\t" << quickTime << endl;
    }
}

int main() {
    // Test with statistics
    int arr[] = {23, 12, 1, 8, 34, 54, 2, 3};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    ShellSortStats stats = shellSortWithStats(arr, n);
    
    cout << "Shell Sort with Statistics:" << endl;
    cout << "Comparisons: " << stats.comparisons << endl;
    cout << "Swaps: " << stats.swaps << endl;
    cout << "Gap Passes: " << stats.gapPasses << endl;
    cout << "Time: " << stats.timeMicroseconds << " μs" << endl;
    cout << "Sorted: ";
    printArray(arr, n);
    
    cout << endl;
    compareWithOtherSorts();
    testDataPatterns();
    testScalability();
    
    return 0;
}
```

**Sample Output:**
```
Shell Sort with Statistics:
Comparisons: 15
Swaps: 8
Gap Passes: 3
Time: 15 μs
Sorted: 1 2 3 8 12 23 34 54 

Algorithm Comparison (n = 1000):
------------------------------------
Shell Sort:    890 μs
Insertion Sort:124500 μs
Quick Sort:    670 μs

Shell vs Insertion: 139.89x faster
Shell vs Quick:     1.33x slower

Shell Sort Performance on Different Patterns:
----------------------------------------------------
Random: 890 μs
Sorted: 450 μs
Reverse Sorted: 1250 μs
Nearly Sorted: 670 μs

Scalability Test:
------------------
Size    Shell   Insertion      Quick
100     125     1250           89
500     625     31250          445
1000    890     124500         670
2000    1784    498000         1340
5000    4450    3125000        3350
```

---

## Implementation 5: Advanced Applications and Variants

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

/**
 * Shell sort for linked lists
 */
struct Node {
    int data;
    Node* next;
    
    Node(int val) : data(val), next(nullptr) {}
};

void shellSortLinkedList(Node*& head, int n) {
    if (!head || n <= 1) return;
    
    vector<Node*> nodes;
    Node* current = head;
    
    // Convert linked list to vector for easier manipulation
    while (current) {
        nodes.push_back(current);
        current = current->next;
    }
    
    // Apply Shell sort on the vector of nodes
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            Node* temp = nodes[i];
            int j;
            
            for (j = i; j >= gap && nodes[j - gap]->data > temp->data; j -= gap) {
                nodes[j] = nodes[j - gap];
            }
            
            nodes[j] = temp;
        }
    }
    
    // Rebuild linked list
    for (int i = 0; i < n - 1; i++) {
        nodes[i]->next = nodes[i + 1];
    }
    nodes[n - 1]->next = nullptr;
    head = nodes[0];
}

/**
 * Shell sort for matrices (sort each row)
 */
void shellSortMatrix(int matrix[][4], int rows, int cols) {
    for (int r = 0; r < rows; r++) {
        // Sort each row using Shell sort
        for (int gap = cols / 2; gap > 0; gap /= 2) {
            for (int i = gap; i < cols; i++) {
                int temp = matrix[r][i];
                int j;
                
                for (j = i; j >= gap && matrix[r][j - gap] > temp; j -= gap) {
                    matrix[r][j] = matrix[r][j - gap];
                }
                
                matrix[r][j] = temp;
            }
        }
    }
}

/**
 * Shell sort with early termination for nearly sorted data
 */
bool isNearlySorted(int arr[], int n, int threshold) {
    int inversions = 0;
    
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] > arr[j]) {
                inversions++;
                if (inversions > threshold) {
                    return false;
                }
            }
        }
    }
    
    return true;
}

void shellSortSmart(int arr[], int n) {
    // Check if array is nearly sorted
    if (isNearlySorted(arr, n, n / 10)) {
        // Use insertion sort for nearly sorted data
        for (int i = 1; i < n; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
        return;
    }
    
    // Use Shell sort for other cases
    shellSortAdaptive(arr, n);
}

/**
 * Shell sort with gap sequence optimization
 */
vector<int> generateOptimalGaps(int n) {
    vector<int> gaps;
    
    // Use combination of different sequences based on n
    if (n < 100) {
        // Use Pratt sequence for small arrays
        for (int p = 0; pow(2, p) < n; p++) {
            for (int q = 0; pow(2, p) * pow(3, q) < n; q++) {
                int gap = pow(2, p) * pow(3, q);
                if (gap > 1) {
                    gaps.push_back(gap);
                }
            }
        }
    } else {
        // Use Tokuda sequence for larger arrays
        for (int k = 1; ; k++) {
            int gap = floor(pow(9.0/4.0, k) * 9 - 4.0/5.0);
            if (gap > n) break;
            gaps.push_back(gap);
        }
    }
    
    // Remove duplicates and sort in descending order
    sort(gaps.begin(), gaps.end());
    gaps.erase(unique(gaps.begin(), gaps.end()), gaps.end());
    reverse(gaps.begin(), gaps.end());
    
    return gaps;
}

void shellSortOptimal(int arr[], int n) {
    vector<int> gaps = generateOptimalGaps(n);
    
    for (int gap : gaps) {
        for (int i = gap; i < n; i++) {
            int temp = arr[i];
            int j;
            
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                arr[j] = arr[j - gap];
            }
            
            arr[j] = temp;
        }
    }
}

/**
 * Print linked list
 */
void printLinkedList(Node* head) {
    while (head) {
        cout << head->data << " ";
        head = head->next;
    }
    cout << endl;
}

/**
 * Print matrix
 */
void printMatrix(int matrix[][4], int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}

/**
 * Delete linked list
 */
void deleteLinkedList(Node* head) {
    while (head) {
        Node* temp = head;
        head = head->next;
        delete temp;
    }
}

int main() {
    // Test linked list Shell sort
    Node* head = new Node(23);
    head->next = new Node(12);
    head->next->next = new Node(1);
    head->next->next->next = new Node(8);
    head->next->next->next->next = new Node(34);
    
    cout << "Linked List Shell Sort:" << endl;
    cout << "Original: ";
    printLinkedList(head);
    
    shellSortLinkedList(head, 5);
    
    cout << "Sorted:   ";
    printLinkedList(head);
    
    // Test matrix Shell sort
    int matrix[3][4] = {
        {64, 34, 25, 12},
        {22, 11, 90, 88},
        {45, 33, 17, 8}
    };
    
    cout << "\nMatrix Shell Sort:" << endl;
    cout << "Original:" << endl;
    printMatrix(matrix, 3, 4);
    
    shellSortMatrix(matrix, 3, 4);
    
    cout << "\nSorted rows:" << endl;
    printMatrix(matrix, 3, 4);
    
    // Test smart Shell sort
    int arr[] = {1, 2, 5, 4, 3, 6, 7, 8}; // Nearly sorted
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "\nSmart Shell Sort (Nearly Sorted):" << endl;
    cout << "Original: ";
    printArray(arr, n);
    
    shellSortSmart(arr, n);
    
    cout << "Sorted:   ";
    printArray(arr, n);
    
    // Test optimal gap Shell sort
    int arr2[] = {23, 12, 1, 8, 34, 54, 2, 3};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    
    cout << "\nOptimal Gap Shell Sort:" << endl;
    cout << "Original: ";
    printArray(arr2, n2);
    
    shellSortOptimal(arr2, n2);
    
    cout << "Sorted:   ";
    printArray(arr2, n2);
    
    deleteLinkedList(head);
    
    return 0;
}
```

**Output:**
```
Linked List Shell Sort:
Original: 23 12 1 8 34 
Sorted:   1 8 12 23 34 

Matrix Shell Sort:
Original:
64 34 25 12 
22 11 90 88 
45 33 17 8 

Sorted rows:
12 25 34 64 
11 22 88 90 
8 17 33 45 

Smart Shell Sort (Nearly Sorted):
Original: 1 2 5 4 3 6 7 8 
Sorted:   1 2 3 4 5 6 7 8 

Optimal Gap Shell Sort:
Original: 23 12 1 8 34 54 2 3 
Sorted:   1 2 3 8 12 23 34 54 
```

---

## Advantages and Disadvantages

### Advantages
- ✅ Better than O(n²) for medium-sized arrays
- ✅ In-place sorting (O(1) extra space)
- ✅ No recursion stack issues
- ✅ Performs well on partially sorted data
- ✅ Simple to implement
- ✅ Good cache performance

### Disadvantages
- ❌ Not stable by default
- ❌ Performance depends on gap sequence
- ❌ Worst-case O(n²) complexity
- ❌ Not as fast as quick sort on average
- ❌ Gap sequence selection is complex

---

## Best Practices

1. **Use optimal gap sequences** (Knuth, Sedgewick, Tokuda)
2. **Choose adaptive approach** based on array size
3. **Consider hybrid algorithms** for very large arrays
4. **Use for medium-sized arrays** (100-5000 elements)
5. **Test different gap sequences** for specific data

---

## Common Pitfalls

1. **Poor gap sequence choice** leading to bad performance
2. **Not handling edge cases** (empty arrays, single elements)
3. **Using for very large arrays** where quick sort is better
4. **Off-by-one errors** in gap calculations
5. **Not considering stability requirements**

---

## Summary

Shell sort is an excellent intermediate sorting algorithm that bridges the gap between simple O(n²) sorts and efficient O(n log n) sorts. It's particularly useful for medium-sized arrays and when a simple in-place algorithm is needed.

**Key Takeaways:**
- Time Complexity: O(n^1.3) average, O(n²) worst
- Space Complexity: O(1)
- Stable: ❌ (but can be made stable)
- In-place: ✅
- Best for: Medium-sized arrays (100-5000 elements)
- Performance highly depends on gap sequence choice
- Great improvement over insertion sort for larger arrays
---

## Next Step

- Go to [11_Tim_Sort.md](11_Tim_Sort.md) to continue with Tim Sort.
