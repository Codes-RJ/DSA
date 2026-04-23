# Tree Operations

## 📖 Overview

Tree operations are the fundamental actions performed on binary trees, including insertion, deletion, searching, and various utility operations. This guide provides complete implementations of all essential tree operations with detailed explanations and complexity analysis.

---

## 🎯 Core Operations

| Operation | Description | Time Complexity |
|-----------|-------------|-----------------|
| **Insertion** | Add a new node to the tree | O(n) |
| **Deletion** | Remove a node from the tree | O(n) |
| **Search** | Find a node with specific value | O(n) |
| **Update** | Modify a node's value | O(n) |
| **Find Minimum** | Find node with smallest value | O(h) |
| **Find Maximum** | Find node with largest value | O(h) |

---

## 📝 Insertion Operations

### Level Order Insertion (Complete Tree)

```cpp
template<typename T>
void BinaryTree<T>::insertLevelOrder(const T& value) {
    Node<T>* newNode = new Node<T>(value);
    
    if (!root_) {
        root_ = newNode;
        size_++;
        return;
    }
    
    queue<Node<T>*> q;
    q.push(root_);
    
    while (!q.empty()) {
        Node<T>* current = q.front();
        q.pop();
        
        if (!current->getLeft()) {
            current->setLeft(newNode);
            size_++;
            return;
        } else if (!current->getRight()) {
            current->setRight(newNode);
            size_++;
            return;
        } else {
            q.push(current->getLeft());
            q.push(current->getRight());
        }
    }
}
```

### Insert at Specific Position

```cpp
template<typename T>
bool BinaryTree<T>::insertAt(Node<T>* parent, const T& value, bool isLeft) {
    if (!parent) return false;
    
    Node<T>* newNode = new Node<T>(value);
    
    if (isLeft) {
        if (parent->getLeft()) return false;
        parent->setLeft(newNode);
    } else {
        if (parent->getRight()) return false;
        parent->setRight(newNode);
    }
    
    size_++;
    return true;
}
```

---

## 🗑️ Deletion Operations

### Delete Node (Complete Tree Deletion)

```cpp
template<typename T>
bool BinaryTree<T>::deleteNode(const T& value) {
    if (!root_) return false;
    
    // Find target node and deepest node
    Node<T>* targetNode = nullptr;
    Node<T>* deepestNode = nullptr;
    Node<T>* parentOfDeepest = nullptr;
    
    queue<Node<T>*> q;
    q.push(root_);
    
    while (!q.empty()) {
        deepestNode = q.front();
        q.pop();
        
        if (deepestNode->getData() == value) {
            targetNode = deepestNode;
        }
        
        if (deepestNode->getLeft()) {
            parentOfDeepest = deepestNode;
            q.push(deepestNode->getLeft());
        }
        if (deepestNode->getRight()) {
            parentOfDeepest = deepestNode;
            q.push(deepestNode->getRight());
        }
    }
    
    if (!targetNode) return false;
    
    // Replace target's data with deepest node's data
    targetNode->setData(deepestNode->getData());
    
    // Delete deepest node
    if (parentOfDeepest) {
        if (parentOfDeepest->getLeft() == deepestNode) {
            parentOfDeepest->setLeft(nullptr);
        } else {
            parentOfDeepest->setRight(nullptr);
        }
    }
    
    delete deepestNode;
    size_--;
    return true;
}
```

### Delete Entire Subtree

```cpp
template<typename T>
void BinaryTree<T>::deleteSubtree(Node<T>* root) {
    if (!root) return;
    
    deleteSubtree(root->getLeft());
    deleteSubtree(root->getRight());
    delete root;
}

template<typename T>
bool BinaryTree<T>::deleteSubtreeAt(const T& value) {
    if (!root_) return false;
    
    if (root_->getData() == value) {
        clear();
        return true;
    }
    
    queue<Node<T>*> q;
    q.push(root_);
    
    while (!q.empty()) {
        Node<T>* current = q.front();
        q.pop();
        
        if (current->getLeft() && current->getLeft()->getData() == value) {
            deleteSubtree(current->getLeft());
            current->setLeft(nullptr);
            size_ = calculateSize(root_);
            return true;
        }
        
        if (current->getRight() && current->getRight()->getData() == value) {
            deleteSubtree(current->getRight());
            current->setRight(nullptr);
            size_ = calculateSize(root_);
            return true;
        }
        
        if (current->getLeft()) q.push(current->getLeft());
        if (current->getRight()) q.push(current->getRight());
    }
    
    return false;
}
```

