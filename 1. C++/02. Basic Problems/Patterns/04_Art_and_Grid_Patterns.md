# Art and Grid-Traversal Patterns

These exercises combine several predicates or require a traversal order. Solve them only after simple solid and hollow boundaries.

## Predicate-Based Exercises

1. plus sign through the center row and column;
2. `X` through both diagonals;
3. butterfly made from mirrored triangles;
4. hourglass made from two inverted pyramids;
5. checkerboard using `(row + column) % 2`;
6. zigzag using a periodic row/column rule;
7. heart outline or filled heart from a documented coordinate equation.

## Traversal Exercises

1. Fill an `N x N` matrix in clockwise spiral order.
2. Print concentric square layers.
3. Fill rows in alternating left-to-right and right-to-left order.
4. Print cells by Manhattan distance from a chosen center.

Spiral filling is a boundary-shrinking traversal, not merely a printing trick. Maintain four boundaries—`top`, `bottom`, `left`, and `right`—and shrink a boundary after traversing its edge. Recheck boundary validity before traversing the opposite edge; this matters for non-square and single-row inputs.

## Scope and Cultural Context

Prefer neutral geometric names for exercises. If reproducing a symbol with religious, political, or historical meanings, explain why it is included and avoid presenting it as context-free decoration.

## Tests

- sizes 1 and 2;
- odd and even dimensions;
- rectangular matrices such as `1 x 4`, `4 x 1`, and `3 x 5`;
- exact expected output for one small case;
- every spiral value appears once and stays within bounds.

## Next Step

Continue to [Mathematical Patterns](05_Mathematical_Patterns.md).
