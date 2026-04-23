# README.md

## Basic Graph Algorithms - Complete Guide

### Overview

Graph algorithms are fundamental to solving problems involving networks, relationships, and connectivity. This section covers essential graph algorithms including traversal (BFS and DFS), finding connected components, cycle detection, and topological sorting. These algorithms form the foundation for more advanced graph algorithms like shortest path, minimum spanning tree, and network flow.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [01_Graph_Traversal_BFS.md](01_Graph_Traversal_BFS.md) | understand Breadth-First Search (BFS) |
| 2. | [02_Graph_Traversal_DFS.md](02_Graph_Traversal_DFS.md) | understand Depth-First Search (DFS) |
| 3. | [03_Connected_Components.md](03_Connected_Components.md) | understand Connected Components |
| 4. | [04_Cycle_Detection.md](04_Cycle_Detection.md) | understand Cycle Detection in Graphs |
| 5. | [05_Topological_Sort.md](05_Topological_Sort.md) | understand Topological Sort |
| 6. | [README.md](README.md) | understand Basic Graph Algorithms Overview |

---

## 1. Breadth-First Search (BFS)

This topic explains BFS traversal for graphs.

**File:** [01_Graph_Traversal_BFS.md](01_Graph_Traversal_BFS.md)

**What you will learn:**
- BFS algorithm for graphs
- Queue-based implementation
- Handling disconnected graphs
- BFS for shortest path (unweighted)
- Time and space complexity

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Queue-based** | Uses FIFO queue for processing |
| **Level Order** | Explores vertices in order of distance from source |
| **Shortest Path** | Finds shortest path in unweighted graphs |
| **Connected** | Visits all reachable vertices from source |

**Algorithm:**
```
BFS(graph, start):
    create queue Q
    create visited array (false)
    
    visited[start] = true
    Q.push(start)
    
    while Q is not empty:
        u = Q.front()
        Q.pop()
        process(u)
        
        for each neighbor v of u:
            if not visited[v]:
                visited[v] = true
                Q.push(v)
```

**Complexity:**

| Operation | Complexity |
|-----------|------------|
| **Time** | O(V + E) |
| **Space** | O(V) |

---

## 2. Depth-First Search (DFS)

This topic explains DFS traversal for graphs.

**File:** [02_Graph_Traversal_DFS.md](02_Graph_Traversal_DFS.md)

**What you will learn:**
- DFS algorithm for graphs
- Recursive and iterative implementations
- Stack-based approach
- Discovery and finish times
- Applications of DFS

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Stack-based** | Uses recursion or explicit stack |
| **Backtracking** | Explores deep before wide |
| **Discovery Time** | Time when vertex is first visited |
| **Finish Time** | Time when vertex exploration completes |

**Algorithm:**
```
DFS(graph, start):
    create visited array (false)
    call DFS_recursive(start)

DFS_recursive(u):
    visited[u] = true
    process(u)
    
    for each neighbor v of u:
        if not visited[v]:
            DFS_recursive(v)
```

**Complexity:**

| Operation | Complexity |
|-----------|------------|
| **Time** | O(V + E) |
| **Space** | O(V) (recursion stack) |

---

## 3. Connected Components

This topic explains finding connected components in undirected graphs.

**File:** [03_Connected_Components.md](03_Connected_Components.md)

**What you will learn:**
- Definition of connected components
- Finding components using BFS/DFS
- Counting number of components
- Labeling components
- Applications (social networks, image segmentation)

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Connected Component** | Maximal set of vertices where each pair has a path |
| **Component ID** | Label assigned to vertices in same component |
| **Disconnected Graph** | Graph with multiple components |

**Algorithm:**
```
findConnectedComponents(graph):
    create visited array (false)
    components = 0
    
    for each vertex v in graph:
        if not visited[v]:
            components++
            BFS/DFS(v) to mark all reachable vertices
```

**Complexity:**

| Operation | Complexity |
|-----------|------------|
| **Time** | O(V + E) |
| **Space** | O(V) |

---

## 4. Cycle Detection

This topic explains detecting cycles in directed and undirected graphs.

**File:** [04_Cycle_Detection.md](04_Cycle_Detection.md)

