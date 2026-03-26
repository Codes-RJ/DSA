# Merge Sort in C++

## Overview
Merge sort is a divide-and-conquer algorithm that divides the array into halves, recursively sorts them, and then merges the sorted halves. It's known for its stability and guaranteed O(n log n) performance.

## Theory

### Definition
Merge sort recursively divides the array into two halves, sorts each half, and then merges the sorted halves back together.

### Algorithm Steps
1. Divide the array into two halves
2. Recursively sort the left half
3. Recursively sort the right half
4. Merge the two sorted halves

### Complexity Analysis
- **Time Complexity**: O(n log n) - All cases
- **Space Complexity**: O(n) - For temporary arrays
- **Stability**: ✅ Stable - Maintains relative order of equal elements

### When to Use
- When stability is required
- When worst-case performance guarantee is needed
- For external sorting (data doesn't fit in memory)
- For linked lists (efficient O(1) space with linked lists)

---

## Implementation 1: Basic Merge Sort

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
 * Print array helper function
 */
void printArray(const int arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "Original array: ";
    printArray(arr, n);
    
    mergeSort(arr, 0, n - 1);
    
    cout << "Sorted array:   ";
    printArray(arr, n);
    
    return 0;
}
```

**Output:**
```
Original array: 12 11 13 5 6 7 
Sorted array:   5 6 7 11 12 13 
```

---

## Implementation 2: In-Place Merge Sort

```cpp
#include <iostream>
#include <vector>
using namespace std;

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

/**
 * In-place merge sort
 */
void mergeSortInPlace(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        
        mergeSortInPlace(arr, left, mid);
        mergeSortInPlace(arr, mid + 1, right);
        mergeInPlace(arr, left, mid, right);
    }
}

/**
 * Merge with gap method (Shell sort like)
 */
int nextGap(int gap) {
    if (gap <= 1) {
        return 0;
    }
    return (gap / 2) + (gap % 2);
}

void mergeInPlaceGap(int arr[], int n, int start1, int start2) {
    int i = start1, j = start2;
    int gap = nextGap(n);
    
    for (gap = nextGap(n); gap > 0; gap = nextGap(gap)) {
        // Compare elements in first part
        for (i = start1; i + gap < start2; i++) {
            if (arr[i] > arr[i + gap]) {
                swap(arr[i], arr[i + gap]);
            }
        }
        
        // Compare elements between first and second part
        for (j = gap > start2 - i ? gap : start2 - i; 
             i < start2 && j < start2 + (n - (start2 - start1)); 
             i++, j++) {
            if (arr[i] > arr[j]) {
                swap(arr[i], arr[j]);
            }
        }
        
        // Compare elements in second part
        if (j < start2 + (n - (start2 - start1))) {
            for (j = start2; j + gap < start2 + (n - (start2 - start1)); j++) {
                if (arr[j] > arr[j + gap]) {
                    swap(arr[j], arr[j + gap]);
                }
            }
        }
    }
}

