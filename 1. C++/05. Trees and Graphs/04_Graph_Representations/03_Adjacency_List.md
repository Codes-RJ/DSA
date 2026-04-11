# Adjacency List Representation

## 📖 Overview

The adjacency list is a space-efficient graph representation where each vertex maintains a list (or vector) of its neighboring vertices. It's the most commonly used representation for real-world graphs because most graphs are sparse (E ≈ V), making it memory-efficient and fast for neighbor iteration.

---

## 🎯 What is an Adjacency List?

### Definition

For a graph with V vertices, we maintain an array of V lists, where `list[i]` contains all vertices adjacent to vertex i.

### Visual Example (Undirected Graph)

```
Graph:                    Adjacency List:
    1 --- 2               1: 2, 3, 4
    |     |               2: 1, 3, 4
    |     |               3: 1, 2, 4
    4 --- 3               4: 1, 2, 3

Each edge appears twice (once for each endpoint)
```

### Visual Example (Directed Graph)

```
Graph:                    Adjacency List:
    1 → 2                1: 2
    ↑   ↓                2: 3
    |   ↓                3: 4
    4 ← 3                4: 1

Each directed edge appears once (from source to destination)
```

---

## 📝 Implementation

### Basic Adjacency List (Unweighted)

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
using namespace std;

class AdjacencyList {
private:
    vector<list<int>> adj;
    int vertices;
    bool isDirected;
    
public:
    // Constructor
    AdjacencyList(int v, bool directed = false) 
        : vertices(v), isDirected(directed) {
        adj.resize(v);
    }
    
    // Add edge
    void addEdge(int u, int v) {
        if (u < 0 || u >= vertices || v < 0 || v >= vertices) {
            cout << "Invalid vertex!" << endl;
            return;
        }
        
        adj[u].push_back(v);
        if (!isDirected) {
            adj[v].push_back(u);
        }
    }
    
    // Remove edge
    void removeEdge(int u, int v) {
        if (u < 0 || u >= vertices || v < 0 || v >= vertices) {
            cout << "Invalid vertex!" << endl;
            return;
        }
        
        adj[u].remove(v);
        if (!isDirected) {
            adj[v].remove(u);
        }
    }
    
    // Check if edge exists
    bool hasEdge(int u, int v) {
        if (u < 0 || u >= vertices) return false;
        
        for (int neighbor : adj[u]) {
            if (neighbor == v) return true;
        }
        return false;
    }
    
    // Get degree of vertex
    int getDegree(int u) {
        if (u < 0 || u >= vertices) return -1;
        
        int degree = adj[u].size();
        
        if (!isDirected) return degree;
        
        // For directed graph, also count incoming edges
        int indegree = 0;
        for (int i = 0; i < vertices; i++) {
            for (int neighbor : adj[i]) {
                if (neighbor == u) indegree++;
            }
        }
        return degree + indegree;
    }
    
    // Get out-degree (for directed graphs)
    int getOutDegree(int u) {
        return adj[u].size();
    }
    
    // Get in-degree (for directed graphs)
    int getInDegree(int u) {
        int indegree = 0;
        for (int i = 0; i < vertices; i++) {
            for (int neighbor : adj[i]) {
                if (neighbor == u) indegree++;
            }
        }
        return indegree;
    }
    
    // Get neighbors of vertex
    vector<int> getNeighbors(int u) {
        vector<int> neighbors;
        if (u < 0 || u >= vertices) return neighbors;
        
        for (int neighbor : adj[u]) {
            neighbors.push_back(neighbor);
        }
        return neighbors;
    }
    
