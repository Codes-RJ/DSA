# Logic Puzzles

## Introduction
Logic puzzles are challenges that require using deduction, inference, and reasoning to solve. They are popular in interviews to test problem-solving skills outside of pure coding.

## Classic Puzzles

### 1. Two Eggs Problem
**Question**: You have 2 eggs and a 100-story building. Find the highest floor from which an egg can be dropped without breaking, using the minimum number of attempts.
- **Solution**: Use **Dynamic Programming** or **Math**.
- `x + (x-1) + (x-2) + ... + 1 >= 100`
- Minimum attempts: `14`.

### 2. Crossing the Bridge
**Question**: Four people need to cross a bridge at night. They have one torch. The bridge can only hold 2 people at a time. Each person has a different crossing speed (1, 2, 5, 10 minutes).
- **Solution**: Send the two slowest people together to minimize the number of slow trips.
- `1 and 2 go → 1 returns` (Total 3)
- `5 and 10 go → 2 returns` (Total 3+10+2=15)
- `1 and 2 go → Done` (Total 15+2=17 minutes).

### 3. Monty Hall Problem
**Question**: Three doors, one with a car, two with goats. You pick one. The host (who knows what's behind) opens one of the other doors with a goat. Should you switch?
- **Solution**: Switch. Initial probability is 1/3. After goat is revealed, the other door has a 2/3 chance.

## Core Concepts for Solving Logic Puzzles
1. **Deductive Reasoning**: Starting with general premises to reach a logical conclusion.
2. **Inductive Reasoning**: Finding patterns or trends.
3. **Pigeonhole Principle**: Distributing items to prove that one container must have multiple.
4. **Constraint Satisfaction**: Identifying what is possible given the rules.

## Puzzle Solving Strategies
- **Start with small values**: Solve for a 4-story building before 100.
- **List all constraints**: Clear hurdles early on.
- **Identify invariants**: What stays the same even as variables change?
- **Use analogies**: Relate it to known problems.
- **Think as an adversary**: How would you break your own solution?
---

## Next Step

- Go to [02_Pattern_Puzzles.md](02_Pattern_Puzzles.md) to continue with Pattern Puzzles.
