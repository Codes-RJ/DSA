# `std::map` Complexity and Invalidation

## Complexity Model

For `N` stored entries:

- key lookup and bound queries are `O(log N)` comparisons;
- insertion is `O(log N)` in general;
- insertion with a correct hint can be amortized constant time;
- erasing by iterator is amortized constant time;
- erasing by key adds logarithmic lookup cost;
- visiting every entry is `O(N)`;
- storing the map is `O(N)` total space, with implementation-dependent per-node overhead.

Comparator cost is part of real running time. If comparing keys costs `C`, a logarithmic lookup performs `O(C log N)` work.

## Iterator and Reference Stability

Insertion does not invalidate iterators or references to existing entries. Erasure invalidates only iterators and references to the erased entries. `clear()` invalidates all of them.

These guarantees do not extend object lifetime beyond the container's lifetime, and they do not make concurrent mutation safe.

Safe erase-while-iterating pattern:

```cpp
for (auto position = values.begin(); position != values.end();) {
    if (should_remove(position->first, position->second)) {
        position = values.erase(position);
    } else {
        ++position;
    }
}
```

## Memory and Locality

The standard does not require a node-based balanced tree, but common implementations allocate nodes separately. Compared with a sorted vector, this often means:

- more allocation and pointer overhead;
- weaker spatial locality;
- stable references under insertion;
- cheaper insertion without shifting a contiguous suffix.

Measure representative workloads. Big-O notation alone cannot decide between `map`, `unordered_map`, and a sorted flat sequence.

## Concurrency

Separate threads may read the same container concurrently when no thread mutates it. Unsynchronized mutation combined with access from another thread is a data race. Iterator stability is not a synchronization-safety guarantee.

## Complexity Exercises

1. Compare `K` independent lookups with one ordered traversal after sorting the queries.
2. Explain the cost of building a map from already sorted input with and without a correct insertion hint.
3. Benchmark integer lookup in `std::map`, `std::unordered_map`, and a sorted vector for several collection sizes.

## Next Step

Continue to [Applied Patterns](05_Applied_Patterns.md).
