# README.md

## Tree Traversals - Complete Guide

### Overview

Tree traversal refers to the process of visiting each node in a tree exactly once in a systematic way. Different traversal orders serve different purposes: inorder traversal of a BST gives sorted order, preorder traversal is useful for creating copies of trees, postorder traversal is used for deleting trees, and level order traversal gives a breadth-first view. Understanding tree traversals is essential for solving many tree-related problems.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [01_Depth_First_Search.md](01_Depth_First_Search.md) | understand Depth-First Search (DFS) Traversal |
| 2. | [02_Breadth_First_Search.md](02_Breadth_First_Search.md) | understand Breadth-First Search (BFS) Traversal |
| 3. | [03_Inorder_Traversal.md](03_Inorder_Traversal.md) | understand Inorder Traversal (Left-Root-Right) |
| 4. | [04_Preorder_Traversal.md](04_Preorder_Traversal.md) | understand Preorder Traversal (Root-Left-Right) |
| 5. | [05_Postorder_Traversal.md](05_Postorder_Traversal.md) | understand Postorder Traversal (Left-Right-Root) |
| 6. | [06_Level_Order_Traversal.md](06_Level_Order_Traversal.md) | understand Level Order Traversal (BFS) |
| 7. | [README.md](README.md) | understand Tree Traversals Overview |

---

## 1. Depth-First Search (DFS)

This topic introduces the DFS approach to tree traversal.

**File:** [01_Depth_First_Search.md](01_Depth_First_Search.md)

**What you will learn:**
- What is Depth-First Search
- Recursive implementation
- Iterative implementation using stack
- Time and space complexity
- Applications of DFS

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Depth-First** | Explores as far as possible along each branch before backtracking |
| **Stack-based** | Uses recursion or explicit stack |
| **Three Orders** | Preorder, Inorder, Postorder |

**Visualization:**
```
        1
       / \
      2   3
     / \   \
    4   5   6

DFS Order (Preorder): 1,2,4,5,3,6
```

**Recursive DFS Template:**
```cpp
void dfs(Node* node) {
    if (!node) return;
    
    // Process node (preorder position)
    
    dfs(node->left);
    
    // Process node (inorder position)
    
    dfs(node->right);
    
    // Process node (postorder position)
}
```

---

## 2. Breadth-First Search (BFS)

This topic introduces the BFS approach to tree traversal.

**File:** [02_Breadth_First_Search.md](02_Breadth_First_Search.md)

**What you will learn:**
- What is Breadth-First Search
- Level order traversal using queue
- Iterative implementation
- Time and space complexity
- Applications of BFS

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Breadth-First** | Explores level by level before going deeper |
| **Queue-based** | Uses queue for processing nodes |
| **Level Order** | Nodes at same depth are visited together |

**Visualization:**
```
        1
       / \
      2   3
     / \   \
    4   5   6

BFS Order (Level Order): 1,2,3,4,5,6
```

**BFS Implementation:**
```cpp
void levelOrder(Node* root) {
    if (!root) return;
    
    queue<Node*> q;
    q.push(root);
    
    while (!q.empty()) {
        Node* curr = q.front();
        q.pop();
        
        cout << curr->data << " ";
        
        if (curr->left) q.push(curr->left);
        if (curr->right) q.push(curr->right);
    }
}
```

---

## 3. Inorder Traversal

This topic explains inorder traversal (Left-Root-Right).

**File:** [03_Inorder_Traversal.md](03_Inorder_Traversal.md)

**What you will learn:**
- Inorder traversal algorithm (recursive and iterative)
- Inorder traversal of BST gives sorted order
- Time and space complexity
- Applications (sorted output, BST validation)

**Key Concepts:**

| Order | Operation |
|-------|-----------|
| **Step 1** | Traverse left subtree |
| **Step 2** | Visit root |
| **Step 3** | Traverse right subtree |

**Visualization:**
```
        1
       / \
      2   3
     / \   \
    4   5   6

Inorder: 4,2,5,1,3,6
```

