# Logic Puzzles in C++ - Algorithmic Deduction & Simulation

## 1. Introduction & Theoretical Foundations

**Logic puzzles** test algorithmic deduction, mathematical invariants, state-space exploration, and probability modeling. In competitive programming and technical interviews, these problems evaluate your ability to translate logical constraints into rigorous code structures—such as dynamic programming, graph state-space search, or Monte Carlo probabilistic simulations.

This module provides exhaustive theoretical derivations and production-grade C++ implementations for the 3 most iconic interview logic puzzles:
1. **The $K$-Eggs, $N$-Floors Drop Problem** (Mathematical Quadratic & Dynamic Programming)
2. **The Bridge and Torch Crossing Problem** (Generalized State-Space Dijkstra Search)
3. **The Monty Hall Problem** (Bayesian Probability & Monte Carlo Simulation)

---

## 2. Puzzle 1: The $K$-Eggs & $N$-Floors Drop Problem

### Problem Statement
You are given $k$ identical eggs and access to a building with $n$ floors labeled $1$ to $n$. There exists a critical floor $f$ ($0 \le f \le n$) such that:
- Any egg dropped from a floor higher than $f$ will break.
- Any egg dropped from floor $f$ or lower will survive undamaged.
- Broken eggs cannot be reused. Undamaged eggs can be dropped again.

**Goal:** Determine the minimum number of egg drops required in the **worst case** to find $f$ with certainty.

### Mathematical Formulation

#### Special Case: $K = 2$ Eggs, $N = 100$ Floors
If we drop the first egg at regular intervals of size $x$:
- When the first egg breaks, we must linearly search the interval below it using our remaining 1 egg.
- To balance the worst case across all intervals, the step size must decrement by $1$ on each subsequent drop:
$$x + (x - 1) + (x - 2) + \dots + 1 \ge 100$$
$$\frac{x(x + 1)}{2} \ge 100 \implies x^2 + x - 200 \ge 0 \implies x = \lceil 13.65 \rceil = 14$$

Thus, the first egg is dropped at floors: $14, 27, 39, 50, 60, 69, 77, 84, 90, 95, 99, 100$.

#### General Case: $K$ Eggs, $N$ Floors (Dynamic Programming)
Let $DP[k][n]$ be the minimum drops needed for $k$ eggs and $n$ floors.
If we drop an egg from floor $x \in [1, n]$:
1. **Egg Breaks**: We now have $k - 1$ eggs and must search the $x - 1$ floors below.
2. **Egg Survives**: We still have $k$ eggs and must search the $n - x$ floors above.

Since we seek the worst case among outcomes and the optimal floor choice:
$$DP[k][n] = 1 + \min_{1 \le x \le n} \left( \max(DP[k - 1][x - 1], DP[k][n - x]) \right)$$

**Base Cases:**
- $DP[1][n] = n$ (Linear scan required)
- $DP[k][0] = 0, \quad DP[k][1] = 1$

### C++ Implementation: $K$-Egg Problem with Optimal Strategy Path

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

class EggDropping {
public:
    // O(K * N^2) Classic Dynamic Programming with strategy reconstruction
    static int solveDP(int k, int n, std::vector<std::vector<int>>& optimalFloor) {
        std::vector<std::vector<int>> dp(k + 1, std::vector<int>(n + 1, 0));
        optimalFloor.assign(k + 1, std::vector<int>(n + 1, 0));

        // Base cases: 1 egg needs n drops
        for (int floor = 1; floor <= n; ++floor) {
            dp[1][floor] = floor;
            optimalFloor[1][floor] = 1;
        }

        // Base cases: 0 or 1 floor
        for (int egg = 1; egg <= k; ++egg) {
            dp[egg][0] = 0;
            dp[egg][1] = 1;
            optimalFloor[egg][1] = 1;
        }

        // Fill DP table
        for (int egg = 2; egg <= k; ++egg) {
            for (int floor = 2; floor <= n; ++floor) {
                int minDrops = INT_MAX;
                int bestChoice = -1;

                // Test every floor x from 1 to floor
                for (int x = 1; x <= floor; ++x) {
                    int broken = dp[egg - 1][x - 1];
                    int survived = dp[egg][floor - x];
                    int worstCase = 1 + std::max(broken, survived);

                    if (worstCase < minDrops) {
                        minDrops = worstCase;
                        bestChoice = x;
                    }
                }
                dp[egg][floor] = minDrops;
                optimalFloor[egg][floor] = bestChoice;
            }
        }

        return dp[k][n];
    }