int main() {
    int arr1[] = {12, 11, 13, 5, 6, 7};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    
    cout << "In-Place Merge Sort:" << endl;
    cout << "Original: ";
    printArray(arr1, n1);
    
    mergeSortInPlace(arr1, 0, n1 - 1);
    
    cout << "Sorted:   ";
    printArray(arr1, n1);
    
    return 0;
}
```

**Output:**
```
In-Place Merge Sort:
Original: 12 11 13 5 6 7 
Sorted:   5 6 7 11 12 13 
```

---

## Implementation 3: Merge Sort with Templates

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

/**
 * Generic merge function using templates
 */
template<typename T>
void mergeTemplate(T arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    
    // Create temporary arrays
    T* L = new T[n1];
    T* R = new T[n2];
    
    // Copy data
    for (int i = 0; i < n1; i++) {
        L[i] = arr[left + i];
    }
    for (int j = 0; j < n2; j++) {
        R[j] = arr[mid + 1 + j];
    }
    
    // Merge
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
    
    // Copy remaining
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
 * Generic merge sort
 */
template<typename T>
void mergeSortTemplate(T arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        
        mergeSortTemplate(arr, left, mid);
        mergeSortTemplate(arr, mid + 1, right);
        mergeTemplate(arr, left, mid, right);
    }
}

/**
 * Merge sort with custom comparator
 */
template<typename T, typename Compare>
void mergeCustom(T arr[], int left, int mid, int right, Compare comp) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    
    T* L = new T[n1];
    T* R = new T[n2];
    
    for (int i = 0; i < n1; i++) {
        L[i] = arr[left + i];
    }
    for (int j = 0; j < n2; j++) {
        R[j] = arr[mid + 1 + j];
    }
    
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (comp(L[i], R[j])) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    
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

template<typename T, typename Compare>
void mergeSortCustom(T arr[], int left, int right, Compare comp) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        
        mergeSortCustom(arr, left, mid, comp);
        mergeSortCustom(arr, mid + 1, right, comp);
        mergeCustom(arr, left, mid, right, comp);
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

int main() {
    // Integer array
    int intArr[] = {12, 11, 13, 5, 6, 7};
    int intSize = sizeof(intArr) / sizeof(intArr[0]);
    
    cout << "Integer array:" << endl;
    cout << "Original: ";
    printArrayTemplate(intArr, intSize);
    
    mergeSortTemplate(intArr, 0, intSize - 1);
    
    cout << "Sorted:   ";
    printArrayTemplate(intArr, intSize);
    
    // Double array
    double doubleArr[] = {3.14, 1.41, 2.71, 1.73, 2.23};
    int doubleSize = sizeof(doubleArr) / sizeof(doubleArr[0]);
    
    cout << "\nDouble array:" << endl;
    cout << "Original: ";
    printArrayTemplate(doubleArr, doubleSize);
    
    mergeSortTemplate(doubleArr, 0, doubleSize - 1);
    
    cout << "Sorted:   ";
    printArrayTemplate(doubleArr, doubleSize);
    
    // String array
    string strArr[] = {"banana", "apple", "cherry", "date"};
    int strSize = sizeof(strArr) / sizeof(strArr[0]);
    
    cout << "\nString array:" << endl;
    cout << "Original: ";
    printArrayTemplate(strArr, strSize);
    
    mergeSortTemplate(strArr, 0, strSize - 1);
    
    cout << "Sorted:   ";
    printArrayTemplate(strArr, strSize);
    
    // Custom comparator (descending order)
    int descArr[] = {12, 11, 13, 5, 6, 7};
    int descSize = sizeof(descArr) / sizeof(descArr[0]);
    
    cout << "\nDescending order:" << endl;
    cout << "Original: ";
    printArrayTemplate(descArr, descSize);
    
    mergeSortCustom(descArr, 0, descSize - 1, [](int a, int b) { return a > b; });
    
    cout << "Sorted:   ";
    printArrayTemplate(descArr, descSize);
    
    return 0;
}
```

**Output:**
```
Integer array:
Original: 12 11 13 5 6 7 
Sorted:   5 6 7 11 12 13 

Double array:
Original: 3.14 1.41 2.71 1.73 2.23 
Sorted:   1.41 1.73 2.23 2.71 3.14 

String array:
Original: banana apple cherry date 
Sorted:   apple banana cherry date 

Descending order:
Original: 12 11 13 5 6 7 
Sorted:   13 12 11 7 6 5 
```

---

## Implementation 4: Merge Sort for Linked Lists

