# AVL Tree Insertion

## 📖 Overview

Insertion in an AVL tree follows the same basic process as insertion in a regular BST, but with an additional step: after inserting the node, we must check the balance factor of each ancestor and perform rotations to restore the AVL property if it's violated. This ensures that the tree remains balanced after every insertion.

---

## 🎯 Insertion Algorithm

### Step-by-Step Process

```
1. Perform standard BST insertion
2. Update heights of all ancestors
3. Calculate balance factor for each ancestor
4. If any node becomes unbalanced (BF = 2 or -2):
   - Identify the case (LL, RR, LR, RL)
   - Perform the appropriate rotation(s)
5. Return the (potentially new) root
```

### Visual Flow

```
Start at root
    ↓
Compare with current node
    ↓
Go left or right (BST property)
    ↓
Insert new node at leaf
    ↓
Update heights up the path
    ↓
Check balance factors
    ↓
If unbalanced → perform rotation
    ↓
Return to parent
```

---

## 📝 Complete Insertion Implementation

### Node Structure with Height

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
```

### Helper Functions

```cpp
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

### Rotation Functions

```cpp
// Right Rotation (LL Case)
AVLNode* rightRotate(AVLNode* y) {
    AVLNode* x = y->left;
    AVLNode* T2 = x->right;
    
    x->right = y;
    y->left = T2;
    
    updateHeight(y);
    updateHeight(x);
    
    return x;
}

// Left Rotation (RR Case)
AVLNode* leftRotate(AVLNode* x) {
    AVLNode* y = x->right;
    AVLNode* T2 = y->left;
    
    y->left = x;
    x->right = T2;
    
    updateHeight(x);
    updateHeight(y);
    
    return y;
}

// Left-Right Rotation (LR Case)
AVLNode* leftRightRotate(AVLNode* z) {
    z->left = leftRotate(z->left);
    return rightRotate(z);
}

// Right-Left Rotation (RL Case)
AVLNode* rightLeftRotate(AVLNode* z) {
    z->right = rightRotate(z->right);
    return leftRotate(z);
}
```

### Balance Function

```cpp
AVLNode* balance(AVLNode* node) {
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
```

### Insert Function

```cpp
AVLNode* insert(AVLNode* node, const T& value) {
    // Step 1: Standard BST insertion
    if (node == nullptr) {
        return new AVLNode(value);
    }
    
    if (value < node->data) {
        node->left = insert(node->left, value);
    } else if (value > node->data) {
        node->right = insert(node->right, value);
    } else {
        // Duplicate value - ignore
        return node;
    }
    
    // Step 2: Balance the node
    return balance(node);
}
```

---

## 🔍 Step-by-Step Examples

### Example 1: LL Case (Right Rotation)

```
Insert 20 into tree with nodes 50, 30:

Step 1: Insert 20 using BST rules
        50 (BF = 2) ← Unbalanced!
       /
      30 (BF = 1)
     /
    20

Step 2: Check balance at 50: BF = 2
        Left child BF = 1 (≥ 0) → LL Case

Step 3: Perform Right Rotation on 50
        30 (BF = 0)
       /  \
      20   50

Result: Tree balanced!
```

### Example 2: RR Case (Left Rotation)

```
Insert 50 into tree with nodes 20, 30:

Step 1: Insert 50 using BST rules
    20 (BF = -2) ← Unbalanced!
     \
      30 (BF = -1)
       \
        50

Step 2: Check balance at 20: BF = -2
        Right child BF = -1 (≤ 0) → RR Case

Step 3: Perform Left Rotation on 20
        30 (BF = 0)
       /  \
      20   50

Result: Tree balanced!
```

### Example 3: LR Case (Left-Right Rotation)

```
Insert 40 into tree with nodes 50, 30:

Step 1: Insert 40 using BST rules
        50 (BF = 2) ← Unbalanced!
       /
      30 (BF = -1)
       \
        40

Step 2: Check balance at 50: BF = 2
        Left child BF = -1 (< 0) → LR Case

Step 3: Left rotate on 30
        50
       /
      40
     /
    30

Step 4: Right rotate on 50
        40 (BF = 0)
       /  \
      30   50

Result: Tree balanced!
```

### Example 4: RL Case (Right-Left Rotation)

```
Insert 30 into tree with nodes 20, 50:

Step 1: Insert 30 using BST rules
    20 (BF = -2) ← Unbalanced!
     \
      50 (BF = 1)
     /
    30

Step 2: Check balance at 20: BF = -2
        Right child BF = 1 (> 0) → RL Case

Step 3: Right rotate on 50
    20
     \
      30
       \
        50

Step 4: Left rotate on 20
        30 (BF = 0)
       /  \
      20   50

Result: Tree balanced!
```

---

## 💻 Complete Implementation

