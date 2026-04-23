# README.md

## AVL Trees - Complete Guide

### Overview

An AVL tree (named after its inventors Adelson-Velsky and Landis) is a self-balancing Binary Search Tree (BST) where the heights of the left and right subtrees of any node differ by at most one. This balance property ensures that operations like insertion, deletion, and search always take O(log n) time, preventing the degenerate O(n) worst-case behavior of ordinary BSTs.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [01_AVL_Introduction.md](01_AVL_Introduction.md) | understand AVL Tree Introduction and Properties |
| 2. | [02_Rotations.md](02_Rotations.md) | understand AVL Rotations (Left, Right, Left-Right, Right-Left) |
| 3. | [03_Balancing_Factor.md](03_Balancing_Factor.md) | understand Balance Factor and Height Calculation |
| 4. | [04_AVL_Insertion.md](04_AVL_Insertion.md) | understand AVL Tree Insertion with Rebalancing |
| 5. | [05_AVL_Deletion.md](05_AVL_Deletion.md) | understand AVL Tree Deletion with Rebalancing |
| 6. | [README.md](README.md) | understand AVL Trees Overview |

---

## 1. AVL Introduction

This topic introduces AVL trees and why self-balancing is necessary.

**File:** [01_AVL_Introduction.md](01_AVL_Introduction.md)

**What you will learn:**
- Problem with ordinary BST (degenerate trees)
- What makes an AVL tree balanced
- Balance factor definition
- Height property of AVL trees
- AVL vs ordinary BST comparison

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Balance Factor** | height(left) - height(right) |
| **AVL Property** | Balance factor ∈ {-1, 0, 1} |
| **Height** | Number of edges on longest path to leaf |
| **Self-Balancing** | Tree automatically rebalances after insert/delete |

**BST Degeneracy Problem:**
```
Insertion order: 1,2,3,4,5

Ordinary BST becomes:
1
 \
  2
   \
    3
     \
      4
       \
        5
Height = 4, Search = O(n)

AVL Tree stays balanced:
    3
   / \
  2   5
 /   /
1   4
Height = 2, Search = O(log n)
```

---

## 2. AVL Rotations

This topic explains the four types of rotations used to rebalance AVL trees.

**File:** [02_Rotations.md](02_Rotations.md)

**What you will learn:**
- Right Rotation (LL case)
- Left Rotation (RR case)
- Left-Right Rotation (LR case)
- Right-Left Rotation (RL case)
- When to apply each rotation

**Key Concepts:**

| Rotation | When Used | Balance Factor Pattern |
|----------|-----------|------------------------|
| **Right Rotation (LL)** | Left-Left case | BF = 2, left child BF ≥ 0 |
| **Left Rotation (RR)** | Right-Right case | BF = -2, right child BF ≤ 0 |
| **Left-Right Rotation (LR)** | Left-Right case | BF = 2, left child BF = -1 |
| **Right-Left Rotation (RL)** | Right-Left case | BF = -2, right child BF = 1 |

**Right Rotation Visualization:**
```
Before:              After:
    y                  x
   / \                / \
  x   T3             T1  y
 / \                    / \
T1 T2                  T2 T3

Step: x becomes new root
      y becomes right child of x
      T2 becomes left child of y
```

**Left Rotation Visualization:**
```
Before:              After:
    x                  y
   / \                / \
  T1  y              x   T3
     / \            / \
    T2 T3          T1 T2

Step: y becomes new root
      x becomes left child of y
      T2 becomes right child of x
```

---

## 3. Balance Factor and Height

This topic explains how to compute balance factors and maintain height information.

**File:** [03_Balancing_Factor.md](03_Balancing_Factor.md)

**What you will learn:**
- Height calculation for AVL nodes
- Balance factor calculation
- Updating heights after rotations
- Why height is stored in each node
- Balance factor ranges and meanings

**Key Concepts:**

