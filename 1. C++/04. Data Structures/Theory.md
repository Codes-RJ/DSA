# Data-Structure Foundations

> **Minimum standard:** C++17
>
> **Purpose:** Establish the vocabulary and reasoning used by every custom data structure in this section.

## 1. Abstract Data Types and Representations

An **abstract data type (ADT)** specifies observable behavior: the values it can represent, the operations clients may request, and the meaning of those operations. A **data structure** is a concrete representation that implements an ADT.

Examples:

| ADT | Possible representations |
|---|---|
| Sequence | Contiguous dynamic array, linked list, tree-backed sequence |
| Stack | Dynamic array, deque, linked list |
| Queue | Circular buffer, deque, linked list |
| Set | Balanced search tree, hash table, bit set |
| Priority queue | Binary heap, d-ary heap, balanced tree |

Choosing an ADT answers "what behavior is required?" Choosing a representation answers "how will the behavior be achieved?"

## 2. Representation Invariants

A representation invariant is a condition that must hold whenever a public operation begins or ends.

Examples:

- a dynamic array satisfies `size <= capacity`;
- a singly linked list's final node points to `nullptr` unless the list is explicitly circular;
- a binary-search tree orders keys consistently;
- a binary heap stores parent keys no greater than child keys for a min-heap;
- a DSU root is its own parent;
- a segment-tree node stores the aggregate of its represented interval.

An implementation is not validated merely because selected output looks correct. Tests should inspect or indirectly verify the invariant after every mutation.

## 3. Cost Models

State which cost is being measured:

- **worst case:** maximum cost for an input of size `N`;
- **average case:** average under a declared input distribution;
- **expected:** average over the algorithm's own randomness;
- **amortized:** average per operation over a worst-case sequence;
- **output-sensitive:** includes the size of the produced result.

Also separate:

- total structure storage;
- auxiliary storage used by one operation;
- recursion-stack storage;
- temporary storage during reallocation or rebuilding.

Do not write `O(4N)` when discussing asymptotic space; it simplifies to `O(N)`. Constants may still matter in an engineering comparison and can be discussed separately.

## 4. Contiguous and Node-Based Storage

Contiguous structures usually provide:

- constant-time indexing;
- good spatial locality;
- compact allocation metadata;
- potential relocation when capacity grows.

Node-based structures usually provide:

- stable node addresses under many mutations;
- inexpensive insertion when the position is already known;
- per-node allocation and pointer overhead;
- poorer locality in many workloads.

These are tendencies, not universal performance guarantees. Benchmark representative workloads when performance matters.

## 5. Ownership and Lifetime

Every pointer must have a documented role:

- **owner:** responsible for destroying the object;
- **non-owning observer:** may access the object only while another owner keeps it alive;
- **iterator/cursor:** temporary position into a structure and subject to invalidation rules.

Prefer standard containers and the Rule of Zero for application code. Manual node ownership is useful in a data-structure lesson, but the lesson must implement destruction and either correctly implement or explicitly disable copying and moving.

## 6. Invalid Input and Empty-State Behavior

Define behavior for:

- access to an empty structure;
- removal of a missing value;
- an index equal to or greater than size;
- duplicate insertion;
- integer overflow in sizes, weights, or aggregates;
- allocation failure where relevant.

Possible policies include documented preconditions, exceptions, `std::optional`, status values, or iterators. Avoid choosing different policies arbitrarily across methods of the same abstraction.

## 7. Testing Strategy

For every mutable structure, test:

1. construction and destruction of an empty object;
2. first insertion and removal;
3. repeated duplicate values;
4. growth and shrink boundaries;
5. copy and move behavior, or confirm those operations are disabled;
6. iterator/reference invalidation;
7. randomized operation sequences against a simple reference model;
8. invariant preservation after each operation.

Examples of reference models:

- custom stack versus `std::vector`;
- custom queue versus `std::deque`;
- DSU connectivity versus BFS on a small graph;
- Fenwick/Segment Tree results versus direct array calculation;
- custom sorting versus `std::sort`.

## 8. Standard Containers Are Canonical Elsewhere

Full API coverage for `std::vector`, `std::array`, `std::deque`, `std::list`, maps, sets, adapters, and vocabulary types belongs in [`00. Headers and Libraries`](../00.%20Headers%20and%20Libraries/README.md). This section links to those pages and focuses on representation and invariants instead of maintaining duplicate tutorials.

## Next Step

Begin the custom implementations with [`09_Linked_List.md`](09_Linked_List.md), then continue through the order in this section's [`README.md`](README.md).