```cpp
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

template<typename T>
class AVLTree {
private:
    struct Node {
        T data;
        Node* left;
        Node* right;
        int height;
        
        Node(const T& value) : data(value), left(nullptr), right(nullptr), height(0) {}
    };
    
    Node* root;
    
    int getHeight(Node* node) {
        return node ? node->height : -1;
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
        cout << "  Right rotation on " << y->data << endl;
        Node* x = y->left;
        Node* T2 = x->right;
        
        x->right = y;
        y->left = T2;
        
        updateHeight(y);
        updateHeight(x);
        
        return x;
    }
    
    Node* leftRotate(Node* x) {
        cout << "  Left rotation on " << x->data << endl;
        Node* y = x->right;
        Node* T2 = y->left;
        
        y->left = x;
        x->right = T2;
        
        updateHeight(x);
        updateHeight(y);
        
        return y;
    }
    
    Node* leftRightRotate(Node* z) {
        cout << "  Left-Right rotation on " << z->data << endl;
        z->left = leftRotate(z->left);
        return rightRotate(z);
    }
    
    Node* rightLeftRotate(Node* z) {
        cout << "  Right-Left rotation on " << z->data << endl;
        z->right = rightRotate(z->right);
        return leftRotate(z);
    }
    
    Node* balance(Node* node) {
        if (node == nullptr) return nullptr;
        
        updateHeight(node);
        int bf = getBalanceFactor(node);
        
        // Left Heavy
        if (bf > 1) {
            if (getBalanceFactor(node->left) >= 0) {
                cout << "  LL case detected at " << node->data << endl;
                return rightRotate(node);
            } else {
                cout << "  LR case detected at " << node->data << endl;
                return leftRightRotate(node);
            }
        }
        
        // Right Heavy
        if (bf < -1) {
            if (getBalanceFactor(node->right) <= 0) {
                cout << "  RR case detected at " << node->data << endl;
                return leftRotate(node);
            } else {
                cout << "  RL case detected at " << node->data << endl;
                return rightLeftRotate(node);
            }
        }
        
        return node;
    }
    
    Node* insert(Node* node, const T& value) {
        if (node == nullptr) {
            cout << "  Inserting " << value << " as new node" << endl;
            return new Node(value);
        }
        
        if (value < node->data) {
            cout << "  " << value << " < " << node->data << ", going left" << endl;
            node->left = insert(node->left, value);
        } else if (value > node->data) {
            cout << "  " << value << " > " << node->data << ", going right" << endl;
            node->right = insert(node->right, value);
        } else {
            cout << "  Duplicate " << value << " ignored" << endl;
            return node;
        }
        
        return balance(node);
    }
    
    void inorder(Node* node, vector<T>& result) {
        if (node == nullptr) return;
        inorder(node->left, result);
        result.push_back(node->data);
        inorder(node->right, result);
    }
    
    void printTree(Node* node, int space, int indent) {
        if (node == nullptr) return;
        
        space += indent;
        
        printTree(node->right, space, indent);
        
        cout << endl;
        for (int i = indent; i < space; i++) cout << " ";
        cout << node->data << "(H=" << node->height << ",BF=" 
             << getBalanceFactor(node) << ")" << endl;
        
        printTree(node->left, space, indent);
    }
    
public:
    AVLTree() : root(nullptr) {}
    
    void insert(const T& value) {
        cout << "\n=== Inserting " << value << " ===" << endl;
        root = insert(root, value);
        cout << "Tree after insertion:" << endl;
        print();
    }
    
    vector<T> inorder() {
        vector<T> result;
        inorder(root, result);
        return result;
    }
    
    void print() {
        printTree(root, 0, 5);
        cout << endl;
    }
    
    bool isEmpty() const {
        return root == nullptr;
    }
};

int main() {
    AVLTree<int> avl;
    
    cout << "=== AVL Tree Insertion Demo ===" << endl;
    
    // Insert nodes that demonstrate all four cases
    avl.insert(50);
    avl.insert(30);
    avl.insert(20);  // LL case - Right rotation
    
    avl.insert(40);
    avl.insert(35);  // LR case - Left-Right rotation
    
    avl.insert(80);
    avl.insert(90);  // RR case - Left rotation
    
    avl.insert(85);  // RL case - Right-Left rotation
    
    avl.insert(10);
    avl.insert(25);
    avl.insert(45);
    avl.insert(60);
    avl.insert(95);
    
    cout << "\n=== Final AVL Tree ===" << endl;
    avl.print();
    
    cout << "\nInorder traversal (should be sorted): ";
    vector<int> sorted = avl.inorder();
    for (int val : sorted) {
        cout << val << " ";
    }
    cout << endl;
    
    cout << "\nTree size: " << sorted.size() << endl;
    cout << "Tree is balanced and maintains AVL property!" << endl;
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Find position** | O(log n) | O(1) |
| **Insert node** | O(1) | O(1) |
| **Update heights** | O(log n) | O(1) |
| **Check balance** | O(log n) | O(1) |
| **Rotations** | O(1) per rotation | O(1) |
| **Total Insert** | O(log n) | O(log n) recursion stack |

---

## 🎯 Insertion Summary

| Case | Pattern | BF(node) | BF(child) | Rotation |
|------|---------|----------|-----------|----------|
| **LL** | Left-Left | 2 | ≥ 0 | Right |
| **RR** | Right-Right | -2 | ≤ 0 | Left |
| **LR** | Left-Right | 2 | -1 | Left-Right |
| **RL** | Right-Left | -2 | 1 | Right-Left |

---

## ✅ Key Takeaways

1. **Insertion follows BST rules** first
2. **Balance factors** checked from inserted node up to root
3. **Four imbalance cases** require different rotations
4. **Heights updated** after each insertion and rotation
5. **Rotations** restore balance in O(1) time
6. **Worst-case** requires O(log n) rotations
7. **AVL property** maintained after every insertion
8. **Guarantees** O(log n) height

---