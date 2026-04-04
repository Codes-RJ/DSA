# Puzzle Problems

## Overview
Puzzle problems are creative and challenging problems that test logical reasoning, mathematical thinking, and algorithmic problem-solving skills. These problems often appear in technical interviews and competitive programming to assess a candidate's ability to think outside the box.

## Topics Covered

### 1. Logic Puzzles (`01_Logic_Puzzles.md`)
- Pattern recognition puzzles
- Logical deduction problems
- Constraint satisfaction problems
- Brain teasers and riddles
- Analytical reasoning challenges

### 2. Pattern Puzzles (`02_Pattern_Puzzles.md`)
- Number pattern recognition
- Geometric pattern generation
- Sequence prediction problems
- Mathematical pattern identification
- Visual pattern programming

### 3. Number Puzzles (`03_Number_Puzzles.md`)
- Number theory puzzles
- Arithmetic and algebraic puzzles
- Prime number puzzles
- Perfect square and cube problems
- Digit manipulation puzzles

### 4. Array Puzzles (`04_Array_Puzzles.md`)
- Array manipulation challenges
- Rearrangement puzzles
- Array transformation problems
- Multi-dimensional array puzzles
- Creative array algorithms

### 5. Recreational Problems (`05_Recreational_Problems.md`)
- Game theory problems
- Recreational mathematics
- Classic puzzles (N-Queens, Sudoku, etc.)
- Algorithmic game solving
- Entertainment mathematics

## Problem-Solving Strategies

### 1. Pattern Recognition
- Identify recurring patterns
- Look for mathematical relationships
- Consider edge cases and boundaries
- Validate patterns with examples

### 2. Mathematical Modeling
- Convert problems to mathematical equations
- Use invariants and properties
- Apply number theory concepts
- Consider combinatorial approaches

### 3. Algorithmic Thinking
- Break down complex problems
- Use divide and conquer
- Apply dynamic programming
- Consider greedy approaches

### 4. Logical Deduction
- Use systematic elimination
- Apply constraints and rules
- Consider all possibilities
- Verify solutions rigorously

## Classic Puzzle Implementations

### 1. N-Queens Problem
```cpp
class NQueens {
public:
    // Solve N-Queens problem
    static std::vector<std::vector<std::string>> solveNQueens(int n) {
        std::vector<std::vector<std::string>> solutions;
        std::vector<std::string> board(n, std::string(n, '.'));
        
        solveNQueensHelper(board, 0, solutions);
        return solutions;
    }
    
    // Count number of solutions
    static int totalNQueens(int n) {
        std::vector<std::string> board(n, std::string(n, '.'));
        int count = 0;
        solveNQueensCount(board, 0, count);
        return count;
    }
    
private:
    static void solveNQueensHelper(std::vector<std::string>& board, int row,
                                   std::vector<std::vector<std::string>>& solutions) {
        if (row == board.size()) {
            solutions.push_back(board);
            return;
        }
        
        for (int col = 0; col < board.size(); col++) {
            if (isValidQueen(board, row, col)) {
                board[row][col] = 'Q';
                solveNQueensHelper(board, row + 1, solutions);
                board[row][col] = '.';
            }
        }
    }
    
    static void solveNQueensCount(std::vector<std::string>& board, int row, int& count) {
        if (row == board.size()) {
            count++;
            return;
        }
        
        for (int col = 0; col < board.size(); col++) {
            if (isValidQueen(board, row, col)) {
                board[row][col] = 'Q';
                solveNQueensCount(board, row + 1, count);
                board[row][col] = '.';
            }
        }
    }
    
    static bool isValidQueen(const std::vector<std::string>& board, int row, int col) {
        int n = board.size();
        
        // Check column
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 'Q') return false;
        }
        
        // Check upper-left diagonal
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 'Q') return false;
        }
        
        // Check upper-right diagonal
        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
            if (board[i][j] == 'Q') return false;
        }
        
        return true;
    }
};
```

