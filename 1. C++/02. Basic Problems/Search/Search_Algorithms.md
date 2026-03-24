# Search Algorithms in C++

## Overview
This document covers various search algorithms implemented in C++, from the fundamental linear search to advanced searching techniques. Each algorithm includes theoretical explanations, complexity analysis, and practical implementations with examples.

---

## 1. Linear Search

Linear search is the simplest searching algorithm that sequentially checks each element in a container until a match is found or the entire container has been searched.

### Complexity
- **Time**: O(n) - Worst case
- **Space**: O(1) - No additional space required

### When to Use
- Unsorted data
- Small datasets
- Simple implementation needed

---

## 2. Binary Search

Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing the search interval in half.

### Theory

#### Definition
Binary search compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated, and the search continues on the remaining half.

#### Algorithm Steps
1. Start with the entire sorted array
2. Find the middle element
3. If middle element equals target, return its index
4. If target < middle element, search left half
5. If target > middle element, search right half
6. Repeat until found or array is exhausted

#### Complexity Analysis
- **Time Complexity (Best Case)**: O(1) - when target is the middle element
- **Time Complexity (Average Case)**: O(log n)
- **Time Complexity (Worst Case)**: O(log n)
- **Space Complexity**: O(1) - iterative version, O(log n) - recursive version

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

## 3. Jump Search

Jump search is an algorithm for searching in sorted arrays. It jumps ahead by fixed steps and then performs linear search within the block.

### Theory

#### Definition
Jump search works by jumping ahead by a fixed block size (typically √n) to find the block where the element might be, then performing linear search within that block.

#### Algorithm Steps
1. Calculate optimal block size: √n
2. Jump ahead by block size until current element >= target or end is reached
3. Perform linear search in the previous block
4. Return index if found, -1 otherwise

#### Complexity Analysis
- **Time Complexity**: O(√n) - Optimal block size
- **Space Complexity**: O(1)

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

/**
 * Jump search algorithm
 * Returns index of target if found, -1 otherwise
 */
int jumpSearch(int arr[], int size, int target) {
    int step = sqrt(size);  // Optimal block size
    int prev = 0;
    
    // Jump ahead to find the block
    while (arr[min(step, size) - 1] < target) {
        prev = step;
        step += sqrt(size);
        if (prev >= size) {
            return -1;
        }
    }
    
    // Linear search within the block
    while (arr[prev] < target) {
        prev++;
        if (prev == min(step, size)) {
            return -1;
        }
    }
    
    // Check if element is found
    if (arr[prev] == target) {
        return prev;
    }
    
    return -1;
}

int main() {
    int arr[] = {10, 23, 45, 70, 89, 100, 123, 145, 167, 189};
    int size = sizeof(arr) / sizeof(arr[0]);
    
    // Test cases
    int targets[] = {70, 10, 189, 99};
    
    for (int target : targets) {
        int result = jumpSearch(arr, size, target);
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
Element 189 found at index: 9
Element 99 not found in array
```

---

## 4. Interpolation Search

Interpolation search is an improved variant of binary search for uniformly distributed sorted arrays. It estimates the position of the target value.

### Theory

#### Definition
Interpolation search uses a formula to estimate the position of the search key, making it more efficient than binary search for uniformly distributed data.

#### Formula
```
position = left + ((target - arr[left]) * (right - left)) / (arr[right] - arr[left])
```

#### Complexity Analysis
- **Time Complexity (Best Case)**: O(log log n) - Uniform distribution
- **Time Complexity (Average Case)**: O(log log n)
- **Time Complexity (Worst Case)**: O(n) - Non-uniform distribution
- **Space Complexity**: O(1)

### Implementation

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Interpolation search algorithm
 * Returns index of target if found, -1 otherwise
 */
int interpolationSearch(int arr[], int size, int target) {
    int left = 0;
    int right = size - 1;
    
    while (left <= right && target >= arr[left] && target <= arr[right]) {
        if (left == right) {
            if (arr[left] == target) {
                return left;
            }
            return -1;
        }
        
        // Calculate position using interpolation formula
        int pos = left + ((double)(target - arr[left]) * (right - left)) / 
                          (arr[right] - arr[left]);
        
        // Check bounds
        if (pos < left || pos > right) {
            break;
        }
        
        if (arr[pos] == target) {
            return pos;
        }
        
        if (arr[pos] < target) {
            left = pos + 1;
        } else {
            right = pos - 1;
        }
    }
    
    return -1;
}

int main() {
    // Uniformly distributed array
    int arr[] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    int size = sizeof(arr) / sizeof(arr[0]);
    
    // Test cases
    int targets[] = {70, 10, 100, 55};
    
    cout << "Interpolation Search on Uniform Distribution:" << endl;
    for (int target : targets) {
        int result = interpolationSearch(arr, size, target);
        if (result != -1) {
            cout << "Element " << target << " found at index: " << result << endl;
        } else {
            cout << "Element " << target << " not found in array" << endl;
        }
    }
    
    // Non-uniform distribution test
    int arr2[] = {10, 15, 23, 45, 70, 89, 100, 145, 200, 500};
    int size2 = sizeof(arr2) / sizeof(arr2[0]);
    
    cout << "\nInterpolation Search on Non-Uniform Distribution:" << endl;
    int target = 70;
    int result = interpolationSearch(arr2, size2, target);
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
Interpolation Search on Uniform Distribution:
Element 70 found at index: 6
Element 10 found at index: 0
Element 100 found at index: 9
Element 55 not found in array

Interpolation Search on Non-Uniform Distribution:
Element 70 found at index: 4
```

---

## 5. Exponential Search

Exponential search is useful for unbounded or infinite arrays. It works by finding a range containing the target and then performing binary search.

### Theory

#### Algorithm Steps
1. Start with index 1
2. While index < size and arr[index] <= target, double the index
3. Perform binary search between index/2 and min(index, size-1)

#### Complexity Analysis
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)

### Implementation

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Binary search helper for exponential search
 */
int binarySearchHelper(int arr[], int left, int right, int target) {
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid;
        }
        
        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1;
}

