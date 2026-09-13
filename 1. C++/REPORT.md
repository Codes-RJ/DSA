# Current C++ and DSA Curriculum Audit

**Audit date:** 2026-09-13

**Scope:** The complete current contents of `1. C++`, including every lesson, navigation document, example source, test, build file, and maintenance script.

**Purpose:** Record only work that remains. Completed cleanup history and resolved findings are intentionally omitted.

## Executive Judgement

The repository is now a broad and navigable C++/DSA study collection with a credible high-level learning sequence. It is not yet a fully dependable end-to-end curriculum.

The main weakness is no longer a lack of material. It is the gap between the amount of material and the amount that has been mechanically verified. There are 1,182 Markdown C++ examples containing `main`, but only eight canonical example headers and one smoke-test source in the compiled suite. Several lessons still overlap semantically, one standard-library lesson is structurally corrupted, and targeted compilation found concrete portability and missing-header defects.

The right next phase is therefore not indiscriminate expansion. It is consolidation, correction, extraction, testing, and only then filling the few remaining curriculum gaps.

### Overall assessment

| Area | Current judgement | Why |
|---|---|---|
| Learning order | Good foundation | `LEARNING_PATH.md` gives stages, prerequisites, and exit criteria, but several stated stage topics do not yet have canonical lessons. |
| Breadth | Very strong | The collection covers language fundamentals, the standard library, OOP, common data structures, graphs, core paradigms, and problem patterns. |
| Topic ownership | Partially resolved | Exact file duplicates are gone, but BFS/DFS, exception handling, modern-language topics, and string algorithms still have competing explanations. |
| Correctness confidence | Mixed | The small checked source suite passes, but most Markdown examples have never been compiled independently. Confirmed defects remain. |
| Maintainability | Weak to moderate | Many lessons are very large, headings are generic, metadata is inconsistent, and code fences are not uniformly typed. |
| Student readiness | Suitable with supervision | Useful today as a study compendium; not yet safe to present every snippet or completeness claim as verified. |

## Audit Baseline

The following measurements exclude this report unless stated otherwise.

| Measure | Current value |
|---|---:|
| Markdown documents | 464 |
| Markdown lines | 219,412 |
| Directories | 62 |
| Fenced blocks | 3,647 |
| C++ fenced blocks | 2,581 |
| C++ blocks containing `main` | 1,182 |
| Unlabeled fenced blocks | 1,047 |
| Markdown files at least 750 lines long | 82 |
| Markdown files at least 1,000 lines long | 26 |
| C++ source/header files in `examples` and `tests` | 9 |
| Files with a references/sources/further-reading heading | 18 |
| Files with an exercise or practice heading | 278 |
| Files with a solution heading | 58 |

Read-only checks also found:

- zero empty Markdown files;
- zero exact duplicate-content groups by SHA-256;
- zero broken local paths under the existing link checker;
- one Markdown file with unbalanced fences;
- no whitespace errors from `git diff --check` (line-ending warnings are informational);
- the canonical smoke-test executable compiles with the locally available GCC 6.3 C++17-mode flag and exits successfully;
- CMake is not installed in the local environment, so the CMake configuration and declared CI matrix were inspected but not executed here.

These facts are useful but limited. A valid local link is not proof that its anchor exists, and a passing nine-file source suite does not validate thousands of embedded snippets.

## Priority 0: Correctness and Structural Defects

These should be fixed before further restructuring because they can directly misteach students or break copied examples.

### 1. Repair the corrupted `<algorithm>` lesson

**File:** [`00. Headers and Libraries/Fundamentals/04_algorithm.md`](00.%20Headers%20and%20Libraries/Fundamentals/04_algorithm.md)

The file has 51 fence markers, so one fence is unmatched. Its second half also repeats earlier sections:

- “Example 4” appears around lines 233 and 428;
- “Performance Considerations” appears around lines 289 and 484;
- “Common Patterns” appears around lines 320 and 515;
- “Pitfalls and Best Practices” appears around lines 360 and 555;
- “Advanced Techniques” appears around lines 402 and 597;
- lines 418-426 contain orphaned `replace(...)`, `return 0`, and closing-brace material outside the intended example boundary.