    // Display adjacency list
    void display() {
        cout << "Adjacency List:" << endl;
        for (int i = 0; i < vertices; i++) {
            cout << i << ": ";
            for (int neighbor : adj[i]) {
                cout << neighbor << " ";
            }
            cout << endl;
        }
    }
};
```

---

## 💪 Weighted Adjacency List

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <utility>
using namespace std;

class WeightedAdjacencyList {
private:
    struct Edge {
        int destination;
        int weight;
        
        Edge(int dest, int w) : destination(dest), weight(w) {}
    };
    
    vector<list<Edge>> adj;
    int vertices;
    bool isDirected;
    
public:
    WeightedAdjacencyList(int v, bool directed = false) 
        : vertices(v), isDirected(directed) {
        adj.resize(v);
    }
    
    void addEdge(int u, int v, int weight) {
        if (u < 0 || u >= vertices || v < 0 || v >= vertices) {
            cout << "Invalid vertex!" << endl;
            return;
        }
        
        adj[u].push_back(Edge(v, weight));
        if (!isDirected) {
            adj[v].push_back(Edge(u, weight));
        }
    }
    
    void removeEdge(int u, int v) {
        if (u < 0 || u >= vertices) return;
        
        adj[u].remove_if([v](const Edge& e) { return e.destination == v; });
        
        if (!isDirected) {
            adj[v].remove_if([u](const Edge& e) { return e.destination == u; });
        }
    }
    
    bool hasEdge(int u, int v) {
        if (u < 0 || u >= vertices) return false;
        
        for (const Edge& e : adj[u]) {
            if (e.destination == v) return true;
        }
        return false;
    }
    
    int getWeight(int u, int v) {
        if (u < 0 || u >= vertices) return -1;
        
        for (const Edge& e : adj[u]) {
            if (e.destination == v) return e.weight;
        }
        return -1;
    }
    
    vector<pair<int, int>> getNeighbors(int u) {
        vector<pair<int, int>> neighbors;
        if (u < 0 || u >= vertices) return neighbors;
        
        for (const Edge& e : adj[u]) {
            neighbors.push_back({e.destination, e.weight});
        }
        return neighbors;
    }
    
    void display() {
        cout << "Weighted Adjacency List:" << endl;
        for (int i = 0; i < vertices; i++) {
            cout << i << ": ";
            for (const Edge& e : adj[i]) {
                cout << "(" << e.destination << "," << e.weight << ") ";
            }
            cout << endl;
        }
    }
};
```

---

## 📊 Complete Example

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
using namespace std;

class Graph {
private:
    vector<list<int>> adj;
    int vertices;
    bool isDirected;
    
public:
    Graph(int v, bool directed = false) : vertices(v), isDirected(directed) {
        adj.resize(v);
    }
    
    void addEdge(int u, int v) {
        adj[u].push_back(v);
        if (!isDirected) adj[v].push_back(u);
    }
    
    void removeEdge(int u, int v) {
        adj[u].remove(v);
        if (!isDirected) adj[v].remove(u);
    }
    
    bool hasEdge(int u, int v) {
        for (int neighbor : adj[u]) {
            if (neighbor == v) return true;
        }
        return false;
    }
    
    int getDegree(int u) {
        int deg = adj[u].size();
        if (!isDirected) return deg;
        
        int indeg = 0;
        for (int i = 0; i < vertices; i++) {
            for (int neighbor : adj[i]) {
                if (neighbor == u) indeg++;
            }
        }
        return deg + indeg;
    }
    
    int getOutDegree(int u) {
        return adj[u].size();
    }
    
    int getInDegree(int u) {
        int indeg = 0;
        for (int i = 0; i < vertices; i++) {
            for (int neighbor : adj[i]) {
                if (neighbor == u) indeg++;
            }
        }
        return indeg;
    }
    
    vector<int> getNeighbors(int u) {
        vector<int> neighbors;
        for (int neighbor : adj[u]) {
            neighbors.push_back(neighbor);
        }
        return neighbors;
    }
    
    void display() {
        cout << "\nAdjacency List:" << endl;
        for (int i = 0; i < vertices; i++) {
            cout << i << ": ";
            // Sort neighbors for consistent display
            vector<int> neighbors = getNeighbors(i);
            sort(neighbors.begin(), neighbors.end());
            for (int n : neighbors) {
                cout << n << " ";
            }
            cout << endl;
        }
    }
    
