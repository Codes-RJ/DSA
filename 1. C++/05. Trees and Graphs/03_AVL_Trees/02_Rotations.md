# AVL Tree Rotations

## 📖 Overview

Rotations are the fundamental operations that maintain balance in AVL trees. When a node becomes unbalanced (balance factor becomes -2 or 2), rotations are performed to restore balance. There are four types of rotations: Right Rotation, Left Rotation, Left-Right Rotation, and Right-Left Rotation. Each rotation operation runs in O(1) time.

---

## 🎯 Why Rotations?

### The Problem

When nodes are inserted or deleted, the balance factor of some nodes may become -2 or 2, violating the AVL property:

```
Unbalanced Tree:
        50 (BF = 2) ← Violation!
       /
      30 (BF = 1)
     /
    20

This tree is left-heavy and needs rebalancing.
```

### The Solution

Rotations restructure the tree while preserving the BST property:

```
After Right Rotation:
        30
       /  \
      20   50

Tree is balanced again!
```

---

## 🔄 Right Rotation (LL Case)

### When to Use

Used when a node becomes left-heavy (BF = 2) and its left child is also left-heavy (BF ≥ 0). This is the **Left-Left (LL)** case.

### Visual Transformation

```
Before Rotation:              After Rotation:
        z (BF = 2)                   y (BF = 0)
       /                           /   \
      y (BF = 1)                  x     z
     /
    x

Where:
- x is left child of y
- y is left child of z
```

### Step-by-Step Process

```
Step 1: Identify nodes
        z
       /
      y
     /
    x

Step 2: Make y the new root
        y
       / \
      x   z

Step 3: Update heights
        y (height updated)
       / \
      x   z (heights updated)
```

### Implementation

```cpp
AVLNode* rightRotate(AVLNode* y) {
    AVLNode* x = y->left;
    AVLNode* T2 = x->right;
    
    // Perform rotation
    x->right = y;
    y->left = T2;
    
    // Update heights
    updateHeight(y);
    updateHeight(x);
    
    return x; // New root
}
```

### Example

```
Before:                       After:
        50 (BF = 2)                 30 (BF = 0)
       /                          /   \
      30 (BF = 1)                20    50
     /
    20

Balance restored!
```

---

## 🔄 Left Rotation (RR Case)

### When to Use

Used when a node becomes right-heavy (BF = -2) and its right child is also right-heavy (BF ≤ 0). This is the **Right-Right (RR)** case.

### Visual Transformation

```
Before Rotation:              After Rotation:
z (BF = -2)                         y (BF = 0)
 \                               /   \
  y (BF = -1)                   z     x
   \
    x

Where:
- x is right child of y
- y is right child of z
```

### Step-by-Step Process

```
Step 1: Identify nodes
z
 \
  y
   \
    x

Step 2: Make y the new root
        y
       / \
      z   x

Step 3: Update heights
        y (height updated)
       / \
      z   x (heights updated)
```

### Implementation

```cpp
AVLNode* leftRotate(AVLNode* x) {
    AVLNode* y = x->right;
    AVLNode* T2 = y->left;
    
    // Perform rotation
    y->left = x;
    x->right = T2;
    
    // Update heights
    updateHeight(x);
    updateHeight(y);
    
    return y; // New root
}
```

### Example

```
Before:                       After:
50 (BF = -2)                       80 (BF = 0)
 \                               /   \
  80 (BF = -1)                  50    90
   \
    90

Balance restored!
```

---

## 🔄 Left-Right Rotation (LR Case)

### When to Use

Used when a node becomes left-heavy (BF = 2) but its left child is right-heavy (BF = -1). This is the **Left-Right (LR)** case.

### Visual Transformation

```
Before Rotation:              After Rotation:
        z (BF = 2)                   x (BF = 0)
       /                           /   \
      y (BF = -1)                  y     z
       \
        x

Step 1: Left rotate on y
        z
       /
      x
     /
    y

Step 2: Right rotate on z
        x
       / \
      y   z
```

### Implementation

```cpp
AVLNode* leftRightRotate(AVLNode* z) {
    z->left = leftRotate(z->left);
    return rightRotate(z);
}
```

