# README.md

## Backtracking - Complete Guide

### Overview

Backtracking is a systematic way to explore all possible configurations of a search space by building candidates incrementally and abandoning (backtracking from) a candidate as soon as it is determined that it cannot lead to a valid solution.

### Key Concepts

| Concept | Description |
|---------|-------------|
| State Space | All possible configurations of the problem |
| Decision Tree | Tree representing choices at each step |
| Pruning | Eliminating branches that cannot lead to solution |
| Backtrack | Undoing a choice to try another option |

### When to Use Backtracking

Backtracking is suitable when:

- The problem requires finding all (or some) solutions
- The solution space is large but has structure
- Constraints can be checked incrementally
- No polynomial-time algorithm is known (NP-complete problems)
- The problem involves permutations, combinations, or subsets

### Backtracking vs Other Paradigms

| Aspect | Backtracking | Divide and Conquer | Dynamic Programming | Greedy |
|--------|--------------|--------------------|---------------------|--------|
| Exploration | All possibilities | Divide only | Optimal substructure | Single path |
| State | Maintained | Independent | Overlapping | Current only |
| Optimality | Always (exhaustive) | Always | Always | Not guaranteed |
| Time complexity | Exponential | O(n log n) | Polynomial | Polynomial |
| Space complexity | O(depth) | O(log n) to O(n) | O(states) | O(1) |

### Complete Index

| # | Topic | File |
|---|-------|------|
| 1 | Introduction to Backtracking | `01_Introduction_to_Backtracking.md` |
| 2 | Recursive Backtracking | `02_Recursive_Backtracking.md` |
| 3 | Pruning Techniques | `03_Pruning_Techniques.md` |
| 4 | N-Queens Problem | `04_N_Queens.md` |
| 5 | Sudoku Solver | `05_Sudoku_Solver.md` |
| 6 | Rat in a Maze | `06_Rat_in_a_Maze.md` |
| 7 | Knight Tour | `07_Knight_Tour.md` |
| 8 | Generate Parentheses | `08_Generate_Parentheses.md` |
| 9 | Subset Generation | `09_Subset_Generation.md` |
| 10 | Permutation Generation | `10_Permutation_Generation.md` |
| 11 | Combination Generation | `11_Combination_Generation.md` |
| 12 | Word Search | `12_Word_Search.md` |
| 13 | Combination Sum | `13_Combination_Sum.md` |
| 14 | Palindrome Partitioning | `14_Palindrome_Partitioning.md` |
| 15 | M-Coloring Problem | `15_M_coloring_Problem.md` |
| 16 | Hamiltonian Cycle | `16_Hamiltonian_Cycle.md` |
| 17 | Tug of War | `17_Tug_of_War.md` |
| 18 | Crossword Puzzle | `18_Crossword_Puzzle.md` |
| 19 | Backtracking vs Brute Force | `19_Backtracking_vs_Brute_Force.md` |
| 20 | Backtracking vs DP | `20_Backtracking_vs_DP.md` |
| 21 | Problems | `Problems.md` |

### Classification by Problem Type

```
Backtracking Categories:

├── Combinatorial Generation
│   ├── Subsets
│   ├── Permutations
│   ├── Combinations
│   └── Generate Parentheses
│
├── Constraint Satisfaction
│   ├── N-Queens
│   ├── Sudoku
│   ├── M-Coloring
│   ├── Hamiltonian Cycle
│   └── Crossword Puzzle
│
├── Path Finding
│   ├── Rat in a Maze
│   ├── Knight Tour
│   └── Word Search
│
├── Partitioning Problems
│   ├── Palindrome Partitioning
│   ├── Tug of War
│   └── Subset Sum
│
└── Optimization
    ├── Combination Sum
    └── Tug of War (minimize difference)
```

### Time Complexity Reference

| Problem | Time Complexity | Space Complexity |
|---------|----------------|------------------|
| N-Queens | O(n!) | O(n²) |
| Sudoku | O(9^(n²)) | O(n²) |
| Rat in a Maze | O(2^(n²)) | O(n²) |
| Knight Tour | O(8^(n²)) | O(n²) |
| Generate Parentheses | O(4^n / √n) | O(n) |
| Subsets | O(2^n) | O(n) |
| Permutations | O(n!) | O(n) |
| Combinations | O(C(n,k)) | O(k) |
| Word Search | O(n * 3^L) | O(L) |
| Combination Sum | O(2^n) | O(n) |
| Palindrome Partitioning | O(n * 2^n) | O(n) |
| M-Coloring | O(k^n) | O(n) |
| Hamiltonian Cycle | O(n!) | O(n) |

### General Backtracking Template

```cpp
void backtrack(candidate, state) {
    if (isSolution(candidate)) {
        processSolution(candidate);
        return;
    }
    
    for (choice in possibleChoices) {
        if (isValid(choice, state)) {
            makeChoice(choice, state);
            backtrack(candidate + choice, newState);
            undoChoice(choice, state);
        }
    }
}
```

### Learning Path

```
Level 1: Basic Generation
├── Subset Generation
├── Permutation Generation
├── Combination Generation
└── Generate Parentheses

Level 2: Classical Problems
├── N-Queens
├── Rat in a Maze
├── Sudoku Solver
└── Word Search

Level 3: Advanced Problems
├── Combination Sum
├── Palindrome Partitioning
├── M-Coloring
├── Hamiltonian Cycle
└── Knight Tour

Level 4: Optimization
├── Pruning Techniques
├── Tug of War
├── Crossword Puzzle
└── Comparison with DP
```