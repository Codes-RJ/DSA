# 11_Inversion_Count.md

## Inversion Count

### Definition

An inversion is a pair of indices (i, j) such that i < j and arr[i] > arr[j]. The inversion count measures how far an array is from being sorted.

### Problem Statement

Input:
- An array arr of integers

Output:
- The number of inversions in the array

### Example

```
Array: [2, 4, 1, 3, 5]

Inversions:
(2,1) at indices (0,2)
(4,1) at indices (1,2)
(4,3) at indices (1,3)

Total inversions = 3
```

### Divide and Conquer Approach (Modified Merge Sort)

```
Step 1: Divide array into two halves
Step 2: Recursively count inversions in left half
Step 3: Recursively count inversions in right half
Step 4: Count cross inversions (one element from left, one from right)
Step 5: Merge the two halves (as in merge sort)
Step 6: Return sum of all three counts
```

### Implementation

```cpp
#include <iostream>
#include <vector>
using namespace std;

long long mergeAndCount(vector<int>& arr, int left, int mid, int right) {
    vector<int> leftArr(arr.begin() + left, arr.begin() + mid + 1);
    vector<int> rightArr(arr.begin() + mid + 1, arr.begin() + right + 1);
    
    int i = 0, j = 0, k = left;
    long long inversions = 0;
    
    while (i < leftArr.size() && j < rightArr.size()) {
        if (leftArr[i] <= rightArr[j]) {
            arr[k++] = leftArr[i++];
        } else {
            // All remaining elements in leftArr are greater than rightArr[j]
            inversions += (leftArr.size() - i);
            arr[k++] = rightArr[j++];
        }
    }
    
    while (i < leftArr.size()) {
        arr[k++] = leftArr[i++];
    }
    
    while (j < rightArr.size()) {
        arr[k++] = rightArr[j++];
    }
    
    return inversions;
}

long long inversionCount(vector<int>& arr, int left, int right) {
    if (left >= right) {
        return 0;
    }
    
    int mid = left + (right - left) / 2;
    
    long long inversions = 0;
    inversions += inversionCount(arr, left, mid);
    inversions += inversionCount(arr, mid + 1, right);
    inversions += mergeAndCount(arr, left, mid, right);
    
    return inversions;
}

int main() {
    vector<int> arr = {2, 4, 1, 3, 5};
    
    long long result = inversionCount(arr, 0, arr.size() - 1);
    
    cout << "Number of inversions: " << result << endl;
    
    return 0;
}
```

### Example Walkthrough

```
Array: [2, 4, 1, 3, 5]

Step 1: Divide
[2, 4, 1] and [3, 5]

Step 2: Divide further
[2, 4] and [1]    [3] and [5]

Step 3: Base cases (size 1, inversions = 0)

Step 4: Merge [2, 4] and [1]
    left=[2,4], right=[1]
    Compare 2 and 1: 2>1 → inversion += 2 (both 2 and 4 > 1)
    inversions = 2, merged = [1,2,4]

Step 5: Merge [1,2,4] and [3]
    left=[1,2,4], right=[3]
    Compare 1 and 3: 1<3 → no inversion, merged add 1
    Compare 2 and 3: 2<3 → no inversion, merged add 2
    Compare 4 and 3: 4>3 → inversion += 1 (only 4 > 3)
    inversions = 2 + 1 = 3, merged = [1,2,3,4]

Step 6: Merge [1,2,3,4] and [5]
    No inversions

Total inversions = 3
```

### Visualization of Cross Inversions

```
Merging [2, 4] and [1]:

leftArr: [2, 4]
rightArr: [1]

When we pick 1 from rightArr:
- All remaining elements in leftArr (2 and 4) are > 1
- inversions += 2

Merging [1, 2, 4] and [3]:

leftArr: [1, 2, 4]
rightArr: [3]

When we pick 3 from rightArr:
- Remaining elements in leftArr are [4] (since 1 and 2 are already merged)
- 4 > 3 → inversions += 1
```

### Time Complexity

| Operation | Complexity |
|-----------|------------|
| Recursive divisions | O(log n) levels |
| Merge at each level | O(n) |
| Total | O(n log n) |

### Space Complexity

O(n) for temporary arrays during merge

### Brute Force Approach (O(n²))

```cpp
long long bruteForceInversions(vector<int>& arr) {
    long long inversions = 0;
    int n = arr.size();
    
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] > arr[j]) {
                inversions++;
            }
        }
    }
    
    return inversions;
}
```

### Comparison of Approaches

| Approach | Time Complexity | Space Complexity | When to Use |
|----------|----------------|------------------|-------------|
| Brute Force | O(n²) | O(1) | n ≤ 5000 |
| Merge Sort | O(n log n) | O(n) | n ≤ 10^5 |
| Fenwick Tree | O(n log n) | O(n) | With coordinate compression |

### Fenwick Tree Approach (Alternative)

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class FenwickTree {
    vector<int> bit;
    int n;
    
public:
    FenwickTree(int size) : n(size), bit(size + 1, 0) {}
    
    void update(int idx, int delta) {
        while (idx <= n) {
            bit[idx] += delta;
            idx += idx & -idx;
        }
    }
    
    int query(int idx) {
        int sum = 0;
        while (idx > 0) {
            sum += bit[idx];
            idx -= idx & -idx;
        }
        return sum;
    }
};

long long inversionCountFenwick(vector<int>& arr) {
    // Coordinate compression
    vector<int> sorted = arr;
    sort(sorted.begin(), sorted.end());
    sorted.erase(unique(sorted.begin(), sorted.end()), sorted.end());
    
    FenwickTree bit(sorted.size());
    long long inversions = 0;
    
    for (int i = arr.size() - 1; i >= 0; i--) {
        int rank = lower_bound(sorted.begin(), sorted.end(), arr[i]) - sorted.begin() + 1;
        inversions += bit.query(rank - 1);
        bit.update(rank, 1);
    }
    
    return inversions;
}
```

### Applications

| Application | Description |
|-------------|-------------|
| Sorting analysis | Measure how unsorted an array is |
| Collaborative filtering | Compare user preferences |
| DNA sequence analysis | Measure similarity |
| Array similarity | Compare two arrays (with mapping) |

### Practice Problems

1. Count inversions in an array
2. Count significant inversions (arr[i] > 2*arr[j])
3. Count inversions in a string (character comparisons)
4. Count inversions after K swaps
5. Count inversions in a circular array
