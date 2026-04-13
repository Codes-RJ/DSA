# Theory.md

## Divide and Conquer Theory

### Definition

Divide and Conquer is a recursive algorithmic paradigm that solves a problem by:
1. **Dividing** the problem into smaller subproblems of the same type
2. **Conquering** the subproblems by solving them recursively
3. **Combining** the subproblem solutions to solve the original problem

### Mathematical Formulation

For a problem of size n, divide and conquer follows:

```
T(n) = a * T(n/b) + f(n)
```

Where:
- a = number of subproblems
- n/b = size of each subproblem
- f(n) = cost of dividing and combining

### The Three Steps in Detail

#### Step 1: Divide

Split the input into smaller parts. The division should be such that:
- Subproblems are smaller instances of the same problem
- Subproblems are independent (no overlap)
- Division is efficient (usually O(n) or O(1))

#### Step 2: Conquer

Solve each subproblem recursively:
- Base case: when problem size is small enough to solve directly
- Recursive case: further divide and conquer

#### Step 3: Combine

Merge the solutions of subproblems to get the final solution:
- Combine must be efficient
- Combine must correctly reconstruct the original solution

### Example: Merge Sort

```
Merge Sort (array of size n):

Divide: Split array into two halves of size n/2

Conquer: Recursively sort each half

Combine: Merge the two sorted halves (O(n))
```

### Example: Binary Search

```
Binary Search (sorted array of size n):

Divide: Compare with middle element
    If equal: found
    If smaller: search left half (size n/2)
    If larger: search right half (size n/2)

Conquer: Recursively search the chosen half

Combine: No combine step needed
```

### Visualization of Divide and Conquer

```
Original Problem (size n)
        │
        ├── Divide
        │
        ▼
┌───────────────┐
│  Subproblem 1 │    ┌───────────────┐
│   (size n/b)  │    │  Subproblem 2 │
└───────┬───────┘    │   (size n/b)  │
        │            └───────┬───────┘
        ▼                    ▼
   (recursively)        (recursively)
        │                    │
        └──────────┬──────────┘
                   │
                   ▼
              Combine
                   │
                   ▼
            Solution (size n)
```

### Base Cases

The base case is when the problem is small enough to solve directly without further recursion.

Common base cases:
- n = 0: empty input
- n = 1: single element
- n = 2: two elements (simple comparison)

### Recurrence Relations

Divide and conquer algorithms are analyzed using recurrence relations:

| Algorithm | Recurrence | Solution |
|-----------|------------|----------|
| Binary Search | T(n) = T(n/2) + O(1) | O(log n) |
| Merge Sort | T(n) = 2T(n/2) + O(n) | O(n log n) |
| Quick Sort (avg) | T(n) = 2T(n/2) + O(n) | O(n log n) |
| Quick Sort (worst) | T(n) = T(n-1) + O(n) | O(n²) |
| Strassen's | T(n) = 7T(n/2) + O(n²) | O(n^log2(7)) ≈ O(n^2.81) |
| Karatsuba | T(n) = 3T(n/2) + O(n) | O(n^log2(3)) ≈ O(n^1.585) |

### Master Theorem

For recurrences of the form T(n) = aT(n/b) + f(n):

| Case | Condition | Solution |
|------|-----------|----------|
| Case 1 | f(n) = O(n^(log_b(a) - ε)) | T(n) = Θ(n^(log_b(a))) |
| Case 2 | f(n) = Θ(n^(log_b(a)) * log^k(n)) | T(n) = Θ(n^(log_b(a)) * log^(k+1)(n)) |
| Case 3 | f(n) = Ω(n^(log_b(a) + ε)) and af(n/b) ≤ cf(n) | T(n) = Θ(f(n)) |

### Advantages of Divide and Conquer

| Advantage | Description |
|-----------|-------------|
| Parallelizability | Subproblems can be solved in parallel |
| Cache efficiency | Works with memory hierarchies |
| Clarity | Recursive structure is often clear |
| Optimality | Many optimal algorithms are divide and conquer |

### Disadvantages

| Disadvantage | Description |
|--------------|-------------|
| Recursion overhead | Function call cost |
| Stack memory | May cause stack overflow for deep recursion |
| Implementation complexity | Harder than iterative for some problems |
| Not suitable for small n | Overhead outweighs benefits |

### When Divide and Conquer is Not Suitable

- Subproblems are not independent (use DP instead)
- Combining step is too expensive
- Problem size is small (use brute force)
- Recursion depth is too large (use iteration)

### Divide and Conquer vs Recursion

| Aspect | Divide and Conquer | General Recursion |
|--------|--------------------|-------------------|
| Structure | Divide, conquer, combine | Self-call only |
| Subproblems | Multiple smaller instances | Usually one smaller instance |
| Combine step | Required | May not exist |
| Examples | Merge Sort, Quick Sort | Factorial, Fibonacci |

### Common Divide and Conquer Patterns

#### Pattern 1: Split in Half

Divide array into two halves. Used in Merge Sort, Binary Search.

```
mid = (left + right) / 2
solve(left, mid)
solve(mid+1, right)
combine(left, mid, right)
```

#### Pattern 2: Partition Around Pivot

Choose pivot and partition. Used in Quick Sort, Quick Select.

```
pivotIndex = partition(arr, left, right)
solve(left, pivotIndex-1)
solve(pivotIndex+1, right)
```

#### Pattern 3: Divide into Subproblems with Overlap

Subproblems may have overlap. Used in Strassen's, Karatsuba.

```
Divide into parts with overlap
Solve subproblems
Combine with arithmetic
```

### Real-World Applications

| Domain | Application |
|--------|-------------|
| Sorting | Merge Sort, Quick Sort |
| Searching | Binary Search |
| Computational Geometry | Closest Pair, Convex Hull |
| Numerical Analysis | Fast Fourier Transform |
| Cryptography | Large number multiplication |
| Graphics | Rendering algorithms |

### Practice Problems for Theory

1. Write recurrence for binary search and solve using Master Theorem
2. Write recurrence for merge sort and solve
3. Write recurrence for quick sort (best, worst, average)
4. Compare divide and conquer vs dynamic programming for Fibonacci
5. Identify which problems are suitable for divide and conquer
---

## Next Step

- Go to [README.md](README.md) to continue.
