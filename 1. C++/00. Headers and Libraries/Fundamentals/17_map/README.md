# `std::map`: Ordered Key-Value Storage

> **Header:** `<map>`
>
> **Minimum standard:** C++17
>
> **Prerequisites:** object lifetime, iterators, pairs, ordering relations, and logarithmic complexity.

`std::map<Key, T>` stores one mapped value per unique key and exposes the entries in comparator order. A balanced search tree is a common implementation, but the C++ standard specifies behavior and complexity rather than mandating a particular tree type.

## Study Order

1. [Core API and invariants](01_Core_API.md)
2. [Insertion, access, and update semantics](02_Access_and_Updates.md)
3. [Ordering, comparators, and heterogeneous lookup](03_Ordering_and_Comparators.md)
4. [Complexity, iterators, and invalidation](04_Complexity_and_Invalidation.md)
5. [Applied patterns and exercises](05_Applied_Patterns.md)

## Decision Guide

Choose `std::map` when:

- traversal must follow key order;
- predecessor, successor, or range-bound queries are required;
- logarithmic worst-case lookup is a useful contract;
- references and iterators to other elements should survive insertion and most erasures.

Consider another container when:

- key order is irrelevant and average constant-time lookup is preferable: [`std::unordered_map`](../18_unordered_map.md);
- only keys are stored: [`std::set`](../15_set.md);
- the collection is small, built once, and searched often: a sorted `std::vector` may be simpler and more cache-friendly;
- duplicate equivalent keys are required: use `std::multimap`.

## Core Invariants

- Keys are unique according to the comparator's equivalence relation.
- Iteration follows the comparator's strict ordering.
- A stored key cannot be modified through an iterator.
- Every iterator refers to a `std::pair<const Key, T>`.

## Next Step

Begin with [Core API and Invariants](01_Core_API.md).
