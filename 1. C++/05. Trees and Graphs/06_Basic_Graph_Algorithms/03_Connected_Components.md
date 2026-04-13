# Connected Components in Graph

## 📖 Overview

Connected components are maximal sets of vertices in an undirected graph where each vertex can reach every other vertex in the same set via some path. Finding connected components is fundamental to understanding graph structure and is used in network analysis, image processing, and social network clustering.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Connected Component** | Maximal set of mutually reachable vertices |
| **Disconnected Graph** | Graph with more than one component |
| **Spanning Component** | Each component is a connected subgraph |
| **Component Count** | Number of isolated groups in graph |

---

## 📊 Connected Components Visualization

### Example Graph
```
Component 1:           Component 2:
    0 --- 1             4 --- 5
    |     |                  |
    |     |                  |
    3 --- 2                  6

Component 1: {0,1,2,3}
Component 2: {4,5,6}
```

### Graph Representation
```
Graph with 3 components:
Component 1: 0-1-2-3
Component 2: 4-5
Component 3: 6 (isolated)
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
#include <map>
#include <set>
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
    
    // ============ DFS BASED CONNECTED COMPONENTS ============
    void dfsComponent(int v, vector<bool>& visited, vector<int>& component) {
        visited[v] = true;
        component.push_back(v);
        
        for (int neighbor : adj[v]) {
            if (!visited[neighbor]) {
                dfsComponent(neighbor, visited, component);
            }
        }
    }
    
    vector<vector<int>> findConnectedComponentsDFS() {
        vector<bool> visited(vertices, false);
        vector<vector<int>> components;
        
        for (int i = 0; i < vertices; i++) {
            if (!visited[i]) {
                vector<int> component;
                dfsComponent(i, visited, component);
                components.push_back(component);
            }
        }
        
        return components;
    }
    
    // ============ BFS BASED CONNECTED COMPONENTS ============
    void bfsComponent(int start, vector<bool>& visited, vector<int>& component) {
        queue<int> q;
        visited[start] = true;
        q.push(start);
        
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            component.push_back(v);
            
            for (int neighbor : adj[v]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }
    }
    
    vector<vector<int>> findConnectedComponentsBFS() {
        vector<bool> visited(vertices, false);
        vector<vector<int>> components;
        
        for (int i = 0; i < vertices; i++) {
            if (!visited[i]) {
                vector<int> component;
                bfsComponent(i, visited, component);
                components.push_back(component);
            }
        }
        
        return components;
    }
    
    // ============ UNION-FIND BASED CONNECTED COMPONENTS ============
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
        
        void unite(int x, int y) {
            int rx = find(x), ry = find(y);
            if (rx != ry) {
                if (rank[rx] < rank[ry]) {
                    parent[rx] = ry;
                } else if (rank[rx] > rank[ry]) {
                    parent[ry] = rx;
                } else {
                    parent[ry] = rx;
                    rank[rx]++;
                }
            }
        }
        
        bool connected(int x, int y) {
            return find(x) == find(y);
        }
    };
    
    vector<vector<int>> findConnectedComponentsUnionFind() {
        UnionFind uf(vertices);
        
        // Union all edges
        for (int u = 0; u < vertices; u++) {
            for (int v : adj[u]) {
                if (u < v || isDirected) {  // Avoid double counting for undirected
                    uf.unite(u, v);
                }
            }
        }
        
        // Group vertices by their root
        map<int, vector<int>> components;
        for (int i = 0; i < vertices; i++) {
            components[uf.find(i)].push_back(i);
        }
        
        vector<vector<int>> result;
        for (auto& [root, comp] : components) {
            result.push_back(comp);
        }
        
        return result;
    }
    
    // ============ COMPONENT STATISTICS ============
    struct ComponentStats {
        int size;
        int edges;
        double density;
        bool isComplete;
        bool isTree;
        int diameter;
    };
    
    ComponentStats analyzeComponent(const vector<int>& component) {
        ComponentStats stats;
        stats.size = component.size();
        stats.edges = 0;
        
        // Create a set for quick lookup
        set<int> compSet(component.begin(), component.end());
        
        // Count edges within component
        for (int u : component) {
            for (int v : adj[u]) {
                if (compSet.count(v) && (u < v || isDirected)) {
                    stats.edges++;
                }
            }
        }
        
        // Calculate density
        int maxEdges = stats.size * (stats.size - 1);
        if (!isDirected) maxEdges /= 2;
        stats.density = (maxEdges > 0) ? (double)stats.edges / maxEdges : 0;
        
        // Check if complete
        stats.isComplete = (stats.edges == maxEdges);
        
        // Check if tree (connected acyclic graph)
        stats.isTree = (stats.edges == stats.size - 1);
        
        // Calculate diameter (longest shortest path)
        stats.diameter = calculateDiameter(component);
        
        return stats;
    }
    
    int calculateDiameter(const vector<int>& component) {
        if (component.size() <= 1) return 0;
        
        // Find farthest node from arbitrary node (component[0])
        int farthest = bfsFarthest(component[0], component);
        
        // Find farthest from that node
        int diameter = bfsFarthest(farthest, component, true);
        
        return diameter;
    }
    
private:
    int bfsFarthest(int start, const vector<int>& component, bool returnDist = false) {
        set<int> compSet(component.begin(), component.end());
        map<int, int> dist;
        queue<int> q;
        
        dist[start] = 0;
        q.push(start);
        
        int farthest = start;
        int maxDist = 0;
        
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            
            for (int neighbor : adj[v]) {
                if (compSet.count(neighbor) && dist.find(neighbor) == dist.end()) {
                    dist[neighbor] = dist[v] + 1;
                    q.push(neighbor);
                    
                    if (dist[neighbor] > maxDist) {
                        maxDist = dist[neighbor];
                        farthest = neighbor;
                    }
                }
            }
        }
        
        return returnDist ? maxDist : farthest;
    }
    
public:
    // ============ DISPLAY FUNCTIONS ============
    void displayComponents(const vector<vector<int>>& components) {
        cout << "\nConnected Components (" << components.size() << "):" << endl;
        for (size_t i = 0; i < components.size(); i++) {
            cout << "Component " << i + 1 << " (size=" << components[i].size() << "): ";
            for (int v : components[i]) {
                cout << v << " ";
            }
            cout << endl;
            
            // Show component statistics
            ComponentStats stats = analyzeComponent(components[i]);
            cout << "  Edges: " << stats.edges;
            if (!isDirected) cout << ", Density: " << stats.density;
            cout << ", Diameter: " << stats.diameter;
            if (stats.isComplete) cout << ", Complete";
            if (stats.isTree) cout << ", Tree";
            cout << endl;
        }
    }
    
    void printComponentInfo() {
        vector<vector<int>> components = findConnectedComponentsDFS();
        displayComponents(components);
    }
    
    // ============ CHECK IF GRAPH IS CONNECTED ============
    bool isConnected() {
        vector<vector<int>> components = findConnectedComponentsDFS();
        return components.size() == 1;
    }
    
    // ============ GET LARGEST COMPONENT ============
    vector<int> getLargestComponent() {
        vector<vector<int>> components = findConnectedComponentsDFS();
        if (components.empty()) return {};
        
        auto largest = max_element(components.begin(), components.end(),
            [](const vector<int>& a, const vector<int>& b) {
                return a.size() < b.size();
            });
        
        return *largest;
    }
    
    // ============ GET SMALLEST COMPONENT ============
    vector<int> getSmallestComponent() {
        vector<vector<int>> components = findConnectedComponentsDFS();
        if (components.empty()) return {};
        
        auto smallest = min_element(components.begin(), components.end(),
            [](const vector<int>& a, const vector<int>& b) {
                return a.size() < b.size();
            });
        
        return *smallest;
    }
    
    // ============ CHECK IF TWO VERTICES ARE IN SAME COMPONENT ============
    bool areConnected(int u, int v) {
        vector<bool> visited(vertices, false);
        queue<int> q;
        
        visited[u] = true;
        q.push(u);
        
        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            
            if (curr == v) return true;
            
            for (int neighbor : adj[curr]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }
        
        return false;
    }
    
    // ============ GET COMPONENT ID FOR EACH VERTEX ============
    vector<int> getComponentIds() {
        vector<int> componentId(vertices, -1);
        vector<vector<int>> components = findConnectedComponentsDFS();
        
        for (size_t i = 0; i < components.size(); i++) {
            for (int v : components[i]) {
                componentId[v] = i;
            }
        }
        
        return componentId;
    }
    
    // ============ DISPLAY GRAPH ============
    void display() {
        cout << "\nGraph Adjacency List:" << endl;
        for (int i = 0; i < vertices; i++) {
            cout << i << ": ";
            for (int neighbor : adj[i]) {
                cout << neighbor << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    cout << "=== Connected Components Demo ===" << endl;
    
    // Graph with multiple components
    cout << "\n1. Graph with 3 Components:" << endl;
    Graph g1(7, false);
    g1.addEdge(0, 1);
    g1.addEdge(1, 2);
    g1.addEdge(2, 0);
    g1.addEdge(3, 4);
    g1.addEdge(5, 6);
    
    g1.display();
    
    cout << "\n--- DFS Based Components ---" << endl;
    auto compDFS = g1.findConnectedComponentsDFS();
    g1.displayComponents(compDFS);
    
    cout << "\n--- BFS Based Components ---" << endl;
    auto compBFS = g1.findConnectedComponentsBFS();
    g1.displayComponents(compBFS);
    
    cout << "\n--- Union-Find Based Components ---" << endl;
    auto compUF = g1.findConnectedComponentsUnionFind();
    g1.displayComponents(compUF);
    
    cout << "\nIs graph connected? " << (g1.isConnected() ? "Yes" : "No") << endl;
    
    // Connected graph
    cout << "\n2. Connected Graph:" << endl;
    Graph g2(5, false);
    g2.addEdge(0, 1);
    g2.addEdge(1, 2);
    g2.addEdge(2, 3);
    g2.addEdge(3, 4);
    g2.addEdge(4, 0);
    
    g2.display();
    cout << "\nConnected Components:" << endl;
    g2.printComponentInfo();
    cout << "Is graph connected? " << (g2.isConnected() ? "Yes" : "No") << endl;
    
    // Complete graph
    cout << "\n3. Complete Graph (K4):" << endl;
    Graph g3(4, false);
    g3.addEdge(0, 1);
    g3.addEdge(0, 2);
    g3.addEdge(0, 3);
    g3.addEdge(1, 2);
    g3.addEdge(1, 3);
    g3.addEdge(2, 3);
    
    g3.display();
    g3.printComponentInfo();
    
    // Tree structure
    cout << "\n4. Tree Structure:" << endl;
    Graph g4(6, false);
    g4.addEdge(0, 1);
    g4.addEdge(0, 2);
    g4.addEdge(1, 3);
    g4.addEdge(1, 4);
    g4.addEdge(2, 5);
    
    g4.display();
    g4.printComponentInfo();
    
    // Component IDs
    cout << "\n5. Component IDs:" << endl;
    Graph g5(6, false);
    g5.addEdge(0, 1);
    g5.addEdge(0, 2);
    g5.addEdge(3, 4);
    
    g5.display();
    vector<int> compIds = g5.getComponentIds();
    cout << "Component IDs: ";
    for (int i = 0; i < 6; i++) {
        cout << i << ":" << compIds[i] << " ";
    }
    cout << endl;
    
    // Largest and smallest components
    vector<int> largest = g5.getLargestComponent();
    vector<int> smallest = g5.getSmallestComponent();
    cout << "Largest component: ";
    for (int v : largest) cout << v << " ";
    cout << "(size=" << largest.size() << ")" << endl;
    
    cout << "Smallest component: ";
    for (int v : smallest) cout << v << " ";
    cout << "(size=" << smallest.size() << ")" << endl;
    
    // Check connectivity between vertices
    cout << "\nAre 0 and 2 connected? " << (g5.areConnected(0, 2) ? "Yes" : "No") << endl;
    cout << "Are 0 and 3 connected? " << (g5.areConnected(0, 3) ? "Yes" : "No") << endl;
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Method | Time Complexity | Space Complexity |
|--------|----------------|------------------|
| **DFS-based** | O(V + E) | O(V) |
| **BFS-based** | O(V + E) | O(V) |
| **Union-Find** | O(E × α(V)) | O(V) |

Where α(V) is the inverse Ackermann function (practically constant)

---

## 🎯 Applications of Connected Components

| Application | Description |
|-------------|-------------|
| **Network Analysis** | Finding isolated network segments |
| **Image Processing** | Connected component labeling |
| **Social Networks** | Finding friend groups |
| **Graph Clustering** | Identifying natural clusters |
| **Circuit Analysis** | Finding connected circuit components |
| **Document Clustering** | Grouping related documents |
| **Image Segmentation** | Separating objects in images |
| **Game Development** | Connected regions in game maps |

---

## ✅ Key Takeaways

1. **Connected components** are maximal sets of reachable vertices
2. **DFS and BFS** both work for finding components
3. **Union-Find** provides near-constant time operations
4. **Component statistics** reveal graph properties
5. **Diameter** is the longest shortest path in a component
6. **Complete components** have all possible edges
7. **Tree components** have V-1 edges and are acyclic

---
---

## Next Step

- Go to [04_Cycle_Detection.md](04_Cycle_Detection.md) to continue with Cycle Detection.
