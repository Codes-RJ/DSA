# Balancing Factor in AVL Trees

## 📖 Overview

The balancing factor (or balance factor) is a critical concept in AVL trees that determines whether a node is balanced and whether rotations are needed. It is defined as the difference between the heights of the left and right subtrees. Understanding balance factors is essential for implementing AVL tree operations.

---

## 🎯 Balance Factor Definition

### Formula

```
Balance Factor (BF) = height(left subtree) - height(right subtree)

Where:
- height of empty tree = -1
- height of leaf node = 0
```

### Valid Range

```
For AVL trees: BF ∈ {-1, 0, 1}

BF = -1: Right subtree is taller by 1
BF = 0:  Both subtrees have equal height
BF = 1:  Left subtree is taller by 1
```

---

## 📊 Balance Factor Examples

### Perfectly Balanced (BF = 0)

```
        50 (BF = 1 - 1 = 0)
       /  \
      30   80
     / \   / \
    20 40 70 90

Left height = 1, Right height = 1
BF = 1 - 1 = 0 ✓
```

### Left Heavy (BF = 1)

```
        50 (BF = 2 - 1 = 1)
       /  \
      30   80
     / \
    20 40
   /
  10

Left height = 2, Right height = 1
BF = 2 - 1 = 1 ✓ (still valid)
```

### Right Heavy (BF = -1)

```
        50 (BF = 1 - 2 = -1)
       /  \
      30   80
          / \
         70 90
           \
           100

Left height = 1, Right height = 2
BF = 1 - 2 = -1 ✓ (still valid)
```

### Unbalanced Nodes

```
Left Heavy (BF = 2) - VIOLATION:
        50 (BF = 3 - 1 = 2) ✗
       /  \
      30   80
     / \
    20 40
   /
  10
 /
5

Right Heavy (BF = -2) - VIOLATION:
        50 (BF = 1 - 3 = -2) ✗
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

## 🔢 Height Calculation

### Height Definition

```
Height of a node = length of longest path from node to leaf (in edges)

Leaf node height = 0
Empty node (nullptr) height = -1
```

### Height Examples

```
Tree:
        50 (height = 2)
       /  \
      30   80 (height = 1)
     / \   / \
    20 40 70 90 (height = 0)

Leaf nodes (20,40,70,90): height = 0
Nodes 30 and 80: height = 1
Root 50: height = 2
```

### Height Calculation Code

```cpp
int getHeight(Node* node) {
    return node ? node->height : -1;
}

void updateHeight(Node* node) {
    if (node) {
        node->height = 1 + max(getHeight(node->left), getHeight(node->right));
    }
}
```

---

## 📐 Balance Factor Calculation

### Step-by-Step Process

```cpp
int getBalanceFactor(Node* node) {
    if (node == nullptr) return 0;
    return getHeight(node->left) - getHeight(node->right);
}
```

### Example Calculation

```
Tree:
        50
       /  \
      30   80
     / \   / \
    20 40 70 90

Calculate BF(50):
    height(left) = height of node 30 = 1
    height(right) = height of node 80 = 1
    BF(50) = 1 - 1 = 0

Calculate BF(30):
    height(left) = height of node 20 = 0
    height(right) = height of node 40 = 0
    BF(30) = 0 - 0 = 0

Calculate BF(20):
    height(left) = -1 (null)
    height(right) = -1 (null)
    BF(20) = -1 - (-1) = 0
```

---

## 📈 Balance Factor After Rotations

### Right Rotation (LL Case)

```
Before:                    After:
    z (BF = 2)                  y (BF = 0)
   /                          /   \
  y (BF = 1)                 x     z
 /
x

BF(z) before = 2
BF(y) before = 1
After rotation:
BF(y) = 0, BF(z) = 0
```

### Left Rotation (RR Case)

```
Before:                    After:
z (BF = -2)                     y (BF = 0)
 \                           /   \
  y (BF = -1)               z     x
   \
    x

