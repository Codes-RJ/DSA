# 13_Combination_Sum.md

## Combination Sum

### Definition

Given an array of distinct integers and a target sum, find all unique combinations of numbers that sum to the target. Numbers can be used unlimited times (unbounded knapsack style).

### Problem Statement

Input:
- An array candidates of distinct integers
- A target integer

Output:
- All unique combinations where the sum of numbers equals target

### Visual Example

```
Input: candidates = [2, 3, 6, 7], target = 7

Output:
[2, 2, 3]
[7]
```

### Backtracking Approach

```
Step 1: Sort candidates (optional but helps with pruning)
Step 2: Start with empty combination
Step 3: At each step, try adding candidates starting from current index
Step 4: Subtract candidate from target
Step 5: If target becomes 0, record combination
Step 6: If target becomes negative, backtrack
Step 7: Allow reuse of same candidate (stay at same index)
```

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void combinationSum(vector<int>& candidates, int target, int start, 
                     vector<int>& current, vector<vector<int>>& result) {
    // Base case: found a combination
    if (target == 0) {
        result.push_back(current);
        return;
    }
    
    // Base case: target becomes negative
    if (target < 0) {
        return;
    }
    
    for (int i = start; i < candidates.size(); i++) {
        // Prune: if candidate exceeds target, break (since array is sorted)
        if (candidates[i] > target) {
            break;
        }
        
        // Make choice
        current.push_back(candidates[i]);
        
        // Recurse (note: i not i+1 because we can reuse same element)
        combinationSum(candidates, target - candidates[i], i, current, result);
        
        // Backtrack
        current.pop_back();
    }
}

vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    sort(candidates.begin(), candidates.end());
    vector<vector<int>> result;
    vector<int> current;
    combinationSum(candidates, target, 0, current, result);
    return result;
}

int main() {
    vector<int> candidates = {2, 3, 6, 7};
    int target = 7;
    
    vector<vector<int>> result = combinationSum(candidates, target);
    
    cout << "All combinations that sum to " << target << ":" << endl;
    for (auto& comb : result) {
        cout << "[ ";
        for (int num : comb) {
            cout << num << " ";
        }
        cout << "]" << endl;
    }
    
    return 0;
}
```

### Recursion Tree (candidates=[2,3,6,7], target=7)

```
                                    root (target=7)
                                    │
                ┌───────────────────┼───────────────────┐
                │                   │                   │
            -2 (5)               -3 (4)               -6 (1)
                │                   │                   │
        ┌───────┼───────┐       ┌───┼───┐               │
      -2 (3) -3 (2) -6 (-1)   -2 (2) -3 (1)           -2 (-1)
        │       │               │       │
      -2 (1)   -2 (0)         -2 (0)   -2 (-1)
        │       │               │
      -2 (-1)  [2,2,3]        [2,3,2]  (duplicate handled by start index)
        │
      [2,2,2,1] (no, target not 0)
```

### Example Walkthrough (Sorted)

```
candidates = [2, 3, 6, 7], target = 7

Start: current=[], target=7, start=0

i=0 (candidate=2):
    current=[2], target=5, start=0
    i=0: current=[2,2], target=3, start=0
        i=0: current=[2,2,2], target=1, start=0
            i=0: 2>1 → break
        i=1: current=[2,2,3], target=0 → record [2,2,3]
        i=2: 6>3 → break
    i=1: current=[2,3], target=2, start=1
        i=1: 3>2 → break (since sorted)
    i=2: 6>5 → break

i=1 (candidate=3):
    current=[3], target=4, start=1
    i=1: current=[3,3], target=1, start=1
        i=1: 3>1 → break
    i=2: 6>4 → break

i=2 (candidate=6):
    current=[6], target=1, start=2
    i=2: 6>1 → break

i=3 (candidate=7):
    current=[7], target=0 → record [7]

Result: [[2,2,3], [7]]
```

### Combination Sum II (No Reuse, No Duplicates)

Each number can be used only once, and candidates may contain duplicates.

```cpp
void combinationSum2(vector<int>& candidates, int target, int start, 
                      vector<int>& current, vector<vector<int>>& result) {
    if (target == 0) {
        result.push_back(current);
        return;
    }
    
    for (int i = start; i < candidates.size() && candidates[i] <= target; i++) {
        // Skip duplicates
        if (i > start && candidates[i] == candidates[i-1]) continue;
        
        current.push_back(candidates[i]);
        combinationSum2(candidates, target - candidates[i], i + 1, current, result);
        current.pop_back();
    }
}

vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    sort(candidates.begin(), candidates.end());
    vector<vector<int>> result;
    vector<int> current;
    combinationSum2(candidates, target, 0, current, result);
    return result;
}
```

### Combination Sum III (k numbers from 1-9)

Find all combinations of k numbers from 1 to 9 that sum to n.

```cpp
void combinationSum3(int k, int n, int start, vector<int>& current, 
                      vector<vector<int>>& result) {
    if (current.size() == k && n == 0) {
        result.push_back(current);
        return;
    }
    
    if (current.size() > k || n < 0) {
        return;
    }
    
    for (int i = start; i <= 9; i++) {
        current.push_back(i);
        combinationSum3(k, n - i, i + 1, current, result);
        current.pop_back();
    }
}

vector<vector<int>> combinationSum3(int k, int n) {
    vector<vector<int>> result;
    vector<int> current;
    combinationSum3(k, n, 1, current, result);
    return result;
}
```

### Combination Sum IV (Permutations)

Count the number of possible sequences that sum to target (order matters).

```cpp
int combinationSum4(vector<int>& nums, int target) {
    vector<unsigned int> dp(target + 1, 0);
    dp[0] = 1;
    
    for (int i = 1; i <= target; i++) {
        for (int num : nums) {
            if (i >= num) {
                dp[i] += dp[i - num];
            }
        }
    }
    
    return dp[target];
}
```

### Time Complexity

| Problem | Time Complexity |
|---------|-----------------|
| Combination Sum (unlimited) | O(2^(t/m)) where m is min candidate |
| Combination Sum II | O(2^n) |
| Combination Sum III | O(C(9, k)) |

### Space Complexity

O(k) for recursion stack + O(number of solutions × k) for storing results

### Variations Summary

| Variation | Reuse | Duplicates in Candidates | Order |
|-----------|-------|-------------------------|-------|
| Combination Sum | Yes | No | Doesn't matter |
| Combination Sum II | No | Yes | Doesn't matter |
| Combination Sum III | No (1-9 only) | No | Doesn't matter |
| Combination Sum IV | Yes | No | Matters (permutations) |

### Practice Problems

1. Find all combinations that sum to target (unlimited use)
2. Find all combinations that sum to target (each used once)
3. Find all combinations of k numbers from 1-9 that sum to n
4. Count number of combinations that sum to target (order matters)
5. Find all combinations that sum to target with a given length constraint
---

## Next Step

- Go to [14_Palindrome_Partitioning.md](14_Palindrome_Partitioning.md) to continue with Palindrome Partitioning.
