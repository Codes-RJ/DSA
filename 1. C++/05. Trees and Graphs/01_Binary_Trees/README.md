# README.md

## Binary Trees - Complete Guide

### Overview

A binary tree is a hierarchical data structure in which each node has at most two children, referred to as the left child and the right child. Binary trees are the foundation for many advanced data structures like Binary Search Trees (BST), AVL Trees, Red-Black Trees, and Heaps. They are widely used in expression parsing, file systems, and efficient searching and sorting algorithms.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [01_Tree_Basics.md](01_Tree_Basics.md) | understand Tree Basics (terminology, properties) |
| 2. | [02_Tree_Node_Structure.md](02_Tree_Node_Structure.md) | understand Tree Node Structure |
| 3. | [03_Tree_Properties.md](03_Tree_Properties.md) | understand Tree Properties (height, depth, level) |
| 4. | [04_Binary_Tree_Implementation.md](04_Binary_Tree_Implementation.md) | understand Binary Tree Implementation |
| 5. | [05_Tree_Operations.md](05_Tree_Operations.md) | understand Tree Operations (insert, delete, search) |
| 6. | [README.md](README.md) | understand Binary Trees Overview |

---

## 1. Tree Basics

This topic introduces fundamental tree terminology and concepts.

**File:** [01_Tree_Basics.md](01_Tree_Basics.md)

**What you will learn:**
- What is a tree data structure
- Tree terminology (node, root, leaf, parent, child, sibling)
- Binary tree definition (max two children per node)
- Types of binary trees (full, complete, perfect, degenerate)
- Tree vs linear data structures

**Key Concepts:**

| Term | Definition |
|------|------------|
| **Node** | Basic unit containing data and links to children |
| **Root** | Topmost node with no parent |
| **Leaf** | Node with no children |
| **Internal Node** | Node with at least one child |
| **Parent** | Node that has a child |
| **Child** | Node directly under another node |
| **Sibling** | Nodes sharing the same parent |
| **Subtree** | Any node and its descendants |

**Types of Binary Trees:**

| Type | Description |
|------|-------------|
| **Full Binary Tree** | Every node has 0 or 2 children |
| **Complete Binary Tree** | All levels filled except possibly last, filled left to right |
| **Perfect Binary Tree** | All internal nodes have 2 children, all leaves at same level |
| **Degenerate Tree** | Each node has exactly one child (like a linked list) |
| **Balanced Binary Tree** | Height difference between left and right subtrees ≤ 1 |

---

## 2. Tree Node Structure

This topic explains how to represent a tree node in C++.

**File:** [02_Tree_Node_Structure.md](02_Tree_Node_Structure.md)

**What you will learn:**
- Node structure for binary trees
- Data members (data, left, right)
- Constructors for tree nodes
- Pointer-based representation
- Array-based representation (for complete trees)

**Key Concepts:**

| Representation | Pros | Cons |
|----------------|------|------|
| **Pointer-based** | Dynamic size, memory efficient | Extra memory for pointers |
| **Array-based** | Cache friendly, no pointers | Wasted space for incomplete trees |

**Pointer-based Node Structure:**
```cpp
struct Node {
    int data;
    Node* left;
    Node* right;
    
    // Constructor
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};
```

**Array-based Representation (for complete trees):**
```cpp
// For node at index i
// Left child: 2*i + 1
// Right child: 2*i + 2
// Parent: (i-1)/2

vector<int> tree;
tree[0] = root;
tree[1] = leftChild;
tree[2] = rightChild;
```

---

## 3. Tree Properties

This topic explains mathematical properties of trees.

**File:** [03_Tree_Properties.md](03_Tree_Properties.md)

**What you will learn:**
- Height of a tree (number of edges on longest path)
- Depth of a node (distance from root)
- Level of a node (depth + 1)
- Size of a tree (number of nodes)
- Relationships between nodes, height, and levels

**Key Concepts:**