**Recursive Implementation:**
```cpp
void inorder(Node* node) {
    if (!node) return;
    inorder(node->left);
    cout << node->data << " ";
    inorder(node->right);
}
```

**Iterative Implementation:**
```cpp
void inorderIterative(Node* root) {
    stack<Node*> st;
    Node* curr = root;
    
    while (curr || !st.empty()) {
        while (curr) {
            st.push(curr);
            curr = curr->left;
        }
        
        curr = st.top();
        st.pop();
        cout << curr->data << " ";
        curr = curr->right;
    }
}
```

---

## 4. Preorder Traversal

This topic explains preorder traversal (Root-Left-Right).

**File:** [04_Preorder_Traversal.md](04_Preorder_Traversal.md)

**What you will learn:**
- Preorder traversal algorithm (recursive and iterative)
- Root visited before children
- Applications (tree copying, serialization, prefix expression)

**Key Concepts:**

| Order | Operation |
|-------|-----------|
| **Step 1** | Visit root |
| **Step 2** | Traverse left subtree |
| **Step 3** | Traverse right subtree |

**Visualization:**
```
        1
       / \
      2   3
     / \   \
    4   5   6

Preorder: 1,2,4,5,3,6
```

**Recursive Implementation:**
```cpp
void preorder(Node* node) {
    if (!node) return;
    cout << node->data << " ";
    preorder(node->left);
    preorder(node->right);
}
```

**Iterative Implementation:**
```cpp
void preorderIterative(Node* root) {
    if (!root) return;
    
    stack<Node*> st;
    st.push(root);
    
    while (!st.empty()) {
        Node* curr = st.top();
        st.pop();
        cout << curr->data << " ";
        
        if (curr->right) st.push(curr->right);
        if (curr->left) st.push(curr->left);
    }
}
```

---

## 5. Postorder Traversal

This topic explains postorder traversal (Left-Right-Root).

**File:** [05_Postorder_Traversal.md](05_Postorder_Traversal.md)

**What you will learn:**
- Postorder traversal algorithm (recursive and iterative)
- Children visited before root
- Applications (tree deletion, postfix expression, dependency resolution)

**Key Concepts:**

| Order | Operation |
|-------|-----------|
| **Step 1** | Traverse left subtree |
| **Step 2** | Traverse right subtree |
| **Step 3** | Visit root |

**Visualization:**
```
        1
       / \
      2   3
     / \   \
    4   5   6

Postorder: 4,5,2,6,3,1
```

**Recursive Implementation:**
```cpp
void postorder(Node* node) {
    if (!node) return;
    postorder(node->left);
    postorder(node->right);
    cout << node->data << " ";
}
```

**Iterative Implementation (Two-Stack Method):**
```cpp
void postorderIterative(Node* root) {
    if (!root) return;
    
    stack<Node*> st1, st2;
    st1.push(root);
    
    while (!st1.empty()) {
        Node* curr = st1.top();
        st1.pop();
        st2.push(curr);
        
        if (curr->left) st1.push(curr->left);
        if (curr->right) st1.push(curr->right);
    }
    
    while (!st2.empty()) {
        cout << st2.top()->data << " ";
        st2.pop();
    }
}
```

---

## 6. Level Order Traversal

This topic explains level order traversal (breadth-first).

**File:** [06_Level_Order_Traversal.md](06_Level_Order_Traversal.md)

**What you will learn:**
- Level order traversal using queue
- Printing level by level
- Zigzag traversal (spiral order)
- Time and space complexity
- Applications (shortest path, tree width)

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Level by Level** | Process nodes at same depth together |
| **Queue-based** | Uses queue for BFS |
| **Level Tracking** | Track level using queue size |

**Visualization:**
```
        1
       / \
      2   3
     / \   \
    4   5   6

Level Order: 1,2,3,4,5,6
```

**Basic Implementation:**
```cpp
void levelOrder(Node* root) {
    if (!root) return;
    
    queue<Node*> q;
    q.push(root);
    
    while (!q.empty()) {
        Node* curr = q.front();
        q.pop();
        cout << curr->data << " ";
        
        if (curr->left) q.push(curr->left);
        if (curr->right) q.push(curr->right);
    }
}
```

