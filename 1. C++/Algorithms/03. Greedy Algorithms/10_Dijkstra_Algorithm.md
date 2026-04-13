I'll continue with the missing Graph Algorithms. Let me start with the next one in sequence.

---

# Graph Algorithm - Dijkstra's Algorithm (Shortest Path)

## 📖 Overview

Dijkstra's Algorithm finds the shortest path from a source vertex to all other vertices in a weighted graph with **non-negative edge weights**. It is widely used in GPS navigation, network routing, and game development.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Single Source Shortest Path** | Finds shortest path from source to all vertices |
| **Greedy Approach** | Always picks vertex with minimum distance |
| **Non-negative Weights** | Fails if negative edges exist |
| **Priority Queue** | Efficient implementation using min-heap |
| **Relaxation** | Updating distances when shorter path found |

---

## 📊 How Dijkstra Works

### Step-by-step Visualization

```
Graph:
        2
    0 ---→ 1
    |       |
   4|       |1
    ↓       ↓
    2 ---→ 3
        3

Initial distances from 0: [0, ∞, ∞, ∞]

Step 1: Visit 0
  - Update 1: 0 + 2 = 2
  - Update 2: 0 + 4 = 4
  Distances: [0, 2, 4, ∞]

Step 2: Visit 1 (smallest unvisited)
  - Update 3: 2 + 1 = 3
  Distances: [0, 2, 4, 3]

Step 3: Visit 3 (smallest unvisited)
  - No updates (no outgoing edges)
  Distances: [0, 2, 4, 3]

Step 4: Visit 2 (last vertex)
  - Update 3: min(3, 4 + 3 = 7) → remains 3

Final shortest paths from 0:
  → 0: 0
  → 1: 2 (0→1)
  → 2: 4 (0→2)
  → 3: 3 (0→1→3)
```

---

## 📝 Complete Implementation

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <climits>
#include <algorithm>
#include <iomanip>
using namespace std;

class Graph {
private:
    int vertices;
    vector<list<pair<int, int>>> adj;  // {neighbor, weight}
    bool isDirected;
    
public:
    Graph(int v, bool directed = false) : vertices(v), isDirected(directed) {
        adj.resize(v);
    }
    
    void addEdge(int u, int v, int weight = 1) {
        adj[u].push_back({v, weight});
        if (!isDirected) {
            adj[v].push_back({u, weight});
        }
    }
    
    // ============ DIJKSTRA'S ALGORITHM (NAIVE) ============
    // Time: O(V²), Space: O(V)
    vector<int> dijkstraNaive(int source) {
        vector<int> dist(vertices, INT_MAX);
        vector<bool> visited(vertices, false);
        
        dist[source] = 0;
        
        for (int count = 0; count < vertices - 1; count++) {
            // Find minimum distance vertex not yet processed
            int u = -1;
            int minDist = INT_MAX;
            for (int i = 0; i < vertices; i++) {
                if (!visited[i] && dist[i] < minDist) {
                    minDist = dist[i];
                    u = i;
                }
            }
            
            if (u == -1) break;  // No reachable vertices
            
            visited[u] = true;
            
            // Relax all neighbors of u
            for (auto& [v, weight] : adj[u]) {
                if (!visited[v] && dist[u] != INT_MAX && 
                    dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                }
            }
        }
        
        return dist;
    }
    
    // ============ DIJKSTRA'S ALGORITHM (PRIORITY QUEUE) ============
    // Time: O((V+E) log V), Space: O(V)
    vector<int> dijkstraPQ(int source) {
        vector<int> dist(vertices, INT_MAX);
        vector<int> parent(vertices, -1);
        
        // Min-heap: {distance, vertex}
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        
        dist[source] = 0;
        pq.push({0, source});
        
        while (!pq.empty()) {
            int d = pq.top().first;
            int u = pq.top().second;
            pq.pop();
            
            // Skip if we found a better distance already
            if (d > dist[u]) continue;
            
            for (auto& [v, weight] : adj[u]) {
                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                    parent[v] = u;
                    pq.push({dist[v], v});
                }
            }
        }
        
