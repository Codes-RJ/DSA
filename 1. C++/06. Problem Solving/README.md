# README.md

## Problem Solving in C++ - Complete Guide

### Overview

Problem solving is the core of programming and algorithm design. This section covers various categories of problems that appear frequently in coding interviews, competitive programming, and software development. Mastering these problem types helps develop logical thinking, pattern recognition, and efficient coding skills.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [01_Mathematical_Problems/README.md](01_Mathematical_Problems/README.md) | understand Mathematical Problems |
| 2. | [02_Bit_Manipulation/README.md](02_Bit_Manipulation/README.md) | understand Bit Manipulation Problems |
| 3. | [03_String_Problems/README.md](03_String_Problems/README.md) | understand String Problems |
| 4. | [04_Array_Problems/README.md](04_Array_Problems/README.md) | understand Array Problems |
| 5. | [05_Puzzle_Problems/README.md](05_Puzzle_Problems/README.md) | understand Puzzle Problems |

---

## 1. Mathematical Problems

This topic covers mathematical problem-solving techniques and number theory.

**Folder:** [01_Mathematical_Problems/](01_Mathematical_Problems/)

**What you will learn:**
- Number theory basics (primes, divisors, GCD, LCM)
- Modular arithmetic
- Combinatorics (factorials, permutations, combinations)
- Series and summations
- Prime number algorithms (Sieve of Eratosthenes)
- Fast exponentiation

**Key Concepts:**

| Concept | Description | Complexity |
|---------|-------------|------------|
| **Sieve of Eratosthenes** | Find all primes up to n | O(n log log n) |
| **GCD (Euclidean Algorithm)** | Greatest common divisor | O(log n) |
| **Fast Exponentiation** | Compute a^b efficiently | O(log b) |
| **Modular Arithmetic** | Operations modulo m | O(1) |

**Sub-topics:**
- Number Theory
- Prime Numbers and Sieve Algorithms
- Factorial and Combinatorics
- GCD and LCM (Euclidean Algorithm)
- Modular Arithmetic
- Series and Summations

---

## 2. Bit Manipulation

This topic covers problems that require working with individual bits.

**Folder:** [02_Bit_Manipulation/](02_Bit_Manipulation/)

