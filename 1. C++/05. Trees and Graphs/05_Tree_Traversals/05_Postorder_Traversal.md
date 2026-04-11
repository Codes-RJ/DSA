# Tree Traversal - Postorder Traversal

## 📖 Overview

Postorder traversal is a depth-first tree traversal method that visits nodes in the order: **Left → Right → Root**. It is called "postorder" because the root is visited **after** (post) its subtrees. This traversal is particularly useful for deleting trees, evaluating expression trees (postfix notation), and calculating directory sizes.

---

## 🎯 Key Characteristics

| Property | Description |
|----------|-------------|
| **Order** | Left subtree → Right subtree → Root |
| **Postfix Notation** | Used for expression trees |
| **DFS Variant** | Depth-first traversal |
| **Bottom-up Processing** | Children before parent |
| **Safe Deletion** | Delete children before parent |

---

## 📊 Postorder Traversal Visualization

```
        50
       /  \
      30   80
     / \   / \
    20 40 70 90

Postorder: 20 → 40 → 30 → 70 → 90 → 80 → 50

Step-by-step:
1. Traverse left subtree (20, 40, 30)
2. Traverse right subtree (70, 90, 80)
3. Visit root (50)
```

---

## 📝 Recursive Implementation

```cpp
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
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
    
    void postorderRecursiveHelper(Node* node, vector<int>& result) {
        if (node == nullptr) return;
        
        postorderRecursiveHelper(node->left, result);
        postorderRecursiveHelper(node->right, result);
        result.push_back(node->data);
    }
    
public:
    BinaryTree() : root(nullptr) {}
    
    void setRoot(Node* node) { root = node; }
    
    vector<int> postorderRecursive() {
        vector<int> result;
        postorderRecursiveHelper(root, result);
        return result;
    }
    
    void printPostorder() {
        vector<int> result = postorderRecursive();
        cout << "Postorder (Recursive): ";
        for (int val : result) cout << val << " ";
        cout << endl;
    }
};
```

---

## 🔄 Iterative Implementation (Using Two Stacks)

