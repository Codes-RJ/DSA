# Data Structures in C++

> **Role in the curriculum:** This section teaches abstract data types, invariants, ownership, and custom implementations. Standard-library API reference material has one canonical home in [`00. Headers and Libraries`](../00.%20Headers%20and%20Libraries/README.md).

## Prerequisites

Before starting, complete:

1. [`01. Basics`](../01.%20Basics/README.md), especially functions, arrays, references, pointers, lifetime, and error handling.
2. The essential standard-library lessons for [`vector`](../00.%20Headers%20and%20Libraries/Fundamentals/02_vector.md), [`string`](../00.%20Headers%20and%20Libraries/Fundamentals/03_string.md), and [`algorithm`](../00.%20Headers%20and%20Libraries/Fundamentals/04_algorithm.md).
3. Basic asymptotic analysis from [`02. Basic Problems`](../02.%20Basic%20Problems/README.md).

## Canonical Study Order

| Step | Topic | Purpose |
|---:|---|---|
| 1 | [Foundations](Theory.md) | ADTs, invariants, cost models, storage, and ownership |
| 2 | [Linked Lists](09_Linked_List.md) | Node ownership, insertion, deletion, traversal, and cycle detection |
| 3 | [Custom Stacks and Queues](10_Custom_Stack_and_Queue.md) | LIFO/FIFO ADTs and array/list implementations |
| 4 | [Trie](11_Trie.md) | Prefix search and bitwise tries |
| 5 | [Disjoint-Set Union](12_Disjoint_Set_Union.md) | Dynamic connectivity, path compression, and union by rank/size |
| 6 | [Fenwick Tree](14_Fenwick_Tree.md) | Prefix aggregation with compact logarithmic updates |
| 7 | [Segment Tree](13_Segment_Tree.md) | General range queries, updates, and lazy propagation |

The Fenwick Tree appears before the Segment Tree because it provides a smaller introduction to logarithmic range-query structures.

## Standard Containers: Learn Once, Reuse Everywhere

The former copies of standard-container tutorials in this folder were removed. Use these canonical pages:

### Sequence containers

- [`std::array`](../00.%20Headers%20and%20Libraries/Fundamentals/11_array/README.md)
- [`std::vector`](../00.%20Headers%20and%20Libraries/Fundamentals/02_vector.md)
- [`std::deque`](../00.%20Headers%20and%20Libraries/Fundamentals/12_deque.md)
- [`std::list`](../00.%20Headers%20and%20Libraries/Fundamentals/13_list.md)
- [`std::forward_list`](../00.%20Headers%20and%20Libraries/Fundamentals/14_forward_list.md)

### Container adapters

- [`std::stack`](../00.%20Headers%20and%20Libraries/Fundamentals/19_stack.md)
- [`std::queue`](../00.%20Headers%20and%20Libraries/Fundamentals/20_queue.md)
- [`std::priority_queue`](../00.%20Headers%20and%20Libraries/Fundamentals/21_priority_queue.md)

### Ordered and unordered associative containers

- [`std::set`](../00.%20Headers%20and%20Libraries/Fundamentals/15_set.md)
- [`std::map`](../00.%20Headers%20and%20Libraries/Fundamentals/17_map/README.md)
- [`std::unordered_set`](../00.%20Headers%20and%20Libraries/Fundamentals/16_unordered_set.md)
- [`std::unordered_map`](../00.%20Headers%20and%20Libraries/Fundamentals/18_unordered_map.md)

### Utility and specialized value types

- [`std::pair` and general utilities](../00.%20Headers%20and%20Libraries/Fundamentals/09_utility.md)
- [`std::tuple`](../00.%20Headers%20and%20Libraries/Fundamentals/10_tuple.md)
- [`std::optional`](../00.%20Headers%20and%20Libraries/Fundamentals/35_optional.md)
- [`std::variant`](../00.%20Headers%20and%20Libraries/Fundamentals/36_variant.md)
- [`std::any`](../00.%20Headers%20and%20Libraries/Fundamentals/37_any.md)
- [`std::bitset`](../00.%20Headers%20and%20Libraries/Fundamentals/38_bitset.md)
- [`std::valarray`](../00.%20Headers%20and%20Libraries/Fundamentals/39_valarray.md)

## What Every Custom Structure Must Explain

Each custom implementation in this section should state:

1. **Abstract behavior:** What operations does the ADT promise?
2. **Representation:** How is state stored?
3. **Invariant:** What must remain true after every operation?
4. **Ownership:** Who creates and destroys allocated objects?
5. **Complexity:** Worst-case and amortized bounds where relevant.
6. **Invalid input:** Preconditions, exceptions, optional results, or sentinels.
7. **Iterator/reference stability:** What becomes invalid after mutation?
8. **Tests:** Empty, singleton, duplicate, boundary, copy/move, and randomized cases.

## Selection Guide

| Need | Preferred starting point |
|---|---|
| Contiguous indexed storage | `std::vector` |
| Fixed-size contiguous storage | `std::array` |
| Frequent insertion at both ends | `std::deque` |
| LIFO/FIFO behavior | `std::stack` / `std::queue` or the custom ADT lesson |
| Ordered lookup | `std::set` / `std::map` |
| Average constant-time lookup | `std::unordered_set` / `std::unordered_map` |
| Prefix lookup | Trie |
| Dynamic connectivity | DSU |
| Prefix sums with point updates | Fenwick Tree |
| General interval aggregation or lazy range updates | Segment Tree |

## Exit Criteria

Before continuing to trees and graphs, you should be able to:

- explain the difference between an ADT and its representation;
- state and verify a representation invariant;
- implement a linked list, stack, queue, trie, and DSU;
- choose standard containers without relying on implementation folklore;
- distinguish total structure storage from auxiliary operation space;
- explain ownership and lifetime for every pointer in a custom structure;
- create tests that compare a custom implementation with a simple reference model.

## Next Step

Continue to [`05. Trees and Graphs`](../05.%20Trees%20and%20Graphs/README.md) or return to the canonical [`LEARNING_PATH.md`](../LEARNING_PATH.md).
