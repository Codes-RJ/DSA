# 15_M_coloring_Problem.md

## M-Coloring Problem

### Definition

Given an undirected graph and m colors, determine if the graph can be colored with at most m colors such that no two adjacent vertices share the same color.

### Problem Statement

Input:
- An undirected graph with n vertices
- Number of colors m

Output:
- A valid coloring (assignment of colors to vertices)
- Or indicate that no such coloring exists

### Visual Example

```
Graph: 4 vertices in a square
Edges: 0-1, 1-2, 2-3, 3-0, 0-2 (diagonal)

With m=3 colors:
Vertex 0: Color 1
Vertex 1: Color 2
Vertex 2: Color 3
Vertex 3: Color 2

All adjacent vertices have different colors.
```

### Backtracking Approach

```
Step 1: Start with no colors assigned
Step 2: For each vertex, try colors 1 to m
Step 3: Check if current color is safe (no adjacent vertex has same color)
Step 4: If safe, assign color and recurse to next vertex
Step 5: If all vertices colored, return true
Step 6: If no color works, backtrack (unassign color)
```

### Implementation

```cpp
#include <iostream>
#include <vector>
using namespace std;

bool isSafe(int vertex, int color, vector<int>& colors, vector<vector<int>>& graph) {
    for (int neighbor = 0; neighbor < graph.size(); neighbor++) {
        if (graph[vertex][neighbor] && colors[neighbor] == color) {
            return false;
        }
    }
    return true;
}

bool graphColoring(int vertex, int m, vector<int>& colors, vector<vector<int>>& graph) {
    int n = graph.size();
    
    // Base case: all vertices colored
    if (vertex == n) {
        return true;
    }
    
    // Try all colors for current vertex
    for (int color = 1; color <= m; color++) {
        if (isSafe(vertex, color, colors, graph)) {
            colors[vertex] = color;
            
            if (graphColoring(vertex + 1, m, colors, graph)) {
                return true;
            }
            
            // Backtrack
            colors[vertex] = 0;
        }
    }
    
    return false;
}

int main() {
    int n = 4;
    vector<vector<int>> graph = {
        {0, 1, 1, 1},
        {1, 0, 1, 0},
        {1, 1, 0, 1},
        {1, 0, 1, 0}
    };
    
    int m = 3;
    vector<int> colors(n, 0);
    
    if (graphColoring(0, m, colors, graph)) {
        cout << "Valid coloring found:" << endl;
        for (int i = 0; i < n; i++) {
            cout << "Vertex " << i << " -> Color " << colors[i] << endl;
        }
    } else {
        cout << "No valid coloring exists with " << m << " colors" << endl;
    }
    
    return 0;
}
```

### Example Walkthrough (4 vertices, m=3)

```
Graph:
0 connected to 1,2,3
1 connected to 0,2
2 connected to 0,1,3
3 connected to 0,2

Start: vertex=0, colors=[0,0,0,0]

vertex=0: try color=1 (safe)
    colors=[1,0,0,0]
    vertex=1: try color=1? no (neighbor 0 has color1)
              try color=2 (safe)
        colors=[1,2,0,0]
        vertex=2: try color=1? no (neighbor 0 has color1)
                  try color=2? no (neighbor 1 has color2)
                  try color=3 (safe)
            colors=[1,2,3,0]
            vertex=3: try color=1? no (neighbor 0 has color1)
                      try color=2? safe (neighbor 0 has1, neighbor 2 has3)
                colors=[1,2,3,2]
                vertex=4 → all colored → return true

Solution: Vertex0=1, Vertex1=2, Vertex2=3, Vertex3=2
```

### Graph Coloring with Adjacency List

```cpp
bool isSafeList(int vertex, int color, vector<int>& colors, vector<vector<int>>& adj) {
    for (int neighbor : adj[vertex]) {
        if (colors[neighbor] == color) {
            return false;
        }
    }
    return true;
}

bool graphColoringList(int vertex, int m, vector<int>& colors, vector<vector<int>>& adj) {
    int n = adj.size();
    
    if (vertex == n) {
        return true;
    }
    
    for (int color = 1; color <= m; color++) {
        if (isSafeList(vertex, color, colors, adj)) {
            colors[vertex] = color;
            
            if (graphColoringList(vertex + 1, m, colors, adj)) {
                return true;
            }
            
            colors[vertex] = 0;
        }
    }
    
    return false;
}
```

### Find All Colorings

```cpp
void findAllColorings(int vertex, int m, vector<int>& colors, 
                       vector<vector<int>>& graph, 
                       vector<vector<int>>& allColorings) {
    int n = graph.size();
    
    if (vertex == n) {
        allColorings.push_back(colors);
        return;
    }
    
    for (int color = 1; color <= m; color++) {
        if (isSafe(vertex, color, colors, graph)) {
            colors[vertex] = color;
            findAllColorings(vertex + 1, m, colors, graph, allColorings);
            colors[vertex] = 0;
        }
    }
}
```

### Chromatic Number

Find the minimum number of colors needed to color the graph.

```cpp
int chromaticNumber(vector<vector<int>>& graph) {
    int n = graph.size();
    
    for (int m = 1; m <= n; m++) {
        vector<int> colors(n, 0);
        if (graphColoring(0, m, colors, graph)) {
            return m;
        }
    }
    
    return n;  // complete graph needs n colors
}
```

### Time Complexity

| Complexity | Value |
|------------|-------|
| Worst case | O(m^n) |
| With pruning | Much better in practice |

### Space Complexity

O(n) for colors array + O(n) recursion stack

### Applications

| Application | Description |
|-------------|-------------|
| Map Coloring | Color regions on a map |
| Register Allocation | Assign variables to registers |
| Scheduling | Assign time slots to tasks |
| Sudoku | 9-coloring of a 9×9 grid |

### Four Color Theorem

Any planar graph can be colored with at most 4 colors. This was the first major theorem proved using a computer.

### Practice Problems

1. Determine if a graph can be colored with m colors
2. Find the chromatic number of a graph
3. Find all possible colorings of a graph with m colors
4. Color a map (planar graph) with 4 colors
5. Determine if a graph is bipartite (2-colorable)