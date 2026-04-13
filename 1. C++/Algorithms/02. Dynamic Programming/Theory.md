# Theory.md

## Introduction to Dynamic Programming Theory

Dynamic Programming (DP) is both a mathematical optimization method and a computer programming method. It refers to simplifying a complicated problem by breaking it down into simpler subproblems in a recursive manner.

## Bellman's Principle of Optimality

An optimal policy has the property that whatever the initial state and initial decision are, the remaining decisions must constitute an optimal policy with regard to the state resulting from the first decision.

In simpler terms: The optimal solution to the main problem contains within it the optimal solutions to subproblems.

## Properties Required for DP

### 1. Overlapping Subproblems

The same smaller subproblem is solved multiple times.

**Example:** In Fibonacci calculation, fib(2) is computed multiple times in naive recursion.

```
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2)
│   │   └── fib(1)
│   └── fib(2)
└── fib(3)
    ├── fib(2)
    └── fib(1)
```

Notice how fib(2) appears multiple times. Without overlapping subproblems, DP gives no benefit over divide and conquer.

### 2. Optimal Substructure

The optimal solution to the problem can be constructed from optimal solutions to its subproblems.

**Example (Works):** Shortest path from A to C via B = shortest path from A to B + shortest path from B to C.

**Example (Fails):** Longest path in a graph has no optimal substructure because paths may reuse vertices.

## DP Approaches Compared

| Aspect | Memoization (Top-Down) | Tabulation (Bottom-Up) |
|--------|------------------------|------------------------|
| Direction | Start from main problem | Start from base cases |
| Implementation | Recursive + cache | Iterative + table |
| Subproblems solved | Only needed ones | All possible ones |
| Memory | Cache + recursion stack | Table only |
| Risk | Stack overflow | None |
| Speed | Slightly slower | Faster |
| Ease of coding | More intuitive | Requires order knowledge |

## Mathematical Formulation

A DP problem can be expressed as:

```
dp[state] = best( dp[prev_state_1] + cost_1, 
                  dp[prev_state_2] + cost_2,
                  ... )
```

Where:
- `state` represents a subproblem
- `best` is either max, min, sum, or count
- `prev_state` are smaller/simpler states
- `cost` is the transition cost

## State Space

The set of all possible states is called the state space. Its size determines the time and memory complexity.

**Examples:**

| Problem | State Space Size |
|---------|------------------|
| Fibonacci(n) | O(n) |
| 0/1 Knapsack (n items, W capacity) | O(n × W) |
| LCS (strings of length m and n) | O(m × n) |
| TSP (n cities) | O(n × 2^n) |

## Transition Graph

DP can be viewed as finding the shortest/longest path in a DAG (Directed Acyclic Graph) where:

- Nodes = states
- Edges = transitions from smaller to larger states
- Edge weights = costs or values

## Types of DP by State Representation

### 1. One-Dimensional DP

States are represented by a single parameter (usually index or length).

**Example:** Fibonacci, Climbing Stairs, House Robber.

```
dp[i] depends on dp[i-1] and dp[i-2]
```

### 2. Two-Dimensional DP

States are represented by two parameters.

**Example:** Knapsack (i items, w weight), LCS (i, j indices).

```
dp[i][j] depends on dp[i-1][j], dp[i][j-1], dp[i-1][j-1]
```

### 3. Three-Dimensional DP

States are represented by three parameters.

**Example:** DP with two constraints, DP on two sequences with additional state.

### 4. DP with Bitmask

States are represented by a bitmask of size n (2^n states).

**Example:** TSP (mask of visited cities + current city).

### 5. Digit DP

States are represented by position, tight flag, and leading zero flag.

**Example:** Count numbers with digit sum = K.

## DP on Different Structures

### DP on Arrays

Most common. State is index i. Transition depends on previous indices.

### DP on Strings

State is usually positions i and j in two strings. Examples: LCS, Edit Distance.

### DP on Trees

State is node u. Transition from children to parent or vice versa.

### DP on Grids

State is cell (i, j). Transitions are up/down/left/right or diagonal.

### DP on Intervals

State is (l, r) representing a subarray or substring. Transition splits interval.

### DP on DAGs

DP can be applied directly to any DAG using topological order.

## Optimization Techniques for DP

### 1. Space Optimization

Use rolling arrays when dp[i] depends only on previous few states.

```
Instead of dp[n], use dp[2] and swap.
```

### 2. Convex Hull Trick (CHT)

Used when transition is of the form: dp[i] = min(m_j * x_i + c_j) for many j.

### 3. Divide and Conquer DP Optimization

Used when opt[i] ≤ opt[i+1] (monotonicity of decision points).

### 4. Knuth Optimization

Used when quadrangle inequality holds. Reduces O(n³) to O(n²).

### 5. Monotone Queue Optimization

Used when transition depends on sliding window minimum/maximum.

### 6. SOS DP (Sum Over Subsets)

Used for problems involving subset sums and convolutions.

## Common DP Patterns

### Pattern 1: Minimization/Maximization

Find the minimum or maximum value achievable.

**Example:** Min cost, max profit, shortest path.

### Pattern 2: Counting

Count the number of ways to achieve something.

**Example:** Number of ways to climb stairs, number of unique paths.

### Pattern 3: Probability

Find the probability of an event.

**Example:** Probability of winning a game, expected value.

### Pattern 4: Existence (True/False)

Determine if something is possible.

**Example:** Can we achieve exact sum, is there a valid partition.

### Pattern 5: Reconstruction

Not just the optimal value, but also the sequence that achieves it.

**Example:** Print the LCS, print the path in grid.

## DP vs Other Techniques

| Technique | When to Use |
|-----------|-------------|
| Recursion | Small input, no overlapping subproblems |
| Memoization DP | Overlapping subproblems, natural recursion |
| Tabulation DP | Overlapping subproblems, need efficiency |
| Greedy | Optimal substructure + greedy choice property |
| Divide and Conquer | No overlapping subproblems |
| Backtracking | Small constraints, need all solutions |

## Common Mistakes in DP Implementation

1. **Wrong base case** – Leads to incorrect answers for smallest inputs.

2. **Off-by-one errors** – Especially with 0-based vs 1-based indexing.

3. **Incorrect transition order** – Using dp[future] before it is computed.

4. **Forgetting to handle invalid states** – Using -inf or +inf appropriately.

5. **Not resetting memoization table** – Between multiple test cases.

6. **Integer overflow** – Using long long when needed.

7. **Memory limit exceeded** – Not using space optimization when possible.

8. **Time limit exceeded** – Not pruning unreachable states.

## How to Identify a DP Problem

Ask these questions:

1. Can the problem be broken into smaller subproblems?

2. Do the subproblems repeat? (Overlapping)

3. Can the optimal solution be built from optimal sub-solutions? (Optimal substructure)

4. Are the constraints reasonable? (n ≤ 10^5 → O(n) or O(n log n) DP; n ≤ 10^3 → O(n²) DP; n ≤ 20 → O(2^n) bitmask DP)

## Steps to Solve a DP Problem

1. **Define the state** – What parameters uniquely identify a subproblem?

2. **Formulate the transition** – How does a state depend on smaller states?

3. **Identify base case** – What is the smallest subproblem?

4. **Determine order** – In what order should states be computed?

5. **Implement** – Use memoization (recursive) or tabulation (iterative).

6. **Optimize** – Reduce space or time if needed.

7. **Extract answer** – The answer is usually dp[full_state] or best over states.
---

## Next Step

- Go to [README.md](README.md) to continue.
