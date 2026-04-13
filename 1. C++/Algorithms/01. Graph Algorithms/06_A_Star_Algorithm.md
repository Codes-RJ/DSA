# Graph Algorithm - A* Search Algorithm

## 📖 Overview

A* (A-star) is an informed search algorithm that finds the shortest path between a start node and a goal node using a heuristic function to guide the search. It is widely used in pathfinding and graph traversal applications such as GPS navigation, video games, and robotics.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Heuristic Function** | Estimates cost from current node to goal |
| **g(n)** | Actual cost from start to current node |
| **h(n)** | Heuristic estimate from current to goal |
| **f(n)** | Total estimated cost = g(n) + h(n) |
| **Admissible Heuristic** | Never overestimates actual cost (guarantees optimality) |

---

## 📊 How A* Works

### Step-by-step Visualization

```
Grid with obstacles (S=Start, G=Goal, #=Obstacle):

    0   1   2   3   4
0   S   .   .   #   .
1   .   #   .   #   .
2   .   #   .   .   .
3   .   .   .   #   .
4   .   .   .   .   G

Heuristic: Manhattan distance

Step 1: Start at (0,0), f = 0 + Manhattan distance to goal
Step 2: Explore neighbors, calculate f scores
Step 3: Expand node with lowest f score
Step 4: Repeat until goal reached
```

---

## 📝 Complete Implementation

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <unordered_map>
#include <set>
#include <algorithm>
#include <iomanip>
using namespace std;

// Point structure for grid coordinates
struct Point {
    int x, y;
    
    Point(int x = 0, int y = 0) : x(x), y(y) {}
    
    bool operator==(const Point& other) const {
        return x == other.x && y == other.y;
    }
    
    bool operator!=(const Point& other) const {
        return !(*this == other);
    }
};

// Hash function for Point
struct PointHash {
    size_t operator()(const Point& p) const {
        return p.x * 1000 + p.y;
    }
};

// Node for A* algorithm
struct AStarNode {
    Point position;
    double g;  // Cost from start to this node
    double h;  // Heuristic cost to goal
    double f;  // Total cost (g + h)
    AStarNode* parent;
    
    AStarNode(Point pos, double gCost, double hCost, AStarNode* par = nullptr)
        : position(pos), g(gCost), h(hCost), f(gCost + hCost), parent(par) {}
    
    bool operator>(const AStarNode& other) const {
        return f > other.f;
    }
};

class AStar {
private:
    vector<vector<int>> grid;  // 0 = free, 1 = obstacle
    int rows, cols;
    
    // Heuristic functions
    double manhattanDistance(const Point& a, const Point& b) {
        return abs(a.x - b.x) + abs(a.y - b.y);
    }
    
    double euclideanDistance(const Point& a, const Point& b) {
        return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
    }
    
    double chebyshevDistance(const Point& a, const Point& b) {
        return max(abs(a.x - b.x), abs(a.y - b.y));
    }
    
    // Get valid neighbors (4-directional or 8-directional)
    vector<Point> getNeighbors(const Point& p, bool allowDiagonal = false) {
        vector<Point> neighbors;
        
        // 4-directional movement
        int dx4[] = {0, 1, 0, -1};
        int dy4[] = {1, 0, -1, 0};
        
        // 8-directional movement (including diagonals)
        int dx8[] = {0, 1, 1, 1, 0, -1, -1, -1};
        int dy8[] = {1, 1, 0, -1, -1, -1, 0, 1};
        
        int* dx = allowDiagonal ? dx8 : dx4;
        int* dy = allowDiagonal ? dy8 : dy4;
        int dirCount = allowDiagonal ? 8 : 4;
        
        for (int i = 0; i < dirCount; i++) {
            int nx = p.x + dx[i];
            int ny = p.y + dy[i];
            
            if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && grid[nx][ny] == 0) {
                neighbors.push_back(Point(nx, ny));
            }
        }
        
        return neighbors;
    }
    
