# Sorting Algorithms in C++

## Overview
This document covers various sorting algorithms implemented in C++, from the fundamental bubble sort to advanced hybrid algorithms. Each algorithm includes theoretical explanations, complexity analysis, and practical implementations with examples.

---

## 1. Bubble Sort

Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.

### Theory

#### Definition
Bubble sort repeatedly compares adjacent elements and swaps them if they're in the wrong order. This process continues until the list is sorted.

#### Algorithm Steps
1. Start from the first element
2. Compare current element with next element
3. If current > next, swap them
4. Move to next element
5. Repeat until no swaps are needed

#### Complexity Analysis
- **Time Complexity (Best Case)**: O(n) - Already sorted
- **Time Complexity (Average Case)**: O(n²)
- **Time Complexity (Worst Case)**: O(n²) - Reverse sorted
- **Space Complexity**: O(1)

### Implementation 1: Basic Bubble Sort

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
 * Print array
 */
void printArray(int arr[], int size) {
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

## 2. Selection Sort

Selection sort divides the input into sorted and unsorted regions, repeatedly selecting the smallest element from the unsorted region and moving it to the sorted region.

### Theory

#### Definition
Selection sort finds the minimum element from the unsorted portion and places it at the beginning of the unsorted portion.

#### Complexity Analysis
- **Time Complexity**: O(n²) - All cases
- **Space Complexity**: O(1)

### Implementation

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Selection sort implementation
 */
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        
        // Find minimum element in unsorted array
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        
        // Swap minimum with first element
        swap(arr[i], arr[minIdx]);
    }
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "Original array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    selectionSort(arr, n);
    
    cout << "Sorted array:   ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    return 0;
}
```

**Output:**
```
Original array: 64 25 12 22 11 
Sorted array:   11 12 22 25 64 
```

---

## 3. Insertion Sort

Insertion sort builds the final sorted array one item at a time, by repeatedly inserting the next element into the already-sorted portion.

### Theory

#### Definition
Insertion sort iterates through the input elements and inserts each element into its correct position in the sorted portion.

#### Complexity Analysis
- **Time Complexity (Best Case)**: O(n) - Already sorted
- **Time Complexity (Average Case)**: O(n²)
- **Time Complexity (Worst Case)**: O(n²) - Reverse sorted
- **Space Complexity**: O(1)

### Implementation

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Insertion sort implementation
 */
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        
        // Move elements greater than key one position ahead
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

/**
 * Insert elements in sorted order
 */
void insertionSortInsert(int arr[], int& n, int element) {
    int i = n - 1;
    
    // Find correct position for new element
    while (i >= 0 && arr[i] > element) {
        arr[i + 1] = arr[i];
        i--;
    }
    
    arr[i + 1] = element;
    n++;
}

int main() {
    int arr[] = {12, 11, 13, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "Original array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    insertionSort(arr, n);
    
    cout << "Sorted array:   ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    // Demonstrate insertion
    int arr2[10] = {10, 20, 30, 40, 50};
    int n2 = 5;
    int newElement = 25;
    
    cout << "\nBefore insertion: ";
    for (int i = 0; i < n2; i++) {
        cout << arr2[i] << " ";
    }
    cout << endl;
    
    insertionSortInsert(arr2, n2, newElement);
    
    cout << "After inserting " << newElement << ": ";
    for (int i = 0; i < n2; i++) {
        cout << arr2[i] << " ";
    }
    cout << endl;
    
    return 0;
}
```

**Output:**
```
Original array: 12 11 13 5 6 
Sorted array:   5 6 11 12 13 

Before insertion: 10 20 30 40 50 
After inserting 25: 10 20 25 30 40 50 
```

---

## 4. Merge Sort

Merge sort is a divide-and-conquer algorithm that divides the array into halves, recursively sorts them, and then merges the sorted halves.

### Theory

