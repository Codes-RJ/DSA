# 17_Tug_of_War.md

## Tug of War

### Definition

Given a set of numbers (weights of people), divide them into two groups of equal size (or as close as possible) such that the difference between the sums of the two groups is minimized.

### Problem Statement

Input:
- An array of integers (weights)
- n = size of array (even for equal division, can handle odd)

Output:
- Two subsets of equal size (floor(n/2) and ceil(n/2)) with minimum sum difference

### Visual Example

```
Input: [3, 4, 5, -3, 100, 1, 89, 54, 23, 20]

Output: Two groups of 5 elements each with sums as close as possible
```

### Backtracking Approach

```
Step 1: Total sum = sum of all elements
Step 2: Target sum = total_sum / 2 (approximately)
Step 3: Find subset of size n/2 with sum closest to target
Step 4: Use backtracking to generate subsets of size n/2
Step 5: Track the best difference found
```

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <climits>
using namespace std;

int bestDiff = INT_MAX;
vector<int> bestSubset;
int totalSum = 0;

void tugOfWar(vector<int>& nums, int index, int count, int currentSum, 
               vector<int>& current, int n) {
    int half = n / 2;
    
    // Pruning: if we have selected more than half, backtrack
    if (count > half) return;
    
    // Pruning: if remaining elements can't reach half, backtrack
    if (count + (n - index) < half) return;
    
    // Base case: we have selected exactly half elements
    if (count == half) {
        int diff = abs(totalSum - 2 * currentSum);
        if (diff < bestDiff) {
            bestDiff = diff;
            bestSubset = current;
        }
        return;
    }
    
    // Base case: reached end of array
    if (index == n) return;
    
    // Option 1: Include current element
    current.push_back(nums[index]);
    tugOfWar(nums, index + 1, count + 1, currentSum + nums[index], current, n);
    current.pop_back();
    
    // Option 2: Exclude current element
    tugOfWar(nums, index + 1, count, currentSum, current, n);
}

void solveTugOfWar(vector<int>& nums) {
    int n = nums.size();
    totalSum = 0;
    for (int num : nums) {
        totalSum += num;
    }
    
    bestDiff = INT_MAX;
    bestSubset.clear();
    vector<int> current;
    
    tugOfWar(nums, 0, 0, 0, current, n);
    
    // Calculate sums of both groups
    int sum1 = 0;
    for (int num : bestSubset) {
        sum1 += num;
    }
    int sum2 = totalSum - sum1;
    
    cout << "Group 1: ";
    for (int num : bestSubset) {
        cout << num << " ";
    }
    cout << "(sum = " << sum1 << ")" << endl;
    
    cout << "Group 2: ";
    for (int num : nums) {
        bool inSubset = false;
        for (int x : bestSubset) {
            if (x == num) {
                inSubset = true;
                break;
            }
        }
        if (!inSubset) {
            cout << num << " ";
        }
    }
    cout << "(sum = " << sum2 << ")" << endl;
    
    cout << "Difference: " << bestDiff << endl;
}

int main() {
    vector<int> nums = {3, 4, 5, -3, 100, 1, 89, 54, 23, 20};
    solveTugOfWar(nums);
    
    return 0;
}
```

### Optimized Implementation with Pruning

```cpp
int bestDiff = INT_MAX;
vector<int> bestSubset;
int totalSum = 0;

void tugOfWarOptimized(vector<int>& nums, int index, int count, int currentSum, 
                        vector<int>& current, int n) {
    int half = n / 2;
    
    // Prune if already worse than best
    int remainingSum = totalSum - currentSum;
    int currentDiff = abs(remainingSum - currentSum);
    if (currentDiff >= bestDiff) return;
    
    // Prune if count exceeds half
    if (count > half) return;
    
    // Prune if not enough elements left
    if (count + (n - index) < half) return;
    
    if (count == half) {
        int diff = abs(totalSum - 2 * currentSum);
        if (diff < bestDiff) {
            bestDiff = diff;
            bestSubset = current;
        }
        return;
    }
    
    if (index == n) return;
    
    // Try including current element
    current.push_back(nums[index]);
    tugOfWarOptimized(nums, index + 1, count + 1, currentSum + nums[index], current, n);
    current.pop_back();
    
    // Try excluding current element
    tugOfWarOptimized(nums, index + 1, count, currentSum, current, n);
}
```

### Dynamic Programming Approach (For Smaller n)

When n is small, DP can also solve this.

```cpp
bool canPartition(vector<int>& nums, int half, int targetSum) {
    // DP to check if we can achieve targetSum with exactly half elements
    vector<vector<bool>> dp(half + 1, vector<bool>(targetSum + 1, false));
    dp[0][0] = true;
    
    for (int num : nums) {
        for (int i = half; i >= 1; i--) {
            for (int s = targetSum; s >= num; s--) {
                if (dp[i-1][s-num]) {
                    dp[i][s] = true;
                }
            }
        }
    }
    
    for (int s = targetSum; s >= 0; s--) {
        if (dp[half][s]) {
            return s;
        }
    }
    return 0;
}
```

### Example Walkthrough

```
nums = [1, 2, 3, 4], n=4, half=2, totalSum=10

Generate subsets of size 2:

Subset [1,2]: sum=3, diff=|10-6|=4
Subset [1,3]: sum=4, diff=|10-8|=2
Subset [1,4]: sum=5, diff=|10-10|=0 → best
Subset [2,3]: sum=5, diff=0
Subset [2,4]: sum=6, diff=2
Subset [3,4]: sum=7, diff=4

Best: [1,4] or [2,3] with difference 0
Groups: [1,4] and [2,3] both sum to 5
```

### For Odd n

When n is odd, one group will have floor(n/2) elements, the other ceil(n/2).

```cpp
void tugOfWarOdd(vector<int>& nums) {
    int n = nums.size();
    int half = n / 2;  // floor division
    // One group has half elements, other has n-half elements
    // Rest of the algorithm is the same
}
```

### Time Complexity

| Complexity | Value |
|------------|-------|
| Without pruning | O(2^n) |
| With pruning | Much better in practice |

### Space Complexity

O(n) for recursion stack + O(n) for storing best subset

### Variations

#### 1. Partition into Two Subsets with Equal Sum (Not Size Constraint)

Classic partition problem (can use DP).

#### 2. Partition into K Equal Sum Subsets

More general version of the problem.

#### 3. Minimum Difference Partition (No Size Constraint)

Any size allowed, just minimize sum difference.

### Practice Problems

1. Divide array into two groups of equal size with minimum sum difference
2. Partition array into two subsets with equal sum (any size)
3. Partition array into k subsets with equal sum
4. Divide players into two teams of equal size with minimum strength difference
5. Partition array into two subsets with minimum product difference