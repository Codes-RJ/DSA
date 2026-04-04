# BST Search and Queries: Beyond Basic Lookup

## Overview
Search in a Binary Search Tree (BST) is not just about finding a value. It's the foundation for many complex queries like range finding, nearest neighbors (floor/ceiling), and statistical analysis (k-th smallest). In a balanced BST, search operations run in $O(\log N)$ time, making them exceptionally efficient for large datasets.

---

## 1. Finding Extremes: Minimum and Maximum
Because of the BST property, the minimum element is always the "leftmost" node, and the maximum is the "rightmost" node.

### Recursive Implementation
```cpp
Node* findMin(Node* root) {
    if (root == nullptr) return nullptr;
    if (root->left == nullptr) return root;
    return findMin(root->left);
}

Node* findMax(Node* root) {
    if (root == nullptr) return nullptr;
    if (root->right == nullptr) return root;
    return findMax(root->right);
}
```

### Iterative Implementation (O(1) Space)
```cpp
Node* findMinIterative(Node* root) {
    if (root == nullptr) return nullptr;
    while (root->left != nullptr) root = root->left;
    return root;
}
```

---

## 2. Near-Neighbor Queries: Floor and Ceiling
- **Floor**: Largest element $\le$ key.
- **Ceiling**: Smallest element $\ge$ key.

### Ceiling Algorithm
1. If node's key == target, return node.
2. If node's key < target, ceiling must be in the right subtree.
3. If node's key > target, node *could* be the ceiling, or it's in the left subtree.

```cpp
int ceiling(Node* root, int key) {
    int res = -1;
    while (root) {
        if (root->data == key) return root->data;
        if (root->data < key) {
            root = root->right;
        } else {
            res = root->data;
            root = root->left;
        }
    }
    return res;
}
```

---

## 3. Order Statistics: K-th Smallest / Largest
To find the k-th smallest element efficiently, we can use an augmented BST where each node stores the size of its subtree.

### Implementation (With Augmented Size)
```cpp
struct Node {
    int data, size; // size = 1 + left->size + right->size
    Node *left, *right;
};

Node* kthSmallest(Node* root, int k) {
    if (root == nullptr) return nullptr;

    int leftSize = (root->left) ? root->left->size : 0;

    if (leftSize + 1 == k) return root;
    if (leftSize >= k) return kthSmallest(root->left, k);
    return kthSmallest(root->right, k - leftSize - 1);
}
```

---

## 4. Finding Successor and Predecessor
Essential for navigation without a full traversal.

### Inorder Successor for a Given Node
1. If node has a right child: Successor is `findMin(node->right)`.
2. If node has no right child: Successor is one of its ancestors. It's the closest ancestor for which the node is in the left subtree.

```cpp
Node* getSuccessor(Node* root, Node* target) {
    if (target->right != nullptr)
        return findMin(target->right);

    Node* successor = nullptr;
    while (root != nullptr) {
        if (target->data < root->data) {
            successor = root;
            root = root->left;
        } else if (target->data > root->data) {
            root = root->right;
        } else break;
    }
    return successor;
}
```

---

## 5. Range Queries and Counting
Finding all elements $x$ such that $L \le x \le R$.

### Optimization: Pruning
Don't explore subtrees that are entirely outside the range.
```cpp
void rangePrint(Node* root, int L, int R) {
    if (root == nullptr) return;

    // Prune left subtree if root's data is already less than L
    if (L < root->data) rangePrint(root->left, L, R);

    // Process current node
    if (L <= root->data && root->data <= R) cout << root->data << " ";

    // Prune right subtree if root's data is already greater than R
    if (R > root->data) rangePrint(root->right, L, R);
}
```

---

## Edge Cases and Exceptions

| Case | Exception | Recovery/Handling |
|------|-----------|-------------------|
| **Empty Tree** | `nullptr` access | Always check `if (root == nullptr)` as the first line of any search function. |
| **Element Not Found** | Returning `INT_MIN` or `-1` | Use a `bool* found` parameter or return a sentinel value. In modern C++, consider `std::optional<int>`. |
| **Duplicates** | Multiple valid paths | Decide (and document) if duplicates go to the left or right. Standard BST apps usually avoid them or store a `count` per node. |
| **K > N** | Requesting 10th element in tree of 5 | Check `k <= root->size` before calling order statistic functions. |

---

## Complexity Summary

| Operation | Best Case | Average Case | Worst Case (Skewed) |
|-----------|-----------|--------------|---------------------|
| Search    | $O(1)$    | $O(\log N)$  | $O(N)$              |
| Min/Max   | $O(1)$    | $O(\log N)$  | $O(N)$              |
| Successor | $O(1)$    | $O(\log N)$  | $O(N)$              |
| Range     | $O(\text{Range Size} + H)$ | $O(K + \log N)$ | $O(N)$ |
