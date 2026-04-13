# Graph Algorithm - Eulerian Path and Circuit

## 📖 Overview

An Eulerian path is a trail that visits every edge exactly once, while an Eulerian circuit (or cycle) starts and ends at the same vertex. These concepts originated from the famous Seven Bridges of Königsberg problem solved by Leonhard Euler in 1736, marking the birth of graph theory.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Eulerian Path** | Visits every edge exactly once (start ≠ end) |
| **Eulerian Circuit** | Visits every edge exactly once (start = end) |
| **Eulerian Trail** | Another name for Eulerian path |
| **Degree** | Number of edges incident to a vertex |
| **Semi-Eulerian** | Graph has Eulerian path but not circuit |

---

## 📊 Eulerian Path/Circuit Rules

### Undirected Graph

| Condition | Eulerian Circuit | Eulerian Path |
|-----------|-----------------|---------------|
| **All vertices** | Even degree | Even degree (except 2 odd) |
| **Connected** | Required (except isolated vertices) | Required (except isolated vertices) |
| **Odd degree vertices** | 0 | Exactly 2 |

### Directed Graph

| Condition | Eulerian Circuit | Eulerian Path |
|-----------|-----------------|---------------|
| **In-degree = Out-degree** | All vertices | All vertices (except start/end) |
| **Connected** | Required (weakly) | Required (weakly) |
| **Degree difference** | 0 for all | Start: out-in=1, End: in-out=1 |

---

## 📝 Complete Implementation

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <cstring>
#include <iomanip>
using namespace std;

class Graph {
private:
    int vertices;
    vector<list<int>> adj;
    vector<list<int>> adjCopy;  // For algorithm use
    bool isDirected;
    
public:
    Graph(int v, bool directed = false) : vertices(v), isDirected(directed) {
        adj.resize(v);
        adjCopy.resize(v);
    }
    
    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adjCopy[u].push_back(v);
        if (!isDirected) {
            adj[v].push_back(u);
            adjCopy[v].push_back(u);
        }
    }
    
    // ============ CHECK CONDITIONS ============
    bool hasEulerianCircuit() {
        if (!isConnected()) return false;
        
        if (isDirected) {
            return hasEulerianCircuitDirected();
        } else {
            return hasEulerianCircuitUndirected();
        }
    }
    
    bool hasEulerianPath() {
        if (!isConnected()) return false;
        
        if (isDirected) {
            return hasEulerianPathDirected();
        } else {
            return hasEulerianPathUndirected();
        }
    }
    
private:
    bool isConnected() {
        // Find first non-isolated vertex
        int start = -1;
        for (int i = 0; i < vertices; i++) {
            if (!adj[i].empty()) {
                start = i;
                break;
            }
        }
        
        if (start == -1) return true;  // Empty graph
        
        // DFS to check connectivity
        vector<bool> visited(vertices, false);
        dfsConnectivity(start, visited);
        
        // Check if all non-isolated vertices are visited
        for (int i = 0; i < vertices; i++) {
            if (!adj[i].empty() && !visited[i]) {
                return false;
            }
        }
        
        return true;
    }
    
    void dfsConnectivity(int u, vector<bool>& visited) {
        visited[u] = true;
        for (int v : adj[u]) {
            if (!visited[v]) {
                dfsConnectivity(v, visited);
            }
        }
    }
    
    bool hasEulerianCircuitUndirected() {
        // All vertices must have even degree
        for (int i = 0; i < vertices; i++) {
            if (adj[i].size() % 2 != 0) {
                return false;
            }
        }
        return true;
    }
    
    bool hasEulerianPathUndirected() {
        int oddCount = 0;
        for (int i = 0; i < vertices; i++) {
            if (adj[i].size() % 2 != 0) {
                oddCount++;
            }
        }
        return oddCount == 0 || oddCount == 2;
    }
    
    bool hasEulerianCircuitDirected() {
        for (int i = 0; i < vertices; i++) {
            if (inDegree(i) != outDegree(i)) {
                return false;
            }
        }
        return true;
    }
    
    bool hasEulerianPathDirected() {
        int startCount = 0, endCount = 0;
        for (int i = 0; i < vertices; i++) {
            int in = inDegree(i);
            int out = outDegree(i);
            
            if (out - in == 1) {
                startCount++;
            } else if (in - out == 1) {
                endCount++;
            } else if (in != out) {
                return false;
            }
        }
        return (startCount == 1 && endCount == 1) || 
               (startCount == 0 && endCount == 0);
    }
    
    int inDegree(int v) {
        int count = 0;
        for (int i = 0; i < vertices; i++) {
            for (int neighbor : adj[i]) {
                if (neighbor == v) count++;
            }
        }
        return count;
    }
    
    int outDegree(int v) {
        return adj[v].size();
    }
    
