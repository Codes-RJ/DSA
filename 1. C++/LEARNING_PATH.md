# Start Here: C++ and DSA Learning Path

This is the one recommended route through `1. C++` for a new learner. The folders remain organized as a reference library, but you should follow the checkpoints on this page instead of reading directories from top to bottom.

> **Core language standard:** C++17
>
> **Optional language extensions:** C++20 and C++23 are labeled where used
>
> **Learning rule:** read a small amount, implement it, explain why it works, test it, and then practice it.

## Choose Your Starting Point

- If you have never compiled C++, begin at **Checkpoint 0**.
- If you can write functions using `std::vector` and can compile from a terminal, begin at **Checkpoint 1**.
- If you already know arrays, hashing, sorting, and binary search, take the exit task for Checkpoint 1 before skipping to Checkpoint 2.
- If your goal is revision, use the checkboxes and attempt the exit task of each checkpoint. Study only the checkpoints you cannot pass.

## Labels

| Label | Meaning |
|---|---|
| **Required** | Part of the main C++/DSA route. |
| **Bridge** | C++ knowledge needed immediately before a DSA topic. |
| **Practice** | A problem to solve after its prerequisites. |
| **Extension** | Useful depth after the checkpoint is complete. |
| **Reference** | Look up when needed; do not read linearly. |

## Progress Checklist

- [ ] Checkpoint 0 — Toolchain and C++ survival skills
- [ ] Checkpoint 1 — Complexity, arrays, hashing, sorting, and binary search
- [ ] Checkpoint 2 — Ownership, linked lists, recursion, and bits
- [ ] Checkpoint 3 — Stacks, queues, monotonic structures, and windows
- [ ] Checkpoint 4 — Heaps, greedy reasoning, intervals, and selection
- [ ] Checkpoint 5 — Trees, BSTs, balanced trees, and range queries
- [ ] Checkpoint 6 — Graph modeling and algorithms
- [ ] Checkpoint 7 — Backtracking and exhaustive search
- [ ] Checkpoint 8 — Dynamic programming by state pattern
- [ ] Checkpoint 9 — Tries and advanced string algorithms
- [ ] Checkpoint 10 — C++ design, reliability, and a project
- [ ] Checkpoint 11 — Electives

## The Study Loop

Use the same loop at every checkpoint:

1. Read the required lessons in order.
2. Type the core implementation yourself.
3. Write the input/output contract and central invariant in your own words.
4. Derive time and space complexity.
5. Test empty, singleton, duplicate, boundary, invalid, and adversarial inputs where relevant.
6. Attempt the practice problems before reading an editorial or solution.
7. Complete the exit task without following the lesson line by line.

The LeetCode links are applications, not replacements for the lessons. Write local tests as well; an accepted submission alone does not prove that you understand ownership, preconditions, or the reason an algorithm works.

## Checkpoint 0: Toolchain and C++ Survival Skills

**Goal:** Build, run, debug, and test a small C++17 program.

### Required route

1. [Toolchain and build guide](TOOLCHAIN.md)
2. [Repository standards](STANDARDS.md)
3. [Variables, keywords, and operators](01.%20Basics/01_Variables_Keywords_and_Operators.md)
4. [Conditionals and loops](01.%20Basics/02_Conditional_Statements.md), then [loops in depth](01.%20Basics/03_Loops_and_Iteration.md)
5. [Functions and scope](01.%20Basics/04_Functions_and_Scope.md)

### C++ support lane

Learn primitive types, expressions, control flow, functions, basic references, `const`, `std::string`, `std::vector`, console I/O, compiler warnings, and assertions. Do not pause here for inheritance, design patterns, concurrency, or manual allocation.

### Practice