**Recommendation:** Reconstruct the page from its first coherent copy, retain any genuinely unique material from the duplicated half, remove the orphaned lines, and run a fence-balance check afterward. Because this is a central Stage 2 lesson, extract at least one representative algorithms example into the compiled suite.

**Done when:** The file has balanced fences, no repeated section sequence, every snippet has a language label, and its representative source compiles under its declared standard.

### 2. Correct two misleading `noexcept` examples

**Files:**

- [`01. Basics/07_Error_Handling.md`](01.%20Basics/07_Error_Handling.md), around lines 395-410
- [`03. OOPS/10_Exception_Handling_in_OOP/Theory.md`](03.%20OOPS/10_Exception_Handling_in_OOP/Theory.md), around line 324

The Basics page declares a function containing stream output as unconditionally `noexcept`. Streams can throw if their exception mask is enabled. The same example uses `noexcept(data)`, which tests the expression `data`, not the operations performed by the function body. It therefore teaches the wrong way to derive a conditional exception specification.

The OOP theory page uses:

```cpp
void swap(T& a, T& b) noexcept(noexcept(T(move(a)))) { }
```

This checks only one move-construction expression, omits the rest of a swap's requirements, leaves the body empty, and uses an unqualified `move`. It is not a sound generic swap example.

**Recommendation:** Make the beginner page explain termination behavior without claiming ordinary I/O is safely non-throwing. In the advanced page, use `std::is_nothrow_move_constructible_v<T>` together with `std::is_nothrow_move_assignable_v<T>`, or delegate to a real operation whose exception specification is queried with `noexcept(...)`. Compile both examples as dedicated tests.

**Done when:** The exception specifications correspond to every potentially throwing operation in the body, the text distinguishes “normally does not throw” from the language-level `noexcept` contract, and tests demonstrate `std::terminate` behavior separately rather than invoking it in the main smoke suite.

### 3. Add missing standard-library headers to graph examples

Targeted extraction and syntax checking identified four real missing-include defects:

| File | Use | Missing header |
|---|---|---|
| [`02_Bellman_Ford_Algorithm.md`](Algorithms/01.%20Graph%20Algorithms/02_Bellman_Ford_Algorithm.md) | `std::log`/`log` in the arbitrage example | `<cmath>` |
| [`04_Kruskal_Algorithm.md`](Algorithms/01.%20Graph%20Algorithms/04_Kruskal_Algorithm.md) | `INT_MAX` | `<climits>` |
| [`10_Bipartite_Graph.md`](Algorithms/01.%20Graph%20Algorithms/10_Bipartite_Graph.md) | `INT_MAX` | `<climits>` |
| [`13_Bipartite_Matching.md`](Algorithms/01.%20Graph%20Algorithms/13_Bipartite_Matching.md) | `std::chrono`/`chrono` | `<chrono>` |

**Recommendation:** Add the direct includes rather than relying on transitive includes. Prefer qualified names where editing the examples. Add all four to extraction-based compile checks.

**Done when:** Each affected complete example compiles in isolation on GCC, Clang, and MSVC under its declared standard.

### 4. Replace a non-standard variable-length array

**File:** [`02. Basic Problems/Sorting/09_Bucket_Sort.md`](02.%20Basic%20Problems/Sorting/09_Bucket_Sort.md), line 45

The implementation uses `vector<float> buckets[n];`, where `n` is a runtime value. Variable-length arrays are not part of standard C++ even if some compilers accept them as an extension.

**Recommendation:** Use `std::vector<std::vector<float>> buckets(static_cast<std::size_t>(n));`, validate the expected input domain, and guard the `1.0` boundary so `n * arr[i]` cannot index one past the final bucket.

**Done when:** The example builds with extensions disabled and tests empty input, one element, repeated values, values near both boundaries, and invalid-domain behavior.

### 5. Correct the range-query complexity entry

**File:** [`MASTER_DSA_MAP.md`](MASTER_DSA_MAP.md), line 337

The decision table currently describes Segment Tree as `O(4N)` and Fenwick Tree as `O(N)` for “point updates with range aggregate queries.” This mixes common allocation sizes with operation complexity. `4N` also simplifies to `O(N)` in asymptotic notation.

