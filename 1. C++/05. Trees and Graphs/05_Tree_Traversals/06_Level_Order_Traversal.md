# Tree Traversal - Level Order Traversal

## 📖 Overview

Level Order Traversal (also known as Breadth-First Search for trees) visits nodes level by level from top to bottom, left to right. Unlike depth-first traversals (inorder, preorder, postorder), level order traversal uses a queue instead of recursion or an explicit stack. This traversal is essential for finding the shortest path, printing tree structure, and solving problems that require level-by-level processing.

---

## 🎯 Key Characteristics

| Property | Description |
|----------|-------------|
| **Order** | Level by level, left to right |
| **BFS Variant** | Breadth-First Search |
| **Data Structure** | Queue (FIFO) |
| **Level Tracking** | Can track depth of each node |
| **Shortest Path** | Finds minimum hops in unweighted tree |

---

## 📊 Level Order Traversal Visualization

```
        50
       /  \
      30   80
     / \   / \
    20 40 70 90

Level Order: 50 → 30 → 80 → 20 → 40 → 70 → 90

Step-by-step:
Level 0: 50
Level 1: 30, 80
Level 2: 20, 40, 70, 90
```

---

## 📝 Basic Level Order Implementation

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;
    
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

class BinaryTree {
private:
    Node* root;
    
public:
    BinaryTree() : root(nullptr) {}
    
    void setRoot(Node* node) { root = node; }
    
    // Basic level order traversal
    vector<int> levelOrder() {
        vector<int> result;
        if (root == nullptr) return result;
        
        queue<Node*> q;
        q.push(root);
        
        while (!q.empty()) {
            Node* current = q.front();
            q.pop();
            
            result.push_back(current->data);
            
            if (current->left) q.push(current->left);
            if (current->right) q.push(current->right);
        }
        
        return result;
    }
    
    void printLevelOrder() {
        vector<int> result = levelOrder();
        cout << "Level Order: ";
        for (int val : result) cout << val << " ";
        cout << endl;
    }
};
```

---

## 📊 Level Order with Level Separation

```cpp
class BinaryTree {
private:
    Node* root;
    
public:
    // Level order with level separation (returns vector of levels)
    vector<vector<int>> levelOrderWithLevels() {
        vector<vector<int>> result;
        if (root == nullptr) return result;
        
        queue<Node*> q;
        q.push(root);
        
        while (!q.empty()) {
            int levelSize = q.size();
            vector<int> currentLevel;
            
            for (int i = 0; i < levelSize; i++) {
                Node* current = q.front();
                q.pop();
                
                currentLevel.push_back(current->data);
                
                if (current->left) q.push(current->left);
                if (current->right) q.push(current->right);
            }
            
            result.push_back(currentLevel);
        }
        
        return result;
    }
    
    void printLevels() {
        vector<vector<int>> levels = levelOrderWithLevels();
        cout << "\nLevel Order with Levels:" << endl;
        for (size_t i = 0; i < levels.size(); i++) {
            cout << "Level " << i << ": ";
            for (int val : levels[i]) cout << val << " ";
            cout << endl;
        }
    }
};
```

---

## 🔄 Zigzag Level Order (Spiral Traversal)

```cpp
class BinaryTree {
private:
    Node* root;
    
public:
    // Zigzag level order (spiral traversal)
    vector<vector<int>> zigzagLevelOrder() {
        vector<vector<int>> result;
        if (root == nullptr) return result;
        
        queue<Node*> q;
        q.push(root);
        bool leftToRight = true;
        
        while (!q.empty()) {
            int levelSize = q.size();
            vector<int> currentLevel(levelSize);
            
            for (int i = 0; i < levelSize; i++) {
                Node* current = q.front();
                q.pop();
                
                // Calculate index based on direction
                int index = leftToRight ? i : levelSize - 1 - i;
                currentLevel[index] = current->data;
                
                if (current->left) q.push(current->left);
                if (current->right) q.push(current->right);
            }
            
            result.push_back(currentLevel);
            leftToRight = !leftToRight;
        }
        
        return result;
    }
    
