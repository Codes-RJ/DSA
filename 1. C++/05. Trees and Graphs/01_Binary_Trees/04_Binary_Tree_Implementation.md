# Binary Tree Implementation

## 📖 Overview

This guide provides complete implementation of a binary tree data structure in C++, including all fundamental operations, constructors, destructors, and utility functions. A binary tree is a tree where each node has at most two children (left and right).

---

## 🎯 Complete Implementation

### Node Structure

```cpp
#include <iostream>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>
using namespace std;

template<typename T>
class BinaryTree;

template<typename T>
class Node {
private:
    T data_;
    Node<T>* left_;
    Node<T>* right_;
    
public:
    Node(const T& data) : data_(data), left_(nullptr), right_(nullptr) {}
    
    T& getData() { return data_; }
    const T& getData() const { return data_; }
    void setData(const T& data) { data_ = data; }
    
    Node<T>* getLeft() { return left_; }
    const Node<T>* getLeft() const { return left_; }
    void setLeft(Node<T>* left) { left_ = left; }
    
    Node<T>* getRight() { return right_; }
    const Node<T>* getRight() const { return right_; }
    void setRight(Node<T>* right) { right_ = right; }
    
    bool isLeaf() const { return left_ == nullptr && right_ == nullptr; }
    bool hasLeft() const { return left_ != nullptr; }
    bool hasRight() const { return right_ != nullptr; }
    
    friend class BinaryTree<T>;
};
```

---

## 🏗️ Binary Tree Class

### Class Declaration

```cpp
template<typename T>
class BinaryTree {
private:
    Node<T>* root_;
    size_t size_;
    
    // Private helper methods
    void clear(Node<T>* node);
    Node<T>* copy(Node<T>* node);
    int getHeight(Node<T>* node) const;
    void preorder(Node<T>* node, vector<T>& result) const;
    void inorder(Node<T>* node, vector<T>& result) const;
    void postorder(Node<T>* node, vector<T>& result) const;
    void levelOrder(Node<T>* node, vector<T>& result) const;
    bool isFull(Node<T>* node) const;
    bool isComplete(Node<T>* node) const;
    bool isPerfect(Node<T>* node) const;
    bool isBalanced(Node<T>* node) const;
    int getLeafCount(Node<T>* node) const;
    int getInternalCount(Node<T>* node) const;
    Node<T>* find(Node<T>* node, const T& value) const;
    
public:
    // Constructors and Destructor
    BinaryTree();
    BinaryTree(const BinaryTree& other);
    BinaryTree(BinaryTree&& other) noexcept;
    ~BinaryTree();
    
    // Assignment operators
    BinaryTree& operator=(const BinaryTree& other);
    BinaryTree& operator=(BinaryTree&& other) noexcept;
    
    // Basic operations
    void insert(const T& value);
    bool remove(const T& value);
    bool search(const T& value) const;
    void clear();
    
    // Properties
    bool isEmpty() const { return root_ == nullptr; }
    size_t size() const { return size_; }
    int height() const { return getHeight(root_); }
    int leafCount() const { return getLeafCount(root_); }
    int internalCount() const { return getInternalCount(root_); }
    
    // Tree classification
    bool isFull() const { return isFull(root_); }
    bool isComplete() const { return isComplete(root_); }
    bool isPerfect() const { return isPerfect(root_); }
    bool isBalanced() const { return isBalanced(root_); }
    
    // Traversals
    vector<T> preorder() const;
    vector<T> inorder() const;
    vector<T> postorder() const;
    vector<T> levelOrder() const;
    
    // Display
    void printTree() const;
    void printPretty() const;
};
```

---

## 📝 Implementation

### Constructors and Destructor

```cpp
template<typename T>
BinaryTree<T>::BinaryTree() : root_(nullptr), size_(0) {}

template<typename T>
BinaryTree<T>::BinaryTree(const BinaryTree& other) 
    : root_(copy(other.root_)), size_(other.size_) {}

template<typename T>
BinaryTree<T>::BinaryTree(BinaryTree&& other) noexcept
    : root_(other.root_), size_(other.size_) {
    other.root_ = nullptr;
    other.size_ = 0;
}

template<typename T>
BinaryTree<T>::~BinaryTree() {
    clear();
}

template<typename T>
void BinaryTree<T>::clear(Node<T>* node) {
    if (node) {
        clear(node->getLeft());
        clear(node->getRight());
        delete node;
    }
}

template<typename T>
void BinaryTree<T>::clear() {
    clear(root_);
    root_ = nullptr;
    size_ = 0;
}
```

### Copy and Move Operations

```cpp
template<typename T>
Node<T>* BinaryTree<T>::copy(Node<T>* node) {
    if (!node) return nullptr;
    
    Node<T>* newNode = new Node<T>(node->getData());
    newNode->setLeft(copy(node->getLeft()));
    newNode->setRight(copy(node->getRight()));
    
    return newNode;
}

template<typename T>
BinaryTree<T>& BinaryTree<T>::operator=(const BinaryTree& other) {
    if (this != &other) {
        clear();
        root_ = copy(other.root_);
        size_ = other.size_;
    }
    return *this;
}

template<typename T>
BinaryTree<T>& BinaryTree<T>::operator=(BinaryTree&& other) noexcept {
    if (this != &other) {
        clear();
        root_ = other.root_;
        size_ = other.size_;
        other.root_ = nullptr;
        other.size_ = 0;
    }
    return *this;
}
```

