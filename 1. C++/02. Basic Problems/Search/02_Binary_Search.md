# Binary Search in C++

## Overview
Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing the search interval in half.

## Theory

### Definition
Binary search compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated, and the search continues on the remaining half.

### Algorithm Steps
1. Start with the entire sorted array
2. Find the middle element
3. If middle element equals target, return its index
4. If target < middle element, search left half
5. If target > middle element, search right half
6. Repeat until found or array is exhausted

### Complexity Analysis
- **Time Complexity (Best Case)**: O(1) - when target is the middle element
- **Time Complexity (Average Case)**: O(log n)
- **Time Complexity (Worst Case)**: O(log n)
- **Space Complexity**: O(1) - iterative version, O(log n) - recursive version

### When to Use
- Sorted arrays
- Large datasets where O(log n) is acceptable
- Static data that doesn't change frequently

---

## Implementation 1: Iterative Binary Search

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

## Implementation 2: Recursive Binary Search

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

## Implementation 3: Binary Search on STL Containers

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

## Implementation 4: Binary Search with Template

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

/**
 * Generic binary search using templates
 * Works with any comparable data type
 */
template<typename T>
int binarySearchTemplate(const vector<T>& vec, const T& target) {
    int left = 0;
    int right = vec.size() - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (vec[mid] == target) {
            return mid;
        }
        
        if (vec[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1;
}

int main() {
    // Integer vector
    vector<int> intVec = {10, 23, 45, 70, 89, 100, 123, 145};
    cout << "Integer search for 70: " 
         << binarySearchTemplate(intVec, 70) << endl;
    
    // String vector (lexicographically sorted)
    vector<string> strVec = {"apple", "banana", "cherry", "date", "elderberry"};
    cout << "String search for 'cherry': " 
         << binarySearchTemplate(strVec, string("cherry")) << endl;
    
    // Double vector
    vector<double> doubleVec = {1.1, 2.2, 3.3, 4.4, 5.5};
    cout << "Double search for 3.3: " 
         << binarySearchTemplate(doubleVec, 3.3) << endl;
    
    return 0;
}
```

**Output:**
```
Integer search for 70: 3
String search for 'cherry': 2
Double search for 3.3: 2
```

---

## Implementation 5: Binary Search Variants

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/**
 * Find first occurrence of target
 */
int findFirstOccurrence(const vector<int>& vec, int target) {
    int left = 0;
    int right = vec.size() - 1;
    int result = -1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (vec[mid] == target) {
            result = mid;
            right = mid - 1;  // Continue searching left
        } else if (vec[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return result;
}

/**
 * Find last occurrence of target
 */
int findLastOccurrence(const vector<int>& vec, int target) {
    int left = 0;
    int right = vec.size() - 1;
    int result = -1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (vec[mid] == target) {
            result = mid;
            left = mid + 1;  // Continue searching right
        } else if (vec[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return result;
}

/**
 * Find count of occurrences
 */
int countOccurrences(const vector<int>& vec, int target) {
    int first = findFirstOccurrence(vec, target);
    if (first == -1) {
        return 0;
    }
    
    int last = findLastOccurrence(vec, target);
    return last - first + 1;
}

/**
 * Find floor of target (greatest element <= target)
 */
int findFloor(const vector<int>& vec, int target) {
    int left = 0;
    int right = vec.size() - 1;
    int floor = -1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (vec[mid] == target) {
            return mid;
        }
        
        if (vec[mid] < target) {
            floor = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return floor;
}

/**
 * Find ceiling of target (smallest element >= target)
 */
int findCeiling(const vector<int>& vec, int target) {
    int left = 0;
    int right = vec.size() - 1;
    int ceiling = -1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (vec[mid] == target) {
            return mid;
        }
        
        if (vec[mid] > target) {
            ceiling = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    
    return ceiling;
}

int main() {
    vector<int> vec = {10, 20, 20, 20, 30, 40, 50, 50, 60};
    
    int target = 20;
    
    cout << "Target: " << target << endl;
    cout << "First occurrence: " << findFirstOccurrence(vec, target) << endl;
    cout << "Last occurrence: " << findLastOccurrence(vec, target) << endl;
    cout << "Count: " << countOccurrences(vec, target) << endl;
    
    target = 35;
    cout << "\nTarget: " << target << endl;
    cout << "Floor: " << findFloor(vec, target) << " (value: " 
         << (findFloor(vec, target) != -1 ? to_string(vec[findFloor(vec, target)]) : "N/A") << ")" << endl;
    cout << "Ceiling: " << findCeiling(vec, target) << " (value: " 
         << (findCeiling(vec, target) != -1 ? to_string(vec[findCeiling(vec, target)]) : "N/A") << ")" << endl;
    
    return 0;
}
```

**Output:**
```
Target: 20
First occurrence: 1
Last occurrence: 3
Count: 3

Target: 35
Floor: 4 (value: 30)
Ceiling: 5 (value: 40)
```

---

## Implementation 6: Binary Search in 2D Matrix

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Binary search in row-wise sorted matrix
 * Matrix is sorted row-wise and column-wise
 */
bool searchMatrix(vector<vector<int>>& matrix, int target) {
    if (matrix.empty() || matrix[0].empty()) {
        return false;
    }
    
    int rows = matrix.size();
    int cols = matrix[0].size();
    
    int row = 0;
    int col = cols - 1;  // Start from top-right corner
    
    while (row < rows && col >= 0) {
        if (matrix[row][col] == target) {
            cout << "Found at (" << row << ", " << col << ")" << endl;
            return true;
        }
        
        if (matrix[row][col] > target) {
            col--;  // Move left
        } else {
            row++;  // Move down
        }
    }
    
    return false;
}

/**
 * Binary search in completely sorted matrix
 * Each row is sorted and first element of each row > last element of previous row
 */
bool searchCompletelySortedMatrix(vector<vector<int>>& matrix, int target) {
    if (matrix.empty() || matrix[0].empty()) {
        return false;
    }
    
    int rows = matrix.size();
    int cols = matrix[0].size();
    
    int left = 0;
    int right = rows * cols - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        int midRow = mid / cols;
        int midCol = mid % cols;
        
        if (matrix[midRow][midCol] == target) {
            cout << "Found at (" << midRow << ", " << midCol << ")" << endl;
            return true;
        }
        
        if (matrix[midRow][midCol] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return false;
}

int main() {
    // Row-wise and column-wise sorted matrix
    vector<vector<int>> matrix1 = {
        {10, 20, 30, 40},
        {15, 25, 35, 45},
        {27, 29, 37, 48},
        {32, 33, 39, 50}
    };
    
    cout << "Search in row-wise sorted matrix:" << endl;
    searchMatrix(matrix1, 29) ? cout << "Found" << endl : cout << "Not found" << endl;
    searchMatrix(matrix1, 100) ? cout << "Found" << endl : cout << "Not found" << endl;
    
    // Completely sorted matrix
    vector<vector<int>> matrix2 = {
        {1, 3, 5, 7},
        {10, 11, 16, 20},
        {23, 30, 34, 60}
    };
    
    cout << "\nSearch in completely sorted matrix:" << endl;
    searchCompletelySortedMatrix(matrix2, 16) ? cout << "Found" << endl : cout << "Not found" << endl;
    searchCompletelySortedMatrix(matrix2, 13) ? cout << "Found" << endl : cout << "Not found" << endl;
    
    return 0;
}
```

**Output:**
```
Search in row-wise sorted matrix:
Found at (2, 1)
Found
Not found

Search in completely sorted matrix:
Found at (1, 2)
Found
Not found
```

---

## Implementation 7: Binary Search for Answer

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/**
 * Example 1: Find square root using binary search
 */
int integerSquareRoot(int x) {
    if (x < 2) {
        return x;
    }
    
    int left = 1;
    int right = x / 2;
    int result = 0;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (mid <= x / mid) {
            result = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return result;
}

/**
 * Example 2: Find minimum in rotated sorted array
 */
int findMinInRotatedArray(const vector<int>& nums) {
    int left = 0;
    int right = nums.size() - 1;
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    
    return nums[left];
}

/**
 * Example 3: Find peak element
 */
int findPeakElement(const vector<int>& nums) {
    int left = 0;
    int right = nums.size() - 1;
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        
        if (nums[mid] < nums[mid + 1]) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    
    return left;
}

/**
 * Example 4: Allocate minimum number of pages
 */
bool isValidAllocation(const vector<int>& books, int students, int maxPages) {
    int studentCount = 1;
    int currentSum = 0;
    
    for (int pages : books) {
        if (pages > maxPages) {
            return false;
        }
        
        if (currentSum + pages > maxPages) {
            studentCount++;
            currentSum = pages;
            
            if (studentCount > students) {
                return false;
            }
        } else {
            currentSum += pages;
        }
    }
    
    return true;
}

int allocateMinimumPages(const vector<int>& books, int students) {
    if (books.size() < students) {
        return -1;
    }
    
    int left = *max_element(books.begin(), books.end());
    int right = 0;
    
    for (int pages : books) {
        right += pages;
    }
    
    int result = -1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (isValidAllocation(books, students, mid)) {
            result = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    
    return result;
}

int main() {
    // Test square root
    cout << "Square root examples:" << endl;
    for (int i = 0; i <= 20; i++) {
        cout << "sqrt(" << i << ") = " << integerSquareRoot(i) << endl;
    }
    
    // Test rotated array
    cout << "\nRotated array minimum:" << endl;
    vector<int> rotated = {4, 5, 6, 7, 0, 1, 2};
    cout << "Minimum in [4,5,6,7,0,1,2]: " << findMinInRotatedArray(rotated) << endl;
    
    // Test peak element
    cout << "\nPeak element:" << endl;
    vector<int> peakArray = {1, 3, 20, 4, 1, 0};
    cout << "Peak in [1,3,20,4,1,0]: " << peakArray[findPeakElement(peakArray)] << endl;
    
    // Test book allocation
    cout << "\nBook allocation:" << endl;
    vector<int> books = {12, 34, 67, 90};
    int students = 2;
    cout << "Minimum pages for " << students << " students: " 
         << allocateMinimumPages(books, students) << endl;
    
    return 0;
}
```

**Output:**
```
Square root examples:
sqrt(0) = 0
sqrt(1) = 1
sqrt(2) = 1
sqrt(3) = 1
sqrt(4) = 2
sqrt(5) = 2
sqrt(6) = 2
sqrt(7) = 2
sqrt(8) = 2
sqrt(9) = 3
sqrt(10) = 3
sqrt(11) = 3
sqrt(12) = 3
sqrt(13) = 3
sqrt(14) = 3
sqrt(15) = 3
sqrt(16) = 4
sqrt(17) = 4
sqrt(18) = 4
sqrt(19) = 4
sqrt(20) = 4

Rotated array minimum:
Minimum in [4,5,6,7,0,1,2]: 0

Peak element:
Peak in [1,3,20,4,1,0]: 20

Book allocation:
Minimum pages for 2 students: 113
```

---

## Advantages and Disadvantages

### Advantages
- ✅ Very efficient for large datasets (O(log n))
- ✅ Simple to implement
- ✅ Guaranteed performance
- ✅ Works with any comparable data type
- ✅ Memory efficient (O(1) space)

### Disadvantages
- ❌ Requires sorted data
- ❌ Not suitable for frequent insertions/deletions
- ❌ Overhead for small datasets
- ❌ Need to maintain sorted order

---

## Best Practices

1. **Use `left + (right - left) / 2`** to prevent integer overflow
2. **Prefer `std::binary_search`** for simple existence checks
3. **Use `lower_bound`/`upper_bound`** for finding ranges
4. **Consider edge cases**: empty array, single element
5. **Test with boundaries**: first, last, non-existent elements
6. **Use templates** for generic implementations

---

## Common Pitfalls

1. **Integer overflow** in mid calculation
2. **Off-by-one errors** in loop conditions
3. **Not handling duplicates** correctly
4. **Using on unsorted data**
5. **Infinite loops** due to incorrect bounds update

---

## Summary

Binary search is a fundamental algorithm that provides O(log n) time complexity for searching in sorted collections. It's the go-to algorithm when you have sorted data and need fast search operations.

**Key Takeaways:**
- Time Complexity: O(log n)
- Space Complexity: O(1)
- Requires sorted data
- Use for large, static datasets
- Multiple variants for different use cases
