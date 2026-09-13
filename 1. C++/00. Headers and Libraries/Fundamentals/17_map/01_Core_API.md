# `std::map` Core API and Invariants

## Construction

```cpp
#include <map>
#include <string>

std::map<std::string, int> score;
std::map<std::string, int> initialized{
    {"Ada", 95},
    {"Grace", 98},
};
```

The template parameters are conceptually:

```cpp
template<class Key,
         class T,
         class Compare = std::less<Key>,
         class Allocator = /* implementation-defined default */>
class map;
```

Do not depend on a concrete internal node or tree layout.

## Essential Operations

| Operation | Meaning | Complexity |
|---|---|---:|
| `empty()`, `size()` | Inspect collection size | `O(1)` |
| `find(key)` | Iterator to equivalent key or `end()` | `O(log N)` |
| `contains(key)` | Whether an equivalent key exists; C++20 | `O(log N)` |
| `lower_bound(key)` | First key not ordered before `key` | `O(log N)` |
| `upper_bound(key)` | First key ordered after `key` | `O(log N)` |
| `equal_range(key)` | Pair of lower and upper bounds | `O(log N)` |
| `insert`, `emplace` | Add when no equivalent key exists | `O(log N)` |
| `erase(key)` | Remove an equivalent key | `O(log N)` plus destroyed elements |
| `erase(iterator)` | Remove at a known position | Amortized `O(1)` |
| `clear()` | Remove every entry | `O(N)` |

## Ordered Iteration

```cpp
for (const auto& entry : initialized) {
    const std::string& name = entry.first;
    const int value = entry.second;
    // name is visited in ascending comparator order.
}
```

In C++17, a structured binding is often clearer:

```cpp
for (const auto& [name, value] : initialized) {
    // name has const-qualified key semantics.
}
```

## Empty and Missing States

`end()` is a past-the-end iterator and must not be dereferenced. Lookup code should make the missing case explicit:

```cpp
const auto position = initialized.find("Katherine");
if (position == initialized.end()) {
    // Missing-key policy belongs here.
}
```

## Exercises

1. Build a map from country code to country name and iterate in code order.
2. Find all keys in the half-open interval `[low, high)` with `lower_bound`.
3. Explain why keys are const through iterators while mapped values are mutable.

## Next Step

Continue to [Access and Updates](02_Access_and_Updates.md).