BF(z) before = -2
BF(y) before = -1
After rotation:
BF(y) = 0, BF(z) = 0
```

### Left-Right Rotation (LR Case)

```
Before:                    After:
    z (BF = 2)                  x (BF = 0)
   /                          /   \
  y (BF = -1)                y     z
   \
    x

After left rotation on y, then right rotation on z:
All affected nodes become balanced (BF = 0)
```

### Right-Left Rotation (RL Case)

```
Before:                    After:
z (BF = -2)                     x (BF = 0)
 \                           /   \
  y (BF = 1)                 z     y
 /
x

After right rotation on y, then left rotation on z:
All affected nodes become balanced (BF = 0)
```

---

## 🔍 Balance Factor Patterns

### Recognizing Imbalance Cases

| BF(node) | BF(child) | Case | Rotation |
|----------|-----------|------|----------|
| 2 | ≥ 0 | LL | Right |
| 2 | -1 | LR | Left-Right |
| -2 | ≤ 0 | RR | Left |
| -2 | 1 | RL | Right-Left |

### Visual Pattern Recognition

```
LL Pattern (BF=2, left child BF≥0):
        z (2)
       /
      y (1 or 0)
     /
    x

LR Pattern (BF=2, left child BF=-1):
        z (2)
       /
      y (-1)
       \
        x

RR Pattern (BF=-2, right child BF≤0):
    z (-2)
     \
      y (-1 or 0)
       \
        x

RL Pattern (BF=-2, right child BF=1):
    z (-2)
     \
      y (1)
     /
    x
```

---

## 💻 Complete Implementation

```cpp
#include <iostream>
#include <algorithm>
#include <queue>
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
    
    void printBalanceFactors(AVLNode<T>* node) {
        if (node == nullptr) return;
        
        printBalanceFactors(node->left);
        cout << "Node " << node->data << ": BF = " << getBalanceFactor(node) << endl;
        printBalanceFactors(node->right);
    }
    
    void printTreeWithBF(AVLNode<T>* node, int space, int indent) {
        if (node == nullptr) return;
        
        space += indent;
        
        printTreeWithBF(node->right, space, indent);
        
        cout << endl;
        for (int i = indent; i < space; i++) cout << " ";
        cout << node->data << "(BF=" << getBalanceFactor(node) << ")" << endl;
        
        printTreeWithBF(node->left, space, indent);
    }
    
    // Rotation functions (from previous section)
    AVLNode<T>* rightRotate(AVLNode<T>* y) {
        AVLNode<T>* x = y->left;
        AVLNode<T>* T2 = x->right;
        
        x->right = y;
        y->left = T2;
        
        updateHeight(y);
        updateHeight(x);
        
        return x;
    }
    
    AVLNode<T>* leftRotate(AVLNode<T>* x) {
        AVLNode<T>* y = x->right;
        AVLNode<T>* T2 = y->left;
        
        y->left = x;
        x->right = T2;
        
        updateHeight(x);
        updateHeight(y);
        
        return y;
    }
    
    AVLNode<T>* leftRightRotate(AVLNode<T>* z) {
        z->left = leftRotate(z->left);
        return rightRotate(z);
    }
    
    AVLNode<T>* rightLeftRotate(AVLNode<T>* z) {
        z->right = rightRotate(z->right);
        return leftRotate(z);
    }
    
    AVLNode<T>* balance(AVLNode<T>* node) {
        if (node == nullptr) return nullptr;
        
        updateHeight(node);
        int bf = getBalanceFactor(node);
        
        cout << "Balancing node " << node->data << " (BF=" << bf << ")" << endl;
        
        // Left Heavy
        if (bf > 1) {
            if (getBalanceFactor(node->left) >= 0) {
                cout << "  LL Case - Performing Right Rotation" << endl;
                return rightRotate(node);
            } else {
                cout << "  LR Case - Performing Left-Right Rotation" << endl;
                return leftRightRotate(node);
            }
        }
        
        // Right Heavy
        if (bf < -1) {
            if (getBalanceFactor(node->right) <= 0) {
                cout << "  RR Case - Performing Left Rotation" << endl;
                return leftRotate(node);
            } else {
                cout << "  RL Case - Performing Right-Left Rotation" << endl;
                return rightLeftRotate(node);
            }
        }
        
        cout << "  Node is balanced" << endl;
        return node;
    }
    
    AVLNode<T>* insert(AVLNode<T>* node, const T& value) {
        if (node == nullptr) {
            cout << "Inserting " << value << endl;
            return new AVLNode<T>(value);
        }
        
        if (value < node->data) {
            node->left = insert(node->left, value);
        } else if (value > node->data) {
            node->right = insert(node->right, value);
        } else {
            return node;
        }
        
        return balance(node);
    }
    
