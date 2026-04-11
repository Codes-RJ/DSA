# Tree Traversal - Preorder Traversal

## 📖 Overview

Preorder traversal is a depth-first tree traversal method that visits nodes in the order: **Root → Left → Right**. It is called "preorder" because the root is visited **before** (pre) its subtrees. This traversal is particularly useful for creating a copy of a tree, serializing a tree structure, and generating prefix expressions from expression trees.

---

## 🎯 Key Characteristics

| Property | Description |
|----------|-------------|
| **Order** | Root → Left subtree → Right subtree |
| **Prefix Notation** | Used for expression trees |
| **DFS Variant** | Depth-first traversal |
| **Tree Copying** | Can recreate tree structure |
| **Serialization** | Easy to serialize/deserialize |

---

## 📊 Preorder Traversal Visualization

```
        50
       /  \
      30   80
     / \   / \
    20 40 70 90

Preorder: 50 → 30 → 20 → 40 → 80 → 70 → 90

Step-by-step:
1. Visit root (50)
2. Traverse left subtree (30, 20, 40)
3. Traverse right subtree (80, 70, 90)
```

---

## 📝 Recursive Implementation

```cpp
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;
    
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

class BinaryTree {
private:
    Node* root;
    
    void preorderRecursiveHelper(Node* node, vector<int>& result) {
        if (node == nullptr) return;
        
        result.push_back(node->data);
        preorderRecursiveHelper(node->left, result);
        preorderRecursiveHelper(node->right, result);
    }
    
public:
    BinaryTree() : root(nullptr) {}
    
    void setRoot(Node* node) { root = node; }
    
    vector<int> preorderRecursive() {
        vector<int> result;
        preorderRecursiveHelper(root, result);
        return result;
    }
    
    void printPreorder() {
        vector<int> result = preorderRecursive();
        cout << "Preorder (Recursive): ";
        for (int val : result) cout << val << " ";
        cout << endl;
    }
};
```

---

## 🔄 Iterative Implementation (Using Stack)

```cpp
class BinaryTree {
private:
    Node* root;
    
public:
    vector<int> preorderIterative() {
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
    
    void printPreorderIterative() {
        vector<int> result = preorderIterative();
        cout << "Preorder (Iterative): ";
        for (int val : result) cout << val << " ";
        cout << endl;
    }
};
```

---

## 💻 Complete Implementation

