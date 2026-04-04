# Basic Graph Algorithms

## Overview
This section covers fundamental graph algorithms that form the foundation for more advanced graph-based problem solving. These algorithms are essential for understanding graph traversal, connectivity, and basic graph properties.

## Topics Covered

### 1. Graph Traversal BFS (`01_Graph_Traversal_BFS.md`)
- Breadth-First Search algorithm
- Queue-based implementation
- Shortest path in unweighted graphs
- Connected components detection
- Level-order graph traversal

### 2. Graph Traversal DFS (`02_Graph_Traversal_DFS.md`)
- Depth-First Search algorithm
- Stack-based and recursive implementations
- Graph exploration and backtracking
- Applications in cycle detection
- Topological sorting preparation

### 3. Connected Components (`03_Connected_Components.md`)
- Finding connected components in undirected graphs
- Strongly connected components in directed graphs
- Component labeling and counting
- Applications in network analysis
- Implementation using BFS/DFS

### 4. Cycle Detection (`04_Cycle_Detection.md`)
- Detecting cycles in directed graphs
- Detecting cycles in undirected graphs
- Using DFS for cycle detection
- Union-Find approach for undirected graphs
- Applications and importance

### 5. Topological Sort (`05_Topological_Sort.md`)
- Topological sorting of DAGs
- Kahn's algorithm (BFS-based)
- DFS-based topological sort
- Applications in task scheduling
- Cycle detection in DAGs

## Graph Representation Basics

### Adjacency List Representation
```cpp
class Graph {
private:
    int V; // Number of vertices
    std::vector<std::vector<int>> adj; // Adjacency list
    bool directed;
    
public:
    Graph(int vertices, bool isDirected = false) 
        : V(vertices), directed(isDirected) {
        adj.resize(V);
    }
    
    void addEdge(int u, int v) {
        adj[u].push_back(v);
        if (!directed) {
            adj[v].push_back(u);
        }
    }
    
    int getVertexCount() const { return V; }
    const std::vector<int>& getNeighbors(int u) const { return adj[u]; }
    bool isDirected() const { return directed; }
};
```

### Weighted Graph Representation
```cpp
class WeightedGraph {
private:
    int V;
    std::vector<std::vector<std::pair<int, int>>> adj; // {neighbor, weight}
    bool directed;
    
public:
    WeightedGraph(int vertices, bool isDirected = false) 
        : V(vertices), directed(isDirected) {
        adj.resize(V);
    }
    
    void addEdge(int u, int v, int weight) {
        adj[u].push_back({v, weight});
        if (!directed) {
            adj[v].push_back({u, weight});
        }
    }
    
    int getVertexCount() const { return V; }
    const std::vector<std::pair<int, int>>& getNeighbors(int u) const { return adj[u]; }
};
```

## Breadth-First Search (BFS)

### Basic BFS Implementation
```cpp
class BFSTraversal {
public:
    // Standard BFS traversal
    static std::vector<int> bfs(const Graph& graph, int start) {
        std::vector<int> result;
        std::vector<bool> visited(graph.getVertexCount(), false);
        std::queue<int> q;
        
        visited[start] = true;
        q.push(start);
        
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            result.push_back(u);
            
            for (int v : graph.getNeighbors(u)) {
                if (!visited[v]) {
                    visited[v] = true;
                    q.push(v);
                }
            }
        }
        
        return result;
    }
    
    // BFS for disconnected graph
    static std::vector<std::vector<int>> bfsAllComponents(const Graph& graph) {
        std::vector<std::vector<int>> components;
        std::vector<bool> visited(graph.getVertexCount(), false);
        
        for (int i = 0; i < graph.getVertexCount(); i++) {
            if (!visited[i]) {
                std::vector<int> component;
                std::queue<int> q;
                
                visited[i] = true;
                q.push(i);
                
                while (!q.empty()) {
                    int u = q.front();
                    q.pop();
                    component.push_back(u);
                    
                    for (int v : graph.getNeighbors(u)) {
                        if (!visited[v]) {
                            visited[v] = true;
                            q.push(v);
                        }
                    }
                }
                
                components.push_back(component);
            }
        }
        
        return components;
    }
    
    // Shortest path in unweighted graph
    static std::vector<int> shortestPath(const Graph& graph, int start, int end) {
        std::vector<int> parent(graph.getVertexCount(), -1);
        std::vector<bool> visited(graph.getVertexCount(), false);
        std::queue<int> q;
        
        visited[start] = true;
        q.push(start);
        
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            
            if (u == end) break;
            
            for (int v : graph.getNeighbors(u)) {
                if (!visited[v]) {
                    visited[v] = true;
                    parent[v] = u;
                    q.push(v);
                }
            }
        }
        
        // Reconstruct path
        std::vector<int> path;
        if (visited[end]) {
            int current = end;
            while (current != -1) {
                path.push_back(current);
                current = parent[current];
            }
            std::reverse(path.begin(), path.end());
        }
        
        return path;
    }
};
```

