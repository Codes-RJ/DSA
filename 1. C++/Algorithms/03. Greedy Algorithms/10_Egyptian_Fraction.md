# Egyptian Fraction Algorithm (Greedy Approach)

## 📖 Overview

An **Egyptian Fraction** is the representation of a positive fraction as a sum of distinct unit fractions (fractions with a numerator of 1), such as:
$$\frac{4}{7} = \frac{1}{2} + \frac{1}{14}$$

The ancient Egyptians expressed all rational numbers (except $2/3$) in this form. In computer science and discrete mathematics, finding an Egyptian fraction decomposition is a classical demonstration of the **Greedy Choice Property**: at each step, we greedily select the largest possible unit fraction that is strictly less than or equal to the remaining fraction.

---

## 🎯 The Fibonacci-Sylvester Greedy Algorithm

Given an irreducible fraction $\frac{p}{q}$ ($p < q$):

```
                       Input Fraction: p / q
                                 │
                     Find smallest ceiling n:
                        n = ceil(q / p)
                                 │
                    Greedily append: + 1 / n
                                 │
                     Compute new remainder:
                     p' / q' = (p * n - q) / (q * n)
                                 │
                     Reduce remainder via GCD
                                 │
                     Is p' == 0? ───YES───> Done!
                                 │ NO
                         Recurse with p' / q'
```

1. **Greedy Selection**:
   Find the largest unit fraction $\frac{1}{n} \le \frac{p}{q}$.
   This implies:
   $$n \ge \frac{q}{p} \implies n = \left\lceil \frac{q}{p} \right\rceil = \left\lfloor \frac{q + p - 1}{p} \right\rfloor$$

2. **Remainder Calculation**:
   Subtract $\frac{1}{n}$ from $\frac{p}{q}$:
   $$\frac{p}{q} - \frac{1}{n} = \frac{p \cdot n - q}{q \cdot n}$$

3. **Reduction**:
   Divide the new numerator and denominator by $\gcd(p \cdot n - q, \; q \cdot n)$ to avoid intermediate numerical growth.

4. **Termination**:
   Repeat until the numerator becomes 0.

---

## 📐 Mathematical Proof of Termination

> **Theorem**: The Fibonacci-Sylvester algorithm terminates in a finite number of steps for any rational number $\frac{p}{q} > 0$.

**Proof:**
1. Let $n = \lceil q/p \rceil$.
2. By definition of the ceiling function:
   $$n - 1 < \frac{q}{p} \le n$$
3. Multiplying $n - 1 < \frac{q}{p}$ by $p$ (since $p > 0$):
   $$p(n - 1) < q \implies pn - p < q \implies pn - q < p$$
4. The new numerator after subtracting $\frac{1}{n}$ is:
   $$p' = pn - q$$
5. Thus, we have:
   $$0 \le p' < p$$
6. Since the numerator is a non-negative integer that strictly decreases with every iteration ($p_0 > p_1 > p_2 > \dots \ge 0$), it must reach 0 in at most $p$ steps. $\blacksquare$

---

## 💻 Complete C++ Implementation

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <cassert>
#include <string>

