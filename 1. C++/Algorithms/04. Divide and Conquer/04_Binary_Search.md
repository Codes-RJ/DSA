# 04_Binary_Search.md

## Binary Search

### Definition

Binary Search is a divide-and-conquer algorithm that finds the position of a target value in a sorted array by repeatedly dividing the search interval in half.

### Algorithm Steps

```
Step 1: Compare target with middle element of array
Step 2: If target matches middle, return its index
Step 3: If target is smaller, search left half
Step 4: If target is larger, search right half
Step 5: Repeat until target is found or interval is empty
```

### Visual Example

```
Sorted array: [1, 3, 5, 7, 9, 11, 13]
Target: 7

Step 1: left=0, right=6, mid=3 → arr[3]=7 → found!

Target: 2

Step 1: left=0, right=6, mid=3 → arr[3]=7 > 2 → search left
Step 2: left=0, right=2, mid=1 → arr[1]=3 > 2 → search left
Step 3: left=0, right=0, mid=0 → arr[0]=1 < 2 → search right
Step 4: left=1, right=0 → loop ends → not found
```

### Implementation (Iterative)

```cpp
#include <iostream>
#include <vector>
using namespace std;

int binarySearch(vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;  // avoid overflow
        
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1;  // not found
}

int main() {
    vector<int> arr = {1, 3, 5, 7, 9, 11, 13};
    int target = 7;
    
    int result = binarySearch(arr, target);
    
    if (result != -1) {
        cout << "Element found at index: " << result << endl;
    } else {
        cout << "Element not found" << endl;
    }
    
    return 0;
}
```

### Implementation (Recursive)

```cpp
int binarySearchRecursive(vector<int>& arr, int left, int right, int target) {
    if (left > right) {
        return -1;
    }
    
    int mid = left + (right - left) / 2;
    
    if (arr[mid] == target) {
        return mid;
    } else if (arr[mid] < target) {
        return binarySearchRecursive(arr, mid + 1, right, target);
    } else {
        return binarySearchRecursive(arr, left, mid - 1, target);
    }
}
```

### Variants of Binary Search

#### 1. First Occurrence (Lower Bound)

Find the first index where target appears.

```cpp
int firstOccurrence(vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    int result = -1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            result = mid;
            right = mid - 1;  // search left for earlier occurrence
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return result;
}
```

#### 2. Last Occurrence (Upper Bound)

Find the last index where target appears.

```cpp
int lastOccurrence(vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    int result = -1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            result = mid;
            left = mid + 1;  // search right for later occurrence
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return result;
}
```

#### 3. Lower Bound (First Element >= Target)

```cpp
int lowerBound(vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size();
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    
    return left;
}
```

#### 4. Upper Bound (First Element > Target)

```cpp
int upperBound(vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size();
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] <= target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    
    return left;
}
```

#### 5. Search in Rotated Sorted Array

```cpp
int searchRotated(vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid;
        }
        
        // Left half is sorted
        if (arr[left] <= arr[mid]) {
            if (arr[left] <= target && target < arr[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        // Right half is sorted
        else {
            if (arr[mid] < target && target <= arr[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }
    
    return -1;
}
```

#### 6. Find Peak Element

```cpp
int findPeak(vector<int>& arr) {
    int left = 0;
    int right = arr.size() - 1;
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] > arr[mid + 1]) {
            right = mid;  // peak is on left (including mid)
        } else {
            left = mid + 1;  // peak is on right
        }
    }
    
    return left;
}
```

### Time Complexity

| Operation | Complexity |
|-----------|------------|
| Best case | O(1) |
| Average case | O(log n) |
| Worst case | O(log n) |

### Space Complexity

| Implementation | Space |
|----------------|-------|
| Iterative | O(1) |
| Recursive | O(log n) (recursion stack) |

### Binary Search on Answer

Binary search can also be used to find optimal values in problems like:

```cpp
// Find minimum x such that condition(x) is true
int binarySearchOnAnswer(int low, int high) {
    int result = -1;
    
    while (low <= high) {
        int mid = low + (high - low) / 2;
        
        if (condition(mid)) {
            result = mid;
            high = mid - 1;  // search left for smaller
        } else {
            low = mid + 1;   // search right
        }
    }
    
    return result;
}
```

### Common Applications

| Problem | Description |
|---------|-------------|
| Search in sorted array | Find element position |
| Find first/last occurrence | Range queries |
| Square root | Find sqrt(x) without math functions |
| Search in rotated array | Modified binary search |
| Find median | Median of two sorted arrays |
| Optimization problems | Binary search on answer |

### Practice Problems

1. Standard binary search
2. Find first and last occurrence of target
3. Search in rotated sorted array
4. Find peak element
5. Find square root of a number
6. Find the smallest element greater than target
7. Find the largest element smaller than target

---