```cpp
#include <iostream>
using namespace std;

/**
 * Node structure for linked list
 */
struct Node {
    int data;
    Node* next;
    
    Node(int val) : data(val), next(nullptr) {}
};

/**
 * Split linked list into two halves
 */
void splitList(Node* source, Node** frontRef, Node** backRef) {
    Node* slow = source;
    Node* fast = source->next;
    
    // Fast moves two steps, slow moves one step
    while (fast != nullptr) {
        fast = fast->next;
        if (fast != nullptr) {
            slow = slow->next;
            fast = fast->next;
        }
    }
    
    // Split at slow pointer
    *frontRef = source;
    *backRef = slow->next;
    slow->next = nullptr;
}

/**
 * Merge two sorted linked lists
 */
Node* sortedMerge(Node* a, Node* b) {
    if (a == nullptr) return b;
    if (b == nullptr) return a;
    
    Node* result = nullptr;
    
    if (a->data <= b->data) {
        result = a;
        result->next = sortedMerge(a->next, b);
    } else {
        result = b;
        result->next = sortedMerge(a, b->next);
    }
    
    return result;
}

/**
 * Merge sort for linked list
 */
void mergeSortLL(Node** headRef) {
    Node* head = *headRef;
    Node* a;
    Node* b;
    
    // Base case: 0 or 1 element
    if (head == nullptr || head->next == nullptr) {
        return;
    }
    
    // Split into two sublists
    splitList(head, &a, &b);
    
    // Recursively sort sublists
    mergeSortLL(&a);
    mergeSortLL(&b);
    
    // Merge sorted sublists
    *headRef = sortedMerge(a, b);
}

/**
 * Insert node at beginning
 */
void push(Node** headRef, int newData) {
    Node* newNode = new Node(newData);
    newNode->next = *headRef;
    *headRef = newNode;
}

/**
 * Print linked list
 */
void printList(Node* node) {
    while (node != nullptr) {
        cout << node->data << " ";
        node = node->next;
    }
    cout << endl;
}

/**
 * Delete linked list
 */
void deleteList(Node** headRef) {
    Node* current = *headRef;
    Node* next;
    
    while (current != nullptr) {
        next = current->next;
        delete current;
        current = next;
    }
    
    *headRef = nullptr;
}

int main() {
    Node* head = nullptr;
    
    // Create linked list
    push(&head, 15);
    push(&head, 10);
    push(&head, 5);
    push(&head, 20);
    push(&head, 3);
    push(&head, 2);
    
    cout << "Linked List before sorting:" << endl;
    printList(head);
    
    mergeSortLL(&head);
    
    cout << "Linked List after sorting:" << endl;
    printList(head);
    
    deleteList(&head);
    
    return 0;
}
```

**Output:**
```
Linked List before sorting:
2 3 20 5 10 15 
Linked List after sorting:
2 3 5 10 15 20 
```

---

## Implementation 5: Bottom-Up Merge Sort (Iterative)

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Iterative merge sort (bottom-up approach)
 */
void mergeSortIterative(int arr[], int n) {
    // For current size of subarrays to be merged, curr_size varies from 1 to n/2
    for (int curr_size = 1; curr_size <= n - 1; curr_size = 2 * curr_size) {
        // For picking starting index of left subarray of range curr_size
        for (int left_start = 0; left_start < n - 1; left_start += 2 * curr_size) {
            // Find ending index of left subarray
            int mid = min(left_start + curr_size - 1, n - 1);
            
            // Find ending index of right subarray
            int right_end = min(left_start + 2 * curr_size - 1, n - 1);
            
            // Merge subarrays arr[left_start...mid] & arr[mid+1...right_end]
            merge(arr, left_start, mid, right_end);
        }
    }
}

/**
 * Bottom-up merge sort with single auxiliary array
 */
void mergeSortBottomUp(int arr[], int n) {
    int* aux = new int[n];
    
    for (int width = 1; width < n; width *= 2) {
        // Copy array to auxiliary
        for (int i = 0; i < n; i++) {
            aux[i] = arr[i];
        }
        
        // Merge adjacent subarrays
        for (int i = 0; i < n; i += 2 * width) {
            int left = i;
            int mid = min(i + width, n);
            int right = min(i + 2 * width, n);
            
            int l = left, r = mid, k = left;
            
            while (l < mid && r < right) {
                if (aux[l] <= aux[r]) {
                    arr[k++] = aux[l++];
                } else {
                    arr[k++] = aux[r++];
                }
            }
            
            while (l < mid) {
                arr[k++] = aux[l++];
            }
            
            while (r < right) {
                arr[k++] = aux[r++];
            }
        }
    }
    
    delete[] aux;
}

