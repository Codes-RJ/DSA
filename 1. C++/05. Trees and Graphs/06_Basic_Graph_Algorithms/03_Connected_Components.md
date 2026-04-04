# Connected Components

## Introduction
A connected component of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.

## Algorithm Concept
We can use either BFS or DFS to find connected components. Every time we start a new traversal (BFS/DFS) from an unvisited node, it represents the discovery of a new connected component.

## C++ Implementation

```cpp
#include <iostream>
#include <vector>

void DFS(int u, std::vector<std::vector<int>>& adj, std::vector<bool>& visited) {
    visited[u] = true;
    for (int v : adj[u]) {
        if (!visited[v]) {
            DFS(v, adj, visited);
        }
    }
}

int countConnectedComponents(std::vector<std::vector<int>>& adj, int V) {
    std::vector<bool> visited(V, false);
    int count = 0;

    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            count++;
            DFS(i, adj, visited);
        }
    }
    return count;
}
```

## Applications
- Social Networks: Finding friend circles or isolated groups.
- Image Processing: Identifying distinct objects in a binary image (connected component labeling).
- Distributed Systems: Checking if all nodes in a cluster are reachable from each other.
- Circuit Design: Determining electrically isolated parts of a circuit.

## Time Complexity
- O(V + E) since each vertex and edge is visited at most once.

## Space Complexity
- O(V) for the `visited` array and recursion stack.