### 2. Sudoku Solver
```cpp
class SudokuSolver {
public:
    // Solve Sudoku puzzle
    static bool solveSudoku(std::vector<std::vector<char>>& board) {
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                if (board[row][col] == '.') {
                    for (char num = '1'; num <= '9'; num++) {
                        if (isValidSudoku(board, row, col, num)) {
                            board[row][col] = num;
                            
                            if (solveSudoku(board)) {
                                return true;
                            }
                            
                            board[row][col] = '.'; // Backtrack
                        }
                    }
                    return false; // No valid number found
                }
            }
        }
        return true; // Puzzle solved
    }
    
    // Check if Sudoku board is valid
    static bool isValidSudoku(const std::vector<std::vector<char>>& board) {
        // Check rows
        for (int row = 0; row < 9; row++) {
            std::unordered_set<char> seen;
            for (int col = 0; col < 9; col++) {
                if (board[row][col] != '.') {
                    if (seen.count(board[row][col])) return false;
                    seen.insert(board[row][col]);
                }
            }
        }
        
        // Check columns
        for (int col = 0; col < 9; col++) {
            std::unordered_set<char> seen;
            for (int row = 0; row < 9; row++) {
                if (board[row][col] != '.') {
                    if (seen.count(board[row][col])) return false;
                    seen.insert(board[row][col]);
                }
            }
        }
        
        // Check 3x3 sub-boxes
        for (int box = 0; box < 9; box++) {
            std::unordered_set<char> seen;
            int startRow = (box / 3) * 3;
            int startCol = (box % 3) * 3;
            
            for (int row = startRow; row < startRow + 3; row++) {
                for (int col = startCol; col < startCol + 3; col++) {
                    if (board[row][col] != '.') {
                        if (seen.count(board[row][col])) return false;
                        seen.insert(board[row][col]);
                    }
                }
            }
        }
        
        return true;
    }
    
private:
    static bool isValidSudoku(const std::vector<std::vector<char>>& board,
                             int row, int col, char num) {
        // Check row
        for (int j = 0; j < 9; j++) {
            if (board[row][j] == num) return false;
        }
        
        // Check column
        for (int i = 0; i < 9; i++) {
            if (board[i][col] == num) return false;
        }
        
        // Check 3x3 sub-box
        int startRow = (row / 3) * 3;
        int startCol = (col / 3) * 3;
        
        for (int i = startRow; i < startRow + 3; i++) {
            for (int j = startCol; j < startCol + 3; j++) {
                if (board[i][j] == num) return false;
            }
        }
        
        return true;
    }
};
```

### 3. Tower of Hanoi
```cpp
class TowerOfHanoi {
public:
    // Solve Tower of Hanoi and return moves
    static std::vector<std::pair<int, int>> solveTowerOfHanoi(int n, int source, 
                                                              int destination, 
                                                              int auxiliary) {
        std::vector<std::pair<int, int>> moves;
        solveTowerOfHanoiHelper(n, source, destination, auxiliary, moves);
        return moves;
    }
    
    // Print Tower of Hanoi solution
    static void printTowerOfHanoiSolution(int n) {
        auto moves = solveTowerOfHanoi(n, 1, 3, 2);
        std::cout << "Number of moves: " << moves.size() << std::endl;
        for (const auto& move : moves) {
            std::cout << "Move disk from peg " << move.first 
                     << " to peg " << move.second << std::endl;
        }
    }
    
    // Minimum number of moves
    static int minMoves(int n) {
        return (1 << n) - 1; // 2^n - 1
    }
    
private:
    static void solveTowerOfHanoiHelper(int n, int source, int destination,
                                        int auxiliary, 
                                        std::vector<std::pair<int, int>>& moves) {
        if (n == 1) {
            moves.push_back({source, destination});
            return;
        }
        
        // Move n-1 disks from source to auxiliary
        solveTowerOfHanoiHelper(n - 1, source, auxiliary, destination, moves);
        
        // Move the largest disk from source to destination
        moves.push_back({source, destination});
        
        // Move n-1 disks from auxiliary to destination
        solveTowerOfHanoiHelper(n - 1, auxiliary, destination, source, moves);
    }
};
```

## Number Puzzles