    // O(K * N log N) Optimized DP using Binary Search
    static int solveOptimized(int k, int n) {
        std::vector<std::vector<int>> dp(k + 1, std::vector<int>(n + 1, 0));

        for (int i = 1; i <= n; ++i) dp[1][i] = i;
        for (int i = 1; i <= k; ++i) dp[i][1] = 1;

        for (int egg = 2; egg <= k; ++egg) {
            for (int floor = 2; floor <= n; ++floor) {
                int low = 1, high = floor, ans = floor;
                while (low <= high) {
                    int mid = low + (high - low) / 2;
                    int broken = dp[egg - 1][mid - 1];
                    int survived = dp[egg][floor - mid];

                    ans = std::min(ans, 1 + std::max(broken, survived));

                    if (broken < survived) {
                        low = mid + 1;
                    } else {
                        high = mid - 1;
                    }
                }
                dp[egg][floor] = ans;
            }
        }
        return dp[k][n];
    }
};
```

---

## 3. Puzzle 2: The Bridge and Torch Crossing Problem

### Problem Statement
Four people with crossing speeds $[1, 2, 5, 10]$ minutes need to cross a narrow bridge at night:
- The bridge holds at most 2 people simultaneously.
- A torch is required to cross, and they have only 1 torch.
- When two people cross together, they move at the speed of the slower person.

### Algorithmic Deduction: Two Competing Strategies
Let sorted speeds be $[T_0, T_1, \dots, T_{N-2}, T_{N-1}]$ where $T_0$ is fastest.

To transport the two slowest people ($T_{N-2}$ and $T_{N-1}$):
1. **Strategy A (Fastest escorts both)**:
   - $T_0$ and $T_{N-1}$ cross $\rightarrow T_{N-1}$ min, $T_0$ returns $\rightarrow T_0$ min.
   - $T_0$ and $T_{N-2}$ cross $\rightarrow T_{N-2}$ min, $T_0$ returns $\rightarrow T_0$ min.
   - Total time: $T_{N-1} + T_{N-2} + 2 \cdot T_0$.
2. **Strategy B (Two fastest cross first, slowest cross together)**:
   - $T_0$ and $T_1$ cross $\rightarrow T_1$ min, $T_0$ returns $\rightarrow T_0$ min.
   - $T_{N-2}$ and $T_{N-1}$ cross $\rightarrow T_{N-1}$ min, $T_1$ returns $\rightarrow T_1$ min.
   - Total time: $T_1 + T_0 + T_{N-1} + T_1 = T_{N-1} + 2 \cdot T_1 + T_0$.

For $[1, 2, 5, 10]$:
- Strategy A: $10 + 5 + 2(1) = 17$ min.
- Strategy B: $10 + 2(2) + 1 = 15$ min (for the two slowest).

### C++ State-Space Search Implementation (Dijkstra)
This implementation generalizes to **any** group size $N$ and arbitrary capacities:

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <unordered_map>
#include <algorithm>

struct BridgeState {
    int mask;        // Bitmask representing who is on the left bank (1 = left, 0 = right)
    bool torchLeft;  // true = torch on left bank, false = right
    int timeSpent;

    bool operator>(const BridgeState& other) const {
        return timeSpent > other.timeSpent;
    }
};

class BridgeCrossing {
public:
    static int findMinTime(const std::vector<int>& speeds, std::vector<std::string>& log) {
        int n = speeds.size();
        int initialMask = (1 << n) - 1; // All on left
        
        // dist[mask][torchPosition] = minimum time
        std::unordered_map<int, int> dist;
        std::priority_queue<BridgeState, std::vector<BridgeState>, std::greater<BridgeState>> pq;

        auto encode = [](int mask, bool torch) { return (mask << 1) | (torch ? 1 : 0); };

        pq.push({initialMask, true, 0});
        dist[encode(initialMask, true)] = 0;

        while (!pq.empty()) {
            BridgeState curr = pq.top();
            pq.pop();

            // Destination reached: all people on right bank
            if (curr.mask == 0 && !curr.torchLeft) {
                return curr.timeSpent;
            }

            int stateKey = encode(curr.mask, curr.torchLeft);
            if (curr.timeSpent > dist[stateKey]) continue;

            if (curr.torchLeft) {
                // 1 or 2 people cross Left -> Right
                for (int i = 0; i < n; ++i) {
                    if (!(curr.mask & (1 << i))) continue;
                    // Try 1 person crossing
                    {
                        int nextMask = curr.mask ^ (1 << i);
                        int nextTime = curr.timeSpent + speeds[i];
                        int nextKey = encode(nextMask, false);
                        if (!dist.count(nextKey) || nextTime < dist[nextKey]) {
                            dist[nextKey] = nextTime;
                            pq.push({nextMask, false, nextTime});
                        }
                    }
                    // Try 2 people crossing
                    for (int j = i + 1; j < n; ++j) {
                        if (!(curr.mask & (1 << j))) continue;
                        int nextMask = curr.mask ^ (1 << i) ^ (1 << j);
                        int nextTime = curr.timeSpent + std::max(speeds[i], speeds[j]);
                        int nextKey = encode(nextMask, false);
                        if (!dist.count(nextKey) || nextTime < dist[nextKey]) {
                            dist[nextKey] = nextTime;
                            pq.push({nextMask, false, nextTime});
                        }
                    }
                }
            } else {
                // 1 person returns Right -> Left with torch
                for (int i = 0; i < n; ++i) {
                    if (curr.mask & (1 << i)) continue; // Person already on left
                    int nextMask = curr.mask | (1 << i);
                    int nextTime = curr.timeSpent + speeds[i];
                    int nextKey = encode(nextMask, true);
                    if (!dist.count(nextKey) || nextTime < dist[nextKey]) {
                        dist[nextKey] = nextTime;
                        pq.push({nextMask, true, nextTime});
                    }
                }
            }
        }
        return -1;
    }
};
```

