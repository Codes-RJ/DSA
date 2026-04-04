# BST Insertion

## Overview
Insertion in a Binary Search Tree maintains the BST property while adding a new element. The algorithm finds the appropriate position for the new node based on its value and inserts it as a leaf node.

## Insertion Algorithm

### Basic Insertion Process
1. Start at the root
2. If tree is empty, new node becomes root
3. Compare new value with current node:
   - If less, go to left child
   - If greater, go to right child
   - If equal, handle based on duplicate policy
4. Repeat until reaching null position
5. Insert new node at that position

### Recursive Implementation
```cpp
class BSTInsertion {
private:
    BSTNode* insertRecursive(BSTNode* node, int value) {
        // Base case: reached null position
        if (node == nullptr) {
            return new BSTNode(value);
        }
        
        // Recursive case: go left or right
        if (value < node->data) {
            node->left = insertRecursive(node->left, value);
        } else if (value > node->data) {
            node->right = insertRecursive(node->right, value);
        } else {
            // Handle duplicate (ignore in this case)
            return node;
        }
        
        return node;
    }
    
public:
    void insert(int value) {
        root = insertRecursive(root, value);
    }
};
```

### Iterative Implementation
```cpp
class BSTInsertionIterative {
private:
    BSTNode* root;
    
public:
    void insert(int value) {
        BSTNode* newNode = new BSTNode(value);
        
        // Empty tree case
        if (root == nullptr) {
            root = newNode;
            return;
        }
        
        BSTNode* current = root;
        BSTNode* parent = nullptr;
        
        // Find insertion position
        while (current != nullptr) {
            parent = current;
            
            if (value < current->data) {
                current = current->left;
            } else if (value > current->data) {
                current = current->right;
            } else {
                // Duplicate found - handle based on policy
                delete newNode; // Clean up
                return;
            }
        }
        
        // Insert new node
        if (value < parent->data) {
            parent->left = newNode;
        } else {
            parent->right = newNode;
        }
    }
};
```

## Duplicate Handling Strategies

### 1. Ignore Duplicates
```cpp
class BSTIgnoreDuplicates {
public:
    BSTNode* insert(BSTNode* node, int value) {
        if (node == nullptr) {
            return new BSTNode(value);
        }
        
        if (value < node->data) {
            node->left = insert(node->left, value);
        } else if (value > node->data) {
            node->right = insert(node->right, value);
        }
        // If equal, ignore (do nothing)
        
        return node;
    }
};
```

### 2. Count Duplicates
```cpp
struct BSTNodeWithCount {
    int data;
    int count;
    BSTNodeWithCount* left;
    BSTNodeWithCount* right;
    
    BSTNodeWithCount(int value) : data(value), count(1), left(nullptr), right(nullptr) {}
};

class BSTWithCount {
public:
    BSTNodeWithCount* insert(BSTNodeWithCount* node, int value) {
        if (node == nullptr) {
            return new BSTNodeWithCount(value);
        }
        
        if (value < node->data) {
            node->left = insert(node->left, value);
        } else if (value > node->data) {
            node->right = insert(node->right, value);
        } else {
            node->count++; // Increment count for duplicate
        }
        
        return node;
    }
};
```

### 3. Allow Duplicates (Left or Right Bias)
```cpp
class BSTAllowDuplicates {
private:
    bool insertLeft; // Policy: insert duplicates to left or right
    
public:
    BSTNode* insert(BSTNode* node, int value) {
        if (node == nullptr) {
            return new BSTNode(value);
        }
        
        if (value < node->data) {
            node->left = insert(node->left, value);
        } else if (value > node->data) {
            node->right = insert(node->right, value);
        } else {
            // Equal - insert based on policy
            if (insertLeft) {
                node->left = insert(node->left, value);
            } else {
                node->right = insert(node->right, value);
            }
        }
        
        return node;
    }
};
```

## Special Insertion Cases

