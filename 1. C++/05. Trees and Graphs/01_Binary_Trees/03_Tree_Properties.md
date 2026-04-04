# Tree Properties and Mathematical Relationships

## Introduction
Understanding tree properties is crucial for analyzing tree algorithms and choosing appropriate tree structures. This section covers the mathematical properties, relationships, and characteristics of binary trees.

## Fundamental Properties

### Height and Depth Definitions
- **Height of Node**: Number of edges on longest path from node to leaf
- **Depth of Node**: Number of edges from root to node
- **Level of Node**: Depth + 1 (root is at level 1)
- **Height of Tree**: Height of root node

### Basic Relationships
```
Height of tree = Maximum height of any node
Depth of root = 0
Height of leaf node = 0
Level = Depth + 1
```

## Mathematical Properties of Binary Trees

### 1. Maximum Number of Nodes

#### At Each Level
- Maximum nodes at level `i`: `2^(i-1)`
- Where level starts from 1 (root is level 1)

```cpp
// Function to calculate maximum nodes at given level
int maxNodesAtLevel(int level) {
    if (level < 1) return 0;
    return (1 << (level - 1));  // 2^(level-1)
}
```

#### In Complete Tree of Height h
- Maximum nodes: `2^(h+1) - 1`
- Where height is number of edges from root to deepest leaf

```cpp
// Function to calculate maximum nodes in tree of given height
int maxNodesInTree(int height) {
    if (height < 0) return 0;
    return (1 << (height + 1)) - 1;  // 2^(height+1) - 1
}
```

### 2. Minimum Height for Given Nodes

For a binary tree with `n` nodes, minimum height is:
```
h_min = ⌊log₂(n+1)⌋ - 1
```

```cpp
// Function to calculate minimum height for given number of nodes
int minHeightForNodes(int n) {
    if (n <= 0) return -1;
    return floor(log2(n + 1)) - 1;
}
```

### 3. Minimum Nodes for Given Height

For a binary tree of height `h`, minimum nodes is:
```
n_min = h + 1
```

```cpp
// Function to calculate minimum nodes for given height
int minNodesForHeight(int height) {
    if (height < 0) return 0;
    return height + 1;
}
```

## Properties of Specific Tree Types

### Full Binary Trees
Every node has either 0 or 2 children.

#### Properties:
- Number of leaf nodes = Number of internal nodes + 1
- Total nodes = 2 × leaf nodes - 1
- Total nodes = 2 × internal nodes + 1

```cpp
class FullBinaryTreeProperties {
public:
    static int countLeaves(TreeNode* root) {
        if (root == nullptr) return 0;
        if (root->left == nullptr && root->right == nullptr) return 1;
        return countLeaves(root->left) + countLeaves(root->right);
    }
    
    static int countInternalNodes(TreeNode* root) {
        if (root == nullptr || (root->left == nullptr && root->right == nullptr)) {
            return 0;
        }
        return 1 + countInternalNodes(root->left) + countInternalNodes(root->right);
    }
    
    static bool isFullBinaryTree(TreeNode* root) {
        if (root == nullptr) return true;
        if (root->left == nullptr && root->right == nullptr) return true;
        if (root->left != nullptr && root->right != nullptr) {
            return isFullBinaryTree(root->left) && isFullBinaryTree(root->right);
        }
        return false;  // Only one child
    }
};
```

### Complete Binary Trees
All levels except possibly the last are completely filled, and all nodes are as far left as possible.

#### Properties:
- Can be efficiently represented in arrays
- Parent-child relationships follow simple index formulas
- No gaps in the array representation

```cpp
class CompleteBinaryTreeProperties {
private:
    std::vector<int> tree;
    
public:
    // Index relationships (0-based indexing)
    int parent(int i) { return (i > 0) ? (i - 1) / 2 : -1; }
    int leftChild(int i) { return 2 * i + 1; }
    int rightChild(int i) { return 2 * i + 2; }
    
    bool isComplete(TreeNode* root) {
        if (root == nullptr) return true;
        
        std::queue<TreeNode*> q;
        q.push(root);
        bool flag = false;  // Flag to mark non-full node seen
        
        while (!q.empty()) {
            TreeNode* current = q.front();
            q.pop();
            
            if (current->left) {
                if (flag) return false;  // Non-full node seen before
                q.push(current->left);
            } else {
                flag = true;  // Mark non-full node
            }
            
            if (current->right) {
                if (flag) return false;  // Non-full node seen before
                q.push(current->right);
            } else {
                flag = true;  // Mark non-full node
            }
        }
        
        return true;
    }
};
```

### Perfect Binary Trees
All internal nodes have 2 children and all leaves are at the same level.

#### Properties:
- Number of nodes = `2^(h+1) - 1`
- Number of leaves = `2^h`
- Number of internal nodes = `2^h - 1`

