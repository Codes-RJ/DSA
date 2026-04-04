# AVL Tree Rotations: The Mechanics of Balance

## Overview
Rotations are the fundamental operations that re-balance an AVL tree while preserving its Binary Search Tree (BST) properties. A rotation changes the tree structure by moving nodes up or down, effectively shifting the height from a taller subtree to a shorter one.

---

## 1. Single Rotations (LL and RR Cases)

### Right Rotation (LL Case)
Triggered when the **Left Child of the Left Child** causes an imbalance in ancestral node $Z$.

**Visual Representation:**
```text
      Z (BF=2)           Y
     / \                / \
    Y   T4      --->   X   Z
   / \                / \ / \
  X   T3             T1 T2 T3 T4
 / \
T1 T2
```

**C++ Subtree Reattachment Logic:**
```cpp
Node* rightRotate(Node* z) {
    Node* y = z->left;
    Node* T3 = y->right;

    // Perform rotation
    y->right = z;
    z->left = T3;

    // Update heights (order matters! Update 'z' first as it's now a child of 'y')
    z->height = 1 + max(getHeight(z->left), getHeight(z->right));
    y->height = 1 + max(getHeight(y->left), getHeight(y->right));

    return y; // New root of this subtree
}
```

### Left Rotation (RR Case)
Triggered when the **Right Child of the Right Child** causes an imbalance in node $Z$. Symmetric to Right Rotation.

---

## 2. Double Rotations (LR and RL Cases)

### Left-Right Rotation (LR Case)
Triggered when the **Right Child of the Left Child** causes an imbalance. A single rotation is not enough because the inner subtree is too tall. We first turn it into an LL Case, then rotate.

**Algorithm:**
1. Perform **Left Rotation** on the Left Child (`z->left`).
2. Perform **Right Rotation** on the root node $Z$.

```cpp
// Logic inside balance() function
if (balance > 1 && key > root->left->data) {
    root->left = leftRotate(root->left); // Convert LR to LL
    return rightRotate(root);            // Solve LL
}
```

### Right-Left Rotation (RL Case)
Triggered when the **Left Child of the Right Child** causes an imbalance. Symmetric to LR.

---

## 3. The "Why" Behind Subtree Reattachment
Notice `T3` in the Right Rotation. It was the right child of `Y` (values $> Y$ and $< Z$). After `Z` becomes the right child of `Y`, $T3$ must be reattached to `Z` as its **new left child** to maintain the BST property ($Y < T3 < Z$).

---

## 4. Complexity and Performance

| Feature | Complexity | Rationale |
|---------|------------|-----------|
| **Time**| $O(1)$ | Only involves updating 3-4 pointers and 2 height values. |
| **Space**| $O(1)$ | No extra memory used (performed in-place). |

### Comparison: AVL vs. Red-Black Rotations
- **AVL Insertion**: At most 2 rotations (1 single or 1 double) to fix balance.
- **AVL Deletion**: Might require $O(\log N)$ rotations in the worst case as balance cascades up.
- **Red-Black Tree**: Guaranteed at most 2 rotations for insertion and 3 for deletion.

---

## 5. Critical Verification Checklist
- [ ] Is the inorder traversal (`T1 < X < T2 < Y < T3 < Z < T4`) identical before and after?
- [ ] Are heights updated for **both** nodes involved in the rotation?
- [ ] Is the height updated for the *lower* node before the *upper* node?
- [ ] Does the function return the *new* root of the subtree to the parent?