## Depth-First Search (DFS)

### Recursive DFS Implementation
```cpp
class DFSTraversal {
public:
    // Recursive DFS traversal
    static std::vector<int> dfsRecursive(const Graph& graph, int start) {
        std::vector<int> result;
        std::vector<bool> visited(graph.getVertexCount(), false);
        dfsHelper(graph, start, visited, result);
        return result;
    }
    
    // Iterative DFS traversal
    static std::vector<int> dfsIterative(const Graph& graph, int start) {
        std::vector<int> result;
        std::vector<bool> visited(graph.getVertexCount(), false);
        std::stack<int> s;
        
        visited[start] = true;
        s.push(start);
        
        while (!s.empty()) {
            int u = s.top();
            s.pop();
            result.push_back(u);
            
            // Push neighbors in reverse order to maintain order
            for (int i = graph.getNeighbors(u).size() - 1; i >= 0; i--) {
                int v = graph.getNeighbors(u)[i];
                if (!visited[v]) {
                    visited[v] = true;
                    s.push(v);
                }
            }
        }
        
        return result;
    }
    
private:
    static void dfsHelper(const Graph& graph, int u, 
                         std::vector<bool>& visited, 
                         std::vector<int>& result) {
        visited[u] = true;
        result.push_back(u);
        
        for (int v : graph.getNeighbors(u)) {
            if (!visited[v]) {
                dfsHelper(graph, v, visited, result);
            }
        }
    }
};
```

## Connected Components

### Finding Connected Components
```cpp
class ConnectedComponents {
public:
    // Find connected components in undirected graph
    static std::vector<std::vector<int>> findComponents(const Graph& graph) {
        std::vector<std::vector<int>> components;
        std::vector<bool> visited(graph.getVertexCount(), false);
        
        for (int i = 0; i < graph.getVertexCount(); i++) {
            if (!visited[i]) {
                std::vector<int> component;
                dfsComponent(graph, i, visited, component);
                components.push_back(component);
            }
        }
        
        return components;
    }
    
    // Count connected components
    static int countComponents(const Graph& graph) {
        return findComponents(graph).size();
    }
    
    // Check if graph is connected
    static bool isConnected(const Graph& graph) {
        if (graph.getVertexCount() == 0) return true;
        
        std::vector<bool> visited(graph.getVertexCount(), false);
        dfsComponent(graph, 0, visited);
        
        return std::all_of(visited.begin(), visited.end(), 
                          [](bool v) { return v; });
    }
    
private:
    static void dfsComponent(const Graph& graph, int u, 
                            std::vector<bool>& visited) {
        visited[u] = true;
        
        for (int v : graph.getNeighbors(u)) {
            if (!visited[v]) {
                dfsComponent(graph, v, visited);
            }
        }
    }
    
    static void dfsComponent(const Graph& graph, int u, 
                            std::vector<bool>& visited, 
                            std::vector<int>& component) {
        visited[u] = true;
        component.push_back(u);
        
        for (int v : graph.getNeighbors(u)) {
            if (!visited[v]) {
                dfsComponent(graph, v, visited, component);
            }
        }
    }
};
```

## Cycle Detection