**What you will learn:**
- Cycle detection in undirected graphs (using parent tracking)
- Cycle detection in directed graphs (using recursion stack)
- DFS-based approach
- Back edge detection
- Applications (deadlock detection, dependency validation)

**Key Concepts:**

| Graph Type | Detection Method | Complexity |
|------------|------------------|------------|
| **Undirected** | Parent tracking in DFS | O(V + E) |
| **Directed** | Recursion stack tracking | O(V + E) |

**Undirected Cycle Detection:**
```
hasCycleUndirected(graph):
    create visited array (false)
    
    for each vertex v:
        if not visited[v]:
            if DFS_Undirected(v, -1):
                return true
    return false

DFS_Undirected(u, parent):
    visited[u] = true
    
    for each neighbor v of u:
        if not visited[v]:
            if DFS_Undirected(v, u):
                return true
        else if v != parent:
            return true  // cycle found
    return false
```

**Directed Cycle Detection:**
```
hasCycleDirected(graph):
    create visited array (false)
    create recStack array (false)
    
    for each vertex v:
        if not visited[v]:
            if DFS_Directed(v):
                return true
    return false

DFS_Directed(u):
    visited[u] = true
    recStack[u] = true
    
    for each neighbor v of u:
        if not visited[v]:
            if DFS_Directed(v):
                return true
        else if recStack[v]:
            return true  // back edge - cycle found
    
    recStack[u] = false
    return false
```

---

## 5. Topological Sort

This topic explains topological ordering of Directed Acyclic Graphs (DAGs).

**File:** [05_Topological_Sort.md](05_Topological_Sort.md)

**What you will learn:**
- Definition of topological sort
- Kahn's algorithm (BFS-based)
- DFS-based topological sort
- Cycle detection prerequisite
- Applications (course scheduling, build systems)

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Topological Order** | Linear ordering where for every edge u→v, u comes before v |
| **DAG** | Directed Acyclic Graph (must have no cycles) |
| **Indegree** | Number of incoming edges to a vertex |

**Kahn's Algorithm (BFS):**
```
topologicalSort(graph):
    compute indegree for each vertex
    queue Q = all vertices with indegree 0
    result = []
    
    while Q is not empty:
        u = Q.front()
        Q.pop()
        result.push(u)
        
        for each neighbor v of u:
            indegree[v]--
            if indegree[v] == 0:
                Q.push(v)
    
    if result.size() != V:
        // graph has a cycle
        return error
    return result
```

**DFS-based Topological Sort:**
```
topologicalSortDFS(graph):
    create visited array (false)
    stack result
    
    for each vertex v:
        if not visited[v]:
            DFS(v, result)
    
    return result (pop from stack)

DFS(u, result):
    visited[u] = true
    
    for each neighbor v of u:
        if not visited[v]:
            DFS(v, result)
    
    result.push(u)
```

**Complexity:**

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Kahn's (BFS)** | O(V + E) | O(V) |
| **DFS-based** | O(V + E) | O(V) |

---

### Complete Graph Algorithms Implementation

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <list>
using namespace std;

class Graph {
private:
    int V;
    vector<vector<int>> adj;
    
public:
    Graph(int vertices) : V(vertices), adj(vertices) {}
    
    void addEdge(int u, int v) {
        adj[u].push_back(v);
    }
    
    void addEdgeUndirected(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    
    // ============ BFS ============
    void BFS(int start) {
        vector<bool> visited(V, false);
        queue<int> q;
        
        visited[start] = true;
        q.push(start);
        
        cout << "BFS from " << start << ": ";
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            cout << u << " ";
            
            for (int v : adj[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    q.push(v);
                }
            }
        }
        cout << endl;
    }
    
