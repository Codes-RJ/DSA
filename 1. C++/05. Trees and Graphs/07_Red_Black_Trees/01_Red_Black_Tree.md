# Red-Black Tree Implementation

## 📖 Overview

A **Red-Black Tree** is an augmented Binary Search Tree that maintains balance using node coloring and tree rotations. By maintaining five fundamental invariants, the tree ensures that the longest path from the root to any leaf is no more than twice the length of the shortest path, guaranteeing **$O(\log N)$** time complexity for insertion, deletion, and lookup operations.

This implementation uses a canonical **NIL sentinel node** technique: instead of using `nullptr` for empty children and the parent of the root, a single shared sentinel node `nil` is used. This simplifies rotation and rebalancing code by eliminating special checks for null pointers.

---

## 🎯 Red-Black Tree Invariants

Every node has an attribute `color` $\in \{\text{RED}, \text{BLACK}\}$:
1. **Node Color**: Every node is either `RED` or `BLACK`.
2. **Root Property**: The root is `BLACK`.
3. **Leaf Property**: Every leaf (`nil` sentinel) is `BLACK`.
4. **Red Property**: If a node is `RED`, then both its children are `BLACK` (no two consecutive red nodes).
5. **Black-Height Property**: For each node, all simple paths from the node to descendant leaves contain the same number of `BLACK` nodes.

```
                  ┌─────────┐
                  │ 13 (B)  │  <-- Root is BLACK
                  └────┬────┘
             ┌─────────┴─────────┐
        ┌────┴────┐         ┌────┴────┐
        │  8 (R)  │         │ 17 (R)  │
        └────┬────┘         └────┬────┘
        ┌────┴────┐              └────┐
   ┌────┴────┐ ┌────┴────┐       ┌────┴────┐
   │  1 (B)  │ │ 11 (B)  │       │ 25 (B)  │
   └────┬────┘ └────┬────┘       └────┬────┘
     ┌──┴──┐     ┌──┴──┐           ┌──┴──┐
    nil   nil   nil   nil         nil   nil  <-- nil sentinels are BLACK
```

---

## 🔄 Insertion Rebalancing (Fixup)

When inserting a new key, we always insert it with color **RED** at a leaf position (like regular BST insertion). This preserves the Black-Height property (Property 5), but may violate the Red Property (Property 4) if the parent is also RED.

Let $z$ be the newly inserted node. While $z$'s parent is **RED**, $z$'s grandparent must exist and must be **BLACK**. We determine which case applies based on $z$'s **uncle** $y$ (the sibling of $z$'s parent):

### Case 1: Uncle $y$ is RED (Recoloring)
```
          Grandparent (B)                     Grandparent (R)  <-- Check grandparent
             /       \                           /       \
        Parent (R)    Uncle (R)   ======>   Parent (B)    Uncle (B)
           /                                   /
       z (R)                               z (R)
```
- **Action**: Recolor Parent and Uncle to `BLACK`. Recolor Grandparent to `RED`.
- Set $z = \text{Grandparent}$ and repeat up the tree.

### Case 2: Uncle $y$ is BLACK, $z$ is an Inner Child (Triangle)
```
          Grandparent (B)                     Grandparent (B)
             /       \                           /       \
        Parent (R)    Uncle (B)   ======>      z (R)      Uncle (B)
             \                                 /
             z (R)                         Parent (R)
```
- **Action**: Perform a rotation on Parent (Left rotate if Parent is left child) to transform into a straight line (Case 3).

### Case 3: Uncle $y$ is BLACK, $z$ is an Outer Child (Line)
```
            Grandparent (B)                     Parent (B)
               /       \                           /   \
          Parent (R)    Uncle (B)  ======>     z (R)  Grandparent (R)
             /                                           \
          z (R)                                          Uncle (B)
```
- **Action**: Recolor Parent to `BLACK`, Grandparent to `RED`.
- Perform a Right rotation on Grandparent. The subtree is now balanced and terminates!

---

## 🗑️ Deletion Rebalancing (Fixup)

When deleting a node, if the spliced node $y$ was **BLACK**, its removal decreases the black-height of that subtree by 1. To fix this, we introduce an imaginary **"double-black"** or **"red-and-black"** node $x$.

If $x$ is red-and-black, we simply color it black. If $x$ is double-black, we resolve it using 4 cases (assuming $x$ is a left child; symmetric for right child):

### Case 1: Sibling $w$ is RED
- **Action**: Recolor $w$ to `BLACK`, parent to `RED`. Left rotate parent. Sibling is now black; fall through to Case 2, 3, or 4.

