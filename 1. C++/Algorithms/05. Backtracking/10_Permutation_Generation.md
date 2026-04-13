# 10_Permutation_Generation.md

## Permutation Generation

### Definition

Given an array of elements, generate all possible permutations (arrangements). For n distinct elements, there are n! permutations.

### Problem Statement

Input:
- An array nums of n elements (may have duplicates or be unique)

Output:
- All possible permutations of nums

### Visual Example (n=3)

```
Input: nums = [1, 2, 3]

Output:
[1,2,3]
[1,3,2]
[2,1,3]
[2,3,1]
[3,1,2]
[3,2,1]
```

### Backtracking Approach (Using Visited Array)

```
Step 1: Start with empty permutation
Step 2: Keep track of used elements
Step 3: For each unused element, add it to current permutation
Step 4: Recurse
Step 5: When permutation size equals n, record it
Step 6: Backtrack by removing element and marking as unused
```

### Implementation (Distinct Elements)

```cpp
#include <iostream>
#include <vector>
using namespace std;

void generatePermutations(vector<int>& nums, vector<bool>& used, vector<int>& current, 
                           vector<vector<int>>& result) {
    // Base case: all elements used
    if (current.size() == nums.size()) {
        result.push_back(current);
        return;
    }
    
    for (int i = 0; i < nums.size(); i++) {
        if (!used[i]) {
            // Make choice
            used[i] = true;
            current.push_back(nums[i]);
            
            // Recurse
            generatePermutations(nums, used, current, result);
            
            // Backtrack
            current.pop_back();
            used[i] = false;
        }
    }
}

vector<vector<int>> permute(vector<int>& nums) {
    vector<vector<int>> result;
    vector<int> current;
    vector<bool> used(nums.size(), false);
    generatePermutations(nums, used, current, result);
    return result;
}

int main() {
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> result = permute(nums);
    
    cout << "All permutations:" << endl;
    for (auto& perm : result) {
        cout << "[ ";
        for (int num : perm) {
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
                ┌───────────────────┼───────────────────┐
                │                   │                   │
               1                    2                    3
                │                   │                   │
        ┌───────┴───────┐    ┌───────┴───────┐    ┌───────┴───────┐
        │               │    │               │    │               │
       2               3    1               3    1               2
        │               │    │               │    │               │
        │               │    │               │    │               │
       3               2    3               1    2               1
        │               │    │               │    │               │
      [1,2,3]        [1,3,2] [2,1,3]     [2,3,1] [3,1,2]     [3,2,1]
```

### Implementation (Swap Method - In-place)

```cpp
void generatePermutationsSwap(vector<int>& nums, int index, vector<vector<int>>& result) {
    if (index == nums.size()) {
        result.push_back(nums);
        return;
    }
    
    for (int i = index; i < nums.size(); i++) {
        swap(nums[index], nums[i]);
        generatePermutationsSwap(nums, index + 1, result);
        swap(nums[index], nums[i]);  // backtrack
    }
}

vector<vector<int>> permuteSwap(vector<int>& nums) {
    vector<vector<int>> result;
    generatePermutationsSwap(nums, 0, result);
    return result;
}
```

### Example Walkthrough (Swap Method)

```
nums = [1, 2, 3], index=0

i=0: swap(0,0) → [1,2,3]
    index=1
    i=1: swap(1,1) → [1,2,3]
        index=2
        i=2: swap(2,2) → [1,2,3] → record [1,2,3]
    i=2: swap(1,2) → [1,3,2]
        index=2 → record [1,3,2]
    swap back → [1,2,3]

i=1: swap(0,1) → [2,1,3]
    index=1
    i=1: swap(1,1) → [2,1,3] → record [2,1,3]
    i=2: swap(1,2) → [2,3,1] → record [2,3,1]
    swap back → [2,1,3]
swap back → [1,2,3]

i=2: swap(0,2) → [3,2,1]
    index=1
    i=1: swap(1,1) → [3,2,1] → record [3,2,1]
    i=2: swap(1,2) → [3,1,2] → record [3,1,2]
    swap back → [3,2,1]
swap back → [1,2,3]
```

### Permutations with Duplicates

When array has duplicates, we need to avoid generating duplicate permutations.

```cpp
void generatePermutationsWithDuplicates(vector<int>& nums, vector<bool>& used, 
                                         vector<int>& current, 
                                         vector<vector<int>>& result) {
    if (current.size() == nums.size()) {
        result.push_back(current);
        return;
    }
    
    for (int i = 0; i < nums.size(); i++) {
        // Skip used elements
        if (used[i]) continue;
        
        // Skip duplicates: if same as previous and previous not used
        if (i > 0 && nums[i] == nums[i-1] && !used[i-1]) continue;
        
        used[i] = true;
        current.push_back(nums[i]);
        generatePermutationsWithDuplicates(nums, used, current, result);
        current.pop_back();
        used[i] = false;
    }
}

vector<vector<int>> permuteUnique(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    vector<int> current;
    vector<bool> used(nums.size(), false);
    generatePermutationsWithDuplicates(nums, used, current, result);
    return result;
}
```

### Number of Permutations

| n | Number of Permutations |
|---|----------------------|
| 1 | 1 |
| 2 | 2 |
| 3 | 6 |
| 4 | 24 |
| 5 | 120 |
| 6 | 720 |
| 7 | 5,040 |
| 8 | 40,320 |
| 9 | 362,880 |
| 10 | 3,628,800 |

### Time Complexity

| Complexity | Value |
|------------|-------|
| Time | O(n!) |
| Space | O(n) for recursion + O(n!) for storing permutations |

### Variations

#### 1. Permutations of a String

Same logic as array.

```cpp
void permuteString(string s, int index, vector<string>& result) {
    if (index == s.length()) {
        result.push_back(s);
        return;
    }
    
    for (int i = index; i < s.length(); i++) {
        swap(s[index], s[i]);
        permuteString(s, index + 1, result);
        swap(s[index], s[i]);
    }
}
```

#### 2. Permutations of Size k (k-permutations)

```cpp
void generateKPermutations(vector<int>& nums, vector<bool>& used, 
                            vector<int>& current, int k, 
                            vector<vector<int>>& result) {
    if (current.size() == k) {
        result.push_back(current);
        return;
    }
    
    for (int i = 0; i < nums.size(); i++) {
        if (!used[i]) {
            used[i] = true;
            current.push_back(nums[i]);
            generateKPermutations(nums, used, current, k, result);
            current.pop_back();
            used[i] = false;
        }
    }
}
```

#### 3. Next Permutation (Lexicographic Order)

Find the next permutation in lexicographic order (without generating all).

```cpp
void nextPermutation(vector<int>& nums) {
    int n = nums.size();
    int i = n - 2;
    
    // Find first decreasing element from right
    while (i >= 0 && nums[i] >= nums[i+1]) {
        i--;
    }
    
    if (i >= 0) {
        int j = n - 1;
        while (nums[j] <= nums[i]) {
            j--;
        }
        swap(nums[i], nums[j]);
    }
    
    // Reverse the suffix
    reverse(nums.begin() + i + 1, nums.end());
}
```

### Practice Problems

1. Generate all permutations of an array of distinct integers
2. Generate all permutations of a string
3. Generate all unique permutations of an array with duplicates
4. Generate all permutations of size k
5. Find the next permutation in lexicographic order
---

## Next Step

- Go to [11_Combination_Generation.md](11_Combination_Generation.md) to continue with Combination Generation.
