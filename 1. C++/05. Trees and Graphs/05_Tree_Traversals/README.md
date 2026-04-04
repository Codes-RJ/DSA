# Tree Traversals

## Overview
Tree traversal is the process of visiting each node in a tree data structure exactly once. Different traversal methods visit nodes in different orders, each serving specific purposes and applications. Understanding traversal algorithms is fundamental to tree-based problem solving.

## Topics Covered

### 1. Depth-First Search (`01_Depth_First_Search.md`)
- DFS concept and implementation
- Recursive and iterative approaches
- Stack-based DFS traversal
- Applications and use cases
- Time and space complexity analysis

### 2. Breadth-First Search (`02_Breadth_First_Search.md`)
- BFS concept and implementation
- Queue-based level order traversal
- Applications in shortest path problems
- Memory considerations
- Implementation variations

### 3. Inorder Traversal (`03_Inorder_Traversal.md`)
- Inorder traversal for binary trees
- Left-Root-Right visiting order
- BST sorted output property
- Recursive and iterative implementations
- Applications and examples

### 4. Preorder Traversal (`04_Preorder_Traversal.md`)
- Preorder traversal for binary trees
- Root-Left-Right visiting order
- Tree copying applications
- Prefix expression evaluation
- Implementation details

### 5. Postorder Traversal (`05_Postorder_Traversal.md`)
- Postorder traversal for binary trees
- Left-Right-Root visiting order
- Tree deletion applications
- Postfix expression evaluation
- Memory management

### 6. Level Order Traversal (`06_Level_Order_Traversal.md`)
- Level-by-level tree traversal
- BFS implementation for trees
- Tree visualization and printing
- Applications in tree problems
- Spiral/zigzag variations

## Traversal Types and Orders

### Depth-First Traversals

#### 1. Inorder Traversal (Left → Root → Right)
```
    A
   / \
  B   C
 / \
D   E

Inorder: D → B → E → A → C
```

#### 2. Preorder Traversal (Root → Left → Right)
```
    A
   / \
  B   C
 / \
D   E

Preorder: A → B → D → E → C
```

#### 3. Postorder Traversal (Left → Right → Root)
```
    A
   / \
  B   C
 / \
D   E

Postorder: D → E → B → C → A
```

### Breadth-First Traversal

#### Level Order Traversal
```
    A
   / \
  B   C
 / \
D   E

Level Order: A → B → C → D → E
```

## Basic Tree Node Structure

```cpp
struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;
    
    TreeNode(int val) : data(val), left(nullptr), right(nullptr) {}
};
```

## Depth-First Search Implementation

### 1. Recursive DFS
```cpp
class DFSTraversals {
public:
    // Inorder traversal (Left, Root, Right)
    static void inorderRecursive(TreeNode* root) {
        if (root == nullptr) return;
        
        inorderRecursive(root->left);
        std::cout << root->data << " ";
        inorderRecursive(root->right);
    }
    
    // Preorder traversal (Root, Left, Right)
    static void preorderRecursive(TreeNode* root) {
        if (root == nullptr) return;
        
        std::cout << root->data << " ";
        preorderRecursive(root->left);
        preorderRecursive(root->right);
    }
    
    // Postorder traversal (Left, Right, Root)
    static void postorderRecursive(TreeNode* root) {
        if (root == nullptr) return;
        
        postorderRecursive(root->left);
        postorderRecursive(root->right);
        std::cout << root->data << " ";
    }
};
```

### 2. Iterative DFS
```cpp
class IterativeDFS {
public:
    // Iterative inorder traversal
    static void inorderIterative(TreeNode* root) {
        std::stack<TreeNode*> s;
        TreeNode* current = root;
        
        while (current != nullptr || !s.empty()) {
            // Reach the leftmost node
            while (current != nullptr) {
                s.push(current);
                current = current->left;
            }
            
            current = s.top();
            s.pop();
            
            std::cout << current->data << " ";
            current = current->right;
        }
    }
    
    // Iterative preorder traversal
    static void preorderIterative(TreeNode* root) {
        if (root == nullptr) return;
        
        std::stack<TreeNode*> s;
        s.push(root);
        
        while (!s.empty()) {
            TreeNode* current = s.top();
            s.pop();
            
            std::cout << current->data << " ";
            
            // Push right first, then left (so left is processed first)
            if (current->right) s.push(current->right);
            if (current->left) s.push(current->left);
        }
    }
    
    // Iterative postorder traversal (using two stacks)
    static void postorderIterative(TreeNode* root) {
        if (root == nullptr) return;
        
        std::stack<TreeNode*> s1, s2;
        s1.push(root);
        
        while (!s1.empty()) {
            TreeNode* current = s1.top();
            s1.pop();
            s2.push(current);
            
            if (current->left) s1.push(current->left);
            if (current->right) s1.push(current->right);
        }
        
        while (!s2.empty()) {
            TreeNode* current = s2.top();
            s2.pop();
            std::cout << current->data << " ";
        }
    }
};
```

