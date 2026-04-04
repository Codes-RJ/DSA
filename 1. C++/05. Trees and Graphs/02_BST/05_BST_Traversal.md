# BST Traversal Masterclass: Efficiency and Variants

## Overview
Traversal is the process of visiting every node in a tree exactly once. While basic recursion is simple, advanced scenarios require iterative approaches (to avoid stack overflow), space-optimized methods like Morris Traversal, or specialized patterns like Zig-Zag and Boundary traversals.

---

## 1. Iterative Traversal (Stack-Based)
Iterative methods are preferred in production systems where tree depth might exceed the stack limit.

### Iterative Inorder
```cpp
void iterativeInorder(Node* root) {
    stack<Node*> s;
    Node* curr = root;

    while (curr != nullptr || !s.empty()) {
        while (curr != nullptr) {
            s.push(curr);
            curr = curr->left;
        }
        curr = s.top();
        s.pop();
        cout << curr->data << " ";
        curr = curr->right;
    }
}
```

---

## 2. Morris Traversal: O(1) Space
Morris Traversal uses **Threaded Binary Trees** (temporarily using null pointers to link back to ancestors) to achieve traversal without a stack or recursion.

### Implementation (Inorder)
```cpp
void morrisInorder(Node* root) {
    Node *curr = root, *pre;

    while (curr != nullptr) {
        if (curr->left == nullptr) {
            cout << curr->data << " ";
            curr = curr->right;
        } else {
            // Find inorder predecessor
            pre = curr->left;
            while (pre->right != nullptr && pre->right != curr)
                pre = pre->right;

            // Make curr as right child of its inorder predecessor
            if (pre->right == nullptr) {
                pre->right = curr;
                curr = curr->left;
            } 
            // Revert the changes (untie)
            else {
                pre->right = nullptr;
                cout << curr->data << " ";
                curr = curr->right;
            }
        }
    }
}
```

---

## 3. Specialized Layout Traversals

### Zig-Zag (Spiral) Traversal
Uses two stacks to alternate direction at each level.
```cpp
void zigZagTraversal(Node* root) {
    if (!root) return;
    stack<Node*> s1, s2; // Current level, next level
    s1.push(root);

    bool leftToRight = true;
    while (!s1.empty()) {
        Node* temp = s1.top();
        s1.pop();
        cout << temp->data << " ";

        if (leftToRight) {
            if (temp->left) s2.push(temp->left);
            if (temp->right) s2.push(temp->right);
        } else {
            if (temp->right) s2.push(temp->right);
            if (temp->left) s2.push(temp->left);
        }

        if (s1.empty()) {
            leftToRight = !leftToRight;
            swap(s1, s2);
        }
    }
}
```

### Vertical Order Traversal
Assigns horizontal distance (HD) to each node: `root=0`, `left = HD-1`, `right = HD+1`.
```cpp
void verticalOrder(Node* root) {
    map<int, vector<int>> m; // HD -> List of nodes
    queue<pair<Node*, int>> q;
    q.push({root, 0});

    while (!q.empty()) {
        auto p = q.front(); q.pop();
        m[p.second].push_back(p.first->data);

        if (p.first->left) q.push({p.first->left, p.second - 1});
        if (p.first->right) q.push({p.first->right, p.second + 1});
    }

    for (auto const& [hd, nodes] : m) {
        for (int x : nodes) cout << x << " ";
    }
}
```

---

## 4. Boundary Traversal
Often used to print the "outline" of a tree:
1. Root
2. Left Boundary (excluding leaves)
3. All Leaves
4. Right Boundary (in reverse, excluding leaves)

```cpp
void printLeftBoundary(Node* root) {
    if (!root || (!root->left && !root->right)) return;
    cout << root->data << " ";
    if (root->left) printLeftBoundary(root->left);
    else printLeftBoundary(root->right);
}

void printLeaves(Node* root) {
    if (!root) return;
    if (!root->left && !root->right) cout << root->data << " ";
    printLeaves(root->left);
    printLeaves(root->right);
}

void printRightBoundary(Node* root) {
    if (!root || (!root->left && !root->right)) return;
    if (root->right) printRightBoundary(root->right);
    else printRightBoundary(root->left);
    cout << root->data << " "; // Print bottom-up
}
```

---

## Performance Comparison

| Mechanism | Time | Space | Pros | Cons |
|-----------|------|-------|------|------|
| **Recursive** | $O(N)$ | $O(H)$ | Simple, readable | Stack overflow risk |
| **Iterative (Stack)** | $O(N)$ | $O(H)$ | Safe for deep trees | Explicit stack management |
| **Morris** | $O(N)$ | $O(1)$ | Best space efficiency | Temporarily modifies tree |
| **Level-Order (Queue)**| $O(N)$ | $O(W)$ | Level-by-level | Max width memory usage |

*H = Height, W = Max Width of Tree.*

---

## Summary Concepts
- **Threaded Trees**: Use null pointers to point to inorder successor/predecessor.
- **Euler Tour**: A traversal where we record every time we enter or leave a node (useful for LCA).
- **Serialization**: Converting a tree into a sequence (often using Preorder + Null placeholders) for storage.
