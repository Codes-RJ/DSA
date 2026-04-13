# 21_Proof_of_Optimality.md

## Proof of Optimality for Greedy Algorithms

### Overview

Proving that a greedy algorithm is optimal requires showing two properties:

1. **Greedy Choice Property** - A locally optimal choice is part of some globally optimal solution
2. **Optimal Substructure** - An optimal solution to the problem contains optimal solutions to subproblems

### Common Proof Techniques

| Technique | Description | Best For |
|-----------|-------------|----------|
| Exchange Argument | Transform any optimal solution into greedy solution without worsening | Interval scheduling, activity selection |
| Greedy Stays Ahead | Show greedy solution is at least as good as any solution at every step | Scheduling with deadlines |
| Structural Proof | Show problem has matroid structure | MST, matroid problems |
| Induction | Prove by induction on number of steps | Huffman coding |

---

### Technique 1: Exchange Argument

**Template:**

```
Let O be an optimal solution
Let G be the greedy solution
Find the first position where O and G differ
Show that swapping O's choice with G's choice yields a solution O' that is no worse than O
Repeat until O becomes G
Therefore G is optimal
```

**Example: Activity Selection**

```
Claim: Selecting the activity with earliest finish time is optimal.

Proof:
Let O be an optimal solution with activities sorted by finish time.
Let g be the first activity selected by greedy (earliest finish time overall).
Let a be the first activity in O.

Since g has earliest finish time, finish(g) ≤ finish(a).
Replace a with g in O to get O'.
O' is still valid because g finishes earlier, so it conflicts with fewer activities.
O' has the same number of activities as O.
Therefore, there exists an optimal solution containing g.

By induction, the greedy solution is optimal.
```

---

### Technique 2: Greedy Stays Ahead

**Template:**

```
Let G = {g1, g2, ..., gk} be greedy solution
Let O = {o1, o2, ..., om} be any other solution
Show by induction that for all i ≤ min(k, m), gi ≥ oi (or ≤ depending on problem)
Conclude that k ≥ m, so greedy is optimal
```

**Example: Job Sequencing with Deadlines**

```
Claim: Scheduling jobs in order of decreasing profit is optimal.

Proof:
Let G be greedy solution (jobs sorted by profit).
Let O be any optimal solution.

After i steps, the total profit of G's first i jobs is at least that of O's first i jobs.
Assume there exists a job j in O with higher profit than the i-th job in G.
But greedy always picks highest profit available, contradiction.
Therefore, greedy yields maximum total profit.
```

---

### Technique 3: Matroid Proof

**Definition:** A matroid M = (E, I) where:
- E is finite set of elements
- I is collection of independent subsets
- Empty set is independent
- Subsets of independent sets are independent
- If A, B ∈ I and |A| < |B|, then ∃ x ∈ B\A such that A ∪ {x} ∈ I

**Greedy Algorithm for Matroids:**

```
Sort elements by weight descending
Initialize S = empty
For each element e in sorted order:
    if S ∪ {e} is independent:
        add e to S
Return S
```

**Theorem:** For any matroid, the greedy algorithm yields a maximum-weight independent set.

**Example: Minimum Spanning Tree**

Graphic matroid (E = edges, I = forests). Greedy = Kruskal's algorithm.

---

### Technique 4: Induction

**Template:**

```
Base case: For smallest instance, greedy is optimal
Inductive step: Assume greedy works for size n-1
Show that greedy choice reduces problem to size n-1
Conclude greedy works for size n
```

**Example: Huffman Coding**

```
Claim: Merging two smallest frequency nodes is optimal.

Base case: n=2, only one way, optimal.
Inductive step: Assume optimal for n-1 nodes.
Let x and y be smallest frequency nodes.
In optimal tree, x and y are siblings at deepest level (can be proven).
Merge x and y into new node z with frequency = freq(x)+freq(y).
Tree for n-1 nodes (including z) is optimal by induction.
Therefore, merging x and y is optimal.
```

---

### Common Proofs for Classic Greedy Algorithms

#### Activity Selection

| Step | Proof |
|------|-------|
| Greedy Choice | Earliest finish time leaves maximum remaining time |
| Exchange | Replace any first activity with greedy choice, solution remains optimal |
| Substructure | After choosing greedy, remaining problem is smaller instance |

#### Fractional Knapsack

| Step | Proof |
|------|-------|
| Greedy Choice | Highest value/weight ratio item |
| Exchange | Replace any lower ratio item with higher ratio item increases value |
| Substructure | After taking max possible of highest ratio, problem reduces |

#### Huffman Coding

| Step | Proof |
|------|-------|
| Greedy Choice | Merge two smallest frequencies |
| Exchange | In optimal tree, two smallest are siblings at deepest level |
| Substructure | Merging reduces problem size by 1 |

#### Dijkstra's Algorithm

| Step | Proof |
|------|-------|
| Greedy Choice | Extract vertex with smallest distance |
| Exchange | Any other vertex would have larger or equal distance |
| Substructure | Once vertex is extracted, its distance is final |

#### Kruskal's Algorithm

| Step | Proof |
|------|-------|
| Greedy Choice | Smallest edge that doesn't create cycle |
| Cut Property | Smallest edge crossing any cut belongs to some MST |
| Substructure | Adding edge reduces problem size |

#### Prim's Algorithm

| Step | Proof |
|------|-------|
| Greedy Choice | Smallest edge connecting tree to outside |
| Cut Property | Smallest crossing edge belongs to some MST |
| Substructure | Adding edge grows tree, problem reduces |

---

### When Greedy Fails: Counterexample Proof

To prove a greedy algorithm is NOT optimal, provide a counterexample.

**Example: Coin Change with denominations {1, 3, 4}**

```
Greedy strategy: Take largest coin first
Target amount: 6

Greedy: 4 + 1 + 1 = 3 coins
Optimal: 3 + 3 = 2 coins

Therefore, greedy is not optimal for this coin system.
```

**Example: 0/1 Knapsack**

```
Greedy strategy: Take highest value/weight ratio
Capacity: 50

Items:
A: weight 40, value 100 (ratio 2.5)
B: weight 30, value 90 (ratio 3.0)
C: weight 30, value 80 (ratio 2.67)

Greedy: Take B (value 90), cannot take anything else → total 90
Optimal: Take A and C (value 100+80=180)

Therefore, greedy is not optimal for 0/1 knapsack.
```

---

### Summary Table

| Algorithm | Proof Technique | Key Insight |
|-----------|----------------|-------------|
| Activity Selection | Exchange | Earliest finish time |
| Fractional Knapsack | Exchange | Highest ratio |
| Huffman Coding | Induction | Merge smallest |
| Dijkstra | Greedy stays ahead | Smallest distance |
| Kruskal | Cut property | Smallest safe edge |
| Prim | Cut property | Smallest crossing edge |
| Job Sequencing | Exchange | Highest profit first |

---
---

## Next Step

- Go to [Theory.md](Theory.md) to continue with Theory.
