# 15_Master_Theorem.md

## Master Theorem

### Definition

The Master Theorem provides a direct way to solve recurrence relations of the form:

```
T(n) = a * T(n/b) + f(n)
```

where:
- a ≥ 1 (number of subproblems)
- b > 1 (factor by which problem size reduces)
- f(n) is the cost of dividing and combining (asymptotically positive)

### The Three Cases

| Case | Condition | Solution |
|------|-----------|----------|
| Case 1 | f(n) = O(n^(log_b(a) - ε)) for some ε > 0 | T(n) = Θ(n^(log_b(a))) |
| Case 2 | f(n) = Θ(n^(log_b(a)) * log^k(n)) for some k ≥ 0 | T(n) = Θ(n^(log_b(a)) * log^(k+1)(n)) |
| Case 3 | f(n) = Ω(n^(log_b(a) + ε)) for some ε > 0 and a*f(n/b) ≤ c*f(n) for some c < 1 | T(n) = Θ(f(n)) |

### Case 1 Explanation

When the work to divide and combine (f(n)) grows slower than the work from the recursive calls.

**Example:** T(n) = 2T(n/2) + n

Here a=2, b=2, log_b(a) = log₂2 = 1
f(n) = n = Θ(n¹)
Compare n¹ with n^(log_b(a)) = n¹
This is Case 2 (equal, not Case 1)

**Actual Case 1 example:** T(n) = 4T(n/2) + n

a=4, b=2, log_b(a) = log₂4 = 2
f(n) = n = O(n^(2-ε)) for ε=1
→ T(n) = Θ(n²)

### Case 2 Explanation

When the work to divide and combine is equal to the work from the recursive calls.

**Example:** T(n) = 2T(n/2) + n

a=2, b=2, log_b(a) = 1
f(n) = n = Θ(n¹ * log⁰(n))
k = 0
→ T(n) = Θ(n¹ * log¹(n)) = Θ(n log n)

**Example with log:** T(n) = 2T(n/2) + n log n

a=2, b=2, log_b(a) = 1
f(n) = n log n = Θ(n¹ * log¹(n))
k = 1
→ T(n) = Θ(n¹ * log²(n)) = Θ(n log² n)

### Case 3 Explanation

When the work to divide and combine grows faster than the work from the recursive calls.

**Example:** T(n) = 2T(n/2) + n²

a=2, b=2, log_b(a) = 1
f(n) = n² = Ω(n^(1+ε)) for ε=1
Check regularity: a*f(n/b) = 2*(n/2)² = 2*(n²/4) = n²/2 ≤ c*n² for c=1/2
→ T(n) = Θ(n²)

### Examples and Solutions

| Recurrence | a | b | log_b(a) | f(n) | Case | Solution |
|------------|---|---|----------|------|------|----------|
| T(n) = 2T(n/2) + 1 | 2 | 2 | 1 | O(1) | Case 1 | Θ(n) |
| T(n) = 2T(n/2) + n | 2 | 2 | 1 | Θ(n) | Case 2 | Θ(n log n) |
| T(n) = 2T(n/2) + n² | 2 | 2 | 1 | Ω(n²) | Case 3 | Θ(n²) |
| T(n) = 4T(n/2) + n | 4 | 2 | 2 | O(n) | Case 1 | Θ(n²) |
| T(n) = 4T(n/2) + n² | 4 | 2 | 2 | Θ(n²) | Case 2 | Θ(n² log n) |
| T(n) = 4T(n/2) + n³ | 4 | 2 | 2 | Ω(n³) | Case 3 | Θ(n³) |
| T(n) = 3T(n/3) + n | 3 | 3 | 1 | Θ(n) | Case 2 | Θ(n log n) |
| T(n) = 7T(n/2) + n² | 7 | 2 | log₂7≈2.81 | O(n²) | Case 1 | Θ(n^2.81) |
| T(n) = 2T(n/4) + √n | 2 | 4 | log₄2=0.5 | Θ(√n) | Case 2 | Θ(√n log n) |

### Visualization of Cases

```
Case 1: f(n) grows slower
        ^
        |  n^(log_b(a))
        |  /
        | /
        |/_____ f(n)
        +----------> n

Case 2: f(n) grows at same rate
        ^
        |  n^(log_b(a)) and f(n)
        |  ================
        |
        +----------> n

Case 3: f(n) grows faster
        ^
        |  f(n)
        |    \
        |     \
        |      n^(log_b(a))
        +----------> n
```

### When Master Theorem Does NOT Apply

The Master Theorem does not apply when:

1. f(n) is not asymptotically positive
2. a is not constant
3. b is not constant
4. f(n) is not of the form n^k or n^k log^p n
5. The recurrence is not of the form T(n) = aT(n/b) + f(n)

### Examples Where Master Theorem Fails

| Recurrence | Why it fails |
|------------|--------------|
| T(n) = 2T(n/2) + n/log n | f(n) is not polynomial |
| T(n) = T(n-1) + n | Not of the form T(n/b) |
| T(n) = 2T(n/2) + 2^n | f(n) grows too fast, not polynomial |
| T(n) = 0.5T(n/2) + n | a < 1 (not allowed) |

### Alternative Methods

When Master Theorem does not apply:

1. **Recursion Tree Method** - Draw the recursion tree and sum costs
2. **Substitution Method** - Guess solution and prove by induction
3. **Akra-Bazzi Method** - More general form for divide-and-conquer recurrences

### Practice Problems

Solve the following recurrences using Master Theorem:

1. T(n) = 9T(n/3) + n
2. T(n) = T(2n/3) + 1
3. T(n) = 3T(n/4) + n log n
4. T(n) = 2T(n/2) + n/log n
5. T(n) = 8T(n/2) + n³
6. T(n) = 16T(n/4) + n²
7. T(n) = T(n/2) + 2^n
---

## Next Step

- Go to [16_Recurrence_Relations.md](16_Recurrence_Relations.md) to continue with Recurrence Relations.
