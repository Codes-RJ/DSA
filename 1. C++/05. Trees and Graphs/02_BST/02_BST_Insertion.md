# BST Insertion

## 📖 Overview

Insertion in a Binary Search Tree (BST) involves adding a new node while maintaining the BST property: for every node, all values in the left subtree are less than the node's value, and all values in the right subtree are greater. This guide covers both recursive and iterative insertion algorithms with complete implementations and complexity analysis.

---

## 🎯 Insertion Algorithm

### Basic Principle

The insertion algorithm follows the BST property to find the correct position for the new node:

```
1. Start at the root
2. Compare new value with current node's value
3. If new value < current value → go left
4. If new value > current value → go right
5. If equal → handle duplicate (typically ignore or count)
6. Repeat until a null position is found
7. Insert new node at that position
```

### Visual Example

```
Insert 50:                Insert 30:                Insert 80:
    50                        50                        50
                             /                         / \
                            30                        30  80

Insert 20:                Insert 40:                Insert 70:
    50                        50                        50
   / \                       / \                       / \
  30  80                    30  80                    30  80
 /                         / \                       / \   \
20                        20 40                     20 40   70

Insert 90:
    50
   / \
  30  80
 / \   \
20 40   90
```

---

## 📝 Recursive Insertion

### Implementation

```cpp
template<typename T>
class BSTNode {
public:
    T data;
    BSTNode* left;
    BSTNode* right;
    
    BSTNode(const T& value) : data(value), left(nullptr), right(nullptr) {}
};

template<typename T>
class BinarySearchTree {
private:
    BSTNode<T>* root;
    
    // Recursive insert helper
    BSTNode<T>* insertRecursive(BSTNode<T>* node, const T& value) {
        // Base case: found empty spot
        if (node == nullptr) {
            return new BSTNode<T>(value);
        }
        
        // Recursive cases
        if (value < node->data) {
            node->left = insertRecursive(node->left, value);
        } 
        else if (value > node->data) {
            node->right = insertRecursive(node->right, value);
        }
        // If equal, do nothing (no duplicates)
        
        return node;
    }
    
public:
    BinarySearchTree() : root(nullptr) {}
    
    void insert(const T& value) {
        root = insertRecursive(root, value);
    }
};
```

### Step-by-Step Execution

```
Insert 50 into empty tree:
    insertRecursive(nullptr, 50) → create node → return node → root = node

Insert 30 into tree with root 50:
    insertRecursive(50, 30):
        30 < 50 → go left (null)
        insertRecursive(nullptr, 30) → create node
        50->left = node
        return 50

Insert 80 into tree with root 50:
    insertRecursive(50, 80):
        80 > 50 → go right (null)
        insertRecursive(nullptr, 80) → create node
        50->right = node
        return 50
```

---

## 🔄 Iterative Insertion

### Implementation

```cpp
template<typename T>
void BinarySearchTree<T>::insertIterative(const T& value) {
    BSTNode<T>* newNode = new BSTNode<T>(value);
    
    // Case 1: Empty tree
    if (root == nullptr) {
        root = newNode;
        return;
    }
    
    // Case 2: Non-empty tree
    BSTNode<T>* current = root;
    BSTNode<T>* parent = nullptr;
    
    while (current != nullptr) {
        parent = current;
        
        if (value < current->data) {
            current = current->left;
        } 
        else if (value > current->data) {
            current = current->right;
        } 
        else {
            // Duplicate found - handle appropriately
            delete newNode;  // or increment count
            return;
        }
    }
    
    // Insert at the correct position
    if (value < parent->data) {
        parent->left = newNode;
    } else {
        parent->right = newNode;
    }
}
```

### Visual Walkthrough

```
Insert 30 into existing tree:

Step 1: current = root(50), parent = null
        30 < 50 → go left

Step 2: current = 30, parent = 50
        30 equals 30? No
        30 < 30? No
        30 > 30? No → duplicate found

Result: Do not insert (or increment count)

Insert 25 into tree:

Step 1: current = 50, parent = null
        25 < 50 → go left

Step 2: current = 30, parent = 50
        25 < 30 → go left

Step 3: current = 20, parent = 30
        25 > 20 → go right

Step 4: current = null, parent = 20
        Insert 25 as right child of 20
```

