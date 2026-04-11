# Graph Basics

## 📖 Overview

A graph is a non-linear data structure consisting of vertices (nodes) and edges (connections between vertices). Graphs are used to model relationships and networks, such as social networks, road maps, computer networks, and dependency graphs. Understanding graph fundamentals is essential for solving complex real-world problems.

---

## 🎯 What is a Graph?

### Formal Definition

A graph G = (V, E) consists of:
- **V**: A set of vertices (nodes)
- **E**: A set of edges (connections between vertices)

### Visual Representation

```
Graph with 5 vertices and 6 edges:

    1 ----- 2
    | \     |
    |   \   |
    |     \ |
    4 ----- 3

Vertices: V = {1, 2, 3, 4}
Edges: E = {(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)}
```

---

## 📊 Graph Terminology

### Basic Terms

| Term | Definition | Example |
|------|------------|---------|
| **Vertex (Node)** | Fundamental unit of a graph | A city in a map |
| **Edge** | Connection between two vertices | A road connecting cities |
| **Adjacent** | Two vertices connected by an edge | Cities connected by road |
| **Degree** | Number of edges incident to a vertex | Number of roads from a city |
| **Path** | Sequence of vertices connected by edges | Route from A to B |
| **Cycle** | Path that starts and ends at same vertex | Loop in a graph |
| **Loop** | Edge from a vertex to itself | Self-connection |

### Advanced Terms

| Term | Definition |
|------|------------|
| **Walk** | Sequence of vertices where consecutive vertices are adjacent |
| **Trail** | Walk with no repeated edges |
| **Circuit** | Trail that starts and ends at same vertex |
| **Simple Path** | Path with no repeated vertices |
| **Connected** | Path exists between every pair of vertices |
| **Component** | Maximal connected subgraph |

---

## 🔄 Types of Graphs

### 1. Directed vs Undirected

```
Undirected Graph:              Directed Graph (Digraph):
    1 --- 2                        1 → 2
    |     |                        ↑   ↓
    4 --- 3                        4 ← 3

Edges have no direction        Edges have direction (arrows)
```

### 2. Weighted vs Unweighted

```
Weighted Graph:                  Unweighted Graph:
    1 ---5--- 2                     1 --- 2
    |         |                     |     |
    2         3                     4 --- 3
    4 ---1--- 3                     

Edges have weights/costs        All edges equal weight (usually 1)
```

### 3. Cyclic vs Acyclic

```
Cyclic Graph:                    Acyclic Graph (DAG):
    1 → 2 → 3                      1 → 2 → 3
    ↑       ↓                           ↓
    5 ← 4                              4

Contains cycle (1→2→3→4→5→1)    No cycles (Directed Acyclic Graph)
```

### 4. Complete Graph

```
Complete Graph (K₄):
    1 --- 2
    | \ / |
    |  X  |
    | / \ |
    4 --- 3

Every vertex connected to every other vertex
Number of edges = V(V-1)/2 for undirected
```

### 5. Bipartite Graph

```
Bipartite Graph:
    A1 --- B1
     |      |
    A2 --- B2
     |      |
    A3 --- B3

Vertices can be divided into two sets (A and B)
All edges go between sets (no edges within set)
```

---

## 📐 Graph Properties

### Degree

```
For Undirected Graph:
    Degree(vertex) = number of incident edges
    
    Example:
        1 --- 2
        |     |
        4 --- 3
    
    deg(1) = 2 (edges to 2 and 4)
    deg(2) = 2 (edges to 1 and 3)
    deg(3) = 2 (edges to 2 and 4)
    deg(4) = 2 (edges to 1 and 3)

For Directed Graph:
    In-degree = number of incoming edges
    Out-degree = number of outgoing edges
```

### Handshaking Lemma

```
Sum of all degrees = 2 × (number of edges)

Proof: Each edge contributes 2 to the sum of degrees
```

### Graph Density

```
Density = 2E / (V(V-1)) for undirected graphs
Density = E / (V(V-1)) for directed graphs

Dense graph:  E ≈ V²
Sparse graph: E ≈ V
```

---

## 🔢 Special Graphs

| Graph Type | Description | Properties |
|------------|-------------|------------|
| **Tree** | Connected acyclic graph | E = V - 1 |
| **Forest** | Collection of trees | E ≤ V - 1 |
| **Complete Graph (Kₙ)** | Every vertex connected | E = V(V-1)/2 |
| **Cycle Graph (Cₙ)** | Simple cycle | deg(v) = 2 for all v |
| **Path Graph (Pₙ)** | Simple path | deg(end)=1, deg(middle)=2 |
| **Star Graph (K₁,ₙ)** | Central vertex connected to all others | deg(center)=n, deg(others)=1 |
| **Regular Graph** | All vertices same degree | deg(v) = k for all v |
| **Bipartite Graph** | Two-part vertex set | No edges within same part |

---

## 💻 Graph Implementation Preview

### Basic Graph Class

```cpp
#include <iostream>
#include <vector>
#include <list>
using namespace std;

class Graph {
private:
    int vertices;
    vector<vector<int>> adjMatrix;
    vector<list<int>> adjList;
    bool isDirected;
    
public:
    // Constructor
    Graph(int v, bool directed = false) 
        : vertices(v), isDirected(directed) {
        // Initialize adjacency matrix
        adjMatrix.resize(v, vector<int>(v, 0));
        
        // Initialize adjacency list
        adjList.resize(v);
    }
    
    // Add edge (to be implemented by specific representation)
    void addEdge(int u, int v, int weight = 1) {
        // Implementation depends on representation
    }
    
    // Display graph
    void display() {
        // Implementation depends on representation
    }
    
    // Get number of vertices
    int getVertices() const { return vertices; }
    
    // Get number of edges (to be implemented)
    int getEdges() const { return 0; }
};
```

---

## 🎯 Graph Applications

| Application | Graph Type | Description |
|-------------|------------|-------------|
| **Social Networks** | Undirected | Friend connections |
| **Road Maps** | Weighted, Directed | Navigation, shortest path |
| **Web Pages** | Directed | PageRank algorithm |
| **Computer Networks** | Undirected | Network connectivity |
| **Dependency Resolution** | DAG | Build systems, package managers |
| **Circuit Design** | Directed | Signal flow |
| **Recommendation Systems** | Bipartite | User-item relationships |
| **Matching Problems** | Bipartite | Job assignments |

---

## 📝 Graph Representation Summary

| Representation | Space | Add Edge | Check Edge | Neighbors |
|----------------|-------|----------|------------|-----------|
| **Adjacency Matrix** | O(V²) | O(1) | O(1) | O(V) |
| **Adjacency List** | O(V+E) | O(1) | O(V) | O(degree) |
| **Edge List** | O(E) | O(1) | O(E) | O(E) |

---

## ✅ Key Takeaways

1. **Graph** = vertices + edges
2. **Directed** edges have direction; **undirected** don't
3. **Weighted** edges have costs; **unweighted** don't
4. **Degree** = number of incident edges
5. **Density** determines if graph is sparse or dense
6. **Connected** graphs have path between all vertices
7. **DAG** = Directed Acyclic Graph (no cycles)
8. **Applications** are everywhere: social, web, maps, dependencies

---