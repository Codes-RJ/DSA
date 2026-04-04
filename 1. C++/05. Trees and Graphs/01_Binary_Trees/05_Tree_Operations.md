# Tree Operations and Algorithms

## Introduction
This section covers fundamental tree operations including insertion, deletion, searching, and various manipulation algorithms. Each operation is analyzed for time and space complexity.

## Search Operations

### 1. Depth-First Search (DFS)
```cpp
class TreeSearch {
public:
    // Recursive DFS
    static TreeNode* dfsRecursive(TreeNode* root, int value) {
        if (root == nullptr) return nullptr;
        if (root->data == value) return root;
        
        TreeNode* leftResult = dfsRecursive(root->left, value);
        if (leftResult != nullptr) return leftResult;
        
        return dfsRecursive(root->right, value);
    }
    
    // Iterative DFS using stack
    static TreeNode* dfsIterative(TreeNode* root, int value) {
        if (root == nullptr) return nullptr;
        
        std::stack<TreeNode*> s;
        s.push(root);
        
        while (!s.empty()) {
            TreeNode* current = s.top();
            s.pop();
            
            if (current->data == value) return current;
            
            // Push right first so left is processed first
            if (current->right) s.push(current->right);
            if (current->left) s.push(current->left);
        }
        
        return nullptr;
    }
    
    // Find minimum value in tree
    static TreeNode* findMin(TreeNode* root) {
        if (root == nullptr) return nullptr;
        
        TreeNode* current = root;
        while (current->left != nullptr) {
            current = current->left;
        }
        return current;
    }
    
    // Find maximum value in tree
    static TreeNode* findMax(TreeNode* root) {
        if (root == nullptr) return nullptr;
        
        TreeNode* current = root;
        while (current->right != nullptr) {
            current = current->right;
        }
        return current;
    }
};
```

### 2. Breadth-First Search (BFS)
```cpp
class BreadthFirstSearch {
public:
    // Find value using BFS
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
    
    // Find all nodes at given level
    static std::vector<TreeNode*> getNodesAtLevel(TreeNode* root, int level) {
        std::vector<TreeNode*> result;
        if (root == nullptr || level < 0) return result;
        
        std::queue<std::pair<TreeNode*, int>> q;
        q.push({root, 0});
        
        while (!q.empty()) {
            auto current = q.front();
            q.pop();
            
            if (current.second == level) {
                result.push_back(current.first);
            } else if (current.second < level) {
                if (current.first->left) {
                    q.push({current.first->left, current.second + 1});
                }
                if (current.first->right) {
                    q.push({current.first->right, current.second + 1});
                }
            }
        }
        
        return result;
    }
};
```

## Insertion Operations

### 1. Level Order Insertion
```cpp
class TreeInsertion {
public:
    // Insert at first available position (complete tree approach)
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
    
    // Insert as left child of specific node
    static bool insertLeft(TreeNode* parent, int value) {
        if (parent == nullptr || parent->left != nullptr) {
            return false;
        }
        parent->left = new TreeNode(value);
        return true;
    }
    
    // Insert as right child of specific node
    static bool insertRight(TreeNode* parent, int value) {
        if (parent == nullptr || parent->right != nullptr) {
            return false;
        }
        parent->right = new TreeNode(value);
        return true;
    }
    
    // Insert at specific position using BFS
    static bool insertAtPosition(TreeNode*& root, int parentValue, int value, bool isLeft) {
        TreeNode* parent = TreeSearch::dfsRecursive(root, parentValue);
        if (parent == nullptr) return false;
        
        if (isLeft) {
            return insertLeft(parent, value);
        } else {
            return insertRight(parent, value);
        }
    }
};
```

### 2. Custom Insertion Strategies
```cpp
class CustomInsertion {
public:
    // Insert to maintain minimum height
    static void insertMinHeight(TreeNode*& root, int value) {
        root = insertMinHeightHelper(root, value);
    }
    
    // Insert to create complete binary tree from array
    static TreeNode* createCompleteFromArray(const std::vector<int>& arr) {
        if (arr.empty()) return nullptr;
        
        return createCompleteHelper(arr, 0);
    }
    
private:
    static TreeNode* insertMinHeightHelper(TreeNode* node, int value) {
        if (node == nullptr) {
            return new TreeNode(value);
        }
        
        if (height(node->left) <= height(node->right)) {
            node->left = insertMinHeightHelper(node->left, value);
        } else {
            node->right = insertMinHeightHelper(node->right, value);
        }
        
        return node;
    }
    
    static TreeNode* createCompleteHelper(const std::vector<int>& arr, int index) {
        if (index >= arr.size()) return nullptr;
        
        TreeNode* root = new TreeNode(arr[index]);
        root->left = createCompleteHelper(arr, 2 * index + 1);
        root->right = createCompleteHelper(arr, 2 * index + 2);
        
        return root;
    }
    
    static int height(TreeNode* node) {
        if (node == nullptr) return -1;
        return 1 + std::max(height(node->left), height(node->right));
    }
};
```

