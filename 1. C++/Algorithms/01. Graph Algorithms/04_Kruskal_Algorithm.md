# Graph Algorithm - Kruskal's Algorithm (Minimum Spanning Tree)

## 📖 Overview

Kruskal's algorithm finds the Minimum Spanning Tree (MST) of a connected, weighted, undirected graph. An MST is a subset of edges that connects all vertices with the minimum total edge weight and no cycles. Kruskal's algorithm is greedy and uses the Union-Find data structure for cycle detection.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Minimum Spanning Tree (MST)** | Connects all vertices with minimum total weight |
| **Greedy Approach** | Always picks the smallest edge that doesn't create a cycle |
| **Union-Find** | Detects cycles efficiently |
| **Edge List** | Sorts edges by weight |
| **V-1 Edges** | MST has exactly V-1 edges for a connected graph |

---

## 📊 How Kruskal's Algorithm Works

### Step-by-step Visualization

```
Graph with 4 vertices and 5 edges:

    0 ---2--- 1
    |         |
    4         3
    |         |
    2 ---1--- 3

Edges sorted by weight:
1: (2,3) weight=1
2: (0,1) weight=2
3: (1,3) weight=3
4: (0,2) weight=4
5: (1,2) weight=5

Step 1: Pick (2,3) weight=1
  Sets: {0}, {1}, {2,3}

Step 2: Pick (0,1) weight=2
  Sets: {0,1}, {2,3}

Step 3: Pick (1,3) weight=3
  - 1 in {0,1}, 3 in {2,3} → different sets → pick it
  Sets: {0,1,2,3}

MST edges: (2,3), (0,1), (1,3)
Total weight: 1 + 2 + 3 = 6
```

---

## 📝 Complete Implementation

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>
#include <iomanip>
using namespace std;

class Edge {
public:
    int source, destination, weight;
    
    Edge(int u, int v, int w) : source(u), destination(v), weight(w) {}
    
    bool operator<(const Edge& other) const {
        return weight < other.weight;
    }
};

// Union-Find (Disjoint Set Union) data structure
class UnionFind {
private:
    vector<int> parent, rank;
    
public:
    UnionFind(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }
    
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);  // Path compression
        }
        return parent[x];
    }
    
    bool unite(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        
        if (rootX == rootY) return false;  // Already connected
        
        // Union by rank
        if (rank[rootX] < rank[rootY]) {
            parent[rootX] = rootY;
        } else if (rank[rootX] > rank[rootY]) {
            parent[rootY] = rootX;
        } else {
            parent[rootY] = rootX;
            rank[rootX]++;
        }
        return true;
    }
    
    bool connected(int x, int y) {
        return find(x) == find(y);
    }
};

class Graph {
private:
    int vertices;
    vector<Edge> edges;
    bool isDirected;
    
public:
    Graph(int v, bool directed = false) : vertices(v), isDirected(directed) {}
    
    void addEdge(int u, int v, int weight) {
        edges.push_back(Edge(u, v, weight));
        if (!isDirected) {
            // For undirected, we store each edge once
            // The algorithm will handle it
        }
    }
    
    // ============ KRUSKAL'S ALGORITHM ============
    vector<Edge> kruskalMST() {
        if (isDirected) {
            cout << "Kruskal's algorithm works only on undirected graphs!" << endl;
            return {};
        }
        
        // Sort edges by weight
        sort(edges.begin(), edges.end());
        
        UnionFind uf(vertices);
        vector<Edge> mst;
        int totalWeight = 0;
        
        for (const Edge& edge : edges) {
            if (uf.unite(edge.source, edge.destination)) {
                mst.push_back(edge);
                totalWeight += edge.weight;
                
                // Early termination if we have V-1 edges
                if (mst.size() == vertices - 1) break;
            }
        }
        
        // Check if graph is connected
        if (mst.size() != vertices - 1) {
            cout << "Graph is not connected! No spanning tree exists." << endl;
            return {};
        }
        
        cout << "Total MST Weight: " << totalWeight << endl;
        return mst;
    }
    
