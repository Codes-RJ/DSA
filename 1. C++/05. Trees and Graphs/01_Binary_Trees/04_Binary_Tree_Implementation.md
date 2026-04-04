# Binary Tree Implementation

## Introduction
This section provides a complete implementation of binary trees in C++, including creation, manipulation, and utility functions. We'll cover both basic and advanced implementations with proper memory management.

## Basic Binary Tree Class

### 1. Simple Implementation
```cpp
#include <iostream>
#include <queue>
#include <stack>

class BinaryTree {
private:
    struct TreeNode {
        int data;
        TreeNode* left;
        TreeNode* right;
        
        TreeNode(int val) : data(val), left(nullptr), right(nullptr) {}
    };
    
    TreeNode* root;
    
    // Helper function to delete tree
    void deleteTree(TreeNode* node) {
        if (node == nullptr) return;
        deleteTree(node->left);
        deleteTree(node->right);
        delete node;
    }
    
public:
    // Constructor
    BinaryTree() : root(nullptr) {}
    
    // Destructor
    ~BinaryTree() {
        deleteTree(root);
    }
    
    // Copy constructor (deep copy)
    BinaryTree(const BinaryTree& other) {
        root = copyTree(other.root);
    }
    
    // Assignment operator
    BinaryTree& operator=(const BinaryTree& other) {
        if (this != &other) {
            deleteTree(root);
            root = copyTree(other.root);
        }
        return *this;
    }
    
private:
    // Helper for deep copy
    TreeNode* copyTree(TreeNode* node) {
        if (node == nullptr) return nullptr;
        
        TreeNode* newNode = new TreeNode(node->data);
        newNode->left = copyTree(node->left);
        newNode->right = copyTree(node->right);
        return newNode;
    }
    
public:
    // Get root
    TreeNode* getRoot() const { return root; }
    
    // Check if tree is empty
    bool isEmpty() const { return root == nullptr; }
};
```

### 2. Enhanced Implementation with Utilities
```cpp
class EnhancedBinaryTree {
private:
    struct TreeNode {
        int data;
        TreeNode* left;
        TreeNode* right;
        
        TreeNode(int val) : data(val), left(nullptr), right(nullptr) {}
    };
    
    TreeNode* root;
    
    // Helper functions
    void deleteTree(TreeNode* node);
    TreeNode* copyTree(TreeNode* node);
    int height(TreeNode* node) const;
    int size(TreeNode* node) const;
    
public:
    // Constructors and destructor
    EnhancedBinaryTree() : root(nullptr) {}
    ~EnhancedBinaryTree() { deleteTree(root); }
    EnhancedBinaryTree(const EnhancedBinaryTree& other);
    EnhancedBinaryTree& operator=(const EnhancedBinaryTree& other);
    
    // Basic operations
    void insert(int value);
    bool search(int value) const;
    void remove(int value);
    
    // Tree properties
    int getHeight() const { return height(root); }
    int getSize() const { return size(root); }
    bool isEmpty() const { return root == nullptr; }
    
    // Traversals
    void inorder() const;
    void preorder() const;
    void postorder() const;
    void levelOrder() const;
    
    // Utility functions
    void clear();
    bool isBalanced() const;
    int diameter() const;
};
```

## Tree Creation Methods

### 1. Manual Creation
```cpp
class TreeCreator {
public:
    static TreeNode* createSampleTree() {
        TreeNode* root = new TreeNode(1);
        root->left = new TreeNode(2);
        root->right = new TreeNode(3);
        root->left->left = new TreeNode(4);
        root->left->right = new TreeNode(5);
        root->right->left = new TreeNode(6);
        root->right->right = new TreeNode(7);
        return root;
    }
    
    static TreeNode* createSkewedTree() {
        TreeNode* root = new TreeNode(1);
        root->right = new TreeNode(2);
        root->right->right = new TreeNode(3);
        root->right->right->right = new TreeNode(4);
        return root;
    }
    
    static TreeNode* createBalancedTree() {
        TreeNode* root = new TreeNode(10);
        root->left = new TreeNode(5);
        root->right = new TreeNode(15);
        root->left->left = new TreeNode(3);
        root->left->right = new TreeNode(7);
        root->right->left = new TreeNode(12);
        root->right->right = new TreeNode(18);
        return root;
    }
};
```

