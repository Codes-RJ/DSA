# Stars and Hollow Shapes

> **Prerequisite:** [Grid Reasoning](01_Grid_Reasoning.md)

## Solid Shapes

Derive and implement these in order:

1. left-aligned right triangle;
2. right-aligned right triangle;
3. inverted versions of both triangles;
4. centered pyramid;
5. inverted centered pyramid;
6. solid diamond made from two pyramids.

For a centered pyramid with one-based row `r`, a common model is:

- leading spaces: `N - r`;
- foreground width: `2r - 1`.

Do not memorize the loops. Verify those two formulas against a drawing.

## Hollow Shapes

A hollow shape prints only its boundary. Begin with the corresponding solid region, then identify boundary conditions.

For a hollow left triangle with one-based row `r` and column `c`, print when:

- `c == 1` for the left edge;
- `c == r` for the diagonal edge;
- `r == N` for the bottom edge.

Apply the same method to a hollow square, pyramid, inverted pyramid, diamond, and hourglass.

## Design Exercises

1. Accept the foreground character as a parameter.
2. Return a string without trailing spaces on any line.
3. Produce identical visible output with zero-based and one-based formulas.
4. Extract a helper that appends a repeated character safely.
5. State how many visible foreground characters each shape emits.

## Common Failures

- Treating the two halves of a diamond as if both contain the middle row.
- Printing a base edge on every row of a hollow triangle.
- Mixing logical columns with terminal character positions when spaces are inserted between symbols.
- Assuming `size == 1` has multiple distinct edges.
- Calling an `O(N^2)` renderer inefficient when its output contains `Theta(N^2)` characters.

## Next Step

Continue to [Numbers and Letters](03_Numbers_and_Letters.md).
