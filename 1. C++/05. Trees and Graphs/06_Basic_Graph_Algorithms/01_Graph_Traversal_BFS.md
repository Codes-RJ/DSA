# Breadth-First Search (BFS) in Graphs

## Introduction
BFS is a graph traversal algorithm that visits vertices in layers starting from a source vertex. It explores all neighbors at the current distance before moving further away.

## Key Logic
- Uses a **Queue** (FIFO).
- Keeps track of **visited** vertices to avoid infinite loops and re-processing.
- Explores all neighbors of a node before moving to their neighbors.

## C++ Implementation (Adjacency List)

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

void BFS(int startNode, vector<vector<int>>& adj, int V) {
    vector<bool> visited(V, false);
    queue<int> q;

    visited[startNode] = true;
    q.push(startNode);

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        cout << u << " "; // Visit node

        for (int v : adj[u]) {
            if (!visited[v]) {
                visited[v] = true;
                q.push(v);
            }
        }
    }
}
```

## Space and Time Complexity

| Complexity | Explanation |
|------------|-------------|
| **Time Complexity** | O(V + E) where V is vertices and E is edges |
| **Space Complexity** | O(V) for visited array and queue |

## Applications
- Shortest path in an unweighted graph.
- Social networking search (people at distance *k*).
- System testing (finding dead code or unreachable components).
- Web crawling.
- Level-wise traversal.
- Checking if a graph is bipartite.

## Disconnected Graphs
To cover all nodes in a potentially disconnected graph:
```cpp
for (int i = 0; i < V; i++) {
    if (!visited[i]) {
        BFS(i, adj, V);
    }
}
```
