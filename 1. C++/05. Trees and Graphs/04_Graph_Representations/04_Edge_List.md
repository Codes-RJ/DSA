# Edge List Representation

## 📖 Overview

The edge list is the simplest graph representation, storing all edges in a list (or vector) of pairs. Each edge is represented as a tuple (u, v) for unweighted graphs or (u, v, weight) for weighted graphs. This representation is particularly useful for algorithms that process all edges sequentially, such as Kruskal's algorithm for minimum spanning trees.

---

## 🎯 What is an Edge List?

### Definition

An edge list is a collection of all edges in a graph, where each edge is stored as:
- `(u, v)` for unweighted graphs
- `(u, v, weight)` for weighted graphs

### Visual Example

```
Graph:                    Edge List:
    1 --- 2               (1, 2)
    |     |               (1, 4)
    |     |               (2, 3)
    4 --- 3               (3, 4)

Each edge appears once (unlike adjacency list)
```

---

## 📝 Implementation

### Basic Edge List (Unweighted)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class EdgeList {
private:
    struct Edge {
        int u, v;
        Edge(int from, int to) : u(from), v(to) {}
    };
    
    vector<Edge> edges;
    int vertices;
    bool isDirected;
    
public:
    EdgeList(int v, bool directed = false) 
        : vertices(v), isDirected(directed) {}
    
    void addEdge(int u, int v) {
        if (u < 0 || u >= vertices || v < 0 || v >= vertices) {
            cout << "Invalid vertex!" << endl;
            return;
        }
        edges.push_back(Edge(u, v));
    }
    
    void removeEdge(int u, int v) {
        edges.erase(remove_if(edges.begin(), edges.end(),
            [u, v](const Edge& e) {
                return (e.u == u && e.v == v) ||
                       (!isDirected && e.u == v && e.v == u);
            }), edges.end());
    }
    
    bool hasEdge(int u, int v) {
        for (const Edge& e : edges) {
            if (e.u == u && e.v == v) return true;
            if (!isDirected && e.u == v && e.v == u) return true;
        }
        return false;
    }
    
    int getDegree(int u) {
        int degree = 0;
        for (const Edge& e : edges) {
            if (e.u == u || (!isDirected && e.v == u)) degree++;
            if (isDirected && e.v == u) degree++;
        }
        return degree;
    }
    
    vector<int> getNeighbors(int u) {
        vector<int> neighbors;
        for (const Edge& e : edges) {
            if (e.u == u) neighbors.push_back(e.v);
            if (!isDirected && e.v == u) neighbors.push_back(e.u);
        }
        return neighbors;
    }
    
    void display() {
        cout << "Edge List:" << endl;
        for (const Edge& e : edges) {
            cout << "  " << e.u << " -- " << e.v << endl;
        }
    }
    
    int getEdgeCount() const {
        return edges.size();
    }
    
    const vector<Edge>& getAllEdges() const {
        return edges;
    }
};
```

---

## 💪 Weighted Edge List

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class WeightedEdgeList {
public:
    struct Edge {
        int u, v, weight;
        Edge(int from, int to, int w) : u(from), v(to), weight(w) {}
        
        // For sorting edges by weight
        bool operator<(const Edge& other) const {
            return weight < other.weight;
        }
    };
    
private:
    vector<Edge> edges;
    int vertices;
    bool isDirected;
    
public:
    WeightedEdgeList(int v, bool directed = false) 
        : vertices(v), isDirected(directed) {}
    
    void addEdge(int u, int v, int weight) {
        if (u < 0 || u >= vertices || v < 0 || v >= vertices) {
            cout << "Invalid vertex!" << endl;
            return;
        }
        edges.push_back(Edge(u, v, weight));
    }
    
    void removeEdge(int u, int v) {
        edges.erase(remove_if(edges.begin(), edges.end(),
            [u, v](const Edge& e) {
                return (e.u == u && e.v == v) ||
                       (!isDirected && e.u == v && e.v == u);
            }), edges.end());
    }
    
    bool hasEdge(int u, int v) {
        for (const Edge& e : edges) {
            if (e.u == u && e.v == v) return true;
            if (!isDirected && e.u == v && e.v == u) return true;
        }
        return false;
    }
    
    int getWeight(int u, int v) {
        for (const Edge& e : edges) {
            if (e.u == u && e.v == v) return e.weight;
            if (!isDirected && e.u == v && e.v == u) return e.weight;
        }
        return -1;
    }
    
    vector<Edge> getEdges() const {
        return edges;
    }
    
    void sortEdgesByWeight() {
        sort(edges.begin(), edges.end());
    }
    
    void display() {
        cout << "Weighted Edge List:" << endl;
        for (const Edge& e : edges) {
            cout << "  " << e.u << " -- " << e.v 
                 << " (weight = " << e.weight << ")" << endl;
        }
    }
    
    int getEdgeCount() const {
        return edges.size();
    }
};
```

