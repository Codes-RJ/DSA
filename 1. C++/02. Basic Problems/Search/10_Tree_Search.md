# Tree Search (BST)

## Overview
Tree search algorithms operate on tree data structures to find specific values. Binary Search Trees (BST) are the most common, providing efficient search, insertion, and deletion operations with O(log n) average time complexity.

## Algorithm Description

### Theory
Binary Search Trees maintain the BST property: for any node, all values in the left subtree are less than the node's value, and all values in the right subtree are greater. This property enables efficient searching by eliminating half of the remaining tree at each step.

### Mathematical Foundation
BST property: left subtree < node < right subtree
- Height determines performance: balanced = O(log n), unbalanced = O(n)
- Average height for random insertions: O(log n)
- Worst case (skewed tree): O(n)

### Algorithm Steps
1. Start at root
2. Compare target with current node
3. If equal, return node
4. If target < node, search left subtree
5. If target > node, search right subtree

### Pseudocode
```
FUNCTION bstSearch(root, target):
    current = root
    
    WHILE current != null:
        IF target == current.value:
            RETURN current
        ELSE IF target < current.value:
            current = current.left
        ELSE:
            current = current.right
    
    RETURN null  // Not found
```

## Complexity Analysis

### Time Complexity
- **Average Case**: O(log n) - Balanced tree
- **Worst Case**: O(n) - Skewed tree
- **Best Case**: O(1) - Target at root

### Space Complexity
- **Space**: O(1) - Iterative implementation
- **Space**: O(log n) - Recursive implementation (stack space)

## Best Practices
- Use self-balancing trees (AVL, Red-Black) for guaranteed performance
- Consider B-Trees for disk-based storage
- Implement proper balancing strategies
- Handle duplicate values consistently

## When to Use
- Dynamic data with frequent insertions/deletions
- Range queries and ordered data
- Database indexing
- Memory management systems
- File system structures

## Variants

### 1. Binary Search Tree (BST)
Basic tree structure with BST property.

### 2. AVL Tree
Self-balancing BST with height balance factor.

### 3. Red-Black Tree
Self-balancing BST with color-based balancing.

### 4. B-Tree
Balanced tree for disk-based storage.

### 5. B+ Tree
Variant of B-tree optimized for range queries.

## Implementation Examples

### Example 1: Basic Binary Search Tree
```cpp
#include <iostream>
#include <memory>

template<typename T>
class BSTNode {
public:
    T data;
    std::shared_ptr<BSTNode<T>> left;
    std::shared_ptr<BSTNode<T>> right;
    
    BSTNode(T value) : data(value), left(nullptr), right(nullptr) {}
};

template<typename T>
class BinarySearchTree {
private:
    std::shared_ptr<BSTNode<T>> root;
    
    std::shared_ptr<BSTNode<T>> insertRecursive(std::shared_ptr<BSTNode<T>> node, T value) {
        if (!node) {
            return std::make_shared<BSTNode<T>>(value);
        }
        
        if (value < node->data) {
            node->left = insertRecursive(node->left, value);
        } else if (value > node->data) {
            node->right = insertRecursive(node->right, value);
        }
        
        return node;
    }
    
    bool searchRecursive(std::shared_ptr<BSTNode<T>> node, T value) const {
        if (!node) {
            return false;
        }
        
        if (value == node->data) {
            return true;
        } else if (value < node->data) {
            return searchRecursive(node->left, value);
        } else {
            return searchRecursive(node->right, value);
        }
    }
    
    void inorderTraversal(std::shared_ptr<BSTNode<T>> node) const {
        if (node) {
            inorderTraversal(node->left);
            std::cout << node->data << " ";
            inorderTraversal(node->right);
        }
    }
    
public:
    BinarySearchTree() : root(nullptr) {}
    
    void insert(T value) {
        root = insertRecursive(root, value);
    }
    
    bool search(T value) const {
        return searchRecursive(root, value);
    }
    
    bool searchIterative(T value) const {
        std::shared_ptr<BSTNode<T>> current = root;
        
        while (current) {
            if (value == current->data) {
                return true;
            } else if (value < current->data) {
                current = current->left;
            } else {
                current = current->right;
            }
        }
        
        return false;
    }
    
    void displayInorder() const {
        inorderTraversal(root);
        std::cout << std::endl;
    }
};
```

