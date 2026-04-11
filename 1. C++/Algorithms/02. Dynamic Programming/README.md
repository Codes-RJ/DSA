# Dynamic Programming (DP) - Complete Guide

## Overview

Dynamic Programming is an optimization technique used to solve complex problems by breaking them down into simpler subproblems. It stores the results of subproblems to avoid redundant computations. This is often called "divide and conquer + memoization".

DP is used when a problem has two key properties:

1. **Overlapping Subproblems** – The same subproblem appears multiple times.
2. **Optimal Substructure** – The optimal solution of the main problem can be constructed from optimal solutions of its subproblems.

## Why Learn Dynamic Programming?

DP is essential for:

- Competitive programming
- Technical interviews (FAANG and other companies)
- Optimizing recursive solutions
- Solving problems like shortest paths, sequence alignment, resource allocation, and game theory

## Complete Index

| # | Topic | File |
|---|-------|------|
| 1 | Introduction to DP | `01_Introduction_to_DP.md` |
| 2 | Memoization (Top-Down) | `02_Memoization.md` |
| 3 | Tabulation (Bottom-Up) | `03_Tabulation.md` |
| 4 | 1D DP | `04_1D_DP.md` |
| 5 | 2D DP | `05_2D_DP.md` |
| 6 | State Transition | `06_State_Transition.md` |
| 7 | DP on Subsequences | `07_DP_on_Subsequences.md` |
| 8 | DP on Strings | `08_DP_on_Strings.md` |
| 9 | DP on Trees | `09_DP_on_Trees.md` |
| 10 | DP on Grids | `10_DP_on_Grids.md` |
| 11 | Knapsack Problems | `11_Knapsack_Problems.md` |
| 12 | Unbounded Knapsack | `12_Unbounded_Knapsack.md` |
| 13 | Longest Common Subsequence | `13_Longest_Common_Subsequence.md` |
| 14 | Longest Increasing Subsequence | `14_Longest_Increasing_Subsequence.md` |
| 15 | Edit Distance | `15_Edit_Distance.md` |
| 16 | Matrix Chain Multiplication | `16_Matrix_Chain_Multiplication.md` |
| 17 | DP with Bitmasks | `17_DP_with_Bitmasks.md` |
| 18 | Digit DP | `18_Digit_DP.md` |
| 19 | DP with State Compression | `19_DP_with_State_Compression.md` |
| 20 | DP on Intervals | `20_DP_on_Intervals.md` |
| 21 | Counting DP | `21_Counting_DP.md` |
| 22 | Probability DP | `22_Probability_DP.md` |
| 23 | DP on DAGs | `23_DP_on_DAGs.md` |
| 24 | Optimization Techniques | `24_Optimization_Techniques.md` |
| 25 | Problems | `Problems.md` |

## DP Classification by Problem Type

```
DP Categories:

├── Linear DP
│   ├── 1D DP (Fibonacci, Climbing Stairs)
│   ├── 2D DP (Longest Common Subsequence)
│   └── Kadane's Algorithm (Maximum Subarray)
│
├── Knapsack Family
│   ├── 0/1 Knapsack
│   ├── Unbounded Knapsack
│   ├── Bounded Knapsack
│   └── Fractional Knapsack (Greedy)
│
├── Sequence DP
│   ├── Longest Increasing Subsequence
│   ├── Longest Common Subsequence
│   ├── Edit Distance
│   └── Shortest Common Supersequence
│
├── Interval DP
│   ├── Matrix Chain Multiplication
│   ├── Burst Balloons
│   └── Stone Game
│
├── Tree DP
│   ├── Tree Diameter
│   ├── Tree Independent Set
│   └── Tree Coloring
│
├── Grid DP
│   ├── Unique Paths
│   ├── Minimum Path Sum
│   └── Dungeon Game
│
├── DP on Strings
│   ├── Palindrome Partitioning
│   ├── Regular Expression Matching
│   └── Wildcard Matching
│
├── DP on Bitmasks
│   ├── Traveling Salesman Problem (TSP)
│   ├── Assigning Tasks
│   └── Set Cover
│
├── Digit DP
│   ├── Count numbers with digit sum
│   ├── Count numbers without consecutive 1s
│   └── Lucky numbers
│
└── DP with Optimization
    ├── Convex Hull Trick
    ├── Divide and Conquer DP
    ├── Knuth Optimization
    └── Monotone Queue Optimization
```

