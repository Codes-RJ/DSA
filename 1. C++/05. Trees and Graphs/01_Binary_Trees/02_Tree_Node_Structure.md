# Tree Node Structure and Implementation

## Introduction
The tree node is the fundamental building block of any tree data structure. In C++, we implement tree nodes using structs or classes that contain data and pointers to child nodes.

## Basic Node Structure

### Simple Binary Tree Node
```cpp
struct TreeNode {
    int data;                    // Data stored in the node
    TreeNode* left;              // Pointer to left child
    TreeNode* right;             // Pointer to right child
    
    // Constructor
    TreeNode(int val) : data(val), left(nullptr), right(nullptr) {}
};
```

### Enhanced Node with Additional Features
```cpp
struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;
    TreeNode* parent;            // Pointer to parent node
    int height;                  // Height of subtree rooted at this node
    int size;                    // Size of subtree rooted at this node
    
    // Constructor with all parameters
    TreeNode(int val, TreeNode* p = nullptr) 
        : data(val), left(nullptr), right(nullptr), parent(p), height(0), size(1) {}
};
```

## Node Implementation Variations

### 1. Template-Based Generic Node
```cpp
template <typename T>
class TreeNode {
private:
    T data;
    TreeNode* left;
    TreeNode* right;
    
public:
    // Constructor
    TreeNode(const T& value) : data(value), left(nullptr), right(nullptr) {}
    
    // Getters
    T getData() const { return data; }
    TreeNode* getLeft() const { return left; }
    TreeNode* getRight() const { return right; }
    
    // Setters
    void setData(const T& value) { data = value; }
    void setLeft(TreeNode* node) { left = node; }
    void setRight(TreeNode* node) { right = node; }
    
    // Utility methods
    bool isLeaf() const { return left == nullptr && right == nullptr; }
    bool hasLeft() const { return left != nullptr; }
    bool hasRight() const { return right != nullptr; }
};
```

### 2. Node with Destructor for Memory Management
```cpp
class TreeNode {
private:
    int data;
    TreeNode* left;
    TreeNode* right;
    
public:
    // Constructor
    TreeNode(int val) : data(val), left(nullptr), right(nullptr) {}
    
    // Destructor - recursively delete subtree
    ~TreeNode() {
        delete left;   // Safe even if left is nullptr
        delete right;  // Safe even if right is nullptr
    }
    
    // Prevent copying to avoid double deletion
    TreeNode(const TreeNode&) = delete;
    TreeNode& operator=(const TreeNode&) = delete;
    
    // Getters and setters
    int getData() const { return data; }
    TreeNode* getLeft() const { return left; }
    TreeNode* getRight() const { return right; }
    
    void setLeft(TreeNode* node) { left = node; }
    void setRight(TreeNode* node) { right = node; }
};
```

## Memory Management Strategies

### 1. Manual Memory Management
```cpp
class BinaryTree {
private:
    TreeNode* root;
    
    // Helper function to delete tree
    void deleteTree(TreeNode* node) {
        if (node == nullptr) return;
        
        deleteTree(node->left);   // Delete left subtree
        deleteTree(node->right);  // Delete right subtree
        delete node;              // Delete current node
    }
    
public:
    BinaryTree() : root(nullptr) {}
    
    ~BinaryTree() {
        deleteTree(root);
    }
    
    // Other tree operations...
};
```

### 2. Smart Pointer Approach (Modern C++)
```cpp
#include <memory>

template <typename T>
class TreeNode {
private:
    T data;
    std::unique_ptr<TreeNode> left;
    std::unique_ptr<TreeNode> right;
    TreeNode* parent;  // Raw pointer to avoid circular reference
    
public:
    TreeNode(const T& value, TreeNode* p = nullptr) 
        : data(value), left(nullptr), right(nullptr), parent(p) {}
    
    // Getters return raw pointers for navigation
    TreeNode* getLeft() const { return left.get(); }
    TreeNode* getRight() const { return right.get(); }
    TreeNode* getParent() const { return parent; }
    
    // Setters take unique_ptr for ownership transfer
    void setLeft(std::unique_ptr<TreeNode> node) {
        left = std::move(node);
        if (left) left->parent = this;
    }
    
    void setRight(std::unique_ptr<TreeNode> node) {
        right = std::move(node);
        if (right) right->parent = this;
    }
    
    T getData() const { return data; }
    void setData(const T& value) { data = value; }
};
```

## Array-Based Node Representation

