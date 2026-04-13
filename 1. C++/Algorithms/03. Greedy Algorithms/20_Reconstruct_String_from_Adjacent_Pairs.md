# 20_Reconstruct_String_from_Adjacent_Pairs.md

## Reconstruct String from Adjacent Pairs

### Definition

You are given a list of adjacent pairs representing neighboring characters in a string. Each pair [a, b] means that a and b are adjacent in the original string (order unknown). Reconstruct the original string.

### Problem Statement

Input:
- A 2D array pairs where pairs[i] = [u, v] indicates u and v are adjacent

Output:
- The reconstructed string (order of characters)

### Greedy Strategy

**Strategy:** Build a graph where edges represent adjacency. The first and last characters will have degree 1. Start from one end and traverse.

**Why this works:** In a path graph (each node appears in at most two pairs), the ends have degree 1. Following the chain reconstructs the string.

### Algorithm

```
Step 1: Build adjacency list for each character
Step 2: Find the character with degree 1 (start or end)
Step 3: Traverse from that character, always moving to an unvisited neighbor
Step 4: Build the string in order
```

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

string reconstructString(vector<vector<int>>& pairs) {
    unordered_map<int, vector<int>> adj;
    unordered_map<int, int> degree;
    
    // Build graph
    for (auto& pair : pairs) {
        int u = pair[0];
        int v = pair[1];
        adj[u].push_back(v);
        adj[v].push_back(u);
        degree[u]++;
        degree[v]++;
    }
    
    // Find starting node (degree 1)
    int start = -1;
    for (auto& [node, deg] : degree) {
        if (deg == 1) {
            start = node;
            break;
        }
    }
    
    // Traverse to build string
    vector<int> result;
    unordered_set<int> visited;
    int current = start;
    int prev = -1;
    
    while (true) {
        result.push_back(current);
        visited.insert(current);
        
        // Find next unvisited neighbor
        int next = -1;
        for (int neighbor : adj[current]) {
            if (!visited.count(neighbor)) {
                next = neighbor;
                break;
            }
        }
        
        if (next == -1) break;
        prev = current;
        current = next;
    }
    
    // Convert to string
    string s;
    for (int num : result) {
        s += char(num + '0');
    }
    
    return s;
}

int main() {
    vector<vector<int>> pairs = {{1, 2}, {2, 3}, {3, 4}};
    string result = reconstructString(pairs);
    cout << "Reconstructed string: " << result << endl;
    
    return 0;
}
```

### Example Walkthrough

```
Example 1:
pairs = [[1, 2], [2, 3], [3, 4]]

Adjacency:
1: [2]
2: [1, 3]
3: [2, 4]
4: [3]

Degrees: deg(1)=1, deg(2)=2, deg(3)=2, deg(4)=1
Start node: 1

Traversal:
current=1 → result=[1], next=2
current=2 → result=[1,2], next=3
current=3 → result=[1,2,3], next=4
current=4 → result=[1,2,3,4], next=-1

Result: "1234"

Example 2:
pairs = [[1, 2], [1, 3], [2, 4]]

Adjacency:
1: [2, 3]
2: [1, 4]
3: [1]
4: [2]

Degrees: deg(1)=2, deg(2)=2, deg(3)=1, deg(4)=1
Start node: 3

Traversal:
current=3 → result=[3], next=1
current=1 → result=[3,1], next=2 (or 3? 3 visited, so 2)
current=2 → result=[3,1,2], next=4
current=4 → result=[3,1,2,4], next=-1

Result: "3124" or "4213" depending on start
```

### Handling Different Data Types (String instead of Integers)

```cpp
string reconstructStringString(vector<pair<string, string>>& pairs) {
    unordered_map<string, vector<string>> adj;
    unordered_map<string, int> degree;
    
    for (auto& pair : pairs) {
        string u = pair.first;
        string v = pair.second;
        adj[u].push_back(v);
        adj[v].push_back(u);
        degree[u]++;
        degree[v]++;
    }
    
    string start;
    for (auto& [node, deg] : degree) {
        if (deg == 1) {
            start = node;
            break;
        }
    }
    
    vector<string> result;
    unordered_set<string> visited;
    string current = start;
    
    while (true) {
        result.push_back(current);
        visited.insert(current);
        
        string next = "";
        for (string neighbor : adj[current]) {
            if (!visited.count(neighbor)) {
                next = neighbor;
                break;
            }
        }
        
        if (next == "") break;
        current = next;
    }
    
    string s;
    for (string& str : result) {
        s += str;
    }
    
    return s;
}
```

### Time Complexity

| Operation | Complexity |
|-----------|------------|
| Building graph | O(n) |
| Finding start | O(n) |
| Traversal | O(n) |
| Total | O(n) |

### Space Complexity

O(n) for graph storage

### Variations

#### 1. Multiple Possible Strings

If there are multiple valid strings (ambiguous pairs), return any.

#### 2. String with Duplicate Adjacent Pairs

If pairs can contain duplicates, handle accordingly.

#### 3. Circular String

If the string is circular (no degree 1 nodes), start anywhere.

#### 4. Reconstruct from Adjacent Pairs with Order

If pairs indicate direction (a before b), use topological sort.

### Proof of Correctness

**Key Insight:** In a valid reconstruction, each character (except ends) appears in exactly two pairs (left and right neighbor). Ends appear in exactly one pair.

**Graph Property:** The adjacency graph forms a path (or multiple paths). By starting at a degree-1 node and following edges, we traverse the entire path.

### Real-World Applications

| Application | Description |
|-------------|-------------|
| DNA sequencing | Reconstruct sequence from fragments |
| String reconstruction | Recover original string from adjacent pairs |
| Puzzle solving | Reconstruct chain from neighboring pieces |
| Travel route | Reconstruct path from adjacent city pairs |
---

## Next Step

- Go to [21_Proof_of_Optimality.md](21_Proof_of_Optimality.md) to continue with Proof of Optimality.
