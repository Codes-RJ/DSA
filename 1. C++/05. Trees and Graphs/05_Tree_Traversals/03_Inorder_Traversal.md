# Inorder Traversal (LNR)

## Introduction
Inorder traversal is a depth-first traversal method where each node is visited between its left and right subtrees. For a **Binary Search Tree (BST)**, inorder traversal visits nodes in non-decreasing order.

## Traversal Steps (LNR)
1. Recursively visit the **Left** subtree.
2. Visit the **Node** (the current node).
3. Recursively visit the **Right** subtree.

## C++ Implementation

### Recursive Method
```cpp
void inorderTraversal(TreeNode* root) {
    if (root == nullptr) return;

    inorderTraversal(root->left);
    cout << root->data << " ";
    inorderTraversal(root->right);
}
```

### Iterative Method
```cpp
#include <stack>

void inorderIterative(TreeNode* root) {
    stack<TreeNode*> s;
    TreeNode* current = root;

    while (current != nullptr || !s.empty()) {
        while (current != nullptr) {
            s.push(current);
            current = current->left;
        }
        current = s.top();
        s.pop();
        cout << current->data << " ";
        current = current->right;
    }
}
```

## Key Properties
- **BST Inorder**: Always yields a sorted sequence of values.
- **Arithmetic Expressions**: If an expression tree is traversed inorder, it yields the infix notation (though parentheses might be needed).

## Time and Space Complexity
- **Time**: O(N)
- **Space**: O(H) (due to call stack or explicit stack)

## Use Cases
- Sorting elements in a Binary Search Tree.
- Validating if a tree is a BST.
- Converting expression trees back to infix notation.