```cpp
class BinaryTree {
private:
    Node* root;
    
public:
    // Method 1: Two stacks
    vector<int> postorderTwoStacks() {
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
    
    // Method 2: Single stack with visited tracking
    vector<int> postorderSingleStack() {
        vector<int> result;
        if (root == nullptr) return result;
        
        stack<pair<Node*, bool>> stk;
        stk.push({root, false});
        
        while (!stk.empty()) {
            auto [node, visited] = stk.top();
            stk.pop();
            
            if (visited) {
                result.push_back(node->data);
            } else {
                stk.push({node, true});
                if (node->right) stk.push({node->right, false});
                if (node->left) stk.push({node->left, false});
            }
        }
        
        return result;
    }
    
    void printPostorderIterative() {
        vector<int> result = postorderTwoStacks();
        cout << "Postorder (Iterative): ";
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
    
    void postorderRecursiveHelper(Node* node, vector<int>& result) {
        if (node == nullptr) return;
        
        postorderRecursiveHelper(node->left, result);
        postorderRecursiveHelper(node->right, result);
        result.push_back(node->data);
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
    
    // Recursive postorder
    vector<int> postorderRecursive() {
        vector<int> result;
        postorderRecursiveHelper(root, result);
        return result;
    }
    
    // Iterative postorder (two stacks)
    vector<int> postorderTwoStacks() {
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
    
    // Iterative postorder (single stack with visited flag)
    vector<int> postorderSingleStack() {
        vector<int> result;
        if (root == nullptr) return result;
        
        stack<pair<Node*, bool>> stk;
        stk.push({root, false});
        
        while (!stk.empty()) {
            auto [node, visited] = stk.top();
            stk.pop();
            
            if (visited) {
                result.push_back(node->data);
            } else {
                stk.push({node, true});
                if (node->right) stk.push({node->right, false});
                if (node->left) stk.push({node->left, false});
            }
        }
        
        return result;
    }
    
    // Delete entire tree (postorder deletion)
    void deleteTree(Node* node) {
        if (node == nullptr) return;
        
        deleteTree(node->left);
        deleteTree(node->right);
        delete node;
    }
    
    void clear() {
        deleteTree(root);
        root = nullptr;
        cout << "Tree deleted successfully!" << endl;
    }
    
    // Calculate height (postorder)
    int getHeight(Node* node) {
        if (node == nullptr) return -1;
        
        int leftHeight = getHeight(node->left);
        int rightHeight = getHeight(node->right);
        
        return 1 + max(leftHeight, rightHeight);
    }
    
    int height() {
        return getHeight(root);
    }
    
    // Evaluate expression tree (postorder)
    int evaluateExpression(Node* node) {
        if (node == nullptr) return 0;
        
        // Leaf node (operand)
        if (node->left == nullptr && node->right == nullptr) {
            return node->data - '0';  // Convert char digit to int
        }
        
        int leftVal = evaluateExpression(node->left);
        int rightVal = evaluateExpression(node->right);
        
        switch (node->data) {
            case '+': return leftVal + rightVal;
            case '-': return leftVal - rightVal;
            case '*': return leftVal * rightVal;
            case '/': return leftVal / rightVal;
            default: return 0;
        }
    }
    
    // Print all traversals
    void printAll() {
        cout << "\n=== Tree Traversals ===" << endl;
        
        vector<int> rec = postorderRecursive();
        cout << "Postorder (Recursive): ";
        for (int v : rec) cout << v << " ";
        cout << endl;
        
        vector<int> twoStack = postorderTwoStacks();
        cout << "Postorder (Two Stacks): ";
        for (int v : twoStack) cout << v << " ";
        cout << endl;
        
        vector<int> singleStack = postorderSingleStack();
        cout << "Postorder (Single Stack): ";
        for (int v : singleStack) cout << v << " ";
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
    cout << "=== Postorder Traversal Demo ===" << endl;
    
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
    
    // Tree height
    cout << "\n=== Tree Properties ===" << endl;
    cout << "Tree height: " << tree.height() << endl;
    
    // Expression tree evaluation
    cout << "\n=== Expression Tree Evaluation ===" << endl;
    // Expression tree for: (3 + 4) * (5 - 2)
    Node* exprRoot = new Node('*');
    exprRoot->left = new Node('+');
    exprRoot->right = new Node('-');
    exprRoot->left->left = new Node('3');
    exprRoot->left->right = new Node('4');
    exprRoot->right->left = new Node('5');
    exprRoot->right->right = new Node('2');
    
    BinaryTree exprTree;
    exprTree.setRoot(exprRoot);
    
    cout << "Expression Tree Postorder (Postfix): ";
    vector<int> exprPost = exprTree.postorderRecursive();
    for (int v : exprPost) cout << (char)v << " ";
    cout << endl;
    cout << "Evaluation result: " << exprTree.evaluateExpression(exprRoot) << endl;
    
    // Tree deletion
    cout << "\n=== Tree Deletion (Postorder) ===" << endl;
    BinaryTree tempTree;
    Node* tempRoot = new Node(10);
    tempRoot->left = new Node(5);
    tempRoot->right = new Node(15);
    tempTree.setRoot(tempRoot);
    
    cout << "Before deletion - Preorder: ";
    for (int v : tempTree.preorderRecursive()) cout << v << " ";
    cout << endl;
    
    tempTree.clear();
    cout << "After deletion - Tree empty" << endl;
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Implementation | Time Complexity | Space Complexity |
|----------------|----------------|------------------|
| **Recursive** | O(n) | O(h) (call stack) |
| **Two Stacks** | O(n) | O(n) (two stacks) |
| **Single Stack** | O(n) | O(n) (stack with flag) |

Where h = height of tree

---

## 🎯 Applications of Postorder Traversal

| Application | Description |
|-------------|-------------|
| **Tree Deletion** | Delete children before parent (safest) |
| **Postfix Evaluation** | Evaluate expression trees |
| **Directory Size** | Calculate total size (sum children first) |
| **Tree Height** | Compute height (postorder calculation) |
| **Bottom-up Processing** | Process children before parent |
| **Freeing Memory** | Release memory bottom-up |

---

## 🔄 Postorder vs Other Traversals

| Traversal | Order | BST Output | Use Case |
|-----------|-------|------------|----------|
| **Preorder** | Root → L → R | Not sorted | Tree copying, serialization |
| **Inorder** | L → Root → R | Sorted | BST operations |
| **Postorder** | L → R → Root | Not sorted | Tree deletion, expression evaluation |

---

## ✅ Key Takeaways

1. **Postorder traversal** visits Left → Right → Root
2. **Root is visited last** after both subtrees
3. **Essential for tree deletion** (delete children first)
4. **Expression trees** produce postfix notation
5. **Two-stack iterative** approach is straightforward
6. **Single-stack** approach uses visited flag
7. **Time complexity** O(n) for all implementations
8. **Bottom-up processing** is natural with postorder

---