# Graph Algorithm - Maximum Flow (Ford-Fulkerson & Edmonds-Karp)

## 📖 Overview

Maximum Flow algorithms find the maximum amount of flow that can be sent from a source vertex to a sink vertex in a flow network. The Ford-Fulkerson method uses augmenting paths, while Edmonds-Karp uses BFS to find the shortest augmenting path, guaranteeing polynomial time complexity.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Flow Network** | Directed graph with source, sink, and edge capacities |
| **Max Flow** | Maximum amount flow from source to sink |
| **Augmenting Path** | Path from source to sink with available capacity |
| **Residual Graph** | Graph showing remaining capacity |
| **Min Cut** | Minimum capacity cut separating source from sink |
| **Max Flow Min Cut Theorem** | Max flow = Min cut capacity |

---

## 📝 Complete Implementation

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <algorithm>
#include <cstring>
#include <iomanip>
using namespace std;

class FlowNetwork {
private:
    int vertices;
    vector<vector<int>> capacity;
    vector<vector<int>> adj;
    
public:
    FlowNetwork(int v) : vertices(v) {
        capacity.resize(v, vector<int>(v, 0));
        adj.resize(v);
    }
    
    void addEdge(int u, int v, int cap) {
        capacity[u][v] += cap;  // Add forward edge
        adj[u].push_back(v);
        adj[v].push_back(u);    // Add reverse edge for residual graph
    }
    
    // ============ FORD-FULKERSON (DFS based) ============
    int fordFulkerson(int source, int sink) {
        // Create residual graph
        vector<vector<int>> residual = capacity;
        vector<int> parent(vertices);
        int maxFlow = 0;
        
        // Augment flow while there's a path from source to sink
        while (dfsAugment(source, sink, residual, parent)) {
            // Find bottleneck capacity
            int pathFlow = INT_MAX;
            for (int v = sink; v != source; v = parent[v]) {
                int u = parent[v];
                pathFlow = min(pathFlow, residual[u][v]);
            }
            
            // Update residual graph
            for (int v = sink; v != source; v = parent[v]) {
                int u = parent[v];
                residual[u][v] -= pathFlow;
                residual[v][u] += pathFlow;
            }
            
            maxFlow += pathFlow;
        }
        
        return maxFlow;
    }
    
private:
    bool dfsAugment(int source, int sink, vector<vector<int>>& residual, 
                    vector<int>& parent) {
        vector<bool> visited(vertices, false);
        return dfs(source, sink, residual, visited, parent);
    }
    
    bool dfs(int u, int sink, vector<vector<int>>& residual, 
             vector<bool>& visited, vector<int>& parent) {
        if (u == sink) return true;
        
        visited[u] = true;
        
        for (int v : adj[u]) {
            if (!visited[v] && residual[u][v] > 0) {
                parent[v] = u;
                if (dfs(v, sink, residual, visited, parent)) {
                    return true;
                }
            }
        }
        return false;
    }
    
public:
    // ============ EDMONDS-KARP (BFS based) ============
    int edmondsKarp(int source, int sink) {
        vector<vector<int>> residual = capacity;
        vector<int> parent(vertices);
        int maxFlow = 0;
        
        while (bfsAugment(source, sink, residual, parent)) {
            // Find bottleneck capacity
            int pathFlow = INT_MAX;
            for (int v = sink; v != source; v = parent[v]) {
                int u = parent[v];
                pathFlow = min(pathFlow, residual[u][v]);
            }
            
            // Update residual graph
            for (int v = sink; v != source; v = parent[v]) {
                int u = parent[v];
                residual[u][v] -= pathFlow;
                residual[v][u] += pathFlow;
            }
            
            maxFlow += pathFlow;
        }
        
        return maxFlow;
    }
    
private:
    bool bfsAugment(int source, int sink, vector<vector<int>>& residual,
                    vector<int>& parent) {
        vector<bool> visited(vertices, false);
        queue<int> q;
        
        q.push(source);
        visited[source] = true;
        parent[source] = -1;
        
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            
            for (int v : adj[u]) {
                if (!visited[v] && residual[u][v] > 0) {
                    visited[v] = true;
                    parent[v] = u;
                    q.push(v);
                    
                    if (v == sink) return true;
                }
            }
        }
        
        return false;
    }
    
public:
    // ============ FIND MIN CUT ============
    vector<pair<int, int>> findMinCut(int source, int sink) {
        // First compute max flow
        edmondsKarp(source, sink);
        
        // Find reachable vertices from source in residual graph
        vector<bool> reachable = getReachableVertices(source);
        
        // Min cut edges are those from reachable to unreachable
        vector<pair<int, int>> minCut;
        for (int u = 0; u < vertices; u++) {
            if (reachable[u]) {
                for (int v : adj[u]) {
                    if (!reachable[v] && capacity[u][v] > 0) {
                        minCut.push_back({u, v});
                    }
                }
            }
        }
        
        return minCut;
    }
    
    vector<bool> getReachableVertices(int source) {
        vector<bool> visited(vertices, false);
        queue<int> q;
        
        q.push(source);
        visited[source] = true;
        
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            
            for (int v : adj[u]) {
                if (!visited[v] && capacity[u][v] > 0) {
                    visited[v] = true;
                    q.push(v);
                }
            }
        }
        
        return visited;
    }
    
    // ============ PRINT FLOW NETWORK ============
    void display() {
        cout << "\nFlow Network:\n";
        cout << "Edge\t\tCapacity\n";
        cout << "-------------------\n";
        for (int u = 0; u < vertices; u++) {
            for (int v : adj[u]) {
                if (capacity[u][v] > 0 && u < v) {  // Print each edge once
                    cout << u << " -> " << v << "\t\t" << capacity[u][v] << endl;
                }
            }
        }
    }
    
    void displayMinCut(const vector<pair<int, int>>& minCut) {
        cout << "\nMinimum Cut Edges:\n";
        int cutCapacity = 0;
        for (auto& edge : minCut) {
            cout << edge.first << " -> " << edge.second << endl;
            cutCapacity += capacity[edge.first][edge.second];
        }
        cout << "Cut Capacity: " << cutCapacity << endl;
    }
};