### Delete Leaf Nodes

```cpp
template<typename T>
bool BinaryTree<T>::deleteLeaf(const T& value) {
    if (!root_) return false;
    
    // Special case: root is leaf
    if (root_->isLeaf() && root_->getData() == value) {
        delete root_;
        root_ = nullptr;
        size_ = 0;
        return true;
    }
    
    queue<Node<T>*> q;
    q.push(root_);
    
    while (!q.empty()) {
        Node<T>* current = q.front();
        q.pop();
        
        // Check left child
        if (current->getLeft() && current->getLeft()->isLeaf() && 
            current->getLeft()->getData() == value) {
            delete current->getLeft();
            current->setLeft(nullptr);
            size_--;
            return true;
        }
        
        // Check right child
        if (current->getRight() && current->getRight()->isLeaf() && 
            current->getRight()->getData() == value) {
            delete current->getRight();
            current->setRight(nullptr);
            size_--;
            return true;
        }
        
        if (current->getLeft()) q.push(current->getLeft());
        if (current->getRight()) q.push(current->getRight());
    }
    
    return false;
}
```

---

## 🔍 Search Operations

### Basic Search

```cpp
template<typename T>
Node<T>* BinaryTree<T>::search(Node<T>* node, const T& value) const {
    if (!node) return nullptr;
    if (node->getData() == value) return node;
    
    Node<T>* leftResult = search(node->getLeft(), value);
    if (leftResult) return leftResult;
    
    return search(node->getRight(), value);
}

template<typename T>
bool BinaryTree<T>::contains(const T& value) const {
    return search(root_, value) != nullptr;
}
```

### Find Parent of a Node

```cpp
template<typename T>
Node<T>* BinaryTree<T>::findParent(Node<T>* node, const T& value) const {
    if (!node) return nullptr;
    
    if ((node->getLeft() && node->getLeft()->getData() == value) ||
        (node->getRight() && node->getRight()->getData() == value)) {
        return node;
    }
    
    Node<T>* leftResult = findParent(node->getLeft(), value);
    if (leftResult) return leftResult;
    
    return findParent(node->getRight(), value);
}
```

### Find Level of a Node

```cpp
template<typename T>
int BinaryTree<T>::findLevel(Node<T>* node, const T& value, int level) const {
    if (!node) return -1;
    if (node->getData() == value) return level;
    
    int leftLevel = findLevel(node->getLeft(), value, level + 1);
    if (leftLevel != -1) return leftLevel;
    
    return findLevel(node->getRight(), value, level + 1);
}

template<typename T>
int BinaryTree<T>::getLevel(const T& value) const {
    return findLevel(root_, value, 0);
}
```

---

## 📈 Min/Max Operations

### Find Minimum Value

```cpp
template<typename T>
T BinaryTree<T>::findMin() const {
    if (!root_) throw runtime_error("Tree is empty");
    
    Node<T>* current = root_;
    while (current->getLeft()) {
        current = current->getLeft();
    }
    return current->getData();
}

template<typename T>
Node<T>* BinaryTree<T>::findMinNode(Node<T>* node) const {
    if (!node) return nullptr;
    
    Node<T>* current = node;
    while (current->getLeft()) {
        current = current->getLeft();
    }
    return current;
}
```

### Find Maximum Value

```cpp
template<typename T>
T BinaryTree<T>::findMax() const {
    if (!root_) throw runtime_error("Tree is empty");
    
    Node<T>* current = root_;
    while (current->getRight()) {
        current = current->getRight();
    }
    return current->getData();
}

template<typename T>
Node<T>* BinaryTree<T>::findMaxNode(Node<T>* node) const {
    if (!node) return nullptr;
    
    Node<T>* current = node;
    while (current->getRight()) {
        current = current->getRight();
    }
    return current;
}
```

---

## 🔄 Update Operations

### Update Node Value

```cpp
template<typename T>
bool BinaryTree<T>::update(const T& oldValue, const T& newValue) {
    Node<T>* node = search(root_, oldValue);
    if (!node) return false;
    
    node->setData(newValue);
    return true;
}
```

### Swap Subtrees

