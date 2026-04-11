# 19_Assign_Cookies.md

## Assign Cookies

### Definition

You have children with greed factors and cookies with sizes. Each child can get at most one cookie. A child is satisfied if the cookie size is at least the child's greed factor. Find the maximum number of children that can be satisfied.

### Problem Statement

Input:
- Array g: greed factors of children
- Array s: sizes of cookies

Output:
- Maximum number of satisfied children

### Greedy Strategy

**Strategy:** Assign the smallest cookie that satisfies the least greedy child.

**Why this works:** Giving a larger cookie to a less greedy child wastes the cookie's potential. Giving the smallest sufficient cookie preserves larger cookies for greedier children.

### Algorithm

```
Step 1: Sort both arrays in ascending order
Step 2: Initialize i = 0 (child index), j = 0 (cookie index)
Step 3: While i < n and j < m:
        if s[j] >= g[i]:
            i++ (satisfy this child)
            j++ (use this cookie)
        else:
            j++ (skip this cookie, too small)
Step 4: Return i (number of satisfied children)
```

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int findContentChildren(vector<int>& g, vector<int>& s) {
    sort(g.begin(), g.end());
    sort(s.begin(), s.end());
    
    int i = 0;  // child index
    int j = 0;  // cookie index
    
    while (i < g.size() && j < s.size()) {
        if (s[j] >= g[i]) {
            i++;  // satisfy this child
        }
        j++;  // try next cookie
    }
    
    return i;
}

int main() {
    vector<int> greed = {1, 2, 3};
    vector<int> cookies = {1, 1};
    
    int result = findContentChildren(greed, cookies);
    cout << "Maximum satisfied children: " << result << endl;
    
    return 0;
}
```

### Example Walkthrough

```
Example 1:
g = [1, 2, 3]
s = [1, 1]

Step 1: Sort (already sorted)
Step 2: Process
    child=0 (g=1), cookie=0 (s=1): 1>=1 → satisfy, i=1, j=1
    child=1 (g=2), cookie=1 (s=1): 1>=2? No → j=2 (end)
Result: 1 child satisfied

Example 2:
g = [1, 2, 3]
s = [3, 2, 1]

Step 1: Sort
    g = [1, 2, 3]
    s = [1, 2, 3]

Step 2: Process
    child=0 (g=1), cookie=0 (s=1): 1>=1 → satisfy, i=1, j=1
    child=1 (g=2), cookie=1 (s=2): 2>=2 → satisfy, i=2, j=2
    child=2 (g=3), cookie=2 (s=3): 3>=3 → satisfy, i=3, j=3
Result: 3 children satisfied

Example 3:
g = [1, 2, 3, 4, 5]
s = [2, 3, 4]

Step 1: Sort (already sorted)
Step 2: Process
    child=0 (g=1), cookie=0 (s=2): 2>=1 → satisfy, i=1, j=1
    child=1 (g=2), cookie=1 (s=3): 3>=2 → satisfy, i=2, j=2
    child=2 (g=3), cookie=2 (s=4): 4>=3 → satisfy, i=3, j=3
    j=3 (end)
Result: 3 children satisfied
```

### Alternative Implementation (Using Multiset)

```cpp
#include <set>

int findContentChildrenMultiset(vector<int>& g, vector<int>& s) {
    sort(g.begin(), g.end());
    multiset<int> cookies(s.begin(), s.end());
    
    int satisfied = 0;
    
    for (int greedVal : g) {
        auto it = cookies.lower_bound(greedVal);
        if (it != cookies.end()) {
            satisfied++;
            cookies.erase(it);
        }
    }
    
    return satisfied;
}
```

### Time Complexity

| Operation | Complexity |
|-----------|------------|
| Sorting g | O(n log n) |
| Sorting s | O(m log m) |
| Two pointer scan | O(n + m) |
| Total | O(n log n + m log m) |

### Space Complexity

O(1) extra space (excluding input)

### Variations

#### 1. Each Child Can Get Multiple Cookies

Different problem, usually requires DP.

#### 2. Cookies Have Different Values

Maximize total satisfaction value (weighted matching).

#### 3. Children Have Maximum Cookie Limit

Each child can get up to k cookies.

#### 4. Minimum Cookie Waste

Minimize total unused cookie size while satisfying children.

### Proof of Optimality

**Greedy Choice Property:** There exists an optimal solution that assigns the smallest sufficient cookie to the least greedy child.

**Proof by Exchange:**
- Let O be an optimal solution
- Let c be the least greedy child
- Let x be the cookie assigned to c in O
- Let y be the smallest cookie that satisfies c
- If x != y, replace x with y in O
- y is at most as large as x, so it still satisfies c
- y might be used to satisfy some other child, but since y ≤ x, swapping doesn't hurt
- Therefore, there exists an optimal solution with the greedy choice

### Real-World Applications

| Application | Description |
|-------------|-------------|
| Resource allocation | Assign smallest sufficient resource |
| Job assignment | Assign smallest capable worker to job |
| Memory allocation | Assign smallest sufficient memory block |
| Scheduling | Assign smallest sufficient time slot |
