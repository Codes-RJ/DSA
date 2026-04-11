# README.md

## Greedy Algorithms - Complete Guide

### Overview

Greedy algorithms make the locally optimal choice at each step with the hope of finding the global optimum. Unlike dynamic programming, greedy algorithms do not consider the entire problem space but make decisions based on the current best option.

### Key Properties

For a greedy algorithm to be correct, the problem must have:

| Property | Description |
|----------|-------------|
| Greedy Choice Property | A locally optimal choice leads to a globally optimal solution |
| Optimal Substructure | The optimal solution to the problem contains optimal solutions to subproblems |

### When to Use Greedy

Greedy algorithms are suitable when:

- Making the best choice now does not hurt future choices
- The problem has optimal substructure
- You need a fast solution (greedy is usually faster than DP)
- The problem is simple enough that greedy is optimal

### Greedy vs Dynamic Programming

| Aspect | Greedy | Dynamic Programming |
|--------|--------|---------------------|
| Approach | Makes one decision at a time | Considers all possibilities |
| Complexity | Usually O(n log n) or O(n) | Usually O(n²) or higher |
| Optimality | Not always optimal | Always optimal |
| Implementation | Simpler | More complex |
| Use case | Problems with greedy choice property | Problems with overlapping subproblems |

### Complete Index

| # | Topic | File |
|---|-------|------|
| 1 | Introduction to Greedy | `01_Introduction_to_Greedy.md` |
| 2 | Activity Selection | `02_Activity_Selection.md` |
| 3 | Job Sequencing with Deadlines | `03_Job_Sequencing.md` |
| 4 | Fractional Knapsack | `04_Fractional_Knapsack.md` |
| 5 | Huffman Coding | `05_Huffman_Coding.md` |
| 6 | Coin Change (Greedy) | `06_Coin_Change_Greedy.md` |
| 7 | Minimum Number of Platforms | `07_Minimum_Number_of_Platforms.md` |
| 8 | Interval Scheduling | `08_Interval_Scheduling.md` |
| 9 | Interval Partitioning | `09_Interval_Partitioning.md` |
| 10 | Dijkstra's Algorithm | `10_Dijkstra_Algorithm.md` |
| 11 | Prim's Algorithm | `11_Prims_Algorithm.md` |
| 12 | Kruskal's Algorithm | `12_Kruskals_Algorithm.md` |
| 13 | Minimum Cost to Connect Sticks | `13_Minimum_Cost_to_Connect_Sticks.md` |
| 14 | Gas Station Problem | `14_Gas_Station_Problem.md` |
| 15 | Lexicographically Smallest Sequence | `15_Lexicographically_Smallest_Sequence.md` |
| 16 | Maximum Sum after K Negations | `16_Maximum_Sum_after_K_Negations.md` |
| 17 | Candy Distribution | `17_Candy_Distribution.md` |
| 18 | Jump Game | `18_Jump_Game.md` |
| 19 | Assign Cookies | `19_Assign_Cookies.md` |
| 20 | Reconstruct String from Adjacent Pairs | `20_Reconstruct_String_from_Adjacent_Pairs.md` |
| 21 | Proof of Optimality | `21_Proof_of_Optimality.md` |

### Classification by Problem Type

```
Greedy Algorithm Categories:

├── Interval Problems
│   ├── Activity Selection
│   ├── Interval Scheduling
│   ├── Interval Partitioning
│   └── Minimum Platforms
│
├── Scheduling Problems
│   ├── Job Sequencing with Deadlines
│   ├── Task Scheduling
│   └── Meeting Rooms
│
├── Graph Problems
│   ├── Dijkstra (Shortest Path)
│   ├── Prim (MST)
│   ├── Kruskal (MST)
│   └── Minimum Cost to Connect
│
├── Compression Problems
│   ├── Huffman Coding
│   └── Optimal Merge Pattern
│
├── Knapsack Variants
│   ├── Fractional Knapsack
│   └── Coin Change (for specific denominations)
│
└── Array Problems
    ├── Jump Game
    ├── Gas Station
    ├── Candy Distribution
    └── Assign Cookies
```

### Time Complexity Comparison

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Activity Selection | O(n log n) | O(1) |
| Job Sequencing | O(n log n) | O(n) |
| Fractional Knapsack | O(n log n) | O(1) |
| Huffman Coding | O(n log n) | O(n) |
| Dijkstra | O((V+E) log V) | O(V) |
| Prim | O((V+E) log V) | O(V) |
| Kruskal | O(E log E) | O(V) |
| Minimum Platforms | O(n log n) | O(n) |
| Jump Game | O(n) | O(1) |

### Common Greedy Strategies

| Problem Type | Greedy Strategy |
|--------------|-----------------|
| Activity Selection | Choose activity with earliest finish time |
| Job Sequencing | Sort by profit descending, schedule at latest available slot |
| Fractional Knapsack | Take items with highest value/weight ratio |
| Huffman Coding | Merge smallest frequency nodes first |
| Dijkstra | Pick vertex with smallest distance |
| Prim | Pick edge with smallest weight from tree |
| Kruskal | Pick smallest edge that doesn't form cycle |
| Minimum Platforms | Sort arrivals and departures, use two pointers |

### When Greedy Fails

Greedy algorithms do not work for:

- 0/1 Knapsack (fractional works, 0/1 requires DP)
- Coin Change with arbitrary denominations
- Longest Path in graph
- Traveling Salesman Problem
- Graph Coloring

### Learning Path

```
Level 1: Basic Greedy
├── Activity Selection
├── Fractional Knapsack
├── Minimum Number of Platforms
└── Assign Cookies

Level 2: Scheduling
├── Job Sequencing with Deadlines
├── Interval Scheduling
├── Interval Partitioning
└── Meeting Rooms

Level 3: Graph Greedy
├── Dijkstra's Algorithm
├── Prim's Algorithm
├── Kruskal's Algorithm
└── Minimum Cost to Connect Sticks

Level 4: Advanced Greedy
├── Huffman Coding
├── Gas Station
├── Jump Game
├── Candy Distribution
└── Lexicographically Smallest Sequence
```