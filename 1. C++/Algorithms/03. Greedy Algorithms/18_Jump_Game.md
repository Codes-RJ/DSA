# 18_Jump_Game.md

## Jump Game

### Definition

You are given an array of non-negative integers. Each element represents the maximum jump length from that position. Determine if you can reach the last index starting from the first index.

### Problem Statement

Input:
- An array nums[0..n-1] where nums[i] is the maximum jump length from position i

Output:
- True if you can reach the last index, false otherwise

### Greedy Strategy

**Strategy:** Track the farthest reachable index as you iterate. If at any point you cannot move forward, return false.

**Why this works:** If you can reach a position, you can reach any position up to its farthest reachable point.

### Algorithm

```
Step 1: Initialize farthest = 0
Step 2: For i from 0 to n-1:
        if i > farthest: return false
        farthest = max(farthest, i + nums[i])
        if farthest >= n-1: return true
Step 3: Return true
```

### Implementation

```cpp
#include <iostream>
#include <vector>
using namespace std;

bool canJump(vector<int>& nums) {
    int n = nums.size();
    int farthest = 0;
    
    for (int i = 0; i < n; i++) {
        if (i > farthest) {
            return false;
        }
        farthest = max(farthest, i + nums[i]);
        if (farthest >= n - 1) {
            return true;
        }
    }
    
    return true;
}

int main() {
    vector<int> nums1 = {2, 3, 1, 1, 4};
    vector<int> nums2 = {3, 2, 1, 0, 4};
    
    cout << "Can jump (1): " << canJump(nums1) << endl;
    cout << "Can jump (2): " << canJump(nums2) << endl;
    
    return 0;
}
```

### Example Walkthrough

```
Example 1: nums = [2, 3, 1, 1, 4]

i=0: farthest = max(0, 0+2)=2
i=1: farthest = max(2, 1+3)=4 → farthest >= 4 → return true

Example 2: nums = [3, 2, 1, 0, 4]

i=0: farthest = max(0, 0+3)=3
i=1: farthest = max(3, 1+2)=3
i=2: farthest = max(3, 2+1)=3
i=3: farthest = max(3, 3+0)=3
i=4: i=4 > farthest=3 → return false
```

### Minimum Number of Jumps

**Problem:** Find the minimum number of jumps to reach the last index.

```cpp
int minJumps(vector<int>& nums) {
    int n = nums.size();
    if (n <= 1) return 0;
    
    int jumps = 0;
    int currentEnd = 0;
    int farthest = 0;
    
    for (int i = 0; i < n - 1; i++) {
        farthest = max(farthest, i + nums[i]);
        
        if (i == currentEnd) {
            jumps++;
            currentEnd = farthest;
            if (currentEnd >= n - 1) break;
        }
    }
    
    return jumps;
}
```

### Example Walkthrough for Min Jumps

```
nums = [2, 3, 1, 1, 4]

jumps=0, currentEnd=0, farthest=0

i=0: farthest = max(0, 0+2)=2
    i==currentEnd (0==0) → jumps=1, currentEnd=2

i=1: farthest = max(2, 1+3)=4
    i!=currentEnd (1!=2)

i=2: farthest = max(4, 2+1)=4
    i==currentEnd (2==2) → jumps=2, currentEnd=4

Result: 2 jumps
```

### Jump Game II (With Path Printing)

```cpp
vector<int> jumpPath(vector<int>& nums) {
    int n = nums.size();
    vector<int> jumps(n, INT_MAX);
    vector<int> parent(n, -1);
    
    jumps[0] = 0;
    
    for (int i = 0; i < n; i++) {
        for (int j = 1; j <= nums[i] && i + j < n; j++) {
            if (jumps[i] + 1 < jumps[i + j]) {
                jumps[i + j] = jumps[i] + 1;
                parent[i + j] = i;
            }
        }
    }
    
    // Reconstruct path
    vector<int> path;
    if (jumps[n-1] == INT_MAX) return path;
    
    for (int i = n-1; i != -1; i = parent[i]) {
        path.push_back(i);
    }
    reverse(path.begin(), path.end());
    
    return path;
}
```

### Time Complexity

| Problem | Time Complexity | Space Complexity |
|---------|----------------|------------------|
| Can Jump (greedy) | O(n) | O(1) |
| Min Jumps (greedy) | O(n) | O(1) |
| Min Jumps (DP) | O(n²) | O(n) |

### Variations

#### 1. Jump Game with Negative Numbers

If array can contain negative numbers (can move backward), use DP.

#### 2. Jump Game with Exact Steps

You must jump exactly the number shown, not up to.

#### 3. Jump Game with Cost

Each jump has a cost, minimize total cost to reach end.

#### 4. Jump Game with Obstacles

Some positions are blocked.

### Proof of Optimality

**For Can Jump:** The greedy algorithm always maintains the farthest reachable index. If you can't reach the end, no other path can because all paths are subsets of the reachable positions.

**For Min Jumps:** When you reach the end of the current jump range, the next jump should be to the position that extends the farthest. This is optimal because any other choice would not extend farther.

### Real-World Applications

| Application | Description |
|-------------|-------------|
| Game development | Character movement with jump power |
| Network routing | Packet forwarding with hop limits |
| Resource allocation | Minimum resources to reach target |
---

## Next Step

- Go to [19_Assign_Cookies.md](19_Assign_Cookies.md) to continue with Assign Cookies.
