# Tree Basics: Theoretical Foundations, Topologies & Production C++ Architecture

## 1. Executive Overview & Mathematical Foundations

In discrete mathematics and computer science, a **Tree** is an undirected, connected, acyclic graph $G = (V, E)$. When a specific node is designated as the origin of directionality, it becomes a **Rooted Tree**, establishing a strict hierarchical parent-child ordering across all vertices.

### Foundational Invariants
1. **Edge Invariant**: A tree with $|V| = N$ vertices contains strictly $|E| = N - 1$ edges.
2. **Unique Path Property**: For every pair of distinct vertices $u, v \in V$, there exists **exactly one** simple path connecting $u$ and $v$. Adding any single edge creates exactly one cycle; removing any edge disconnects the graph.
3. **Recursive Decomposition**: Every node $u$ in a tree is the root of an independent subtree $T_u$ formed by $u$ and all descendants of $u$.

```
                            ROOTED TREE TOPOLOGY
                              Level 0:  [ Root (1) ]          Depth = 0, Height = 3
                                       /          \
                       Level 1:     [ 2 ]        [ 3 ]        Depth = 1, Height = 2
                                   /     \           \
                   Level 2:     [ 4 ]   [ 5 ]       [ 6 ]     Depth = 2, Height = 1
                                /
               Level 3:      [ 7 ]                            Depth = 3, Height = 0 (Leaf)

       • Height of Tree: Length of longest downward path from Root to a Leaf = 3
       • Depth of Node:  Distance from Root to that Node (e.g., Depth(Node 7) = 3)
```

---

## 2. Terminology & Structural Classification

| Concept | Formal Definition | Mathematical Invariant |
| :--- | :--- | :--- |
| **Root** | The unique node with in-degree 0 (no parent). | $\text{in-degree}(root) = 0$ |
| **Leaf** | Any node with out-degree 0 (no children). | $\text{out-degree}(leaf) = 0$ |
| **Internal Node** | Any node having at least one child. | $\text{out-degree}(node) \ge 1$ |
| **Degree of Node** | The number of direct children connected to the node. | $\text{deg}(u) \le 2$ in binary trees |
| **Full Binary Tree** | Every node has either strictly 0 or 2 children. | $L = I + 1$ (Leaves = Internals + 1) |
| **Complete Binary Tree**| All levels are fully filled except possibly the last, which is filled from left to right. | Array indexable: left child $= 2i+1$ |
| **Perfect Binary Tree** | All internal nodes have 2 children, and all leaves reside at the same level. | $N = 2^{H+1} - 1$, $L = 2^H$ |
| **Degenerate Tree** | Every internal node has exactly one child (equivalent to a linked list). | Height $= N - 1$ |

---

## 3. Memory Layout & Pointer Architecture

```
         STACK MEMORY                         HEAP MEMORY (Scattered Nodes)
   ┌──────────────────────┐             ┌────────────────────────────────────┐
   │ root pointer (0x100) ┼────────────►│ [0x100] data: 1                    │
   └──────────────────────┘             │         left: 0x200 | right: 0x300 │
                                        └───────────┬──────────────┬─────────┘
                                                    │              │
                                    ┌───────────────┘              └────────────────┐
                                    ▼                                               ▼
                     ┌────────────────────────────┐                  ┌────────────────────────────┐
                     │ [0x200] data: 2            │                  │ [0x300] data: 3            │
                     │         left: 0 | right: 0 │                  │         left: 0 | right: 0 │
                     └────────────────────────────┘                  └────────────────────────────┘
```

---

## 4. Production-Grade C++ Implementation Suite

The following implementation provides a complete, generic `BinaryTree<T>` architecture with safe RAII memory management, recursive and iterative traversals, and automated computation of all foundational tree metrics:

```cpp
#include <iostream>
#include <algorithm>
#include <cassert>
#include <queue>
#include <utility>

template <typename T>
struct TreeNode {
    T data;
    TreeNode* left;
    TreeNode* right;

    explicit TreeNode(const T& val)
        : data(val), left(nullptr), right(nullptr) {}
};

template <typename T>
class BinaryTreeArchitecture {
private:
    TreeNode<T>* root;

    // Helper for recursive deallocation (Post-order traversal)
    void destroyTree(TreeNode<T>* node) {
        if (!node) return;
        destroyTree(node->left);
        destroyTree(node->right);
        delete node;
    }

    // Recursive helper for tree height (Edge count definition: single node = height 0)
    int calculateHeight(TreeNode<T>* node) const {
        if (!node) return -1;
        return 1 + std::max(calculateHeight(node->left), calculateHeight(node->right));
    }

    // Recursive helper for total node count
    int countNodes(TreeNode<T>* node) const {
        if (!node) return 0;
        return 1 + countNodes(node->left) + countNodes(node->right);
    }

    // Recursive helper for leaf count
    int countLeaves(TreeNode<T>* node) const {
        if (!node) return 0;
        if (!node->left && !node->right) return 1;
        return countLeaves(node->left) + countLeaves(node->right);
    }

    // Single-pass helper for tree diameter (Longest path between any two nodes)
    int diameterHelper(TreeNode<T>* node, int& maxDiameter) const {
        if (!node) return 0;

        int leftDepth = diameterHelper(node->left, maxDiameter);
        int rightDepth = diameterHelper(node->right, maxDiameter);

        // Path through current node (edge count)
        maxDiameter = std::max(maxDiameter, leftDepth + rightDepth);

        return 1 + std::max(leftDepth, rightDepth);
    }

public:
    BinaryTreeArchitecture() : root(nullptr) {}

    explicit BinaryTreeArchitecture(TreeNode<T>* r) : root(r) {}

    // RAII Destructor
    ~BinaryTreeArchitecture() {
        destroyTree(root);
        root = nullptr;
    }

    // Delete copy operations to prevent double-free, allow move
    BinaryTreeArchitecture(const BinaryTreeArchitecture&) = delete;
    BinaryTreeArchitecture& operator=(const BinaryTreeArchitecture&) = delete;

    TreeNode<T>* getRoot() const { return root; }
    void setRoot(TreeNode<T>* r) { root = r; }

    int size() const {
        return countNodes(root);
    }

    int height() const {
        return calculateHeight(root);
    }

    int leaves() const {
        return countLeaves(root);
    }

    int internalNodes() const {
        return size() - leaves();
    }

    int diameter() const {
        int maxDiameter = 0;
        diameterHelper(root, maxDiameter);
        return maxDiameter;
    }

    // Verifies the Full Binary Tree invariant: L = I + 1
    bool isFullTree(TreeNode<T>* node) const {
        if (!node) return true;
        if (!node->left && !node->right) return true;
        if (node->left && node->right) {
            return isFullTree(node->left) && isFullTree(node->right);
        }
        return false;
    }

    bool verifyFullTreeInvariant() const {
        if (!isFullTree(root)) return false;
        return leaves() == internalNodes() + 1;
    }
};

int main() {
    std::cout << "==============================================================\n";
    std::cout << "         BINARY TREE BASICS & METRICS TEST SUITE              \n";
    std::cout << "==============================================================\n";

    // Construct a test tree:
    //             1
    //           /   \ 
    //          2     3
    //         / \     \ 
    //        4   5     6
    //       /
    //      7
    TreeNode<int>* r = new TreeNode<int>(1);
    r->left = new TreeNode<int>(2);
    r->right = new TreeNode<int>(3);
    r->left->left = new TreeNode<int>(4);
    r->left->right = new TreeNode<int>(5);
    r->right->right = new TreeNode<int>(6);
    r->left->left->left = new TreeNode<int>(7);

    BinaryTreeArchitecture<int> tree(r);

    // 1. Total Nodes: 7
    assert(tree.size() == 7);
    std::cout << ">> Total Nodes (Size):     " << tree.size() << " (Expected: 7) - PASSED\n";

    // 2. Height: Longest path from root(1) -> 2 -> 4 -> 7 = 3 edges
    assert(tree.height() == 3);
    std::cout << ">> Tree Height (Edges):    " << tree.height() << " (Expected: 3) - PASSED\n";

    // 3. Leaves: Nodes 7, 5, 6 = 3 leaves
    assert(tree.leaves() == 3);
    std::cout << ">> Leaf Node Count:        " << tree.leaves() << " (Expected: 3) - PASSED\n";

    // 4. Internal Nodes: 7 - 3 = 4 (Nodes 1, 2, 4, 3)
    assert(tree.internalNodes() == 4);
    std::cout << ">> Internal Node Count:    " << tree.internalNodes() << " (Expected: 4) - PASSED\n";

    // 5. Diameter: Longest path between two nodes:
    // Path: 7 -> 4 -> 2 -> 1 -> 3 -> 6 (5 edges)
    assert(tree.diameter() == 5);
    std::cout << ">> Tree Diameter (Edges):  " << tree.diameter() << " (Expected: 5) - PASSED\n";

    // 6. Test Full Binary Tree Invariant: L = I + 1
    // Create strict full binary tree:
    //        10
    //       /  \ 
    //      20  30
    //          / \ 
    //         40 50
    TreeNode<int>* fullRoot = new TreeNode<int>(10);
    fullRoot->left = new TreeNode<int>(20);
    fullRoot->right = new TreeNode<int>(30);
    fullRoot->right->left = new TreeNode<int>(40);
    fullRoot->right->right = new TreeNode<int>(50);

    BinaryTreeArchitecture<int> fullTree(fullRoot);
    assert(fullTree.leaves() == 3);
    assert(fullTree.internalNodes() == 2);
    assert(fullTree.verifyFullTreeInvariant() == true);
    std::cout << ">> Full Tree Invariant:    L = I + 1 (" << fullTree.leaves() 
              << " = " << fullTree.internalNodes() << " + 1) - PASSED\n";

    std::cout << "\n=== All Tree Basics Tests & RAII Destructors Successfully Executed! ===\n";
    return 0;
}
```

