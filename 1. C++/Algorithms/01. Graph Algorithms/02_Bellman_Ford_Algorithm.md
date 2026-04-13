# Graph Algorithm - Bellman-Ford Algorithm

## 📖 Overview

The Bellman-Ford algorithm finds the shortest paths from a source vertex to all other vertices in a weighted graph. Unlike Dijkstra's algorithm, Bellman-Ford can handle **negative edge weights** and can **detect negative cycles**. It is commonly used in applications like currency arbitrage detection and network routing protocols.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Single Source Shortest Path** | Finds shortest paths from source to all vertices |
| **Negative Weights** | Works correctly with negative edges |
| **Negative Cycle Detection** | Can detect cycles that reduce total distance |
| **Dynamic Programming Approach** | Relaxes edges V-1 times |
| **Slower but More Powerful** | O(V×E) vs Dijkstra's O((V+E) log V) |

---

## 📊 How Bellman-Ford Works

### Step-by-step Visualization

```
Graph with negative edge:
        4
    0 ---→ 1
    |       |
   2|       |-3
    ↓       ↓
    2 ---→ 3
        1

Initial distances from 0: [0, ∞, ∞, ∞]

Relaxation Pass 1:
  Edge (0,1): 0 + 4 = 4 → dist[1] = 4
  Edge (0,2): 0 + 2 = 2 → dist[2] = 2
  Edge (2,3): 2 + 1 = 3 → dist[3] = 3
  Edge (1,3): 4 + (-3) = 1 → dist[3] = min(3,1) = 1

Relaxation Pass 2:
  Edge (1,3): 4 + (-3) = 1 → dist[3] stays 1
  (Other edges don't improve)

Final distances from 0:
  → 0: 0
  → 1: 4 (0→1)
  → 2: 2 (0→2)
  → 3: 1 (0→1→3)  Note: Path 0→2→3 gives 3, but 0→1→3 gives 1
```

---

## 📝 Complete Implementation

