# Adjacency Matrix Representation

## 📖 Overview

The adjacency matrix is a 2D array representation of a graph where each cell `matrix[i][j]` indicates whether there's an edge from vertex `i` to vertex `j`. It's the simplest graph representation and provides O(1) edge lookup, but requires O(V²) space, making it ideal for dense graphs.

---

## 🎯 What is an Adjacency Matrix?

### Definition

For a graph with V vertices, the adjacency matrix is a V × V matrix where:

```
matrix[i][j] = 1 (or weight) if there's an edge from i to j
matrix[i][j] = 0 if there's no edge
```

### Visual Example (Undirected Graph)

```
Graph:                    Adjacency Matrix:
    1 --- 2               |   1   2   3   4
    |     |             1 |   0   1   1   1
    |     |             2 |   1   0   1   1
    4 --- 3             3 |   1   1   0   1
                        4 |   1   1   1   0

The matrix is symmetric for undirected graphs
```

### Visual Example (Directed Graph)

```
Graph:                    Adjacency Matrix:
    1 → 2                 |   1   2   3   4
    ↑   ↓               1 |   0   1   0   0
    |   ↓               2 |   0   0   1   0
    4 ← 3               3 |   0   0   0   1
                        4 |   1   0   0   0

The matrix may not be symmetric for directed graphs
```

---

## 📝 Implementation

### Basic Adjacency Matrix (Unweighted)

```cpp
#include <iostream>
#include <vector>
using namespace std;

class AdjacencyMatrix {
private:
    vector<vector<int>> matrix;
    int vertices;
    bool isDirected;
    
public:
    // Constructor
    AdjacencyMatrix(int v, bool directed = false) 
        : vertices(v), isDirected(directed) {
        matrix.resize(v, vector<int>(v, 0));
    }
    
    // Add edge
    void addEdge(int u, int v) {
        // Validate vertices
        if (u < 0 || u >= vertices || v < 0 || v >= vertices) {
            cout << "Invalid vertex!" << endl;
            return;
        }
        
        matrix[u][v] = 1;
        if (!isDirected) {
            matrix[v][u] = 1;  // Undirected: add both directions
        }
    }
    
    // Remove edge
    void removeEdge(int u, int v) {
        if (u < 0 || u >= vertices || v < 0 || v >= vertices) {
            cout << "Invalid vertex!" << endl;
            return;
        }
        
        matrix[u][v] = 0;
        if (!isDirected) {
            matrix[v][u] = 0;
        }
    }
    
    // Check if edge exists
    bool hasEdge(int u, int v) {
        if (u < 0 || u >= vertices || v < 0 || v >= vertices) {
            return false;
        }
        return matrix[u][v] != 0;
    }
    
    // Get degree of vertex
    int getDegree(int u) {
        if (u < 0 || u >= vertices) return -1;
        
        int degree = 0;
        for (int v = 0; v < vertices; v++) {
            if (matrix[u][v] != 0) degree++;
        }
        
        if (!isDirected) return degree;
        
        // For directed graph, degree = indegree + outdegree
        int indegree = 0;
        for (int v = 0; v < vertices; v++) {
            if (matrix[v][u] != 0) indegree++;
        }
        return degree + indegree;
    }
    
    // Get neighbors of vertex
    vector<int> getNeighbors(int u) {
        vector<int> neighbors;
        if (u < 0 || u >= vertices) return neighbors;
        
        for (int v = 0; v < vertices; v++) {
            if (matrix[u][v] != 0) {
                neighbors.push_back(v);
            }
        }
        return neighbors;
    }
    
    // Display the matrix
    void display() {
        cout << "Adjacency Matrix:" << endl;
        cout << "  ";
        for (int i = 0; i < vertices; i++) {
            cout << i << " ";
        }
        cout << endl;
        
        for (int i = 0; i < vertices; i++) {
            cout << i << " ";
            for (int j = 0; j < vertices; j++) {
                cout << matrix[i][j] << " ";
            }
            cout << endl;
        }
    }
};
```

