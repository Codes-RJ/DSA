# 03_Bit_Masks.md

## Bit Masks

### Overview

A bit mask is a pattern of bits used to select or modify specific bits within a binary number. Bit masks are essential for representing sets, performing efficient subset enumeration, and implementing state in dynamic programming problems. They allow us to pack multiple boolean flags into a single integer, saving memory and enabling fast bitwise operations.

---

### 1. Representing Sets with Bit Masks

A bit mask can represent a subset of a set of n elements, where each bit corresponds to one element.

**Representation:**
- Bit i = 1 means element i is in the set
- Bit i = 0 means element i is not in the set

**Example with n = 4 (elements 0, 1, 2, 3):**

| Bitmask | Binary | Subset |
|---------|--------|--------|
| 0 | 0000 | {} |
| 1 | 0001 | {0} |
| 2 | 0010 | {1} |
| 3 | 0011 | {0, 1} |
| 4 | 0100 | {2} |
| 5 | 0101 | {0, 2} |
| 6 | 0110 | {1, 2} |
| 7 | 0111 | {0, 1, 2} |
| 8 | 1000 | {3} |
| 15 | 1111 | {0, 1, 2, 3} |

```cpp
#include <iostream>
#include <vector>
#include <bitset>
using namespace std;

void printSubset(int mask, int n) {
    cout << "{ ";
    for (int i = 0; i < n; i++) {
        if (mask & (1 << i)) {
            cout << i << " ";
        }
    }
    cout << "}";
}

int main() {
    int n = 4;
    cout << "Bitmask representation of subsets:" << endl;
    
    for (int mask = 0; mask < (1 << n); mask++) {
        cout << "mask = " << mask << " (" << bitset<4>(mask) << ") -> ";
        printSubset(mask, n);
        cout << endl;
    }
    
    return 0;
}
```

**Output:**
```
Bitmask representation of subsets:
mask = 0 (0000) -> { }
mask = 1 (0001) -> { 0 }
mask = 2 (0010) -> { 1 }
mask = 3 (0011) -> { 0 1 }
mask = 4 (0100) -> { 2 }
mask = 5 (0101) -> { 0 2 }
mask = 6 (0110) -> { 1 2 }
mask = 7 (0111) -> { 0 1 2 }
mask = 8 (1000) -> { 3 }
mask = 9 (1001) -> { 0 3 }
mask = 10 (1010) -> { 1 3 }
mask = 11 (1011) -> { 0 1 3 }
mask = 12 (1100) -> { 2 3 }
mask = 13 (1101) -> { 0 2 3 }
mask = 14 (1110) -> { 1 2 3 }
mask = 15 (1111) -> { 0 1 2 3 }
```

---

### 2. Basic Set Operations Using Bit Masks

| Operation | Expression | Description |
|-----------|------------|-------------|
| **Empty set** | `0` | No elements |
| **Universal set** | `(1 << n) - 1` | All n elements |
| **Add element i** | `mask \| (1 << i)` | Set bit i to 1 |
| **Remove element i** | `mask & ~(1 << i)` | Set bit i to 0 |
| **Check element i** | `(mask >> i) & 1` | Test if bit i is set |
| **Toggle element i** | `mask ^ (1 << i)` | Flip bit i |
| **Union** | `a \| b` | Elements in a or b |
| **Intersection** | `a & b` | Elements in both a and b |
| **Difference (a - b)** | `a & ~b` | Elements in a not in b |
| **Symmetric difference** | `a ^ b` | Elements in a or b but not both |
| **Subset check** | `(a & b) == a` | Is a subset of b? |
| **Size (popcount)** | `__builtin_popcount(mask)` | Number of elements |

```cpp
#include <iostream>
#include <bitset>
using namespace std;

void printSet(int mask, int n, const string& name) {
    cout << name << " = " << mask << " (" << bitset<5>(mask) << ") -> { ";
    for (int i = 0; i < n; i++) {
        if (mask & (1 << i)) {
            cout << i << " ";
        }
    }
    cout << "}" << endl;
}

int main() {
    int n = 5;
    int A = 0;
    int B = 0;
    
    // Add elements to set A: {0, 2, 4}
    A |= (1 << 0);
    A |= (1 << 2);
    A |= (1 << 4);
    
    // Add elements to set B: {1, 2, 3}
    B |= (1 << 1);
    B |= (1 << 2);
    B |= (1 << 3);
    
    printSet(A, n, "A");
    printSet(B, n, "B");
    cout << endl;
    
    // Set operations
    printSet(A | B, n, "A ∪ B");
    printSet(A & B, n, "A ∩ B");
    printSet(A & ~B, n, "A - B");
    printSet(B & ~A, n, "B - A");
    printSet(A ^ B, n, "A Δ B (symmetric difference)");
    
    // Check subset
    cout << "\nIs A subset of B? " << ((A & B) == A ? "Yes" : "No") << endl;
    cout << "Is {2} subset of A? " << (((1 << 2) & A) == (1 << 2) ? "Yes" : "No") << endl;
    
    // Size of sets
    cout << "\n|A| = " << __builtin_popcount(A) << endl;
    cout << "|B| = " << __builtin_popcount(B) << endl;
    
    return 0;
}
```

