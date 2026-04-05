# Tree Properties

## 📖 Overview

Understanding tree properties is essential for analyzing tree performance, implementing algorithms, and choosing the right tree structure for specific problems. This guide covers all fundamental properties of trees, including height, depth, size, balance factors, and their mathematical relationships.

---

## 🎯 Core Properties

| Property | Definition | Symbol |
|----------|------------|--------|
| **Size** | Total number of nodes in the tree | n |
| **Height** | Maximum number of edges from root to leaf | h |
| **Depth** | Number of edges from root to a specific node | d |
| **Level** | Depth + 1 | L |
| **Degree** | Number of children a node has | deg(node) |
| **Leaf Count** | Number of nodes with degree 0 | L |
| **Internal Nodes** | Nodes with at least one child | I |

---

## 📐 Height and Depth

### Height Definition

```
Tree height = length of longest path from root to leaf (in edges)

        Root (height = 2)
        / \
    Node1   Node2 (height = 1)
    /         \
  Leaf       Leaf (height = 0)

Height = 2 (edges: Root → Node1 → Leaf)
```

### Depth Definition

```
Depth of Root = 0
Depth of children = parent depth + 1

        Root (depth = 0)
        / \
    Node1   Node2 (depth = 1)
    /         \
  Leaf       Leaf (depth = 2)
```

### Height vs Depth Relationship

| Relationship | Formula |
|--------------|---------|
| Node height | max(child heights) + 1 |
| Leaf height | 0 |
| Tree height | height(root) |
| Node depth | parent depth + 1 |
| Root depth | 0 |

---

## 📊 Size Properties

### Node Count Relationships

| Property | Formula | Example |
|----------|---------|---------|
| **Maximum nodes at level L** | 2^L | Level 3 → 8 nodes |
| **Maximum nodes in tree of height h** | 2^(h+1) - 1 | h=3 → 15 nodes |
| **Minimum nodes in tree of height h** | h + 1 | h=3 → 4 nodes (skewed) |
| **Minimum height for n nodes** | ⌈log₂(n+1)⌉ - 1 | n=15 → height=3 |
| **Maximum height for n nodes** | n - 1 | n=5 → height=4 (skewed) |

### Complete Binary Tree Properties

```cpp
// For a complete binary tree with n nodes:
// Height = floor(log₂(n))
// Leaves = ceil(n/2)
// Internal nodes = floor(n/2)

int getHeightFromNodes(int n) {
    return floor(log2(n));
}

int getLeavesFromNodes(int n) {
    return (n + 1) / 2;
}
```

---

## 🔢 Degree and Leaf Relationships

### Full Binary Tree Property

```
In a full binary tree (every node has 0 or 2 children):
    Leaves = Internal Nodes + 1
    
    Example:
        Root (internal)
        / \
     Node   Node (internal)
     / \   / \
   L   L L   L
    
    Internal nodes = 3
    Leaves = 4
    4 = 3 + 1 ✓
```

### Proof: L = I + 1

```
Total edges = n - 1
Total edges also = sum of degrees = 2I + L (since leaves have degree 0)
n = I + L

Therefore:
2I + L = (I + L) - 1
2I + L = I + L - 1
I = L - 1
L = I + 1
```

---

## ⚖️ Balance Properties

### Balance Factor

```
Balance Factor = height(left subtree) - height(right subtree)

Values: -1, 0, 1 for AVL trees
```

### Balance Types

| Type | Condition | Height Difference |
|------|-----------|-------------------|
| **Perfectly Balanced** | All levels completely filled | 0 |
| **Height-Balanced** | |BF| ≤ 1 for all nodes | ≤ 1 |
| **Weight-Balanced** | Left and right sizes are proportional | Varies |
| **Skewed** | All nodes on one side | n-1 |

---

## 📈 Path Properties

### Internal Path Length (IPL)

```
IPL = sum of depths of all nodes

For a perfect binary tree of height h:
IPL = ∑(i * 2^i) for i = 0 to h

Example (h=2):
Level 0: 1 node × 0 = 0
Level 1: 2 nodes × 1 = 2
Level 2: 4 nodes × 2 = 8
IPL = 10
```

### External Path Length (EPL)

```
EPL = IPL + 2n (for full binary trees)

Or directly: EPL = sum of depths of all null pointers
```

---

## 🎯 Level Properties

### Level Numbering

```
Level 0 (root):     1 node
Level 1:            2 nodes
Level 2:            4 nodes
Level L:            2^L nodes (maximum)
```

### Array Indexing (for complete binary trees)

```
For node at index i (0-based):
    Left child index  = 2i + 1
    Right child index = 2i + 2
    Parent index      = (i - 1) / 2

Example (index 0 = root):
    Left child: 1
    Right child: 2
```

---

## 📊 Complexity Analysis

### Operation Complexities

| Operation | Best Case | Average Case | Worst Case |
|-----------|-----------|--------------|------------|
| **Search** | O(1) at root | O(log n) balanced | O(n) skewed |
| **Insert** | O(1) at root | O(log n) balanced | O(n) skewed |
| **Delete** | O(1) at root | O(log n) balanced | O(n) skewed |
| **Traversal** | O(n) | O(n) | O(n) |

### Space Complexity

```
Space = O(n) for storing n nodes
Plus recursion stack for traversals: O(h)
```

---

## 🔧 Useful Formulas

```cpp
// Calculate tree height recursively
int getHeight(Node* root) {
    if (!root) return -1;  // or 0 depending on definition
    return 1 + max(getHeight(root->left), getHeight(root->right));
}

// Calculate tree size recursively
int getSize(Node* root) {
    if (!root) return 0;
    return 1 + getSize(root->left) + getSize(root->right);
}

// Calculate number of leaves
int getLeafCount(Node* root) {
    if (!root) return 0;
    if (!root->left && !root->right) return 1;
    return getLeafCount(root->left) + getLeafCount(root->right);
}

// Calculate number of internal nodes
int getInternalCount(Node* root) {
    if (!root || (!root->left && !root->right)) return 0;
    return 1 + getInternalCount(root->left) + getInternalCount(root->right);
}
```

---

## 📝 Quick Reference Table

| Property | Formula | When to Use |
|----------|---------|-------------|
| **Height** | max(child heights) + 1 | Complexity analysis |
| **Size** | 1 + left size + right size | Memory estimation |
| **Leaves** | nodes with no children | Tree classification |
| **Internal nodes** | nodes with children | Tree classification |
| **Balance factor** | left height - right height | AVL tree validation |
| **IPL** | sum of all depths | Average search time |
| **Max nodes at level L** | 2^L | Capacity planning |

---

## ✅ Key Takeaways

1. **Height** = longest path from root to leaf (in edges)
2. **Depth** = distance from root to node
3. **Size** = total number of nodes
4. **Full binary tree**: L = I + 1
5. **Complete binary tree**: Can be stored in array
6. **Perfect binary tree**: All levels completely filled
7. **Skewed tree**: Worst-case for operations

---