    // ============ FIND MST WEIGHT ONLY ============
    int mstWeight() {
        vector<Edge> mst = kruskalMST();
        if (mst.empty()) return -1;
        
        int total = 0;
        for (const Edge& e : mst) {
            total += e.weight;
        }
        return total;
    }
    
    // ============ FIND MAXIMUM SPANNING TREE ============
    vector<Edge> maximumSpanningTree() {
        if (isDirected) {
            cout << "Maximum spanning tree works only on undirected graphs!" << endl;
            return {};
        }
        
        // Sort edges in descending order
        sort(edges.begin(), edges.end(),
             [](const Edge& a, const Edge& b) {
                 return a.weight > b.weight;
             });
        
        UnionFind uf(vertices);
        vector<Edge> mst;
        int totalWeight = 0;
        
        for (const Edge& edge : edges) {
            if (uf.unite(edge.source, edge.destination)) {
                mst.push_back(edge);
                totalWeight += edge.weight;
                if (mst.size() == vertices - 1) break;
            }
        }
        
        if (mst.size() != vertices - 1) {
            cout << "Graph is not connected!" << endl;
            return {};
        }
        
        cout << "Total Maximum Spanning Tree Weight: " << totalWeight << endl;
        return mst;
    }
    
    // ============ SECOND BEST MST ============
    int secondBestMST() {
        vector<Edge> mst = kruskalMST();
        if (mst.empty()) return -1;
        
        int secondBest = INT_MAX;
        
        // Try removing each edge from MST and find next best
        for (const Edge& excluded : mst) {
            UnionFind uf(vertices);
            int weight = 0;
            int edgesUsed = 0;
            
            // Kruskal without the excluded edge
            for (const Edge& edge : edges) {
                if (edge.source == excluded.source && 
                    edge.destination == excluded.destination &&
                    edge.weight == excluded.weight) {
                    continue;  // Skip the excluded edge
                }
                
                if (uf.unite(edge.source, edge.destination)) {
                    weight += edge.weight;
                    edgesUsed++;
                    if (edgesUsed == vertices - 1) break;
                }
            }
            
            if (edgesUsed == vertices - 1 && weight < secondBest) {
                secondBest = weight;
            }
        }
        
        return secondBest;
    }
    
    // ============ CHECK IF GRAPH IS CONNECTED ============
    bool isConnected() {
        UnionFind uf(vertices);
        for (const Edge& edge : edges) {
            uf.unite(edge.source, edge.destination);
        }
        
        int root = uf.find(0);
        for (int i = 1; i < vertices; i++) {
            if (uf.find(i) != root) return false;
        }
        return true;
    }
    
    // ============ PRINT MST ============
    void printMST() {
        vector<Edge> mst = kruskalMST();
        if (mst.empty()) return;
        
        cout << "\nMinimum Spanning Tree Edges:\n";
        cout << "Edge\t\tWeight\n";
        cout << "-------------------\n";
        for (const Edge& edge : mst) {
            cout << edge.source << " -- " << edge.destination << "\t\t" << edge.weight << endl;
        }
    }
    
    // ============ PRINT MAXIMUM SPANNING TREE ============
    void printMaxST() {
        vector<Edge> mst = maximumSpanningTree();
        if (mst.empty()) return;
        
        cout << "\nMaximum Spanning Tree Edges:\n";
        cout << "Edge\t\tWeight\n";
        cout << "-------------------\n";
        for (const Edge& edge : mst) {
            cout << edge.source << " -- " << edge.destination << "\t\t" << edge.weight << endl;
        }
    }
    