### 1. Happy Number
```cpp
class HappyNumber {
public:
    // Check if a number is happy
    static bool isHappy(int n) {
        std::unordered_set<int> seen;
        
        while (n != 1 && seen.find(n) == seen.end()) {
            seen.insert(n);
            n = sumOfSquares(n);
        }
        
        return n == 1;
    }
    
    // Find all happy numbers up to n
    static std::vector<int> happyNumbersUpTo(int n) {
        std::vector<int> happy;
        for (int i = 1; i <= n; i++) {
            if (isHappy(i)) {
                happy.push_back(i);
            }
        }
        return happy;
    }
    
private:
    static int sumOfSquares(int n) {
        int sum = 0;
        while (n > 0) {
            int digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        return sum;
    }
};
```

### 2. Ugly Number
```cpp
class UglyNumber {
public:
    // Check if a number is ugly (prime factors only 2, 3, 5)
    static bool isUgly(int n) {
        if (n <= 0) return false;
        
        for (int prime : {2, 3, 5}) {
            while (n % prime == 0) {
                n /= prime;
            }
        }
        
        return n == 1;
    }
    
    // Find the nth ugly number
    static int nthUglyNumber(int n) {
        std::vector<int> ugly(n);
        ugly[0] = 1;
        
        int i2 = 0, i3 = 0, i5 = 0;
        
        for (int i = 1; i < n; i++) {
            int nextUgly = std::min({ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5});
            ugly[i] = nextUgly;
            
            if (nextUgly == ugly[i2] * 2) i2++;
            if (nextUgly == ugly[i3] * 3) i3++;
            if (nextUgly == ugly[i5] * 5) i5++;
        }
        
        return ugly[n - 1];
    }
};
```

### 3. Perfect Number
```cpp
class PerfectNumber {
public:
    // Check if a number is perfect
    static bool isPerfect(int n) {
        if (n <= 1) return false;
        
        int sum = 1; // 1 is a proper divisor for all n > 1
        
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                sum += i;
                if (i * i != n) {
                    sum += n / i;
                }
            }
        }
        
        return sum == n;
    }
    
    // Find all perfect numbers up to n
    static std::vector<int> perfectNumbersUpTo(int n) {
        std::vector<int> perfect;
        for (int i = 2; i <= n; i++) {
            if (isPerfect(i)) {
                perfect.push_back(i);
            }
        }
        return perfect;
    }
};
```

## Pattern Puzzles

### 1. Pascal's Triangle
```cpp
class PascalsTriangle {
public:
    // Generate Pascal's Triangle up to n rows
    static std::vector<std::vector<int>> generate(int numRows) {
        std::vector<std::vector<int>> triangle(numRows);
        
        for (int i = 0; i < numRows; i++) {
            triangle[i].resize(i + 1, 1);
            
            for (int j = 1; j < i; j++) {
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
            }
        }
        
        return triangle;
    }
    
    // Get specific row of Pascal's Triangle
    static std::vector<int> getRow(int rowIndex) {
        std::vector<int> row(rowIndex + 1, 1);
        
        for (int i = 1; i < rowIndex; i++) {
            for (int j = i; j > 0; j--) {
                row[j] += row[j - 1];
            }
        }
        
        return row;
    }
    
    // Calculate binomial coefficient
    static long long binomialCoefficient(int n, int k) {
        if (k > n - k) k = n - k;
        
        long long result = 1;
        for (int i = 0; i < k; i++) {
            result = result * (n - i) / (i + 1);
        }
        
        return result;
    }
};
```

