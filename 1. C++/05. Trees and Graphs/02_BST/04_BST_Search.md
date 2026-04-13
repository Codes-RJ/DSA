# BST Search

## 📖 Overview

Searching in a Binary Search Tree (BST) is the most fundamental operation that leverages the BST property to achieve efficient lookups. The algorithm exploits the ordered nature of BSTs to eliminate half of the remaining tree at each step, similar to binary search on a sorted array.

---

## 🎯 Search Algorithm

### Basic Principle

The search algorithm follows the BST property to locate a target value:

```
1. Start at the root
2. If root is null → target not found
3. If target equals current node's value → found
4. If target < current node's value → search left subtree
5. If target > current node's value → search right subtree
6. Repeat until found or leaf reached
```

### Visual Example

```
Search for 70:

        50
       /  \
      30   80
     / \   / \
    20 40 70 90
           ↑
         found!

Step 1: Start at 50 → 70 > 50 → go right
Step 2: At 80 → 70 < 80 → go left
Step 3: At 70 → 70 == 70 → found!
```

---

## 📝 Recursive Search

### Implementation

```cpp
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
    
    // Recursive search helper
    bool searchRecursive(Node* node, const T& target) const {
        // Base case: not found
        if (node == nullptr) {
            return false;
        }
        
        // Base case: found
        if (target == node->data) {
            return true;
        }
        
        // Recursive cases
        if (target < node->data) {
            return searchRecursive(node->left, target);
        } else {
            return searchRecursive(node->right, target);
        }
    }
    
    // Recursive search returning node pointer
    Node* findNodeRecursive(Node* node, const T& target) const {
        if (node == nullptr || node->data == target) {
            return node;
        }
        
        if (target < node->data) {
            return findNodeRecursive(node->left, target);
        } else {
            return findNodeRecursive(node->right, target);
        }
    }
    
public:
    bool search(const T& target) const {
        return searchRecursive(root, target);
    }
    
    Node* find(const T& target) const {
        return findNodeRecursive(root, target);
    }
};
```

### Step-by-Step Execution

```
Search for 40 in tree:

Call 1: searchRecursive(root=50, target=40)
    40 < 50 → go left
    Call 2: searchRecursive(node=30, target=40)
        40 > 30 → go right
        Call 3: searchRecursive(node=40, target=40)
            target == node.data → return true

Result: true (found)
```

---

## 🔄 Iterative Search

### Implementation

```cpp
template<typename T>
bool BST<T>::searchIterative(const T& target) const {
    Node* current = root;
    
    while (current != nullptr) {
        if (target == current->data) {
            return true;
        } else if (target < current->data) {
            current = current->left;
        } else {
            current = current->right;
        }
    }
    
    return false;
}

template<typename T>
typename BST<T>::Node* BST<T>::findIterative(const T& target) const {
    Node* current = root;
    
    while (current != nullptr && current->data != target) {
        if (target < current->data) {
            current = current->left;
        } else {
            current = current->right;
        }
    }
    
    return current;
}
```

### Visual Walkthrough

```
Search for 25 in tree:

        50
       /  \
      30   80
     / \   / \
    20 40 70 90

Step 1: current = 50
    25 < 50 → current = 30

Step 2: current = 30
    25 < 30 → current = 20

Step 3: current = 20
    25 > 20 → current = nullptr

Step 4: current == nullptr → return false
```

---

## 📊 Complexity Analysis

### Time Complexity

| Case | Complexity | Description |
|------|------------|-------------|
| **Best Case** | O(1) | Target is at the root |
| **Average Case** | O(log n) | Tree is reasonably balanced |
| **Worst Case** | O(n) | Tree is skewed (like linked list) |

### Space Complexity

| Implementation | Space | Description |
|----------------|-------|-------------|
| **Recursive** | O(h) | Call stack depth equals height |
| **Iterative** | O(1) | No recursion overhead |

### Height Analysis

```
Perfect tree (height 3, 15 nodes):
    Search requires at most 4 comparisons
    log₂(15) ≈ 4

Skewed tree (height 4, 5 nodes):
    1
     \
      2
       \
        3
         \
          4
           \
            5
    Search for 5 requires 5 comparisons (O(n))
```

---

## 🎯 Search Patterns

### Find Minimum Value

```cpp
T findMin() const {
    if (root == nullptr) {
        throw runtime_error("Tree is empty");
    }
    
    Node* current = root;
    while (current->left != nullptr) {
        current = current->left;
    }
    return current->data;
}
```

### Find Maximum Value

```cpp
T findMax() const {
    if (root == nullptr) {
        throw runtime_error("Tree is empty");
    }
    
    Node* current = root;
    while (current->right != nullptr) {
        current = current->right;
    }
    return current->data;
}
```

### Find Successor (Next Larger Value)

