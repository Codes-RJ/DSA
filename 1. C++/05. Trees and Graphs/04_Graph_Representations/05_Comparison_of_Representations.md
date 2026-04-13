# Comparison of Graph Representations

## 📖 Overview

Choosing the right graph representation is crucial for algorithm efficiency. Each representation has its own trade-offs in terms of space, time for various operations, and ease of implementation. This guide provides a comprehensive comparison to help you select the optimal representation for your use case.

---

## 📊 Quick Reference Table

| Operation | Adjacency Matrix | Adjacency List | Edge List |
|-----------|-----------------|----------------|-----------|
| **Space** | O(V²) | O(V+E) | O(E) |
| **Add Edge** | O(1) | O(1) | O(1) |
| **Remove Edge** | O(1) | O(V) | O(E) |
| **Check Edge** | O(1) | O(V) | O(E) |
| **Get Neighbors** | O(V) | O(degree) | O(E) |
| **Get Degree** | O(V) | O(1) | O(E) |
| **Iterate All Edges** | O(V²) | O(V+E) | O(E) |

---

## 📈 Detailed Comparison

### Space Complexity

```
Graph: V = 1000 vertices

Dense graph (E = 500,000):
- Adjacency Matrix: 1,000,000 cells (~4 MB)
- Adjacency List: ~500,000 edges × 2 × 8 bytes = ~8 MB
- Edge List: ~500,000 edges × 16 bytes = ~8 MB

Sparse graph (E = 2000 edges):
- Adjacency Matrix: 1,000,000 cells (~4 MB)
- Adjacency List: ~4,000 pointers + 2000 edges = ~32 KB
- Edge List: ~2000 edges × 16 bytes = ~32 KB

Conclusion: 
- Dense graphs → Adjacency Matrix is better
- Sparse graphs → Adjacency List/Edge List are better
```

### Time Complexity for Common Operations

```
Graph: V = 1000, E = 2000 (sparse)

Check if edge (u, v) exists:
- Matrix: O(1) → 1 operation
- List: O(V) worst → up to 1000 operations
- Edge List: O(E) worst → up to 2000 operations

Find all neighbors of vertex u:
- Matrix: O(V) → 1000 operations
- List: O(degree) → average 2 operations
- Edge List: O(E) → 2000 operations

Add new edge (u, v):
- Matrix: O(1) → 1 operation
- List: O(1) → 1 operation
- Edge List: O(1) → 1 operation
```

---

## 🎯 Algorithm-Specific Recommendations

### Graph Traversal (BFS, DFS)

| Algorithm | Best Representation | Reason |
|-----------|---------------------|--------|
| **BFS** | Adjacency List | Need to iterate neighbors efficiently |
| **DFS** | Adjacency List | Need to iterate neighbors efficiently |

### Shortest Path Algorithms

| Algorithm | Best Representation | Reason |
|-----------|---------------------|--------|
| **Dijkstra** | Adjacency List | Need to iterate neighbors |
| **Bellman-Ford** | Edge List | Need to iterate all edges |
| **Floyd-Warshall** | Adjacency Matrix | Need O(1) edge lookup |

### Minimum Spanning Tree

| Algorithm | Best Representation | Reason |
|-----------|---------------------|--------|
| **Kruskal** | Edge List | Need to sort edges by weight |
| **Prim** | Adjacency List | Need to iterate neighbors |

### Connectivity Algorithms

| Algorithm | Best Representation | Reason |
|-----------|---------------------|--------|
| **Union-Find** | Edge List | Only need edges |
| **Tarjan's SCC** | Adjacency List | Need neighbor iteration |

---

## 💻 Implementation Comparison

### Adjacency Matrix (Dense Graph)

```cpp
// Best for: Dense graphs, Floyd-Warshall, frequent edge checks
class Graph {
    vector<vector<int>> adj;
    int V;
    
public:
    Graph(int n) : V(n), adj(n, vector<int>(n, 0)) {}
    
    void addEdge(int u, int v) { adj[u][v] = 1; }
    bool hasEdge(int u, int v) { return adj[u][v]; }
    
    // Floyd-Warshall - O(V³)
    void floydWarshall() {
        for (int k = 0; k < V; k++)
            for (int i = 0; i < V; i++)
                for (int j = 0; j < V; j++)
                    if (adj[i][k] && adj[k][j])
                        adj[i][j] = 1;
    }
};
```

### Adjacency List (Sparse Graph)

```cpp
// Best for: Sparse graphs, BFS, DFS, Dijkstra, Prim
class Graph {
    vector<vector<int>> adj;
    int V;
    
public:
    Graph(int n) : V(n), adj(n) {}
    
    void addEdge(int u, int v) { 
        adj[u].push_back(v); 
        adj[v].push_back(u);  // Undirected
    }
    
    // BFS - O(V+E)
    void bfs(int start) {
        vector<bool> visited(V, false);
        queue<int> q;
        visited[start] = true;
        q.push(start);
        
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : adj[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    q.push(v);
                }
            }
        }
    }
};
```

