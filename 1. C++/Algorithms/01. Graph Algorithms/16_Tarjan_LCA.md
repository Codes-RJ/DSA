# Graph Algorithm - Tarjan's LCA (Lowest Common Ancestor)

## 📖 Overview

Tarjan's algorithm finds the Lowest Common Ancestor (LCA) of pairs of nodes in a rooted tree using the Union-Find data structure. It processes queries offline in O(N + Q) time, where N is the number of nodes and Q is the number of queries. This is significantly faster than the naive O(N) per query approach.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Lowest Common Ancestor (LCA)** | The deepest node that is an ancestor of both given nodes |
| **Offline Algorithm** | All queries are known in advance |
| **Union-Find (DSU)** | Disjoint Set Union for efficient ancestor tracking |
| **DFS Traversal** | Post-order traversal to process nodes |
| **Color Marking** | 0 = unvisited, 1 = visiting, 2 = visited |

---

## 📊 LCA Visualization

```
Tree:
        1
       / \
      2   3
     / \   \
    4   5   6
       / \
      7   8

LCA(4,5) = 2
LCA(7,8) = 5
LCA(7,6) = 1
LCA(4,8) = 2
```

---

## 📝 Complete Implementation

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <cstring>
#include <iomanip>
using namespace std;

class TarjanLCA {
private:
    int vertices;
    vector<list<int>> tree;
    vector<vector<pair<int, int>>> queries;  // (otherNode, queryIndex)
    vector<int> parent;
    vector<int> ancestor;
    vector<bool> visited;
    vector<int> result;
    
    // Union-Find (Disjoint Set Union)
    vector<int> dsuParent;
    vector<int> rank;
    
    int find(int x) {
        if (dsuParent[x] != x) {
            dsuParent[x] = find(dsuParent[x]);
        }
        return dsuParent[x];
    }
    
    void unite(int x, int y) {
        int rx = find(x);
        int ry = find(y);
        if (rx != ry) {
            if (rank[rx] < rank[ry]) {
                dsuParent[rx] = ry;
            } else if (rank[rx] > rank[ry]) {
                dsuParent[ry] = rx;
            } else {
                dsuParent[ry] = rx;
                rank[rx]++;
            }
        }
    }
    
    void dfs(int u) {
        dsuParent[u] = u;
        ancestor[u] = u;
        
        for (int v : tree[u]) {
            if (v == parent[u]) continue;
            parent[v] = u;
            dfs(v);
            unite(u, v);
            ancestor[find(u)] = u;
        }
        
        visited[u] = true;
        
        // Process all queries involving u
        for (auto& query : queries[u]) {
            int v = query.first;
            int idx = query.second;
            if (visited[v]) {
                result[idx] = ancestor[find(v)];
            }
        }
    }
    
public:
    TarjanLCA(int n) : vertices(n) {
        tree.resize(n);
        queries.resize(n);
        parent.resize(n, -1);
        ancestor.resize(n, -1);
        visited.resize(n, false);
        dsuParent.resize(n);
        rank.resize(n, 0);
    }
    
    void addEdge(int u, int v) {
        tree[u].push_back(v);
        tree[v].push_back(u);
    }
    
    void addQuery(int u, int v, int idx) {
        queries[u].push_back({v, idx});
        queries[v].push_back({u, idx});
    }
    
    vector<int> computeLCA(int root) {
        result.resize(queries.size(), -1);
        dfs(root);
        return result;
    }
    
    // ============ PREPROCESSING FOR BINARY LIFTING (Alternative) ============
    vector<vector<int>> up;
    vector<int> depth;
    int LOG;
    
    void preprocessBinaryLifting(int root) {
        LOG = 0;
        while ((1 << LOG) <= vertices) LOG++;
        
        up.assign(vertices, vector<int>(LOG));
        depth.assign(vertices, 0);
        
        dfsBinary(root, root);
        
        for (int j = 1; j < LOG; j++) {
            for (int i = 0; i < vertices; i++) {
                up[i][j] = up[up[i][j-1]][j-1];
            }
        }
    }
    
    void dfsBinary(int u, int p) {
        up[u][0] = p;
        for (int v : tree[u]) {
            if (v == p) continue;
            depth[v] = depth[u] + 1;
            dfsBinary(v, u);
        }
    }
    
    int lcaBinary(int u, int v) {
        if (depth[u] < depth[v]) swap(u, v);
        
        // Lift u to depth of v
        int diff = depth[u] - depth[v];
        for (int i = 0; i < LOG; i++) {
            if (diff & (1 << i)) {
                u = up[u][i];
            }
        }
        
        if (u == v) return u;
        
        for (int i = LOG - 1; i >= 0; i--) {
            if (up[u][i] != up[v][i]) {
                u = up[u][i];
                v = up[v][i];
            }
        }
        
        return up[u][0];
    }
    
    // ============ DISPLAY ============
    void displayTree() {
        cout << "\nTree Structure:\n";
        for (int i = 0; i < vertices; i++) {
            cout << i << ": ";
            for (int neighbor : tree[i]) {
                cout << neighbor << " ";
            }
            cout << endl;
        }
    }
    
