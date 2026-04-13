# 15_Lexicographically_Smallest_Sequence.md

## Lexicographically Smallest Sequence

### Definition

Given constraints or operations, find the lexicographically smallest sequence (array, string, or permutation) that satisfies given conditions.

### Problem Statement (General Form)

Input:
- Constraints on the sequence (length, sum, adjacency rules, etc.)

Output:
- Lexicographically smallest sequence satisfying all constraints

### Greedy Strategy

**Strategy:** Build the sequence from left to right. At each position, try the smallest possible value that allows the remaining positions to be filled validly.

**Why this works:** Lexicographic order is determined by the first differing position. Making the earliest positions as small as possible guarantees the smallest lexicographic sequence.

### Algorithm Template

```
Step 1: Initialize result array of size n
Step 2: For position i from 0 to n-1:
        For value v from minValue to maxValue:
            if assigning v at position i allows a valid completion:
                result[i] = v
                break
Step 3: Return result
```

### Example 1: Smallest Number with Given Digit Sum

**Problem:** Find the smallest number with n digits and digit sum = s.

```cpp
string smallestNumberWithDigitSum(int n, int s) {
    if (s == 0) {
        return (n == 1) ? "0" : "-1";
    }
    if (s > 9 * n) {
        return "-1";
    }
    
    string result(n, '0');
    
    for (int i = n - 1; i >= 0; i--) {
        if (s > 9) {
            result[i] = '9';
            s -= 9;
        } else {
            result[i] = char('0' + s);
            s = 0;
        }
    }
    
    if (result[0] == '0') {
        // Find first non-zero and move one to front
        for (int i = 1; i < n; i++) {
            if (result[i] > '0') {
                result[i]--;
                result[0] = '1';
                break;
            }
        }
    }
    
    return result;
}
```

### Example 2: Smallest Subsequence of Distinct Characters

**Problem:** Given a string, find the lexicographically smallest subsequence that contains all distinct characters exactly once.

```cpp
string smallestSubsequence(string s) {
    vector<int> lastPos(26, -1);
    vector<bool> inStack(26, false);
    
    for (int i = 0; i < s.length(); i++) {
        lastPos[s[i] - 'a'] = i;
    }
    
    string result;
    
    for (int i = 0; i < s.length(); i++) {
        char c = s[i];
        if (inStack[c - 'a']) continue;
        
        while (!result.empty() && c < result.back() && 
               lastPos[result.back() - 'a'] > i) {
            inStack[result.back() - 'a'] = false;
            result.pop_back();
        }
        
        result.push_back(c);
        inStack[c - 'a'] = true;
    }
    
    return result;
}
```

### Example 3: Smallest Number After Removing K Digits

**Problem:** Remove k digits from a number to make it as small as possible.

```cpp
string removeKdigits(string num, int k) {
    string result;
    
    for (char c : num) {
        while (!result.empty() && k > 0 && result.back() > c) {
            result.pop_back();
            k--;
        }
        result.push_back(c);
    }
    
    while (k > 0) {
        result.pop_back();
        k--;
    }
    
    // Remove leading zeros
    int i = 0;
    while (i < result.length() && result[i] == '0') {
        i++;
    }
    
    result = result.substr(i);
    return result.empty() ? "0" : result;
}
```

### Example 4: Smallest Permutation with Given Condition

**Problem:** Find lexicographically smallest permutation of 1..n where adjacent differences satisfy certain conditions.

```cpp
vector<int> smallestPermutation(int n, vector<pair<int, int>>& constraints) {
    vector<int> result(n);
    vector<bool> used(n + 1, false);
    
    for (int i = 0; i < n; i++) {
        for (int val = 1; val <= n; val++) {
            if (used[val]) continue;
            
            // Check if placing val at position i violates any constraint
            bool valid = true;
            for (auto& [pos, condition] : constraints) {
                // Check constraints that involve this position
            }
            
            if (valid) {
                result[i] = val;
                used[val] = true;
                break;
            }
        }
    }
    
    return result;
}
```

### Example 5: Smallest String After Swaps

**Problem:** Given a string and allowed swap positions, find lexicographically smallest string after any number of swaps.

```cpp
string smallestStringAfterSwaps(string s, vector<pair<int, int>>& allowedSwaps) {
    int n = s.length();
    vector<vector<int>> adj(n);
    
    for (auto& swap : allowedSwaps) {
        adj[swap.first].push_back(swap.second);
        adj[swap.second].push_back(swap.first);
    }
    
    vector<bool> visited(n, false);
    string result = s;
    
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            // Find connected component via BFS/DFS
            vector<int> component;
            queue<int> q;
            q.push(i);
            visited[i] = true;
            
            while (!q.empty()) {
                int u = q.front();
                q.pop();
                component.push_back(u);
                
                for (int v : adj[u]) {
                    if (!visited[v]) {
                        visited[v] = true;
                        q.push(v);
                    }
                }
            }
            
            // Sort characters within component
            vector<char> chars;
            for (int idx : component) {
                chars.push_back(s[idx]);
            }
            sort(chars.begin(), chars.end());
            sort(component.begin(), component.end());
            
            for (int j = 0; j < component.size(); j++) {
                result[component[j]] = chars[j];
            }
        }
    }
    
    return result;
}
```

### Greedy Strategy Summary

| Problem Type | Greedy Approach |
|--------------|-----------------|
| Smallest number with digit sum | Fill largest digits at the end |
| Remove K digits | Remove larger left digits when possible |
| Smallest subsequence | Use monotonic stack |
| Permutation with constraints | Try smallest valid at each position |
| String after swaps | Sort within connected components |

### Time Complexity

Typically O(n²) for simple greedy, O(n log n) with optimizations
---

## Next Step

- Go to [16_Maximum_Sum_after_K_Negations.md](16_Maximum_Sum_after_K_Negations.md) to continue with Maximum Sum after K Negations.