// Helper to compute greatest common divisor using Euclidean algorithm
long long gcd(long long a, long long b) {
    while (b != 0) {
        long long temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

struct EgyptianFraction {
    long long integerPart;
    std::vector<long long> denominators; // Each element represents 1 / d

    void print() const {
        bool first = true;
        if (integerPart > 0) {
            std::cout << integerPart;
            first = false;
        }
        for (long long d : denominators) {
            if (!first) std::cout << " + ";
            std::cout << "1/" << d;
            first = false;
        }
        if (first) {
            std::cout << "0";
        }
        std::cout << "\n";
    }
};

class EgyptianFractionSolver {
public:
    static EgyptianFraction solve(long long p, long long q) {
        if (q == 0) {
            throw std::invalid_argument("Denominator cannot be zero.");
        }
        if (p == 0) {
            return {0, {}};
        }

        // Simplify signs
        if (q < 0) {
            p = -p;
            q = -q;
        }

        EgyptianFraction result;
        result.integerPart = 0;

        // Handle improper fractions (p >= q)
        if (p >= q) {
            result.integerPart = p / q;
            p = p % q;
            if (p == 0) return result;
        }

        // Reduce initial fraction
        long long g = gcd(p, q);
        p /= g;
        q /= g;

        // Greedy loop
        while (p > 0) {
            // Find smallest n such that 1/n <= p/q => n = ceil(q / p)
            long long n = (q + p - 1) / p;

            result.denominators.push_back(n);

            // Remainder = (p * n - q) / (q * n)
            long long newP = p * n - q;
            long long newQ = q * n;

            // Reduce fraction
            long long common = gcd(newP, newQ);
            p = newP / common;
            q = newQ / common;
        }

        return result;
    }

    // Verify mathematical correctness of the decomposition
    static bool verify(long long originalP, long long originalQ, const EgyptianFraction& ef) {
        // Calculate sum: ef.integerPart + sum(1 / d)
        // Using common denominator
        long long commonDenom = 1;
        for (long long d : ef.denominators) {
            long long g = gcd(commonDenom, d);
            commonDenom = (commonDenom / g) * d;
        }

        long long totalNum = ef.integerPart * commonDenom;
        for (long long d : ef.denominators) {
            totalNum += commonDenom / d;
        }

        // Check if totalNum / commonDenom == originalP / originalQ
        long long left = totalNum * originalQ;
        long long right = originalP * commonDenom;
        return left == right;
    }
};

int main() {
    std::cout << "=== Egyptian Fraction Greedy Algorithm Test Harness ===\n\n";

    struct TestCase {
        long long p, q;
        std::string description;
    };

    std::vector<TestCase> testCases = {
        {2, 3,   "Simple Fraction 2/3"},
        {6, 14,  "Reducible Fraction 6/14 (= 3/7)"},
        {12, 13, "Close to 1 Fraction 12/13"},
        {4, 7,   "Classic 4/7"},
        {5, 121, "Erdos-Straus candidate 5/121"},
        {7, 4,   "Improper Fraction 7/4 (> 1)"}
    };

    for (const auto& tc : testCases) {
        std::cout << "Testing " << tc.description << " (" << tc.p << "/" << tc.q << "):\n";
        EgyptianFraction ef = EgyptianFractionSolver::solve(tc.p, tc.q);
        std::cout << "  Result: ";
        ef.print();

        bool ok = EgyptianFractionSolver::verify(tc.p, tc.q, ef);
        std::cout << "  Verification: " << (ok ? "PASSED (100% Equal)" : "FAILED") << "\n\n";
        assert(ok);
    }

    std::cout << "=== All Egyptian Fraction Tests Passed Successfully! ===\n";
    return 0;
}
```

---

## 📊 Complexity Analysis

| Metric | Bound | Explanation |
| :--- | :--- | :--- |
| **Number of Unit Fractions** | $O(p)$ | At each step, numerator strictly decreases ($p' \le p - 1$). |
| **Time per Step** | $O(\log(\min(p, q)))$ | GCD Euclidean reduction step. |
| **Total Time Complexity** | $O(p \log q)$ | At most $p$ iterations. |
| **Auxiliary Space** | $O(p)$ | Array storing the resulting denominators. |

---

## 💡 Practical Insights & Pitfalls

1. **Large Denominators**:
   - The Fibonacci-Sylvester greedy method can produce rapidly exploding denominators (e.g., $5/121 \to 1/25 + 1/757 + 1/763309 + \dots$).
   - In competitive programming, utilize 64-bit `long long` or `__int128` to avoid overflow during cross-multiplication `p * n - q`.
2. **Alternative Methods**:
   - Other Egyptian fraction algorithms (such as the binary method or continued fraction expansion) produce fractions with smaller denominators, but the greedy algorithm is famous for its simple, direct proof of termination.
