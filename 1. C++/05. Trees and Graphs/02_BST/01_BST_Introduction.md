# BST Introduction

## Overview
A Binary Search Tree (BST) is a binary tree data structure that maintains the BST property: for each node, all values in its left subtree are less than the node's value, and all values in its right subtree are greater than the node's value. This property enables efficient searching, insertion, and deletion operations.

## BST Properties and Invariants

### Core BST Property
For any node `N` in the tree:
- All keys in `N`'s left subtree < `N`'s key
- All keys in `N`'s right subtree > `N`'s key
- Both left and right subtrees are also BSTs

### Important Invariants
- **No duplicate keys**: Standard BST doesn't allow duplicates (can be modified)
- **Ordered structure**: Inorder traversal yields sorted keys
- **Recursive property**: BST property holds recursively for all subtrees

## BST Node Structure

### Basic Node Implementation
```cpp
struct BSTNode {
    int data;
    BSTNode* left;
    BSTNode* right;
    
    // Constructor
    BSTNode(int value) : data(value), left(nullptr), right(nullptr) {}
    
    // Constructor with children
    BSTNode(int value, BSTNode* leftChild, BSTNode* rightChild) 
        : data(value), left(leftChild), right(rightChild) {}
};
```

### Enhanced Node with Parent Pointer
```cpp
struct BSTNodeWithParent {
    int data;
    BSTNodeWithParent* left;
    BSTNodeWithParent* right;
    BSTNodeWithParent* parent;
    
    BSTNodeWithParent(int value) 
        : data(value), left(nullptr), right(nullptr), parent(nullptr) {}
};
```

### Template-Based Generic Node
```cpp
template <typename T>
struct GenericBSTNode {
    T data;
    GenericBSTNode* left;
    GenericBSTNode* right;
    
    GenericBSTNode(const T& value) 
        : data(value), left(nullptr), right(nullptr) {}
    
    // Comparison operators
    bool operator<(const GenericBSTNode& other) const {
        return data < other.data;
    }
    
    bool operator>(const GenericBSTNode& other) const {
        return data > other.data;
    }
    
    bool operator==(const GenericBSTNode& other) const {
        return data == other.data;
    }
};
```

## BST Class Structure

### Basic BST Class
```cpp
class BinarySearchTree {
private:
    BSTNode* root;
    
    // Private helper methods
    BSTNode* insert(BSTNode* node, int value);
    BSTNode* remove(BSTNode* node, int value);
    BSTNode* search(BSTNode* node, int value);
    BSTNode* findMin(BSTNode* node);
    BSTNode* findMax(BSTNode* node);
    void inorder(BSTNode* node);
    void preorder(BSTNode* node);
    void postorder(BSTNode* node);
    void destroyTree(BSTNode* node);
    int height(BSTNode* node);
    int size(BSTNode* node);
    
public:
    // Constructor and destructor
    BinarySearchTree() : root(nullptr) {}
    ~BinarySearchTree() { destroyTree(root); }
    
    // Copy constructor and assignment operator
    BinarySearchTree(const BinarySearchTree& other);
    BinarySearchTree& operator=(const BinarySearchTree& other);
    
    // Public interface
    void insert(int value);
    void remove(int value);
    bool search(int value);
    int getMin();
    int getMax();
    void inorderTraversal();
    void preorderTraversal();
    void postorderTraversal();
    int getHeight();
    int getSize();
    bool isEmpty();
};
```

### Template-Based BST Class
```cpp
template <typename T>
class GenericBST {
private:
    GenericBSTNode<T>* root;
    
    // Helper methods
    GenericBSTNode<T>* insert(GenericBSTNode<T>* node, const T& value);
    GenericBSTNode<T>* remove(GenericBSTNode<T>* node, const T& value);
    GenericBSTNode<T>* search(GenericBSTNode<T>* node, const T& value);
    void destroyTree(GenericBSTNode<T>* node);
    
public:
    GenericBST() : root(nullptr) {}
    ~GenericBST() { destroyTree(root); }
    
    void insert(const T& value);
    void remove(const T& value);
    bool search(const T& value);
    // ... other methods
};
```

## Key Characteristics

### Advantages of BST
1. **Efficient Search**: Average case O(log n) search time
2. **Ordered Structure**: Maintains sorted order of elements
3. **Dynamic**: Supports efficient insertions and deletions
4. **Simple Implementation**: Relatively easy to implement
5. **Flexible**: Can be extended to various applications

### Disadvantages of BST
1. **Worst-Case Performance**: Can become skewed (O(n) operations)
2. **No Balance Guarantee**: Height depends on insertion order
3. **Memory Overhead**: Extra space for pointers
4. **Duplicate Handling**: Standard implementation doesn't handle duplicates

### Performance Characteristics
| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Search | O(log n) | O(n) |
| Insertion | O(log n) | O(n) |
| Deletion | O(log n) | O(n) |
| Traversal | O(n) | O(n) |
| Space | O(n) | O(n) |

## BST Variants and Extensions

### 1. BST with Duplicate Handling
```cpp
class BSTWithDuplicates {
private:
    struct Node {
        int data;
        int count;
        Node* left;
        Node* right;
        
        Node(int value) : data(value), count(1), left(nullptr), right(nullptr) {}
    };
    
    Node* root;
    
public:
    void insert(int value);
    void remove(int value);
    int getCount(int value); // Returns count of occurrences
};
```