- **Bridge:** [1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) — trace a loop and preserve a prefix invariant.
- **Preview:** [1. Two Sum](https://leetcode.com/problems/two-sum/) — first solve with nested loops; revisit with hashing in Checkpoint 1.

### Exit task

Build a program that reads integers, reports their minimum, maximum, and running sums, and has tests for one element, duplicates, and negative values. Explain every variable's lifetime.

## Checkpoint 1: Complexity, Arrays, Hashing, Sorting, and Binary Search

**Goal:** Acquire the first practical algorithm toolkit early.

### Required route

1. [Search theory and complexity](02.%20Basic%20Problems/Search/Theory.md)
2. [Array fundamentals](01.%20Basics/05_Arrays_and_Strings.md) and [`std::vector`](00.%20Headers%20and%20Libraries/Fundamentals/09_vector.md)
3. [`std::unordered_map`](00.%20Headers%20and%20Libraries/Fundamentals/18_unordered_map.md) and [`std::unordered_set`](00.%20Headers%20and%20Libraries/Fundamentals/16_unordered_set.md)
4. [Insertion Sort](02.%20Basic%20Problems/Sorting/02_Insertion_Sort.md), [Merge Sort](02.%20Basic%20Problems/Sorting/04_Merge_Sort.md), [Quick Sort](02.%20Basic%20Problems/Sorting/05_Quick_Sort.md), and [Heap Sort](02.%20Basic%20Problems/Sorting/06_Heap_Sort.md)
5. [Binary Search](02.%20Basic%20Problems/Search/02_Binary_Search.md)

### C++ support lane

Learn iterators, `std::sort`, `std::lower_bound`, comparator basics, capacity versus size, iterator invalidation, direct includes, and integer-overflow checks. Standard-container API details remain reference material.

### Practice

- [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) — frequency array versus hash map.
- [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) — expected linear-time hashing.
- [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) — implement an `O(N log N)` sort without calling the library sorter.
- [704. Binary Search](https://leetcode.com/problems/binary-search/) — interval invariant.
- [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) — binary search under partial order.
- [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) — binary search on a monotonic answer.

### Exit task

Given input constraints, choose between linear scan, sorting, binary search, ordered lookup, and hash lookup. Implement two choices, derive their costs, and explain which assumptions make each valid.

### Extension

Counting, radix, and bucket sort follow the core comparison sorts. Shell, Tim, Intro, Cocktail, Comb, Gnome, Odd-Even, Bitonic, Pancake, Cycle, and Bogo Sort are optional comparisons, not prerequisites.

## Checkpoint 2: Ownership, Linked Lists, Recursion, and Bits

**Goal:** Build pointer-based structures without confusing links with ownership.

### Required route

1. [Pointers and memory management](01.%20Basics/06_Pointers_and_Memory_Management.md)
2. [Data-structure interfaces and invariants](04.%20Data%20Structures/Theory.md)
3. [Custom linked list](04.%20Data%20Structures/09_Linked_List.md)
4. [Divide-and-conquer introduction](Algorithms/04.%20Divide%20and%20Conquer/01_Introduction_to_Divide_and_Conquer.md)
5. [Bit-manipulation module](06.%20Problem%20Solving/02_Bit_Manipulation/README.md)

### C++ support lane

Learn addresses, pointers, references, automatic versus dynamic storage, RAII, destructor purpose, `std::unique_ptr`, non-owning observation, and recursion-depth risk. Raw allocation is a learning tool here, not the default production recommendation.

### Practice

- [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) — iterative and recursive pointer rewiring.
- [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) — sorted merge and sentinel reasoning.
- [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) — Floyd's constant-space cycle detection.
- [78. Subsets](https://leetcode.com/problems/subsets/) — preview a recursive decision tree; revisit in Checkpoint 7.

### Exit task

Implement insertion, deletion, reversal, and cycle detection for a list. Draw the ownership relation separately from `next` links and verify invariants after each mutation.

## Checkpoint 3: Stacks, Queues, Monotonic Structures, and Windows

**Goal:** Learn reusable state-maintenance patterns immediately after their base ADTs.

### Required route

1. [Custom Stack and Queue](04.%20Data%20Structures/10_Custom_Stack_and_Queue.md)
2. [`std::stack`](00.%20Headers%20and%20Libraries/Fundamentals/19_stack.md), [`std::queue`](00.%20Headers%20and%20Libraries/Fundamentals/20_queue.md), and [`std::deque`](00.%20Headers%20and%20Libraries/Fundamentals/12_deque.md)
3. [Two-pointer technique](06.%20Problem%20Solving/04_Array_Problems/02_Two_Pointer_Technique.md)
4. [Sliding window](06.%20Problem%20Solving/04_Array_Problems/03_Sliding_Window.md)

### Practice

- [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) — direct stack application.
- [155. Min Stack](https://leetcode.com/problems/min-stack/) — augment an ADT while retaining `O(1)` operations.
- [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) — monotonic stack.
- [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) — variable window.
- [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) — monotonic deque challenge.

### Exit task

For one stack and one window problem, define exactly what every stored index means and prove that each item enters and leaves the structure only a bounded number of times.

> **Current gap:** Dedicated monotonic-stack and monotonic-queue lessons still need to be added. Use the practice problems only after the relevant invariant has been introduced.

## Checkpoint 4: Heaps, Greedy Reasoning, Intervals, and Selection

**Goal:** Connect priority-based processing to correctness arguments.

### Required route

1. [Binary Heap](05.%20Trees%20and%20Graphs/08_Binary_Heap/01_Binary_Heap.md)
2. [`std::priority_queue`](00.%20Headers%20and%20Libraries/Fundamentals/21_priority_queue.md)
3. [Quickselect](Algorithms/04.%20Divide%20and%20Conquer/13_Quick_Select.md)
4. [Greedy introduction](Algorithms/03.%20Greedy%20Algorithms/01_Introduction_to_Greedy.md)
5. [Proof of greedy optimality](Algorithms/03.%20Greedy%20Algorithms/21_Proof_of_Optimality.md)

### Practice

- [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) — compare heap, quickselect, and full sort.
- [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) — combine hashing and selection.
- [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) — two-heap balance invariant.
- [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) — sorted covered-prefix invariant.
- [55. Jump Game](https://leetcode.com/problems/jump-game/) — prove a greedy frontier and compare with DP.

### Exit task

Solve one problem with a heap and one with a greedy choice. Give an exchange argument for the greedy solution or a counterexample proving the proposed rule wrong.

## Checkpoint 5: Trees, BSTs, Balanced Trees, and Range Queries

**Goal:** Move from traversal to mutation invariants, then to workload-driven structures.

### Required route

1. [Binary Trees](05.%20Trees%20and%20Graphs/01_Binary_Trees/README.md)
2. [Tree traversals](05.%20Trees%20and%20Graphs/05_Tree_Traversals/README.md)
3. [Binary Search Trees](05.%20Trees%20and%20Graphs/02_BST/README.md)
4. [Fenwick Tree](04.%20Data%20Structures/14_Fenwick_Tree.md)
5. [Segment Tree](04.%20Data%20Structures/13_Segment_Tree.md)

### Practice

- [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) — queue-based tree BFS.
- [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) — postorder state.
- [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) — global ordering bounds.
- [307. Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) — Fenwick or Segment Tree by operation contract.

### Exit task

Implement a BST mutation and a range-query structure. State the invariant before and after every operation and test an input that would break a naive implementation.

### Extension

[AVL Trees](05.%20Trees%20and%20Graphs/03_AVL_Trees/README.md) follow BST mutations. [Red-Black Trees](05.%20Trees%20and%20Graphs/07_Red_Black_Trees/README.md) may remain conceptual. [LCA and Euler-tour techniques](05.%20Trees%20and%20Graphs/09_Advanced_Tree_Techniques/README.md) follow ordinary traversal and range-query competence.

## Checkpoint 6: Graph Modeling and Algorithms

**Goal:** Choose a representation and declare the graph contract before selecting an algorithm.

### Required route

1. [Graph representations](05.%20Trees%20and%20Graphs/04_Graph_Representations/README.md)
2. [BFS, DFS, components, cycles, and topological order](05.%20Trees%20and%20Graphs/06_Basic_Graph_Algorithms/README.md)
3. [Disjoint-Set Union](04.%20Data%20Structures/12_Disjoint_Set_Union.md)
4. [Shortest paths](Algorithms/01.%20Graph%20Algorithms/01_Dijkstra_Algorithm.md), then [Bellman-Ford](Algorithms/01.%20Graph%20Algorithms/02_Bellman_Ford_Algorithm.md)
5. [Minimum spanning trees](Algorithms/01.%20Graph%20Algorithms/04_Kruskal_Algorithm.md), then [Prim](Algorithms/01.%20Graph%20Algorithms/05_Prim_Algorithm.md)

### Practice

- [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) — implicit graph and components.
- [133. Clone Graph](https://leetcode.com/problems/clone-graph/) — traversal, identity mapping, and deep copy.
- [207. Course Schedule](https://leetcode.com/problems/course-schedule/) — cycle detection/topological ordering.
- [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/) — DSU.
- [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) — Dijkstra and unreachable vertices.
- [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) — MST modeling.

### Exit task

For every graph solution, declare directedness, weight domain, self-loop/parallel-edge policy, disconnected behavior, and overflow strategy. Implement and test one traversal, one shortest path, and one MST algorithm.

### Extension

Floyd-Warshall and Johnson follow single-source shortest paths. A* follows Dijkstra and heuristic admissibility. SCCs, bridges, articulation points, Eulerian paths, maximum flow, minimum cut, and matching close the graph unit; none should interrupt the representation/BFS/DFS foundation.

## Checkpoint 7: Backtracking and Exhaustive Search

**Goal:** Convert recursion into explicit state-space search with pruning.

### Required route

1. [Backtracking introduction](Algorithms/05.%20Backtracking/01_Introduction_to_Backtracking.md)
2. [Recursive backtracking](Algorithms/05.%20Backtracking/02_Recursive_Backtracking.md)
3. [Pruning](Algorithms/05.%20Backtracking/03_Pruning_Techniques.md)
4. [Subset generation](Algorithms/05.%20Backtracking/09_Subset_Generation.md)
5. [N-Queens](Algorithms/05.%20Backtracking/04_N_Queens.md)

### Practice

- [78. Subsets](https://leetcode.com/problems/subsets/) — formalize the binary decision tree.
- [39. Combination Sum](https://leetcode.com/problems/combination-sum/) — reusable choices and target pruning.
- [51. N-Queens](https://leetcode.com/problems/n-queens/) — column and diagonal constraints.

### Exit task

Before coding, write the state, choices, rejection rule, undo operation, stopping condition, and worst-case search space. Then show how pruning changes explored states without changing valid answers.

## Checkpoint 8: Dynamic Programming by State Pattern

**Goal:** Derive states and recurrences rather than memorize problem titles.

### Required route

1. [DP introduction](Algorithms/02.%20Dynamic%20Programming/01_Introduction_to_DP.md)
2. [Memoization](Algorithms/02.%20Dynamic%20Programming/02_Memoization.md) and [tabulation](Algorithms/02.%20Dynamic%20Programming/03_Tabulation.md)
3. [State transitions](Algorithms/02.%20Dynamic%20Programming/06_State_Transition.md)
4. [1D DP](Algorithms/02.%20Dynamic%20Programming/04_1D_DP.md) and [2D DP](Algorithms/02.%20Dynamic%20Programming/05_2D_DP.md)
5. [Knapsack](Algorithms/02.%20Dynamic%20Programming/11_Knapsack_Problems.md) and [DP on strings](Algorithms/02.%20Dynamic%20Programming/08_DP_on_Strings.md)

### Practice

- [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) — minimal state and transition.
- [198. House Robber](https://leetcode.com/problems/house-robber/) — include/exclude state.
- [322. Coin Change](https://leetcode.com/problems/coin-change/) — unreachable states and unbounded choice.
- [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) — Boolean knapsack.
- [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) — 2D string state.
- [72. Edit Distance](https://leetcode.com/problems/edit-distance/) — operation transitions and boundary initialization.

### Exit task

For an unfamiliar problem, write the state meaning, base cases, recurrence, evaluation order, correctness argument, and complexity before writing C++.

### Extension

Grid, tree, DAG, interval, digit, bitmask, probability, and optimization lessons come after ordinary state derivation. Meet-in-the-middle is a separate exponential-reduction pattern and must not be hidden inside DP optimization.

## Checkpoint 9: Tries and Advanced String Algorithms

**Goal:** Select a string technique from its query and preprocessing requirements.

### Required route

1. [Trie](04.%20Data%20Structures/11_Trie.md)
2. [String algorithms](06.%20Problem%20Solving/03_String_Problems/02_String_Algorithms.md)
3. [Pattern matching](06.%20Problem%20Solving/03_String_Problems/03_Pattern_Matching.md)

### Practice

- [208. Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) — prefix-structure contract.
- [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) — KMP after naive matching.
- [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) — compare center expansion and DP.
- [212. Word Search II](https://leetcode.com/problems/word-search-ii/) — trie plus backtracking capstone.

### Exit task

Given text size, pattern count, update frequency, and alphabet, justify direct scan, hashing, KMP/Z, trie indexing, suffix structure, or DP. State collision and character-domain assumptions.

## Checkpoint 10: C++ Design, Reliability, and a Project

**Goal:** Turn isolated solutions into maintainable multi-file C++ software.

### Required route

1. [OOP module guide](03.%20OOPS/README.md) — follow its foundations, classes, lifetime, encapsulation, and polymorphism sequence
2. [Templates and generic programming](03.%20OOPS/09_Templates_and_Generic_Programming/README.md)
3. [Exception handling](03.%20OOPS/10_Exception_Handling_in_OOP/README.md)
4. [Memory management](03.%20OOPS/11_Memory_Management_in_OOP/README.md)
5. [Projects and applications](03.%20OOPS/15_Projects_and_Applications/README.md)

### Practice

- [706. Design HashMap](https://leetcode.com/problems/design-hashmap/) — do this after a canonical hash-table-internals lesson is available.
- [146. LRU Cache](https://leetcode.com/problems/lru-cache/) — integrate hashing, ordering, invariants, and class design.
- Convert one earlier solution into a reusable header/source pair with automated tests and documented invalid-input behavior.

### Exit task

Build a graph-analysis command-line project with headers, sources, CMake, tests, parsing, explicit error behavior, and at least two algorithms. A clean checkout must build without manual IDE setup.

## Checkpoint 11: Electives

Choose these only after their prerequisites and only when they serve your goal:

- **Advanced C++:** concepts, advanced templates, allocators, placement new, memory pools, and low-level optimization.
- **Systems C++:** concurrency, atomics, filesystem, debugging, profiling, and portability.
- **Design:** pattern catalogs and larger OOP examples, preferably learned through a real project need.
- **Advanced DSA:** heavy-light/centroid decomposition, specialized balanced trees, advanced DP optimizations, and advanced string indexes.
- **Competitive programming:** contest mathematics, specialized tricks, and speed-oriented templates with their portability limitations stated.

The complete [Headers and Libraries](00.%20Headers%20and%20Libraries/README.md) section is always available as a reference. It is not a required linear course.

## Where Extra Topics Belong

| Material | Placement |
|---|---|
| Pattern-making exercises | Optional loop warm-up before or during Checkpoint 0. |
| Standard-library header encyclopedia | Reference shelf, linked just in time. |
| Manual memory and deep pointer mechanics | Bridge before linked lists; advanced material in Checkpoint 10. |
| Classes and encapsulation | Small practical subset for custom ADTs; full treatment in Checkpoint 10. |
| Inheritance and polymorphism | Checkpoint 10, not a gate before core DSA. |
| Templates | Basic use with custom structures; advanced techniques in Checkpoint 10/electives. |
| Exception guarantees and `noexcept` | Checkpoint 10 after RAII; basic error handling may appear earlier. |
| Design patterns | Project-driven elective after core DSA. |
| Novelty sorting | Optional appendix after core sorting. |
| Math and array/string puzzles | Tagged practice attached to the checkpoint that supplies their prerequisites. |
| AVL/Red-Black Trees | Extension after BST. |
| Fenwick/Segment Tree/LCA/Euler tour | End of the tree checkpoint. |
| Advanced graph algorithms | Layered at the end of the graph checkpoint. |
| Advanced DP | Layered at the end of the DP checkpoint. |
| Modern C++20/C++23 | Version-labeled support/elective lane; never a silent core-standard change. |

## Practice Placement Rule

When lessons are revised, each canonical lesson should end with no more than:

1. one **bridge** problem that directly applies the new operation;
2. one **validation** problem that requires recognizing the topic;
3. one **challenge** that combines it with an earlier topic;
4. a reflection prompt asking for the invariant, complexity, tests, and a rejected alternative.

Attempt first, inspect hints second, and read an editorial only after a serious attempt. Re-solve selected validation problems after a delay. Do not copy third-party problem statements or solutions into this repository; link to the official page and provide original prerequisite/hint notes.

## Canonical Topic Ownership

| Topic type | Canonical location | Other sections should do |
|---|---|---|
| C++ syntax and foundations | `01. Basics` | Link to the prerequisite. |
| Standard-library APIs and guarantees | `00. Headers and Libraries` | Apply or compare; do not repeat API catalogs. |
| Object lifetime and class design | `03. OOPS` | Link from structures/projects. |
| Custom structures and invariants | `04. Data Structures` | Compare with the standard alternative. |
| Tree and graph foundations | `05. Trees and Graphs` | Reuse the canonical representation/traversal. |
| Reusable problem patterns | `06. Problem Solving` | Attach applications, not duplicate algorithm theory. |
| Algorithm implementations and proofs | `Algorithms` | Other modules provide prerequisite context and links. |

## Verification Labels

- **Illustrative:** useful explanation, not independently built yet.
- **Compiles:** built under its declared language standard.
- **Tested:** automated normal and edge-case tests pass.
- **Verified:** compiled, tested, technically reviewed, appropriately sourced, and connected to this path.

Current limitations and the remaining implementation order are tracked in [`REPORT.md`](REPORT.md).
