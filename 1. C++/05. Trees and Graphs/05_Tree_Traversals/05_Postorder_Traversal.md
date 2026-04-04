# Postorder Traversal (LRN)

## Introduction
Postorder traversal is a depth-first traversal method where the root node is visited **after** both of its subtrees have been processed.

## Traversal Steps (LRN)
1. Recursively visit the **Left** subtree.
2. Recursively visit the **Right** subtree.
3. Visit the **Node** (the current node).

## C++ Implementation

### Recursive Method
```cpp
void postorderTraversal(TreeNode* root) {
    if (root == nullptr) return;

    postorderTraversal(root->left);
    postorderTraversal(root->right);
    cout << root->data << " ";
}
```

### Iterative Method (Two Stacks)
```cpp
#include <stack>

void postorderIterative(TreeNode* root) {
    if (root == nullptr) return;

    stack<TreeNode*> s1, s2;
    s1.push(root);

    while (!s1.empty()) {
        TreeNode* current = s1.top();
        s1.pop();
        s2.push(current);

        if (current->left) s1.push(current->left);
        if (current->right) s1.push(current->right);
    }

    while (!s2.empty()) {
        cout << s2.top()->data << " ";
        s2.pop();
    }
}
```

## Key Properties
- **Post-order Deletion**: Essential for deleting a tree from the bottom up to avoid memory leaks.
- **Dependency Calculation**: Useful where child calculations are necessary before parent results can be computed.

## Time and Space Complexity
- **Time**: O(N)
- **Space**: O(H) (or O(N) for iterative 2-stack approach)

## Use Cases
- Tree deletion (freeing memory).
- Evaluating arithmetic expression trees (postfix notation).
- Calculating the size or height of a tree.
- Computing dependencies in build systems.
