# Graph Algorithm - Bridges (Cut Edges)

## 📖 Overview

Bridges (also called cut edges) are edges in a graph whose removal increases the number of connected components. They represent critical connections whose failure would disconnect the graph. Finding bridges is essential for network reliability, communication systems, and identifying vulnerabilities.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Bridge** | Edge whose removal disconnects the graph |
| **Cut Edge** | Another name for bridge |
| **DFS Tree** | Tree formed by DFS traversal |
| **Discovery Time** | Time when vertex is first visited |
| **Low Value** | Earliest visited vertex reachable from subtree |
| **Bridge Condition** | low[v] > disc[u] for edge (u,v) |

---

## 📊 Bridges Visualization

```
Graph with bridges:

    0 --- 1 --- 2
    |     |     |
    |     |     |
    3 --- 4     5

Bridges: (1,2) and (4,5) are bridges

Why?
- Removing (1,2) disconnects vertex 2
- Removing (4,5) disconnects vertex 5
- Other edges are part of cycles
```

---

## 📝 Complete Implementation

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
#include <set>
#include <iomanip>
#include <map>
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
    
    // ============ FIND BRIDGES ============
    vector<pair<int, int>> findBridges() {
        vector<bool> visited(vertices, false);
        vector<int> disc(vertices, -1);
        vector<int> low(vertices, -1);
        vector<int> parent(vertices, -1);
        vector<pair<int, int>> bridges;
        
        int time = 0;
        
        for (int i = 0; i < vertices; i++) {
            if (!visited[i]) {
                dfsBridge(i, visited, disc, low, parent, bridges, time);
            }
        }
        
        return bridges;
    }
    
private:
    void dfsBridge(int u, vector<bool>& visited, vector<int>& disc,
                   vector<int>& low, vector<int>& parent,
                   vector<pair<int, int>>& bridges, int& time) {
        visited[u] = true;
        disc[u] = low[u] = ++time;
        
        for (int v : adj[u]) {
            if (!visited[v]) {
                parent[v] = u;
                dfsBridge(v, visited, disc, low, parent, bridges, time);
                
                low[u] = min(low[u], low[v]);
                
                // Bridge condition: low[v] > disc[u]
                if (low[v] > disc[u]) {
                    bridges.push_back({u, v});
                }
            } else if (v != parent[u]) {
                low[u] = min(low[u], disc[v]);
            }
        }
    }
    
public:
    // ============ FIND BRIDGES WITH DETAILS ============
    struct BridgeInfo {
        int u, v;
        int discoveryTimeU;
        int lowV;
        string reason;
    };
    
    vector<BridgeInfo> findBridgesDetailed() {
        vector<bool> visited(vertices, false);
        vector<int> disc(vertices, -1);
        vector<int> low(vertices, -1);
        vector<int> parent(vertices, -1);
        vector<BridgeInfo> bridges;
        
        int time = 0;
        
        for (int i = 0; i < vertices; i++) {
            if (!visited[i]) {
                dfsBridgeDetailed(i, visited, disc, low, parent, bridges, time);
            }
        }
        
        return bridges;
    }
    
private:
    void dfsBridgeDetailed(int u, vector<bool>& visited, vector<int>& disc,
                           vector<int>& low, vector<int>& parent,
                           vector<BridgeInfo>& bridges, int& time) {
        visited[u] = true;
        disc[u] = low[u] = ++time;
        
        for (int v : adj[u]) {
            if (!visited[v]) {
                parent[v] = u;
                dfsBridgeDetailed(v, visited, disc, low, parent, bridges, time);
                
                low[u] = min(low[u], low[v]);
                
                if (low[v] > disc[u]) {
                    bridges.push_back({u, v, disc[u], low[v], 
                                      "low[" + to_string(v) + "]=" + to_string(low[v]) + 
                                      " > disc[" + to_string(u) + "]=" + to_string(disc[u])});
                }
            } else if (v != parent[u]) {
                low[u] = min(low[u], disc[v]);
            }
        }
    }
    
public:
    // ============ CHECK IF EDGE IS BRIDGE ============
    bool isBridge(int u, int v) {
        vector<pair<int, int>> bridges = findBridges();
        for (auto& edge : bridges) {
            if ((edge.first == u && edge.second == v) ||
                (edge.first == v && edge.second == u)) {
                return true;
            }
        }
        return false;
    }
    
    // ============ FIND 2-EDGE CONNECTED COMPONENTS ============
    vector<vector<int>> findTwoEdgeConnectedComponents() {
        vector<pair<int, int>> bridges = findBridges();
        set<pair<int, int>> bridgeSet;
        
        for (auto& edge : bridges) {
            bridgeSet.insert({edge.first, edge.second});
            bridgeSet.insert({edge.second, edge.first});
        }
        
        vector<bool> visited(vertices, false);
        vector<vector<int>> components;
        
        for (int i = 0; i < vertices; i++) {
            if (!visited[i]) {
                vector<int> component;
                dfsComponent(i, visited, component, bridgeSet);
                components.push_back(component);
            }
        }
        
        return components;
    }
    
