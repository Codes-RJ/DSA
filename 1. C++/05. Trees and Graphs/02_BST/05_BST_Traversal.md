# BST Traversal

## 📖 Overview

Tree traversal refers to the process of visiting each node in a tree exactly once. In Binary Search Trees (BSTs), different traversal orders produce different sequences with distinct properties. The most important traversal for BSTs is **inorder traversal**, which produces nodes in sorted order. This guide covers all traversal methods with complete implementations and use cases.

---

## 🎯 Types of Traversals

| Traversal | Order | Use Case |
|-----------|-------|----------|
| **Inorder** | Left → Root → Right | Sorted output |
| **Preorder** | Root → Left → Right | Tree copying, serialization |
| **Postorder** | Left → Right → Root | Tree deletion, expression evaluation |
| **Level Order** | Level by level (BFS) | Shortest path, breadth-first search |

---

## 📊 Traversal Comparison

```
        50
       /  \
      30   80
     / \   / \
    20 40 70 90

Inorder:    20, 30, 40, 50, 70, 80, 90
Preorder:   50, 30, 20, 40, 80, 70, 90
Postorder:  20, 40, 30, 70, 90, 80, 50
Level Order:50, 30, 80, 20, 40, 70, 90
```

---

## 🌲 Inorder Traversal (Left → Root → Right)

### Characteristics
- Produces nodes in **sorted order** for BST
- Most commonly used traversal for BSTs
- Visits left subtree, then root, then right subtree

### Recursive Implementation

```cpp
template<typename T>
void inorderRecursive(Node<T>* node, vector<T>& result) {
    if (node == nullptr) return;
    
    inorderRecursive(node->left, result);
    result.push_back(node->data);
    inorderRecursive(node->right, result);
}

template<typename T>
vector<T> inorder() const {
    vector<T> result;
    inorderRecursive(root, result);
    return result;
}
```

### Iterative Implementation (Using Stack)

```cpp
template<typename T>
vector<T> inorderIterative() const {
    vector<T> result;
    stack<Node<T>*> stk;
    Node<T>* current = root;
    
    while (current != nullptr || !stk.empty()) {
        // Go to leftmost node
        while (current != nullptr) {
            stk.push(current);
            current = current->left;
        }
        
        // Process node
        current = stk.top();
        stk.pop();
        result.push_back(current->data);
        
        // Go to right subtree
        current = current->right;
    }
    
    return result;
}
```

### Step-by-Step Execution

```
Tree:
        50
       /  \
      30   80
     / \   / \
    20 40 70 90

Inorder Traversal Steps:
1. Go left from 50 → 30 → 20
2. Process 20 → push to result
3. Back to 30 → process 30
4. Go right from 30 → 40 → process 40
5. Back to 50 → process 50
6. Go right from 50 → 80 → 70 → process 70
7. Back to 80 → process 80
8. Go right from 80 → 90 → process 90

Result: 20, 30, 40, 50, 70, 80, 90
```

---

## 🌳 Preorder Traversal (Root → Left → Right)

### Characteristics
- Creates a copy of the tree when combined with insertion order
- Useful for serialization (saving tree structure)
- Visits root, then left subtree, then right subtree

### Recursive Implementation

```cpp
template<typename T>
void preorderRecursive(Node<T>* node, vector<T>& result) {
    if (node == nullptr) return;
    
    result.push_back(node->data);
    preorderRecursive(node->left, result);
    preorderRecursive(node->right, result);
}

template<typename T>
vector<T> preorder() const {
    vector<T> result;
    preorderRecursive(root, result);
    return result;
}
```

### Iterative Implementation (Using Stack)

```cpp
template<typename T>
vector<T> preorderIterative() const {
    vector<T> result;
    if (root == nullptr) return result;
    
    stack<Node<T>*> stk;
    stk.push(root);
    
    while (!stk.empty()) {
        Node<T>* current = stk.top();
        stk.pop();
        
        result.push_back(current->data);
        
        // Push right first so left is processed first (stack LIFO)
        if (current->right) stk.push(current->right);
        if (current->left) stk.push(current->left);
    }
    
    return result;
}
```

### Step-by-Step Execution

```
Tree:
        50
       /  \
      30   80
     / \   / \
    20 40 70 90

Preorder Traversal Steps:
1. Process 50
2. Go left to 30 → process 30
3. Go left to 20 → process 20
4. Back to 30 → go right to 40 → process 40
5. Back to 50 → go right to 80 → process 80
6. Go left to 70 → process 70
7. Back to 80 → go right to 90 → process 90

Result: 50, 30, 20, 40, 80, 70, 90
```

---

## 🌴 Postorder Traversal (Left → Right → Root)

### Characteristics
- Used for deleting trees (delete children before parent)
- Used in expression evaluation (postfix notation)
- Visits left subtree, then right subtree, then root

### Recursive Implementation

