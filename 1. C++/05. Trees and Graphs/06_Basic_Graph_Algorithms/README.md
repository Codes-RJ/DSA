# Basic Graph Algorithms - README.md

## 📖 Overview

Basic graph algorithms form the foundation for solving graph-related problems. This section covers essential algorithms including connectivity, cycle detection, and topological sorting. These algorithms are building blocks for more advanced graph algorithms like shortest path and minimum spanning tree.

---

## 🎯 Algorithms Covered

| Algorithm | Description | Time Complexity |
|-----------|-------------|-----------------|
| **Connected Components** | Find all connected subgraphs | O(V + E) |
| **Cycle Detection (Undirected)** | Detect cycles in undirected graph | O(V + E) |
| **Cycle Detection (Directed)** | Detect cycles in directed graph | O(V + E) |
| **Topological Sort** | Linear ordering of DAG vertices | O(V + E) |
| **Bipartite Graph Check** | Check if graph is 2-colorable | O(V + E) |

---

## 📚 Folder Structure

```
06_Basic_Graph_Algorithms/
├── README.md                       # This file
├── 01_Connected_Components.md      # Finding connected components
├── 02_Cycle_Detection.md           # Detecting cycles in graphs
├── 03_Topological_Sort.md          # Topological ordering of DAG
└── 04_Bipartite_Graph.md           # Bipartite graph checking
```

---

## 📊 Algorithm Comparison

| Algorithm | Graph Type | DFS/BFS | Use Case |
|-----------|------------|---------|----------|
| **Connected Components** | Undirected | Both | Finding clusters |
| **Cycle Detection (Undirected)** | Undirected | DFS | Detecting cycles |
| **Cycle Detection (Directed)** | Directed | DFS | Detecting cycles in DAG |
| **Topological Sort** | Directed (DAG) | DFS/Kahn | Task scheduling |
| **Bipartite Check** | Undirected | BFS | Graph coloring |

---

## 🔧 Common Graph Utilities

```cpp
// Graph class with basic utilities
class Graph {
private:
    int vertices;
    vector<vector<int>> adj;
    bool isDirected;
    
public:
    Graph(int v, bool directed = false) 
        : vertices(v), isDirected(directed) {
        adj.resize(v);
    }
    
    void addEdge(int u, int v) {
        adj[u].push_back(v);
        if (!isDirected) adj[v].push_back(u);
    }
    
    vector<int> getNeighbors(int u) {
        return adj[u];
    }
    
    int getVertices() const { return vertices; }
    
    void display() {
        cout << "\nGraph Adjacency List:" << endl;
        for (int i = 0; i < vertices; i++) {
            cout << i << ": ";
            for (int v : adj[i]) cout << v << " ";
            cout << endl;
        }
    }
};
```

---

## 🚀 Learning Path

```
1. Connected_Components.md     → Find connected subgraphs
           ↓
2. Cycle_Detection.md          → Detect cycles in graphs
           ↓
3. Topological_Sort.md         → Order vertices in DAG
           ↓
4. Bipartite_Graph.md          → Check 2-colorability
```

---

## ✅ Key Takeaways

1. **Connected components** found via DFS/BFS traversal
2. **Cycle detection** uses visited states (0=unvisited, 1=visiting, 2=processed)
3. **Topological sort** only works on DAGs
4. **Bipartite graphs** are 2-colorable (no odd cycles)
5. **Time complexity** O(V + E) for all basic algorithms

---