### 2. Fibonacci Pattern
```cpp
class FibonacciPatterns {
public:
    // Generate Fibonacci sequence
    static std::vector<int> generateFibonacci(int n) {
        if (n <= 0) return {};
        if (n == 1) return {0};
        
        std::vector<int> fib(n);
        fib[0] = 0;
        fib[1] = 1;
        
        for (int i = 2; i < n; i++) {
            fib[i] = fib[i - 1] + fib[i - 2];
        }
        
        return fib;
    }
    
    // Check if number is Fibonacci
    static bool isFibonacci(int n) {
        if (n < 0) return false;
        
        // A number is Fibonacci if and only if one or both of (5*n^2 + 4) or (5*n^2 - 4) is a perfect square
        return isPerfectSquare(5LL * n * n + 4) || isPerfectSquare(5LL * n * n - 4);
    }
    
    // Generate Fibonacci spiral pattern
    static std::vector<std::vector<int>> fibonacciSpiral(int size) {
        std::vector<std::vector<int>> spiral(size, std::vector<int>(size, 0));
        
        std::vector<int> fib = generateFibonacci(size * size);
        int index = 0;
        
        int top = 0, bottom = size - 1;
        int left = 0, right = size - 1;
        
        while (top <= bottom && left <= right && index < fib.size()) {
            // Traverse from left to right
            for (int i = left; i <= right && index < fib.size(); i++) {
                spiral[top][i] = fib[index++];
            }
            top++;
            
            // Traverse from top to bottom
            for (int i = top; i <= bottom && index < fib.size(); i++) {
                spiral[i][right] = fib[index++];
            }
            right--;
            
            // Traverse from right to left
            for (int i = right; i >= left && index < fib.size(); i--) {
                spiral[bottom][i] = fib[index++];
            }
            bottom--;
            
            // Traverse from bottom to top
            for (int i = bottom; i >= top && index < fib.size(); i--) {
                spiral[i][left] = fib[index++];
            }
            left++;
        }
        
        return spiral;
    }
    
private:
    static bool isPerfectSquare(long long n) {
        long long root = sqrt(n);
        return root * root == n;
    }
};
```

## Logic Puzzles

### 1. Water Jug Problem
```cpp
class WaterJug {
public:
    // Solve water jug problem using BFS
    static std::vector<std::pair<int, int>> waterJugProblem(int jug1, int jug2, int target) {
        std::queue<std::pair<int, int>> q;
        std::set<std::pair<int, int>> visited;
        std::map<std::pair<int, int>, std::pair<int, int>> parent;
        
        std::pair<int, int> start = {0, 0};
        q.push(start);
        visited.insert(start);
        
        while (!q.empty()) {
            auto current = q.front();
            q.pop();
            
            if (current.first == target || current.second == target) {
                return reconstructPath(parent, start, current);
            }
            
            // Try all possible operations
            std::vector<std::pair<int, int>> nextStates = {
                {jug1, current.second},           // Fill jug1
                {current.first, jug2},           // Fill jug2
                {0, current.second},             // Empty jug1
                {current.first, 0},             // Empty jug2
                {std::max(0, current.first - (jug2 - current.second)), 
                 std::min(jug2, current.second + current.first)}, // Pour jug1 -> jug2
                {std::min(jug1, current.first + current.second),
                 std::max(0, current.second - (jug1 - current.first))}  // Pour jug2 -> jug1
            };
            
            for (auto next : nextStates) {
                if (visited.find(next) == visited.end()) {
                    visited.insert(next);
                    parent[next] = current;
                    q.push(next);
                }
            }
        }
        
        return {}; // No solution found
    }
    
private:
    static std::vector<std::pair<int, int>> reconstructPath(
        const std::map<std::pair<int, int>, std::pair<int, int>>& parent,
        std::pair<int, int> start, std::pair<int, int> end) {
        
        std::vector<std::pair<int, int>> path;
        std::pair<int, int> current = end;
        
        while (current != start) {
            path.push_back(current);
            current = parent.at(current);
        }
        
        path.push_back(start);
        std::reverse(path.begin(), path.end());
        return path;
    }
};
```

