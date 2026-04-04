# Binary Search Trees (BST)

## Overview
A Binary Search Tree (BST) is a binary tree data structure that maintains the BST property: for each node, all values in its left subtree are less than the node's value, and all values in its right subtree are greater than the node's value. This property enables efficient searching, insertion, and deletion operations.

## Topics Covered

### 1. BST Introduction (`01_BST_Introduction.md`)
- BST definition and properties
- BST invariants and rules
- Advantages and disadvantages
- Time complexity analysis
- Real-world applications

### 2. BST Insertion (`02_BST_Insertion.md`)
- Insertion algorithm and implementation
- Handling duplicates
- Recursive vs iterative approaches
- Edge cases and validation
- Performance considerations

### 3. BST Deletion (`03_BST_Deletion.md`)
- Three cases of node deletion
- Leaf node deletion
- Node with one child deletion
- Node with two children deletion
- Inorder successor/predecessor

### 4. BST Search (`04_BST_Search.md`)
- Search algorithm implementation
- Recursive and iterative search
- Range queries
- Floor and ceiling operations
- Search complexity analysis

### 5. BST Traversal (`05_BST_Traversal.md`)
- Inorder traversal (sorted output)
- Preorder traversal
- Postorder traversal
- Level order traversal
- Traversal applications

## Key Properties

### BST Property
For any node `N` in the tree:
- All values in `N`'s left subtree < `N`'s value
- All values in `N`'s right subtree > `N`'s value
- Both left and right subtrees are also BSTs

### Time Complexity
| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Search | O(log n) | O(n) |
| Insertion | O(log n) | O(n) |
| Deletion | O(log n) | O(n) |
| Traversal | O(n) | O(n) |

### Space Complexity
- **Space**: O(n) for storing nodes
- **Recursion Stack**: O(h) where h is tree height

## Basic BST Implementation

### Node Structure
```cpp
struct BSTNode {
    int data;
    BSTNode* left;
    BSTNode* right;
    
    BSTNode(int value) : data(value), left(nullptr), right(nullptr) {}
};
```

### BST Class
```cpp
class BinarySearchTree {
private:
    BSTNode* root;
    
    // Helper functions
    BSTNode* insert(BSTNode* node, int value);
    BSTNode* remove(BSTNode* node, int value);
    BSTNode* search(BSTNode* node, int value);
    BSTNode* findMin(BSTNode* node);
    BSTNode* findMax(BSTNode* node);
    void inorder(BSTNode* node);
    void destroyTree(BSTNode* node);
    
public:
    BinarySearchTree() : root(nullptr) {}
    ~BinarySearchTree() { destroyTree(root); }
    
    // Public interface
    void insert(int value) { root = insert(root, value); }
    void remove(int value) { root = remove(root, value); }
    bool search(int value) { return search(root, value) != nullptr; }
    void inorder() { inorder(root); }
    bool isEmpty() { return root == nullptr; }
};
```

## BST Operations

### 1. Insertion
```cpp
BSTNode* BinarySearchTree::insert(BSTNode* node, int value) {
    if (node == nullptr) {
        return new BSTNode(value);
    }
    
    if (value < node->data) {
        node->left = insert(node->left, value);
    } else if (value > node->data) {
        node->right = insert(node->right, value);
    }
    // If value == node->data, handle based on requirements
    
    return node;
}
```

### 2. Search
```cpp
BSTNode* BinarySearchTree::search(BSTNode* node, int value) {
    if (node == nullptr || node->data == value) {
        return node;
    }
    
    if (value < node->data) {
        return search(node->left, value);
    } else {
        return search(node->right, value);
    }
}
```

### 3. Deletion
```cpp
BSTNode* BinarySearchTree::remove(BSTNode* node, int value) {
    if (node == nullptr) return nullptr;
    
    if (value < node->data) {
        node->left = remove(node->left, value);
    } else if (value > node->data) {
        node->right = remove(node->right, value);
    } else {
        // Node to be deleted found
        
        // Case 1: No child
        if (node->left == nullptr && node->right == nullptr) {
            delete node;
            return nullptr;
        }
        
        // Case 2: One child
        if (node->left == nullptr) {
            BSTNode* temp = node->right;
            delete node;
            return temp;
        }
        if (node->right == nullptr) {
            BSTNode* temp = node->left;
            delete node;
            return temp;
        }
        
        // Case 3: Two children
        // Find inorder successor (smallest in right subtree)
        BSTNode* temp = findMin(node->right);
        node->data = temp->data;
        node->right = remove(node->right, temp->data);
    }
    
    return node;
}
```

## Advanced BST Operations

