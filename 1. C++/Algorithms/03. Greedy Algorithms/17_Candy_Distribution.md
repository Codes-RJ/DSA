# 17_Candy_Distribution.md

## Candy Distribution Problem

### Definition

There are n children standing in a line. Each child has a rating. You want to give candies to these children such that:

1. Each child gets at least 1 candy
2. Children with a higher rating get more candies than their neighbors

Find the minimum total candies needed.

### Problem Statement

Input:
- An array ratings[0..n-1] representing each child's rating

Output:
- Minimum total candies to distribute

### Greedy Strategy

**Strategy:** Make two passes: left to right, then right to left.

**Why this works:** The left pass ensures each child has more candies than the left neighbor if rating is higher. The right pass ensures each child has more candies than the right neighbor if rating is higher.

### Algorithm

```
Step 1: Initialize candies array with 1 for each child
Step 2: Left to right pass:
        for i from 1 to n-1:
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
Step 3: Right to left pass:
        for i from n-2 down to 0:
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
Step 4: Return sum of candies
```

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int candyDistribution(vector<int>& ratings) {
    int n = ratings.size();
    vector<int> candies(n, 1);
    
    // Left to right pass
    for (int i = 1; i < n; i++) {
        if (ratings[i] > ratings[i-1]) {
            candies[i] = candies[i-1] + 1;
        }
    }
    
    // Right to left pass
    for (int i = n - 2; i >= 0; i--) {
        if (ratings[i] > ratings[i+1]) {
            candies[i] = max(candies[i], candies[i+1] + 1);
        }
    }
    
    int total = 0;
    for (int c : candies) {
        total += c;
    }
    
    return total;
}

int main() {
    vector<int> ratings = {1, 0, 2};
    int result = candyDistribution(ratings);
    cout << "Minimum candies: " << result << endl;
    
    return 0;
}
```

### Example Walkthrough

```
Example 1:
ratings = [1, 0, 2]

Step 1: Initialize candies = [1, 1, 1]

Step 2: Left to right pass
    i=1: ratings[1]=0 > ratings[0]=1? No → candies[1]=1
    i=2: ratings[2]=2 > ratings[1]=0? Yes → candies[2]=candies[1]+1=2
    candies = [1, 1, 2]

Step 3: Right to left pass
    i=1: ratings[1]=0 > ratings[2]=2? No → candies[1]=max(1, ?)=1
    i=0: ratings[0]=1 > ratings[1]=0? Yes → candies[0]=max(1, candies[1]+1=2)=2
    candies = [2, 1, 2]

Total = 2+1+2 = 5

Example 2:
ratings = [1, 2, 2]

Step 1: Initialize candies = [1, 1, 1]

Step 2: Left to right
    i=1: 2>1? Yes → candies[1]=2
    i=2: 2>2? No → candies[2]=1
    candies = [1, 2, 1]

Step 3: Right to left
    i=1: 2>2? No → candies[1]=max(2, ?)=2
    i=0: 1>2? No → candies[0]=max(1, ?)=1
    candies = [1, 2, 1]

Total = 1+2+1 = 4

Example 3:
ratings = [1, 3, 2, 1]

Step 1: Initialize candies = [1, 1, 1, 1]

Step 2: Left to right
    i=1: 3>1? Yes → candies[1]=2
    i=2: 2>3? No → candies[2]=1
    i=3: 1>2? No → candies[3]=1
    candies = [1, 2, 1, 1]

Step 3: Right to left
    i=2: 2>1? Yes → candies[2]=max(1, candies[3]+1=2)=2
    i=1: 3>2? Yes → candies[1]=max(2, candies[2]+1=3)=3
    i=0: 1>3? No → candies[0]=1
    candies = [1, 3, 2, 1]

Total = 1+3+2+1 = 7
```

### Space Optimized Version (No Extra Array)

```cpp
int candyDistributionOptimized(vector<int>& ratings) {
    int n = ratings.size();
    if (n == 1) return 1;
    
    int total = 0;
    int i = 0;
    
    while (i < n) {
        // Find increasing sequence
        int incLen = 1;
        while (i + incLen < n && ratings[i + incLen] > ratings[i + incLen - 1]) {
            incLen++;
        }
        
        // Find decreasing sequence
        int decLen = 1;
        while (i + decLen < n && ratings[i + decLen] < ratings[i + decLen - 1]) {
            decLen++;
        }
        
        // Add candies for this segment
        total += (incLen * (incLen + 1)) / 2;
        total += (decLen * (decLen + 1)) / 2;
        total -= incLen;  // peak counted twice
        
        i += incLen + decLen - 1;
    }
    
    return total;
}
```

### Time Complexity

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Two-pass array | O(n) | O(n) |
| Space optimized | O(n) | O(1) |

### Variations

#### 1. Candies with Adjacent Constraint Only

Same as above.

#### 2. Candies with Circular Arrangement

Children in a circle (first and last are neighbors).

#### 3. Minimum Candies with Different Increments

Instead of +1, use variable increments.

#### 4. Candies with Equal Rating Rule

If equal rating, neighbors can have same candies (already handled).

### Proof of Optimality

**Left Pass:** Ensures all increasing sequences are satisfied with minimal increments.

**Right Pass:** Ensures all decreasing sequences are satisfied without breaking left pass constraints.

**Minimality:** Each child gets exactly 1 plus the number of consecutive increasing or decreasing neighbors. This is the minimum possible.

### Real-World Applications

| Application | Description |
|-------------|-------------|
| Grade distribution | Fairly assign rewards based on performance |
| Salary increments | Distribute raises based on performance ranking |
| Resource allocation | Distribute resources based on priority |
