# Auditing and Testing Non-Throwing Code

## Audit Every Operation

Before declaring `noexcept`, inspect:

- allocations and container growth;
- string construction and formatting;
- user-defined constructors, assignments, conversions, and destructors;
- comparator, hash, callback, and visitor invocations;
- stream and logging operations;
- locks and operating-system calls;
- cleanup executed on every branch.

A comment such as “this should not throw” is not evidence. Trace the actual operations and their contracts.

## Test Failure Paths

Ordinary unit tests cannot safely catch an exception that escapes a `noexcept` function because termination occurs first. Instead:

1. test potentially throwing helpers independently;
2. inject failures before the non-throwing commit step;
3. verify the containing object's invariant after each injected failure;
4. run intentional termination checks in a separate process if the contract itself must be tested;
5. use sanitizers to find lifetime and undefined-behavior defects that exception tests cannot detect.

## Review Matrix

| Question | Evidence expected |
|---|---|
| Is `noexcept` semantically required? | Caller or generic algorithm relies on the guarantee |
| Is it mechanically accurate? | Every expression in every branch has been audited |
| Does a conditional specification match the exact expression? | Trait or `noexcept(expr)` mirrors the implementation |
| Is object state safe if a helper throws? | Invariant-focused test or prepare/commit structure |
| Can cleanup report failure explicitly? | Separate `close`, `flush`, or commit operation where appropriate |
| Are external effects covered by the claim? | Documented transaction boundary |

## Exercises

1. Audit a vector wrapper and identify why insertion is not non-throwing.
2. Implement a value type whose swap is conditionally `noexcept` based on its members.
3. Give a mutating operation the strong guarantee with a temporary and commit step.
4. Design a resource wrapper with explicit error-reporting cleanup and a non-throwing destructor.
5. Explain why a runtime Boolean cannot select a function's exception specification.

## Exit Criteria

You can distinguish `noexcept` from the strong guarantee, derive a conditional specification from an exact generic operation, explain vector relocation behavior, and audit a destructor without assuming that logging is harmless.

## Next Step

Continue to [RAII](../05_RAII.md).
