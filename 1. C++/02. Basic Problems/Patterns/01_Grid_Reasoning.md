# Grid Reasoning for Pattern Problems

> **Minimum standard:** C++17

## The Coordinate Model

Treat the output as a rectangular grid. For each cell `(row, column)`, decide whether it contains a foreground character, a number or letter, or a space.

| Relationship | Zero-based condition |
|---|---|
| Main diagonal | `row == column` |
| Anti-diagonal in an `N x N` grid | `row + column == N - 1` |
| Top edge | `row == 0` |
| Bottom edge | `row == N - 1` |
| Left edge | `column == 0` |
| Right edge | `column == N - 1` |
| Lower triangle | `column <= row` |
| Upper triangle | `column >= row` |
| Manhattan ring | `abs(row - center) + abs(column - center) == radius` |

## A Testable Renderer

```cpp
#include <functional>
#include <stdexcept>
#include <string>

using CellRule = std::function<bool(int, int, int)>;

std::string render_square(int size, const CellRule& foreground) {
    if (size <= 0) {
        throw std::invalid_argument("size must be positive");
    }

    std::string output;
    for (int row = 0; row < size; ++row) {
        for (int column = 0; column < size; ++column) {
            output += foreground(row, column, size) ? '*' : ' ';
        }
        output += '\n';
    }
    return output;
}
```

Example rule for an `X`:

```cpp
const auto x_rule = [](int row, int column, int size) {
    return row == column || row + column == size - 1;
};
```

## Derivation Checklist

1. Draw sizes 1, 2, 3, and 4.
2. Label row and column indexes.
3. Identify the first and last foreground column in each row.
4. Convert those boundaries into formulas.
5. Decide whether spaces after the final visible character are required.
6. Test the exact string, including newlines.

## Exercises

1. Render the main diagonal.
2. Render both diagonals.
3. Render only the border of a square.
4. Render the lower triangle.
5. Generalize the renderer to different width and height.

## Next Step

Continue to [Stars and Hollow Shapes](02_Stars_and_Hollow_Shapes.md).