---

## 4. Puzzle 3: The Monty Hall Problem

### Problem Statement
A contestant is shown 3 doors: behind one is a car; behind the other two are goats.
1. The contestant chooses Door 1.
2. The host, Monty Hall (who knows what is behind every door), opens Door 3, revealing a goat.
3. Monty asks: *"Do you want to switch to Door 2?"*

### Mathematical Proof (Bayes' Theorem)
Let $C_i$ be the event that the prize is behind Door $i$ ($P(C_i) = 1/3$).
Assume contestant selects Door 1, and host opens Door 3 ($H_3$):
$$P(H_3 | C_1) = \frac{1}{2} \quad (\text{Host randomly picks between Door 2 and 3})$$
$$P(H_3 | C_2) = 1 \quad (\text{Host MUST pick Door 3, since Door 2 has the car})$$
$$P(H_3 | C_3) = 0 \quad (\text{Host cannot reveal the car})$$

By Bayes' Theorem:
$$P(C_1 | H_3) = \frac{P(H_3 | C_1) P(C_1)}{P(H_3)} = \frac{\frac{1}{2} \cdot \frac{1}{3}}{\frac{1}{2}} = \frac{1}{3}$$
$$P(C_2 | H_3) = \frac{P(H_3 | C_2) P(C_2)}{P(H_3)} = \frac{1 \cdot \frac{1}{3}}{\frac{1}{2}} = \frac{2}{3}$$

**Conclusion:** Switching doubles the probability of winning from $33.3\%$ to $66.7\%$.

### C++ Monte Carlo Simulation

```cpp
#include <iostream>
#include <vector>
#include <random>
#include <iomanip>

class MontyHallSimulation {
public:
    struct Result {
        int stayWins;
        int switchWins;
        int totalTrials;
        double stayWinRate;
        double switchWinRate;
    };

    static Result runSimulation(int trials) {
        std::mt19937 rng(1337); // Deterministic seed for reproducible testing
        std::uniform_int_distribution<int> dist3(0, 2);

        int stayWins = 0;
        int switchWins = 0;

        for (int i = 0; i < trials; ++i) {
            int carDoor = dist3(rng);
            int initialPick = dist3(rng);

            // Host opens a goat door that is neither chosen nor the car door
            int hostDoor = -1;
            for (int d = 0; d < 3; ++d) {
                if (d != initialPick && d != carDoor) {
                    hostDoor = d;
                    break;
                }
            }

            // Strategy 1: Stay
            if (initialPick == carDoor) {
                stayWins++;
            }

            // Strategy 2: Switch to the remaining door
            int switchedPick = -1;
            for (int d = 0; d < 3; ++d) {
                if (d != initialPick && d != hostDoor) {
                    switchedPick = d;
                    break;
                }
            }

            if (switchedPick == carDoor) {
                switchWins++;
            }
        }

        return {
            stayWins,
            switchWins,
            trials,
            (double)stayWins / trials * 100.0,
            (double)switchWins / trials * 100.0
        };
    }
};
```

