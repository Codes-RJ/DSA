# Graph Traversal - DFS (Depth-First Search) - Complete Guide

## 📖 Overview

Depth-First Search (DFS) is a fundamental graph traversal algorithm that explores as far as possible along each branch before backtracking. It uses a stack (either explicitly or via recursion) to keep track of vertices to visit. DFS is essential for many graph algorithms including topological sorting, cycle detection, and finding connected components.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Stack-based** | Uses LIFO (Last In, First Out) principle |
| **Recursive/Iterative** | Can be implemented both ways |
| **Discovery Time** | When node is first visited |
| **Finish Time** | When all descendants are processed |
| **Parent Array** | Tracks the parent of each node |
| **Visited Tracking** | Essential to avoid cycles |

---

## 📊 DFS Traversal Visualization

### Example Graph
```
    0 --- 1
    |     |
    |     |
    3 --- 2
    
    Adjacency List:
    0: 1, 3
    1: 0, 2
    2: 1, 3
    3: 0, 2
```

### DFS Order (Starting from 0)
```
Order: 0 → 1 → 2 → 3

Step-by-step:
Step 1: Visit 0
Step 2: Go to neighbor 1 (unvisited)
Step 3: From 1, go to neighbor 2 (unvisited)
Step 4: From 2, go to neighbor 3 (unvisited)
Step 5: Backtrack when no unvisited neighbors
```

---

## 📝 Complete DFS Implementation

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <stack>
#include <algorithm>
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
    
    // ============ RECURSIVE DFS ============
    void dfsRecursiveUtil(int v, vector<bool>& visited, vector<int>& order) {
        visited[v] = true;
        order.push_back(v);
        
        // Sort neighbors for consistent output
        vector<int> neighbors(adj[v].begin(), adj[v].end());
        sort(neighbors.begin(), neighbors.end());
        
        for (int neighbor : neighbors) {
            if (!visited[neighbor]) {
                dfsRecursiveUtil(neighbor, visited, order);
            }
        }
    }
    
    void dfsRecursive(int start) {
        vector<bool> visited(vertices, false);
        vector<int> order;
        dfsRecursiveUtil(start, visited, order);
        
        cout << "DFS Recursive from " << start << ": ";
        for (int v : order) cout << v << " ";
        cout << endl;
    }
    
    // ============ ITERATIVE DFS (USING STACK) ============
    void dfsIterative(int start) {
        vector<bool> visited(vertices, false);
        vector<int> order;
        stack<int> stk;
        
        stk.push(start);
        
        while (!stk.empty()) {
            int v = stk.top();
            stk.pop();
            
            if (!visited[v]) {
                visited[v] = true;
                order.push_back(v);
                
                // Sort neighbors in reverse order for consistent output
                vector<int> neighbors(adj[v].begin(), adj[v].end());
                sort(neighbors.rbegin(), neighbors.rend());
                
                for (int neighbor : neighbors) {
                    if (!visited[neighbor]) {
                        stk.push(neighbor);
                    }
                }
            }
        }
        
        cout << "DFS Iterative from " << start << ": ";
        for (int v : order) cout << v << " ";
        cout << endl;
    }
    
    // ============ DFS WITH DISCOVERY AND FINISH TIMES ============
    void dfsWithTimesUtil(int v, vector<bool>& visited, 
                          vector<int>& discovery, vector<int>& finish, 
                          int& time) {
        visited[v] = true;
        discovery[v] = ++time;
        
        vector<int> neighbors(adj[v].begin(), adj[v].end());
        sort(neighbors.begin(), neighbors.end());
        
        for (int neighbor : neighbors) {
            if (!visited[neighbor]) {
                dfsWithTimesUtil(neighbor, visited, discovery, finish, time);
            }
        }
        
        finish[v] = ++time;
    }
    
    void dfsWithTimes(int start) {
        vector<bool> visited(vertices, false);
        vector<int> discovery(vertices, 0);
        vector<int> finish(vertices, 0);
        int time = 0;
        
        dfsWithTimesUtil(start, visited, discovery, finish, time);
        
        cout << "\nDFS with Discovery/Finish Times from " << start << ":" << endl;
        for (int i = 0; i < vertices; i++) {
            if (discovery[i] != 0) {
                cout << "Vertex " << i << ": discovery = " << discovery[i] 
                     << ", finish = " << finish[i] << endl;
            }
        }
    }
    
    // ============ DFS FOR DISCONNECTED GRAPH ============
    void dfsDisconnected() {
        vector<bool> visited(vertices, false);
        vector<vector<int>> components;
        
        for (int i = 0; i < vertices; i++) {
            if (!visited[i]) {
                vector<int> component;
                dfsComponent(i, visited, component);
                components.push_back(component);
            }
        }
        
        cout << "\nDFS on Disconnected Graph:" << endl;
        cout << "Number of connected components: " << components.size() << endl;
        for (size_t i = 0; i < components.size(); i++) {
            cout << "Component " << i + 1 << ": ";
            for (int v : components[i]) cout << v << " ";
            cout << endl;
        }
    }
    
