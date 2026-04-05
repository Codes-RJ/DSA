# Tree Basics

## 📖 Overview

A tree is a hierarchical data structure that consists of nodes connected by edges. Unlike arrays, linked lists, stacks, or queues which are linear data structures, trees are non-linear. Trees represent hierarchical relationships, making them ideal for modeling real-world scenarios like file systems, organization charts, and HTML DOM structures.

---

## 🎯 What is a Tree?

A tree is a collection of nodes where:
- One node is designated as the **root**
- Every other node has exactly one **parent**
- Nodes are connected by **edges**
- There are no **cycles** (acyclic)

```
        Root
       /    \
    Child   Child
    /  \      \
 Leaf  Leaf   Leaf
```

---

## 📊 Tree vs Other Data Structures

| Feature | Array | Linked List | Stack/Queue | Tree |
|---------|-------|-------------|-------------|------|
| **Structure** | Linear | Linear | Linear | Hierarchical |
| **Organization** | Sequential | Sequential | Sequential | Parent-child |
| **Traversal** | Single path | Single path | Single path | Multiple paths |
| **Representation** | Index-based | Pointer-based | Pointer-based | Pointer-based |

---

## 📝 Basic Terminology

| Term | Definition | Real-world Analogy |
|------|------------|-------------------|
| **Node** | Fundamental unit containing data | A person in a family tree |
| **Root** | Topmost node with no parent | Ancestor / Founder |
| **Parent** | Node that has children | A parent in a family |
| **Child** | Node connected to a parent | A child in a family |
| **Sibling** | Nodes sharing the same parent | Brothers/sisters |
| **Leaf** | Node with no children | Person with no descendants |
| **Internal Node** | Node with at least one child | Parent/grandparent |
| **Edge** | Connection between two nodes | Family relationship line |
| **Path** | Sequence of edges connecting nodes | Ancestry line |
| **Subtree** | Any node and all its descendants | A branch of the family |

---

## 🏗️ Key Properties

### 1. **Root Property**
- There is exactly one root node
- Root has no parent
- Every tree has one root

### 2. **Parent-Child Property**
- Every non-root node has exactly one parent
- A node can have multiple children
- Parent-child relationships define the tree structure

### 3. **Acyclic Property**
- Trees have no cycles
- There is exactly one path between any two nodes
- Adding any edge creates a cycle

### 4. **Recursive Property**
- Every node in a tree is the root of its own subtree
- Trees are naturally recursive structures
- This property enables recursive algorithms

---

## 📐 Types of Trees

| Tree Type | Description | Example |
|-----------|-------------|---------|
| **General Tree** | Nodes can have any number of children | File system |
| **Binary Tree** | Maximum 2 children per node | Expression tree |
| **Binary Search Tree** | Left < Root < Right | Database index |
| **AVL Tree** | Self-balancing BST | Memory management |
| **Heap** | Complete binary tree with heap property | Priority queue |
| **Trie** | Tree for storing strings | Autocomplete |

---

## 🎯 Real-World Applications

| Application | How Tree is Used |
|-------------|------------------|
| **File System** | Directories and files organized hierarchically |
| **HTML DOM** | Web page structure as a tree |
| **Organization Chart** | Employee reporting structure |
| **Database Indexing** | B-trees and B+ trees for fast search |
| **Expression Parsing** | Arithmetic expression evaluation |
| **Routing Algorithms** | Network routing tables |
| **Game AI** | Decision trees for game moves |
| **Compression** | Huffman coding tree |

---

## 📊 Mathematical Properties

| Property | Formula | Example |
|----------|---------|---------|
| **Nodes vs Edges** | Edges = Nodes - 1 | 10 nodes → 9 edges |
| **Maximum nodes at level L** | 2^L | Level 3 → 8 nodes |
| **Maximum nodes in tree of height H** | 2^(H+1) - 1 | Height 3 → 15 nodes |
| **Minimum height for N nodes** | ⌈log₂(N+1)⌉ - 1 | 15 nodes → height 3 |
| **Leaf count in full tree** | Internal nodes + 1 | 4 internal → 5 leaves |

---

## 🔄 Tree Traversal Overview

| Traversal Type | Order | Use Case |
|----------------|-------|----------|
| **Depth-First (DFS)** | Go deep first | Path finding, tree cloning |
| **Breadth-First (BFS)** | Level by level | Shortest path, level order |
| **Inorder** | Left → Root → Right | BST sorted output |
| **Preorder** | Root → Left → Right | Tree copying |
| **Postorder** | Left → Right → Root | Tree deletion |
| **Level Order** | Level by level | Breadth-first traversal |

---

## 💡 Key Insights

1. **Trees are recursive** - Every node can be seen as the root of its own subtree
2. **No cycles** - There's exactly one path between any two nodes
3. **Edges = Nodes - 1** - A fundamental property of all trees
4. **Height matters** - Shorter trees mean faster operations
5. **Leaf count** - In a full tree, leaves = internal nodes + 1
6. **Recursive algorithms** are natural for trees
7. **Balance** is crucial for performance in search trees

---

## ✅ Key Takeaways

1. A **tree** is a hierarchical, acyclic collection of nodes
2. **Root** is the topmost node with no parent
3. **Leaf** nodes have no children
4. **Edges** connect parent to child
5. **Subtree** is any node with its descendants
6. Trees have **exactly one path** between any two nodes
7. **N nodes** in a tree have **N-1 edges**

---

## 🚀 Next Steps

After understanding tree basics, proceed to:

1. **Binary Trees** - Trees with at most 2 children
2. **Tree Traversals** - Different ways to visit nodes
3. **Binary Search Trees** - Ordered binary trees
4. **Self-balancing Trees** - AVL, Red-Black trees
5. **Advanced Tree Structures** - B-trees, Segment trees

---