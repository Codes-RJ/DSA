# README.md

## Graph Representations - Complete Guide

### Overview

A graph is a non-linear data structure consisting of vertices (nodes) and edges (connections between vertices). Graphs model relationships between objects and are fundamental to many real-world applications like social networks, GPS navigation, network routing, and recommendation systems. Choosing the right graph representation is crucial for algorithm efficiency and memory usage.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [01_Graph_Basics.md](01_Graph_Basics.md) | understand Graph Basics (terminology, types) |
| 2. | [02_Adjacency_Matrix.md](02_Adjacency_Matrix.md) | understand Adjacency Matrix Representation |
| 3. | [03_Adjacency_List.md](03_Adjacency_List.md) | understand Adjacency List Representation |
| 4. | [04_Edge_List.md](04_Edge_List.md) | understand Edge List Representation |
| 5. | [05_Comparison_of_Representations.md](05_Comparison_of_Representations.md) | understand Comparison of Graph Representations |
| 6. | [README.md](README.md) | understand Graph Representations Overview |

---

## 1. Graph Basics

This topic introduces fundamental graph terminology and concepts.

**File:** [01_Graph_Basics.md](01_Graph_Basics.md)

**What you will learn:**
- Graph definition (vertices, edges)
- Directed vs Undirected graphs
- Weighted vs Unweighted graphs
- Degree of a vertex (indegree, outdegree)
- Path, cycle, connected components
- Graph applications

**Key Concepts:**

| Term | Definition |
|------|------------|
| **Vertex (Node)** | A point in the graph |
| **Edge** | A connection between two vertices |
| **Directed Graph** | Edges have direction |
| **Undirected Graph** | Edges have no direction (bidirectional) |
| **Weighted Graph** | Edges have associated weights/costs |
| **Degree** | Number of edges incident to a vertex |
| **Indegree** | Number of incoming edges (directed) |
| **Outdegree** | Number of outgoing edges (directed) |
| **Path** | Sequence of vertices connected by edges |
| **Cycle** | Path that starts and ends at same vertex |
| **Connected Component** | Maximal set of connected vertices |

**Graph Types:**
```
Undirected Graph:          Directed Graph:
    1 ----- 2                 1 ---→ 2
    |        |                ↑       |
    |        |                |       ↓
    4 ----- 3                 4 ←--- 3

Weighted Graph:
    1 ----5---- 2
    |           |
    2           3
    |           |
    4 ----1---- 3
```

---

## 2. Adjacency Matrix

This topic explains the adjacency matrix representation using a 2D array.

**File:** [02_Adjacency_Matrix.md](02_Adjacency_Matrix.md)

**What you will learn:**
- Adjacency matrix definition
- Memory layout (V x V matrix)
- For undirected graphs (symmetric)
- For directed graphs (not necessarily symmetric)
- For weighted graphs (store weights)
- Space and time complexity

**Key Concepts:**

| Operation | Complexity |
|-----------|------------|
| **Space** | O(V²) |
| **Edge Lookup** | O(1) |
| **Add Edge** | O(1) |
| **Remove Edge** | O(1) |
| **Get Neighbors** | O(V) |

**Representation:**
```
Undirected Graph:          Adjacency Matrix:
    1 ----- 2             [0][1][2][3]
    |       |           0[0 1 1 0]
    |       |           1[1 0 0 1]
    4 ----- 3           2[1 0 0 1]
                        3[0 1 1 0]
```

**Implementation:**
```cpp
// Unweighted graph
int V = 5;
vector<vector<bool>> adj(V, vector<bool>(V, false));

// Add edge between u and v (undirected)
adj[u][v] = true;
adj[v][u] = true;

// Check if edge exists
if (adj[u][v]) { /* edge exists */ }

// Get all neighbors of u
for (int v = 0; v < V; v++) {
    if (adj[u][v]) {
        cout << v << " ";
    }
}

// Weighted graph
vector<vector<int>> adj(V, vector<int>(V, INF));
adj[u][v] = weight;
adj[v][u] = weight;  // for undirected
```

---

## 3. Adjacency List

This topic explains the adjacency list representation using arrays of lists.

**File:** [03_Adjacency_List.md](03_Adjacency_List.md)

**What you will learn:**
- Adjacency list definition
- For undirected graphs (each edge stored twice)
- For directed graphs (each edge stored once)
- For weighted graphs (store pairs of neighbor and weight)
- Space and time complexity

**Key Concepts:**

| Operation | Complexity |
|-----------|------------|
| **Space** | O(V + E) |
| **Edge Lookup** | O(V) (or O(log V) with sorted list) |
| **Add Edge** | O(1) |
| **Remove Edge** | O(V) |
| **Get Neighbors** | O(degree) |

**Representation:**
```
Undirected Graph:          Adjacency List:
    1 ----- 2             0: 1 → 2
    |       |             1: 0 → 3
    |       |             2: 0 → 3
    4 ----- 3             3: 1 → 2
```