/**
 * Exponential search algorithm
 * Returns index of target if found, -1 otherwise
 */
int exponentialSearch(int arr[], int size, int target) {
    // If first element is the target
    if (arr[0] == target) {
        return 0;
    }
    
    // Find range for binary search
    int i = 1;
    while (i < size && arr[i] <= target) {
        i *= 2;
    }
    
    // Perform binary search in found range
    return binarySearchHelper(arr, i / 2, min(i, size - 1), target);
}

int main() {
    int arr[] = {10, 23, 45, 70, 89, 100, 123, 145, 167, 189};
    int size = sizeof(arr) / sizeof(arr[0]);
    
    // Test cases
    int targets[] = {70, 10, 189, 99};
    
    for (int target : targets) {
        int result = exponentialSearch(arr, size, target);
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
Element 189 found at index: 9
Element 99 not found in array
```

---

## 6. Fibonacci Search

Fibonacci search is similar to binary search but uses Fibonacci numbers to divide the array.

### Theory

#### Algorithm Steps
1. Generate Fibonacci numbers until F(k) >= size
2. Compare target with element at index F(k-2)
3. Adjust range based on comparison
4. Repeat until found or exhausted

#### Complexity Analysis
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)

### Implementation

```cpp
#include <iostream>
using namespace std;

/**
 * Find smallest Fibonacci number >= n
 */
int findFibonacciIndex(int n) {
    int fib1 = 0, fib2 = 1, fib3 = 1;
    
    while (fib3 < n) {
        fib1 = fib2;
        fib2 = fib3;
        fib3 = fib1 + fib2;
    }
    
    return fib3;
}

/**
 * Fibonacci search algorithm
 * Returns index of target if found, -1 otherwise
 */
int fibonacciSearch(int arr[], int size, int target) {
    int fib1 = 0;    // (k-2)th Fibonacci
    int fib2 = 1;    // (k-1)th Fibonacci
    int fib3 = fib1 + fib2;  // kth Fibonacci
    
    // Find smallest Fibonacci >= size
    while (fib3 < size) {
        fib1 = fib2;
        fib2 = fib3;
        fib3 = fib1 + fib2;
    }
    
    int offset = -1;
    
    while (fib3 > 1) {
        int i = min(offset + fib1, size - 1);
        
        if (arr[i] < target) {
            fib3 = fib2;
            fib2 = fib1;
            fib1 = fib3 - fib2;
            offset = i;
        } else if (arr[i] > target) {
            fib3 = fib1;
            fib2 = fib2 - fib1;
            fib1 = fib3 - fib2;
        } else {
            return i;
        }
    }
    
    // Check for last element
    if (fib2 && offset + 1 < size && arr[offset + 1] == target) {
        return offset + 1;
    }
    
    return -1;
}

int main() {
    int arr[] = {10, 23, 45, 70, 89, 100, 123, 145, 167, 189};
    int size = sizeof(arr) / sizeof(arr[0]);
    
    // Test cases
    int targets[] = {70, 10, 189, 99};
    
    for (int target : targets) {
        int result = fibonacciSearch(arr, size, target);
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
Element 189 found at index: 9
Element 99 not found in array
```

---

## 7. Ternary Search

Ternary search divides the array into three parts instead of two, useful for unimodal functions.

### Theory

#### Algorithm Steps
1. Divide array into three parts using two mid points
2. Compare target with both mid points
3. Eliminate two-thirds of the array based on comparisons
4. Repeat until found

#### Complexity Analysis
- **Time Complexity**: O(log₃ n) ≈ O(log n)
- **Space Complexity**: O(1)

### Implementation

```cpp
#include <iostream>
using namespace std;

/**
 * Iterative ternary search
 * Returns index of target if found, -1 otherwise
 */
int ternarySearch(int arr[], int size, int target) {
    int left = 0;
    int right = size - 1;
    
    while (left <= right) {
        int third = (right - left) / 3;
        int mid1 = left + third;
        int mid2 = right - third;
        
        if (arr[mid1] == target) {
            return mid1;
        }
        
        if (arr[mid2] == target) {
            return mid2;
        }
        
        if (target < arr[mid1]) {
            right = mid1 - 1;
        } else if (target > arr[mid2]) {
            left = mid2 + 1;
        } else {
            left = mid1 + 1;
            right = mid2 - 1;
        }
    }
    
    return -1;
}

/**
 * Recursive ternary search
 */
int ternarySearchRecursive(int arr[], int left, int right, int target) {
    if (left > right) {
        return -1;
    }
    
    int third = (right - left) / 3;
    int mid1 = left + third;
    int mid2 = right - third;
    
    if (arr[mid1] == target) {
        return mid1;
    }
    
    if (arr[mid2] == target) {
        return mid2;
    }
    
    if (target < arr[mid1]) {
        return ternarySearchRecursive(arr, left, mid1 - 1, target);
    } else if (target > arr[mid2]) {
        return ternarySearchRecursive(arr, mid2 + 1, right, target);
    } else {
        return ternarySearchRecursive(arr, mid1 + 1, mid2 - 1, target);
    }
}

int main() {
    int arr[] = {10, 23, 45, 70, 89, 100, 123, 145, 167, 189};
    int size = sizeof(arr) / sizeof(arr[0]);
    
    // Test cases
    int targets[] = {70, 10, 189, 99};
    
    cout << "Iterative Ternary Search:" << endl;
    for (int target : targets) {
        int result = ternarySearch(arr, size, target);
        if (result != -1) {
            cout << "Element " << target << " found at index: " << result << endl;
        } else {
            cout << "Element " << target << " not found in array" << endl;
        }
    }
    
    cout << "\nRecursive Ternary Search:" << endl;
    for (int target : targets) {
        int result = ternarySearchRecursive(arr, 0, size - 1, target);
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
Iterative Ternary Search:
Element 70 found at index: 3
Element 10 found at index: 0
Element 189 found at index: 9
Element 99 not found in array

Recursive Ternary Search:
Element 70 found at index: 3
Element 10 found at index: 0
Element 189 found at index: 9
Element 99 not found in array
```

---

## 8. Hash Table Search

Hash tables provide O(1) average time complexity for search operations using key-value pairs.

### Theory

#### Complexity Analysis
- **Time Complexity (Average)**: O(1)
- **Time Complexity (Worst)**: O(n) - Due to collisions
- **Space Complexity**: O(n)

### Implementation

```cpp
#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

/**
 * Hash table search using unordered_map
 */
template<typename K, typename V>
bool hashTableSearch(const unordered_map<K, V>& hashMap, const K& key, V& value) {
    auto it = hashMap.find(key);
    if (it != hashMap.end()) {
        value = it->second;
        return true;
    }
    return false;
}

int main() {
    // Example 1: Integer keys and values
    unordered_map<int, string> phoneBook = {
        {1001, "Alice"},
        {1002, "Bob"},
        {1003, "Charlie"},
        {1004, "Diana"},
        {1005, "Eve"}
    };
    
    cout << "Phone Book Search:" << endl;
    int searchId = 1003;
    string name;
    
    if (hashTableSearch(phoneBook, searchId, name)) {
        cout << "ID " << searchId << " belongs to " << name << endl;
    } else {
        cout << "ID " << searchId << " not found" << endl;
    }
    
    // Example 2: String keys
    unordered_map<string, int> wordCount = {
        {"hello", 5},
        {"world", 3},
        {"cpp", 7},
        {"search", 2}
    };
    
    string searchWord = "cpp";
    int count;
    
    if (hashTableSearch(wordCount, searchWord, count)) {
        cout << "Word '" << searchWord << "' appears " << count << " times" << endl;
    } else {
        cout << "Word '" << searchWord << "' not found" << endl;
    }
    
    // Example 3: Custom hash function
    struct Person {
        string name;
        int age;
        
        bool operator==(const Person& other) const {
            return name == other.name && age == other.age;
        }
    };
    
    struct PersonHash {
        size_t operator()(const Person& p) const {
            return hash<string>()(p.name) ^ hash<int>()(p.age);
        }
    };
    
    unordered_map<Person, string, PersonHash> employeeData = {
        {{"Alice", 25}, "Engineer"},
        {{"Bob", 30}, "Manager"},
        {{"Charlie", 35}, "Director"}
    };
    
    Person searchPerson = {"Bob", 30};
    auto it = employeeData.find(searchPerson);
    
    if (it != employeeData.end()) {
        cout << searchPerson.name << " (age " << searchPerson.age 
             << ") is a " << it->second << endl;
    } else {
        cout << "Employee not found" << endl;
    }
    
    return 0;
}
```

**Output:**
```
Phone Book Search:
ID 1003 belongs to Charlie
Word 'cpp' appears 7 times
Bob (age 30) is a Manager
```

---

## 9. Search in Trees

### Binary Search Tree (BST) Search

```cpp
#include <iostream>
#include <string>
using namespace std;

/**
 * Node structure for Binary Search Tree
 */
struct BSTNode {
    int data;
    BSTNode* left;
    BSTNode* right;
    
    BSTNode(int val) : data(val), left(nullptr), right(nullptr) {}
};

/**
 * Binary Search Tree class
 */
class BinarySearchTree {
private:
    BSTNode* root;
    
    /**
     * Insert helper function
     */
    BSTNode* insert(BSTNode* node, int data) {
        if (node == nullptr) {
            return new BSTNode(data);
        }
        
        if (data < node->data) {
            node->left = insert(node->left, data);
        } else if (data > node->data) {
            node->right = insert(node->right, data);
        }
        
        return node;
    }
    
    /**
     * Search helper function
     */
    bool search(BSTNode* node, int data) {
        if (node == nullptr) {
            return false;
        }
        
        if (node->data == data) {
            return true;
        }
        
        if (data < node->data) {
            return search(node->left, data);
        } else {
            return search(node->right, data);
        }
    }
    
    /**
     * Find minimum value node
     */
    BSTNode* findMin(BSTNode* node) {
        while (node->left != nullptr) {
            node = node->left;
        }
        return node;
    }
    
    /**
     * Delete helper function
     */
    BSTNode* deleteNode(BSTNode* node, int data) {
        if (node == nullptr) {
            return node;
        }
        
        if (data < node->data) {
            node->left = deleteNode(node->left, data);
        } else if (data > node->data) {
            node->right = deleteNode(node->right, data);
        } else {
            // Node with only one child or no child
            if (node->left == nullptr) {
                BSTNode* temp = node->right;
                delete node;
                return temp;
            } else if (node->right == nullptr) {
                BSTNode* temp = node->left;
                delete node;
                return temp;
            }
            
            // Node with two children
            BSTNode* temp = findMin(node->right);
            node->data = temp->data;
            node->right = deleteNode(node->right, temp->data);
        }
        
        return node;
    }
    
    /**
     * Inorder traversal
     */
    void inorder(BSTNode* node) {
        if (node == nullptr) return;
        
        inorder(node->left);
        cout << node->data << " ";
        inorder(node->right);
    }
    
public:
    BinarySearchTree() : root(nullptr) {}
    
    void insert(int data) {
        root = insert(root, data);
    }
    
    bool search(int data) {
        return search(root, data);
    }
    
    void remove(int data) {
        root = deleteNode(root, data);
    }
    
    void display() {
        cout << "BST (Inorder): ";
        inorder(root);
        cout << endl;
    }
};

int main() {
    BinarySearchTree bst;
    
    // Insert elements
    int elements[] = {50, 30, 70, 20, 40, 60, 80};
    for (int elem : elements) {
        bst.insert(elem);
    }
    
    bst.display();
    
    // Search operations
    int searchElements[] = {40, 90, 50, 25};
    
    for (int elem : searchElements) {
        cout << "Search " << elem << ": ";
        if (bst.search(elem)) {
            cout << "Found" << endl;
        } else {
            cout << "Not found" << endl;
        }
    }
    
    // Delete and search
    cout << "\nDeleting 40 and 70..." << endl;
    bst.remove(40);
    bst.remove(70);
    
    bst.display();
    
    cout << "Search 40 after deletion: ";
    if (bst.search(40)) {
        cout << "Found" << endl;
    } else {
        cout << "Not found" << endl;
    }
    
    return 0;
}
```

**Output:**
```
BST (Inorder): 20 30 40 50 60 70 80 
Search 40: Found
Search 90: Not found
Search 50: Found
Search 25: Not found

Deleting 40 and 70...
BST (Inorder): 20 30 50 60 80 
Search 40 after deletion: Not found
```

---

## 10. Performance Comparison

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <random>
#include <unordered_map>
using namespace std;
using namespace chrono;

/**
 * Performance comparison of search algorithms
 */
class SearchBenchmark {
private:
    vector<int> data;
    unordered_map<int, int> hashMap;
    
public:
    SearchBenchmark(int size) {
        // Generate sorted data for binary search algorithms
        data.reserve(size);
        for (int i = 0; i < size; i++) {
            data.push_back(i * 2);  // Even numbers
        }
        
        // Build hash map
        for (int i = 0; i < size; i++) {
            hashMap[data[i]] = i;
        }
    }
    
    // Linear Search
    long long benchmarkLinearSearch(int target) {
        auto start = high_resolution_clock::now();
        
        for (int val : data) {
            if (val == target) break;
        }
        
        auto end = high_resolution_clock::now();
        return duration_cast<nanoseconds>(end - start).count();
    }
    
    // Binary Search
    long long benchmarkBinarySearch(int target) {
        auto start = high_resolution_clock::now();
        
        binary_search(data.begin(), data.end(), target);
        
        auto end = high_resolution_clock::now();
        return duration_cast<nanoseconds>(end - start).count();
    }
    
    // Hash Table Search
    long long benchmarkHashSearch(int target) {
        auto start = high_resolution_clock::now();
        
        hashMap.find(target);
        
        auto end = high_resolution_clock::now();
        return duration_cast<nanoseconds>(end - start).count();
    }
    
    // STL Find
    long long benchmarkSTLFind(int target) {
        auto start = high_resolution_clock::now();
        
        find(data.begin(), data.end(), target);
        
        auto end = high_resolution_clock::now();
        return duration_cast<nanoseconds>(end - start).count();
    }
    
    void runBenchmark() {
        const int SIZE = data.size();
        int targetPresent = data[SIZE / 2];  // Middle element
        int targetAbsent = -1;               // Not present
        
        cout << "Search Algorithm Performance Comparison" << endl;
        cout << "Dataset size: " << SIZE << endl;
        cout << "Target (present): " << targetPresent << endl;
        cout << "Target (absent): " << targetAbsent << endl;
        cout << "----------------------------------------" << endl;
        
        // Test with present element
        cout << "\nSearching for PRESENT element:" << endl;
        cout << "Linear Search:    " << benchmarkLinearSearch(targetPresent) << " ns" << endl;
        cout << "Binary Search:    " << benchmarkBinarySearch(targetPresent) << " ns" << endl;
        cout << "Hash Table:       " << benchmarkHashSearch(targetPresent) << " ns" << endl;
        cout << "STL Find:         " << benchmarkSTLFind(targetPresent) << " ns" << endl;
        
        // Test with absent element
        cout << "\nSearching for ABSENT element:" << endl;
        cout << "Linear Search:    " << benchmarkLinearSearch(targetAbsent) << " ns" << endl;
        cout << "Binary Search:    " << benchmarkBinarySearch(targetAbsent) << " ns" << endl;
        cout << "Hash Table:       " << benchmarkHashSearch(targetAbsent) << " ns" << endl;
        cout << "STL Find:         " << benchmarkSTLFind(targetAbsent) << " ns" << endl;
    }
};

int main() {
    SearchBenchmark benchmark(100000);  // 100k elements
    benchmark.runBenchmark();
    
    return 0;
}
```

**Sample Output:**
```
Search Algorithm Performance Comparison
Dataset size: 100000
Target (present): 100000
Target (absent): -1
----------------------------------------

Searching for PRESENT element:
Linear Search:    125000 ns
Binary Search:    3500 ns
Hash Table:       150 ns
STL Find:         124000 ns

Searching for ABSENT element:
Linear Search:    250000 ns
Binary Search:    3500 ns
Hash Table:       200 ns
STL Find:         250000 ns
```

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