    // BFS for disconnected graph
    void BFSDisconnected() {
        vector<bool> visited(V, false);
        
        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                queue<int> q;
                visited[i] = true;
                q.push(i);
                
                while (!q.empty()) {
                    int u = q.front();
                    q.pop();
                    cout << u << " ";
                    
                    for (int v : adj[u]) {
                        if (!visited[v]) {
                            visited[v] = true;
                            q.push(v);
                        }
                    }
                }
                cout << endl;
            }
        }
    }
    
    // ============ DFS ============
    void DFS(int start) {
        vector<bool> visited(V, false);
        cout << "DFS from " << start << ": ";
        DFSUtil(start, visited);
        cout << endl;
    }
    
    void DFSUtil(int u, vector<bool>& visited) {
        visited[u] = true;
        cout << u << " ";
        
        for (int v : adj[u]) {
            if (!visited[v]) {
                DFSUtil(v, visited);
            }
        }
    }
    
    void DFSIterative(int start) {
        vector<bool> visited(V, false);
        stack<int> st;
        
        visited[start] = true;
        st.push(start);
        
        cout << "DFS Iterative from " << start << ": ";
        while (!st.empty()) {
            int u = st.top();
            st.pop();
            cout << u << " ";
            
            for (int v : adj[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    st.push(v);
                }
            }
        }
        cout << endl;
    }
    
    // ============ Connected Components ============
    int countConnectedComponents() {
        vector<bool> visited(V, false);
        int components = 0;
        
        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                components++;
                DFSUtil(i, visited);
                cout << endl;
            }
        }
        return components;
    }
    
    // ============ Cycle Detection (Undirected) ============
    bool hasCycleUndirected() {
        vector<bool> visited(V, false);
        
        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                if (cycleUtilUndirected(i, -1, visited)) {
                    return true;
                }
            }
        }
        return false;
    }
    
    bool cycleUtilUndirected(int u, int parent, vector<bool>& visited) {
        visited[u] = true;
        
        for (int v : adj[u]) {
            if (!visited[v]) {
                if (cycleUtilUndirected(v, u, visited)) {
                    return true;
                }
            } else if (v != parent) {
                return true;  // Cycle detected
            }
        }
        return false;
    }
    
    // ============ Cycle Detection (Directed) ============
    bool hasCycleDirected() {
        vector<bool> visited(V, false);
        vector<bool> recStack(V, false);
        
        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                if (cycleUtilDirected(i, visited, recStack)) {
                    return true;
                }
            }
        }
        return false;
    }
    
    bool cycleUtilDirected(int u, vector<bool>& visited, vector<bool>& recStack) {
        visited[u] = true;
        recStack[u] = true;
        
        for (int v : adj[u]) {
            if (!visited[v]) {
                if (cycleUtilDirected(v, visited, recStack)) {
                    return true;
                }
            } else if (recStack[v]) {
                return true;  // Back edge found
            }
        }
        
        recStack[u] = false;
        return false;
    }
    
    // ============ Topological Sort (Kahn's Algorithm) ============
    vector<int> topologicalSortKahn() {
        vector<int> indegree(V, 0);
        
        for (int u = 0; u < V; u++) {
            for (int v : adj[u]) {
                indegree[v]++;
            }
        }
        
        queue<int> q;
        for (int i = 0; i < V; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }
        
        vector<int> result;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            result.push_back(u);
            
            for (int v : adj[u]) {
                indegree[v]--;
                if (indegree[v] == 0) {
                    q.push(v);
                }
            }
        }
        
        if (result.size() != V) {
            cout << "Graph has a cycle - topological sort not possible" << endl;
            return {};
        }
        return result;
    }
    
    // ============ Topological Sort (DFS-based) ============
    vector<int> topologicalSortDFS() {
        vector<bool> visited(V, false);
        stack<int> st;
        
        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                topologicalSortDFSUtil(i, visited, st);
            }
        }
        
        vector<int> result;
        while (!st.empty()) {
            result.push_back(st.top());
            st.pop();
        }
        return result;
    }
    
    void topologicalSortDFSUtil(int u, vector<bool>& visited, stack<int>& st) {
        visited[u] = true;
        
        for (int v : adj[u]) {
            if (!visited[v]) {
                topologicalSortDFSUtil(v, visited, st);
            }
        }
        
        st.push(u);
    }
    
    // ============ Print Graph ============
    void printGraph() {
        for (int i = 0; i < V; i++) {
            cout << i << ": ";
            for (int v : adj[i]) {
                cout << v << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    cout << "=== Undirected Graph ===" << endl;
    Graph undirected(5);
    undirected.addEdgeUndirected(0, 1);
    undirected.addEdgeUndirected(0, 2);
    undirected.addEdgeUndirected(1, 3);
    undirected.addEdgeUndirected(2, 4);
    
    undirected.printGraph();
    undirected.BFS(0);
    undirected.DFS(0);
    
    cout << "\nConnected Components: " << undirected.countConnectedComponents() << endl;
    cout << "Has Cycle: " << (undirected.hasCycleUndirected() ? "Yes" : "No") << endl;
    
    cout << "\n=== Directed Acyclic Graph (DAG) ===" << endl;
    Graph dag(6);
    dag.addEdge(5, 2);
    dag.addEdge(5, 0);
    dag.addEdge(4, 0);
    dag.addEdge(4, 1);
    dag.addEdge(2, 3);
    dag.addEdge(3, 1);
    
    cout << "Topological Sort (Kahn): ";
    vector<int> topo = dag.topologicalSortKahn();
    for (int v : topo) cout << v << " ";
    cout << endl;
    
    cout << "Has Cycle: " << (dag.hasCycleDirected() ? "Yes" : "No") << endl;
    
    cout << "\n=== Directed Cyclic Graph ===" << endl;
    Graph cyclic(4);
    cyclic.addEdge(0, 1);
    cyclic.addEdge(1, 2);
    cyclic.addEdge(2, 0);  // Creates cycle
    
    cout << "Has Cycle: " << (cyclic.hasCycleDirected() ? "Yes" : "No") << endl;
    
    return 0;
}
```

---

### Algorithm Comparison Summary

| Algorithm | Purpose | Data Structure | Complexity | Space |
|-----------|---------|----------------|------------|-------|
| **BFS** | Level order, shortest path (unweighted) | Queue | O(V+E) | O(V) |
| **DFS** | Connectivity, cycle detection | Stack/Recursion | O(V+E) | O(V) |
| **Connected Components** | Find connected subgraphs | BFS/DFS | O(V+E) | O(V) |
| **Cycle Detection (Undirected)** | Detect cycles | DFS + parent | O(V+E) | O(V) |
| **Cycle Detection (Directed)** | Detect cycles | DFS + recursion stack | O(V+E) | O(V) |
| **Topological Sort (Kahn)** | Linear ordering of DAG | Queue + indegree | O(V+E) | O(V) |
| **Topological Sort (DFS)** | Linear ordering of DAG | Stack + DFS | O(V+E) | O(V) |

---

### Prerequisites

Before starting this section, you should have completed:

- [04_Graph_Representations/README.md](../04_Graph_Representations/README.md) - Graph representations
- [04. Data Structures](../../04.%20Data%20Structures/README.md) - Queues, stacks

---

### Learning Path

```
Level 1: Graph Traversal
├── BFS (Queue-based)
├── DFS (Recursive)
└── DFS (Iterative)

Level 2: Graph Properties
├── Connected Components
├── Cycle Detection (Undirected)
└── Cycle Detection (Directed)

Level 3: DAG Algorithms
├── Topological Sort (Kahn's)
└── Topological Sort (DFS-based)

Level 4: Advanced
├── BFS for Shortest Path
├── DFS for Parent/Discovery Time
└── Applications
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Forgetting to mark visited | Always mark when adding to queue/stack |
| Not handling disconnected graphs | Loop through all vertices |
| Stack overflow in deep DFS | Use iterative DFS for very deep graphs |
| Cycle detection without parent (undirected) | Track parent to avoid false positives |
| Cycle detection without recursion stack (directed) | Use separate recStack array |
| Topological sort on cyclic graph | Check for cycles first |

---

### Practice Questions

After completing this section, you should be able to:

1. Implement BFS and DFS for a graph
2. Find connected components in an undirected graph
3. Detect cycles in undirected graphs
4. Detect cycles in directed graphs
5. Perform topological sort on a DAG
6. Determine if a topological order exists
7. Find the shortest path in an unweighted graph using BFS
8. Find the number of connected components

---

### Next Steps

- Go to [01_Graph_Traversal_BFS.md](01_Graph_Traversal_BFS.md) to understand Breadth-First Search.