# Pattern Puzzles in C++ - Cellular Automata, Fractals, and Matrix Geometry

## 1. Introduction & Theoretical Foundations

**Pattern puzzles** require identifying underlying mathematical symmetries, spatial invariants, and recursive self-similarity. They span a rich continuum from coordinate arithmetic (printing concentric geometric shapes) to recursive fractal generation (Sierpinski triangles) and complex emergent behavior in zero-player cellular automata (Conway's Game of Life).

This module delivers exhaustive theory, coordinate transformations, and production-ready C++ implementations for:
1. **Conway's Game of Life** (Cellular Automata with In-Place Bit-State Optimization)
2. **Sierpinski Triangle Generator** (Recursive Decomposition & Pascal's Triangle Modulo 2)
3. **Concentric Number Spirals & Zigzag Matrices** (Manhattan Distance Metric & Boundary Logic)

---

## 2. Puzzle 1: Conway's Game of Life

### Problem Statement
Given an $M \times N$ grid of cells, each either **live** ($1$) or **dead** ($0$), compute the next generation following Conway's 4 fundamental rules:
1. **Underpopulation**: Any live cell with fewer than 2 live neighbors dies.
2. **Survival**: Any live cell with 2 or 3 live neighbors lives on to the next generation.
3. **Overpopulation**: Any live cell with more than 3 live neighbors dies.
4. **Reproduction**: Any dead cell with exactly 3 live neighbors becomes a live cell.

All transitions happen simultaneously at each discrete time step.

```
       Underpopulation         Survival             Reproduction
          [ ][Live][ ]        [Live][Live][ ]         [Live][ ][Live]
          [ ][Live][ ]   -->  [Live][Live][ ]    -->  [ ][Dead][ ]  --> [Live]
          [ ][ ][ ]           [ ][ ][ ]               [ ][Live][ ]
```

### In-Place 2-Bit State Encoding ($O(1)$ Space)
Normally, simultaneous updates require an $O(M \cdot N)$ auxiliary matrix. However, since cell states only require 1 bit ($0$ or $1$), we can encode the **current** and **next** states into the 2 least significant bits of an integer:
- Bit 0 (`cell & 1`): Current state.
- Bit 1 (`(cell >> 1) & 1`): Next state.

| Transition (Old $\to$ New) | Binary Encoding | Decimal Value |
| :--- | :---: | :---: |
| $0 \to 0$ (Dead remains Dead) | `00` | 0 |
| $1 \to 0$ (Live becomes Dead) | `01` | 1 |
| $0 \to 1$ (Dead becomes Live) | `10` | 2 |
| $1 \to 1$ (Live remains Live) | `11` | 3 |

### C++ Implementation: Conway's Game of Life

```cpp
#include <iostream>
#include <vector>
#include <string>

class GameOfLife {
private:
    int rows;
    int cols;
    std::vector<std::vector<int>> grid;

    // Count live neighbors using the lowest bit (current state)
    int countLiveNeighbors(int r, int c) const {
        int count = 0;
        for (int dr = -1; dr <= 1; ++dr) {
            for (int dc = -1; dc <= 1; ++dc) {
                if (dr == 0 && dc == 0) continue;
                int nr = r + dr;
                int nc = c + dc;
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols) {
                    count += (grid[nr][nc] & 1); // Extract bit 0
                }
            }
        }
        return count;
    }

public:
    GameOfLife(const std::vector<std::vector<int>>& initialGrid)
        : rows(initialGrid.size()), cols(initialGrid[0].size()), grid(initialGrid) {}

    // Computes next generation in O(M * N) time and O(1) auxiliary space
    void step() {
        // Pass 1: Compute next state and encode into bit 1
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                int liveNeighbors = countLiveNeighbors(r, c);
                bool isAlive = (grid[r][c] & 1);

                if (isAlive) {
                    if (liveNeighbors == 2 || liveNeighbors == 3) {
                        grid[r][c] |= 2; // Set bit 1: live in next state (11 in binary = 3)
                    }
                } else {
                    if (liveNeighbors == 3) {
                        grid[r][c] |= 2; // Set bit 1: born in next state (10 in binary = 2)
                    }
                }
            }
        }

        // Pass 2: Shift bit 1 to bit 0 to transition to next generation
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                grid[r][c] >>= 1;
            }
        }
    }

    void display(const std::string& title = "") const {
        if (!title.empty()) std::cout << "--- " << title << " ---" << std::endl;
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                std::cout << (grid[r][c] ? "# " : ". ");
            }
            std::cout << "\n";
        }
    }

    const std::vector<std::vector<int>>& getGrid() const { return grid; }
};
```

---

## 3. Puzzle 2: Sierpinski Triangle Generator

### Problem Statement
The **Sierpinski Triangle** is a mathematically fractal pattern with self-similarity across infinite scales. 
At level $K$, the canvas has dimensions $2^K \times (2^{K+1} - 1)$. 

```
Level 1:        Level 2:
   /\              /\
  /__\            /__\
                 /\  /\
                /__\/__\
```

### Mathematical Approaches

#### Approach A: Recursive Subdivision (Top-Down)
To draw a triangle of height $h$ rooted at $(r, c)$:
1. If $h = 1$, draw:
   - Line 0: `/ \`
   - Line 1: `/__\`
2. Else, recursively draw:
   - Top triangle of height $h/2$ at $(r, c)$.
   - Left triangle of height $h/2$ at $(r + h/2, c - h/2)$.
   - Right triangle of height $h/2$ at $(r + h/2, c + h/2)$.

#### Approach B: Lucas' Theorem & Pascal's Triangle Modulo 2
An entry in Pascal's triangle $\binom{n}{k}$ is odd if and only if the binary representation of $k$ is a sub-mask of $n$ (`(n & k) == k`). Plotting odd values of Pascal's triangle directly generates a Sierpinski triangle in $O(N^2)$ bitwise operations!

### C++ Implementation: Sierpinski Canvas Generator

```cpp
#include <iostream>
#include <vector>
#include <string>

class SierpinskiFractal {
public:
    // Generates recursive ASCII Sierpinski Triangle of order k
    static std::vector<std::string> generateRecursive(int order) {
        if (order <= 0) return {};
        
        int height = 1 << order; // 2^order
        int width = (height << 1); // 2^(order + 1)
        std::vector<std::string> canvas(height, std::string(width, ' '));

        auto drawTriangle = [&](auto& self, int h, int r, int c) -> void {
            if (h == 2) {
                // Base triangle of height 2
                canvas[r][c] = '/';
                canvas[r][c + 1] = '\\';
                canvas[r + 1][c - 1] = '/';
                canvas[r + 1][c] = '_';
                canvas[r + 1][c + 1] = '_';
                canvas[r + 1][c + 2] = '\\';
                return;
            }

            int half = h / 2;
            // Top triangle
            self(self, half, r, c);
            // Bottom-left triangle
            self(self, half, r + half, c - half);
            // Bottom-right triangle
            self(self, half, r + half, c + half);
        };

        drawTriangle(drawTriangle, height, 0, height - 1);
        return canvas;
    }

    // Generates Sierpinski Triangle via Pascal's Triangle Modulo 2
    static std::vector<std::string> generateBitwise(int rows) {
        std::vector<std::string> canvas(rows, std::string(2 * rows, ' '));
        for (int n = 0; n < rows; ++n) {
            for (int k = 0; k <= n; ++k) {
                // Lucas Theorem: C(n, k) is odd iff (n & k) == k
                if ((n & k) == k) {
                    canvas[n][rows - n + 2 * k] = '*';
                }
            }
        }
        return canvas;
    }
};
```

---

## 4. Puzzle 3: Concentric Number Spirals & Matrix Geometry

### Problem Statement
Generate an $N \times N$ matrix composed of concentric square number rings where the outermost boundary consists of $N$, the next ring consists of $N-1$, descending inwards to $1$ at the center.

For $N = 4$ (matrix dimensions $7 \times 7$, size $2N - 1$):
```
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
```

### Mathematical Coordinate Transformation
For a grid of size $S = 2N - 1$ indexed from $0$ to $S - 1$:
The distance from cell $(r, c)$ to the nearest matrix border is:
$$\text{dist}(r, c) = \min(r, c, S - 1 - r, S - 1 - c)$$

Since the border has value $N$, the value at any coordinate $(r, c)$ is computed in **$O(1)$ time without auxiliary matrices**:
$$\text{val}(r, c) = N - \text{dist}(r, c)$$

### C++ Implementation: Concentric & Spiral Number Patterns

```cpp
#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

class MatrixPatterns {
public:
    // Generates concentric square rings in O(N^2) time and O(1) extra space
    static std::vector<std::vector<int>> generateConcentricRings(int n) {
        int size = 2 * n - 1;
        std::vector<std::vector<int>> matrix(size, std::vector<int>(size));

        for (int r = 0; r < size; ++r) {
            for (int c = 0; c < size; ++c) {
                int distToBorder = std::min({r, c, size - 1 - r, size - 1 - c});
                matrix[r][c] = n - distToBorder;
            }
        }
        return matrix;
    }

    // Generates 1 to N^2 spiral matrix in-place
    static std::vector<std::vector<int>> generateSpiralMatrix(int n) {
        std::vector<std::vector<int>> matrix(n, std::vector<int>(n));
        int top = 0, bottom = n - 1, left = 0, right = n - 1;
        int val = 1;

        while (top <= bottom && left <= right) {
            for (int c = left; c <= right; ++c) matrix[top][c] = val++;
            top++;

            for (int r = top; r <= bottom; ++r) matrix[r][right] = val++;
            right--;

            if (top <= bottom) {
                for (int c = right; c >= left; --c) matrix[bottom][c] = val++;
                bottom--;
            }

            if (left <= right) {
                for (int r = bottom; r >= top; --r) matrix[r][left] = val++;
                left++;
            }
        }
        return matrix;
    }
};
```

---

## 5. Complete Runnable Verification Suite

```cpp
#include <iostream>
#include <vector>
#include <iomanip>

int main() {
    std::cout << "=====================================================" << std::endl;
    std::cout << "          PATTERN PUZZLES ALGORITHMIC SUITE          " << std::endl;
    std::cout << "=====================================================" << std::endl;

    // --- 1. Conway's Game of Life (Blinker Oscillator & Glider) ---
    std::cout << "\n[1] CONWAY'S GAME OF LIFE (Blinker Oscillator 3x3):" << std::endl;
    std::vector<std::vector<int>> blinker = {
        {0, 1, 0},
        {0, 1, 0},
        {0, 1, 0}
    };
    GameOfLife gol(blinker);
    gol.display("Generation 0");
    gol.step();
    gol.display("Generation 1 (Horizontal)");
    gol.step();
    gol.display("Generation 2 (Vertical)");

    // --- 2. Sierpinski Triangle Fractal (Order 2) ---
    std::cout << "\n[2] SIERPINSKI TRIANGLE FRACTAL (Order 2):" << std::endl;
    auto triangle = SierpinskiFractal::generateRecursive(2);
    for (const auto& line : triangle) {
        std::cout << line << "\n";
    }

    // --- 3. Concentric Number Rings (N = 3) ---
    std::cout << "\n[3] CONCENTRIC NUMBER RINGS (N = 3):" << std::endl;
    auto rings = MatrixPatterns::generateConcentricRings(3);
    for (const auto& row : rings) {
        for (int v : row) std::cout << v << " ";
        std::cout << "\n";
    }

    // --- 4. Spiral Matrix (N = 3) ---
    std::cout << "\n[4] SPIRAL MATRIX (N = 3):" << std::endl;
    auto spiral = MatrixPatterns::generateSpiralMatrix(3);
    for (const auto& row : spiral) {
        for (int v : row) std::cout << std::setw(2) << v << " ";
        std::cout << "\n";
    }

    std::cout << "\n=====================================================" << std::endl;
    return 0;
}
```

---

## 6. Complexity Analysis Table

| Pattern Puzzle | Algorithm Technique | Time Complexity | Auxiliary Space | Key Mechanics |
| :--- | :--- | :--- | :--- | :--- |
| **Game of Life** | 2-Bit State Encoding | $O(M \cdot N)$ | $O(1)$ | Bit 0: current state, Bit 1: next state |
| **Sierpinski (Recursive)** | Divide & Conquer Canvas | $O(3^K)$ triangles | $O(2^K \cdot 2^{K+1})$ | 3-way recursive quadrant delegation |
| **Sierpinski (Lucas)** | Pascal's Triangle Mod 2 | $O(N^2)$ | $O(1)$ | Sub-mask test `(n & k) == k` |
| **Concentric Rings** | Manhattan Boundary Math | $O(N^2)$ | $O(1)$ | $\min(r, c, S-1-r, S-1-c)$ |
| **Spiral Matrix** | 4-Boundary Pointers | $O(N^2)$ | $O(1)$ | $top, bottom, left, right$ contraction |

---

## 7. Common Pitfalls & Interview Traps

1. **Game of Life Asynchronous Mutation**: Modifying array values during neighbor scanning destroys the neighbor counts for subsequent cells. Use bit-encoding (`val |= 2`) or double-buffering.
2. **Sierpinski Canvas Allocation**: Forgetting that an ASCII triangle of height $H$ requires width $2H$ to accommodate symmetric diagonal slashes.
3. **Spiral Matrix Single Row/Column Edge Cases**: In rectangular spiral matrices ($M \ne N$), failing to re-check `top <= bottom` and `left <= right` before the bottom and left sweeps results in duplicate element processing.

---

## Next Step

- Proceed to [03_Number_Puzzles.md](03_Number_Puzzles.md) to explore the Tower of Hanoi, Josephus problem, and cycle detection in C++.
