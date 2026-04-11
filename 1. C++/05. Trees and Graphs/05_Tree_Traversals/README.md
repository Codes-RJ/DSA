# Tree Traversals - Complete Guide

## 📖 Overview

Tree traversal refers to the process of visiting each node in a tree exactly once. Different traversal orders produce different sequences with distinct properties. In Binary Search Trees (BSTs), inorder traversal produces nodes in sorted order. This guide covers all major traversal methods with complete implementations and use cases.

---

## 🎯 Types of Traversals

| Traversal | Order | Use Case |
|-----------|-------|----------|
| **Inorder** | Left → Root → Right | Sorted output from BST |
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
void inorderRecursive(Node* node, vector<int>& result) {
    if (node == nullptr) return;
    
    inorderRecursive(node->left, result);
    result.push_back(node->data);
    inorderRecursive(node->right, result);
}
```

### Iterative Implementation (Using Stack)

```cpp
vector<int> inorderIterative(Node* root) {
    vector<int> result;
    stack<Node*> stk;
    Node* current = root;
    
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

---

## 🌳 Preorder Traversal (Root → Left → Right)

### Characteristics
- Creates a copy of the tree when combined with insertion order
- Useful for serialization (saving tree structure)
- Visits root, then left subtree, then right subtree

### Recursive Implementation

```cpp
void preorderRecursive(Node* node, vector<int>& result) {
    if (node == nullptr) return;
    
    result.push_back(node->data);
    preorderRecursive(node->left, result);
    preorderRecursive(node->right, result);
}
```

### Iterative Implementation (Using Stack)

```cpp
vector<int> preorderIterative(Node* root) {
    vector<int> result;
    if (root == nullptr) return result;
    
    stack<Node*> stk;
    stk.push(root);
    
    while (!stk.empty()) {
        Node* current = stk.top();
        stk.pop();
        
        result.push_back(current->data);
        
        // Push right first so left is processed first (stack LIFO)
        if (current->right) stk.push(current->right);
        if (current->left) stk.push(current->left);
    }
    
    return result;
}
```

---

## 🌴 Postorder Traversal (Left → Right → Root)

### Characteristics
- Used for deleting trees (delete children before parent)
- Used in expression evaluation (postfix notation)
- Visits left subtree, then right subtree, then root

### Recursive Implementation

```cpp
void postorderRecursive(Node* node, vector<int>& result) {
    if (node == nullptr) return;
    
    postorderRecursive(node->left, result);
    postorderRecursive(node->right, result);
    result.push_back(node->data);
}
```

### Iterative Implementation (Using Two Stacks)

```cpp
vector<int> postorderIterative(Node* root) {
    vector<int> result;
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
```

---

## 📊 Level Order Traversal (BFS)

### Characteristics
- Visits nodes level by level from top to bottom
- Uses a queue instead of recursion
- Finds shortest path in unweighted trees

### Implementation (Using Queue)

```cpp
vector<int> levelOrder(Node* root) {
    vector<int> result;
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
```

### Level Order with Level Separation

```cpp
vector<vector<int>> levelOrderWithLevels(Node* root) {
    vector<vector<int>> result;
    if (root == nullptr) return result;
    
    queue<Node*> q;
    q.push(root);
    
    while (!q.empty()) {
        int levelSize = q.size();
        vector<int> currentLevel;
        
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
class Node {
public:
    T data;
    Node* left;
    Node* right;
    
    Node(const T& value) : data(value), left(nullptr), right(nullptr) {}
};

template<typename T>
class BinaryTree {
private:
    Node<T>* root;
    
    // Recursive traversals
    void inorderRecursive(Node<T>* node, vector<T>& result) {
        if (node == nullptr) return;
        inorderRecursive(node->left, result);
        result.push_back(node->data);
        inorderRecursive(node->right, result);
    }
    
    void preorderRecursive(Node<T>* node, vector<T>& result) {
        if (node == nullptr) return;
        result.push_back(node->data);
        preorderRecursive(node->left, result);
        preorderRecursive(node->right, result);
    }
    
    void postorderRecursive(Node<T>* node, vector<T>& result) {
        if (node == nullptr) return;
        postorderRecursive(node->left, result);
        postorderRecursive(node->right, result);
        result.push_back(node->data);
    }
    
public:
    BinaryTree() : root(nullptr) {}
    
    void setRoot(Node<T>* node) { root = node; }
    
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
        stack<Node<T>*> stk;
        Node<T>* current = root;
        
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
        
        stack<Node<T>*> stk;
        stk.push(root);
        
        while (!stk.empty()) {
            Node<T>* current = stk.top();
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
    
    vector<T> levelOrder() {
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
    
    vector<vector<T>> levelOrderWithLevels() {
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
    
    void print(const string& title, const vector<T>& result) {
        cout << title << ": ";
        for (const T& val : result) {
            cout << val << " ";
        }
        cout << endl;
    }
    
    void printAll() {
        cout << "\n=== Tree Traversals ===" << endl;
        print("Inorder (recursive)", inorderRecursive());
        print("Preorder (recursive)", preorderRecursive());
        print("Postorder (recursive)", postorderRecursive());
        print("Inorder (iterative)", inorderIterative());
        print("Preorder (iterative)", preorderIterative());
        print("Postorder (iterative)", postorderIterative());
        print("Level Order", levelOrder());
        
        cout << "\nLevel Order with Levels:" << endl;
        vector<vector<int>> levels = levelOrderWithLevels();
        for (size_t i = 0; i < levels.size(); i++) {
            cout << "Level " << i << ": ";
            for (int val : levels[i]) {
                cout << val << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    // Create tree: 
    //        50
    //       /  \
    //      30   80
    //     / \   / \
    //    20 40 70 90
    
    Node<int>* root = new Node<int>(50);
    root->left = new Node<int>(30);
    root->right = new Node<int>(80);
    root->left->left = new Node<int>(20);
    root->left->right = new Node<int>(40);
    root->right->left = new Node<int>(70);
    root->right->right = new Node<int>(90);
    
    BinaryTree<int> tree;
    tree.setRoot(root);
    
    cout << "=== Binary Tree Traversals Demo ===" << endl;
    cout << "Tree structure:" << endl;
    cout << "        50" << endl;
    cout << "       /  \\" << endl;
    cout << "      30   80" << endl;
    cout << "     / \\   / \\" << endl;
    cout << "    20 40 70 90" << endl;
    
    tree.printAll();
    
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

---