## Deletion Operations

### 1. Delete Specific Node
```cpp
class TreeDeletion {
public:
    // Delete node with given value
    static bool deleteNode(TreeNode*& root, int value) {
        return deleteNodeHelper(root, value);
    }
    
    // Delete deepest node
    static TreeNode* deleteDeepest(TreeNode* root) {
        if (root == nullptr) return nullptr;
        
        TreeNode* deepest = nullptr;
        TreeNode* parent = nullptr;
        
        std::queue<std::pair<TreeNode*, TreeNode*>> q;
        q.push({root, nullptr});
        
        while (!q.empty()) {
            auto current = q.front();
            q.pop();
            
            deepest = current.first;
            parent = current.second;
            
            if (current.first->left) {
                q.push({current.first->left, current.first});
            }
            if (current.first->right) {
                q.push({current.first->right, current.first});
            }
        }
        
        // Remove deepest node from its parent
        if (parent != nullptr) {
            if (parent->left == deepest) {
                parent->left = nullptr;
            } else {
                parent->right = nullptr;
            }
        }
        
        return deepest;
    }
    
    // Delete node by replacing with deepest node
    static bool deleteByDeepestReplacement(TreeNode*& root, int value) {
        if (root == nullptr) return false;
        
        // Find node to delete
        TreeNode* nodeToDelete = TreeSearch::dfsRecursive(root, value);
        if (nodeToDelete == nullptr) return false;
        
        // Find deepest node
        TreeNode* deepest = findDeepestNode(root);
        
        // Replace values
        nodeToDelete->data = deepest->data;
        
        // Delete deepest node
        return deleteDeepestNode(root, deepest);
    }
    
private:
    static bool deleteNodeHelper(TreeNode*& node, int value) {
        if (node == nullptr) return false;
        
        if (node->data == value) {
            // Node found, delete it
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
                // Node has two children, replace with inorder successor
                TreeNode* successor = findInorderSuccessor(node->right);
                node->data = successor->data;
                return deleteNodeHelper(node->right, successor->data);
            }
            return true;
        }
        
        return deleteNodeHelper(node->left, value) || 
               deleteNodeHelper(node->right, value);
    }
    
    static TreeNode* findInorderSuccessor(TreeNode* node) {
        while (node->left != nullptr) {
            node = node->left;
        }
        return node;
    }
    
    static TreeNode* findDeepestNode(TreeNode* root) {
        if (root == nullptr) return nullptr;
        
        std::queue<TreeNode*> q;
        q.push(root);
        TreeNode* deepest = nullptr;
        
        while (!q.empty()) {
            deepest = q.front();
            q.pop();
            
            if (deepest->left) q.push(deepest->left);
            if (deepest->right) q.push(deepest->right);
        }
        
        return deepest;
    }
    
    static bool deleteDeepestNode(TreeNode* root, TreeNode* target) {
        if (root == nullptr || target == nullptr) return false;
        
        if (root == target) {
            delete root;
            return true;
        }
        
        std::queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            TreeNode* current = q.front();
            q.pop();
            
            if (current->left == target) {
                delete current->left;
                current->left = nullptr;
                return true;
            }
            if (current->right == target) {
                delete current->right;
                current->right = nullptr;
                return true;
            }
            
            if (current->left) q.push(current->left);
            if (current->right) q.push(current->right);
        }
        
        return false;
    }
};
```

## Tree Modification Operations