### 1. Bulk Insertion
```cpp
class BSTBulkInsertion {
public:
    // Insert from array (maintains BST property)
    void insertFromArray(const std::vector<int>& arr) {
        for (int value : arr) {
            insert(value);
        }
    }
    
    // Insert to create balanced BST from sorted array
    BSTNode* insertFromSorted(const std::vector<int>& sorted, int start, int end) {
        if (start > end) return nullptr;
        
        int mid = start + (end - start) / 2;
        BSTNode* root = new BSTNode(sorted[mid]);
        
        root->left = insertFromSorted(sorted, start, mid - 1);
        root->right = insertFromSorted(sorted, mid + 1, end);
        
        return root;
    }
    
    void createBalancedFromSorted(const std::vector<int>& sorted) {
        root = insertFromSorted(sorted, 0, sorted.size() - 1);
    }
};
```

### 2. Insertion with Height Tracking
```cpp
struct BSTNodeWithHeight {
    int data;
    int height;
    BSTNodeWithHeight* left;
    BSTNodeWithHeight* right;
    
    BSTNodeWithHeight(int value) : data(value), height(1), left(nullptr), right(nullptr) {}
};

class BSTWithHeight {
private:
    int getHeight(BSTNodeWithHeight* node) {
        return node ? node->height : 0;
    }
    
    void updateHeight(BSTNodeWithHeight* node) {
        if (node) {
            node->height = 1 + std::max(getHeight(node->left), getHeight(node->right));
        }
    }
    
public:
    BSTNodeWithHeight* insert(BSTNodeWithHeight* node, int value) {
        if (node == nullptr) {
            return new BSTNodeWithHeight(value);
        }
        
        if (value < node->data) {
            node->left = insert(node->left, value);
        } else if (value > node->data) {
            node->right = insert(node->right, value);
        }
        
        updateHeight(node);
        return node;
    }
};
```

### 3. Insertion with Parent Pointers
```cpp
class BSTWithParentPointers {
private:
    struct Node {
        int data;
        Node* left;
        Node* right;
        Node* parent;
        
        Node(int value) : data(value), left(nullptr), right(nullptr), parent(nullptr) {}
    };
    
    Node* root;
    
public:
    void insert(int value) {
        Node* newNode = new Node(value);
        
        if (root == nullptr) {
            root = newNode;
            return;
        }
        
        Node* current = root;
        Node* parent = nullptr;
        
        while (current != nullptr) {
            parent = current;
            
            if (value < current->data) {
                current = current->left;
            } else if (value > current->data) {
                current = current->right;
            } else {
                delete newNode; // Handle duplicate
                return;
            }
        }
        
        // Set parent pointer
        newNode->parent = parent;
        
        // Link to parent
        if (value < parent->data) {
            parent->left = newNode;
        } else {
            parent->right = newNode;
        }
    }
};
```

## Performance Analysis

### Time Complexity
| Case | Time Complexity | Description |
|------|-----------------|-------------|
| Best | O(log n) | Balanced tree, insert at leaf |
| Average | O(log n) | Random insertions |
| Worst | O(n) | Skewed tree, insert at end |

### Space Complexity
- **Recursive**: O(h) call stack space
- **Iterative**: O(1) auxiliary space
- **Overall**: O(n) for storing nodes

### Factors Affecting Performance
1. **Tree Balance**: More balanced = better performance
2. **Insertion Order**: Sorted order creates worst case
3. **Duplicate Handling**: Affects tree structure
4. **Node Size**: Larger nodes = more memory overhead

## Insertion Order Impact

### Best Case (Balanced Tree)
```cpp
// Insertion order that creates balanced tree
std::vector<int> balancedOrder = {50, 30, 70, 20, 40, 60, 80};
// Results in tree with height ~log n
```

### Worst Case (Skewed Tree)
```cpp
// Insertion order that creates skewed tree
std::vector<int> skewedOrder = {10, 20, 30, 40, 50, 60, 70};
// Results in tree with height = n
```

### Random Order
```cpp
// Random insertion typically creates reasonably balanced tree
std::vector<int> randomOrder = {45, 23, 67, 12, 34, 56, 78, 89, 1};
// Expected height: O(log n)
```

## Advanced Insertion Techniques

### 1. Insertion with Rebalancing
```cpp
class BSTWithRebalancing {
private:
    BSTNode* insertAndBalance(BSTNode* node, int value) {
        node = insert(node, value);
        
        // Check if rebalancing is needed
        if (isUnbalanced(node)) {
            node = rebalance(node);
        }
        
        return node;
    }
    
    bool isUnbalanced(BSTNode* node) {
        int leftHeight = height(node->left);
        int rightHeight = height(node->right);
        return abs(leftHeight - rightHeight) > 1;
    }
    
    BSTNode* rebalance(BSTNode* node) {
        // Simple rebalancing: rebuild from sorted array
        std::vector<int> values;
        inorderTraversal(node, values);
        return buildBalanced(values, 0, values.size() - 1);
    }
};
```

