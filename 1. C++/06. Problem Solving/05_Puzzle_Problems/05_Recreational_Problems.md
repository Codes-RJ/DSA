# Recreational Problems in C++ - Heuristics, Matching Theory, and Combinatorics

## 1. Introduction & Theoretical Foundations

**Recreational mathematics and computer science problems** demonstrate algorithmic brilliance by solving seemingly intractable combinatorial search spaces with elegant mathematical heuristics and greedy invariants. Problems that would require millions of years via naive exhaustive search can often be solved in milliseconds once the underlying structural topology is exploited.

This module delivers comprehensive theoretical analyses and production-ready C++ implementations for:
1. **The Knight's Tour Problem** (Backtracking Enhanced by Warnsdorff's Heuristic)
2. **The Gale-Shapley Stable Marriage Algorithm** (Deferred Acceptance & Matching Invariants)
3. **Magic Square Generator** (The Siamese Method for Odd-Order Matrices)

---

## 2. Problem 1: The Knight's Tour (Warnsdorff's Algorithm)

### Problem Statement
A knight is placed on an empty $N \times N$ chessboard. Moving according to standard chess rules (an L-shape: 2 squares in one dimension, 1 square in the orthogonal dimension), the knight must visit **every single square on the board exactly once**.

```
                           (r-2, c-1)     (r-2, c+1)
                                ▲             ▲
                                │             │
                    (r-1, c-2) ◄───         ───► (r-1, c+2)
                                      Knight
                    (r+1, c-2) ◄───   [r, c]  ───► (r+1, c+2)
                                │             │
                                ▼             ▼
                           (r+2, c-1)     (r+2, c+1)
```

### The Complexity Dilemma: Why Pure Backtracking Fails
On an $8 \times 8$ board, there are $64$ moves. Each square has up to 8 moves, leading to a state-space of approximately $8^{64} \approx 6.27 \times 10^{57}$ states. Pure depth-first search easily gets trapped in deep exponential dead ends, taking centuries to terminate.

### Warnsdorff's Degree Heuristic
In 1823, H. C. von Warnsdorff proposed an inspired greedy heuristic:
> **Always move the knight to an adjacent unvisited square from which the knight will have the FEWEST onward available moves (minimum degree).**

By prioritizing squares with the fewest exits (such as corners and edges), the knight prevents creating isolated inaccessible "islands" that would ruin the tour later. With Warnsdorff's heuristic, the solution is found in **linear time $O(N^2)$** with near-zero backtracking!

### C++ Implementation: Knight's Tour

```cpp
#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

class KnightsTour {
private:
    static bool isValid(int x, int y, int n, const std::vector<std::vector<int>>& board) {
        return (x >= 0 && x < n && y >= 0 && y < n && board[x][y] == -1);
    }

    // Count available onward moves from (x, y)
    static int getDegree(int x, int y, int n, const std::vector<std::vector<int>>& board) {
        const int dx[8] = {-2, -1, 1, 2,  2,  1, -1, -2};
        const int dy[8] = { 1,  2, 2, 1, -1, -2, -2, -1};
        int degree = 0;
        for (int i = 0; i < 8; ++i) {
            if (isValid(x + dx[i], y + dy[i], n, board)) {
                degree++;
            }
        }
        return degree;
    }

public:
    static bool solveWarnsdorff(int n, int startX, int startY, std::vector<std::vector<int>>& board) {
        const int dx[8] = {-2, -1, 1, 2,  2,  1, -1, -2};
        const int dy[8] = { 1,  2, 2, 1, -1, -2, -2, -1};
        board.assign(n, std::vector<int>(n, -1));

        int currX = startX;
        int currY = startY;
        board[currX][currY] = 1; // Move 1

        for (int move = 2; move <= n * n; ++move) {
            int minDeg = 9;
            int nextX = -1, nextY = -1;

            // Examine all 8 neighbors and select the one with minimal degree
            for (int i = 0; i < 8; ++i) {
                int nx = currX + dx[i];
                int ny = currY + dy[i];

                if (isValid(nx, ny, n, board)) {
                    int deg = getDegree(nx, ny, n, board);
                    if (deg < minDeg) {
                        minDeg = deg;
                        nextX = nx;
                        nextY = ny;
                    }
                }
            }

            if (nextX == -1) {
                return false; // Dead end reached
            }

            currX = nextX;
            currY = nextY;
            board[currX][currY] = move;
        }
        return true;
    }
};
```

---

## 3. Problem 2: Gale-Shapley Stable Marriage Algorithm