#### Definition
Merge sort recursively divides the array into two halves, sorts each half, and then merges the sorted halves.

#### Complexity Analysis
- **Time Complexity**: O(n log n) - All cases
- **Space Complexity**: O(n) - For temporary arrays

### Implementation

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Merge two sorted subarrays
 */
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    
    // Create temporary arrays
    int* L = new int[n1];
    int* R = new int[n2];
    
    // Copy data to temporary arrays
    for (int i = 0; i < n1; i++) {
        L[i] = arr[left + i];
    }
    for (int j = 0; j < n2; j++) {
        R[j] = arr[mid + 1 + j];
    }
    
    // Merge temporary arrays back into arr
    int i = 0, j = 0, k = left;
    
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    
    // Copy remaining elements
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
    
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
    
    delete[] L;
    delete[] R;
}

/**
 * Merge sort implementation
 */
void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        
        // Sort first and second halves
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        
        // Merge sorted halves
        merge(arr, left, mid, right);
    }
}

/**
 * In-place merge (more memory efficient)
 */
void mergeInPlace(int arr[], int left, int mid, int right) {
    int i = left;
    int j = mid + 1;
    
    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) {
            i++;
        } else {
            int value = arr[j];
            int index = j;
            
            // Shift all elements
            while (index > i) {
                arr[index] = arr[index - 1];
                index--;
            }
            
            arr[i] = value;
            
            i++;
            mid++;
            j++;
        }
    }
}

int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "Original array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    mergeSort(arr, 0, n - 1);
    
    cout << "Sorted array:   ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    return 0;
}
```

**Output:**
```
Original array: 12 11 13 5 6 7 
Sorted array:   5 6 7 11 12 13 
```

---

## 5. Quick Sort

Quick sort is a divide-and-conquer algorithm that picks a pivot element and partitions the array around it.

### Theory

#### Definition
Quick sort selects a pivot element and partitions the array such that elements less than pivot come before it, and elements greater come after.

#### Complexity Analysis
- **Time Complexity (Best Case)**: O(n log n) - Balanced partitions
- **Time Complexity (Average Case)**: O(n log n)
- **Time Complexity (Worst Case)**: O(n²) - Unbalanced partitions
- **Space Complexity**: O(log n) - Recursion stack

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <random>
using namespace std;

/**
 * Partition function for quick sort
 */
int partition(int arr[], int low, int high) {
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
 * Quick sort implementation
 */
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

/**
 * Randomized quick sort for better average performance
 */
int partitionRandom(int arr[], int low, int high) {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(low, high);
    
    int random = dis(gen);
    swap(arr[random], arr[high]);
    
    return partition(arr, low, high);
}

void quickSortRandom(int arr[], int low, int high) {
    if (low < high) {
        int pi = partitionRandom(arr, low, high);
        
        quickSortRandom(arr, low, pi - 1);
        quickSortRandom(arr, pi + 1, high);
    }
}

/**
 * Iterative quick sort
 */
void quickSortIterative(int arr[], int low, int high) {
    int stack[high - low + 1];
    int top = -1;
    
    stack[++top] = low;
    stack[++top] = high;
    
    while (top >= 0) {
        high = stack[top--];
        low = stack[top--];
        
        int pi = partition(arr, low, high);
        
        if (pi - 1 > low) {
            stack[++top] = low;
            stack[++top] = pi - 1;
        }
        
        if (pi + 1 < high) {
            stack[++top] = pi + 1;
            stack[++top] = high;
        }
    }
}

int main() {
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "Original array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    quickSort(arr, 0, n - 1);
    
    cout << "Sorted array:   ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    return 0;
}
```

**Output:**
```
Original array: 10 7 8 9 1 5 
Sorted array:   1 5 7 8 9 10 
```

---

## 6. Heap Sort

Heap sort uses a binary heap data structure to sort elements. It first builds a max heap and then repeatedly extracts the maximum element.

### Theory