    void printZigzag() {
        vector<vector<int>> zigzag = zigzagLevelOrder();
        cout << "\nZigzag Level Order:" << endl;
        for (size_t i = 0; i < zigzag.size(); i++) {
            cout << "Level " << i << ": ";
            for (int val : zigzag[i]) cout << val << " ";
            cout << endl;
        }
    }
};
```

---

## 💻 Complete Implementation

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;

class Node {
public:
    int data;
    Node* left;
    Node* right;
    
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

class BinaryTree {
private:
    Node* root;
    
    Node* createTreeFromArray(const vector<int>& arr, int index) {
        if (index >= arr.size() || arr[index] == -1) return nullptr;
        
        Node* node = new Node(arr[index]);
        node->left = createTreeFromArray(arr, 2 * index + 1);
        node->right = createTreeFromArray(arr, 2 * index + 2);
        
        return node;
    }
    
public:
    BinaryTree() : root(nullptr) {}
    
    void setRoot(Node* node) { root = node; }
    
    void buildFromLevelOrder(const vector<int>& arr) {
        root = createTreeFromArray(arr, 0);
    }
    
    // 1. Basic Level Order
    vector<int> levelOrder() {
        vector<int> result;
        if (root == nullptr) return result;
        
        queue<Node*> q;
        q.push(root);
        
        while (!q.empty()) {
            Node* current = q.front();
            q.pop();
            
            result.push_back(current->data);
            
            if (current->left) q.push(current->left);
            if (current->right) q.push(current->right);
        }
        
        return result;
    }
    
    // 2. Level Order with Level Separation
    vector<vector<int>> levelOrderWithLevels() {
        vector<vector<int>> result;
        if (root == nullptr) return result;
        
        queue<Node*> q;
        q.push(root);
        
        while (!q.empty()) {
            int levelSize = q.size();
            vector<int> currentLevel;
            
            for (int i = 0; i < levelSize; i++) {
                Node* current = q.front();
                q.pop();
                
                currentLevel.push_back(current->data);
                
                if (current->left) q.push(current->left);
                if (current->right) q.push(current->right);
            }
            
            result.push_back(currentLevel);
        }
        
        return result;
    }
    
    // 3. Zigzag Level Order (Spiral)
    vector<vector<int>> zigzagLevelOrder() {
        vector<vector<int>> result;
        if (root == nullptr) return result;
        
        queue<Node*> q;
        q.push(root);
        bool leftToRight = true;
        
        while (!q.empty()) {
            int levelSize = q.size();
            vector<int> currentLevel(levelSize);
            
            for (int i = 0; i < levelSize; i++) {
                Node* current = q.front();
                q.pop();
                
                int index = leftToRight ? i : levelSize - 1 - i;
                currentLevel[index] = current->data;
                
                if (current->left) q.push(current->left);
                if (current->right) q.push(current->right);
            }
            
            result.push_back(currentLevel);
            leftToRight = !leftToRight;
        }
        
        return result;
    }
    
    // 4. Reverse Level Order (bottom-up)
    vector<vector<int>> reverseLevelOrder() {
        vector<vector<int>> result = levelOrderWithLevels();
        reverse(result.begin(), result.end());
        return result;
    }
    
    // 5. Level order using recursion (height-based)
    int getHeight(Node* node) {
        if (node == nullptr) return 0;
        return 1 + max(getHeight(node->left), getHeight(node->right));
    }
    
    void printLevelRecursive(Node* node, int level, vector<int>& result) {
        if (node == nullptr) return;
        if (level == 1) {
            result.push_back(node->data);
        } else if (level > 1) {
            printLevelRecursive(node->left, level - 1, result);
            printLevelRecursive(node->right, level - 1, result);
        }
    }
    
    vector<int> levelOrderRecursive() {
        vector<int> result;
        int height = getHeight(root);
        
        for (int i = 1; i <= height; i++) {
            printLevelRecursive(root, i, result);
        }
        
        return result;
    }
    
    // 6. Right Side View
    vector<int> rightSideView() {
        vector<int> result;
        if (root == nullptr) return result;
        
        queue<Node*> q;
        q.push(root);
        
        while (!q.empty()) {
            int levelSize = q.size();
            
            for (int i = 0; i < levelSize; i++) {
                Node* current = q.front();
                q.pop();
                
                if (i == levelSize - 1) {
                    result.push_back(current->data);
                }
                
                if (current->left) q.push(current->left);
                if (current->right) q.push(current->right);
            }
        }
        
        return result;
    }
    
    // 7. Left Side View
    vector<int> leftSideView() {
        vector<int> result;
        if (root == nullptr) return result;
        
        queue<Node*> q;
        q.push(root);
        
        while (!q.empty()) {
            int levelSize = q.size();
            
            for (int i = 0; i < levelSize; i++) {
                Node* current = q.front();
                q.pop();
                
                if (i == 0) {
                    result.push_back(current->data);
                }
                
                if (current->left) q.push(current->left);
                if (current->right) q.push(current->right);
            }
        }
        
        return result;
    }
    
    // 8. Bottom View (using BFS with horizontal distance)
    // Simplified version for this example
    vector<int> bottomView() {
        vector<int> result;
        if (root == nullptr) return result;
        
        // Using map to store horizontal distance -> node value
        map<int, int> hdMap;
        queue<pair<Node*, int>> q;
        q.push({root, 0});
        
        while (!q.empty()) {
            auto [node, hd] = q.front();
            q.pop();
            
            hdMap[hd] = node->data;  // Last node at each HD
            
            if (node->left) q.push({node->left, hd - 1});
            if (node->right) q.push({node->right, hd + 1});
        }
        
        for (auto& [hd, val] : hdMap) {
            result.push_back(val);
        }
        
        return result;
    }
    
    // Print all traversals
    void printAll() {
        cout << "\n=== Level Order Traversals ===" << endl;
        
        // Basic level order
        vector<int> basic = levelOrder();
        cout << "Basic Level Order: ";
        for (int v : basic) cout << v << " ";
        cout << endl;
        
        // Recursive level order
        vector<int> rec = levelOrderRecursive();
        cout << "Level Order (Recursive): ";
        for (int v : rec) cout << v << " ";
        cout << endl;
        
        // Levels separated
        vector<vector<int>> levels = levelOrderWithLevels();
        cout << "\nLevels Separated:" << endl;
        for (size_t i = 0; i < levels.size(); i++) {
            cout << "  Level " << i << ": ";
            for (int v : levels[i]) cout << v << " ";
            cout << endl;
        }
        
        // Zigzag
        vector<vector<int>> zigzag = zigzagLevelOrder();
        cout << "\nZigzag (Spiral) Order:" << endl;
        for (size_t i = 0; i < zigzag.size(); i++) {
            cout << "  Level " << i << ": ";
            for (int v : zigzag[i]) cout << v << " ";
            cout << endl;
        }
        
        // Reverse level order
        vector<vector<int>> reverse = reverseLevelOrder();
        cout << "\nReverse Level Order (Bottom-up):" << endl;
        for (size_t i = 0; i < reverse.size(); i++) {
            cout << "  Level " << reverse.size() - 1 - i << ": ";
            for (int v : reverse[i]) cout << v << " ";
            cout << endl;
        }
        
        // Side views
        vector<int> rightView = rightSideView();
        cout << "\nRight Side View: ";
        for (int v : rightView) cout << v << " ";
        cout << endl;
        
        vector<int> leftView = leftSideView();
        cout << "Left Side View: ";
        for (int v : leftView) cout << v << " ";
        cout << endl;
        
        // Bottom view
        vector<int> bottom = bottomView();
        cout << "Bottom View: ";
        for (int v : bottom) cout << v << " ";
        cout << endl;
    }
    
    // Display tree structure
    void displayTree() {
        if (!root) {
            cout << "Tree is empty" << endl;
            return;
        }
        
        vector<vector<int>> levels = levelOrderWithLevels();
        cout << "\nTree Structure (Level by Level):" << endl;
        for (size_t i = 0; i < levels.size(); i++) {
            // Add spaces for alignment
            int spaces = (levels.size() - i) * 2;
            cout << string(spaces, ' ');
            
            for (int v : levels[i]) {
                cout << v << "   ";
            }
            cout << endl;
        }
    }
};

int main() {
    cout << "=== Level Order Traversal Demo ===" << endl;
    
    // Create tree: 
    //        50
    //       /  \
    //      30   80
    //     / \   / \
    //    20 40 70 90
    
    Node* root = new Node(50);
    root->left = new Node(30);
    root->right = new Node(80);
    root->left->left = new Node(20);
    root->left->right = new Node(40);
    root->right->left = new Node(70);
    root->right->right = new Node(90);
    
    BinaryTree tree;
    tree.setRoot(root);
    
    tree.displayTree();
    tree.printAll();
    
    // Additional test: Tree with missing nodes
    cout << "\n=== Tree with Missing Nodes ===" << endl;
    Node* root2 = new Node(1);
    root2->left = new Node(2);
    root2->right = new Node(3);
    root2->left->right = new Node(4);
    root2->right->left = new Node(5);
    
    BinaryTree tree2;
    tree2.setRoot(root2);
    
    vector<vector<int>> levels2 = tree2.levelOrderWithLevels();
    cout << "Levels:" << endl;
    for (size_t i = 0; i < levels2.size(); i++) {
        cout << "Level " << i << ": ";
        for (int v : levels2[i]) cout << v << " ";
        cout << endl;
    }
    
    // Zigzag for this tree
    vector<vector<int>> zigzag2 = tree2.zigzagLevelOrder();
    cout << "\nZigzag Order:" << endl;
    for (size_t i = 0; i < zigzag2.size(); i++) {
        cout << "Level " << i << ": ";
        for (int v : zigzag2[i]) cout << v << " ";
        cout << endl;
    }
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Implementation | Time Complexity | Space Complexity |
|----------------|----------------|------------------|
| **Basic BFS** | O(n) | O(w) where w = max width |
| **Level Separation** | O(n) | O(w) |
| **Zigzag** | O(n) | O(w) |
| **Recursive** | O(n²) | O(h) (call stack) |

---

## 🎯 Applications of Level Order Traversal

| Application | Description |
|-------------|-------------|
| **Tree Printing** | Display tree structure visually |
| **Level-wise Processing** | Process nodes by depth |
| **Shortest Path** | Minimum hops in unweighted tree |
| **Side Views** | Left/Right view of tree |
| **Bottom View** | Nodes visible from bottom |
| **Maximum Width** | Find widest level |
| **Level Order Serialization** | Save tree structure |
| **Binary Heap Building** | Complete tree construction |

---

## ✅ Key Takeaways

1. **Level Order** uses a queue (FIFO)
2. **Level separation** tracks depth using level size
3. **Zigzag traversal** alternates direction each level
4. **Side views** capture first/last node at each level
5. **Recursive level order** is O(n²) - not efficient
6. **Bottom view** uses horizontal distance mapping
7. **Time complexity** O(n) for queue-based implementations
8. **Space complexity** O(w) where w is maximum width

---
---

## Next Step

- Go to [README.md](README.md) to continue.
