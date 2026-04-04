# Pattern Puzzles

## Introduction
Pattern puzzles involve identifying a sequence or visual structure and reproducing it or finding its rules.

## 1. Number Sequences
Recognize a mathematical order.
- **Arithmetic progression**: `2, 4, 6, 8, ...`
- **Geometric progression**: `1, 3, 9, 27, ...`
- **Fibonacci**: `0, 1, 1, 2, 3, 5, ...`
- **Square numbers**: `1, 4, 9, 16, 25, ...`

## 2. Visual Patterns (Grid based)
Often found in IQ tests or as coding challenges (e.g., printing stars in specific shapes).

### Pyramid Pattern (C++)
```cpp
/*
    *
   ***
  *****
*/
for(int i = 1; i <= n; i++) {
    for(int j = 1; j <= n - i; j++) cout << " ";
    for(int j = 1; j <= 2 * i - 1; j++) cout << "*";
    cout << endl;
}
```

## 3. Conway's Game of Life
A cellular automaton where the next state is determined by its neighbors.
- Rule: Survival, death, birth based on number of living neighbors.
- Used to study emergent patterns.

## 4. Fractal Patterns
Repeating self-similar structures at every scale (e.g., Sierpinski triangle).
- Usually solved using **Recursion**.

## Techniques for Pattern Discovery
1. **Subtract adjacent terms**: See if there is a common difference.
2. **Divide adjacent terms**: See if there is a common ratio.
3. **Check for known series**: Squares, cubes, primes, powers of two.
4. **Coordinate Mapping**: For 2D patterns, find a functional relationship between `(i, j)` and the character to print.

## Summary Checklist
- [ ] Constant difference? → Linear pattern.
- [ ] Constant ratio? → Exponential pattern.
- [ ] Recursion involved? → Fractal or dynamic sequence.
- [ ] Symmetry? → Reflective coordinate logic.
