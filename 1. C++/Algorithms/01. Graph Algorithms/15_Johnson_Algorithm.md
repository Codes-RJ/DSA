# Graph Algorithm - Johnson's Algorithm (All-Pairs Shortest Path)

## 📖 Overview

Johnson's algorithm finds the shortest paths between all pairs of vertices in a weighted directed graph. It combines the benefits of Dijkstra's algorithm (efficiency for sparse graphs) and Bellman-Ford (handling negative weights) by using reweighting to eliminate negative edges. It runs in O(V² log V + V × E) time, making it faster than Floyd-Warshall for sparse graphs.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Reweighting** | Assign new weights to eliminate negatives |
| **Potential Function** | Distance from a dummy source |
| **Reduced Weight** | w'(u,v) = w(u,v) + h(u) - h(v) |
| **No Negative Cycles** | Required for correctness |
| **Sparse Graphs** | Johnson's performs better than Floyd-Warshall |

---

## 📊 How Johnson's Algorithm Works

```
1. Add a dummy source vertex (s) connected to all vertices with weight 0
2. Run Bellman-Ford from s to compute potential h(v)
3. Remove dummy source
4. Reweight edges: w'(u,v) = w(u,v) + h(u) - h(v)
5. Run Dijkstra from each vertex using w'
6. Convert distances back: d(u,v) = d'(u,v) - h(u) + h(v)
```

---

## 📝 Complete Implementation

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <algorithm>
#include <iomanip>
#include <chrono>
using namespace std;

class JohnsonAlgorithm {
private:
    int vertices;
    vector<vector<pair<int, int>>> adj;
    
public:
    JohnsonAlgorithm(int v) : vertices(v) {
        adj.resize(v);
    }
    
    void addEdge(int u, int v, int weight) {
        adj[u].push_back({v, weight});
    }
    
    // ============ JOHNSON'S ALGORITHM ============
    vector<vector<int>> johnson() {
        // Step 1: Add dummy vertex (index = vertices)
        vector<vector<pair<int, int>>> adjWithDummy = adj;
        adjWithDummy.resize(vertices + 1);
        
        for (int i = 0; i < vertices; i++) {
            adjWithDummy[vertices].push_back({i, 0});
        }
        
        // Step 2: Run Bellman-Ford from dummy vertex
        vector<int> h = bellmanFord(vertices, adjWithDummy);
        
        if (h.empty()) {
            cout << "Graph contains a negative cycle!" << endl;
            return {};
        }
        
        // Step 3: Reweight edges
        vector<vector<pair<int, int>>> reweightedAdj(vertices);
        for (int u = 0; u < vertices; u++) {
            for (auto& edge : adj[u]) {
                int v = edge.first;
                int w = edge.second;
                reweightedAdj[u].push_back({v, w + h[u] - h[v]});
            }
        }
        
        // Step 4: Run Dijkstra from each vertex
        vector<vector<int>> dist(vertices, vector<int>(vertices, INT_MAX));
        
        for (int u = 0; u < vertices; u++) {
            vector<int> d = dijkstra(u, reweightedAdj);
            for (int v = 0; v < vertices; v++) {
                if (d[v] != INT_MAX) {
                    // Step 5: Convert back to original distances
                    dist[u][v] = d[v] - h[u] + h[v];
                }
            }
        }
        
        return dist;
    }
    
private:
    vector<int> bellmanFord(int source, vector<vector<pair<int, int>>>& graph) {
        int n = graph.size();
        vector<int> dist(n, INT_MAX);
        dist[source] = 0;
        
        // Relax edges V-1 times
        for (int i = 0; i < n - 1; i++) {
            bool updated = false;
            for (int u = 0; u < n; u++) {
                if (dist[u] == INT_MAX) continue;
                for (auto& edge : graph[u]) {
                    int v = edge.first;
                    int w = edge.second;
                    if (dist[u] + w < dist[v]) {
                        dist[v] = dist[u] + w;
                        updated = true;
                    }
                }
            }
            if (!updated) break;
        }
        
        // Check for negative cycle
        for (int u = 0; u < n; u++) {
            if (dist[u] == INT_MAX) continue;
            for (auto& edge : graph[u]) {
                int v = edge.first;
                int w = edge.second;
                if (dist[u] + w < dist[v]) {
                    return {};  // Negative cycle detected
                }
            }
        }
        
        return dist;
    }
    
    vector<int> dijkstra(int source, vector<vector<pair<int, int>>>& graph) {
        int n = graph.size();
        vector<int> dist(n, INT_MAX);
        vector<bool> visited(n, false);
        
        using P = pair<int, int>;
        priority_queue<P, vector<P>, greater<P>> pq;
        
        dist[source] = 0;
        pq.push({0, source});
        
        while (!pq.empty()) {
            int u = pq.top().second;
            pq.pop();
            
            if (visited[u]) continue;
            visited[u] = true;
            
            for (auto& edge : graph[u]) {
                int v = edge.first;
                int w = edge.second;
                if (dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    pq.push({dist[v], v});
                }
            }
        }
        
        return dist;
    }
    
public:
    // ============ DISPLAY ============
    void displayGraph() {
        cout << "\nGraph (Weighted Directed):\n";
        for (int u = 0; u < vertices; u++) {
            cout << u << ": ";
            for (auto& edge : adj[u]) {
                cout << "(" << edge.first << "," << edge.second << ") ";
            }
            cout << endl;
        }
    }
    
    void displayDistanceMatrix(const vector<vector<int>>& dist) {
        if (dist.empty()) return;
        
        cout << "\nAll-Pairs Shortest Paths:\n";
        cout << "   ";
        for (int i = 0; i < vertices; i++) {
            cout << setw(4) << i;
        }
        cout << endl;
        
        for (int i = 0; i < vertices; i++) {
            cout << setw(2) << i << " ";
            for (int j = 0; j < vertices; j++) {
                if (dist[i][j] == INT_MAX) {
                    cout << "  ∞";
                } else {
                    cout << setw(4) << dist[i][j];
                }
            }
            cout << endl;
        }
    }
    
