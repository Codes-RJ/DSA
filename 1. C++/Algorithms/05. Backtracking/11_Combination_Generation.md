# 11_Combination_Generation.md

## Combination Generation

### Definition

Given n elements, generate all possible combinations of size k (where order does not matter). This is different from permutations where order matters.

### Problem Statement

Input:
- n (range 1 to n) or an array of elements
- k (size of combination)

Output:
- All possible combinations of k elements

### Visual Example (n=4, k=2)

```
Input: n=4, k=2 (elements 1,2,3,4)

Output:
[1,2]
[1,3]
[1,4]
[2,3]
[2,4]
[3,4]
```

### Backtracking Approach

```
Step 1: Start with empty combination
Step 2: For each possible next element (starting from current index)
Step 3: Add element to combination
Step 4: Recurse with next index (i+1 to avoid reuse and maintain order)
Step 5: When combination size equals k, record it
Step 6: Backtrack by removing element
```

### Implementation (Numbers 1 to n)

```cpp
#include <iostream>
#include <vector>
using namespace std;

void generateCombinations(int n, int k, int start, vector<int>& current, vector<vector<int>>& result) {
    // Base case: combination of size k found
    if (current.size() == k) {
        result.push_back(current);
        return;
    }
    
    // Try each possible next element
    for (int i = start; i <= n; i++) {
        current.push_back(i);
        generateCombinations(n, k, i + 1, current, result);
        current.pop_back();  // backtrack
    }
}

vector<vector<int>> combine(int n, int k) {
    vector<vector<int>> result;
    vector<int> current;
    generateCombinations(n, k, 1, current, result);
    return result;
}

int main() {
    int n = 4, k = 2;
    vector<vector<int>> result = combine(n, k);
    
    cout << "All combinations of " << k << " from 1 to " << n << ":" << endl;
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

### Implementation (Array of Elements)

```cpp
void generateCombinationsArray(vector<int>& nums, int k, int start, 
                                vector<int>& current, 
                                vector<vector<int>>& result) {
    if (current.size() == k) {
        result.push_back(current);
        return;
    }
    
    for (int i = start; i < nums.size(); i++) {
        current.push_back(nums[i]);
        generateCombinationsArray(nums, k, i + 1, current, result);
        current.pop_back();
    }
}

vector<vector<int>> combineArray(vector<int>& nums, int k) {
    vector<vector<int>> result;
    vector<int> current;
    generateCombinationsArray(nums, k, 0, current, result);
    return result;
}
```

### Recursion Tree (n=4, k=2)

```
                                    root
                                    │
                ┌───────────────────┼───────────────────┐
                │                   │                   │
               1                    2                    3
                │                   │                   │
        ┌───────┼───────┐    ┌───────┼───────┐    ┌───────┼───────┐
        │       │       │    │       │       │    │       │       │
       2       3       4    3       4       4    4       -       -
        │       │       │    │       │       │    │
      [1,2]   [1,3]   [1,4] [2,3]   [2,4]   [3,4] (stop at i=4)
```

### Example Walkthrough (n=4, k=2)

```
Start: current=[], start=1

i=1: add 1 → current=[1], recurse with start=2
    i=2: add 2 → current=[1,2], size=2 → record [1,2], backtrack remove 2
    i=3: add 3 → current=[1,3] → record [1,3], backtrack
    i=4: add 4 → current=[1,4] → record [1,4], backtrack
    backtrack remove 1

i=2: add 2 → current=[2], recurse with start=3
    i=3: add 3 → current=[2,3] → record [2,3], backtrack
    i=4: add 4 → current=[2,4] → record [2,4], backtrack
    backtrack remove 2

i=3: add 3 → current=[3], recurse with start=4
    i=4: add 4 → current=[3,4] → record [3,4], backtrack
    backtrack remove 3

i=4: add 4 → current=[4], recurse with start=5 (no more elements)
    (no combinations of size 2 possible)
```

### Number of Combinations

| n | k | Number of Combinations (C(n,k)) |
|---|---|-------------------------------|
| 5 | 2 | 10 |
| 5 | 3 | 10 |
| 6 | 3 | 20 |
| 10 | 3 | 120 |
| 10 | 5 | 252 |
| 20 | 10 | 184,756 |

### Time Complexity

| Complexity | Value |
|------------|-------|
| Time | O(C(n,k) * k) |
| Space | O(k) for recursion + O(C(n,k)*k) for storing combinations |

### Combinations with Duplicates (Subsets of Size k)

When array has duplicates, we need to avoid duplicate combinations.

```cpp
void combineWithDuplicates(vector<int>& nums, int k, int start, 
                            vector<int>& current, 
                            vector<vector<int>>& result) {
    if (current.size() == k) {
        result.push_back(current);
        return;
    }
    
    for (int i = start; i < nums.size(); i++) {
        // Skip duplicates
        if (i > start && nums[i] == nums[i-1]) continue;
        
        current.push_back(nums[i]);
        combineWithDuplicates(nums, k, i + 1, current, result);
        current.pop_back();
    }
}

vector<vector<int>> combineUnique(vector<int>& nums, int k) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    vector<int> current;
    combineWithDuplicates(nums, k, 0, current, result);
    return result;
}
```

### Optimization (Pruning)

We can prune branches that cannot reach size k:

```cpp
void generateCombinationsOptimized(int n, int k, int start, vector<int>& current, 
                                    vector<vector<int>>& result) {
    if (current.size() == k) {
        result.push_back(current);
        return;
    }
    
    // Prune: not enough elements left to reach size k
    for (int i = start; i <= n - (k - current.size()) + 1; i++) {
        current.push_back(i);
        generateCombinationsOptimized(n, k, i + 1, current, result);
        current.pop_back();
    }
}
```

### Variations

#### 1. Combinations with Repetition (Stars and Bars)

Allow elements to be repeated.

```cpp
void combineWithRepetition(int n, int k, int start, vector<int>& current, 
                            vector<vector<int>>& result) {
    if (current.size() == k) {
        result.push_back(current);
        return;
    }
    
    for (int i = start; i <= n; i++) {
        current.push_back(i);
        combineWithRepetition(n, k, i, current, result);  // note: i not i+1
        current.pop_back();
    }
}
```

#### 2. Combinations of Sum to Target (Combination Sum)

```cpp
void combinationSum(vector<int>& candidates, int target, int start, 
                     vector<int>& current, 
                     vector<vector<int>>& result) {
    if (target == 0) {
        result.push_back(current);
        return;
    }
    
    for (int i = start; i < candidates.size() && candidates[i] <= target; i++) {
        current.push_back(candidates[i]);
        combinationSum(candidates, target - candidates[i], i, current, result);
        current.pop_back();
    }
}
```

#### 3. Letter Combinations of a Phone Number

```cpp
vector<string> letterCombinations(string digits) {
    vector<string> mapping = {"", "", "abc", "def", "ghi", "jkl", 
                               "mno", "pqrs", "tuv", "wxyz"};
    vector<string> result;
    string current;
    
    function<void(int)> backtrack = [&](int index) {
        if (index == digits.length()) {
            if (!current.empty()) result.push_back(current);
            return;
        }
        
        string letters = mapping[digits[index] - '0'];
        for (char c : letters) {
            current.push_back(c);
            backtrack(index + 1);
            current.pop_back();
        }
    };
    
    backtrack(0);
    return result;
}
```

### Practice Problems

1. Generate all combinations of k numbers from 1 to n
2. Generate all combinations of size k from an array
3. Generate all combinations with duplicates (unique combinations)
4. Generate all combinations with repetition allowed
5. Generate all combinations that sum to a target (Combination Sum)