**Recommendation:** State build/storage and operation costs separately. For example: Segment Tree—build `O(N)`, storage `O(N)`, point update and range query `O(log N)`; Fenwick Tree—build `O(N)` with the linear construction or `O(N log N)` with repeated updates, storage `O(N)`, point update and prefix/range query `O(log N)`.

**Done when:** The map no longer mixes storage constants with query/update complexity and agrees with both canonical data-structure lessons.

## Priority 1: Finish Semantic Deduplication

Exact byte-for-byte duplication is no longer the problem. The remaining duplication is conceptual: two pages can differ in wording while still competing to teach the same topic. Every pair below needs one canonical owner and a deliberately narrower role for the other location.

### 1. BFS and DFS have two full graph tutorials each

Competing pages:

- [`05_Tree_Traversals/02_Breadth_First_Search.md`](05.%20Trees%20and%20Graphs/05_Tree_Traversals/02_Breadth_First_Search.md) and [`06_Basic_Graph_Algorithms/01_Graph_Traversal_BFS.md`](05.%20Trees%20and%20Graphs/06_Basic_Graph_Algorithms/01_Graph_Traversal_BFS.md)
- [`05_Tree_Traversals/01_Depth_First_Search.md`](05.%20Trees%20and%20Graphs/05_Tree_Traversals/01_Depth_First_Search.md) and [`06_Basic_Graph_Algorithms/02_Graph_Traversal_DFS.md`](05.%20Trees%20and%20Graphs/06_Basic_Graph_Algorithms/02_Graph_Traversal_DFS.md)

The pages in `05_Tree_Traversals` are graph-traversal tutorials, not tree-only traversal lessons, so their location and content both conflict with the `06_Basic_Graph_Algorithms` versions.

**Recommendation:** Make `06_Basic_Graph_Algorithms` the canonical home for general graph BFS/DFS. Replace the two files under `05_Tree_Traversals` with genuinely tree-specific level-order and preorder/inorder/postorder material, or remove them and link to the graph pages where relevant. Do not keep two full implementations under different labels.

### 2. `override` and `final` repeat runtime-polymorphism lessons

**Competing page:** [`03. OOPS/14_Modern_Cpp_OOP_Features/09_Override_and_Final.md`](03.%20OOPS/14_Modern_Cpp_OOP_Features/09_Override_and_Final.md)

**Canonical pages:**

- [`02_Override_Specifier.md`](03.%20OOPS/06_Polymorphism/02_Run_Time_Polymorphism/02_Override_Specifier.md)
- [`03_Final_Specifier.md`](03.%20OOPS/06_Polymorphism/02_Run_Time_Polymorphism/03_Final_Specifier.md)

**Recommendation:** Keep the detailed semantics and examples in runtime polymorphism. Reduce the modern-features page to a concise C++11 adoption note linking to the canonical lessons, or delete it if it contributes no distinct migration perspective.

### 3. Beginner error handling competes with the full exception module

[`01. Basics/07_Error_Handling.md`](01.%20Basics/07_Error_Handling.md) is large enough to function as a second exception-handling course, overlapping [`03. OOPS/10_Exception_Handling_in_OOP/`](03.%20OOPS/10_Exception_Handling_in_OOP/README.md).

**Recommendation:** Restrict Basics to error categories, return values, simple exceptions, assertions, RAII motivation, and when to continue to the advanced module. Keep exception hierarchies, custom exception design, exception guarantees, constructor/destructor behavior, and `noexcept` in the canonical OOP exception module.

### 4. The STL overview needs a decision-guide role

[`00. Headers and Libraries/Others/stl_containers.md`](00.%20Headers%20and%20Libraries/Others/stl_containers.md) overlaps the individual container reference pages.

**Recommendation:** Turn it into a compact container-selection guide: ownership model, ordering, lookup needs, invalidation, memory locality, and links. Remove repeated API catalogs and long implementations already owned by individual header lessons.

### 5. Concepts needs one canonical C++20 owner

[`03. OOPS/14_Modern_Cpp_OOP_Features/10_Concepts.md`](03.%20OOPS/14_Modern_Cpp_OOP_Features/10_Concepts.md) overlaps Concepts material inside template theory.

**Recommendation:** Keep language syntax, constraint normalization, subsumption, and diagnostics in the Modern C++ page. Keep only the minimum prerequisite/link in template theory. Mark the canonical page as C++20 in structured metadata and compile it in a C++20 target.

