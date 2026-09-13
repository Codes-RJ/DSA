# Exception-Safety Guarantees

An exception-safety guarantee describes what callers can observe after an operation fails.

| Guarantee | After an exception |
|---|---|
| No guarantee | Invariants or resource safety may be lost |
| Basic guarantee | Invariants hold and resources are not leaked, but state may have changed |
| Strong guarantee | Observable state is unchanged; the operation behaves transactionally |
| Non-throwing guarantee | The operation completes without allowing an exception to escape |

## Strong Guarantee by Prepare and Commit

```cpp
#include <string>
#include <utility>

class Profile {
public:
    void rename(std::string proposed) {
        validate(proposed);       // May throw; object is unchanged.
        name_.swap(proposed);     // Non-throwing commit for this allocator setup.
    }

private:
    static void validate(const std::string& value);
    std::string name_;
};
```

Build the new state in temporary objects, then commit with operations whose exception behavior is known. This often costs simpler and safer than trying to undo many mutations.

## Basic Guarantee

The basic guarantee is appropriate when partial progress is acceptable and the resulting state remains valid and documented. A stream extraction or batch-processing operation may consume some input before reporting failure.

## Preconditions Are Different

Exception safety does not define behavior after undefined behavior or a violated unchecked precondition. If an algorithm requires a valid index or non-negative edge weight, document and enforce the chosen contract before discussing its failure guarantee.

## External Side Effects

Copy-and-swap can restore in-memory state, but it cannot automatically undo files written, messages sent, or payments requested. Claims of a strong guarantee must define the observable system boundary.

## Review Questions

1. What invariant must hold before and after the operation?
2. Which expressions can throw?
3. What state changes before the final potentially throwing expression?
4. Can changes be prepared in temporary storage?
5. Are external side effects reversible or idempotent?

## Next Step

Continue to [Move, Swap, and Destructors](04_Move_Swap_and_Destructors.md).
