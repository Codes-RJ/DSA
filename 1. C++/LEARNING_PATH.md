# C++ and DSA Learning Path

This is the canonical order for studying the material in `1. C++`. Directory numbers are retained for link stability, but learners should follow the stages below rather than reading folders alphabetically.

> **Core standard:** C++17
>
> **Optional extensions:** C++20 and C++23 lessons are explicitly labeled
>
> **Rule:** Learn the concept, implement it, test it, analyze it, and only then move to the next stage.

## How to Use the Path

For each stage:

1. Read the listed concept lessons in order.
2. Type the important examples instead of copying them blindly.
3. Complete the exercises before opening solutions.
4. State the time and space complexity of every algorithm.
5. Test empty, singleton, duplicate, boundary, and large inputs.
6. Revisit the stage if you cannot explain its invariants without the notes.

## Stage 0: Toolchain and Study Setup

**Goal:** Compile and debug a small C++17 program independently.

Learn:

- source files, headers, translation units, compilation, and linking;
- selecting the C++ language standard;
- compiler warnings;
- debugger and sanitizer basics;
- the repository's example and verification conventions.

Start with [`TOOLCHAIN.md`](TOOLCHAIN.md), then read the repository's [`STANDARDS.md`](STANDARDS.md) and build the canonical examples in [`examples/`](examples/README.md).

**Exit criteria:** You can build a two-file program, interpret a compiler diagnostic, and run a debugger or sanitizer.

## Stage 1: C++ Language Foundations

**Start:** [`01. Basics/README.md`](01.%20Basics/README.md)

Study in this order:

1. [`01_Variables_Keywords_and_Operators.md`](01.%20Basics/01_Variables_Keywords_and_Operators.md)
2. [`02_Conditional_Statements.md`](01.%20Basics/02_Conditional_Statements.md)
3. [`03_Loops_and_Iteration.md`](01.%20Basics/03_Loops_and_Iteration.md)
4. [`04_Functions_and_Scope.md`](01.%20Basics/04_Functions_and_Scope.md)
5. [`05_Arrays_and_Strings.md`](01.%20Basics/05_Arrays_and_Strings.md)
6. [`06_Pointers_and_Memory_Management.md`](01.%20Basics/06_Pointers_and_Memory_Management.md)
7. [`07_Error_Handling.md`](01.%20Basics/07_Error_Handling.md)

Required concepts before continuing:

- automatic versus dynamic storage;
- references, pointers, `const`, and object lifetime;
- pass by value versus reference;
- array bounds and string ownership;
- undefined behavior at a beginner level;
- RAII as the default resource-management model.

**Exit criteria:** You can implement small functions without global state, explain every variable's lifetime, and avoid manual allocation unless an exercise explicitly requires it.

## Stage 2: Essential Standard Library

**Start:** [`00. Headers and Libraries/README.md`](00.%20Headers%20and%20Libraries/README.md)

Do not read every header reference linearly. Begin with this core:

1. `iostream` and `string`
2. `vector` and `array`
3. `algorithm` and iterators
4. `pair` and `tuple`
5. `stack`, `queue`, and `priority_queue`
6. `set`, `map`, `unordered_set`, and `unordered_map`
7. `memory` and smart pointers
8. `numeric`, `limits`, `random`, and `chrono`

Use the remaining header pages as references when later topics need them.

Required distinctions:

- standard guarantees versus common implementation details;
- sequence versus ordered associative versus unordered associative containers;
- iterator and reference invalidation;
- total storage versus auxiliary operation space;
- ownership versus observation.

**Exit criteria:** Given a problem, you can choose an appropriate container and justify its operation complexities and invalidation behavior.

## Stage 3: Complexity and Problem-Solving Foundations

**Start:** [`02. Basic Problems/README.md`](02.%20Basic%20Problems/README.md)

Core topics:

1. Asymptotic notation and cost models
2. Loop and recursion analysis
3. Linear and binary search
4. Insertion, merge, quick, and heap sort
5. Correctness invariants
6. Testing and counterexamples

Recommended search lessons:

- linear search;
- binary search;
- exponential search as an extension;
- hash-based lookup and tree lookup after their data structures are learned.

Recommended sorting lessons:

- insertion sort for incremental invariants;
- merge sort for divide and conquer;
- quicksort for partitioning and adversarial cases;
- heap sort for heap application;
- counting/radix sort for non-comparison sorting;
- `std::sort` for practical C++.

Novelty sorts are optional appendices, not prerequisites.

**Exit criteria:** You can derive rather than memorize the complexity of the core algorithms and can identify best, average, worst, amortized, and expected bounds.

## Stage 4: Linear and Hash-Based Data Structures

**Start:** [`04. Data Structures/README.md`](04.%20Data%20Structures/README.md)

Study:

1. Abstract data types and invariants
2. Dynamic arrays and amortized growth
3. Linked lists
4. Stacks and queues
5. Hash tables through the standard unordered containers
6. Tries
7. Disjoint-set union

Use the standard-library section for container APIs. The Data Structures section owns conceptual models and custom implementations; it should not duplicate the full `std::vector`, `std::map`, or `std::queue` API reference.

