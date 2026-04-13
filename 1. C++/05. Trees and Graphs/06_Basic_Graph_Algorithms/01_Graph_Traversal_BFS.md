# Graph Traversal - BFS (Breadth-First Search) - Complete Guide

## 📖 Overview

Breadth-First Search (BFS) is a fundamental graph traversal algorithm that explores vertices level by level, visiting all neighbors of a vertex before moving to their neighbors. It uses a queue data structure and is particularly useful for finding the shortest path in unweighted graphs.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Queue-based** | Uses FIFO (First In, First Out) principle |
| **Level Order** | Explores vertices by distance from source |
| **Shortest Path** | Finds minimum number of edges in unweighted graphs |
| **Parent Array** | Tracks the parent of each node for path reconstruction |
| **Distance Array** | Stores distance from source vertex |
| **Visited Tracking** | Essential to avoid cycles |

---

## 📊 BFS Traversal Visualization

### Example Graph
```
    0 --- 1
    |     |
    |     |
    3 --- 2
    
    Adjacency List:
    0: 1, 3
    1: 0, 2
    2: 1, 3
    3: 0, 2
```

### BFS Order (Starting from 0)
```
Level 0: 0
Level 1: 1, 3
Level 2: 2

Order: 0 → 1 → 3 → 2

Step-by-step:
Step 1: Visit 0, add to queue
Step 2: Visit all neighbors of 0 (1, 3)
Step 3: Visit all neighbors of 1 (2) and 3 (2)
Step 4: 2 already visited
```

---

## 📝 Complete BFS Implementation

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <algorithm>
#include <iomanip>
#include <climits>
using namespace std;

class Graph {
private:
    int vertices;
    vector<list<int>> adj;
    bool isDirected;
    
public:
    Graph(int v, bool directed = false) : vertices(v), isDirected(directed) {
        adj.resize(v);
    }
    
    void addEdge(int u, int v) {
        adj[u].push_back(v);
        if (!isDirected) {
            adj[v].push_back(u);
        }
    }
    
    // ============ BASIC BFS TRAVERSAL ============
    void bfs(int start) {
        vector<bool> visited(vertices, false);
        queue<int> q;
        vector<int> order;
        
        visited[start] = true;
        q.push(start);
        
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            order.push_back(v);
            
            for (int neighbor : adj[v]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }
        
        cout << "BFS Order from " << start << ": ";
        for (int v : order) cout << v << " ";
        cout << endl;
    }
    