public:
    // ============ FIND EULERIAN CIRCUIT/PATH (Fleury's Algorithm) ============
    vector<int> findEulerianCircuit() {
        if (!hasEulerianCircuit()) {
            cout << "Graph does not have an Eulerian circuit!" << endl;
            return {};
        }
        
        // Make a copy of adjacency list
        vector<list<int>> tempAdj = adj;
        vector<int> circuit;
        
        // Find start vertex (any vertex with edges)
        int start = 0;
        for (int i = 0; i < vertices; i++) {
            if (!tempAdj[i].empty()) {
                start = i;
                break;
            }
        }
        
        fleury(start, tempAdj, circuit);
        
        return circuit;
    }
    
    vector<int> findEulerianPath() {
        if (!hasEulerianPath()) {
            cout << "Graph does not have an Eulerian path!" << endl;
            return {};
        }
        
        vector<list<int>> tempAdj = adj;
        vector<int> path;
        
        // Find start vertex
        int start = findStartVertex();
        
        fleury(start, tempAdj, path);
        
        return path;
    }
    
private:
    void fleury(int u, vector<list<int>>& tempAdj, vector<int>& result) {
        for (auto it = tempAdj[u].begin(); it != tempAdj[u].end();) {
            int v = *it;
            
            // Check if edge (u,v) is a bridge
            if (isBridge(u, v, tempAdj)) {
                ++it;
                continue;
            }
            
            // Remove edge and continue
            removeEdge(u, v, tempAdj);
            fleury(v, tempAdj, result);
            it = tempAdj[u].begin();  // Reset iterator
        }
        
        result.push_back(u);
    }
    
    bool isBridge(int u, int v, vector<list<int>>& tempAdj) {
        // Count reachable vertices from u before removing edge
        vector<bool> visited(vertices, false);
        int countBefore = dfsCount(u, visited, tempAdj);
        
        // Remove edge
        removeEdge(u, v, tempAdj);
        
        // Count reachable vertices from u after removing edge
        fill(visited.begin(), visited.end(), false);
        int countAfter = dfsCount(u, visited, tempAdj);
        
        // Add edge back
        addEdgeTemp(u, v, tempAdj);
        
        // Edge is bridge if count decreases
        return countAfter < countBefore;
    }
    
    int dfsCount(int u, vector<bool>& visited, vector<list<int>>& tempAdj) {
        visited[u] = true;
        int count = 1;
        for (int v : tempAdj[u]) {
            if (!visited[v]) {
                count += dfsCount(v, visited, tempAdj);
            }
        }
        return count;
    }
    
    void removeEdge(int u, int v, vector<list<int>>& tempAdj) {
        tempAdj[u].remove(v);
        if (!isDirected) {
            tempAdj[v].remove(u);
        }
    }
    
    void addEdgeTemp(int u, int v, vector<list<int>>& tempAdj) {
        tempAdj[u].push_back(v);
        if (!isDirected) {
            tempAdj[v].push_back(u);
        }
    }
    
    int findStartVertex() {
        if (isDirected) {
            // Find vertex with out-degree = in-degree + 1 (start of path)
            for (int i = 0; i < vertices; i++) {
                if (outDegree(i) - inDegree(i) == 1) {
                    return i;
                }
            }
        } else {
            // Find vertex with odd degree
            for (int i = 0; i < vertices; i++) {
                if (adj[i].size() % 2 != 0) {
                    return i;
                }
            }
        }
        
        // If no odd degree vertex, start from any vertex with edges
        for (int i = 0; i < vertices; i++) {
            if (!adj[i].empty()) {
                return i;
            }
        }
        return 0;
    }
    
public:
    // ============ HIERHOLZER'S ALGORITHM (More efficient) ============
    vector<int> hierholzerEulerianCircuit() {
        if (!hasEulerianCircuit()) {
            cout << "Graph does not have an Eulerian circuit!" << endl;
            return {};
        }
        
        vector<list<int>> tempAdj = adj;
        vector<int> circuit;
        stack<int> currPath;
        
        int start = 0;
        for (int i = 0; i < vertices; i++) {
            if (!tempAdj[i].empty()) {
                start = i;
                break;
            }
        }
        
        currPath.push(start);
        
        while (!currPath.empty()) {
            int u = currPath.top();
            
            if (!tempAdj[u].empty()) {
                int v = tempAdj[u].front();
                tempAdj[u].pop_front();
                if (!isDirected) {
                    tempAdj[v].remove(u);
                }
                currPath.push(v);
            } else {
                circuit.push_back(u);
                currPath.pop();
            }
        }
        
        reverse(circuit.begin(), circuit.end());
        return circuit;
    }
    
    // ============ DISPLAY ============
    void display() {
        cout << "\nGraph (" << (isDirected ? "Directed" : "Undirected") << "):\n";
        for (int i = 0; i < vertices; i++) {
            cout << i << ": ";
            for (int neighbor : adj[i]) {
                cout << neighbor << " ";
            }
            cout << endl;
        }
    }
    
    void displayEulerianStatus() {
        cout << "\nEulerian Status:" << endl;
        cout << "Has Eulerian Circuit: " << (hasEulerianCircuit() ? "Yes" : "No") << endl;
        cout << "Has Eulerian Path: " << (hasEulerianPath() ? "Yes" : "No") << endl;
    }
    
    void displayEulerianCircuit() {
        vector<int> circuit = hierholzerEulerianCircuit();
        if (circuit.empty()) return;
        
        cout << "\nEulerian Circuit: ";
        for (int v : circuit) {
            cout << v << " ";
        }
        cout << endl;
    }
};