#### Definition
Heap sort first builds a max heap from the input data, then repeatedly extracts the maximum element and places it at the end of the array.

#### Complexity Analysis
- **Time Complexity**: O(n log n) - All cases
- **Space Complexity**: O(1) - In-place sorting

### Implementation

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Heapify a subtree rooted with node i
 */
void heapify(int arr[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    
    if (left < n && arr[left] > arr[largest]) {
        largest = left;
    }
    
    if (right < n && arr[right] > arr[largest]) {
        largest = right;
    }
    
    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

/**
 * Heap sort implementation
 */
void heapSort(int arr[], int n) {
    // Build max heap
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }
    
    // Extract elements from heap one by one
    for (int i = n - 1; i > 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}

/**
 * Build min heap (for ascending order using min heap)
 */
void minHeapify(int arr[], int n, int i) {
    int smallest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    
    if (left < n && arr[left] < arr[smallest]) {
        smallest = left;
    }
    
    if (right < n && arr[right] < arr[smallest]) {
        smallest = right;
    }
    
    if (smallest != i) {
        swap(arr[i], arr[smallest]);
        minHeapify(arr, n, smallest);
    }
}

int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "Original array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    heapSort(arr, n);
    
    cout << "Sorted array:   ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    return 0;
}
```

**Output:**
```
Original array: 12 11 13 5 6 7 
Sorted array:   5 6 7 11 12 13 
```

---

## 7. Counting Sort

Counting sort is a non-comparison-based sorting algorithm that works by counting the number of occurrences of each distinct element.

### Theory

#### Definition
Counting sort counts the frequency of each element and uses these counts to determine the final sorted order.

#### Complexity Analysis
- **Time Complexity**: O(n + k) where k is the range of input
- **Space Complexity**: O(k)

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/**
 * Counting sort implementation
 */
void countingSort(int arr[], int n) {
    if (n <= 0) return;
    
    // Find range
    int max_val = arr[0];
    int min_val = arr[0];
    
    for (int i = 1; i < n; i++) {
        max_val = max(max_val, arr[i]);
        min_val = min(min_val, arr[i]);
    }
    
    int range = max_val - min_val + 1;
    
    // Create count array
    int* count = new int[range]();
    
    // Store count of each element
    for (int i = 0; i < n; i++) {
        count[arr[i] - min_val]++;
    }
    
    // Modify count array to store positions
    for (int i = 1; i < range; i++) {
        count[i] += count[i - 1];
    }
    
    // Build output array
    int* output = new int[n];
    
    for (int i = n - 1; i >= 0; i--) {
        output[count[arr[i] - min_val] - 1] = arr[i];
        count[arr[i] - min_val]--;
    }
    
    // Copy to original array
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }
    
    delete[] count;
    delete[] output;
}

/**
 * Counting sort for characters
 */
void countingSortString(char arr[], int n) {
    const int RANGE = 256;
    int count[RANGE] = {0};
    char* output = new char[n];
    
    // Store count of each character
    for (int i = 0; i < n; i++) {
        count[(int)arr[i]]++;
    }
    
    // Modify count array
    for (int i = 1; i < RANGE; i++) {
        count[i] += count[i - 1];
    }
    
    // Build output array
    for (int i = n - 1; i >= 0; i--) {
        output[count[(int)arr[i]] - 1] = arr[i];
        count[(int)arr[i]]--;
    }
    
    // Copy to original array
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }
    
    delete[] output;
}

int main() {
    int arr[] = {4, 2, 2, 8, 3, 3, 1};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "Original array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    countingSort(arr, n);
    
    cout << "Sorted array:   ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    // Test with characters
    char str[] = "geeksforgeeks";
    int len = sizeof(str) - 1;  // Exclude null terminator
    
    cout << "\nOriginal string: " << str << endl;
    countingSortString(str, len);
    cout << "Sorted string:   " << str << endl;
    
    return 0;
}
```

**Output:**
```
Original array: 4 2 2 8 3 3 1 
Sorted array:   1 2 2 3 3 4 8 

Original string: geeksforgeeks
Sorted string:   eeeefggkkorss
```

---

## 8. Radix Sort

Radix sort is a non-comparison-based sorting algorithm that sorts integers by processing individual digits.

### Theory

#### Definition
Radix sort sorts numbers digit by digit, starting from the least significant digit to the most significant digit.

#### Complexity Analysis
- **Time Complexity**: O(d × (n + k)) where d is number of digits
- **Space Complexity**: O(n + k)

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/**
 * Get maximum value in array
 */
int getMax(int arr[], int n) {
    int max_val = arr[0];
    for (int i = 1; i < n; i++) {
        max_val = max(max_val, arr[i]);
    }
    return max_val;
}

/**
 * Counting sort for specific digit
 */
void countingSortByDigit(int arr[], int n, int exp) {
    int* output = new int[n];
    int count[10] = {0};
    
    // Store count of occurrences
    for (int i = 0; i < n; i++) {
        count[(arr[i] / exp) % 10]++;
    }
    
    // Change count[i] to contain actual position
    for (int i = 1; i < 10; i++) {
        count[i] += count[i - 1];
    }
    
    // Build output array
    for (int i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }
    
    // Copy to original array
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }
    
    delete[] output;
}