---

## 📊 Complete Example

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Graph {
private:
    struct Edge {
        int u, v;
        Edge(int from, int to) : u(from), v(to) {}
    };
    
    vector<Edge> edges;
    int vertices;
    bool isDirected;
    
public:
    Graph(int v, bool directed = false) : vertices(v), isDirected(directed) {}
    
    void addEdge(int u, int v) {
        edges.push_back(Edge(u, v));
    }
    
    bool hasEdge(int u, int v) {
        for (const Edge& e : edges) {
            if (e.u == u && e.v == v) return true;
            if (!isDirected && e.u == v && e.v == u) return true;
        }
        return false;
    }
    
    int getDegree(int u) {
        int degree = 0;
        for (const Edge& e : edges) {
            if (e.u == u) degree++;
            if (!isDirected && e.v == u) degree++;
        }
        return degree;
    }
    
    vector<int> getNeighbors(int u) {
        vector<int> neighbors;
        for (const Edge& e : edges) {
            if (e.u == u) neighbors.push_back(e.v);
            if (!isDirected && e.v == u) neighbors.push_back(e.u);
        }
        return neighbors;
    }
    
    void display() {
        cout << "\nEdge List:" << endl;
        for (const Edge& e : edges) {
            cout << "  " << e.u << " -- " << e.v << endl;
        }
    }
    
    void printGraph() {
        cout << "\nGraph Details:" << endl;
        cout << "Type: " << (isDirected ? "Directed" : "Undirected") << endl;
        cout << "Vertices: " << vertices << endl;
        cout << "Edges: " << edges.size() << endl;
        
        cout << "\nVertex Information:" << endl;
        for (int i = 0; i < vertices; i++) {
            cout << "Vertex " << i << ": degree = " << getDegree(i);
            cout << ", neighbors: ";
            vector<int> neighbors = getNeighbors(i);
            sort(neighbors.begin(), neighbors.end());
            for (int n : neighbors) {
                cout << n << " ";
            }
            cout << endl;
        }
    }
    
    // Kruskal's algorithm requires sorted edges
    vector<Edge> getAllEdges() const {
        return edges;
    }
    
    int getVertexCount() const {
        return vertices;
    }
};

// Weighted graph for Kruskal's algorithm demonstration
class WeightedGraph {
public:
    struct Edge {
        int u, v, weight;
        Edge(int from, int to, int w) : u(from), v(to), weight(w) {}
    };
    
private:
    vector<Edge> edges;
    int vertices;
    
public:
    WeightedGraph(int v) : vertices(v) {}
    
    void addEdge(int u, int v, int weight) {
        edges.push_back(Edge(u, v, weight));
    }
    
    void sortEdges() {
        sort(edges.begin(), edges.end(),
            [](const Edge& a, const Edge& b) {
                return a.weight < b.weight;
            });
    }
    
    void display() {
        cout << "\nWeighted Edge List:" << endl;
        for (const Edge& e : edges) {
            cout << "  " << e.u << " -- " << e.v 
                 << " (weight = " << e.weight << ")" << endl;
        }
    }
    
    vector<Edge> getEdges() const {
        return edges;
    }
};