```cpp
T findSuccessor(const T& target) const {
    Node* node = find(target);
    if (node == nullptr) return T();
    
    // Case 1: Node has right subtree
    if (node->right != nullptr) {
        Node* current = node->right;
        while (current->left != nullptr) {
            current = current->left;
        }
        return current->data;
    }
    
    // Case 2: No right subtree - go up
    Node* successor = nullptr;
    Node* current = root;
    
    while (current != nullptr) {
        if (target < current->data) {
            successor = current;
            current = current->left;
        } else if (target > current->data) {
            current = current->right;
        } else {
            break;
        }
    }
    
    return successor ? successor->data : T();
}
```

### Find Predecessor (Next Smaller Value)

```cpp
T findPredecessor(const T& target) const {
    Node* node = find(target);
    if (node == nullptr) return T();
    
    // Case 1: Node has left subtree
    if (node->left != nullptr) {
        Node* current = node->left;
        while (current->right != nullptr) {
            current = current->right;
        }
        return current->data;
    }
    
    // Case 2: No left subtree - go up
    Node* predecessor = nullptr;
    Node* current = root;
    
    while (current != nullptr) {
        if (target < current->data) {
            current = current->left;
        } else if (target > current->data) {
            predecessor = current;
            current = current->right;
        } else {
            break;
        }
    }
    
    return predecessor ? predecessor->data : T();
}
```

---

## 🔍 Range Search

### Find All Nodes in Range [low, high]

```cpp
void findInRange(Node* node, const T& low, const T& high, vector<T>& result) const {
    if (node == nullptr) return;
    
    // If current node is greater than low, search left subtree
    if (low < node->data) {
        findInRange(node->left, low, high, result);
    }
    
    // If current node is within range, add to result
    if (low <= node->data && node->data <= high) {
        result.push_back(node->data);
    }
    
    // If current node is less than high, search right subtree
    if (node->data < high) {
        findInRange(node->right, low, high, result);
    }
}

vector<T> rangeSearch(const T& low, const T& high) const {
    vector<T> result;
    findInRange(root, low, high, result);
    return result;
}
```

### Example

```
Tree:                    Range search [25, 75]:
        50                   Results: 30, 40, 50, 70
       /  \
      30   80
     / \   / \
    20 40 70 90

Nodes in range: 30, 40, 50, 70
```

---

## 💻 Complete Implementation