### Example 2: AVL Tree (Self-Balancing)
```cpp
#include <algorithm>
#include <memory>

template<typename T>
class AVLNode {
public:
    T data;
    int height;
    std::shared_ptr<AVLNode<T>> left;
    std::shared_ptr<AVLNode<T>> right;
    
    AVLNode(T value) : data(value), height(1), left(nullptr), right(nullptr) {}
};

template<typename T>
class AVLTree {
private:
    std::shared_ptr<AVLNode<T>> root;
    
    int getHeight(std::shared_ptr<AVLNode<T>> node) const {
        return node ? node->height : 0;
    }
    
    int getBalanceFactor(std::shared_ptr<AVLNode<T>> node) const {
        return node ? getHeight(node->left) - getHeight(node->right) : 0;
    }
    
    int updateHeight(std::shared_ptr<AVLNode<T>> node) const {
        return node ? 1 + std::max(getHeight(node->left), getHeight(node->right)) : 0;
    }
    
    std::shared_ptr<AVLNode<T>> rotateRight(std::shared_ptr<AVLNode<T>> y) {
        std::shared_ptr<AVLNode<T>> x = y->left;
        std::shared_ptr<AVLNode<T>> T2 = x->right;
        
        x->right = y;
        y->left = T2;
        
        y->height = updateHeight(y);
        x->height = updateHeight(x);
        
        return x;
    }
    
    std::shared_ptr<AVLNode<T>> rotateLeft(std::shared_ptr<AVLNode<T>> x) {
        std::shared_ptr<AVLNode<T>> y = x->right;
        std::shared_ptr<AVLNode<T>> T2 = y->left;
        
        y->left = x;
        x->right = T2;
        
        x->height = updateHeight(x);
        y->height = updateHeight(y);
        
        return y;
    }
    
    std::shared_ptr<AVLNode<T>> insert(std::shared_ptr<AVLNode<T>> node, T value) {
        if (!node) {
            return std::make_shared<AVLNode<T>>(value);
        }
        
        if (value < node->data) {
            node->left = insert(node->left, value);
        } else if (value > node->data) {
            node->right = insert(node->right, value);
        } else {
            return node;  // Duplicate values not allowed
        }
        
        node->height = updateHeight(node);
        int balance = getBalanceFactor(node);
        
        // Left Left Case
        if (balance > 1 && value < node->left->data) {
            return rotateRight(node);
        }
        
        // Right Right Case
        if (balance < -1 && value > node->right->data) {
            return rotateLeft(node);
        }
        
        // Left Right Case
        if (balance > 1 && value > node->left->data) {
            node->left = rotateLeft(node->left);
            return rotateRight(node);
        }
        
        // Right Left Case
        if (balance < -1 && value < node->right->data) {
            node->right = rotateRight(node->right);
            return rotateLeft(node);
        }
        
        return node;
    }
    
public:
    AVLTree() : root(nullptr) {}
    
    void insert(T value) {
        root = insert(root, value);
    }
    
    bool search(T value) const {
        std::shared_ptr<AVLNode<T>> current = root;
        
        while (current) {
            if (value == current->data) {
                return true;
            } else if (value < current->data) {
                current = current->left;
            } else {
                current = current->right;
            }
        }
        
        return false;
    }
};
```

### Example 3: Red-Black Tree
```cpp
#include <memory>

enum class Color { RED, BLACK };

template<typename T>
class RBNode {
public:
    T data;
    Color color;
    std::shared_ptr<RBNode<T>> left;
    std::shared_ptr<RBNode<T>> right;
    std::shared_ptr<RBNode<T>> parent;
    
    RBNode(T value) : data(value), color(Color::RED), 
                     left(nullptr), right(nullptr), parent(nullptr) {}
};

template<typename T>
class RedBlackTree {
private:
    std::shared_ptr<RBNode<T>> root;
    std::shared_ptr<RBNode<T>> NIL;
    
    RedBlackTree() {
        NIL = std::make_shared<RBNode<T>>(T());
        NIL->color = Color::BLACK;
        root = NIL;
    }
    
    void leftRotate(std::shared_ptr<RBNode<T>> x) {
        std::shared_ptr<RBNode<T>> y = x->right;
        x->right = y->left;
        
        if (y->left != NIL) {
            y->left->parent = x;
        }
        
        y->parent = x->parent;
        
        if (x->parent == nullptr) {
            root = y;
        } else if (x == x->parent->left) {
            x->parent->left = y;
        } else {
            x->parent->right = y;
        }
        
        y->left = x;
        x->parent = y;
    }
    
    void rightRotate(std::shared_ptr<RBNode<T>> y) {
        std::shared_ptr<RBNode<T>> x = y->left;
        y->left = x->right;
        
        if (x->right != NIL) {
            x->right->parent = y;
        }
        
        x->parent = y->parent;
        
        if (y->parent == nullptr) {
            root = x;
        } else if (y == y->parent->right) {
            y->parent->right = x;
        } else {
            y->parent->left = x;
        }
        
        x->right = y;
        y->parent = x;
    }
    
    void insertFixup(std::shared_ptr<RBNode<T>> z) {
        while (z->parent && z->parent->color == Color::RED) {
            if (z->parent == z->parent->parent->left) {
                std::shared_ptr<RBNode<T>> y = z->parent->parent->right;
                
                if (y->color == Color::RED) {
                    z->parent->color = Color::BLACK;
                    y->color = Color::BLACK;
                    z->parent->parent->color = Color::RED;
                    z = z->parent->parent;
                } else {
                    if (z == z->parent->right) {
                        z = z->parent;
                        leftRotate(z);
                    }
                    
                    z->parent->color = Color::BLACK;
                    z->parent->parent->color = Color::RED;
                    rightRotate(z->parent->parent);
                }
            } else {
                // Symmetric case
                std::shared_ptr<RBNode<T>> y = z->parent->parent->left;
                
                if (y->color == Color::RED) {
                    z->parent->color = Color::BLACK;
                    y->color = Color::BLACK;
                    z->parent->parent->color = Color::RED;
                    z = z->parent->parent;
                } else {
                    if (z == z->parent->left) {
                        z = z->parent;
                        rightRotate(z);
                    }
                    
                    z->parent->color = Color::BLACK;
                    z->parent->parent->color = Color::RED;
                    leftRotate(z->parent->parent);
                }
            }
        }
        
        root->color = Color::BLACK;
    }
    
public:
    void insert(T value) {
        std::shared_ptr<RBNode<T>> z = std::make_shared<RBNode<T>>(value);
        z->left = NIL;
        z->right = NIL;
        
        std::shared_ptr<RBNode<T>> y = nullptr;
        std::shared_ptr<RBNode<T>> x = root;
        
        while (x != NIL) {
            y = x;
            if (z->data < x->data) {
                x = x->left;
            } else {
                x = x->right;
            }
        }
        
        z->parent = y;
        
        if (y == nullptr) {
            root = z;
        } else if (z->data < y->data) {
            y->left = z;
        } else {
            y->right = z;
        }
        
        insertFixup(z);
    }
    
    bool search(T value) const {
        std::shared_ptr<RBNode<T>> current = root;
        
        while (current != NIL) {
            if (value == current->data) {
                return true;
            } else if (value < current->data) {
                current = current->left;
            } else {
                current = current->right;
            }
        }
        
        return false;
    }
};
```

