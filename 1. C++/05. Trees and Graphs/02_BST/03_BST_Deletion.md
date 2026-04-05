# BST Deletion

## 📖 Overview

Deletion in a Binary Search Tree (BST) is the most complex fundamental operation because it must maintain the BST property after removing a node. There are three distinct cases to handle: deleting a leaf node, deleting a node with one child, and deleting a node with two children. Understanding these cases is crucial for implementing a correct BST.

---

## 🎯 The Three Deletion Cases

| Case | Description | Difficulty |
|------|-------------|------------|
| **Case 1** | Node has no children (leaf) | Easy |
| **Case 2** | Node has one child | Medium |
| **Case 3** | Node has two children | Hard |

---

## 📝 Case 1: Deleting a Leaf Node

### Description
The node to be deleted has no children. This is the simplest case.

### Algorithm
```
1. Find the node to delete and its parent
2. Set parent's left/right pointer to null
3. Delete the node
```

### Visual Example

```
Before deletion:              After deletion:
    50                            50
   /  \                          /  \
  30   80                       30   80
 / \   / \                     / \   / \
20 40 70 90                  20 40 70 90
                              (90 removed)

Delete leaf node 90:
- Find node 90 (right child of 80)
- Set 80's right pointer to nullptr
- Delete node 90
```

### Implementation

```cpp
// Case 1: Leaf node
if (nodeToDelete->left == nullptr && nodeToDelete->right == nullptr) {
    if (parent->left == nodeToDelete) {
        parent->left = nullptr;
    } else {
        parent->right = nullptr;
    }
    delete nodeToDelete;
}
```

---

## 📝 Case 2: Node with One Child

### Description
The node to be deleted has exactly one child (either left or right).

### Algorithm
```
1. Find the node to delete and its parent
2. Identify the single child
3. Link parent directly to the child
4. Delete the node
```

### Visual Examples

#### Deleting node with left child only

```
Before deletion:              After deletion:
    50                            50
   /  \                          /  \
  30   80                       20   80
 /     / \                           / \
20    70 90                         70 90

Delete node 30 (has left child 20):
- Parent (50) left pointer points to 20
- Delete node 30
```

#### Deleting node with right child only

```
Before deletion:              After deletion:
    50                            50
   /  \                          /  \
  30   80                       40   80
   \   / \                           / \
    40 70 90                         70 90

Delete node 30 (has right child 40):
- Parent (50) left pointer points to 40
- Delete node 30
```

### Implementation

```cpp
// Case 2: Node with one child
if (nodeToDelete->left != nullptr && nodeToDelete->right == nullptr) {
    // Only left child exists
    if (parent->left == nodeToDelete) {
        parent->left = nodeToDelete->left;
    } else {
        parent->right = nodeToDelete->left;
    }
    delete nodeToDelete;
}
else if (nodeToDelete->left == nullptr && nodeToDelete->right != nullptr) {
    // Only right child exists
    if (parent->left == nodeToDelete) {
        parent->left = nodeToDelete->right;
    } else {
        parent->right = nodeToDelete->right;
    }
    delete nodeToDelete;
}
```

---

## 📝 Case 3: Node with Two Children

### Description
The node to be deleted has both left and right children. This is the most complex case.

### Algorithm
```
1. Find the node to delete
2. Find the inorder successor (smallest node in right subtree)
   OR inorder predecessor (largest node in left subtree)
3. Copy successor's value to the node to delete
4. Delete the successor node (which will be a leaf or have one child)
```

### Visual Example (Using Inorder Successor)

```
Before deletion:                    After deletion:
        50                              55
       /  \                            /  \
      30   80                         30   80
     / \   / \                       / \   / \
    20 40 70 90                     20 40 70 90
         /                              /
        55                              (deleted)

Delete node 50 (has two children):
- Find inorder successor: 55 (smallest in right subtree)
- Copy 55 to node 50
- Delete original node 55 (now a leaf)
```

### Why Successor/Predecessor Works

The inorder successor is the smallest node in the right subtree. It has two important properties:
1. It is greater than all nodes in left subtree
2. It is smaller than all other nodes in right subtree

Therefore, replacing the deleted node with its successor maintains the BST property.

---

## 💻 Complete Deletion Implementation

