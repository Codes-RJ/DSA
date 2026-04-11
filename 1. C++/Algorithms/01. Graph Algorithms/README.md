# Graph Algorithms - Complete Guide in C++

## 📖 Overview

This comprehensive guide covers essential graph algorithms implemented in **C++** for solving problems related to shortest paths, minimum spanning trees, network flow, connectivity, and more. Graphs model relationships between objects and are fundamental to social networks, GPS navigation, network routing, game development, and many other domains.

---

## 🎯 Why Graph Algorithms?

Graphs are everywhere in computer science and real-world applications:

| Domain | Application |
|--------|-------------|
| **GPS Navigation** | Finding shortest routes between locations |
| **Social Networks** | Finding connections and communities |
| **Network Routing** | Optimizing data packet transmission |
| **Game Development** | Pathfinding for NPCs and AI |
| **Recommendation Systems** | Finding similar users/products |
| **Bioinformatics** | Protein interaction networks |
| **Circuit Design** | Optimizing electronic circuits |
| **Transportation** | Optimizing delivery routes |

---

## 📚 Complete Index

| # | Algorithm | File | Use Case |
|---|-----------|------|----------|
| **Shortest Path Algorithms** |
| 1 | Dijkstra's Algorithm | `01_Dijkstra_Algorithm.md` | Shortest path (non-negative weights) |
| 2 | Bellman-Ford Algorithm | `02_Bellman_Ford_Algorithm.md` | Shortest path (negative weights allowed) |
| 3 | Floyd-Warshall Algorithm | `03_Floyd_Warshall_Algorithm.md` | All-pairs shortest paths |
| 4 | Johnson's Algorithm | `15_Johnson_Algorithm.md` | All-pairs (sparse graphs) |
| 5 | A* Search Algorithm | `06_A_Star_Algorithm.md` | Heuristic-based pathfinding |
| **Minimum Spanning Tree** |
| 6 | Kruskal's Algorithm | `04_Kruskal_Algorithm.md` | MST (edge-based approach) |
| 7 | Prim's Algorithm | `05_Prim_Algorithm.md` | MST (vertex-based approach) |
| **Network Flow** |
| 8 | Maximum Flow | `08_Maximum_Flow.md` | Max flow in network |
| 9 | Minimum Cut | `09_Minimum_Cut.md` | Min cut / Graph partitioning |
| **Graph Connectivity** |
| 10 | Strongly Connected Components | `07_SCC.md` | Finding SCCs in directed graphs |
| 11 | Bipartite Graph Check | `10_Bipartite_Graph.md` | 2-colorability test |
| **Critical Nodes & Edges** |
| 12 | Articulation Points | `11_Articulation_Points.md` | Cut vertices |
| 13 | Bridges (Cut Edges) | `12_Bridges.md` | Critical edges |
| **Matching** |
| 14 | Bipartite Matching | `13_Bipartite_Matching.md` | Maximum matching in bipartite graphs |
| **Special Paths** |
| 15 | Eulerian Path/Circuit | `14_Eulerian_Path.md` | Path using every edge exactly once |
| **Tree Algorithms** |
| 16 | Tarjan's LCA | `16_Tarjan_LCA.md` | Lowest Common Ancestor queries |

---

## 📊 Algorithm Complexity Quick Reference

| Algorithm | Time Complexity | Space Complexity | Negative Edges | Negative Cycles |
|-----------|----------------|------------------|----------------|-----------------|
| **Dijkstra** | O((V+E) log V) | O(V) | ❌ No | ❌ No |
| **Bellman-Ford** | O(V × E) | O(V) | ✅ Yes | ✅ Detects |
| **Floyd-Warshall** | O(V³) | O(V²) | ✅ Yes | ❌ No |
| **Johnson** | O(V² log V + V×E) | O(V²) | ✅ Yes | ✅ Detects |
| **A*** | O(E log V) | O(V) | ❌ No | ❌ No |
| **Kruskal** | O(E log E) | O(V+E) | N/A | N/A |
| **Prim** | O((V+E) log V) | O(V) | N/A | N/A |
| **Ford-Fulkerson** | O(E × max_flow) | O(V²) | N/A | N/A |
| **Edmonds-Karp** | O(V × E²) | O(V²) | N/A | N/A |
| **Kosaraju/Tarjan (SCC)** | O(V+E) | O(V) | N/A | N/A |
| **Articulation Points** | O(V+E) | O(V) | N/A | N/A |
| **Bridges** | O(V+E) | O(V) | N/A | N/A |
| **Hopcroft-Karp** | O(E √V) | O(V) | N/A | N/A |
| **Eulerian Path** | O(E) | O(V+E) | N/A | N/A |
| **Tarjan's LCA** | O(N + Q) | O(N + Q) | N/A | N/A |