### 1. Range Queries
```cpp
class BSTRangeOperations {
public:
    // Find all values in range [low, high]
    static std::vector<int> rangeQuery(BSTNode* root, int low, int high) {
        std::vector<int> result;
        rangeQueryHelper(root, low, high, result);
        return result;
    }
    
    // Count values in range [low, high]
    static int countInRange(BSTNode* root, int low, int high) {
        if (root == nullptr) return 0;
        
        if (root->data < low) {
            return countInRange(root->right, low, high);
        } else if (root->data > high) {
            return countInRange(root->left, low, high);
        } else {
            return 1 + countInRange(root->left, low, high) + 
                   countInRange(root->right, low, high);
        }
    }
    
private:
    static void rangeQueryHelper(BSTNode* node, int low, int high, 
                                std::vector<int>& result) {
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
};
```

### 2. Floor and Ceiling Operations
```cpp
class BSTFloorCeiling {
public:
    // Find greatest value <= given value
    static int floor(BSTNode* root, int value) {
        int floorValue = INT_MIN;
        
        while (root != nullptr) {
            if (root->data == value) {
                return value;
            } else if (root->data < value) {
                floorValue = root->data;
                root = root->right;
            } else {
                root = root->left;
            }
        }
        
        return (floorValue == INT_MIN) ? -1 : floorValue;
    }
    
    // Find smallest value >= given value
    static int ceiling(BSTNode* root, int value) {
        int ceilingValue = INT_MAX;
        
        while (root != nullptr) {
            if (root->data == value) {
                return value;
            } else if (root->data > value) {
                ceilingValue = root->data;
                root = root->left;
            } else {
                root = root->right;
            }
        }
        
        return (ceilingValue == INT_MAX) ? -1 : ceilingValue;
    }
};
```

### 3. BST Validation
```cpp
class BSTValidation {
public:
    // Check if a binary tree is a valid BST
    static bool isValidBST(BSTNode* root) {
        return isValidBSTHelper(root, LONG_MIN, LONG_MAX);
    }
    
    // Check if tree is balanced
    static bool isBalanced(BSTNode* root) {
        return checkBalance(root).first;
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
    
    static std::pair<bool, int> checkBalance(BSTNode* node) {
        if (node == nullptr) return {true, -1};
        
        auto left = checkBalance(node->left);
        auto right = checkBalance(node->right);
        
        if (!left.first || !right.first) return {false, 0};
        if (abs(left.second - right.second) > 1) return {false, 0};
        
        return {true, std::max(left.second, right.second) + 1};
    }
};
```

## BST Variants and Optimizations

### 1. Iterative Implementations
```cpp
class BSTIterative {
public:
    // Iterative insertion
    static BSTNode* insertIterative(BSTNode* root, int value) {
        BSTNode* newNode = new BSTNode(value);
        
        if (root == nullptr) return newNode;
        
        BSTNode* current = root;
        BSTNode* parent = nullptr;
        
        while (current != nullptr) {
            parent = current;
            if (value < current->data) {
                current = current->left;
            } else if (value > current->data) {
                current = current->right;
            } else {
                delete newNode; // Handle duplicate as needed
                return root;
            }
        }
        
        if (value < parent->data) {
            parent->left = newNode;
        } else {
            parent->right = newNode;
        }
        
        return root;
    }
    
    // Iterative search
    static BSTNode* searchIterative(BSTNode* root, int value) {
        BSTNode* current = root;
        
        while (current != nullptr) {
            if (current->data == value) {
                return current;
            } else if (value < current->data) {
                current = current->left;
            } else {
                current = current->right;
            }
        }
        
        return nullptr;
    }
};
```

### 2. BST with Parent Pointers
```cpp
struct BSTNodeWithParent {
    int data;
    BSTNodeWithParent* left;
    BSTNodeWithParent* right;
    BSTNodeWithParent* parent;
    
    BSTNodeWithParent(int value) : data(value), left(nullptr), right(nullptr), parent(nullptr) {}
};

class BSTWithParent {
private:
    BSTNodeWithParent* root;
    
public:
    BSTWithParent() : root(nullptr) {}
    
    void insert(int value) {
        BSTNodeWithParent* newNode = new BSTNodeWithParent(value);
        
        if (root == nullptr) {
            root = newNode;
            return;
        }
        
        BSTNodeWithParent* current = root;
        BSTNodeWithParent* parent = nullptr;
        
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
        
        newNode->parent = parent;
        if (value < parent->data) {
            parent->left = newNode;
        } else {
            parent->right = newNode;
        }
    }
    
    // Find successor using parent pointers
    BSTNodeWithParent* findSuccessor(BSTNodeWithParent* node) {
        if (node == nullptr) return nullptr;
        
        // If right subtree exists, find minimum in right subtree
        if (node->right != nullptr) {
            return findMinimum(node->right);
        }
        
        // Otherwise, go up using parent pointers
        BSTNodeWithParent* current = node;
        BSTNodeWithParent* parent = node->parent;
        
        while (parent != nullptr && current == parent->right) {
            current = parent;
            parent = parent->parent;
        }
        
        return parent;
    }
    
private:
    BSTNodeWithParent* findMinimum(BSTNodeWithParent* node) {
        while (node->left != nullptr) {
            node = node->left;
        }
        return node;
    }
};
```

## BST Applications

