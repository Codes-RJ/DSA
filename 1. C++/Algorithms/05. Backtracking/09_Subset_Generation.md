# 09_Subset_Generation.md

## Subset Generation

### Definition

Given an array of unique elements, generate all possible subsets (the power set). The power set contains 2^n subsets, including the empty set.

### Problem Statement

Input:
- An array nums of n unique elements

Output:
- All possible subsets of nums

### Visual Example

```
Input: nums = [1, 2, 3]

Output:
[]
[1]
[2]
[3]
[1,2]
[1,3]
[2,3]
[1,2,3]
```

### Backtracking Approach (Include/Exclude)

```
Step 1: Start with empty subset
Step 2: For each element, decide to include or exclude it
Step 3: After processing all elements, record the subset
```

### Implementation (Include/Exclude)

```cpp
#include <iostream>
#include <vector>
using namespace std;

void generateSubsets(vector<int>& nums, int index, vector<int>& current, vector<vector<int>>& result) {
    // Base case: processed all elements
    if (index == nums.size()) {
        result.push_back(current);
        return;
    }
    
    // Option 1: Exclude current element
    generateSubsets(nums, index + 1, current, result);
    
    // Option 2: Include current element
    current.push_back(nums[index]);
    generateSubsets(nums, index + 1, current, result);
    
    // Backtrack
    current.pop_back();
}

vector<vector<int>> subsets(vector<int>& nums) {
    vector<vector<int>> result;
    vector<int> current;
    generateSubsets(nums, 0, current, result);
    return result;
}

int main() {
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> result = subsets(nums);
    
    cout << "All subsets:" << endl;
    for (auto& subset : result) {
        cout << "[ ";
        for (int num : subset) {
            cout << num << " ";
        }
        cout << "]" << endl;
    }
    
    return 0;
}
```

### Recursion Tree for n=3

```
                              root
                              │
              ┌───────────────┴───────────────┐
          exclude 1                        include 1
              │                               │
      ┌───────┴───────┐               ┌───────┴───────┐
   exclude 2      include 2        exclude 2      include 2
      │               │               │               │
   ┌──┴──┐         ┌──┴──┐         ┌──┴──┐         ┌──┴──┐
  e3    i3       e3    i3       e3    i3       e3    i3
  │     │        │     │        │     │        │     │
 []    [3]      [2]   [2,3]    [1]   [1,3]    [1,2] [1,2,3]
```

### Implementation (Iterative - Pick/Not Pick)

```cpp
vector<vector<int>> subsetsIterative(vector<int>& nums) {
    vector<vector<int>> result = {{}};  // start with empty set
    
    for (int num : nums) {
        int size = result.size();
        for (int i = 0; i < size; i++) {
            vector<int> newSubset = result[i];
            newSubset.push_back(num);
            result.push_back(newSubset);
        }
    }
    
    return result;
}
```

### Implementation (Bitmask)

```cpp
vector<vector<int>> subsetsBitmask(vector<int>& nums) {
    int n = nums.size();
    vector<vector<int>> result;
    
    for (int mask = 0; mask < (1 << n); mask++) {
        vector<int> subset;
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) {
                subset.push_back(nums[i]);
            }
        }
        result.push_back(subset);
    }
    
    return result;
}
```

### Example Walkthrough (Iterative)

```
nums = [1, 2, 3]

Start: result = [[]]

Process num=1:
    size = 1
    i=0: [] + [1] = [1] → add to result
    result = [[], [1]]

Process num=2:
    size = 2
    i=0: [] + [2] = [2] → add
    i=1: [1] + [2] = [1,2] → add
    result = [[], [1], [2], [1,2]]

Process num=3:
    size = 4
    i=0: [] + [3] = [3] → add
    i=1: [1] + [3] = [1,3] → add
    i=2: [2] + [3] = [2,3] → add
    i=3: [1,2] + [3] = [1,2,3] → add
    result = [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
```

### Time Complexity

| Complexity | Value |
|------------|-------|
| Time | O(2^n) (each of 2^n subsets is generated) |
| Space | O(2^n) for storing all subsets |

### Subsets with Duplicates

If the array contains duplicates, we need to avoid generating duplicate subsets.

```cpp
void generateSubsetsWithDuplicates(vector<int>& nums, int index, vector<int>& current, 
                                     vector<vector<int>>& result) {
    result.push_back(current);
    
    for (int i = index; i < nums.size(); i++) {
        // Skip duplicates
        if (i > index && nums[i] == nums[i-1]) continue;
        
        current.push_back(nums[i]);
        generateSubsetsWithDuplicates(nums, i + 1, current, result);
        current.pop_back();
    }
}

vector<vector<int>> subsetsWithDup(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    vector<int> current;
    generateSubsetsWithDuplicates(nums, 0, current, result);
    return result;
}
```

### Number of Subsets

| n | Number of Subsets |
|---|-------------------|
| 0 | 1 |
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |
| 5 | 32 |
| 10 | 1024 |
| 20 | 1,048,576 |

### Variations

#### 1. Subsets of Size k (Combinations)

```cpp
void combinations(vector<int>& nums, int k, int start, vector<int>& current, 
                   vector<vector<int>>& result) {
    if (current.size() == k) {
        result.push_back(current);
        return;
    }
    
    for (int i = start; i < nums.size(); i++) {
        current.push_back(nums[i]);
        combinations(nums, k, i + 1, current, result);
        current.pop_back();
    }
}
```

#### 2. Subsets with Sum Target (Subset Sum)

```cpp
void subsetSum(vector<int>& nums, int target, int index, vector<int>& current, 
                vector<vector<int>>& result) {
    if (target == 0) {
        result.push_back(current);
        return;
    }
    
    for (int i = index; i < nums.size() && nums[i] <= target; i++) {
        current.push_back(nums[i]);
        subsetSum(nums, target - nums[i], i + 1, current, result);
        current.pop_back();
    }
}
```

#### 3. Subsets with Product Constraint

Similar to subset sum but with multiplication.

### Practice Problems

1. Generate all subsets of an array
2. Generate all subsets of size k
3. Generate all subsets with duplicates (unique subsets)
4. Generate all subsets that sum to a target
5. Generate all subsets in lexicographic order
---

## Next Step

- Go to [10_Permutation_Generation.md](10_Permutation_Generation.md) to continue with Permutation Generation.