        return dist;
    }
    
    // ============ GET SHORTEST PATH TREE ============
    vector<int> shortestPathTree(int source) {
        vector<int> dist(vertices, INT_MAX);
        vector<int> parent(vertices, -1);
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        
        dist[source] = 0;
        pq.push({0, source});
        
        while (!pq.empty()) {
            int d = pq.top().first;
            int u = pq.top().second;
            pq.pop();
            
            if (d > dist[u]) continue;
            
            for (auto& [v, weight] : adj[u]) {
                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                    parent[v] = u;
                    pq.push({dist[v], v});
                }
            }
        }
        
        return parent;
    }
    
    // ============ GET PATH FROM SOURCE TO TARGET ============
    vector<int> getPath(int source, int target) {
        vector<int> parent = shortestPathTree(source);
        
        if (parent[target] == -1 && source != target) {
            return {};  // No path
        }
        
        vector<int> path;
        for (int v = target; v != -1; v = parent[v]) {
            path.push_back(v);
        }
        reverse(path.begin(), path.end());
        
        return path;
    }
    
    // ============ DIJKSTRA WITH PATH PRINTING ============
    void printShortestPaths(int source) {
        vector<int> dist = dijkstraPQ(source);
        cout << "\nShortest distances from vertex " << source << ":\n";
        cout << "Vertex\tDistance\tPath\n";
        
        for (int i = 0; i < vertices; i++) {
            cout << i << "\t";
            if (dist[i] == INT_MAX) {
                cout << "INF\t\tNo path";
            } else {
                cout << dist[i] << "\t\t";
                vector<int> path = getPath(source, i);
                for (int v : path) cout << v << " ";
            }
            cout << endl;
        }
    }
    
    // ============ FIND SHORTEST DISTANCE BETWEEN TWO VERTICES ============
    int shortestDistance(int source, int target) {
        vector<int> dist = dijkstraPQ(source);
        return dist[target];
    }
    
    // ============ DIJKSTRA FOR SPECIFIC TARGET (EARLY STOP) ============
    int shortestPathToTarget(int source, int target) {
        vector<int> dist(vertices, INT_MAX);
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        
        dist[source] = 0;
        pq.push({0, source});
        
        while (!pq.empty()) {
            int d = pq.top().first;
            int u = pq.top().second;
            pq.pop();
            
            if (u == target) return d;  // Early termination
            
            if (d > dist[u]) continue;
            
            for (auto& [v, weight] : adj[u]) {
                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                    pq.push({dist[v], v});
                }
            }
        }
        
        return INT_MAX;  // No path
    }
    
    // ============ PRINT DISTANCE MATRIX ============
    void printDistanceMatrix() {
        cout << "\nDistance Matrix (All-pairs shortest paths using Dijkstra from each vertex):\n";
        cout << "   ";
        for (int i = 0; i < vertices; i++) {
            cout << setw(4) << i;
        }
        cout << endl;
        
        for (int i = 0; i < vertices; i++) {
            vector<int> dist = dijkstraPQ(i);
            cout << setw(2) << i << " ";
            for (int j = 0; j < vertices; j++) {
                if (dist[j] == INT_MAX) {
                    cout << "  ∞";
                } else {
                    cout << setw(4) << dist[j];
                }
            }
            cout << endl;
        }
    }
    
    // ============ CHECK IF GRAPH HAS NEGATIVE EDGES ============
    bool hasNegativeEdges() {
        for (int u = 0; u < vertices; u++) {
            for (auto& [v, weight] : adj[u]) {
                if (weight < 0) return true;
            }
        }
        return false;
    }
    
    // ============ DISPLAY GRAPH ============
    void display() {
        cout << "\nGraph Adjacency List (Weighted):" << endl;
        for (int i = 0; i < vertices; i++) {
            cout << i << ": ";
            for (auto& [neighbor, weight] : adj[i]) {
                cout << "(" << neighbor << "," << weight << ") ";
            }
            cout << endl;
        }
    }
};