    // ============ DISPLAY GRAPH ============
    void display() {
        cout << "\nGraph Edges:\n";
        cout << "Source -> Destination (Weight)\n";
        for (const Edge& edge : edges) {
            cout << edge.source << " -> " << edge.destination << " (" << edge.weight << ")" << endl;
        }
    }
};

int main() {
    cout << "=== Kruskal's Algorithm Demo ===" << endl;
    
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
    g1.printMST();
    
    // Example 2: Graph from visualization
    cout << "\n2. Graph from Visualization:" << endl;
    Graph g2(4, false);
    g2.addEdge(0, 1, 2);
    g2.addEdge(0, 2, 4);
    g2.addEdge(1, 2, 5);
    g2.addEdge(1, 3, 3);
    g2.addEdge(2, 3, 1);
    
    g2.display();
    g2.printMST();
    
    // Example 3: Maximum Spanning Tree
    cout << "\n3. Maximum Spanning Tree:" << endl;
    Graph g3(4, false);
    g3.addEdge(0, 1, 10);
    g3.addEdge(0, 2, 6);
    g3.addEdge(0, 3, 5);
    g3.addEdge(1, 3, 15);
    g3.addEdge(2, 3, 4);
    
    g3.display();
    g3.printMST();
    g3.printMaxST();
    
    // Example 4: Disconnected graph
    cout << "\n4. Disconnected Graph:" << endl;
    Graph g4(5, false);
    g4.addEdge(0, 1, 2);
    g4.addEdge(0, 2, 3);
    g4.addEdge(3, 4, 4);
    // No edge connecting {0,1,2} to {3,4}
    
    g4.display();
    cout << "Is connected? " << (g4.isConnected() ? "Yes" : "No") << endl;
    g4.printMST();  // Will show error
    
    // Example 5: Second Best MST
    cout << "\n5. Second Best MST:" << endl;
    Graph g5(4, false);
    g5.addEdge(0, 1, 1);
    g5.addEdge(0, 2, 2);
    g5.addEdge(0, 3, 3);
    g5.addEdge(1, 2, 3);
    g5.addEdge(1, 3, 4);
    g5.addEdge(2, 3, 5);
    
    g5.display();
    g5.printMST();
    
    int secondBest = g5.secondBestMST();
    if (secondBest != INT_MAX) {
        cout << "\nSecond Best MST Weight: " << secondBest << endl;
    }
    
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
    g6.printMST();
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Sorting Edges** | O(E log E) | O(E) |
| **Union-Find Operations** | O(E × α(V)) | O(V) |
| **Total Kruskal** | O(E log E) | O(V + E) |

Where α(V) is the inverse Ackermann function (practically constant)

---

## 🎯 Applications of Kruskal's Algorithm

| Application | Description |
|-------------|-------------|
| **Network Design** | Minimum cost to connect all nodes |
| **Clustering** | Single-linkage clustering |
| **Approximation Algorithms** | Traveling Salesman Problem (TSP) |
| **Image Segmentation** | Minimum spanning tree-based segmentation |
| **Maze Generation** | Creating perfect mazes |
| **Electric Grid Design** | Minimizing wiring cost |
| **Telecommunications** | Minimum cost network layout |

---

## 📊 Kruskal vs Prim vs Boruvka

| Algorithm | Approach | Time Complexity | Best For |
|-----------|----------|-----------------|----------|
| **Kruskal** | Edge-based (sort edges) | O(E log E) | Sparse graphs |
| **Prim** | Vertex-based (priority queue) | O((V+E) log V) | Dense graphs |
| **Boruvka** | Component-based | O(E log V) | Parallel processing |

---

## ✅ Key Takeaways

1. **Kruskal's algorithm** builds MST by adding smallest edges
2. **Union-Find** detects cycles efficiently
3. **Sort edges first** by weight
4. **Stops when V-1 edges** are selected
5. **Works only on undirected graphs**
6. **Graph must be connected** for MST to exist
7. **Maximum spanning tree** uses same algorithm with descending weights

---