public:
    AStar(int r, int c) : rows(r), cols(c) {
        grid.resize(rows, vector<int>(cols, 0));
    }
    
    void setObstacle(int x, int y) {
        if (x >= 0 && x < rows && y >= 0 && y < cols) {
            grid[x][y] = 1;
        }
    }
    
    void clearObstacle(int x, int y) {
        if (x >= 0 && x < rows && y >= 0 && y < cols) {
            grid[x][y] = 0;
        }
    }
    
    // Main A* algorithm
    vector<Point> findPath(Point start, Point goal, 
                           string heuristicType = "manhattan",
                           bool allowDiagonal = false) {
        // Priority queue for open set (min-heap by f value)
        priority_queue<AStarNode, vector<AStarNode>, greater<AStarNode>> openSet;
        
        // Maps for quick lookup
        unordered_map<Point, double, PointHash> gScore;
        unordered_map<Point, double, PointHash> fScore;
        unordered_map<Point, AStarNode*, PointHash> nodeMap;
        
        // Closed set (visited nodes)
        set<Point, decltype([](const Point& a, const Point& b) {
            return a.x < b.x || (a.x == b.x && a.y < b.y);
        })> closedSet;
        
        // Initialize start node
        double hStart = getHeuristic(start, goal, heuristicType);
        AStarNode* startNode = new AStarNode(start, 0, hStart);
        
        gScore[start] = 0;
        fScore[start] = hStart;
        nodeMap[start] = startNode;
        openSet.push(*startNode);
        
        while (!openSet.empty()) {
            AStarNode current = openSet.top();
            openSet.pop();
            
            Point currentPos = current.position;
            
            // Check if goal reached
            if (currentPos == goal) {
                // Reconstruct path
                vector<Point> path;
                AStarNode* node = nodeMap[currentPos];
                while (node != nullptr) {
                    path.push_back(node->position);
                    node = node->parent;
                }
                reverse(path.begin(), path.end());
                
                // Cleanup
                for (auto& pair : nodeMap) {
                    delete pair.second;
                }
                
                return path;
            }
            
            closedSet.insert(currentPos);
            
            // Explore neighbors
            vector<Point> neighbors = getNeighbors(currentPos, allowDiagonal);
            for (const Point& neighbor : neighbors) {
                if (closedSet.count(neighbor)) continue;
                
                double tentativeG = gScore[currentPos] + getMoveCost(currentPos, neighbor);
                
                if (!gScore.count(neighbor) || tentativeG < gScore[neighbor]) {
                    gScore[neighbor] = tentativeG;
                    double h = getHeuristic(neighbor, goal, heuristicType);
                    double f = tentativeG + h;
                    fScore[neighbor] = f;
                    
                    AStarNode* neighborNode = new AStarNode(neighbor, tentativeG, h, nodeMap[currentPos]);
                    nodeMap[neighbor] = neighborNode;
                    openSet.push(*neighborNode);
                }
            }
        }
        
        // No path found
        cout << "No path found!" << endl;
        
        // Cleanup
        for (auto& pair : nodeMap) {
            delete pair.second;
        }
        
        return {};
    }
    
private:
    double getHeuristic(const Point& a, const Point& b, const string& type) {
        if (type == "manhattan") return manhattanDistance(a, b);
        if (type == "euclidean") return euclideanDistance(a, b);
        if (type == "chebyshev") return chebyshevDistance(a, b);
        return manhattanDistance(a, b);  // default
    }
    
    double getMoveCost(const Point& from, const Point& to) {
        // Diagonal moves cost more (1.414), orthogonal moves cost 1
        if (from.x != to.x && from.y != to.y) {
            return 1.414;  // Diagonal
        }
        return 1.0;  // Orthogonal
    }
    
public:
    // Display grid with path
    void displayGrid(const vector<Point>& path = {}) {
        vector<vector<char>> display(rows, vector<char>(cols, '.'));
        
        // Mark obstacles
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1) {
                    display[i][j] = '#';
                }
            }
        }
        
        // Mark path
        for (size_t i = 0; i < path.size(); i++) {
            if (i == 0) {
                display[path[i].x][path[i].y] = 'S';
            } else if (i == path.size() - 1) {
                display[path[i].x][path[i].y] = 'G';
            } else {
                display[path[i].x][path[i].y] = '*';
            }
        }
        
        // Print grid
        cout << "\n  ";
        for (int j = 0; j < cols; j++) {
            cout << setw(2) << j;
        }
        cout << endl;
        
        for (int i = 0; i < rows; i++) {
            cout << setw(2) << i;
            for (int j = 0; j < cols; j++) {
                cout << " " << display[i][j];
            }
            cout << endl;
        }
    }
};

