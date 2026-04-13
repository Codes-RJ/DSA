# 03_Pruning_Techniques.md

## Pruning Techniques in Backtracking

### Definition

Pruning is the technique of eliminating branches of the search tree that cannot possibly lead to a valid solution. It is the key to making backtracking efficient.

### Why Pruning Matters

Without pruning, backtracking explores the entire search space:

- Subsets of 30 elements: 2^30 ≈ 1 billion branches
- Permutations of 15 elements: 15! ≈ 1.3 trillion branches
- N-Queens (n=20): 20! ≈ 2.4 quintillion branches

With pruning, many branches are cut off early, dramatically reducing the search space.

### Types of Pruning

| Type | Description | Example |
|------|-------------|---------|
| Constraint Pruning | Check constraints at each step | N-Queens diagonal check |
| Bound Pruning | Stop if cannot beat best solution | Tug of War bound |
| Forward Checking | Check future constraints | Sudoku row/column/box |
| Symmetry Pruning | Skip symmetric configurations | First queen in first half |
| Ordering Pruning | Try promising choices first | Warnsdorff's rule |
| Memoization | Cache visited states | Avoid revisiting |

### 1. Constraint Pruning

Check if current partial solution violates any constraints.

**Example: N-Queens**

```cpp
bool isSafe(vector<string>& board, int row, int col, int n) {
    // Check column
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
```

### 2. Forward Checking

Check future constraints before making a choice.

**Example: Sudoku**

```cpp
bool canPlace(vector<vector<int>>& board, int row, int col, int num) {
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

// Forward checking: also check if any cell has no possible numbers
bool hasValidMoves(vector<vector<int>>& board, int row, int col) {
    // Check if there exists at least one number that can be placed
    for (int num = 1; num <= 9; num++) {
        if (canPlace(board, row, col, num)) return true;
    }
    return false;
}
```

### 3. Bound Pruning (For Optimization Problems)

Stop exploring a branch if it cannot improve the best solution found so far.

**Example: Tug of War (Minimize difference)**

```cpp
int bestDiff = INT_MAX;
int totalSum = 0;

void tugOfWar(vector<int>& nums, int index, int currentSum, int count, int n) {
    // Prune if cannot beat best
    int remainingSum = totalSum - currentSum;
    int potentialDiff = abs(remainingSum - currentSum);
    if (potentialDiff >= bestDiff) {
        return;  // Cannot improve
    }
    
    if (count == n / 2) {
        bestDiff = min(bestDiff, abs(remainingSum - currentSum));
        return;
    }
    
    if (index >= nums.size()) return;
    
    // Include current element
    tugOfWar(nums, index + 1, currentSum + nums[index], count + 1, n);
    
    // Exclude current element
    tugOfWar(nums, index + 1, currentSum, count, n);
}
```

### 4. Symmetry Pruning

Skip equivalent configurations that would produce symmetric solutions.

**Example: N-Queens - First Queen in First Half**

```cpp
void solveNQueens(int n, int row, vector<string>& board, vector<vector<string>>& result) {
    if (row == n) {
        result.push_back(board);
        return;
    }
    
    int startCol = 0;
    int endCol = n;
    
    // For first row, only try first half (symmetry)
    if (row == 0) {
        endCol = (n + 1) / 2;  // Only first half
    }
    
    for (int col = startCol; col < endCol; col++) {
        if (isSafe(board, row, col, n)) {
            board[row][col] = 'Q';
            solveNQueens(n, row + 1, board, result);
            board[row][col] = '.';
        }
    }
    
    // Mirror solutions for complete set
    if (row == 0) {
        vector<vector<string>> mirrored;
        for (auto& sol : result) {
            vector<string> mirror;
            for (string& rowStr : sol) {
                string mirroredRow = rowStr;
                reverse(mirroredRow.begin(), mirroredRow.end());
                mirror.push_back(mirroredRow);
            }
            mirrored.push_back(mirror);
        }
        result.insert(result.end(), mirrored.begin(), mirrored.end());
    }
}
```

