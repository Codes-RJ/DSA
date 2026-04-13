# AVL Trees - Introduction

## 📖 Overview

AVL Tree (named after its inventors Adelson-Velsky and Landis) is a self-balancing Binary Search Tree where the heights of the two child subtrees of any node differ by at most one. This balance property guarantees that operations like search, insert, and delete always take O(log n) time, making AVL trees ideal for applications requiring fast and predictable performance.

---

## 🎯 Problem with Regular BST

### The Skewed Tree Problem

When data is inserted in sorted order into a regular BST, the tree becomes skewed (like a linked list):

```
Insert: 1, 2, 3, 4, 5

Regular BST:
    1
     \
      2
       \
        3
         \
          4
           \
            5

Height = 4
Search time = O(n) = 5 operations
```

### AVL Tree Solution

AVL trees automatically rebalance after each insertion:

```
Same insertions in AVL Tree:
        3
       / \
      2   4
     /     \
    1       5

Height = 2
Search time = O(log n) = 3 operations
```

---

## 📐 AVL Tree Properties

### Balance Factor Definition

For every node in an AVL tree:
```
Balance Factor = height(left subtree) - height(right subtree)

Allowed values: -1, 0, 1
```

### Visual Examples

```
Balanced Node (BF = 0):
        50 (BF = 1 - 1 = 0)
       /  \
      30   80
     / \   / \
    20 40 70 90

Left Heavy Node (BF = 1):
        50 (BF = 2 - 1 = 1)
       /  \
      30   80
     / \
    20 40
   /
  10

Right Heavy Node (BF = -1):
        50 (BF = 1 - 2 = -1)
       /  \
      30   80
          / \
         70 90
           \
           100
```

### Invalid AVL Nodes

```
Left Heavy (BF = 2) - NOT ALLOWED:
        50 (BF = 3 - 1 = 2) ← Violation!
       /  \
      30   80
     / \
    20 40
   /
  10

Right Heavy (BF = -2) - NOT ALLOWED:
        50 (BF = 1 - 3 = -2) ← Violation!
       /  \
      30   80
          / \
         70 90
           \
           100
             \
             110
```

---

## 📊 AVL vs Regular BST

| Aspect | Regular BST | AVL Tree |
|--------|-------------|----------|
| **Height** | O(n) worst case | O(log n) guaranteed |
| **Search Time** | O(n) worst case | O(log n) guaranteed |
| **Insert Time** | O(n) worst case | O(log n) guaranteed |
| **Delete Time** | O(n) worst case | O(log n) guaranteed |
| **Balance Maintenance** | None | Automatic rotations |
| **Memory Overhead** | Minimal | Extra height storage |
| **Implementation Complexity** | Simple | More complex |

---

## 🔢 Mathematical Properties

### Height Bounds

For an AVL tree with n nodes:
```
Minimum height: floor(log₂(n))
Maximum height: 1.44 * log₂(n + 2) - 0.328

Examples:
n = 1,000,000
- Regular BST worst height: 999,999
- AVL Tree height: ~20-30
```

### Minimum Nodes for Height h

```
N(h) = N(h-1) + N(h-2) + 1
where N(0) = 1, N(1) = 2

h=0: 1 node
h=1: 2 nodes
h=2: 4 nodes
h=3: 7 nodes
h=4: 12 nodes
h=5: 20 nodes
```

### Maximum Height for n nodes

```
h ≈ 1.44 * log₂(n + 2)

Example: n = 1,000,000
h ≈ 1.44 * 20 = 28.8 ≈ 29
```

---

## 🏗️ AVL Node Structure

```cpp
template<typename T>
class AVLNode {
public:
    T data;
    AVLNode* left;
    AVLNode* right;
    int height;
    
    AVLNode(const T& value) 
        : data(value), left(nullptr), right(nullptr), height(0) {}
};

// Height helper functions
int getHeight(AVLNode* node) {
    return node ? node->height : -1;
}

int getBalanceFactor(AVLNode* node) {
    return node ? getHeight(node->left) - getHeight(node->right) : 0;
}

void updateHeight(AVLNode* node) {
    if (node) {
        node->height = 1 + max(getHeight(node->left), getHeight(node->right));
    }
}
```