### Edge List (Edge-Centric Algorithms)

```cpp
// Best for: Kruskal, Bellman-Ford, edge processing
class Graph {
    struct Edge { int u, v, w; };
    vector<Edge> edges;
    int V;
    
public:
    Graph(int n) : V(n) {}
    
    void addEdge(int u, int v, int w) { 
        edges.push_back({u, v, w}); 
    }
    
    // Kruskal's algorithm - O(E log E)
    int kruskal() {
        sort(edges.begin(), edges.end(), 
             [](Edge a, Edge b) { return a.w < b.w; });
        
        UnionFind uf(V);
        int mstWeight = 0;
        
        for (Edge e : edges) {
            if (uf.find(e.u) != uf.find(e.v)) {
                uf.unite(e.u, e.v);
                mstWeight += e.w;
            }
        }
        return mstWeight;
    }
    
    // Bellman-Ford - O(V*E)
    vector<int> bellmanFord(int src) {
        vector<int> dist(V, INF);
        dist[src] = 0;
        
        for (int i = 0; i < V - 1; i++) {
            for (Edge e : edges) {
                if (dist[e.u] != INF && dist[e.u] + e.w < dist[e.v]) {
                    dist[e.v] = dist[e.u] + e.w;
                }
            }
        }
        return dist;
    }
};
```

---

## 📊 Decision Tree

```
Start with graph characteristics:

Is graph dense (E ≈ V²)?
├── Yes → Use Adjacency Matrix
│   ├── Need Floyd-Warshall? → Yes, use Matrix
│   └── Need transitive closure? → Yes, use Matrix
│
└── No (graph is sparse)
    ├── Need to iterate neighbors frequently?
    │   ├── Yes → Use Adjacency List
    │   │   ├── BFS/DFS → List
    │   │   ├── Dijkstra → List
    │   │   └── Prim → List
    │   │
    │   └── No → Need to process all edges?
    │       ├── Yes → Use Edge List
    │       │   ├── Kruskal → Edge List
    │       │   └── Bellman-Ford → Edge List
    │       │
    │       └── No → Adjacency List (default)
```

---

## 📊 Summary Table by Use Case

| Use Case | Best Representation | Runner Up |
|----------|---------------------|-----------|
| **Dense Graph** | Adjacency Matrix | - |
| **Sparse Graph** | Adjacency List | Edge List |
| **Frequent edge checks** | Adjacency Matrix | - |
| **Frequent neighbor iteration** | Adjacency List | - |
| **BFS / DFS** | Adjacency List | - |
| **Dijkstra** | Adjacency List | - |
| **Bellman-Ford** | Edge List | - |
| **Kruskal (MST)** | Edge List | - |
| **Prim (MST)** | Adjacency List | - |
| **Floyd-Warshall** | Adjacency Matrix | - |
| **Dynamic graph (add/remove vertices)** | Adjacency List | - |
| **Memory constrained** | Edge List | Adjacency List |

---

## ✅ Key Takeaways

1. **Adjacency Matrix**: Best for dense graphs, O(1) edge checks, Floyd-Warshall
2. **Adjacency List**: Best for sparse graphs, BFS, DFS, Dijkstra, Prim
3. **Edge List**: Best for edge-centric algorithms (Kruskal, Bellman-Ford)
4. **Space-time trade-off**: Matrix uses more space but faster lookups
5. **No single best representation** - depends on the algorithm
6. **Hybrid representations** possible for specialized needs

---

## 📚 Complete Code Example

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <algorithm>
#include <climits>
using namespace std;

// Union-Find for Kruskal
class UnionFind {
    vector<int> parent, rank;
public:
    UnionFind(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++) parent[i] = i;
    }
    
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    
    void unite(int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx != ry) {
            if (rank[rx] < rank[ry]) parent[rx] = ry;
            else if (rank[rx] > rank[ry]) parent[ry] = rx;
            else { parent[ry] = rx; rank[rx]++; }
        }
    }
};

// Graph with multiple representations
class Graph {
private:
    int V;
    bool isDirected;
    
    // All three representations
    vector<vector<int>> matrix;
    vector<vector<int>> adjList;
    struct Edge { int u, v, w; };
    vector<Edge> edgeList;
    
public:
    Graph(int vertices, bool directed = false) 
        : V(vertices), isDirected(directed) {
        matrix.resize(V, vector<int>(V, 0));
        adjList.resize(V);
    }
    