```cpp
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
using namespace std;

class Node {
public:
    int data;
    Node* left;
    Node* right;
    
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

class BinaryTree {
private:
    Node* root;
    
    void preorderRecursiveHelper(Node* node, vector<int>& result) {
        if (node == nullptr) return;
        
        result.push_back(node->data);
        preorderRecursiveHelper(node->left, result);
        preorderRecursiveHelper(node->right, result);
    }
    
    Node* createTreeFromArray(const vector<int>& arr, int index) {
        if (index >= arr.size() || arr[index] == -1) return nullptr;
        
        Node* node = new Node(arr[index]);
        node->left = createTreeFromArray(arr, 2 * index + 1);
        node->right = createTreeFromArray(arr, 2 * index + 2);
        
        return node;
    }
    
public:
    BinaryTree() : root(nullptr) {}
    
    void setRoot(Node* node) { root = node; }
    
    void buildFromLevelOrder(const vector<int>& arr) {
        root = createTreeFromArray(arr, 0);
    }
    
    // Recursive preorder
    vector<int> preorderRecursive() {
        vector<int> result;
        preorderRecursiveHelper(root, result);
        return result;
    }
    
    // Iterative preorder using stack
    vector<int> preorderIterative() {
        vector<int> result;
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
    
    // Serialize tree to string (preorder)
    string serialize() {
        vector<int> pre = preorderRecursive();
        string result;
        for (int val : pre) {
            result += to_string(val) + " ";
        }
        return result;
    }
    
    // Create a copy of the tree
    Node* copyTree(Node* node) {
        if (node == nullptr) return nullptr;
        
        Node* newNode = new Node(node->data);
        newNode->left = copyTree(node->left);
        newNode->right = copyTree(node->right);
        
        return newNode;
    }
    
    BinaryTree copy() {
        BinaryTree newTree;
        newTree.setRoot(copyTree(root));
        return newTree;
    }
    
    // Print all traversals
    void printAll() {
        cout << "\n=== Tree Traversals ===" << endl;
        
        vector<int> rec = preorderRecursive();
        cout << "Preorder (Recursive): ";
        for (int v : rec) cout << v << " ";
        cout << endl;
        
        vector<int> iter = preorderIterative();
        cout << "Preorder (Iterative): ";
        for (int v : iter) cout << v << " ";
        cout << endl;
    }
    
    // Display tree structure
    void displayTree() {
        if (!root) {
            cout << "Tree is empty" << endl;
            return;
        }
        
        queue<Node*> q;
        q.push(root);
        int level = 0;
        
        cout << "\nTree Structure (Level Order):" << endl;
        while (!q.empty()) {
            int levelSize = q.size();
            cout << "Level " << level << ": ";
            
            for (int i = 0; i < levelSize; i++) {
                Node* current = q.front();
                q.pop();
                
                if (current) {
                    cout << current->data << " ";
                    q.push(current->left);
                    q.push(current->right);
                } else {
                    cout << "- ";
                }
            }
            cout << endl;
            level++;
        }
    }
};

int main() {
    cout << "=== Preorder Traversal Demo ===" << endl;
    
    // Create tree: 
    //        50
    //       /  \
    //      30   80
    //     / \   / \
    //    20 40 70 90
    
    Node* root = new Node(50);
    root->left = new Node(30);
    root->right = new Node(80);
    root->left->left = new Node(20);
    root->left->right = new Node(40);
    root->right->left = new Node(70);
    root->right->right = new Node(90);
    
    BinaryTree tree;
    tree.setRoot(root);
    
    tree.displayTree();
    tree.printAll();
    
    // Serialization
    cout << "\n=== Serialization ===" << endl;
    cout << "Serialized tree (preorder): " << tree.serialize() << endl;
    
    // Tree copying
    cout << "\n=== Tree Copying ===" << endl;
    BinaryTree copiedTree = tree.copy();
    cout << "Original tree preorder: ";
    for (int v : tree.preorderRecursive()) cout << v << " ";
    cout << endl;
    cout << "Copied tree preorder:   ";
    for (int v : copiedTree.preorderRecursive()) cout << v << " ";
    cout << endl;
    
    // Expression tree example
    cout << "\n=== Expression Tree ===" << endl;
    // Expression tree for: (a + b) * (c - d)
    Node* exprRoot = new Node('*');
    exprRoot->left = new Node('+');
    exprRoot->right = new Node('-');
    exprRoot->left->left = new Node('a');
    exprRoot->left->right = new Node('b');
    exprRoot->right->left = new Node('c');
    exprRoot->right->right = new Node('d');
    
    BinaryTree exprTree;
    exprTree.setRoot(exprRoot);
    
    cout << "Expression Tree Preorder (Prefix): ";
    vector<int> exprPre = exprTree.preorderRecursive();
    for (int v : exprPre) cout << (char)v << " ";
    cout << endl;
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Implementation | Time Complexity | Space Complexity |
|----------------|----------------|------------------|
| **Recursive** | O(n) | O(h) (call stack) |
| **Iterative** | O(n) | O(h) (explicit stack) |

Where h = height of tree

---

## 🎯 Applications of Preorder Traversal

| Application | Description |
|-------------|-------------|
| **Tree Copying** | Create exact copy of tree structure |
| **Serialization** | Save tree structure to file/string |
| **Prefix Expressions** | Generate prefix notation from expression tree |
| **Tree Equality** | Compare two trees for structural equality |
| **Tree Reconstruction** | Build tree from preorder sequence |
| **Directory Listing** | Display directory structure (root first) |

---

## 🔄 Preorder vs Other Traversals

| Traversal | Order | BST Output | Use Case |
|-----------|-------|------------|----------|
| **Preorder** | Root → L → R | Not sorted | Tree copying, serialization |
| **Inorder** | L → Root → R | Sorted | BST operations |
| **Postorder** | L → R → Root | Not sorted | Tree deletion |

---

## ✅ Key Takeaways

1. **Preorder traversal** visits Root → Left → Right
2. **Root is visited first** before its children
3. **Useful for tree copying** and serialization
4. **Recursive** implementation is straightforward
5. **Iterative** uses explicit stack (push right first)
6. **Expression trees** produce prefix notation
7. **Time complexity** O(n) for all implementations

---