**Output:**
```
A = 21 (10101) -> { 0 2 4 }
B = 14 (01110) -> { 1 2 3 }

A ∪ B = 31 (11111) -> { 0 1 2 3 4 }
A ∩ B = 4 (00100) -> { 2 }
A - B = 17 (10001) -> { 0 4 }
B - A = 10 (01010) -> { 1 3 }
A Δ B = 27 (11011) -> { 0 1 3 4 }

Is A subset of B? No
Is {2} subset of A? Yes

|A| = 3
|B| = 3
```

---

### 3. Iterating Over All Subsets

There are 2ⁿ subsets of an n-element set.

```cpp
#include <iostream>
#include <vector>
using namespace std;

void generateAllSubsets(int n) {
    int total = 1 << n;  // 2^n
    cout << "Total subsets: " << total << endl;
    
    for (int mask = 0; mask < total; mask++) {
        cout << mask << ": ";
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) {
                cout << i << " ";
            }
        }
        cout << endl;
    }
}

// Generate subsets of a specific array
vector<vector<int>> subsets(vector<int>& nums) {
    int n = nums.size();
    vector<vector<int>> result;
    
    for (int mask = 0; mask < (1 << n); mask++) {
        vector<int> subset;
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) {
                subset.push_back(nums[i]);
            }
        }
        result.push_back(subset);
    }
    return result;
}

int main() {
    cout << "All subsets of {0, 1, 2}:" << endl;
    generateAllSubsets(3);
    
    cout << "\nSubsets of array [1, 2, 3]:" << endl;
    vector<int> arr = {1, 2, 3};
    vector<vector<int>> allSubsets = subsets(arr);
    
    for (auto& subset : allSubsets) {
        cout << "{ ";
        for (int x : subset) {
            cout << x << " ";
        }
        cout << "}" << endl;
    }
    
    return 0;
}
```

---

### 4. Iterating Over Submasks of a Mask

To iterate over all submasks of a given mask efficiently:

**Trick:** `sub = (sub - 1) & mask`

```cpp
#include <iostream>
#include <bitset>
using namespace std;

void iterateSubmasks(int mask, int n) {
    cout << "All submasks of " << mask << " (" << bitset<4>(mask) << "):" << endl;
    
    for (int sub = mask; sub; sub = (sub - 1) & mask) {
        cout << "  " << sub << " (" << bitset<4>(sub) << ") -> { ";
        for (int i = 0; i < n; i++) {
            if (sub & (1 << i)) {
                cout << i << " ";
            }
        }
        cout << "}" << endl;
    }
    cout << "  0 (empty set)" << endl;
}

int main() {
    int mask = 0b1101;  // bits 0, 2, 3 set (assuming 0-indexed)
    iterateSubmasks(mask, 4);
    
    return 0;
}
```

**Output:**
```
All submasks of 13 (1101):
  13 (1101) -> { 0 2 3 }
  12 (1100) -> { 2 3 }
  9 (1001) -> { 0 3 }
  8 (1000) -> { 3 }
  5 (0101) -> { 0 2 }
  4 (0100) -> { 2 }
  1 (0001) -> { 0 }
  0 (empty set)
```

---

### 5. Iterating Over All Subsets of Size k

Generating all subsets with exactly k elements (combinations).

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Method 1: Generate all masks and filter by popcount
vector<int> subsetsOfSizeK(int n, int k) {
    vector<int> result;
    for (int mask = 0; mask < (1 << n); mask++) {
        if (__builtin_popcount(mask) == k) {
            result.push_back(mask);
        }
    }
    return result;
}

// Method 2: Gosper's hack (next combination)
int nextCombination(int x) {
    int u = x & -x;
    int v = u + x;
    return v + (((v ^ x) / u) >> 2);
}

void iterateCombinations(int n, int k) {
    int mask = (1 << k) - 1;
    int limit = (1 << n);
    
    cout << "Combinations of size " << k << " from " << n << " elements:" << endl;
    
    while (mask < limit) {
        cout << mask << ": ";
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) {
                cout << i << " ";
            }
        }
        cout << endl;
        
        mask = nextCombination(mask);
    }
}

