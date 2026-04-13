# 02_Merge_Sort.md

## Merge Sort

### Definition

Merge Sort is a divide-and-conquer sorting algorithm that divides an array into two halves, recursively sorts each half, and then merges the two sorted halves.

### Algorithm Steps

```
Step 1: DIVIDE
        Find the middle index and split array into left and right halves

Step 2: CONQUER
        Recursively sort the left half
        Recursively sort the right half

Step 3: COMBINE
        Merge the two sorted halves into a single sorted array
```

### Visual Example

```
Input: [38, 27, 43, 3, 9, 82, 10]

Step 1: Divide
[38, 27, 43, 3]  and  [9, 82, 10]

Step 2: Further divide
[38, 27] and [43, 3]    [9, 82] and [10]

Step 3: Further divide (base cases)
[38] [27] [43] [3]      [9] [82] [10]

Step 4: Merge
[27, 38] and [3, 43]    [9, 82] and [10]
[3, 27, 38, 43]         [9, 10, 82]

Step 5: Final merge
[3, 9, 10, 27, 38, 43, 82]
```

### Implementation

```cpp
#include <iostream>
#include <vector>
using namespace std;

void merge(vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    
    vector<int> leftArr(n1);
    vector<int> rightArr(n2);
    
    for (int i = 0; i < n1; i++) {
        leftArr[i] = arr[left + i];
    }
    for (int j = 0; j < n2; j++) {
        rightArr[j] = arr[mid + 1 + j];
    }
    
    int i = 0, j = 0, k = left;
    
    while (i < n1 && j < n2) {
        if (leftArr[i] <= rightArr[j]) {
            arr[k] = leftArr[i];
            i++;
        } else {
            arr[k] = rightArr[j];
            j++;
        }
        k++;
    }
    
    while (i < n1) {
        arr[k] = leftArr[i];
        i++;
        k++;
    }
    
    while (j < n2) {
        arr[k] = rightArr[j];
        j++;
        k++;
    }
}

void mergeSort(vector<int>& arr, int left, int right) {
    if (left >= right) {
        return;
    }
    
    int mid = left + (right - left) / 2;
    
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    
    merge(arr, left, mid, right);
}

int main() {
    vector<int> arr = {38, 27, 43, 3, 9, 82, 10};
    
    mergeSort(arr, 0, arr.size() - 1);
    
    cout << "Sorted array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
    
    return 0;
}
```

### Step-by-Step Merge Example

```
Merging [27, 38] and [3, 43]:

leftArr = [27, 38], rightArr = [3, 43]

Compare 27 and 3: 3 is smaller → result = [3]
Compare 27 and 43: 27 is smaller → result = [3, 27]
Compare 38 and 43: 38 is smaller → result = [3, 27, 38]
Left exhausted, add remaining 43 → result = [3, 27, 38, 43]
```

### Time Complexity Analysis

| Case | Complexity | Explanation |
|------|------------|-------------|
| Best | O(n log n) | Always divides and merges |
| Average | O(n log n) | Always divides and merges |
| Worst | O(n log n) | Always divides and merges |

### Space Complexity

O(n) for the temporary arrays used in merging

### Stability

Merge Sort is stable. Equal elements maintain their relative order.

### Advantages

| Advantage | Description |
|-----------|-------------|
| Guaranteed O(n log n) | Performance doesn't depend on input order |
| Stable | Equal elements keep original order |
| Works well for linked lists | Can merge linked lists in O(1) extra space |
| Predictable | Same complexity for all cases |

### Disadvantages

| Disadvantage | Description |
|--------------|-------------|
| Extra space | Requires O(n) auxiliary space |
| Not in-place | Cannot sort without extra memory |
| Overhead | More memory operations than Quick Sort |

### Merge Sort on Linked Lists

```cpp
struct Node {
    int data;
    Node* next;
};

Node* merge(Node* left, Node* right) {
    if (!left) return right;
    if (!right) return left;
    
    if (left->data <= right->data) {
        left->next = merge(left->next, right);
        return left;
    } else {
        right->next = merge(left, right->next);
        return right;
    }
}

Node* mergeSort(Node* head) {
    if (!head || !head->next) return head;
    
    // Find middle
    Node* slow = head;
    Node* fast = head->next;
    
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    
    Node* mid = slow->next;
    slow->next = nullptr;
    
    Node* left = mergeSort(head);
    Node* right = mergeSort(mid);
    
    return merge(left, right);
}
```

### Iterative Merge Sort (Bottom-Up)

```cpp
void iterativeMergeSort(vector<int>& arr) {
    int n = arr.size();
    
    for (int currSize = 1; currSize < n; currSize *= 2) {
        for (int leftStart = 0; leftStart < n - 1; leftStart += 2 * currSize) {
            int mid = min(leftStart + currSize - 1, n - 1);
            int rightEnd = min(leftStart + 2 * currSize - 1, n - 1);
            merge(arr, leftStart, mid, rightEnd);
        }
    }
}
```

### Merge Sort vs Quick Sort

| Aspect | Merge Sort | Quick Sort |
|--------|------------|------------|
| Time (average) | O(n log n) | O(n log n) |
| Time (worst) | O(n log n) | O(n²) |
| Space | O(n) | O(log n) |
| Stability | Stable | Unstable |
| In-place | No | Yes (mostly) |
| Cache performance | Poor | Good |

### Practice Problems

1. Sort an array using merge sort
2. Sort a linked list using merge sort
3. Count inversions using merge sort (see Inversion Count file)
4. Merge two sorted arrays
5. Sort an array of strings using merge sort
---

## Next Step

- Go to [03_Quick_Sort.md](03_Quick_Sort.md) to continue with Quick Sort.
