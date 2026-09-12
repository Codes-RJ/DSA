# Red-Black Trees

## 📖 Overview

A **Red-Black Tree** is a self-balancing Binary Search Tree (BST) where every node stores an extra bit representing **color** (`RED` or `BLACK`). Through a strict set of coloring rules and tree rotations during insertions and deletions, a Red-Black tree guarantees that no simple path from the root to a leaf is more than twice as long as any other path. This ensures that dynamic set operations—such as `search`, `insert`, and `delete`—always execute in guaranteed **$O(\log N)$** worst-case time.

Red-Black trees are one of the most widely used data structures in modern software systems:
- **C++ Standard Template Library**: Powers `std::set`, `std::map`, `std::multiset`, and `std::multimap`.
- **Java Collections Framework**: Backs `java.util.TreeMap` and `java.util.TreeSet`.
- **Linux Kernel**: Powers the Completely Fair Scheduler (CFS) for process scheduling and virtual memory management (`vm_area_struct`).

---

## 🎯 The 5 Fundamental Invariants

To be a valid Red-Black Tree, the binary search tree must satisfy all five of the following properties at all times:

```
                  ┌─────────┐
                  │ 13 (B)  │  <-- Property 2: Root is BLACK
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
    NIL   NIL   NIL   NIL         NIL   NIL  <-- Property 3: Leaves are NIL (BLACK)
```

1. **Node Color**: Every node is either **RED** or **BLACK**.
2. **Root Property**: The root node is always **BLACK**.
3. **Leaf Property**: Every leaf (sentinel node `NIL`) is **BLACK**.
4. **Red Property**: If a node is **RED**, both of its children must be **BLACK** (i.e., no two consecutive red nodes on any root-to-leaf path).
5. **Black-Height Property**: For each node, every simple path from that node to descendant `NIL` leaves contains the exact same number of **BLACK** nodes (this count is termed the **Black-Height**, $bh(x)$).

---

## 📐 Mathematical Proof: Height Bound ($H \le 2 \log_2(N + 1)$)

### Black-Height Definition
The **black-height** of a node $x$, denoted $bh(x)$, is the number of black nodes on any path from $x$ (not including $x$ itself) down to a leaf `NIL` (which counts as black).

### Lemma 1: Subtree Size Bound
> A subtree rooted at any node $x$ contains at least $2^{bh(x)} - 1$ internal nodes.

**Proof by Induction on the height of $x$:**
1. **Base Case**: If height of $x$ is 0, $x$ is a leaf sentinel `NIL`.
   - $bh(\text{NIL}) = 0$.
   - Internal nodes in subtree = 0.
   - Formula: $2^0 - 1 = 1 - 1 = 0$. Base case holds.

2. **Inductive Step**: Consider an internal node $x$ with height $> 0$ and two children $c_1$ and $c_2$.
   - If $c_i$ is black: $bh(c_i) = bh(x) - 1$.
   - If $c_i$ is red: $bh(c_i) = bh(x)$.
   - In either case: $bh(c_i) \ge bh(x) - 1$.
   - By the inductive hypothesis, each child $c_i$ roots a subtree with at least $2^{bh(c_i)} - 1 \ge 2^{bh(x) - 1} - 1$ internal nodes.
   - The number of internal nodes in the subtree rooted at $x$ is:
     $$\text{Size}(x) = \text{Size}(c_1) + \text{Size}(c_2) + 1$$
     $$\text{Size}(x) \ge (2^{bh(x) - 1} - 1) + (2^{bh(x) - 1} - 1) + 1 = 2 \cdot 2^{bh(x) - 1} - 1 = 2^{bh(x)} - 1$$
   - Thus, the lemma holds for all nodes $x$. $\blacksquare$

### Theorem: Maximum Height Bound
> A Red-Black tree with $N$ internal nodes has height at most $2 \log_2(N + 1)$.