### Problem Statement
Given $N$ men and $N$ women, where each person has strictly ranked all members of the opposite sex by preference, match them into $N$ heterosexual couples such that the matching is **stable**.

A matching is **unstable** if there exists a **blocking pair** $(M, W)$ where:
1. $M$ prefers $W$ over his assigned partner.
2. $W$ prefers $M$ over her assigned partner.
If such a pair exists, they have an incentive to abandon their partners and pair with each other.

### Algorithmic Mechanics (Deferred Acceptance)
In each round:
1. Every unengaged man proposes to the highest-ranked woman on his list to whom he has not yet proposed.
2. Each woman tentatively accepts the proposal from the man she likes best among her current partner and new suitors, rejecting the rest.
3. Terminate when all men are engaged.

**Guarantees:**
- The algorithm always terminates in at most $N^2$ proposals.
- The resulting matching is guaranteed to be **stable**.
- The result is **male-optimal** (each man receives the best partner possible across all stable matchings) and **female-pessimal**.

### C++ Implementation: Gale-Shapley Algorithm

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

class StableMarriage {
public:
    // menPref[m] is vector of women ranked by preference
    // womenPref[w] is vector of men ranked by preference
    static std::vector<int> match(int n, 
                                  const std::vector<std::vector<int>>& menPref,
                                  const std::vector<std::vector<int>>& womenPref) {
        // womenRanking[w][m] = rank of man m for woman w (lower rank = more preferred)
        std::vector<std::vector<int>> womenRanking(n, std::vector<int>(n, 0));
        for (int w = 0; w < n; ++w) {
            for (int rank = 0; rank < n; ++rank) {
                int m = womenPref[w][rank];
                womenRanking[w][m] = rank;
            }
        }

        std::vector<int> womenPartner(n, -1); // Current partner of woman w
        std::vector<int> menPartner(n, -1);   // Partner of man m
        std::vector<int> nextProposal(n, 0);  // Index of next woman to propose to for man m
        std::queue<int> freeMen;

        for (int m = 0; m < n; ++m) freeMen.push(m);

        while (!freeMen.empty()) {
            int m = freeMen.front();
            freeMen.pop();

            int w = menPref[m][nextProposal[m]++];

            if (womenPartner[w] == -1) {
                // Woman is free; accept proposal tentatively
                womenPartner[w] = m;
                menPartner[m] = w;
            } else {
                int currentM = womenPartner[w];
                // Check if woman prefers new suitor m over current partner
                if (womenRanking[w][m] < womenRanking[w][currentM]) {
                    // Woman dumps currentM for m
                    womenPartner[w] = m;
                    menPartner[m] = w;
                    menPartner[currentM] = -1;
                    freeMen.push(currentM); // Previous partner becomes free
                } else {
                    // Proposal rejected; man remains free
                    freeMen.push(m);
                }
            }
        }

        return menPartner; // menPartner[m] = assigned woman w
    }
};
```

---

## 4. Problem 3: Magic Square Generator (The Siamese Method)

### Problem Statement
An $N \times N$ **magic square** is an arrangement of distinct integers from $1$ to $N^2$ such that the sum of the numbers in each row, each column, and both main diagonals is identical:
$$M = \frac{N(N^2 + 1)}{2}$$

For $N = 3$, $M = \frac{3(9 + 1)}{2} = 15$:
```
       8   1   6   ──► 15
       3   5   7   ──► 15
       4   9   2   ──► 15
       │   │   │
       ▼   ▼   ▼
      15  15  15
```

### The Siamese Method (de la Loubère) for Odd $N$
For any odd integer $N \ge 3$:
1. Place $1$ in the middle cell of the first row: $(0, \lfloor N/2 \rfloor)$.
2. Successively place numbers $k = 2, 3, \dots, N^2$ by moving **one step up and one step right** $(r - 1, c + 1)$:
   - If a move falls off the top border ($r < 0$), wrap around to the bottom row ($r = N - 1$).
   - If a move falls off the right border ($c \ge N$), wrap around to the first column ($c = 0$).
   - If the candidate cell is **already occupied** or if the previous number was in the top-right corner, place the number directly **below** the previous position: $(r + 1, c)$.

### C++ Implementation: Magic Square Generator

```cpp
#include <iostream>
#include <vector>
#include <iomanip>

