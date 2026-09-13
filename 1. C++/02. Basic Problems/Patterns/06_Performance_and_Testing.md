# Pattern Performance and Testing

## Output-Sensitive Analysis

Let `K` be the number of emitted characters, including necessary spaces and separators. Any renderer must perform at least `Omega(K)` output work. A square `N x N` pattern therefore has an `Omega(N^2)` output-size lower bound even if its foreground predicate is constant time.

Distinguish:

- logical cell evaluations;
- characters appended to an in-memory buffer;
- calls made to the output stream;
- auxiliary memory retained at one time.

## Buffer Before Printing

Build a string or use stream in memory, then write it in one operation. This makes testing deterministic and avoids one formatted I/O call per cell.

```cpp
#include <ostream>
#include <string>

void print_pattern(std::ostream& output, const std::string& pattern) {
    output << pattern;
}
```

Do not call an implementation “optimized” without measurements. Replacing two clear loops with one loop does not change `Theta(N^2)` work and may make boundary reasoning harder.

## Exact-Output Tests

Test returned strings directly:

```cpp
#include <cassert>
#include <string>

void test_size_two_square() {
    const std::string expected = "**\n**\n";
    assert(render_solid_square(2) == expected);
}
```

Also test:

- invalid sizes;
- `size == 1`;
- odd and even centers;
- absence or documented presence of trailing spaces;
- one larger input for accidental cubic behavior;
- numeric overflow boundaries for sequence-based output.

## Completion Exercise

Design one generic renderer and use it for a border, `X`, plus sign, and checkerboard. Keep each shape-specific rule under five lines and give each case an exact-output test.

## Next Step

Attempt the module exercises, then compare your decisions with [Reference Solutions](Reference_Solutions.md). Continue afterward to [Searching](../Search/README.md).
