# 05_Sudoku_Solver.md

## Sudoku Solver

### Definition

Sudoku is a puzzle where a 9×9 grid must be filled with digits 1-9 such that each row, each column, and each 3×3 subgrid contains all digits exactly once.

### Problem Statement

Input:
- A 9×9 grid with some cells filled (0 or '.' represents empty)

Output:
- The filled grid satisfying all Sudoku constraints

### Visual Example

```
Input:
5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
------+-------+------
8 . . | . 6 . | . . 3
4 . . | 8 . 3 | . . 1
7 . . | . 2 . | . . 6
------+-------+------
. 6 . | . . . | 2 8 .
. . . | 4 1 9 | . . 5
. . . | . 8 . | . 7 9

Output (solved):
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
------+-------+------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
------+-------+------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9
```

### Backtracking Approach

```
Step 1: Find an empty cell
Step 2: Try placing digits 1-9 in that cell
Step 3: Before placing, check if digit is valid (row, column, box)
Step 4: If valid, place digit and recurse
Step 5: If recursion returns true, solution found
Step 6: If no digit works, backtrack (set cell back to empty)
```

### Implementation

```cpp
#include <iostream>
#include <vector>
using namespace std;

bool isValid(vector<vector<char>>& board, int row, int col, char num) {
    // Check row
    for (int j = 0; j < 9; j++) {
        if (board[row][j] == num) return false;
    }
    
    // Check column
    for (int i = 0; i < 9; i++) {
        if (board[i][col] == num) return false;
    }
    
    // Check 3x3 box
    int boxRow = (row / 3) * 3;
    int boxCol = (col / 3) * 3;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[boxRow + i][boxCol + j] == num) return false;
        }
    }
    
    return true;
}

bool solveSudoku(vector<vector<char>>& board) {
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (board[i][j] == '.') {
                for (char num = '1'; num <= '9'; num++) {
                    if (isValid(board, i, j, num)) {
                        board[i][j] = num;
                        
                        if (solveSudoku(board)) {
                            return true;
                        }
                        
                        board[i][j] = '.';
                    }
                }
                return false;
            }
        }
    }
    return true;
}

int main() {
    vector<vector<char>> board = {
        {'5','3','.', '.','7','.', '.','.','.'},
        {'6','.','.', '1','9','5', '.','.','.'},
        {'.','9','8', '.','.','.', '.','6','.'},
        {'8','.','.', '.','6','.', '.','.','3'},
        {'4','.','.', '8','.','3', '.','.','1'},
        {'7','.','.', '.','2','.', '.','.','6'},
        {'.','6','.', '.','.','.', '2','8','.'},
        {'.','.','.', '4','1','9', '.','.','5'},
        {'.','.','.', '.','8','.', '.','7','9'}
    };
    
    solveSudoku(board);
    
    cout << "Solved Sudoku:" << endl;
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cout << board[i][j] << " ";
            if (j == 2 || j == 5) cout << "| ";
        }
        cout << endl;
        if (i == 2 || i == 5) cout << "------+-------+------" << endl;
    }
    
    return 0;
}
```

### Optimized Implementation with Candidate Lists

```cpp
class SudokuSolver {
private:
    vector<vector<char>> board;
    vector<vector<bool>> rowUsed, colUsed, boxUsed;
    
    int getBoxIndex(int row, int col) {
        return (row / 3) * 3 + (col / 3);
    }
    
    void placeNumber(int row, int col, char num, bool place) {
        int val = num - '1';
        board[row][col] = place ? num : '.';
        rowUsed[row][val] = place;
        colUsed[col][val] = place;
        boxUsed[getBoxIndex(row, col)][val] = place;
    }
    
    bool isValid(int row, int col, char num) {
        int val = num - '1';
        return !rowUsed[row][val] && !colUsed[col][val] && 
               !boxUsed[getBoxIndex(row, col)][val];
    }
    
    bool solve() {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    for (char num = '1'; num <= '9'; num++) {
                        if (isValid(i, j, num)) {
                            placeNumber(i, j, num, true);
                            if (solve()) return true;
                            placeNumber(i, j, num, false);
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }
    
public:
    SudokuSolver(vector<vector<char>>& b) : board(b) {
        rowUsed.assign(9, vector<bool>(9, false));
        colUsed.assign(9, vector<bool>(9, false));
        boxUsed.assign(9, vector<bool>(9, false));
        
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    int val = board[i][j] - '1';
                    rowUsed[i][val] = true;
                    colUsed[j][val] = true;
                    boxUsed[getBoxIndex(i, j)][val] = true;
                }
            }
        }
    }
    
    void solveSudoku() {
        solve();
    }
    
    vector<vector<char>> getBoard() {
        return board;
    }
};
```

### Finding Next Cell (Heuristic)

Choose the cell with the fewest possible candidates first.

```cpp
pair<int, int> findBestEmptyCell(vector<vector<char>>& board) {
    int bestRow = -1, bestCol = -1;
    int minCandidates = 10;
    
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (board[i][j] == '.') {
                int candidates = 0;
                for (char num = '1'; num <= '9'; num++) {
                    if (isValid(board, i, j, num)) {
                        candidates++;
                    }
                }
                if (candidates < minCandidates) {
                    minCandidates = candidates;
                    bestRow = i;
                    bestCol = j;
                    if (candidates == 1) return {bestRow, bestCol};
                }
            }
        }
    }
    
    return {bestRow, bestCol};
}

bool solveSudokuHeuristic(vector<vector<char>>& board) {
    auto [row, col] = findBestEmptyCell(board);
    if (row == -1) return true;
    
    for (char num = '1'; num <= '9'; num++) {
        if (isValid(board, row, col, num)) {
            board[row][col] = num;
            if (solveSudokuHeuristic(board)) return true;
            board[row][col] = '.';
        }
    }
    
    return false;
}
```

### Time Complexity

| Complexity | Value |
|------------|-------|
| Worst case | O(9^(n)) where n = number of empty cells |
| With pruning | Much faster in practice |
| Typical puzzle | Solved in milliseconds |

### Space Complexity

O(n²) for the board (81 cells)

### Variations

#### 1. Sudoku Validator (Check if solution is valid)

```cpp
bool isValidSudoku(vector<vector<char>>& board) {
    vector<vector<bool>> rowUsed(9, vector<bool>(9, false));
    vector<vector<bool>> colUsed(9, vector<bool>(9, false));
    vector<vector<bool>> boxUsed(9, vector<bool>(9, false));
    
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (board[i][j] != '.') {
                int val = board[i][j] - '1';
                int boxIndex = (i / 3) * 3 + (j / 3);
                
                if (rowUsed[i][val] || colUsed[j][val] || boxUsed[boxIndex][val]) {
                    return false;
                }
                
                rowUsed[i][val] = true;
                colUsed[j][val] = true;
                boxUsed[boxIndex][val] = true;
            }
        }
    }
    
    return true;
}
```

#### 2. 4x4 or 16x16 Sudoku

Same logic with different board size.

### Practice Problems

1. Solve a given Sudoku puzzle
2. Check if a Sudoku solution is valid
3. Generate a valid Sudoku puzzle
4. Solve Sudoku with diagonal constraint (both main diagonals also unique)
5. Count number of solutions for a given puzzle
---

## Next Step

- Go to [06_Rat_in_a_Maze.md](06_Rat_in_a_Maze.md) to continue with Rat in a Maze.