---

## 📊 Handling Duplicates

### Method 1: Count Duplicates

```cpp
template<typename T>
class BSTNodeWithCount {
public:
    T data;
    int count;
    BSTNodeWithCount* left;
    BSTNodeWithCount* right;
    
    BSTNodeWithCount(const T& value) 
        : data(value), count(1), left(nullptr), right(nullptr) {}
};

template<typename T>
void insertWithCount(BSTNodeWithCount<T>*& node, const T& value) {
    if (node == nullptr) {
        node = new BSTNodeWithCount<T>(value);
        return;
    }
    
    if (value < node->data) {
        insertWithCount(node->left, value);
    } 
    else if (value > node->data) {
        insertWithCount(node->right, value);
    } 
    else {
        node->count++;  // Increment count for duplicates
    }
}
```

### Method 2: Store Duplicates in Right Subtree

```cpp
template<typename T>
void insertWithDuplicatesRight(BSTNode<T>*& node, const T& value) {
    if (node == nullptr) {
        node = new BSTNode<T>(value);
        return;
    }
    
    if (value <= node->data) {  // Allow duplicates in left
        insertWithDuplicatesRight(node->left, value);
    } else {
        insertWithDuplicatesRight(node->right, value);
    }
}
```

### Method 3: Store Duplicates in Left Subtree

```cpp
template<typename T>
void insertWithDuplicatesLeft(BSTNode<T>*& node, const T& value) {
    if (node == nullptr) {
        node = new BSTNode<T>(value);
        return;
    }
    
    if (value < node->data) {
        insertWithDuplicatesLeft(node->left, value);
    } else {  // Allow duplicates in right
        insertWithDuplicatesLeft(node->right, value);
    }
}
```

---

## 📈 Complexity Analysis

### Time Complexity

| Case | Complexity | Description |
|------|------------|-------------|
| **Best Case** | O(1) | Inserting at root (empty tree) |
| **Average Case** | O(log n) | Tree is reasonably balanced |
| **Worst Case** | O(n) | Tree is skewed (like linked list) |

### Space Complexity

| Implementation | Space | Description |
|----------------|-------|-------------|
| **Recursive** | O(h) | Call stack depth equals height |
| **Iterative** | O(1) | No recursion overhead |

### Height Analysis

```
Perfect tree of height 3:
        50
       /  \
      30   80
     / \   / \
    20 40 70 90

Insert operations: O(log n) where n = 15, log₂(15) ≈ 4

Skewed tree:
    1
     \
      2
       \
        3
         \
          4
           \
            5

Insert operations: O(n) where n = 5
```

---

## 🎯 Edge Cases

### Case 1: Empty Tree

```cpp
// Initial state: root = nullptr
bst.insert(50);
// Result: root becomes new node with value 50
```

### Case 2: Duplicate Value

```cpp
bst.insert(50);
bst.insert(50);  // Duplicate

// Option A: Ignore (no change)
// Option B: Increment count
// Option C: Insert in left/right subtree
```

### Case 3: Inserting Minimum Value

```cpp
// Tree:    50
//         /  \
//        30   80

bst.insert(10);
// Result: 10 becomes left child of 30
```

### Case 4: Inserting Maximum Value

```cpp
// Tree:    50
//         /  \
//        30   80

bst.insert(100);
// Result: 100 becomes right child of 80
```

### Case 5: Inserting Between Values

```cpp
// Tree:    50
//         /  \
//        30   80

bst.insert(60);
// Result: 60 becomes left child of 80
```

---

## 💻 Complete Implementation

