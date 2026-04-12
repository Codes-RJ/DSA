# 01_Introduction_to_Backtracking.md

## Introduction to Backtracking

### What is Backtracking?

Backtracking is a systematic way to try all possible combinations of choices to solve a problem. It builds a solution incrementally, one piece at a time, and removes (backtracks) choices that lead to dead ends.

The name comes from the idea of "backtracking" to a previous decision point when a path does not lead to a solution.

### Real-World Analogy

Imagine you are in a maze trying to find the exit:

```
Start → choice A → dead end → backtrack to start → choice B → exit found
```

At each junction, you choose a path. If you hit a dead end, you go back (backtrack) and try another path.

### Simple Example: Finding a Path in a Grid

**Problem:** Find a path from top-left to bottom-right in a grid, moving only right or down.

```
Grid: 2x2

(0,0) → (0,1) → (1,1) is one path
(0,0) → (1,0) → (1,1) is another path
```

**Backtracking Approach:**

```
Start at (0,0)

Try moving right → (0,1)
    Try moving down → (1,1) → reached target → solution found

Try moving down → (1,0)
    Try moving right → (1,1) → reached target → solution found
```

### Key Characteristics

| Characteristic | Description |
|----------------|-------------|
| Incremental | Builds solution step by step |
| Recursive | Uses recursion to explore choices |
| Pruning | Abandons invalid paths early |
| Undo | Reverts choices when backtracking |

### Steps of Backtracking

```
Step 1: CHOICE
        Make a decision at current step

Step 2: CHECK
        Verify if the current partial solution is still valid

Step 3: RECURSE
        If valid, continue to next step

Step 4: BACKTRACK
        If invalid or solution found, undo the choice and try another
```

### Visual Example: Generating All Subsets

**Problem:** Generate all subsets of {1, 2, 3}

```
Decision tree:

                    root
                    │
        ┌───────────┴───────────┐
       include 1               exclude 1
        │                        │
    ┌───┴───┐                ┌───┴───┐
  include2 exclude2        include2 exclude2
    │        │                │        │
  include3  include3        include3  include3

Resulting subsets:
include1,include2,include3 → {1,2,3}
include1,include2,exclude3 → {1,2}
include1,exclude2,include3 → {1,3}
include1,exclude2,exclude3 → {1}
exclude1,include2,include3 → {2,3}
exclude1,include2,exclude3 → {2}
exclude1,exclude2,include3 → {3}
exclude1,exclude2,exclude3 → {}
```

### Simple Implementation: Subset Generation

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
    
    // Choice 1: Exclude current element
    generateSubsets(nums, index + 1, current, result);
    
    // Choice 2: Include current element
    current.push_back(nums[index]);
    generateSubsets(nums, index + 1, current, result);
    
    // Backtrack: remove the element (undo choice)
    current.pop_back();
}

int main() {
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> result;
    vector<int> current;
    
    generateSubsets(nums, 0, current, result);
    
    cout << "All subsets:" << endl;
    for (auto& subset : result) {
        cout << "{ ";
        for (int num : subset) {
            cout << num << " ";
        }
        cout << "}" << endl;
    }
    
    return 0;
}
```

### Simple Example: Generate All Binary Strings of Length n

```cpp
void generateBinaryStrings(int n, string current, vector<string>& result) {
    if (current.length() == n) {
        result.push_back(current);
        return;
    }
    
    // Try '0'
    generateBinaryStrings(n, current + '0', result);
    
    // Try '1'
    generateBinaryStrings(n, current + '1', result);
}

// Usage: generateBinaryStrings(3, "", result)
// Result: 000, 001, 010, 011, 100, 101, 110, 111
```

### Advantages of Backtracking

| Advantage | Description |
|-----------|-------------|
| Systematic | Explores all possibilities methodically |
| Memory efficient | Only stores current path, not all solutions |
| Prunable | Can cut off invalid branches early |
| Versatile | Works for many combinatorial problems |

### Disadvantages

| Disadvantage | Description |
|--------------|-------------|
| Exponential time | Can be very slow for large n |
| Recursion depth | May cause stack overflow |
| No optimal guarantee | Finds all solutions, not necessarily optimal (unless optimized) |

### When to Use Backtracking

**Use backtracking when:**
- You need to find all (or some) solutions
- The problem has constraints that can be checked incrementally
- No polynomial-time algorithm exists
- The input size is small (typically n ≤ 20-30)

**Do NOT use backtracking when:**
- A polynomial solution exists (use that instead)
- Input size is large (n > 30)
- Only the optimal solution is needed (consider DP)
- The problem has overlapping subproblems (consider DP)

### Simple Problems to Start With

1. Generate all binary strings of length n
2. Generate all subsets of an array
3. Generate all permutations of an array
4. Find all paths in a grid
5. Solve a simple maze

### Template for Backtracking

```cpp
void backtrack(parameters) {
    // Base case
    if (isSolution()) {
        processSolution();
        return;
    }
    
    // Try all choices
    for (choice : possibleChoices) {
        if (isValid(choice)) {
            makeChoice(choice);
            backtrack(updatedParameters);
            undoChoice(choice);  // backtrack
        }
    }
}
```