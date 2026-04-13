# Graph Algorithm - Floyd-Warshall Algorithm

## 📖 Overview

The Floyd-Warshall algorithm finds the shortest paths between **all pairs** of vertices in a weighted graph. Unlike Dijkstra (single source) or Bellman-Ford (single source), Floyd-Warshall computes the shortest path distance between every pair of vertices. It can handle negative edge weights but cannot handle negative cycles.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **All-Pairs Shortest Path** | Finds shortest paths between every vertex pair |
| **Dynamic Programming** | Builds solutions using intermediate vertices |
| **Adjacency Matrix** | Uses matrix representation for efficiency |
| **Negative Edge Support** | Works with negative weights (no negative cycles) |
| **Transitive Closure** | Can be adapted to find reachability |

---

## 📊 How Floyd-Warshall Works

### Step-by-step Visualization

```
Initial Graph (Adjacency Matrix):
     0   1   2   3
0    0   3   ∞   5
1    2   0   ∞   4
2    ∞   1   0   ∞
3    ∞   ∞   2   0

After k=0 (using vertex 0 as intermediate):
- Path 1→3: min(4, 1→0→3 = 2+5=7) → remains 4
- No improvements

After k=1 (using vertex 1 as intermediate):
- Path 0→2: min(∞, 0→1→2 = 3+∞=∞) → no change
- Path 2→0: min(∞, 2→1→0 = 1+2=3) → 3
- Path 2→3: min(∞, 2→1→3 = 1+4=5) → 5
- Path 3→0: min(∞, 3→1→0 = ∞+2=∞) → no change

After k=2 (using vertex 2 as intermediate):
- Path 0→3: min(5, 0→2→3 = ∞+∞=∞) → no change
- Path 1→0: min(2, 1→2→0 = ∞+3=∞) → no change
- Path 3→0: min(∞, 3→2→0 = 2+3=5) → 5
- Path 3→1: min(∞, 3→2→1 = 2+1=3) → 3

After k=3 (using vertex 3 as intermediate):
- Path 0→2: min(∞, 0→3→2 = 5+2=7) → 7
- Path 1→2: min(∞, 1→3→2 = 4+2=6) → 6
- Path 2→0: min(3, 2→3→0 = 5+5=10) → remains 3

Final Distance Matrix:
     0   1   2   3
0    0   3   7   5
1    2   0   6   4
2    3   1   0   5
3    5   3   2   0
```

---

## 📝 Complete Implementation

