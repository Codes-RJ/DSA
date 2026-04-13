# Binary Search Trees - Introduction

## 📖 Overview

A Binary Search Tree (BST) is a binary tree data structure that maintains a specific ordering property: for every node, all values in its left subtree are less than the node's value, and all values in its right subtree are greater than the node's value. This ordering property enables efficient searching, insertion, and deletion operations.

BSTs are fundamental to computer science and serve as the foundation for more advanced data structures like AVL trees, Red-Black trees, and B-trees. They are widely used in database indexing, compiler symbol tables, file systems, and network routing algorithms.

---

## 🎯 BST Definition

### Formal Definition

A Binary Search Tree is a binary tree that satisfies the **Binary Search Property**:

For every node `x` in the tree:
- If `y` is a node in the left subtree of `x`, then `y.key ≤ x.key`
- If `y` is a node in the right subtree of `x`, then `y.key ≥ x.key`

### Visual Representation

```
        50
       /  \
      30   80
     / \   / \
    20 40 70 90

Properties:
- 30 and all its descendants (20,40) are < 50
- 80 and all its descendants (70,90) are > 50
- 20 < 30 ✓
- 40 > 30 ✓
- 70 < 80 ✓
- 90 > 80 ✓
```

---

## 📐 BST Property Explained

### The Ordering Rule

For any node `N` in a BST:

| Condition | Requirement |
|-----------|-------------|
| **Left subtree** | All values < N's value |
| **Right subtree** | All values > N's value |
| **Recursive** | Left and right subtrees are also BSTs |
| **Duplicates** | Typically not allowed (or handled explicitly) |

### Why This Property Works

The ordering property enables **binary search**:
1. Compare target with current node
2. If equal → found
3. If smaller → go left (all smaller values are there)
4. If larger → go right (all larger values are there)
5. Repeat until found or leaf reached

---

## 📊 Valid vs Invalid BST

### Example 1: Valid BST

```
        50
       /  \
      30   80
     / \   / \
    20 40 70 90

Check each node:
50: left(30,20,40) < 50 ✓ | right(80,70,90) > 50 ✓
30: left(20) < 30 ✓ | right(40) > 30 ✓
80: left(70) < 80 ✓ | right(90) > 80 ✓
20,40,70,90: leaves (trivially valid)

Result: VALID BST
```

### Example 2: Invalid BST

```
        50
       /  \
      30   80
     / \   / \
    20 60 70 90
         ↑
    60 > 50 but in LEFT subtree!

Check: 60 is in left subtree of 50
But 60 > 50 → violates BST property

Result: INVALID BST
```

### Example 3: Another Invalid BST

```
        50
       /  \
      30   40
     / \    \
    20 25    45
              ↑
    45 is in right subtree of 30 (should be > 30)
    But 45 < 50? Actually 45 is fine for 30
    Wait, let's check root: right child is 40 (should be > 50? NO!)
    
    40 < 50 but is in RIGHT subtree!
    
Result: INVALID BST
```

---

## 📈 Mathematical Properties

### Height and Node Relationships

| Property | Formula | Example |
|----------|---------|---------|
| **Minimum nodes for height h** | h + 1 | h=3 → 4 nodes (skewed) |
| **Maximum nodes for height h** | 2^(h+1) - 1 | h=3 → 15 nodes (perfect) |
| **Minimum height for n nodes** | ⌈log₂(n+1)⌉ - 1 | n=15 → height 3 |
| **Maximum height for n nodes** | n - 1 | n=5 → height 4 |

### Node Distribution

| Level | Maximum Nodes | Cumulative |
|-------|---------------|------------|
| 0 (root) | 1 | 1 |
| 1 | 2 | 3 |
| 2 | 4 | 7 |
| 3 | 8 | 15 |
| h | 2^h | 2^(h+1) - 1 |

### Leaf and Internal Node Relationship

In a **full BST** (every node has 0 or 2 children):
- **Leaves = Internal Nodes + 1**

```
Example:
        50 (internal)
       /  \
    30    80 (internal)
    / \   / \
  20 40 70 90 (all leaves)

Internal nodes: 3 (50, 30, 80)
Leaves: 4 (20, 40, 70, 90)
4 = 3 + 1 ✓
```

---

## ⏱️ Complexity Analysis

### Time Complexity

