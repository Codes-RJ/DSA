# Mathematical Patterns

These exercises combine sequence generation with output structure. Separate the mathematical generator from the renderer so each can be tested independently.

## Exercises

1. **Prime triangle:** fill rows with successive prime numbers.
2. **Fibonacci triangle:** fill rows with successive Fibonacci values.
3. **Factorial rows:** print `0!` through a chosen limit.
4. **Binomial triangle:** produce Pascal's triangle with checked arithmetic.
5. **Wave samples:** sample a sine wave and map values to rows.
6. **Recursive tree:** generate branch segments to a fixed depth, then render them.

## Numeric Contracts

For every generator, define:

- the largest supported input;
- the integer or floating-point type used;
- whether overflow is rejected, reported, or intentionally allowed;
- whether repeated primality tests are acceptable or a sieve is required;
- how sampled real values map to discrete output rows.

Fibonacci numbers and factorials overflow fixed-width integers quickly. Checking only after an overflowing addition or multiplication is too late because signed overflow is undefined behavior. Check before performing the operation.

## Complexity Questions

1. Is the sequence generated once, or recomputed for every cell?
2. Does a prime generator trial-divide every candidate or reuse known primes?
3. Is the rendering cost smaller than, equal to, or larger than the number of emitted characters?
4. Does recursion create output-sized work or an exponential number of branches?

## Next Step

Continue to [Performance and Testing](06_Performance_and_Testing.md).
