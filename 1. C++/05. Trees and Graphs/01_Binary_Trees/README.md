# Binary Trees - Complete Guide

## 📖 Overview

A binary tree is a hierarchical data structure where each node has at most two children, referred to as the left child and the right child. Binary trees are the foundation for many advanced data structures like Binary Search Trees (BST), AVL Trees, Heaps, and expression trees.

---

## 🎯 Key Characteristics

| Property | Description |
|----------|-------------|
| **Maximum children** | 2 (left and right) |
| **Root** | Topmost node with no parent |
| **Leaf** | Node with no children |
| **Internal Node** | Node with at least one child |
| **Edge** | Connection between parent and child |

---

## 📊 Types of Binary Trees

| Type | Description | Example |
|------|-------------|---------|
| **Full Binary Tree** | Every node has 0 or 2 children | Huffman coding tree |
| **Complete Binary Tree** | All levels filled except possibly last, filled left to right | Binary Heap |
| **Perfect Binary Tree** | All internal nodes have 2 children, all leaves at same level | Theoretical ideal |
| **Balanced Binary Tree** | Height difference ≤ 1 for all nodes | AVL Tree |
| **Degenerate/Skewed Tree** | Each node has only one child | Essentially a linked list |

---

## 📐 Mathematical Properties

| Property | Formula | Example (height=3) |
|----------|---------|-------------------|
| Maximum nodes at level L | 2^L | 2^3 = 8 nodes |
| Maximum nodes in tree of height H | 2^(H+1) - 1 | 2^4 - 1 = 15 nodes |
| Minimum height for N nodes | ⌈log₂(N+1)⌉ - 1 | For 15 nodes, height=3 |
| Number of leaf nodes in full tree | Internal nodes + 1 | If 4 internal nodes, 5 leaves |
| Relationship: L = I + 1 | L=leaves, I=internal nodes | Always true for full trees |

---

## 🏗️ Node Structure

```cpp
struct Node {
    int data;
    Node* left;
    Node* right;
    
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};
```

---

## 📊 Binary Tree vs Other Trees

| Feature | Binary Tree | General Tree | BST |
|---------|-------------|--------------|-----|
| Max children | 2 | Unlimited | 2 |
| Order property | No | No | Yes (left < root < right) |
| Search time | O(n) | O(n) | O(log n) average |
| Use case | Expression trees | File systems | Fast lookup |

---

## 🎯 Common Applications

| Application | Description |
|-------------|-------------|
| **Expression Trees** | Parsing mathematical expressions |
| **Huffman Coding** | Data compression |
| **Binary Heaps** | Priority queues |
| **Syntax Trees** | Compiler design |
| **Decision Trees** | Machine learning |
| **Binary Space Partition** | Computer graphics |

---

## 📝 Terminology Deep Dive

| Term | Definition | Example |
|------|------------|---------|
| **Root** | Node with no parent | Topmost node |
| **Parent** | Node that has children | Node A with children B, C |
| **Child** | Node directly connected to parent | B and C are children of A |
| **Sibling** | Nodes sharing same parent | B and C are siblings |
| **Leaf** | Node with no children | End nodes |
| **Ancestor** | Parent, grandparent, etc. | Root is ancestor of all |
| **Descendant** | Child, grandchild, etc. | Leaves are descendants of root |
| **Subtree** | Any node and its descendants | Tree rooted at any node |
| **Height** | Max edges from node to leaf | Root height = longest path |
| **Depth** | Edges from root to node | Root depth = 0 |

---

## ⏱️ Complexity Summary

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Insertion (unsorted) | O(1) for position known, O(n) to find | O(1) |
| Deletion | O(1) for node known, O(n) to find | O(1) |
| Search | O(n) worst case | O(1) |
| Traversal (all methods) | O(n) | O(h) for recursion stack |

---

## ✅ Key Takeaways

1. **Binary trees** have at most two children per node
2. **Full vs Complete vs Perfect** - understand the differences
3. **Height** of a tree is the longest path from root to leaf
4. **Depth** of a node is distance from root
5. **Mathematical properties** help analyze tree efficiency
6. **Leaf count** in full binary trees is always internal nodes + 1

---