**Implementation:**
```cpp
// Unweighted graph
vector<vector<int>> adj(V);

// Add edge between u and v (undirected)
adj[u].push_back(v);
adj[v].push_back(u);

// Check if edge exists (O(degree))
bool edgeExists = false;
for (int neighbor : adj[u]) {
    if (neighbor == v) {
        edgeExists = true;
        break;
    }
}

// Get all neighbors of u
for (int v : adj[u]) {
    cout << v << " ";
}

// Weighted graph
vector<vector<pair<int, int>>> adj(V);

// Add weighted edge
adj[u].push_back({v, weight});
adj[v].push_back({u, weight});  // for undirected

// Iterate over neighbors with weights
for (auto [neighbor, weight] : adj[u]) {
    cout << neighbor << " (weight: " << weight << ") ";
}
```

---

## 4. Edge List

This topic explains the edge list representation storing all edges in a list.

**File:** [04_Edge_List.md](04_Edge_List.md)

**What you will learn:**
- Edge list definition
- For directed and undirected graphs
- For weighted graphs (store triples)
- Space and time complexity
- When edge list is preferred (Kruskal's algorithm)

**Key Concepts:**

| Operation | Complexity |
|-----------|------------|
| **Space** | O(E) |
| **Edge Lookup** | O(E) |
| **Add Edge** | O(1) |
| **Remove Edge** | O(E) |
| **Get Neighbors** | O(E) |

**Representation:**
```
Undirected Graph:          Edge List:
    1 ----- 2             (0,1)
    |       |             (0,2)
    |       |             (1,3)
    4 ----- 3             (2,3)
```

**Implementation:**
```cpp
// Unweighted graph
vector<pair<int, int>> edges;

// Add edge between u and v (undirected)
edges.push_back({u, v});
// For undirected, edge appears once (direction not stored)

// Weighted graph
struct Edge {
    int u, v, weight;
};
vector<Edge> edges;

// Add weighted edge
edges.push_back({u, v, weight});

// Sort edges by weight (for Kruskal's algorithm)
sort(edges.begin(), edges.end(), 
     [](Edge a, Edge b) { return a.weight < b.weight; });

// Iterate over all edges
for (auto [u, v, w] : edges) {
    cout << u << " - " << v << " (" << w << ")" << endl;
}
```

---

## 5. Comparison of Representations

This topic compares the three representations to help choose the right one.

**File:** [05_Comparison_of_Representations.md](05_Comparison_of_Representations.md)

**What you will learn:**
- When to use each representation
- Memory usage comparison
- Operation complexity comparison
- Dense vs Sparse graphs
- Algorithm-specific considerations

**Key Concepts:**

| Representation | Space | Edge Lookup | Neighbors | Best For |
|----------------|-------|-------------|-----------|----------|
| **Adjacency Matrix** | O(V²) | O(1) | O(V) | Dense graphs (E ≈ V²) |
| **Adjacency List** | O(V+E) | O(degree) | O(degree) | Sparse graphs (E ≪ V²) |
| **Edge List** | O(E) | O(E) | O(E) | Edge-centric algorithms |

**Comparison Table:**

| Criterion | Adjacency Matrix | Adjacency List | Edge List |
|-----------|-----------------|----------------|-----------|
| **Memory (V=1000, E=3000)** | ~1 MB (int) | ~24 KB | ~24 KB |
| **Memory (V=1000, E=500,000)** | ~1 MB | ~4 MB | ~4 MB |
| **Add Edge** | O(1) | O(1) | O(1) |
| **Remove Edge** | O(1) | O(degree) | O(E) |
| **Check Edge** | O(1) | O(degree) | O(E) |
| **Get Neighbors** | O(V) | O(degree) | O(E) |
| **Iterate over edges** | O(V²) | O(V+E) | O(E) |

**Selection Guide:**

| Scenario | Recommended Representation |
|----------|---------------------------|
| **Dense graph (E ≈ V²)** | Adjacency Matrix |
| **Sparse graph (E ≪ V²)** | Adjacency List |
| **Need fast edge lookup** | Adjacency Matrix |
| **Need fast neighbor iteration** | Adjacency List |
| **Need to sort edges by weight** | Edge List |
| **Running BFS/DFS** | Adjacency List |
| **Running Floyd-Warshall** | Adjacency Matrix |
| **Running Kruskal's algorithm** | Edge List |
| **Limited memory** | Adjacency List (sparse) or Edge List |

---

### Complete Graph Implementation (All Representations)

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <utility>
using namespace std;

// ============ ADJACENCY MATRIX ============
class GraphMatrix {
private:
    int V;
    vector<vector<bool>> adj;
    
public:
    GraphMatrix(int vertices) : V(vertices), adj(vertices, vector<bool>(vertices, false)) {}
    
    void addEdge(int u, int v) {
        adj[u][v] = true;
        adj[v][u] = true;  // undirected
    }
    
    bool hasEdge(int u, int v) {
        return adj[u][v];
    }
    
    void print() {
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                cout << adj[i][j] << " ";
            }
            cout << endl;
        }
    }
};