| Balance Factor | Meaning |
|----------------|---------|
| **+1 or +2** | Left heavy |
| **0** | Perfectly balanced |
| **-1 or -2** | Right heavy |

**Height Calculation:**
```
height(node) = 1 + max(height(left), height(right))
balanceFactor(node) = height(left) - height(right)
```

**Node Structure with Height:**
```cpp
struct Node {
    int data;
    int height;
    Node* left;
    Node* right;
    
    Node(int val) : data(val), height(1), left(nullptr), right(nullptr) {}
};

int getHeight(Node* node) {
    return node ? node->height : 0;
}

int getBalanceFactor(Node* node) {
    return node ? getHeight(node->left) - getHeight(node->right) : 0;
}

void updateHeight(Node* node) {
    if (node) {
        node->height = 1 + max(getHeight(node->left), getHeight(node->right));
    }
}
```

---

## 4. AVL Insertion

This topic explains how to insert a node into an AVL tree with rebalancing.

**File:** [04_AVL_Insertion.md](04_AVL_Insertion.md)

**What you will learn:**
- Standard BST insertion
- Updating heights after insertion
- Checking balance factor
- Applying appropriate rotations
- Four imbalance cases (LL, RR, LR, RL)

**Key Concepts:**

| Imbalance Type | Condition | Rotation |
|----------------|-----------|----------|
| **LL** | BF > 1 and value < left->data | Right rotation |
| **RR** | BF < -1 and value > right->data | Left rotation |
| **LR** | BF > 1 and value > left->data | Left-Right rotation |
| **RL** | BF < -1 and value < right->data | Right-Left rotation |

**Insertion Algorithm:**
```
insert(node, value):
    // Step 1: Standard BST insert
    if node is null: return new node
    if value < node.data: node.left = insert(node.left, value)
    else if value > node.data: node.right = insert(node.right, value)
    else: return node (duplicate)
    
    // Step 2: Update height
    updateHeight(node)
    
    // Step 3: Check balance
    balance = getBalanceFactor(node)
    
    // Step 4: Rebalance if needed
    // LL case
    if balance > 1 and value < node.left.data:
        return rightRotate(node)
    // RR case
    if balance < -1 and value > node.right.data:
        return leftRotate(node)
    // LR case
    if balance > 1 and value > node.left.data:
        node.left = leftRotate(node.left)
        return rightRotate(node)
    // RL case
    if balance < -1 and value < node.right.data:
        node.right = rightRotate(node.right)
        return leftRotate(node)
    
    return node
```

---

## 5. AVL Deletion

This topic explains how to delete a node from an AVL tree with rebalancing.

**File:** [05_AVL_Deletion.md](05_AVL_Deletion.md)

**What you will learn:**
- Standard BST deletion (three cases)
- Updating heights after deletion
- Rebalancing after deletion
- Same rotation rules as insertion
- Time complexity analysis

**Key Concepts:**

| Deletion Case | Action |
|---------------|--------|
| **Leaf node** | Simply remove |
| **One child** | Replace node with child |
| **Two children** | Find inorder successor, copy value, delete successor |

**Deletion Algorithm:**
```
delete(node, value):
    // Step 1: Standard BST delete
    if node is null: return null
    if value < node.data: node.left = delete(node.left, value)
    else if value > node.data: node.right = delete(node.right, value)
    else:
        // Node to delete found
        if node.left is null: return node.right
        if node.right is null: return node.left
        // Two children
        successor = findMin(node.right)
        node.data = successor.data
        node.right = delete(node.right, successor.data)
    
    // Step 2: Update height
    updateHeight(node)
    
    // Step 3: Check balance
    balance = getBalanceFactor(node)
    
    // Step 4: Rebalance (same as insertion)
    // LL case
    if balance > 1 and getBalanceFactor(node.left) >= 0:
        return rightRotate(node)
    // LR case
    if balance > 1 and getBalanceFactor(node.left) < 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)
    // RR case
    if balance < -1 and getBalanceFactor(node.right) <= 0:
        return leftRotate(node)
    // RL case
    if balance < -1 and getBalanceFactor(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)
    
    return node
```

