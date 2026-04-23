# README.md

## Trees and Graphs in C++ - Complete Guide

### Overview

Trees and graphs are non-linear data structures that represent hierarchical and network relationships. Trees are specialized graphs without cycles, while graphs can represent any arbitrary connections between elements. Understanding trees and graphs is essential for solving complex problems in networking, AI, databases, and many other domains.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [01_Binary_Trees](01_Binary_Trees/README.md) | understand Binary Trees |
| 2. | [02_BST](02_BST/README.md) | understand Binary Search Trees (BST) |
| 3. | [03_AVL_Trees](03_AVL_Trees/README.md) | understand AVL Trees (Self-Balancing BST) |
| 4. | [04_Graph_Representations](04_Graph_Representations/README.md) | understand Graph Representations |
| 5. | [05_Tree_Traversals](05_Tree_Traversals/README.md) | understand Tree Traversals (DFS, BFS, Inorder, Preorder, Postorder) |
| 6. | [06_Basic_Graph_Algorithms](06_Basic_Graph_Algorithms/README.md) | understand Basic Graph Algorithms (BFS, DFS, Connected Components, Cycle Detection, Topological Sort) |

---

## 1. Binary Trees

This topic explains the fundamental tree data structure where each node has at most two children.

**File:** [01_Binary_Trees](01_Binary_Trees/README.md)

**What you will learn:**
- What is a tree (nodes, edges, root, leaves)
- Binary tree definition and properties
- Node structure (data, left, right)
- Types of binary trees (full, complete, perfect, degenerate)
- Tree terminology (height, depth, level, size)

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Node** | Basic unit containing data and child pointers |
| **Root** | Topmost node with no parent |
| **Leaf** | Node with no children |
| **Height** | Number of edges on longest path from node to leaf |
| **Depth** | Number of edges from root to node |
| **Level** | Depth + 1 |

**Node Structure:**
```cpp
struct Node {
    int data;
    Node* left;
    Node* right;
    
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};
```

---

## 2. Binary Search Trees (BST)

This topic explains BST, a binary tree with the property that left subtree contains smaller values and right subtree contains larger values.

**File:** [02_BST](02_BST/README.md)

**What you will learn:**
- BST property (left < root < right)
- BST insertion, deletion, search
- BST inorder traversal gives sorted order
- BST complexity analysis
- Applications of BST

**Key Concepts:**

| Property | Description |
|----------|-------------|
| **Left Subtree** | All nodes have values less than root |
| **Right Subtree** | All nodes have values greater than root |
| **No Duplicates** | Typically unique keys (multiset for duplicates) |

**Complexity:**

| Operation | Average | Worst |
|-----------|---------|-------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |

---

## 3. AVL Trees

This topic explains AVL trees, self-balancing BSTs that maintain O(log n) height.

**File:** [03_AVL_Trees](03_AVL_Trees/README.md)

**What you will learn:**
- AVL tree definition (balance factor -1, 0, 1)
- Balance factor calculation
- Rotations (left, right, left-right, right-left)
- Insertion and deletion with rebalancing
- AVL vs regular BST

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Balance Factor** | height(left) - height(right) |
| **Left Rotation** | Rotate right child up |
| **Right Rotation** | Rotate left child up |
| **Double Rotation** | Combination of two rotations |

**Balance Factor Values:**
```
-1: Right heavy
 0: Balanced
 1: Left heavy
```

---

## 4. Graph Representations

This topic explains different ways to represent graphs in memory.

**File:** [04_Graph_Representations](04_Graph_Representations/README.md)

**What you will learn:**
- Graph terminology (vertices, edges, degree, path, cycle)
- Directed vs Undirected graphs
- Weighted vs Unweighted graphs
- Adjacency Matrix representation
- Adjacency List representation
- Edge List representation
- Space and time complexity comparison

**Key Concepts:**

| Representation | Space | Edge Lookup | Neighbors | Best For |
|----------------|-------|-------------|-----------|----------|
| **Adjacency Matrix** | O(V²) | O(1) | O(V) | Dense graphs |
| **Adjacency List** | O(V+E) | O(V) | O(degree) | Sparse graphs |
| **Edge List** | O(E) | O(E) | O(E) | Edge-centric algorithms |

**Adjacency Matrix Example:**
```cpp
// For n vertices
vector<vector<bool>> adj(n, vector<bool>(n, false));
adj[0][1] = true;  // Edge from 0 to 1
```

**Adjacency List Example:**
```cpp
// For n vertices
vector<vector<int>> adj(n);
adj[0].push_back(1);  // Edge from 0 to 1
adj[1].push_back(0);  // For undirected graph
```

---

## 5. Tree Traversals

This topic explains various ways to traverse trees.

**File:** [05_Tree_Traversals](05_Tree_Traversals/README.md)

**What you will learn:**
- Depth-First Search (DFS) traversals
  - Inorder (Left-Root-Right)
  - Preorder (Root-Left-Right)
  - Postorder (Left-Right-Root)
- Breadth-First Search (BFS) traversal
  - Level Order traversal
- Recursive vs iterative implementations
- Applications of each traversal

**Key Concepts:**

| Traversal | Order | Use Case |
|-----------|-------|----------|
| **Inorder** | Left → Root → Right | Get sorted order (BST) |
| **Preorder** | Root → Left → Right | Create copy of tree |
| **Postorder** | Left → Right → Root | Delete tree, expression evaluation |
| **Level Order** | Level by level (BFS) | Shortest path, breadth-first search |

**Visual Example:**
```
        1
       / \
      2   3
     / \   \
    4   5   6

Inorder:   4 2 5 1 3 6
Preorder:  1 2 4 5 3 6
Postorder: 4 5 2 6 3 1
Level Order: 1 2 3 4 5 6
```

