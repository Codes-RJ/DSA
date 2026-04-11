# Graph Algorithm - Bipartite Graph

## 📖 Overview

A bipartite graph is a graph whose vertices can be divided into two disjoint sets such that every edge connects a vertex from one set to a vertex from the other set. Bipartite graphs are also known as 2-colorable graphs. They are used to model matching problems, job assignments, and relationships between two distinct groups.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Bipartite Graph** | Graph that can be colored with 2 colors |
| **2-Colorable** | Adjacent vertices have different colors |
| **Odd Cycle** | Graph with odd cycle is NOT bipartite |
| **Bipartition** | The two disjoint sets (U and V) |
| **Matching** | Set of edges without common vertices |

---

## 📊 Bipartite Graph Examples

### Bipartite Graph
```
    U         V
    0 --- 3
    |     |
    1 --- 4
    |     |
    2 --- 5

    Color 0: {0,1,2}
    Color 1: {3,4,5}
```

### Non-Bipartite Graph (Triangle)
```
    0 --- 1
    | \   |
    |  \  |
    |   \ |
    2 --- 3
    
    Contains odd cycle (0-1-3-2-0)
    NOT bipartite!
```

---

## 📝 Complete Implementation

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstring>
#include <iomanip>
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
    
    // ============ BFS-BASED BIPARTITE CHECK ============
    bool isBipartiteBFS() {
        vector<int> color(vertices, -1);  // -1: uncolored, 0: color A, 1: color B
        
        for (int i = 0; i < vertices; i++) {
            if (color[i] == -1) {
                if (!bfsCheck(i, color)) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
private:
    bool bfsCheck(int start, vector<int>& color) {
        queue<int> q;
        q.push(start);
        color[start] = 0;
        
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            
            for (int v : adj[u]) {
                if (color[v] == -1) {
                    color[v] = color[u] ^ 1;  // Alternate color
                    q.push(v);
                } else if (color[v] == color[u]) {
                    return false;  // Same color on adjacent vertices
                }
            }
        }
        
        return true;
    }
    
public:
    // ============ DFS-BASED BIPARTITE CHECK ============
    bool isBipartiteDFS() {
        vector<int> color(vertices, -1);
        
        for (int i = 0; i < vertices; i++) {
            if (color[i] == -1) {
                if (!dfsCheck(i, 0, color)) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
private:
    bool dfsCheck(int u, int c, vector<int>& color) {
        color[u] = c;
        
        for (int v : adj[u]) {
            if (color[v] == -1) {
                if (!dfsCheck(v, c ^ 1, color)) {
                    return false;
                }
            } else if (color[v] == color[u]) {
                return false;
            }
        }
        
        return true;
    }
    
public:
    // ============ GET BIPARTITION ============
    pair<vector<int>, vector<int>> getBipartition() {
        vector<int> color(vertices, -1);
        vector<int> setA, setB;
        
        for (int i = 0; i < vertices; i++) {
            if (color[i] == -1) {
                if (!dfsCheck(i, 0, color)) {
                    cout << "Graph is not bipartite!" << endl;
                    return {{}, {}};
                }
            }
        }
        
        for (int i = 0; i < vertices; i++) {
            if (color[i] == 0) {
                setA.push_back(i);
            } else {
                setB.push_back(i);
            }
        }
        
        return {setA, setB};
    }
    
    // ============ MAXIMUM BIPARTITE MATCHING ============
    int maxBipartiteMatching(int leftSetSize) {
        // For bipartite graph where vertices 0..leftSetSize-1 are left side
        vector<int> matchRight(vertices, -1);
        int result = 0;
        
        for (int u = 0; u < leftSetSize; u++) {
            vector<bool> visited(vertices, false);
            if (bpmDFS(u, visited, matchRight)) {
                result++;
            }
        }
        
        return result;
    }
    
private:
    bool bpmDFS(int u, vector<bool>& visited, vector<int>& matchRight) {
        for (int v : adj[u]) {
            if (!visited[v]) {
                visited[v] = true;
                
                if (matchRight[v] == -1 || bpmDFS(matchRight[v], visited, matchRight)) {
                    matchRight[v] = u;
                    return true;
                }
            }
        }
        return false;
    }
    
public:
    // ============ CHECK IF GRAPH HAS ODD CYCLE ============
    bool hasOddCycle() {
        return !isBipartiteBFS();  // Non-bipartite means odd cycle exists
    }
    
    // ============ FIND ODD CYCLE (if exists) ============
    vector<int> findOddCycle() {
        vector<int> color(vertices, -1);
        vector<int> parent(vertices, -1);
        
        for (int i = 0; i < vertices; i++) {
            if (color[i] == -1) {
                vector<int> cycle = findOddCycleDFS(i, color, parent);
                if (!cycle.empty()) {
                    return cycle;
                }
            }
        }
        
        return {};
    }
    
private:
    vector<int> findOddCycleDFS(int u, vector<int>& color, vector<int>& parent) {
        color[u] = 0;
        
        for (int v : adj[u]) {
            if (color[v] == -1) {
                parent[v] = u;
                vector<int> cycle = findOddCycleDFS(v, color, parent);
                if (!cycle.empty()) return cycle;
            } else if (color[v] == 0 && parent[u] != v) {
                // Found a cycle
                vector<int> cycle;
                int current = u;
                while (current != v) {
                    cycle.push_back(current);
                    current = parent[current];
                }
                cycle.push_back(v);
                cycle.push_back(u);
                return cycle;
            }
        }
        
        color[u] = 1;
        return {};
    }
    
public:
    // ============ MAXIMUM BIPARTITE MATCHING (Hopcroft-Karp) ============
    int hopcroftKarp(int leftSetSize) {
        vector<int> pairU(leftSetSize, -1);
        vector<int> pairV(vertices, -1);
        vector<int> dist(leftSetSize);
        
        int matching = 0;
        
        while (bfsHopcroftKarp(pairU, pairV, dist)) {
            for (int u = 0; u < leftSetSize; u++) {
                if (pairU[u] == -1) {
                    if (dfsHopcroftKarp(u, pairU, pairV, dist)) {
                        matching++;
                    }
                }
            }
        }
        
        return matching;
    }
    
private:
    bool bfsHopcroftKarp(vector<int>& pairU, vector<int>& pairV, vector<int>& dist) {
        queue<int> q;
        
        for (int u = 0; u < pairU.size(); u++) {
            if (pairU[u] == -1) {
                dist[u] = 0;
                q.push(u);
            } else {
                dist[u] = INT_MAX;
            }
        }
        
        bool found = false;
        
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            
            for (int v : adj[u]) {
                if (pairV[v] != -1 && dist[pairV[v]] == INT_MAX) {
                    dist[pairV[v]] = dist[u] + 1;
                    q.push(pairV[v]);
                } else if (pairV[v] == -1) {
                    found = true;
                }
            }
        }
        
        return found;
    }
    
    bool dfsHopcroftKarp(int u, vector<int>& pairU, vector<int>& pairV, vector<int>& dist) {
        for (int v : adj[u]) {
            if (pairV[v] == -1 || (dist[pairV[v]] == dist[u] + 1 && 
                dfsHopcroftKarp(pairV[v], pairU, pairV, dist))) {
                pairU[u] = v;
                pairV[v] = u;
                return true;
            }
        }
        
        dist[u] = INT_MAX;
        return false;
    }
    
public:
    // ============ DISPLAY ============
    void display() {
        cout << "\nGraph Adjacency List:\n";
        for (int i = 0; i < vertices; i++) {
            cout << i << ": ";
            for (int neighbor : adj[i]) {
                cout << neighbor << " ";
            }
            cout << endl;
        }
    }
    
    void displayBipartition() {
        if (!isBipartiteBFS()) {
            cout << "Graph is not bipartite!" << endl;
            return;
        }
        
        auto [setA, setB] = getBipartition();
        
        cout << "\nBipartition:\n";
        cout << "Set A (Color 0): ";
        for (int v : setA) cout << v << " ";
        cout << endl;
        cout << "Set B (Color 1): ";
        for (int v : setB) cout << v << " ";
        cout << endl;
    }
};

int main() {
    cout << "=== Bipartite Graph Demo ===" << endl;
    
    // Example 1: Bipartite graph (even cycle)
    cout << "\n1. Bipartite Graph (Even Cycle):" << endl;
    Graph g1(4, false);
    g1.addEdge(0, 1);
    g1.addEdge(1, 2);
    g1.addEdge(2, 3);
    g1.addEdge(3, 0);
    
    g1.display();
    cout << "Is bipartite (BFS): " << (g1.isBipartiteBFS() ? "Yes" : "No") << endl;
    cout << "Is bipartite (DFS): " << (g1.isBipartiteDFS() ? "Yes" : "No") << endl;
    g1.displayBipartition();
    
    // Example 2: Non-bipartite graph (odd cycle)
    cout << "\n2. Non-Bipartite Graph (Triangle):" << endl;
    Graph g2(3, false);
    g2.addEdge(0, 1);
    g2.addEdge(1, 2);
    g2.addEdge(2, 0);
    
    g2.display();
    cout << "Is bipartite: " << (g2.isBipartiteBFS() ? "Yes" : "No") << endl;
    cout << "Has odd cycle: " << (g2.hasOddCycle() ? "Yes" : "No") << endl;
    
    vector<int> oddCycle = g2.findOddCycle();
    if (!oddCycle.empty()) {
        cout << "Odd cycle found: ";
        for (int v : oddCycle) cout << v << " ";
        cout << endl;
    }
    
    // Example 3: Bipartite graph for matching
    cout << "\n3. Bipartite Graph for Matching:" << endl;
    Graph g3(6, false);
    // Left side: 0,1,2 | Right side: 3,4,5
    g3.addEdge(0, 3);
    g3.addEdge(0, 4);
    g3.addEdge(1, 4);
    g3.addEdge(1, 5);
    g3.addEdge(2, 5);
    
    g3.display();
    g3.displayBipartition();
    
    cout << "\nMaximum Bipartite Matching: " << g3.maxBipartiteMatching(3) << endl;
    cout << "Hopcroft-Karp Matching: " << g3.hopcroftKarp(3) << endl;
    
    // Example 4: Tree (always bipartite)
    cout << "\n4. Tree (Always Bipartite):" << endl;
    Graph g4(5, false);
    g4.addEdge(0, 1);
    g4.addEdge(0, 2);
    g4.addEdge(1, 3);
    g4.addEdge(1, 4);
    
    g4.display();
    cout << "Is bipartite: " << (g4.isBipartiteBFS() ? "Yes" : "No") << endl;
    g4.displayBipartition();
    
    // Example 5: Disconnected bipartite graph
    cout << "\n5. Disconnected Bipartite Graph:" << endl;
    Graph g5(6, false);
    // Component 1: even cycle
    g5.addEdge(0, 1);
    g5.addEdge(1, 2);
    g5.addEdge(2, 3);
    g5.addEdge(3, 0);
    // Component 2: bipartite chain
    g5.addEdge(4, 5);
    
    g5.display();
    cout << "Is bipartite: " << (g5.isBipartiteBFS() ? "Yes" : "No") << endl;
    g5.displayBipartition();
    
    // Example 6: Complete bipartite graph K3,3
    cout << "\n6. Complete Bipartite Graph K3,3:" << endl;
    Graph g6(6, false);
    // Left: 0,1,2 | Right: 3,4,5
    for (int i = 0; i < 3; i++) {
        for (int j = 3; j < 6; j++) {
            g6.addEdge(i, j);
        }
    }
    
    g6.display();
    cout << "Is bipartite: " << (g6.isBipartiteBFS() ? "Yes" : "No") << endl;
    g6.displayBipartition();
    
    // Example 7: Graph with odd cycle detection
    cout << "\n7. Odd Cycle Detection:" << endl;
    Graph g7(5, false);
    g7.addEdge(0, 1);
    g7.addEdge(1, 2);
    g7.addEdge(2, 0);  // Triangle
    g7.addEdge(2, 3);
    g7.addEdge(3, 4);
    
    g7.display();
    cout << "Has odd cycle: " << (g7.hasOddCycle() ? "Yes" : "No") << endl;
    
    oddCycle = g7.findOddCycle();
    if (!oddCycle.empty()) {
        cout << "Odd cycle found: ";
        for (int v : oddCycle) cout << v << " ";
        cout << endl;
    }
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Bipartite Check (BFS/DFS)** | O(V + E) | O(V) |
| **Maximum Matching (DFS)** | O(V × E) | O(V) |
| **Hopcroft-Karp** | O(E × √V) | O(V) |

---

## 🎯 Applications

| Application | Description |
|-------------|-------------|
| **Job Assignment** | Matching workers to tasks |
| **Marriage Problem** | Stable matching |
| **Recommendation Systems** | User-item matching |
| **Scheduling** | Two-group scheduling |
| **Network Flow** | Bipartite matching via max flow |
| **Social Networks** | Finding two distinct groups |

---

## ✅ Key Takeaways

1. **Bipartite graphs** are 2-colorable
2. **No odd cycles** in bipartite graphs
3. **BFS/DFS** can check bipartiteness
4. **Matching** finds maximum edge set without shared vertices
5. **Hopcroft-Karp** is efficient for large bipartite graphs

---