int main() {
    int n = 5, k = 3;
    
    cout << "Subsets of size " << k << " from " << n << " elements:" << endl;
    vector<int> masks = subsetsOfSizeK(n, k);
    
    for (int mask : masks) {
        cout << mask << ": ";
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) {
                cout << i << " ";
            }
        }
        cout << endl;
    }
    
    cout << "\nUsing Gosper's hack:" << endl;
    iterateCombinations(n, k);
    
    return 0;
}
```

---

### 6. Dynamic Programming with Bit Masks

Bit masks are commonly used in DP for problems like Traveling Salesman Problem (TSP), Set Cover, and Assignment Problem.

**Example: Assignment Problem (Minimum cost to assign n tasks to n workers)**

```cpp
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int assignmentProblem(vector<vector<int>>& cost) {
    int n = cost.size();
    vector<int> dp(1 << n, INT_MAX);
    dp[0] = 0;
    
    for (int mask = 0; mask < (1 << n); mask++) {
        int worker = __builtin_popcount(mask);
        
        for (int task = 0; task < n; task++) {
            if (!(mask & (1 << task))) {
                int newMask = mask | (1 << task);
                dp[newMask] = min(dp[newMask], dp[mask] + cost[worker][task]);
            }
        }
    }
    
    return dp[(1 << n) - 1];
}

int main() {
    vector<vector<int>> cost = {
        {9, 2, 7, 8},
        {6, 4, 3, 7},
        {5, 8, 1, 8},
        {7, 6, 9, 4}
    };
    
    int result = assignmentProblem(cost);
    cout << "Minimum assignment cost: " << result << endl;
    
    return 0;
}
```

**Output:**
```
Minimum assignment cost: 13
```

---

### 7. Real-World Applications

#### a) Flag Management

```cpp
#include <iostream>
using namespace std;

// Define flags
const int READ = 1 << 0;    // 1
const int WRITE = 1 << 1;   // 2
const int EXEC = 1 << 2;    // 4
const int DELETE = 1 << 3;  // 8

int main() {
    int permissions = 0;
    
    // Grant permissions
    permissions |= READ;
    permissions |= WRITE;
    cout << "Permissions: " << permissions << endl;
    
    // Check if has READ
    if (permissions & READ) {
        cout << "Has READ permission" << endl;
    }
    
    // Revoke WRITE
    permissions &= ~WRITE;
    cout << "After revoking WRITE: " << permissions << endl;
    
    // Has WRITE?
    if (!(permissions & WRITE)) {
        cout << "WRITE permission removed" << endl;
    }
    
    // Toggle EXEC
    permissions ^= EXEC;
    cout << "After toggling EXEC: " << permissions << endl;
    
    return 0;
}
```

#### b) Subset Sum Using Bit Mask

```cpp
#include <iostream>
#include <vector>
using namespace std;

bool subsetSum(vector<int>& nums, int target) {
    int n = nums.size();
    
    for (int mask = 0; mask < (1 << n); mask++) {
        int sum = 0;
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) {
                sum += nums[i];
            }
        }
        if (sum == target) {
            cout << "Subset found: ";
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) {
                    cout << nums[i] << " ";
                }
            }
            cout << endl;
            return true;
        }
    }
    return false;
}

int main() {
    vector<int> nums = {3, 34, 4, 12, 5, 2};
    int target = 9;
    
    if (subsetSum(nums, target)) {
        cout << "Subset with sum " << target << " exists" << endl;
    } else {
        cout << "No subset with sum " << target << endl;
    }
    
    return 0;
}
```

---

### Summary Table

| Operation | Expression | Example (mask = 0b1010, i=2) |
|-----------|------------|------------------------------|
| **Add element i** | `mask \| (1 << i)` | 1010 | 0100 = 1110 |
| **Remove element i** | `mask & ~(1 << i)` | 1010 & 1011 = 1010 |
| **Check element i** | `(mask >> i) & 1` | (1010 >> 2) & 1 = 10 & 1 = 0 |
| **Toggle element i** | `mask ^ (1 << i)` | 1010 ^ 0100 = 1110 |
| **Union** | `a \| b` | 1010 | 1100 = 1110 |
| **Intersection** | `a & b` | 1010 & 1100 = 1000 |
| **Difference** | `a & ~b` | 1010 & 0011 = 0010 |
| **Subset check** | `(a & b) == a` | (1010 & 1110) == 1010 ? Yes |

---

### Key Takeaways

1. **Bit masks** represent sets as integers, with each bit representing an element
2. **2ⁿ subsets** can be generated by iterating masks from 0 to (1 << n) - 1
3. **Set operations** become single bitwise operations (much faster than array operations)
4. **Submask iteration** can be done efficiently with `sub = (sub - 1) & mask`
5. **Dynamic programming** with bit masks solves exponential problems (TSP, assignment)
6. **Integer size** limits n to 64 for 64-bit integers (practical for n ≤ 20 in DP)

---

### Practice Questions

1. Write a function to add an element to a bitmask
2. Write a function to remove an element from a bitmask
3. Check if an element is present in a bitmask
4. Compute the union and intersection of two bitmasks
5. Generate all subsets of an array using bit masks
6. Find all subsets of size k using bit masks
7. Solve the subset sum problem using bit masks
8. Implement a bitmask-based solution for the assignment problem

---

### Next Steps

- Go to [04_Binary_Representation.md](04_Binary_Representation.md) for Binary Representation.