### 2. Missionaries and Cannibals
```cpp
class MissionariesCannibals {
public:
    // Solve missionaries and cannibals problem
    static std::vector<std::string> solve(int missionaries, int cannibals) {
        State start = {missionaries, cannibals, 1, 0, 0};
        State goal = {0, 0, 0, missionaries, cannibals};
        
        std::queue<State> q;
        std::set<State> visited;
        std::map<State, State> parent;
        std::map<State, std::string> move;
        
        q.push(start);
        visited.insert(start);
        
        while (!q.empty()) {
            State current = q.front();
            q.pop();
            
            if (current == goal) {
                return reconstructSolution(parent, move, start, goal);
            }
            
            // Generate all possible moves
            std::vector<std::pair<int, int>> boatMoves = {
                {1, 0}, {0, 1}, {1, 1}, {2, 0}, {0, 2}
            };
            
            for (auto boatMove : boatMoves) {
                State next = current;
                
                if (next.boatSide == 1) {
                    // Moving from left to right
                    next.leftMissionaries -= boatMove.first;
                    next.leftCannibals -= boatMove.second;
                    next.rightMissionaries += boatMove.first;
                    next.rightCannibals += boatMove.second;
                } else {
                    // Moving from right to left
                    next.rightMissionaries -= boatMove.first;
                    next.rightCannibals -= boatMove.second;
                    next.leftMissionaries += boatMove.first;
                    next.leftCannibals += boatMove.second;
                }
                
                next.boatSide = 1 - next.boatSide;
                
                if (isValidState(next) && visited.find(next) == visited.end()) {
                    visited.insert(next);
                    parent[next] = current;
                    move[next] = getMoveString(boatMove, current.boatSide);
                    q.push(next);
                }
            }
        }
        
        return {}; // No solution found
    }
    
private:
    struct State {
        int leftMissionaries, leftCannibals;
        int boatSide;
        int rightMissionaries, rightCannibals;
        
        bool operator<(const State& other) const {
            return std::tie(leftMissionaries, leftCannibals, boatSide,
                           rightMissionaries, rightCannibals) <
                   std::tie(other.leftMissionaries, other.leftCannibals, other.boatSide,
                           other.rightMissionaries, other.rightCannibals);
        }
        
        bool operator==(const State& other) const {
            return leftMissionaries == other.leftMissionaries &&
                   leftCannibals == other.leftCannibals &&
                   boatSide == other.boatSide &&
                   rightMissionaries == other.rightMissionaries &&
                   rightCannibals == other.rightCannibals;
        }
    };
    
    static bool isValidState(const State& state) {
        // Check non-negative counts
        if (state.leftMissionaries < 0 || state.leftCannibals < 0 ||
            state.rightMissionaries < 0 || state.rightCannibals < 0) {
            return false;
        }
        
        // Check cannibals don't outnumber missionaries on either side
        if (state.leftMissionaries > 0 && state.leftCannibals > state.leftMissionaries) {
            return false;
        }
        if (state.rightMissionaries > 0 && state.rightCannibals > state.rightMissionaries) {
            return false;
        }
        
        return true;
    }
    
    static std::string getMoveString(std::pair<int, int> move, int boatSide) {
        std::string side = (boatSide == 1) ? "left to right" : "right to left";
        return "Move " + std::to_string(move.first) + " missionaries and " +
               std::to_string(move.second) + " cannibals " + side;
    }
    
    static std::vector<std::string> reconstructSolution(
        const std::map<State, State>& parent,
        const std::map<State, std::string>& move,
        State start, State goal) {
        
        std::vector<std::string> solution;
        State current = goal;
        
        while (current != start) {
            solution.push_back(move.at(current));
            current = parent.at(current);
        }
        
        std::reverse(solution.begin(), solution.end());
        return solution;
    }
};
```

## Performance Analysis

### Time Complexity
| Problem | Time Complexity | Space Complexity |
|---------|-----------------|------------------|
| N-Queens | O(N!) | O(N) |
| Sudoku | O(9^(81)) | O(81) |
| Tower of Hanoi | O(2^N) | O(N) |
| Water Jug | O(jug1 × jug2) | O(jug1 × jug2) |
| Missionaries & Cannibals | O(2^N) | O(2^N) |

## Best Practices

### 1. Problem Analysis
- Understand constraints and rules
- Identify patterns and invariants
- Consider multiple solution approaches
- Start with brute force, then optimize

### 2. Implementation Strategy
- Use appropriate data structures
- Handle edge cases properly
- Implement backtracking carefully
- Optimize after getting correct solution

### 3. Testing and Validation
- Test with small cases first
- Verify solution correctness
- Check performance with larger inputs
- Consider memory limitations

## Applications

### 1. Education
- Teaching problem-solving skills
- Developing logical thinking
- Understanding algorithms
- Competitive programming preparation

### 2. Artificial Intelligence
- Search algorithms
- Constraint satisfaction
- Planning and reasoning
- Game playing

### 3. Entertainment
- Puzzle games
- Brain training apps
- Educational software
- Recreational mathematics

## Summary

Puzzle problems provide an excellent way to develop problem-solving skills and algorithmic thinking. They require creativity, logical reasoning, and systematic approaches. Mastering these problems enhances one's ability to tackle complex real-world problems and prepares for technical interviews and competitive programming challenges.
