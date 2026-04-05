# Trees and Graphs - Complete Guide

## 📖 Overview

Trees and graphs are fundamental non-linear data structures that represent hierarchical and network relationships. Understanding these structures is crucial for solving complex problems in computer science, from file systems to social networks.

---

## 🎯 Why Trees and Graphs?

| Structure | Use Case | Example |
|-----------|----------|---------|
| **Trees** | Hierarchical data | File systems, HTML DOM, Organization charts |
| **Binary Trees** | Expression parsing, Huffman coding | Arithmetic expression trees |
| **BST** | Efficient searching, sorted data | Database indexes |
| **AVL Trees** | Self-balancing search trees | Memory management |
| **Graphs** | Network relationships | Social networks, maps, routing |

---

## 📚 Folder Structure

```
05. Trees and Graphs/
│
├── README.md                                    # This file
│
├── 01_Binary_Trees/                             # Basic binary tree concepts
│   ├── README.md
│   ├── 01_Tree_Basics.md                        # Definition, terminology
│   ├── 02_Tree_Node_Structure.md                # Node implementation
│   ├── 03_Tree_Properties.md                    # Height, depth, size
│   ├── 04_Binary_Tree_Implementation.md         # Complete implementation
│   └── 05_Tree_Operations.md                    # Insert, delete, search
│
├── 02_BST/                                      # Binary Search Trees
│   ├── README.md
│   ├── 01_BST_Introduction.md                   # BST properties
│   ├── 02_BST_Insertion.md                      # Insert operation
│   ├── 03_BST_Deletion.md                       # Delete operation
│   ├── 04_BST_Search.md                         # Search operation
│   └── 05_BST_Traversal.md                      # BST traversals
│
├── 03_AVL_Trees/                                # Self-balancing BST
│   ├── README.md
│   ├── 01_AVL_Introduction.md                   # AVL properties
│   ├── 02_Rotations.md                          # Left, right rotations
│   ├── 03_Balancing_Factor.md                   # Balance factor
│   ├── 04_AVL_Insertion.md                      # Insert with balancing
│   └── 05_AVL_Deletion.md                       # Delete with balancing
│
├── 04_Graph_Representations/                    # Ways to store graphs
│   ├── README.md
│   ├── 01_Graph_Basics.md                       # Terminology, types
│   ├── 02_Adjacency_Matrix.md                   # Matrix representation
│   ├── 03_Adjacency_List.md                     # List representation
│   ├── 04_Edge_List.md                          # Edge list representation
│   └── 05_Comparison_of_Representations.md      # Pros and cons
│
├── 05_Tree_Traversals/                          # Tree traversal methods
│   ├── README.md
│   ├── 01_Depth_First_Search.md                 # DFS overview
│   ├── 02_Breadth_First_Search.md               # BFS overview
│   ├── 03_Inorder_Traversal.md                  # Left-Root-Right
│   ├── 04_Preorder_Traversal.md                 # Root-Left-Right
│   ├── 05_Postorder_Traversal.md                # Left-Right-Root
│   └── 06_Level_Order_Traversal.md              # Level by level
│
└── 06_Basic_Graph_Algorithms/                   # Fundamental graph algorithms
    ├── README.md
    ├── 01_Graph_Traversal_BFS.md                # BFS on graphs
    ├── 02_Graph_Traversal_DFS.md                # DFS on graphs
    ├── 03_Connected_Components.md               # Finding components
    ├── 04_Cycle_Detection.md                    # Detecting cycles
    └── 05_Topological_Sort.md                   # Ordering DAGs
```

---

## 📊 Prerequisites

Before diving into trees and graphs, ensure you understand:

| Topic | Importance |
|-------|------------|
| **Recursion** | Essential for tree traversals |
| **Pointers/References** | For node linking |
| **Queues** | For level-order traversals and BFS |
| **Stacks** | For DFS implementations |
| **Dynamic Memory** | For creating nodes |

---

## 🎯 Learning Path

```
Step 1: Binary Trees
    ↓
Step 2: Tree Traversals (DFS, BFS, Inorder, Preorder, Postorder, Level Order)
    ↓
Step 3: Binary Search Trees (BST)
    ↓
Step 4: Self-balancing Trees (AVL)
    ↓
Step 5: Graph Representations (Matrix, List, Edge List)
    ↓
Step 6: Graph Traversals (BFS, DFS)
    ↓
Step 7: Basic Graph Algorithms (Components, Cycles, Topological Sort)
```

---

## 📊 Complexity Comparison

### Tree Operations

| Tree Type | Search | Insert | Delete | Space |
|-----------|--------|--------|--------|-------|
| Binary Tree (unbalanced) | O(n) | O(n) | O(n) | O(n) |
| BST (average) | O(log n) | O(log n) | O(log n) | O(n) |
| BST (worst) | O(n) | O(n) | O(n) | O(n) |
| AVL Tree | O(log n) | O(log n) | O(log n) | O(n) |

### Graph Representations

| Representation | Space | Add Vertex | Add Edge | Check Edge | Iterate Edges |
|----------------|-------|------------|----------|------------|---------------|
| Adjacency Matrix | O(V²) | O(V²) | O(1) | O(1) | O(V) |
| Adjacency List | O(V+E) | O(1) | O(1) | O(V) | O(degree) |
| Edge List | O(E) | O(1) | O(1) | O(E) | O(E) |

### Graph Traversal Complexity

| Algorithm | Time | Space |
|-----------|------|-------|
| BFS (Adjacency List) | O(V+E) | O(V) |
| BFS (Adjacency Matrix) | O(V²) | O(V) |
| DFS (Adjacency List) | O(V+E) | O(V) |
| DFS (Adjacency Matrix) | O(V²) | O(V) |

---

## 📝 Terminology

### Tree Terminology

| Term | Definition |
|------|------------|
| **Root** | Topmost node of the tree |
| **Parent** | Node that has children |
| **Child** | Node directly connected to parent |
| **Leaf** | Node with no children |
| **Internal Node** | Node with at least one child |
| **Subtree** | Any node and its descendants |
| **Height** | Number of edges on longest path from node to leaf |
| **Depth** | Number of edges from root to node |
| **Level** | Depth + 1 |

### Graph Terminology

| Term | Definition |
|------|------------|
| **Vertex (Node)** | Fundamental unit of a graph |
| **Edge** | Connection between vertices |
| **Degree** | Number of edges incident to a vertex |
| **Path** | Sequence of vertices connected by edges |
| **Cycle** | Path that starts and ends at same vertex |
| **Connected Component** | Maximal set of connected vertices |
| **Directed Graph** | Edges have direction |
| **Undirected Graph** | Edges have no direction |
| **Weighted Graph** | Edges have weights |
| **DAG** | Directed Acyclic Graph |

---

## ✅ Key Takeaways

1. **Trees** are specialized graphs with no cycles
2. **BSTs** provide O(log n) operations when balanced
3. **AVL Trees** automatically maintain balance
4. **Graph representations** have trade-offs: matrix for dense, list for sparse
5. **BFS** finds shortest paths in unweighted graphs
6. **DFS** is useful for connectivity and cycle detection
7. **Topological Sort** orders tasks with dependencies

---

## 🚀 Next Steps

After mastering trees and graphs, proceed to:

- **Graph Algorithms** (Dijkstra, Bellman-Ford, Floyd-Warshall)
- **Minimum Spanning Trees** (Kruskal, Prim)
- **Network Flow** (Ford-Fulkerson, Edmonds-Karp)
- **Advanced Tree Structures** (Red-Black, B-Trees, Segment Trees)

---