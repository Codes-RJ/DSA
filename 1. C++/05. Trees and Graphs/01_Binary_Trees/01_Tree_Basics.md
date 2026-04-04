# Tree Basics and Terminology

## Introduction
A tree is a non-linear hierarchical data structure consisting of nodes connected by edges. Unlike linear data structures (arrays, linked lists), trees represent relationships with a parent-child hierarchy.

## Basic Tree Terminology

### Core Components
- **Node**: Fundamental unit containing data and pointers to child nodes
- **Edge**: Connection between two nodes
- **Root**: Topmost node with no parent
- **Leaf**: Node with no children (also called external node)
- **Internal Node**: Node with at least one child

### Relationships
- **Parent**: Node that has child nodes
- **Child**: Node directly connected to another node when moving away from root
- **Sibling**: Nodes with the same parent
- **Ancestor**: Any node on the path from root to current node
- **Descendant**: Any node reachable from current node by following child edges

### Levels and Depth
- **Level**: Distance from root (root is level 0)
- **Depth**: Number of edges from root to node
- **Height**: Number of edges on longest path from node to leaf
- **Height of Tree**: Height of root node

## Binary Tree Properties

### Definition
A binary tree is a tree where each node has at most two children, designated as left and right.

### Types of Binary Trees

#### 1. Strict Binary Tree
Every node has either 0 or 2 children (no nodes with only one child).

```
    A
   / \
  B   C
 / \
D   E
```

#### 2. Full Binary Tree
Every node except leaves has exactly 2 children.

```
      A
     / \
    B   C
   / \ / \
  D  E F  G
```

#### 3. Complete Binary Tree
All levels except possibly the last are completely filled, and all nodes are as far left as possible.

```
      A
     / \
    B   C
   / \ /
  D  E F
```

#### 4. Perfect Binary Tree
All internal nodes have 2 children and all leaves are at the same level.

```
      A
     / \
    B   C
   / \ / \
  D  E F  G
```

#### 5. Balanced Binary Tree
Height difference between left and right subtrees for every node is not more than 1.

## Mathematical Properties

### Maximum Nodes
- Maximum nodes at level `i`: `2^i`
- Maximum nodes in tree of height `h`: `2^(h+1) - 1`

### Minimum Height
For a binary tree with `n` nodes, minimum height is:
```
h_min = ⌊log₂(n+1)⌋ - 1
```

### Minimum Nodes
For a binary tree of height `h`, minimum nodes is:
```
n_min = h + 1
```

### Leaf Nodes
In a full binary tree:
- Number of leaf nodes = Number of internal nodes + 1
- Total nodes = 2 × leaf nodes - 1

## Tree Representation Methods

### 1. Pointer-Based (Dynamic) Representation
```cpp
struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;
};
```

### 2. Array-Based Representation
For complete binary trees, nodes can be stored in array:
- Parent of node at index `i`: `(i-1)/2`
- Left child of node at index `i`: `2*i + 1`
- Right child of node at index `i`: `2*i + 2`

## Applications of Binary Trees

### Computer Science
- **Expression Trees**: Represent arithmetic expressions
- **Binary Search Trees**: Efficient searching and sorting
- **Huffman Trees**: Data compression algorithms
- **Syntax Trees**: Compiler design and parsing

### Real World
- **File Systems**: Directory hierarchies
- **Organization Charts**: Company structures
- **Decision Trees**: Machine learning and AI
- **Family Trees**: Genealogical relationships

## Advantages of Binary Trees

1. **Hierarchical Representation**: Natural way to represent hierarchical data
2. **Efficient Searching**: Binary search trees provide O(log n) search
3. **Sorted Data**: Inorder traversal yields sorted data
4. **Flexible Size**: Can grow and shrink dynamically
5. **Memory Efficiency**: No wasted space for sparse trees

## Limitations

1. **Unbalanced Trees**: Can degenerate to linked list (O(n) operations)
2. **Memory Overhead**: Pointer storage requires extra memory
3. **Complex Operations**: Deletion and balancing can be complex
4. **Recursive Nature**: May cause stack overflow for deep trees

## Common Operations

### Basic Operations
- **Insertion**: Add new node maintaining tree properties
- **Deletion**: Remove node while preserving structure
- **Search**: Find specific value in tree
- **Traversal**: Visit all nodes in specific order

### Traversal Methods
- **Depth-First**: Inorder, Preorder, Postorder
- **Breadth-First**: Level order traversal

## Time Complexity Analysis

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Search    | O(log n)     | O(n)       |
| Insertion | O(log n)     | O(n)       |
| Deletion  | O(log n)     | O(n)       |
| Traversal | O(n)         | O(n)       |

## Best Practices

1. **Always Initialize Pointers**: Set left/right to nullptr
2. **Handle Memory**: Proper allocation and deallocation
3. **Check for Empty Tree**: Handle null root cases
4. **Balance Trees**: Use self-balancing trees when needed
5. **Recursive Design**: Many tree operations are naturally recursive

## Summary

Binary trees provide a powerful way to organize and access data hierarchically. Understanding the terminology, properties, and types of binary trees is essential before moving to more complex tree structures like BSTs and AVL trees.
