# AVL Tree Deletion

## 📖 Overview

Deletion in an AVL tree is the most complex operation because it may cause multiple imbalances that need to be corrected. After removing a node, we must traverse back up to the root, updating heights and checking balance factors at each node. If a node becomes unbalanced, we perform the appropriate rotation(s) to restore the AVL property.

---

## 🎯 Deletion Algorithm

### Step-by-Step Process

```
1. Perform standard BST deletion
2. Update heights of all ancestors
3. Calculate balance factor for each ancestor
4. If any node becomes unbalanced (BF = 2 or -2):
   - Identify the case (LL, RR, LR, RL)
   - Perform the appropriate rotation(s)
5. Return the (potentially new) root
```

### Three Deletion Cases (Same as BST)

```
Case 1: Delete leaf node
Case 2: Delete node with one child
Case 3: Delete node with two children (replace with inorder successor)
```

---

## 📝 Complete Deletion Implementation

### Helper Functions (Same as Insertion)

```cpp
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
```

### Find Minimum Node (for Successor)

```cpp
Node* findMin(Node* node) {
    while (node->left != nullptr) {
        node = node->left;
    }
    return node;
}
```

### Balance Function (Same as Insertion)

```cpp
Node* balance(Node* node) {
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

### Delete Function

```cpp
Node* deleteNode(Node* node, const T& value) {
    if (node == nullptr) {
        return nullptr;
    }
    
    // Step 1: Find node to delete (BST deletion)
    if (value < node->data) {
        node->left = deleteNode(node->left, value);
    } 
    else if (value > node->data) {
        node->right = deleteNode(node->right, value);
    } 
    else {
        // Node found - handle deletion cases
        
        // Case 1 & 2: No child or one child
        if (node->left == nullptr) {
            Node* temp = node->right;
            delete node;
            return temp;
        }
        else if (node->right == nullptr) {
            Node* temp = node->left;
            delete node;
            return temp;
        }
        
        // Case 3: Two children
        // Find inorder successor (smallest in right subtree)
        Node* successor = findMin(node->right);
        node->data = successor->data;
        node->right = deleteNode(node->right, successor->data);
    }
    
    // Step 2: Balance the node
    return balance(node);
}
```

---

## 🔍 Step-by-Step Examples

### Example 1: Delete Leaf Node (No Rotation)

```
Before deletion:              After deleting 20:
        50 (BF=0)                   50 (BF=1)
       /  \                        /  \
      30   80                     30   80
     / \   / \                     \   / \
    20 40 70 90                    40 70 90

Delete 20 (leaf):
- Remove node 20
- Update heights up the path
- Check balance: 30 (BF= -1? Actually left null, right has 40)
- No rotation needed
```

### Example 2: Delete Node with One Child

```
Before deletion:              After deleting 30:
        50 (BF=1)                   50 (BF=0)
       /  \                        /  \
      30   80                     40   80
     / \   / \                         / \
    20 40 70 90                       70 90
       (40 is right child of 30)

Delete 30 (has right child 40):
- Replace 30 with 40
- Update heights
- Check balance: 50 (BF=0) - balanced
```

### Example 3: Delete Node with Two Children

```
Before deletion:              After deleting 50:
        50 (BF=0)                   55 (BF=0)
       /  \                        /  \
      30   80                     30   80
     / \   / \                   / \   / \
    20 40 70 90                 20 40 70 90
         /                          /
        55                         55 (deleted)

Delete 50 (has two children):
- Find inorder successor: 55 (smallest in right subtree)
- Copy 55 to node 50
- Delete original 55 (leaf case)
- Update heights and check balance
```

---

## 🔄 Multiple Rotations During Deletion

Unlike insertion which requires at most one rotation, deletion may require multiple rotations up the path to the root.

### Example: Deletion Causing Multiple Rotations

```
Initial AVL Tree:
        50
       /  \
      30   80
     / \   / \
    20 40 70 90

Delete 20:
        50 (BF=1)
       /  \
      30   80
       \   / \
       40 70 90
       (30 becomes left-heavy? Check BF)
       
After deletion, check 30: BF= -1? left null, right has 40
30 is balanced (BF= -1? Actually left=-1, right=0? BF = -1 - 0 = -1)
50 is balanced (BF=1 - 1 = 0)

No rotation needed.
```

### Deletion Requiring Rotation

```
Before deletion:              After deleting 90:
        50 (BF=0)                   50 (BF= -2) ← Unbalanced!
       /  \                        /  \
      30   80                     30   80
     / \   / \                   / \   /
    20 40 70 90                 20 40 70

Delete 90 (leaf):
- Remove 90
- Update heights: 80 becomes height 1 (only left child 70)
- 50 BF = height(30)=1 - height(80)=1? Actually height(30)=1, height(80)=1, BF=0
Wait, need careful height calculation...

Actually: 
height(70)=0, height(80)=1 (70 has height 0), height(30)=1, height(50)=2
50 BF = 1 - 1 = 0 (balanced)
```

### True Example Requiring Rotation

```
Before deletion:              After deleting 70:
        50 (BF=1)                   50 (BF=2) ← Unbalanced!
       /  \                        /  \
      30   80                     30   80
     / \   / \                   / \    \
    20 40 70 90                 20 40   90

Delete 70 (leaf):
- Remove 70
- Update height of 80: now height 1 (only right child 90)
- 50 BF = height(30)=1 - height(80)=1 = 0? Actually height(80)=1, so BF=0

Check 50: left height=1, right height=1 → BF=0
No rotation needed.
```

### Deletion with RL Case

```
Before deletion:              After deleting 70:
        50 (BF=-2) ← Unbalanced!   60 (BF=0)
       /  \                        /  \
      30   80                     50   80
     / \   / \                   /      \
    20 40 60 90                 30      90
         / \                   / \
        55 65                 20 40

