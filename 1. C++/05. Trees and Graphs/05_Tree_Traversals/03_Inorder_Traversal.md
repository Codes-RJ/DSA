# Tree Traversal - Inorder Traversal

## 📖 Overview

Inorder traversal is a depth-first tree traversal method that visits nodes in the order: **Left → Root → Right**. For Binary Search Trees (BSTs), inorder traversal produces nodes in **sorted ascending order**, making it one of the most important traversal methods for BST operations.

---

## 🎯 Key Characteristics

| Property | Description |
|----------|-------------|
| **Order** | Left subtree → Root → Right subtree |
| **BST Property** | Produces sorted output |
| **DFS Variant** | Depth-first traversal |
| **Recursive Pattern** | Natural recursive implementation |
| **Stack-based** | Can be implemented iteratively |

---

## 📊 Inorder Traversal Visualization

```
        50
       /  \
      30   80
     / \   / \
    20 40 70 90

Inorder: 20 → 30 → 40 → 50 → 70 → 80 → 90

Step-by-step:
1. Go left from 50 → 30 → 20
2. Visit 20 (leaf)
3. Back to 30, visit 30
4. Go right from 30 → 40, visit 40
5. Back to 50, visit 50
6. Go right from 50 → 80 → 70
7. Visit 70 (leaf)
8. Back to 80, visit 80
9. Go right from 80 → 90, visit 90
```

---

## 📝 Recursive Implementation

```cpp
#include <iostream>
#include <vector>
#include <stack>
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
    
    void inorderRecursive(Node* node, vector<int>& result) {
        if (node == nullptr) return;
        
        inorderRecursive(node->left, result);
        result.push_back(node->data);
        inorderRecursive(node->right, result);
    }
    
public:
    BinaryTree() : root(nullptr) {}
    
    void setRoot(Node* node) { root = node; }
    
    vector<int> inorderRecursive() {
        vector<int> result;
        inorderRecursive(root, result);
        return result;
    }
    
    void printInorder() {
        vector<int> result = inorderRecursive();
        cout << "Inorder (Recursive): ";
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
    vector<int> inorderIterative() {
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
    
    void printInorderIterative() {
        vector<int> result = inorderIterative();
        cout << "Inorder (Iterative): ";
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
    
    // Helper for recursive inorder
    void inorderRecursiveHelper(Node* node, vector<int>& result) {
        if (node == nullptr) return;
        
        inorderRecursiveHelper(node->left, result);
        result.push_back(node->data);
        inorderRecursiveHelper(node->right, result);
    }
    
    // Helper to create tree from array (level order)
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
    
    // Build tree from level order array
    void buildFromLevelOrder(const vector<int>& arr) {
        root = createTreeFromArray(arr, 0);
    }
    
    // Recursive inorder
    vector<int> inorderRecursive() {
        vector<int> result;
        inorderRecursiveHelper(root, result);
        return result;
    }
    
    // Iterative inorder using stack
    vector<int> inorderIterative() {
        vector<int> result;
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
    
    // Morris Traversal (O(1) space)
    vector<int> inorderMorris() {
        vector<int> result;
        Node* current = root;
        
        while (current != nullptr) {
            if (current->left == nullptr) {
                result.push_back(current->data);
                current = current->right;
            } else {
                // Find predecessor
                Node* predecessor = current->left;
                while (predecessor->right != nullptr && predecessor->right != current) {
                    predecessor = predecessor->right;
                }
                
                if (predecessor->right == nullptr) {
                    predecessor->right = current;
                    current = current->left;
                } else {
                    predecessor->right = nullptr;
                    result.push_back(current->data);
                    current = current->right;
                }
            }
        }
        
        return result;
    }
    
    // Check if tree is BST using inorder
    bool isBST() {
        vector<int> inorder = inorderIterative();
        for (size_t i = 1; i < inorder.size(); i++) {
            if (inorder[i] <= inorder[i - 1]) return false;
        }
        return true;
    }
    
    // Find kth smallest element
    int kthSmallest(int k) {
        vector<int> inorder = inorderIterative();
        if (k > 0 && k <= inorder.size()) {
            return inorder[k - 1];
        }
        return -1;
    }
    
    // Print all traversals
    void printAll() {
        cout << "\n=== Tree Traversals ===" << endl;
        
        vector<int> rec = inorderRecursive();
        cout << "Inorder (Recursive): ";
        for (int v : rec) cout << v << " ";
        cout << endl;
        
        vector<int> iter = inorderIterative();
        cout << "Inorder (Iterative): ";
        for (int v : iter) cout << v << " ";
        cout << endl;
        
        vector<int> morris = inorderMorris();
        cout << "Inorder (Morris):   ";
        for (int v : morris) cout << v << " ";
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
    cout << "=== Inorder Traversal Demo ===" << endl;
    
    // Create BST: 
    //        50
    //       /  \
    //      30   80
    //     / \   / \
    //    20 40 70 90
    
    BinaryTree tree;
    Node* root = new Node(50);
    root->left = new Node(30);
    root->right = new Node(80);
    root->left->left = new Node(20);
    root->left->right = new Node(40);
    root->right->left = new Node(70);
    root->right->right = new Node(90);
    
    tree.setRoot(root);
    
    tree.displayTree();
    tree.printAll();
    
    // BST property check
    cout << "\n=== BST Property ===" << endl;
    cout << "Is BST? " << (tree.isBST() ? "Yes" : "No") << endl;
    
    // Kth smallest
    cout << "\n=== Kth Smallest ===" << endl;
    for (int k = 1; k <= 7; k++) {
        cout << k << "th smallest: " << tree.kthSmallest(k) << endl;
    }
    
    // Create non-BST tree
    cout << "\n=== Non-BST Tree ===" << endl;
    BinaryTree nonBST;
    Node* root2 = new Node(50);
    root2->left = new Node(60);  // 60 > 50 in left subtree - violates BST
    root2->right = new Node(40); // 40 < 50 in right subtree - violates BST
    root2->left->left = new Node(30);
    root2->left->right = new Node(70);
    
    nonBST.setRoot(root2);
    nonBST.displayTree();
    nonBST.printAll();
    cout << "Is BST? " << (nonBST.isBST() ? "Yes" : "No") << endl;
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Implementation | Time Complexity | Space Complexity |
|----------------|----------------|------------------|
| **Recursive** | O(n) | O(h) (call stack) |
| **Iterative** | O(n) | O(h) (explicit stack) |
| **Morris** | O(n) | O(1) |

Where h = height of tree

---

## 🎯 Applications of Inorder Traversal

| Application | Description |
|-------------|-------------|
| **BST Sorting** | Get sorted elements from BST |
| **BST Validation** | Check if tree follows BST property |
| **Kth Smallest/Largest** | Find element by rank |
| **Tree to Sorted List** | Convert BST to sorted array |
| **Range Queries** | Find elements in value range |
| **Expression Trees** | Infix notation generation |

---

## 🔄 Inorder vs Other Traversals

| Traversal | Order | BST Output | Use Case |
|-----------|-------|------------|----------|
| **Inorder** | L → R → Root | Sorted | BST operations |
| **Preorder** | Root → L → R | Not sorted | Tree copying |
| **Postorder** | L → R → Root | Not sorted | Tree deletion |

---

## ✅ Key Takeaways

1. **Inorder traversal** visits Left → Root → Right
2. **BST inorder** produces sorted ascending order
3. **Recursive** implementation is simplest
4. **Iterative** uses explicit stack
5. **Morris traversal** achieves O(1) space
6. **Used for** BST validation and kth smallest
7. **Time complexity** O(n) for all implementations

---