/**
 * Natural merge sort (detects already sorted runs)
 */
bool isSorted(int arr[], int start, int end) {
    for (int i = start; i < end; i++) {
        if (arr[i] > arr[i + 1]) {
            return false;
        }
    }
    return true;
}

void naturalMergeSort(int arr[], int n) {
    if (n <= 1) return;
    
    // Find natural runs
    vector<pair<int, int>> runs;
    int start = 0;
    
    while (start < n) {
        int end = start;
        while (end < n - 1 && arr[end] <= arr[end + 1]) {
            end++;
        }
        runs.push_back({start, end});
        start = end + 1;
    }
    
    // Merge runs pairwise
    while (runs.size() > 1) {
        vector<pair<int, int>> newRuns;
        
        for (int i = 0; i < runs.size(); i += 2) {
            if (i + 1 < runs.size()) {
                merge(arr, runs[i].first, runs[i].second, runs[i + 1].second);
                newRuns.push_back({runs[i].first, runs[i + 1].second});
            } else {
                newRuns.push_back(runs[i]);
            }
        }
        
        runs = newRuns;
    }
}

int main() {
    int arr1[] = {12, 11, 13, 5, 6, 7};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    
    cout << "Iterative Merge Sort:" << endl;
    cout << "Original: ";
    printArray(arr1, n1);
    
    mergeSortIterative(arr1, n1);
    
    cout << "Sorted:   ";
    printArray(arr1, n1);
    
    int arr2[] = {12, 11, 13, 5, 6, 7};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    
    cout << "\nBottom-Up Merge Sort:" << endl;
    cout << "Original: ";
    printArray(arr2, n2);
    
    mergeSortBottomUp(arr2, n2);
    
    cout << "Sorted:   ";
    printArray(arr2, n2);
    
    int arr3[] = {1, 2, 3, 2, 1, 4, 5, 6};
    int n3 = sizeof(arr3) / sizeof(arr3[0]);
    
    cout << "\nNatural Merge Sort:" << endl;
    cout << "Original: ";
    printArray(arr3, n3);
    
    naturalMergeSort(arr3, n3);
    
    cout << "Sorted:   ";
    printArray(arr3, n3);
    
    return 0;
}
```

**Output:**
```
Iterative Merge Sort:
Original: 12 11 13 5 6 7 
Sorted:   5 6 7 11 12 13 

Bottom-Up Merge Sort:
Original: 12 11 13 5 6 7 
Sorted:   5 6 7 11 12 13 

Natural Merge Sort:
Original: 1 2 3 2 1 4 5 6 
Sorted:   1 1 2 2 3 4 5 6 
```

---

## Implementation 6: Merge Sort Performance Analysis

```cpp
#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <algorithm>
using namespace std;
using namespace chrono;

/**
 * Merge sort with statistics tracking
 */
struct MergeSortStats {
    int comparisons;
    int merges;
    int recursiveCalls;
    long long timeMicroseconds;
};

MergeSortStats stats;

void mergeWithStats(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    
    int* L = new int[n1];
    int* R = new int[n2];
    
    for (int i = 0; i < n1; i++) {
        L[i] = arr[left + i];
    }
    for (int j = 0; j < n2; j++) {
        R[j] = arr[mid + 1 + j];
    }
    
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        stats.comparisons++;
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    
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
    
    stats.merges++;
    delete[] L;
    delete[] R;
}

void mergeSortWithStats(int arr[], int left, int right) {
    stats.recursiveCalls++;
    
    if (left < right) {
        int mid = left + (right - left) / 2;
        
        mergeSortWithStats(arr, left, mid);
        mergeSortWithStats(arr, mid + 1, right);
        mergeWithStats(arr, left, mid, right);
    }
}