### 2. Insertion with Statistics
```cpp
class BSTWithStats {
private:
    struct StatsNode {
        int data;
        int size; // Size of subtree
        int height;
        StatsNode* left;
        StatsNode* right;
        
        StatsNode(int value) : data(value), size(1), height(1), left(nullptr), right(nullptr) {}
    };
    
    void updateStats(StatsNode* node) {
        if (node) {
            node->size = 1 + getSize(node->left) + getSize(node->right);
            node->height = 1 + std::max(getHeight(node->left), getHeight(node->right));
        }
    }
    
public:
    StatsNode* insert(StatsNode* node, int value) {
        if (node == nullptr) {
            return new StatsNode(value);
        }
        
        if (value < node->data) {
            node->left = insert(node->left, value);
        } else if (value > node->data) {
            node->right = insert(node->right, value);
        }
        
        updateStats(node);
        return node;
    }
    
    int getRank(StatsNode* root, int value) {
        // Find rank (number of elements <= value)
        int rank = 0;
        StatsNode* current = root;
        
        while (current != nullptr) {
            if (value < current->data) {
                current = current->left;
            } else {
                rank += 1 + getSize(current->left);
                current = current->right;
            }
        }
        
        return rank;
    }
};
```

## Common Insertion Patterns

### 1. Sequential Insertion
```cpp
class SequentialInsertion {
public:
    void insertSequential(int start, int end) {
        for (int i = start; i <= end; i++) {
            insert(i);
        }
    }
    
    void insertSequentialReverse(int start, int end) {
        for (int i = end; i >= start; i--) {
            insert(i);
        }
    }
};
```

### 2. Range Insertion
```cpp
class RangeInsertion {
public:
    void insertRange(int min, int max, int step = 1) {
        for (int i = min; i <= max; i += step) {
            insert(i);
        }
    }
    
    void insertRandomRange(int count, int min, int max) {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<> dis(min, max);
        
        for (int i = 0; i < count; i++) {
            insert(dis(gen));
        }
    }
};
```

## Error Handling and Validation

### 1. Input Validation
```cpp
class SafeBSTInsertion {
public:
    bool insert(int value) {
        try {
            // Validate input
            if (!isValidValue(value)) {
                return false;
            }
            
            root = insertRecursive(root, value);
            return true;
        } catch (const std::exception& e) {
            // Handle memory allocation failure
            std::cerr << "Insertion failed: " << e.what() << std::endl;
            return false;
        }
    }
    
private:
    bool isValidValue(int value) {
        // Add any validation logic
        return true; // For now, accept all integers
    }
};
```

### 2. Memory Management
```cpp
class MemorySafeBST {
private:
    std::vector<BSTNode*> allocatedNodes;
    
public:
    ~MemorySafeBST() {
        for (BSTNode* node : allocatedNodes) {
            delete node;
        }
    }
    
    void insert(int value) {
        BSTNode* newNode = new BSTNode(value);
        allocatedNodes.push_back(newNode);
        
        // Insert into tree...
    }
};
```

## Best Practices

### 1. Implementation Guidelines
- Choose appropriate duplicate handling strategy
- Consider iterative version for deep trees
- Validate input before insertion
- Handle memory allocation failures
- Maintain tree invariants

### 2. Performance Optimization
- Use bulk insertion for sorted data
- Consider rebalancing for skewed trees
- Optimize for common insertion patterns
- Cache frequently accessed nodes
- Use memory pools for frequent operations

### 3. Testing Strategies
- Test with various insertion orders
- Verify BST property after insertion
- Test edge cases (empty tree, duplicates)
- Measure performance with large datasets
- Test memory usage and leaks

## Summary

BST insertion is a fundamental operation that maintains the ordered property of the tree. The choice between recursive and iterative implementations, duplicate handling strategies, and performance optimizations depends on the specific use case. Understanding insertion patterns and their impact on tree structure is crucial for maintaining efficient BST operations.