| Property | Formula | Description |
|----------|---------|-------------|
| **Maximum nodes at level L** | 2^L | Number of nodes at level L (root level 0) |
| **Maximum nodes in height H** | 2^(H+1) - 1 | Complete tree with height H |
| **Minimum height for N nodes** | ⌈log₂(N+1)⌉ - 1 | Balanced tree |
| **Leaf nodes in full tree** | Internal nodes + 1 | For full binary trees |

**Height vs Depth:**
```
Level 0:      A      ← root (depth=0)
             / \
Level 1:    B   C    ← depth=1
           / \   \
Level 2:  D   E   F  ← depth=2
               \
Level 3:        G    ← depth=3

Height of tree = 3 (edges from root to deepest leaf)
Depth of node G = 3
Level of node G = 4
```

---

## 4. Binary Tree Implementation

This topic provides complete implementation of binary trees.

**File:** [04_Binary_Tree_Implementation.md](04_Binary_Tree_Implementation.md)

**What you will learn:**
- Creating a binary tree node
- Building a tree manually
- Inserting nodes
- Tree traversal methods
- Memory management (deleting nodes)

**Key Concepts:**

| Operation | Description | Complexity |
|-----------|-------------|------------|
| **Create Node** | Allocate memory for new node | O(1) |
| **Insert** | Add node to tree (unspecified position) | O(n) |
| **Traverse** | Visit all nodes in specific order | O(n) |
| **Delete Tree** | Free all allocated memory | O(n) |

**Basic Implementation:**
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

class BinaryTree {
private:
    Node* root;
    
    void inorderHelper(Node* node) {
        if (!node) return;
        inorderHelper(node->left);
        cout << node->data << " ";
        inorderHelper(node->right);
    }
    
    void preorderHelper(Node* node) {
        if (!node) return;
        cout << node->data << " ";
        preorderHelper(node->left);
        preorderHelper(node->right);
    }
    
    void postorderHelper(Node* node) {
        if (!node) return;
        postorderHelper(node->left);
        postorderHelper(node->right);
        cout << node->data << " ";
    }
    
    void deleteTree(Node* node) {
        if (!node) return;
        deleteTree(node->left);
        deleteTree(node->right);
        delete node;
    }
    
public:
    BinaryTree() : root(nullptr) {}
    
    ~BinaryTree() {
        deleteTree(root);
    }
    
    void setRoot(Node* node) { root = node; }
    Node* getRoot() { return root; }
    
    void inorder() {
        inorderHelper(root);
        cout << endl;
    }
    
    void preorder() {
        preorderHelper(root);
        cout << endl;
    }
    
    void postorder() {
        postorderHelper(root);
        cout << endl;
    }
    
    void levelOrder() {
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
        cout << endl;
    }
};
```

---

## 5. Tree Operations

This topic explains various operations on binary trees.

**File:** [05_Tree_Operations.md](05_Tree_Operations.md)

**What you will learn:**
- Computing height of a tree
- Counting nodes (size)
- Counting leaf nodes
- Counting internal nodes
- Finding maximum/minimum value
- Checking if tree is balanced
- Mirroring a tree

**Key Concepts:**

| Operation | Implementation | Complexity |
|-----------|----------------|------------|
| **Height** | max(leftHeight, rightHeight) + 1 | O(n) |
| **Size** | leftSize + rightSize + 1 | O(n) |
| **Leaf Count** | Count nodes with no children | O(n) |
| **Max/Min** | Compare node with left/right max/min | O(n) |
| **Mirror** | Swap left and right children recursively | O(n) |

**Operation Implementations:**
```cpp
// Compute height of tree
int getHeight(Node* node) {
    if (!node) return -1;  // or 0 depending on definition
    return 1 + max(getHeight(node->left), getHeight(node->right));
}

// Count total nodes
int getSize(Node* node) {
    if (!node) return 0;
    return 1 + getSize(node->left) + getSize(node->right);
}

