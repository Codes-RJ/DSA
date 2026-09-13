# Choosing an STL Container

[← Return to the main learning path](../../LEARNING_PATH.md)

- **Role:** Reference and decision guide
- **Prerequisites:** Complexity notation, iterators, and basic `std::vector`
- **Core standard:** C++17

This page helps you choose a standard container from the operations and guarantees your program needs. It does not repeat the full APIs owned by the individual header lessons.

## Start With the Requirement

Ask these questions in order:

1. Must elements remain contiguous in memory?
2. Is position/order meaningful, or are values addressed by a key?
3. Must keys be sorted?
4. Which operations dominate: indexed access, insertion, deletion, lookup, minimum/maximum, or traversal?
5. Do iterator/reference invalidation rules fit the program?
6. Is expected complexity acceptable, or is a deterministic worst-case bound required?

Do not choose a linked container merely because insertion is described as `O(1)`. Finding the insertion position may still cost `O(N)`, and poor locality may dominate real performance.

## Container Families

| Need | First candidate | Important tradeoff | Canonical lesson |
|---|---|---|---|
| General resizable sequence | `std::vector` | Fast random access and locality; growth/middle insertion can invalidate | [`vector`](../Fundamentals/09_vector.md) |
| Fixed-size contiguous sequence | `std::array` | Size is part of the type; no growth | [`array`](../Fundamentals/11_array/README.md) |
| Frequent operations at both ends | `std::deque` | Random access without one contiguous allocation | [`deque`](../Fundamentals/12_deque.md) |
| Stable node references and known-position insertion | `std::list` | No random access; allocation and locality costs | [`list`](../Fundamentals/13_list.md) |
| Minimal-overhead singly linked nodes | `std::forward_list` | Forward traversal only; operations use “before” positions | [`forward_list`](../Fundamentals/14_forward_list.md) |
| Sorted unique keys | `std::set` | Logarithmic operations; node-based overhead | [`set`](../Fundamentals/15_set.md) |
| Sorted key/value pairs | `std::map` | Logarithmic operations and ordered traversal | [`map`](../Fundamentals/17_map/README.md) |
| Expected constant-time unique-key membership | `std::unordered_set` | No ordering; rehashing and collision behavior matter | [`unordered_set`](../Fundamentals/16_unordered_set.md) |
| Expected constant-time key/value lookup | `std::unordered_map` | No ordering; hash quality and load factor matter | [`unordered_map`](../Fundamentals/18_unordered_map.md) |
| LIFO access only | `std::stack` | Restricted adapter interface | [`stack`](../Fundamentals/19_stack.md) |
| FIFO access only | `std::queue` | Restricted adapter interface | [`queue`](../Fundamentals/20_queue.md) |
| Repeated access to highest-priority item | `std::priority_queue` | No arbitrary search/removal | [`priority_queue`](../Fundamentals/21_priority_queue.md) |

## Decision Guide

### Choose `std::vector` by default for sequences

It is the normal first choice when you need iteration, indexed access, sorting, or append-heavy storage. Contiguous layout works well with caches and standard algorithms. Consider another container only when a concrete requirement conflicts with vector's invalidation or insertion costs.

### Choose ordered associative containers for order-dependent queries

Use `std::set` or `std::map` when you need sorted iteration, lower/upper bounds, predecessor/successor logic, or deterministic logarithmic operations. If none of those properties is used, an unordered container may be simpler and faster on average.

### Choose unordered containers for key-based lookup without ordering

Use `std::unordered_set` or `std::unordered_map` when expected constant-time membership/lookup matters and iteration order does not. State the hash/equality assumptions. Worst-case operations can be linear, and rehashing invalidates iterators.

### Choose node-based sequences only from an operation contract

`std::list` and `std::forward_list` are appropriate when you already hold valid positions and need stable node references or splicing. They are usually poor substitutes for a vector when the program mostly scans, sorts, or indexes data.

### Choose adapters when a restricted interface expresses the invariant

`std::stack`, `std::queue`, and `std::priority_queue` deliberately hide unrelated operations. Their narrower interface helps communicate LIFO, FIFO, or priority behavior.

