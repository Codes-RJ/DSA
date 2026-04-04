# Breadth-First Search (BFS) in Trees

## Introduction
Breadth-First Search (BFS), also known as **Level Order Traversal**, visits all nodes at the current level before moving to the next level. It starts at the root, then visits its children (level 1), then its grandchildren (level 2), and so on.

## Core Concept
BFS uses a **queue** data structure to keep track of nodes to visit. As each node is visited, its children are added to the back of the queue to be processed later.

## Iterative Implementation

```cpp
#include <iostream>
#include <queue>

using namespace std;

struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;
};

void BFS(TreeNode* root) {
    if (root == nullptr) return;

    queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
        TreeNode* current = q.front();
        q.pop();

        cout << current->data << " "; // Visit node

        if (current->left) q.push(current->left);
        if (current->right) q.push(current->right);
    }
}
```

## Space and Time Complexity

| Complexity | Explanation |
|------------|-------------|
| **Time Complexity** | O(N) where N is the number of nodes |
| **Space Complexity** | O(W) where W is the maximum width of the tree |

*Note: In a perfect binary tree, the width W is roughly N/2, so space complexity can be O(N) in the worst case for wide trees.*

## Why Breadth-First?
- Visits nodes level by level.
- Guaranteed to find the shortest path from the root to any other node (in terms of edges).
- Excellent for trees that are very deep but relatively narrow.

## Advantages
1. **Shortest Path**: Naturally finds the shortest distance from the source to any other node.
2. **Level-wise Information**: Useful whenever processing nodes based on their "depth" or "generation".

## Disadvantages
1. **Memory Usage**: Requires significant memory for wide trees, potentially much more than DFS.
2. **Queue Overhead**: Requires an auxiliary data structure (queue).
