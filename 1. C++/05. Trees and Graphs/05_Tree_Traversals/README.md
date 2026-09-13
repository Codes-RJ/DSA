# Tree Traversals: Study Guide

[← Return to the main learning path](../../LEARNING_PATH.md)

- **Role:** Required in Checkpoint 5
- **Prerequisites:** Binary-tree vocabulary, node structure, recursion, stack, and queue
- **Core standard:** C++17

Tree traversal means visiting every node according to a deliberate order. For binary trees, depth-first traversal has three canonical orders, determined by when the root is processed. Breadth-first traversal is normally called level-order traversal.

## Required Order

| Order | Lesson | Central invariant or use |
|---:|---|---|
| 1 | [Inorder Traversal](03_Inorder_Traversal.md) | Left subtree, root, right subtree; yields sorted keys for a valid BST. |
| 2 | [Preorder Traversal](04_Preorder_Traversal.md) | Root before subtrees; useful for copying and serialization. |
| 3 | [Postorder Traversal](05_Postorder_Traversal.md) | Subtrees before root; useful for bottom-up properties and destruction. |
| 4 | [Level-Order Traversal](06_Level_Order_Traversal.md) | Queue contains the discovered nodes whose children have not yet been processed. |

## One Mental Model for Depth-First Traversal

```cpp
void traverse(Node* node) {
    if (node == nullptr) {
        return;
    }

    // Preorder position: process node here.
    traverse(node->left);
    // Inorder position: process node here.
    traverse(node->right);
    // Postorder position: process node here.
}
```

The recursive calls are the same; moving the processing step changes the order. Recursive auxiliary space is `O(h)`, where `h` is tree height. That is `O(log N)` for a height-balanced tree and `O(N)` for a completely skewed tree.

## Tree Traversal Versus Graph Traversal

A tree has a unique path from its root to every node, so a normal downward traversal does not need a visited set. A general graph may contain cycles and multiple paths, so its traversal must track visited vertices.

- For general graph depth-first search, use [Graph DFS](../06_Basic_Graph_Algorithms/02_Graph_Traversal_DFS.md).
- For general graph breadth-first search, use [Graph BFS](../06_Basic_Graph_Algorithms/01_Graph_Traversal_BFS.md).

Those graph lessons are the canonical owners of DFS/BFS terminology, component traversal, visited-state handling, and graph applications. This module owns binary-tree traversal orders only.

## Required Practice

- **Bridge:** Reproduce all four orders for the same seven-node tree by hand.
- **Validation:** [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- **Challenge:** [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) — determine the postorder state returned by each call.

For each implementation, test an empty tree, one node, a left-skewed tree, a right-skewed tree, and a balanced tree.

## Exit Task

Implement recursive and iterative inorder traversal plus level-order traversal. State:

1. what each stack or queue entry represents;
2. the visit order;
3. total time;
4. auxiliary space in terms of both `N` and height `h`;
5. why no visited set is needed for downward tree edges.

## Next Step

Continue to [Binary Search Trees](../02_BST/README.md).
