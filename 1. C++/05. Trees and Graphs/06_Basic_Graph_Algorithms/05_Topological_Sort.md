# Topological Sort

## 📖 Overview

Topological sort is a linear ordering of vertices in a Directed Acyclic Graph (DAG) such that for every directed edge u → v, vertex u comes before vertex v in the ordering. It is essential for scheduling tasks with dependencies, resolving build dependencies, and course prerequisite planning.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **DAG** | Directed Acyclic Graph (no cycles) |
| **Linear Ordering** | Vertices arranged in sequence |
| **Dependency Order** | Prerequisites come before dependents |
| **Multiple Solutions** | A DAG can have multiple valid topological orders |

---

## 📊 Topological Sort Visualization

### Example DAG
```
5 → 0 ← 4
↓    ↓    ↓
2 → 3 → 1

Valid topological orders:
5, 4, 2, 3, 1, 0
4, 5, 2, 3, 0, 1
5, 2, 4, 3, 0, 1
```

### Dependency Graph Example
```
Course Prerequisites:
CS101 → CS201 → CS301
CS101 → CS202 → CS301
MATH101 → CS201

Topological order: CS101, MATH101, CS201, CS202, CS301
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
using namespace std;

class Graph {
private:
    int vertices;
    vector<list<int>> adj;
    bool isDirected;
    
public:
    Graph(int v, bool directed = true) : vertices(v), isDirected(directed) {
        adj.resize(v);
    }
    
    void addEdge(int u, int v) {
        adj[u].push_back(v);
        if (!isDirected) {
            adj[v].push_back(u);
        }
    }
    
    // ============ DFS-BASED TOPOLOGICAL SORT ============
    void topologicalSortDFS(int v, vector<bool>& visited, stack<int>& stk) {
        visited[v] = true;
        
        for (int neighbor : adj[v]) {
            if (!visited[neighbor]) {
                topologicalSortDFS(neighbor, visited, stk);
            }
        }
        
        stk.push(v);
    }
    
    vector<int> topologicalSortDFS() {
        if (!isDirected) {
            cout << "Topological sort only works on directed graphs!" << endl;
            return {};
        }
        
        vector<bool> visited(vertices, false);
        stack<int> stk;
        
        for (int i = 0; i < vertices; i++) {
            if (!visited[i]) {
                topologicalSortDFS(i, visited, stk);
            }
        }
        
        vector<int> result;
        while (!stk.empty()) {
            result.push_back(stk.top());
            stk.pop();
        }
        
        return result;
    }
    
    // ============ KAHN'S ALGORITHM (BFS-BASED) ============
    vector<int> topologicalSortKahn() {
        if (!isDirected) {
            cout << "Topological sort only works on directed graphs!" << endl;
            return {};
        }
        
        // Calculate indegree for each vertex
        vector<int> indegree(vertices, 0);
        for (int u = 0; u < vertices; u++) {
            for (int v : adj[u]) {
                indegree[v]++;
            }
        }
        
        // Queue for vertices with indegree 0
        queue<int> q;
        for (int i = 0; i < vertices; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }
        
        vector<int> result;
        int count = 0;
        
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            result.push_back(u);
            count++;
            
            for (int v : adj[u]) {
                indegree[v]--;
                if (indegree[v] == 0) {
                    q.push(v);
                }
            }
        }
        
        // Check for cycle
        if (count != vertices) {
            cout << "Graph has a cycle! Topological sort not possible." << endl;
            return {};
        }
        
        return result;
    }
    
    // ============ FIND ALL POSSIBLE TOPOLOGICAL ORDERS ============
    void findAllTopologicalOrdersUtil(vector<bool>& visited, 
                                      vector<int>& indegree, 
                                      vector<int>& order,
                                      vector<vector<int>>& allOrders) {
        bool allVisited = true;
        
        for (int i = 0; i < vertices; i++) {
            if (indegree[i] == 0 && !visited[i]) {
                // Choose this vertex
                visited[i] = true;
                order.push_back(i);
                
                // Reduce indegree of neighbors
                for (int v : adj[i]) {
                    indegree[v]--;
                }
                
                // Recurse
                findAllTopologicalOrdersUtil(visited, indegree, order, allOrders);
                
                // Backtrack
                visited[i] = false;
                order.pop_back();
                for (int v : adj[i]) {
                    indegree[v]++;
                }
                
                allVisited = false;
            }
        }
        
        if (allVisited) {
            allOrders.push_back(order);
        }
    }
    
    vector<vector<int>> findAllTopologicalOrders() {
        if (!isDirected) {
            cout << "Topological sort only works on directed graphs!" << endl;
            return {};
        }
        
        vector<int> indegree(vertices, 0);
        for (int u = 0; u < vertices; u++) {
            for (int v : adj[u]) {
                indegree[v]++;
            }
        }
        
        vector<bool> visited(vertices, false);
        vector<int> order;
        vector<vector<int>> allOrders;
        
        findAllTopologicalOrdersUtil(visited, indegree, order, allOrders);
        
        return allOrders;
    }
    
    // ============ TOPOLOGICAL SORT WITH LEVELS ============
    vector<vector<int>> topologicalSortWithLevels() {
        if (!isDirected) {
            cout << "Topological sort only works on directed graphs!" << endl;
            return {};
        }
        
        vector<int> indegree(vertices, 0);
        for (int u = 0; u < vertices; u++) {
            for (int v : adj[u]) {
                indegree[v]++;
            }
        }
        
        queue<int> q;
        for (int i = 0; i < vertices; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }
        
        vector<vector<int>> levels;
        int level = 0;
        
        while (!q.empty()) {
            int levelSize = q.size();
            vector<int> currentLevel;
            
            for (int i = 0; i < levelSize; i++) {
                int u = q.front();
                q.pop();
                currentLevel.push_back(u);
                
                for (int v : adj[u]) {
                    indegree[v]--;
                    if (indegree[v] == 0) {
                        q.push(v);
                    }
                }
            }
            
            levels.push_back(currentLevel);
            level++;
        }
        
        return levels;
    }
    
    // ============ CRITICAL PATH METHOD (LONGEST PATH) ============
    vector<int> criticalPath() {
        if (!isDirected) {
            cout << "Critical path only works on directed graphs!" << endl;
            return {};
        }
        
        // First get topological order
        vector<int> topOrder = topologicalSortKahn();
        if (topOrder.empty()) return {};
        
        // Calculate earliest start times
        vector<int> earliest(vertices, 0);
        for (int u : topOrder) {
            for (int v : adj[u]) {
                earliest[v] = max(earliest[v], earliest[u] + 1);
            }
        }
        
        // Calculate latest start times
        vector<int> latest(vertices, earliest[topOrder.back()]);
        reverse(topOrder.begin(), topOrder.end());
        
        for (int u : topOrder) {
            for (int v : adj[u]) {
                latest[u] = min(latest[u], latest[v] - 1);
            }
        }
        
        // Find critical path (where earliest == latest)
        vector<int> critical;
        for (int i = 0; i < vertices; i++) {
            if (earliest[i] == latest[i]) {
                critical.push_back(i);
            }
        }
        
        return critical;
    }
    
    // ============ CHECK IF GRAPH IS DAG ============
    bool isDAG() {
        if (!isDirected) return false;
        
        vector<int> indegree(vertices, 0);
        for (int u = 0; u < vertices; u++) {
            for (int v : adj[u]) {
                indegree[v]++;
            }
        }
        
        queue<int> q;
        for (int i = 0; i < vertices; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }
        
        int count = 0;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            count++;
            
            for (int v : adj[u]) {
                indegree[v]--;
                if (indegree[v] == 0) {
                    q.push(v);
                }
            }
        }
        
        return count == vertices;
    }
    
    // ============ GET DEPENDENCY ORDER FOR SPECIFIC NODE ============
    vector<int> getDependencyOrder(int target) {
        if (!isDirected) {
            cout << "Dependency order only works on directed graphs!" << endl;
            return {};
        }
        
        vector<bool> visited(vertices, false);
        stack<int> stk;
        
        // DFS to find all prerequisites
        function<void(int)> dfs = [&](int v) {
            visited[v] = true;
            for (int neighbor : adj[v]) {
                if (!visited[neighbor]) {
                    dfs(neighbor);
                }
            }
            stk.push(v);
        };
        
        dfs(target);
        
        vector<int> order;
        while (!stk.empty()) {
            order.push_back(stk.top());
            stk.pop();
        }
        
        return order;
    }
    
    // ============ DISPLAY FUNCTIONS ============
    void displayTopologicalSort(const vector<int>& order) {
        if (order.empty()) return;
        
        cout << "Topological Sort: ";
        for (int v : order) {
            cout << v << " ";
        }
        cout << endl;
    }
    
    void displayAllOrders(const vector<vector<int>>& orders) {
        if (orders.empty()) {
            cout << "No topological orders found (graph may have cycles)." << endl;
            return;
        }
        
        cout << "\nAll Topological Orders (" << orders.size() << "):" << endl;
        for (size_t i = 0; i < min(orders.size(), (size_t)10); i++) {
            cout << "  Order " << i + 1 << ": ";
            for (int v : orders[i]) cout << v << " ";
            cout << endl;
        }
        if (orders.size() > 10) {
            cout << "  ... and " << orders.size() - 10 << " more" << endl;
        }
    }
    
    void displayLevels(const vector<vector<int>>& levels) {
        cout << "\nTopological Sort with Levels:" << endl;
        for (size_t i = 0; i < levels.size(); i++) {
            cout << "Level " << i << ": ";
            for (int v : levels[i]) cout << v << " ";
            cout << endl;
        }
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
    cout << "=== Topological Sort Demo ===" << endl;
    
    // Create DAG for course prerequisites
    cout << "\n1. Course Prerequisites DAG:" << endl;
    Graph g1(6, true);
    g1.addEdge(0, 1);  // CS101 → CS201
    g1.addEdge(0, 2);  // CS101 → CS202
    g1.addEdge(1, 3);  // CS201 → CS301
    g1.addEdge(2, 3);  // CS202 → CS301
    g1.addEdge(4, 1);  // MATH101 → CS201
    
    g1.display();
    
    cout << "\nIs DAG? " << (g1.isDAG() ? "Yes" : "No") << endl;
    
    cout << "\n--- DFS-based Topological Sort ---" << endl;
    vector<int> dfsOrder = g1.topologicalSortDFS();
    g1.displayTopologicalSort(dfsOrder);
    
    cout << "\n--- Kahn's Algorithm (BFS-based) ---" << endl;
    vector<int> kahnOrder = g1.topologicalSortKahn();
    g1.displayTopologicalSort(kahnOrder);
    
    cout << "\n--- Topological Sort with Levels ---" << endl;
    vector<vector<int>> levels = g1.topologicalSortWithLevels();
    g1.displayLevels(levels);
    
    cout << "\n--- All Possible Topological Orders ---" << endl;
    vector<vector<int>> allOrders = g1.findAllTopologicalOrders();
    g1.displayAllOrders(allOrders);
    
    // Build system example
    cout << "\n2. Build System DAG:" << endl;
    Graph g2(7, true);
    g2.addEdge(0, 1);  // libA → libB
    g2.addEdge(0, 2);  // libA → libC
    g2.addEdge(1, 3);  // libB → appX
    g2.addEdge(2, 3);  // libC → appX
    g2.addEdge(2, 4);  // libC → appY
    g2.addEdge(5, 1);  // util → libB
    g2.addEdge(5, 2);  // util → libC
    
    g2.display();
    
    vector<int> buildOrder = g2.topologicalSortKahn();
    g2.displayTopologicalSort(buildOrder);
    
    // Critical path
    cout << "\n--- Critical Path ---" << endl;
    vector<int> critical = g2.criticalPath();
    cout << "Critical path nodes: ";
    for (int v : critical) cout << v << " ";
    cout << endl;
    
    // Dependency order for specific node
    cout << "\n--- Dependency Order for appX (node 3) ---" << endl;
    vector<int> deps = g2.getDependencyOrder(3);
    cout << "Prerequisites for appX: ";
    for (int v : deps) cout << v << " ";
    cout << endl;
    
    // Graph with cycle
    cout << "\n3. Graph with Cycle (Not a DAG):" << endl;
    Graph g3(4, true);
    g3.addEdge(0, 1);
    g3.addEdge(1, 2);
    g3.addEdge(2, 3);
    g3.addEdge(3, 1);  // Creates cycle
    
    g3.display();
    cout << "Is DAG? " << (g3.isDAG() ? "Yes" : "No") << endl;
    
    vector<int> cycleOrder = g3.topologicalSortKahn();
    if (cycleOrder.empty()) {
        cout << "Topological sort not possible due to cycle!" << endl;
    }
    
    // Task scheduling example
    cout << "\n4. Task Scheduling Example:" << endl;
    Graph g4(8, true);
    g4.addEdge(0, 3);  // Task 0 must be before Task 3
    g4.addEdge(0, 4);
    g4.addEdge(1, 4);
    g4.addEdge(2, 5);
    g4.addEdge(3, 6);
    g4.addEdge(4, 6);
    g4.addEdge(5, 7);
    g4.addEdge(6, 7);
    
    g4.display();
    
    vector<int> taskOrder = g4.topologicalSortKahn();
    g4.displayTopologicalSort(taskOrder);
    
    vector<vector<int>> taskLevels = g4.topologicalSortWithLevels();
    g4.displayLevels(taskLevels);
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **DFS-based** | O(V + E) | O(V) |
| **Kahn's Algorithm** | O(V + E) | O(V) |
| **Find All Orders** | O(V! × V) in worst case | O(V) |

---

## 🎯 Applications of Topological Sort

| Application | Description |
|-------------|-------------|
| **Build Systems** | Determining compilation order (make, gradle) |
| **Course Prerequisites** | Planning course sequences |
| **Task Scheduling** | Ordering dependent tasks |
| **Deadlock Detection** | Finding circular dependencies |
| **Data Processing Pipelines** | Ordering ETL jobs |
| **Compiler Design** | Instruction scheduling |
| **Package Managers** | Resolving dependencies (apt, npm) |
| **Project Management** | Critical path analysis |

---

## ✅ Key Takeaways

1. **Topological sort** only works on DAGs (Directed Acyclic Graphs)
2. **DFS-based method** uses stack to record finishing times
3. **Kahn's algorithm** uses indegree counting and queue
4. **Multiple valid orders** may exist for a DAG
5. **Levels** represent parallelizable tasks
6. **Critical path** identifies longest dependency chain
7. **Cycle detection** is essential before topological sort

---
---

## Next Step

- Go to [Problem Solving](/1.%20C++/06.%20Problem%20Solving/README.md) to continue.