### 6. String algorithms are repeated across problem pages

KMP, Z-function, and suffix-array explanations recur across:

- [`02_String_Algorithms.md`](06.%20Problem%20Solving/03_String_Problems/02_String_Algorithms.md)
- [`03_Pattern_Matching.md`](06.%20Problem%20Solving/03_String_Problems/03_Pattern_Matching.md)
- [`05_Advanced_String_Problems.md`](06.%20Problem%20Solving/03_String_Problems/05_Advanced_String_Problems.md)

KMP is also embedded as machinery in the sublist-search lesson.

**Recommendation:** Give each algorithm exactly one proof-and-implementation page. Pattern/application pages should state the problem transformation and link to the canonical algorithm rather than restating preprocessing, correctness, and full source. A sublist-search page may show adaptation-specific code, but should not become another general KMP tutorial.

### 7. README and Theory pages have ambiguous identity

Search README/Theory and Sorting README/Theory pairs use the same H1 text. Even where their bodies differ, learners cannot infer which is navigation and which is instruction.

**Recommendation:** Rename H1s by role, such as “Search Algorithms: Study Guide” versus “Search Algorithms: Theory and Complexity.” Apply the same rule to Sorting and other module pairs.

## Priority 1: Build a Real Verification Pipeline

### The present confidence gap

There are 2,581 C++ fenced blocks and 1,182 blocks that contain a `main` function. The checked suite contains eight reusable headers plus one smoke-test source. That suite is valuable, but it directly represents well under one percent of the apparently runnable Markdown programs.

A targeted syntax-check of graph and custom-data-structure `main` blocks examined 22 blocks:

- 9 compiled as extracted;
- 4 exposed the confirmed missing headers listed above;
- 3 used structured bindings that the locally installed GCC 6.3 does not fully support, so those failures are toolchain limitations rather than established source defects;
- 6 custom-data-structure mains depended on class definitions located in earlier fences and therefore could not compile independently.

The last category is an important documentation-design issue. A page may present several fragments that collectively form a program, but a student copying the block labeled as the example's `main` cannot build it alone. Verification tooling needs either named multi-block assembly or a single complete source.

### Recommended pipeline

1. Add stable identifiers to executable fences, for example `example-id`, declared standard, and whether the block is `complete`, `fragment`, `output`, or `pseudocode`.
2. Build an extractor that assembles explicitly related blocks and writes temporary `.cpp` files.
3. Compile complete examples with warnings enabled and compiler extensions disabled.
4. Run deterministic examples with expected output; convert algorithms into library-style functions so edge cases can be unit tested.
5. Maintain separate C++17, C++20, and C++23 targets. Never silently raise the standard for the entire curriculum because one lesson needs a newer feature.
6. Test on GCC, Clang, and MSVC; add sanitizer jobs for executable C++17 examples where supported.
7. Publish a generated verification manifest containing file, example ID, standard, compile status, test status, and last verification commit.
8. Fail CI when a complete example is unverified, an extraction mapping becomes stale, or a verified badge has no manifest entry.

### First extraction batch

Start with the learning path's spine rather than novelty material:

1. variables/functions and ownership examples;
2. `vector`, iterators, `algorithm`, maps, and unordered maps;
3. binary search, merge sort, quicksort, and heap sort;
4. linked list, stack, queue, trie, DSU, Fenwick Tree, and Segment Tree;
5. tree traversals, BST, and heap;
6. BFS, DFS, topological sort, shortest paths, MST, SCC, and max flow;
7. one representative implementation from each DP, greedy, divide-and-conquer, and backtracking stage.

This order creates a trustworthy student path sooner than compiling files alphabetically.

## Priority 2: Close the Curriculum Gaps

### 1. Dynamic arrays need a canonical data-structure lesson

Stage 4 promises dynamic arrays and amortized growth, but `04. Data Structures` does not own a focused custom dynamic-array implementation. A custom array-like implementation exists inside [`06. Problem Solving/04_Array_Problems/01_Array_Basics.md`](06.%20Problem%20Solving/04_Array_Problems/01_Array_Basics.md), which is the wrong conceptual home.