### 1. Ordered Set Implementation
```cpp
class OrderedSet {
private:
    BSTNode* root;
    
public:
    OrderedSet() : root(nullptr) {}
    
    void insert(int value) {
        root = BSTIterative::insertIterative(root, value);
    }
    
    void erase(int value) {
        root = remove(root, value);
    }
    
    bool contains(int value) {
        return BSTIterative::searchIterative(root, value) != nullptr;
    }
    
    int lower_bound(int value) {
        return BSTFloorCeiling::ceiling(root, value);
    }
    
    int upper_bound(int value) {
        // Find smallest value > given value
        int result = INT_MAX;
        BSTNode* current = root;
        
        while (current != nullptr) {
            if (current->data > value) {
                result = current->data;
                current = current->left;
            } else {
                current = current->right;
            }
        }
        
        return (result == INT_MAX) ? -1 : result;
    }
    
    std::vector<int> getRange(int low, int high) {
        return BSTRangeOperations::rangeQuery(root, low, high);
    }
};
```

### 2. Dictionary Implementation
```cpp
template <typename K, typename V>
class BSTDictionary {
private:
    struct DictNode {
        K key;
        V value;
        DictNode* left;
        DictNode* right;
        
        DictNode(K k, V v) : key(k), value(v), left(nullptr), right(nullptr) {}
    };
    
    DictNode* root;
    
    DictNode* insert(DictNode* node, K key, V value) {
        if (node == nullptr) {
            return new DictNode(key, value);
        }
        
        if (key < node->key) {
            node->left = insert(node->left, key, value);
        } else if (key > node->key) {
            node->right = insert(node->right, key, value);
        } else {
            node->value = value; // Update existing key
        }
        
        return node;
    }
    
    V* search(DictNode* node, K key) {
        if (node == nullptr) return nullptr;
        
        if (key < node->key) {
            return search(node->left, key);
        } else if (key > node->key) {
            return search(node->right, key);
        } else {
            return &node->value;
        }
    }
    
public:
    BSTDictionary() : root(nullptr) {}
    
    void insert(K key, V value) {
        root = insert(root, key, value);
    }
    
    V* get(K key) {
        return search(root, key);
    }
    
    bool contains(K key) {
        return get(key) != nullptr;
    }
};
```

## Performance Analysis

### Height Analysis
- **Best Case**: Balanced tree, height = O(log n)
- **Worst Case**: Skewed tree, height = O(n)
- **Average Case**: Random insertions, height = O(log n)

### Comparison with Other Structures

| Structure | Search | Insert | Delete | Space |
|-----------|--------|--------|--------|-------|
| Array | O(n) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(1) | O(1) | O(n) |
| BST (avg) | O(log n) | O(log n) | O(log n) | O(n) |
| BST (worst) | O(n) | O(n) | O(n) | O(n) |
| Hash Table | O(1) | O(1) | O(1) | O(n) |

## Common Problems and Solutions

### 1. BST to Sorted Array
```cpp
std::vector<int> bstToSortedArray(BSTNode* root) {
    std::vector<int> result;
    inorderTraversal(root, result);
    return result;
}

void inorderTraversal(BSTNode* node, std::vector<int>& result) {
    if (node == nullptr) return;
    
    inorderTraversal(node->left, result);
    result.push_back(node->data);
    inorderTraversal(node->right, result);
}
```

### 2. Validate BST
```cpp
bool isValidBST(BSTNode* root) {
    return validateBST(root, nullptr, nullptr);
}

bool validateBST(BSTNode* node, BSTNode* minNode, BSTNode* maxNode) {
    if (node == nullptr) return true;
    
    if (minNode && node->data <= minNode->data) return false;
    if (maxNode && node->data >= maxNode->data) return false;
    
    return validateBST(node->left, minNode, node) &&
           validateBST(node->right, node, maxNode);
}
```

## Best Practices

1. **Handle Duplicates**: Decide on policy (ignore, count, or allow)
2. **Memory Management**: Properly delete nodes to avoid leaks
3. **Edge Cases**: Handle empty tree and single node cases
4. **Balancing**: Consider self-balancing trees for better performance
5. **Iterative vs Recursive**: Choose based on tree depth and stack limits

## Limitations and Solutions

### Limitations
1. **Worst-case Performance**: O(n) for skewed trees
2. **No Duplicate Handling**: Standard BST doesn't handle duplicates well
3. **Memory Overhead**: Pointer storage for each node
4. **Cache Performance**: Poor locality compared to arrays

### Solutions
1. **Self-Balancing Trees**: AVL, Red-Black trees
2. **Duplicate Handling**: Modify insertion logic
3. **Memory Optimization**: Use array representation for complete trees
4. **Balancing**: Periodic rebalancing or using balanced variants

## Summary

Binary Search Trees provide an excellent foundation for understanding tree data structures and enable efficient ordered data operations. While they have limitations in worst-case scenarios, they form the basis for more advanced balanced tree structures and are essential for many applications requiring ordered data management.