int main() {
    cout << "=== A* Search Algorithm Demo ===" << endl;
    
    // Example 1: Simple grid with obstacles
    cout << "\n1. Simple Grid Pathfinding:" << endl;
    AStar astar1(6, 6);
    
    // Add obstacles
    astar1.setObstacle(1, 2);
    astar1.setObstacle(2, 2);
    astar1.setObstacle(3, 2);
    astar1.setObstacle(1, 3);
    astar1.setObstacle(2, 3);
    astar1.setObstacle(3, 3);
    
    Point start1(0, 0);
    Point goal1(5, 5);
    
    cout << "Grid (S=Start, G=Goal, #=Obstacle, *=Path):" << endl;
    astar1.displayGrid();
    
    vector<Point> path1 = astar1.findPath(start1, goal1, "manhattan", false);
    
    if (!path1.empty()) {
        cout << "\nPath found! Length: " << path1.size() << " steps" << endl;
        cout << "Path: ";
        for (const Point& p : path1) {
            cout << "(" << p.x << "," << p.y << ") ";
        }
        cout << endl;
        
        astar1.displayGrid(path1);
    }
    
    // Example 2: Maze with diagonal movement
    cout << "\n2. Maze with Diagonal Movement:" << endl;
    AStar astar2(8, 8);
    
    // Create a maze
    for (int i = 0; i < 8; i++) {
        astar2.setObstacle(0, i);
        astar2.setObstacle(7, i);
        astar2.setObstacle(i, 0);
        astar2.setObstacle(i, 7);
    }
    
    // Internal walls
    astar2.setObstacle(2, 3);
    astar2.setObstacle(2, 4);
    astar2.setObstacle(3, 3);
    astar2.setObstacle(4, 3);
    astar2.setObstacle(5, 3);
    astar2.setObstacle(5, 4);
    
    Point start2(1, 1);
    Point goal2(6, 6);
    
    cout << "\nWith 4-directional movement:" << endl;
    vector<Point> path2a = astar2.findPath(start2, goal2, "manhattan", false);
    if (!path2a.empty()) {
        cout << "Path length: " << path2a.size() << " steps" << endl;
        astar2.displayGrid(path2a);
    }
    
    cout << "\nWith 8-directional movement (diagonals allowed):" << endl;
    vector<Point> path2b = astar2.findPath(start2, goal2, "chebyshev", true);
    if (!path2b.empty()) {
        cout << "Path length: " << path2b.size() << " steps" << endl;
        astar2.displayGrid(path2b);
    }
    
    // Example 3: Different heuristics comparison
    cout << "\n3. Heuristic Comparison:" << endl;
    AStar astar3(10, 10);
    
    // Add random obstacles
    astar3.setObstacle(2, 3);
    astar3.setObstacle(2, 4);
    astar3.setObstacle(3, 3);
    astar3.setObstacle(4, 5);
    astar3.setObstacle(5, 5);
    astar3.setObstacle(5, 6);
    astar3.setObstacle(6, 5);
    astar3.setObstacle(7, 2);
    astar3.setObstacle(7, 3);
    astar3.setObstacle(8, 2);
    
    Point start3(0, 0);
    Point goal3(9, 9);
    
    cout << "Grid with obstacles:" << endl;
    astar3.displayGrid();
    
    vector<string> heuristics = {"manhattan", "euclidean", "chebyshev"};
    
    for (const string& h : heuristics) {
        cout << "\nUsing " << h << " heuristic:" << endl;
        vector<Point> path = astar3.findPath(start3, goal3, h, true);
        if (!path.empty()) {
            cout << "Path length: " << path.size() << " steps" << endl;
        }
    }
    
    // Example 4: Empty grid (no obstacles)
    cout << "\n4. Empty Grid (No Obstacles):" << endl;
    AStar astar4(5, 5);
    Point start4(0, 0);
    Point goal4(4, 4);
    
    cout << "Empty grid:" << endl;
    astar4.displayGrid();
    
    vector<Point> path4 = astar4.findPath(start4, goal4, "manhattan", true);
    if (!path4.empty()) {
        cout << "\nShortest path (diagonals allowed):" << endl;
        astar4.displayGrid(path4);
        cout << "Path length: " << path4.size() << " steps" << endl;
    }
    
    // Example 5: No path scenario
    cout << "\n5. No Path Scenario:" << endl;
    AStar astar5(4, 4);
    astar5.setObstacle(0, 1);
    astar5.setObstacle(1, 0);
    astar5.setObstacle(1, 1);
    astar5.setObstacle(2, 2);
    astar5.setObstacle(2, 3);
    astar5.setObstacle(3, 2);
    // Start and goal isolated
    Point start5(0, 0);
    Point goal5(3, 3);
    
    astar5.displayGrid();
    vector<Point> path5 = astar5.findPath(start5, goal5, "manhattan", true);
    if (path5.empty()) {
        cout << "\nNo path exists between S and G!" << endl;
    }
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Aspect | Time Complexity | Space Complexity |
|--------|----------------|------------------|
| **A* with Binary Heap** | O(E log V) | O(V) |
| **A* with perfect heuristic** | O(d) where d = solution depth | O(V) |

---

## 🎯 Applications of A* Algorithm

| Application | Description |
|-------------|-------------|
| **GPS Navigation** | Finding shortest routes |
| **Video Games** | NPC pathfinding (e.g., in StarCraft, Age of Empires) |
| **Robotics** | Robot motion planning |
| **Network Routing** | Optimizing data packet paths |
| **Puzzle Solving** | Solving sliding puzzles, Rubik's cube |
| **Biology** | Protein folding path prediction |
| **Web Crawling** | Intelligent crawling strategies |

---

## 📊 A* vs Other Pathfinding Algorithms

| Algorithm | Heuristic | Optimal | Complete | Use Case |
|-----------|-----------|---------|----------|----------|
| **Dijkstra** | None (0) | Yes | Yes | Uninformed search |
| **Greedy BFS** | Yes | No | No | Fast but not optimal |
| **A*** | Yes | Yes (admissible) | Yes | Optimal informed search |
| **IDA*** | Yes (memory-bounded) | Yes | Yes | Large state spaces |

---

## ✅ Key Takeaways

1. **A*** combines actual cost (g) and heuristic estimate (h)
2. **Admissible heuristics** guarantee optimality
3. **Manhattan distance** works well for grid-based movement
4. **Euclidean distance** works for continuous spaces
5. **Priority queue** efficiently selects best node
6. **More efficient than Dijkstra** when heuristic is good
7. **Widely used** in games and real-time applications

---
---

## Next Step

- Go to [07_SCC.md](07_SCC.md) to continue with SCC.
