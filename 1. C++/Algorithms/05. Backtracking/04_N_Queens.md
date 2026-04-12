# 04_N_Queens.md

## N-Queens Problem

### Definition

The N-Queens problem asks to place N queens on an N×N chessboard such that no two queens attack each other. Queens attack horizontally, vertically, and diagonally.

### Problem Statement

Input:
- An integer n (size of chessboard)

Output:
- All possible arrangements of n queens on an n×n board where no two queens attack each other

### Constraints

Two queens cannot share:
- Same row
- Same column
- Same diagonal (both directions)

### Visual Example (n=4)

```
Solution 1:
. Q . .
. . . Q
Q . . .
. . Q .

Solution 2:
. . Q .
Q . . .
. . . Q
. Q . .
```

### Backtracking Approach

```
Step 1: Place queens row by row (one queen per row)
Step 2: For each row, try placing queen in each column
Step 3: Before placing, check if position is safe
Step 4: If safe, place queen and move to next row
Step 5: If no safe column in current row, backtrack
Step 6: When all n queens placed, record solution
```

### Implementation

```cpp
#include <iostream>
#include <vector>
using namespace std;

bool isSafe(vector<string>& board, int row, int col, int n) {
    // Check column (above only)
    for (int i = 0; i < row; i++) {
        if (board[i][col] == 'Q') return false;
    }
    
    // Check upper-left diagonal
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j] == 'Q') return false;
    }
    
    // Check upper-right diagonal
    for (int i = row, j = col; i >= 0 && j < n; i--, j++) {
        if (board[i][j] == 'Q') return false;
    }
    
    return true;
}

void solveNQueens(int n, int row, vector<string>& board, vector<vector<string>>& result) {
    if (row == n) {
        result.push_back(board);
        return;
    }
    
    for (int col = 0; col < n; col++) {
        if (isSafe(board, row, col, n)) {
            board[row][col] = 'Q';
            solveNQueens(n, row + 1, board, result);
            board[row][col] = '.';
        }
    }
}

vector<vector<string>> nQueens(int n) {
    vector<vector<string>> result;
    vector<string> board(n, string(n, '.'));
    solveNQueens(n, 0, board, result);
    return result;
}

int main() {
    int n = 4;
    vector<vector<string>> solutions = nQueens(n);
    
    cout << "Number of solutions for " << n << "-Queens: " << solutions.size() << endl;
    
    for (int i = 0; i < solutions.size(); i++) {
        cout << "\nSolution " << i + 1 << ":\n";
        for (string row : solutions[i]) {
            cout << row << endl;
        }
    }
    
    return 0;
}
```

### Optimized Implementation (Using Boolean Arrays)

Instead of checking diagonals each time, use boolean arrays to mark used columns and diagonals.

```cpp
void solveNQueensOptimized(int n, int row, vector<string>& board, 
                           vector<bool>& cols, 
                           vector<bool>& diag1, 
                           vector<bool>& diag2,
                           vector<vector<string>>& result) {
    if (row == n) {
        result.push_back(board);
        return;
    }
    
    for (int col = 0; col < n; col++) {
        int d1 = row - col + n - 1;  // diagonal 1 index (row - col)
        int d2 = row + col;           // diagonal 2 index (row + col)
        
        if (!cols[col] && !diag1[d1] && !diag2[d2]) {
            board[row][col] = 'Q';
            cols[col] = true;
            diag1[d1] = true;
            diag2[d2] = true;
            
            solveNQueensOptimized(n, row + 1, board, cols, diag1, diag2, result);
            
            board[row][col] = '.';
            cols[col] = false;
            diag1[d1] = false;
            diag2[d2] = false;
        }
    }
}

vector<vector<string>> nQueensOptimized(int n) {
    vector<vector<string>> result;
    vector<string> board(n, string(n, '.'));
    vector<bool> cols(n, false);
    vector<bool> diag1(2 * n - 1, false);
    vector<bool> diag2(2 * n - 1, false);
    
    solveNQueensOptimized(n, 0, board, cols, diag1, diag2, result);
    return result;
}
```

### Diagonal Index Explanation

```
For an n×n board:
- Main diagonals (top-left to bottom-right): d1 = row - col
  Range: -(n-1) to (n-1) → offset by +(n-1) to make 0 to 2n-2

- Anti-diagonals (top-right to bottom-left): d2 = row + col
  Range: 0 to 2n-2
```

### Example Walkthrough (n=4)

```
Start: empty board

Row 0: try col 0
    Place Q at (0,0)
    Mark col0, diag1[3], diag2[0]

Row 1: try col 0 (blocked), col 1 (diag2[1] free? check)
    col1: d1=1-1+3=3? blocked, d2=1+1=2 free → but d1 blocked → skip
    col2: d1=1-2+3=2 free, d2=1+2=3 free → place Q at (1,2)
    Mark col2, diag1[2], diag2[3]

Row 2: try col 0 (col0 blocked), col1 (d2=2+1=3 blocked)
    col3: d1=2-3+3=2 blocked, d2=2+3=5 free → d1 blocked → skip
    No safe column → backtrack

Row 1: remove Q from (1,2), try col3
    col3: d1=1-3+3=1 free, d2=1+3=4 free → place Q at (1,3)
    ...

Continue until all rows filled or all options exhausted
```

### Number of Solutions

| n | Number of Distinct Solutions |
|---|------------------------------|
| 1 | 1 |
| 2 | 0 |
| 3 | 0 |
| 4 | 2 |
| 5 | 10 |
| 6 | 4 |
| 7 | 40 |
| 8 | 92 |
| 9 | 352 |
| 10 | 724 |
| 11 | 2680 |
| 12 | 14200 |
| 13 | 73712 |
| 14 | 365596 |

### Time Complexity

| Complexity | Value |
|------------|-------|
| Worst case | O(n!) |
| With pruning | Much less in practice |
| Number of solutions | Grows exponentially |

### Space Complexity

O(n²) for the board representation
O(n) for recursion stack

### Variations

#### 1. Count Only (Not All Solutions)

```cpp
int countNQueens(int n) {
    vector<bool> cols(n, false);
    vector<bool> diag1(2*n-1, false);
    vector<bool> diag2(2*n-1, false);
    
    function<int(int)> solve = [&](int row) {
        if (row == n) return 1;
        
        int count = 0;
        for (int col = 0; col < n; col++) {
            int d1 = row - col + n - 1;
            int d2 = row + col;
            
            if (!cols[col] && !diag1[d1] && !diag2[d2]) {
                cols[col] = diag1[d1] = diag2[d2] = true;
                count += solve(row + 1);
                cols[col] = diag1[d1] = diag2[d2] = false;
            }
        }
        return count;
    };
    
    return solve(0);
}
```

#### 2. One Solution Only

Modify to return true when first solution found.

#### 3. N-Queens on Toroidal Board

Queens also attack across board edges.

### Practice Problems

1. Find all solutions to N-Queens for n=8
2. Count number of solutions for n=10
3. Find one solution for n=20
4. Implement N-Queens with bitmask optimization
5. Solve N-Queens for n=1000 using heuristic (not exact)