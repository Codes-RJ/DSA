# 19_Backtracking_vs_Brute_Force.md

## Backtracking vs Brute Force

### Definition

Brute force generates all possible candidates and checks each one for validity. Backtracking generates candidates incrementally and prunes invalid branches early.

### Key Differences

| Aspect | Brute Force | Backtracking |
|--------|-------------|--------------|
| Generation | All candidates first | Incremental |
| Pruning | No pruning | Prunes invalid branches |
| Memory | Stores all candidates | Stores only current path |
| Efficiency | Always O(total candidates) | Often much faster |
| Implementation | Simpler | More complex |

### Visual Comparison

```
Brute Force (All permutations of 1,2,3):
[1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]
Generate ALL → then filter

Backtracking (Same problem):
Start with []
  → add 1 → [1] → add 2 → [1,2] → add 3 → [1,2,3] → record
                → remove 3, add 3? already tried
        → remove 2, add 3 → [1,3] → add 2 → [1,3,2] → record
  → add 2 → [2] → ...
Prunes nothing because all permutations are valid
```

### Example: N-Queens (n=8)

| Approach | Operations | Time |
|----------|-----------|------|
| Brute Force | 64 choose 8 ≈ 4.4 billion | Too long |
| Backtracking | ~15,000 placements | < 1 second |

### Example: Subset Sum (n=20)

| Approach | Operations | Time |
|----------|-----------|------|
| Brute Force | 2^20 = 1,048,576 | Moderate |
| Backtracking with pruning | Much less | Fast |

### Example: Sudoku

| Approach | Operations | Time |
|----------|-----------|------|
| Brute Force | 9^81 (huge) | Impossible |
| Backtracking | ~10^4 typical | Milliseconds |

### When Brute Force is Acceptable

| Scenario | Example |
|----------|---------|
| Very small n (n ≤ 10) | Permutations of 5 items |
| All candidates needed | Testing all possible passwords of length 4 |
| No pruning possible | All subsets (need all) |
| Simple check | Finding maximum in array |

### When Backtracking is Better

| Scenario | Example |
|----------|---------|
| Large search space | N-Queens n=20 |
| Early pruning possible | Sudoku, graph coloring |
| Constraints are tight | Crossword puzzle |
| One solution sufficient | Hamiltonian cycle |

### Brute Force Implementation (Subset Sum)

```cpp
bool bruteForceSubsetSum(vector<int>& nums, int target) {
    int n = nums.size();
    
    // Generate all 2^n subsets
    for (int mask = 0; mask < (1 << n); mask++) {
        int sum = 0;
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) {
                sum += nums[i];
            }
        }
        if (sum == target) return true;
    }
    return false;
}
```

### Backtracking Implementation (Subset Sum)

```cpp
bool backtrackSubsetSum(vector<int>& nums, int index, int target) {
    if (target == 0) return true;
    if (index == nums.size() || target < 0) return false;
    
    // Include current
    if (backtrackSubsetSum(nums, index + 1, target - nums[index])) {
        return true;
    }
    
    // Exclude current
    return backtrackSubsetSum(nums, index + 1, target);
}
```

### Performance Comparison Table

| Problem | n | Brute Force | Backtracking | Speedup |
|---------|---|-------------|--------------|---------|
| N-Queens | 12 | 12! = 479M | ~3M | 160x |
| Sudoku | 81 | 9^81 | ~10^4 | Massive |
| Subset Sum | 30 | 1B | ~1M | 1000x |
| Graph Coloring | 10, 3 colors | 3^10 = 59K | ~10K | 6x |
| Permutations | 10 | 3.6M | 3.6M | 1x |

### Memory Comparison

| Approach | Memory Usage |
|----------|--------------|
| Brute Force (store all) | O(total candidates × size) |
| Brute Force (generate on fly) | O(size) |
| Backtracking | O(depth) |

### Implementation Complexity

```cpp
// Brute Force (simpler)
for each candidate:
    if isValid(candidate):
        process(candidate)

// Backtracking (more complex)
void backtrack(state):
    if isComplete(state):
        process(state)
        return
    for each choice:
        if isValid(state, choice):
            makeChoice(state, choice)
            backtrack(state)
            undoChoice(state, choice)
```

### When to Choose Which

**Choose Brute Force when:**
- Input size is very small (n ≤ 10)
- All solutions are needed
- Validation is very cheap
- Problem has no structure to prune

**Choose Backtracking when:**
- Input size is moderate (10 ≤ n ≤ 30)
- Constraints allow early pruning
- Only one (or few) solutions needed
- Problem has natural recursive structure

### Hybrid Approaches

Sometimes combine both:

```cpp
// Use brute force for small subproblems
if (n <= 10) {
    return bruteForce(nums);
} else {
    return backtrack(nums);
}
```

### Practice Problems

1. Implement both brute force and backtracking for subset sum
2. Compare performance for n=20, target=50
3. Implement both for generating all permutations of n elements
4. Compare performance for n=10
5. Determine when brute force is better than backtracking