### 5. Ordering Pruning (Heuristics)

Try the most promising choices first to find solutions faster.

**Example: Knight Tour - Warnsdorff's Rule**

```cpp
// Move to the square with the fewest onward moves first
int knightMoves[8][2] = {{-2,-1},{-2,1},{-1,-2},{-1,2},{1,-2},{1,2},{2,-1},{2,1}};

int getDegree(int x, int y, vector<vector<int>>& board, int n) {
    int count = 0;
    for (int i = 0; i < 8; i++) {
        int nx = x + knightMoves[i][0];
        int ny = y + knightMoves[i][1];
        if (nx >= 0 && nx < n && ny >= 0 && ny < n && board[nx][ny] == -1) {
            count++;
        }
    }
    return count;
}

bool solveKnightTour(int x, int y, int moveNum, vector<vector<int>>& board, int n) {
    if (moveNum == n * n) return true;
    
    // Get all possible moves
    vector<tuple<int,int,int>> nextMoves;  // degree, x, y
    for (int i = 0; i < 8; i++) {
        int nx = x + knightMoves[i][0];
        int ny = y + knightMoves[i][1];
        if (nx >= 0 && nx < n && ny >= 0 && ny < n && board[nx][ny] == -1) {
            int degree = getDegree(nx, ny, board, n);
            nextMoves.push_back({degree, nx, ny});
        }
    }
    
    // Sort by degree (Warnsdorff's rule)
    sort(nextMoves.begin(), nextMoves.end());
    
    // Try moves in order of increasing degree
    for (auto& [degree, nx, ny] : nextMoves) {
        board[nx][ny] = moveNum;
        if (solveKnightTour(nx, ny, moveNum + 1, board, n)) {
            return true;
        }
        board[nx][ny] = -1;
    }
    
    return false;
}
```

### 6. Memoization Pruning

Cache results of visited states to avoid recomputation.

**Example: Word Search with Memoization**

```cpp
vector<vector<int>> memo;  // -1: not computed, 0: false, 1: true

bool exist(vector<vector<char>>& board, string word, int i, int j, int pos) {
    if (pos == word.length()) return true;
    if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size()) return false;
    if (board[i][j] != word[pos]) return false;
    if (memo[i][j] != -1) return memo[i][j];
    
    char temp = board[i][j];
    board[i][j] = '#';
    
    bool found = exist(board, word, i+1, j, pos+1) ||
                 exist(board, word, i-1, j, pos+1) ||
                 exist(board, word, i, j+1, pos+1) ||
                 exist(board, word, i, j-1, pos+1);
    
    board[i][j] = temp;
    memo[i][j] = found;
    
    return found;
}
```

### Pruning Effectiveness Comparison

| Problem | Without Pruning | With Pruning | Reduction |
|---------|----------------|--------------|-----------|
| N-Queens (n=12) | ~14 million | ~1.6 million | ~90% |
| Sudoku | 9^81 (huge) | ~10^4 typical | Massive |
| Knight Tour (8x8) | 8^64 (huge) | Solvable | Massive |
| Permutations (n=10) | 3.6 million | 3.6 million | 0% (no pruning) |

### Best Practices for Pruning

1. **Prune early** - Check constraints as soon as possible
2. **Order matters** - Try most constrained choices first
3. **Bound aggressively** - Use tight bounds for optimization
4. **Use symmetry** - Eliminate equivalent states
5. **Cache results** - Avoid revisiting same state
6. **Iterative deepening** - For problems with unknown depth

### Practice Problems

1. Add pruning to N-Queens (column and diagonal checks)
2. Implement forward checking for Sudoku
3. Add bound pruning to Subset Sum (stop if sum exceeds target)
4. Implement Warnsdorff's rule for Knight Tour
5. Add symmetry pruning to Generate Permutations (skip duplicates)
---

## Next Step

- Go to [04_N_Queens.md](04_N_Queens.md) to continue with N Queens.