// ============ ADJACENCY LIST ============
class GraphList {
private:
    int V;
    vector<vector<int>> adj;
    
public:
    GraphList(int vertices) : V(vertices), adj(vertices) {}
    
    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u);  // undirected
    }
    
    bool hasEdge(int u, int v) {
        for (int neighbor : adj[u]) {
            if (neighbor == v) return true;
        }
        return false;
    }
    
    void print() {
        for (int i = 0; i < V; i++) {
            cout << i << ": ";
            for (int v : adj[i]) {
                cout << v << " ";
            }
            cout << endl;
        }
    }
    
    vector<int> getNeighbors(int u) {
        return adj[u];
    }
};

// ============ EDGE LIST ============
class GraphEdgeList {
private:
    vector<pair<int, int>> edges;
    int V;
    
public:
    GraphEdgeList(int vertices) : V(vertices) {}
    
    void addEdge(int u, int v) {
        edges.push_back({u, v});
    }
    
    void print() {
        for (auto [u, v] : edges) {
            cout << u << " -- " << v << endl;
        }
    }
    
    vector<pair<int, int>> getAllEdges() {
        return edges;
    }
};

// ============ WEIGHTED ADJACENCY LIST ============
class WeightedGraphList {
private:
    int V;
    vector<vector<pair<int, int>>> adj;
    
public:
    WeightedGraphList(int vertices) : V(vertices), adj(vertices) {}
    
    void addEdge(int u, int v, int weight) {
        adj[u].push_back({v, weight});
        adj[v].push_back({u, weight});  // undirected
    }
    
    void print() {
        for (int i = 0; i < V; i++) {
            cout << i << ": ";
            for (auto [v, w] : adj[i]) {
                cout << "(" << v << "," << w << ") ";
            }
            cout << endl;
        }
    }
};

int main() {
    int V = 5;
    
    cout << "=== Adjacency Matrix ===" << endl;
    GraphMatrix gm(V);
    gm.addEdge(0, 1);
    gm.addEdge(0, 2);
    gm.addEdge(1, 3);
    gm.addEdge(2, 3);
    gm.print();
    
    cout << "\n=== Adjacency List ===" << endl;
    GraphList gl(V);
    gl.addEdge(0, 1);
    gl.addEdge(0, 2);
    gl.addEdge(1, 3);
    gl.addEdge(2, 3);
    gl.print();
    
    cout << "\n=== Edge List ===" << endl;
    GraphEdgeList gel(V);
    gel.addEdge(0, 1);
    gel.addEdge(0, 2);
    gel.addEdge(1, 3);
    gel.addEdge(2, 3);
    gel.print();
    
    cout << "\n=== Weighted Graph ===" << endl;
    WeightedGraphList wgl(V);
    wgl.addEdge(0, 1, 5);
    wgl.addEdge(0, 2, 3);
    wgl.addEdge(1, 3, 2);
    wgl.addEdge(2, 3, 4);
    wgl.print();
    
    return 0;
}
```

---

### Memory Calculation Example

For a graph with V = 1000 vertices and E = 3000 edges:

| Representation | Memory Calculation | Total |
|----------------|-------------------|-------|
| **Adjacency Matrix** | 1000 × 1000 × 1 byte | ~1 MB |
| **Adjacency List** | 1000 lists + 2×3000 edges × 4 bytes | ~28 KB |
| **Edge List** | 2×3000 edges × 4 bytes | ~24 KB |

For a dense graph with V = 1000, E = 500,000:

| Representation | Memory Calculation | Total |
|----------------|-------------------|-------|
| **Adjacency Matrix** | 1000 × 1000 × 1 byte | ~1 MB |
| **Adjacency List** | 1000 lists + 2×500,000 edges × 4 bytes | ~4 MB |
| **Edge List** | 2×500,000 edges × 4 bytes | ~4 MB |

---

### Prerequisites

Before starting this section, you should have completed:

- [01. Basics](../../01.%20Basics/README.md) - Arrays, vectors, pointers
- [04. Data Structures](../../04.%20Data%20Structures/README.md) - Vectors, lists

---

### Learning Path

```
Level 1: Graph Basics
├── Terminology
├── Directed vs Undirected
└── Weighted vs Unweighted

Level 2: Representations
├── Adjacency Matrix
├── Adjacency List
└── Edge List

Level 3: Implementation
├── Adding edges
├── Removing edges
├── Checking existence
└── Iterating neighbors

Level 4: Selection Guide
├── Dense vs Sparse
├── Memory constraints
└── Algorithm requirements
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Forgetting to add both directions for undirected graphs | Add edge[u][v] AND edge[v][u] |
| Using matrix for sparse graphs | Use adjacency list to save memory |
| Using list for dense graphs | Use matrix for O(1) edge lookup |
| Not reserving vector capacity | Use `reserve()` for known size |
| Mixing 0-based and 1-based indexing | Be consistent throughout |

---

### Practice Questions

After completing this section, you should be able to:

1. Choose the appropriate representation for a given graph
2. Convert between adjacency matrix and adjacency list
3. Implement all three representations
4. Calculate memory usage for a graph
5. Add and remove edges in each representation
6. Iterate over neighbors efficiently
7. Detect if a graph is dense or sparse
8. Explain the trade-offs between representations

---

### Next Steps

- Go to [01_Graph_Basics.md](01_Graph_Basics.md) to understand Graph Basics.