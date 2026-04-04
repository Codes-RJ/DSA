# Graph Representations

## Overview
Graph representation is the method of storing graph data structures in computer memory. Different representation methods have different advantages in terms of space complexity, time complexity for various operations, and suitability for different types of graphs and algorithms.

## Topics Covered

### 1. Graph Basics (`01_Graph_Basics.md`)
- Graph terminology and definitions
- Types of graphs (directed, undirected, weighted, unweighted)
- Graph properties and characteristics
- Real-world graph applications
- Graph traversal basics

### 2. Adjacency Matrix (`02_Adjacency_Matrix.md`)
- Matrix representation implementation
- Space and time complexity analysis
- Advantages and disadvantages
- Suitable algorithms and operations
- Optimization techniques

### 3. Adjacency List (`03_Adjacency_List.md`)
- List representation implementation
- Dynamic memory management
- Iterator patterns and traversal
- Performance characteristics
- Use cases and applications

### 4. Edge List (`04_Edge_List.md`)
- Edge-based representation
- Sparse graph optimization
- Kruskal's algorithm compatibility
- Memory efficiency analysis
- Implementation details

### 5. Comparison of Representations (`05_Comparison_of_Representations.md`)
- Space complexity comparison
- Time complexity for common operations
- Memory usage analysis
- Algorithm-specific recommendations
- Choosing the right representation

## Graph Types and Properties

### Basic Graph Types
- **Undirected Graph**: Edges have no direction
- **Directed Graph (Digraph)**: Edges have direction
- **Weighted Graph**: Edges have associated weights
- **Unweighted Graph**: All edges have equal weight
- **Simple Graph**: No self-loops or multiple edges
- **Multigraph**: Can have multiple edges between vertices

### Graph Properties
- **Vertices (Nodes)**: Fundamental units
- **Edges**: Connections between vertices
- **Degree**: Number of edges incident to a vertex
- **Path**: Sequence of vertices connected by edges
- **Cycle**: Path that starts and ends at same vertex
- **Connected**: All vertices reachable from each other

## Representation Methods

### 1. Adjacency Matrix

#### Concept
A 2D array where `matrix[i][j]` represents the edge between vertex `i` and vertex `j`.

#### Implementation
```cpp
class AdjacencyMatrix {
private:
    std::vector<std::vector<int>> matrix;
    int numVertices;
    bool isDirected;
    
public:
    AdjacencyMatrix(int vertices, bool directed = false) 
        : numVertices(vertices), isDirected(directed) {
        matrix.resize(vertices, std::vector<int>(vertices, 0));
    }
    
    void addEdge(int u, int v, int weight = 1) {
        matrix[u][v] = weight;
        if (!isDirected) {
            matrix[v][u] = weight;
        }
    }
    
    void removeEdge(int u, int v) {
        matrix[u][v] = 0;
        if (!isDirected) {
            matrix[v][u] = 0;
        }
    }
    
    bool hasEdge(int u, int v) const {
        return matrix[u][v] != 0;
    }
    
    int getEdgeWeight(int u, int v) const {
        return matrix[u][v];
    }
    
    std::vector<int> getNeighbors(int vertex) const {
        std::vector<int> neighbors;
        for (int i = 0; i < numVertices; i++) {
            if (matrix[vertex][i] != 0) {
                neighbors.push_back(i);
            }
        }
        return neighbors;
    }
    
    int getDegree(int vertex) const {
        int degree = 0;
        for (int i = 0; i < numVertices; i++) {
            if (matrix[vertex][i] != 0) degree++;
        }
        return degree;
    }
    
    void print() const {
        std::cout << "Adjacency Matrix:\n";
        for (int i = 0; i < numVertices; i++) {
            for (int j = 0; j < numVertices; j++) {
                std::cout << matrix[i][j] << " ";
            }
            std::cout << std::endl;
        }
    }
};
```

### 2. Adjacency List

#### Concept
An array of lists where each list contains the neighbors of a vertex.