    // ============ BFS WITH LEVEL (DISTANCE) TRACKING ============
    void bfsWithLevels(int start) {
        vector<bool> visited(vertices, false);
        vector<int> distance(vertices, -1);
        vector<int> parent(vertices, -1);
        queue<int> q;
        
        visited[start] = true;
        distance[start] = 0;
        q.push(start);
        
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            
            for (int neighbor : adj[v]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    distance[neighbor] = distance[v] + 1;
                    parent[neighbor] = v;
                    q.push(neighbor);
                }
            }
        }
        
        cout << "\nBFS with Levels from " << start << ":" << endl;
        for (int i = 0; i < vertices; i++) {
            cout << "Vertex " << i << ": distance = " << distance[i];
            if (parent[i] != -1) {
                cout << ", parent = " << parent[i];
            }
            cout << endl;
        }
    }
    
    // ============ SHORTEST PATH USING BFS ============
    vector<int> shortestPath(int start, int end) {
        vector<bool> visited(vertices, false);
        vector<int> parent(vertices, -1);
        queue<int> q;
        
        visited[start] = true;
        q.push(start);
        
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            
            if (v == end) break;
            
            for (int neighbor : adj[v]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    parent[neighbor] = v;
                    q.push(neighbor);
                }
            }
        }
        
        // Reconstruct path
        vector<int> path;
        if (parent[end] != -1 || start == end) {
            for (int v = end; v != -1; v = parent[v]) {
                path.push_back(v);
            }
            reverse(path.begin(), path.end());
        }
        
        return path;
    }
    
    void printShortestPath(int start, int end) {
        vector<int> path = shortestPath(start, end);
        if (!path.empty()) {
            cout << "Shortest path from " << start << " to " << end << ": ";
            for (int v : path) cout << v << " ";
            cout << "(length = " << path.size() - 1 << ")" << endl;
        } else {
            cout << "No path from " << start << " to " << end << endl;
        }
    }
    
    // ============ BFS FOR DISCONNECTED GRAPH ============
    void bfsDisconnected() {
        vector<bool> visited(vertices, false);
        vector<vector<int>> components;
        
        for (int i = 0; i < vertices; i++) {
            if (!visited[i]) {
                vector<int> component;
                queue<int> q;
                
                visited[i] = true;
                q.push(i);
                
                while (!q.empty()) {
                    int v = q.front();
                    q.pop();
                    component.push_back(v);
                    
                    for (int neighbor : adj[v]) {
                        if (!visited[neighbor]) {
                            visited[neighbor] = true;
                            q.push(neighbor);
                        }
                    }
                }
                components.push_back(component);
            }
        }
        
        cout << "\nBFS on Disconnected Graph:" << endl;
        cout << "Number of connected components: " << components.size() << endl;
        for (size_t i = 0; i < components.size(); i++) {
            cout << "Component " << i + 1 << ": ";
            for (int v : components[i]) cout << v << " ";
            cout << endl;
        }
    }
    
    // ============ LEVEL ORDER PRINTING ============
    void printLevelOrder() {
        vector<bool> visited(vertices, false);
        queue<int> q;
        
        cout << "\nLevel Order Traversal (by components):" << endl;
        int componentNum = 1;
        
        for (int i = 0; i < vertices; i++) {
            if (!visited[i]) {
                cout << "Component " << componentNum++ << ":" << endl;
                queue<int> levelQueue;
                levelQueue.push(i);
                visited[i] = true;
                
                while (!levelQueue.empty()) {
                    int levelSize = levelQueue.size();
                    cout << "  ";
                    for (int j = 0; j < levelSize; j++) {
                        int v = levelQueue.front();
                        levelQueue.pop();
                        cout << v << " ";
                        
                        for (int neighbor : adj[v]) {
                            if (!visited[neighbor]) {
                                visited[neighbor] = true;
                                levelQueue.push(neighbor);
                            }
                        }
                    }
                    cout << endl;
                }
            }
        }
    }
    
    // ============ BFS FOR BIPARTITE CHECK ============
    bool isBipartite() {
        vector<int> color(vertices, -1);  // -1: uncolored, 0: color A, 1: color B
        queue<int> q;
        
        for (int i = 0; i < vertices; i++) {
            if (color[i] == -1) {
                color[i] = 0;
                q.push(i);
                
                while (!q.empty()) {
                    int v = q.front();
                    q.pop();
                    
                    for (int neighbor : adj[v]) {
                        if (color[neighbor] == -1) {
                            color[neighbor] = color[v] ^ 1;  // Alternate color
                            q.push(neighbor);
                        } else if (color[neighbor] == color[v]) {
                            return false;  // Same color on adjacent vertices
                        }
                    }
                }
            }
        }
        return true;
    }
    
    // ============ FIND ALL VERTICES AT GIVEN DISTANCE ============
    vector<int> verticesAtDistance(int start, int targetDist) {
        vector<bool> visited(vertices, false);
        vector<int> distance(vertices, -1);
        queue<int> q;
        vector<int> result;
        
        visited[start] = true;
        distance[start] = 0;
        q.push(start);
        
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            
            if (distance[v] == targetDist) {
                result.push_back(v);
            }
            
            for (int neighbor : adj[v]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    distance[neighbor] = distance[v] + 1;
                    q.push(neighbor);
                }
            }
        }
        
        return result;
    }
    
    // ============ DISPLAY GRAPH ============
    void display() {
        cout << "\nGraph Adjacency List:" << endl;
        cout << "Type: " << (isDirected ? "Directed" : "Undirected") << endl;
        for (int i = 0; i < vertices; i++) {
            cout << i << ": ";
            for (int neighbor : adj[i]) {
                cout << neighbor << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    cout << "=== Graph BFS Traversal Demo ===" << endl;
    
    // Create connected graph
    Graph g(6, false);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(1, 4);
    g.addEdge(2, 4);
    g.addEdge(3, 4);
    g.addEdge(3, 5);
    
    g.display();
    
    cout << "\n=== BFS Traversal ===" << endl;
    g.bfs(0);
    
    cout << "\n=== BFS with Level Tracking ===" << endl;
    g.bfsWithLevels(0);
    
    cout << "\n=== Shortest Path ===" << endl;
    g.printShortestPath(0, 5);
    g.printShortestPath(0, 4);
    g.printShortestPath(2, 5);
    
    cout << "\n=== Vertices at Distance ===" << endl;
    vector<int> atDist2 = g.verticesAtDistance(0, 2);
    cout << "Vertices at distance 2 from 0: ";
    for (int v : atDist2) cout << v << " ";
    cout << endl;
    
    // Disconnected graph
    cout << "\n=== Disconnected Graph ===" << endl;
    Graph g2(6, false);
    g2.addEdge(0, 1);
    g2.addEdge(0, 2);
    g2.addEdge(3, 4);
    g2.addEdge(3, 5);
    g2.display();
    g2.bfsDisconnected();
    g2.printLevelOrder();
    
    // Bipartite check
    cout << "\n=== Bipartite Check ===" << endl;
    Graph g3(4, false);
    g3.addEdge(0, 1);
    g3.addEdge(0, 3);
    g3.addEdge(1, 2);
    g3.addEdge(2, 3);
    g3.display();
    cout << "Is bipartite? " << (g3.isBipartite() ? "Yes" : "No") << endl;
    
    // Non-bipartite graph
    Graph g4(3, false);
    g4.addEdge(0, 1);
    g4.addEdge(1, 2);
    g4.addEdge(2, 0);
    g4.display();
    cout << "Is bipartite? " << (g4.isBipartite() ? "Yes" : "No") << endl;
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Basic BFS** | O(V + E) | O(V) |
| **BFS with Levels** | O(V + E) | O(V) |
| **Shortest Path** | O(V + E) | O(V) |
| **Connected Components** | O(V + E) | O(V) |
| **Bipartite Check** | O(V + E) | O(V) |

---

## 🎯 BFS Applications

| Application | Description |
|-------------|-------------|
| **Shortest Path** | Minimum edges in unweighted graph |
| **Connected Components** | Finding all connected subgraphs |
| **Bipartite Check** | Testing 2-colorability |
| **Web Crawling** | Indexing pages level by level |
| **Social Networks** | Finding friend connections (degrees of separation) |
| **GPS Navigation** | Shortest route finding |
| **Puzzle Solving** | Minimum moves to solve puzzle |
| **Network Broadcasting** | Sending messages to all nodes |

---

## 📊 BFS vs DFS Comparison

| Aspect | BFS | DFS |
|--------|-----|-----|
| **Data Structure** | Queue | Stack |
| **Order** | Level by level | Depth first |
| **Shortest Path** | Yes (unweighted) | No |
| **Space Complexity** | O(V) (queue) | O(V) (stack) |
| **Memory Usage** | More (queue) | Less (stack) |
| **Best for** | Shortest path, level order | Topological sort, connectivity |

---

## ✅ Key Takeaways

1. **BFS** explores vertices level by level
2. **Queue** is the primary data structure
3. **Time complexity** O(V + E)
4. **Finds shortest path** in unweighted graphs
5. **Parent array** enables path reconstruction
6. **Level tracking** shows distance from source
7. **Disconnected graphs** require multiple BFS runs
8. **Bipartite check** uses 2-coloring via BFS

---
---

## Next Step

- Go to [02_Graph_Traversal_DFS.md](02_Graph_Traversal_DFS.md) to continue with Graph Traversal DFS.
