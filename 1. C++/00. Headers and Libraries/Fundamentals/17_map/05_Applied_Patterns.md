# `std::map` Applied Patterns

## Frequency Counting in Key Order

```cpp
#include <map>
#include <string>
#include <vector>

std::map<std::string, std::size_t>
ordered_frequencies(const std::vector<std::string>& words) {
    std::map<std::string, std::size_t> counts;
    for (const std::string& word : words) {
        ++counts[word];
    }
    return counts;
}
```

Use an unordered map if ordered output and bound queries are unnecessary.

## Half-Open Range Query

```cpp
template <class Map, class Key>
auto entries_between(Map& values, const Key& low, const Key& high) {
    return std::make_pair(values.lower_bound(low), values.lower_bound(high));
}
```

The returned iterators remain valid only while the container exists and the referenced entries are not erased.

## Sparse Index

A map can represent only non-default positions of a large logical index space. Before choosing it, compare:

- number of occupied positions;
- need for ordered neighbor queries;
- update frequency;
- key and node memory cost;
- whether coordinate compression plus a vector would be simpler.

## Exercises and Cache Design

A map alone does not implement cache eviction. An LRU cache normally combines:

- an associative lookup from key to list iterator;
- a linked sequence representing recency;
- one ownership policy for values;
- explicit capacity and invalidation rules.

Do not present `std::map` as a complete cache merely because it stores key-value pairs.

## Exercises

1. Build a time-indexed event log and query `[start, end)`.
2. Count words case-insensitively with a comparator, then explain its equivalence rules.
3. Implement an interval lookup using `upper_bound` and test boundary points.
4. Compare `try_emplace` and `operator[]` with a mapped type that logs construction.
5. Differentially test random insert/find/erase operations against a simple sorted-vector model.

## Exit Criteria

You can choose between `map`, `unordered_map`, and a sorted vector; explain comparator equivalence; select an access/update operation without accidental insertion; and state iterator invalidation precisely.

## Next Step

Continue to [`std::unordered_map`](../18_unordered_map.md) and compare its guarantees.