/**
 * Compare merge sort variants
 */
void compareMergeVariants() {
    const int SIZE = 10000;
    vector<int> data(SIZE);
    
    // Generate random data
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 100000);
    
    for (int i = 0; i < SIZE; i++) {
        data[i] = dis(gen);
    }
    
    cout << "Merge Sort Variant Comparison (n = " << SIZE << "):" << endl;
    cout << "--------------------------------------------" << endl;
    
    // Test regular merge sort
    vector<int> test1 = data;
    stats = {0, 0, 0, 0};
    auto start = high_resolution_clock::now();
    mergeSortWithStats(test1.data(), 0, SIZE - 1);
    auto end = high_resolution_clock::now();
    stats.timeMicroseconds = duration_cast<microseconds>(end - start).count();
    
    cout << "Regular Merge Sort:" << endl;
    cout << "  Time:           " << stats.timeMicroseconds << " μs" << endl;
    cout << "  Comparisons:    " << stats.comparisons << endl;
    cout << "  Merges:         " << stats.merges << endl;
    cout << "  Recursive Calls:" << stats.recursiveCalls << endl;
    
    // Test iterative merge sort
    vector<int> test2 = data;
    start = high_resolution_clock::now();
    mergeSortIterative(test2.data(), SIZE);
    end = high_resolution_clock::now();
    auto iterativeTime = duration_cast<microseconds>(end - start).count();
    
    cout << "\nIterative Merge Sort:" << endl;
    cout << "  Time: " << iterativeTime << " μs" << endl;
    
    // Test bottom-up merge sort
    vector<int> test3 = data;
    start = high_resolution_clock::now();
    mergeSortBottomUp(test3.data(), SIZE);
    end = high_resolution_clock::now();
    auto bottomUpTime = duration_cast<microseconds>(end - start).count();
    
    cout << "\nBottom-Up Merge Sort:" << endl;
    cout << "  Time: " << bottomUpTime << " μs" << endl;
}

/**
 * Test stability of merge sort
 */
void testStability() {
    struct Person {
        string name;
        int age;
        int originalIndex;
        
        bool operator<=(const Person& other) const {
            return age <= other.age;
        }
    };
    
    Person people[] = {
        {"Alice", 25, 0},
        {"Bob", 20, 1},
        {"Charlie", 25, 2},
        {"Diana", 20, 3},
        {"Eve", 30, 4}
    };
    
    int n = sizeof(people) / sizeof(people[0]);
    
    cout << "\nStability Test:" << endl;
    cout << "Before sorting:" << endl;
    for (int i = 0; i < n; i++) {
        cout << people[i].name << " (" << people[i].age << ") [" << people[i].originalIndex << "]" << endl;
    }
    
    // Sort by age
    mergeSortTemplate(people, 0, n - 1);
    
    cout << "\nAfter sorting:" << endl;
    for (int i = 0; i < n; i++) {
        cout << people[i].name << " (" << people[i].age << ") [" << people[i].originalIndex << "]" << endl;
    }
    
    // Check stability
    bool stable = true;
    for (int i = 0; i < n - 1; i++) {
        if (people[i].age == people[i + 1].age && 
            people[i].originalIndex > people[i + 1].originalIndex) {
            stable = false;
            break;
        }
    }
    
    cout << "\nStability: " << (stable ? "Stable" : "Not Stable") << endl;
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
    cout << "-----------------------------------------" << endl;
    
    // Test merge sort
    vector<int> mergeData = data;
    auto start = high_resolution_clock::now();
    mergeSort(mergeData.data(), 0, SIZE - 1);
    auto end = high_resolution_clock::now();
    auto mergeTime = duration_cast<microseconds>(end - start).count();
    
    // Test STL sort
    vector<int> stlData = data;
    start = high_resolution_clock::now();
    sort(stlData.begin(), stlData.end());
    end = high_resolution_clock::now();
    auto stlTime = duration_cast<microseconds>(end - start).count();
    
    cout << "Merge Sort: " << mergeTime << " μs" << endl;
    cout << "STL Sort:   " << stlTime << " μs" << endl;
    cout << "Ratio:      " << (double)mergeTime / stlTime << "x" << endl;
    
    // Verify both are sorted
    bool mergeSorted = is_sorted(mergeData.begin(), mergeData.end());
    bool stlSorted = is_sorted(stlData.begin(), stlData.end());
    
    cout << "Merge Sorted: " << (mergeSorted ? "Yes" : "No") << endl;
    cout << "STL Sorted:   " << (stlSorted ? "Yes" : "No") << endl;
}