```cpp
#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>
#include <iomanip>
using namespace std;

class Edge {
public:
    int source, destination, weight;
    Edge(int u, int v, int w) : source(u), destination(v), weight(w) {}
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
            edges.push_back(Edge(v, u, weight));
        }
    }
    
    // ============ BELLMAN-FORD ALGORITHM ============
    // Returns true if no negative cycle, false otherwise
    bool bellmanFord(int source, vector<int>& dist, vector<int>& parent) {
        // Step 1: Initialize distances
        dist.assign(vertices, INT_MAX);
        parent.assign(vertices, -1);
        dist[source] = 0;
        
        // Step 2: Relax all edges V-1 times
        for (int i = 1; i <= vertices - 1; i++) {
            bool updated = false;
            for (const Edge& edge : edges) {
                if (dist[edge.source] != INT_MAX && 
                    dist[edge.source] + edge.weight < dist[edge.destination]) {
                    dist[edge.destination] = dist[edge.source] + edge.weight;
                    parent[edge.destination] = edge.source;
                    updated = true;
                }
            }
            if (!updated) break;  // Early termination if no updates
        }
        
        // Step 3: Check for negative cycles
        for (const Edge& edge : edges) {
            if (dist[edge.source] != INT_MAX && 
                dist[edge.source] + edge.weight < dist[edge.destination]) {
                return false;  // Negative cycle detected
            }
        }
        
        return true;  // No negative cycle
    }
    
    // ============ BASIC BELLMAN-FORD (VECTOR RETURN) ============
    vector<int> shortestPaths(int source) {
        vector<int> dist, parent;
        bool noNegativeCycle = bellmanFord(source, dist, parent);
        
        if (!noNegativeCycle) {
            cout << "Graph contains a negative cycle!" << endl;
            return {};
        }
        
        return dist;
    }
    
    // ============ BELLMAN-FORD WITH PATH ============
    vector<int> getPath(int source, int target) {
        vector<int> dist, parent;
        bool noNegativeCycle = bellmanFord(source, dist, parent);
        
        if (!noNegativeCycle || dist[target] == INT_MAX) {
            return {};
        }
        
        vector<int> path;
        for (int v = target; v != -1; v = parent[v]) {
            path.push_back(v);
        }
        reverse(path.begin(), path.end());
        
        return path;
    }
    
    // ============ PRINT SHORTEST PATHS ============
    void printShortestPaths(int source) {
        vector<int> dist, parent;
        bool noNegativeCycle = bellmanFord(source, dist, parent);
        
        if (!noNegativeCycle) {
            cout << "Graph contains a negative cycle! Cannot compute shortest paths." << endl;
            return;
        }
        
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
    
    // ============ DETECT NEGATIVE CYCLE ============
    bool hasNegativeCycle() {
        vector<int> dist, parent;
        return !bellmanFord(0, dist, parent);
    }
    
    // ============ FIND NEGATIVE CYCLE (if exists) ============
    vector<int> findNegativeCycle() {
        vector<int> dist(vertices, 0);  // Start with all distances 0
        vector<int> parent(vertices, -1);
        int lastUpdated = -1;
        
        // Run V iterations (one extra to detect cycle)
        for (int i = 0; i < vertices; i++) {
            lastUpdated = -1;
            for (const Edge& edge : edges) {
                if (dist[edge.source] != INT_MAX && 
                    dist[edge.source] + edge.weight < dist[edge.destination]) {
                    dist[edge.destination] = dist[edge.source] + edge.weight;
                    parent[edge.destination] = edge.source;
                    lastUpdated = edge.destination;
                }
            }
        }
        
        if (lastUpdated == -1) {
            return {};  // No negative cycle
        }
        
        // Find cycle by backtracking
        vector<bool> visited(vertices, false);
        vector<int> cycle;
        
        // Move to a node in the cycle
        for (int i = 0; i < vertices; i++) {
            lastUpdated = parent[lastUpdated];
        }
        
        // Trace the cycle
        int start = lastUpdated;
        do {
            cycle.push_back(lastUpdated);
            lastUpdated = parent[lastUpdated];
        } while (lastUpdated != start);
        cycle.push_back(start);
        reverse(cycle.begin(), cycle.end());
        
        return cycle;
    }
    
    // ============ CURRENCY ARBITRAGE DETECTION ============
    // Exchange rates: if rate[i][j] = 1.5, means 1 unit of currency i = 1.5 of currency j
    // To detect arbitrage, we use logarithms to convert multiplication to addition
    bool detectArbitrage(vector<vector<double>>& exchangeRates) {
        int n = exchangeRates.size();
        vector<double> dist(n, 0);
        
        // Convert to negative log (for shortest path)
        vector<Edge> arbitrageEdges;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j) {
                    // Using negative log to detect positive cycles
                    double weight = -log(exchangeRates[i][j]);
                    arbitrageEdges.push_back(Edge(i, j, weight));
                }
            }
        }
        
        // Bellman-Ford to detect negative cycle (which indicates arbitrage)
        for (int i = 0; i < n - 1; i++) {
            for (const Edge& edge : arbitrageEdges) {
                if (dist[edge.source] + edge.weight < dist[edge.destination]) {
                    dist[edge.destination] = dist[edge.source] + edge.weight;
                }
            }
        }
        
        // Check for negative cycle
        for (const Edge& edge : arbitrageEdges) {
            if (dist[edge.source] + edge.weight < dist[edge.destination]) {
                return true;  // Arbitrage opportunity found
            }
        }
        
        return false;
    }
    
    // ============ PRINT DISTANCE MATRIX ============
    void printDistanceMatrix() {
        cout << "\nDistance Matrix (All-pairs shortest paths):\n";
        cout << "   ";
        for (int i = 0; i < vertices; i++) {
            cout << setw(5) << i;
        }
        cout << endl;
        
        for (int i = 0; i < vertices; i++) {
            vector<int> dist = shortestPaths(i);
            cout << setw(2) << i << " ";
            for (int j = 0; j < vertices; j++) {
                if (dist.empty() || dist[j] == INT_MAX) {
                    cout << "  ∞";
                } else {
                    cout << setw(5) << dist[j];
                }
            }
            cout << endl;
        }
    }
    
    // ============ DISPLAY GRAPH ============
    void display() {
        cout << "\nGraph Edges (Weighted):" << endl;
        for (const Edge& edge : edges) {
            cout << edge.source << " --(" << edge.weight << ")--> " << edge.destination << endl;
        }
    }
};

int main() {
    cout << "=== Bellman-Ford Algorithm Demo ===" << endl;
    
    // Example 1: Graph with positive and negative edges
    cout << "\n1. Graph with Negative Edge:" << endl;
    Graph g1(5, true);
    g1.addEdge(0, 1, 6);
    g1.addEdge(0, 2, 7);
    g1.addEdge(1, 2, 8);
    g1.addEdge(1, 3, 5);
    g1.addEdge(1, 4, -4);
    g1.addEdge(2, 3, -3);
    g1.addEdge(2, 4, 9);
    g1.addEdge(3, 1, -2);
    g1.addEdge(4, 0, 2);
    g1.addEdge(4, 3, 7);
    
    g1.display();
    
    cout << "\nHas negative cycle? " << (g1.hasNegativeCycle() ? "Yes" : "No") << endl;
    g1.printShortestPaths(0);
    
    // Example 2: Graph with negative cycle
    cout << "\n2. Graph with Negative Cycle:" << endl;
    Graph g2(4, true);
    g2.addEdge(0, 1, 1);
    g2.addEdge(1, 2, -1);
    g2.addEdge(2, 3, -1);
    g2.addEdge(3, 0, -1);  // Creates negative cycle
    
    g2.display();
    
    cout << "\nHas negative cycle? " << (g2.hasNegativeCycle() ? "Yes" : "No") << endl;
    
    if (g2.hasNegativeCycle()) {
        vector<int> cycle = g2.findNegativeCycle();
        if (!cycle.empty()) {
            cout << "Negative cycle: ";
            for (int v : cycle) cout << v << " ";
            cout << endl;
        }
    }
    
    // Example 3: Simple graph (no negative edges)
    cout << "\n3. Simple Graph (No Negative Edges):" << endl;
    Graph g3(5, false);
    g3.addEdge(0, 1, 2);
    g3.addEdge(0, 2, 4);
    g3.addEdge(1, 2, 1);
    g3.addEdge(1, 3, 7);
    g3.addEdge(2, 3, 3);
    g3.addEdge(3, 4, 1);
    g3.addEdge(2, 4, 5);
    
    g3.display();
    g3.printShortestPaths(0);
    
    // Example 4: Currency Arbitrage Detection
    cout << "\n4. Currency Arbitrage Detection:" << endl;
    vector<vector<double>> exchangeRates = {
        {1, 0.5, 0.2},
        {2, 1, 0.4},
        {5, 2.5, 1}
    };
    
    Graph arb(3, true);
    bool hasArbitrage = arb.detectArbitrage(exchangeRates);
    cout << "Arbitrage opportunity? " << (hasArbitrage ? "Yes" : "No") << endl;
    
    // Another exchange rate matrix with arbitrage
    vector<vector<double>> exchangeRates2 = {
        {1, 0.8, 1.2},
        {1.3, 1, 0.9},
        {0.8, 1.1, 1}
    };
    
    hasArbitrage = arb.detectArbitrage(exchangeRates2);
    cout << "Arbitrage opportunity? " << (hasArbitrage ? "Yes" : "No") << endl;
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Standard Bellman-Ford** | O(V × E) | O(V) |
| **With Early Termination** | O(V × E) worst case | O(V) |
| **Negative Cycle Detection** | O(V × E) | O(V) |

---

## 🎯 Applications of Bellman-Ford

| Application | Description |
|-------------|-------------|
| **Currency Arbitrage** | Detecting profitable currency exchange cycles |
| **Network Routing** | RIP (Routing Information Protocol) |
| **GPS Navigation** | Handling roads with negative weights (downhill) |
| **Game Development** | Pathfinding with varying terrain costs |
| **Financial Analysis** | Detecting arbitrage opportunities |
| **Traffic Flow** | Modeling congestion with negative weights |

---

## 📊 Dijkstra vs Bellman-Ford

| Feature | Dijkstra | Bellman-Ford |
|---------|----------|--------------|
| **Negative Edges** | ❌ No | ✅ Yes |
| **Negative Cycle Detection** | ❌ No | ✅ Yes |
| **Time Complexity** | O((V+E) log V) | O(V × E) |
| **Space Complexity** | O(V) | O(V) |
| **Greedy Approach** | ✅ Yes | ❌ No (DP) |

---

## ✅ Key Takeaways

1. **Bellman-Ford** handles negative edge weights
2. **Detects negative cycles** (can't find shortest paths in such graphs)
3. **Slower than Dijkstra** (O(V×E) vs O((V+E) log V))
4. **Dynamic programming approach** (relaxes edges V-1 times)
5. **Useful for** currency arbitrage detection
6. **Early termination** possible if no updates in a pass
7. **Widely used** in routing protocols (RIP)

---
---

## Next Step

- Go to [03_Floyd_Warshall_Algorithm.md](03_Floyd_Warshall_Algorithm.md) to continue with Floyd Warshall Algorithm.
