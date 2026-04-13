# 02_Recursive_Backtracking.md

## Recursive Backtracking

### Definition

Recursive backtracking is the most common implementation of backtracking. It uses recursion to explore the decision tree, making a choice, recursing, and then undoing that choice to try alternatives.

### Why Recursion?

Recursion naturally models the decision tree:

- Each recursive call represents moving one level deeper in the tree
- The call stack automatically tracks the path
- Returning from a function automatically backtracks

### Basic Structure

```cpp
void backtrack(State& state, int depth) {
    // Base case: reached a leaf (complete solution)
    if (depth == maxDepth || isComplete(state)) {
        processSolution(state);
        return;
    }
    
    // Try all possible choices at this level
    for (Choice choice : getChoices(state, depth)) {
        if (isValid(state, choice)) {
            // Make the choice
            applyChoice(state, choice);
            
            // Recurse to next level
            backtrack(state, depth + 1);
            
            // Undo the choice (backtrack)
            undoChoice(state, choice);
        }
    }
}
```

### Visualizing Recursion

```
backtrack(empty, depth=0)
    │
    ├── choice A
    │       │
    │       backtrack(partial A, depth=1)
    │           │
    │           ├── choice A1 → solution found
    │           │
    │           └── choice A2 → dead end (backtrack)
    │
    └── choice B
            │
            backtrack(partial B, depth=1)
                │
                └── choice B1 → solution found
```

### Example 1: Generate All Permutations

```cpp
#include <iostream>
#include <vector>
using namespace std;

void generatePermutations(vector<int>& nums, vector<bool>& used, vector<int>& current, vector<vector<int>>& result) {
    // Base case: all numbers are used
    if (current.size() == nums.size()) {
        result.push_back(current);
        return;
    }
    
    // Try each unused number
    for (int i = 0; i < nums.size(); i++) {
        if (!used[i]) {
            // Make choice
            used[i] = true;
            current.push_back(nums[i]);
            
            // Recurse
            generatePermutations(nums, used, current, result);
            
            // Backtrack (undo choice)
            current.pop_back();
            used[i] = false;
        }
    }
}

int main() {
    vector<int> nums = {1, 2, 3};
    vector<bool> used(nums.size(), false);
    vector<int> current;
    vector<vector<int>> result;
    
    generatePermutations(nums, used, current, result);
    
    cout << "All permutations:" << endl;
    for (auto& perm : result) {
        cout << "{ ";
        for (int num : perm) {
            cout << num << " ";
        }
        cout << "}" << endl;
    }
    
    return 0;
}
```

### Recursion Trace for Permutations (n=3)

```
backtrack([], depth=0)
│
├── i=0: used[0]=true, current=[1]
│   │
│   ├── backtrack([1], depth=1)
│   │   ├── i=1: used[1]=true, current=[1,2]
│   │   │   └── backtrack([1,2], depth=2)
│   │   │       └── i=2: used[2]=true, current=[1,2,3]
│   │   │           └── backtrack([1,2,3], depth=3) → solution found
│   │   └── i=2: used[2]=true, current=[1,3]
│   │       └── backtrack([1,3], depth=2)
│   │           └── i=1: used[1]=true, current=[1,3,2] → solution found
│   │
│   └── undo: used[0]=false, current=[]
│
├── i=1: used[1]=true, current=[2]
│   │
│   ├── backtrack([2], depth=1)
│   │   ├── i=0: used[0]=true, current=[2,1]
│   │   │   └── backtrack([2,1], depth=2)
│   │   │       └── i=2: used[2]=true, current=[2,1,3] → solution found
│   │   └── i=2: used[2]=true, current=[2,3]
│   │       └── backtrack([2,3], depth=2)
│   │           └── i=0: used[0]=true, current=[2,3,1] → solution found
│   │
│   └── undo: used[1]=false, current=[]
│
└── i=2: used[2]=true, current=[3]
    │
    ├── backtrack([3], depth=1)
    │   ├── i=0: used[0]=true, current=[3,1]
    │   │   └── backtrack([3,1], depth=2)
    │   │       └── i=1: used[1]=true, current=[3,1,2] → solution found
    │   └── i=1: used[1]=true, current=[3,2]
    │       └── backtrack([3,2], depth=2)
    │           └── i=0: used[0]=true, current=[3,2,1] → solution found
    │
    └── undo: used[2]=false, current=[]
```

### Example 2: Generate All Combinations (n choose k)

```cpp
void generateCombinations(int n, int k, int start, vector<int>& current, vector<vector<int>>& result) {
    // Base case: combination of size k found
    if (current.size() == k) {
        result.push_back(current);
        return;
    }
    
    // Try each possible next element
    for (int i = start; i <= n; i++) {
        // Make choice
        current.push_back(i);
        
        // Recurse with next start (i+1 ensures no duplicates)
        generateCombinations(n, k, i + 1, current, result);
        
        // Backtrack
        current.pop_back();
    }
}
```

### Example 3: Generate All Subsets (Power Set)

```cpp
void generateSubsets(vector<int>& nums, int index, vector<int>& current, vector<vector<int>>& result) {
    // Each recursive call represents a subset (including empty)
    result.push_back(current);
    
    // Try adding each remaining element
    for (int i = index; i < nums.size(); i++) {
        // Make choice
        current.push_back(nums[i]);
        
        // Recurse
        generateSubsets(nums, i + 1, current, result);
        
        // Backtrack
        current.pop_back();
    }
}
```

### Recursion Depth Considerations

| Problem | Max Depth | Stack Usage |
|---------|-----------|-------------|
| Subsets (n=20) | 20 | Very low |
| Permutations (n=10) | 10 | Low |
| N-Queens (n=20) | 20 | Low |
| Knight Tour (64 squares) | 64 | Moderate |
| Sudoku (81 cells) | 81 | Moderate |

### Common Mistakes

1. **Forgetting to backtrack** - Not undoing changes leads to incorrect results
2. **Incorrect base case** - Missing or wrong termination condition
3. **Not copying state** - Modifying shared state incorrectly
4. **Infinite recursion** - No progress toward base case
5. **Too deep recursion** - Stack overflow for large depth

### Backtracking vs Regular Recursion

| Aspect | Regular Recursion | Backtracking |
|--------|-------------------|--------------|
| Purpose | Compute value | Explore choices |
| State modification | Usually immutable | Mutable (needs undo) |
| Multiple solutions | Single return value | Multiple solutions collected |
| Undo step | Not needed | Required |

### Practice Problems

1. Generate all permutations of a string
2. Generate all combinations of size k from 1 to n
3. Generate all subsets of an array
4. Generate all binary strings of length n with no consecutive 1s
5. Generate all ways to climb n stairs using steps 1, 2, or 3
---

## Next Step

- Go to [03_Pruning_Techniques.md](03_Pruning_Techniques.md) to continue with Pruning Techniques.