    void addEdge(int u, int v, int weight = 1) {
        // Update matrix
        matrix[u][v] = weight;
        if (!isDirected) matrix[v][u] = weight;
        
        // Update adjacency list
        adjList[u].push_back(v);
        if (!isDirected) adjList[v].push_back(u);
        
        // Update edge list
        edgeList.push_back({u, v, weight});
        if (!isDirected) edgeList.push_back({v, u, weight});
    }
    
    // BFS using adjacency list
    void bfs(int start) {
        vector<bool> visited(V, false);
        queue<int> q;
        visited[start] = true;
        q.push(start);
        
        cout << "BFS: ";
        while (!q.empty()) {
            int u = q.front(); q.pop();
            cout << u << " ";
            for (int v : adjList[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    q.push(v);
                }
            }
        }
        cout << endl;
    }
    
    // DFS using adjacency list
    void dfsUtil(int u, vector<bool>& visited) {
        visited[u] = true;
        cout << u << " ";
        for (int v : adjList[u]) {
            if (!visited[v]) dfsUtil(v, visited);
        }
    }
    
    void dfs(int start) {
        vector<bool> visited(V, false);
        cout << "DFS: ";
        dfsUtil(start, visited);
        cout << endl;
    }
    
    // Kruskal using edge list
    int kruskal() {
        vector<Edge> edges = edgeList;
        // Remove duplicates for undirected graphs
        if (!isDirected) {
            vector<Edge> unique;
            for (size_t i = 0; i < edges.size(); i += 2) {
                unique.push_back(edges[i]);
            }
            edges = unique;
        }
        
        sort(edges.begin(), edges.end(),
             [](const Edge& a, const Edge& b) { return a.w < b.w; });
        
        UnionFind uf(V);
        int mstWeight = 0;
        vector<Edge> mst;
        
        for (Edge e : edges) {
            if (uf.find(e.u) != uf.find(e.v)) {
                uf.unite(e.u, e.v);
                mstWeight += e.w;
                mst.push_back(e);
            }
        }
        
        cout << "Kruskal MST weight: " << mstWeight << endl;
        cout << "MST edges: ";
        for (Edge e : mst) {
            cout << "(" << e.u << "," << e.v << ") ";
        }
        cout << endl;
        
        return mstWeight;
    }
    
    // Floyd-Warshall using matrix
    void floydWarshall() {
        vector<vector<int>> dist = matrix;
        
        // Initialize distances
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (i != j && dist[i][j] == 0) dist[i][j] = INT_MAX / 2;
            }
        }
        
        for (int k = 0; k < V; k++) {
            for (int i = 0; i < V; i++) {
                for (int j = 0; j < V; j++) {
                    if (dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }
        
        cout << "All-pairs shortest paths:" << endl;
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (dist[i][j] >= INT_MAX / 2) cout << "∞ ";
                else cout << dist[i][j] << " ";
            }
            cout << endl;
        }
    }
    
    void display() {
        cout << "\nGraph: V=" << V << ", " 
             << (isDirected ? "Directed" : "Undirected") << endl;
        
        cout << "\nAdjacency Matrix:" << endl;
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                cout << matrix[i][j] << " ";
            }
            cout << endl;
        }
        
        cout << "\nAdjacency List:" << endl;
        for (int i = 0; i < V; i++) {
            cout << i << ": ";
            for (int v : adjList[i]) cout << v << " ";
            cout << endl;
        }
        
        cout << "\nEdge List:" << endl;
        for (Edge e : edgeList) {
            cout << "  " << e.u << " - " << e.v;
            if (e.w != 1) cout << " (w=" << e.w << ")";
            cout << endl;
        }
    }
};

int main() {
    cout << "=== Graph Representations Comparison ===" << endl;
    
    // Create weighted undirected graph
    Graph g(5, false);
    g.addEdge(0, 1, 10);
    g.addEdge(0, 2, 6);
    g.addEdge(0, 3, 5);
    g.addEdge(1, 3, 15);
    g.addEdge(2, 3, 4);
    g.addEdge(3, 4, 8);
    
    g.display();
    
    cout << "\n=== Algorithm Demonstrations ===" << endl;
    g.bfs(0);
    g.dfs(0);
    g.kruskal();
    g.floydWarshall();
    
    return 0;
}
```

---

## ✅ Final Recommendations

| If you need... | Use... |
|----------------|--------|
| Fast edge existence checks | Adjacency Matrix |
| Fast neighbor iteration | Adjacency List |
| Memory efficiency for sparse graphs | Adjacency List |
| Simple edge processing | Edge List |
| Floyd-Warshall algorithm | Adjacency Matrix |
| BFS/DFS traversal | Adjacency List |
| Kruskal's algorithm | Edge List |
| Dijkstra's algorithm | Adjacency List |
| Bellman-Ford algorithm | Edge List |

---
---

## Next Step

- Go to [README.md](README.md) to continue.