### Recursive Deletion

```cpp
template<typename T>
class BST {
private:
    struct Node {
        T data;
        Node* left;
        Node* right;
        Node(const T& value) : data(value), left(nullptr), right(nullptr) {}
    };
    
    Node* root;
    
    // Find minimum value node in subtree
    Node* findMin(Node* node) {
        while (node->left != nullptr) {
            node = node->left;
        }
        return node;
    }
    
    // Recursive deletion
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
            // Find inorder successor
            Node* successor = findMin(node->right);
            node->data = successor->data;
            node->right = deleteNode(node->right, successor->data);
        }
        
        return node;
    }
    
public:
    void remove(const T& value) {
        root = deleteNode(root, value);
    }
};
```

### Iterative Deletion with Parent Tracking

```cpp
template<typename T>
bool BST<T>::removeIterative(const T& value) {
    if (root == nullptr) return false;
    
    // Step 1: Find node to delete and its parent
    Node* parent = nullptr;
    Node* current = root;
    
    while (current != nullptr && current->data != value) {
        parent = current;
        if (value < current->data) {
            current = current->left;
        } else {
            current = current->right;
        }
    }
    
    // Node not found
    if (current == nullptr) return false;
    
    // Step 2: Handle deletion cases
    
    // Case 1: Leaf node
    if (current->left == nullptr && current->right == nullptr) {
        if (parent == nullptr) {
            // Deleting root
            root = nullptr;
        } else if (parent->left == current) {
            parent->left = nullptr;
        } else {
            parent->right = nullptr;
        }
        delete current;
    }
    // Case 2a: Only left child
    else if (current->left != nullptr && current->right == nullptr) {
        if (parent == nullptr) {
            root = current->left;
        } else if (parent->left == current) {
            parent->left = current->left;
        } else {
            parent->right = current->left;
        }
        delete current;
    }
    // Case 2b: Only right child
    else if (current->left == nullptr && current->right != nullptr) {
        if (parent == nullptr) {
            root = current->right;
        } else if (parent->left == current) {
            parent->left = current->right;
        } else {
            parent->right = current->right;
        }
        delete current;
    }
    // Case 3: Two children
    else {
        // Find inorder successor and its parent
        Node* successorParent = current;
        Node* successor = current->right;
        
        while (successor->left != nullptr) {
            successorParent = successor;
            successor = successor->left;
        }
        
        // Copy successor's value to current node
        current->data = successor->data;
        
        // Delete successor (which will be a leaf or have right child)
        if (successorParent->left == successor) {
            successorParent->left = successor->right;
        } else {
            successorParent->right = successor->right;
        }
        
        delete successor;
    }
    
    return true;
}
```

---

## 📊 Complexity Analysis

### Time Complexity

| Case | Complexity | Description |
|------|------------|-------------|
| **Best Case** | O(1) | Deleting root or leaf with direct access |
| **Average Case** | O(log n) | Tree is reasonably balanced |
| **Worst Case** | O(n) | Tree is skewed |

### Space Complexity

| Implementation | Space | Description |
|----------------|-------|-------------|
| **Recursive** | O(h) | Call stack depth equals height |
| **Iterative** | O(1) | No recursion overhead |

### Case Breakdown

| Case | Search Time | Deletion Time | Total |
|------|-------------|---------------|-------|
| Leaf | O(h) | O(1) | O(h) |
| One Child | O(h) | O(1) | O(h) |
| Two Children | O(h) | O(h) (finding successor) | O(h) |

Where h = height of tree

---

## 🎯 Detailed Examples

### Example 1: Delete Leaf Node (20)

```
Initial tree:                 Step 1: Find 20
        50                        50
       /  \                       /  \
      30   80                    30   80
     / \   / \                   / \   / \
    20 40 70 90                 20 40 70 90
                               (found)

Step 2: Delete 20            Step 3: Result
        50                        50
       /  \                       /  \
      30   80                    30   80
       \   / \                     \   / \
       40 70 90                     40 70 90
```

### Example 2: Delete Node with One Child (30)