### Example

```
Before:                       After:
        50 (BF = 2)                 40 (BF = 0)
       /                          /   \
      30 (BF = -1)               30    50
       \
        40

Balance restored!
```

---

## 🔄 Right-Left Rotation (RL Case)

### When to Use

Used when a node becomes right-heavy (BF = -2) but its right child is left-heavy (BF = 1). This is the **Right-Left (RL)** case.

### Visual Transformation

```
Before Rotation:              After Rotation:
z (BF = -2)                         x (BF = 0)
 \                                 / \
  y (BF = 1)                       z   y
 /
x

Step 1: Right rotate on y
z
 \
  x
   \
    y

Step 2: Left rotate on z
        x
       / \
      z   y
```

### Implementation

```cpp
AVLNode* rightLeftRotate(AVLNode* z) {
    z->right = rightRotate(z->right);
    return leftRotate(z);
}
```

### Example

```
Before:                       After:
50 (BF = -2)                       70 (BF = 0)
 \                               /   \
  80 (BF = 1)                   50    80
 /
70

Balance restored!
```

---

## 📊 Rotation Summary Table

| Case | Pattern | Balance Factors | Rotation | Steps |
|------|---------|-----------------|----------|-------|
| **LL** | Left-Left | BF(z)=2, BF(y)≥0 | Right | Single |
| **RR** | Right-Right | BF(z)=-2, BF(y)≤0 | Left | Single |
| **LR** | Left-Right | BF(z)=2, BF(y)=-1 | Left-Right | Double |
| **RL** | Right-Left | BF(z)=-2, BF(y)=1 | Right-Left | Double |

---

## 💻 Complete Rotation Implementation

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

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

template<typename T>
class AVLTree {
private:
    AVLNode<T>* root;
    
    int getHeight(AVLNode<T>* node) {
        return node ? node->height : -1;
    }
    
    int getBalanceFactor(AVLNode<T>* node) {
        return node ? getHeight(node->left) - getHeight(node->right) : 0;
    }
    
    void updateHeight(AVLNode<T>* node) {
        if (node) {
            node->height = 1 + max(getHeight(node->left), getHeight(node->right));
        }
    }
    
    // Right Rotation (LL Case)
    AVLNode<T>* rightRotate(AVLNode<T>* y) {
        cout << "Performing Right Rotation on " << y->data << endl;
        
        AVLNode<T>* x = y->left;
        AVLNode<T>* T2 = x->right;
        
        // Perform rotation
        x->right = y;
        y->left = T2;
        
        // Update heights
        updateHeight(y);
        updateHeight(x);
        
        return x;
    }
    
    // Left Rotation (RR Case)
    AVLNode<T>* leftRotate(AVLNode<T>* x) {
        cout << "Performing Left Rotation on " << x->data << endl;
        
        AVLNode<T>* y = x->right;
        AVLNode<T>* T2 = y->left;
        
        // Perform rotation
        y->left = x;
        x->right = T2;
        
        // Update heights
        updateHeight(x);
        updateHeight(y);
        
        return y;
    }
    
    // Left-Right Rotation (LR Case)
    AVLNode<T>* leftRightRotate(AVLNode<T>* z) {
        cout << "Performing Left-Right Rotation on " << z->data << endl;
        z->left = leftRotate(z->left);
        return rightRotate(z);
    }
    
    // Right-Left Rotation (RL Case)
    AVLNode<T>* rightLeftRotate(AVLNode<T>* z) {
        cout << "Performing Right-Left Rotation on " << z->data << endl;
        z->right = rightRotate(z->right);
        return leftRotate(z);
    }
    
    // Balance the node
    AVLNode<T>* balance(AVLNode<T>* node) {
        if (node == nullptr) return nullptr;
        
        updateHeight(node);
        int bf = getBalanceFactor(node);
        
        // Left Heavy
        if (bf > 1) {
            if (getBalanceFactor(node->left) >= 0) {
                // LL Case
                return rightRotate(node);
            } else {
                // LR Case
                return leftRightRotate(node);
            }
        }
        
        // Right Heavy
        if (bf < -1) {
            if (getBalanceFactor(node->right) <= 0) {
                // RR Case
                return leftRotate(node);
            } else {
                // RL Case
                return rightLeftRotate(node);
            }
        }
        
        return node;
    }
    
