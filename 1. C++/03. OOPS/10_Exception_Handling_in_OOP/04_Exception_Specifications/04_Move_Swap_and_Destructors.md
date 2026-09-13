# Move, Swap, Destructors, and Containers

## Why Non-Throwing Move Matters

When a `std::vector` grows, it must relocate existing elements. If copying is available and moving might throw, an implementation can prefer copying to preserve stronger failure behavior. A truthful non-throwing move constructor lets generic code choose moving confidently.

Prefer the Rule of Zero. If a class owns only standard RAII members, compiler-generated move operations often have the right conditional exception specification.

## A Custom Resource Type

```cpp
#include <cstddef>
#include <memory>
#include <utility>

class Buffer {
public:
    explicit Buffer(std::size_t size)
        : data_(std::make_unique<int[]>(size)), size_(size) {}

    Buffer(Buffer&&) noexcept = default;
    Buffer& operator=(Buffer&&) noexcept = default;

    Buffer(const Buffer&) = delete;
    Buffer& operator=(const Buffer&) = delete;

    friend void swap(Buffer& left, Buffer& right) noexcept {
        using std::swap;
        swap(left.data_, right.data_);
        swap(left.size_, right.size_);
    }

private:
    std::unique_ptr<int[]> data_;
    std::size_t size_ = 0U;
};
```

The allocation occurs in the ordinary constructor, not in the move operation. Moving a `std::unique_ptr` transfers ownership without allocating.

## Destructors

Destructors are normally non-throwing. An exception escaping a destructor during stack unwinding causes termination. If cleanup can fail:

- provide an explicit operation that reports the failure before destruction;
- make the destructor perform best-effort cleanup without throwing;
- record diagnostics through a channel whose own failure behavior is controlled.

Do not blindly perform allocating log operations inside a `noexcept` destructor.

## Swap

A non-throwing swap is useful for commit/rollback designs and generic algorithms. Its specification must reflect every member swap. For generic members, derive the condition from the actual swap expressions instead of assuming all swaps are non-throwing.

## Container Wrappers

Do not write this:

```cpp
template <class T>
void append(std::vector<T>& values, T value)
    noexcept(std::is_nothrow_move_constructible_v<T>);
```

Vector growth may allocate, so the condition does not describe the complete operation. The wrapper should normally be potentially throwing.

## Next Step

Continue to [Auditing and Testing](05_Auditing_and_Testing.md).