### 2. Creation from Array
```cpp
class ArrayToTree {
public:
    // Create complete binary tree from array (level order)
    static TreeNode* createCompleteTree(const std::vector<int>& arr) {
        if (arr.empty()) return nullptr;
        
        TreeNode* root = new TreeNode(arr[0]);
        std::queue<TreeNode*> q;
        q.push(root);
        
        int i = 1;
        while (!q.empty() && i < arr.size()) {
            TreeNode* current = q.front();
            q.pop();
            
            // Left child
            if (i < arr.size()) {
                current->left = new TreeNode(arr[i]);
                q.push(current->left);
                i++;
            }
            
            // Right child
            if (i < arr.size()) {
                current->right = new TreeNode(arr[i]);
                q.push(current->right);
                i++;
            }
        }
        
        return root;
    }
    
    // Create BST from sorted array
    static TreeNode* createBSTFromSorted(const std::vector<int>& arr, int start, int end) {
        if (start > end) return nullptr;
        
        int mid = start + (end - start) / 2;
        TreeNode* root = new TreeNode(arr[mid]);
        
        root->left = createBSTFromSorted(arr, start, mid - 1);
        root->right = createBSTFromSorted(arr, mid + 1, end);
        
        return root;
    }
    
    static TreeNode* createBSTFromSorted(const std::vector<int>& arr) {
        return createBSTFromSorted(arr, 0, arr.size() - 1);
    }
};
```

### 3. User Input Creation
```cpp
class InteractiveTreeCreator {
public:
    // Create tree from user input (level order)
    static TreeNode* createFromUserInput() {
        std::cout << "Enter root value: ";
        int rootVal;
        std::cin >> rootVal;
        
        TreeNode* root = new TreeNode(rootVal);
        std::queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            TreeNode* current = q.front();
            q.pop();
            
            // Left child
            std::cout << "Enter left child of " << current->data << " (-1 for none): ";
            int leftVal;
            std::cin >> leftVal;
            if (leftVal != -1) {
                current->left = new TreeNode(leftVal);
                q.push(current->left);
            }
            
            // Right child
            std::cout << "Enter right child of " << current->data << " (-1 for none): ";
            int rightVal;
            std::cin >> rightVal;
            if (rightVal != -1) {
                current->right = new TreeNode(rightVal);
                q.push(current->right);
            }
        }
        
        return root;
    }
    
    // Create tree from preorder and inorder traversals
    static TreeNode* createFromTraversals(const std::vector<int>& preorder, 
                                         const std::vector<int>& inorder) {
        std::unordered_map<int, int> inorderMap;
        for (int i = 0; i < inorder.size(); i++) {
            inorderMap[inorder[i]] = i;
        }
        
        return buildTree(preorder, 0, preorder.size() - 1,
                        inorder, 0, inorder.size() - 1, inorderMap);
    }
    
private:
    static TreeNode* buildTree(const std::vector<int>& preorder, int preStart, int preEnd,
                              const std::vector<int>& inorder, int inStart, int inEnd,
                              const std::unordered_map<int, int>& inorderMap) {
        if (preStart > preEnd || inStart > inEnd) return nullptr;
        
        int rootVal = preorder[preStart];
        TreeNode* root = new TreeNode(rootVal);
        
        int rootPos = inorderMap.at(rootVal);
        int leftSize = rootPos - inStart;
        
        root->left = buildTree(preorder, preStart + 1, preStart + leftSize,
                              inorder, inStart, rootPos - 1, inorderMap);
        root->right = buildTree(preorder, preStart + leftSize + 1, preEnd,
                               inorder, rootPos + 1, inEnd, inorderMap);
        
        return root;
    }
};
```

## Tree Operations Implementation

### 1. Insertion Operations
```cpp
class TreeOperations {
public:
    // Insert at first available position (level order)
    static void insertLevelOrder(TreeNode*& root, int value) {
        if (root == nullptr) {
            root = new TreeNode(value);
            return;
        }
        
        std::queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            TreeNode* current = q.front();
            q.pop();
            
            if (current->left == nullptr) {
                current->left = new TreeNode(value);
                return;
            } else {
                q.push(current->left);
            }
            
            if (current->right == nullptr) {
                current->right = new TreeNode(value);
                return;
            } else {
                q.push(current->right);
            }
        }
    }
    
    // Insert as left child of given node
    static bool insertLeft(TreeNode* parent, int value) {
        if (parent == nullptr || parent->left != nullptr) return false;
        parent->left = new TreeNode(value);
        return true;
    }
    
    // Insert as right child of given node
    static bool insertRight(TreeNode* parent, int value) {
        if (parent == nullptr || parent->right != nullptr) return false;
        parent->right = new TreeNode(value);
        return true;
    }
};
```

