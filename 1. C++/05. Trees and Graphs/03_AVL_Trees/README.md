# AVL Trees (Adelson-Velsky and Landis Trees)

## Overview
AVL trees are self-balancing binary search trees where the height difference between left and right subtrees of any node is at most 1. This property ensures that the tree remains balanced, guaranteeing O(log n) time complexity for all basic operations.

## Topics Covered

### 1. AVL Introduction (`01_AVL_Introduction.md`)
- AVL tree definition and properties
- Balance factor concept
- Need for self-balancing trees
- Comparison with BST and other balanced trees
- Applications and use cases

### 2. Rotations (`02_Rotations.md`)
- Single rotations (LL, RR)
- Double rotations (LR, RL)
- Rotation algorithms and implementation
- When and how to perform rotations
- Visual examples and step-by-step process

### 3. Balancing Factor (`03_Balancing_Factor.md`)
- Balance factor calculation
- Height maintenance
- When rebalancing is needed
- Balance factor update after operations
- Performance implications

### 4. AVL Insertion (`04_AVL_Insertion.md`)
- Insertion algorithm with rebalancing
- Step-by-step insertion process
- Balance factor updates
- Rotation triggers
- Complexity analysis

### 5. AVL Deletion (`05_AVL_Deletion.md`)
- Deletion algorithm with rebalancing
- Complex cases in AVL deletion
- Multiple rotations in single deletion
- Balance factor restoration
- Performance analysis

## Key Properties

### Balance Factor
For any node in AVL tree:
```
Balance Factor = Height(Left Subtree) - Height(Right Subtree)
```
Allowed values: -1, 0, 1

### Height Guarantee
For an AVL tree with n nodes:
- **Maximum Height**: ⌊1.44 × log₂(n + 2)⌋ - 2
- **Guaranteed O(log n)** operations

### Time Complexity
| Operation | Time Complexity |
|-----------|----------------|
| Search | O(log n) |
| Insertion | O(log n) |
| Deletion | O(log n) |
| Rotation | O(1) |

## Basic AVL Node Structure

```cpp
struct AVLNode {
    int data;
    AVLNode* left;
    AVLNode* right;
    int height;
    
    AVLNode(int value) : data(value), left(nullptr), right(nullptr), height(1) {}
};
```

## AVL Tree Class

```cpp
class AVLTree {
private:
    AVLNode* root;
    
    // Helper functions
    int height(AVLNode* node);
    int balanceFactor(AVLNode* node);
    AVLNode* rightRotate(AVLNode* y);
    AVLNode* leftRotate(AVLNode* x);
    AVLNode* insert(AVLNode* node, int key);
    AVLNode* deleteNode(AVLNode* root, int key);
    AVLNode* minValueNode(AVLNode* node);
    void inorder(AVLNode* root);
    AVLNode* balanceTree(AVLNode* node);
    
public:
    AVLTree() : root(nullptr) {}
    
    // Public interface
    void insert(int key) { root = insert(root, key); }
    void remove(int key) { root = deleteNode(root, key); }
    bool search(int key);
    void inorder() { inorder(root); }
    int getHeight() { return height(root); }
    bool isBalanced();
};
```

## Rotation Operations

### 1. Right Rotation (LL Case)
```cpp
AVLNode* AVLTree::rightRotate(AVLNode* y) {
    AVLNode* x = y->left;
    AVLNode* T2 = x->right;
    
    // Perform rotation
    x->right = y;
    y->left = T2;
    
    // Update heights
    y->height = std::max(height(y->left), height(y->right)) + 1;
    x->height = std::max(height(x->left), height(x->right)) + 1;
    
    return x; // New root
}
```

### 2. Left Rotation (RR Case)
```cpp
AVLNode* AVLTree::leftRotate(AVLNode* x) {
    AVLNode* y = x->right;
    AVLNode* T2 = y->left;
    
    // Perform rotation
    y->left = x;
    x->right = T2;
    
    // Update heights
    x->height = std::max(height(x->left), height(x->right)) + 1;
    y->height = std::max(height(y->left), height(y->right)) + 1;
    
    return y; // New root
}
```

## AVL Operations

### 1. Height and Balance Factor
```cpp
int AVLTree::height(AVLNode* node) {
    if (node == nullptr) return 0;
    return node->height;
}

int AVLTree::balanceFactor(AVLNode* node) {
    if (node == nullptr) return 0;
    return height(node->left) - height(node->right);
}
```

### 2. Tree Balancing
```cpp
AVLNode* AVLTree::balanceTree(AVLNode* node) {
    // Update height
    node->height = 1 + std::max(height(node->left), height(node->right));
    
    // Get balance factor
    int balance = balanceFactor(node);
    
    // Left Left Case
    if (balance > 1 && balanceFactor(node->left) >= 0) {
        return rightRotate(node);
    }
    
    // Right Right Case
    if (balance < -1 && balanceFactor(node->right) <= 0) {
        return leftRotate(node);
    }
    
    // Left Right Case
    if (balance > 1 && balanceFactor(node->left) < 0) {
        node->left = leftRotate(node->left);
        return rightRotate(node);
    }
    
    // Right Left Case
    if (balance < -1 && balanceFactor(node->right) > 0) {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }
    
    return node; // Balanced
}
```

