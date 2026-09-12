# Master Theorem: Mathematical Analysis, Extended Cases & C++ Recurrence Engine

## 1. Executive Overview & Theoretical Foundations

In algorithm analysis, the **Master Theorem** provides a closed-form asymptotic solution ($\Theta$-notation) for divide-and-conquer recurrence relations of the form:

$$T(N) = a \cdot T\left(\frac{N}{b}\right) + f(N)$$

where:
- $N$: Problem size.
- $a \ge 1$: Number of recursive subproblems generated per step.
- $b > 1$: Shrink factor by which each subproblem size decreases.
- $f(N)$: Non-recursive computational cost to partition the problem and merge/combine the subproblem solutions.

### The Critical Exponent ($\mathbf{c_{crit}}$)
The asymptotic behavior is governed by the comparison between the leaf-level work and the root-level division/combination work. The number of leaves in the recursion tree is:
$$\text{Leaves} = a^{\log_b N} = N^{\log_b a}$$
Thus, the critical exponent is defined as:
$$c_{crit} = \log_b a$$

```
                          RECURSION TREE GEOMETRY
   Level 0:                         f(N)                     ──► Cost: f(N)
                                  /  |  \  (a branches)
   Level 1:                 f(N/b) f(N/b) f(N/b)             ──► Cost: a * f(N/b)
                            / | \  / | \  / | \
   Level 2:               .....................              ──► Cost: a^2 * f(N/b^2)
   ...                             ...
   Level log_b(N):     Θ(1) Θ(1) Θ(1) ... Θ(1) Θ(1)          ──► Cost: N^(log_b a) * Θ(1)
                      └────────────────────────────┘
                         Total Leaves = N^(log_b a)
```

---

## 2. The Three Classical Cases (and Extended Case 2)

Assume $f(N) = \Theta(N^d \log^k N)$ with $k \ge 0$:

| Case | Mathematical Condition | Dominant Factor | Asymptotic Complexity $T(N)$ | Canonical Algorithm |
| :--- | :--- | :--- | :---: | :--- |
| **Case 1** | $f(N) = O(N^{\log_b a - \epsilon})$ for $\epsilon > 0$ ($d < \log_b a$) | **Leaves Dominate** (Bottom-heavy) | $\Theta(N^{\log_b a})$ | Karatsuba ($a=3, b=2$), Strassen ($a=7, b=2$) |
| **Case 2** | $f(N) = \Theta(N^{\log_b a} \log^k N)$ ($d = \log_b a$) | **Balanced Across All Levels** | $\Theta(N^{\log_b a} \log^{k+1} N)$ | Merge Sort ($a=2, b=2, k=0 \implies \Theta(N \log N)$) |
| **Case 3** | $f(N) = \Omega(N^{\log_b a + \epsilon})$ for $\epsilon > 0$ ($d > \log_b a$)<br>and satisfies **Regularity**: $a f(N/b) \le c f(N)$ for $c < 1$ | **Root Dominates** (Top-heavy) | $\Theta(f(N))$ | Quickselect average case, $T(N) = 2T(N/2) + N^2$ |

---

## 3. Production-Grade C++ Implementation Suite

The following C++ engine provides an analytical Master Theorem Classifier alongside an **Empirical Recurrence Simulator** that measures recursive operation counts across power-of-two problem sizes:

```cpp
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <cassert>
#include <iomanip>

class MasterTheoremEngine {
public:
    struct AnalysisResult {
        int caseNumber;
        double log_b_a;
        std::string complexityFormula;
        std::string explanation;
    };

    // Solves recurrence: T(N) = a * T(N / b) + Theta(N^d * log^k(N))
    static AnalysisResult solve(double a, double b, double d, int k = 0) {
        assert(a >= 1.0 && "Parameter 'a' must be >= 1");
        assert(b > 1.0 && "Parameter 'b' must be > 1");
        assert(k >= 0 && "Parameter 'k' must be >= 0");

        double log_b_a = std::log(a) / std::log(b);
        double epsilon = 1e-6;

        AnalysisResult res;
        res.log_b_a = log_b_a;

        if (d < log_b_a - epsilon) {
            // Case 1: Leaves dominate
            res.caseNumber = 1;
            std::ostringstream ss;
            ss << "Theta(N^" << std::fixed << std::setprecision(2) << log_b_a << ")";
            res.complexityFormula = ss.str();
            res.explanation = "Case 1: Work is dominated by the leaf nodes (Bottom-Heavy).";
        } else if (std::abs(d - log_b_a) <= epsilon) {
            // Case 2: Balanced work across levels
            res.caseNumber = 2;
            std::ostringstream ss;
            if (std::abs(d) < epsilon) {
                // d = 0 (e.g., Binary Search: T(N) = T(N/2) + 1 -> Theta(log^(k+1) N))
                if (k + 1 == 1) ss << "Theta(log N)";
                else ss << "Theta(log^" << (k + 1) << " N)";
            } else if (std::abs(d - 1.0) < epsilon) {
                // d = 1 (e.g., Merge Sort: T(N) = 2T(N/2) + N -> Theta(N log^(k+1) N))
                if (k + 1 == 1) ss << "Theta(N log N)";
                else ss << "Theta(N log^" << (k + 1) << " N)";
            } else {
                ss << "Theta(N^" << std::fixed << std::setprecision(2) << d << " * log^" << (k + 1) << " N)";
            }
            res.complexityFormula = ss.str();
            res.explanation = "Case 2: Work is evenly distributed across all tree levels.";
        } else {
            // Case 3: Root dominates
            res.caseNumber = 3;
            std::ostringstream ss;
            if (k == 0) {
                if (std::abs(d - 1.0) < epsilon) ss << "Theta(N)";
                else if (std::abs(d - 2.0) < epsilon) ss << "Theta(N^2)";
                else ss << "Theta(N^" << std::fixed << std::setprecision(2) << d << ")";
            } else {
                ss << "Theta(N^" << std::fixed << std::setprecision(2) << d << " * log^" << k << " N)";
            }
            res.complexityFormula = ss.str();
            res.explanation = "Case 3: Work is dominated by the root combine step (Top-Heavy).";
        }
        return res;
    }

    // -------------------------------------------------------------------------
    // Empirical Simulator: Directly counts recursive steps & combine operations
    // -------------------------------------------------------------------------
    static unsigned long long simulateWork(int n, int a, int b, double d, int k) {
        if (n <= 1) return 1;

        unsigned long long localCombineWork = 0;
        double polyTerm = std::pow((double)n, d);
        double logTerm = (k > 0) ? std::pow(std::log2((double)n), (double)k) : 1.0;
        localCombineWork = (unsigned long long)(polyTerm * logTerm);
        if (localCombineWork == 0) localCombineWork = 1;

        unsigned long long subproblemWork = 0;
        for (int i = 0; i < a; ++i) {
            subproblemWork += simulateWork(n / b, a, b, d, k);
        }

        return localCombineWork + subproblemWork;
    }
};

int main() {
    std::cout << "==============================================================\n";
    std::cout << "        MASTER THEOREM ANALYZER & SIMULATION ENGINE           \n";
    std::cout << "==============================================================\n";

    // Benchmark 1: Binary Search: T(N) = 1*T(N/2) + Theta(1) (a=1, b=2, d=0, k=0)
    auto bs = MasterTheoremEngine::solve(1, 2, 0, 0);
    assert(bs.caseNumber == 2);
    assert(bs.complexityFormula == "Theta(log N)");
    std::cout << "1. Binary Search:        T(N) = T(N/2) + 1       -> " 
              << bs.complexityFormula << " [Case " << bs.caseNumber << "] - PASSED\n";

    // Benchmark 2: Merge Sort: T(N) = 2*T(N/2) + Theta(N) (a=2, b=2, d=1, k=0)
    auto ms = MasterTheoremEngine::solve(2, 2, 1, 0);
    assert(ms.caseNumber == 2);
    assert(ms.complexityFormula == "Theta(N log N)");
    std::cout << "2. Merge Sort:           T(N) = 2T(N/2) + N      -> " 
              << ms.complexityFormula << " [Case " << ms.caseNumber << "] - PASSED\n";

    // Benchmark 3: Karatsuba Multiplication: T(N) = 3*T(N/2) + Theta(N) (a=3, b=2, d=1)
    auto km = MasterTheoremEngine::solve(3, 2, 1, 0);
    assert(km.caseNumber == 1);
    assert(std::abs(km.log_b_a - 1.585) < 0.01);
    std::cout << "3. Karatsuba Algorithm:  T(N) = 3T(N/2) + N      -> " 
              << km.complexityFormula << " [Case " << km.caseNumber << "] - PASSED\n";

    // Benchmark 4: Strassen Matrix Multiply: T(N) = 7*T(N/2) + Theta(N^2) (a=7, b=2, d=2)
    auto sm = MasterTheoremEngine::solve(7, 2, 2, 0);
    assert(sm.caseNumber == 1);
    assert(std::abs(sm.log_b_a - 2.807) < 0.01);
    std::cout << "4. Strassen Multiply:    T(N) = 7T(N/2) + N^2    -> " 
              << sm.complexityFormula << " [Case " << sm.caseNumber << "] - PASSED\n";

    // Benchmark 5: Top-Heavy Recurrence: T(N) = 2*T(N/2) + Theta(N^2) (a=2, b=2, d=2)
    auto th = MasterTheoremEngine::solve(2, 2, 2, 0);
    assert(th.caseNumber == 3);
    assert(th.complexityFormula == "Theta(N^2)");
    std::cout << "5. Top-Heavy Recurrence: T(N) = 2T(N/2) + N^2    -> " 
              << th.complexityFormula << " [Case " << th.caseNumber << "] - PASSED\n";

    // -------------------------------------------------------------------------
    // Empirical Verification of Scaling: Merge Sort T(N) = 2T(N/2) + N
    // -------------------------------------------------------------------------
    std::cout << "\n--- Empirical Recurrence Scaling for Merge Sort ---\n";
    std::vector<int> testSizes = {64, 128, 256, 512, 1024};
    std::cout << std::setw(8) << "N" 
              << std::setw(16) << "Simulated Ops" 
              << std::setw(16) << "N * log2(N)" 
              << std::setw(16) << "Ratio (Ops / Ref)\n";

    for (int n : testSizes) {
        unsigned long long ops = MasterTheoremEngine::simulateWork(n, 2, 2, 1.0, 0);
        double ref = n * std::log2((double)n);
        std::cout << std::setw(8) << n 
                  << std::setw(16) << ops 
                  << std::setw(16) << (unsigned long long)ref 
                  << std::setw(16) << std::fixed << std::setprecision(2) << (ops / ref) << "\n";
    }

    std::cout << "\n=== All Master Theorem Solver & Simulation Tests Verified! ===\n";
    return 0;
}
```

---

## 4. Limitations: When the Master Theorem Cannot Be Applied

The Master Theorem is powerful, but fails when recurrences violate its structural constraints:

1. **Non-Polynomial Gap ($\epsilon$ non-constant)**:
   - Example: $T(N) = 2T(N/2) + N / \log N$.
   - Here $f(N) = N / \log N$ is asymptotically smaller than $N^{\log_2 2} = N$, but not by a polynomial factor $N^\epsilon$. The Master Theorem does not apply (solved via recursion trees to $\Theta(N \log \log N)$).
2. **Variable Subproblem Sizes**:
   - Example: $T(N) = T(N/3) + T(2N/3) + N$ (requires the **Akra-Bazzi Theorem**).
3. **Non-Constant $a$ or $b$**:
   - Example: $T(N) = N \cdot T(N/2) + N$ (branching factor grows with $N$).
4. **Regularity Violation in Case 3**:
   - When $a f(N/b) \le c f(N)$ fails for all $c < 1$ (e.g., oscillating functions like $f(N) = N^2 (2 + \sin N)$).

---

## Next Step

- Proceed to [16_Recurrence_Relations.md](16_Recurrence_Relations.md) to study general substitution methods, characteristic equations, and Akra-Bazzi extensions for asymmetric subproblems.