---

## 🔄 Balance Cases

### Four Imbalance Cases

| Case | Pattern | Balance Factor | Required Rotation |
|------|---------|----------------|-------------------|
| **Left-Left (LL)** | Node has left child with left child | BF = 2, left BF ≥ 0 | Right Rotation |
| **Right-Right (RR)** | Node has right child with right child | BF = -2, right BF ≤ 0 | Left Rotation |
| **Left-Right (LR)** | Node has left child with right child | BF = 2, left BF < 0 | Left-Right Rotation |
| **Right-Left (RL)** | Node has right child with left child | BF = -2, right BF > 0 | Right-Left Rotation |

### Visual Case Recognition

```
LL Case (Left-Left):
    z (BF = 2)
   /
  y (BF = 1)
 /
x

LR Case (Left-Right):
    z (BF = 2)
   /
  y (BF = -1)
   \
    x

RR Case (Right-Right):
z (BF = -2)
 \
  y (BF = -1)
   \
    x

RL Case (Right-Left):
z (BF = -2)
 \
  y (BF = 1)
 /
x
```

---

## 📈 Performance Comparison

### Operation Performance

| Operation | BST (Average) | BST (Worst) | AVL (Worst) |
|-----------|---------------|-------------|-------------|
| **Search** | O(log n) | O(n) | O(log n) |
| **Insert** | O(log n) | O(n) | O(log n) |
| **Delete** | O(log n) | O(n) | O(log n) |
| **Space** | O(n) | O(n) | O(n) |

### Empirical Performance (n = 1,000,000)

| Operation | BST (Best) | BST (Worst) | AVL |
|-----------|------------|-------------|-----|
| **Search** | ~20 steps | ~1,000,000 steps | ~20-30 steps |
| **Insert** | ~20 steps | ~1,000,000 steps | ~20-30 steps |
| **Balance** | N/A | N/A | ~2-3 rotations |

---

## 🎯 When to Use AVL Tree

### Use AVL Tree When

| Scenario | Reason |
|----------|--------|
| **Frequent lookups** | Guaranteed O(log n) search |
| **Read-heavy operations** | Balance maintained automatically |
| **Predictable performance** | No worst-case degradation |
| **Sorted data insertion** | Tree stays balanced |
| **Database indexing** | Fast retrieval guaranteed |

### Consider Alternatives When

| Scenario | Alternative |
|----------|-------------|
| **Very frequent inserts/deletes** | Red-Black Tree (fewer rotations) |
| **Memory is extremely limited** | Regular BST (less overhead) |
| **Data is static** | Sorted array + binary search |
| **Simple implementation needed** | Regular BST |

---

## 💡 Key Insights

1. **Balance factor** must be -1, 0, or 1 for every node
2. **Height** of an AVL tree is always O(log n)
3. **Rotations** restore balance in O(1) time
4. **Four imbalance cases** require different rotations
5. **Worst-case search** is never more than 1.44 * log₂(n)
6. **Insertions and deletions** may require multiple rotations up the tree
7. **AVL trees** are stricter than Red-Black trees (more balanced)

---

## 🚀 Next Steps

After understanding AVL basics, proceed to:

1. **Rotations.md** - Master the four rotation operations
2. **Balancing_Factor.md** - Learn to calculate and check balance
3. **AVL_Insertion.md** - Implement insert with rebalancing
4. **AVL_Deletion.md** - Implement delete with rebalancing

---

## ✅ Key Takeaways

1. **AVL trees** are self-balancing BSTs
2. **Balance factor** ensures O(log n) height
3. **Rotations** maintain balance after modifications
4. **Four cases** (LL, RR, LR, RL) cover all imbalances
5. **Height stored** in each node for O(1) balance factor
6. **All operations** are O(log n) guaranteed
7. **More balanced** than Red-Black trees (but more rotations)

---
---

## Next Step

- Go to [02_Rotations.md](02_Rotations.md) to continue with Rotations.
