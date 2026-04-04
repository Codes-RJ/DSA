# AVL Tree Deletion: Handling the Cascading Rebalance

## Overview
Deletion in an AVL tree is more complex than insertion because **the balance factor shift can propagate all the way to the root**. While a single rotation fixes balance after an insertion, a single rotation after a deletion can reduce the height of the current subtree, which in turn could cause an imbalance in its parent, and so on.

---

## 1. Comprehensive Recursive Deletion

```cpp
Node* deleteNode(Node* root, int key) {
    // Stage 1: Standard BST Deletion
    if (root == nullptr) return root;

    if (key < root->data) {
        root->left = deleteNode(root->left, key);
    } else if (key > root->data) {
        root->right = deleteNode(root->right, key);
    } else {
        // Node found! Determine children status
        if (root->left == nullptr || root->right == nullptr) {
            Node* temp = root->left ? root->left : root->right;

            if (temp == nullptr) { // Case: Leaf node
                delete root;
                return nullptr;
            } else { // Case: Node with one child
                *root = *temp; // Copy content of non-empty child
                delete temp; 
            }
        } else {
            // Case: Node with two children
            // Find inorder successor
            Node* temp = findMin(root->right);
            root->data = temp->data;
            root->right = deleteNode(root->right, temp->data);
        }
    }

    // Stage 2: Vital update for parent after modification
    if (root == nullptr) return root;

    root->height = 1 + std::max(getHeight(root->left), getHeight(root->right));
    int balance = getBF(root);

    // Stage 3: Identifying and Fixing Imbalance (Cascading)
    
    // Left-Heavy
    if (balance > 1) {
        // Left-Left or Left-Right? 
        // In deletion, we check the BF of the child.
        if (getBF(root->left) >= 0) {
            return rightRotate(root); // LL Case
        } else {
            root->left = leftRotate(root->left); // LR Case
            return rightRotate(root);
        }
    }

    // Right-Heavy
    if (balance < -1) {
        if (getBF(root->right) <= 0) {
            return leftRotate(root); // RR Case
        } else {
            root->right = rightRotate(root->right); // RL Case
            return leftRotate(root);
        }
    }

    return root;
}
```

---

## 2. The Cascading Effect: Why Multiple Rotations?
Consider a deletion that removes a node from the right subtree, making the current node left-heavy ($BF=2$). A right rotation will elevate the left child and push the current node down.
- **In Insertion**: Rotation restores the original height of the subtree.
- **In Deletion**: Rotation might result in a subtree height that is **smaller** than before. This reduction in height can cause an imbalance in the parent. Thus, we must check every ancestor back to the root ($O(\log N)$ checks).

---

## 3. Successor vs. Predecessor Choice
For Case 3 (two children), you can use either the inorder successor (min of right) or predecessor (max of left). To maintain tree symmetry and balance over millions of deletions, some implementations:
- Alternate between the two.
- Always choose the successor of the **taller** subtree.

---

## 4. Exceptions and Edge Cases
1. **Node Not Found**: The recursion reaches a `nullptr` base case and returns it back up. No heights change, no rotations occur.
2. **Deleting the Last Node**: The tree becomes empty (`root == nullptr`).
3. **One Child Case**: We copy the child's data into the parent then `delete` the child. This is a common shortcut to avoid re-linking pointers.

---

## Summary Comparison

| Feature | Insertion | Deletion |
|---------|-----------|----------|
| **Logic** | Find leaf, add, backtrack. | Find node, replace/delete, backtrack. |
| **Max Rotations** | **1** (single or double) | **$O(\log N)$** (cascading) |
| **BF Trigger** | New node added | Subtree removed |

## Checklist
- [ ] Are and `getHeight` and `getBF` used to safely handle null pointers?
- [ ] Is height updated **before** rebalancing?
- [ ] Does the two-child case recursively delete the successor to trigger its rebalance?
- [ ] Is the original node memory freed correctly?