#### Implementation
```cpp
class AdjacencyList {
private:
    std::vector<std::vector<std::pair<int, int>>> list;
    int numVertices;
    bool isDirected;
    
public:
    AdjacencyList(int vertices, bool directed = false) 
        : numVertices(vertices), isDirected(directed) {
        list.resize(vertices);
    }
    
    void addEdge(int u, int v, int weight = 1) {
        list[u].push_back({v, weight});
        if (!isDirected) {
            list[v].push_back({u, weight});
        }
    }
    
    void removeEdge(int u, int v) {
        list[u].erase(std::remove_if(list[u].begin(), list[u].end(),
                                    [v](const std::pair<int, int>& edge) {
                                        return edge.first == v;
                                    }), list[u].end());
        
        if (!isDirected) {
            list[v].erase(std::remove_if(list[v].begin(), list[v].end(),
                                        [u](const std::pair<int, int>& edge) {
                                            return edge.first == u;
                                        }), list[v].end());
        }
    }
    
    bool hasEdge(int u, int v) const {
        for (const auto& edge : list[u]) {
            if (edge.first == v) return true;
        }
        return false;
    }
    
    int getEdgeWeight(int u, int v) const {
        for (const auto& edge : list[u]) {
            if (edge.first == v) return edge.second;
        }
        return 0;
    }
    
    const std::vector<std::pair<int, int>>& getNeighbors(int vertex) const {
        return list[vertex];
    }
    
    int getDegree(int vertex) const {
        return list[vertex].size();
    }
    
    void print() const {
        std::cout << "Adjacency List:\n";
        for (int i = 0; i < numVertices; i++) {
            std::cout << i << ": ";
            for (const auto& edge : list[i]) {
                std::cout << "(" << edge.first << "," << edge.second << ") ";
            }
            std::cout << std::endl;
        }
    }
};
```

### 3. Edge List

#### Concept
A list of all edges in the graph, typically as pairs of vertices.

#### Implementation
```cpp
class EdgeList {
private:
    struct Edge {
        int u, v, weight;
        Edge(int u, int v, int weight = 1) : u(u), v(v), weight(weight) {}
    };
    
    std::vector<Edge> edges;
    int numVertices;
    bool isDirected;
    
public:
    EdgeList(int vertices, bool directed = false) 
        : numVertices(vertices), isDirected(directed) {}
    
    void addEdge(int u, int v, int weight = 1) {
        edges.emplace_back(u, v, weight);
        if (!isDirected) {
            edges.emplace_back(v, u, weight);
        }
    }
    
    void removeEdge(int u, int v) {
        edges.erase(std::remove_if(edges.begin(), edges.end(),
                                 [u, v](const Edge& edge) {
                                     return edge.u == u && edge.v == v;
                                 }), edges.end());
        
        if (!isDirected) {
            edges.erase(std::remove_if(edges.begin(), edges.end(),
                                     [u, v](const Edge& edge) {
                                         return edge.u == v && edge.v == u;
                                     }), edges.end());
        }
    }
    
    bool hasEdge(int u, int v) const {
        for (const auto& edge : edges) {
            if (edge.u == u && edge.v == v) return true;
        }
        return false;
    }
    
    std::vector<int> getNeighbors(int vertex) const {
        std::vector<int> neighbors;
        for (const auto& edge : edges) {
            if (edge.u == vertex) {
                neighbors.push_back(edge.v);
            }
        }
        return neighbors;
    }
    
    int getDegree(int vertex) const {
        int degree = 0;
        for (const auto& edge : edges) {
            if (edge.u == vertex) degree++;
        }
        return degree;
    }
    
    const std::vector<Edge>& getAllEdges() const {
        return edges;
    }
    
    void print() const {
        std::cout << "Edge List:\n";
        for (const auto& edge : edges) {
            std::cout << edge.u << " -> " << edge.v 
                     << " (weight: " << edge.weight << ")\n";
        }
    }
};
```

## Advanced Representations

