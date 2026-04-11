# Graph Traversal - DFS (Depth-First Search)

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
| **Tree Edges** | Edges that lead to new vertices |

---

## 📊 DFS Traversal Order

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

Step 1: Visit 0
Step 2: Go to neighbor 1 (unvisited)
Step 3: From 1, go to neighbor 2 (unvisited)
Step 4: From 2, go to neighbor 3 (unvisited)
Step 5: Backtrack when no unvisited neighbors
```

---

## 📝 Recursive DFS Implementation

```cpp
#include <iostream>
#include <vector>
#include <list>
using namespace std;

class Graph {
private:
    int vertices;
    vector<list<int>> adj;
    
    void dfsRecursiveUtil(int v, vector<bool>& visited) {
        visited[v] = true;
        cout << v << " ";
        
        for (int neighbor : adj[v]) {
            if (!visited[neighbor]) {
                dfsRecursiveUtil(neighbor, visited);
            }
        }
    }
    
public:
    Graph(int v) : vertices(v) {
        adj.resize(v);
    }
    
    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u);  // Undirected graph
    }
    
    void dfsRecursive(int start) {
        vector<bool> visited(vertices, false);
        cout << "DFS (Recursive): ";
        dfsRecursiveUtil(start, visited);
        cout << endl;
    }
};
```

---

## 🔄 Iterative DFS Implementation

```cpp
class Graph {
private:
    int vertices;
    vector<list<int>> adj;
    
public:
    Graph(int v) : vertices(v) {
        adj.resize(v);
    }
    
    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    
    void dfsIterative(int start) {
        vector<bool> visited(vertices, false);
        stack<int> stk;
        
        stk.push(start);
        visited[start] = true;
        
        cout << "DFS (Iterative): ";
        
        while (!stk.empty()) {
            int v = stk.top();
            stk.pop();
            cout << v << " ";
            
            for (int neighbor : adj[v]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    stk.push(neighbor);
                }
            }
        }
        cout << endl;
    }
};
```

---

## 📊 Complete DFS Implementation

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <stack>
#include <algorithm>
using namespace std;

class Graph {
private:
    int vertices;
    vector<list<int>> adj;
    
public:
    Graph(int v) : vertices(v) {
        adj.resize(v);
    }
    
    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u);  // Undirected graph
    }
    
    // Recursive DFS
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
        
        cout << "DFS Recursive: ";
        for (int v : order) cout << v << " ";
        cout << endl;
    }
    
    // Iterative DFS
    void dfsIterative(int start) {
        vector<bool> visited(vertices, false);
        vector<int> order;
        stack<int> stk;
        
        stk.push(start);
        visited[start] = true;
        
        while (!stk.empty()) {
            int v = stk.top();
            stk.pop();
            order.push_back(v);
            
            // Sort neighbors for consistent output
            vector<int> neighbors(adj[v].begin(), adj[v].end());
            sort(neighbors.rbegin(), neighbors.rend());  // Reverse to maintain order
            
            for (int neighbor : neighbors) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    stk.push(neighbor);
                }
            }
        }
        
        cout << "DFS Iterative: ";
        for (int v : order) cout << v << " ";
        cout << endl;
    }
    
    // DFS with discovery and finish times
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
        
        cout << "\nDFS with Discovery/Finish Times:" << endl;
        for (int i = 0; i < vertices; i++) {
            cout << "Vertex " << i << ": discovery = " << discovery[i] 
                 << ", finish = " << finish[i] << endl;
        }
    }
    
    // Find all connected components
    void findConnectedComponents() {
        vector<bool> visited(vertices, false);
        vector<vector<int>> components;
        
        for (int i = 0; i < vertices; i++) {
            if (!visited[i]) {
                vector<int> component;
                dfsComponent(i, visited, component);
                components.push_back(component);
            }
        }
        
        cout << "\nConnected Components (" << components.size() << "):" << endl;
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
        
        for (int neighbor : adj[v]) {
            if (!visited[neighbor]) {
                dfsComponent(neighbor, visited, component);
            }
        }
    }
    
public:
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
    cout << "=== Depth-First Search (DFS) Demo ===" << endl;
    
    // Create graph
    Graph g(6);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(1, 4);
    g.addEdge(2, 4);
    g.addEdge(3, 4);
    g.addEdge(3, 5);
    
    g.display();
    
    cout << "\n=== DFS Traversals ===" << endl;
    g.dfsRecursive(0);
    g.dfsIterative(0);
    
    g.dfsWithTimes(0);
    g.findConnectedComponents();
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Aspect | Complexity |
|--------|------------|
| **Time Complexity** | O(V + E) |
| **Space Complexity** | O(V) (stack + visited array) |
| **Recursive Space** | O(V) worst case (call stack) |

---

## 🎯 Applications of DFS

| Application | Description |
|-------------|-------------|
| **Topological Sorting** | Ordering vertices in DAG |
| **Cycle Detection** | Finding cycles in graph |
| **Connected Components** | Finding all connected subgraphs |
| **Biconnected Components** | Finding articulation points |
| **Strongly Connected Components** | Kosaraju's algorithm |
| **Path Finding** | Finding paths between vertices |
| **Maze Solving** | Finding exit in maze |
| **Tree Traversals** | Preorder, inorder, postorder |

---

## 🔄 Recursive vs Iterative DFS

| Aspect | Recursive | Iterative |
|--------|-----------|-----------|
| **Code Complexity** | Simple | More complex |
| **Stack Overflow Risk** | Yes (deep graphs) | No |
| **Performance** | Slightly slower | Slightly faster |
| **Space** | O(V) call stack | O(V) explicit stack |

---

## ✅ Key Takeaways

1. **DFS** explores depth-first, backtracking when needed
2. **Time complexity** O(V + E)
3. **Space complexity** O(V)
4. **Recursive** implementation is simpler
5. **Iterative** implementation avoids stack overflow
6. **Discovery/Finish times** are useful for many algorithms
7. **Connected components** found by running DFS on all unvisited vertices

---