    // Insert helper
    AVLNode<T>* insert(AVLNode<T>* node, const T& value) {
        if (node == nullptr) {
            return new AVLNode<T>(value);
        }
        
        if (value < node->data) {
            node->left = insert(node->left, value);
        } else if (value > node->data) {
            node->right = insert(node->right, value);
        } else {
            return node; // Duplicate not allowed
        }
        
        return balance(node);
    }
    
    // Inorder traversal
    void inorder(AVLNode<T>* node) {
        if (node == nullptr) return;
        inorder(node->left);
        cout << node->data << " ";
        inorder(node->right);
    }
    
    // Print tree structure
    void printTree(AVLNode<T>* node, int space, int indent) {
        if (node == nullptr) return;
        
        space += indent;
        
        printTree(node->right, space, indent);
        
        cout << endl;
        for (int i = indent; i < space; i++) cout << " ";
        cout << node->data << "(BF=" << getBalanceFactor(node) << ")" << endl;
        
        printTree(node->left, space, indent);
    }
    
public:
    AVLTree() : root(nullptr) {}
    
    void insert(const T& value) {
        root = insert(root, value);
    }
    
    void inorder() {
        inorder(root);
        cout << endl;
    }
    
    void print() {
        printTree(root, 0, 5);
        cout << endl;
    }
};

int main() {
    AVLTree<int> avl;
    
    cout << "=== AVL Tree Rotations Demo ===" << endl;
    
    cout << "\n1. LL Case - Insert 50, 30, 20 (Right Rotation):" << endl;
    avl.insert(50);
    avl.insert(30);
    avl.insert(20);
    avl.print();
    
    cout << "\n2. RR Case - Insert 20, 30, 50 (Left Rotation):" << endl;
    AVLTree<int> avl2;
    avl2.insert(20);
    avl2.insert(30);
    avl2.insert(50);
    avl2.print();
    
    cout << "\n3. LR Case - Insert 50, 30, 40 (Left-Right Rotation):" << endl;
    AVLTree<int> avl3;
    avl3.insert(50);
    avl3.insert(30);
    avl3.insert(40);
    avl3.print();
    
    cout << "\n4. RL Case - Insert 20, 50, 30 (Right-Left Rotation):" << endl;
    AVLTree<int> avl4;
    avl4.insert(20);
    avl4.insert(50);
    avl4.insert(30);
    avl4.print();
    
    cout << "\n5. Complete AVL Tree:" << endl;
    AVLTree<int> avl5;
    int values[] = {50, 30, 80, 20, 40, 70, 90, 10, 25, 35, 45, 65, 75};
    for (int v : values) {
        avl5.insert(v);
    }
    avl5.print();
    
    cout << "Inorder traversal: ";
    avl5.inorder();
    
    return 0;
}
```

---

## 🎯 Rotation Decision Tree

```
Check Balance Factor at node:

If BF > 1 (Left Heavy):
    If BF(left child) ≥ 0:
        → Right Rotation (LL Case)
    Else:
        → Left-Right Rotation (LR Case)

If BF < -1 (Right Heavy):
    If BF(right child) ≤ 0:
        → Left Rotation (RR Case)
    Else:
        → Right-Left Rotation (RL Case)
```

---

## 📊 Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Right Rotation** | O(1) | O(1) |
| **Left Rotation** | O(1) | O(1) |
| **Left-Right Rotation** | O(1) | O(1) |
| **Right-Left Rotation** | O(1) | O(1) |

---

## ✅ Key Takeaways

1. **Rotations** restore balance in O(1) time
2. **Four types**: LL, RR, LR, RL
3. **LL and RR** are single rotations
4. **LR and RL** are double rotations
5. **Right rotation** fixes left-heavy trees
6. **Left rotation** fixes right-heavy trees
7. **Balance factor** determines which rotation to use
8. **Height updates** must occur after rotations

---
---

## Next Step

- Go to [03_Balancing_Factor.md](03_Balancing_Factor.md) to continue with Balancing Factor.
