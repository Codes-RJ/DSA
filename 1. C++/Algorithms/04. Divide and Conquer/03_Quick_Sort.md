# 03_Quick_Sort.md

## Quick Sort

### Definition

Quick Sort is a divide-and-conquer sorting algorithm that selects a pivot element, partitions the array around the pivot (placing smaller elements to the left and larger to the right), and then recursively sorts the subarrays.

### Algorithm Steps

```
Step 1: PARTITION
        Choose a pivot element
        Rearrange array so elements < pivot come before pivot
        Elements > pivot come after pivot

Step 2: CONQUER
        Recursively sort the left subarray (elements < pivot)
        Recursively sort the right subarray (elements > pivot)

Step 3: COMBINE
        No combine step needed (array is sorted in place)
```

### Visual Example

```
Input: [10, 7, 8, 9, 1, 5]

Choose pivot = 5 (last element)
Partition: [1, 5, 7, 8, 9, 10]  (pivot in correct position)

Recursively sort left of 5: [1] → already sorted
Recursively sort right of 5: [7, 8, 9, 10]

Choose pivot = 10
Partition: [7, 8, 9, 10] → 10 in correct position

Recursively sort [7, 8, 9]
Choose pivot = 9
Partition: [7, 8, 9] → 9 in correct position

Recursively sort [7, 8]
Choose pivot = 8
Partition: [7, 8] → 8 in correct position

Final: [1, 5, 7, 8, 9, 10]
```

### Implementation

```cpp
#include <iostream>
#include <vector>
using namespace std;

int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];  // choose last element as pivot
    int i = low - 1;  // index of smaller element
    
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    
    swap(arr[i + 1], arr[high]);
    return i + 1;  // return pivot index
}

void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pivotIndex = partition(arr, low, high);
        
        quickSort(arr, low, pivotIndex - 1);
        quickSort(arr, pivotIndex + 1, high);
    }
}

int main() {
    vector<int> arr = {10, 7, 8, 9, 1, 5};
    
    quickSort(arr, 0, arr.size() - 1);
    
    cout << "Sorted array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
    
    return 0;
}
```

### Partition Step in Detail

```
Array: [10, 7, 8, 9, 1, 5], pivot = 5, i = -1

j=0: arr[0]=10 <=5? No → nothing
j=1: arr[1]=7 <=5? No → nothing
j=2: arr[2]=8 <=5? No → nothing
j=3: arr[3]=9 <=5? No → nothing
j=4: arr[4]=1 <=5? Yes → i=0, swap(1,10) → [1, 7, 8, 9, 10, 5]

After loop: swap(arr[1], arr[5]) → [1, 5, 8, 9, 10, 7]
Return pivotIndex = 1
```

### Different Pivot Choices

```cpp
// 1. First element as pivot
int partitionFirst(vector<int>& arr, int low, int high) {
    int pivot = arr[low];
    int i = high + 1;
    
    for (int j = high; j > low; j--) {
        if (arr[j] >= pivot) {
            i--;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i - 1], arr[low]);
    return i - 1;
}

// 2. Middle element as pivot
int partitionMiddle(vector<int>& arr, int low, int high) {
    int mid = low + (high - low) / 2;
    swap(arr[mid], arr[high]);  // move pivot to end
    return partition(arr, low, high);
}

// 3. Random pivot (avoids worst case)
#include <cstdlib>
#include <ctime>

int partitionRandom(vector<int>& arr, int low, int high) {
    srand(time(NULL));
    int random = low + rand() % (high - low + 1);
    swap(arr[random], arr[high]);
    return partition(arr, low, high);
}

// 4. Median of three (best for nearly sorted arrays)
int medianOfThree(vector<int>& arr, int low, int high) {
    int mid = low + (high - low) / 2;
    
    if (arr[low] > arr[mid]) swap(arr[low], arr[mid]);
    if (arr[low] > arr[high]) swap(arr[low], arr[high]);
    if (arr[mid] > arr[high]) swap(arr[mid], arr[high]);
    
    swap(arr[mid], arr[high]);  // move median to end
    return partition(arr, low, high);
}
```

### Time Complexity Analysis

| Case | Complexity | Explanation |
|------|------------|-------------|
| Best | O(n log n) | Pivot divides array into equal halves |
| Average | O(n log n) | Random pivot gives balanced partitions |
| Worst | O(n²) | Pivot is smallest or largest element (sorted array) |

### Space Complexity

O(log n) for recursion stack (average case)
O(n) for recursion stack (worst case)

### Stability

Quick Sort is not stable. Equal elements may change relative order.

### Advantages

| Advantage | Description |
|-----------|-------------|
| In-place sorting | Uses O(log n) extra space |
| Cache efficient | Works well with memory hierarchy |
| Fast in practice | Often faster than merge sort for random data |
| Tail recursion | Can be optimized to use less stack |

### Disadvantages

| Disadvantage | Description |
|--------------|-------------|
| Worst-case O(n²) | Sorted or reverse sorted arrays |
| Unstable | Equal elements may be reordered |
| Not suitable for linked lists | Poor performance due to random access |

### Quick Sort for Linked Lists

```cpp
struct Node {
    int data;
    Node* next;
};

Node* getTail(Node* head) {
    while (head && head->next) {
        head = head->next;
    }
    return head;
}

Node* partitionList(Node* head, Node* end, Node** newHead, Node** newEnd) {
    Node* pivot = end;
    Node* prev = nullptr;
    Node* curr = head;
    Node* tail = pivot;
    
    while (curr != pivot) {
        if (curr->data < pivot->data) {
            if (!(*newHead)) *newHead = curr;
            prev = curr;
            curr = curr->next;
        } else {
            if (prev) prev->next = curr->next;
            Node* temp = curr->next;
            curr->next = nullptr;
            tail->next = curr;
            tail = curr;
            curr = temp;
        }
    }
    
    if (!(*newHead)) *newHead = pivot;
    *newEnd = tail;
    
    return pivot;
}

Node* quickSortList(Node* head, Node* end) {
    if (!head || head == end) return head;
    
    Node* newHead = nullptr;
    Node* newEnd = nullptr;
    
    Node* pivot = partitionList(head, end, &newHead, &newEnd);
    
    if (newHead != pivot) {
        Node* temp = newHead;
        while (temp->next != pivot) {
            temp = temp->next;
        }
        temp->next = nullptr;
        
        newHead = quickSortList(newHead, temp);
        
        temp = getTail(newHead);
        temp->next = pivot;
    }
    
    pivot->next = quickSortList(pivot->next, newEnd);
    
    return newHead;
}
```

### Iterative Quick Sort

```cpp
void iterativeQuickSort(vector<int>& arr, int low, int high) {
    vector<pair<int, int>> stack;
    stack.push_back({low, high});
    
    while (!stack.empty()) {
        auto [l, h] = stack.back();
        stack.pop_back();
        
        if (l < h) {
            int p = partition(arr, l, h);
            
            stack.push_back({l, p - 1});
            stack.push_back({p + 1, h});
        }
    }
}
```

### Quick Sort vs Merge Sort

| Aspect | Quick Sort | Merge Sort |
|--------|------------|------------|
| Time (average) | O(n log n) | O(n log n) |
| Time (worst) | O(n²) | O(n log n) |
| Space | O(log n) | O(n) |
| In-place | Yes | No |
| Stable | No | Yes |
| Cache friendly | Yes | No |
| Linked lists | Poor | Good |

### Practice Problems

1. Sort an array using quick sort
2. Implement quick sort with random pivot
3. Implement quick sort with median-of-three pivot
4. Sort an array of strings using quick sort
5. Implement iterative quick sort
