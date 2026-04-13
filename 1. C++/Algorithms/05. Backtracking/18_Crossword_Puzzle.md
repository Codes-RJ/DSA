# 18_Crossword_Puzzle.md

## Crossword Puzzle

### Definition

Given a crossword grid (with empty cells and blocked cells) and a list of words, place the words into the grid such that all words fit exactly into the empty spaces (horizontally or vertically).

### Problem Statement

Input:
- A 10×10 crossword grid (or any size) where:
  - '+' represents a blocked cell
  - '-' represents an empty cell to be filled
- A list of words separated by semicolons

Output:
- The filled crossword grid with words placed correctly

### Visual Example

```
Input Grid:
++++++++++
+------+++
+++-++++++
+++----+++
+++++-++++
++++++-+++
++++++++++

Words: "LONDON;DELHI;ICELAND;ANKARA"

Output (filled):
++++++++++
+LONDON+++
+++D++++++
+++ELHI+++
+++++C++++
++++++A+++
++++++++++
```

### Backtracking Approach

```
Step 1: Find all empty slots (horizontal and vertical)
Step 2: For each slot, try placing each word that fits
Step 3: Place the word in the slot (fill the cells)
Step 4: Recurse to next slot
Step 5: If all words placed, return true
Step 6: If no word fits, backtrack (clear the slot)
```

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

struct Slot {
    int row, col;
    int length;
    bool isHorizontal;
};

vector<Slot> findSlots(vector<string>& grid) {
    vector<Slot> slots;
    int n = grid.size();
    
    // Find horizontal slots
    for (int i = 0; i < n; i++) {
        int j = 0;
        while (j < n) {
            if (grid[i][j] == '-') {
                int start = j;
                int len = 0;
                while (j < n && grid[i][j] == '-') {
                    len++;
                    j++;
                }
                slots.push_back({i, start, len, true});
            } else {
                j++;
            }
        }
    }
    
    // Find vertical slots
    for (int j = 0; j < n; j++) {
        int i = 0;
        while (i < n) {
            if (grid[i][j] == '-') {
                int start = i;
                int len = 0;
                while (i < n && grid[i][j] == '-') {
                    len++;
                    i++;
                }
                slots.push_back({start, j, len, false});
            } else {
                i++;
            }
        }
    }
    
    return slots;
}

bool canPlaceWord(vector<string>& grid, Slot& slot, string& word) {
    if (slot.length != word.length()) return false;
    
    for (int i = 0; i < slot.length; i++) {
        int row = slot.row + (slot.isHorizontal ? 0 : i);
        int col = slot.col + (slot.isHorizontal ? i : 0);
        
        if (grid[row][col] != '-' && grid[row][col] != word[i]) {
            return false;
        }
    }
    return true;
}

void placeWord(vector<string>& grid, Slot& slot, string& word) {
    for (int i = 0; i < slot.length; i++) {
        int row = slot.row + (slot.isHorizontal ? 0 : i);
        int col = slot.col + (slot.isHorizontal ? i : 0);
        grid[row][col] = word[i];
    }
}

void removeWord(vector<string>& grid, Slot& slot) {
    for (int i = 0; i < slot.length; i++) {
        int row = slot.row + (slot.isHorizontal ? 0 : i);
        int col = slot.col + (slot.isHorizontal ? i : 0);
        grid[row][col] = '-';
    }
}

bool solveCrossword(vector<string>& grid, vector<Slot>& slots, 
                     vector<string>& words, int index, vector<bool>& used) {
    if (index == slots.size()) {
        return true;  // All slots filled
    }
    
    for (int i = 0; i < words.size(); i++) {
        if (!used[i] && canPlaceWord(grid, slots[index], words[i])) {
            placeWord(grid, slots[index], words[i]);
            used[i] = true;
            
            if (solveCrossword(grid, slots, words, index + 1, used)) {
                return true;
            }
            
            used[i] = false;
            removeWord(grid, slots[index]);
        }
    }
    
    return false;
}

int main() {
    vector<string> grid = {
        "++++++++++",
        "+------+++",
        "+++-++++++",
        "+++----+++",
        "+++++-++++",
        "++++++-+++",
        "++++++++++",
        "++++++++++",
        "++++++++++",
        "++++++++++"
    };
    
    string wordsStr = "LONDON;DELHI;ICELAND;ANKARA";
    vector<string> words;
    stringstream ss(wordsStr);
    string word;
    while (getline(ss, word, ';')) {
        words.push_back(word);
    }
    
    vector<Slot> slots = findSlots(grid);
    vector<bool> used(words.size(), false);
    
    if (solveCrossword(grid, slots, words, 0, used)) {
        cout << "Solved Crossword:" << endl;
        for (string& row : grid) {
            cout << row << endl;
        }
    } else {
        cout << "No solution found" << endl;
    }
    
    return 0;
}
```

### Slot Finding Example

```
Grid (5x5 for simplicity):
+ - - - +
+ - + - +
+ - + - +
+ - - - +
+ + + + +

Horizontal slots:
(0,1) length 3
(1,1) length 1
(2,1) length 1
(3,1) length 3

Vertical slots:
(0,1) length 4
(0,3) length 3
(1,1) length 2
(1,3) length 2
(2,1) length 1
```

### Word Placement Example

```
Slot: (0,1) horizontal, length 3
Words: "CAT", "DOG", "BAT"

Try "CAT":
Place C at (0,1), A at (0,2), T at (0,3)
Recurse to next slot

If later conflict occurs, backtrack and remove "CAT"
Try "DOG" next
```

### Optimization: Slot Ordering

Sort slots by length descending (longest slots first) for better pruning.

```cpp
sort(slots.begin(), slots.end(), [](Slot& a, Slot& b) {
    return a.length > b.length;
});
```

### Time Complexity

| Complexity | Value |
|------------|-------|
| Worst case | O(w! × s) where w = number of words, s = number of slots |

### Space Complexity

O(n²) for grid + O(slots) for slot storage

### Variations

#### 1. Crossword with Pre-filled Letters

Some cells already have letters (constraints).

#### 2. Crossword with Multiple Solutions

Find all possible solutions.

#### 3. Crossword Puzzle Generator

Generate a crossword puzzle from a word list.

### Practice Problems

1. Fill a crossword puzzle with given words
2. Find all possible placements for a word in a crossword
3. Determine if a crossword puzzle has a unique solution
4. Generate a crossword puzzle from a word list
5. Solve a crossword with intersecting constraints
---

## Next Step

- Go to [19_Backtracking_vs_Brute_Force.md](19_Backtracking_vs_Brute_Force.md) to continue with Backtracking vs Brute Force.