### Case 2: Sibling $w$ is BLACK, and both of $w$'s children are BLACK
- **Action**: Recolor sibling $w$ to `RED`. Move extra black up to parent ($x = x\to\text{parent}$).

### Case 3: Sibling $w$ is BLACK, $w$'s left child is RED, right child is BLACK (Inner child RED)
- **Action**: Recolor $w$'s left child to `BLACK`, $w$ to `RED`. Right rotate $w$. Transforms into Case 4.

### Case 4: Sibling $w$ is BLACK, $w$'s right child is RED (Outer child RED)
- **Action**: Recolor $w$ to parent's color, parent to `BLACK`, $w$'s right child to `BLACK`. Left rotate parent. Double-black is eliminated; set $x = \text{root}$ to terminate!

---

## 💻 Complete C++ Implementation

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>
#include <iomanip>

enum Color { RED, BLACK };

template <typename Key, typename Value>
class RedBlackTree {
private:
    struct Node {
        Key key;
        Value val;
        Color color;
        Node* parent;
        Node* left;
        Node* right;

        Node(const Key& k, const Value& v, Color c, Node* p, Node* l, Node* r)
            : key(k), val(v), color(c), parent(p), left(l), right(r) {}
    };

    Node* root;
    Node* nil;
    size_t treeSize;

    // Allocate and initialize sentinel node
    void initNil() {
        nil = new Node(Key(), Value(), BLACK, nullptr, nullptr, nullptr);
        nil->left = nil;
        nil->right = nil;
        nil->parent = nil;
    }

    void leftRotate(Node* x) {
        Node* y = x->right;
        x->right = y->left;
        if (y->left != nil) {
            y->left->parent = x;
        }
        y->parent = x->parent;
        if (x->parent == nil) {
            root = y;
        } else if (x == x->parent->left) {
            x->parent->left = y;
        } else {
            x->parent->right = y;
        }
        y->left = x;
        x->parent = y;
    }

    void rightRotate(Node* y) {
        Node* x = y->left;
        y->left = x->right;
        if (x->right != nil) {
            x->right->parent = y;
        }
        x->parent = y->parent;
        if (y->parent == nil) {
            root = x;
        } else if (y == y->parent->right) {
            y->parent->right = x;
        } else {
            y->parent->left = x;
        }
        x->right = y;
        y->parent = x;
    }

    void insertFixup(Node* z) {
        while (z->parent->color == RED) {
            if (z->parent == z->parent->parent->left) {
                Node* y = z->parent->parent->right; // Uncle
                if (y->color == RED) {
                    // Case 1: Uncle is RED
                    z->parent->color = BLACK;
                    y->color = BLACK;
                    z->parent->parent->color = RED;
                    z = z->parent->parent;
                } else {
                    if (z == z->parent->right) {
                        // Case 2: Uncle is BLACK, z is right child (triangle)
                        z = z->parent;
                        leftRotate(z);
                    }
                    // Case 3: Uncle is BLACK, z is left child (line)
                    z->parent->color = BLACK;
                    z->parent->parent->color = RED;
                    rightRotate(z->parent->parent);
                }
            } else {
                // Symmetric case: z's parent is right child of grandparent
                Node* y = z->parent->parent->left; // Uncle
                if (y->color == RED) {
                    // Case 1: Uncle is RED
                    z->parent->color = BLACK;
                    y->color = BLACK;
                    z->parent->parent->color = RED;
                    z = z->parent->parent;
                } else {
                    if (z == z->parent->left) {
                        // Case 2: Triangle
                        z = z->parent;
                        rightRotate(z);
                    }
                    // Case 3: Line
                    z->parent->color = BLACK;
                    z->parent->parent->color = RED;
                    leftRotate(z->parent->parent);
                }
            }
        }
        root->color = BLACK;
    }

    void transplant(Node* u, Node* v) {
        if (u->parent == nil) {
            root = v;
        } else if (u == u->parent->left) {
            u->parent->left = v;
        } else {
            u->parent->right = v;
        }
        v->parent = u->parent;
    }

    Node* treeMinimum(Node* x) const {
        while (x->left != nil) {
            x = x->left;
        }
        return x;
    }

    Node* treeMaximum(Node* x) const {
        while (x->right != nil) {
            x = x->right;
        }
        return x;
    }

