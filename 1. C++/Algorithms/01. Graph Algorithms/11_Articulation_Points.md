# Graph Algorithm - Articulation Points (Cut Vertices)

## 📖 Overview

Articulation points (or cut vertices) are vertices in a graph whose removal increases the number of connected components. They represent critical points whose failure would disconnect the graph. Finding articulation points is crucial for network reliability, communication systems, and identifying vulnerabilities.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Articulation Point** | Vertex whose removal disconnects the graph |
| **Cut Vertex** | Another name for articulation point |
| **DFS Tree** | Tree formed by DFS traversal |
| **Discovery Time** | Time when vertex is first visited |
| **Low Value** | Earliest visited vertex reachable from subtree |
| **Root Rule** | Root is articulation point if it has >1 child |

---

## 📊 Articulation Points Visualization

```
Graph with articulation points:

    0 --- 1 --- 3 --- 4
    |     |     |
    |     |     |
    2 --- 5     6

Articulation Points: 1, 3

Why?
- Vertex 1 removal disconnects {0,2,5} from {3,4,6}
- Vertex 3 removal disconnects {4,6} from {0,1,2,5}
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
    
    // ============ FIND ARTICULATION POINTS ============
    vector<int> findArticulationPoints() {
        vector<bool> visited(vertices, false);
        vector<int> disc(vertices, -1);  // Discovery time
        vector<int> low(vertices, -1);   // Low value
        vector<int> parent(vertices, -1);
        vector<bool> isArticulation(vertices, false);
        
        int time = 0;
        
        for (int i = 0; i < vertices; i++) {
            if (!visited[i]) {
                dfsArticulation(i, visited, disc, low, parent, isArticulation, time);
            }
        }
        
        vector<int> articulationPoints;
        for (int i = 0; i < vertices; i++) {
            if (isArticulation[i]) {
                articulationPoints.push_back(i);
            }
        }
        
        return articulationPoints;
    }
    
private:
    void dfsArticulation(int u, vector<bool>& visited, vector<int>& disc,
                         vector<int>& low, vector<int>& parent,
                         vector<bool>& isArticulation, int& time) {
        visited[u] = true;
        disc[u] = low[u] = ++time;
        int children = 0;
        
        for (int v : adj[u]) {
            if (!visited[v]) {
                children++;
                parent[v] = u;
                dfsArticulation(v, visited, disc, low, parent, isArticulation, time);
                
                low[u] = min(low[u], low[v]);
                
                // u is articulation point if:
                // 1. u is root and has >= 2 children
                // 2. u is not root and low[v] >= disc[u]
                if (parent[u] == -1 && children > 1) {
                    isArticulation[u] = true;
                }
                if (parent[u] != -1 && low[v] >= disc[u]) {
                    isArticulation[u] = true;
                }
            } else if (v != parent[u]) {
                low[u] = min(low[u], disc[v]);
            }
        }
    }
    
public:
    // ============ FIND ARTICULATION POINTS WITH DETAILS ============
    struct ArticulationInfo {
        int vertex;
        int discoveryTime;
        int lowValue;
        vector<int> children;
    };
    
    vector<ArticulationInfo> getArticulationPointsDetailed() {
        vector<bool> visited(vertices, false);
        vector<int> disc(vertices, -1);
        vector<int> low(vertices, -1);
        vector<int> parent(vertices, -1);
        vector<bool> isArticulation(vertices, false);
        vector<vector<int>> children(vertices);
        
        int time = 0;
        
        for (int i = 0; i < vertices; i++) {
            if (!visited[i]) {
                dfsArticulationDetailed(i, visited, disc, low, parent, 
                                        isArticulation, children, time);
            }
        }
        
        vector<ArticulationInfo> result;
        for (int i = 0; i < vertices; i++) {
            if (isArticulation[i]) {
                result.push_back({i, disc[i], low[i], children[i]});
            }
        }
        
        return result;
    }
    
private:
    void dfsArticulationDetailed(int u, vector<bool>& visited, vector<int>& disc,
                                 vector<int>& low, vector<int>& parent,
                                 vector<bool>& isArticulation,
                                 vector<vector<int>>& children, int& time) {
        visited[u] = true;
        disc[u] = low[u] = ++time;
        int childCount = 0;
        
        for (int v : adj[u]) {
            if (!visited[v]) {
                childCount++;
                parent[v] = u;
                children[u].push_back(v);
                dfsArticulationDetailed(v, visited, disc, low, parent,
                                        isArticulation, children, time);
                
                low[u] = min(low[u], low[v]);
                
                if (parent[u] == -1 && childCount > 1) {
                    isArticulation[u] = true;
                }
                if (parent[u] != -1 && low[v] >= disc[u]) {
                    isArticulation[u] = true;
                }
            } else if (v != parent[u]) {
                low[u] = min(low[u], disc[v]);
            }
        }
    }
    
public:
    // ============ CHECK IF VERTEX IS ARTICULATION POINT ============
    bool isArticulationPoint(int vertex) {
        vector<int> articulationPoints = findArticulationPoints();
        return find(articulationPoints.begin(), articulationPoints.end(), vertex) 
               != articulationPoints.end();
    }
    
    // ============ FIND BICONNECTED COMPONENTS ============
    struct Edge {
        int u, v;
        Edge(int u, int v) : u(u), v(v) {}
    };
    
    vector<vector<Edge>> findBiconnectedComponents() {
        vector<bool> visited(vertices, false);
        vector<int> disc(vertices, -1);
        vector<int> low(vertices, -1);
        vector<int> parent(vertices, -1);
        vector<vector<Edge>> components;
        vector<Edge> stack;
        
        int time = 0;
        
        for (int i = 0; i < vertices; i++) {
            if (!visited[i]) {
                dfsBiconnected(i, visited, disc, low, parent, stack, components, time);
            }
        }
        
        return components;
    }
    
private:
    void dfsBiconnected(int u, vector<bool>& visited, vector<int>& disc,
                        vector<int>& low, vector<int>& parent,
                        vector<Edge>& stack, vector<vector<Edge>>& components,
                        int& time) {
        visited[u] = true;
        disc[u] = low[u] = ++time;
        int children = 0;
        
        for (int v : adj[u]) {
            if (!visited[v]) {
                children++;
                parent[v] = u;
                stack.push_back(Edge(u, v));
                dfsBiconnected(v, visited, disc, low, parent, stack, components, time);
                
                low[u] = min(low[u], low[v]);
                
                if ((parent[u] == -1 && children > 1) || 
                    (parent[u] != -1 && low[v] >= disc[u])) {
                    vector<Edge> component;
                    while (stack.back().u != u || stack.back().v != v) {
                        component.push_back(stack.back());
                        stack.pop_back();
                    }
                    component.push_back(stack.back());
                    stack.pop_back();
                    components.push_back(component);
                }
            } else if (v != parent[u] && disc[v] < disc[u]) {
                low[u] = min(low[u], disc[v]);
                stack.push_back(Edge(u, v));
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
    
    void displayArticulationPoints() {
        vector<int> articulationPoints = findArticulationPoints();
        
        cout << "\nArticulation Points (" << articulationPoints.size() << "): ";
        if (articulationPoints.empty()) {
            cout << "None" << endl;
        } else {
            for (int v : articulationPoints) {
                cout << v << " ";
            }
            cout << endl;
        }
    }
    
    void displayArticulationPointsDetailed() {
        vector<ArticulationInfo> info = getArticulationPointsDetailed();
        
        if (info.empty()) {
            cout << "\nNo articulation points found." << endl;
            return;
        }
        
        cout << "\nArticulation Points Details:\n";
        cout << "Vertex\tDisc\tLow\tChildren\n";
        cout << "------\t----\t---\t--------\n";
        for (auto& ap : info) {
            cout << ap.vertex << "\t" << ap.discoveryTime << "\t" 
                 << ap.lowValue << "\t";
            for (int child : ap.children) {
                cout << child << " ";
            }
            cout << endl;
        }
    }
    
    void displayBiconnectedComponents() {
        vector<vector<Edge>> components = findBiconnectedComponents();
        
        cout << "\nBiconnected Components (" << components.size() << "):\n";
        for (size_t i = 0; i < components.size(); i++) {
            cout << "Component " << i + 1 << ": ";
            for (const Edge& e : components[i]) {
                cout << "(" << e.u << "," << e.v << ") ";
            }
            cout << endl;
        }
    }
};

int main() {
    cout << "=== Articulation Points Demo ===" << endl;
    
    // Example 1: Graph with articulation points
    cout << "\n1. Graph with Articulation Points:" << endl;
    Graph g1(7, false);
    g1.addEdge(0, 1);
    g1.addEdge(1, 2);
    g1.addEdge(1, 3);
    g1.addEdge(2, 5);
    g1.addEdge(3, 4);
    g1.addEdge(3, 5);
    g1.addEdge(4, 6);
    g1.addEdge(5, 6);
    
    g1.display();
    g1.displayArticulationPoints();
    g1.displayArticulationPointsDetailed();
    g1.displayBiconnectedComponents();
    
    // Example 2: Tree (all internal nodes are articulation points)
    cout << "\n2. Tree (Internal nodes are articulation points):" << endl;
    Graph g2(6, false);
    g2.addEdge(0, 1);
    g2.addEdge(0, 2);
    g2.addEdge(1, 3);
    g2.addEdge(1, 4);
    g2.addEdge(2, 5);
    
    g2.display();
    g2.displayArticulationPoints();
    
    // Example 3: Cycle (no articulation points)
    cout << "\n3. Cycle (No articulation points):" << endl;
    Graph g3(5, false);
    g3.addEdge(0, 1);
    g3.addEdge(1, 2);
    g3.addEdge(2, 3);
    g3.addEdge(3, 4);
    g3.addEdge(4, 0);
    
    g3.display();
    g3.displayArticulationPoints();
    
    // Example 4: Complete graph (no articulation points)
    cout << "\n4. Complete Graph K4 (No articulation points):" << endl;
    Graph g4(4, false);
    for (int i = 0; i < 4; i++) {
        for (int j = i + 1; j < 4; j++) {
            g4.addEdge(i, j);
        }
    }
    
    g4.display();
    g4.displayArticulationPoints();
    
    // Example 5: Graph with multiple articulation points
    cout << "\n5. Graph with Multiple Articulation Points:" << endl;
    Graph g5(9, false);
    g5.addEdge(0, 1);
    g5.addEdge(1, 2);
    g5.addEdge(2, 3);
    g5.addEdge(2, 4);
    g5.addEdge(3, 5);
    g5.addEdge(4, 5);
    g5.addEdge(5, 6);
    g5.addEdge(6, 7);
    g5.addEdge(6, 8);
    
    g5.display();
    g5.displayArticulationPoints();
    
    // Check specific vertex
    cout << "\nIs vertex 2 an articulation point? " 
         << (g5.isArticulationPoint(2) ? "Yes" : "No") << endl;
    cout << "Is vertex 5 an articulation point? " 
         << (g5.isArticulationPoint(5) ? "Yes" : "No") << endl;
    cout << "Is vertex 0 an articulation point? " 
         << (g5.isArticulationPoint(0) ? "Yes" : "No") << endl;
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Articulation Points** | O(V + E) | O(V) |
| **Biconnected Components** | O(V + E) | O(V + E) |

---

## 🎯 Applications

| Application | Description |
|-------------|-------------|
| **Network Reliability** | Identifying critical routers/servers |
| **Communication Networks** | Finding single points of failure |
| **Social Networks** | Key influencers whose removal disconnects network |
| **Transportation** | Critical intersections/bridges |
| **Power Grids** | Vulnerable substations |
| **Internet Topology** | Critical backbone routers |

---

## ✅ Key Takeaways

1. **Articulation points** disconnect graph when removed
2. **DFS** with discovery time and low values
3. **Root rule**: root is articulation if it has >1 child
4. **Non-root rule**: articulation if low[child] >= disc[u]
5. **Biconnected components** are maximal 2-connected subgraphs

---