### Insertion Operation

```cpp
template<typename T>
void BinaryTree<T>::insert(const T& value) {
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

### Deletion Operation

```cpp
template<typename T>
bool BinaryTree<T>::remove(const T& value) {
    if (!root_) return false;
    
    if (root_->getData() == value && !root_->getLeft() && !root_->getRight()) {
        delete root_;
        root_ = nullptr;
        size_--;
        return true;
    }
    
    queue<Node<T>*> q;
    q.push(root_);
    Node<T>* targetNode = nullptr;
    Node<T>* deepestNode = nullptr;
    Node<T>* parentOfDeepest = nullptr;
    
    // Find target node and deepest node
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
    
    // Replace target node's data with deepest node's data
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

### Search Operation

```cpp
template<typename T>
Node<T>* BinaryTree<T>::find(Node<T>* node, const T& value) const {
    if (!node) return nullptr;
    if (node->getData() == value) return node;
    
    Node<T>* leftResult = find(node->getLeft(), value);
    if (leftResult) return leftResult;
    
    return find(node->getRight(), value);
}

template<typename T>
bool BinaryTree<T>::search(const T& value) const {
    return find(root_, value) != nullptr;
}
```

### Height Calculation

```cpp
template<typename T>
int BinaryTree<T>::getHeight(Node<T>* node) const {
    if (!node) return -1;
    return 1 + max(getHeight(node->getLeft()), getHeight(node->getRight()));
}
```

### Leaf and Internal Node Count

```cpp
template<typename T>
int BinaryTree<T>::getLeafCount(Node<T>* node) const {
    if (!node) return 0;
    if (node->isLeaf()) return 1;
    return getLeafCount(node->getLeft()) + getLeafCount(node->getRight());
}

template<typename T>
int BinaryTree<T>::getInternalCount(Node<T>* node) const {
    if (!node || node->isLeaf()) return 0;
    return 1 + getInternalCount(node->getLeft()) + getInternalCount(node->getRight());
}
```

---

## 🌲 Tree Classifications

### Full Binary Tree Check

```cpp
template<typename T>
bool BinaryTree<T>::isFull(Node<T>* node) const {
    if (!node) return true;
    
    if (node->getLeft() && !node->getRight()) return false;
    if (!node->getLeft() && node->getRight()) return false;
    
    return isFull(node->getLeft()) && isFull(node->getRight());
}
```

### Complete Binary Tree Check

```cpp
template<typename T>
bool BinaryTree<T>::isComplete(Node<T>* node) const {
    if (!node) return true;
    
    queue<Node<T>*> q;
    q.push(node);
    bool hasNull = false;
    
    while (!q.empty()) {
        Node<T>* current = q.front();
        q.pop();
        
        if (!current) {
            hasNull = true;
        } else {
            if (hasNull) return false;
            q.push(current->getLeft());
            q.push(current->getRight());
        }
    }
    return true;
}
```

### Perfect Binary Tree Check

```cpp
template<typename T>
bool BinaryTree<T>::isPerfect(Node<T>* node) const {
    if (!node) return true;
    
    int leftHeight = getHeight(node->getLeft());
    int rightHeight = getHeight(node->getRight());
    
    if (leftHeight != rightHeight) return false;
    
    return isPerfect(node->getLeft()) && isPerfect(node->getRight());
}
```

### Balanced Tree Check

```cpp
template<typename T>
bool BinaryTree<T>::isBalanced(Node<T>* node) const {
    if (!node) return true;
    
    int leftHeight = getHeight(node->getLeft());
    int rightHeight = getHeight(node->getRight());
    
    if (abs(leftHeight - rightHeight) > 1) return false;
    
    return isBalanced(node->getLeft()) && isBalanced(node->getRight());
}
```

---

## 🔄 Traversals

### Preorder Traversal (Root → Left → Right)

```cpp
template<typename T>
void BinaryTree<T>::preorder(Node<T>* node, vector<T>& result) const {
    if (!node) return;
    
    result.push_back(node->getData());
    preorder(node->getLeft(), result);
    preorder(node->getRight(), result);
}

template<typename T>
vector<T> BinaryTree<T>::preorder() const {
    vector<T> result;
    preorder(root_, result);
    return result;
}
```

### Inorder Traversal (Left → Root → Right)

```cpp
template<typename T>
void BinaryTree<T>::inorder(Node<T>* node, vector<T>& result) const {
    if (!node) return;
    
    inorder(node->getLeft(), result);
    result.push_back(node->getData());
    inorder(node->getRight(), result);
}

template<typename T>
vector<T> BinaryTree<T>::inorder() const {
    vector<T> result;
    inorder(root_, result);
    return result;
}
```

### Postorder Traversal (Left → Right → Root)

```cpp
template<typename T>
void BinaryTree<T>::postorder(Node<T>* node, vector<T>& result) const {
    if (!node) return;
    
    postorder(node->getLeft(), result);
    postorder(node->getRight(), result);
    result.push_back(node->getData());
}

template<typename T>
vector<T> BinaryTree<T>::postorder() const {
    vector<T> result;
    postorder(root_, result);
    return result;
}
```

### Level Order Traversal (BFS)

```cpp
template<typename T>
void BinaryTree<T>::levelOrder(Node<T>* node, vector<T>& result) const {
    if (!node) return;
    
    queue<Node<T>*> q;
    q.push(node);
    
    while (!q.empty()) {
        Node<T>* current = q.front();
        q.pop();
        
        result.push_back(current->getData());
        
        if (current->getLeft()) q.push(current->getLeft());
        if (current->getRight()) q.push(current->getRight());
    }
}

template<typename T>
vector<T> BinaryTree<T>::levelOrder() const {
    vector<T> result;
    levelOrder(root_, result);
    return result;
}
```

---

## 🖨️ Display Methods

### Basic Tree Display

```cpp
template<typename T>
void BinaryTree<T>::printTree() const {
    if (!root_) {
        cout << "Tree is empty" << endl;
        return;
    }
    
    queue<Node<T>*> q;
    q.push(root_);
    
    while (!q.empty()) {
        int levelSize = q.size();
        
        for (int i = 0; i < levelSize; i++) {
            Node<T>* current = q.front();
            q.pop();
            
            cout << current->getData() << " ";
            
            if (current->getLeft()) q.push(current->getLeft());
            if (current->getRight()) q.push(current->getRight());
        }
        cout << endl;
    }
}
```

### Pretty Print (Visual Tree)

```cpp
template<typename T>
void printSpaces(int count) {
    for (int i = 0; i < count; i++) {
        cout << " ";
    }
}

template<typename T>
void printPretty(Node<T>* node, int space, int indent = 5) {
    if (!node) return;
    
    space += indent;
    
    printPretty(node->getRight(), space);
    
    cout << endl;
    printSpaces(space - indent);
    cout << node->getData() << endl;
    
    printPretty(node->getLeft(), space);
}

template<typename T>
void BinaryTree<T>::printPretty() const {
    printPretty(root_, 0);
    cout << endl;
}
```

---

## 🧪 Example Usage

```cpp
int main() {
    BinaryTree<int> tree;
    
    // Insert elements
    tree.insert(1);
    tree.insert(2);
    tree.insert(3);
    tree.insert(4);
    tree.insert(5);
    tree.insert(6);
    tree.insert(7);
    
    // Display
    cout << "Tree size: " << tree.size() << endl;
    cout << "Tree height: " << tree.height() << endl;
    cout << "Leaf count: " << tree.leafCount() << endl;
    cout << "Internal count: " << tree.internalCount() << endl;
    
    cout << "\nTree structure:" << endl;
    tree.printPretty();
    
    // Traversals
    cout << "\nPreorder: ";
    for (int x : tree.preorder()) cout << x << " ";
    cout << endl;
    
    cout << "Inorder: ";
    for (int x : tree.inorder()) cout << x << " ";
    cout << endl;
    
    cout << "Postorder: ";
    for (int x : tree.postorder()) cout << x << " ";
    cout << endl;
    
    cout << "Level order: ";
    for (int x : tree.levelOrder()) cout << x << " ";
    cout << endl;
    
    // Search
    cout << "\nSearch 5: " << (tree.search(5) ? "Found" : "Not found") << endl;
    cout << "Search 10: " << (tree.search(10) ? "Found" : "Not found") << endl;
    
    // Remove
    tree.remove(3);
    cout << "\nAfter removing 3:" << endl;
    tree.printPretty();
    
    // Classification
    cout << "\nisFull: " << (tree.isFull() ? "Yes" : "No") << endl;
    cout << "isComplete: " << (tree.isComplete() ? "Yes" : "No") << endl;
    cout << "isPerfect: " << (tree.isPerfect() ? "Yes" : "No") << endl;
    cout << "isBalanced: " << (tree.isBalanced() ? "Yes" : "No") << endl;
    
    return 0;
}
```

---

## 📊 Complexity Summary

| Operation | Time | Space |
|-----------|------|-------|
| Insert | O(n) | O(1) |
| Delete | O(n) | O(1) |
| Search | O(n) | O(1) |
| Preorder | O(n) | O(h) |
| Inorder | O(n) | O(h) |
| Postorder | O(n) | O(h) |
| Level Order | O(n) | O(n) |
| Height | O(n) | O(h) |
| Clear | O(n) | O(h) |

---

## ✅ Key Takeaways

1. **Complete implementation** includes all standard operations
2. **Traversals** are essential for processing tree data
3. **Properties** help classify and analyze trees
4. **Queue-based insertion** maintains level order
5. **Deep copy** ensures independent tree copies
6. **Proper cleanup** prevents memory leaks

---