int main() {
    compareMergeVariants();
    testStability();
    compareWithSTL();
    
    return 0;
}
```

**Sample Output:**
```
Merge Sort Variant Comparison (n = 10000):
--------------------------------------------
Regular Merge Sort:
  Time:           12450 μs
  Comparisons:    120456
  Merges:         9999
  Recursive Calls:19999

Iterative Merge Sort:
  Time: 11200 μs

Bottom-Up Merge Sort:
  Time: 10890 μs

Stability Test:
Before sorting:
Alice (25) [0]
Bob (20) [1]
Charlie (25) [2]
Diana (20) [3]
Eve (30) [4]

After sorting:
Bob (20) [1]
Diana (20) [3]
Alice (25) [0]
Charlie (25) [2]
Eve (30) [4]

Stability: Stable

Comparison with STL Sort (n = 100000):
-----------------------------------------
Merge Sort: 124500 μs
STL Sort:   89200 μs
Ratio:      1.40x
Merge Sorted: Yes
STL Sorted:   Yes
```

---

## Implementation 7: External Merge Sort

```cpp
#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <queue>
using namespace std;

/**
 * External merge sort for large files
 * Simulates sorting data that doesn't fit in memory
 */

const int MEMORY_LIMIT = 1000;  // Simulated memory limit

/**
 * Write array to file
 */
void writeToFile(const vector<int>& data, const string& filename) {
    ofstream file(filename);
    for (int num : data) {
        file << num << " ";
    }
    file.close();
}

/**
 * Read array from file
 */
vector<int> readFromFile(const string& filename) {
    vector<int> data;
    ifstream file(filename);
    int num;
    while (file >> num) {
        data.push_back(num);
    }
    file.close();
    return data;
}

/**
 * Create initial runs
 */
vector<string> createInitialRuns(const string& inputFile, int runSize) {
    vector<string> runFiles;
    vector<int> buffer;
    
    ifstream file(inputFile);
    int num;
    int runCount = 0;
    
    while (file >> num) {
        buffer.push_back(num);
        
        if (buffer.size() >= runSize) {
            // Sort buffer and write to file
            sort(buffer.begin(), buffer.end());
            
            string filename = "run_" + to_string(runCount++) + ".txt";
            writeToFile(buffer, filename);
            runFiles.push_back(filename);
            
            buffer.clear();
        }
    }
    
    // Handle remaining elements
    if (!buffer.empty()) {
        sort(buffer.begin(), buffer.end());
        string filename = "run_" + to_string(runCount++) + ".txt";
        writeToFile(buffer, filename);
        runFiles.push_back(filename);
    }
    
    file.close();
    return runFiles;
}

/**
 * Merge k sorted files
 */
