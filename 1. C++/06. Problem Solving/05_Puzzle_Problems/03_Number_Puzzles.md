# Number Puzzles in C++ - Number Theory, Recursion, and State Reachability

## 1. Introduction & Theoretical Foundations

**Number puzzles** combine discrete mathematics, number theory, and recursive invariants. Unlike naive brute-force arithmetic, these problems leverage structural properties such as modular arithmetic, Bézout's identity, cycle detection, and binary representation.

This module delivers comprehensive theoretical analyses and production-ready C++ implementations for the 4 classical number puzzles:
1. **Tower of Hanoi** (Recursive Divide & Conquer and Bitwise Iterative Execution)
2. **The Josephus Problem** (Modular Recurrence and $O(1)$ Power-of-Two Bitwise Solution)
3. **The Water Jug Problem** (Bézout's Identity & BFS Shortest-Path State Reachability)
4. **Happy Number Detection** (Sum-of-Squares and Floyd's Cycle-Finding Algorithm)

---

## 2. Puzzle 1: Tower of Hanoi

### Problem Statement
Given 3 rods labeled **Source** ($A$), **Auxiliary** ($B$), and **Target** ($C$), move $N$ disks from $A$ to $C$ subject to:
1. Only one disk may be moved at a time.
2. Each move takes the upper disk from one stack and places it on top of another rod.
3. No larger disk may be placed atop a smaller disk.

```
         |                 |                 |
        ===                |                 |
       =====               |                 |
      =======              |                 |
   ───┴─────┴───       ───┴─────┴───       ───┴─────┴───
     Source (A)        Auxiliary (B)        Target (C)
```

### Recurrence & Mathematical Proof
To move $n$ disks from $A$ to $C$ using $B$:
1. Recursively move $n - 1$ disks from $A$ to $B$ ($T(n - 1)$ moves).
2. Move disk $n$ directly from $A$ to $C$ ($1$ move).
3. Recursively move $n - 1$ disks from $B$ to $C$ ($T(n - 1)$ moves).

$$T(n) = 2T(n - 1) + 1, \quad T(1) = 1$$
Solving by expansion:
$$T(n) = 2^n - 1$$

### Iterative Bitwise Pattern
For move $m$ ($1 \le m \le 2^n - 1$):
- The disk to move is determined by the position of the lowest set bit in $m$: $\text{disk} = \text{ctz}(m) + 1$.
- Even-numbered disks and odd-numbered disks alternate cycles between rods in deterministic rotational directions.

### C++ Implementation: Tower of Hanoi

```cpp
#include <iostream>
#include <vector>
#include <string>

class TowerOfHanoi {
public:
    // Classic Recursive Solution: O(2^N) time, O(N) call stack
    static void solveRecursive(int n, char fromRod, char toRod, char auxRod, 
                               std::vector<std::string>& moves) {
        if (n == 0) return;
        // Step 1: Move top n-1 disks from Source to Auxiliary
        solveRecursive(n - 1, fromRod, auxRod, toRod, moves);
        
        // Step 2: Move the nth disk from Source to Target
        moves.push_back("Move disk " + std::to_string(n) + " from " + fromRod + " to " + toRod);
        
        // Step 3: Move top n-1 disks from Auxiliary to Target
        solveRecursive(n - 1, auxRod, toRod, fromRod, moves);
    }

    // Iterative Bitwise Solution: Demonstrating ctz (count trailing zeros)
    static void solveIterative(int n, std::vector<std::string>& moves) {
        int totalMoves = (1 << n) - 1;
        char rods[3] = {'A', 'B', 'C'};
        
        // For even n, target and aux swap rotational directions
        if (n % 2 == 0) std::swap(rods[1], rods[2]);

        for (int m = 1; m <= totalMoves; ++m) {
            int disk = __builtin_ctz(m) + 1;
            int fromIdx = (m & (m - 1)) % 3;
            int toIdx = ((m | (m - 1)) + 1) % 3;
            moves.push_back("Move disk " + std::to_string(disk) + " from " + 
                            rods[fromIdx] + " to " + rods[toIdx]);
        }
    }
};
```

---

## 3. Puzzle 2: The Josephus Problem

### Problem Statement
$N$ people stand in a circle numbered $0$ to $N - 1$. Starting from person $0$, counting proceeds around the circle. In each step, every $k$-th person is eliminated until exactly one person survives. Find the position of the survivor.

### Mathematical Formulation

#### General Recurrence ($O(N)$ Time)
Let $J(n, k)$ be the $0$-indexed position of the survivor in a circle of $n$ people:
- After the first person is eliminated (at index $(k - 1) \bmod n$), the circle shrinks to $n - 1$ people.
- The next count starts at index $k \bmod n$.
- Shifting the subproblem back to the original index frame yields the recurrence:
$$J(n, k) = (J(n - 1, k) + k) \bmod n, \quad J(1, k) = 0$$

#### Closed-Form Solution for $k = 2$ ($O(1)$ Time)
When every 2nd person is eliminated ($k = 2$), let $N = 2^m + L$ where $2^m$ is the largest power of 2 less than or equal to $N$, and $0 \le L < 2^m$.
The survivor is:
$$J(N, 2) = 2L + 1 \quad \text{(1-indexed)}$$
In binary, this is equivalent to a **circular 1-bit left rotation** of $N$!

### C++ Implementation: Josephus Problem

```cpp
#include <iostream>

class JosephusSolver {
public:
    // General Iterative: O(N) time, O(1) space (0-indexed return)
    static int solveGeneral(int n, int k) {
        int survivor = 0; // Base case: J(1, k) = 0
        for (int i = 2; i <= n; ++i) {
            survivor = (survivor + k) % i;
        }
        return survivor; // 0-indexed
    }

    // Special Case k = 2: O(1) bitwise circular rotation
    static int solveK2Bitwise(int n) {
        // Find highest set bit: 2^floor(log2(n))
        int highestPowerOf2 = 1;
        while ((highestPowerOf2 << 1) <= n) {
            highestPowerOf2 <<= 1;
        }
        int l = n - highestPowerOf2;
        return (2 * l) + 1; // 1-indexed
    }
};
```

---

## 4. Puzzle 3: The Water Jug Problem

### Problem Statement
Given two jugs of capacities $M$ and $N$ liters ($M, N \in \mathbb{Z}^+$) and an infinite water supply, measure exactly $D$ liters.
Allowed operations:
1. Fill either jug completely to capacity.
2. Empty either jug completely.
3. Pour water from one jug into the other until either the donor is empty or the receiver is full.

### Number Theory Condition: Bézout's Identity
By Bézout's Identity, any sequence of pours and fills results in a total volume that is a linear combination of $M$ and $N$:
$$a \cdot M + b \cdot N = D \quad (a, b \in \mathbb{Z})$$
**Theorem:** $D$ liters can be measured if and only if:
1. $D \le \max(M, N)$
2. $D \bmod \gcd(M, N) == 0$

### Shortest-Path BFS Implementation
We model the two jugs as an unweighted directed state graph $(j_1, j_2)$ where $0 \le j_1 \le M$ and $0 \le j_2 \le N$. Breadth-First Search (BFS) finds the minimum number of steps to reach any state with $j_1 = D$ or $j_2 = D$.

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <string>
#include <numeric>

struct JugState {
    int j1, j2;
    int steps;
    std::string action;
};

class WaterJugBFS {
private:
    static int gcd(int a, int b) {
        while (b) {
            a %= b;
            std::swap(a, b);
        }
        return a;
    }

public:
    static bool isSolvable(int m, int n, int d) {
        if (d > std::max(m, n)) return false;
        return (d % gcd(m, n) == 0);
    }

    static int minStepsBFS(int cap1, int cap2, int target, std::vector<std::string>& pathLog) {
        if (!isSolvable(cap1, cap2, target)) return -1;

        // Visited set using pair encoding
        std::set<std::pair<int, int>> visited;
        std::queue<JugState> q;

        q.push({0, 0, 0, "Initial State (0, 0)"});
        visited.insert({0, 0});

        while (!q.empty()) {
            JugState curr = q.front();
            q.pop();

            if (curr.j1 == target || curr.j2 == target) {
                pathLog.push_back(curr.action);
                return curr.steps;
            }

            // Generate all 6 possible next states:
            std::vector<JugState> nextStates = {
                {cap1, curr.j2, curr.steps + 1, "Fill Jug 1"},                           // Fill 1
                {curr.j1, cap2, curr.steps + 1, "Fill Jug 2"},                           // Fill 2
                {0, curr.j2, curr.steps + 1, "Empty Jug 1"},                             // Empty 1
                {curr.j1, 0, curr.steps + 1, "Empty Jug 2"},                             // Empty 2
                // Pour 1 -> 2
                {curr.j1 - std::min(curr.j1, cap2 - curr.j2), 
                 curr.j2 + std::min(curr.j1, cap2 - curr.j2), curr.steps + 1, "Pour Jug 1 -> Jug 2"},
                // Pour 2 -> 1
                {curr.j1 + std::min(curr.j2, cap1 - curr.j1), 
                 curr.j2 - std::min(curr.j2, cap1 - curr.j1), curr.steps + 1, "Pour Jug 2 -> Jug 1"}
            };

            for (const auto& next : nextStates) {
                if (!visited.count({next.j1, next.j2})) {
                    visited.insert({next.j1, next.j2});
                    q.push(next);
                }
            }
        }
        return -1;
    }
};
```

---

## 5. Puzzle 4: Happy Number Detection

### Problem Statement
A **happy number** is defined by the following process:
1. Starting with any positive integer, replace the number by the sum of the squares of its digits.
2. Repeat the process until the number equals $1$ (where it stays), or it **loops endlessly in a cycle** which does not include $1$.
3. Those numbers for which this process ends in $1$ are happy.

### Cycle Detection: Floyd's Tortoise and Hare
Because the sum of squares of digits of any 32-bit integer is strictly bounded (e.g., $999{,}999{,}999 \to 9^2 \cdot 9 = 729$), the sequence must either reach $1$ or enter a closed cycle.

Rather than allocating an $O(N)$ hash set to remember visited numbers, **Floyd's Cycle-Finding Algorithm** runs two pointers:
- `slow` advances $1$ step at a time: `slow = getNext(slow)`
- `fast` advances $2$ steps at a time: `fast = getNext(getNext(fast))`
If a cycle exists, `slow` and `fast` will inevitably collide in $O(\text{cycle length})$ time with **$O(1)$ auxiliary space**.

### C++ Implementation: Happy Number

```cpp
#include <iostream>

class HappyNumberSolver {
public:
    static int getNext(int n) {
        int sum = 0;
        while (n > 0) {
            int digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        return sum;
    }

    // Floyd's Cycle Detection: O(log N) time, O(1) space
    static bool isHappy(int n) {
        int slow = n;
        int fast = getNext(n);

        while (fast != 1 && slow != fast) {
            slow = getNext(slow);
            fast = getNext(getNext(fast));
        }

        return fast == 1;
    }
};
```

---

## 6. Complete Runnable Verification Suite

```cpp
#include <iostream>
#include <vector>

int main() {
    std::cout << "=====================================================" << std::endl;
    std::cout << "           NUMBER PUZZLES ALGORITHMIC SUITE          " << std::endl;
    std::cout << "=====================================================" << std::endl;

    // --- 1. Tower of Hanoi (N = 3) ---
    std::cout << "\n[1] TOWER OF HANOI (N = 3 Disks):" << std::endl;
    std::vector<std::string> hanoiMoves;
    TowerOfHanoi::solveRecursive(3, 'A', 'C', 'B', hanoiMoves);
    std::cout << "  Total moves: " << hanoiMoves.size() << " (Expected: 2^3 - 1 = 7)" << std::endl;
    for (const auto& move : hanoiMoves) {
        std::cout << "    " << move << std::endl;
    }

    // --- 2. Josephus Problem ---
    std::cout << "\n[2] JOSEPHUS PROBLEM (N = 7, K = 3):" << std::endl;
    int survivorGeneral = JosephusSolver::solveGeneral(7, 3);
    std::cout << "  Survivor index (0-indexed): " << survivorGeneral 
              << " (1-indexed: " << survivorGeneral + 1 << ")" << std::endl;

    std::cout << "  Josephus Special Case (N = 10, K = 2):" << std::endl;
    int survivorK2 = JosephusSolver::solveK2Bitwise(10);
    std::cout << "  Survivor index (1-indexed): " << survivorK2 << " (Expected: 5)" << std::endl;

    // --- 3. Water Jug Problem ---
    std::cout << "\n[3] WATER JUG PROBLEM (Capacities: 4L and 3L, Target: 2L):" << std::endl;
    std::vector<std::string> jugPath;
    int minSteps = WaterJugBFS::minStepsBFS(4, 3, 2, jugPath);
    std::cout << "  Solvable: " << (WaterJugBFS::isSolvable(4, 3, 2) ? "YES" : "NO") << std::endl;
    std::cout << "  Minimum steps needed: " << minSteps << std::endl;

    // --- 4. Happy Number Detection ---
    std::cout << "\n[4] HAPPY NUMBER DETECTION:" << std::endl;
    std::vector<int> testNums = {19, 2, 7, 20};
    for (int num : testNums) {
        std::cout << "  Number " << num << " is " 
                  << (HappyNumberSolver::isHappy(num) ? "HAPPY :)" : "UNHAPPY :(") 
                  << std::endl;
    }

    std::cout << "\n=====================================================" << std::endl;
    return 0;
}
```

---

## 7. Complexity Analysis Table

| Number Puzzle | Algorithm Technique | Time Complexity | Auxiliary Space | Mathematical Invariant |
| :--- | :--- | :--- | :--- | :--- |
| **Tower of Hanoi** | Divide & Conquer | $O(2^N)$ | $O(N)$ stack / $O(1)$ iterative | $T(N) = 2^N - 1$ |
| **Josephus (General)** | Modular Recurrence | $O(N)$ | $O(1)$ | $J(n, k) = (J(n-1, k) + k) \bmod n$ |
| **Josephus ($K = 2$)** | Binary Cyclic Shift | $O(1)$ | $O(1)$ | $2(N - 2^{\lfloor \log_2 N \rfloor}) + 1$ |
| **Water Jug Problem** | State-Space BFS | $O(M \cdot N)$ | $O(M \cdot N)$ | Bézout: $d \bmod \gcd(m, n) == 0$ |
| **Happy Number** | Floyd's Cycle Finding | $O(\log N)$ | $O(1)$ | Bounded sum of squares $\le 729$ |

---

## 8. Common Pitfalls & Interview Traps

1. **Josephus 0-Based vs. 1-Based Indexing**: Recurrence formulas apply to $0$-indexed representations. Always convert to 1-based indexing for output by adding $1$ at the final step.
2. **Water Jug Solvability Guard**: Running BFS on unsolvable states ($D \bmod \gcd(M, N) \ne 0$) without an initial check traverses the entire $(M+1) \times (N+1)$ space before failing. Always apply Bézout's identity first.
3. **Happy Number Hash Table Memory Overhead**: Using `std::unordered_set<int>` consumes unnecessary dynamic memory and is slower than Floyd's two-pointer cycle detection.

---

## Next Step

- Proceed to [04_Array_Puzzles.md](04_Array_Puzzles.md) to master 2D Spiral Traversals, Trapping Rain Water, and Median of Sorted Arrays.
