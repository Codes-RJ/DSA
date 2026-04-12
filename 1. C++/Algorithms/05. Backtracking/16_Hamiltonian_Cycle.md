# 16_Hamiltonian_Cycle.md

## Hamiltonian Cycle

### Definition

A Hamiltonian cycle is a cycle in a graph that visits each vertex exactly once and returns to the starting vertex. This is different from an Eulerian cycle (which visits edges exactly once).

### Problem Statement

Input:
- An undirected graph with n vertices

Output:
- A Hamiltonian cycle (sequence of vertices)
- Or indicate that no such cycle exists

### Visual Example

```
Graph (5 vertices in a pentagon shape):
0-1-2-3-4-0 (all connected in a cycle)

Hamiltonian cycle: 0 → 1 → 2 → 3 → 4 → 0
```

### Backtracking Approach

```
Step 1: Start at vertex 0 (any vertex)
Step 2: Add vertices one by one to the path
Step 3: At each step, try unvisited vertices adjacent to current vertex
Step 4: When path length equals n, check if last vertex is adjacent to start
Step 5: If yes, Hamiltonian cycle found
Step 6: If no vertex works, backtrack
```

### Implementation

```cpp
#include <iostream>
#include <vector>
using namespace std;

bool isSafe(int vertex, int pos, vector<int>& path, vector<vector<int>>& graph) {
    // Check if vertex is adjacent to previous vertex in path
    if (graph[path[pos - 1]][vertex] == 0) {
        return false;
    }
    
    // Check if vertex already used
    for (int i = 0; i < pos; i++) {
        if (path[i] == vertex) {
            return false;
        }
    }
    
    return true;
}

bool hamiltonianCycleUtil(vector<vector<int>>& graph, vector<int>& path, int pos) {
    int n = graph.size();
    
    // Base case: all vertices are in path
    if (pos == n) {
        // Check if last vertex is adjacent to start vertex
        if (graph[path[pos - 1]][path[0]] == 1) {
            return true;
        }
        return false;
    }
    
    // Try different vertices as next candidate
    for (int v = 1; v < n; v++) {
        if (isSafe(v, pos, path, graph)) {
            path[pos] = v;
            
            if (hamiltonianCycleUtil(graph, path, pos + 1)) {
                return true;
            }
            
            // Backtrack
            path[pos] = -1;
        }
    }
    
    return false;
}

void findHamiltonianCycle(vector<vector<int>>& graph) {
    int n = graph.size();
    vector<int> path(n, -1);
    
    // Start from vertex 0
    path[0] = 0;
    
    if (hamiltonianCycleUtil(graph, path, 1)) {
        cout << "Hamiltonian Cycle found: ";
        for (int i = 0; i < n; i++) {
            cout << path[i] << " ";
        }
        cout << path[0] << endl;
    } else {
        cout << "No Hamiltonian Cycle exists" << endl;
    }
}

int main() {
    vector<vector<int>> graph = {
        {0, 1, 0, 1, 0},
        {1, 0, 1, 1, 1},
        {0, 1, 0, 0, 1},
        {1, 1, 0, 0, 1},
        {0, 1, 1, 1, 0}
    };
    
    findHamiltonianCycle(graph);
    
    return 0;
}
```

### Example Walkthrough (5 vertices)

```
Graph adjacency:
0: connected to 1, 3
1: connected to 0, 2, 3, 4
2: connected to 1, 4
3: connected to 0, 1, 4
4: connected to 1, 2, 3

Start: path=[0, -1, -1, -1, -1], pos=1

pos=1: try v=1 (adjacent to 0, not used)
    path=[0,1,-1,-1,-1], pos=2
    try v=0? used, v=2 (adjacent to 1)
        path=[0,1,2,-1,-1], pos=3
        try v=4 (adjacent to 2)
            path=[0,1,2,4,-1], pos=4
            try v=3 (adjacent to 4, not used)
                path=[0,1,2,4,3], pos=5 (all vertices)
                Check graph[3][0] = 1? Yes (3 adjacent to 0)
                → Cycle found: 0-1-2-4-3-0
```

### Hamiltonian Path (Not Cycle)

A path that visits each vertex exactly once but does not need to return to start.

```cpp
bool hamiltonianPathUtil(vector<vector<int>>& graph, vector<int>& path, int pos) {
    int n = graph.size();
    
    if (pos == n) {
        return true;  // All vertices visited
    }
    
    for (int v = 0; v < n; v++) {
        if (isSafe(v, pos, path, graph)) {
            path[pos] = v;
            
            if (hamiltonianPathUtil(graph, path, pos + 1)) {
                return true;
            }
            
            path[pos] = -1;
        }
    }
    
    return false;
}
```

### Find All Hamiltonian Cycles

```cpp
void findAllHamiltonianCycles(vector<vector<int>>& graph, vector<int>& path, 
                               int pos, vector<vector<int>>& allCycles) {
    int n = graph.size();
    
    if (pos == n) {
        if (graph[path[pos - 1]][path[0]] == 1) {
            allCycles.push_back(path);
        }
        return;
    }
    
    for (int v = 1; v < n; v++) {
        if (isSafe(v, pos, path, graph)) {
            path[pos] = v;
            findAllHamiltonianCycles(graph, path, pos + 1, allCycles);
            path[pos] = -1;
        }
    }
}
```

### Time Complexity

| Complexity | Value |
|------------|-------|
| Worst case | O(n!) |
| With pruning | Much better for sparse graphs |

### Space Complexity

O(n) for path array + O(n) recursion stack

### Necessary Conditions

For a Hamiltonian cycle to exist:

1. Graph must be connected
2. Each vertex must have degree ≥ 2
3. Dirac's theorem: If every vertex has degree ≥ n/2, Hamiltonian cycle exists
4. Ore's theorem: If deg(u) + deg(v) ≥ n for every non-adjacent pair, Hamiltonian cycle exists

### Dirac's and Ore's Theorems

| Theorem | Condition | Conclusion |
|---------|-----------|------------|
| Dirac | deg(v) ≥ n/2 for all v | Hamiltonian cycle exists |
| Ore | deg(u) + deg(v) ≥ n for all non-adjacent u,v | Hamiltonian cycle exists |

### Applications

| Application | Description |
|-------------|-------------|
| Traveling Salesman | Find shortest Hamiltonian cycle (weighted graph) |
| Routing | Find path visiting all locations |
| DNA sequencing | Reconstruct sequence from fragments |
| Puzzle solving | Knight's tour on chessboard |

### Hamiltonian Cycle vs Eulerian Cycle

| Aspect | Hamiltonian Cycle | Eulerian Cycle |
|--------|-------------------|----------------|
| Visits | Vertices exactly once | Edges exactly once |
| Complexity | NP-complete | Polynomial time |
| Condition | No simple necessary/sufficient | All vertices have even degree |
| Application | TSP | Chinese postman |

### Practice Problems

1. Find a Hamiltonian cycle in a given graph
2. Determine if a Hamiltonian path exists
3. Find all Hamiltonian cycles in a graph
4. Find the shortest Hamiltonian cycle (TSP)
5. Determine if a graph is Hamiltonian (Dirac/Ore conditions)