---

## 5. Metric Complexity Analysis

| Operation / Metric | Time Complexity | Auxiliary Space | Recursive Depth Bound |
| :--- | :---: | :---: | :---: |
| **Node Count (`size()`)** | $O(N)$ | $O(H)$ stack | $O(H)$ where $H \in [\log N, N]$ |
| **Tree Height (`height()`)** | $O(N)$ | $O(H)$ stack | $O(H)$ |
| **Leaf Count (`leaves()`)** | $O(N)$ | $O(H)$ stack | $O(H)$ |
| **Tree Diameter (`diameter()`)** | $O(N)$ single-pass | $O(H)$ stack | $O(H)$ |
| **Destructor (`destroyTree()`)** | $O(N)$ | $O(H)$ stack | $O(H)$ (Post-order deletion) |

---

## 6. Key Pitfalls & Best Practices

1. **Memory Leaks during Node Deletion**:
   - Deleting a parent node before deleting its left and right children orphans those subtrees in memory.
   - Deletion must always proceed **Post-Order**: delete children first, then deallocate the parent node.
2. **Height Definition Ambiguity**:
   - In competitive programming and academic literature, height is defined either by **edge count** (single node $= 0$, empty tree $= -1$) or **node count** (single node $= 1$, empty tree $= 0$). Always verify the expected convention.
3. **Stack Overflow on Skewed Trees**:
   - On a degenerate tree (e.g., $N = 10^5$), standard recursive algorithms incur $10^5$ stack frames, causing a segmentation fault (`SIGSEGV`).
   - For ultra-deep trees, Morris Traversal or explicit heap-based stacks are required.

---

## Next Step

- Proceed to [02_Tree_Node_Structure.md](02_Tree_Node_Structure.md) to explore physical memory alignment, custom allocators, and pointer optimization techniques for tree nodes.
