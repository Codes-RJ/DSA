# 16_Maximum_Sum_after_K_Negations.md

## Maximum Sum after K Negations

### Definition

Given an array of integers, you can perform exactly K operations. In each operation, you can choose any element and negate it (multiply by -1). Find the maximum possible sum of the array after exactly K operations.

### Problem Statement

Input:
- An array arr of integers (can be positive, negative, or zero)
- An integer K (number of negations to perform)

Output:
- Maximum possible sum after exactly K negations

### Greedy Strategy

**Strategy:** 
1. Negate the smallest (most negative) elements first
2. If K is still remaining after making all numbers non-negative, handle the smallest absolute value

**Why this works:** Negating a negative number increases the sum. Once all numbers are non-negative, negating the smallest number minimizes the loss.

### Algorithm

```
Step 1: Sort the array
Step 2: For i from 0 to n-1 while K > 0 and arr[i] < 0:
        arr[i] = -arr[i]
        K--
Step 3: If K is odd:
        Find the smallest absolute value in the array
        Negate it (this will reduce the sum by 2 * smallest)
Step 4: Return sum of array
```

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int maxSumAfterKNegations(vector<int>& arr, int K) {
    sort(arr.begin(), arr.end());
    
    int n = arr.size();
    
    // Negate the most negative numbers first
    for (int i = 0; i < n && K > 0; i++) {
        if (arr[i] < 0) {
            arr[i] = -arr[i];
            K--;
        }
    }
    
    // If K is still odd, negate the smallest absolute value
    if (K % 2 == 1) {
        int minIndex = 0;
        for (int i = 1; i < n; i++) {
            if (arr[i] < arr[minIndex]) {
                minIndex = i;
            }
        }
        arr[minIndex] = -arr[minIndex];
    }
    
    // Calculate sum
    int sum = 0;
    for (int num : arr) {
        sum += num;
    }
    
    return sum;
}

int main() {
    vector<int> arr = {4, 2, 3, -1, -5};
    int K = 2;
    
    int result = maxSumAfterKNegations(arr, K);
    cout << "Maximum sum: " << result << endl;
    
    return 0;
}
```

### Example Walkthrough

```
Example 1:
arr = [4, 2, 3, -1, -5], K = 2

Step 1: Sort → [-5, -1, 2, 3, 4]
Step 2: Negate negatives
    i=0: -5 → 5, K=1
    i=1: -1 → 1, K=0
    arr = [5, 1, 2, 3, 4]
Step 3: K=0 (even), no further negation
Step 4: Sum = 5+1+2+3+4 = 15

Example 2:
arr = [4, 2, 3, -1, -5], K = 3

Step 1: Sort → [-5, -1, 2, 3, 4]
Step 2: Negate negatives
    i=0: -5 → 5, K=2
    i=1: -1 → 1, K=1
    arr = [5, 1, 2, 3, 4]
Step 3: K=1 (odd), smallest absolute value = 1
    Negate 1 → -1
    arr = [5, -1, 2, 3, 4]
Step 4: Sum = 5 + (-1) + 2 + 3 + 4 = 13

Example 3:
arr = [4, 2, 3, 1, 5], K = 2

Step 1: Sort → [1, 2, 3, 4, 5] (no negatives)
Step 2: No negatives to negate, K still 2
Step 3: K=2 (even), no further negation needed
    (Even K means we can negate same number twice, returning to original)
Step 4: Sum = 1+2+3+4+5 = 15
```

### Why Even/Odd K Matters

| K parity | Effect when all numbers non-negative |
|----------|--------------------------------------|
| Even | Can negate same number twice → no net change |
| Odd | Must negate one number, choose smallest to minimize loss |

### Alternative Implementation (Using Min-Heap)

```cpp
int maxSumAfterKNegationsHeap(vector<int>& arr, int K) {
    priority_queue<int, vector<int>, greater<int>> pq;
    
    for (int num : arr) {
        pq.push(num);
    }
    
    for (int i = 0; i < K; i++) {
        int smallest = pq.top();
        pq.pop();
        pq.push(-smallest);
    }
    
    int sum = 0;
    while (!pq.empty()) {
        sum += pq.top();
        pq.pop();
    }
    
    return sum;
}
```

### Time Complexity

| Implementation | Time Complexity |
|----------------|-----------------|
| Sorting method | O(n log n) |
| Heap method | O(K log n) but K can be large |

### Space Complexity

O(1) extra space for sorting method

### Variations

#### 1. At Most K Negations

If you can perform at most K negations (not exactly), then only negate negatives and if K remains odd, you can choose to not negate the smallest.

#### 2. Maximum Product after K Negations

Similar but with multiplication instead of sum.

#### 3. Maximize Sum after K Swaps

Different problem where you can swap elements.

### Proof of Optimality

**Greedy Choice Property:** Negating the smallest (most negative) number always increases the sum the most.

**Proof:**
- Let x be the smallest number (most negative)
- Negating x increases sum by -2x (since -x - x = -2x)
- Any other number y > x gives increase -2y which is smaller
- Therefore, always choose smallest number

**After all negatives are gone:** Negating a positive number reduces sum by 2×value
- To minimize loss, choose smallest positive number
- If K is even, we can negate same number twice → no net loss