    void deleteFixup(Node* x) {
        while (x != root && x->color == BLACK) {
            if (x == x->parent->left) {
                Node* w = x->parent->right; // Sibling
                if (w->color == RED) {
                    // Case 1: Sibling is RED
                    w->color = BLACK;
                    x->parent->color = RED;
                    leftRotate(x->parent);
                    w = x->parent->right;
                }
                if (w->left->color == BLACK && w->right->color == BLACK) {
                    // Case 2: Sibling is BLACK, both children BLACK
                    w->color = RED;
                    x = x->parent;
                } else {
                    if (w->right->color == BLACK) {
                        // Case 3: Sibling is BLACK, left child RED, right child BLACK
                        w->left->color = BLACK;
                        w->color = RED;
                        rightRotate(w);
                        w = x->parent->right;
                    }
                    // Case 4: Sibling is BLACK, right child RED
                    w->color = x->parent->color;
                    x->parent->color = BLACK;
                    w->right->color = BLACK;
                    leftRotate(x->parent);
                    x = root;
                }
            } else {
                // Symmetric case: x is right child
                Node* w = x->parent->left; // Sibling
                if (w->color == RED) {
                    // Case 1
                    w->color = BLACK;
                    x->parent->color = RED;
                    rightRotate(x->parent);
                    w = x->parent->left;
                }
                if (w->right->color == BLACK && w->left->color == BLACK) {
                    // Case 2
                    w->color = RED;
                    x = x->parent;
                } else {
                    if (w->left->color == BLACK) {
                        // Case 3
                        w->right->color = BLACK;
                        w->color = RED;
                        leftRotate(w);
                        w = x->parent->left;
                    }
                    // Case 4
                    w->color = x->parent->color;
                    x->parent->color = BLACK;
                    w->left->color = BLACK;
                    rightRotate(x->parent);
                    x = root;
                }
            }
        }
        x->color = BLACK;
    }

    void destroyTree(Node* node) {
        if (node != nil) {
            destroyTree(node->left);
            destroyTree(node->right);
            delete node;
        }
    }

    Node* cloneTree(Node* node, Node* parentNode, Node* otherNil) {
        if (node == otherNil) {
            return nil;
        }
        Node* newNode = new Node(node->key, node->val, node->color, parentNode, nil, nil);
        newNode->left = cloneTree(node->left, newNode, otherNil);
        newNode->right = cloneTree(node->right, newNode, otherNil);
        return newNode;
    }

    void printTreeHelper(Node* rootNode, const std::string& prefix, bool isLeft) const {
        if (rootNode != nil) {
            std::cout << prefix;
            std::cout << (isLeft ? "├── " : "└── ");
            std::cout << rootNode->key << " [" << (rootNode->color == RED ? "R" : "B") << "]\n";
            printTreeHelper(rootNode->left, prefix + (isLeft ? "│   " : "    "), true);
            printTreeHelper(rootNode->right, prefix + (isLeft ? "│   " : "    "), false);
        }
    }

    int verifyHelper(Node* node, bool& valid) const {
        if (node == nil) {
            return 1; // Leaf nil has black-height 1
        }
        // Check Red Property: No two consecutive red nodes
        if (node->color == RED) {
            if (node->left->color == RED || node->right->color == RED) {
                std::cerr << "Violation: Consecutive RED nodes at " << node->key << "\n";
                valid = false;
            }
        }
        // Check BST Property
        if (node->left != nil && node->left->key >= node->key) {
            std::cerr << "Violation: BST left ordering failed at " << node->key << "\n";
            valid = false;
        }
        if (node->right != nil && node->right->key <= node->key) {
            std::cerr << "Violation: BST right ordering failed at " << node->key << "\n";
            valid = false;
        }

        int leftBH = verifyHelper(node->left, valid);
        int rightBH = verifyHelper(node->right, valid);

        if (leftBH != rightBH) {
            std::cerr << "Violation: Black-height mismatch at " << node->key 
                      << " (left: " << leftBH << ", right: " << rightBH << ")\n";
            valid = false;
        }

        return leftBH + (node->color == BLACK ? 1 : 0);
    }

    void inorderHelper(Node* node, std::vector<std::pair<Key, Value>>& out) const {
        if (node != nil) {
            inorderHelper(node->left, out);
            out.push_back({node->key, node->val});
            inorderHelper(node->right, out);
        }
    }

public:
    RedBlackTree() : treeSize(0) {
        initNil();
        root = nil;
    }

    ~RedBlackTree() {
        destroyTree(root);
        delete nil;
    }

