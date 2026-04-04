# AVL Tree Insertion: Detailed Lifecycle

## Overview
Insertion in an AVL tree is a two-phase operation:
1.  **Phase 1 (Top-Down)**: The standard BST insertion where we find the correct leaf position for the new node.
2.  **Phase 2 (Bottom-Up)**: As the recursion stack unwinds, we update heights and perform rotations at the first node that becomes unbalanced.

---

## 1. The Full Implementation

```cpp
Node* insert(Node* node, int key) {
    // Stage 1: Standard BST Insertion
    if (node == nullptr) {
        return new Node(key);
    }
    
    if (key < node->data) {
        node->left = insert(node->left, key);
    } else if (key > node->data) {
        node->right = insert(node->right, key);
    } else {
        return node; // Duplicate keys are generally ignored in standard AVL
    }
    
    // Stage 2: Height Update and Balance
    node->height = 1 + max(getHeight(node->left), getHeight(node->right));
    int balance = getBF(node);
    
    // Stage 3: Identifying and Fixing Imbalance
    
    // Case 1: LL (Left-Left) - Needs Right Rotation
    if (balance > 1 && key < node->left->data) {
        return rightRotate(node);
    }
    
    // Case 2: RR (Right-Right) - Needs Left Rotation
    if (balance < -1 && key > node->right->data) {
        return leftRotate(node);
    }
    
    // Case 3: LR (Left-Right) - Needs Left-Right Rotation
    if (balance > 1 && key > node->left->data) {
        node->left = leftRotate(node->left);
        return rightRotate(node);
    }
    
    // Case 4: RL (Right-Left) - Needs Right-Left Rotation
    if (balance < -1 && key < node->right->data) {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }
    
    return node; // Return naturally if already balanced
}
```

---

## 2. Why Only One Rotation?
In an AVL **insertion**, once you perform the necessary rotation at the lowest unbalanced node, the height of *that specific subtree* returns to exactly what it was before the insertion. Consequently, all ancestors of this node will automatically become balanced again. This means insertion requires at most **one single or double rotation**.

---

## 3. Exceptions and Edge Cases
- **Handling Duplicates**: If duplicates must be stored, you can either increment a `count` field in the existing node ($O(\log N)$ search) or consistently place them in one subtree.
- **Memory Allocation Failure**: In a production-grade C++ environment, `new Node(key)` could throw `std::bad_alloc`. Always wrap it or use smart pointers.
- **Large Keys**: Be careful with very large values or complex objects if you are using them as keys; ensure the `operator<` and `operator>` are correctly defined.

---

## 4. Complexity Analysis

| Measure | Complexity | Rationale |
|---------|------------|-----------|
| **Search Time** | $O(\log N)$ | Standard BST navigation. |
| **Rotation Time** | $O(1)$ | Pointer swapping only. |
| **Space** | $O(\log N)$ | Recursion stack depth. |
| **Nodes Visited** | $2 \cdot \log N$ | Once going down, once coming up. |

---

## Summary Checklist
- [ ] Is the height of the current node updated **before** calculating the balance factor?
- [ ] Are the 4 imbalance cases correctly identified based on `key` and `balance`?
- [ ] Does the function correctly return the `new root` of each subtree?
- [ ] Is memory handled for the newly created leaf node?
