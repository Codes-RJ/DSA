# Cycle Detection in Graphs

## 📖 Overview

Cycle detection is a fundamental graph algorithm that determines whether a graph contains a cycle (a path that starts and ends at the same vertex). Cycle detection is crucial for many applications, including deadlock detection, dependency resolution, and validating graph structures like trees.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Cycle** | Path that starts and ends at same vertex |
| **Back Edge** | Edge from a vertex to an ancestor in DFS tree |
| **Cross Edge** | Edge connecting different DFS trees |
| **Forward Edge** | Edge from ancestor to descendant (not tree edge) |
| **Tree Edge** | Edge used in DFS traversal |

---

## 📊 Cycle Types

### Undirected Graph Cycle
```
Cycle: 0-1-2-0
    0 --- 1
    |     |
    |     |
    3 --- 2
    
This graph has a cycle: 0-1-2-3-0
```

### Directed Graph Cycle
```
Cycle: 0→1→2→0
    0 → 1
    ↑   ↓
    3 ← 2
    
This graph has a cycle: 0→1→2→0
```

---

## 📝 Complete Implementation

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <algorithm>
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
    
    // ============ CYCLE DETECTION IN UNDIRECTED GRAPH ============
    bool hasCycleUndirectedUtil(int v, int parent, vector<bool>& visited) {
        visited[v] = true;
        
        for (int neighbor : adj[v]) {
            if (!visited[neighbor]) {
                if (hasCycleUndirectedUtil(neighbor, v, visited)) {
                    return true;
                }
            } else if (neighbor != parent) {
                return true;  // Found a back edge (cycle)
            }
        }
        return false;
    }
    
    bool hasCycleUndirected() {
        if (isDirected) {
            cout << "Graph is directed. Use hasCycleDirected() instead." << endl;
            return false;
        }
        
        vector<bool> visited(vertices, false);
        
        for (int i = 0; i < vertices; i++) {
            if (!visited[i]) {
                if (hasCycleUndirectedUtil(i, -1, visited)) {
                    return true;
                }
            }
        }
        return false;
    }
    
    // ============ CYCLE DETECTION IN DIRECTED GRAPH ============
    bool hasCycleDirectedUtil(int v, vector<bool>& visited, vector<bool>& recStack, 
                               vector<int>& parent, vector<vector<int>>& cycles) {
        visited[v] = true;
        recStack[v] = true;
        
        for (int neighbor : adj[v]) {
            if (!visited[neighbor]) {
                parent[neighbor] = v;
                if (hasCycleDirectedUtil(neighbor, visited, recStack, parent, cycles)) {
                    return true;
                }
            } else if (recStack[neighbor]) {
                // Found a cycle
                cycles.push_back(getCyclePath(parent, v, neighbor));
                return true;
            }
        }
        
        recStack[v] = false;
        return false;
    }
    
    vector<int> getCyclePath(vector<int>& parent, int end, int start) {
        vector<int> path;
        int current = end;
        
        while (current != start && current != -1) {
            path.push_back(current);
            current = parent[current];
        }
        path.push_back(start);
        
        reverse(path.begin(), path.end());
        return path;
    }
    
    bool hasCycleDirected() {
        if (!isDirected) {
            cout << "Graph is undirected. Use hasCycleUndirected() instead." << endl;
            return false;
        }
        
        vector<bool> visited(vertices, false);
        vector<bool> recStack(vertices, false);
        vector<int> parent(vertices, -1);
        vector<vector<int>> cycles;
        
        for (int i = 0; i < vertices; i++) {
            if (!visited[i]) {
                if (hasCycleDirectedUtil(i, visited, recStack, parent, cycles)) {
                    // Print the cycle
                    cout << "Cycle detected: ";
                    for (int v : cycles[0]) cout << v << " ";
                    cout << endl;
                    return true;
                }
            }
        }
        return false;
    }
    
    // ============ FIND ALL CYCLES (LIMITED TO SIMPLE CYCLES) ============
    void findAllCyclesUndirected() {
        if (isDirected) {
            cout << "Directed graph not supported for this method." << endl;
            return;
        }
        
        vector<bool> visited(vertices, false);
        vector<int> parent(vertices, -1);
        vector<vector<int>> cycles;
        
        for (int i = 0; i < vertices; i++) {
            if (!visited[i]) {
                dfsCycleFind(i, -1, visited, parent, cycles);
            }
        }
        
        cout << "\nFound " << cycles.size() << " cycles:" << endl;
        for (size_t i = 0; i < cycles.size(); i++) {
            cout << "Cycle " << i + 1 << ": ";
            for (int v : cycles[i]) cout << v << " ";
            cout << endl;
        }
    }
    