void mergeKFiles(const vector<string>& files, const string& outputFile) {
    struct FileNode {
        int value;
        int fileIndex;
        int elementIndex;
        vector<int> data;
        
        bool operator>(const FileNode& other) const {
            return value > other.value;
        }
    };
    
    priority_queue<FileNode, vector<FileNode>, greater<FileNode>> minHeap;
    
    // Read first element from each file
    for (int i = 0; i < files.size(); i++) {
        vector<int> data = readFromFile(files[i]);
        if (!data.empty()) {
            minHeap.push({data[0], i, 0, data});
        }
    }
    
    ofstream output(outputFile);
    
    while (!minHeap.empty()) {
        FileNode node = minHeap.top();
        minHeap.pop();
        
        output << node.value << " ";
        
        // Push next element from same file
        if (node.elementIndex + 1 < node.data.size()) {
            minHeap.push({
                node.data[node.elementIndex + 1],
                node.fileIndex,
                node.elementIndex + 1,
                node.data
            });
        }
    }
    
    output.close();
}

/**
 * External merge sort main function
 */
void externalMergeSort(const string& inputFile, const string& outputFile) {
    cout << "Starting External Merge Sort..." << endl;
    
    // Create initial runs
    vector<string> runFiles = createInitialRuns(inputFile, MEMORY_LIMIT);
    cout << "Created " << runFiles.size() << " initial runs" << endl;
    
    // Merge all runs
    mergeKFiles(runFiles, outputFile);
    cout << "Merged all runs into " << outputFile << endl;
    
    // Clean up run files (in real implementation)
    for (const string& file : runFiles) {
        // remove(file.c_str());  // Uncomment to actually delete files
    }
}

/**
 * Demonstrate external merge sort
 */
void demonstrateExternalSort() {
    // Create large input file
    const int DATA_SIZE = 5000;
    vector<int> largeData;
    
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 100000);
    
    for (int i = 0; i < DATA_SIZE; i++) {
        largeData.push_back(dis(gen));
    }
    
    writeToFile(largeData, "large_input.txt");
    cout << "Created input file with " << DATA_SIZE << " elements" << endl;
    
    // Perform external sort
    externalMergeSort("large_input.txt", "sorted_output.txt");
    
    // Verify result
    vector<int> sortedData = readFromFile("sorted_output.txt");
    bool isSorted = std::is_sorted(sortedData.begin(), sortedData.end());
    
    cout << "Verification: " << (isSorted ? "Sorted correctly" : "Error in sorting") << endl;
    cout << "Output size: " << sortedData.size() << " elements" << endl;
}

int main() {
    demonstrateExternalSort();
    return 0;
}
```

**Sample Output:**
```
Starting External Merge Sort...
Created input file with 5000 elements
Created 5 initial runs
Merged all runs into sorted_output.txt
Verification: Sorted correctly
Output size: 5000 elements
```

---

## Advantages and Disadvantages

### Advantages
- ✅ Guaranteed O(n log n) performance in all cases
- ✅ Stable sort - maintains relative order
- ✅ Excellent for external sorting
- ✅ Parallelizable
- ✅ Works well with linked lists (O(1) space)
- ✅ Predictable performance

### Disadvantages
- ❌ Requires O(n) additional space for arrays
- ❌ Slower than quick sort on average
- ❌ Not in-place for arrays
- ❌ More complex than simpler sorts
- ❌ Extra memory overhead

---

## Best Practices

1. **Use for stability requirements** - Merge sort is naturally stable
2. **Consider linked lists** - O(1) space with linked lists
3. **Use external sort** for large datasets
4. **Optimize merge function** - Reduce memory allocations
5. **Consider iterative version** to avoid recursion overhead

---

## Common Pitfalls

1. **Memory allocation overhead** in merge function
2. **Not handling edge cases** - empty arrays, single elements
3. **Inefficient copying** of data during merge
4. **Recursion depth** for very large arrays
5. **Not considering cache performance**

---

## Summary

Merge sort is a reliable sorting algorithm with guaranteed O(n log n) performance and stability. While it requires additional space, it's excellent for situations where stability and predictable performance are important.

**Key Takeaways:**
- Time Complexity: O(n log n) all cases
- Space Complexity: O(n) for arrays, O(1) for linked lists
- Stable: ✅
- In-place: ❌ for arrays, ✅ for linked lists
- Best for: External sorting, stability requirements, linked lists