```cpp
template<typename T>
void postorderRecursive(Node<T>* node, vector<T>& result) {
    if (node == nullptr) return;
    
    postorderRecursive(node->left, result);
    postorderRecursive(node->right, result);
    result.push_back(node->data);
}

template<typename T>
vector<T> postorder() const {
    vector<T> result;
    postorderRecursive(root, result);
    return result;
}
```

### Iterative Implementation (Using Two Stacks)

```cpp
template<typename T>
vector<T> postorderIterative() const {
    vector<T> result;
    if (root == nullptr) return result;
    
    stack<Node<T>*> stk1, stk2;
    stk1.push(root);
    
    while (!stk1.empty()) {
        Node<T>* current = stk1.top();
        stk1.pop();
        stk2.push(current);
        
        if (current->left) stk1.push(current->left);
        if (current->right) stk1.push(current->right);
    }
    
    while (!stk2.empty()) {
        result.push_back(stk2.top()->data);
        stk2.pop();
    }
    
    return result;
}
```

### Step-by-Step Execution

```
Tree:
        50
       /  \
      30   80
     / \   / \
    20 40 70 90

Postorder Traversal Steps:
1. Go left from 50 → 30 → 20 (leaf) → process 20
2. Back to 30 → go right to 40 → process 40
3. Process 30
4. Back to 50 → go right to 80 → 70 → process 70
5. Back to 80 → go right to 90 → process 90
6. Process 80
7. Process 50

Result: 20, 40, 30, 70, 90, 80, 50
```

---

## 📊 Level Order Traversal (BFS)

### Characteristics
- Visits nodes level by level from top to bottom
- Uses a queue instead of recursion
- Finds shortest path in unweighted trees

### Implementation (Using Queue)

```cpp
template<typename T>
vector<T> levelOrder() const {
    vector<T> result;
    if (root == nullptr) return result;
    
    queue<Node<T>*> q;
    q.push(root);
    
    while (!q.empty()) {
        Node<T>* current = q.front();
        q.pop();
        
        result.push_back(current->data);
        
        if (current->left) q.push(current->left);
        if (current->right) q.push(current->right);
    }
    
    return result;
}
```

### Level Order with Level Separation

```cpp
template<typename T>
vector<vector<T>> levelOrderWithLevels() const {
    vector<vector<T>> result;
    if (root == nullptr) return result;
    
    queue<Node<T>*> q;
    q.push(root);
    
    while (!q.empty()) {
        int levelSize = q.size();
        vector<T> currentLevel;
        
        for (int i = 0; i < levelSize; i++) {
            Node<T>* current = q.front();
            q.pop();
            
            currentLevel.push_back(current->data);
            
            if (current->left) q.push(current->left);
            if (current->right) q.push(current->right);
        }
        
        result.push_back(currentLevel);
    }
    
    return result;
}
```

### Visual Execution

```
Tree:
        50
       /  \
      30   80
     / \   / \
    20 40 70 90

Level Order Traversal:
Level 0: 50
Level 1: 30, 80
Level 2: 20, 40, 70, 90

Result: 50, 30, 80, 20, 40, 70, 90
```

---

## 💻 Complete Implementation

