# README.md - Graph Representations

## 📖 Overview

Graphs are non-linear data structures consisting of vertices (nodes) and edges (connections between vertices). Choosing the right graph representation is crucial for algorithm efficiency. This guide covers all major graph representations, their trade-offs, and when to use each.

---

## 🎯 Why Graph Representations Matter

| Representation | Space | Add Edge | Check Edge | Iterate Neighbors | Use Case |
|----------------|-------|----------|------------|-------------------|----------|
| **Adjacency Matrix** | O(V²) | O(1) | O(1) | O(V) | Dense graphs |
| **Adjacency List** | O(V+E) | O(1) | O(V) | O(degree) | Sparse graphs |
| **Edge List** | O(E) | O(1) | O(E) | O(E) | Simple edge processing |
| **Incidence Matrix** | O(V×E) | O(1) | O(E) | O(E) | Hypergraphs |

---

## 📊 Graph Terminology

### Basic Terms

| Term | Definition | Example |
|------|------------|---------|
| **Vertex (Node)** | Fundamental unit | City in a map |
| **Edge** | Connection between vertices | Road between cities |
| **Degree** | Number of edges incident to vertex | Number of roads from city |
| **Path** | Sequence of vertices connected by edges | Route from A to B |
| **Cycle** | Path that starts and ends at same vertex | Loop in a graph |
| **Connected Component** | Maximal set of connected vertices | Isolated clusters |

### Graph Types

```
Undirected Graph:            Directed Graph (Digraph):
    1 --- 2                      1 → 2
    |     |                      ↑   ↓
    4 --- 3                      4 ← 3

Weighted Graph:               Unweighted Graph:
    1 ---5--- 2                   1 --- 2
    |         |                   |     |
    2         3                   4 --- 3
    4 ---1--- 3
```

---

## 🗂️ Graph Representations

### 1. Adjacency Matrix

A 2D array where `matrix[i][j] = 1` if there's an edge from vertex i to vertex j.

```cpp
class AdjacencyMatrix {
private:
    int** matrix;
    int vertices;
    
public:
    AdjacencyMatrix(int v) : vertices(v) {
        matrix = new int*[v];
        for (int i = 0; i < v; i++) {
            matrix[i] = new int[v]();
        }
    }
    
    void addEdge(int u, int v, int weight = 1) {
        matrix[u][v] = weight;
        matrix[v][u] = weight;  // For undirected
    }
    
    bool hasEdge(int u, int v) {
        return matrix[u][v] != 0;
    }
};
```

### 2. Adjacency List

Array of lists where list[i] contains all vertices adjacent to vertex i.

```cpp
class AdjacencyList {
private:
    vector<vector<int>> adj;
    
public:
    AdjacencyList(int v) : adj(v) {}
    
    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u);  // For undirected
    }
    
    vector<int> getNeighbors(int u) {
        return adj[u];
    }
};
```

### 3. Edge List

Simple list of all edges, each as a pair (u, v).

```cpp
struct Edge {
    int u, v, weight;
    Edge(int u, int v, int w = 1) : u(u), v(v), weight(w) {}
};

class EdgeList {
private:
    vector<Edge> edges;
    
public:
    void addEdge(int u, int v, int w = 1) {
        edges.emplace_back(u, v, w);
    }
    
    vector<Edge> getAllEdges() {
        return edges;
    }
};
```

### 4. Incidence Matrix

Matrix where rows represent vertices, columns represent edges.

```cpp
class IncidenceMatrix {
private:
    vector<vector<int>> matrix;
    int vertices;
    int edgeCount;
    
public:
    IncidenceMatrix(int v) : vertices(v), edgeCount(0) {
        matrix.resize(v);
    }
    
    void addEdge(int u, int v) {
        for (int i = 0; i < vertices; i++) {
            matrix[i].push_back(0);
        }
        matrix[u][edgeCount] = 1;
        matrix[v][edgeCount] = 1;
        edgeCount++;
    }
};
```

---

## 📈 Representation Comparison

### Space Complexity

| Graph Type | Adjacency Matrix | Adjacency List | Edge List |
|------------|------------------|----------------|-----------|
| **Dense (E ≈ V²)** | O(V²) | O(V²) | O(V²) |
| **Sparse (E ≈ V)** | O(V²) | O(V+E) = O(V) | O(V) |

### Time Complexity for Operations

| Operation | Matrix | List | Edge List |
|-----------|--------|------|-----------|
| **Add Edge** | O(1) | O(1) | O(1) |
| **Remove Edge** | O(1) | O(V) | O(E) |
| **Check Edge** | O(1) | O(V) | O(E) |
| **Get Neighbors** | O(V) | O(degree) | O(E) |
| **Iterate all edges** | O(V²) | O(V+E) | O(E) |

---

## 📚 Folder Structure

```
04_Graph_Representations/
├── README.md                       # This file - Complete guide
├── 01_Graph_Basics.md              # Graph terminology and types
├── 02_Adjacency_Matrix.md          # Matrix representation
├── 03_Adjacency_List.md            # List representation
├── 04_Edge_List.md                 # Edge list representation
└── 05_Comparison.md                # When to use which representation
```

---

## 🚀 Learning Path

```
1. Graph_Basics.md          → Understand graph terminology
           ↓
2. Adjacency_Matrix.md      → Learn matrix representation
           ↓
3. Adjacency_List.md        → Learn list representation
           ↓
4. Edge_List.md             → Learn edge list representation
           ↓
5. Comparison.md            → Choose the right representation
```

---

## ✅ Key Takeaways

1. **Adjacency Matrix** is best for dense graphs with frequent edge checks
2. **Adjacency List** is best for sparse graphs with neighbor iteration
3. **Edge List** is best for algorithms processing all edges
4. **Space-time trade-off** between representations
5. **Directed vs undirected** affects memory usage
6. **Weighted graphs** require storing weights
7. **Choice of representation** impacts algorithm efficiency

---