```
Initial tree:                 Step 1: Find 30
        50                        50
       /  \                       /  \
      30   80                    30   80
     / \   / \                   / \   / \
    20 40 70 90                 20 40 70 90
                               (found, has child 20)

Step 2: Link parent to child  Step 3: Delete 30
        50                        50
       /  \                       /  \
      20   80                    20   80
         / \                         / \
        40 70 90                    40 70 90
```

### Example 3: Delete Node with Two Children (50 - root)

```
Initial tree:                 Step 1: Find 50 (root)
        50
       /  \
      30   80
     / \   / \
    20 40 70 90

Step 2: Find inorder successor (55)
        50
       /  \
      30   80
     / \   / \
    20 40 70 90
         /
        55

Step 3: Copy successor value   Step 4: Delete successor
        55                        55
       /  \                       /  \
      30   80                    30   80
     / \   / \                   / \   / \
    20 40 70 90                 20 40 70 90
```

---

## 🔄 Successor vs Predecessor

### Using Inorder Successor (Right subtree minimum)

```cpp
Node* findSuccessor(Node* node) {
    Node* current = node->right;
    while (current->left != nullptr) {
        current = current->left;
    }
    return current;
}
```

### Using Inorder Predecessor (Left subtree maximum)

```cpp
Node* findPredecessor(Node* node) {
    Node* current = node->left;
    while (current->right != nullptr) {
        current = current->right;
    }
    return current;
}
```

### Comparison

| Aspect | Successor | Predecessor |
|--------|-----------|-------------|
| **Direction** | Right subtree, then left | Left subtree, then right |
| **When to Use** | Default choice | Symmetric alternative |
| **Result** | Next larger value | Next smaller value |

---

## 🎯 Special Cases

### Case 1: Deleting Root with No Children

```cpp
if (root->left == nullptr && root->right == nullptr) {
    delete root;
    root = nullptr;
}
```

### Case 2: Deleting Root with One Child

```cpp
if (root->left != nullptr && root->right == nullptr) {
    Node* temp = root->left;
    delete root;
    root = temp;
}
```

### Case 3: Deleting Root with Two Children

```cpp
Node* successor = findMin(root->right);
root->data = successor->data;
root->right = deleteNode(root->right, successor->data);
```

### Case 4: Deleting Node Not Found

```cpp
if (current == nullptr) {
    return false;  // Node doesn't exist
}
```

---

## 💡 Best Practices

1. **Always find the node first** before attempting deletion
2. **Track parent pointer** for iterative deletion
3. **Use recursion** for cleaner code (watch stack depth)
4. **Handle root separately** when parent is null
5. **Choose successor or predecessor** consistently
6. **Update size counter** after successful deletion
7. **Test all three cases** thoroughly

---

## 🧪 Complete Test Program

```cpp
int main() {
    BST<int> bst;
    
    // Insert nodes
    int values[] = {50, 30, 80, 20, 40, 70, 90, 55, 85, 95};
    for (int v : values) {
        bst.insert(v);
    }
    
    cout << "Original tree:\n";
    bst.print();
    
    // Test Case 1: Delete leaf (20)
    cout << "\nDeleting leaf node 20:\n";
    bst.remove(20);
    bst.print();
    
    // Test Case 2: Delete node with one child (30)
    cout << "\nDeleting node with one child 30:\n";
    bst.remove(30);
    bst.print();
    
    // Test Case 3: Delete node with two children (80)
    cout << "\nDeleting node with two children 80:\n";
    bst.remove(80);
    bst.print();
    
    // Test Case 4: Delete root (50)
    cout << "\nDeleting root 50:\n";
    bst.remove(50);
    bst.print();
    
    // Test Case 5: Delete non-existent node
    cout << "\nDeleting non-existent node 999:\n";
    cout << "Success: " << (bst.remove(999) ? "Yes" : "No") << endl;
    
    return 0;
}
```

---

## ✅ Key Takeaways

1. **Three cases**: leaf, one child, two children
2. **Leaf deletion**: Simply remove and update parent pointer
3. **One child**: Replace node with its child
4. **Two children**: Replace with inorder successor/predecessor
5. **Successor**: Smallest node in right subtree
6. **Predecessor**: Largest node in left subtree
7. **Root deletion**: Special case with no parent
8. **Time complexity**: O(h) where h is tree height
9. **Space complexity**: O(h) recursive, O(1) iterative

---