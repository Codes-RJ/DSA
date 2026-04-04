# Adjacency Matrix Representation

## Introduction
An adjacency matrix is a 2D array of size `V x V` where `V` is the number of vertices in a graph. Each element `matrix[i][j]` represents the presence or weight of an edge between vertex `i` and vertex `j`.

## Implementation Concept

### Undirected Graph
In an undirected graph, if there is an edge between `i` and `j`, then `matrix[i][j] = 1` and `matrix[j][i] = 1`. The matrix is symmetric.

### Directed Graph
In a directed graph, if there is an edge from `i` to `j`, then `matrix[i][j] = 1`. The matrix is not necessarily symmetric.

### Weighted Graph
For weighted graphs, `matrix[i][j]` stores the weight of the edge instead of just 1. A special value (like 0 or infinity) represents "no edge".

## C++ Implementation

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Graph {
private:
    int V; // Number of vertices
    vector<vector<int>> adjMatrix;

public:
    Graph(int V) {
        this->V = V;
        adjMatrix.resize(V, vector<int>(V, 0));
    }

    // Add edge for undirected graph
    void addEdge(int u, int v) {
        if (u >= 0 && u < V && v >= 0 && v < V) {
            adjMatrix[u][v] = 1;
            adjMatrix[v][u] = 1; // For undirected
        }
    }

    // Display the matrix
    void display() {
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                cout << adjMatrix[i][j] << " ";
            }
            cout << endl;
        }
    }

    // Check if edge exists
    bool hasEdge(int u, int v) {
        return adjMatrix[u][v] == 1;
    }
};

int main() {
    Graph g(4);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 3);
    
    g.display();
    return 0;
}
```

## Space and Time Complexity

| Aspect | Complexity |
|--------|------------|
| Space Complexity | O(V²) |
| Add Edge | O(1) |
| Remove Edge | O(1) |
| Check Edge | O(1) |
| Find Neighbors | O(V) |

## Advantages
1. **Constant Time Edge Check**: Checking if an edge exists between two vertices takes O(1) time.
2. **Simple Implementation**: Easy to understand and code for small graphs.
3. **Good for Dense Graphs**: Efficient when the number of edges is close to V².

## Disadvantages
1. **Space Inefficient**: Always uses O(V²) space regardless of the number of edges. Not suitable for sparse graphs.
2. **Slow Vertex Iteration**: Finding all neighbors of a vertex requires scanning the entire row, taking O(V) time.
3. **Difficult Scaling**: Resizing the matrix when adding more vertices is expensive.

## Use Cases
- Small graphs with fewer than a few thousand vertices.
- Dense graphs where E ≈ V².
- All-pairs shortest path algorithms like Floyd-Warshall.
- Situations where edge existence checks are frequent.