**Recommendation:** Move or rebuild that implementation as a canonical `Dynamic_Array.md` lesson under Data Structures. Cover capacity versus size, geometric growth, amortized `push_back`, strong/basic exception guarantees during reallocation, move-aware element transfer, iterator/reference invalidation, and why students should use `std::vector` in production. The problem-solving page should link to it.

### 2. Hash-table internals are missing from the custom-structure path

The path currently teaches hash tables “through the standard unordered containers.” That teaches API selection, not the data structure in depth.

**Recommendation:** Add one canonical hash-table module under Data Structures covering hash functions, separate chaining, open addressing, tombstones, load factor, rehashing, expected versus adversarial complexity, iterator invalidation, and collision-focused tests. Keep the standard container API in Headers and Libraries.

### 3. Three Stage 8 patterns need dedicated canonical lessons

The learning path itself identifies these as gaps:

- monotonic stack and monotonic queue;
- binary search on a monotonic answer;
- meet-in-the-middle.

Material exists in scattered subsections, but none currently serves as a focused canonical lesson with recognition rules, invariant, template, counterexamples, and exercises.

**Recommendation:** Add one concise lesson per pattern under `06. Problem Solving`, then replace scattered re-explanations with application links. For monotonic structures, distinguish next-greater-element stacks from window-extrema deques. For answer search, require proof of predicate monotonicity and safe midpoint/bounds. For meet-in-the-middle, explain the `2^(N/2)` tradeoff and when hashing, sorting, or two pointers combines halves.

### 4. The project stage is still an outline

[`03. OOPS/15_Projects_and_Applications/README.md`](03.%20OOPS/15_Projects_and_Applications/README.md) describes projects, while the learning path explicitly says they are still being converted into tested projects.

**Recommendation:** Implement at least one end-to-end project before describing Stage 9 as complete. It should contain headers and sources, CMake targets, unit tests, invalid-input handling, a short architecture explanation, and a student milestone sequence. A graph-analysis CLI is the best first project because it integrates parsing, containers, ownership, algorithms, testing, and performance constraints.

### 5. Optional advanced depth is uneven

Heavy-light decomposition and centroid decomposition are mentioned but not taught as complete modules. Suffix automata, treaps, and B-trees are absent or overview-only. These are not blockers for a strong core DSA course.

**Recommendation:** Mark them explicitly as optional extensions. Add them only after the core verification backlog is substantially reduced; otherwise breadth will continue to outrun reliability.

## Priority 2: Split the Remaining Oversized Lessons

There are 82 files at least 750 lines long and 26 at least 1,000 lines long. File length is not automatically a defect, but these files commonly combine theory, multiple implementations, applications, benchmarks, exercises, and references. That makes navigation, deduplication, review, and example extraction unnecessarily difficult.

Largest current instructional files:

| Lines | File |
|---:|---|
| 1,384 | `02. Basic Problems/Sorting/09_Bucket_Sort.md` |
| 1,326 | `00. Headers and Libraries/Fundamentals/15_set.md` |
| 1,323 | `02. Basic Problems/Sorting/04_Merge_Sort.md` |
| 1,321 | `02. Basic Problems/Sorting/02_Insertion_Sort.md` |
| 1,300 | `02. Basic Problems/Sorting/10_Shell_Sort.md` |
| 1,292 | `00. Headers and Libraries/Fundamentals/16_unordered_set.md` |
| 1,287 | `02. Basic Problems/Sorting/06_Heap_Sort.md` |
| 1,287 | `00. Headers and Libraries/Fundamentals/14_forward_list.md` |
| 1,242 | `00. Headers and Libraries/Fundamentals/20_queue.md` |
| 1,198 | `00. Headers and Libraries/Fundamentals/25_functional.md` |
| 1,185 | `02. Basic Problems/Sorting/08_Counting_Sort.md` |
| 1,152 | `02. Basic Problems/Sorting/Theory.md` |
| 1,145 | `00. Headers and Libraries/Fundamentals/13_list.md` |
| 1,138 | `02. Basic Problems/Sorting/07_Radix_Sort.md` |
| 1,129 | `00. Headers and Libraries/Fundamentals/23_iterator.md` |
| 1,120 | `00. Headers and Libraries/Fundamentals/18_unordered_map.md` |
| 1,116 | `00. Headers and Libraries/Fundamentals/19_stack.md` |
| 1,114 | `02. Basic Problems/Sorting/05_Quick_Sort.md` |

