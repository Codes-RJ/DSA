# README.md

## 📖 Overview

A Binary Search Tree (BST) is a binary tree data structure that maintains a specific ordering property: for every node, all values in its left subtree are less than the node's value, and all values in its right subtree are greater than the node's value. This property enables efficient searching, insertion, and deletion operations in O(log n) time on average.

BSTs are fundamental to computer science and form the basis for more advanced data structures like AVL trees, Red-Black trees, and B-trees. They are used extensively in database indexing, memory management, and compiler symbol tables.

---

## 🎯 Why BST Matters

| Application | Description |
|-------------|-------------|
| **Database Indexing** | B-trees and B+ trees are generalizations of BSTs |
| **Symbol Tables** | Compilers use BSTs to store variable names |
| **File Systems** | Directory structures can be organized as BSTs |
| **Priority Queues** | Can be implemented using BSTs |
| **Spell Checkers** | Dictionary words stored for quick lookup |
| **Network Routing** | Routing tables use tree structures |

---

## 📚 Complete Folder Structure

```
02_BST/
├── README.md                       # This file - Complete folder guide
├── 01_BST_Introduction.md          # BST definition, properties, terminology
├── 02_BST_Insertion.md             # Insert algorithm with all cases
├── 03_BST_Deletion.md              # Delete algorithm (3 cases)
├── 04_BST_Search.md                # Search algorithm and analysis
└── 05_BST_Traversal.md             # Inorder, Preorder, Postorder
```

---

## 📊 BST Property - Deep Dive

### The Ordering Rule

For any node N in a BST:
- All nodes in the **left subtree** have values **less than** N's value
- All nodes in the **right subtree** have values **greater than** N's value
- The left and right subtrees are also BSTs
- Typically, duplicate values are not allowed

### Visual Example

```
Valid BST:

        50
       /  \
      30   80
     / \   / \
    20 40 70 90

Check: 30 < 50 ✓ | 80 > 50 ✓ | 20 < 30 ✓ | 40 > 30 ✓ | 70 < 80 ✓ | 90 > 80 ✓
```

### Invalid BST (Violation)

```
        50
       /  \
      30   80
     / \   / \
    20 60 70 90
         ↑
    60 > 50 but in LEFT subtree - VIOLATION!
```

---

## 📐 Mathematical Properties

| Property | Formula | Example (height=3) |
|----------|---------|-------------------|
| **Minimum nodes for height h** | h + 1 | 4 nodes (skewed) |
| **Maximum nodes for height h** | 2^(h+1) - 1 | 15 nodes (perfect) |
| **Minimum height for n nodes** | ⌈log₂(n+1)⌉ - 1 | 15 nodes → height 3 |
| **Maximum height for n nodes** | n - 1 | 5 nodes → height 4 |
| **Number of leaf nodes** | I + 1 (for full BST) | Internal + 1 |

---

## ⏱️ Complete Complexity Analysis

### Time Complexity Table

| Operation | Average Case | Worst Case | Best Case |
|-----------|--------------|------------|-----------|
| **Search** | O(log n) | O(n) | O(1) |
| **Insert** | O(log n) | O(n) | O(1) |
| **Delete** | O(log n) | O(n) | O(1) |
| **Find Min** | O(log n) | O(n) | O(1) |
| **Find Max** | O(log n) | O(n) | O(1) |
| **Inorder Traversal** | O(n) | O(n) | O(n) |
| **Preorder Traversal** | O(n) | O(n) | O(n) |
| **Postorder Traversal** | O(n) | O(n) | O(n) |
| **Height Calculation** | O(n) | O(n) | O(n) |

### Space Complexity

| Operation | Space |
|-----------|-------|
| **All operations** | O(1) for iterative |
| **Recursive operations** | O(h) for call stack |

### Why Worst Case O(n)?

```
Skewed BST (like a linked list):
    1
     \
      2
       \
        3
         \
          4
           \
            5

Search for 5 requires traversing all 5 nodes → O(n)
```

---

## 🔧 BST vs Other Data Structures

| Operation | BST (avg) | BST (worst) | Sorted Array | Linked List | Hash Table |
|-----------|-----------|-------------|--------------|-------------|------------|
| **Search** | O(log n) | O(n) | O(log n) | O(n) | O(1) avg |
| **Insert** | O(log n) | O(n) | O(n) | O(1) | O(1) avg |
| **Delete** | O(log n) | O(n) | O(n) | O(1) | O(1) avg |
| **Traverse** | O(n) | O(n) | O(n) | O(n) | O(n) |
| **Sorted order** | Yes | Yes | Yes | No | No |

---

## 🏗️ BST Node Structure

```cpp
template<typename T>
class BSTNode {
private:
    T data;
    BSTNode<T>* left;
    BSTNode<T>* right;
    
public:
    BSTNode(const T& value) : data(value), left(nullptr), right(nullptr) {}
    
    // Getters and setters
    T& getData() { return data; }
    BSTNode<T>* getLeft() { return left; }
    BSTNode<T>* getRight() { return right; }
    void setLeft(BSTNode<T>* node) { left = node; }
    void setRight(BSTNode<T>* node) { right = node; }
    
    // Utility methods
    bool isLeaf() const { return !left && !right; }
    bool hasLeft() const { return left != nullptr; }
    bool hasRight() const { return right != nullptr; }
    bool hasBoth() const { return left && right; }
};
```

