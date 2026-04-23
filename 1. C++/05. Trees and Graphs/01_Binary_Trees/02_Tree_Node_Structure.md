# Tree Node Structure

## 📖 Overview

The node is the fundamental building block of any tree data structure. Each node contains data and references (pointers) to its children. Understanding the node structure is essential for implementing and manipulating trees.

---

## 🎯 Basic Node Structure

### C++ Implementation

```cpp
// Basic tree node
struct Node {
    int data;
    Node* firstChild;
    Node* nextSibling;
    
    Node(int val) : data(val), firstChild(nullptr), nextSibling(nullptr) {}
};

// General tree node with vector of children
struct TreeNode {
    int data;
    vector<TreeNode*> children;
    
    TreeNode(int val) : data(val) {}
};
```

---

## 📊 Types of Node Structures

| Node Type | Children Storage | Memory | Use Case |
|-----------|-----------------|--------|----------|
| **Fixed Array** | Fixed-size array | Fixed | Known maximum children |
| **Dynamic Array** | Vector/list | Dynamic | Variable children count |
| **First-Child/Next-Sibling** | Two pointers | Compact | General trees |
| **Parent Pointer** | Single pointer | Minimal | Upward traversal only |
| **Binary Node** | Left/Right pointers | Compact | Binary trees only |

---

## 🏗️ Binary Tree Node

### Standard Binary Node

```cpp
struct BinaryNode {
    int data;
    BinaryNode* left;
    BinaryNode* right;
    
    // Constructor
    BinaryNode(int val) : data(val), left(nullptr), right(nullptr) {}
    
    // Constructor with children
    BinaryNode(int val, BinaryNode* l, BinaryNode* r) 
        : data(val), left(l), right(r) {}
};

// Usage
BinaryNode* root = new BinaryNode(10);
root->left = new BinaryNode(5);
root->right = new BinaryNode(15);
```

### Binary Node with Parent Pointer

```cpp
struct BinaryNodeWithParent {
    int data;
    BinaryNodeWithParent* left;
    BinaryNodeWithParent* right;
    BinaryNodeWithParent* parent;
    
    BinaryNodeWithParent(int val) 
        : data(val), left(nullptr), right(nullptr), parent(nullptr) {}
};

// Setting parent during insertion
void insert(BinaryNodeWithParent* parent, int val) {
    BinaryNodeWithParent* newNode = new BinaryNodeWithParent(val);
    newNode->parent = parent;
    
    if (val < parent->data) {
        parent->left = newNode;
    } else {
        parent->right = newNode;
    }
}
```

---

## 🌳 General Tree Node

### Vector-based Children

```cpp
struct GeneralNode {
    int data;
    vector<GeneralNode*> children;
    
    GeneralNode(int val) : data(val) {}
    
    void addChild(GeneralNode* child) {
        children.push_back(child);
    }
    
    void addChild(int val) {
        children.push_back(new GeneralNode(val));
    }
};

// Usage
GeneralNode* root = new GeneralNode(1);
root->addChild(2);
root->addChild(3);
root->children[0]->addChild(4);
```

### First-Child/Next-Sibling Representation

```cpp
struct FCNSNode {
    int data;
    FCNSNode* firstChild;
    FCNSNode* nextSibling;
    
    FCNSNode(int val) : data(val), firstChild(nullptr), nextSibling(nullptr) {}
};

// Convert general tree to FCNS representation
// Root with children: 2, 3, 4
FCNSNode* root = new FCNSNode(1);
root->firstChild = new FCNSNode(2);
root->firstChild->nextSibling = new FCNSNode(3);
root->firstChild->nextSibling->nextSibling = new FCNSNode(4);
```

---

## 🔧 Node Operations

### Creating Nodes

```cpp
// Stack allocation (automatic)
BinaryNode node1(10);

// Heap allocation (dynamic)
BinaryNode* node2 = new BinaryNode(20);
BinaryNode* node3 = new BinaryNode(30);

// Linking nodes
node2->left = node3;
node2->right = new BinaryNode(40);
```

### Copying Nodes

```cpp
// Shallow copy (copies pointers, not children)
BinaryNode* shallowCopy(BinaryNode* node) {
    if (!node) return nullptr;
    return new BinaryNode(node->data, node->left, node->right);
}

// Deep copy (recursively copies entire subtree)
BinaryNode* deepCopy(BinaryNode* node) {
    if (!node) return nullptr;
    
    BinaryNode* newNode = new BinaryNode(node->data);
    newNode->left = deepCopy(node->left);
    newNode->right = deepCopy(node->right);
    
    return newNode;
}
```

### Deleting Nodes

```cpp
// Delete single node (orphans children)
void deleteNode(BinaryNode* node) {
    if (node) {
        delete node;
    }
}

// Delete entire subtree (post-order deletion)
void deleteSubtree(BinaryNode* node) {
    if (!node) return;
    
    deleteSubtree(node->left);
    deleteSubtree(node->right);
    delete node;
}
```

---

## 📊 Memory Layout

### Binary Node Memory

```
BinaryNode (32 bytes on 64-bit system):
┌────────────┬────────────┬────────────┬────────────┐
│   data     │   left     │   right    │  padding   │
│  (4 bytes) │ (8 bytes)  │ (8 bytes)  │ (12 bytes) │
└────────────┴────────────┴────────────┴────────────┘
```

### FCNS Node Memory (more compact)

```
FCNSNode (24 bytes on 64-bit system):
┌────────────┬────────────┬────────────┐
│   data     │ firstChild │ nextSibling│
│  (4 bytes) │ (8 bytes)  │ (8 bytes)  │
└────────────┴────────────┴────────────┘
```

---

## 🎯 Node Comparison

| Feature | Binary Node | Vector Node | FCNS Node |
|---------|-------------|-------------|-----------|
| **Children Limit** | 2 | Unlimited | Unlimited |
| **Memory per Node** | ~24-32 bytes | 24 + vector overhead | ~24 bytes |
| **Child Access** | O(1) | O(1) index | O(k) traversal |
| **Adding Child** | Direct assignment | push_back | Update sibling chain |
| **Use Case** | Binary trees | General trees | Memory-efficient trees |

---

## 💡 Best Practices

1. **Always initialize pointers** to nullptr in constructor
2. **Use smart pointers** for automatic memory management
3. **Delete children before parent** to avoid memory leaks
4. **Consider using vectors** for variable children count
5. **FCNS representation** saves memory for wide trees

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Dangling pointers** | Node deleted but still referenced | Set pointers to nullptr after delete |
| **Memory leaks** | Children not deleted | Delete subtree recursively |
| **Shallow copy** | Modifying copy affects original | Implement deep copy |
| **Parent not updated** | Lost upward references | Store parent pointer if needed |

---

## ✅ Key Takeaways

1. **Node structure** defines how tree is stored in memory
2. **Binary nodes** have left and right pointers
3. **General tree nodes** can use vectors or FCNS representation
4. **Parent pointers** enable upward traversal
5. **Deep copy** creates independent subtree copies
6. **Proper deletion** prevents memory leaks

---

## Next Step

- Go to [03_Tree_Properties.md](03_Tree_Properties.md) to continue with Tree Properties.