```cpp
template<typename T>
bool BinaryTree<T>::swapSubtrees(const T& value) {
    Node<T>* node = search(root_, value);
    if (!node) return false;
    
    Node<T>* temp = node->getLeft();
    node->setLeft(node->getRight());
    node->setRight(temp);
    
    return true;
}
```

---

## 📏 Utility Operations

### Calculate Size (Number of Nodes)

```cpp
template<typename T>
int BinaryTree<T>::calculateSize(Node<T>* node) const {
    if (!node) return 0;
    return 1 + calculateSize(node->getLeft()) + calculateSize(node->getRight());
}
```

### Calculate Diameter

```cpp
template<typename T>
int BinaryTree<T>::calculateDiameter(Node<T>* node, int& height) const {
    if (!node) {
        height = -1;
        return 0;
    }
    
    int leftHeight = 0, rightHeight = 0;
    int leftDiameter = calculateDiameter(node->getLeft(), leftHeight);
    int rightDiameter = calculateDiameter(node->getRight(), rightHeight);
    
    height = 1 + max(leftHeight, rightHeight);
    
    return max({leftDiameter, rightDiameter, leftHeight + rightHeight + 2});
}

template<typename T>
int BinaryTree<T>::diameter() const {
    int height = 0;
    return calculateDiameter(root_, height);
}
```

### Check if Two Trees are Identical

```cpp
template<typename T>
bool BinaryTree<T>::isIdentical(Node<T>* node1, Node<T>* node2) const {
    if (!node1 && !node2) return true;
    if (!node1 || !node2) return false;
    
    return (node1->getData() == node2->getData()) &&
           isIdentical(node1->getLeft(), node2->getLeft()) &&
           isIdentical(node1->getRight(), node2->getRight());
}
```

### Check if Tree is a Subtree

```cpp
template<typename T>
bool BinaryTree<T>::isSubtree(Node<T>* tree, Node<T>* subtree) const {
    if (!subtree) return true;
    if (!tree) return false;
    
    if (isIdentical(tree, subtree)) return true;
    
    return isSubtree(tree->getLeft(), subtree) || 
           isSubtree(tree->getRight(), subtree);
}
```

---

## 🧪 Example Usage

```cpp
int main() {
    BinaryTree<int> tree;
    
    // Insert nodes
    tree.insertLevelOrder(1);
    tree.insertLevelOrder(2);
    tree.insertLevelOrder(3);
    tree.insertLevelOrder(4);
    tree.insertLevelOrder(5);
    tree.insertLevelOrder(6);
    tree.insertLevelOrder(7);
    
    cout << "Tree structure:" << endl;
    tree.printPretty();
    
    // Search operations
    cout << "\nContains 5: " << (tree.contains(5) ? "Yes" : "No") << endl;
    cout << "Level of 5: " << tree.getLevel(5) << endl;
    
    // Min/Max
    cout << "\nMinimum value: " << tree.findMin() << endl;
    cout << "Maximum value: " << tree.findMax() << endl;
    
    // Update
    tree.update(5, 50);
    cout << "\nAfter updating 5 to 50:" << endl;
    tree.printPretty();
    
    // Swap subtrees
    tree.swapSubtrees(2);
    cout << "\nAfter swapping subtrees of node 2:" << endl;
    tree.printPretty();
    
    // Diameter
    cout << "\nTree diameter: " << tree.diameter() << endl;
    
    // Delete operations
    tree.deleteLeaf(50);
    cout << "\nAfter deleting leaf 50:" << endl;
    tree.printPretty();
    
    return 0;
}
```

---

## 📊 Complexity Summary

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Insert (level order) | O(n) | O(n) |
| Delete (any node) | O(n) | O(n) |
| Search | O(n) | O(h) |
| Find Min/Max | O(h) | O(1) |
| Update | O(n) | O(h) |
| Swap Subtrees | O(n) | O(h) |
| Diameter | O(n) | O(h) |
| Identical Check | O(n) | O(h) |

---

## ✅ Key Takeaways

1. **Insertion** in general binary tree is O(n) (no ordering property)
2. **Deletion** requires finding deepest node for replacement
3. **Search** traverses entire tree in worst case
4. **Min/Max** operations are O(h) when following left/right pointers
5. **Update** is search + modification
6. **Swap subtrees** is constant time after finding target
7. **Diameter** calculation uses post-order traversal

---

## Next Step

- Go to [BST](../02_BST//README.md) to start with Binary Search Trees.
