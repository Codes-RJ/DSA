# Depth-First Search (DFS) in Trees

## Introduction
Depth-First Search (DFS) for a tree is an algorithm for traversing or searching tree data structures. It starts at the root and explores as far as possible along each branch before backtracking.

## Subtypes of DFS
In binary trees, there are three common orders for DFS:
1. **Preorder**: (Root, Left, Right)
2. **Inorder**: (Left, Root, Right)
3. **Postorder**: (Left, Right, Root)

## Core Concept
DFS is naturally recursive. It uses a **stack** data structure (implicitly via the call stack in recursion, or explicitly in iterative approaches) to keep track of the path and facilitate backtracking.

## Recursive Implementation Template

```cpp
void DFS(TreeNode* root) {
    if (root == nullptr) return;

    // Process Root (Position depends on Pre/In/Post order)
    DFS(root->left);
    // Process Root (Inorder)
    DFS(root->right);
    // Process Root (Postorder)
}
```

## Space and Time Complexity

| Complexity | Explanation |
|------------|-------------|
| **Time Complexity** | O(N) where N is the number of nodes |
| **Space Complexity** | O(H) where H is the height of the tree |

*Note: In the worst case (a skewed tree), H = N, leading to O(N) space. For balanced trees, H = log N.*

## Why Depth-First?
- Uses less memory than BFS for deep, narrow trees.
- Naturally represents genealogical relationships or hierarchical dependencies.
- Fundamental for solving many advanced tree problems (lowest common ancestor, path finding).

## Advantages
1. **Simple Implementation**: Recursive solutions are very concise.
2. **Path Finding**: Useful when you need to find a path from root to a specific node or leaf.
3. **Memory Efficient**: In a well-balanced tree, space usage is logarithmic relative to the number of nodes.

## Disadvantages
1. **Recursion Depth**: Can cause stack overflow for very deep trees if using recursion.
2. **Not Optimal for Shortest Path**: DFS might find a deeper node before finding a shallower one on a different branch.
