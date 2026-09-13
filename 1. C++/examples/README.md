# Verified Curriculum Examples

This directory contains small canonical C++17 implementations extracted from the curriculum's main stages. Unlike illustrative Markdown fragments, these files are compiled with warnings enabled and exercised by CTest.

| Curriculum stage | Tested example |
|---|---|
| Standard library | [`word_frequencies.hpp`](include/dsa/word_frequencies.hpp) |
| Language basics | [`prime.hpp`](include/dsa/prime.hpp) |
| Basic problems | [`merge_sort.hpp`](include/dsa/merge_sort.hpp) |
| Object-oriented design | [`score_board.hpp`](include/dsa/score_board.hpp) |
| Data structures | [`disjoint_set_union.hpp`](include/dsa/disjoint_set_union.hpp) |
| Trees and graphs | [`binary_search_tree.hpp`](include/dsa/binary_search_tree.hpp) |
| Problem solving | [`bit_count.hpp`](include/dsa/bit_count.hpp) |
| Algorithms | [`dijkstra.hpp`](include/dsa/dijkstra.hpp) |

## Build and Test

```text
cmake -S . -B build -DBUILD_TESTING=ON
cmake --build build --config Release
ctest --test-dir build --output-on-failure -C Release
```

Run these commands from `1. C++`. On GCC or Clang, add `-DDSA_ENABLE_SANITIZERS=ON` for a sanitizer build.

## Status Convention

- A page may call code **verified** only when its canonical source is built here or by another automated target.
- Markdown-only fragments remain **illustrative**.
- Each extracted example should have normal, boundary, and invalid-input tests where its interface admits invalid input.
