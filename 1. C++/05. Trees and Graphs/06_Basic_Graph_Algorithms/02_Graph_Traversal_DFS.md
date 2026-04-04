# Depth-First Search (DFS) in Graphs

## Introduction
DFS is a graph traversal algorithm that explores as deep as possible along each branch before backtracking. It is fundamentally recursive and is used to visit vertices of a graph in depth-first order.

## Key Logic
- Uses a **Stack** (implicitly via recursion).
- Keeps track of **visited** vertices to avoid cycles.
- Explores one neighbor's path fully before moving to another neighbor.

## C++ Implementation (Recursive)

```cpp
#include <iostream>
#include <vector>

using namespace std;

void DFS_Util(int u, vector<vector<int>>& adj, vector<bool>& visited) {
    visited[u] = true;
    cout << u << " "; // Visit node

    for (int v : adj[u]) {
        if (!visited[v]) {
            DFS_Util(v, adj, visited);
        }
    }
}

void DFS(vector<vector<int>>& adj, int V) {
    vector<bool> visited(V, false);
    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            DFS_Util(i, adj, visited);
        }
    }
}
```

## Space and Time Complexity

| Complexity | Explanation |
|------------|-------------|
| **Time Complexity** | O(V + E) |
| **Space Complexity** | O(V) for visited array and recursion stack |

## Applications
- Path finding between two nodes.
- Topological sorting for Directed Acyclic Graphs (DAG).
- Finding connected components.
- Cycle detection (using recursion stack).
- Solving puzzles like mazes.
- Strongly Connected Components (Tarjan's or Kosaraju's).

## Advantages
- Simple to implement using recursion.
- Excellent for reaching deep parts of a graph quickly.
- Useful for structured problems like exhaustive searching.

## Disadvantages
- Can blow up the call stack for very large graphs.
- Not guaranteed to find the shortest path.