/**
 * Radix sort implementation
 */
void radixSort(int arr[], int n) {
    int max_val = getMax(arr, n);
    
    // Do counting sort for every digit
    for (int exp = 1; max_val / exp > 0; exp *= 10) {
        countingSortByDigit(arr, n, exp);
    }
}

/**
 * Radix sort for strings
 */
int getMaxLength(string arr[], int n) {
    int max_len = arr[0].length();
    for (int i = 1; i < n; i++) {
        max_len = max(max_len, (int)arr[i].length());
    }
    return max_len;
}

void countingSortByChar(string arr[], int n, int pos) {
    const int RANGE = 256;
    string* output = new string[n];
    int count[RANGE] = {0};
    
    // Store count of characters
    for (int i = 0; i < n; i++) {
        if (pos < arr[i].length()) {
            count[(int)arr[i][pos]]++;
        } else {
            count[0]++;  // For strings shorter than current position
        }
    }
    
    // Change count[i] to contain actual position
    for (int i = 1; i < RANGE; i++) {
        count[i] += count[i - 1];
    }
    
    // Build output array
    for (int i = n - 1; i >= 0; i--) {
        char c;
        if (pos < arr[i].length()) {
            c = arr[i][pos];
        } else {
            c = 0;
        }
        
        output[count[c] - 1] = arr[i];
        count[c]--;
    }
    
    // Copy to original array
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }
    
    delete[] output;
}

void radixSortStrings(string arr[], int n) {
    int max_len = getMaxLength(arr, n);
    
    for (int pos = max_len - 1; pos >= 0; pos--) {
        countingSortByChar(arr, n, pos);
    }
}

int main() {
    int arr[] = {170, 45, 75, 90, 802, 24, 2, 66};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "Original array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    radixSort(arr, n);
    
    cout << "Sorted array:   ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    // Test with strings
    string strArr[] = {"apple", "banana", "cherry", "date", "elderberry"};
    int strN = sizeof(strArr) / sizeof(strArr[0]);
    
    cout << "\nOriginal strings:" << endl;
    for (int i = 0; i < strN; i++) {
        cout << strArr[i] << " ";
    }
    cout << endl;
    
    radixSortStrings(strArr, strN);
    
    cout << "Sorted strings:" << endl;
    for (int i = 0; i < strN; i++) {
        cout << strArr[i] << " ";
    }
    cout << endl;
    
    return 0;
}
```

**Output:**
```
Original array: 170 45 75 90 802 24 2 66 
Sorted array:   2 24 45 66 75 90 170 802 

