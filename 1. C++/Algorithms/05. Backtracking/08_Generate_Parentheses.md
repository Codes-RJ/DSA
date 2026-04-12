# 08_Generate_Parentheses.md

## Generate Parentheses

### Definition

Given n pairs of parentheses, generate all combinations of well-formed parentheses. A well-formed parentheses string has:
- Equal number of opening and closing brackets
- Every closing bracket matches a previous opening bracket

### Problem Statement

Input:
- Integer n (number of pairs of parentheses)

Output:
- All valid parentheses combinations

### Visual Example (n=3)

```
Valid strings:
((()))
(()())
(())()
()(())
()()()
```

### Backtracking Approach

```
Step 1: Start with empty string
Step 2: Keep track of:
        - open: number of opening brackets used
        - close: number of closing brackets used
Step 3: Add '(' if open < n
Step 4: Add ')' if close < open
Step 5: When open == close == n, record solution
```

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

void generateParentheses(int n, int open, int close, string current, vector<string>& result) {
    // Base case: used all parentheses
    if (open == n && close == n) {
        result.push_back(current);
        return;
    }
    
    // Add opening bracket if possible
    if (open < n) {
        generateParentheses(n, open + 1, close, current + '(', result);
    }
    
    // Add closing bracket if possible
    if (close < open) {
        generateParentheses(n, open, close + 1, current + ')', result);
    }
}

vector<string> generateParentheses(int n) {
    vector<string> result;
    generateParentheses(n, 0, 0, "", result);
    return result;
}

int main() {
    int n = 3;
    vector<string> result = generateParentheses(n);
    
    cout << "All valid parentheses for n=" << n << ":" << endl;
    for (string s : result) {
        cout << s << endl;
    }
    
    return 0;
}
```

### Example Walkthrough (n=3)

```
Start: open=0, close=0, current=""

open=0, close=0
├── Add '(' (open < 3)
│   open=1, close=0, current="("
│   ├── Add '(' (open=1 < 3)
│   │   open=2, close=0, current="(("
│   │   ├── Add '(' (open=2 < 3)
│   │   │   open=3, close=0, current="((("
│   │   │   ├── Add ')' (close=0 < open=3)
│   │   │   │   open=3, close=1, current="((()"
│   │   │   │   ├── Add ')' (close=1 < open=3)
│   │   │   │   │   open=3, close=2, current="((())"
│   │   │   │   │   ├── Add ')' (close=2 < open=3)
│   │   │   │   │   │   open=3, close=3, current="((()))" → solution
│   │   │   │   │   └── ...
│   │   │   │   └── ...
│   │   │   └── ...
│   │   ├── Add ')' (close=0 < open=2)
│   │   │   open=2, close=1, current="(()"
│   │   │   ├── Add '(' (open=2 < 3)
│   │   │   │   open=3, close=1, current="(()("
│   │   │   │   ├── Add ')' (close=1 < open=3)
│   │   │   │   │   open=3, close=2, current="(()()"
│   │   │   │   │   ├── Add ')' (close=2 < open=3)
│   │   │   │   │   │   open=3, close=3, current="(()())" → solution
│   │   │   │   │   └── ...
│   │   │   │   └── ...
│   │   │   └── Add ')' (close=1 < open=2)
│   │   │       open=2, close=2, current="(())"
│   │   │       ├── Add '(' (open=2 < 3)
│   │   │       │   open=3, close=2, current="(())("
│   │   │       │   ├── Add ')' (close=2 < open=3)
│   │   │       │   │   open=3, close=3, current="(())()" → solution
│   │   │       │   └── ...
│   │   │       └── Add ')' (close=2 < open=2? No)
│   │   │       └── ...
│   │   └── ...
│   └── ...
└── Add ')' cannot (close=0 < open=0? No)
```

### Recursion Tree Visualization

```
Level 0: ""
         │
Level 1: "("
         │
    ┌────┴────┐
Level 2: "(("   "()"
         │       │
    ┌────┴────┐  │
Level 3: "(((" "(()" "()("
         │      │     │
        ...    ...   ...
```

### Time Complexity

| Complexity | Value |
|------------|-------|
| Time | O(4^n / √n) - nth Catalan number |
| Number of solutions | Catalan number C_n = (1/(n+1)) * C(2n, n) |

### Catalan Numbers for n

| n | Number of Valid Parentheses |
|---|----------------------------|
| 1 | 1 |
| 2 | 2 |
| 3 | 5 |
| 4 | 14 |
| 5 | 42 |
| 6 | 132 |
| 7 | 429 |
| 8 | 1430 |

### Space Complexity

O(n) for recursion stack + O(n) for string

### Variations

#### 1. Generate All Combinations with Different Brackets

```cpp
void generateBrackets(int n, int open1, int close1, int open2, int close2, 
                       string current, vector<string>& result) {
    if (open1 == n && close1 == n && open2 == n && close2 == n) {
        result.push_back(current);
        return;
    }
    
    // Add '('
    if (open1 < n) {
        generateBrackets(n, open1 + 1, close1, open2, close2, current + '(', result);
    }
    
    // Add '[' 
    if (open2 < n) {
        generateBrackets(n, open1, close1, open2 + 1, close2, current + '[', result);
    }
    
    // Add ')'
    if (close1 < open1) {
        generateBrackets(n, open1, close1 + 1, open2, close2, current + ')', result);
    }
    
    // Add ']'
    if (close2 < open2) {
        generateBrackets(n, open1, close1, open2, close2 + 1, current + ']', result);
    }
}
```

#### 2. Valid Parentheses Checker

```cpp
bool isValid(string s) {
    int balance = 0;
    for (char c : s) {
        if (c == '(') balance++;
        else balance--;
        if (balance < 0) return false;
    }
    return balance == 0;
}
```

#### 3. Generate All Combinations of Length 2n

Not all combinations are valid; backtracking ensures validity.

#### 4. Longest Valid Parentheses Substring

Different problem (usually solved with stack or DP).

### Practice Problems

1. Generate all valid parentheses for given n
2. Count number of valid parentheses for given n
3. Generate all valid parentheses with k types of brackets
4. Check if a given parentheses string is valid
5. Find the longest valid parentheses substring