int main() {
    cout << "=== Dijkstra's Algorithm Demo ===" << endl;
    
    // Example graph
    Graph g(5, false);
    g.addEdge(0, 1, 2);
    g.addEdge(0, 2, 4);
    g.addEdge(1, 2, 1);
    g.addEdge(1, 3, 7);
    g.addEdge(2, 3, 3);
    g.addEdge(3, 4, 1);
    g.addEdge(2, 4, 5);
    
    g.display();
    
    // Check for negative edges
    if (g.hasNegativeEdges()) {
        cout << "\nWarning: Graph contains negative edges! Dijkstra may not work correctly." << endl;
    }
    
    // Naive implementation
    cout << "\n--- Naive Dijkstra (O(V²)) ---" << endl;
    vector<int> distNaive = g.dijkstraNaive(0);
    cout << "Distances from 0: ";
    for (int d : distNaive) cout << d << " ";
    cout << endl;
    
    // Priority Queue implementation
    cout << "\n--- Dijkstra with Priority Queue (O((V+E)log V)) ---" << endl;
    vector<int> distPQ = g.dijkstraPQ(0);
    cout << "Distances from 0: ";
    for (int d : distPQ) cout << d << " ";
    cout << endl;
    
    // Print shortest paths
    g.printShortestPaths(0);
    
    // Distance matrix
    g.printDistanceMatrix();
    
    // Shortest path between two vertices
    cout << "\n--- Specific Path Queries ---" << endl;
    cout << "Shortest distance from 0 to 4: " << g.shortestDistance(0, 4) << endl;
    cout << "Shortest path from 0 to 4: ";
    vector<int> path = g.getPath(0, 4);
    for (int v : path) cout << v << " ";
    cout << endl;
    
    // Early termination
    cout << "\n--- Early Termination (0 → 4) ---" << endl;
    int dist = g.shortestPathToTarget(0, 4);
    cout << "Distance (early stop): " << dist << endl;
    
    // Larger graph example
    cout << "\n--- Road Network Example ---" << endl;
    Graph road(6, false);
    road.addEdge(0, 1, 5);
    road.addEdge(0, 2, 3);
    road.addEdge(1, 3, 6);
    road.addEdge(1, 4, 2);
    road.addEdge(2, 4, 4);
    road.addEdge(2, 5, 2);
    road.addEdge(3, 4, 1);
    road.addEdge(4, 5, 3);
    
    road.display();
    road.printShortestPaths(0);
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Implementation | Time Complexity | Space Complexity |
|----------------|----------------|------------------|
| **Naive (Array-based)** | O(V²) | O(V) |
| **Priority Queue (Binary Heap)** | O((V+E) log V) | O(V) |
| **Priority Queue (Fibonacci Heap)** | O(E + V log V) | O(V) |

---

## 🎯 Applications of Dijkstra's Algorithm

| Application | Description |
|-------------|-------------|
| **GPS Navigation** | Shortest route between locations |
| **Network Routing** | OSPF (Open Shortest Path First) protocol |
| **Game Development** | Pathfinding for NPCs |
| **Social Networks** | Degree of separation |
| **Telecommunications** | Optimal data routing |
| **Robotics** | Path planning |
| **Transportation** | Shortest delivery routes |

---

## 📊 Dijkstra vs BFS vs Bellman-Ford

| Algorithm | Edge Weights | Negative Edges | Time Complexity |
|-----------|--------------|----------------|-----------------|
| **BFS** | Unweighted only | No | O(V+E) |
| **Dijkstra** | Non-negative only | No | O((V+E) log V) |
| **Bellman-Ford** | Any (negative allowed) | Yes | O(V×E) |

---

## ✅ Key Takeaways

1. **Dijkstra's algorithm** finds shortest paths from single source
2. **Requires non-negative edge weights** (fails with negatives)
3. **Greedy approach** with optimal substructure
4. **Priority queue** implementation is most efficient
5. **Early termination** possible when target is known
6. **Cannot handle negative cycles** (use Bellman-Ford)
7. **Time complexity** O((V+E) log V) with binary heap

---
---

## Next Step

- Go to [11_Prim_Algorithm.md](11_Prim_Algorithm.md) to continue with Prim Algorithm.
