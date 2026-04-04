# Adjacency List Representation

## Introduction
An adjacency list represents a graph as an array of lists. Each element of the array represents a vertex, and the list at that index contains all the vertices to which it is connected.

## Implementation Concept

### Dynamic Array (vector) or Linked List
In C++, adjacency lists are most efficiently implemented using `std::vector<int> adj[V]` or `std::vector<std::vector<int>>`. Each vector stores the neighbors of a vertex.

### Undirected Graph
An edge between `u` and `v` is stored twice: `v` is added to `adj[u]` and `u` is added to `adj[v]`.

### Directed Graph
An edge from `u` to `v` is stored once: `v` is added to `adj[u]`.

## C++ Implementation

```cpp
#include <iostream>
#include <vector>
#include <list>

using namespace std;

class Graph {
private:
    int V;
    vector<vector<int>> adjList;

public:
    Graph(int V) {
        this->V = V;
        adjList.resize(V);
    }

    // Add edge for undirected graph
    void addEdge(int u, int v) {
        adjList[u].push_back(v);
        adjList[v].push_back(u); // For undirected
    }

    // Display the adjacency list
    void display() {
        for (int i = 0; i < V; i++) {
            cout << "Vertex " << i << ": ";
            for (int neighbor : adjList[i]) {
                cout << neighbor << " -> ";
            }
            cout << "NULL" << endl;
        }
    }

    // Check if edge exists
    bool hasEdge(int u, int v) {
        for (int neighbor : adjList[u]) {
            if (neighbor == v) return true;
        }
        return false;
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
| Space Complexity | O(V + E) |
| Add Edge | O(1) (average) |
| Remove Edge | O(E/V) (average) |
| Check Edge | O(V) (worst case) |
| Find Neighbors | O(degree(V)) |

## Advantages
1. **Space Efficient**: Uses memory proportional to the actual number of edges and vertices. Ideal for sparse graphs.
2. **Fast Neighbor Retrieval**: Finding neighbors of a vertex takes time proportional to the number of neighbors, not total vertices.
3. **Easy Vertex Addition**: Adding new vertices or edges is straightforward.

## Disadvantages
1. **Slow Edge Check**: Checking if an edge exists between two specific vertices takes O(V) in the worst case (or degree of node).
2. **Pointer Overhead**: If implemented with linked lists, there is additional memory for pointers.

## Use Cases
- Most real-world graphs (social networks, web graphs) which are typically sparse.
- Large graphs where V² memory is not feasible.
- Graph traversal algorithms like BFS and DFS.
- Finding connected components or shortest paths in sparse graphs.