```cpp
#include <iostream>
#include <queue>
#include <stack>
using namespace std;

template<typename T>
class BST {
private:
    struct Node {
        T data;
        Node* left;
        Node* right;
        
        Node(const T& value) : data(value), left(nullptr), right(nullptr) {}
    };
    
    Node* root;
    size_t nodeCount;
    
    // Recursive insert helper
    Node* insertRecursive(Node* node, const T& value) {
        if (node == nullptr) {
            nodeCount++;
            return new Node(value);
        }
        
        if (value < node->data) {
            node->left = insertRecursive(node->left, value);
        } else if (value > node->data) {
            node->right = insertRecursive(node->right, value);
        }
        // Duplicate: ignore
        
        return node;
    }
    
    // Inorder traversal helper
    void inorderRecursive(Node* node) {
        if (node == nullptr) return;
        
        inorderRecursive(node->left);
        cout << node->data << " ";
        inorderRecursive(node->right);
    }
    
    // Print tree structure
    void printTree(Node* node, int space, int indent) {
        if (node == nullptr) return;
        
        space += indent;
        
        printTree(node->right, space, indent);
        
        cout << endl;
        for (int i = indent; i < space; i++) cout << " ";
        cout << node->data << endl;
        
        printTree(node->left, space, indent);
    }
    
public:
    BST() : root(nullptr), nodeCount(0) {}
    
    void insert(const T& value) {
        root = insertRecursive(root, value);
    }
    
    void insertIterative(const T& value) {
        Node* newNode = new Node(value);
        
        if (root == nullptr) {
            root = newNode;
            nodeCount++;
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
                delete newNode;  // Duplicate
                return;
            }
        }
        
        if (value < parent->data) {
            parent->left = newNode;
        } else {
            parent->right = newNode;
        }
        nodeCount++;
    }
    
    void inorder() {
        inorderRecursive(root);
        cout << endl;
    }
    
    void print() {
        printTree(root, 0, 5);
        cout << endl;
    }
    
    size_t size() const { return nodeCount; }
    bool empty() const { return root == nullptr; }
};

int main() {
    BST<int> bst;
    
    cout << "Inserting values: 50, 30, 80, 20, 40, 70, 90\n\n";
    
    bst.insert(50);
    bst.insert(30);
    bst.insert(80);
    bst.insert(20);
    bst.insert(40);
    bst.insert(70);
    bst.insert(90);
    
    cout << "Tree structure:\n";
    bst.print();
    
    cout << "Inorder traversal (sorted): ";
    bst.inorder();
    
    cout << "Tree size: " << bst.size() << endl;
    
    cout << "\nInserting duplicate 50 (ignored)\n";
    bst.insert(50);
    cout << "Tree size after duplicate: " << bst.size() << endl;
    
    return 0;
}
```

---

## 📊 Performance Comparison

### Recursive vs Iterative

| Aspect | Recursive | Iterative |
|--------|-----------|-----------|
| **Code Simplicity** | Cleaner, more elegant | More verbose |
| **Space Complexity** | O(h) stack space | O(1) extra space |
| **Risk** | Stack overflow for deep trees | No recursion risk |
| **Performance** | Slightly slower due to calls | Slightly faster |
| **Debugging** | Easier to understand | Harder to trace |

### When to Use Each

| Use Recursive When | Use Iterative When |
|--------------------|--------------------|
| Tree is relatively balanced | Tree may be very deep |
| Code readability is priority | Stack space is limited |
| Learning/teaching | Production code |
| Small to medium datasets | Large datasets |

---

## 🎯 Common Pitfalls

| Pitfall | Consequence | Solution |
|---------|-------------|----------|
| **Not updating parent links** | Broken tree structure | Always track parent in iterative |
| **Memory leak on duplicate** | Wasted memory | Delete or reuse duplicate node |
| **Stack overflow** | Program crash | Use iterative for deep trees |
| **Not handling empty tree** | Null pointer access | Check root == nullptr |
| **Incorrect comparison** | Violates BST property | Use consistent comparison logic |

---

## 💡 Best Practices

1. **Always maintain BST property** during insertion
2. **Handle duplicates explicitly** based on requirements
3. **Prefer iterative** for deep trees to avoid stack overflow
4. **Use recursion** for clarity when tree is balanced
5. **Update size counter** correctly on successful insertion
6. **Delete duplicate nodes** to prevent memory leaks
7. **Test edge cases**: empty tree, duplicates, min, max

---

## ✅ Key Takeaways

1. **Insertion follows BST property**: left < root < right
2. **Two approaches**: recursive (simpler) and iterative (safer)
3. **Time complexity**: O(log n) average, O(n) worst case
4. **Space complexity**: O(h) recursive, O(1) iterative
5. **Duplicates** can be handled by ignoring, counting, or storing
6. **Empty tree** is a valid state (insert becomes root)
7. **Skewed trees** cause worst-case O(n) performance

---