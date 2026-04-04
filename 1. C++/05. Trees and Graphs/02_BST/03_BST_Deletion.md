# BST Deletion: Comprehensive Guide

## Overview
Deletion in a Binary Search Tree (BST) is one of the most intricate operations because it requires restructuring the tree to maintain the **BST invariant**: for every node, all values in its left subtree must be smaller, and all values in its right subtree must be larger.

## The Three Core Cases of Deletion

### Case 1: Node is a Leaf (0 Children)
- **Scenario**: The node has no children (`left == nullptr` and `right == nullptr`).
- **Action**: Simply delete the node and set the corresponding parent pointer to `nullptr`.
- **Memory Management**: In C++, ensure the memory is freed using `delete`.

### Case 2: Node has One Child
- **Scenario**: The node has either a left child or a right child, but not both.
- **Action**: The single child "jumps up" to take the place of the deleted node. The parent of the deleted node now points directly to the deleted node's child.
- **Visual**: Like removing a link in a chain and connecting the two adjacent links.

### Case 3: Node has Two Children
- **Scenario**: The node has both left and right subtrees.
- **Action**: You cannot simply remove this node as it would orphan two subtrees. Instead:
    1. Find a "replacement" node that can maintain the BST property. This is either:
        - **Inorder Successor**: The smallest value in the right subtree (`findMin(node->right)`).
        - **Inorder Predecessor**: The largest value in the left subtree (`findMax(node->left)`).
    2. Copy the data from the replacement node to the target node.
    3. Recursively delete the replacement node from its original position (which will now be a Case 1 or Case 2 deletion).

---

## Detailed Recursive Implementation

```cpp
#include <iostream>

struct Node {
    int data;
    Node *left, *right;
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

class BST {
public:
    Node* root;

    BST() : root(nullptr) {}

    // Find the minimum node in a given subtree
    Node* findMin(Node* node) {
        while (node && node->left != nullptr) {
            node = node->left;
        }
        return node;
    }

    Node* remove(Node* root, int key) {
        // Base Case: Key not found
        if (root == nullptr) return nullptr;

        // Standard BST Search
        if (key < root->data) {
            root->left = remove(root->left, key);
        } else if (key > root->data) {
            root->right = remove(root->right, key);
        } 
        // We found the node to be deleted
        else {
            // Case 1 & 2: Node with 0 or 1 child
            if (root->left == nullptr) {
                Node* temp = root->right;
                delete root;
                return temp;
            } else if (root->right == nullptr) {
                Node* temp = root->left;
                delete root;
                return temp;
            }

            // Case 3: Node with two children
            // Get the inorder successor (smallest in the right subtree)
            Node* temp = findMin(root->right);

            // Copy the inorder successor's content to this node
            root->data = temp->data;

            // Delete the inorder successor
            root->right = remove(root->right, temp->data);
        }
        return root;
    }
};
```

---

## Iterative Implementation (The "Hard" Way)
Iterative deletion is more complex as you must manually track parent pointers.

```cpp
void deleteIterative(Node* &root, int key) {
    Node* curr = root;
    Node* prev = nullptr;

    // Search for the node and its parent
    while (curr != nullptr && curr->data != key) {
        prev = curr;
        if (key < curr->data) curr = curr->left;
        else curr = curr->right;
    }

    if (curr == nullptr) return; // Key not found

    // Case: At least one child is null
    if (curr->left == nullptr || curr->right == nullptr) {
        Node* newCurr;
        if (curr->left == nullptr) newCurr = curr->right;
        else newCurr = curr->left;

        if (prev == nullptr) { // Deleting the root
            root = newCurr;
        } else {
            if (curr == prev->left) prev->left = newCurr;
            else prev->right = newCurr;
        }
        delete curr;
    } 
    // Case: Both children exist
    else {
        Node* p = nullptr;
        Node* temp;

        // Compute the inorder successor
        temp = curr->right;
        while (temp->left != nullptr) {
            p = temp;
            temp = temp->left;
        }

        if (p != nullptr) p->left = temp->right;
        else curr->right = temp->right;

        curr->data = temp->data;
        delete temp;
    }
}
```

---

## Edge Cases and Exceptions

1. **Empty Tree**: The function should return `nullptr` immediately.
2. **Value Not Found**: The tree remains unchanged; recursion reaches `nullptr` and returns.
3. **Deleting the Root**:
    - If the root is a leaf, `root` becomes `nullptr`.
    - If the root has one child, the child becomes the new root.
    - If the root has two children, its value is replaced and the successor is deleted.
4. **Duplicates**: 
    - Standard BSTs don't allow duplicates. 
    - If they do (e.g., duplicates in the right subtree), the `remove` logic must consistently target either the first or last occurrence.
5. **Memory Leaks**: Always `delete` the specific node being removed. Using `Smart Pointers` (`std::unique_ptr`) can automate this but adds complexity to tree restructuring.

---

## Complexity Analysis

| Scenario | Time Complexity | Space Complexity |
|----------|-----------------|------------------|
| **Average Case (Balanced)** | $O(\log N)$ | $O(H)$ (Recursive) / $O(1)$ (Iterative) |
| **Worst Case (Skewed)** | $O(N)$ | $O(N)$ (Recursive) / $O(1)$ (Iterative) |

---

## Successor vs. Predecessor
- **Inorder Successor**: Smallest node in the right subtree. Advantageous if the right subtree is taller.
- **Inorder Predecessor**: Largest node in the left subtree. Advantageous if the left subtree is taller.
- **Optimization Tip**: In a production environment (like `std::set`), the choice between successor and predecessor can be randomized or based on subtree heights to help keep the tree balanced during many deletions.