**Level-by-Level Output:**
```cpp
void levelOrderByLevel(Node* root) {
    if (!root) return;
    
    queue<Node*> q;
    q.push(root);
    
    while (!q.empty()) {
        int levelSize = q.size();
        
        for (int i = 0; i < levelSize; i++) {
            Node* curr = q.front();
            q.pop();
            cout << curr->data << " ";
            
            if (curr->left) q.push(curr->left);
            if (curr->right) q.push(curr->right);
        }
        cout << endl;  // New line after each level
    }
}
```

**Zigzag (Spiral) Traversal:**
```cpp
void zigzagTraversal(Node* root) {
    if (!root) return;
    
    queue<Node*> q;
    q.push(root);
    bool leftToRight = true;
    
    while (!q.empty()) {
        int levelSize = q.size();
        vector<int> level(levelSize);
        
        for (int i = 0; i < levelSize; i++) {
            Node* curr = q.front();
            q.pop();
            
            int index = leftToRight ? i : (levelSize - 1 - i);
            level[index] = curr->data;
            
            if (curr->left) q.push(curr->left);
            if (curr->right) q.push(curr->right);
        }
        
        for (int val : level) {
            cout << val << " ";
        }
        cout << endl;
        
        leftToRight = !leftToRight;
    }
}
```

---

### Complete Traversal Demo

```cpp
#include <iostream>
#include <queue>
#include <stack>
#include <vector>
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
    
    // ============ RECURSIVE TRAVERSALS ============
    
    void inorderRecursive(Node* node) {
        if (!node) return;
        inorderRecursive(node->left);
        cout << node->data << " ";
        inorderRecursive(node->right);
    }
    
    void preorderRecursive(Node* node) {
        if (!node) return;
        cout << node->data << " ";
        preorderRecursive(node->left);
        preorderRecursive(node->right);
    }
    
    void postorderRecursive(Node* node) {
        if (!node) return;
        postorderRecursive(node->left);
        postorderRecursive(node->right);
        cout << node->data << " ";
    }
    
    // ============ ITERATIVE TRAVERSALS ============
    
    void inorderIterative() {
        stack<Node*> st;
        Node* curr = root;
        
        while (curr || !st.empty()) {
            while (curr) {
                st.push(curr);
                curr = curr->left;
            }
            curr = st.top();
            st.pop();
            cout << curr->data << " ";
            curr = curr->right;
        }
        cout << endl;
    }
    
    void preorderIterative() {
        if (!root) return;
        
        stack<Node*> st;
        st.push(root);
        
        while (!st.empty()) {
            Node* curr = st.top();
            st.pop();
            cout << curr->data << " ";
            
            if (curr->right) st.push(curr->right);
            if (curr->left) st.push(curr->left);
        }
        cout << endl;
    }
    
    void postorderIterative() {
        if (!root) return;
        
        stack<Node*> st1, st2;
        st1.push(root);
        
        while (!st1.empty()) {
            Node* curr = st1.top();
            st1.pop();
            st2.push(curr);
            
            if (curr->left) st1.push(curr->left);
            if (curr->right) st1.push(curr->right);
        }
        
        while (!st2.empty()) {
            cout << st2.top()->data << " ";
            st2.pop();
        }
        cout << endl;
    }
    
    // ============ LEVEL ORDER ============
    
    void levelOrder() {
        if (!root) return;
        
        queue<Node*> q;
        q.push(root);
        
        while (!q.empty()) {
            Node* curr = q.front();
            q.pop();
            cout << curr->data << " ";
            
            if (curr->left) q.push(curr->left);
            if (curr->right) q.push(curr->right);
        }
        cout << endl;
    }
    
    void levelOrderByLevel() {
        if (!root) return;
        
        queue<Node*> q;
        q.push(root);
        
        while (!q.empty()) {
            int levelSize = q.size();
            
            for (int i = 0; i < levelSize; i++) {
                Node* curr = q.front();
                q.pop();
                cout << curr->data << " ";
                
                if (curr->left) q.push(curr->left);
                if (curr->right) q.push(curr->right);
            }
            cout << endl;
        }
    }
    
    void displayAllTraversals() {
        cout << "Recursive Traversals:" << endl;
        cout << "  Inorder:   ";
        inorderRecursive(root);
        cout << endl;
        cout << "  Preorder:  ";
        preorderRecursive(root);
        cout << endl;
        cout << "  Postorder: ";
        postorderRecursive(root);
        cout << endl;
        
        cout << "\nIterative Traversals:" << endl;
        cout << "  Inorder:   ";
        inorderIterative();
        cout << "  Preorder:  ";
        preorderIterative();
        cout << "  Postorder: ";
        postorderIterative();
        
        cout << "\nLevel Order Traversal:" << endl;
        cout << "  Single line: ";
        levelOrder();
        cout << "  By level:" << endl;
        levelOrderByLevel();
    }
};

int main() {
    // Build tree
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->right->right = new Node(6);
    
    BinaryTree tree;
    tree.setRoot(root);
    
    tree.displayAllTraversals();
    
    return 0;
}
```