public:
    AVLTree() : root(nullptr) {}
    
    void insert(const T& value) {
        cout << "\n--- Inserting " << value << " ---" << endl;
        root = insert(root, value);
        cout << "Tree after insertion:" << endl;
        print();
    }
    
    void printBalanceFactors() {
        cout << "\n=== Balance Factors ===" << endl;
        printBalanceFactors(root);
    }
    
    void print() {
        printTreeWithBF(root, 0, 5);
        cout << endl;
    }
    
    void inorder() {
        inorder(root);
        cout << endl;
    }
    
private:
    void inorder(AVLNode<T>* node) {
        if (node == nullptr) return;
        inorder(node->left);
        cout << node->data << " ";
        inorder(node->right);
    }
};

int main() {
    AVLTree<int> avl;
    
    cout << "=== AVL Tree Balance Factor Demo ===" << endl;
    
    // Insert nodes that cause different imbalance cases
    cout << "\n1. LL Case - Insert 50, 30, 20:" << endl;
    avl.insert(50);
    avl.insert(30);
    avl.insert(20);
    avl.printBalanceFactors();
    
    cout << "\n2. RR Case - Insert 20, 30, 50:" << endl;
    AVLTree<int> avl2;
    avl2.insert(20);
    avl2.insert(30);
    avl2.insert(50);
    avl2.printBalanceFactors();
    
    cout << "\n3. LR Case - Insert 50, 30, 40:" << endl;
    AVLTree<int> avl3;
    avl3.insert(50);
    avl3.insert(30);
    avl3.insert(40);
    avl3.printBalanceFactors();
    
    cout << "\n4. RL Case - Insert 20, 50, 30:" << endl;
    AVLTree<int> avl4;
    avl4.insert(20);
    avl4.insert(50);
    avl4.insert(30);
    avl4.printBalanceFactors();
    
    cout << "\n5. Complete AVL Tree with many nodes:" << endl;
    AVLTree<int> avl5;
    int values[] = {50, 30, 80, 20, 40, 70, 90, 10, 25, 35, 45, 65, 75, 85, 95};
    for (int v : values) {
        avl5.insert(v);
    }
    avl5.print();
    avl5.printBalanceFactors();
    
    cout << "\nInorder traversal (should be sorted): ";
    avl5.inorder();
    
    return 0;
}
```

---

## 📊 Balance Factor Summary

| BF Value | Meaning | Action Required |
|----------|---------|-----------------|
| **-2** | Right heavy by 2 | Rotation needed |
| **-1** | Right heavy by 1 | Balanced (OK) |
| **0** | Perfectly balanced | Balanced (OK) |
| **1** | Left heavy by 1 | Balanced (OK) |
| **2** | Left heavy by 2 | Rotation needed |

---

## ✅ Key Takeaways

1. **Balance factor** = height(left) - height(right)
2. **Valid range**: -1, 0, 1
3. **BF = 2 or -2** requires rotation
4. **Height of empty node** = -1
5. **Height of leaf node** = 0
6. **Update heights** after rotations
7. **Pattern recognition** (LL, LR, RR, RL) determines rotation type
8. **Balance factors** change after rotations

---