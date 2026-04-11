# README.md

## Divide and Conquer - Complete Guide

### Overview

Divide and Conquer is an algorithmic paradigm that solves a problem by breaking it into smaller subproblems, solving each subproblem recursively, and combining the results to form the solution to the original problem.

### Three Steps of Divide and Conquer

| Step | Description |
|------|-------------|
| Divide | Break the problem into smaller subproblems of the same type |
| Conquer | Solve the subproblems recursively (base case when small enough) |
| Combine | Merge the solutions of subproblems to solve the original problem |

### Key Properties

- Subproblems must be independent (unlike DP where they overlap)
- Each subproblem must be a smaller instance of the same problem
- Combining step must be efficient

### When to Use Divide and Conquer

Divide and conquer is suitable when:

- Problem can be broken into independent subproblems
- Subproblems are smaller instances of the same problem
- Solutions can be combined efficiently
- Problem has a natural recursive structure

### Divide and Conquer vs Other Paradigms

| Aspect | Divide and Conquer | Dynamic Programming | Greedy |
|--------|--------------------|---------------------|--------|
| Subproblems | Independent | Overlapping | Single path |
| Solution | Combine subproblem solutions | Use previous subproblem results | One decision at a time |
| Typical complexity | O(n log n) | O(n²) or higher | O(n log n) |
| Examples | Merge Sort, Binary Search | Knapsack, LCS | Activity Selection |

### Complete Index

| # | Topic | File |
|---|-------|------|
| 1 | Introduction to Divide and Conquer | `01_Introduction_to_Divide_and_Conquer.md` |
| 2 | Merge Sort | `02_Merge_Sort.md` |
| 3 | Quick Sort | `03_Quick_Sort.md` |
| 4 | Binary Search | `04_Binary_Search.md` |
| 5 | Power Exponentiation | `05_Power_Exponentiation.md` |
| 6 | Strassen's Matrix Multiplication | `06_Strassens_Matrix_Multiplication.md` |
| 7 | Closest Pair of Points | `07_Closest_Pair_of_Points.md` |
| 8 | Maximum Subarray Sum | `08_Maximum_Subarray_Sum.md` |
| 9 | Karatsuba Algorithm | `09_Karatsuba_Algorithm.md` |
| 10 | Median of Two Sorted Arrays | `10_Median_of_Two_Sorted_Arrays.md` |
| 11 | Inversion Count | `11_Inversion_Count.md` |
| 12 | Majority Element | `12_Majority_Element.md` |
| 13 | Quick Select (Kth Smallest) | `13_Quick_Select.md` |
| 14 | Convex Hull | `14_Convex_Hull.md` |
| 15 | Master Theorem | `15_Master_Theorem.md` |
| 16 | Recurrence Relations | `16_Recurrence_Relations.md` |
| 17 | When to Use Divide and Conquer | `17_When_to_Use_Divide_and_Conquer.md` |
| 18 | Problems | `Problems.md` |

### Classification by Problem Type

```
Divide and Conquer Categories:

├── Sorting
│   ├── Merge Sort
│   ├── Quick Sort
│   └── Quick Select
│
├── Searching
│   ├── Binary Search
│   └── Exponential Search
│
├── Mathematical
│   ├── Power Exponentiation
│   ├── Karatsuba Multiplication
│   └── Strassen's Matrix Multiplication
│
├── Geometric
│   ├── Closest Pair of Points
│   └── Convex Hull
│
├── Array Problems
│   ├── Maximum Subarray Sum
│   ├── Inversion Count
│   ├── Majority Element
│   └── Median of Two Arrays
│
└── Complexity Analysis
    ├── Master Theorem
    └── Recurrence Relations
```

### Time Complexity Comparison

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Merge Sort | O(n log n) | O(n) |
| Quick Sort (average) | O(n log n) | O(log n) |
| Quick Sort (worst) | O(n²) | O(log n) |
| Binary Search | O(log n) | O(1) |
| Power Exponentiation | O(log n) | O(1) |
| Strassen's Matrix | O(n^2.81) | O(n²) |
| Closest Pair | O(n log n) | O(n) |
| Maximum Subarray | O(n log n) | O(log n) |
| Inversion Count | O(n log n) | O(n) |
| Majority Element | O(n log n) | O(log n) |
| Quick Select | O(n) average | O(log n) |
| Karatsuba | O(n^1.585) | O(n) |

### Learning Path

```
Level 1: Basic Divide and Conquer
├── Binary Search
├── Power Exponentiation
├── Merge Sort
└── Quick Sort

Level 2: Array Problems
├── Maximum Subarray Sum
├── Inversion Count
├── Majority Element
└── Quick Select

Level 3: Advanced Algorithms
├── Closest Pair of Points
├── Median of Two Sorted Arrays
├── Karatsuba Algorithm
└── Strassen's Matrix Multiplication

Level 4: Theory
├── Convex Hull
├── Master Theorem
└── Recurrence Relations
```