```cpp
#include <iostream>
#include <vector>
#include <stdexcept>
using namespace std;

template<typename T>
class BinarySearchTree {
private:
    struct Node {
        T data;
        Node* left;
        Node* right;
        
        Node(const T& value) : data(value), left(nullptr), right(nullptr) {}
    };
    
    Node* root;
    size_t nodeCount;
    
    // Recursive search helpers
    bool searchRecursive(Node* node, const T& target) const {
        if (node == nullptr) return false;
        if (target == node->data) return true;
        
        if (target < node->data) {
            return searchRecursive(node->left, target);
        } else {
            return searchRecursive(node->right, target);
        }
    }
    
    Node* findNodeRecursive(Node* node, const T& target) const {
        if (node == nullptr || node->data == target) {
            return node;
        }
        
        if (target < node->data) {
            return findNodeRecursive(node->left, target);
        } else {
            return findNodeRecursive(node->right, target);
        }
    }
    
    void rangeSearchRecursive(Node* node, const T& low, const T& high, vector<T>& result) const {
        if (node == nullptr) return;
        
        if (low < node->data) {
            rangeSearchRecursive(node->left, low, high, result);
        }
        
        if (low <= node->data && node->data <= high) {
            result.push_back(node->data);
        }
        
        if (node->data < high) {
            rangeSearchRecursive(node->right, low, high, result);
        }
    }
    
public:
    BinarySearchTree() : root(nullptr), nodeCount(0) {}
    
    // Insert (simplified for demonstration)
    void insert(const T& value) {
        // Insert implementation (covered in previous section)
        // For brevity, assume insert exists
    }
    
    // Search methods
    bool search(const T& target) const {
        return searchRecursive(root, target);
    }
    
    bool searchIterative(const T& target) const {
        Node* current = root;
        
        while (current != nullptr) {
            if (target == current->data) return true;
            if (target < current->data) {
                current = current->left;
            } else {
                current = current->right;
            }
        }
        
        return false;
    }
    
    Node* find(const T& target) const {
        return findNodeRecursive(root, target);
    }
    
    // Min/Max
    T findMin() const {
        if (root == nullptr) {
            throw runtime_error("Tree is empty");
        }
        
        Node* current = root;
        while (current->left != nullptr) {
            current = current->left;
        }
        return current->data;
    }
    
    T findMax() const {
        if (root == nullptr) {
            throw runtime_error("Tree is empty");
        }
        
        Node* current = root;
        while (current->right != nullptr) {
            current = current->right;
        }
        return current->data;
    }
    
    // Successor/Predecessor
    T findSuccessor(const T& target) const {
        Node* node = find(target);
        if (node == nullptr) return T();
        
        // Has right subtree
        if (node->right != nullptr) {
            Node* current = node->right;
            while (current->left != nullptr) {
                current = current->left;
            }
            return current->data;
        }
        
        // No right subtree - go up
        Node* successor = nullptr;
        Node* current = root;
        
        while (current != nullptr) {
            if (target < current->data) {
                successor = current;
                current = current->left;
            } else if (target > current->data) {
                current = current->right;
            } else {
                break;
            }
        }
        
        if (successor == nullptr) {
            throw runtime_error("No successor found");
        }
        return successor->data;
    }
    
    T findPredecessor(const T& target) const {
        Node* node = find(target);
        if (node == nullptr) return T();
        
        // Has left subtree
        if (node->left != nullptr) {
            Node* current = node->left;
            while (current->right != nullptr) {
                current = current->right;
            }
            return current->data;
        }
        
        // No left subtree - go up
        Node* predecessor = nullptr;
        Node* current = root;
        
        while (current != nullptr) {
            if (target < current->data) {
                current = current->left;
            } else if (target > current->data) {
                predecessor = current;
                current = current->right;
            } else {
                break;
            }
        }
        
        if (predecessor == nullptr) {
            throw runtime_error("No predecessor found");
        }
        return predecessor->data;
    }
    
    // Range search
    vector<T> rangeSearch(const T& low, const T& high) const {
        vector<T> result;
        rangeSearchRecursive(root, low, high, result);
        return result;
    }
    
    // Utility
    bool empty() const { return root == nullptr; }
    size_t size() const { return nodeCount; }
};

int main() {
    BinarySearchTree<int> bst;
    
    // Insert values
    int values[] = {50, 30, 80, 20, 40, 70, 90, 55, 85};
    for (int v : values) {
        bst.insert(v);
    }
    
    // Test search
    cout << "=== Search Tests ===" << endl;
    cout << "Search 40: " << (bst.search(40) ? "Found" : "Not found") << endl;
    cout << "Search 100: " << (bst.search(100) ? "Found" : "Not found") << endl;
    
    // Test min/max
    cout << "\n=== Min/Max ===" << endl;
    cout << "Minimum: " << bst.findMin() << endl;
    cout << "Maximum: " << bst.findMax() << endl;
    
    // Test successor/predecessor
    cout << "\n=== Successor/Predecessor ===" << endl;
    cout << "Successor of 40: " << bst.findSuccessor(40) << endl;
    cout << "Predecessor of 80: " << bst.findPredecessor(80) << endl;
    
    // Test range search
    cout << "\n=== Range Search [30, 70] ===" << endl;
    vector<int> range = bst.rangeSearch(30, 70);
    for (int val : range) {
        cout << val << " ";
    }
    cout << endl;
    
    return 0;
}
```

---

## 📊 Performance Comparison

### Recursive vs Iterative Search

| Aspect | Recursive | Iterative |
|--------|-----------|-----------|
| **Code Clarity** | Cleaner, more intuitive | More verbose |
| **Space Complexity** | O(h) stack space | O(1) extra space |
| **Risk** | Stack overflow for deep trees | No recursion risk |
| **Performance** | Slightly slower | Slightly faster |

### When to Use Each

| Use Recursive When | Use Iterative When |
|--------------------|--------------------|
| Tree is balanced | Tree may be very deep |
| Code readability is priority | Stack space is limited |
| Learning/teaching | Production code |
| Small to medium trees | Large trees |

---

## 🎯 Common Search Problems

| Problem | Solution Approach |
|---------|-------------------|
| **Lowest Common Ancestor** | Recursive search from root |
| **K-th Smallest Element** | Inorder traversal with counter |
| **Validate BST** | Check range constraints recursively |
| **Two Sum in BST** | Inorder traversal + two pointers |
| **Closest Value** | Track closest during traversal |

---

## 💡 Best Practices

1. **Use iterative search** for deep trees to avoid stack overflow
2. **Return node pointer** when additional operations needed
3. **Handle empty tree** gracefully (return false/nullptr)
4. **Use const correctness** for search methods
5. **Leverage BST property** to eliminate half the tree
6. **Consider balanced trees** for guaranteed O(log n) search

---

## ✅ Key Takeaways

1. **Search exploits BST property**: left < root < right
2. **Time complexity**: O(log n) average, O(n) worst case
3. **Space complexity**: O(h) recursive, O(1) iterative
4. **Min/Max** are found by traversing left/right completely
5. **Successor** is smallest node in right subtree
6. **Predecessor** is largest node in left subtree
7. **Range search** uses modified inorder traversal
8. **Recursive search** is elegant but uses stack space

---
---

## Next Step

- Go to [05_BST_Traversal.md](05_BST_Traversal.md) to continue with BST Traversal.
