# Theory.md

## Greedy Algorithms Theory

### Definition

A greedy algorithm is an algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most immediate benefit. It makes the locally optimal choice at each step with the hope that these local choices will lead to a globally optimal solution.

### Mathematical Foundation

A problem exhibits optimal substructure if an optimal solution to the problem contains within it optimal solutions to subproblems.

A problem exhibits the greedy choice property if a globally optimal solution can be arrived at by making a locally optimal choice.

### Proof Techniques for Greedy Algorithms

To prove that a greedy algorithm is correct, we typically use one of these methods:

#### 1. Exchange Argument

Show that if there is an optimal solution different from the greedy solution, we can transform it into the greedy solution without making it worse.

**Template:**
- Let O be an optimal solution
- Let G be the greedy solution
- Find the first place where O and G differ
- Show that swapping O's choice with G's choice does not increase the cost
- Repeat until O becomes G

#### 2. Greedy Stays Ahead

Show that the greedy solution is at least as good as any other solution at every step.

**Template:**
- Let O be an optimal solution
- Let G be the greedy solution
- Prove by induction that after k steps, G is at least as good as O
- Conclude that G is optimal

#### 3. Structural Argument

Show that the problem has a matroid structure, which guarantees that the greedy algorithm works.

### Matroid Theory

A matroid is a pair (E, I) where E is a finite set and I is a collection of independent subsets satisfying:

1. Empty set is independent
2. Every subset of an independent set is independent
3. If A and B are independent and |A| < |B|, then there exists x in B\A such that A ∪ {x} is independent

**Property:** For any matroid, the greedy algorithm that always picks the heaviest element that maintains independence yields the maximum weight independent set.

Examples of matroids:
- Graphic matroid (forests in a graph)
- Linear matroid (linearly independent vectors)
- Uniform matroid (all subsets of size ≤ k)

### Greedy Algorithm Design Process

```
Step 1: Determine the greedy choice
Step 2: Prove that the greedy choice is safe (leads to optimal solution)
Step 3: Reduce the problem to a smaller subproblem
Step 4: Apply recursion or iteration
```

### Common Greedy Patterns

#### Pattern 1: Earliest Finish Time

Used for interval scheduling. Choose the activity that finishes first.

```
Sort activities by finish time
Select the first activity
For each subsequent activity:
    if start time >= last finish time:
        select it
```

#### Pattern 2: Highest Value Density

Used for fractional knapsack. Choose items with highest value per unit weight.

```
Sort items by value/weight ratio descending
Take as much as possible of the highest ratio item
Repeat with remaining capacity
```

#### Pattern 3: Smallest First

Used for Huffman coding and optimal merge pattern. Always merge the two smallest items.

```
While more than one item remains:
    Take the two smallest items
    Merge them
    Insert the merged item back
```

#### Pattern 4: Latest Possible Schedule

Used for job sequencing. Schedule jobs as late as possible within their deadline.

```
Sort jobs by profit descending
For each job:
    Find the latest available slot before deadline
    Assign the job to that slot
```

#### Pattern 5: Minimum Edge Weight

Used for MST algorithms. Always pick the smallest edge that doesn't create a cycle.

### Proof of Optimality for Classic Problems

#### Activity Selection

**Greedy Choice:** Pick the activity with the earliest finish time.

**Exchange Argument Proof:**
- Let O be an optimal solution with activities sorted by finish time
- Let G be the greedy solution
- Let the first activity in O be a (finish time f_a)
- Let the first activity in G be g (finish time f_g)
- Since g has earliest finish time, f_g ≤ f_a
- Replace a with g in O. The new solution is still valid (g finishes earlier, so more room for others)
- New solution has same number of activities as O
- By induction, greedy yields optimal solution

#### Fractional Knapsack

**Greedy Choice:** Pick item with highest value/weight ratio.

**Exchange Argument Proof:**
- Let O be an optimal solution
- If O takes any item with lower ratio than the highest ratio item, we can exchange some amount
- Replace some weight of lower ratio item with same weight of higher ratio item
- Total value increases or stays same
- Repeat until all items are taken in ratio order

#### Huffman Coding

**Greedy Choice:** Merge the two nodes with smallest frequency.

**Proof by Contradiction:**
- Assume there exists an optimal tree where the two smallest frequency nodes are not siblings
- Swap them with their siblings
- The cost does not increase (proved by inequality)
- Therefore, there exists an optimal tree where they are siblings
- Merge them and apply induction

### When Greedy Fails

#### Counterexample for 0/1 Knapsack

```
Capacity = 50

Item 1: weight = 40, value = 100 (ratio = 2.5)
Item 2: weight = 30, value = 90 (ratio = 3.0)
Item 3: weight = 30, value = 80 (ratio = 2.67)

Greedy (highest ratio): picks Item 2 then can't pick anything else → value = 90
Optimal: picks Item 1 and Item 3 → value = 180

Greedy fails because it doesn't consider capacity constraints properly.
```

#### Counterexample for Coin Change

```
Denominations: {1, 3, 4}
Target: 6

Greedy (largest first): 4 + 1 + 1 = 3 coins
Optimal: 3 + 3 = 2 coins

Greedy fails because larger coin doesn't always lead to optimal.
```

### Characteristics of Greedy Problems

| Characteristic | Description |
|----------------|-------------|
| Local optimum | The best choice at current step is clear |
| No look-ahead | Decision doesn't require future information |
| Irreversible | Once a choice is made, it cannot be undone |
| Subproblem independence | Remaining problem doesn't depend on how we got here |

### Greedy vs Other Paradigms

| Paradigm | Decision | Backtracking | Optimality |
|----------|----------|--------------|------------|
| Greedy | One-time | No | Not guaranteed |
| Dynamic Programming | Multiple | No | Guaranteed |
| Divide and Conquer | Multiple | No | Guaranteed |
| Backtracking | Multiple | Yes | Guaranteed |