### 1. Compressed Sparse Row (CSR)
```cpp
class CSRGraph {
private:
    std::vector<int> rowPtr;    // Row pointers
    std::vector<int> colIdx;    // Column indices
    std::vector<int> values;    // Edge values/weights
    int numVertices;
    int numEdges;
    
public:
    CSRGraph(int vertices) : numVertices(vertices), numEdges(0) {
        rowPtr.resize(vertices + 1, 0);
    }
    
    void buildFromAdjacencyList(const AdjacencyList& adjList) {
        // Build rowPtr
        rowPtr[0] = 0;
        for (int i = 0; i < numVertices; i++) {
            rowPtr[i + 1] = rowPtr[i] + adjList.getDegree(i);
        }
        
        // Build colIdx and values
        colIdx.resize(rowPtr.back());
        values.resize(rowPtr.back());
        
        std::vector<int> currentPos(numVertices, 0);
        for (int i = 0; i < numVertices; i++) {
            for (const auto& edge : adjList.getNeighbors(i)) {
                int pos = rowPtr[i] + currentPos[i]++;
                colIdx[pos] = edge.first;
                values[pos] = edge.second;
            }
        }
        
        numEdges = colIdx.size();
    }
    
    std::vector<int> getNeighbors(int vertex) const {
        std::vector<int> neighbors;
        for (int i = rowPtr[vertex]; i < rowPtr[vertex + 1]; i++) {
            neighbors.push_back(colIdx[i]);
        }
        return neighbors;
    }
    
    int getDegree(int vertex) const {
        return rowPtr[vertex + 1] - rowPtr[vertex];
    }
};
```

### 2. Implicit Graph Representation
```cpp
class ImplicitGraph {
private:
    int gridSize;
    std::vector<std::vector<bool>> obstacles;
    
public:
    ImplicitGraph(int size) : gridSize(size) {
        obstacles.resize(size, std::vector<bool>(size, false));
    }
    
    void setObstacle(int x, int y) {
        if (isValidCell(x, y)) {
            obstacles[x][y] = true;
        }
    }
    
    std::vector<std::pair<int, int>> getNeighbors(int x, int y) const {
        std::vector<std::pair<int, int>> neighbors;
        
        // Four directions: up, down, left, right
        int dx[] = {-1, 1, 0, 0};
        int dy[] = {0, 0, -1, 1};
        
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (isValidCell(nx, ny) && !obstacles[nx][ny]) {
                neighbors.push_back({nx, ny});
            }
        }
        
        return neighbors;
    }
    
private:
    bool isValidCell(int x, int y) const {
        return x >= 0 && x < gridSize && y >= 0 && y < gridSize;
    }
};
```

## Graph Utilities and Algorithms

### 1. Graph Validation
```cpp
class GraphUtils {
public:
    // Check if graph is connected
    static bool isConnected(const AdjacencyList& graph) {
        int numVertices = graph.getNumVertices();
        if (numVertices == 0) return true;
        
        std::vector<bool> visited(numVertices, false);
        std::queue<int> q;
        
        q.push(0);
        visited[0] = true;
        
        while (!q.empty()) {
            int current = q.front();
            q.pop();
            
            for (const auto& neighbor : graph.getNeighbors(current)) {
                if (!visited[neighbor.first]) {
                    visited[neighbor.first] = true;
                    q.push(neighbor.first);
                }
            }
        }
        
        return std::all_of(visited.begin(), visited.end(), 
                          [](bool v) { return v; });
    }
    
    // Check if graph has cycles
    static bool hasCycle(const AdjacencyList& graph) {
        int numVertices = graph.getNumVertices();
        std::vector<bool> visited(numVertices, false);
        std::vector<bool> recursionStack(numVertices, false);
        
        for (int i = 0; i < numVertices; i++) {
            if (!visited[i]) {
                if (hasCycleDFS(graph, i, visited, recursionStack)) {
                    return true;
                }
            }
        }
        
        return false;
    }
    
    // Calculate graph density
    static double getDensity(const AdjacencyList& graph) {
        int numVertices = graph.getNumVertices();
        int numEdges = graph.getNumEdges();
        
        int maxEdges = graph.isDirected() ? 
                      numVertices * (numVertices - 1) :
                      numVertices * (numVertices - 1) / 2;
        
        return static_cast<double>(numEdges) / maxEdges;
    }
    
private:
    static bool hasCycleDFS(const AdjacencyList& graph, int vertex,
                           std::vector<bool>& visited,
                           std::vector<bool>& recursionStack) {
        visited[vertex] = true;
        recursionStack[vertex] = true;
        
        for (const auto& neighbor : graph.getNeighbors(vertex)) {
            if (!visited[neighbor.first]) {
                if (hasCycleDFS(graph, neighbor.first, visited, recursionStack)) {
                    return true;
                }
            } else if (recursionStack[neighbor.first]) {
                return true;
            }
        }
        
        recursionStack[vertex] = false;
        return false;
    }
};
```