## Breadth-First Search Implementation

### Level Order Traversal
```cpp
class BFSTraversals {
public:
    // Basic level order traversal
    static void levelOrder(TreeNode* root) {
        if (root == nullptr) return;
        
        std::queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            TreeNode* current = q.front();
            q.pop();
            
            std::cout << current->data << " ";
            
            if (current->left) q.push(current->left);
            if (current->right) q.push(current->right);
        }
    }
    
    // Level order traversal with levels separated
    static std::vector<std::vector<int>> levelOrderWithLevels(TreeNode* root) {
        std::vector<std::vector<int>> result;
        if (root == nullptr) return result;
        
        std::queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            int levelSize = q.size();
            std::vector<int> currentLevel;
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode* current = q.front();
                q.pop();
                
                currentLevel.push_back(current->data);
                
                if (current->left) q.push(current->left);
                if (current->right) q.push(current->right);
            }
            
            result.push_back(currentLevel);
        }
        
        return result;
    }
};
```

## Advanced Traversal Techniques

### 1. Spiral/Zigzag Traversal
```cpp
class AdvancedTraversals {
public:
    // Spiral order traversal
    static std::vector<std::vector<int>> spiralOrder(TreeNode* root) {
        std::vector<std::vector<int>> result;
        if (root == nullptr) return result;
        
        std::stack<TreeNode*> s1; // Left to right
        std::stack<TreeNode*> s2; // Right to left
        
        s1.push(root);
        
        while (!s1.empty() || !s2.empty()) {
            std::vector<int> currentLevel;
            
            // Left to right
            while (!s1.empty()) {
                TreeNode* current = s1.top();
                s1.pop();
                currentLevel.push_back(current->data);
                
                if (current->left) s2.push(current->left);
                if (current->right) s2.push(current->right);
            }
            
            if (!currentLevel.empty()) {
                result.push_back(currentLevel);
                currentLevel.clear();
            }
            
            // Right to left
            while (!s2.empty()) {
                TreeNode* current = s2.top();
                s2.pop();
                currentLevel.push_back(current->data);
                
                if (current->right) s1.push(current->right);
                if (current->left) s1.push(current->left);
            }
            
            if (!currentLevel.empty()) {
                result.push_back(currentLevel);
            }
        }
        
        return result;
    }
};
```

### 2. Boundary Traversal
```cpp
class BoundaryTraversal {
public:
    // Boundary traversal (left boundary + leaves + right boundary)
    static std::vector<int> boundaryTraversal(TreeNode* root) {
        std::vector<int> result;
        if (root == nullptr) return result;
        
        result.push_back(root->data);
        
        // Left boundary
        leftBoundary(root->left, result);
        
        // Leaves (left subtree)
        leaves(root->left, result);
        
        // Leaves (right subtree)
        leaves(root->right, result);
        
        // Right boundary (reverse)
        rightBoundary(root->right, result);
        
        return result;
    }
    
private:
    static void leftBoundary(TreeNode* node, std::vector<int>& result) {
        if (node == nullptr) return;
        
        if (node->left != nullptr || node->right != nullptr) {
            result.push_back(node->data);
        }
        
        if (node->left) {
            leftBoundary(node->left, result);
        } else if (node->right) {
            leftBoundary(node->right, result);
        }
    }
    
    static void rightBoundary(TreeNode* node, std::vector<int>& result) {
        if (node == nullptr) return;
        
        if (node->right) {
            rightBoundary(node->right, result);
        } else if (node->left) {
            rightBoundary(node->left, result);
        }
        
        if (node->left != nullptr || node->right != nullptr) {
            result.push_back(node->data);
        }
    }
    
    static void leaves(TreeNode* node, std::vector<int>& result) {
        if (node == nullptr) return;
        
        if (node->left == nullptr && node->right == nullptr) {
            result.push_back(node->data);
            return;
        }
        
        leaves(node->left, result);
        leaves(node->right, result);
    }
};
```

