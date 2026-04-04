# Level-Order Traversal

## Introduction
Level-order traversal is a breadth-first approach that visits each node level by level, starting from the root and going left to right across each level.

## Logic and Concept
We use a **Queue** (FIFO).
1. Add the root to the queue.
2. While the queue is not empty:
   - Pop the front node.
   - Print/process its data.
   - Push its left child (if any).
   - Push its right child (if any).

## Level-by-Level Separation
Sometimes you need to know which nodes belong to which level (e.g., printing each level on a new line).

```cpp
void levelOrder(TreeNode* root) {
    if (root == nullptr) return;

    queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
        int levelSize = q.size(); // Number of nodes at current level
        
        for (int i = 0; i < levelSize; i++) {
            TreeNode* current = q.front();
            q.pop();
            cout << current->data << " ";

            if (current->left) q.push(current->left);
            if (current->right) q.push(current->right);
        }
        cout << endl; // Level finished
    }
}
```

## Time and Space Complexity
- **Time**: O(N)
- **Space**: O(W) where W is the maximum width of the tree.

## Applications
- Finding the diameter of a tree.
- Finding the level with maximum nodes.
- Horizontal/Vertical distance calculations.
- Connected nodes on the same level (e.g., "Next Right Pointer" problem).
- Spiral/Zigzag traversal variations.
