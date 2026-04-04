# Preorder Traversal (NLR)

## Introduction
Preorder traversal is a depth-first traversal method where the root node is visited **before** its subtrees.

## Traversal Steps (NLR)
1. Visit the **Node** (the current node).
2. Recursively visit the **Left** subtree.
3. Recursively visit the **Right** subtree.

## C++ Implementation

### Recursive Method
```cpp
void preorderTraversal(TreeNode* root) {
    if (root == nullptr) return;

    cout << root->data << " ";
    preorderTraversal(root->left);
    preorderTraversal(root->right);
}
```

### Iterative Method
```cpp
#include <stack>

void preorderIterative(TreeNode* root) {
    if (root == nullptr) return;

    stack<TreeNode*> s;
    s.push(root);

    while (!s.empty()) {
        TreeNode* current = s.top();
        s.pop();
        cout << current->data << " ";

        // Push right first so that left is processed first
        if (current->right) s.push(current->right);
        if (current->left) s.push(current->left);
    }
}
```

## Key Properties
- **Cloning a Tree**: Preorder is the most natural way to create a copy of a tree.
- **Serialization**: Often used to serialize a tree structure for storage or transmission.

## Time and Space Complexity
- **Time**: O(N)
- **Space**: O(H)

## Use Cases
- Creating a prefix expression from an expression tree.
- Copying/cloning a directory structure or file tree.
- Printing a document structure (chapters, then sections, then paragraphs).