### 1. Tree Pruning
```cpp
class TreePruning {
public:
    // Remove all nodes with values less than given threshold
    static TreeNode* pruneLessThan(TreeNode* root, int threshold) {
        if (root == nullptr) return nullptr;
        
        root->left = pruneLessThan(root->left, threshold);
        root->right = pruneLessThan(root->right, threshold);
        
        if (root->data < threshold && root->left == nullptr && root->right == nullptr) {
            delete root;
            return nullptr;
        }
        
        return root;
    }
    
    // Remove leaf nodes
    static TreeNode* removeLeaves(TreeNode* root) {
        if (root == nullptr) return nullptr;
        
        if (root->left == nullptr && root->right == nullptr) {
            delete root;
            return nullptr;
        }
        
        root->left = removeLeaves(root->left);
        root->right = removeLeaves(root->right);
        
        return root;
    }
    
    // Remove nodes at odd levels
    static TreeNode* removeOddLevels(TreeNode* root) {
        return removeOddLevelsHelper(root, 0);
    }
    
private:
    static TreeNode* removeOddLevelsHelper(TreeNode* node, int level) {
        if (node == nullptr) return nullptr;
        
        if (level % 2 == 1) {
            // Remove this node and return its children
            TreeNode* leftChild = removeOddLevelsHelper(node->left, level + 1);
            TreeNode* rightChild = removeOddLevelsHelper(node->right, level + 1);
            delete node;
            
            // For odd level, we need to merge children somehow
            // This is a simplified approach - you might want different logic
            return leftChild ? leftChild : rightChild;
        }
        
        node->left = removeOddLevelsHelper(node->left, level + 1);
        node->right = removeOddLevelsHelper(node->right, level + 1);
        
        return node;
    }
};
```

### 2. Tree Transformation
```cpp
class TreeTransformation {
public:
    // Mirror tree (left becomes right and vice versa)
    static TreeNode* mirrorTree(TreeNode* root) {
        if (root == nullptr) return nullptr;
        
        // Swap left and right children
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;
        
        // Recursively mirror subtrees
        mirrorTree(root->left);
        mirrorTree(root->right);
        
        return root;
    }
    
    // Increment all node values by given amount
    static void incrementValues(TreeNode* root, int increment) {
        if (root == nullptr) return;
        
        root->data += increment;
        incrementValues(root->left, increment);
        incrementValues(root->right, increment);
    }
    
    // Convert tree to its sum tree (each node contains sum of its subtree)
    static int convertToSumTree(TreeNode* root) {
        if (root == nullptr) return 0;
        
        int oldValue = root->data;
        
        root->data = convertToSumTree(root->left) + convertToSumTree(root->right);
        
        return root->data + oldValue;
    }
    
    // Convert to double tree (duplicate each node)
    static void convertToDoubleTree(TreeNode* root) {
        if (root == nullptr) return;
        
        convertToDoubleTree(root->left);
        convertToDoubleTree(root->right);
        
        // Duplicate current node as left child
        TreeNode* duplicate = new TreeNode(root->data);
        duplicate->left = root->left;
        root->left = duplicate;
    }
};
```

## Tree Analysis Operations

### 1. Path Operations
```cpp
class PathOperations {
public:
    // Find root to leaf paths
    static std::vector<std::vector<int>> findAllRootToLeafPaths(TreeNode* root) {
        std::vector<std::vector<int>> result;
        std::vector<int> currentPath;
        
        findAllPathsHelper(root, currentPath, result);
        
        return result;
    }
    
    // Find path from root to given node
    static std::vector<int> findPathToNode(TreeNode* root, int value) {
        std::vector<int> path;
        findPathHelper(root, value, path);
        return path;
    }
    
    // Check if path exists with given sum
    static bool hasPathWithSum(TreeNode* root, int sum) {
        if (root == nullptr) return sum == 0;
        
        return hasPathWithSum(root->left, sum - root->data) ||
               hasPathWithSum(root->right, sum - root->data);
    }
    
    // Find maximum path sum
    static int maxPathSum(TreeNode* root) {
        int result = INT_MIN;
        maxPathSumHelper(root, result);
        return result;
    }
    
private:
    static void findAllPathsHelper(TreeNode* node, std::vector<int>& currentPath, 
                                  std::vector<std::vector<int>>& result) {
        if (node == nullptr) return;
        
        currentPath.push_back(node->data);
        
        if (node->left == nullptr && node->right == nullptr) {
            result.push_back(currentPath);
        } else {
            findAllPathsHelper(node->left, currentPath, result);
            findAllPathsHelper(node->right, currentPath, result);
        }
        
        currentPath.pop_back();
    }
    
    static bool findPathHelper(TreeNode* node, int value, std::vector<int>& path) {
        if (node == nullptr) return false;
        
        path.push_back(node->data);
        
        if (node->data == value) return true;
        
        if (findPathHelper(node->left, value, path) || 
            findPathHelper(node->right, value, path)) {
            return true;
        }
        
        path.pop_back();
        return false;
    }
    
    static int maxPathSumHelper(TreeNode* node, int& result) {
        if (node == nullptr) return 0;
        
        int left = std::max(0, maxPathSumHelper(node->left, result));
        int right = std::max(0, maxPathSumHelper(node->right, result));
        
        result = std::max(result, left + right + node->data);
        
        return std::max(left, right) + node->data;
    }
};
```