---

### Complete AVL Tree Implementation

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

struct Node {
    int data;
    int height;
    Node* left;
    Node* right;
    
    Node(int val) : data(val), height(1), left(nullptr), right(nullptr) {}
};

class AVLTree {
private:
    Node* root;
    
    int getHeight(Node* node) {
        return node ? node->height : 0;
    }
    
    int getBalanceFactor(Node* node) {
        return node ? getHeight(node->left) - getHeight(node->right) : 0;
    }
    
    void updateHeight(Node* node) {
        if (node) {
            node->height = 1 + max(getHeight(node->left), getHeight(node->right));
        }
    }
    
    Node* rightRotate(Node* y) {
        Node* x = y->left;
        Node* T2 = x->right;
        
        // Perform rotation
        x->right = y;
        y->left = T2;
        
        // Update heights
        updateHeight(y);
        updateHeight(x);
        
        return x;
    }
    
    Node* leftRotate(Node* x) {
        Node* y = x->right;
        Node* T2 = y->left;
        
        // Perform rotation
        y->left = x;
        x->right = T2;
        
        // Update heights
        updateHeight(x);
        updateHeight(y);
        
        return y;
    }
    
    Node* insertHelper(Node* node, int value) {
        // Step 1: Standard BST insert
        if (!node) return new Node(value);
        
        if (value < node->data) {
            node->left = insertHelper(node->left, value);
        } else if (value > node->data) {
            node->right = insertHelper(node->right, value);
        } else {
            return node;  // Duplicate not allowed
        }
        
        // Step 2: Update height
        updateHeight(node);
        
        // Step 3: Get balance factor
        int balance = getBalanceFactor(node);
        
        // Step 4: Rebalance
        
        // LL Case
        if (balance > 1 && value < node->left->data) {
            return rightRotate(node);
        }
        
        // RR Case
        if (balance < -1 && value > node->right->data) {
            return leftRotate(node);
        }
        
        // LR Case
        if (balance > 1 && value > node->left->data) {
            node->left = leftRotate(node->left);
            return rightRotate(node);
        }
        
        // RL Case
        if (balance < -1 && value < node->right->data) {
            node->right = rightRotate(node->right);
            return leftRotate(node);
        }
        
        return node;
    }
    
    Node* findMin(Node* node) {
        while (node && node->left) {
            node = node->left;
        }
        return node;
    }
    
    Node* deleteHelper(Node* node, int value) {
        // Step 1: Standard BST delete
        if (!node) return nullptr;
        
        if (value < node->data) {
            node->left = deleteHelper(node->left, value);
        } else if (value > node->data) {
            node->right = deleteHelper(node->right, value);
        } else {
            // Node to delete found
            
            // Case 1: No child or one child
            if (!node->left) {
                Node* temp = node->right;
                delete node;
                return temp;
            }
            if (!node->right) {
                Node* temp = node->left;
                delete node;
                return temp;
            }
            
            // Case 2: Two children
            Node* successor = findMin(node->right);
            node->data = successor->data;
            node->right = deleteHelper(node->right, successor->data);
        }
        
        // Step 2: Update height
        updateHeight(node);
        
        // Step 3: Get balance factor
        int balance = getBalanceFactor(node);
        
        // Step 4: Rebalance
        
        // LL Case
        if (balance > 1 && getBalanceFactor(node->left) >= 0) {
            return rightRotate(node);
        }
        
        // LR Case
        if (balance > 1 && getBalanceFactor(node->left) < 0) {
            node->left = leftRotate(node->left);
            return rightRotate(node);
        }
        
        // RR Case
        if (balance < -1 && getBalanceFactor(node->right) <= 0) {
            return leftRotate(node);
        }
        
        // RL Case
        if (balance < -1 && getBalanceFactor(node->right) > 0) {
            node->right = rightRotate(node->right);
            return leftRotate(node);
        }
        
        return node;
    }
    