**What you will learn:**
- Bitwise operators (&, |, ^, ~, <<, >>)
- Setting, clearing, toggling bits
- Checking if a bit is set
- Counting set bits (Brian Kernighan's algorithm)
- Bit masking techniques
- Common bit tricks

**Key Concepts:**

| Operation | Expression | Description |
|-----------|------------|-------------|
| **Set bit** | `x \| (1 << k)` | Set kth bit to 1 |
| **Clear bit** | `x & ~(1 << k)` | Set kth bit to 0 |
| **Toggle bit** | `x ^ (1 << k)` | Flip kth bit |
| **Check bit** | `(x >> k) & 1` | Get kth bit value |
| **Lowest set bit** | `x & -x` | Isolate lowest set bit |
| **Clear lowest set bit** | `x & (x - 1)` | Remove lowest set bit |

**Sub-topics:**
- Basic Bit Operations
- Common Bit Tricks
- Bit Masks and Subset Generation
- Binary Representation
- Bit Manipulation Problems

---

## 3. String Problems

This topic covers string manipulation and pattern matching.

**Folder:** [03_String_Problems/](03_String_Problems/)

**What you will learn:**
- String traversal and manipulation
- Pattern matching algorithms (KMP, Rabin-Karp)
- Palindrome checking
- Anagram detection
- String transformation problems
- Efficient string algorithms

**Key Concepts:**

| Algorithm | Purpose | Complexity |
|-----------|---------|------------|
| **KMP (Knuth-Morris-Pratt)** | Pattern matching | O(n + m) |
| **Rabin-Karp** | Pattern matching (rolling hash) | O(n + m) |
| **Two Pointer** | Palindrome, substring | O(n) |
| **Sliding Window** | Substring problems | O(n) |

**Sub-topics:**
- String Basics
- String Algorithms
- Pattern Matching
- String Transformation
- Advanced String Problems

---

## 4. Array Problems

This topic covers array manipulation and algorithm techniques.

**Folder:** [04_Array_Problems/](04_Array_Problems/)

**What you will learn:**
- Two-pointer technique
- Sliding window technique
- Array rotation and reversal
- Subarray problems (Kadane's algorithm)
- Sorting and searching in arrays
- Prefix sum technique

**Key Concepts:**

| Technique | Purpose | Complexity |
|-----------|---------|------------|
| **Two Pointer** | Pair sum, palindrome | O(n) |
| **Sliding Window** | Subarray sum, longest substring | O(n) |
| **Kadane's Algorithm** | Maximum subarray sum | O(n) |
| **Prefix Sum** | Range sum queries | O(1) per query |
| **Moore's Voting** | Majority element | O(n) |

**Sub-topics:**
- Array Basics
- Two Pointer Technique
- Sliding Window
- Array Rotation
- Subarray Problems

---

## 5. Puzzle Problems

This topic covers logic puzzles and brain teasers.

**Folder:** [05_Puzzle_Problems/](05_Puzzle_Problems/)

**What you will learn:**
- Logic puzzles and reasoning
- Pattern recognition
- Mathematical puzzles
- Array puzzles
- Recreational problem solving

**Key Concepts:**

| Puzzle Type | Description | Approach |
|-------------|-------------|----------|
| **Logic Puzzles** | Deductive reasoning | Process of elimination |
| **Pattern Puzzles** | Number/sequence patterns | Find repeating pattern |
| **Number Puzzles** | Mathematical relationships | Equation formulation |
| **Array Puzzles** | Data structure challenges | Optimization techniques |

**Sub-topics:**
- Logic Puzzles
- Pattern Puzzles
- Number Puzzles
- Array Puzzles
- Recreational Problems

---

### Problem-Solving Techniques

| Technique | Description | Best For |
|-----------|-------------|----------|
| **Brute Force** | Try all possibilities | Small input size |
| **Two Pointers** | Iterate from both ends | Sorted arrays, palindrome |
| **Sliding Window** | Maintain window of elements | Subarray/substring problems |
| **Divide and Conquer** | Split and merge | Sorting, search |
| **Greedy** | Local optimal choices | Optimization problems |
| **Dynamic Programming** | Store subproblem results | Overlapping subproblems |
| **Backtracking** | Explore possibilities | Constraint satisfaction |
| **Bit Manipulation** | Work with individual bits | Performance-critical operations |

---

### Complexity Guide

| Input Size | Acceptable Complexity |
|------------|----------------------|
| n ≤ 10 | O(n!) |
| n ≤ 20 | O(2^n) |
| n ≤ 100 | O(n³) |
| n ≤ 1000 | O(n²) |
| n ≤ 10^5 | O(n log n) |
| n ≤ 10^7 | O(n) |
| n > 10^7 | O(log n) or O(1) |

---

### Prerequisites

Before starting this section, you should have completed:

- [01. Basics](../01.%20Basics/README.md) - C++ fundamentals
- [02. Basic Problems](../02.%20Basic%20Problems/README.md) - Basic problem solving
- [04. Data Structures](../04.%20Data%20Structures/README.md) - Data structures

---

### Learning Path

```
Level 1: Mathematical Problems
├── Number Theory
├── Modular Arithmetic
└── Combinatorics

Level 2: Bit Manipulation
├── Bitwise Operators
├── Bit Tricks
└── Bit Masks

Level 3: String Problems
├── String Manipulation
├── Pattern Matching
└── String Algorithms

Level 4: Array Problems
├── Two Pointers
├── Sliding Window
├── Prefix Sum
└── Kadane's Algorithm

Level 5: Puzzle Problems
├── Logic Puzzles
├── Pattern Recognition
└── Optimization Puzzles
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Integer overflow | Use long long, check bounds |
| Off-by-one errors | Carefully test edge cases |
| Ignoring constraints | Choose appropriate algorithm |
| Premature optimization | Write correct code first |
| Not handling empty input | Always check edge cases |

---

### Practice Questions

After completing this section, you should be able to:

1. Check if a number is prime (optimized)
2. Find GCD and LCM of two numbers
3. Count set bits in an integer
4. Find the single number in an array (XOR trick)
5. Check if two strings are anagrams
6. Find maximum subarray sum (Kadane's algorithm)
7. Solve two-sum problem with O(n) time
8. Find missing number in 1..n array
9. Reverse a string in-place
10. Find the longest common prefix

---

### Next Steps

- Go to [01_Mathematical_Problems/README.md](01_Mathematical_Problems/README.md) to understand Mathematical Problems.