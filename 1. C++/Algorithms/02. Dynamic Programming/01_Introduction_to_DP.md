# Introduction to Dynamic Programming in C++: Foundations, Invariants & Paradigms

## 1. Executive Overview & Theoretical Foundations

**Dynamic Programming (DP)** is a mathematical optimization method and algorithmic paradigm that solves complex problems by decomposing them into a collection of simpler subproblems, solving each subproblem exactly once, and storing their solutions in a memory structure (table or cache).

Coined by Richard Bellman in the 1950s, the word *"programming"* refers to tabular mathematical planning rather than writing computer code.

Dynamic Programming is fundamentally applicable when a problem exhibits two critical properties:
1. **Optimal Substructure**: An optimal solution to the overall problem can be constructed from optimal solutions to its constituent subproblems. (Governed by **Bellman's Principle of Optimality**).
2. **Overlapping Subproblems**: The recursive decomposition of the problem revisits the identical subproblems repeatedly, rather than generating new subproblems at every branch.

```
                  NAIVE RECURSION                         DYNAMIC PROGRAMMING
             (Exponential Call Tree)                       (State-Space DAG)

                     fib(5)                                      fib(5)
                   /        \                                      │
              fib(4)        fib(3)                               fib(4)
             /      \       /    \                                 │
          fib(3)   fib(2) fib(2) fib(1)                          fib(3)
          /    \   /    \                                          │
       fib(2) fib(1)...  ...                                     fib(2)
       /    \                                                      │
    fib(1) fib(0)                                                fib(1)
                                                                   │
   Operations: O(2^N) Redundant Recomputations                  fib(0)
                                                    Operations: O(N) Subproblems Solved Once
```

---

## 2. Paradigms: Top-Down vs. Bottom-Up vs. Space Optimization

| Metric | Top-Down (Memoization) | Bottom-Up (Tabulation) | Space-Optimized Tabulation |
| :--- | :--- | :--- | :--- |
| **Execution Direction** | Target State $\to$ Base Cases | Base Cases $\to$ Target State | Base Cases $\to$ Target State |
| **Control Flow** | Recursion + Function Call Stack | Iterative Loops | Iterative Loops |
| **Memory Allocation** | Heap/Stack Cache + $O(N)$ Recursion Frames | Table/Array $O(N)$ | $O(1)$ Primitive Registers |
| **Subproblem Evaluation** | Lazy (solves only reachable states) | Eager (evaluates entire table) | Eager (retains only active frontiers) |
| **Overhead** | Stack frame push/pop overhead | Cache-friendly sequential memory | Maximum CPU register & cache utilization |

---

## 3. Production-Grade C++ Implementation Suite

The following implementation contrasts all dynamic programming approaches alongside an $O(\log N)$ Matrix Exponentiation solution and an exact profiling harness:

```cpp
#include <iostream>
#include <vector>
#include <ctime>
#include <cassert>
#include <iomanip>

class DynamicProgrammingFoundations {
public:
    // -------------------------------------------------------------
    // 1. Naive Recursion with Call Counter (Demonstrating O(2^N))
    // -------------------------------------------------------------
    static long long naiveFib(int n, unsigned long long& callCount) {
        callCount++;
        if (n <= 0) return 0;
        if (n == 1) return 1;
        return naiveFib(n - 1, callCount) + naiveFib(n - 2, callCount);
    }

    // -------------------------------------------------------------
    // 2. Top-Down DP (Memoization) - O(N) Time, O(N) Space
    // -------------------------------------------------------------
    static long long memoizedFib(int n, std::vector<long long>& memo, unsigned long long& callCount) {
        callCount++;
        if (n <= 0) return 0;
        if (n == 1) return 1;
        if (memo[n] != -1) return memo[n];

        memo[n] = memoizedFib(n - 1, memo, callCount) + memoizedFib(n - 2, memo, callCount);
        return memo[n];
    }

    static long long solveMemoized(int n, unsigned long long& callCount) {
        if (n <= 0) return 0;
        std::vector<long long> memo(n + 1, -1);
        return memoizedFib(n, memo, callCount);
    }

    // -------------------------------------------------------------
    // 3. Bottom-Up DP (Tabulation) - O(N) Time, O(N) Space
    // -------------------------------------------------------------
    static long long tabulatedFib(int n) {
        if (n <= 0) return 0;
        if (n == 1) return 1;

        std::vector<long long> dp(n + 1, 0);
        dp[0] = 0;
        dp[1] = 1;

        for (int i = 2; i <= n; ++i) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }

    // -------------------------------------------------------------
    // 4. Space-Optimized Tabulation - O(N) Time, O(1) Auxiliary Space
    // -------------------------------------------------------------
    static long long spaceOptimizedFib(int n) {
        if (n <= 0) return 0;
        if (n == 1) return 1;

        long long prev2 = 0;
        long long prev1 = 1;
        long long current = 0;

        for (int i = 2; i <= n; ++i) {
            current = prev1 + prev2;
            prev2 = prev1;
            prev1 = current;
        }
        return current;
    }

    // -------------------------------------------------------------
    // 5. Matrix Exponentiation - O(log N) Time, O(1) Auxiliary Space
    //    [ F(n+1)  F(n)   ] = [ 1  1 ]^n
    //    [ F(n)    F(n-1) ]   [ 1  0 ]
    // -------------------------------------------------------------
    struct Matrix2x2 {
        long long m[2][2];
        Matrix2x2() {
            m[0][0] = 1; m[0][1] = 1;
            m[1][0] = 1; m[1][1] = 0;
        }
        static Matrix2x2 identity() {
            Matrix2x2 res;
            res.m[0][0] = 1; res.m[0][1] = 0;
            res.m[1][0] = 0; res.m[1][1] = 1;
            return res;
        }
        Matrix2x2 operator*(const Matrix2x2& o) const {
            Matrix2x2 res;
            for (int r = 0; r < 2; ++r) {
                for (int c = 0; c < 2; ++c) {
                    res.m[r][c] = m[r][0] * o.m[0][c] + m[r][1] * o.m[1][c];
                }
            }
            return res;
        }
    };

    static long long logarithmicFib(int n) {
        if (n <= 0) return 0;
        if (n == 1) return 1;

        Matrix2x2 base;
        Matrix2x2 result = Matrix2x2::identity();
        int power = n - 1;

        while (power > 0) {
            if (power & 1) {
                result = result * base;
            }
            base = base * base;
            power >>= 1;
        }
        return result.m[0][0];
    }
};

int main() {
    std::cout << "==============================================================\n";
    std::cout << "       DYNAMIC PROGRAMMING FOUNDATIONS AND PROFILING HARNESS  \n";
    std::cout << "==============================================================\n";

    // 1. Correctness Verification across all variants
    for (int n = 0; n <= 40; ++n) {
        unsigned long long memoCalls = 0;
        long long valMemo = DynamicProgrammingFoundations::solveMemoized(n, memoCalls);
        long long valTab  = DynamicProgrammingFoundations::tabulatedFib(n);
        long long valOpt  = DynamicProgrammingFoundations::spaceOptimizedFib(n);
        long long valLog  = DynamicProgrammingFoundations::logarithmicFib(n);

        assert(valMemo == valTab);
        assert(valTab == valOpt);
        assert(valOpt == valLog);
    }
    std::cout << ">> Invariant Verification PASSED for all n in [0, 40].\n\n";

    // 2. Call Stack Comparison: Naive vs Memoized
    int testN = 30;
    unsigned long long naiveCalls = 0;
    unsigned long long memoCalls = 0;

    clock_t t1 = clock();
    long long ansNaive = DynamicProgrammingFoundations::naiveFib(testN, naiveCalls);
    clock_t t2 = clock();

    long long ansMemo = DynamicProgrammingFoundations::solveMemoized(testN, memoCalls);
    clock_t t3 = clock();

    long long ansOpt = DynamicProgrammingFoundations::spaceOptimizedFib(testN);
    clock_t t4 = clock();

    long long ansLog = DynamicProgrammingFoundations::logarithmicFib(testN);
    clock_t t5 = clock();

    (void)ansMemo;
    (void)ansOpt;
    (void)ansLog;

    double naiveDuration = double(t2 - t1) * 1000.0 / CLOCKS_PER_SEC;
    double memoDuration  = double(t3 - t2) * 1000.0 / CLOCKS_PER_SEC;
    double optDuration   = double(t4 - t3) * 1000.0 / CLOCKS_PER_SEC;
    double logDuration   = double(t5 - t4) * 1000.0 / CLOCKS_PER_SEC;

    std::cout << "Results for Fibonacci(" << testN << ") = " << ansNaive << ":\n";
    std::cout << "--------------------------------------------------------------\n";
    std::cout << "1. Naive Recursive:   Calls = " << std::setw(10) << naiveCalls 
              << " | Time = " << std::fixed << std::setprecision(3) << naiveDuration << " ms (O(2^N))\n";
    std::cout << "2. Memoized (TopDown): Calls = " << std::setw(10) << memoCalls 
              << " | Time = " << std::fixed << std::setprecision(3) << memoDuration  << " ms (O(N))\n";
    std::cout << "3. Space Optimized:   Loops = " << std::setw(10) << testN 
              << " | Time = " << std::fixed << std::setprecision(3) << optDuration   << " ms (O(N) time, O(1) space)\n";
    std::cout << "4. Matrix Exponent:   Mults = " << std::setw(10) << 5 
              << " | Time = " << std::fixed << std::setprecision(3) << logDuration   << " ms (O(log N))\n";
    std::cout << "--------------------------------------------------------------\n";
    std::cout << "Call reduction ratio: " << (naiveCalls / (double)memoCalls) << "x fewer invocations!\n";

    return 0;
}
```

---

## 4. Complexity Analysis & Invariant Formulations

| Approach | Time Complexity | Auxiliary Space | Call Stack Depth | Invariant Preserved |
| :--- | :---: | :---: | :---: | :--- |
| **Naive Recursion** | $O(2^N)$ | $O(N)$ stack | $N$ | Tree evaluation identity |
| **Memoization (Top-Down)** | $O(N)$ | $O(N)$ heap $+ O(N)$ stack | $N$ | Subproblem result cached at most once |
| **Tabulation (Bottom-Up)** | $O(N)$ | $O(N)$ heap | $O(1)$ | $dp[i]$ contains true optimum for size $i$ |
| **Space-Optimized Tabulation** | $O(N)$ | $O(1)$ | $O(1)$ | $\{prev2, prev1\} = \{F(i-2), F(i-1)\}$ |
| **Matrix Exponentiation** | $O(\log N)$ | $O(1)$ | $O(1)$ | Group associative exponent multiplication |

---

## 5. Diagnostic Decision Tree: When to Apply DP

```
                      Does the problem ask for:
          - Optimal value (Min / Max / Shortest / Longest)?
          - Counting combinations (Number of ways)?
          - Feasibility (Can reach / Is partitionable)?
                                │
                                ▼
                               Yes
                                │
               Can it be divided into subproblems?
                                │
                                ▼
                               Yes
                                │
               Do the subproblems repeat/overlap?
                ├── No  ──► Use Divide and Conquer (Merge Sort, Binary Search)
                └── Yes
                     │
         Does local greed guarantee global optimum?
          (Can an exchange argument prove local choice?)
                ├── Yes ──► Use Greedy Algorithm (Huffman, Dijkstra, Kruskal)
                └── No  ──► Dynamic Programming is REQUIRED
```

---

## Next Step

- Proceed to [02_Memoization.md](02_Memoization.md) to explore formal top-down memoization data structures and cache eviction policies.
