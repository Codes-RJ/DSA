# Topological Sort

## Introduction
Topological Sort of a Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge `u -> v`, vertex `u` comes before `v` in the ordering.

## Constraints
1. Must be a **Directed** graph.
2. Must be **Acyclic** (no cycles).

## Algorithms

### 1. DFS-Based (Kahn's Alternative)
Perform a DFS and push the vertex onto a stack after its children have been processed. The final stack contains the topological order (reverse order of when nodes finished).

```cpp
void topoSortDFS(int u, vector<vector<int>>& adj, vector<bool>& visited, stack<int>& s) {
    visited[u] = true;
    for (int v : adj[u]) {
        if (!visited[v]) topoSortDFS(v, adj, visited, s);
    }
    s.push(u); // Push to stack when processing is complete
}
```

### 2. Kahn's Algorithm (BFS-Based)
Uses the concept of **In-degree** (number of edges pointing to a node).
1. Calculate in-degree for all vertices.
2. Put all vertices with in-degree 0 into a queue.
3. While queue is not empty:
   - Extract `u`. Add to sort result.
   - For each neighbor `v` of `u`:
     - Decrement in-degree of `v`.
     - If in-degree becomes 0, push `v` to queue.

## C++ Implementation (Kahn's)
```cpp
vector<int> topologicalSort(int V, vector<vector<int>>& adj) {
    vector<int> inDegree(V, 0);
    for (int i = 0; i < V; i++) {
        for (int v : adj[i]) inDegree[v]++;
    }

    queue<int> q;
    for (int i = 0; i < V; i++) {
        if (inDegree[i] == 0) q.push(i);
    }

    vector<int> topo;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        topo.push_back(u);

        for (int v : adj[u]) {
            if (--inDegree[v] == 0) q.push(v);
        }
    }
    
    if (topo.size() != V) return {}; // Cycle detected
    return topo;
}
```

## Applications
- Build systems (e.g., `make`) to determine compilation order.
- Course scheduling (prerequisites).
- Task prioritization.
- Data processing pipelines.

## Complexity
- **Time**: O(V + E)
- **Space**: O(V)
