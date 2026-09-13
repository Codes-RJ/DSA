# Testing Custom Exceptions

## What to Test

Test behavior and guarantees, not only message spelling:

1. the operation succeeds for valid input;
2. the documented dynamic exception type is thrown for each failure category;
3. structured fields contain owned, correct data;
4. the object or data structure still satisfies its invariant after failure;
5. resources are released during stack unwinding;
6. a nested exception preserves the original cause;
7. a catch hierarchy routes derived failures to the intended handler;
8. secrets and unstable implementation details are absent from diagnostics.

## Minimal Test Shape

```cpp
bool threw_parse_error = false;
try {
    parse_document("invalid input");
} catch (const ParseError& error) {
    threw_parse_error = true;
    assert(error.line() == 1U);
}
assert(threw_parse_error);
```

A production test framework gives better diagnostics than raw `assert`, but the essential point is to fail the test when no exception or the wrong type is observed.

## Exercises

### 1. Configuration Loader

Design a small hierarchy for file-access, syntax, and validation failures. Decide which failures callers may recover from separately. Preserve a lower-level parsing cause when translating it to a configuration-level error.

### 2. Bounded Graph

Create a checked graph API. Decide whether an invalid vertex is a precondition violation or a reported runtime failure. Test that a rejected edge does not partially mutate adjacency storage.

### 3. Transactional Update

Update two related values while preserving the strong exception guarantee. Inject a failure between preparation and commit, then prove the original state remains observable.

### 4. Error-Model Comparison

Implement the same routine three ways: exception, `std::optional`, and explicit result object. Compare caller code, diagnostic detail, and the likelihood that failure is ignored.

## Exit Criteria

You should be able to justify why a custom type exists, place it in a shallow recovery-oriented hierarchy, preserve owned context and nested causes, and test both the failure category and post-failure invariant.

## Next Step

Continue to [Exception Specifications](../04_Exception_Specifications/README.md), then study [RAII](../05_RAII.md).
