# Pattern Exercises

Pattern printing is short practice for loop boundaries, coordinate reasoning, decomposition, and output testing. It is not a DSA topic by itself, so this module is intentionally bounded.

## Study Order

1. [Grid reasoning](01_Grid_Reasoning.md)
2. [Stars and hollow shapes](02_Stars_and_Hollow_Shapes.md)
3. [Numbers and letters](03_Numbers_and_Letters.md)
4. [Art and grid traversals](04_Art_and_Grid_Patterns.md)
5. [Mathematical patterns](05_Mathematical_Patterns.md)
6. [Performance and testing](06_Performance_and_Testing.md)
7. [Reference solutions](Reference_Solutions.md) — open only after attempting the exercises

## Required Workflow

- Number rows and columns from zero unless a formula is clearer with one-based indexes.
- Write a predicate `should_print(row, column, size)` before formatting output.
- Return a `std::string` from practice functions so exact output can be tested.
- Reject or define non-positive sizes rather than relying on accidental loop behavior.
- Separate shape logic from the character used to render it.

## Completion Target

Complete at least two solid shapes, two hollow shapes, two number patterns, one traversal pattern, and one mathematical pattern without viewing the references. Then explain the time cost in terms of both input size and characters emitted.

## Next Step

Start with [Grid Reasoning](01_Grid_Reasoning.md).