### Example 4: Range Query Operations
```cpp
template<typename T>
class BSTWithRangeQueries : public BinarySearchTree<T> {
private:
    void rangeQueryHelper(std::shared_ptr<BSTNode<T>> node, T low, T high, 
                         std::vector<T>& result) const {
        if (!node) return;
        
        if (node->data > low) {
            rangeQueryHelper(node->left, low, high, result);
        }
        
        if (node->data >= low && node->data <= high) {
            result.push_back(node->data);
        }
        
        if (node->data < high) {
            rangeQueryHelper(node->right, low, high, result);
        }
    }
    
public:
    std::vector<T> rangeQuery(T low, T high) const {
        std::vector<T> result;
        rangeQueryHelper(this->root, low, high, result);
        return result;
    }
    
    T findMin() const {
        if (!this->root) {
            throw std::runtime_error("Tree is empty");
        }
        
        std::shared_ptr<BSTNode<T>> current = this->root;
        while (current->left) {
            current = current->left;
        }
        
        return current->data;
    }
    
    T findMax() const {
        if (!this->root) {
            throw std::runtime_error("Tree is empty");
        }
        
        std::shared_ptr<BSTNode<T>> current = this->root;
        while (current->right) {
            current = current->right;
        }
        
        return current->data;
    }
};
```

## Testing and Verification

### Test Cases
1. **Basic operations**: Insert, search, delete
2. **Balancing**: AVL and Red-Black tree balance verification
3. **Edge cases**: Empty tree, single node
4. **Range queries**: Test range search functionality
5. **Performance**: Compare with other data structures

### Performance Tests
1. **Search performance**: Average case O(log n) verification
2. **Balancing overhead**: Self-balancing vs basic BST
3. **Memory usage**: Space complexity analysis
4. **Tree height**: Balance verification

## Common Pitfalls
1. Not maintaining BST property
2. Forgetting to update heights in AVL trees
3. Incorrect color assignments in Red-Black trees
4. Memory leaks in tree destruction
5. Improper handling of duplicate values

## Optimization Tips
1. Use self-balancing trees for guaranteed performance
2. Implement iterative versions to avoid stack overflow
3. Consider memory pooling for frequent allocations
4. Use appropriate balancing strategies
5. Implement efficient range queries

## Real-World Applications
- Database indexing
- File systems
- Memory allocators
- Compiler symbol tables
- Network routing
- Game development (spatial partitioning)

## Advanced Topics

### Tree Traversals
- In-order, pre-order, post-order
- Level-order traversal
- Threaded binary trees

### Balanced Tree Variants
- Splay trees
- Treaps
- Weight-balanced trees
- scapegoat trees

### External Memory Trees
- B-trees and B+ trees
- Fractal tree indexes
- Cache-oblivious trees

## Related Data Structures
- Heaps
- Tries
- Skip lists
- Graphs

## References
- Introduction to Algorithms (CLRS)
- The Art of Computer Programming (Donald Knuth)
- Data Structures and Algorithm Analysis

---

*This implementation provides a comprehensive guide to tree search algorithms with various balancing strategies and optimization techniques.*