---

## 💪 Weighted Adjacency Matrix

```cpp
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class WeightedAdjacencyMatrix {
private:
    vector<vector<int>> matrix;
    int vertices;
    bool isDirected;
    
public:
    WeightedAdjacencyMatrix(int v, bool directed = false) 
        : vertices(v), isDirected(directed) {
        // Initialize with INF (no edge)
        matrix.resize(v, vector<int>(v, INT_MAX));
        
        // Diagonal elements are 0
        for (int i = 0; i < v; i++) {
            matrix[i][i] = 0;
        }
    }
    
    // Add edge with weight
    void addEdge(int u, int v, int weight) {
        if (u < 0 || u >= vertices || v < 0 || v >= vertices) {
            cout << "Invalid vertex!" << endl;
            return;
        }
        
        matrix[u][v] = weight;
        if (!isDirected) {
            matrix[v][u] = weight;
        }
    }
    
    // Remove edge (set to INF)
    void removeEdge(int u, int v) {
        if (u < 0 || u >= vertices || v < 0 || v >= vertices) {
            cout << "Invalid vertex!" << endl;
            return;
        }
        
        matrix[u][v] = INT_MAX;
        if (!isDirected) {
            matrix[v][u] = INT_MAX;
        }
    }
    
    // Get edge weight
    int getWeight(int u, int v) {
        if (u < 0 || u >= vertices || v < 0 || v >= vertices) {
            return INT_MAX;
        }
        return matrix[u][v];
    }
    
    // Check if edge exists
    bool hasEdge(int u, int v) {
        return matrix[u][v] != INT_MAX;
    }
    
    // Display matrix
    void display() {
        cout << "Weighted Adjacency Matrix:" << endl;
        cout << "    ";
        for (int i = 0; i < vertices; i++) {
            cout << i << "  ";
        }
        cout << endl;
        
        for (int i = 0; i < vertices; i++) {
            cout << i << " ";
            for (int j = 0; j < vertices; j++) {
                if (matrix[i][j] == INT_MAX) {
                    cout << "∞ ";
                } else {
                    cout << matrix[i][j] << " ";
                }
                if (matrix[i][j] < 10) cout << " ";
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
#include <iomanip>
using namespace std;

class Graph {
private:
    vector<vector<int>> adj;
    int vertices;
    bool isDirected;
    
public:
    Graph(int v, bool directed = false) : vertices(v), isDirected(directed) {
        adj.resize(v, vector<int>(v, 0));
    }
    
    void addEdge(int u, int v, int weight = 1) {
        adj[u][v] = weight;
        if (!isDirected) adj[v][u] = weight;
    }
    
    void removeEdge(int u, int v) {
        adj[u][v] = 0;
        if (!isDirected) adj[v][u] = 0;
    }
    
    bool hasEdge(int u, int v) {
        return adj[u][v] != 0;
    }
    
    int getDegree(int u) {
        int deg = 0;
        for (int v = 0; v < vertices; v++) {
            if (adj[u][v] != 0) deg++;
        }
        if (!isDirected) return deg;
        
        int indeg = 0;
        for (int v = 0; v < vertices; v++) {
            if (adj[v][u] != 0) indeg++;
        }
        return deg + indeg;
    }
    
    vector<int> getNeighbors(int u) {
        vector<int> neighbors;
        for (int v = 0; v < vertices; v++) {
            if (adj[u][v] != 0) neighbors.push_back(v);
        }
        return neighbors;
    }
    
    void printMatrix() {
        cout << "\nAdjacency Matrix:" << endl;
        cout << "   ";
        for (int i = 0; i < vertices; i++) {
            cout << setw(3) << i;
        }
        cout << endl;
        
        for (int i = 0; i < vertices; i++) {
            cout << setw(2) << i << " ";
            for (int j = 0; j < vertices; j++) {
                cout << setw(3) << adj[i][j];
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
            for (int j = 0; j < vertices; j++) {
                if (adj[i][j] != 0) edges++;
            }
        }
        if (!isDirected) edges /= 2;
        cout << "Edges: " << edges << endl;
        
        cout << "\nVertex Information:" << endl;
        for (int i = 0; i < vertices; i++) {
            cout << "Vertex " << i << ": degree = " << getDegree(i);
            cout << ", neighbors: ";
            vector<int> neighbors = getNeighbors(i);
            for (int n : neighbors) {
                cout << n << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    cout << "=== Adjacency Matrix Representation ===" << endl;
    
    // Create undirected graph
    cout << "\n1. Undirected Graph:" << endl;
    Graph g1(4, false);
    g1.addEdge(0, 1);
    g1.addEdge(0, 2);
    g1.addEdge(0, 3);
    g1.addEdge(1, 2);
    g1.addEdge(1, 3);
    g1.addEdge(2, 3);
    
    g1.printMatrix();
    g1.printGraph();
    
    // Create directed graph
    cout << "\n2. Directed Graph:" << endl;
    Graph g2(4, true);
    g2.addEdge(0, 1);
    g2.addEdge(0, 2);
    g2.addEdge(1, 2);
    g2.addEdge(2, 3);
    g2.addEdge(3, 0);
    
    g2.printMatrix();
    g2.printGraph();
    
    // Test operations
    cout << "\n3. Testing Operations:" << endl;
    Graph g3(3, false);
    g3.addEdge(0, 1);
    g3.addEdge(1, 2);
    
    cout << "Initial graph:" << endl;
    g3.printMatrix();
    
    cout << "\nCheck edge (0,1): " << (g3.hasEdge(0, 1) ? "Yes" : "No") << endl;
    cout << "Check edge (0,2): " << (g3.hasEdge(0, 2) ? "Yes" : "No") << endl;
    
    g3.addEdge(0, 2);
    cout << "\nAfter adding edge (0,2):" << endl;
    g3.printMatrix();
    
    g3.removeEdge(1, 2);
    cout << "\nAfter removing edge (1,2):" << endl;
    g3.printMatrix();
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Add Edge** | O(1) | O(1) |
| **Remove Edge** | O(1) | O(1) |
| **Check Edge** | O(1) | O(1) |
| **Get Degree** | O(V) | O(1) |
| **Get Neighbors** | O(V) | O(V) |
| **Space** | O(V²) | O(V²) |

---

## ✅ Advantages and Disadvantages

### Advantages

| Advantage | Description |
|-----------|-------------|
| **O(1) edge lookup** | Constant time to check if edge exists |
| **Simple implementation** | Easy to understand and code |
| **Fast edge updates** | Add/remove edges in O(1) |
| **Good for dense graphs** | When E ≈ V², space is optimal |

### Disadvantages

| Disadvantage | Description |
|--------------|-------------|
| **O(V²) space** | Wastes space for sparse graphs |
| **Slow neighbor iteration** | O(V) to find all neighbors |
| **Poor for large V** | Memory becomes prohibitive |
| **Not dynamic** | Resizing matrix is expensive |

---

## 🎯 When to Use Adjacency Matrix

| Use When | Avoid When |
|----------|------------|
| Graph is dense (E ≈ V²) | Graph is sparse (E ≈ V) |
| Frequent edge existence checks | Frequent neighbor iteration |
| V is small (< 1000) | V is large (> 10000) |
| Floyd-Warshall algorithm | BFS/DFS on large graphs |
| All-pairs shortest path | Memory is limited |

---

## ✅ Key Takeaways

1. **Adjacency matrix** uses O(V²) space
2. **Edge lookup** is O(1) - fastest possible
3. **Symmetric** for undirected graphs
4. **Best for dense graphs** (many edges)
5. **Simple to implement** and understand
6. **Not memory efficient** for sparse graphs
7. **Good for** Floyd-Warshall, transitive closure

---