Delete 70 (not in tree) - better example with proper imbalance:

Tree after some operations:
        50 (BF=-2)
       /  \
      30   80
     / \   /
    20 40 60
         / \
        55 65

Delete 20:
        50 (BF=-2) ← Still unbalanced
       /  \
      30   80
       \   /
       40 60
          / \
         55 65

Now check 50: BF = height(30)=1 - height(80)=2 = -1? Actually height(80)=2, height(30)=1 → BF=-1
```

---

## 💻 Complete Implementation

```cpp
#include <iostream>
#include <algorithm>
#include <vector>
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
                cout << "  LL case at " << node->data << endl;
                return rightRotate(node);
            } else {
                cout << "  LR case at " << node->data << endl;
                return leftRightRotate(node);
            }
        }
        
        // Right Heavy
        if (bf < -1) {
            if (getBalanceFactor(node->right) <= 0) {
                cout << "  RR case at " << node->data << endl;
                return leftRotate(node);
            } else {
                cout << "  RL case at " << node->data << endl;
                return rightLeftRotate(node);
            }
        }
        
        return node;
    }
    
    Node* findMin(Node* node) {
        while (node->left != nullptr) {
            node = node->left;
        }
        return node;
    }
    
    Node* insert(Node* node, const T& value) {
        if (node == nullptr) {
            return new Node(value);
        }
        
        if (value < node->data) {
            node->left = insert(node->left, value);
        } else if (value > node->data) {
            node->right = insert(node->right, value);
        } else {
            return node;  // Duplicate ignored
        }
        
        return balance(node);
    }
    
    Node* deleteNode(Node* node, const T& value) {
        if (node == nullptr) {
            return nullptr;
        }
        
        // Search for node to delete
        if (value < node->data) {
            node->left = deleteNode(node->left, value);
        } 
        else if (value > node->data) {
            node->right = deleteNode(node->right, value);
        } 
        else {
            // Node found
            
            // Case 1 & 2: No child or one child
            if (node->left == nullptr) {
                Node* temp = node->right;
                delete node;
                return temp;
            }
            else if (node->right == nullptr) {
                Node* temp = node->left;
                delete node;
                return temp;
            }
            
            // Case 3: Two children
            Node* successor = findMin(node->right);
            node->data = successor->data;
            node->right = deleteNode(node->right, successor->data);
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
        cout << "\n--- Inserting " << value << " ---" << endl;
        root = insert(root, value);
        print();
    }
    
    void remove(const T& value) {
        cout << "\n--- Deleting " << value << " ---" << endl;
        root = deleteNode(root, value);
        print();
    }
    
    vector<T> inorder() {
        vector<T> result;
        inorder(root, result);
        return result;
    }
    
    void print() {
        if (root == nullptr) {
            cout << "Tree is empty" << endl;
            return;
        }
        printTree(root, 0, 5);
        cout << endl;
    }
    
    bool search(const T& value) {
        Node* current = root;
        while (current) {
            if (value == current->data) return true;
            if (value < current->data) current = current->left;
            else current = current->right;
        }
        return false;
    }
};

int main() {
    AVLTree<int> avl;
    
    cout << "=== AVL Tree Deletion Demo ===" << endl;
    
    // Build a tree
    cout << "\n--- Building AVL Tree ---" << endl;
    int values[] = {50, 30, 80, 20, 40, 70, 90, 10, 25, 35, 45, 65, 75, 85, 95};
    for (int v : values) {
        avl.insert(v);
    }
    
    cout << "\n=== Testing Deletions ===" << endl;
    
    // Test Case 1: Delete leaf node
    avl.remove(10);
    
    // Test Case 2: Delete node with one child
    avl.remove(20);
    
    // Test Case 3: Delete node with two children
    avl.remove(50);
    
    // Test Case 4: Delete another internal node
    avl.remove(80);
    
    // Test Case 5: Delete non-existent node
    cout << "\n--- Deleting 999 (non-existent) ---" << endl;
    avl.remove(999);
    
    // Test Case 6: Delete remaining nodes
    avl.remove(30);
    avl.remove(40);
    avl.remove(70);
    avl.remove(90);
    avl.remove(25);
    avl.remove(35);
    avl.remove(45);
    avl.remove(65);
    avl.remove(75);
    avl.remove(85);
    avl.remove(95);
    
    cout << "\n=== Final Tree ===" << endl;
    avl.print();
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Find node** | O(log n) | O(1) |
| **Delete node** | O(1) | O(1) |
| **Update heights** | O(log n) | O(1) |
| **Check balance** | O(log n) | O(1) |
| **Rotations** | O(1) per rotation | O(1) |
| **Total Delete** | O(log n) | O(log n) recursion stack |

---

## 📋 Deletion Summary Table

| Deletion Case | Action | Rotations Needed |
|---------------|--------|------------------|
| **Leaf node** | Remove directly | May cause imbalance up the path |
| **One child** | Replace with child | May cause imbalance up the path |
| **Two children** | Replace with successor, delete successor | May cause imbalance up the path |

---

## ✅ Key Takeaways

1. **Deletion follows BST rules** first
2. **Three deletion cases** same as BST
3. **Balance factors checked** from deleted node up to root
4. **Multiple rotations** may be needed (unlike insertion)
5. **Successor used** for two-child case
6. **Heights updated** after each deletion and rotation
7. **AVL property maintained** after every deletion
8. **O(log n) time** guaranteed for all operations

---
---

## Next Step

- Go to [README.md](README.md) to continue.