private:
    void dfsComponent(int u, vector<bool>& visited, vector<int>& component,
                      set<pair<int, int>>& bridgeSet) {
        visited[u] = true;
        component.push_back(u);
        
        for (int v : adj[u]) {
            if (!visited[v] && bridgeSet.find({u, v}) == bridgeSet.end()) {
                dfsComponent(v, visited, component, bridgeSet);
            }
        }
    }
    
public:
    // ============ BRIDGE CONNECTIVITY (EDGE CONNECTIVITY) ============
    int edgeConnectivity() {
        vector<pair<int, int>> bridges = findBridges();
        return bridges.size();
    }
    
    // ============ REMOVE BRIDGES AND GET COMPONENTS ============
    vector<vector<int>> removeBridgesAndGetComponents() {
        vector<pair<int, int>> bridges = findBridges();
        set<pair<int, int>> bridgeSet;
        
        for (auto& edge : bridges) {
            bridgeSet.insert({edge.first, edge.second});
            bridgeSet.insert({edge.second, edge.first});
        }
        
        vector<bool> visited(vertices, false);
        vector<vector<int>> components;
        
        for (int i = 0; i < vertices; i++) {
            if (!visited[i]) {
                vector<int> component;
                dfsComponentNoBridges(i, visited, component, bridgeSet);
                components.push_back(component);
            }
        }
        
        return components;
    }
    
private:
    void dfsComponentNoBridges(int u, vector<bool>& visited, vector<int>& component,
                                set<pair<int, int>>& bridgeSet) {
        visited[u] = true;
        component.push_back(u);
        
        for (int v : adj[u]) {
            if (!visited[v] && bridgeSet.find({u, v}) == bridgeSet.end()) {
                dfsComponentNoBridges(v, visited, component, bridgeSet);
            }
        }
    }
    
public:
    // ============ FIND BRIDGES IN DIRECTED GRAPH ============
    vector<pair<int, int>> findBridgesDirected() {
        if (!isDirected) {
            cout << "This method is for directed graphs only." << endl;
            return {};
        }
        
        vector<bool> visited(vertices, false);
        vector<int> disc(vertices, -1);
        vector<int> low(vertices, -1);
        vector<int> parent(vertices, -1);
        vector<pair<int, int>> bridges;
        
        int time = 0;
        
        for (int i = 0; i < vertices; i++) {
            if (!visited[i]) {
                dfsBridgeDirected(i, visited, disc, low, parent, bridges, time);
            }
        }
        
        return bridges;
    }
    
private:
    void dfsBridgeDirected(int u, vector<bool>& visited, vector<int>& disc,
                           vector<int>& low, vector<int>& parent,
                           vector<pair<int, int>>& bridges, int& time) {
        visited[u] = true;
        disc[u] = low[u] = ++time;
        
        for (int v : adj[u]) {
            if (!visited[v]) {
                parent[v] = u;
                dfsBridgeDirected(v, visited, disc, low, parent, bridges, time);
                
                low[u] = min(low[u], low[v]);
                
                if (low[v] > disc[u]) {
                    bridges.push_back({u, v});
                }
            } else if (v != parent[u]) {
                low[u] = min(low[u], disc[v]);
            }
        }
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
    
    void displayBridges() {
        vector<pair<int, int>> bridges = findBridges();
        
        cout << "\nBridges (" << bridges.size() << "): ";
        if (bridges.empty()) {
            cout << "None" << endl;
        } else {
            for (auto& edge : bridges) {
                cout << "(" << edge.first << "," << edge.second << ") ";
            }
            cout << endl;
        }
    }
    
    void displayBridgesDetailed() {
        vector<BridgeInfo> bridges = findBridgesDetailed();
        
        if (bridges.empty()) {
            cout << "\nNo bridges found." << endl;
            return;
        }
        
        cout << "\nBridges Details:\n";
        cout << "Edge\t\tCondition\n";
        cout << "----\t\t---------\n";
        for (auto& info : bridges) {
            cout << info.u << " - " << info.v << "\t\t" << info.reason << endl;
        }
    }
    
    void displayTwoEdgeComponents() {
        vector<vector<int>> components = findTwoEdgeConnectedComponents();
        
        cout << "\n2-Edge Connected Components (" << components.size() << "):\n";
        for (size_t i = 0; i < components.size(); i++) {
            cout << "Component " << i + 1 << ": ";
            for (int v : components[i]) {
                cout << v << " ";
            }
            cout << endl;
        }
    }
    
    void displayEdgeConnectivity() {
        int bridges = findBridges().size();
        cout << "\nEdge Connectivity (Number of Bridges): " << bridges << endl;
    }
};

