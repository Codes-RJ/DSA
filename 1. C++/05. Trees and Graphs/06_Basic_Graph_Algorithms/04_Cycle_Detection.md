# Cycle Detection in Graphs: Comprehensive Strategies

## Overview
Cycle detection is a fundamental graph problem. A cycle exists if you can start at a vertex $v$, follow a path of non-zero length, and return to $v$. The methodology differs significantly between directed and undirected graphs.

---

## 1. Undirected Graphs: DFS and Union-Find

### DFS Method
**Condition**: A cycle exists if we encounter a visited vertex that is not the direct parent of the current vertex.

```cpp
bool isCycleDFS(int u, int parent, vector<vector<int>>& adj, vector<bool>& visited) {
    visited[u] = true;
    for (int v : adj[u]) {
        if (!visited[v]) {
            if (isCycleDFS(v, u, adj, visited)) return true;
        } else if (v != parent) {
            return true; // Cycle found (back-edge to non-parent)
        }
    }
    return false;
}
```

### Union-Find (DSU) Method
**Condition**: While adding edges one by one, if both vertices of an edge `{u, v}` already belong to the same disjoint set (i.e., they have the same representative), a cycle is formed.

```cpp
struct DSU {
    vector<int> parent;
    DSU(int n) {
        parent.resize(n);
        for(int i=0; i<n; i++) parent[i] = i;
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]); // Path compression
    }
    bool unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i == root_j) return false; // Cycle detected
        parent[root_i] = root_j;
        return true;
    }
};
```

---

## 2. Directed Graphs: Recursion Stack vs. Kahn's

### DFS Method (Recursion Stack)
**Condition**: A cycle exists if we encounter a vertex that is currently in the active recursion stack (`recStack`). This represents a **back-edge** to an ancestor.

```cpp
bool isCycleDirected(int u, vector<vector<int>>& adj, vector<bool>& visited, vector<bool>& recStack) {
    visited[u] = true;
    recStack[u] = true;
    for (int v : adj[u]) {
        if (!visited[v]) {
            if (isCycleDirected(v, adj, visited, recStack)) return true;
        } else if (recStack[v]) {
            return true; // Back-edge found
        }
    }
    recStack[u] = false; // Important: Clear stack after processing
    return false;
}
```

### Kahn's Algorithm (BFS-Based)
**Condition**: If the topological sort of a graph does not include every vertex, then the graph must contain a cycle.

---

## 3. Practical Use Case: Deadlock Detection
In Operating Systems, a **Resource Allocation Graph (RAG)** is used. If a cycle exists in a directed RAG, it indicates a **deadlock**—a set of processes waiting infinitely for resources held by each other.

---

## 4. Comparison Summary

| Method | Graph Type | Time | Space | Notes |
|--------|------------|------|-------|-------|
| **DFS** | Undirected | $O(V+E)$ | $O(V)$ | Simplest for traversing. |
| **Union-Find** | Undirected | $O(E \cdot \alpha(V))$| $O(V)$ | Best for dynamic edge-adding. |
| **DFS (Stack)**| Directed | $O(V+E)$ | $O(V)$ | Identifies back-edges. |
| **Kahn's (BFS)**| Directed | $O(V+E)$ | $O(V)$ | Also generates topological sort. |

---

## Final Checklist
- [ ] For undirected graphs, do you check `v != parent`?
- [ ] For directed graphs, do you clear `recStack[u]` on backtrack?
- [ ] Did you handle disconnected graphs by calling the function from every node?
- [ ] If using DSU, did you implement **Path Compression** for efficiency?