| Operation | Average Case | Worst Case | Best Case |
|-----------|--------------|------------|-----------|
| **Search** | O(log n) | O(n) | O(1) |
| **Insert** | O(log n) | O(n) | O(1) |
| **Delete** | O(log n) | O(n) | O(1) |
| **Find Min** | O(log n) | O(n) | O(1) |
| **Find Max** | O(log n) | O(n) | O(1) |
| **Inorder Traversal** | O(n) | O(n) | O(n) |

### Space Complexity

| Aspect | Complexity |
|--------|------------|
| **Tree storage** | O(n) |
| **Recursive operations** | O(h) call stack |
| **Iterative operations** | O(1) |

### Why Worst Case O(n)?

When a BST becomes **skewed** (like a linked list):

```
1
 \
  2
   \
    3
     \
      4
       \
        5

Searching for 5 requires traversing all 5 nodes → O(n)
```

---

## 🏗️ BST Terminology

| Term | Definition | Example |
|------|------------|---------|
| **Root** | Topmost node with no parent | 50 |
| **Parent** | Node that has children | 50 is parent of 30,80 |
| **Child** | Node connected to parent | 30,80 are children of 50 |
| **Leaf** | Node with no children | 20,40,70,90 |
| **Internal Node** | Node with at least one child | 50,30,80 |
| **Subtree** | Any node and its descendants | 30,20,40 form a subtree |
| **Height** | Edges on longest path from node to leaf | Height of root = 3 |
| **Depth** | Edges from root to node | Depth of 70 = 2 |
| **Level** | Depth + 1 | Level of 70 = 3 |
| **Successor** | Smallest node greater than current | Successor of 40 is 50 |
| **Predecessor** | Largest node smaller than current | Predecessor of 40 is 30 |

---

## 🔄 BST vs Other Data Structures

### Comparison Table

| Feature | BST (avg) | BST (worst) | Sorted Array | Linked List | Hash Table |
|---------|-----------|-------------|--------------|-------------|------------|
| **Search** | O(log n) | O(n) | O(log n) | O(n) | O(1) avg |
| **Insert** | O(log n) | O(n) | O(n) | O(1) | O(1) avg |
| **Delete** | O(log n) | O(n) | O(n) | O(1) | O(1) avg |
| **Find Min** | O(log n) | O(n) | O(1) | O(1) | O(n) |
| **Find Max** | O(log n) | O(n) | O(1) | O(1) | O(n) |
| **Sorted Traverse** | O(n) | O(n) | O(n) | O(n log n) | O(n log n) |
| **Memory** | O(n) | O(n) | O(n) | O(n) | O(n) |

### When to Use BST

| Use BST When | Use Array When | Use Hash Table When |
|--------------|----------------|---------------------|
| Sorted order needed | Index-based access needed | Fast exact lookup needed |
| Dynamic data | Static data | Order doesn't matter |
| Range queries | Memory is critical | No need for ordering |
| Predecessor/successor | Simple implementation | Keys are well-distributed |

---

## 🎯 Applications of BST

| Application | Description |
|-------------|-------------|
| **Database Indexing** | B-trees and B+ trees are generalizations of BST |
| **Compiler Symbol Tables** | Store variable names and their attributes |
| **File Systems** | Directory structures organized as trees |
| **Network Routing** | Routing tables use tree structures |
| **Spell Checkers** | Dictionary words stored for quick lookup |
| **Auto-complete** | Prefix trees (Tries) are BST-like |
| **3D Graphics** | Binary Space Partition (BSP) trees |
| **Priority Queues** | Can be implemented using BSTs |

---

## 📝 BST Node Structure

### Basic Node Implementation

```cpp
template<typename T>
class BSTNode {
private:
    T data_;
    BSTNode<T>* left_;
    BSTNode<T>* right_;
    
public:
    // Constructor
    BSTNode(const T& value) : data_(value), left_(nullptr), right_(nullptr) {}
    
    // Getters
    T& getData() { return data_; }
    const T& getData() const { return data_; }
    BSTNode<T>* getLeft() { return left_; }
    const BSTNode<T>* getLeft() const { return left_; }
    BSTNode<T>* getRight() { return right_; }
    const BSTNode<T>* getRight() const { return right_; }
    
    // Setters
    void setData(const T& value) { data_ = value; }
    void setLeft(BSTNode<T>* left) { left_ = left; }
    void setRight(BSTNode<T>* right) { right_ = right; }
    
    // Utility methods
    bool isLeaf() const { return !left_ && !right_; }
    bool hasLeft() const { return left_ != nullptr; }
    bool hasRight() const { return right_ != nullptr; }
    bool hasBoth() const { return left_ && right_; }
};
```