### 2. Tree Comparison
```cpp
class TreeComparison {
public:
    // Check if two trees are identical
    static bool areIdentical(TreeNode* root1, TreeNode* root2) {
        if (root1 == nullptr && root2 == nullptr) return true;
        if (root1 == nullptr || root2 == nullptr) return false;
        
        return (root1->data == root2->data) &&
               areIdentical(root1->left, root2->left) &&
               areIdentical(root1->right, root2->right);
    }
    
    // Check if two trees are mirrors
    static bool areMirrors(TreeNode* root1, TreeNode* root2) {
        if (root1 == nullptr && root2 == nullptr) return true;
        if (root1 == nullptr || root2 == nullptr) return false;
        
        return (root1->data == root2->data) &&
               areMirrors(root1->left, root2->right) &&
               areMirrors(root1->right, root2->left);
    }
    
    // Check if tree2 is subtree of tree1
    static bool isSubtree(TreeNode* mainTree, TreeNode* subTree) {
        if (subTree == nullptr) return true;
        if (mainTree == nullptr) return false;
        
        if (areIdentical(mainTree, subTree)) return true;
        
        return isSubtree(mainTree->left, subTree) || 
               isSubtree(mainTree->right, subTree);
    }
};
```

## Advanced Operations

### 1. Tree Serialization/Deserialization
```cpp
class TreeSerialization {
public:
    // Serialize tree to string (preorder with null markers)
    static std::string serialize(TreeNode* root) {
        std::string result;
        serializeHelper(root, result);
        return result;
    }
    
    // Deserialize tree from string
    static TreeNode* deserialize(const std::string& data) {
        std::stringstream ss(data);
        return deserializeHelper(ss);
    }
    
    // Serialize to vector (level order)
    static std::vector<int> serializeToVector(TreeNode* root) {
        std::vector<int> result;
        if (root == nullptr) return result;
        
        std::queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            TreeNode* current = q.front();
            q.pop();
            
            if (current != nullptr) {
                result.push_back(current->data);
                q.push(current->left);
                q.push(current->right);
            } else {
                result.push_back(INT_MIN); // Use INT_MIN as null marker
            }
        }
        
        return result;
    }
    
private:
    static void serializeHelper(TreeNode* node, std::string& result) {
        if (node == nullptr) {
            result += "null,";
            return;
        }
        
        result += std::to_string(node->data) + ",";
        serializeHelper(node->left, result);
        serializeHelper(node->right, result);
    }
    
    static TreeNode* deserializeHelper(std::stringstream& ss) {
        std::string val;
        std::getline(ss, val, ',');
        
        if (val == "null" || val.empty()) {
            return nullptr;
        }
        
        TreeNode* node = new TreeNode(std::stoi(val));
        node->left = deserializeHelper(ss);
        node->right = deserializeHelper(ss);
        
        return node;
    }
};
```

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Search (DFS) | O(n) | O(h) |
| Search (BFS) | O(n) | O(w) |
| Insert (Level Order) | O(n) | O(w) |
| Delete (Specific Node) | O(n) | O(h) |
| Mirror Tree | O(n) | O(h) |
| Find Paths | O(n) | O(h) |
| Serialize | O(n) | O(h) |
| Deserialize | O(n) | O(h) |

Where:
- n = number of nodes
- h = height of tree
- w = maximum width of tree

## Best Practices

1. **Always handle nullptr cases** - Check for null before dereferencing
2. **Use recursion carefully** - Deep trees can cause stack overflow
3. **Memory management** - Properly delete nodes to avoid leaks
4. **Iterative alternatives** - Consider stack/queue based implementations for deep trees
5. **Input validation** - Validate parameters before operations

## Summary

These tree operations form the foundation for tree manipulation and are essential building blocks for more complex tree algorithms and data structures. Understanding these operations is crucial before moving to specialized tree types like BSTs and AVL trees.