### 3. AVL Insertion
```cpp
AVLNode* AVLTree::insert(AVLNode* node, int key) {
    // Standard BST insertion
    if (node == nullptr) {
        return new AVLNode(key);
    }
    
    if (key < node->data) {
        node->left = insert(node->left, key);
    } else if (key > node->data) {
        node->right = insert(node->right, key);
    } else {
        return node; // Duplicate keys not allowed
    }
    
    // Balance the tree
    return balanceTree(node);
}
```

### 4. AVL Deletion
```cpp
AVLNode* AVLTree::deleteNode(AVLNode* root, int key) {
    // Standard BST deletion
    if (root == nullptr) return root;
    
    if (key < root->data) {
        root->left = deleteNode(root->left, key);
    } else if (key > root->data) {
        root->right = deleteNode(root->right, key);
    } else {
        // Node with one child or no child
        if ((root->left == nullptr) || (root->right == nullptr)) {
            AVLNode* temp = root->left ? root->left : root->right;
            
            if (temp == nullptr) {
                temp = root;
                root = nullptr;
            } else {
                *root = *temp; // Copy the contents
            }
            delete temp;
        } else {
            // Node with two children
            AVLNode* temp = minValueNode(root->right);
            root->data = temp->data;
            root->right = deleteNode(root->right, temp->data);
        }
    }
    
    if (root == nullptr) return root;
    
    // Balance the tree
    return balanceTree(root);
}
```

## AVL vs Other Trees

### Comparison with BST
| Property | BST | AVL Tree |
|----------|-----|----------|
| Height | O(n) worst case | O(log n) guaranteed |
| Search | O(log n) avg, O(n) worst | O(log n) always |
| Insertion | O(log n) avg, O(n) worst | O(log n) always |
| Deletion | O(log n) avg, O(n) worst | O(log n) always |
| Memory | O(n) | O(n) |
| Rotations | None | O(1) per operation |

### Comparison with Red-Black Trees
| Property | AVL Tree | Red-Black Tree |
|----------|----------|----------------|
| Height | More strict (1.44 log n) | Less strict (2 log n) |
| Rotations | More rotations per operation | Fewer rotations |
| Search | Faster (shorter height) | Slightly slower |
| Insert/Delete | Slower (more rebalancing) | Faster |
| Use Case | Read-heavy operations | Write-heavy operations |

## Advanced AVL Operations

### 1. Range Queries
```cpp
std::vector<int> rangeQuery(AVLNode* root, int low, int high) {
    std::vector<int> result;
    rangeQueryHelper(root, low, high, result);
    return result;
}

void rangeQueryHelper(AVLNode* node, int low, int high, std::vector<int>& result) {
    if (node == nullptr) return;
    
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
```

### 2. Tree Validation
```cpp
bool AVLTree::isBalanced() {
    return isBalancedHelper(root);
}

bool AVLTree::isBalancedHelper(AVLNode* node) {
    if (node == nullptr) return true;
    
    int balance = balanceFactor(node);
    if (balance < -1 || balance > 1) return false;
    
    return isBalancedHelper(node->left) && isBalancedHelper(node->right);
}
```

## Performance Analysis

### Space Complexity
- **Space**: O(n) for storing nodes
- **Recursion Stack**: O(log n) due to balanced height

### Time Complexity Analysis
- **Search**: O(log n) - guaranteed by height balance
- **Insertion**: O(log n) - BST insertion + O(1) rotations
- **Deletion**: O(log n) - BST deletion + O(1) rotations
- **Rotations**: O(1) - constant time pointer updates

### Height Analysis
For an AVL tree with n nodes:
- **Minimum nodes for height h**: Fibonacci-like sequence
- **Maximum height**: ⌊1.44 × log₂(n + 2)⌋ - 2 ≈ 1.44 log₂n
- **Practical height**: Much closer to log₂n than worst case

## Common Applications

### 1. Database Indexing
- Secondary indexes in databases
- B-tree variants inspired by AVL balancing
- Fast lookup operations

### 2. Memory Management
- Dynamic memory allocation
- Free space management
- Garbage collection systems

### 3. File Systems
- Directory structures
- File allocation tables
- Index management

### 4. Network Routing
- Routing tables
- Network topology management
- Load balancing

## Best Practices

### 1. Implementation Tips
- Always update height after modifications
- Check balance factor after every operation
- Use recursive implementations for clarity
- Handle edge cases (empty tree, single node)

### 2. Performance Optimization
- Cache height values to avoid recalculation
- Use iterative versions for very deep trees
- Minimize memory allocations
- Consider memory pooling for frequent operations

### 3. Debugging
- Visualize tree structure during operations
- Track balance factor changes
- Verify AVL properties after each operation
- Use comprehensive test cases

## Common Pitfalls

1. **Height Updates**: Forgetting to update heights after rotations
2. **Balance Factor**: Incorrect calculation or update
3. **Rotation Logic**: Wrong rotation for given imbalance case
4. **Memory Management**: Memory leaks in node deletion
5. **Edge Cases**: Not handling empty tree or single node cases

## Summary

AVL trees provide guaranteed logarithmic performance for all basic operations through automatic balancing. While they require more complex implementation than standard BSTs, their performance guarantees make them ideal for applications where consistent performance is critical. The strict balance ensures efficient operations but may require more rotations than other self-balancing trees.