---

## 🔍 Basic Operations Overview

### Search Algorithm (Conceptual)

```
1. Start at root
2. If root is null → return false
3. If target equals root value → return true
4. If target < root value → search left subtree
5. If target > root value → search right subtree
6. Repeat until found or leaf reached
```

### Insert Algorithm (Conceptual)

```
1. If tree is empty → create root node
2. Else:
   a. If value < current node → go left
   b. If value > current node → go right
   c. If equal → return (no duplicates)
3. When null is reached → insert new node
```

### Delete Algorithm (Conceptual)

Three cases:
1. **Leaf node**: Simply remove it
2. **Node with one child**: Replace node with its child
3. **Node with two children**: 
   - Find inorder successor (smallest in right subtree)
   - Copy successor value to node
   - Delete successor

---

## 🌲 Traversals Overview

| Traversal | Order | Result for Example Tree |
|-----------|-------|------------------------|
| **Inorder** | Left → Root → Right | 20, 30, 40, 50, 70, 80, 90 |
| **Preorder** | Root → Left → Right | 50, 30, 20, 40, 80, 70, 90 |
| **Postorder** | Left → Right → Root | 20, 40, 30, 70, 90, 80, 50 |

```
        50
       /  \
      30   80
     / \   / \
    20 40 70 90
```

---

## 📊 Types of Binary Search Trees

| Type | Description | Height | Use Case |
|------|-------------|--------|----------|
| **Standard BST** | Basic BST with no balance guarantees | O(n) worst | Simple implementations |
| **AVL Tree** | Height-balanced BST (|BF| ≤ 1) | O(log n) | Read-heavy workloads |
| **Red-Black Tree** | Color-balanced BST | O(log n) | Write-heavy workloads |
| **Treap** | BST + heap property (randomized) | O(log n) expected | Randomized algorithms |
| **Splay Tree** | Self-adjusting with amortized analysis | Amortized O(log n) | Caching applications |
| **B-Tree** | Generalized BST for disk storage | O(log n) | Database indexing |

---

## 💡 Key Insights

1. **BST property** enables binary search, eliminating half the tree at each step
2. **Inorder traversal** of a BST produces sorted order
3. **Height** directly affects performance: shorter = faster
4. **Skewed trees** degenerate to linked lists (O(n) operations)
5. **Balanced BSTs** guarantee O(log n) operations
6. **Successor** is the smallest node larger than current
7. **Predecessor** is the largest node smaller than current

---

## 🎯 Common BST Interview Problems

| Problem | Difficulty | Solution Approach |
|---------|------------|-------------------|
| **Validate BST** | Medium | Inorder traversal or range check |
| **Lowest Common Ancestor** | Easy | Recursive search |
| **K-th Smallest Element** | Medium | Inorder traversal with counter |
| **Convert Sorted Array to BST** | Easy | Recursive middle element |
| **Two Sum in BST** | Medium | Inorder + two pointers |
| **Range Sum Query** | Easy | Traverse nodes in range |
| **BST to Greater Sum Tree** | Medium | Reverse inorder traversal |
| **Recover BST (two swapped nodes)** | Hard | Inorder traversal to find violations |

---

## ✅ Key Takeaways

1. **BST property**: left < root < right (strict inequality typical)
2. **Inorder traversal** gives sorted order in O(n) time
3. **Search, insert, delete** are O(log n) average, O(n) worst case
4. **Worst case** occurs when tree becomes skewed (like linked list)
5. **Balanced variants** (AVL, Red-Black) guarantee O(log n) operations
6. **Successor** and **predecessor** are important for deletion
7. **BSTs are recursive** by nature → recursive algorithms are natural fit

---

## 📚 Prerequisites

Before proceeding, ensure you understand:

- ✅ Binary tree basics
- ✅ Recursion concepts
- ✅ Pointers and dynamic memory
- ✅ Basic sorting principles
- ✅ Time and space complexity analysis

---

## 🚀 Next Steps

After mastering BST basics, proceed to:

1. **BST_Insertion.md** - Learn to insert nodes
2. **BST_Search.md** - Master efficient searching
3. **BST_Deletion.md** - Handle all deletion cases
4. **BST_Traversal.md** - Explore traversal methods
5. **Advanced Topics** - AVL trees, Red-Black trees

---
---

## Next Step

- Go to [02_BST_Insertion.md](02_BST_Insertion.md) to continue with BST Insertion.
