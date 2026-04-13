# 13_Minimum_Cost_to_Connect_Sticks.md

## Minimum Cost to Connect Sticks

### Definition

You have n sticks with given lengths. You can connect two sticks at a cost equal to the sum of their lengths. The resulting stick becomes a new stick. Find the minimum cost to connect all sticks into one stick.

### Problem Statement

Input:
- An array of stick lengths

Output:
- Minimum total cost to connect all sticks

### Greedy Strategy

**Strategy:** Always connect the two smallest sticks first.

**Why this works:** This is the optimal merge pattern. Connecting smaller sticks first minimizes the number of times longer sticks are added to the total cost.

### Algorithm

```
Step 1: Insert all stick lengths into a min-heap (priority queue)
Step 2: While heap has more than one element:
        Extract two smallest sticks
        cost += sum of the two
        Push the sum back into heap
Step 3: Return total cost
```

### Implementation

```cpp
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int minCostToConnectSticks(vector<int>& sticks) {
    priority_queue<int, vector<int>, greater<int>> pq;
    
    for (int len : sticks) {
        pq.push(len);
    }
    
    int totalCost = 0;
    
    while (pq.size() > 1) {
        int first = pq.top(); pq.pop();
        int second = pq.top(); pq.pop();
        
        int cost = first + second;
        totalCost += cost;
        pq.push(cost);
    }
    
    return totalCost;
}

int main() {
    vector<int> sticks = {2, 4, 3, 6};
    int result = minCostToConnectSticks(sticks);
    cout << "Minimum cost: " << result << endl;
    
    return 0;
}
```

### Example Walkthrough

```
Sticks: [2, 4, 3, 6]

Step 1: Insert into heap → [2, 3, 4, 6]

Step 2: Extract 2 and 3 → cost = 5, totalCost = 5, push 5 → heap = [4, 5, 6]

Step 3: Extract 4 and 5 → cost = 9, totalCost = 14, push 9 → heap = [6, 9]

Step 4: Extract 6 and 9 → cost = 15, totalCost = 29, push 15 → heap = [15]

Result: Minimum cost = 29

Explanation of cost accumulation:
- Connect 2 and 3 (cost 5) → sticks become [4, 5, 6]
- Connect 4 and 5 (cost 9) → sticks become [6, 9]
- Connect 6 and 9 (cost 15) → sticks become [15]
Total = 5 + 9 + 15 = 29
```

### Why Greedy Works

If you connect larger sticks first, they get added to the cost multiple times.

Example: Connecting 6 and 4 first (cost 10), then with 3 (cost 13), then with 2 (cost 15) → total = 10+13+15=38 (worse than 29)

### Time Complexity

| Operation | Complexity |
|-----------|------------|
| Building heap | O(n) |
| Each merge (n-1 merges) | O(log n) |
| Total | O(n log n) |

### Space Complexity

O(n) for the heap

### Variations

#### 1. Connect Sticks with Unlimited Operations

Same as above.

#### 2. Minimum Cost to Merge Files

Same problem. Used in optimal merge patterns for external sorting.

#### 3. Connect Ropes

Same problem (minimum cost to connect ropes).

```cpp
int minCostToConnectRopes(vector<int>& ropes) {
    return minCostToConnectSticks(ropes);
}
```

#### 4. K-way Merge

When you can merge k sticks at a time, use k-ary Huffman coding.

### Real-World Applications

| Application | Description |
|-------------|-------------|
| File merging | Merge sorted files optimally |
| Cable connections | Join cables with minimum cost |
| Pipeline construction | Connect pipes with minimum welding cost |
| Data compression | Huffman coding (same principle) |
---

## Next Step

- Go to [14_Gas_Station_Problem.md](14_Gas_Station_Problem.md) to continue with Gas Station Problem.