### 2. Graph Conversion
```cpp
class GraphConverter {
public:
    // Convert adjacency matrix to adjacency list
    static AdjacencyList matrixToList(const AdjacencyMatrix& matrix) {
        int vertices = matrix.getNumVertices();
        AdjacencyList list(vertices, matrix.isDirected());
        
        for (int i = 0; i < vertices; i++) {
            for (int j = 0; j < vertices; j++) {
                if (matrix.hasEdge(i, j)) {
                    list.addEdge(i, j, matrix.getEdgeWeight(i, j));
                }
            }
        }
        
        return list;
    }
    
    // Convert adjacency list to adjacency matrix
    static AdjacencyMatrix listToMatrix(const AdjacencyList& list) {
        int vertices = list.getNumVertices();
        AdjacencyMatrix matrix(vertices, list.isDirected());
        
        for (int i = 0; i < vertices; i++) {
            for (const auto& neighbor : list.getNeighbors(i)) {
                matrix.addEdge(i, neighbor.first, neighbor.second);
            }
        }
        
        return matrix;
    }
    
    // Convert adjacency list to edge list
    static EdgeList listToEdgeList(const AdjacencyList& list) {
        int vertices = list.getNumVertices();
        EdgeList edgeList(vertices, list.isDirected());
        
        for (int i = 0; i < vertices; i++) {
            for (const auto& neighbor : list.getNeighbors(i)) {
                if (!list.isDirected() || i <= neighbor.first) {
                    edgeList.addEdge(i, neighbor.first, neighbor.second);
                }
            }
        }
        
        return edgeList;
    }
};
```

## Performance Comparison

### Space Complexity
| Representation | Space Complexity |
|----------------|------------------|
| Adjacency Matrix | O(V²) |
| Adjacency List | O(V + E) |
| Edge List | O(E) |
| CSR | O(V + E) |

### Time Complexity for Common Operations

| Operation | Adjacency Matrix | Adjacency List | Edge List |
|-----------|------------------|----------------|-----------|
| Add Edge | O(1) | O(1) | O(1) |
| Remove Edge | O(1) | O(V) | O(E) |
| Check Edge | O(1) | O(V) | O(E) |
| Get Neighbors | O(V) | O(degree) | O(E) |
| Get Degree | O(V) | O(1) | O(E) |

### When to Use Each Representation

#### Adjacency Matrix
- **Dense graphs** (E ≈ V²)
- **Frequent edge queries**
- **Small graphs**
- **Matrix operations**

#### Adjacency List
- **Sparse graphs** (E << V²)
- **Graph traversal algorithms**
- **Memory efficiency**
- **Dynamic graphs**

#### Edge List
- **Kruskal's algorithm**
- **Very sparse graphs**
- **Edge-centric operations**
- **Sorting edges**

## Best Practices

1. **Choose Based on Graph Density**: Matrix for dense, list for sparse
2. **Consider Algorithm Requirements**: Some algorithms prefer specific representations
3. **Memory Constraints**: Consider space complexity for large graphs
4. **Dynamic vs Static**: Lists are better for dynamic graphs
5. **Cache Performance**: Matrix has better cache locality

## Common Applications

### 1. Social Networks
```cpp
class SocialNetwork {
private:
    AdjacencyList graph;
    
public:
    SocialNetwork(int users) : graph(users, true) {} // Directed
    
    void addFriendship(int user1, int user2) {
        graph.addEdge(user1, user2);
        graph.addEdge(user2, user1); // Mutual friendship
    }
    
    std::vector<int> getFriends(int user) {
        std::vector<int> friends;
        for (const auto& neighbor : graph.getNeighbors(user)) {
            friends.push_back(neighbor.first);
        }
        return friends;
    }
    
    int getFriendCount(int user) {
        return graph.getDegree(user);
    }
};
```

### 2. Road Networks
```cpp
class RoadNetwork {
private:
    AdjacencyList graph;
    
public:
    RoadNetwork(int intersections) : graph(intersections, false) {} // Undirected
    
    void addRoad(int intersection1, int intersection2, int distance) {
        graph.addEdge(intersection1, intersection2, distance);
    }
    
    std::vector<std::pair<int, int>> getConnectedRoads(int intersection) {
        return graph.getNeighbors(intersection);
    }
};
```

## Summary

Graph representation is a fundamental concept that significantly impacts algorithm performance and memory usage. Understanding the trade-offs between different representations enables optimal algorithm design and efficient problem-solving in various domains involving network structures.