// Count leaf nodes
int countLeaves(Node* node) {
    if (!node) return 0;
    if (!node->left && !node->right) return 1;
    return countLeaves(node->left) + countLeaves(node->right);
}

// Find maximum value
int findMax(Node* node) {
    if (!node) return INT_MIN;
    int leftMax = findMax(node->left);
    int rightMax = findMax(node->right);
    return max(node->data, max(leftMax, rightMax));
}

// Check if tree is balanced (height diff ≤ 1)
bool isBalanced(Node* node) {
    if (!node) return true;
    int leftHeight = getHeight(node->left);
    int rightHeight = getHeight(node->right);
    
    if (abs(leftHeight - rightHeight) > 1) return false;
    
    return isBalanced(node->left) && isBalanced(node->right);
}

// Mirror the tree
void mirror(Node* node) {
    if (!node) return;
    
    mirror(node->left);
    mirror(node->right);
    
    swap(node->left, node->right);
}
```

---

### Binary Tree Visual Representation

```
        1  ← Root
       / \
      2   3
     / \   \
    4   5   6
       /
      7

- Root: 1
- Leaves: 4, 7, 6
- Internal nodes: 1, 2, 3, 5
- Height: 3 (edges from root to deepest leaf 7)
- Size: 7 nodes
```

---

### Complexity Summary

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Create Node** | O(1) | O(1) |
| **Insert (unspecified)** | O(n) | O(1) |
| **Search (unsorted)** | O(n) | O(1) |
| **Height** | O(n) | O(h) recursion stack |
| **Size** | O(n) | O(h) recursion stack |
| **Traversal** | O(n) | O(h) recursion stack |
| **Mirror** | O(n) | O(h) recursion stack |

---

### Prerequisites

Before starting this section, you should have completed:

- [01. Basics](../../01.%20Basics/README.md) - Pointers, recursion
- [04. Data Structures](../../04.%20Data%20Structures/README.md) - Queues (for level order)

---

### Sample Usage

```cpp
#include <iostream>
using namespace std;

int main() {
    // Create nodes
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->right->right = new Node(6);
    
    BinaryTree tree;
    tree.setRoot(root);
    
    cout << "Inorder: ";
    tree.inorder();     // 4 2 5 1 3 6
    
    cout << "Preorder: ";
    tree.preorder();    // 1 2 4 5 3 6
    
    cout << "Postorder: ";
    tree.postorder();   // 4 5 2 6 3 1
    
    cout << "Level Order: ";
    tree.levelOrder();  // 1 2 3 4 5 6
    
    cout << "Height: " << getHeight(root) << endl;
    cout << "Size: " << getSize(root) << endl;
    cout << "Leaves: " << countLeaves(root) << endl;
    
    return 0;
}
```

---

### Learning Path

```
Level 1: Basics
├── Tree Terminology
├── Node Structure
└── Tree Properties

Level 2: Implementation
├── Creating Nodes
├── Building Trees
└── Memory Management

Level 3: Traversals
├── Inorder
├── Preorder
├── Postorder
└── Level Order

Level 4: Operations
├── Height, Size
├── Count Leaves
├── Find Max/Min
├── Check Balance
└── Mirror Tree
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Forgetting to check for null before accessing children | Always check `if (node)` |
| Memory leaks from dynamically allocated nodes | Delete entire tree in destructor |
| Stack overflow in deep trees | Use iterative traversal for very deep trees |
| Confusing height definitions | Decide: edges vs nodes, be consistent |
| Not handling empty tree | Check for null root in all operations |

---

### Practice Questions

After completing this section, you should be able to:

1. Implement a binary tree node structure
2. Build a binary tree manually
3. Perform all four traversals (inorder, preorder, postorder, level order)
4. Compute height and size of a tree
5. Count leaf and internal nodes
6. Find maximum and minimum values
7. Check if a tree is balanced
8. Mirror a binary tree

---

### Next Steps

- Go to [01_Tree_Basics.md](01_Tree_Basics.md) to understand Tree Basics.