    void printGraph() {
        cout << "\nGraph Details:" << endl;
        cout << "Type: " << (isDirected ? "Directed" : "Undirected") << endl;
        cout << "Vertices: " << vertices << endl;
        
        int edges = 0;
        for (int i = 0; i < vertices; i++) {
            edges += adj[i].size();
        }
        if (!isDirected) edges /= 2;
        cout << "Edges: " << edges << endl;
        
        cout << "\nVertex Information:" << endl;
        for (int i = 0; i < vertices; i++) {
            cout << "Vertex " << i << ": ";
            if (isDirected) {
                cout << "out-degree = " << getOutDegree(i);
                cout << ", in-degree = " << getInDegree(i);
                cout << ", degree = " << getDegree(i);
            } else {
                cout << "degree = " << getDegree(i);
            }
            cout << ", neighbors: ";
            vector<int> neighbors = getNeighbors(i);
            sort(neighbors.begin(), neighbors.end());
            for (int n : neighbors) {
                cout << n << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    cout << "=== Adjacency List Representation ===" << endl;
    
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
    
    // Operations demonstration
    cout << "\n3. Testing Operations:" << endl;
    Graph g3(3, false);
    g3.addEdge(0, 1);
    g3.addEdge(1, 2);
    
    cout << "Initial graph:" << endl;
    g3.display();
    
    cout << "\nCheck edge (0,1): " << (g3.hasEdge(0, 1) ? "Yes" : "No") << endl;
    cout << "Check edge (0,2): " << (g3.hasEdge(0, 2) ? "Yes" : "No") << endl;
    
    g3.addEdge(0, 2);
    cout << "\nAfter adding edge (0,2):" << endl;
    g3.display();
    
    g3.removeEdge(1, 2);
    cout << "\nAfter removing edge (1,2):" << endl;
    g3.display();
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Add Edge** | O(1) | O(1) |
| **Remove Edge** | O(V) (worst) | O(1) |
| **Check Edge** | O(V) | O(1) |
| **Get Degree** | O(1) | O(1) |
| **Get Neighbors** | O(degree) | O(degree) |
| **Space** | O(V+E) | O(V+E) |

---

## ✅ Advantages and Disadvantages

### Advantages

| Advantage | Description |
|-----------|-------------|
| **Space efficient** | O(V+E) space for sparse graphs |
| **Fast neighbor iteration** | O(degree) to traverse neighbors |
| **Dynamic** | Easy to add/remove vertices |
| **Good for BFS/DFS** | Efficient graph traversal |
| **Most common** | Used in real-world applications |

### Disadvantages

| Disadvantage | Description |
|--------------|-------------|
| **Slow edge check** | O(V) to check if edge exists |
| **Not cache-friendly** | Pointers scattered in memory |
| **Overhead** | Extra space for pointers |

---

## 🎯 When to Use Adjacency List

| Use When | Avoid When |
|----------|------------|
| Graph is sparse (E ≈ V) | Graph is dense (E ≈ V²) |
| Frequent neighbor iteration | Frequent edge existence checks |
| Memory is limited | V is very small |
| BFS, DFS, Dijkstra | Floyd-Warshall algorithm |
| Real-world graphs | Complete graphs |

---

## 📊 Representation Comparison

| Feature | Adjacency Matrix | Adjacency List |
|---------|-----------------|----------------|
| **Space** | O(V²) | O(V+E) |
| **Edge Check** | O(1) | O(V) |
| **Add Edge** | O(1) | O(1) |
| **Remove Edge** | O(1) | O(V) |
| **Neighbors** | O(V) | O(degree) |
| **Best for** | Dense graphs | Sparse graphs |

---

## ✅ Key Takeaways

1. **Adjacency list** uses O(V+E) space - optimal for sparse graphs
2. **Fast neighbor iteration** - O(degree) to traverse neighbors
3. **Slower edge lookup** - O(V) in worst case
4. **Most common representation** for real-world graphs
5. **Good for BFS, DFS, Dijkstra** - algorithms that explore neighbors
6. **Dynamic** - easy to add/remove vertices
7. **Memory efficient** for sparse graphs (E ≈ V)

---