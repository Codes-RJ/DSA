# 01_Introduction_to_Greedy.md

## Introduction to Greedy Algorithms

### What is a Greedy Algorithm?

A greedy algorithm is a problem-solving approach that makes the locally optimal choice at each step, hoping that these local choices will lead to a globally optimal solution.

The term "greedy" comes from the fact that the algorithm takes the best possible immediate gain without considering the long-term consequences.

### Simple Example: Coin Change with Standard Denominations

**Problem:** Make change for a given amount using the fewest coins possible. Denominations available: 1, 5, 10, 25 (standard currency).

**Greedy Approach:**
```
amount = 87

Step 1: Take largest coin ≤ 87 → 25, remaining = 62
Step 2: Take largest coin ≤ 62 → 25, remaining = 37
Step 3: Take largest coin ≤ 37 → 25, remaining = 12
Step 4: Take largest coin ≤ 12 → 10, remaining = 2
Step 5: Take largest coin ≤ 2 → 1, remaining = 1
Step 6: Take largest coin ≤ 1 → 1, remaining = 0

Result: 25 + 25 + 25 + 10 + 1 + 1 = 6 coins
```

This works for standard denominations but fails for arbitrary denominations.

### Characteristics of Greedy Algorithms

| Characteristic | Description |
|----------------|-------------|
| Greedy Choice | A choice that seems best at the moment |
| Optimal Substructure | Problem can be broken into smaller subproblems |
| No Backtracking | Once a choice is made, it is never reconsidered |
| Efficiency | Usually very fast (O(n log n) or O(n)) |

### Steps to Design a Greedy Algorithm

```
Step 1: Formulate the problem as making a sequence of choices

Step 2: Determine the greedy choice (what looks best right now)

Step 3: Prove that the greedy choice is always part of some optimal solution

Step 4: Show that after making the greedy choice, the remaining problem is a smaller instance of the same problem

Step 5: Implement the algorithm recursively or iteratively
```

### Greedy vs Brute Force

**Problem:** Find the maximum number of tasks you can complete given time constraints.

| Approach | Time Complexity | Optimality |
|----------|----------------|------------|
| Brute Force | O(2^n) | Always optimal |
| Greedy | O(n log n) | Optimal for this problem |

### Greedy vs Dynamic Programming

| Aspect | Greedy | Dynamic Programming |
|--------|--------|---------------------|
| Number of decisions | One per step | Many per step |
| State space | No state needed | Large state space |
| Time complexity | O(n log n) typically | O(n²) or higher |
| Solution quality | Not always optimal | Always optimal |
| Implementation | Simple | Complex |

### When to Consider Greedy

Ask these questions:

1. Does the problem have a greedy choice property?
2. Does making a local choice reduce the problem to a smaller instance?
3. Is there a clear measure of "best" at each step?
4. Have I seen similar problems solved with greedy?

### Examples Where Greedy Works

| Problem | Greedy Strategy |
|---------|-----------------|
| Activity Selection | Pick earliest finishing activity |
| Fractional Knapsack | Pick highest value/weight ratio |
| Huffman Coding | Merge smallest frequencies |
| Dijkstra's Algorithm | Pick vertex with smallest distance |
| Minimum Spanning Tree | Pick smallest edge that doesn't create cycle |

### Examples Where Greedy Fails

| Problem | Why Greedy Fails |
|---------|------------------|
| 0/1 Knapsack | Can't take fractions, so local ratio doesn't guarantee global optimum |
| Coin Change (arbitrary) | Largest coin may prevent using combination of smaller coins |
| Longest Path | Choosing longest edge early may lead to dead ends |
| Traveling Salesman | Nearest neighbor doesn't guarantee shortest tour |

### Simple Greedy Problems to Start With

1. Activity Selection
2. Fractional Knapsack
3. Minimum Number of Platforms
4. Assign Cookies
5. Maximum Sum after K Negations

### Implementation Template

```cpp
// General structure of a greedy algorithm

// Step 1: Sort or preprocess data
sort(data.begin(), data.end(), comparator);

// Step 2: Initialize result
int result = 0;

// Step 3: Make greedy choices
for (auto item : data) {
    if (canTake(item)) {
        take(item);
        result += value(item);
        updateState(item);
    }
}

// Step 4: Return result
return result;
```

### Advantages and Disadvantages

**Advantages:**

- Easy to implement
- Fast execution time
- Low memory usage
- Often produces near-optimal solutions even when not optimal

**Disadvantages:**

- Not always optimal
- Proving optimality can be difficult
- May fail on certain inputs
- Not suitable for all problems
---

## Next Step

- Go to [02_Activity_Selection.md](02_Activity_Selection.md) to continue with Activity Selection.