## Complexity Summary

`N` is the number of stored elements. Unordered-container bounds below are expected/amortized unless stated otherwise.

| Container | Indexed access | End insertion | Middle/known-position insertion | Key lookup |
|---|---:|---:|---:|---:|
| `vector` | `O(1)` | amortized `O(1)` | `O(N)` | `O(N)` unless sorted and binary searched |
| `array` | `O(1)` | not supported | not supported | `O(N)` unless sorted and binary searched |
| `deque` | `O(1)` | amortized `O(1)` at either end | `O(N)` | `O(N)` |
| `list` | `O(N)` | `O(1)` | `O(1)` with a known iterator | `O(N)` |
| `forward_list` | `O(N)` | `O(1)` at front | `O(1)` after a known iterator | `O(N)` |
| `set` / `map` | not positional | `O(log N)` | `O(log N)` | `O(log N)` |
| `unordered_set` / `unordered_map` | not positional | expected `O(1)` | expected `O(1)` | expected `O(1)`, worst-case `O(N)` |

Complexity alone is insufficient. Include memory overhead, cache locality, invalidation, ordering, and adversarial input in the decision.

## Invalidation Questions

Before storing an iterator, pointer, or reference into a container, check the canonical lesson for the exact operation. The high-level risks are:

- a `vector` reallocation invalidates all iterators, pointers, and references into it;
- vector/deque insertion or erasure can invalidate positions at or after the modification, with deque having additional operation-specific rules;
- list/forward-list operations normally preserve references to other elements;
- erasing an element invalidates handles to that element in every container;
- unordered-container rehashing invalidates iterators, while references/pointers to elements generally remain valid unless the element is erased;
- swapping/moving containers has allocator- and operation-specific details that belong in the canonical reference page.

Never rely on this summary when exact lifetime behavior is part of correctness; consult the relevant container specification/reference.

## DSA Mapping

| Abstract need | Standard implementation | What a DSA learner should still understand |
|---|---|---|
| Dynamic array | `std::vector` | geometric growth, amortized analysis, relocation, invalidation |
| Stack | `std::stack` or `std::vector` | LIFO invariant and representation tradeoffs |
| Queue/deque | `std::queue` / `std::deque` | FIFO invariant and circular-buffer alternatives |
| Ordered dictionary | `std::map` | balanced-search-tree invariants and logarithmic operations |
| Hash table | `std::unordered_map` | hashing, collisions, load factor, rehashing, adversarial cases |
| Heap | `std::priority_queue` | heap shape/order invariants and sift operations |

Use the standard container in application code unless the exercise explicitly asks you to implement the structure. Custom implementations belong in [Data Structures](../../04.%20Data%20Structures/README.md), not in API reference pages.

## Common Selection Errors

- Using `map[key]` only to test membership and accidentally inserting a value.
- Depending on `unordered_map` iteration order.
- Calling `reserve` as if it changed a vector's size.
- Keeping vector iterators across an operation that may reallocate.
- Choosing `list` for “fast insertion” without already having the insertion iterator.
- Using a priority queue when arbitrary deletion or priority updates are required.
- Assuming average unordered-container complexity is a deterministic worst-case guarantee.
- Treating container adapter internals as part of their public contract.

## Practice Decisions

For each scenario, name the first candidate and the requirement that could change your choice:

1. Store graph adjacency lists and traverse every edge.
2. Count word frequencies without needing sorted output.
3. Print a leaderboard in key order.
4. Maintain the next job by priority.
5. Keep a sliding window with insertion/removal at opposite ends.
6. Preserve stable references while splicing whole ranges.

Then implement one scenario with two plausible containers and compare correctness, asymptotic cost, and measured behavior. A benchmark without a representative workload is not evidence of a generally superior container.

## Next Step

Return to [Checkpoint 1 of the learning path](../../LEARNING_PATH.md#checkpoint-1-complexity-arrays-hashing-sorting-and-binary-search) or open the canonical lesson for the container your current problem requires.
