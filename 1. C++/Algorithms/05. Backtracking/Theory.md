# Theory.md

## Backtracking Theory

### Definition

Backtracking is a systematic search algorithm for solving constraint satisfaction problems. It builds candidates incrementally and abandons a candidate (backtracks) as soon as it determines that the candidate cannot possibly lead to a valid solution.

### Core Principles

| Principle | Description |
|-----------|-------------|
| Incremental Construction | Build solution piece by piece |
| Feasibility Check | Verify partial solution against constraints |
| Pruning | Eliminate branches that cannot lead to solution |
| Backtracking | Undo choices to explore alternatives |

### State Space Tree

The state space tree represents all possible configurations:

```
                    root
                    │
        ┌───────────┼───────────┐
        │           │           │
    choice1     choice2     choice3
        │           │           │
    ┌───┼───┐   ┌───┼───┐   ┌───┼───┐
    │   │   │   │   │   │   │   │   │
   ... ... ... ... ... ... ... ... ...
```

- Root: Empty configuration
- Each level: One decision
- Leaf: Complete solution or dead end
- Path from root to leaf: One candidate solution

### General Backtracking Algorithm

```
Algorithm Backtrack(candidate, depth):
    if isSolution(candidate):
        processSolution(candidate)
        return true (or false to continue searching)
    
    for each choice in possibleChoices:
        if isValid(candidate, choice):
            makeChoice(choice)
            result = Backtrack(candidate + choice, depth + 1)
            if result == true and we need only one solution:
                return true
            undoChoice(choice)  // backtrack
    
    return false
```

### Types of Backtracking

#### 1. Decision Problem

Find if a solution exists.

```cpp
bool solve(config) {
    if (isComplete(config)) return true;
    
    for (move in possibleMoves) {
        if (isValid(config, move)) {
            apply(move);
            if (solve(config)) return true;
            undo(move);
        }
    }
    return false;
}
```

#### 2. Optimization Problem

Find the best solution (minimum, maximum, etc.).

```cpp
void solve(config, currentCost) {
    if (isComplete(config)) {
        bestCost = min(bestCost, currentCost);
        return;
    }
    
    for (move in possibleMoves) {
        if (isValid(config, move)) {
            apply(move);
            solve(config, currentCost + cost(move));
            undo(move);
        }
    }
}
```

#### 3. Enumeration Problem

Find all solutions.

```cpp
void solve(config, solutions) {
    if (isComplete(config)) {
        solutions.push_back(config);
        return;
    }
    
    for (move in possibleMoves) {
        if (isValid(config, move)) {
            apply(move);
            solve(config, solutions);
            undo(move);
        }
    }
}
```

### Recursive Backtracking Structure

```cpp
void backtrack(vector<int>& state, int depth, vector<bool>& used) {
    // Base case: solution found
    if (depth == targetDepth) {
        process(state);
        return;
    }
    
    // Try all possibilities
    for (int i = 0; i < n; i++) {
        if (!used[i] && isValid(state, i)) {
            // Make choice
            used[i] = true;
            state.push_back(i);
            
            // Recurse
            backtrack(state, depth + 1, used);
            
            // Undo choice (backtrack)
            state.pop_back();
            used[i] = false;
        }
    }
}
```

### Pruning Techniques

Pruning is the key to making backtracking efficient.

| Technique | Description | Example |
|-----------|-------------|---------|
| Forward Checking | Check future constraints | Sudoku: check row, column, box |
| Constraint Propagation | Reduce domain of future variables | N-Queens: mark diagonals |
| Bound Pruning | Stop if cannot beat best solution | Tug of War: stop if difference too high |
| Symmetry Breaking | Skip symmetric configurations | N-Queens: start first queen in first half |
| Ordering Heuristics | Try most promising first | Knight Tour: Warnsdorff's rule |
| Memoization | Cache visited states | Avoid revisiting same state |

### Complexity Analysis

Backtracking complexity depends on:

- Number of choices at each level (branching factor)
- Depth of recursion
- Effectiveness of pruning

**Worst case:** O(b^d) where b = branching factor, d = depth

**With pruning:** Often much better in practice

### Backtracking vs Brute Force

| Aspect | Brute Force | Backtracking |
|--------|-------------|--------------|
| Approach | Generate all, then check | Generate and check incrementally |
| Memory | Stores all candidates | Stores only current path |
| Pruning | No pruning | Can prune invalid branches |
| Efficiency | Always exponential | Exponential but often faster |
| Implementation | Simpler | More complex |

### Backtracking vs DFS

| Aspect | DFS | Backtracking |
|--------|-----|--------------|
| Purpose | Traverse graph | Solve constraint problems |
| State | Node and visited set | Partial solution |
| Backtrack | Not needed | Explicit undo |
| Use case | Graph traversal | Combinatorial search |

### Backtracking vs DP

| Aspect | Backtracking | DP |
|--------|--------------|-----|
| Subproblems | Overlapping possible | Must overlap |
| Memoization | Optional | Essential |
| Optimality | Finds all solutions | Finds optimal |
| Time | Exponential | Polynomial |
| Space | O(depth) | O(states) |

### When Backtracking is Appropriate

**Good candidates:**
- Constraint satisfaction problems
- Problems requiring all solutions
- NP-complete problems (small n)
- Puzzles (Sudoku, N-Queens)
- Combinatorial generation

**Poor candidates:**
- Problems with optimal substructure (use DP)
- Large input size (n > 30)
- Problems with polynomial solution
- Problems where greedy works

### Common Backtracking Problems

| Problem | Branching Factor | Depth | Pruning |
|---------|-----------------|-------|---------|
| N-Queens | n | n | Row, column, diagonal |
| Sudoku | 9 | n² | Row, column, box |
| Permutations | n | n | Used array |
| Subsets | 2 | n | Include/exclude |
| Knight Tour | 8 | n² | Visited squares |
| Hamiltonian Cycle | n | n | Visited vertices |

### Optimization Techniques

1. **Order of choices:** Try most constrained first
2. **Forward checking:** Check future constraints early
3. **Constraint propagation:** Reduce domains
4. **Memoization:** Cache results of subproblems
5. **Heuristics:** Use domain knowledge
6. **Iterative deepening:** Depth-limited DFS
7. **Parallelization:** Explore branches in parallel

### Practice Problems for Theory

1. Draw state space tree for generating all subsets of {a,b,c}
2. Draw state space tree for N-Queens (n=4)
3. Analyze branching factor for Sudoku
4. Explain how pruning works in N-Queens
5. Compare backtracking and DP for subset sum problem
---

## Next Step

- Go to [README.md](README.md) to continue.