    // Copy Constructor
    RedBlackTree(const RedBlackTree& other) : treeSize(other.treeSize) {
        initNil();
        root = cloneTree(other.root, nil, other.nil);
    }

    // Copy Assignment
    RedBlackTree& operator=(const RedBlackTree& other) {
        if (this != &other) {
            destroyTree(root);
            treeSize = other.treeSize;
            root = cloneTree(other.root, nil, other.nil);
        }
        return *this;
    }

    // Move Constructor
    RedBlackTree(RedBlackTree&& other) noexcept 
        : root(other.root), nil(other.nil), treeSize(other.treeSize) {
        other.initNil();
        other.root = other.nil;
        other.treeSize = 0;
    }

    // Move Assignment
    RedBlackTree& operator=(RedBlackTree&& other) noexcept {
        if (this != &other) {
            destroyTree(root);
            delete nil;
            root = other.root;
            nil = other.nil;
            treeSize = other.treeSize;
            other.initNil();
            other.root = other.nil;
            other.treeSize = 0;
        }
        return *this;
    }

    size_t size() const { return treeSize; }
    bool empty() const { return treeSize == 0; }

    bool insert(const Key& key, const Value& val) {
        Node* y = nil;
        Node* x = root;

        while (x != nil) {
            y = x;
            if (key == x->key) {
                x->val = val; // Update existing value
                return false;
            } else if (key < x->key) {
                x = x->left;
            } else {
                x = x->right;
            }
        }

        Node* z = new Node(key, val, RED, y, nil, nil);
        if (y == nil) {
            root = z;
        } else if (z->key < y->key) {
            y->left = z;
        } else {
            y->right = z;
        }

        treeSize++;
        insertFixup(z);
        return true;
    }

    bool remove(const Key& key) {
        Node* z = root;
        while (z != nil && z->key != key) {
            if (key < z->key) z = z->left;
            else z = z->right;
        }

        if (z == nil) return false; // Key not found

        Node* y = z;
        Node* x = nil;
        Color yOriginalColor = y->color;

        if (z->left == nil) {
            x = z->right;
            transplant(z, z->right);
        } else if (z->right == nil) {
            x = z->left;
            transplant(z, z->left);
        } else {
            y = treeMinimum(z->right);
            yOriginalColor = y->color;
            x = y->right;
            if (y->parent == z) {
                x->parent = y;
            } else {
                transplant(y, y->right);
                y->right = z->right;
                y->right->parent = y;
            }
            transplant(z, y);
            y->left = z->left;
            y->left->parent = y;
            y->color = z->color;
        }

        delete z;
        treeSize--;

        if (yOriginalColor == BLACK) {
            deleteFixup(x);
        }
        return true;
    }

    bool find(const Key& key, Value& outVal) const {
        Node* x = root;
        while (x != nil) {
            if (key == x->key) {
                outVal = x->val;
                return true;
            } else if (key < x->key) {
                x = x->left;
            } else {
                x = x->right;
            }
        }
        return false;
    }

    bool contains(const Key& key) const {
        Value temp;
        return find(key, temp);
    }

    bool getMin(Key& outKey, Value& outVal) const {
        if (root == nil) return false;
        Node* m = treeMinimum(root);
        outKey = m->key;
        outVal = m->val;
        return true;
    }

    bool getMax(Key& outKey, Value& outVal) const {
        if (root == nil) return false;
        Node* m = treeMaximum(root);
        outKey = m->key;
        outVal = m->val;
        return true;
    }

    std::vector<std::pair<Key, Value>> inorder() const {
        std::vector<std::pair<Key, Value>> result;
        inorderHelper(root, result);
        return result;
    }

    void printTree() const {
        if (root == nil) {
            std::cout << "[Empty Tree]\n";
            return;
        }
        printTreeHelper(root, "", false);
    }

    bool verifyProperties() const {
        if (root == nil) return true;
        if (root->color != BLACK) {
            std::cerr << "Violation: Root is not BLACK!\n";
            return false;
        }
        bool valid = true;
        verifyHelper(root, valid);
        return valid;
    }
};