---

## 📝 Basic BST Operations Overview

### Insertion

```
Insert 50:        Insert 30:        Insert 80:
    50                50                50
                      /                 / \
                     30                30  80
```

### Deletion (Three Cases)

```
Case 1: Leaf node        Case 2: One child      Case 3: Two children
    50                      50                      50
   /  \                    /  \                    /  \
  30  80    delete 30     30  80   delete 30      30  80
       ↓                       ↓                       ↓
    50                      50                      55
      \                      / \                    /  \
      80                    55  80                 35   80
                           (55 replaces 30)
```

### Search

```
Search for 70:
    50 → 80 → 70 (found)
    
Search for 25:
    50 → 30 → 20 → (not found)
```

---

## 🌲 Traversals Overview

| Traversal | Order | Use Case |
|-----------|-------|----------|
| **Inorder** | Left → Root → Right | Sorted output |
| **Preorder** | Root → Left → Right | Tree copying |
| **Postorder** | Left → Right → Root | Tree deletion |

```
        50
       /  \
      30   80
     / \   / \
    20 40 70 90

Inorder:   20, 30, 40, 50, 70, 80, 90
Preorder:  50, 30, 20, 40, 80, 70, 90
Postorder: 20, 40, 30, 70, 90, 80, 50
```

---

## 🎯 Common BST Problems

| Problem | Solution Approach |
|---------|-------------------|
| **Lowest Common Ancestor** | Recursively search both subtrees |
| **Validate BST** | Check range constraints |
| **K-th Smallest Element** | Inorder traversal with counter |
| **Convert Sorted Array to BST** | Pick middle element as root |
| **Range Sum Query** | Traverse only relevant nodes |
| **Two Sum in BST** | Use inorder traversal + two pointers |

---

## 🔄 Recursive vs Iterative Implementation

| Operation | Recursive | Iterative |
|-----------|-----------|-----------|
| **Insert** | Simple, elegant | Uses while loop |
| **Search** | Simple, elegant | Uses while loop |
| **Delete** | Complex but clean | Very complex |
| **Traversal** | Natural fit | Requires explicit stack |

---

## 💡 Best Practices

1. **Always maintain BST property** after modifications
2. **Use recursion** for simpler code (but watch stack depth)
3. **Consider balanced trees** (AVL, Red-Black) for production use
4. **Handle duplicates** explicitly (left ≤ root < right or similar)
5. **Free memory** properly in destructor to avoid leaks
6. **Use const references** for large data types

---

## 🐛 Common Mistakes

| Mistake | Consequence | Solution |
|---------|-------------|----------|
| **Violating BST property** | Search fails | Always verify after insert |
| **Memory leaks** | Resource waste | Proper destructor implementation |
| **Stack overflow** | Crash on deep recursion | Use iterative or increase stack |
| **Not handling empty tree** | Null pointer crash | Always check for nullptr |
| **Forgetting parent update** | Broken links | Update parent references |

---

## 🚀 Learning Path

```
Step 1: BST_Introduction.md
    ↓
Step 2: BST_Insertion.md
    ↓
Step 3: BST_Search.md
    ↓
Step 4: BST_Deletion.md
    ↓
Step 5: BST_Traversal.md
    ↓
Practice: Implement from scratch
    ↓
Advanced: Balanced BSTs (AVL, Red-Black)
```

---

## 📚 References

- CLRS Introduction to Algorithms (Chapter 12)
- Robert Sedgewick's Algorithms (Chapter 3)
- GeeksforGeeks BST section
- LeetCode BST problems (100+ practice problems)

---

## ✅ Key Takeaways

1. **BST property**: left < root < right
2. **Inorder traversal** gives sorted order
3. **Average case** O(log n), **worst case** O(n)
4. **Deletion** has three cases: leaf, one child, two children
5. **Successor** is the smallest node in right subtree
6. **Predecessor** is the largest node in left subtree
7. **Balanced BSTs** (AVL, Red-Black) guarantee O(log n)

---

## 📋 File Navigation

| File | Description | Difficulty |
|------|-------------|------------|
| [01_BST_Introduction.md](01_BST_Introduction.md) | Basic concepts and properties | ⭐ Beginner |
| [02_BST_Insertion.md](02_BST_Insertion.md) | Insert algorithm | ⭐⭐ Intermediate |
| [03_BST_Deletion.md](03_BST_Deletion.md) | Delete algorithm (3 cases) | ⭐⭐⭐ Advanced |
| [04_BST_Search.md](04_BST_Search.md) | Search algorithm | ⭐ Beginner |
| [05_BST_Traversal.md](05_BST_Traversal.md) | All traversal methods | ⭐⭐ Intermediate |

---

**Ready to start?** Type **"next"** to continue to `01_BST_Introduction.md`