## Time Complexity Comparison

| Technique | Approach | Time | Space | Use Case |
|-----------|----------|------|-------|----------|
| Naive Recursion | Top-down without memo | Exponential | O(depth) | Never use |
| Memoization | Top-down with cache | O(states × transition) | O(states) + stack | When recursion is natural |
| Tabulation | Bottom-up iterative | O(states × transition) | O(states) | When order is known |
| Space Optimized DP | Rolling arrays | Same as tabulation | O(1) or O(n) | When only previous states needed |

## DP State Definition

A **state** is a set of parameters that uniquely identifies a subproblem.

Examples:

| Problem | State Definition |
|---------|------------------|
| Fibonacci | dp[i] = i-th Fibonacci number |
| 0/1 Knapsack | dp[i][w] = max value using first i items with capacity w |
| LCS | dp[i][j] = LCS length of prefix A[0..i-1] and B[0..j-1] |
| Edit Distance | dp[i][j] = min edits to convert A[0..i-1] to B[0..j-1] |

## State Transition Equation

This is the formula to compute dp[state] from smaller states.

Examples:

| Problem | Transition |
|---------|------------|
| Fibonacci | dp[i] = dp[i-1] + dp[i-2] |
| 0/1 Knapsack | dp[i][w] = max(dp[i-1][w], dp[i-1][w - wt[i]] + val[i]) |
| LCS | dp[i][j] = dp[i-1][j-1] + 1 if A[i-1]==B[j-1] else max(dp[i-1][j], dp[i][j-1]) |

## Base Case

The smallest subproblem(s) that can be solved directly.

Examples:

| Problem | Base Case |
|---------|-----------|
| Fibonacci | dp[0] = 0, dp[1] = 1 |
| 0/1 Knapsack | dp[0][w] = 0 for all w |
| LCS | dp[0][j] = 0, dp[i][0] = 0 |

## Learning Path

```
Level 1: Beginner DP

  ├── Fibonacci (memoization + tabulation)
  ├── Climbing Stairs
  ├── Min Cost Climbing Stairs
  ├── House Robber
  └── Maximum Subarray (Kadane's Algorithm)

Level 2: Intermediate DP

  ├── 0/1 Knapsack
  ├── Unbounded Knapsack
  ├── Coin Change
  ├── Longest Common Subsequence (LCS)
  ├── Longest Increasing Subsequence (LIS)
  ├── Edit Distance
  ├── Unique Paths
  └── Minimum Path Sum

Level 3: Advanced DP

  ├── Matrix Chain Multiplication
  ├── Palindrome Partitioning
  ├── DP on Trees
  ├── DP with Bitmasks (TSP)
  ├── Digit DP
  ├── Interval DP
  └── DP with Optimizations

Level 4: Expert DP

  ├── Convex Hull Trick
  ├── Divide and Conquer DP Optimization
  ├── Knuth Optimization
  ├── Aliens Trick (Lagrange Optimization)
  └── SOS DP (Sum Over Subsets)
```

## Common DP Mistakes

- Forgetting base case
- Incorrect state definition
- Wrong transition order in tabulation
- Stack overflow in recursion (use iterative when needed)
- Not handling out-of-bounds indices
- Using too much memory (optimize with rolling arrays)
- Trying to use DP when a greedy solution works

## When Not to Use DP

- If the problem has no overlapping subproblems (use divide and conquer)
- If a greedy algorithm gives the optimal solution (simpler and faster)
- If constraints are very small (brute force is acceptable)
- If the state space is huge and no optimization is possible