# Graph Algorithm - Minimum Cut

## 📖 Overview

The Minimum Cut problem finds the smallest capacity cut that separates a source vertex from a sink vertex in a flow network. The Max-Flow Min-Cut Theorem states that the maximum flow value equals the minimum cut capacity. This has applications in network reliability, image segmentation, and graph partitioning.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Cut** | Partition of vertices into two sets (S containing source, T containing sink) |
| **Cut Capacity** | Sum of capacities of edges from S to T |
| **Minimum Cut** | Cut with smallest capacity |
| **Max-Flow Min-Cut Theorem** | Max flow = Min cut capacity |
| **Global Min Cut** | Minimum cut separating any two vertices |

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
#include <random>
using namespace std;

class Graph {
private:
    int vertices;
    vector<vector<int>> capacity;
    vector<vector<int>> adj;
    
public:
    Graph(int v) : vertices(v) {
        capacity.resize(v, vector<int>(v, 0));
        adj.resize(v);
    }
    
    void addEdge(int u, int v, int cap) {
        capacity[u][v] += cap;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    
    // ============ STOER-WAGNER ALGORITHM (Global Min Cut) ============
    int stoerWagner() {
        vector<int> vertices(::vertices);
        for (int i = 0; i < ::vertices; i++) {
            vertices[i] = i;
        }
        
        int minCut = INT_MAX;
        
        while (vertices.size() > 1) {
            // Phase 1: Find min cut phase
            vector<int> weights(::vertices, 0);
            vector<bool> added(::vertices, false);
            vector<int> order;
            
            for (int i = 0; i < vertices.size(); i++) {
                // Select most tightly connected vertex
                int next = -1;
                for (int v : vertices) {
                    if (!added[v] && (next == -1 || weights[v] > weights[next])) {
                        next = v;
                    }
                }
                
                added[next] = true;
                order.push_back(next);
                
                // Update weights
                for (int v : vertices) {
                    if (!added[v]) {
                        weights[v] += capacity[next][v];
                    }
                }
            }
            
            // Phase 2: Update min cut
            int last = order.back();
            int secondLast = order[order.size() - 2];
            minCut = min(minCut, weights[last]);
            
            // Merge last two vertices
            for (int v : vertices) {
                if (v != last) {
                    capacity[secondLast][v] += capacity[last][v];
                    capacity[v][secondLast] += capacity[v][last];
                }
            }
            
            // Remove last vertex
            vertices.erase(remove(vertices.begin(), vertices.end(), last), vertices.end());
        }
        
        return minCut;
    }
    
    // ============ MIN CUT FROM MAX FLOW (s-t cut) ============
    pair<int, vector<pair<int, int>>> minCut(int source, int sink) {
        // First compute max flow using Edmonds-Karp
        vector<vector<int>> residual = capacity;
        vector<int> parent(vertices);
        
        // Edmonds-Karp
        while (bfs(source, sink, residual, parent)) {
            int pathFlow = INT_MAX;
            for (int v = sink; v != source; v = parent[v]) {
                int u = parent[v];
                pathFlow = min(pathFlow, residual[u][v]);
            }
            
            for (int v = sink; v != source; v = parent[v]) {
                int u = parent[v];
                residual[u][v] -= pathFlow;
                residual[v][u] += pathFlow;
            }
        }
        
        // Find reachable vertices from source in residual graph
        vector<bool> reachable = getReachable(source, residual);
        
        // Find min cut edges
        vector<pair<int, int>> minCutEdges;
        int cutCapacity = 0;
        
        for (int u = 0; u < vertices; u++) {
            if (reachable[u]) {
                for (int v : adj[u]) {
                    if (!reachable[v] && capacity[u][v] > 0) {
                        minCutEdges.push_back({u, v});
                        cutCapacity += capacity[u][v];
                    }
                }
            }
        }
        
        return {cutCapacity, minCutEdges};
    }
    
private:
    bool bfs(int source, int sink, vector<vector<int>>& residual, vector<int>& parent) {
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
    
    vector<bool> getReachable(int source, vector<vector<int>>& residual) {
        vector<bool> visited(vertices, false);
        queue<int> q;
        
        q.push(source);
        visited[source] = true;
        
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            
            for (int v : adj[u]) {
                if (!visited[v] && residual[u][v] > 0) {
                    visited[v] = true;
                    q.push(v);
                }
            }
        }
        
        return visited;
    }
    
public:
    // ============ KARGER'S ALGORITHM (Randomized) ============
    int kargerMinCut() {
        // Make a copy of edges
        vector<pair<int, int>> edges;
        for (int u = 0; u < vertices; u++) {
            for (int v : adj[u]) {
                if (u < v && capacity[u][v] > 0) {
                    edges.push_back({u, v});
                }
            }
        }
        
        vector<int> parent(vertices);
        vector<int> rank(vertices);
        
        // Run multiple trials for better probability
        int minCut = INT_MAX;
        
        for (int trial = 0; trial < vertices * vertices; trial++) {
            // Initialize Union-Find
            for (int i = 0; i < vertices; i++) {
                parent[i] = i;
                rank[i] = 0;
            }
            
            int remaining = vertices;
            
            // Randomly contract edges
            while (remaining > 2) {
                // Pick random edge
                random_device rd;
                mt19937 gen(rd());
                uniform_int_distribution<> dis(0, edges.size() - 1);
                int idx = dis(gen);
                int u = edges[idx].first;
                int v = edges[idx].second;
                
                int ru = find(parent, u);
                int rv = find(parent, v);
                
                if (ru != rv) {
                    unite(parent, rank, ru, rv);
                    remaining--;
                }
            }
            
            // Count edges between the two remaining components
            int cutSize = 0;
            for (const auto& edge : edges) {
                int ru = find(parent, edge.first);
                int rv = find(parent, edge.second);
                if (ru != rv) {
                    cutSize++;
                }
            }
            
            minCut = min(minCut, cutSize);
        }
        
        return minCut;
    }
    
private:
    int find(vector<int>& parent, int x) {
        if (parent[x] != x) {
            parent[x] = find(parent, parent[x]);
        }
        return parent[x];
    }
    
    void unite(vector<int>& parent, vector<int>& rank, int x, int y) {
        if (rank[x] < rank[y]) {
            parent[x] = y;
        } else if (rank[x] > rank[y]) {
            parent[y] = x;
        } else {
            parent[y] = x;
            rank[x]++;
        }
    }
    
public:
    // ============ FIND VERTEX COVER FROM MIN CUT ============
    vector<int> vertexCoverFromMinCut(int source, int sink) {
        auto [cutCapacity, minCutEdges] = minCut(source, sink);
        
        // Find vertices on source side
        vector<vector<int>> residual = capacity;
        vector<int> parent(vertices);
        bfs(source, sink, residual, parent);
        
        vector<bool> reachable = getReachable(source, residual);
        
        // Vertex cover = vertices on source side that have edges to sink side
        vector<int> vertexCover;
        for (int u = 0; u < vertices; u++) {
            if (reachable[u]) {
                for (int v : adj[u]) {
                    if (!reachable[v] && capacity[u][v] > 0) {
                        vertexCover.push_back(u);
                        break;
                    }
                }
            }
        }
        
        return vertexCover;
    }
    
    // ============ DISPLAY ============
    void display() {
        cout << "\nGraph:\n";
        cout << "Edge\t\tCapacity\n";
        cout << "-------------------\n";
        for (int u = 0; u < vertices; u++) {
            for (int v : adj[u]) {
                if (capacity[u][v] > 0 && u < v) {
                    cout << u << " -> " << v << "\t\t" << capacity[u][v] << endl;
                }
            }
        }
    }
    
    void displayMinCut(int source, int sink) {
        auto [cutCapacity, minCutEdges] = minCut(source, sink);
        
        cout << "\nMinimum s-t Cut (" << source << " -> " << sink << "):\n";
        cout << "Cut Edges:\n";
        for (auto& edge : minCutEdges) {
            cout << "  " << edge.first << " -> " << edge.second << endl;
        }
        cout << "Cut Capacity: " << cutCapacity << endl;
    }
};

int main() {
    cout << "=== Minimum Cut Demo ===" << endl;
    
    // Example 1: Standard network
    cout << "\n1. Standard Network (s-t cut):" << endl;
    Graph g1(6);
    g1.addEdge(0, 1, 16);
    g1.addEdge(0, 2, 13);
    g1.addEdge(1, 2, 10);
    g1.addEdge(1, 3, 12);
    g1.addEdge(2, 1, 4);
    g1.addEdge(2, 4, 14);
    g1.addEdge(3, 2, 9);
    g1.addEdge(3, 5, 20);
    g1.addEdge(4, 3, 7);
    g1.addEdge(4, 5, 4);
    
    g1.display();
    g1.displayMinCut(0, 5);
    
    // Example 2: Simple network
    cout << "\n2. Simple Network:" << endl;
    Graph g2(4);
    g2.addEdge(0, 1, 3);
    g2.addEdge(0, 2, 2);
    g2.addEdge(1, 2, 1);
    g2.addEdge(1, 3, 2);
    g2.addEdge(2, 3, 2);
    
    g2.display();
    g2.displayMinCut(0, 3);
    
    // Example 3: Global Min Cut (Stoer-Wagner)
    cout << "\n3. Global Min Cut (Stoer-Wagner):" << endl;
    Graph g3(5);
    g3.addEdge(0, 1, 2);
    g3.addEdge(0, 2, 3);
    g3.addEdge(1, 2, 4);
    g3.addEdge(1, 3, 5);
    g3.addEdge(2, 3, 1);
    g3.addEdge(2, 4, 2);
    g3.addEdge(3, 4, 3);
    
    g3.display();
    cout << "\nGlobal Min Cut: " << g3.stoerWagner() << endl;
    
    // Example 4: Karger's Algorithm (Randomized)
    cout << "\n4. Karger's Algorithm (Randomized):" << endl;
    Graph g4(4);
    g4.addEdge(0, 1, 1);
    g4.addEdge(0, 2, 1);
    g4.addEdge(0, 3, 1);
    g4.addEdge(1, 2, 1);
    g4.addEdge(1, 3, 1);
    g4.addEdge(2, 3, 1);
    
    g4.display();
    cout << "\nKarger's Min Cut (approx): " << g4.kargerMinCut() << endl;
    
    // Example 5: Bipartite graph
    cout << "\n5. Bipartite Graph:" << endl;
    Graph g5(6);
    g5.addEdge(0, 3, 1);
    g5.addEdge(0, 4, 1);
    g5.addEdge(1, 3, 1);
    g5.addEdge(1, 5, 1);
    g5.addEdge(2, 4, 1);
    g5.addEdge(2, 5, 1);
    
    g5.display();
    g5.displayMinCut(0, 5);
    
    // Example 6: Vertex cover from min cut
    cout << "\n6. Vertex Cover from Min Cut:" << endl;
    Graph g6(6);
    g6.addEdge(0, 1, 1);
    g6.addEdge(0, 2, 1);
    g6.addEdge(1, 3, 1);
    g6.addEdge(2, 3, 1);
    g6.addEdge(3, 4, 1);
    g6.addEdge(3, 5, 1);
    
    g6.display();
    auto vertexCover = g6.vertexCoverFromMinCut(0, 5);
    cout << "\nVertex Cover (source side vertices with edges to sink side): ";
    for (int v : vertexCover) cout << v << " ";
    cout << endl;
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **s-t Min Cut (via Max Flow)** | O(V × E²) | O(V²) |
| **Stoer-Wagner (Global)** | O(V³) | O(V²) |
| **Karger's (Randomized)** | O(V² × log V) | O(E) |

---

## 🎯 Applications

| Application | Description |
|-------------|-------------|
| **Network Reliability** | Finding weakest links |
| **Image Segmentation** | Separating foreground from background |
| **Cluster Analysis** | Partitioning data into clusters |
| **Circuit Design** | Minimizing interconnections |
| **Social Networks** | Finding communities |
| **Image Processing** | Object extraction |

---

## ✅ Key Takeaways

1. **s-t Min Cut** = minimum capacity cut separating source and sink
2. **Global Min Cut** = minimum cut separating any two vertices
3. **Max Flow = Min Cut** (fundamental theorem)
4. **Stoer-Wagner** finds global min cut in O(V³)
5. **Karger's algorithm** is randomized but efficient
6. **Cut edges** form the minimum capacity boundary

---
---

## Next Step

- Go to [10_Bipartite_Graph.md](10_Bipartite_Graph.md) to continue with Bipartite Graph.
