# 16_Recurrence_Relations.md

## Recurrence Relations

### Definition

A recurrence relation is an equation that defines a sequence recursively, where each term is defined as a function of previous terms. In algorithm analysis, recurrence relations describe the time complexity of recursive algorithms.

### Basic Form

```
T(n) = a * T(n/b) + f(n)
```

Where:
- T(n) is the time for input size n
- a is the number of subproblems
- n/b is the size of each subproblem
- f(n) is the cost of dividing and combining

### Common Recurrence Patterns

| Pattern | Recurrence | Solution | Example Algorithm |
|---------|------------|----------|-------------------|
| Linear | T(n) = T(n-1) + c | Θ(n) | Simple recursion |
| Linear with extra work | T(n) = T(n-1) + n | Θ(n²) | Selection sort |
| Divide and conquer | T(n) = 2T(n/2) + c | Θ(n) | Tree traversal |
| Divide and conquer with linear work | T(n) = 2T(n/2) + n | Θ(n log n) | Merge sort |
| Binary search | T(n) = T(n/2) + c | Θ(log n) | Binary search |
| Unbalanced | T(n) = T(n-1) + T(1) + n | Θ(n²) | Quick sort (worst) |
| Fibonacci | T(n) = T(n-1) + T(n-2) | Θ(φⁿ) | Naive Fibonacci |

### Methods to Solve Recurrences

#### 1. Substitution Method (Induction)

Guess the solution and prove by mathematical induction.

**Example:** T(n) = 2T(n/2) + n, guess T(n) = O(n log n)

```
Assume T(k) ≤ c*k log k for k < n

T(n) = 2T(n/2) + n
     ≤ 2(c*(n/2)*log(n/2)) + n
     = c*n*(log n - 1) + n
     = c*n log n - c*n + n
     = c*n log n - n(c - 1)
     ≤ c*n log n  (for c ≥ 1)

Therefore, T(n) = O(n log n)
```

#### 2. Recursion Tree Method

Draw the recursion tree and sum the work at each level.

**Example:** T(n) = 3T(n/4) + n²

```
Level 0: n²
Level 1: 3*(n/4)² = 3n²/16
Level 2: 9*(n/16)² = 9n²/256
...

Total = n² * (1 + 3/16 + 9/256 + ...)
      = n² * (1 / (1 - 3/16))
      = n² * (16/13)
      = Θ(n²)
```

#### 3. Master Theorem

Covered in previous file (15_Master_Theorem.md).

#### 4. Characteristic Equation (For Linear Recurrences)

For recurrences of the form: T(n) = c₁T(n-1) + c₂T(n-2) + ... + cₖT(n-k)

**Example:** Fibonacci: F(n) = F(n-1) + F(n-2)

Characteristic equation: r² = r + 1 → r² - r - 1 = 0
Roots: r = (1 ± √5)/2
Solution: F(n) = A*φⁿ + B*(-φ)⁻ⁿ where φ = (1+√5)/2

### Solving Recurrences by Type

#### Type 1: T(n) = T(n-1) + f(n)

```
T(n) = T(0) + sum_{i=1 to n} f(i)
```

**Example:** T(n) = T(n-1) + n

```
T(n) = T(0) + 1 + 2 + ... + n = Θ(n²)
```

#### Type 2: T(n) = aT(n-1) + f(n)

```
T(n) = a^n * T(0) + sum_{i=1 to n} a^(n-i) * f(i)
```

**Example:** T(n) = 2T(n-1) + 1

```
T(n) = 2^n * T(0) + (2^n - 1) = Θ(2^n)
```

#### Type 3: T(n) = aT(n/b) + f(n) (Divide and Conquer)

Use Master Theorem or recursion tree.

### Common Recurrence Solutions

| Recurrence | Solution |
|------------|----------|
| T(n) = T(n-1) + 1 | Θ(n) |
| T(n) = T(n-1) + n | Θ(n²) |
| T(n) = T(n-1) + log n | Θ(n log n) |
| T(n) = 2T(n-1) + 1 | Θ(2ⁿ) |
| T(n) = T(n/2) + 1 | Θ(log n) |
| T(n) = T(n/2) + n | Θ(n) |
| T(n) = 2T(n/2) + 1 | Θ(n) |
| T(n) = 2T(n/2) + n | Θ(n log n) |
| T(n) = 2T(n/2) + n² | Θ(n²) |
| T(n) = 4T(n/2) + n | Θ(n²) |
| T(n) = 4T(n/2) + n² | Θ(n² log n) |
| T(n) = 4T(n/2) + n³ | Θ(n³) |
| T(n) = T(n-1) + T(n-2) | Θ(φⁿ) |

### Visualizing Recursion Trees

```
Merge Sort: T(n) = 2T(n/2) + n

Level 0: n
Level 1: n/2 + n/2 = n
Level 2: n/4 + n/4 + n/4 + n/4 = n
...
Level log n: 1 + 1 + ... (n times) = n

Total work = n * (log n + 1) = Θ(n log n)
```

```
Fibonacci: T(n) = T(n-1) + T(n-2) + 1

Level 0: 1
Level 1: 1 + 1 = 2
Level 2: 1+1 + 1+1 = 4
...
Level n: 2^n

Total work = Θ(2ⁿ)
```

### Practice Problems

Solve the following recurrences:

1. T(n) = 3T(n/2) + n²
2. T(n) = 2T(n/3) + n
3. T(n) = T(n/2) + n²
4. T(n) = 3T(n/4) + n log n
5. T(n) = 2T(n/2) + n log n
6. T(n) = T(n-2) + 1
7. T(n) = T(√n) + 1
8. T(n) = 2T(√n) + log n
9. T(n) = T(n/3) + T(2n/3) + n
10. T(n) = 2T(n/4) + √n

### Answers

1. Case 3: Θ(n²)
2. Case 1: Θ(n^(log₂3))
3. Case 3: Θ(n²)
4. Case 1: Θ(n^(log₄3))
5. Case 2: Θ(n log² n)
6. Θ(n)
7. Θ(log log n)
8. Θ(log n)
9. Θ(n log n)
10. Case 2: Θ(√n log n)