Original strings:
apple banana cherry date elderberry 
Sorted strings:
apple banana cherry date elderberry 
```

---

## 9. Bucket Sort

Bucket sort distributes elements into buckets, sorts each bucket, and then concatenates the buckets.

### Theory

#### Definition
Bucket sort divides the interval into buckets, distributes elements into appropriate buckets, sorts each bucket, and concatenates them.

#### Complexity Analysis
- **Time Complexity (Average)**: O(n + k)
- **Time Complexity (Worst)**: O(n²)
- **Space Complexity**: O(n + k)

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/**
 * Bucket sort implementation
 */
void bucketSort(float arr[], int n) {
    // Create n empty buckets
    vector<float> buckets[n];
    
    // Put array elements in different buckets
    for (int i = 0; i < n; i++) {
        int bucketIndex = n * arr[i];  // Index in bucket
        buckets[bucketIndex].push_back(arr[i]);
    }
    
    // Sort individual buckets
    for (int i = 0; i < n; i++) {
        sort(buckets[i].begin(), buckets[i].end());
    }
    
    // Concatenate all buckets into arr[]
    int index = 0;
    for (int i = 0; i < n; i++) {
        for (float num : buckets[i]) {
            arr[index++] = num;
        }
    }
}

/**
 * Bucket sort for integers with custom range
 */
void bucketSortInt(int arr[], int n, int min_val, int max_val) {
    int range = max_val - min_val + 1;
    int numBuckets = min(range, n);
    
    // Create buckets
    vector<vector<int>> buckets(numBuckets);
    
    // Distribute elements into buckets
    for (int i = 0; i < n; i++) {
        int bucketIndex = ((arr[i] - min_val) * (numBuckets - 1)) / range;
        buckets[bucketIndex].push_back(arr[i]);
    }
    
    // Sort individual buckets
    for (int i = 0; i < numBuckets; i++) {
        sort(buckets[i].begin(), buckets[i].end());
    }
    
    // Concatenate buckets
    int index = 0;
    for (int i = 0; i < numBuckets; i++) {
        for (int num : buckets[i]) {
            arr[index++] = num;
        }
    }
}

int main() {
    float arr[] = {0.897f, 0.565f, 0.656f, 0.1234f, 0.665f, 0.3434f};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "Original array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    bucketSort(arr, n);
    
    cout << "Sorted array:   ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    // Test with integers
    int intArr[] = {29, 25, 3, 49, 37, 13, 33, 44, 12, 8, 9};
    int intN = sizeof(intArr) / sizeof(intArr[0]);
    
    cout << "\nOriginal integer array: ";
    for (int i = 0; i < intN; i++) {
        cout << intArr[i] << " ";
    }
    cout << endl;
    
    bucketSortInt(intArr, intN, 0, 50);
    
    cout << "Sorted integer array:   ";
    for (int i = 0; i < intN; i++) {
        cout << intArr[i] << " ";
    }
    cout << endl;
    
    return 0;
}
```

**Output:**
```
Original array: 0.897 0.565 0.656 0.1234 0.665 0.3434 
Sorted array:   0.1234 0.3434 0.565 0.656 0.665 0.897 

Original integer array: 29 25 3 49 37 13 33 44 12 8 9 
Sorted integer array:   3 8 9 12 13 25 29 33 37 44 49 
```

---

## 10. Shell Sort

Shell sort is an optimization of insertion sort that allows the exchange of items far apart.

### Theory

#### Definition
Shell sort sorts elements at a specific gap, gradually reducing the gap until it becomes 1 (regular insertion sort).

#### Complexity Analysis
- **Time Complexity**: Depends on gap sequence (average O(n^1.3))
- **Space Complexity**: O(1)

### Implementation

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Shell sort implementation
 */