```cpp
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
using namespace std;

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
    
    // Recursive traversals
    void inorderRecursive(Node* node, vector<T>& result) {
        if (node == nullptr) return;
        inorderRecursive(node->left, result);
        result.push_back(node->data);
        inorderRecursive(node->right, result);
    }
    
    void preorderRecursive(Node* node, vector<T>& result) {
        if (node == nullptr) return;
        result.push_back(node->data);
        preorderRecursive(node->left, result);
        preorderRecursive(node->right, result);
    }
    
    void postorderRecursive(Node* node, vector<T>& result) {
        if (node == nullptr) return;
        postorderRecursive(node->left, result);
        postorderRecursive(node->right, result);
        result.push_back(node->data);
    }
    
public:
    BST() : root(nullptr) {}
    
    // Insert method (assume implemented)
    void insert(const T& value) {
        // Insert implementation from previous section
    }
    
    // Recursive traversals
    vector<T> inorderRecursive() {
        vector<T> result;
        inorderRecursive(root, result);
        return result;
    }
    
    vector<T> preorderRecursive() {
        vector<T> result;
        preorderRecursive(root, result);
        return result;
    }
    
    vector<T> postorderRecursive() {
        vector<T> result;
        postorderRecursive(root, result);
        return result;
    }
    
    // Iterative traversals
    vector<T> inorderIterative() {
        vector<T> result;
        stack<Node*> stk;
        Node* current = root;
        
        while (current != nullptr || !stk.empty()) {
            while (current != nullptr) {
                stk.push(current);
                current = current->left;
            }
            
            current = stk.top();
            stk.pop();
            result.push_back(current->data);
            current = current->right;
        }
        
        return result;
    }
    
    vector<T> preorderIterative() {
        vector<T> result;
        if (root == nullptr) return result;
        
        stack<Node*> stk;
        stk.push(root);
        
        while (!stk.empty()) {
            Node* current = stk.top();
            stk.pop();
            
            result.push_back(current->data);
            
            if (current->right) stk.push(current->right);
            if (current->left) stk.push(current->left);
        }
        
        return result;
    }
    
    vector<T> postorderIterative() {
        vector<T> result;
        if (root == nullptr) return result;
        
        stack<Node*> stk1, stk2;
        stk1.push(root);
        
        while (!stk1.empty()) {
            Node* current = stk1.top();
            stk1.pop();
            stk2.push(current);
            
            if (current->left) stk1.push(current->left);
            if (current->right) stk1.push(current->right);
        }
        
        while (!stk2.empty()) {
            result.push_back(stk2.top()->data);
            stk2.pop();
        }
        
        return result;
    }
    
    vector<T> levelOrder() {
        vector<T> result;
        if (root == nullptr) return result;
        
        queue<Node*> q;
        q.push(root);
        
        while (!q.empty()) {
            Node* current = q.front();
            q.pop();
            
            result.push_back(current->data);
            
            if (current->left) q.push(current->left);
            if (current->right) q.push(current->right);
        }
        
        return result;
    }
    
    vector<vector<T>> levelOrderWithLevels() {
        vector<vector<T>> result;
        if (root == nullptr) return result;
        
        queue<Node*> q;
        q.push(root);
        
        while (!q.empty()) {
            int levelSize = q.size();
            vector<T> currentLevel;
            
            for (int i = 0; i < levelSize; i++) {
                Node* current = q.front();
                q.pop();
                
                currentLevel.push_back(current->data);
                
                if (current->left) q.push(current->left);
                if (current->right) q.push(current->right);
            }
            
            result.push_back(currentLevel);
        }
        
        return result;
    }
    
    // Print methods
    void printInorder() {
        vector<T> result = inorderIterative();
        for (const T& val : result) cout << val << " ";
        cout << endl;
    }
    
    void printPreorder() {
        vector<T> result = preorderIterative();
        for (const T& val : result) cout << val << " ";
        cout << endl;
    }
    
    void printPostorder() {
        vector<T> result = postorderIterative();
        for (const T& val : result) cout << val << " ";
        cout << endl;
    }
    
    void printLevelOrder() {
        vector<T> result = levelOrder();
        for (const T& val : result) cout << val << " ";
        cout << endl;
    }
    
    void printLevels() {
        vector<vector<T>> levels = levelOrderWithLevels();
        for (size_t i = 0; i < levels.size(); i++) {
            cout << "Level " << i << ": ";
            for (const T& val : levels[i]) {
                cout << val << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    BST<int> bst;
    
    // Insert nodes
    int values[] = {50, 30, 80, 20, 40, 70, 90};
    for (int v : values) {
        bst.insert(v);
    }
    
    cout << "=== BST Traversals ===" << endl;
    cout << "Tree structure:"        << endl;
    cout << "        50"             << endl;
    cout << "       /  \\"           << endl;
    cout << "      30   80"          << endl;
    cout << "     / \\   / \\"       << endl;
    cout << "    20 40 70 90"        << endl;
    
    cout << "\n1. Inorder (sorted): ";
    bst.printInorder();
    
    cout << "2. Preorder: ";
    bst.printPreorder();
    
    cout << "3. Postorder: ";
    bst.printPostorder();
    
    cout << "4. Level Order: ";
    bst.printLevelOrder();
    
    cout << "\n5. Level Order with levels:" << endl;
    bst.printLevels();
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Traversal | Time Complexity | Space Complexity | Space (Recursive) |
|-----------|----------------|------------------|-------------------|
| **Inorder** | O(n) | O(1) iterative | O(h) |
| **Preorder** | O(n) | O(1) iterative | O(h) |
| **Postorder** | O(n) | O(n) iterative (2 stacks) | O(h) |
| **Level Order** | O(n) | O(w) where w = max width | N/A |

---

## 🎯 Use Cases Summary

| Traversal | Best Use Case |
|-----------|---------------|
| **Inorder** | Getting sorted data from BST |
| **Preorder** | Serializing/deserializing tree, creating copy |
| **Postorder** | Deleting tree, evaluating expressions |
| **Level Order** | Finding shortest path, printing tree levels |

---

## ✅ Key Takeaways

1. **Inorder** produces sorted order for BST
2. **Preorder** is useful for tree serialization
3. **Postorder** is used for tree deletion
4. **Level order** uses BFS and a queue
5. **Iterative traversals** avoid recursion stack overflow
6. **Recursive traversals** are more readable but use O(h) space
7. **BST property** only guarantees inorder sorting
8. **Morris traversal** achieves O(1) space for inorder

---
---

## Next Step

- Go to [README.md](README.md) to continue.