### Recommended split rule

Do not split by arbitrary line count. Convert each oversized topic into a folder only when it has multiple independent learning units. Use this stable shape:

```text
Topic/
  README.md                 # scope, prerequisites, order, summary
  01_Concepts_and_Invariants.md
  02_Core_Operations.md
  03_Implementation.md
  04_Complexity_and_Correctness.md
  05_Applications_and_Exercises.md
```

Header/reference topics may instead use “API and guarantees,” “invalidation and complexity,” and “examples.” Sorting topics should separate invariant/proof, baseline implementation, variants, and benchmarking. Preserve old incoming links with a small redirect page when deletion would strand external bookmarks.

### Split order

1. `04_algorithm.md`, because it is already corrupted;
2. Bucket, Merge, Quick, Heap, Counting, and Radix Sort, because they are core and code-heavy;
3. `set`, `unordered_set`, `unordered_map`, `list`, `forward_list`, `stack`, and `queue`, because they need clear API-versus-internals boundaries;
4. remaining files over 1,000 lines;
5. files over 750 lines only where heading analysis shows multiple independent lessons.

## Priority 2: Normalize Lesson Contracts and Navigation

### Metadata is too inconsistent

Approximate text scans found only:

- 25 files mentioning a minimum/core language standard;
- 46 mentioning prerequisites;
- 13 mentioning learning outcomes or exit criteria;
- 384 containing a “Next Step.”

These counts include free-form prose and therefore overestimate truly structured metadata.

**Recommendation:** Give every instructional lesson a small machine-readable or consistently formatted contract:

```yaml
level: beginner | intermediate | advanced
prerequisites:
  - canonical-topic-id
cpp_standard: 17
status: illustrative | compiles | tested | verified
estimated_time: 45m
```

Follow it with explicit learning outcomes, the lesson, exercises, and a next step. Generate stage indexes from this metadata to prevent path drift.

### Generic H1 titles reduce orientation

Fourteen module pages are titled only `README.md`, and eleven instructional overviews are titled only `Theory.md`. File names belong in the filesystem, not in the visible curriculum title.

**Recommendation:** Use descriptive H1s such as “Runtime Polymorphism: Module Guide” and “Dynamic Programming: Theory, State Design, and Proof.” Require H1 uniqueness within a module and distinguish navigation pages from teaching pages.

### Root inventory is stale and manually maintained

[`README.md`](README.md) says there are 435 Markdown files, while the current tree contains 464 Markdown documents excluding this report. Its hand-written tree also contains inconsistent labels such as “Tree Transversals” and can drift whenever files are split.

**Recommendation:** Remove the exact count or generate it. Replace the detailed hand-maintained tree with links to canonical module indexes, or generate the tree from the filesystem during CI.

### Exercise flow is not consistently protected

Many lessons contain practice prompts, but solutions are often embedded immediately after examples or mixed into the same long page. The learning path tells students to solve exercises before opening solutions, yet the repository does not consistently make that possible.

**Recommendation:** For core assessed lessons, put exercises in the lesson and solutions in a sibling `Solutions.md` or collapsible section clearly marked as a spoiler. Add expected complexity and edge-case requirements to each exercise, not just a target output.

## Priority 3: Improve Claims, Sources, and Modern Style

### Completeness and production claims exceed the evidence

A broad scan found 179 phrases across 167 files matching claims such as “100%,” “production-ready/grade,” “complete guide/implementation/reference/coverage,” or “fully implemented.” Some are harmless descriptions of a full snippet, but the aggregate claim level is incompatible with the current verification coverage.

**Recommendation:** Replace marketing-style claims with bounded statements: what inputs are supported, which standard is required, what tests exist, and what remains illustrative. Permit “verified” only when backed by the generated manifest.

### Sources and further reading are sparse

Only 18 of 464 documents have a references, sources, or further-reading heading, and only 10 files contain any external URL. Algorithm proofs, standard-library guarantees, complexity bounds, and language-rule explanations often have no provenance.

**Recommendation:** Adopt a short source policy. Language rules should link to the current ISO draft section or cppreference as appropriate; algorithms should cite a textbook, original paper, or reputable course; implementation-specific facts should identify the implementation/version. References should support non-obvious claims rather than become a generic link dump.

