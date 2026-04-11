# Graph Traversal - BFS (Breadth-First Search)

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

---

## 📊 BFS Traversal Order

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

Step 1: Visit 0
Step 2: Visit all neighbors of 0 (1, 3)
Step 3: Visit all neighbors of 1 (2) and 3 (2)
Step 4: 2 already visited
```

---

## 📝 BFS Implementation

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <algorithm>
#include <iomanip>
using namespace std;

class Graph {
private:
    int vertices;
    vector<list<int>> adj;
    
public:
    Graph(int v) : vertices(v) {
        adj.resize(v);
    }
    
    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u);  // Undirected graph
    }
    
    // Basic BFS traversal
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
            
            // Sort neighbors for consistent output
            vector<int> neighbors(adj[v].begin(), adj[v].end());
            sort(neighbors.begin(), neighbors.end());
            
            for (int neighbor : neighbors) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }
        
        cout << "BFS Order: ";
        for (int v : order) cout << v << " ";
        cout << endl;
    }
    
    // BFS with level (distance) tracking
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
            
            vector<int> neighbors(adj[v].begin(), adj[v].end());
            sort(neighbors.begin(), neighbors.end());
            
            for (int neighbor : neighbors) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    distance[neighbor] = distance[v] + 1;
                    parent[neighbor] = v;
                    q.push(neighbor);
                }
            }
        }
        
        cout << "\nBFS with Levels:" << endl;
        for (int i = 0; i < vertices; i++) {
            cout << "Vertex " << i << ": distance = " << distance[i];
            if (parent[i] != -1) {
                cout << ", parent = " << parent[i];
            }
            cout << endl;
        }
    }
    
    // Find shortest path using BFS
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
    
    // BFS for disconnected graph
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
        cout << "Number of components: " << components.size() << endl;
        for (size_t i = 0; i < components.size(); i++) {
            cout << "Component " << i + 1 << ": ";
            for (int v : components[i]) cout << v << " ";
            cout << endl;
        }
    }
    
    // Display adjacency list
    void display() {
        cout << "\nGraph Adjacency List:" << endl;
        for (int i = 0; i < vertices; i++) {
            cout << i << ": ";
            vector<int> neighbors(adj[i].begin(), adj[i].end());
            sort(neighbors.begin(), neighbors.end());
            for (int neighbor : neighbors) {
                cout << neighbor << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    cout << "=== Breadth-First Search (BFS) Demo ===" << endl;
    
    // Create graph
    Graph g(8);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(1, 4);
    g.addEdge(2, 4);
    g.addEdge(2, 5);
    g.addEdge(3, 6);
    g.addEdge(4, 6);
    g.addEdge(4, 7);
    g.addEdge(5, 7);
    
    g.display();
    
    cout << "\n=== BFS Traversal ===" << endl;
    g.bfs(0);
    
    cout << "\n=== BFS with Level Tracking ===" << endl;
    g.bfsWithLevels(0);
    
    cout << "\n=== Shortest Path ===" << endl;
    vector<int> path = g.shortestPath(0, 7);
    cout << "Shortest path from 0 to 7: ";
    for (int v : path) cout << v << " ";
    cout << " (length = " << path.size() - 1 << ")" << endl;
    
    path = g.shortestPath(0, 6);
    cout << "Shortest path from 0 to 6: ";
    for (int v : path) cout << v << " ";
    cout << " (length = " << path.size() - 1 << ")" << endl;
    
    // Create disconnected graph
    Graph g2(6);
    g2.addEdge(0, 1);
    g2.addEdge(0, 2);
    g2.addEdge(3, 4);
    g2.addEdge(3, 5);
    
    cout << "\n=== Disconnected Graph ===" << endl;
    g2.display();
    g2.bfsDisconnected();
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Aspect | Complexity |
|--------|------------|
| **Time Complexity** | O(V + E) |
| **Space Complexity** | O(V) (queue + visited array) |
| **Adjacency Matrix** | O(V²) |

---

## 🎯 Applications of BFS

| Application | Description |
|-------------|-------------|
| **Shortest Path** | Minimum edges in unweighted graph |
| **Web Crawling** | Indexing web pages level by level |
| **Social Networks** | Finding friend connections |
| **GPS Navigation** | Shortest route finding |
| **Broadcasting** | Sending messages to all nodes |
| **Garbage Collection** | Reachability analysis |
| **Puzzle Solving** | Minimum moves to solve puzzle |
| **Network Broadcasting** | Flood fill algorithms |

---

## 📊 BFS vs DFS Comparison

| Aspect | BFS | DFS |
|--------|-----|-----|
| **Data Structure** | Queue | Stack |
| **Order** | Level by level | Depth first |
| **Shortest Path** | Yes (unweighted) | No |
| **Space Complexity** | O(V) | O(V) |
| **Memory Usage** | More (queue) | Less (stack) |
| **Best for** | Shortest path | Topological sort |

---

## ✅ Key Takeaways

1. **BFS** explores vertices level by level
2. **Queue** is the primary data structure
3. **Time complexity** O(V + E)
4. **Finds shortest path** in unweighted graphs
5. **Parent array** enables path reconstruction
6. **Level tracking** shows distance from source
7. **Disconnected graphs** require multiple BFS runs

---