int main() {
    std::cout << "=== Red-Black Tree Comprehensive Test Harness ===\n\n";

    RedBlackTree<int, std::string> rbt;

    std::cout << "1. Inserting elements: 10, 20, 30, 15, 25, 5, 1\n";
    rbt.insert(10, "Ten");
    rbt.insert(20, "Twenty");
    rbt.insert(30, "Thirty");
    rbt.insert(15, "Fifteen");
    rbt.insert(25, "Twenty-Five");
    rbt.insert(5,  "Five");
    rbt.insert(1,  "One");

    std::cout << "Tree Size: " << rbt.size() << "\n";
    std::cout << "Tree Structure (R=Red, B=Black):\n";
    rbt.printTree();

    bool valid = rbt.verifyProperties();
    std::cout << "Red-Black Invariants Check: " << (valid ? "PASSED (100% Valid)" : "FAILED") << "\n\n";

    std::cout << "2. In-order Traversal (Sorted Key-Value pairs):\n";
    auto pairs = rbt.inorder();
    for (const auto& p : pairs) {
        std::cout << "  " << p.first << " => " << p.second << "\n";
    }
    std::cout << "\n";

    std::cout << "3. Testing Lookup:\n";
    std::string val;
    if (rbt.find(25, val)) {
        std::cout << "  Found key 25 with value: " << val << "\n";
    }
    std::cout << "  Contains 99: " << (rbt.contains(99) ? "Yes" : "No") << "\n\n";

    std::cout << "4. Testing Deletions and Rebalancing:\n";
    std::cout << "  Removing key 20 (internal node)...\n";
    rbt.remove(20);
    rbt.printTree();
    assert(rbt.verifyProperties());
    std::cout << "  Invariants after removing 20: PASSED\n\n";

    std::cout << "  Removing key 1 (leaf node)...\n";
    rbt.remove(1);
    rbt.printTree();
    assert(rbt.verifyProperties());
    std::cout << "  Invariants after removing 1: PASSED\n\n";

    std::cout << "  Removing root...\n";
    int minKey, maxKey;
    std::string minVal, maxVal;
    rbt.getMin(minKey, minVal);
    rbt.getMax(maxKey, maxVal);
    std::cout << "  Current Min: " << minKey << " (" << minVal << "), Max: " << maxKey << " (" << maxVal << ")\n";

    std::cout << "\n5. Stress Testing Sequential Insertions & Deletions:\n";
    RedBlackTree<int, int> stressTree;
    const int NUM_ITEMS = 100;
    for (int i = 1; i <= NUM_ITEMS; i++) {
        stressTree.insert(i, i * 10);
        assert(stressTree.verifyProperties());
    }
    std::cout << "  Inserted " << NUM_ITEMS << " sequential keys. Invariants PASSED.\n";
    std::cout << "  Tree size: " << stressTree.size() << "\n";

    for (int i = 1; i <= NUM_ITEMS; i += 2) {
        stressTree.remove(i);
        assert(stressTree.verifyProperties());
    }
    std::cout << "  Removed all odd keys. Invariants PASSED.\n";
    std::cout << "  Tree size: " << stressTree.size() << "\n";

    std::cout << "\n=== All Red-Black Tree Tests Completed Successfully! ===\n";
    return 0;
}
```

---

## 📊 Complexity Analysis

| Operation | Average Case | Worst Case | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Search** | $O(\log N)$ | $O(\log N)$ | $O(1)$ |
| **Insert** | $O(\log N)$ | $O(\log N)$ | $O(1)$ |
| **Delete** | $O(\log N)$ | $O(\log N)$ | $O(1)$ |
| **Min / Max** | $O(\log N)$ | $O(\log N)$ | $O(1)$ |
| **Rotations (Insert)** | $O(1)$ | At most 2 | $O(1)$ |
| **Rotations (Delete)** | $O(1)$ | At most 3 | $O(1)$ |
| **Total Memory** | $\Theta(N)$ | $\Theta(N)$ | $\Theta(N)$ nodes |

---

## 💡 Practical Insights & STL Comparison

1. **Why STL Uses Red-Black Trees over AVL Trees**:
   - In `std::set` and `std::map`, elements are dynamically inserted and erased. In AVL trees, deletions can trigger up to $O(\log N)$ cascading rotations. In Red-Black trees, deletion requires **at most 3 rotations**, making dynamic write operations substantially faster.
2. **Sentinel Node Pattern**:
   - By creating a shared `nil` node whose color is always `BLACK`, every boundary check `node != nullptr` is simplified to `node != nil`. Crucially, accessing `nil->color` is safe and returns `BLACK`, seamlessly satisfying Property 3 without null-pointer checks.
3. **Cache Performance**:
   - Modern B-Trees and cache-oblivious search trees often outperform binary trees for massive in-memory datasets due to CPU cache-line alignment. However, for pointer-based node-stable associative containers (where references to un-erased nodes must never invalidate), Red-Black trees remain the gold standard.