### Cycle Detection in Undirected Graphs
```cpp
class CycleDetection {
public:
    // Detect cycle in undirected graph using DFS
    static bool hasCycleUndirected(const Graph& graph) {
        std::vector<bool> visited(graph.getVertexCount(), false);
        
        for (int i = 0; i < graph.getVertexCount(); i++) {
            if (!visited[i]) {
                if (dfsCycleUndirected(graph, i, -1, visited)) {
                    return true;
                }
            }
        }
        
        return false;
    }
    
    // Detect cycle in directed graph using DFS
    static bool hasCycleDirected(const Graph& graph) {
        std::vector<bool> visited(graph.getVertexCount(), false);
        std::vector<bool> recStack(graph.getVertexCount(), false);
        
        for (int i = 0; i < graph.getVertexCount(); i++) {
            if (!visited[i]) {
                if (dfsCycleDirected(graph, i, visited, recStack)) {
                    return true;
                }
            }
        }
        
        return false;
    }
    
private:
    static bool dfsCycleUndirected(const Graph& graph, int u, int parent,
                                  std::vector<bool>& visited) {
        visited[u] = true;
        
        for (int v : graph.getNeighbors(u)) {
            if (!visited[v]) {
                if (dfsCycleUndirected(graph, v, u, visited)) {
                    return true;
                }
            } else if (v != parent) {
                return true; // Back edge found
            }
        }
        
        return false;
    }
    
    static bool dfsCycleDirected(const Graph& graph, int u,
                                std::vector<bool>& visited,
                                std::vector<bool>& recStack) {
        visited[u] = true;
        recStack[u] = true;
        
        for (int v : graph.getNeighbors(u)) {
            if (!visited[v]) {
                if (dfsCycleDirected(graph, v, visited, recStack)) {
                    return true;
                }
            } else if (recStack[v]) {
                return true; // Back edge found
            }
        }
        
        recStack[u] = false;
        return false;
    }
};
```

## Topological Sort

### Kahn's Algorithm (BFS-based)
```cpp
class TopologicalSort {
public:
    // Topological sort using Kahn's algorithm
    static std::vector<int> topologicalSortBFS(const Graph& graph) {
        std::vector<int> inDegree(graph.getVertexCount(), 0);
        std::vector<int> result;
        std::queue<int> q;
        
        // Calculate in-degree of each vertex
        for (int u = 0; u < graph.getVertexCount(); u++) {
            for (int v : graph.getNeighbors(u)) {
                inDegree[v]++;
            }
        }
        
        // Add vertices with 0 in-degree to queue
        for (int i = 0; i < graph.getVertexCount(); i++) {
            if (inDegree[i] == 0) {
                q.push(i);
            }
        }
        
        // Process vertices
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            result.push_back(u);
            
            for (int v : graph.getNeighbors(u)) {
                inDegree[v]--;
                if (inDegree[v] == 0) {
                    q.push(v);
                }
            }
        }
        
        // Check if topological sort exists (no cycle)
        if (result.size() != graph.getVertexCount()) {
            return {}; // Graph has a cycle
        }
        
        return result;
    }
    
    // Topological sort using DFS
    static std::vector<int> topologicalSortDFS(const Graph& graph) {
        std::vector<bool> visited(graph.getVertexCount(), false);
        std::vector<int> result;
        std::stack<int> s;
        
        for (int i = 0; i < graph.getVertexCount(); i++) {
            if (!visited[i]) {
                dfsTopological(graph, i, visited, s);
            }
        }
        
        // Pop from stack to get topological order
        while (!s.empty()) {
            result.push_back(s.top());
            s.pop();
        }
        
        return result;
    }
    
    // Check if graph is a DAG
    static bool isDAG(const Graph& graph) {
        return !topologicalSortBFS(graph).empty();
    }
    
private:
    static void dfsTopological(const Graph& graph, int u,
                              std::vector<bool>& visited,
                              std::stack<int>& s) {
        visited[u] = true;
        
        for (int v : graph.getNeighbors(u)) {
            if (!visited[v]) {
                dfsTopological(graph, v, visited, s);
            }
        }
        
        s.push(u);
    }
};
```

## Advanced Graph Algorithms