int main() {
    cout << "=== Edge List Representation ===" << endl;
    
    // Undirected graph
    cout << "\n1. Undirected Graph:" << endl;
    Graph g1(4, false);
    g1.addEdge(0, 1);
    g1.addEdge(0, 2);
    g1.addEdge(0, 3);
    g1.addEdge(1, 2);
    g1.addEdge(1, 3);
    g1.addEdge(2, 3);
    
    g1.display();
    g1.printGraph();
    
    // Directed graph
    cout << "\n2. Directed Graph:" << endl;
    Graph g2(4, true);
    g2.addEdge(0, 1);
    g2.addEdge(0, 2);
    g2.addEdge(1, 2);
    g2.addEdge(2, 3);
    g2.addEdge(3, 0);
    
    g2.display();
    g2.printGraph();
    
    // Weighted graph for Kruskal's algorithm
    cout << "\n3. Weighted Graph (for Kruskal's algorithm):" << endl;
    WeightedGraph g3(4);
    g3.addEdge(0, 1, 10);
    g3.addEdge(0, 2, 6);
    g3.addEdge(0, 3, 5);
    g3.addEdge(1, 3, 15);
    g3.addEdge(2, 3, 4);
    
    g3.display();
    
    cout << "\n4. Testing Operations:" << endl;
    Graph g4(3, false);
    g4.addEdge(0, 1);
    g4.addEdge(1, 2);
    
    cout << "Initial graph:" << endl;
    g4.display();
    
    cout << "\nCheck edge (0,1): " << (g4.hasEdge(0, 1) ? "Yes" : "No") << endl;
    cout << "Check edge (0,2): " << (g4.hasEdge(0, 2) ? "Yes" : "No") << endl;
    
    // Note: Edge list doesn't have direct add/remove operations
    // To add/remove, we would need to rebuild the list
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Add Edge** | O(1) | O(1) |
| **Remove Edge** | O(E) | O(1) |
| **Check Edge** | O(E) | O(1) |
| **Get Degree** | O(E) | O(1) |
| **Get Neighbors** | O(E) | O(degree) |
| **Space** | O(E) | O(E) |

---

## ✅ Advantages and Disadvantages

### Advantages

| Advantage | Description |
|-----------|-------------|
| **Simple implementation** | Just a list of edges |
| **Space efficient** | O(E) space only |
| **Good for edge processing** | Algorithms that process all edges |
| **Easy to sort** | Sort edges by weight for Kruskal |
| **Memory contiguous** | Cache-friendly (if using vector) |

### Disadvantages

| Disadvantage | Description |
|--------------|-------------|
| **Slow edge lookup** | O(E) to find edge |
| **No direct neighbor access** | Need to scan all edges |
| **Not good for BFS/DFS** | Inefficient for traversal |
| **Duplicate edges possible** | No automatic duplicate detection |

---

## 🎯 When to Use Edge List

| Use When | Avoid When |
|----------|------------|
| Kruskal's algorithm (MST) | BFS, DFS traversals |
| Processing all edges sequentially | Frequent edge existence checks |
| Edge count is small | Need fast neighbor iteration |
| Sorting edges by weight | Dense graphs |
| Simple edge storage | Dynamic edge updates |

---

## 📊 Representation Comparison

| Feature | Adjacency Matrix | Adjacency List | Edge List |
|---------|-----------------|----------------|-----------|
| **Space** | O(V²) | O(V+E) | O(E) |
| **Edge Check** | O(1) | O(V) | O(E) |
| **Add Edge** | O(1) | O(1) | O(1) |
| **Remove Edge** | O(1) | O(V) | O(E) |
| **Neighbors** | O(V) | O(degree) | O(E) |
| **All Edges** | O(V²) | O(V+E) | O(E) |

---

## ✅ Key Takeaways

1. **Edge list** uses O(E) space - most memory efficient
2. **Simple to implement** - just a list of pairs/tuples
3. **Ideal for Kruskal's algorithm** - sort edges by weight
4. **Slow for edge lookup** - O(E) time
5. **Not good for BFS/DFS** - inefficient neighbor finding
6. **Cache-friendly** - edges stored contiguously in memory
7. **Use for** edge-centric algorithms, not vertex-centric

---
---

## Next Step

- Go to [05_Comparison_of_Representations.md](05_Comparison_of_Representations.md) to continue with Comparison of Representations.