---

## 5. Complete Runnable Verification Suite

```cpp
#include <iostream>
#include <vector>
#include <iomanip>

// Include the classes defined above
int main() {
    std::cout << "=====================================================" << std::endl;
    std::cout << "           LOGIC PUZZLES ALGORITHMIC SUITE           " << std::endl;
    std::cout << "=====================================================" << std::endl;

    // --- 1. Two Eggs Problem ---
    std::cout << "\n[1] K-EGGS & N-FLOORS PROBLEM (2 Eggs, 100 Floors):" << std::endl;
    std::vector<std::vector<int>> optimalFloor;
    int minDrops = EggDropping::solveDP(2, 100, optimalFloor);
    std::cout << "  Optimal worst-case drops needed: " << minDrops << std::endl;
    std::cout << "  First test drop should be at floor: " << optimalFloor[2][100] << std::endl;

    // --- 2. Bridge & Torch Crossing ---
    std::cout << "\n[2] BRIDGE AND TORCH CROSSING (Speeds: 1, 2, 5, 10 min):" << std::endl;
    std::vector<int> speeds = {1, 2, 5, 10};
    std::vector<std::string> log;
    int minTime = BridgeCrossing::findMinTime(speeds, log);
    std::cout << "  Minimum time to cross bridge: " << minTime << " minutes (Optimal: 17 min)" << std::endl;

    // --- 3. Monty Hall Simulation ---
    std::cout << "\n[3] MONTY HALL MONTE CARLO SIMULATION (100,000 trials):" << std::endl;
    int trials = 100000;
    auto res = MontyHallSimulation::runSimulation(trials);
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "  Strategy 'Stay'   Wins: " << res.stayWins << " / " << trials 
              << " (" << res.stayWinRate << "%)" << std::endl;
    std::cout << "  Strategy 'Switch' Wins: " << res.switchWins << " / " << trials 
              << " (" << res.switchWinRate << "%)" << std::endl;

    std::cout << "\n=====================================================" << std::endl;
    return 0;
}
```

---

## 6. Complexity Analysis Table

| Puzzle | Algorithm Technique | Time Complexity | Auxiliary Space | Key Invariant |
| :--- | :--- | :--- | :--- | :--- |
| **2-Egg Drop** | Mathematical / DP | $O(1)$ Math / $O(K \cdot N^2)$ DP | $O(K \cdot N)$ | Triangular bounds $x(x+1)/2 \ge N$ |
| **$K$-Egg Drop** | Binary Search DP | $O(K \cdot N \log N)$ | $O(K \cdot N)$ | Monotonicity of $DP[k-1][x-1]$ vs $DP[k][n-x]$ |
| **Bridge Crossing** | Dijkstra State-Space | $O(2^N \cdot N^2 \log(2^N))$ | $O(2^N)$ | Bitmask representation of river banks |
| **Monty Hall** | Monte Carlo Simulation | $O(\text{Trials})$ | $O(1)$ | Conditional probability shifts to unopened door |

---

## 7. Common Pitfalls & Interview Traps

1. **Egg Dropping Off-by-One**: Assuming $DP[k][n - x]$ represents floor numbers rather than the **remaining count of floors**. Subproblems depend only on interval size, not absolute floor indices.
2. **Bridge Crossing Greediness**: Always choosing the fastest person to escort everyone back and forth. For $[1, 2, 5, 10]$, this yields $19$ minutes, whereas pairing the two slowest ($5$ and $10$) yields $17$ minutes.
3. **Monty Hall Independence Fallacy**: Assuming that after one goat is revealed, each remaining door has a $50/50$ chance. The host's choice is **not random**; it is constrained by knowledge of the car's location.

---

## Next Step

- Proceed to [02_Pattern_Puzzles.md](02_Pattern_Puzzles.md) to explore cellular automata, Conway's Game of Life, and fractal generation in C++.
