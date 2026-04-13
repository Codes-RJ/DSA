# 06_Rat_in_a_Maze.md

## Rat in a Maze

### Definition

A rat is placed at the top-left corner of an N×N maze. It needs to reach the bottom-right corner. The rat can only move right or down (or sometimes in all four directions). Some cells are blocked. Find a path from start to end.

### Problem Statement

Input:
- An N×N maze where 1 represents an open cell and 0 represents a blocked cell
- Starting position: (0, 0)
- Ending position: (N-1, N-1)

Output:
- A path from start to end (sequence of moves)
- Or indicate that no path exists

### Visual Example

```
Maze (N=4):
1 0 0 0
1 1 0 0
0 1 1 1
0 0 0 1

Path (1=path, 0=blocked, *=path taken):
1* 0  0  0
1* 1* 0  0
0  1* 1* 1*
0  0  0  1*

Path: (0,0) → (1,0) → (1,1) → (2,1) → (2,2) → (2,3) → (3,3)
```

### Backtracking Approach (Right and Down Only)

```
Step 1: Start at (0, 0)
Step 2: If current cell is the destination, print path and return true
Step 3: Mark current cell as part of path
Step 4: Try moving right (if valid)
Step 5: Try moving down (if valid)
Step 6: If neither leads to solution, unmark current cell and return false
```

### Implementation (Right and Down Only)

```cpp
#include <iostream>
#include <vector>
using namespace std;

bool isSafe(vector<vector<int>>& maze, int x, int y, int n) {
    return (x >= 0 && x < n && y >= 0 && y < n && maze[x][y] == 1);
}

bool solveMazeUtil(vector<vector<int>>& maze, int x, int y, vector<vector<int>>& solution, int n) {
    // If destination reached
    if (x == n-1 && y == n-1) {
        solution[x][y] = 1;
        return true;
    }
    
    // Check if current cell is valid
    if (isSafe(maze, x, y, n)) {
        solution[x][y] = 1;
        
        // Move right
        if (solveMazeUtil(maze, x, y + 1, solution, n)) {
            return true;
        }
        
        // Move down
        if (solveMazeUtil(maze, x + 1, y, solution, n)) {
            return true;
        }
        
        // Backtrack
        solution[x][y] = 0;
        return false;
    }
    
    return false;
}

void solveMaze(vector<vector<int>>& maze, int n) {
    vector<vector<int>> solution(n, vector<int>(n, 0));
    
    if (solveMazeUtil(maze, 0, 0, solution, n)) {
        cout << "Path found:" << endl;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cout << solution[i][j] << " ";
            }
            cout << endl;
        }
    } else {
        cout << "No path exists" << endl;
    }
}

int main() {
    int n = 4;
    vector<vector<int>> maze = {
        {1, 0, 0, 0},
        {1, 1, 0, 0},
        {0, 1, 1, 1},
        {0, 0, 0, 1}
    };
    
    solveMaze(maze, n);
    
    return 0;
}
```

### Implementation (All Four Directions)

```cpp
bool isSafe(vector<vector<int>>& maze, int x, int y, int n, vector<vector<bool>>& visited) {
    return (x >= 0 && x < n && y >= 0 && y < n && maze[x][y] == 1 && !visited[x][y]);
}

bool solveMazeAllDirections(vector<vector<int>>& maze, int x, int y, 
                             vector<vector<int>>& solution, 
                             vector<vector<bool>>& visited, int n) {
    if (x == n-1 && y == n-1) {
        solution[x][y] = 1;
        return true;
    }
    
    if (isSafe(maze, x, y, n, visited)) {
        visited[x][y] = true;
        solution[x][y] = 1;
        
        // Move up
        if (solveMazeAllDirections(maze, x - 1, y, solution, visited, n)) {
            return true;
        }
        
        // Move down
        if (solveMazeAllDirections(maze, x + 1, y, solution, visited, n)) {
            return true;
        }
        
        // Move left
        if (solveMazeAllDirections(maze, x, y - 1, solution, visited, n)) {
            return true;
        }
        
        // Move right
        if (solveMazeAllDirections(maze, x, y + 1, solution, visited, n)) {
            return true;
        }
        
        // Backtrack
        visited[x][y] = false;
        solution[x][y] = 0;
        return false;
    }
    
    return false;
}
```

### Find All Paths

```cpp
void findAllPaths(vector<vector<int>>& maze, int x, int y, 
                   vector<vector<bool>>& visited, 
                   vector<pair<int,int>>& path,
                   vector<vector<pair<int,int>>>& allPaths, int n) {
    if (x == n-1 && y == n-1) {
        path.push_back({x, y});
        allPaths.push_back(path);
        path.pop_back();
        return;
    }
    
    if (!isSafe(maze, x, y, n, visited)) {
        return;
    }
    
    visited[x][y] = true;
    path.push_back({x, y});
    
    // Try all four directions
    findAllPaths(maze, x + 1, y, visited, path, allPaths, n); // down
    findAllPaths(maze, x - 1, y, visited, path, allPaths, n); // up
    findAllPaths(maze, x, y + 1, visited, path, allPaths, n); // right
    findAllPaths(maze, x, y - 1, visited, path, allPaths, n); // left
    
    // Backtrack
    visited[x][y] = false;
    path.pop_back();
}

void printPath(vector<pair<int,int>>& path) {
    for (int i = 0; i < path.size(); i++) {
        cout << "(" << path[i].first << "," << path[i].second << ")";
        if (i < path.size() - 1) cout << " → ";
    }
    cout << endl;
}
```

### Example Walkthrough (Right and Down Only)

```
Maze:
1 0 0 0
1 1 0 0
0 1 1 1
0 0 0 1

Start at (0,0)
├── Try right: (0,1) is blocked → no
├── Try down: (1,0) is open
    ├── Try right: (1,1) is open
    │   ├── Try right: (1,2) is blocked → no
    │   ├── Try down: (2,1) is open
    │       ├── Try right: (2,2) is open
    │       │   ├── Try right: (2,3) is open
    │       │   │   ├── Try right: (2,4) out of bounds
    │       │   │   ├── Try down: (3,3) is open → reached destination!
    │       │   │       └── Path found
    │       │   └── Backtrack...
    │       └── ...
    └── ...

Path: (0,0) → (1,0) → (1,1) → (2,1) → (2,2) → (2,3) → (3,3)
```

### Time Complexity

| Variant | Time Complexity |
|---------|-----------------|
| Right and Down only | O(2^(n)) |
| All four directions | O(4^(n²)) |
| With pruning | Much better in practice |

### Space Complexity

O(n²) for the solution matrix and visited matrix

### Variations

#### 1. Count Number of Paths

```cpp
int countPaths(vector<vector<int>>& maze, int x, int y, int n) {
    if (x == n-1 && y == n-1) return 1;
    if (!isSafe(maze, x, y, n)) return 0;
    
    return countPaths(maze, x + 1, y, n) + countPaths(maze, x, y + 1, n);
}
```

#### 2. Shortest Path

Use BFS instead of backtracking for shortest path.

#### 3. Rat with Multiple Cheeses

Collect all items (cheeses) in the maze before reaching destination.

### Practice Problems

1. Find a path from start to end in a maze (right and down only)
2. Find a path in a maze with all four directions
3. Find all paths from start to end
4. Count number of paths in a maze
5. Find the path with maximum sum (if cells have values)
---

## Next Step

- Go to [07_Knight_Tour.md](07_Knight_Tour.md) to continue with Knight Tour.