**Proof:**
- By Property 4, no two red nodes can appear consecutively on any simple path from root to leaf.
- Therefore, at least half of the nodes on any simple path from the root (excluding the root itself) must be **BLACK**.
- Hence, the black-height of the root must be at least half the total height:
  $$bh(\text{root}) \ge \frac{H}{2}$$
- Combining this with Lemma 1 for the root:
  $$N \ge 2^{bh(\text{root})} - 1 \ge 2^{H/2} - 1$$
  $$N + 1 \ge 2^{H/2}$$
  $$\log_2(N + 1) \ge \frac{H}{2}$$
  $$H \le 2 \log_2(N + 1)$$
- Consequently, search, insertion, and deletion run in $O(\log N)$ time in the absolute worst case. $\blacksquare$

---

## ⚖️ Red-Black Trees vs. AVL Trees

| Dimension | Red-Black Tree | AVL Tree |
| :--- | :--- | :--- |
| **Balance Condition** | Path length ratio $\le 2:1$ | Subtree height difference $|h_L - h_R| \le 1$ |
| **Balance Strictness** | Looser balance ($H \le 2 \log_2 N$) | Rigidly balanced ($H \le 1.44 \log_2 N$) |
| **Lookup Performance** | Fast ($O(\log N)$), slightly more traversals | Fastest ($O(\log N)$), fewer node visits |
| **Rotations on Insertion**| At most **2 rotations** | At most **2 rotations** |
| **Rotations on Deletion** | At most **3 rotations** | Up to **$O(\log N)$ rotations** (cascading) |
| **Memory Overhead** | 1 bit per node for color | 2 bits (or integer) for balance factor/height |
| **Primary Use Case** | Insert/Delete-heavy workloads (`std::map`) | Read/Search-heavy lookups (dictionaries) |

---

## 🔄 Fundamental Rotations

Rotations are local pointer updates that modify tree topology while strictly preserving the Binary Search Tree invariant ($A < x < B < y < C$).

### 1. Left Rotation on Node $X$

```
      |                                  |
      X                                  Y
     / \         Left Rotate (X)        / \
    A   Y       ────────────────>      X   C
       / \                            / \
      B   C                          A   B
```

**Pointer Reassignments:**
1. $Y$'s left child becomes $X$'s right child ($X \to \text{right} = Y \to \text{left}$).
2. If $Y \to \text{left} \neq \text{NIL}$, update $Y \to \text{left} \to \text{parent} = X$.
3. $Y$'s parent becomes $X$'s parent.
4. $X$ becomes $Y$'s left child ($Y \to \text{left} = X$).
5. $X$'s parent becomes $Y$.

### 2. Right Rotation on Node $Y$

```
        |                                |
        Y                                X
       / \       Right Rotate (Y)       / \
      X   C     ────────────────>      A   Y
     / \                                  / \
    A   B                                B   C
```

**Pointer Reassignments:**
1. $X$'s right child becomes $Y$'s left child ($Y \to \text{left} = X \to \text{right}$).
2. If $X \to \text{right} \neq \text{NIL}$, update $X \to \text{right} \to \text{parent} = Y$.
3. $X$'s parent becomes $Y$'s parent.
4. $Y$ becomes $X$'s right child ($X \to \text{right} = Y$).
5. $Y$'s parent becomes $X$.

---

## 📑 Directory Contents

- **`01_Red_Black_Tree.md`**: Complete production C++ implementation of a generic `RedBlackTree<Key, Value>` class featuring:
  - Explicit `NIL` sentinel node design (eliminating null-pointer edge cases).
  - Insertion rebalancing covering **Cases 1, 2, and 3** (Uncle red vs uncle black).
  - Deletion rebalancing covering **Cases 1, 2, 3, and 4** (Sibling color and sibling's children colors).
  - Tree pretty-printer with ASCII branch rendering.
  - Invariant validator method verifying all 5 Red-Black properties on demand.
  - Comprehensive interactive `main()` test harness.