### 1. Bipartite Graph Check
```cpp
class BipartiteGraph {
public:
    // Check if graph is bipartite using BFS
    static bool isBipartite(const Graph& graph) {
        std::vector<int> color(graph.getVertexCount(), -1);
        
        for (int i = 0; i < graph.getVertexCount(); i++) {
            if (color[i] == -1) {
                if (!bfsBipartite(graph, i, color)) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
private:
    static bool bfsBipartite(const Graph& graph, int start, 
                             std::vector<int>& color) {
        std::queue<int> q;
        q.push(start);
        color[start] = 0;
        
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            
            for (int v : graph.getNeighbors(u)) {
                if (color[v] == -1) {
                    color[v] = 1 - color[u];
                    q.push(v);
                } else if (color[v] == color[u]) {
                    return false; // Same color on adjacent vertices
                }
            }
        }
        
        return true;
    }
};
```

### 2. Graph Center and Eccentricity
```cpp
class GraphProperties {
public:
    // Find eccentricity of all vertices
    static std::vector<int> eccentricity(const Graph& graph) {
        std::vector<int> ecc(graph.getVertexCount());
        
        for (int i = 0; i < graph.getVertexCount(); i++) {
            ecc[i] = bfsEccentricity(graph, i);
        }
        
        return ecc;
    }
    
    // Find graph center (vertices with minimum eccentricity)
    static std::vector<int> center(const Graph& graph) {
        std::vector<int> ecc = eccentricity(graph);
        int minEcc = *std::min_element(ecc.begin(), ecc.end());
        
        std::vector<int> centers;
        for (int i = 0; i < ecc.size(); i++) {
            if (ecc[i] == minEcc) {
                centers.push_back(i);
            }
        }
        
        return centers;
    }
    
private:
    static int bfsEccentricity(const Graph& graph, int start) {
        std::vector<int> distance(graph.getVertexCount(), -1);
        std::queue<int> q;
        
        distance[start] = 0;
        q.push(start);
        
        int maxDist = 0;
        
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            
            maxDist = std::max(maxDist, distance[u]);
            
            for (int v : graph.getNeighbors(u)) {
                if (distance[v] == -1) {
                    distance[v] = distance[u] + 1;
                    q.push(v);
                }
            }
        }
        
        return maxDist;
    }
};
```

## Performance Analysis

### Time Complexity
| Algorithm | Time Complexity |
|-----------|-----------------|
| BFS | O(V + E) |
| DFS | O(V + E) |
| Connected Components | O(V + E) |
| Cycle Detection | O(V + E) |
| Topological Sort | O(V + E) |
| Bipartite Check | O(V + E) |

### Space Complexity
| Algorithm | Space Complexity |
|-----------|------------------|
| BFS | O(V) |
| DFS | O(V) |
| Connected Components | O(V) |
| Cycle Detection | O(V) |
| Topological Sort | O(V) |
| Bipartite Check | O(V) |

Where:
- V = number of vertices
- E = number of edges

## Applications

### 1. Network Analysis
- Finding connected components in social networks
- Shortest path in communication networks
- Network connectivity analysis

### 2. Task Scheduling
- Topological sorting for dependency resolution
- Cycle detection in project planning
- Task ordering with constraints

### 3. Computer Graphics
- Graph traversal for rendering
- Connected component labeling
- Region filling algorithms

### 4. Bioinformatics
- Protein interaction networks
- Gene regulatory networks
- Pathway analysis

## Best Practices

### 1. Algorithm Selection
- Use BFS for shortest path in unweighted graphs
- Use DFS for cycle detection and topological sort
- Choose appropriate graph representation based on density

### 2. Implementation Tips
- Handle disconnected graphs properly
- Consider iterative versions for large graphs
- Use appropriate data structures for efficiency

### 3. Performance Considerations
- Adjacency list is better for sparse graphs
- Adjacency matrix is better for dense graphs
- Consider memory constraints for large graphs

## Summary

Basic graph algorithms provide the foundation for more complex graph-based problem solving. Understanding these fundamental algorithms is essential for working with any graph-based application, from social networks to routing algorithms. Mastering BFS, DFS, and related concepts enables efficient solution of many practical problems.
