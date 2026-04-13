# Graph Algorithm - Prim's Algorithm (Minimum Spanning Tree)

## 📖 Overview

Prim's algorithm finds the Minimum Spanning Tree (MST) of a connected, weighted, undirected graph. Unlike Kruskal's algorithm which builds the MST by adding edges, Prim's algorithm grows the MST from a starting vertex, adding the cheapest edge that connects a vertex in the tree to a vertex outside the tree.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Minimum Spanning Tree (MST)** | Connects all vertices with minimum total weight |
| **Greedy Approach** | Always picks the cheapest edge connecting tree to outside |
| **Priority Queue** | Efficiently selects minimum weight edge |
| **Vertex-based** | Grows the tree one vertex at a time |
| **Works on connected graphs** | Graph must be connected |

---

## 📊 How Prim's Algorithm Works

### Step-by-step Visualization

```
Graph with 5 vertices:

    0 ---2--- 1
    |         |
    4         3
    |         |
    2 ---1--- 3

Start from vertex 0:

Step 1: Tree = {0}
  Edges from tree: (0,1)=2, (0,2)=4
  Pick smallest: (0,1)=2 → Add vertex 1

Step 2: Tree = {0,1}
  Edges from tree: (0,2)=4, (1,2)=5, (1,3)=3
  Pick smallest: (1,3)=3 → Add vertex 3

Step 3: Tree = {0,1,3}
  Edges from tree: (0,2)=4, (1,2)=5, (3,2)=1
  Pick smallest: (3,2)=1 → Add vertex 2

Step 4: Tree = {0,1,2,3}
  All vertices added → MST complete

MST edges: (0,1)=2, (1,3)=3, (3,2)=1
Total weight: 6
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
using namespace std;

class Graph {
private:
    int vertices;
    vector<vector<pair<int, int>>> adj;  // {neighbor, weight}
    bool isDirected;
    
public:
    Graph(int v, bool directed = false) : vertices(v), isDirected(directed) {
        adj.resize(v);
    }
    
    void addEdge(int u, int v, int weight) {
        adj[u].push_back({v, weight});
        if (!isDirected) {
            adj[v].push_back({u, weight});
        }
    }
    
    // ============ PRIM'S ALGORITHM (NAIVE - O(V²)) ============
    vector<pair<int, int>> primMSTNaive(int start = 0) {
        if (isDirected) {
            cout << "Prim's algorithm works only on undirected graphs!" << endl;
            return {};
        }
        
        vector<int> key(vertices, INT_MAX);
        vector<bool> inMST(vertices, false);
        vector<int> parent(vertices, -1);
        
        key[start] = 0;
        
        for (int count = 0; count < vertices - 1; count++) {
            // Find vertex with minimum key value not yet in MST
            int u = -1;
            int minKey = INT_MAX;
            for (int i = 0; i < vertices; i++) {
                if (!inMST[i] && key[i] < minKey) {
                    minKey = key[i];
                    u = i;
                }
            }
            
            if (u == -1) break;  // Graph disconnected
            
            inMST[u] = true;
            
            // Update key values of adjacent vertices
            for (auto& [v, weight] : adj[u]) {
                if (!inMST[v] && weight < key[v]) {
                    key[v] = weight;
                    parent[v] = u;
                }
            }
        }
        
        // Build MST edges
        vector<pair<int, int>> mst;
        int totalWeight = 0;
        for (int i = 0; i < vertices; i++) {
            if (parent[i] != -1) {
                mst.push_back({parent[i], i});
                totalWeight += key[i];
            }
        }
        
        cout << "Total MST Weight (Naive): " << totalWeight << endl;
        return mst;
    }
    
    // ============ PRIM'S ALGORITHM (PRIORITY QUEUE - O((V+E) log V)) ============
    vector<pair<int, int>> primMSTPQ(int start = 0) {
        if (isDirected) {
            cout << "Prim's algorithm works only on undirected graphs!" << endl;
            return {};
        }
        
        vector<int> key(vertices, INT_MAX);
        vector<bool> inMST(vertices, false);
        vector<int> parent(vertices, -1);
        
        // Min-heap: {key, vertex}
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        
        key[start] = 0;
        pq.push({0, start});
        
        while (!pq.empty()) {
            int u = pq.top().second;
            pq.pop();
            
            if (inMST[u]) continue;
            inMST[u] = true;
            
            for (auto& [v, weight] : adj[u]) {
                if (!inMST[v] && weight < key[v]) {
                    key[v] = weight;
                    parent[v] = u;
                    pq.push({key[v], v});
                }
            }
        }
        
        // Build MST edges
        vector<pair<int, int>> mst;
        int totalWeight = 0;
        for (int i = 0; i < vertices; i++) {
            if (parent[i] != -1) {
                mst.push_back({parent[i], i});
                totalWeight += key[i];
            }
        }
        
        cout << "Total MST Weight (PQ): " << totalWeight << endl;
        return mst;
    }
    
    // ============ PRIM'S WITH PATH PRINTING ============
    void printMST(int start = 0) {
        vector<pair<int, int>> mst = primMSTPQ(start);
        if (mst.empty()) return;
        
        cout << "\nMinimum Spanning Tree Edges:\n";
        cout << "Edge\t\tWeight\n";
        cout << "-------------------\n";
        
        int totalWeight = 0;
        for (auto& [u, v] : mst) {
            // Find weight of edge (u, v)
            int weight = 0;
            for (auto& [neighbor, w] : adj[u]) {
                if (neighbor == v) {
                    weight = w;
                    break;
                }
            }
            cout << u << " -- " << v << "\t\t" << weight << endl;
            totalWeight += weight;
        }
        cout << "Total Weight: " << totalWeight << endl;
    }
    
    // ============ PRIM'S FOR SPECIFIC START VERTEX ============
    vector<int> primMSTEdges(int start = 0) {
        vector<int> parent(vertices, -1);
        vector<int> key(vertices, INT_MAX);
        vector<bool> inMST(vertices, false);
        
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        
        key[start] = 0;
        pq.push({0, start});
        
        while (!pq.empty()) {
            int u = pq.top().second;
            pq.pop();
            
            if (inMST[u]) continue;
            inMST[u] = true;
            
            for (auto& [v, weight] : adj[u]) {
                if (!inMST[v] && weight < key[v]) {
                    key[v] = weight;
                    parent[v] = u;
                    pq.push({key[v], v});
                }
            }
        }
        
        return parent;
    }
    
    // ============ CHECK IF GRAPH IS CONNECTED ============
    bool isConnected() {
        vector<bool> visited(vertices, false);
        queue<int> q;
        q.push(0);
        visited[0] = true;
        
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            
            for (auto& [v, weight] : adj[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    q.push(v);
                }
            }
        }
        
        for (int i = 0; i < vertices; i++) {
            if (!visited[i]) return false;
        }
        return true;
    }
    
    // ============ FIND MST WEIGHT ONLY ============
    int mstWeight() {
        vector<pair<int, int>> mst = primMSTPQ();
        if (mst.empty()) return -1;
        
        int total = 0;
        for (auto& [u, v] : mst) {
            for (auto& [neighbor, w] : adj[u]) {
                if (neighbor == v) {
                    total += w;
                    break;
                }
            }
        }
        return total;
    }
    
    // ============ PRIM'S WITH COST TRACKING ============
    pair<vector<pair<int, int>>, int> primMSTWithCost(int start = 0) {
        vector<pair<int, int>> mst = primMSTPQ(start);
        int totalCost = 0;
        
        for (auto& [u, v] : mst) {
            for (auto& [neighbor, w] : adj[u]) {
                if (neighbor == v) {
                    totalCost += w;
                    break;
                }
            }
        }
        
        return {mst, totalCost};
    }
    
    // ============ DISPLAY GRAPH ============
    void display() {
        cout << "\nGraph Adjacency List:\n";
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
    cout << "=== Prim's Algorithm Demo ===" << endl;
    
    // Example 1: Standard graph
    cout << "\n1. Standard Graph:" << endl;
    Graph g1(5, false);
    g1.addEdge(0, 1, 2);
    g1.addEdge(0, 3, 6);
    g1.addEdge(1, 2, 3);
    g1.addEdge(1, 3, 8);
    g1.addEdge(1, 4, 5);
    g1.addEdge(2, 4, 7);
    g1.addEdge(3, 4, 9);
    
    g1.display();
    g1.printMST(0);
    
    // Example 2: Graph from visualization
    cout << "\n2. Graph from Visualization:" << endl;
    Graph g2(4, false);
    g2.addEdge(0, 1, 2);
    g2.addEdge(0, 2, 4);
    g2.addEdge(1, 2, 5);
    g2.addEdge(1, 3, 3);
    g2.addEdge(2, 3, 1);
    
    g2.display();
    g2.printMST(0);
    
    // Example 3: Different start vertex
    cout << "\n3. MST Starting from Different Vertex (start=2):" << endl;
    Graph g3(4, false);
    g3.addEdge(0, 1, 2);
    g3.addEdge(0, 2, 4);
    g3.addEdge(1, 2, 5);
    g3.addEdge(1, 3, 3);
    g3.addEdge(2, 3, 1);
    
    g3.display();
    cout << "\nMST from vertex 2:" << endl;
    g3.printMST(2);
    
    // Example 4: Dense graph
    cout << "\n4. Dense Graph (Complete Graph K4):" << endl;
    Graph g4(4, false);
    g4.addEdge(0, 1, 10);
    g4.addEdge(0, 2, 6);
    g4.addEdge(0, 3, 5);
    g4.addEdge(1, 2, 8);
    g4.addEdge(1, 3, 15);
    g4.addEdge(2, 3, 4);
    
    g4.display();
    g4.printMST(0);
    
    // Example 5: Disconnected graph
    cout << "\n5. Disconnected Graph:" << endl;
    Graph g5(5, false);
    g5.addEdge(0, 1, 2);
    g5.addEdge(0, 2, 3);
    g5.addEdge(3, 4, 4);
    // No edge connecting {0,1,2} to {3,4}
    
    g5.display();
    cout << "Is connected? " << (g5.isConnected() ? "Yes" : "No") << endl;
    g5.printMST(0);  // Will show error
    
    // Example 6: Large graph
    cout << "\n6. Large Graph (6 vertices):" << endl;
    Graph g6(6, false);
    g6.addEdge(0, 1, 4);
    g6.addEdge(0, 2, 3);
    g6.addEdge(1, 2, 1);
    g6.addEdge(1, 3, 2);
    g6.addEdge(2, 3, 4);
    g6.addEdge(3, 4, 2);
    g6.addEdge(3, 5, 6);
    g6.addEdge(4, 5, 3);
    
    g6.display();
    g6.printMST(0);
    
    // Compare Naive vs PQ implementation
    cout << "\n7. Performance Comparison (Naive vs PQ):" << endl;
    Graph g7(6, false);
    g7.addEdge(0, 1, 4);
    g7.addEdge(0, 2, 3);
    g7.addEdge(1, 2, 1);
    g7.addEdge(1, 3, 2);
    g7.addEdge(2, 3, 4);
    g7.addEdge(3, 4, 2);
    g7.addEdge(3, 5, 6);
    g7.addEdge(4, 5, 3);
    
    cout << "\nNaive Implementation:" << endl;
    auto mst1 = g7.primMSTNaive(0);
    
    cout << "\nPriority Queue Implementation:" << endl;
    auto mst2 = g7.primMSTPQ(0);
    
    // Get MST with cost
    cout << "\n8. MST with Cost Tracking:" << endl;
    auto [mst, cost] = g7.primMSTWithCost(0);
    cout << "MST edges count: " << mst.size() << endl;
    cout << "MST total cost: " << cost << endl;
    
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

## 🎯 Applications of Prim's Algorithm

| Application | Description |
|-------------|-------------|
| **Network Design** | Minimum cost to connect all nodes |
| **Telecommunications** | Laying fiber optic cables |
| **Electrical Grids** | Power distribution networks |
| **Road Networks** | Connecting cities with minimum road length |
| **Clustering** | Single-linkage clustering |
| **Image Segmentation** | Graph-based segmentation |
| **Approximation Algorithms** | TSP and Steiner tree problems |

---

## 📊 Kruskal vs Prim Comparison

| Feature | Kruskal | Prim |
|---------|---------|------|
| **Approach** | Edge-based | Vertex-based |
| **Data Structure** | Union-Find | Priority Queue |
| **Time Complexity** | O(E log E) | O((V+E) log V) |
| **Best for** | Sparse graphs | Dense graphs |
| **Implementation** | Slightly simpler | Slightly more complex |
| **Start vertex** | Not required | Required |

---

## ✅ Key Takeaways

1. **Prim's algorithm** grows MST from a starting vertex
2. **Priority queue** selects the cheapest edge to add
3. **Vertex-based** approach differs from Kruskal's edge-based
4. **Better for dense graphs** than Kruskal
5. **Requires connected graph** to form MST
6. **Greedy choice property** ensures optimal solution
7. **Can start from any vertex** (result same weight, different edges)

---
---

## Next Step

- Go to [06_A_Star_Algorithm.md](06_A_Star_Algorithm.md) to continue with A Star Algorithm.