### 2. Search Operations
```cpp
class TreeSearch {
public:
    // Depth-first search
    static TreeNode* dfs(TreeNode* root, int value) {
        if (root == nullptr) return nullptr;
        if (root->data == value) return root;
        
        TreeNode* leftResult = dfs(root->left, value);
        if (leftResult != nullptr) return leftResult;
        
        return dfs(root->right, value);
    }
    
    // Breadth-first search
    static TreeNode* bfs(TreeNode* root, int value) {
        if (root == nullptr) return nullptr;
        
        std::queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            TreeNode* current = q.front();
            q.pop();
            
            if (current->data == value) return current;
            
            if (current->left) q.push(current->left);
            if (current->right) q.push(current->right);
        }
        
        return nullptr;
    }
    
    // Find parent of a node
    static TreeNode* findParent(TreeNode* root, TreeNode* child) {
        if (root == nullptr || child == nullptr || root == child) return nullptr;
        
        if (root->left == child || root->right == child) return root;
        
        TreeNode* leftResult = findParent(root->left, child);
        if (leftResult != nullptr) return leftResult;
        
        return findParent(root->right, child);
    }
};
```

### 3. Deletion Operations
```cpp
class TreeDeletion {
public:
    // Delete leaf node
    static bool deleteLeaf(TreeNode*& root, int value) {
        if (root == nullptr) return false;
        
        if (root->data == value && root->left == nullptr && root->right == nullptr) {
            delete root;
            root = nullptr;
            return true;
        }
        
        return deleteLeaf(root->left, value) || deleteLeaf(root->right, value);
    }
    
    // Delete node with one child
    static bool deleteNodeWithOneChild(TreeNode*& root, int value) {
        if (root == nullptr) return false;
        
        if (root->data == value) {
            TreeNode* child = (root->left != nullptr) ? root->left : root->right;
            delete root;
            root = child;
            return true;
        }
        
        return deleteNodeWithOneChild(root->left, value) || 
               deleteNodeWithOneChild(root->right, value);
    }
    
    // Delete node with two children (replace with inorder successor)
    static bool deleteNodeWithTwoChildren(TreeNode*& root, int value) {
        if (root == nullptr) return false;
        
        if (root->data == value) {
            TreeNode* successor = findMin(root->right);
            root->data = successor->data;
            return deleteNode(root->right, successor->data);
        }
        
        return deleteNodeWithTwoChildren(root->left, value) || 
               deleteNodeWithTwoChildren(root->right, value);
    }
    
private:
    static TreeNode* findMin(TreeNode* node) {
        while (node->left != nullptr) {
            node = node->left;
        }
        return node;
    }
    
    static bool deleteNode(TreeNode*& node, int value) {
        if (node == nullptr) return false;
        
        if (node->data == value) {
            if (node->left == nullptr && node->right == nullptr) {
                delete node;
                node = nullptr;
            } else if (node->left == nullptr) {
                TreeNode* temp = node->right;
                delete node;
                node = temp;
            } else if (node->right == nullptr) {
                TreeNode* temp = node->left;
                delete node;
                node = temp;
            } else {
                TreeNode* successor = findMin(node->right);
                node->data = successor->data;
                return deleteNode(node->right, successor->data);
            }
            return true;
        }
        
        return deleteNode(node->left, value) || deleteNode(node->right, value);
    }
};
```

## Utility Functions