    void displayPaths(const vector<vector<int>>& dist) {
        cout << "\nDetailed Paths:\n";
        for (int i = 0; i < vertices; i++) {
            for (int j = 0; j < vertices; j++) {
                if (i != j && dist[i][j] != INT_MAX) {
                    cout << "Distance from " << i << " to " << j << ": " << dist[i][j] << endl;
                }
            }
        }
    }
    
    // ============ GET SHORTEST PATH BETWEEN TWO VERTICES ============
    int shortestPath(int source, int dest) {
        vector<vector<int>> dist = johnson();
        if (dist.empty() || dist[source][dest] == INT_MAX) {
            return -1;
        }
        return dist[source][dest];
    }
};

int main() {
    cout << "=== Johnson's Algorithm Demo ===" << endl;
    
    // Example 1: Simple graph with negative edge
    cout << "\n1. Graph with Negative Edge:" << endl;
    JohnsonAlgorithm j1(4);
    j1.addEdge(0, 1, 3);
    j1.addEdge(0, 2, 8);
    j1.addEdge(0, 3, -4);
    j1.addEdge(1, 2, 1);
    j1.addEdge(1, 3, 7);
    j1.addEdge(2, 3, 2);
    
    j1.displayGraph();
    
    auto dist1 = j1.johnson();
    j1.displayDistanceMatrix(dist1);
    j1.displayPaths(dist1);
    
    cout << "\nShortest path 0 → 2: " << j1.shortestPath(0, 2) << endl;
    
    // Example 2: Graph with only positive edges
    cout << "\n2. Graph with Positive Edges Only:" << endl;
    JohnsonAlgorithm j2(5);
    j2.addEdge(0, 1, 2);
    j2.addEdge(0, 2, 4);
    j2.addEdge(1, 2, 1);
    j2.addEdge(1, 3, 7);
    j2.addEdge(2, 3, 3);
    j2.addEdge(3, 4, 1);
    j2.addEdge(2, 4, 5);
    
    j2.displayGraph();
    
    auto dist2 = j2.johnson();
    j2.displayDistanceMatrix(dist2);
    
    // Example 3: Sparse graph
    cout << "\n3. Sparse Graph (Better for Johnson's):" << endl;
    JohnsonAlgorithm j3(6);
    j3.addEdge(0, 1, 5);
    j3.addEdge(0, 2, 3);
    j3.addEdge(1, 3, 2);
    j3.addEdge(2, 3, 4);
    j3.addEdge(3, 4, 1);
    j3.addEdge(3, 5, 6);
    j3.addEdge(4, 5, 2);
    
    j3.displayGraph();
    
    auto dist3 = j3.johnson();
    j3.displayDistanceMatrix(dist3);
    
    // Example 4: Graph with negative cycle (should detect)
    cout << "\n4. Graph with Negative Cycle (Detection):" << endl;
    JohnsonAlgorithm j4(3);
    j4.addEdge(0, 1, 1);
    j4.addEdge(1, 2, -2);
    j4.addEdge(2, 0, -1);  // Creates negative cycle
    
    j4.displayGraph();
    
    auto dist4 = j4.johnson();
    if (dist4.empty()) {
        cout << "Negative cycle detected! Cannot compute shortest paths." << endl;
    }
    
    // Example 5: Disconnected graph
    cout << "\n5. Disconnected Graph:" << endl;
    JohnsonAlgorithm j5(5);
    j5.addEdge(0, 1, 2);
    j5.addEdge(1, 2, 3);
    // No edges between 3 and 4
    j5.addEdge(3, 4, 1);
    
    j5.displayGraph();
    
    auto dist5 = j5.johnson();
    j5.displayDistanceMatrix(dist5);
    
    // Example 6: Performance comparison with Floyd-Warshall
    cout << "\n6. Performance Comparison:" << endl;
    const int V = 100;
    
    // Create a sparse graph (each vertex connected to next 5)
    JohnsonAlgorithm j6(V);
    for (int i = 0; i < V; i++) {
        for (int j = 1; j <= 5 && i + j < V; j++) {
            j6.addEdge(i, i + j, rand() % 20 + 1);
        }
    }
    
    auto start = chrono::high_resolution_clock::now();
    auto dist6 = j6.johnson();
    auto end = chrono::high_resolution_clock::now();
    auto johnsonTime = chrono::duration_cast<chrono::milliseconds>(end - start).count();
    
    cout << "Graph size: " << V << " vertices, ~" << (V * 5) << " edges" << endl;
    cout << "Johnson's Algorithm time: " << johnsonTime << " ms" << endl;
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Johnson's Algorithm** | O(V² log V + V × E) | O(V²) |
| **Floyd-Warshall** | O(V³) | O(V²) |
| **Dijkstra (repeated)** | O(V × (V+E) log V) | O(V²) |

---

## 🎯 Applications

| Application | Description |
|-------------|-------------|
| **Network Routing** | All-pairs shortest paths in sparse networks |
| **Transportation** | Shortest routes between all cities |
| **Social Networks** | Distance between all users |
| **Game Development** | Pathfinding between all points |
| **Data Analysis** | Similarity measurement |

---

## ✅ Key Takeaways

1. **Johnson's algorithm** works with negative weights (no negative cycles)
2. **Reweighting** eliminates negative edges
3. **Bellman-Ford** computes potential function
4. **Dijkstra** runs on reweighted graph
5. **Best for sparse graphs** (E << V²)
6. **Detects negative cycles**

---