### 3. Vertical Order Traversal
```cpp
class VerticalTraversal {
public:
    // Vertical order traversal
    static std::vector<std::vector<int>> verticalOrder(TreeNode* root) {
        std::map<int, std::vector<int>> verticalMap;
        std::queue<std::pair<TreeNode*, int>> q;
        
        if (root) q.push({root, 0});
        
        while (!q.empty()) {
            auto current = q.front();
            q.pop();
            
            TreeNode* node = current.first;
            int hd = current.second; // Horizontal distance
            
            verticalMap[hd].push_back(node->data);
            
            if (node->left) q.push({node->left, hd - 1});
            if (node->right) q.push({node->right, hd + 1});
        }
        
        std::vector<std::vector<int>> result;
        for (auto& pair : verticalMap) {
            result.push_back(pair.second);
        }
        
        return result;
    }
};
```

## Traversal Applications

### 1. Tree Serialization and Deserialization
```cpp
class TreeSerialization {
public:
    // Serialize tree using preorder traversal
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

### 2. Tree Validation
```cpp
class TreeValidation {
public:
    // Validate BST using inorder traversal
    static bool isValidBST(TreeNode* root) {
        std::vector<int> inorder;
        inorderTraversal(root, inorder);
        
        for (int i = 1; i < inorder.size(); i++) {
            if (inorder[i] <= inorder[i - 1]) {
                return false;
            }
        }
        
        return true;
    }
    
    // Check if two trees are identical
    static bool areIdentical(TreeNode* root1, TreeNode* root2) {
        if (root1 == nullptr && root2 == nullptr) return true;
        if (root1 == nullptr || root2 == nullptr) return false;
        
        return (root1->data == root2->data) &&
               areIdentical(root1->left, root2->left) &&
               areIdentical(root1->right, root2->right);
    }
    
private:
    static void inorderTraversal(TreeNode* root, std::vector<int>& result) {
        if (root == nullptr) return;
        
        inorderTraversal(root->left, result);
        result.push_back(root->data);
        inorderTraversal(root->right, result);
    }
};
```

## Performance Analysis

### Time Complexity
| Traversal Type | Time Complexity |
|----------------|-----------------|
| Inorder | O(n) |
| Preorder | O(n) |
| Postorder | O(n) |
| Level Order | O(n) |
| Spiral Order | O(n) |
| Vertical Order | O(n log n) |

### Space Complexity
| Traversal Type | Space Complexity |
|----------------|-----------------|
| Recursive DFS | O(h) |
| Iterative DFS | O(h) |
| Level Order BFS | O(w) |
| Spiral Order | O(w) |
| Vertical Order | O(n) |

Where:
- n = number of nodes
- h = height of tree
- w = maximum width of tree

## Best Practices

### 1. Choosing Traversal Method
- **Inorder**: For BST sorted output and validation
- **Preorder**: For tree copying and prefix notation
- **Postorder**: For tree deletion and postfix notation
- **Level Order**: For tree visualization and BFS problems

### 2. Implementation Tips
- Handle null pointer cases
- Consider iterative versions for deep trees
- Use appropriate data structures (stack/queue)
- Manage memory properly in iterative versions

### 3. Performance Considerations
- Recursive versions use call stack space
- Iterative versions may use more explicit memory
- Choose based on tree depth and memory constraints

## Common Applications

### 1. Expression Trees
- Inorder: Infix expressions
- Preorder: Prefix expressions
- Postorder: Postfix expressions

### 2. File Systems
- Preorder: Directory listing with subdirectories
- Level Order: Breadth-first file search

### 3. XML/HTML Parsing
- Preorder: Document structure traversal
- Inorder: Content extraction

### 4. Game Trees
- Preorder: Game state exploration
- Level Order: Breadth-first game search

## Summary

Tree traversals are fundamental operations that enable various tree-based algorithms. Each traversal method has specific characteristics and applications. Understanding when and how to use each traversal type is crucial for efficient tree problem-solving and algorithm design.