private:
    void dfsComponent(int v, vector<bool>& visited, vector<int>& component) {
        visited[v] = true;
        component.push_back(v);
        
        vector<int> neighbors(adj[v].begin(), adj[v].end());
        sort(neighbors.begin(), neighbors.end());
        
        for (int neighbor : neighbors) {
            if (!visited[neighbor]) {
                dfsComponent(neighbor, visited, component);
            }
        }
    }
    
public:
    // ============ CYCLE DETECTION IN UNDIRECTED GRAPH ============
    bool hasCycleUndirectedUtil(int v, int parent, vector<bool>& visited) {
        visited[v] = true;
        
        for (int neighbor : adj[v]) {
            if (!visited[neighbor]) {
                if (hasCycleUndirectedUtil(neighbor, v, visited)) {
                    return true;
                }
            } else if (neighbor != parent) {
                return true;  // Found a back edge
            }
        }
        return false;
    }
    
    bool hasCycleUndirected() {
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
    bool hasCycleDirectedUtil(int v, vector<bool>& visited, vector<bool>& recStack) {
        visited[v] = true;
        recStack[v] = true;
        
        for (int neighbor : adj[v]) {
            if (!visited[neighbor]) {
                if (hasCycleDirectedUtil(neighbor, visited, recStack)) {
                    return true;
                }
            } else if (recStack[neighbor]) {
                return true;  // Found a back edge
            }
        }
        
        recStack[v] = false;
        return false;
    }
    
    bool hasCycleDirected() {
        if (!isDirected) {
            cout << "Graph is undirected. Use hasCycleUndirected() instead." << endl;
            return false;
        }
        
        vector<bool> visited(vertices, false);
        vector<bool> recStack(vertices, false);
        
        for (int i = 0; i < vertices; i++) {
            if (!visited[i]) {
                if (hasCycleDirectedUtil(i, visited, recStack)) {
                    return true;
                }
            }
        }
        return false;
    }
    
    // ============ TOPOLOGICAL SORT (DIRECTED ACYCLIC GRAPH) ============
    void topologicalSortUtil(int v, vector<bool>& visited, stack<int>& stk) {
        visited[v] = true;
        
        for (int neighbor : adj[v]) {
            if (!visited[neighbor]) {
                topologicalSortUtil(neighbor, visited, stk);
            }
        }
        
        stk.push(v);
    }
    
    void topologicalSort() {
        if (!isDirected) {
            cout << "Topological sort only works on directed graphs!" << endl;
            return;
        }
        
        vector<bool> visited(vertices, false);
        stack<int> stk;
        
        for (int i = 0; i < vertices; i++) {
            if (!visited[i]) {
                topologicalSortUtil(i, visited, stk);
            }
        }
        
        cout << "\nTopological Sort: ";
        while (!stk.empty()) {
            cout << stk.top() << " ";
            stk.pop();
        }
        cout << endl;
    }
    
    // ============ FIND PATH BETWEEN TWO VERTICES ============
    bool hasPath(int start, int end) {
        vector<bool> visited(vertices, false);
        stack<int> stk;
        
        stk.push(start);
        
        while (!stk.empty()) {
            int v = stk.top();
            stk.pop();
            
            if (v == end) return true;
            
            if (!visited[v]) {
                visited[v] = true;
                for (int neighbor : adj[v]) {
                    if (!visited[neighbor]) {
                        stk.push(neighbor);
                    }
                }
            }
        }
        
        return false;
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
    cout << "=== Graph DFS Traversal Demo ===" << endl;
    
    // Create undirected graph
    Graph g(6, false);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(1, 4);
    g.addEdge(2, 4);
    g.addEdge(3, 4);
    g.addEdge(3, 5);
    
    g.display();
    
    cout << "\n=== DFS Traversal ===" << endl;
    g.dfsRecursive(0);
    g.dfsIterative(0);
    
    cout << "\n=== DFS with Discovery/Finish Times ===" << endl;
    g.dfsWithTimes(0);
    
    cout << "\n=== Path Finding ===" << endl;
    cout << "Path from 0 to 5: " << (g.hasPath(0, 5) ? "Yes" : "No") << endl;
    cout << "Path from 0 to 6: " << (g.hasPath(0, 6) ? "Yes" : "No") << endl;
    
    // Cycle detection
    cout << "\n=== Cycle Detection ===" << endl;
    cout << "Has cycle (undirected): " << (g.hasCycleUndirected() ? "Yes" : "No") << endl;
    
    // Directed graph for cycle detection and topological sort
    cout << "\n=== Directed Graph ===" << endl;
    Graph g2(6, true);
    g2.addEdge(5, 2);
    g2.addEdge(5, 0);
    g2.addEdge(4, 0);
    g2.addEdge(4, 1);
    g2.addEdge(2, 3);
    g2.addEdge(3, 1);
    
    g2.display();
    cout << "Has cycle (directed): " << (g2.hasCycleDirected() ? "Yes" : "No") << endl;
    g2.topologicalSort();
    
    // Graph with cycle
    cout << "\n=== Graph with Cycle ===" << endl;
    Graph g3(3, true);
    g3.addEdge(0, 1);
    g3.addEdge(1, 2);
    g3.addEdge(2, 0);
    
    g3.display();
    cout << "Has cycle (directed): " << (g3.hasCycleDirected() ? "Yes" : "No") << endl;
    
    // Disconnected graph
    cout << "\n=== Disconnected Graph ===" << endl;
    Graph g4(6, false);
    g4.addEdge(0, 1);
    g4.addEdge(0, 2);
    g4.addEdge(3, 4);
    g4.addEdge(3, 5);
    g4.display();
    g4.dfsDisconnected();
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Recursive DFS** | O(V + E) | O(V) (call stack) |
| **Iterative DFS** | O(V + E) | O(V) (explicit stack) |
| **Cycle Detection** | O(V + E) | O(V) |
| **Topological Sort** | O(V + E) | O(V) |
| **Connected Components** | O(V + E) | O(V) |

---

## 🎯 DFS Applications

| Application | Description |
|-------------|-------------|
| **Topological Sorting** | Ordering vertices in DAG |
| **Cycle Detection** | Finding cycles in graph |
| **Connected Components** | Finding all connected subgraphs |
| **Strongly Connected Components** | Kosaraju's algorithm |
| **Path Finding** | Finding paths between vertices |
| **Maze Solving** | Finding exit in maze |
| **Biconnected Components** | Finding articulation points |
| **Solving Puzzles** | Sudoku, N-Queens |

---

## 📊 DFS vs BFS Comparison

| Aspect | DFS | BFS |
|--------|-----|-----|
| **Data Structure** | Stack | Queue |
| **Order** | Depth first | Level by level |
| **Shortest Path** | No | Yes (unweighted) |
| **Space Complexity** | O(V) | O(V) |
| **Memory Usage** | Less (stack) | More (queue) |
| **Best for** | Topological sort, connectivity | Shortest path, level order |

---

## ✅ Key Takeaways

1. **DFS** explores depth-first, backtracking when needed
2. **Time complexity** O(V + E)
3. **Space complexity** O(V)
4. **Recursive** implementation is simpler
5. **Iterative** implementation avoids stack overflow
6. **Discovery/Finish times** are useful for many algorithms
7. **Connected components** found by running DFS on all unvisited vertices
8. **Cycle detection** uses parent tracking for undirected, recursion stack for directed

---