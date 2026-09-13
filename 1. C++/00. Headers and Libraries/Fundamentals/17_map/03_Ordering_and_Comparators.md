# `std::map` Ordering and Comparators

## Strict Weak Ordering

The comparator must behave as a strict weak ordering. In practical terms:

- `compare(x, x)` is false;
- if `compare(a, b)` is true, `compare(b, a)` is false;
- ordering is transitive;
- the induced equivalence relation is transitive;
- the result must not change while affected keys remain in the map.

The map treats `a` and `b` as equivalent when both `compare(a, b)` and `compare(b, a)` are false. Equality via `operator==` does not determine key uniqueness.

## Custom Record Ordering

```cpp
#include <map>
#include <string>
#include <tuple>

struct StudentKey {
    std::string family_name;
    std::string given_name;
    int id;
};

struct StudentKeyLess {
    bool operator()(const StudentKey& left,
                    const StudentKey& right) const {
        return std::tie(left.family_name, left.given_name, left.id) <
               std::tie(right.family_name, right.given_name, right.id);
    }
};

std::map<StudentKey, int, StudentKeyLess> grades;
```

Never base the comparator on mutable external state that can change the relative order of stored keys.

## Descending Order

```cpp
std::map<int, std::string, std::greater<int>> descending;
```

Iteration is now descending according to the comparator; the meanings of `lower_bound` and `upper_bound` must also be interpreted through that ordering rather than ordinary numeric `<`.

## Transparent Lookup

A transparent comparator such as `std::less<>` can allow lookup with a compatible key-like type without first constructing a `Key` object:

```cpp
#include <map>
#include <string>

std::map<std::string, int, std::less<>> counts;
const char* query = "tree";

// Heterogeneous find support depends on compatible comparisons.
const auto position = counts.find(query);
```

With a custom comparator, expose `using is_transparent = void;` and provide valid comparisons between every supported lookup type. Do this only when it measurably clarifies or improves a real lookup path.

## Comparator Checklist

1. Does it define equivalence exactly as the domain requires?
2. Is it stable for the lifetime of stored keys?
3. Does it avoid subtraction that can overflow?
4. Can its operations throw, and does the surrounding API account for that?
5. Do tests cover keys that are equivalent but not equal?

## Next Step

Continue to [Complexity and Invalidation](04_Complexity_and_Invalidation.md).
