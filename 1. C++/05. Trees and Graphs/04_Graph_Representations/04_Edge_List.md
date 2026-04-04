# Edge List Representation

## Introduction
An edge list is perhaps the simplest way to represent a graph. It consists of a simple list (or array) of all edges in the graph. Each edge is usually represented as a pair or triplet (for weighted graphs) of vertices.

## Implementation Concept

### Basic Structure
In C++, an edge list can be implemented as a `vector` of `pairs` or a custom struct.

```cpp
struct Edge {
    int src, dest, weight;
};
vector<Edge> edges;
```

### Representation
For an undirected graph, each edge `{u, v}` is typically stored once, though some algorithms might require storing both `{u, v}` and `{v, u}`.

## C++ Implementation

```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Edge {
    int src, dest, weight;
};

class Graph {
private:
    int V;
    vector<Edge> edges;

public:
    Graph(int V) : V(V) {}

    void addEdge(int u, int v, int w = 1) {
        edges.push_back({u, v, w});
    }

    void display() {
        cout << "Edge List:" << endl;
        for (const auto& edge : edges) {
            cout << edge.src << " --(" << edge.weight << ")--> " << edge.dest << endl;
        }
    }
};

int main() {
    Graph g(4);
    g.addEdge(0, 1, 10);
    g.addEdge(0, 2, 5);
    g.addEdge(1, 2, 2);
    g.addEdge(2, 3, 1);
    
    g.display();
    return 0;
}
```

## Space and Time Complexity

| Aspect | Complexity |
|--------|------------|
| Space Complexity | O(E) |
| Add Edge | O(1) |
| Remove Edge | O(E) |
| Check Edge | O(E) |
| Find Neighbors | O(E) |

## Advantages
1. **Extremely Space Efficient**: Uses exactly O(E) space.
2. **Simple to Sort**: Useful for algorithms that require edges to be sorted by weight.
3. **Easy Modification**: Adding a new edge is just a push operation.

## Disadvantages
1. **Inefficient Queries**: Checking for an edge or finding neighbors requires scanning the entire list of edges.
2. **Lack of Structure**: Doesn't provide easy access to vertex-specific information like degree or neighbors.

## Use Cases
- Algorithms that primarily iterate over edges, such as Kruskal's Algorithm for Minimum Spanning Tree or Bellman-Ford for shortest paths.
- Initial representation when reading graph data from a file (e.g., CSV or text file containing edge pairs).
- Very sparse graphs where E is much smaller than V.
