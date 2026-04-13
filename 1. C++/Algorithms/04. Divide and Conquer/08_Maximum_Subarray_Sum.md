# 08_Maximum_Subarray_Sum.md

## Maximum Subarray Sum (Kadane's Algorithm and Divide and Conquer)

### Definition

Given an array of integers (which may include negative numbers), find the contiguous subarray with the largest sum.

### Problem Statement

Input:
- An array arr of integers

Output:
- The maximum sum of any contiguous subarray
- The starting and ending indices of that subarray

### Divide and Conquer Approach

```
Step 1: Divide array into two halves
Step 2: Recursively find maximum subarray sum in left half
Step 3: Recursively find maximum subarray sum in right half
Step 4: Find maximum subarray sum that crosses the midpoint
Step 5: Return max of these three values
```

### Implementation (Divide and Conquer)

```cpp
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

struct Result {
    int sum;
    int left;
    int right;
};

Result maxCrossingSum(vector<int>& arr, int left, int mid, int right) {
    int leftSum = INT_MIN;
    int sum = 0;
    int maxLeft = mid;
    
    for (int i = mid; i >= left; i--) {
        sum += arr[i];
        if (sum > leftSum) {
            leftSum = sum;
            maxLeft = i;
        }
    }
    
    int rightSum = INT_MIN;
    sum = 0;
    int maxRight = mid + 1;
    
    for (int i = mid + 1; i <= right; i++) {
        sum += arr[i];
        if (sum > rightSum) {
            rightSum = sum;
            maxRight = i;
        }
    }
    
    return {leftSum + rightSum, maxLeft, maxRight};
}

Result maxSubarraySum(vector<int>& arr, int left, int right) {
    if (left == right) {
        return {arr[left], left, right};
    }
    
    int mid = left + (right - left) / 2;
    
    Result leftResult = maxSubarraySum(arr, left, mid);
    Result rightResult = maxSubarraySum(arr, mid + 1, right);
    Result crossResult = maxCrossingSum(arr, left, mid, right);
    
    if (leftResult.sum >= rightResult.sum && leftResult.sum >= crossResult.sum) {
        return leftResult;
    } else if (rightResult.sum >= leftResult.sum && rightResult.sum >= crossResult.sum) {
        return rightResult;
    } else {
        return crossResult;
    }
}

int main() {
    vector<int> arr = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    
    Result result = maxSubarraySum(arr, 0, arr.size() - 1);
    
    cout << "Maximum subarray sum: " << result.sum << endl;
    cout << "Subarray from index " << result.left << " to " << result.right << endl;
    
    return 0;
}
```

### Example Walkthrough (Divide and Conquer)

```
Array: [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Divide at mid = 4
Left:  [-2, 1, -3, 4, -1]
Right: [2, 1, -5, 4]

Recursively find:
Left best: sum = 4 (subarray [4])
Right best: sum = 6 (subarray [2, 1, 4]? Let's check)

Crossing sum:
Left part from mid to left: max ending at mid
    -1, -1+4=3, 3+(-3)=0, 0+1=1, 1+(-2)=-1 → max = 3 (from index 3 to 4)
Right part from mid+1 to right: max starting at mid+1
    2, 2+1=3, 3+(-5)=-2, -2+4=2 → max = 3 (from index 5 to 6)
Crossing sum = 3 + 3 = 6 (subarray [4, -1, 2, 1] = 4-1+2+1=6)

Maximum is 6
```

### Kadane's Algorithm (O(n) - For Reference)

```cpp
int kadane(vector<int>& arr) {
    int maxSoFar = arr[0];
    int maxEndingHere = arr[0];
    
    for (int i = 1; i < arr.size(); i++) {
        maxEndingHere = max(arr[i], maxEndingHere + arr[i]);
        maxSoFar = max(maxSoFar, maxEndingHere);
    }
    
    return maxSoFar;
}
```

### Visual Comparison

```
Array: [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Kadane's Algorithm:
i=0: maxEnding= -2, maxSoFar= -2
i=1: maxEnding= max(1, -2+1= -1) = 1, maxSoFar= max(-2,1)=1
i=2: maxEnding= max(-3, 1-3= -2) = -2, maxSoFar= max(1,-2)=1
i=3: maxEnding= max(4, -2+4=2) = 4, maxSoFar= max(1,4)=4
i=4: maxEnding= max(-1, 4-1=3) = 3, maxSoFar= max(4,3)=4
i=5: maxEnding= max(2, 3+2=5) = 5, maxSoFar= max(4,5)=5
i=6: maxEnding= max(1, 5+1=6) = 6, maxSoFar= max(5,6)=6
i=7: maxEnding= max(-5, 6-5=1) = 1, maxSoFar= max(6,1)=6
i=8: maxEnding= max(4, 1+4=5) = 5, maxSoFar= max(6,5)=6

Result: 6
```

### Time Complexity

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Brute Force | O(n³) | O(1) |
| Optimized Brute Force | O(n²) | O(1) |
| Divide and Conquer | O(n log n) | O(log n) |
| Kadane's Algorithm | O(n) | O(1) |

### Divide and Conquer vs Kadane

| Aspect | Divide and Conquer | Kadane |
|--------|--------------------|--------|
| Time | O(n log n) | O(n) |
| Complexity | More complex | Simple |
| Parallelizable | Yes | No |
| Teaching value | Demonstrates D&C | Practical use |

### Applications

| Application | Description |
|-------------|-------------|
| Stock market | Best time to buy and sell (maximum profit) |
| Signal processing | Find strongest signal segment |
| DNA sequencing | Find region with highest concentration |
| Image processing | Find brightest region |

### Practice Problems

1. Find maximum subarray sum in an array
2. Find maximum subarray sum in a circular array
3. Find maximum product subarray
4. Find maximum subarray sum with at least k elements
5. Find maximum subarray sum with at most k elements
6. Find two non-overlapping subarrays with maximum sum
---

## Next Step

- Go to [09_Karatsuba_Algorithm.md](09_Karatsuba_Algorithm.md) to continue with Karatsuba Algorithm.