    void displayQueries() {
        cout << "\nQueries:\n";
        for (int i = 0; i < queries.size(); i++) {
            for (auto& q : queries[i]) {
                if (i < q.first) {  // Print each query once
                    cout << "LCA(" << i << ", " << q.first << ")" << endl;
                }
            }
        }
    }
    
    void displayResults(const vector<int>& results) {
        cout << "\nResults:\n";
        for (int i = 0; i < results.size(); i++) {
            cout << "Query " << i << ": LCA = " << results[i] << endl;
        }
    }
};

int main() {
    cout << "=== Tarjan's LCA Algorithm Demo ===" << endl;
    
    // Example 1: Simple tree
    cout << "\n1. Simple Tree:" << endl;
    TarjanLCA lca1(7);
    lca1.addEdge(0, 1);
    lca1.addEdge(0, 2);
    lca1.addEdge(1, 3);
    lca1.addEdge(1, 4);
    lca1.addEdge(2, 5);
    lca1.addEdge(2, 6);
    
    lca1.displayTree();
    
    // Add queries
    lca1.addQuery(3, 4, 0);
    lca1.addQuery(3, 5, 1);
    lca1.addQuery(4, 6, 2);
    lca1.addQuery(5, 6, 3);
    lca1.addQuery(3, 0, 4);
    
    lca1.displayQueries();
    
    vector<int> results1 = lca1.computeLCA(0);
    lca1.displayResults(results1);
    
    // Example 2: Binary Lifting (Online queries)
    cout << "\n2. Binary Lifting (Online Queries):" << endl;
    TarjanLCA lca2(7);
    lca2.addEdge(0, 1);
    lca2.addEdge(0, 2);
    lca2.addEdge(1, 3);
    lca2.addEdge(1, 4);
    lca2.addEdge(2, 5);
    lca2.addEdge(2, 6);
    
    lca2.preprocessBinaryLifting(0);
    
    cout << "LCA(3,4) = " << lca2.lcaBinary(3, 4) << endl;
    cout << "LCA(3,5) = " << lca2.lcaBinary(3, 5) << endl;
    cout << "LCA(4,6) = " << lca2.lcaBinary(4, 6) << endl;
    cout << "LCA(5,6) = " << lca2.lcaBinary(5, 6) << endl;
    cout << "LCA(3,0) = " << lca2.lcaBinary(3, 0) << endl;
    
    // Example 3: Larger tree
    cout << "\n3. Larger Tree (10 nodes):" << endl;
    TarjanLCA lca3(10);
    lca3.addEdge(0, 1);
    lca3.addEdge(0, 2);
    lca3.addEdge(1, 3);
    lca3.addEdge(1, 4);
    lca3.addEdge(2, 5);
    lca3.addEdge(2, 6);
    lca3.addEdge(3, 7);
    lca3.addEdge(3, 8);
    lca3.addEdge(4, 9);
    
    lca3.addQuery(7, 8, 0);
    lca3.addQuery(7, 9, 1);
    lca3.addQuery(7, 5, 2);
    lca3.addQuery(8, 9, 3);
    lca3.addQuery(9, 6, 4);
    
    vector<int> results3 = lca3.computeLCA(0);
    lca3.displayResults(results3);
    
    // Example 4: Chain tree
    cout << "\n4. Chain Tree (Degenerate):" << endl;
    TarjanLCA lca4(5);
    lca4.addEdge(0, 1);
    lca4.addEdge(1, 2);
    lca4.addEdge(2, 3);
    lca4.addEdge(3, 4);
    
    lca4.addQuery(0, 4, 0);
    lca4.addQuery(1, 3, 1);
    lca4.addQuery(2, 4, 2);
    
    vector<int> results4 = lca4.computeLCA(0);
    lca4.displayResults(results4);
    
    // Example 5: Binary Lifting on chain
    cout << "\n5. Binary Lifting on Chain Tree:" << endl;
    TarjanLCA lca5(5);
    lca5.addEdge(0, 1);
    lca5.addEdge(1, 2);
    lca5.addEdge(2, 3);
    lca5.addEdge(3, 4);
    
    lca5.preprocessBinaryLifting(0);
    
    cout << "LCA(0,4) = " << lca5.lcaBinary(0, 4) << endl;
    cout << "LCA(1,3) = " << lca5.lcaBinary(1, 3) << endl;
    cout << "LCA(2,4) = " << lca5.lcaBinary(2, 4) << endl;
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Algorithm | Time Complexity | Space Complexity | Type |
|-----------|----------------|------------------|------|
| **Tarjan's (Offline)** | O(N + Q) | O(N + Q) | Offline |
| **Binary Lifting (Online)** | O(N log N) preprocessing, O(log N) per query | O(N log N) | Online |

---

## 🎯 Applications

| Application | Description |
|-------------|-------------|
| **Family Trees** | Finding common ancestors |
| **Computer Networks** | Finding common routers |
| **File Systems** | Finding common parent directory |
| **Compiler Design** | Finding common base class |
| **Biology** | Finding common ancestors in evolutionary trees |

---

## ✅ Key Takeaways

1. **Tarjan's LCA** processes queries offline in O(N + Q)
2. **Union-Find** efficiently tracks ancestors
3. **Binary Lifting** answers online queries in O(log N)
4. **DFS traversal** is used to visit nodes
5. **Color marking** tracks visited nodes

---
---

## Next Step

- Go to [README.md](README.md) to continue.