int main() {
    cout << "=== Maximum Flow Demo ===" << endl;
    
    // Example 1: Standard flow network
    cout << "\n1. Standard Flow Network:" << endl;
    FlowNetwork fn1(6);
    fn1.addEdge(0, 1, 16);
    fn1.addEdge(0, 2, 13);
    fn1.addEdge(1, 2, 10);
    fn1.addEdge(1, 3, 12);
    fn1.addEdge(2, 1, 4);
    fn1.addEdge(2, 4, 14);
    fn1.addEdge(3, 2, 9);
    fn1.addEdge(3, 5, 20);
    fn1.addEdge(4, 3, 7);
    fn1.addEdge(4, 5, 4);
    
    fn1.display();
    
    cout << "\nFord-Fulkerson (DFS): " << fn1.fordFulkerson(0, 5) << endl;
    cout << "Edmonds-Karp (BFS): " << fn1.edmondsKarp(0, 5) << endl;
    
    auto minCut1 = fn1.findMinCut(0, 5);
    fn1.displayMinCut(minCut1);
    
    // Example 2: Simple network
    cout << "\n2. Simple Network:" << endl;
    FlowNetwork fn2(4);
    fn2.addEdge(0, 1, 3);
    fn2.addEdge(0, 2, 2);
    fn2.addEdge(1, 2, 1);
    fn2.addEdge(1, 3, 2);
    fn2.addEdge(2, 3, 2);
    
    fn2.display();
    
    cout << "\nMax Flow (0 -> 3): " << fn2.edmondsKarp(0, 3) << endl;
    
    // Example 3: Multiple paths
    cout << "\n3. Multiple Paths Network:" << endl;
    FlowNetwork fn3(5);
    fn3.addEdge(0, 1, 10);
    fn3.addEdge(0, 2, 5);
    fn3.addEdge(1, 2, 5);
    fn3.addEdge(1, 3, 15);
    fn3.addEdge(2, 3, 10);
    fn3.addEdge(3, 4, 20);
    
    fn3.display();
    
    cout << "\nMax Flow (0 -> 4): " << fn3.edmondsKarp(0, 4) << endl;
    
    // Example 4: Bottleneck network
    cout << "\n4. Bottleneck Network:" << endl;
    FlowNetwork fn4(4);
    fn4.addEdge(0, 1, 5);
    fn4.addEdge(0, 2, 3);
    fn4.addEdge(1, 3, 4);
    fn4.addEdge(2, 3, 6);
    
    fn4.display();
    
    cout << "\nMax Flow (0 -> 3): " << fn4.edmondsKarp(0, 3) << endl;
    
    // Example 5: Large network
    cout << "\n5. Large Network (8 vertices):" << endl;
    FlowNetwork fn5(8);
    fn5.addEdge(0, 1, 20);
    fn5.addEdge(0, 2, 15);
    fn5.addEdge(1, 2, 5);
    fn5.addEdge(1, 3, 10);
    fn5.addEdge(1, 4, 15);
    fn5.addEdge(2, 4, 10);
    fn5.addEdge(2, 5, 20);
    fn5.addEdge(3, 6, 10);
    fn5.addEdge(4, 6, 15);
    fn5.addEdge(4, 7, 10);
    fn5.addEdge(5, 7, 15);
    fn5.addEdge(6, 7, 10);
    
    fn5.display();
    
    cout << "\nMax Flow (0 -> 7): " << fn5.edmondsKarp(0, 7) << endl;
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Ford-Fulkerson** | O(E × max_flow) | O(V²) |
| **Edmonds-Karp** | O(V × E²) | O(V²) |

---

## 🎯 Applications

| Application | Description |
|-------------|-------------|
| **Network Routing** | Maximizing data throughput |
| **Bipartite Matching** | Job assignment, marriage problem |
| **Image Segmentation** | Foreground/background separation |
| **Project Selection** | Maximizing profit from projects |
| **Circulation Problems** | Flow with demands |
| **Transportation** | Maximum goods delivery |

---

## ✅ Key Takeaways

1. **Max Flow** = maximum amount from source to sink
2. **Ford-Fulkerson** uses DFS (may be exponential)
3. **Edmonds-Karp** uses BFS (polynomial time)
4. **Residual graph** tracks remaining capacity
5. **Augmenting path** increases flow
6. **Max Flow = Min Cut** (important theorem)

---
---

## Next Step

- Go to [09_Minimum_Cut.md](09_Minimum_Cut.md) to continue with Minimum Cut.