---

## 6. Basic Graph Algorithms

This topic explains fundamental graph algorithms.

**File:** [06_Basic_Graph_Algorithms](06_Basic_Graph_Algorithms/README.md)

**What you will learn:**
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Connected Components detection
- Cycle Detection in directed and undirected graphs
- Topological Sort for DAGs

**Key Concepts:**

| Algorithm | Purpose | Time Complexity | Space Complexity |
|-----------|---------|----------------|------------------|
| **BFS** | Shortest path (unweighted), level order | O(V+E) | O(V) |
| **DFS** | Connectivity, cycle detection | O(V+E) | O(V) |
| **Connected Components** | Find connected subgraphs | O(V+E) | O(V) |
| **Cycle Detection** | Detect cycles in graph | O(V+E) | O(V) |
| **Topological Sort** | Linear ordering of DAG | O(V+E) | O(V) |

**BFS Algorithm:**
```cpp
void BFS(vector<vector<int>>& adj, int start) {
    vector<bool> visited(adj.size(), false);
    queue<int> q;
    
    visited[start] = true;
    q.push(start);
    
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        
        for (int v : adj[u]) {
            if (!visited[v]) {
                visited[v] = true;
                q.push(v);
            }
        }
    }
}
```

**DFS Algorithm:**
```cpp
void DFS(vector<vector<int>>& adj, int u, vector<bool>& visited) {
    visited[u] = true;
    
    for (int v : adj[u]) {
        if (!visited[v]) {
            DFS(adj, v, visited);
        }
    }
}
```

---

### Tree vs Graph Comparison

| Property | Tree | Graph |
|----------|------|-------|
| **Cycles** | No cycles | May have cycles |
| **Edges** | Exactly V-1 edges | Any number of edges |
| **Connectivity** | Always connected | May be disconnected |
| **Root** | Has a root | No root |
| **Direction** | Usually undirected | Directed or undirected |
| **Parent-Child** | Clear hierarchy | No hierarchy |

---

### Prerequisites

Before starting this section, you should have completed:

- [01. Basics](../01.%20Basics/README.md) - Pointers, recursion
- [02. Basic Problems](../02.%20Basic%20Problems/README.md) - Recursion problems
- [04. Data Structures](../04.%20Data%20Structures/README.md) - Queues, stacks, vectors

---

### Sample Tree Implementation

```cpp
#include <iostream>
#include <queue>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;
    
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

// Inorder traversal
void inorder(Node* root) {
    if (!root) return;
    inorder(root->left);
    cout << root->data << " ";
    inorder(root->right);
}

// Level order traversal (BFS)
void levelOrder(Node* root) {
    if (!root) return;
    queue<Node*> q;
    q.push(root);
    
    while (!q.empty()) {
        Node* curr = q.front();
        q.pop();
        cout << curr->data << " ";
        
        if (curr->left) q.push(curr->left);
        if (curr->right) q.push(curr->right);
    }
}

int main() {
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    
    cout << "Inorder: ";
    inorder(root);
    cout << endl;
    
    cout << "Level Order: ";
    levelOrder(root);
    cout << endl;
    
    return 0;
}
```

---

### Sample Graph Implementation

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Graph {
private:
    int V;
    vector<vector<int>> adj;
    
public:
    Graph(int vertices) : V(vertices), adj(vertices) {}
    
    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u);  // For undirected graph
    }
    
    void BFS(int start) {
        vector<bool> visited(V, false);
        queue<int> q;
        
        visited[start] = true;
        q.push(start);
        
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            cout << u << " ";
            
            for (int v : adj[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    q.push(v);
                }
            }
        }
        cout << endl;
    }
    
    void DFS(int start) {
        vector<bool> visited(V, false);
        DFSUtil(start, visited);
        cout << endl;
    }
    
private:
    void DFSUtil(int u, vector<bool>& visited) {
        visited[u] = true;
        cout << u << " ";
        
        for (int v : adj[u]) {
            if (!visited[v]) {
                DFSUtil(v, visited);
            }
        }
    }
};

int main() {
    Graph g(5);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(2, 4);
    
    cout << "BFS from 0: ";
    g.BFS(0);
    
    cout << "DFS from 0: ";
    g.DFS(0);
    
    return 0;
}
```

---

### Learning Path

```
Level 1: Tree Basics
├── Binary Tree
├── BST (Binary Search Tree)
└── Tree Traversals

Level 2: Balanced Trees
├── AVL Trees
└── Tree Traversals (BFS, DFS)

Level 3: Graph Basics
├── Graph Representations
└── BFS and DFS

Level 4: Graph Algorithms
├── Connected Components
├── Cycle Detection
└── Topological Sort
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Forgetting base case in recursion | Always check for null node |
| Stack overflow in deep trees | Use iterative traversal for very deep trees |
| Confusing BFS and DFS use cases | BFS for shortest path, DFS for connectivity |
| Not handling disconnected graphs | Run algorithms from all unvisited nodes |
| Cycle detection without visited set | Always track visited nodes |

---

### Practice Questions

After completing this section, you should be able to:

1. Implement inorder, preorder, postorder traversals
2. Implement level order traversal using queue
3. Insert and delete nodes in BST
4. Balance an AVL tree using rotations
5. Represent a graph using adjacency list and matrix
6. Perform BFS and DFS on graphs
7. Detect cycles in directed and undirected graphs
8. Perform topological sort on DAG

---

### Next Steps

- Go to [01_Binary_Trees](01_Binary_Trees/README.md) to understand Binary Trees.