int main() {
    cout << "=== Bridges (Cut Edges) Demo ===" << endl;
    
    // Example 1: Graph with bridges
    cout << "\n1. Graph with Bridges:" << endl;
    Graph g1(6, false);
    g1.addEdge(0, 1);
    g1.addEdge(1, 2);
    g1.addEdge(1, 3);
    g1.addEdge(2, 4);
    g1.addEdge(3, 4);
    g1.addEdge(4, 5);
    
    g1.display();
    g1.displayBridges();
    g1.displayBridgesDetailed();
    g1.displayTwoEdgeComponents();
    g1.displayEdgeConnectivity();
    
    // Example 2: Cycle (no bridges)
    cout << "\n2. Cycle (No Bridges):" << endl;
    Graph g2(5, false);
    g2.addEdge(0, 1);
    g2.addEdge(1, 2);
    g2.addEdge(2, 3);
    g2.addEdge(3, 4);
    g2.addEdge(4, 0);
    
    g2.display();
    g2.displayBridges();
    
    // Example 3: Tree (all edges are bridges)
    cout << "\n3. Tree (All edges are bridges):" << endl;
    Graph g3(6, false);
    g3.addEdge(0, 1);
    g3.addEdge(0, 2);
    g3.addEdge(1, 3);
    g3.addEdge(1, 4);
    g3.addEdge(2, 5);
    
    g3.display();
    g3.displayBridges();
    g3.displayTwoEdgeComponents();
    
    // Example 4: Graph with multiple bridges
    cout << "\n4. Graph with Multiple Bridges:" << endl;
    Graph g4(8, false);
    g4.addEdge(0, 1);
    g4.addEdge(1, 2);
    g4.addEdge(1, 3);
    g4.addEdge(2, 4);
    g4.addEdge(3, 4);
    g4.addEdge(4, 5);
    g4.addEdge(5, 6);
    g4.addEdge(5, 7);
    
    g4.display();
    g4.displayBridges();
    g4.displayTwoEdgeComponents();
    
    // Example 5: Complete graph (no bridges)
    cout << "\n5. Complete Graph K4 (No Bridges):" << endl;
    Graph g5(4, false);
    for (int i = 0; i < 4; i++) {
        for (int j = i + 1; j < 4; j++) {
            g5.addEdge(i, j);
        }
    }
    
    g5.display();
    g5.displayBridges();
    
    // Example 6: Check specific edge
    cout << "\n6. Check Specific Edge:" << endl;
    Graph g6(4, false);
    g6.addEdge(0, 1);
    g6.addEdge(1, 2);
    g6.addEdge(2, 3);
    g6.addEdge(3, 0);
    
    g6.display();
    cout << "Is edge (0,1) a bridge? " << (g6.isBridge(0, 1) ? "Yes" : "No") << endl;
    cout << "Is edge (1,2) a bridge? " << (g6.isBridge(1, 2) ? "Yes" : "No") << endl;
    
    // Example 7: Remove bridges and get components
    cout << "\n7. Components After Bridge Removal:" << endl;
    Graph g7(6, false);
    g7.addEdge(0, 1);
    g7.addEdge(0, 2);
    g7.addEdge(1, 2);
    g7.addEdge(2, 3);
    g7.addEdge(3, 4);
    g7.addEdge(3, 5);
    
    g7.display();
    g7.displayBridges();
    
    auto components = g7.removeBridgesAndGetComponents();
    cout << "\nComponents after removing bridges:" << endl;
    for (size_t i = 0; i < components.size(); i++) {
        cout << "Component " << i + 1 << ": ";
        for (int v : components[i]) cout << v << " ";
        cout << endl;
    }
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Find Bridges** | O(V + E) | O(V) |
| **2-Edge Connected Components** | O(V + E) | O(V + E) |

---

## 🎯 Applications

| Application | Description |
|-------------|-------------|
| **Network Reliability** | Identifying critical connections |
| **Communication Networks** | Finding single points of failure |
| **Transportation** | Critical roads/bridges |
| **Power Grids** | Vulnerable transmission lines |
| **Internet Topology** | Critical backbone links |
| **Social Networks** | Connections whose removal disconnects groups |

---

## ✅ Key Takeaways

1. **Bridges** disconnect graph when removed
2. **DFS** with discovery time and low values
3. **Bridge condition**: low[v] > disc[u]
4. **Tree edges** are always bridges
5. **Cycle edges** are never bridges
6. **2-edge connected components** are maximal subgraphs without bridges

---