### Complete Binary Tree in Array
```cpp
class ArrayBinaryTree {
private:
    std::vector<int> tree;
    int capacity;
    
public:
    ArrayBinaryTree(int size) : capacity(size) {
        tree.resize(size, -1);  // -1 indicates empty
    }
    
    // Get index calculations
    int leftChild(int index) const {
        int left = 2 * index + 1;
        return (left < capacity && tree[left] != -1) ? left : -1;
    }
    
    int rightChild(int index) const {
        int right = 2 * index + 2;
        return (right < capacity && tree[right] != -1) ? right : -1;
    }
    
    int parent(int index) const {
        return (index > 0) ? (index - 1) / 2 : -1;
    }
    
    // Operations
    void insert(int value, int index) {
        if (index < capacity) {
            tree[index] = value;
        }
    }
    
    int getValue(int index) const {
        return (index < capacity) ? tree[index] : -1;
    }
};
```

## Node Utility Functions

### 1. Node Creation Functions
```cpp
// Create leaf node
TreeNode* createLeaf(int value) {
    return new TreeNode(value);
}

// Create node with left child
TreeNode* createNodeWithLeft(int value, TreeNode* leftChild) {
    TreeNode* node = new TreeNode(value);
    node->setLeft(leftChild);
    return node;
}

// Create node with both children
TreeNode* createNodeWithChildren(int value, TreeNode* leftChild, TreeNode* rightChild) {
    TreeNode* node = new TreeNode(value);
    node->setLeft(leftChild);
    node->setRight(rightChild);
    return node;
}
```

### 2. Node Inspection Functions
```cpp
// Check if node is leaf
bool isLeaf(const TreeNode* node) {
    return node != nullptr && node->getLeft() == nullptr && node->getRight() == nullptr;
}

// Check if node is full (has both children)
bool isFullNode(const TreeNode* node) {
    return node != nullptr && node->getLeft() != nullptr && node->getRight() != nullptr;
}

// Count children of node
int countChildren(const TreeNode* node) {
    if (node == nullptr) return 0;
    
    int count = 0;
    if (node->getLeft() != nullptr) count++;
    if (node->getRight() != nullptr) count++;
    return count;
}
```

## Advanced Node Features

### 1. Node with Thread Support (Threaded Binary Tree)
```cpp
class ThreadedTreeNode {
private:
    int data;
    ThreadedTreeNode* left;
    ThreadedTreeNode* right;
    bool leftThread;    // true if left points to predecessor
    bool rightThread;   // true if right points to successor
    
public:
    ThreadedTreeNode(int val) : data(val), left(nullptr), right(nullptr), 
                               leftThread(false), rightThread(false) {}
    
    // Getters and setters...
};
```

### 2. Node with Metadata
```cpp
struct MetaTreeNode {
    int data;
    MetaTreeNode* left;
    MetaTreeNode* right;
    
    // Metadata
    int height;
    int size;
    int sum;
    int min;
    int max;
    
    MetaTreeNode(int val) : data(val), left(nullptr), right(nullptr),
                           height(0), size(1), sum(val), min(val), max(val) {}
    
    // Update metadata based on children
    void updateMetadata() {
        size = 1;
        sum = data;
        min = data;
        max = data;
        
        if (left) {
            size += left->size;
            sum += left->sum;
            min = std::min(min, left->min);
            max = std::max(max, left->max);
        }
        
        if (right) {
            size += right->size;
            sum += right->sum;
            min = std::min(min, right->min);
            max = std::max(max, right->max);
        }
    }
};
```

## Best Practices

### 1. Initialization
```cpp
// Always initialize pointers to nullptr
TreeNode* node = new TreeNode(10);
// left and right are automatically nullptr due to constructor
```

### 2. Memory Safety
```cpp
// Use RAII and smart pointers when possible
class SafeBinaryTree {
    std::unique_ptr<TreeNode> root;
public:
    // Automatic memory cleanup
};
```

### 3. Copy Semantics
```cpp
// Prevent accidental copying
TreeNode(const TreeNode&) = delete;
TreeNode& operator=(const TreeNode&) = delete;
```

### 4. Null Checks
```cpp
void safeOperation(TreeNode* node) {
    if (node == nullptr) return;
    // Safe to use node here
}
```

## Common Pitfalls

1. **Dangling Pointers**: Deleting a node without updating parent pointers
2. **Memory Leaks**: Forgetting to delete dynamically allocated nodes
3. **Double Deletion**: Deleting the same node multiple times
4. **Null Pointer Dereference**: Not checking for nullptr before access
5. **Circular References**: In smart pointers, creating reference cycles

## Performance Considerations

### Memory Usage
- **Pointer-based**: O(n) nodes + O(n) pointers = O(n) space
- **Array-based**: O(n) space, but may have wasted space for sparse trees

### Cache Performance
- **Array-based**: Better cache locality
- **Pointer-based**: Poorer cache locality due to scattered memory

### Allocation Overhead
- **Dynamic allocation**: Higher overhead per node
- **Array allocation**: Lower overhead, but fixed size

## Summary

The tree node structure is the foundation of all tree-based data structures. Choose the appropriate implementation based on your specific needs:
- Use simple structs for basic trees
- Use templates for generic implementations
- Use smart pointers for automatic memory management
- Use array representation for complete trees with known size