```cpp
#include <iostream>
#include <vector>
#include <climits>
#include <iomanip>
#include <algorithm>
using namespace std;

class Graph {
private:
    int vertices;
    vector<vector<int>> dist;
    vector<vector<int>> next;
    bool hasNegativeCycle;
    
public:
    Graph(int v) : vertices(v), hasNegativeCycle(false) {
        // Initialize distance matrix
        dist.resize(v, vector<int>(v, INT_MAX));
        next.resize(v, vector<int>(v, -1));
        
        // Distance to self is 0
        for (int i = 0; i < v; i++) {
            dist[i][i] = 0;
            next[i][i] = i;
        }
    }
    
    void addEdge(int u, int v, int weight) {
        dist[u][v] = weight;
        next[u][v] = v;
    }
    
    // ============ FLOYD-WARSHALL ALGORITHM ============
    void floydWarshall() {
        // Copy original distances for path reconstruction
        vector<vector<int>> oldDist = dist;
        
        // Main algorithm: consider each vertex as intermediate
        for (int k = 0; k < vertices; k++) {
            for (int i = 0; i < vertices; i++) {
                for (int j = 0; j < vertices; j++) {
                    if (dist[i][k] != INT_MAX && dist[k][j] != INT_MAX &&
                        dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                        next[i][j] = next[i][k];
                    }
                }
            }
        }
        
        // Check for negative cycles
        for (int i = 0; i < vertices; i++) {
            if (dist[i][i] < 0) {
                hasNegativeCycle = true;
                break;
            }
        }
    }
    
    // ============ GET SHORTEST DISTANCE BETWEEN VERTICES ============
    int getDistance(int u, int v) {
        return dist[u][v];
    }
    
    // ============ GET SHORTEST PATH BETWEEN VERTICES ============
    vector<int> getPath(int u, int v) {
        if (next[u][v] == -1) return {};
        
        vector<int> path;
        path.push_back(u);
        
        while (u != v) {
            u = next[u][v];
            path.push_back(u);
        }
        
        return path;
    }
    
    // ============ PRINT DISTANCE MATRIX ============
    void printDistanceMatrix() {
        cout << "\nShortest Distance Matrix:\n";
        cout << "   ";
        for (int i = 0; i < vertices; i++) {
            cout << setw(5) << i;
        }
        cout << endl;
        
        for (int i = 0; i < vertices; i++) {
            cout << setw(2) << i << " ";
            for (int j = 0; j < vertices; j++) {
                if (dist[i][j] == INT_MAX) {
                    cout << "  ∞";
                } else {
                    cout << setw(5) << dist[i][j];
                }
            }
            cout << endl;
        }
    }
    
    // ============ PRINT ALL PAIRS SHORTEST PATHS ============
    void printAllPaths() {
        cout << "\nAll-Pairs Shortest Paths:\n";
        for (int i = 0; i < vertices; i++) {
            for (int j = 0; j < vertices; j++) {
                if (i != j && dist[i][j] != INT_MAX) {
                    vector<int> path = getPath(i, j);
                    cout << "Path from " << i << " to " << j << ": ";
                    for (int v : path) cout << v << " ";
                    cout << "(distance = " << dist[i][j] << ")" << endl;
                }
            }
        }
    }
    
    // ============ CHECK IF GRAPH HAS NEGATIVE CYCLE ============
    bool hasNegativeCycle() {
        return hasNegativeCycle;
    }
    
    // ============ FIND GRAPH DIAMETER (LONGEST SHORTEST PATH) ============
    int getDiameter() {
        int diameter = 0;
        for (int i = 0; i < vertices; i++) {
            for (int j = 0; j < vertices; j++) {
                if (dist[i][j] != INT_MAX && dist[i][j] > diameter) {
                    diameter = dist[i][j];
                }
            }
        }
        return diameter;
    }
    
    // ============ FIND GRAPH RADIUS (MINIMUM ECCENTRICITY) ============
    int getRadius() {
        vector<int> eccentricity(vertices, 0);
        
        for (int i = 0; i < vertices; i++) {
            for (int j = 0; j < vertices; j++) {
                if (dist[i][j] != INT_MAX && dist[i][j] > eccentricity[i]) {
                    eccentricity[i] = dist[i][j];
                }
            }
        }
        
        int radius = INT_MAX;
        for (int i = 0; i < vertices; i++) {
            if (eccentricity[i] < radius) {
                radius = eccentricity[i];
            }
        }
        
        return radius;
    }
    
    // ============ FIND CENTER OF GRAPH ============
    vector<int> getCenters() {
        vector<int> eccentricity(vertices, 0);
        
        for (int i = 0; i < vertices; i++) {
            for (int j = 0; j < vertices; j++) {
                if (dist[i][j] != INT_MAX && dist[i][j] > eccentricity[i]) {
                    eccentricity[i] = dist[i][j];
                }
            }
        }
        
        int radius = getRadius();
        vector<int> centers;
        for (int i = 0; i < vertices; i++) {
            if (eccentricity[i] == radius) {
                centers.push_back(i);
            }
        }
        
        return centers;
    }
    
    // ============ TRANSITIVE CLOSURE (REACHABILITY) ============
    vector<vector<bool>> transitiveClosure() {
        vector<vector<bool>> reachable(vertices, vector<bool>(vertices, false));
        
        // Initialize reachability
        for (int i = 0; i < vertices; i++) {
            for (int j = 0; j < vertices; j++) {
                reachable[i][j] = (dist[i][j] != INT_MAX);
            }
        }
        
        // Floyd-Warshall for reachability
        for (int k = 0; k < vertices; k++) {
            for (int i = 0; i < vertices; i++) {
                for (int j = 0; j < vertices; j++) {
                    if (reachable[i][k] && reachable[k][j]) {
                        reachable[i][j] = true;
                    }
                }
            }
        }
        
        return reachable;
    }
    
    // ============ DETECT NEGATIVE CYCLE (DETAILED) ============
    bool detectNegativeCycle() {
        floydWarshall();
        return hasNegativeCycle;
    }
    
    // ============ DISPLAY GRAPH ============
    void display() {
        cout << "\nGraph Adjacency Matrix:\n";
        cout << "   ";
        for (int i = 0; i < vertices; i++) {
            cout << setw(3) << i;
        }
        cout << endl;
        
        for (int i = 0; i < vertices; i++) {
            cout << setw(2) << i << " ";
            for (int j = 0; j < vertices; j++) {
                if (i == j) {
                    cout << "  0";
                } else if (dist[i][j] == INT_MAX) {
                    cout << "  ∞";
                } else {
                    cout << setw(3) << dist[i][j];
                }
            }
            cout << endl;
        }
    }
};

int main() {
    cout << "=== Floyd-Warshall Algorithm Demo ===" << endl;
    
    // Example 1: Simple directed graph
    cout << "\n1. Simple Directed Graph:" << endl;
    Graph g1(4);
    g1.addEdge(0, 1, 3);
    g1.addEdge(0, 3, 5);
    g1.addEdge(1, 0, 2);
    g1.addEdge(1, 3, 4);
    g1.addEdge(2, 1, 1);
    g1.addEdge(3, 2, 2);
    
    g1.floydWarshall();
    g1.printDistanceMatrix();
    g1.printAllPaths();
    
    cout << "\nHas negative cycle? " << (g1.hasNegativeCycle() ? "Yes" : "No") << endl;
    cout << "Graph diameter: " << g1.getDiameter() << endl;
    cout << "Graph radius: " << g1.getRadius() << endl;
    
    vector<int> centers = g1.getCenters();
    cout << "Graph centers: ";
    for (int c : centers) cout << c << " ";
    cout << endl;
    
    // Example 2: Undirected weighted graph
    cout << "\n2. Undirected Weighted Graph:" << endl;
    Graph g2(5);
    g2.addEdge(0, 1, 2);
    g2.addEdge(0, 2, 4);
    g2.addEdge(1, 2, 1);
    g2.addEdge(1, 3, 7);
    g2.addEdge(2, 3, 3);
    g2.addEdge(3, 4, 1);
    g2.addEdge(2, 4, 5);
    
    // Add reverse edges for undirected (in Floyd-Warshall, we add both directions)
    g2.addEdge(1, 0, 2);
    g2.addEdge(2, 0, 4);
    g2.addEdge(2, 1, 1);
    g2.addEdge(3, 1, 7);
    g2.addEdge(3, 2, 3);
    g2.addEdge(4, 3, 1);
    g2.addEdge(4, 2, 5);
    
    g2.floydWarshall();
    g2.printDistanceMatrix();
    
    // Example 3: Graph with negative cycle
    cout << "\n3. Graph with Negative Cycle:" << endl;
    Graph g3(4);
    g3.addEdge(0, 1, 1);
    g3.addEdge(1, 2, -1);
    g3.addEdge(2, 3, -1);
    g3.addEdge(3, 0, -1);
    
    g3.floydWarshall();
    cout << "Has negative cycle? " << (g3.hasNegativeCycle() ? "Yes" : "No") << endl;
    if (g3.hasNegativeCycle()) {
        cout << "Negative cycle detected! Shortest paths are not well-defined." << endl;
    }
    
    // Example 4: Transitive closure
    cout << "\n4. Transitive Closure (Reachability):" << endl;
    Graph g4(4);
    g4.addEdge(0, 1, 1);
    g4.addEdge(1, 2, 1);
    g4.addEdge(2, 3, 1);
    // No edge from 0 to 3 directly
    
    g4.floydWarshall();
    vector<vector<bool>> reachable = g4.transitiveClosure();
    
    cout << "Reachability Matrix:\n";
    cout << "   ";
    for (int i = 0; i < 4; i++) cout << setw(3) << i;
    cout << endl;
    for (int i = 0; i < 4; i++) {
        cout << setw(2) << i << " ";
        for (int j = 0; j < 4; j++) {
            cout << setw(3) << (reachable[i][j] ? 1 : 0);
        }
        cout << endl;
    }
    
    // Example 5: Path reconstruction
    cout << "\n5. Path Reconstruction Example:" << endl;
    Graph g5(5);
    g5.addEdge(0, 1, 3);
    g5.addEdge(0, 2, 8);
    g5.addEdge(1, 2, 2);
    g5.addEdge(1, 3, 5);
    g5.addEdge(2, 3, 1);
    g5.addEdge(2, 4, 6);
    g5.addEdge(3, 4, 2);
    
    g5.floydWarshall();
    g5.printAllPaths();
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Aspect | Complexity |
|--------|------------|
| **Time Complexity** | O(V³) |
| **Space Complexity** | O(V²) |
| **Negative Cycle Detection** | O(V³) |

---

## 🎯 Applications of Floyd-Warshall

| Application | Description |
|-------------|-------------|
| **Shortest Path in Dense Graphs** | When V is small (≤ 500) |
| **Transitive Closure** | Finding reachability between vertices |
| **Graph Diameter** | Longest shortest path in graph |
| **Graph Radius** | Minimum eccentricity |
| **Finding Graph Centers** | Vertices with minimum eccentricity |
| **Network Routing** | Computing routing tables |
| **Minimum Cost Path** | In weighted graphs |
| **Detecting Negative Cycles** | For currency arbitrage |

---

## 📊 Floyd-Warshall vs Other Shortest Path Algorithms

| Algorithm | Pairs | Negative Edges | Time Complexity |
|-----------|-------|----------------|-----------------|
| **Dijkstra (repeated)** | All | No | O(V × (V+E) log V) |
| **Bellman-Ford (repeated)** | All | Yes | O(V² × E) |
| **Floyd-Warshall** | All | Yes (no cycles) | O(V³) |
| **Johnson's Algorithm** | All | Yes | O(V×E log V) |

---

## ✅ Key Takeaways

1. **Floyd-Warshall** computes all-pairs shortest paths
2. **Dynamic programming** approach with O(V³) time
3. **Simple to implement** using adjacency matrix
4. **Works with negative edges** but not negative cycles
5. **Path reconstruction** possible using next matrix
6. **Transitive closure** is a special case (unweighted)
7. **Best for dense graphs** with small vertex count

---
---

## Next Step

- Go to [04_Kruskal_Algorithm.md](04_Kruskal_Algorithm.md) to continue with Kruskal Algorithm.