    void inorderHelper(Node* node) {
        if (!node) return;
        inorderHelper(node->left);
        cout << node->data << " ";
        inorderHelper(node->right);
    }
    
    void destroyTree(Node* node) {
        if (!node) return;
        destroyTree(node->left);
        destroyTree(node->right);
        delete node;
    }
    
public:
    AVLTree() : root(nullptr) {}
    
    ~AVLTree() {
        destroyTree(root);
    }
    
    void insert(int value) {
        root = insertHelper(root, value);
    }
    
    void remove(int value) {
        root = deleteHelper(root, value);
    }
    
    void inorder() {
        inorderHelper(root);
        cout << endl;
    }
    
    bool isEmpty() {
        return root == nullptr;
    }
};

int main() {
    AVLTree tree;
    
    // Insert values that would create degenerate BST
    cout << "Inserting: 10, 20, 30, 40, 50, 25" << endl;
    tree.insert(10);
    tree.insert(20);
    tree.insert(30);
    tree.insert(40);
    tree.insert(50);
    tree.insert(25);
    
    cout << "Inorder (sorted): ";
    tree.inorder();  // 10 20 25 30 40 50
    
    cout << "\nDeleting 40" << endl;
    tree.remove(40);
    
    cout << "Inorder after deletion: ";
    tree.inorder();  // 10 20 25 30 50
    
    return 0;
}
```

---

### Complexity Summary

| Operation | AVL Tree | Ordinary BST (Worst) |
|-----------|----------|----------------------|
| **Insert** | O(log n) | O(n) |
| **Search** | O(log n) | O(n) |
| **Delete** | O(log n) | O(n) |

---

### AVL vs Other Balanced Trees

| Property | AVL Tree | Red-Black Tree |
|----------|----------|----------------|
| **Balance** | Strict (height diff ≤ 1) | Loose (black height) |
| **Height** | ~1.44 log n | ~2 log n |
| **Lookup** | Faster (more balanced) | Slightly slower |
| **Insert/Delete** | Slower (more rotations) | Faster (fewer rotations) |
| **Use Case** | Read-heavy | Write-heavy |

---

### Prerequisites

Before starting this section, you should have completed:

- [01_Binary_Trees/README.md](../01_Binary_Trees/README.md) - Binary tree basics
- [02_BST/README.md](../02_BST/README.md) - BST operations

---

### Learning Path

```
Level 1: Introduction
├── BST Degeneracy Problem
├── AVL Property
└── Balance Factor

Level 2: Rotations
├── Right Rotation (LL)
├── Left Rotation (RR)
├── Left-Right Rotation (LR)
└── Right-Left Rotation (RL)

Level 3: Insertion
├── BST Insert
├── Height Update
├── Balance Check
└── Apply Rotation

Level 4: Deletion
├── BST Delete
├── Height Update
├── Balance Check
└── Apply Rotation
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Forgetting to update heights | Update height after every insert/delete |
| Incorrect rotation implementation | Carefully reassign child pointers |
| Wrong balance factor calculation | height(left) - height(right) |
| Applying wrong rotation | Check both node and child balance factors |
| Not handling null children | Check for null before accessing child data |

---

### Practice Questions

After completing this section, you should be able to:

1. Explain why AVL trees are needed
2. Calculate balance factor for any node
4. Implement left and right rotations
5. Insert values and rebalance an AVL tree
6. Delete values and rebalance an AVL tree
7. Identify the four imbalance cases (LL, RR, LR, RL)
8. Compare AVL trees with Red-Black trees

---

### Next Steps

- Go to [01_AVL_Introduction.md](01_AVL_Introduction.md) to understand AVL Tree Introduction and Properties.