**Exit criteria:** You can implement a list, stack, queue, trie, and DSU; explain ownership; and verify each structure's invariants after mutations.

## Stage 5: Trees, Heaps, and Range Structures

**Start:** [`05. Trees and Graphs/README.md`](05.%20Trees%20and%20Graphs/README.md)

Study in this order:

1. Binary-tree vocabulary and node structure
2. Recursive and iterative traversals
3. Binary search trees
4. Binary heaps
5. AVL trees
6. Red-black-tree concepts
7. Fenwick trees
8. Segment trees and lazy propagation
9. Binary lifting and LCA
10. Euler-tour flattening

**Exit criteria:** You can derive traversal orders, implement BST and heap operations, explain balance invariants, and select a suitable range-query structure.

## Stage 6: Graph Foundations and Algorithms

Begin with graph representation and traversal:

1. [`04_Graph_Representations`](05.%20Trees%20and%20Graphs/04_Graph_Representations/README.md)
2. [`06_Basic_Graph_Algorithms`](05.%20Trees%20and%20Graphs/06_Basic_Graph_Algorithms/README.md)
3. [`Algorithms/01. Graph Algorithms`](Algorithms/01.%20Graph%20Algorithms/README.md)

Then study:

1. BFS shortest paths in unweighted graphs
2. DFS, components, and cycle detection
3. Topological sorting
4. Dijkstra
5. Bellman-Ford
6. Floyd-Warshall
7. Kruskal and Prim
8. SCCs, articulation points, and bridges
9. Eulerian paths
10. Max flow, min cut, and bipartite matching

For every graph algorithm, define:

- directed or undirected input;
- weighted or unweighted input;
- parallel-edge and self-loop behavior;
- valid weight range and overflow policy;
- disconnected-graph behavior;
- exact output contract.

**Exit criteria:** You can select a graph representation and algorithm from the input constraints, state all preconditions, and prove the central invariant.

## Stage 7: Algorithmic Design Paradigms

**Start:** [`Algorithms/README.md`](Algorithms/README.md)

Recommended order:

1. Divide and conquer
2. Greedy methods
3. Backtracking
4. Dynamic programming

Why this order:

- divide and conquer strengthens recurrence reasoning;
- greedy methods introduce proof obligations and counterexamples;
- backtracking makes state-space search explicit;
- dynamic programming builds on recursion, states, and optimal substructure.

Within dynamic programming, follow:

1. memoization and tabulation;
2. 1D and 2D state design;
3. subsequences, strings, grids, and knapsack;
4. reconstruction and space optimization;
5. tree, DAG, interval, digit, and bitmask DP;
6. advanced optimization techniques only after the base recurrence is clear.

**Exit criteria:** You can identify the paradigm from constraints, write a correctness argument, and explain why competing paradigms fail or are inferior for the problem.

## Stage 8: Applied Problem Patterns

**Start:** [`06. Problem Solving/README.md`](06.%20Problem%20Solving/README.md)

Study reusable patterns rather than memorizing solutions:

- two pointers;
- sliding windows;
- prefix and suffix accumulation;
- interval merging;
- cyclic traversal and Floyd's cycle detection;
- bit masks;
- modular arithmetic;
- string matching;
- monotonic structures;
- binary search on a monotonic answer;
- meet-in-the-middle.

Some of the final three items are curriculum gaps and will be added during cleanup.

**Exit criteria:** You can derive the pattern from constraints and invariants without identifying the problem by title.

## Stage 9: Projects and Integration

**Start:** [`03. OOPS/15_Projects_and_Applications/README.md`](03.%20OOPS/15_Projects_and_Applications/README.md)

The project section is currently a design outline and is being converted into tested projects. A completed student path should include:

1. a command-line container/algorithm playground;
2. a small library with headers, sources, tests, and CMake;
3. a graph-analysis tool;
4. one larger project combining ownership, interfaces, persistence, and testing.

**Exit criteria:** You can structure, build, test, document, and debug a multi-file C++ project rather than only solving isolated functions.

## Canonical Topic Ownership

To prevent duplicate lessons, new and existing content follows this ownership map:

| Topic type | Canonical location | Other sections should do |
|---|---|---|
| C++ syntax and language foundations | `01. Basics` | Link to the canonical lesson |
| Standard-library APIs and guarantees | `00. Headers and Libraries` | Link instead of repeating full API catalogs |
| Object lifetime and class design | `03. OOPS` | Link from examples requiring the concept |
| Custom data structures and invariants | `04. Data Structures` | Link to standard-container alternatives |
| Trees and graph foundations | `05. Trees and Graphs` | Reuse the canonical representations |
| Reusable problem patterns | `06. Problem Solving` | Avoid duplicating full algorithm lessons |
| Algorithm implementations and proofs | `Algorithms` | Other sections provide only prerequisite context |

## Verification Meaning

- **Illustrative:** useful for explanation but not yet independently built.
- **Compiles:** built under its declared language standard.
- **Tested:** automated normal and edge-case tests pass.
- **Verified:** compiled, tested, technically reviewed, cited where needed, and linked into this path.

The repository audit and remaining remediation work are tracked in [`REPORT.md`](REPORT.md).