### 2. Self-Balancing BST Variants
- **AVL Trees**: Strictly balanced, O(log n) guaranteed
- **Red-Black Trees**: Approximately balanced, widely used
- **Splay Trees**: Self-adjusting, amortized O(log n)
- **B-Trees**: External memory, disk-based structures

### 3. Specialized BSTs
- **Interval Trees**: For interval queries
- **Segment Trees**: For range queries
- **Trie**: Prefix trees for strings
- **Heap**: Priority queue variant

## Common Applications

### 1. Dictionary Implementation
```cpp
class Dictionary {
private:
    BSTNode* root;
    
public:
    void insertWord(const std::string& word, const std::string& meaning);
    std::string searchWord(const std::string& word);
    void removeWord(const std::string& word);
};
```

### 2. Database Indexing
- **Primary Index**: Main data organization
- **Secondary Index**: Alternative access paths
- **Composite Index**: Multiple field indexing

### 3. File Systems
- **Directory Structure**: Hierarchical organization
- **File Allocation**: Efficient file lookup
- **Symbol Tables**: Compiler implementation

## BST Validation and Properties

### Check if Tree is Valid BST
```cpp
class BSTValidator {
public:
    // Method 1: Using min/max range
    static bool isValidBST(BSTNode* root) {
        return isValidBSTHelper(root, INT_MIN, INT_MAX);
    }
    
private:
    static bool isValidBSTHelper(BSTNode* node, long long min, long long max) {
        if (node == nullptr) return true;
        
        if (node->data <= min || node->data >= max) {
            return false;
        }
        
        return isValidBSTHelper(node->left, min, node->data) &&
               isValidBSTHelper(node->right, node->data, max);
    }
    
    // Method 2: Using inorder traversal
    static bool isValidBSTInorder(BSTNode* root) {
        std::vector<int> inorder;
        inorderTraversal(root, inorder);
        
        for (int i = 1; i < inorder.size(); i++) {
            if (inorder[i] <= inorder[i - 1]) {
                return false;
            }
        }
        
        return true;
    }
    
    static void inorderTraversal(BSTNode* node, std::vector<int>& result) {
        if (node == nullptr) return;
        
        inorderTraversal(node->left, result);
        result.push_back(node->data);
        inorderTraversal(node->right, result);
    }
};
```

## BST Properties Analysis

### Height Analysis
- **Best Case**: Balanced tree, height = O(log n)
- **Worst Case**: Skewed tree, height = O(n)
- **Average Case**: Random insertions, height = O(log n)

### Size and Height Relationship
For a BST with `n` nodes:
- **Minimum height**: ⌊log₂n⌋ (perfectly balanced)
- **Maximum height**: n-1 (completely skewed)
- **Average height**: ~1.39 log₂n (random BST)

### Density and Sparsity
- **Dense BST**: Many nodes, relatively balanced
- **Sparse BST**: Few nodes, potentially unbalanced
- **Complete BST**: All levels filled except possibly last

## Memory Management

### Manual Memory Management
```cpp
class BSTMemoryManager {
private:
    void destroyTree(BSTNode* node) {
        if (node == nullptr) return;
        
        destroyTree(node->left);
        destroyTree(node->right);
        delete node;
    }
    
public:
    ~BinarySearchTree() {
        destroyTree(root);
    }
};
```

### Smart Pointer Implementation
```cpp
class ModernBST {
private:
    using NodePtr = std::unique_ptr<BSTNode>;
    NodePtr root;
    
public:
    void insert(int value) {
        root = insert(std::move(root), value);
    }
    
private:
    NodePtr insert(NodePtr node, int value) {
        if (!node) {
            return std::make_unique<BSTNode>(value);
        }
        
        if (value < node->data) {
            node->left = insert(std::move(node->left), value);
        } else if (value > node->data) {
            node->right = insert(std::move(node->right), value);
        }
        
        return node;
    }
};
```

## Best Practices

### Implementation Guidelines
1. **Handle Edge Cases**: Empty tree, single node, duplicates
2. **Memory Management**: Proper cleanup to avoid leaks
3. **Error Handling**: Validate inputs and handle exceptions
4. **Consistency**: Maintain BST invariants after all operations
5. **Testing**: Test with various tree shapes and sizes

### Performance Optimization
1. **Balancing**: Consider self-balancing variants
2. **Memory Pool**: For frequent insertions/deletions
3. **Iterative Methods**: Avoid recursion for deep trees
4. **Caching**: Store frequently accessed values
5. **Bulk Operations**: Batch insertions when possible

## Common Pitfalls

### Implementation Errors
1. **Incorrect BST Property**: Not maintaining order invariant
2. **Memory Leaks**: Forgetting to delete nodes
3. **Null Pointer Dereference**: Not checking for null
4. **Infinite Recursion**: Incorrect base cases
5. **Duplicate Handling**: Inconsistent duplicate policy

### Logic Errors
1. **Wrong Comparison**: Using wrong comparison operators
2. **Incorrect Rotation**: In self-balancing variants
3. **Height Calculation**: Off-by-one errors
4. **Traversal Order**: Wrong visiting sequence
5. **Parent Pointer Updates**: Forgetting to update parents

## Summary

Binary Search Trees provide an efficient way to store and retrieve ordered data. While they offer excellent average-case performance, their worst-case performance can be poor without balancing. Understanding BST fundamentals is crucial before moving to more advanced balanced tree structures. Proper implementation requires careful attention to maintaining the BST property and handling edge cases.
