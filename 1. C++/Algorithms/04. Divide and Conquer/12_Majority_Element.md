# 12_Majority_Element.md

## Majority Element

### Definition

The majority element in an array is the element that appears more than ⌊n/2⌋ times (more than half the array). The problem guarantees that such an element exists.

### Problem Statement

Input:
- An array arr of size n

Output:
- The majority element (appears more than n/2 times)

### Divide and Conquer Approach

```
Step 1: Divide array into two halves
Step 2: Recursively find majority element in left half
Step 3: Recursively find majority element in right half
Step 4: If both halves agree on majority, return that element
Step 5: Otherwise, count occurrences of both candidates in the whole array
Step 6: Return the one that appears more than n/2 times
```

### Implementation

```cpp
#include <iostream>
#include <vector>
using namespace std;

int countOccurrences(vector<int>& arr, int left, int right, int target) {
    int count = 0;
    for (int i = left; i <= right; i++) {
        if (arr[i] == target) {
            count++;
        }
    }
    return count;
}

int majorityElementDC(vector<int>& arr, int left, int right) {
    // Base case: single element
    if (left == right) {
        return arr[left];
    }
    
    int mid = left + (right - left) / 2;
    
    int leftMajority = majorityElementDC(arr, left, mid);
    int rightMajority = majorityElementDC(arr, mid + 1, right);
    
    // If both halves agree
    if (leftMajority == rightMajority) {
        return leftMajority;
    }
    
    // Otherwise, count both candidates in the whole range
    int leftCount = countOccurrences(arr, left, right, leftMajority);
    int rightCount = countOccurrences(arr, left, right, rightMajority);
    
    return (leftCount > rightCount) ? leftMajority : rightMajority;
}

int main() {
    vector<int> arr = {2, 2, 1, 1, 1, 2, 2};
    
    int result = majorityElementDC(arr, 0, arr.size() - 1);
    
    cout << "Majority element: " << result << endl;
    
    return 0;
}
```

### Example Walkthrough

```
Array: [2, 2, 1, 1, 1, 2, 2]
n = 7, majority appears > 3.5 times (at least 4 times)

Divide:
[2, 2, 1] and [1, 1, 2, 2]

Left half [2, 2, 1]:
    Divide [2, 2] and [1]
    [2,2]: majority = 2
    [1]: majority = 1
    Count in [2,2,1]: 2 appears twice, 1 appears once → majority = 2

Right half [1, 1, 2, 2]:
    Divide [1,1] and [2,2]
    [1,1]: majority = 1
    [2,2]: majority = 2
    Count in [1,1,2,2]: 1 appears twice, 2 appears twice → tie
    But since array is guaranteed to have a majority overall, 
    the correct majority (2) will win when counting in full array

Full array counting:
    leftMajority = 2, rightMajority = 1
    Count 2 in full array: appears 4 times (indices 0,1,5,6)
    Count 1 in full array: appears 3 times (indices 2,3,4)
    Return 2
```

### Alternative: Moore's Voting Algorithm (O(n))

```cpp
int majorityElementMoore(vector<int>& arr) {
    int candidate = arr[0];
    int count = 1;
    
    for (int i = 1; i < arr.size(); i++) {
        if (count == 0) {
            candidate = arr[i];
            count = 1;
        } else if (arr[i] == candidate) {
            count++;
        } else {
            count--;
        }
    }
    
    // Verify candidate appears more than n/2 times
    int freq = 0;
    for (int num : arr) {
        if (num == candidate) freq++;
    }
    
    return (freq > arr.size() / 2) ? candidate : -1;
}
```

### Moore's Voting Visualization

```
Array: [2, 2, 1, 1, 1, 2, 2]

i=0: candidate=2, count=1
i=1: arr[1]=2 == candidate → count=2
i=2: arr[2]=1 != candidate → count=1
i=3: arr[3]=1 != candidate → count=0
i=4: count=0 → candidate=1, count=1
i=5: arr[5]=2 != candidate → count=0
i=6: count=0 → candidate=2, count=1

Candidate = 2
Verify: 2 appears 4 times > 3.5 → majority = 2
```

### Time Complexity

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Divide and Conquer | O(n log n) | O(log n) |
| Moore's Voting | O(n) | O(1) |
| Brute Force | O(n²) | O(1) |
| Hash Map | O(n) | O(n) |

### Comparison of Approaches

| Approach | Pros | Cons |
|----------|------|------|
| Divide and Conquer | Teaches recursion, parallelizable | O(n log n) time |
| Moore's Voting | O(n) time, O(1) space | Need verification pass |
| Hash Map | Simple to understand | O(n) extra space |

### Variations

#### 1. Majority Element II (more than ⌊n/3⌋ times)

```cpp
vector<int> majorityElementTwo(vector<int>& arr) {
    int candidate1 = 0, candidate2 = 0;
    int count1 = 0, count2 = 0;
    
    for (int num : arr) {
        if (num == candidate1) {
            count1++;
        } else if (num == candidate2) {
            count2++;
        } else if (count1 == 0) {
            candidate1 = num;
            count1 = 1;
        } else if (count2 == 0) {
            candidate2 = num;
            count2 = 1;
        } else {
            count1--;
            count2--;
        }
    }
    
    // Verify
    count1 = count2 = 0;
    for (int num : arr) {
        if (num == candidate1) count1++;
        else if (num == candidate2) count2++;
    }
    
    vector<int> result;
    if (count1 > arr.size() / 3) result.push_back(candidate1);
    if (count2 > arr.size() / 3) result.push_back(candidate2);
    
    return result;
}
```

#### 2. Check if Majority Element Exists

Moore's voting with verification pass.

#### 3. Majority Element in Sorted Array

Use binary search to find first and last occurrence.

### Applications

| Application | Description |
|-------------|-------------|
| Voting systems | Determine winner with majority |
| Data stream processing | Find frequent elements |
| Fault tolerance | Identify majority in distributed systems |

### Practice Problems

1. Find majority element (more than n/2 times)
2. Find elements appearing more than n/3 times
3. Find majority element in sorted array
4. Find majority element using bit manipulation
5. Find majority element in a stream
---

## Next Step

- Go to [13_Quick_Select.md](13_Quick_Select.md) to continue with Quick Select.