### Modern-style inconsistencies are widespread

Text-level scans, which include prose as well as code, found:

| Pattern | Occurrences | Files |
|---|---:|---:|
| `using namespace std;` | 833 | 227 |
| `new` | 1,113 | 187 |
| `delete` | 672 | 118 |
| `rand(...)` | 41 | 16 |
| `srand(...)` | 13 | 7 |
| `malloc(...)` | 13 | 3 |
| `free(...)` | 14 | 4 |
| `NULL` | 6 | 5 |

Raw allocation is necessary in lessons that explicitly teach ownership, allocators, or data-structure internals, so blanket replacement would be wrong. The problem is that pedagogical and recommended usage are not always distinguished.

**Recommendation:**

- avoid `using namespace std;` in canonical complete programs and headers;
- label intentional raw-memory examples and immediately show their RAII production counterpart;
- use `std::mt19937` and distributions for normal examples, reserving `rand`/`srand` for legacy comparison;
- use `nullptr` in live modern code;
- reserve `malloc`/`free` for C interoperability or allocator education;
- qualify standard names and include every directly used header;
- enforce the policy first in extracted/verified examples, then migrate illustrative snippets by module.

### Fence labels need normalization

There are 1,047 unlabeled fences. Many are diagrams or output, but without `text`, `console`, `mermaid`, `cpp`, or `pseudocode` labels, renderers and verification tools cannot reliably classify them.

**Recommendation:** Label every fence and reject new unlabeled fences in CI. Do not infer that every unlabeled block is C++.

### Link checking is narrower than the curriculum needs

The current checker reports zero broken local paths, which is good. It does not establish that fragment anchors, image references, or external sources are valid.

**Recommendation:** Extend it to check local heading fragments and images deterministically. Check external URLs in a separate non-blocking or cached job to avoid making ordinary CI depend on network stability.

## Recommended Work Order

Work should proceed in this exact sequence so that later cleanup is built on trustworthy material:

1. Repair `04_algorithm.md` and the five confirmed code/complexity issues.
2. Add a Markdown structure check for balanced and labeled fences.
3. Consolidate BFS/DFS and the remaining OOP/exception/string overlaps.
4. Define the lesson metadata contract and canonical topic IDs.
5. Build the extraction/compiler manifest and validate the first core batch.
6. Split the largest core sorting and standard-container lessons while preserving links.
7. Add canonical dynamic-array and hash-table-internals lessons by relocating reusable material rather than duplicating it.
8. Add the three missing applied-pattern lessons.
9. Implement and test the first Stage 9 project.
10. Normalize titles, sources, exercise/solution separation, claims, and modern style across the remaining modules.
11. Add optional advanced topics only after the verified core path is complete.

## Definition of “Complete Path”

The C++/DSA path should be called complete only when all of the following are true:

- every learning-path stage links to actual canonical lessons in a deliberate order;
- every canonical topic has exactly one owner, with other pages linking or applying rather than reteaching it;
- every lesson declares prerequisites, level, language standard, and verification status;
- every core implementation compiles with extensions disabled on GCC, Clang, and MSVC;
- every core data structure has invariant-focused mutation tests;
- every core algorithm has normal, boundary, invalid/precondition, and adversarial tests where relevant;
- complexity tables separate preprocessing, operation time, auxiliary space, and total storage;
- graph lessons declare directedness, weight rules, disconnected behavior, overflow policy, and output contract;
- exercises can be attempted without immediately revealing solutions;
- all local paths, anchors, images, and navigation indexes pass automated checks;
- “verified” and similar claims are generated from evidence rather than written manually;
- at least one multi-file project demonstrates build structure, testing, debugging, ownership, and algorithm integration.

## Final Assessment

The collection has enough raw content to become an unusually deep C++ and DSA curriculum. Its remaining problem is editorial and engineering discipline: too many independently written examples, too little executable evidence, and several topic boundaries that are still porous.

The most effective strategy is to stop measuring progress by file count. Measure it by canonical topics with explicit prerequisites, compiled examples, tested invariants, accurate complexity contracts, and a single clear next step. Once the Priority 0 defects, semantic duplicates, and verification pipeline are handled, the remaining content additions are small and well defined.
