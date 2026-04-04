# AVL Balance Factor and Height Maintenance

## Overview
The Balance Factor (BF) is the biological clock of an AVL tree. It tells each node whether it's "growing" correctly or becoming "unbalanced." Without efficient height maintenance, every balance check would take $O(N)$ time, destroying the very efficiency AVL trees are designed to provide.

---

## 1. Defining Height vs. Depth
- **Depth**: How far the node is from the root (Root = 0).
- **Height**: The length of the longest path from the node down to a leaf (Leaf = 1).
- **Null Height**: To make calculations work, `nullptr` height is strictly defined as **0**.

---

## 2. Robust Height Implementation
In production systems, we must handle `nullptr` safely to prevent segmentation faults.

```cpp
// Safe Height Getter
int getHeight(Node* n) {
    return n ? n->height : 0;
}

// Update Height using children
void updateHeight(Node* n) {
    if (n) {
        n->height = 1 + std::max(getHeight(n->left), getHeight(n->right));
    }
}
```

---

## 3. The Balance Factor States

| BF Value | State | Action Required |
|----------|-------|-----------------|
| **-1** | Right-leaning | None (Wait for next modification) |
| **0** | Perfectly Balanced | None |
| **1** | Left-leaning | None (Wait for next modification) |
| **$\|BF\| > 1$** | **CRITICAL UNBALANCE** | **IMMEDIATE ROTATION** |

---

## 4. Rebalancing Logic: Under the Hood
The `balance()` function is typically called at the end of every recursive `insert` or `delete` call as the recursion unwinds ("bubbles up").

```cpp
Node* balance(Node* n) {
    updateHeight(n); // Step 1: Update current node's height
    int bf = getBF(n); // Step 2: Calculate balance factor

    // Case 1: Left-Heavy
    if (bf > 1) {
        // Sub-case: LR (Left-Right)
        if (getBF(n->left) < 0) {
            n->left = leftRotate(n->left);
        }
        return rightRotate(n);
    }

    // Case 2: Right-Heavy
    if (bf < -1) {
        // Sub-case: RL (Right-Left)
        if (getBF(n->right) > 0) {
            n->right = rightRotate(n->right);
        }
        return leftRotate(n);
    }

    return n; // Balanced
}
```

---

## 5. Mathematical Complexity

| Feature | Complexity | Rationale |
|---------|------------|-----------|
| **Verification**| $O(1)$ | Accessing the `height` field is constant. |
| **Recalculation**| $O(1)$ | Only looks at the `height` of two direct children. |
| **Total Overhead**| $O(\log N)$| In total, we update $\log N$ nodes from the point of insertion back to the root. |

---

## Summary Checklist
- [ ] Is height updated **after** every child modification?
- [ ] Does `getBF` handle `nullptr` gracefully?
- [ ] Is the height of a leaf node consistently defined as 1 (or 0, depending on convention)?
- [ ] Does the `balance` function distinguish between LL/LR and RR/RL sub-cases?
