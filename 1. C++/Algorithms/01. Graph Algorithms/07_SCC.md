# Strongly Connected Components (Kosaraju's Algorithm)

## 📖 Overview

Strongly Connected Components (SCC) are maximal sets of vertices in a directed graph where every vertex can reach every other vertex in the same set. Kosaraju's algorithm finds all SCCs in O(V+E) time using two DFS traversals.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Strongly Connected Component** | Maximal set where every vertex reaches every other |
| **Kosaraju's Algorithm** | Two-pass DFS approach |
| **Transpose Graph** | Reverse all edges |
| **Finish Time** | Order of DFS completion |

---

## 📝 Complete Implementation

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <stack>
#include <algorithm>
#include <cstring>
using namespace std;

class Graph {
private:
    int vertices;
    vector<list<int>> adj;
    
    // DFS for first pass (fill stack with finishing times)
    void dfs1(int v, vector<bool>& visited, stack<int>& stk) {
        visited[v] = true;
        
        for (int neighbor : adj[v]) {
            if (!visited[neighbor]) {
                dfs1(neighbor, visited, stk);
            }
        }
        
        stk.push(v);
    }
    
    // DFS on transpose graph
    void dfs2(int v, vector<bool>& visited, vector<int>& component) {
        visited[v] = true;
        component.push_back(v);
        
        for (int neighbor : transpose[v]) {
            if (!visited[neighbor]) {
                dfs2(neighbor, visited, component);
            }
        }
    }
    
public:
    vector<list<int>> transpose;
    
    Graph(int v) : vertices(v) {
        adj.resize(v);
        transpose.resize(v);
    }
    
    void addEdge(int u, int v) {
        adj[u].push_back(v);
        transpose[v].push_back(u);
    }
    
    // Kosaraju's Algorithm
    vector<vector<int>> findSCCs() {
        // Step 1: Fill vertices in stack according to finishing times
        stack<int> stk;
        vector<bool> visited(vertices, false);
        
        for (int i = 0; i < vertices; i++) {
            if (!visited[i]) {
                dfs1(i, visited, stk);
            }
        }
        
        // Step 2: Process vertices in stack order on transpose graph
        vector<vector<int>> sccs;
        fill(visited.begin(), visited.end(), false);
        
        while (!stk.empty()) {
            int v = stk.top();
            stk.pop();
            
            if (!visited[v]) {
                vector<int> component;
                dfs2(v, visited, component);
                sccs.push_back(component);
            }
        }
        
        return sccs;
    }
    
    // Check if graph is strongly connected
    bool isStronglyConnected() {
        vector<vector<int>> sccs = findSCCs();
        return sccs.size() == 1;
    }
    
    // Tarjan's Algorithm (alternative, single pass)
    vector<vector<int>> findSCCsTarjan() {
        vector<int> disc(vertices, -1);
        vector<int> low(vertices, -1);
        vector<bool> onStack(vertices, false);
        stack<int> stk;
        vector<vector<int>> sccs;
        int time = 0;
        
        for (int i = 0; i < vertices; i++) {
            if (disc[i] == -1) {
                tarjanDFS(i, disc, low, onStack, stk, sccs, time);
            }
        }
        
        return sccs;
    }
    
private:
    void tarjanDFS(int u, vector<int>& disc, vector<int>& low, 
                   vector<bool>& onStack, stack<int>& stk,
                   vector<vector<int>>& sccs, int& time) {
        disc[u] = low[u] = ++time;
        stk.push(u);
        onStack[u] = true;
        
        for (int v : adj[u]) {
            if (disc[v] == -1) {
                tarjanDFS(v, disc, low, onStack, stk, sccs, time);
                low[u] = min(low[u], low[v]);
            } else if (onStack[v]) {
                low[u] = min(low[u], disc[v]);
            }
        }
        
        if (low[u] == disc[u]) {
            vector<int> component;
            while (true) {
                int v = stk.top();
                stk.pop();
                onStack[v] = false;
                component.push_back(v);
                if (v == u) break;
            }
            sccs.push_back(component);
        }
    }
    
public:
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
    
    void displaySCCs(const vector<vector<int>>& sccs) {
        cout << "\nStrongly Connected Components (" << sccs.size() << "):\n";
        for (size_t i = 0; i < sccs.size(); i++) {
            cout << "SCC " << i + 1 << ": ";
            for (int v : sccs[i]) {
                cout << v << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    cout << "=== Strongly Connected Components Demo ===" << endl;
    
    // Example 1: Graph with multiple SCCs
    cout << "\n1. Graph with Multiple SCCs:" << endl;
    Graph g1(7);
    g1.addEdge(0, 1);
    g1.addEdge(1, 2);
    g1.addEdge(2, 0);
    g1.addEdge(1, 3);
    g1.addEdge(3, 4);
    g1.addEdge(4, 5);
    g1.addEdge(5, 3);
    g1.addEdge(6, 5);
    g1.addEdge(6, 4);
    
    g1.display();
    
    auto sccs1 = g1.findSCCs();
    g1.displaySCCs(sccs1);
    
    // Example 2: Single SCC (strongly connected)
    cout << "\n2. Strongly Connected Graph:" << endl;
    Graph g2(4);
    g2.addEdge(0, 1);
    g2.addEdge(1, 2);
    g2.addEdge(2, 3);
    g2.addEdge(3, 0);
    
    g2.display();
    
    auto sccs2 = g2.findSCCs();
    g2.displaySCCs(sccs2);
    cout << "Is strongly connected? " << (g2.isStronglyConnected() ? "Yes" : "No") << endl;
    
    // Example 3: Tarjan's Algorithm
    cout << "\n3. Tarjan's Algorithm:" << endl;
    Graph g3(8);
    g3.addEdge(0, 1);
    g3.addEdge(1, 2);
    g3.addEdge(2, 3);
    g3.addEdge(3, 0);
    g3.addEdge(2, 4);
    g3.addEdge(4, 5);
    g3.addEdge(5, 6);
    g3.addEdge(6, 4);
    g3.addEdge(7, 6);
    
    auto sccs3 = g3.findSCCsTarjan();
    g3.displaySCCs(sccs3);
    
    // Example 4: DAG (each vertex its own SCC)
    cout << "\n4. DAG (Each vertex its own SCC):" << endl;
    Graph g4(5);
    g4.addEdge(0, 1);
    g4.addEdge(1, 2);
    g4.addEdge(2, 3);
    g4.addEdge(3, 4);
    
    g4.display();
    
    auto sccs4 = g4.findSCCs();
    g4.displaySCCs(sccs4);
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Kosaraju's** | O(V + E) | O(V + E) |
| **Tarjan's** | O(V + E) | O(V) |

---

## 🎯 Applications

| Application | Description |
|-------------|-------------|
| **Social Networks** | Finding groups where everyone knows everyone |
| **Web Crawling** | Identifying strongly connected web pages |
| **Circuit Analysis** | Finding feedback loops |
| **Deadlock Detection** | Finding circular wait in resource allocation |
| **Software Dependencies** | Finding circular dependencies |

---

## ✅ Key Takeaways

1. **SCC** = maximal set where every vertex reaches every other
2. **Kosaraju's** = two-pass DFS (simpler, more intuitive)
3. **Tarjan's** = single-pass DFS (more efficient in practice)
4. **Transpose graph** is key to Kosaraju's algorithm
5. **Low-link values** are key to Tarjan's algorithm

---