# Array Puzzles

## Introduction
Array-based puzzles require rearranging, selecting, or processing array elements in non-trivial ways, often without extra memory.

## 1. 2D Array Spiralling (Spiral Print)
**Question**: Print a matrix in a spiral order starting from top-left.
- **Solution**: Use four boundaries (top, bottom, left, right) and update them as you finish a row or column.

## 2. Rain Water Trapping
**Question**: Given heights of bars, calculate the total trapped water after raining.
- **Solution**: Use two-pointers or prefix-max and suffix-max arrays.
- `water_at_i = min(max_left_i, max_right_i) - height_i`.

## 3. Median of Two Sorted Arrays
- **Brute** : Merge and find (O(N+M)).
- **Optimized**: Binary search on partitions (O(log(min(N,M)))).

## 4. N-Queens Problem (on a grid/array)
- **Question**: Place N queens on an NxN board so that no two queens attack each other.
- **Solution**: Backtracking with a boolean status array for columns and diagonals.

## 5. Game of Sudoku Solver
- **Question**: Fill a 9x9 grid so every row, column, and 3x3 subgrid has digits 1-9.
- **Solution**: Backtracking with array flags.

## Patterns in Array Puzzles
- **In-place modifications**: Using indices as markers or encoding two values in one.
- **Symmetry exploitation**: Rotating a matrix by 90 degrees by transposing then reversing rows.
- **Hashing with indices**: Storing frequency or presence by using the array indices themselves as keys.

## Complexity
- Most puzzles aim for **O(N)** or **O(N log N)** time and **O(1)** extra space if possible.
