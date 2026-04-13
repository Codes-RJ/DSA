# 06_State_Transition.md

## State Transition in Dynamic Programming

### Definition

State transition is the formula or rule that defines how to compute the value of a state from previously computed states. It is the core of any DP solution.

### Components of a Transition

A transition typically consists of:

1. Current state: The subproblem we are trying to solve
2. Previous states: Smaller subproblems that are already solved
3. Operation: How to combine previous states (max, min, sum, etc.)
4. Cost/Value: Additional value added in this step

### Mathematical Representation

dp[current_state] = operation( dp[prev_state_1] + cost_1, dp[prev_state_2] + cost_2, ... )

### Common Transition Patterns

#### Pattern 1: Linear Addition

dp[i] = dp[i-1] + dp[i-2]

**Example:** Fibonacci, Climbing Stairs

#### Pattern 2: Minimization/Maximization

dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

**Example:** Min Cost Climbing Stairs

#### Pattern 3: Take or Skip

dp[i] = max(dp[i-1], dp[i-2] + value[i])

**Example:** House Robber

#### Pattern 4: Prefix Maximum/Minimum

dp[i] = max(dp[i-1], arr[i])

**Example:** Maximum subarray ending at i

#### Pattern 5: Grid Movement

dp[i][j] = dp[i-1][j] + dp[i][j-1]

**Example:** Unique Paths

#### Pattern 6: String Comparison

```
if (s1[i] == s2[j]):
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

**Example:** Longest Common Subsequence

#### Pattern 7: Knapsack Decision

```
if (w >= weight[i]):
    dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i]] + value[i])
else:
    dp[i][w] = dp[i-1][w]
```

**Example:** 0/1 Knapsack

#### Pattern 8: Interval Partition

dp[i][j] = min over k of (dp[i][k] + dp[k+1][j] + cost(i, j, k))

**Example:** Matrix Chain Multiplication

#### Pattern 9: Bitmask Transitions

dp[mask][i] = min over j of (dp[mask ^ (1<<i)][j] + dist[j][i])

**Example:** Traveling Salesman Problem

#### Pattern 10: Digit DP Transitions

dp[pos][tight][sum] = sum over digit d of dp[pos+1][tight && d==limit][sum+d]

**Example:** Digit sum problems

### How to Derive Transitions

#### Step 1: Define what dp[state] represents

Ask: "What is the best/optimal/count for this subproblem?"

#### Step 2: Identify the last decision

Ask: "What is the final step that leads to this state?"

#### Step 3: Express current state in terms of smaller states

Ask: "If I knew the answers for smaller states, how would I compute this one?"

#### Step 4: Write the formula

Combine smaller states using max, min, sum, or other operations.

### Examples of Transition Derivation

#### Example 1: Climbing Stairs

**Problem:** Ways to reach step n using 1 or 2 steps.

**Last decision:** Either took 1 step from step n-1, or 2 steps from step n-2.

**Transition:** dp[n] = dp[n-1] + dp[n-2]

#### Example 2: House Robber

**Problem:** Max money without robbing adjacent houses.

**Last decision:** Either rob house i (then must skip i-1) or skip house i.

**Transition:** dp[i] = max(dp[i-1], dp[i-2] + nums[i])

#### Example 3: Knapsack

**Problem:** Max value with weight capacity.

**Last decision:** Either take item i (add its value, reduce capacity) or skip it.

**Transition:** dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i]] + val[i])

#### Example 4: LCS

**Problem:** Longest common subsequence.

**Last decision:** Either match characters s1[i] and s2[j] or skip one of them.

**Transition:**
- If match: dp[i][j] = dp[i-1][j-1] + 1
- If skip: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

### Transition Order

The order of computation must ensure that all dependencies are computed first.

| Problem | Dependencies | Order |
|---------|--------------|-------|
| Fibonacci | dp[i] needs dp[i-1], dp[i-2] | Increasing i |
| Grid DP | dp[i][j] needs dp[i-1][j], dp[i][j-1] | Row-major |
| LCS | dp[i][j] needs dp[i-1][j], dp[i][j-1], dp[i-1][j-1] | Increasing i, j |
| Interval DP | dp[i][j] needs smaller intervals | Increasing length |
| Tree DP | dp[u] needs dp[children] | Post-order DFS |

### Invalid Transitions

Some transitions are invalid for certain problems:

- **Cyclic dependencies:** When A depends on B and B depends on A
- **Out of bounds:** Accessing indices outside array limits
- **Negative indices:** Not handling base cases properly
- **Infinite loops:** Not making progress toward base case

### Multiple Transitions per State

Some states can have multiple possible transitions:

```
dp[i] = max(
    dp[i-1] + 1,
    dp[i-2] * 2,
    dp[i/2] + 5 if i%2 == 0
)
```

### Transition with Conditions

```
if (condition1):
    dp[i] = min(dp[i], dp[i-1] + cost1)
if (condition2):
    dp[i] = min(dp[i], dp[i-2] + cost2)
if (condition3):
    dp[i] = min(dp[i], dp[i-3] + cost3)
```

### Transition with Loops

Sometimes you need to loop over all possible previous states:

```
for (int j = 0; j < i; j++) {
    if (canTransition(j, i)) {
        dp[i] = max(dp[i], dp[j] + value(j, i));
    }
}
```
---

## Next Step

- Go to [07_DP_on_Subsequences.md](07_DP_on_Subsequences.md) to continue with DP on Subsequences.