int main() {
    cout << "=== Eulerian Path & Circuit Demo ===" << endl;
    
    // Example 1: Graph with Eulerian circuit (all vertices even degree)
    cout << "\n1. Graph with Eulerian Circuit (Square):" << endl;
    Graph g1(4, false);
    g1.addEdge(0, 1);
    g1.addEdge(1, 2);
    g1.addEdge(2, 3);
    g1.addEdge(3, 0);
    
    g1.display();
    g1.displayEulerianStatus();
    g1.displayEulerianCircuit();
    
    // Example 2: Graph with Eulerian path (2 odd degree vertices)
    cout << "\n2. Graph with Eulerian Path (2 odd degrees):" << endl;
    Graph g2(4, false);
    g2.addEdge(0, 1);
    g2.addEdge(1, 2);
    g2.addEdge(2, 3);
    
    g2.display();
    g2.displayEulerianStatus();
    
    // Example 3: Directed graph with Eulerian circuit
    cout << "\n3. Directed Graph with Eulerian Circuit:" << endl;
    Graph g3(4, true);
    g3.addEdge(0, 1);
    g3.addEdge(1, 2);
    g3.addEdge(2, 3);
    g3.addEdge(3, 0);
    
    g3.display();
    g3.displayEulerianStatus();
    g3.displayEulerianCircuit();
    
    // Example 4: Directed graph with Eulerian path
    cout << "\n4. Directed Graph with Eulerian Path:" << endl;
    Graph g4(4, true);
    g4.addEdge(0, 1);
    g4.addEdge(1, 2);
    g4.addEdge(2, 3);
    
    g4.display();
    g4.displayEulerianStatus();
    
    // Example 5: Graph with no Eulerian path/circuit
    cout << "\n5. Graph with No Eulerian Path:" << endl;
    Graph g5(5, false);
    g5.addEdge(0, 1);
    g5.addEdge(1, 2);
    g5.addEdge(2, 3);
    g5.addEdge(3, 4);
    g5.addEdge(4, 0);
    g5.addEdge(0, 2);  // Creates odd degree vertices
    
    g5.display();
    g5.displayEulerianStatus();
    
    // Example 6: Hierholzer's algorithm demonstration
    cout << "\n6. Hierholzer's Algorithm (More efficient):" << endl;
    Graph g6(5, false);
    g6.addEdge(0, 1);
    g6.addEdge(1, 2);
    g6.addEdge(2, 3);
    g6.addEdge(3, 4);
    g6.addEdge(4, 0);
    g6.addEdge(0, 2);
    g6.addEdge(2, 4);
    
    g6.display();
    g6.displayEulerianStatus();
    g6.displayEulerianCircuit();
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Fleury's Algorithm** | O(E²) | O(V + E) |
| **Hierholzer's Algorithm** | O(E) | O(V + E) |

---

## 🎯 Applications

| Application | Description |
|-------------|-------------|
| **Route Planning** | Garbage collection, snow plowing |
| **DNA Sequencing** | Reconstructing DNA fragments |
| **Network Design** | Efficient network traversal |
| **Puzzle Solving** | Chinese postman problem |
| **Circuit Design** | Testing electrical circuits |

---

## ✅ Key Takeaways

1. **Eulerian circuit** exists if all vertices have even degree (undirected)
2. **Eulerian path** exists if exactly 0 or 2 vertices have odd degree
3. **Directed Eulerian circuit** requires in-degree = out-degree for all vertices
4. **Hierholzer's algorithm** is more efficient than Fleury's
5. **Connectedness** is essential (ignoring isolated vertices)

---
---

## Next Step

- Go to [15_Johnson_Algorithm.md](15_Johnson_Algorithm.md) to continue with Johnson Algorithm.