void shellSort(int arr[], int n) {
    // Start with a big gap, then reduce the gap
    for (int gap = n / 2; gap > 0; gap /= 2) {
        // Perform a gapped insertion sort
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
 * Shell sort with different gap sequences
 */
void shellSortKnuth(int arr[], int n) {
    // Knuth sequence: 1, 4, 13, 40, 121, ...
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
        
        gap /= 3;
    }
}

/**
 * Shell sort with Sedgewick sequence
 */
void shellSortSedgewick(int arr[], int n) {
    // Generate Sedgewick sequence
    vector<int> gaps;
    int k = 0;
    
    while (true) {
        int gap;
        if (k % 2 == 0) {
            gap = 9 * (pow(2, k) - pow(2, k/2)) + 1;
        } else {
            gap = 8 * pow(2, k) - 6 * pow(2, (k + 1)/2) + 1;
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

int main() {
    int arr[] = {23, 12, 1, 8, 34, 54, 2, 3};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "Original array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    shellSort(arr, n);
    
    cout << "Sorted array:   ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    return 0;
}
```

**Output:**
```
Original array: 23 12 1 8 34 54 2 3 
Sorted array:   1 2 3 8 12 23 34 54 
```

---

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

---

## Choosing the Right Sorting Algorithm

### Decision Guide

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
   - **Small (< 50)**: Insertion Sort, Selection Sort
   - **Medium (50-1000)**: Shell Sort, Quick Sort
   - **Large (> 1000)**: Merge Sort, Quick Sort, Heap Sort

---

## Performance Comparison

```cpp
#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <algorithm>
using namespace std;
using namespace chrono;

/**
 * Performance comparison of sorting algorithms
 */
void compareSortingAlgorithms() {
    const int SIZE = 10000;
    vector<int> data(SIZE);
    
    // Generate random data
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 100000);
    
    for (int i = 0; i < SIZE; i++) {
        data[i] = dis(gen);
    }
    
    vector<int> testArrays[] = {data, data, data, data, data};
    string names[] = {"STL Sort", "Quick Sort", "Merge Sort", "Heap Sort", "Shell Sort"};
    
    // Test STL sort
    auto start = high_resolution_clock::now();
    sort(testArrays[0].begin(), testArrays[0].end());
    auto end = high_resolution_clock::now();
    auto stlTime = duration_cast<microseconds>(end - start).count();
    
    // Test other algorithms (implementations would go here)
    // For brevity, showing only STL sort timing
    
    cout << "Sorting Algorithm Performance Comparison" << endl;
    cout << "Dataset size: " << SIZE << " elements" << endl;
    cout << "----------------------------------------" << endl;
    cout << "STL Sort:      " << stlTime << " microseconds" << endl;
    
    // Verify sorted
    bool isSorted = is_sorted(testArrays[0].begin(), testArrays[0].end());
    cout << "Verification:   " << (isSorted ? "Sorted correctly" : "Error in sorting") << endl;
}

int main() {
    compareSortingAlgorithms();
    return 0;
}
```

---

## Best Practices

1. **Use STL algorithms** - `std::sort`, `std::stable_sort`, `std::partial_sort`
2. **Consider data characteristics** - Size, distribution, type
3. **Profile before optimizing** - Measure actual performance
4. **Handle edge cases** - Empty arrays, single elements, duplicates
5. **Choose appropriate algorithm** - Based on requirements

---

## Common Pitfalls

1. **Using wrong algorithm for data size**
2. **Not handling stability requirements**
3. **Ignoring space complexity constraints**
4. **Not testing with edge cases**
5. **Choosing based on best-case instead of average-case**

---

## Summary

Sorting algorithms are fundamental to computer science. The choice of algorithm depends on various factors including data size, stability requirements, memory constraints, and data distribution.

**Key Takeaways:**
- No single algorithm is best for all cases
- Consider trade-offs between time, space, and stability
- Use STL algorithms for production code
- Understand the characteristics of your data
- Profile and measure actual performance
