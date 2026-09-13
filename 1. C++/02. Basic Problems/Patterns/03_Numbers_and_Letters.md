# Number and Letter Patterns

These exercises add state and arithmetic to the row/column model. Keep the value rule separate from alignment.

## Number Exercises

1. **Floyd's triangle:** fill successive rows with one increasing counter.
2. **Row-number triangle:** row `r` contains `r` copies of `r`.
3. **Column-number triangle:** each row prints `1` through its width.
4. **Centered number pyramid:** values increase toward the center and then decrease.
5. **Number diamond:** combine increasing and decreasing widths without duplicating the middle row.
6. **Pascal's triangle:** generate each row from the previous row or update a binomial coefficient incrementally.

For Pascal's triangle, avoid computing three factorials for every cell. Within one row, update:

```text
C(r, 0) = 1
C(r, k + 1) = C(r, k) * (r - k) / (k + 1)
```

Use a sufficiently wide integer type and state the maximum supported row. Even 64-bit values overflow for moderately large rows.

## Letter Exercises

1. Row `r` contains the first `r` uppercase letters.
2. Row `r` contains `r` copies of its row letter.
3. Letters continue across row boundaries.
4. Print a centered alphabet pyramid.
5. Wrap after `Z` using an explicitly documented rule.

If a solution relies on arithmetic involving `'A'`, state the character-set assumption or use an explicit lookup string.

## Testing Questions

- What happens for size 1?
- Is zero rejected or defined as empty output?
- Does alignment change after values gain a second digit?
- Can arithmetic overflow before the requested row is printed?
- Are spaces part of the required output contract?

## Next Step

Continue to [Art and Grid Patterns](04_Art_and_Grid_Patterns.md).
