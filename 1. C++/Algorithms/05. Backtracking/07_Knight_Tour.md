# 07_Knight_Tour.md

## Knight Tour Problem

### Definition

A knight is placed on an empty chessboard. The knight must visit every square exactly once, moving according to chess rules (L-shaped moves: 2 steps in one direction, 1 step perpendicular).

### Problem Statement

Input:
- Board size n (typically 8×8)
- Starting position (optional, usually (0,0))

Output:
- A sequence of moves visiting all squares exactly once
- Or indicate that no tour exists

### Knight Moves

A knight can make 8 possible moves:

```
( -2, -1 ), ( -2, +1 ),
( -1, -2 ), ( -1, +2 ),
( +1, -2 ), ( +1, +2 ),
( +2, -1 ), ( +2, +1 )
```

### Visual Example (5×5 Tour)

```
 0  15  10   5  20
 9   4  19  14  11
16   1   6  21   2
 7  12  23  18  13
24  17   8   3  22

Numbers represent move order (0 to 24)
```

### Backtracking Approach

```
Step 1: Start at (0,0) with move number 0
Step 2: Mark current cell with move number
Step 3: If all cells are visited (move number = n²-1), return true
Step 4: Try all 8 possible knight moves
Step 5: For each move, check if destination is within board and unvisited
Step 6: If valid, move knight to new position and recurse
Step 7: If recursion returns true, propagate success
Step 8: If no move works, backtrack (unmark current cell)
```

### Basic Implementation

```cpp
#include <iostream>
#include <vector>
using namespace std;

int knightMoves[8][2] = {
    {-2, -1}, {-2, 1},
    {-1, -2}, {-1, 2},
    {1, -2},  {1, 2},
    {2, -1},  {2, 1}
};

bool isSafe(int x, int y, vector<vector<int>>& board, int n) {
    return (x >= 0 && x < n && y >= 0 && y < n && board[x][y] == -1);
}

bool solveKnightTour(int x, int y, int moveNum, vector<vector<int>>& board, int n) {
    if (moveNum == n * n) {
        return true;
    }
    
    for (int i = 0; i < 8; i++) {
        int nextX = x + knightMoves[i][0];
        int nextY = y + knightMoves[i][1];
        
        if (isSafe(nextX, nextY, board, n)) {
            board[nextX][nextY] = moveNum;
            
            if (solveKnightTour(nextX, nextY, moveNum + 1, board, n)) {
                return true;
            }
            
            // Backtrack
            board[nextX][nextY] = -1;
        }
    }
    
    return false;
}

void printBoard(vector<vector<int>>& board, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << board[i][j] << "\t";
        }
        cout << endl;
    }
}

int main() {
    int n = 8;
    vector<vector<int>> board(n, vector<int>(n, -1));
    
    // Start at (0,0)
    board[0][0] = 0;
    
    if (solveKnightTour(0, 0, 1, board, n)) {
        cout << "Knight Tour found:" << endl;
        printBoard(board, n);
    } else {
        cout << "No solution exists" << endl;
    }
    
    return 0;
}
```

### Optimized Implementation with Warnsdorff's Rule

Warnsdorff's rule: always move to the square with the fewest onward moves. This heuristic makes the algorithm find a solution much faster.

```cpp
int getDegree(int x, int y, vector<vector<int>>& board, int n) {
    int count = 0;
    for (int i = 0; i < 8; i++) {
        int nextX = x + knightMoves[i][0];
        int nextY = y + knightMoves[i][1];
        if (isSafe(nextX, nextY, board, n)) {
            count++;
        }
    }
    return count;
}

bool solveKnightTourWarnsdorff(int x, int y, int moveNum, vector<vector<int>>& board, int n) {
    if (moveNum == n * n) {
        return true;
    }
    
    // Get all possible moves with their degrees
    vector<tuple<int, int, int>> nextMoves; // degree, nextX, nextY
    
    for (int i = 0; i < 8; i++) {
        int nextX = x + knightMoves[i][0];
        int nextY = y + knightMoves[i][1];
        
        if (isSafe(nextX, nextY, board, n)) {
            int degree = getDegree(nextX, nextY, board, n);
            nextMoves.push_back({degree, nextX, nextY});
        }
    }
    
    // Sort by degree (ascending) - Warnsdorff's rule
    sort(nextMoves.begin(), nextMoves.end());
    
    // Try moves in order of increasing degree
    for (auto& [degree, nextX, nextY] : nextMoves) {
        board[nextX][nextY] = moveNum;
        
        if (solveKnightTourWarnsdorff(nextX, nextY, moveNum + 1, board, n)) {
            return true;
        }
        
        // Backtrack
        board[nextX][nextY] = -1;
    }
    
    return false;
}
```

### Example Walkthrough (5×5)

```
Start at (0,0)
Move 0: (0,0)

Possible moves from (0,0):
(1,2) and (2,1)

Check (1,2):
    From (1,2), possible onward moves: (0,0 visited), (0,4), (2,4), (3,3), (3,1)
    Degree = 4

Check (2,1):
    From (2,1), possible onward moves: (0,0 visited), (0,2), (1,3), (3,3), (4,2), (4,0)
    Degree = 5

Warnsdorff: choose (1,2) (degree 4 < 5)

Continue...
```

### Number of Solutions

| Board Size | Number of Tours (closed) |
|------------|--------------------------|
| 1×1 | 1 |
| 2×2 | 0 |
| 3×3 | 0 |
| 4×4 | 0 |
| 5×5 | 1,728 |
| 6×6 | 6,637,920 |
| 7×7 | 165,575,218,320 |
| 8×8 | 19,591,828,170,979,904 |

### Time Complexity

| Approach | Time Complexity |
|----------|-----------------|
| Naive backtracking | O(8^(n²)) |
| With Warnsdorff | O(n²) in practice |

### Space Complexity

O(n²) for the board

### Closed vs Open Tour

- **Open Tour:** Start and end on different squares
- **Closed Tour:** Start and end on same square (knight can return to start)

### Variations

#### 1. Closed Knight Tour

Requires the last move to be able to return to start.

```cpp
bool isClosedTour(int lastX, int lastY, int startX, int startY) {
    for (int i = 0; i < 8; i++) {
        if (lastX + knightMoves[i][0] == startX && 
            lastY + knightMoves[i][1] == startY) {
            return true;
        }
    }
    return false;
}
```

#### 2. Knight Tour with Fixed Start Position

Any square can be the starting point (for n≥5, all squares are reachable).

#### 3. Knight Tour for Non-Square Boards

Extend to rectangular boards (m×n).

### Practice Problems

1. Find a knight tour on an 8×8 board
2. Find a knight tour starting from a specific position
3. Determine if a knight tour exists for a given board size
4. Find a closed knight tour
5. Implement Warnsdorff's rule for 8×8 board