class MagicSquare {
public:
    // Generates odd-order magic square in O(N^2) time and O(1) auxiliary space
    static std::vector<std::vector<int>> generateOdd(int n) {
        if (n % 2 == 0) throw std::invalid_argument("Siamese method requires an odd order.");

        std::vector<std::vector<int>> square(n, std::vector<int>(n, 0));
        int r = 0;
        int c = n / 2;

        for (int val = 1; val <= n * n; ++val) {
            square[r][c] = val;

            int nextR = (r - 1 + n) % n;
            int nextC = (c + 1) % n;

            if (square[nextR][nextC] != 0) {
                // Cell occupied: move down from original position
                r = (r + 1) % n;
            } else {
                r = nextR;
                c = nextC;
            }
        }
        return square;
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
    std::cout << "        RECREATIONAL PUZZLES ALGORITHMIC SUITE       " << std::endl;
    std::cout << "=====================================================" << std::endl;

    // --- 1. Knight's Tour on 8x8 Board ---
    std::cout << "\n[1] KNIGHT'S TOUR (8x8 Board with Warnsdorff's Heuristic):" << std::endl;
    std::vector<std::vector<int>> board;
    bool success = KnightsTour::solveWarnsdorff(8, 0, 0, board);
    if (success) {
        std::cout << "  Tour completed successfully! Board step sequence:\n";
        for (int r = 0; r < 8; ++r) {
            std::cout << "  ";
            for (int c = 0; c < 8; ++c) {
                std::cout << std::setw(3) << board[r][c] << " ";
            }
            std::cout << "\n";
        }
    } else {
        std::cout << "  Tour failed to complete.\n";
    }

    // --- 2. Gale-Shapley Stable Marriage (N = 3) ---
    std::cout << "\n[2] GALE-SHAPLEY STABLE MARRIAGE (3 Men, 3 Women):" << std::endl;
    // Men's preference lists (ranked highest to lowest)
    std::vector<std::vector<int>> menPref = {
        {0, 1, 2}, // Man 0 prefers W0 > W1 > W2
        {1, 0, 2}, // Man 1 prefers W1 > W0 > W2
        {0, 1, 2}  // Man 2 prefers W0 > W1 > W2
    };
    // Women's preference lists
    std::vector<std::vector<int>> womenPref = {
        {1, 0, 2}, // Woman 0 prefers M1 > M0 > M2
        {0, 1, 2}, // Woman 1 prefers M0 > M1 > M2
        {0, 1, 2}  // Woman 2 prefers M0 > M1 > M2
    };
    auto matches = StableMarriage::match(3, menPref, womenPref);
    for (int m = 0; m < 3; ++m) {
        std::cout << "  Man " << m << " is stably married to Woman " << matches[m] << std::endl;
    }

    // --- 3. Magic Square of Order 3 ---
    std::cout << "\n[3] MAGIC SQUARE GENERATION (Order N = 3):" << std::endl;
    auto magic = MagicSquare::generateOdd(3);
    int magicConstant = 3 * (3 * 3 + 1) / 2;
    std::cout << "  Magic Constant M = " << magicConstant << "\n";
    for (const auto& row : magic) {
        std::cout << "  ";
        for (int v : row) std::cout << std::setw(2) << v << " ";
        std::cout << "\n";
    }

    std::cout << "\n=====================================================" << std::endl;
    return 0;
}
```

---

## 6. Complexity Analysis Table

| Recreational Problem | Algorithm Technique | Time Complexity | Auxiliary Space | Key Invariant |
| :--- | :--- | :--- | :--- | :--- |
| **Knight's Tour** | Warnsdorff Heuristic | $O(N^2)$ average | $O(N^2)$ board | Minimum degree selection avoids isolates |
| **Stable Marriage** | Gale-Shapley Deferred | $O(N^2)$ | $O(N^2)$ rank table | No blocking pairs; monotonically improving women |
| **Magic Square** | Siamese Up-Right Walk | $O(N^2)$ | $O(1)$ extra | Row/col wrap with collision down-step |

---

## 7. Common Pitfalls & Interview Traps

1. **Warnsdorff Tie-Breaking**: On large boards ($N > 12$), tie-breaking between multiple squares with the same minimum degree can lead to dead ends without backtracking. Random or secondary degree tie-breaking (degree of next moves) resolves this.
2. **Stable Marriage Lookup Inefficiency**: Linearly scanning a woman's preference list to see if she prefers suitor $M$ over her current partner takes $O(N)$ per proposal, inflating total time to $O(N^3)$. Precomputing an inverted rank matrix (`womenRanking[w][m]`) ensures $O(1)$ comparisons and $O(N^2)$ overall time.
3. **Magic Square Parity Violation**: The Siamese method only works for **odd** orders ($N = 3, 5, 7, \dots$). Even orders require doubly-even cross-out methods ($4k$) or Strachey methods ($4k+2$).

---

## Next Step

- Proceed to [README.md](README.md) for the complete Problem Solving curriculum overview.