**Output:**
```
Recursive Traversals:
  Inorder:   4 2 5 1 3 6 
  Preorder:  1 2 4 5 3 6 
  Postorder: 4 5 2 6 3 1 

Iterative Traversals:
  Inorder:   4 2 5 1 3 6 
  Preorder:  1 2 4 5 3 6 
  Postorder: 4 5 2 6 3 1 

Level Order Traversal:
  Single line: 1 2 3 4 5 6 
  By level:
1 
2 3 
4 5 6 
```

---

### Complexity Summary

| Traversal | Time Complexity | Space Complexity (Recursive) | Space Complexity (Iterative) |
|-----------|----------------|------------------------------|------------------------------|
| **Inorder** | O(n) | O(h) | O(h) |
| **Preorder** | O(n) | O(h) | O(h) |
| **Postorder** | O(n) | O(h) | O(h) |
| **Level Order** | O(n) | O(w) | O(w) |

- h = height of tree
- w = maximum width of tree

---

### Applications Summary

| Traversal | Applications |
|-----------|--------------|
| **Inorder** | BST sorted output, BST validation |
| **Preorder** | Tree copying, Serialization, Prefix expression |
| **Postorder** | Tree deletion, Postfix expression, Dependency resolution |
| **Level Order** | Shortest path (unweighted), Tree width, Zigzag traversal |

---

### Prerequisites

Before starting this section, you should have completed:

- [01_Binary_Trees/README.md](../01_Binary_Trees/README.md) - Binary tree basics
- [02_BST/README.md](../02_BST/README.md) - BST basics
- [04. Data Structures](../../04.%20Data%20Structures/README.md) - Stack and Queue

---

### Learning Path

```
Level 1: Depth-First Traversals
├── Recursive DFS (Inorder, Preorder, Postorder)
├── Iterative DFS using Stack
└── Applications

Level 2: Breadth-First Traversals
├── Level Order using Queue
├── Level-by-Level Output
└── Zigzag/Spiral Traversal

Level 3: Advanced Topics
├── Morris Traversal (O(1) space)
├── Boundary Traversal
└── Diagonal Traversal
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Forgetting base case in recursion | Always check for null node |
| Infinite loop in iterative traversal | Update pointers correctly |
| Not preserving order in iterative methods | Use appropriate stack/queue order |
| Confusing preorder and postorder | Remember: pre = root first, post = root last |
| Stack overflow for deep trees | Use iterative traversal for very deep trees |

---

### Practice Questions

After completing this section, you should be able to:

1. Implement all three DFS traversals recursively
2. Implement all three DFS traversals iteratively
3. Implement level order traversal using queue
4. Print level order traversal level by level
5. Implement zigzag (spiral) level order traversal
6. Identify which traversal produces a given output
7. Use inorder traversal to get sorted order from BST
8. Use preorder traversal to serialize a tree

---

### Next Steps

- Go to [01_Depth_First_Search.md](01_Depth_First_Search.md) to understand Depth-First Search.