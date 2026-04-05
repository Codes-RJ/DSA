# README.md - AVL Trees

## 📖 Overview

AVL Trees (named after inventors Adelson-Velsky and Landis) are self-balancing Binary Search Trees where the heights of the two child subtrees of any node differ by at most one. This balance property ensures that operations like search, insert, and delete always take O(log n) time, avoiding the worst-case O(n) degradation that can occur in regular BSTs.

---

## 🎯 Why AVL Trees?

### Problem with Regular BST

```
Regular BST after inserting sorted data:
    1
     \
      2
       \
        3
         \
          4
           \
            5

This becomes a linked list!
Search time: O(n) instead of O(log n)
```

### AVL Tree Solution

```
AVL Tree after same insertions:
        3
       / \
      2   4
     /     \
    1       5

Height is balanced!
Search time: O(log n) guaranteed
```

---

## 📊 AVL Tree Properties

| Property | Description | Requirement |
|----------|-------------|-------------|
| **Balance Factor** | height(left) - height(right) | -1, 0, or 1 |
| **Height** | Max distance to leaf | Maintained during operations |
| **Self-balancing** | Automatically rebalances | After insertions/deletions |
| **Rotation** | Operation to restore balance | Left, Right, Left-Right, Right-Left |

---

## 🔄 Balance Factor

### Definition

```
Balance Factor = height(left subtree) - height(right subtree)

Valid values: -1, 0, 1

Example:
        50 (BF = 1 - 1 = 0)
       /  \
      30   80
     / \   / \
    20 40 70 90
    (h=2) (h=2)
```

### Balance Factor Examples

```
Tree A (Balanced):
        50 (BF = 1 - 1 = 0)
       /  \
      30   80
     /     /
    20    70
    (h=1) (h=1)

Tree B (Left Heavy):
        50 (BF = 2 - 1 = 1)
       /  \
      30   80
     / \
    20 40
   /
  10
  (h=2)

Tree C (Right Heavy):
        50 (BF = 1 - 2 = -1)
       /  \
      30   80
          / \
         70 90
           \
           100
          (h=2)
```

---

## 🔄 Rotation Operations

### Four Types of Rotations

| Rotation | When Used | Visual |
|----------|-----------|--------|
| **Right Rotation** | Left-Left case | `O` becomes right child of `O`'s left child |
| **Left Rotation** | Right-Right case | `O` becomes left child of `O`'s right child |
| **Left-Right Rotation** | Left-Right case | Left rotate left child, then right rotate |
| **Right-Left Rotation** | Right-Left case | Right rotate right child, then left rotate |

---

## 📈 Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Search** | O(log n) | O(1) |
| **Insert** | O(log n) | O(1) |
| **Delete** | O(log n) | O(1) |
| **Rotation** | O(1) | O(1) |

---

## 📚 Folder Structure

```
03_AVL_Trees/
├── README.md                       # This file - Complete guide
├── 01_AVL_Introduction.md          # AVL tree basics and properties
├── 02_Rotations.md                 # Rotation operations explained
├── 03_Balancing_Factor.md          # Balance factor calculation
├── 04_AVL_Insertion.md             # Insert with rebalancing
└── 05_AVL_Deletion.md              # Delete with rebalancing
```

---

## 🚀 Learning Path

```
1. AVL_Introduction.md     → Understand AVL properties
           ↓
2. Rotations.md            → Master rotation operations
           ↓
3. Balancing_Factor.md     → Learn balance factor calculation
           ↓
4. AVL_Insertion.md        → Insert with rebalancing
           ↓
5. AVL_Deletion.md         → Delete with rebalancing
```

---

## ✅ Key Takeaways

1. **AVL trees** are self-balancing BSTs
2. **Balance factor** must be -1, 0, or 1 for every node
3. **Rotations** restore balance after insertions/deletions
4. **Four rotation types**: LL, RR, LR, RL
5. **Height** is maintained in each node
6. **All operations** are O(log n) guaranteed
7. **More rigid** than Red-Black trees (stricter balancing)

---