```cpp
class PerfectBinaryTreeProperties {
public:
    static bool isPerfectBinaryTree(TreeNode* root) {
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

## Tree Balance Properties

### Balanced Binary Tree
A tree is balanced if for every node, the height difference between left and right subtrees is at most 1.

```cpp
class BalancedTreeProperties {
public:
    static bool isBalanced(TreeNode* root) {
        return checkBalance(root).first;
    }
    
private:
    static std::pair<bool, int> checkBalance(TreeNode* node) {
        if (node == nullptr) {
            return {true, -1};  // height of empty tree is -1
        }
        
        auto left = checkBalance(node->left);
        auto right = checkBalance(node->right);
        
        if (!left.first || !right.first) {
            return {false, 0};
        }
        
        if (abs(left.second - right.second) > 1) {
            return {false, 0};
        }
        
        return {true, std::max(left.second, right.second) + 1};
    }
};
```

## Tree Traversal Properties

### Traversal Order Properties

#### Inorder Traversal (Left → Root → Right)
- For BST: Produces sorted order
- Time Complexity: O(n)
- Space Complexity: O(h) for recursion stack

#### Preorder Traversal (Root → Left → Right)
- Useful for tree copying
- Used in expression tree evaluation
- Time Complexity: O(n)

#### Postorder Traversal (Left → Right → Root)
- Useful for tree deletion
- Used in expression tree evaluation
- Time Complexity: O(n)

#### Level Order Traversal
- Breadth-first traversal
- Uses queue for implementation
- Time Complexity: O(n)

## Path Properties

### Longest Path (Diameter)
The diameter of a tree is the number of edges on the longest path between any two nodes.

```cpp
class TreePathProperties {
public:
    static int diameter(TreeNode* root) {
        return calculateDiameter(root).first;
    }
    
private:
    static std::pair<int, int> calculateDiameter(TreeNode* node) {
        if (node == nullptr) {
            return {0, -1};  // {diameter, height}
        }
        
        auto left = calculateDiameter(node->left);
        auto right = calculateDiameter(node->right);
        
        int currentDiameter = std::max({
            left.first,
            right.first,
            left.second + right.second + 2
        });
        
        int currentHeight = std::max(left.second, right.second) + 1;
        
        return {currentDiameter, currentHeight};
    }
};
```

### Maximum Path Sum
Maximum sum of values along any path in the tree.

```cpp
class TreePathSumProperties {
public:
    static int maxPathSum(TreeNode* root) {
        int result = INT_MIN;
        maxPathDown(root, result);
        return result;
    }
    
private:
    static int maxPathDown(TreeNode* node, int& result) {
        if (node == nullptr) return 0;
        
        int left = std::max(0, maxPathDown(node->left, result));
        int right = std::max(0, maxPathDown(node->right, result));
        
        result = std::max(result, left + right + node->data);
        
        return std::max(left, right) + node->data;
    }
};
```

## Width Properties

### Maximum Width
Maximum number of nodes at any level of the tree.

```cpp
class TreeWidthProperties {
public:
    static int maxWidth(TreeNode* root) {
        if (root == nullptr) return 0;
        
        std::queue<TreeNode*> q;
        q.push(root);
        int result = 0;
        
        while (!q.empty()) {
            int count = q.size();
            result = std::max(result, count);
            
            while (count--) {
                TreeNode* current = q.front();
                q.pop();
                
                if (current->left) q.push(current->left);
                if (current->right) q.push(current->right);
            }
        }
        
        return result;
    }
};
```

## Density Properties

### Tree Density
Ratio of number of nodes to maximum possible nodes for given height.

```cpp
class TreeDensityProperties {
public:
    static double density(TreeNode* root) {
        int nodes = countNodes(root);
        int height = treeHeight(root);
        int maxNodes = (1 << (height + 1)) - 1;  // 2^(height+1) - 1
        
        return static_cast<double>(nodes) / maxNodes;
    }
    
private:
    static int countNodes(TreeNode* root) {
        if (root == nullptr) return 0;
        return 1 + countNodes(root->left) + countNodes(root->right);
    }
    
    static int treeHeight(TreeNode* root) {
        if (root == nullptr) return -1;
        return 1 + std::max(treeHeight(root->left), treeHeight(root->right));
    }
};
```

## Complexity Analysis Summary

| Property | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Height Calculation | O(n) | O(h) |
| Node Count | O(n) | O(h) |
| Balance Check | O(n) | O(h) |
| Diameter | O(n) | O(h) |
| Max Width | O(n) | O(w) |
| Density | O(n) | O(h) |

Where:
- n = number of nodes
- h = height of tree
- w = maximum width of tree

## Practical Applications

### 1. Algorithm Selection
- Use height to decide between recursive and iterative approaches
- Use balance factor to determine if rebalancing is needed

### 2. Performance Optimization
- Complete trees enable array representation with better cache performance
- Balanced trees ensure O(log n) operations

### 3. Memory Planning
- Density helps estimate memory efficiency
- Width helps plan queue sizes for level-order traversal

## Summary

Understanding tree properties is essential for:
- Choosing appropriate tree structures
- Analyzing algorithm performance
- Optimizing memory usage
- Debugging tree-related issues

These mathematical relationships provide the foundation for advanced tree algorithms and data structure selection.