private:
    void dfsCycleFind(int v, int parent, vector<bool>& visited, 
                      vector<int>& parentArr, vector<vector<int>>& cycles) {
        visited[v] = true;
        parentArr[v] = parent;
        
        for (int neighbor : adj[v]) {
            if (!visited[neighbor]) {
                dfsCycleFind(neighbor, v, visited, parentArr, cycles);
            } else if (neighbor != parent && neighbor < v) {
                // Found a cycle
                vector<int> cycle;
                int current = v;
                cycle.push_back(current);
                while (current != neighbor) {
                    current = parentArr[current];
                    cycle.push_back(current);
                }
                cycles.push_back(cycle);
            }
        }
    }
    
public:
    // ============ DETECT CYCLE USING UNION-FIND (UNDIRECTED) ============
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
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }
        
        bool unite(int x, int y) {
            int rx = find(x), ry = find(y);
            if (rx == ry) return false;  // Cycle detected
            
            if (rank[rx] < rank[ry]) {
                parent[rx] = ry;
            } else if (rank[rx] > rank[ry]) {
                parent[ry] = rx;
            } else {
                parent[ry] = rx;
                rank[rx]++;
            }
            return true;
        }
    };
    
    bool hasCycleUnionFind() {
        if (isDirected) {
            cout << "Union-Find cycle detection works only for undirected graphs." << endl;
            return false;
        }
        
        UnionFind uf(vertices);
        
        for (int u = 0; u < vertices; u++) {
            for (int v : adj[u]) {
                if (u < v) {  // Check each edge only once
                    if (!uf.unite(u, v)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
    
    // ============ CYCLE DETECTION USING COLORS (DIRECTED) ============
    // 0 = unvisited, 1 = visiting (in recursion stack), 2 = fully processed
    bool hasCycleColoredUtil(int v, vector<int>& color) {
        color[v] = 1;  // Currently in recursion stack
        
        for (int neighbor : adj[v]) {
            if (color[neighbor] == 0) {
                if (hasCycleColoredUtil(neighbor, color)) {
                    return true;
                }
            } else if (color[neighbor] == 1) {
                return true;  // Back edge found
            }
        }
        
        color[v] = 2;  // Fully processed
        return false;
    }
    
    bool hasCycleColored() {
        if (!isDirected) {
            cout << "Color-based cycle detection works only for directed graphs." << endl;
            return false;
        }
        
        vector<int> color(vertices, 0);  // 0 = unvisited
        
        for (int i = 0; i < vertices; i++) {
            if (color[i] == 0) {
                if (hasCycleColoredUtil(i, color)) {
                    return true;
                }
            }
        }
        return false;
    }
    
    // ============ FIND CYCLE LENGTH ============
    int getCycleLength() {
        if (!hasCycleUndirected() && !hasCycleDirected()) {
            return 0;
        }
        
        // BFS to find shortest cycle
        int shortestCycle = INT_MAX;
        
        for (int i = 0; i < vertices; i++) {
            vector<int> dist(vertices, -1);
            vector<int> parent(vertices, -1);
            queue<int> q;
            
            dist[i] = 0;
            q.push(i);
            
            while (!q.empty()) {
                int v = q.front();
                q.pop();
                
                for (int neighbor : adj[v]) {
                    if (dist[neighbor] == -1) {
                        dist[neighbor] = dist[v] + 1;
                        parent[neighbor] = v;
                        q.push(neighbor);
                    } else if (parent[v] != neighbor && parent[neighbor] != v) {
                        // Found a cycle
                        shortestCycle = min(shortestCycle, dist[v] + dist[neighbor] + 1);
                    }
                }
            }
        }
        
        return shortestCycle;
    }
    
    // ============ DISPLAY GRAPH ============
    void display() {
        cout << "\nGraph Adjacency List:" << endl;
        cout << "Type: " << (isDirected ? "Directed" : "Undirected") << endl;
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
    cout << "=== Cycle Detection Demo ===" << endl;
    
    // ============ UNDIRECTED GRAPHS ============
    cout << "\n1. Undirected Graph with Cycle:" << endl;
    Graph g1(4, false);
    g1.addEdge(0, 1);
    g1.addEdge(1, 2);
    g1.addEdge(2, 3);
    g1.addEdge(3, 0);  // Creates cycle 0-1-2-3-0
    
    g1.display();
    cout << "Has cycle (DFS): " << (g1.hasCycleUndirected() ? "Yes" : "No") << endl;
    cout << "Has cycle (Union-Find): " << (g1.hasCycleUnionFind() ? "Yes" : "No") << endl;
    
    cout << "\n2. Undirected Graph without Cycle (Tree):" << endl;
    Graph g2(5, false);
    g2.addEdge(0, 1);
    g2.addEdge(0, 2);
    g2.addEdge(1, 3);
    g2.addEdge(1, 4);
    
    g2.display();
    cout << "Has cycle: " << (g2.hasCycleUndirected() ? "Yes" : "No") << endl;
    
    cout << "\n3. Undirected Graph with Multiple Cycles:" << endl;
    Graph g3(5, false);
    g3.addEdge(0, 1);
    g3.addEdge(1, 2);
    g3.addEdge(2, 0);  // Cycle 0-1-2
    g3.addEdge(2, 3);
    g3.addEdge(3, 4);
    g3.addEdge(4, 2);  // Cycle 2-3-4
    
    g3.display();
    cout << "Has cycle: " << (g3.hasCycleUndirected() ? "Yes" : "No") << endl;
    
    // ============ DIRECTED GRAPHS ============
    cout << "\n4. Directed Graph with Cycle:" << endl;
    Graph g4(4, true);
    g4.addEdge(0, 1);
    g4.addEdge(1, 2);
    g4.addEdge(2, 3);
    g4.addEdge(3, 1);  // Creates cycle 1-2-3-1
    
    g4.display();
    cout << "Has cycle (DFS): " << (g4.hasCycleDirected() ? "Yes" : "No") << endl;
    cout << "Has cycle (Color method): " << (g4.hasCycleColored() ? "Yes" : "No") << endl;
    
    cout << "\n5. Directed Acyclic Graph (DAG):" << endl;
    Graph g5(5, true);
    g5.addEdge(0, 1);
    g5.addEdge(0, 2);
    g5.addEdge(1, 3);
    g5.addEdge(2, 3);
    g5.addEdge(3, 4);
    
    g5.display();
    cout << "Has cycle: " << (g5.hasCycleDirected() ? "Yes" : "No") << endl;
    
    cout << "\n6. Directed Graph with Self-Loop:" << endl;
    Graph g6(3, true);
    g6.addEdge(0, 1);
    g6.addEdge(1, 1);  // Self-loop (cycle of length 1)
    g6.addEdge(1, 2);
    
    g6.display();
    cout << "Has cycle: " << (g6.hasCycleDirected() ? "Yes" : "No") << endl;
    
    // ============ CYCLE LENGTH ============
    cout << "\n7. Cycle Length Analysis:" << endl;
    Graph g7(5, false);
    g7.addEdge(0, 1);
    g7.addEdge(1, 2);
    g7.addEdge(2, 0);  // Triangle (cycle length 3)
    g7.addEdge(2, 3);
    g7.addEdge(3, 4);
    g7.addEdge(4, 2);  // Another cycle
    
    g7.display();
    cout << "Has cycle: " << (g7.hasCycleUndirected() ? "Yes" : "No") << endl;
    int cycleLen = g7.getCycleLength();
    if (cycleLen != INT_MAX) {
        cout << "Shortest cycle length: " << cycleLen << endl;
    }
    
    // ============ FIND ALL CYCLES ============
    cout << "\n8. Finding All Cycles:" << endl;
    Graph g8(5, false);
    g8.addEdge(0, 1);
    g8.addEdge(1, 2);
    g8.addEdge(2, 0);
    g8.addEdge(2, 3);
    g8.addEdge(3, 4);
    g8.addEdge(4, 2);
    
    g8.display();
    g8.findAllCyclesUndirected();
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Method | Graph Type | Time Complexity | Space Complexity |
|--------|------------|----------------|------------------|
| **DFS (Undirected)** | Undirected | O(V + E) | O(V) |
| **DFS (Directed)** | Directed | O(V + E) | O(V) |
| **Union-Find** | Undirected | O(E × α(V)) | O(V) |
| **Color Method** | Directed | O(V + E) | O(V) |

---

## 🎯 Applications of Cycle Detection

| Application | Description |
|-------------|-------------|
| **Deadlock Detection** | Finding circular wait in operating systems |
| **Dependency Resolution** | Detecting circular dependencies in build systems |
| **Garbage Collection** | Detecting cyclic references |
| **Circuit Analysis** | Finding loops in electronic circuits |
| **Graph Validation** | Checking if graph is a tree |
| **Deadlock Prevention** | Detecting potential deadlocks |
| **Social Networks** | Finding friend circles |
| **Routing Protocols** | Detecting routing loops |

---

## ✅ Key Takeaways

1. **Undirected graph**: A cycle exists if an edge connects two already visited vertices that are not parent
2. **Directed graph**: A cycle exists if we find a back edge (edge to vertex in recursion stack)
3. **Union-Find** provides near-constant time cycle detection for undirected graphs
4. **Color method** (0/1/2) elegantly detects cycles in directed graphs
5. **Self-loops** are cycles of length 1
6. **Multiple cycles** can exist in a single graph
7. **Cycle length** can be found using BFS from each vertex

---
---

## Next Step

- Go to [05_Topological_Sort.md](05_Topological_Sort.md) to continue with Topological Sort.
