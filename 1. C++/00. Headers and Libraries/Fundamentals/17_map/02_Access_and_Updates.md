# `std::map` Access and Update Semantics

## Choose the Operation by Intent

| Intent | Preferred operation | Missing key |
|---|---|---|
| Observe without insertion | `find` or `at` | `find` returns `end`; `at` throws |
| Count occurrences | `operator[]` | Inserts a value-initialized mapped value |
| Insert only | `insert` or `emplace` | Creates the entry |
| Insert only, construct from arguments | `try_emplace` | Constructs the mapped value only if insertion occurs |
| Insert or replace | `insert_or_assign` | Creates the entry |

## The `operator[]` Trap

```cpp
std::map<std::string, int> counts;
const int value = counts["missing"]; // Inserts {"missing", 0}.
```

This behavior is convenient for frequency counting and dangerous for read-only lookup. It also requires the mapped type to be default-constructible.

Use `find` for a non-throwing observation or `at` when a missing key violates the caller's contract:

```cpp
const auto position = counts.find("missing");
if (position != counts.end()) {
    const int observed = position->second;
}

const int required = counts.at("required"); // Throws std::out_of_range if absent.
```

## C++17 Insertion Results

```cpp
auto [position, inserted] = counts.try_emplace("tree", 1);
if (!inserted) {
    ++position->second;
}

counts.insert_or_assign("graph", 4);
```

`try_emplace` is especially useful when construction of the mapped value is expensive or the mapped type cannot be copied.

## Exception Guarantees

Insertion can allocate and can invoke constructors and the comparator. Do not mark a wrapper `noexcept` merely because moving `T` is non-throwing. If insertion throws, standard containers generally preserve their invariants; the exact guarantee can depend on the operation and the involved types.

## Node Handles

C++17 node handles allow ownership of a node to move between compatible associative containers and permit changing a detached key:

```cpp
auto node = counts.extract("tree");
if (!node.empty()) {
    node.key() = "binary_tree";
    counts.insert(std::move(node));
}
```

Always inspect the insertion result when the destination may already contain an equivalent key.

## Exercises

1. Implement a frequency counter using `try_emplace` rather than `operator[]`.
2. Store `std::unique_ptr<Record>` values without copying them.
3. Rename a key with a node handle and handle a destination collision.

## Next Step

Continue to [Ordering and Comparators](03_Ordering_and_Comparators.md).