### 1. Tree Analysis
```cpp
class TreeAnalysis {
public:
    // Calculate height
    static int height(TreeNode* root) {
        if (root == nullptr) return -1;
        return 1 + std::max(height(root->left), height(root->right));
    }
    
    // Count nodes
    static int countNodes(TreeNode* root) {
        if (root == nullptr) return 0;
        return 1 + countNodes(root->left) + countNodes(root->right);
    }
    
    // Count leaf nodes
    static int countLeaves(TreeNode* root) {
        if (root == nullptr) return 0;
        if (root->left == nullptr && root->right == nullptr) return 1;
        return countLeaves(root->left) + countLeaves(root->right);
    }
    
    // Count internal nodes
    static int countInternalNodes(TreeNode* root) {
        if (root == nullptr || (root->left == nullptr && root->right == nullptr)) {
            return 0;
        }
        return 1 + countInternalNodes(root->left) + countInternalNodes(root->right);
    }
    
    // Check if tree is balanced
    static bool isBalanced(TreeNode* root) {
        return checkBalance(root).first;
    }
    
    // Calculate diameter
    static int diameter(TreeNode* root) {
        return calculateDiameter(root).first;
    }
    
private:
    static std::pair<bool, int> checkBalance(TreeNode* node) {
        if (node == nullptr) return {true, -1};
        
        auto left = checkBalance(node->left);
        auto right = checkBalance(node->right);
        
        if (!left.first || !right.first) return {false, 0};
        if (abs(left.second - right.second) > 1) return {false, 0};
        
        return {true, std::max(left.second, right.second) + 1};
    }
    
    static std::pair<int, int> calculateDiameter(TreeNode* node) {
        if (node == nullptr) return {0, -1};
        
        auto left = calculateDiameter(node->left);
        auto right = calculateDiameter(node->right);
        
        int currentDiameter = std::max({left.first, right.first, 
                                       left.second + right.second + 2});
        int currentHeight = std::max(left.second, right.second) + 1;
        
        return {currentDiameter, currentHeight};
    }
};
```

### 2. Tree Validation
```cpp
class TreeValidation {
public:
    // Check if tree is full
    static bool isFull(TreeNode* root) {
        if (root == nullptr) return true;
        if (root->left == nullptr && root->right == nullptr) return true;
        if (root->left != nullptr && root->right != nullptr) {
            return isFull(root->left) && isFull(root->right);
        }
        return false;
    }
    
    // Check if tree is complete
    static bool isComplete(TreeNode* root) {
        if (root == nullptr) return true;
        
        std::queue<TreeNode*> q;
        q.push(root);
        bool flag = false;
        
        while (!q.empty()) {
            TreeNode* current = q.front();
            q.pop();
            
            if (current->left) {
                if (flag) return false;
                q.push(current->left);
            } else {
                flag = true;
            }
            
            if (current->right) {
                if (flag) return false;
                q.push(current->right);
            } else {
                flag = true;
            }
        }
        
        return true;
    }
    
    // Check if tree is perfect
    static bool isPerfect(TreeNode* root) {
        if (root == nullptr) return true;
        
        int depth = getDepth(root);
        return isPerfectRec(root, depth, 0);
    }
    
private:
    static int getDepth(TreeNode* node) {
        int depth = 0;
        while (node != nullptr) {
            depth++;
            node = node->left;
        }
        return depth;
    }
    
    static bool isPerfectRec(TreeNode* root, int depth, int level) {
        if (root == nullptr) return true;
        
        if (root->left == nullptr && root->right == nullptr) {
            return (depth == level + 1);
        }
        
        if (root->left == nullptr || root->right == nullptr) {
            return false;
        }
        
        return isPerfectRec(root->left, depth, level + 1) &&
               isPerfectRec(root->right, depth, level + 1);
    }
};
```

## Complete Example Usage

```cpp
int main() {
    // Create tree from array
    std::vector<int> arr = {1, 2, 3, 4, 5, 6, 7};
    TreeNode* root = ArrayToTree::createCompleteTree(arr);
    
    // Analyze tree
    std::cout << "Tree height: " << TreeAnalysis::height(root) << std::endl;
    std::cout << "Number of nodes: " << TreeAnalysis::countNodes(root) << std::endl;
    std::cout << "Number of leaves: " << TreeAnalysis::countLeaves(root) << std::endl;
    std::cout << "Is balanced: " << (TreeValidation::isBalanced(root) ? "Yes" : "No") << std::endl;
    
    // Search operations
    TreeNode* found = TreeSearch::bfs(root, 5);
    if (found) {
        std::cout << "Found node with value 5" << std::endl;
    }
    
    // Insert new node
    TreeOperations::insertLevelOrder(root, 8);
    
    // Cleanup
    // Note: In real implementation, use proper destructor or smart pointers
    
    return 0;
}
```

## Best Practices

1. **Memory Management**: Always clean up dynamically allocated nodes
2. **Error Handling**: Check for nullptr before dereferencing
3. **Copy Semantics**: Implement proper copy constructor and assignment operator
4. **Recursive Depth**: Be aware of stack overflow for very deep trees
5. **Const Correctness**: Use const methods for read-only operations

## Summary

This implementation provides a complete foundation for binary tree operations in C++. The modular design allows for easy extension and customization based on specific requirements.
