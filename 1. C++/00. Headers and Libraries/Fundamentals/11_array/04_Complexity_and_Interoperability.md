# `std::array` Complexity and Interoperability

## Complexity

| Operation | Complexity |
|---|---:|
| Index, `front`, `back`, `data` | `O(1)` |
| `size`, `empty`, `max_size` | `O(1)` |
| Iterate, search, fill | `O(N)` |
| Copy, assignment, comparison | Up to `O(N)` |
| Swap | `O(N)` |

Storage is `O(N)` and the elements are contiguous. The array object contains its element storage; it does not separately allocate merely because it is a `std::array`.

## C Interoperability

Use `data()` and `size()` when an API accepts a pointer and element count:

```cpp
void consume(const int* data, std::size_t size);

std::array<int, 4> values{1, 2, 3, 4};
consume(values.data(), values.size());
```

The pointer is non-owning. It remains valid only while the array exists and has not been moved or destroyed in a way that ends the referenced object's lifetime.

## References and Iterators

The array cannot grow or shrink, so ordinary element assignment does not invalidate pointers or iterators. Swapping two arrays preserves pointer validity to elements but the pointed-to values are now associated with the other array object through element-wise exchange.

## Selection Checklist

Choose `std::array` when:

- the extent is known at compile time and belongs in the type;
- contiguous storage is required;
- value semantics are useful;
- stack or inline object storage is appropriate for the element count.

Large arrays can make objects expensive to copy and may exceed practical automatic-storage limits. Fixed size alone does not imply that `std::array` is always the best representation.

## Next Step

Continue to [Applied Patterns and Exercises](05_Applied_Patterns.md).
