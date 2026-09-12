# Police and Thieves Catching Problem (Greedy Matching)

## 📖 Overview

The **Police and Thieves** problem is a canonical greedy matching problem on a linear discrete space. 

Given an array of size $N$ containing characters `'P'` (representing a police officer) and `'T'` (representing a thief), along with an integer $K$:
- Each police officer can catch **at most one** thief.
- A police officer at index $i$ can catch a thief at index $j$ if and only if the distance $|i - j| \le K$.
- **Objective**: Determine the **maximum number of thieves** that can be caught.

---

## 🎯 Greedy Choice Property & Strategy

```
Array:   [ P,  T,  T,  P,  T,  P ]      K = 2
Index:     0   1   2   3   4   5

Police indices:   [ 0, 3, 5 ]
Thieves indices:  [ 1, 2, 4 ]

Matching Trace:
  P[0] matches T[1] (dist = 1 <= 2)  --> Caught!
  P[3] matches T[2] (dist = 1 <= 2)  --> Caught!
  P[5] matches T[4] (dist = 1 <= 2)  --> Caught!

Total Caught: 3 (Maximum Possible)
```

### The Invariant
Always match the **leftmost available police officer** with the **leftmost reachable thief**. 

Why is this optimal?
1. If the current thief $t$ is too far to the left of the current officer $p$ ($t < p - K$), no subsequent officer $p' > p$ will ever be able to reach $t$. Therefore, $t$ can never be caught and must be discarded.
2. If the current officer $p$ is too far to the left of the current thief $t$ ($p < t - K$), this officer cannot reach $t$ or any subsequent thief $t' > t$. Therefore, $p$ can never catch any thief and must be discarded.
3. If $|p - t| \le K$, matching $p$ with $t$ is optimal: reserving $p$ for a thief further to the right could prevent a future officer from finding an unassigned thief, while leaving $t$ for a future officer unnecessarily consumes reach.

---

## 📐 Mathematical Proof by Exchange Argument

Let $G$ be the greedy matching and $O$ be an arbitrary optimal matching.
Suppose $G$ differs from $O$. Let $(p, t)$ be the first pair in $G$ that does not exist in $O$.
- If neither $p$ nor $t$ is matched in $O$, adding $(p, t)$ to $O$ produces a valid matching with $|O| + 1$ pairs, contradicting the optimality of $O$.
- If $p$ is matched to $t'$ in $O$ (where $t' > t$ by greedy ordering):
  - If $t$ is unmatched in $O$, we can safely replace $(p, t')$ with $(p, t)$ because $|p - t| \le |p - t'| \le K$.
  - If $t$ is matched to $p'$ in $O$ (where $p' > p$), we can swap their targets to form $(p, t)$ and $(p', t')$. Since $p \le p'$ and $t \le t'$, the distance $|p' - t'| \le K$ is maintained.
- In all cases, $O$ can be transformed into $G$ without decreasing the matching size.
- Therefore, the greedy strategy is mathematically optimal. $\blacksquare$

---

## 💻 Complete C++ Implementation

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <cassert>
#include <algorithm>

class PoliceAndThieves {
public:
    // Approach 1: Auxiliary Index Vectors (O(N) Time, O(N) Space)
    static int catchThievesQueue(const std::vector<char>& arr, int k) {
        std::vector<int> police;
        std::vector<int> thieves;

        for (int i = 0; i < static_cast<int>(arr.size()); i++) {
            if (arr[i] == 'P') police.push_back(i);
            else if (arr[i] == 'T') thieves.push_back(i);
        }

        int pIdx = 0, tIdx = 0;
        int caught = 0;

        while (pIdx < static_cast<int>(police.size()) && tIdx < static_cast<int>(thieves.size())) {
            int p = police[pIdx];
            int t = thieves[tIdx];

            if (std::abs(p - t) <= k) {
                // Officer catches thief
                caught++;
                pIdx++;
                tIdx++;
            } else if (t < p) {
                // Thief is too far left; no future officer can catch them
                tIdx++;
            } else {
                // Officer is too far left; cannot catch this or future thieves
                pIdx++;
            }
        }

        return caught;
    }

    // Approach 2: Two-Pointer In-Place (O(N) Time, O(1) Auxiliary Space)
    static int catchThievesOptimal(const std::vector<char>& arr, int k) {
        int n = static_cast<int>(arr.size());
        int p = 0; // Pointer to next officer
        int t = 0; // Pointer to next thief
        int caught = 0;

        while (p < n && t < n) {
            // Advance p to next officer
            while (p < n && arr[p] != 'P') p++;
            // Advance t to next thief
            while (t < n && arr[t] != 'T') t++;

            if (p < n && t < n) {
                if (std::abs(p - t) <= k) {
                    caught++;
                    p++;
                    t++;
                } else if (t < p) {
                    t++;
                } else {
                    p++;
                }
            }
        }

        return caught;
    }
};

int main() {
    std::cout << "=== Police and Thieves Greedy Matching Test Harness ===\n\n";

    struct TestCase {
        std::vector<char> arr;
        int k;
        int expected;
        std::string description;
    };

    std::vector<TestCase> testCases = {
        {
            {'P', 'T', 'T', 'P', 'T'}, 
            1, 2, 
            "Alternating sequence with K=1"
        },
        {
            {'T', 'T', 'P', 'P', 'T', 'P'}, 
            2, 3, 
            "Multiple officers together with K=2"
        },
        {
            {'P', 'T', 'P', 'T', 'T', 'P'}, 
            3, 3, 
            "Large reach K=3"
        },
        {
            {'P', 'P', 'P'}, 
            2, 0, 
            "Zero thieves available"
        },
        {
            {'T', 'T', 'T'}, 
            2, 0, 
            "Zero officers available"
        },
        {
            {'P', 'T', 'P', 'T'}, 
            0, 0, 
            "Zero reach K=0"
        }
    };

    for (const auto& tc : testCases) {
        std::cout << "Testing: " << tc.description << " (K=" << tc.k << ")\n";
        std::cout << "  Array: [ ";
        for (char c : tc.arr) std::cout << c << " ";
        std::cout << "]\n";

        int res1 = PoliceAndThieves::catchThievesQueue(tc.arr, tc.k);
        int res2 = PoliceAndThieves::catchThievesOptimal(tc.arr, tc.k);

        std::cout << "  Result (Queue Method):   " << res1 << "\n";
        std::cout << "  Result (Two-Pointer O(1)): " << res2 << "\n";
        std::cout << "  Expected: " << tc.expected << " => " 
                  << (res1 == tc.expected && res2 == tc.expected ? "PASSED" : "FAILED") << "\n\n";

        assert(res1 == tc.expected);
        assert(res2 == tc.expected);
    }

    std::cout << "=== All Police and Thieves Tests Completed Successfully! ===\n";
    return 0;
}
```

---

## 📊 Complexity Analysis

| Approach | Time Complexity | Auxiliary Space | Notes |
| :--- | :--- | :--- | :--- |
| **Queue / Vector Storage** | $O(N)$ | $O(N)$ | Easy to trace; separate index lists |
| **Two-Pointer Direct Scan** | $O(N)$ | $O(1)$ | Optimal cache-friendly linear sweep |