---

## 🎯 Algorithm Selection Guide

### By Problem Type
```
Shortest Path Problems:
├── Single source, non-negative weights → Dijkstra
├── Single source, negative weights → Bellman-Ford
├── All-pairs, dense graph → Floyd-Warshall
├── All-pairs, sparse graph → Johnson
└── With heuristic, grid/graph → A*

Minimum Spanning Tree:
├── Sparse graph → Kruskal
└── Dense graph → Prim

Network Flow:
├── Basic max flow → Ford-Fulkerson / Edmonds-Karp
└── Min cut → Derived from max flow

Connectivity:
├── Directed graph SCC → Tarjan (in 07_SCC.md)
├── Undirected connectivity → DFS/BFS
├── Critical vertices → Articulation Points
└── Critical edges → Bridges

Matching:
└── Bipartite graph → Bipartite Matching

Special Paths:
├── Every edge once → Eulerian Path
└── Every vertex once → Hamiltonian (NP-hard - not covered)

Tree Queries:
└── LCA multiple queries → Tarjan's LCA
```
---

## 📈 Graph Representations

| Representation | Space | Edge Lookup | Neighbors | Best For |
|----------------|-------|-------------|-----------|----------|
| **Adjacency Matrix** | O(V²) | O(1) | O(V) | Dense graphs, Floyd-Warshall |
| **Adjacency List** | O(V+E) | O(V) | O(degree) | Sparse graphs, most algorithms |
| **Edge List** | O(E) | O(E) | O(E) | Kruskal, Bellman-Ford |

---

## 🔧 Prerequisites

Before diving into these algorithms, ensure you understand:

- ✅ Basic graph terminology (vertices, edges, degree, path, cycle)
- ✅ Graph representations (matrix, list, edge list)
- ✅ Recursion and stack concepts
- ✅ Priority queues and heaps (for Dijkstra, Prim, A*)
- ✅ Time and space complexity analysis

---

## 🚀 Learning Path

```
Level 1: Fundamentals
    ├── Dijkstra (Shortest Path)
    ├── Bellman-Ford (Negative Weights)
    └── Floyd-Warshall (All Pairs)

Level 2: Spanning Trees
    ├── Kruskal
    └── Prim

Level 3: Flow & Connectivity
    ├── Maximum Flow
    ├── Minimum Cut
    └── SCC (Tarjan)

Level 4: Critical Analysis
    ├── Articulation Points
    └── Bridges

Level 5: Specialized
    ├── A* Search
    ├── Bipartite Matching
    ├── Eulerian Path
    ├── Johnson's Algorithm
    └── Tarjan's LCA
```

---

## 💻 Implementation Notes

All algorithms are implemented in **C++** with:

- **Complete working code** - Ready to compile and run
- **Detailed comments** - Explaining each step
- **Multiple examples** - Covering edge cases
- **Complexity analysis** - Time and space
- **Real-world applications** - Practical use cases

---

## 📖 How to Use This Guide

1. **Start with Dijkstra** if you're new to graph algorithms
2. **Follow the learning path** for progressive difficulty
3. **Run the examples** to see algorithms in action
4. **Refer to complexity table** when choosing algorithms
5. **Use selection guide** for problem-specific needs

---

## ✅ Summary

This guide provides complete coverage of **16 essential graph algorithms**:

| Category | Count | Algorithms |
|----------|-------|------------|
| Shortest Path | 5 | Dijkstra, Bellman-Ford, Floyd-Warshall, Johnson, A* |
| MST | 2 | Kruskal, Prim |
| Network Flow | 2 | Max Flow, Min Cut |
| Connectivity | 2 | SCC, Bipartite Graph |
| Critical Nodes | 2 | Articulation Points, Bridges |
| Matching | 1 | Bipartite Matching |
| Special Paths | 1 | Eulerian Path |
| Tree Queries | 1 | Tarjan's LCA |
| **TOTAL** | **16** | |

---

## 🎯 Next Steps

After mastering graph algorithms, proceed to:

- **Dynamic Programming** - Optimization problems
- **Greedy Algorithms** - Local optimal choices
- **Divide and Conquer** - Recursive problem solving
- **Backtracking** - Constraint satisfaction

---

## 🤝 Contributing

Feel free to contribute by:
- Reporting bugs or edge cases
- Suggesting optimizations
- Adding missing algorithms (Topological Sort, Hamiltonian Path, etc.)

---