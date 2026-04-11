# 14_Gas_Station_Problem.md

## Gas Station Problem

### Definition

There are n gas stations arranged in a circle. You have a car with an unlimited gas tank. You are given two arrays: gas[i] = amount of gas at station i, cost[i] = amount of gas needed to travel from station i to station i+1. Find the starting station index from which you can travel around the circuit once, or return -1 if impossible.

### Problem Statement

Input:
- gas array: gas available at each station
- cost array: gas needed to go to next station

Output:
- Starting station index (if possible)
- -1 if impossible

### Greedy Strategy

**Strategy:** If total gas < total cost, impossible. Otherwise, there is exactly one valid starting point. Start from station 0, track running balance. When balance becomes negative, reset start to next station.

**Why this works:** If you cannot reach station i+1 from start, no station between start and i can be a valid starting point.

### Algorithm

```
Step 1: Calculate total_gas = sum(gas), total_cost = sum(cost)
Step 2: If total_gas < total_cost, return -1
Step 3: Initialize start = 0, balance = 0
Step 4: For i from 0 to n-1:
        balance += gas[i] - cost[i]
        if balance < 0:
            start = i + 1
            balance = 0
Step 5: Return start
```

### Implementation

```cpp
#include <iostream>
#include <vector>
using namespace std;

int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
    int n = gas.size();
    
    int totalGas = 0;
    int totalCost = 0;
    for (int i = 0; i < n; i++) {
        totalGas += gas[i];
        totalCost += cost[i];
    }
    
    if (totalGas < totalCost) {
        return -1;
    }
    
    int start = 0;
    int balance = 0;
    
    for (int i = 0; i < n; i++) {
        balance += gas[i] - cost[i];
        
        if (balance < 0) {
            start = i + 1;
            balance = 0;
        }
    }
    
    return start;
}

int main() {
    vector<int> gas = {1, 2, 3, 4, 5};
    vector<int> cost = {3, 4, 5, 1, 2};
    
    int result = canCompleteCircuit(gas, cost);
    cout << "Starting station: " << result << endl;
    
    return 0;
}
```

### Example Walkthrough

```
gas  = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
diff = [-2, -2, -2, 3, 3]

total_gas = 15, total_cost = 15 → possible

start = 0, balance = 0

i=0: balance = 0 + (-2) = -2 → balance < 0 → start = 1, balance = 0
i=1: balance = 0 + (-2) = -2 → balance < 0 → start = 2, balance = 0
i=2: balance = 0 + (-2) = -2 → balance < 0 → start = 3, balance = 0
i=3: balance = 0 + 3 = 3 → balance >= 0
i=4: balance = 3 + 3 = 6 → balance >= 0

Result: start = 3

Verification:
Start at station 3: gas=4, cost=1 → remaining=3
Go to station 4: gas=5, cost=2 → remaining=3+5-2=6
Go to station 0: gas=1, cost=3 → remaining=6+1-3=4
Go to station 1: gas=2, cost=4 → remaining=4+2-4=2
Go to station 2: gas=3, cost=5 → remaining=2+3-5=0
Successfully completed circuit.
```

### Detailed Walkthrough with Balance Tracking

```
Stations:   0    1    2    3    4
gas:        1    2    3    4    5
cost:       3    4    5    1    2
diff:      -2   -2   -2    3    3

Method 2: Try each starting point

Start at 0: tank=0
    +1 =1, -3=-2 → fail at station 0 itself

Start at 1: tank=0
    +2=2, -4=-2 → fail at station 1

Start at 2: tank=0
    +3=3, -5=-2 → fail at station 2

Start at 3: tank=0
    +4=4, -1=3 → ok
    +5=8, -2=6 → ok
    +1=7, -3=4 → ok
    +2=6, -4=2 → ok
    +3=5, -5=0 → ok (complete)

Start at 4: tank=0
    +5=5, -2=3 → ok
    +1=4, -3=1 → ok
    +2=3, -4=-1 → fail at station 1
```

### Proof of Optimality

**Key Insight:** If you cannot reach station j from station i, then no station between i and j can be a valid starting point.

**Proof:**
- Let i be a starting point that fails at station j
- For any station k between i and j, the car starting at k would have less gas than starting at i when reaching k (because it skipped stations i through k-1)
- Since starting at i had negative balance at j, starting at k will have even worse balance
- Therefore, no station in [i, j] can be valid
- Reset start to j+1

### Time Complexity

O(n) for a single pass

### Space Complexity

O(1) extra space

### Variations

#### 1. Circular Tour with Limited Tank Capacity

Add constraint that tank cannot exceed capacity.

#### 2. Find All Possible Starting Stations

Can be multiple if total_gas == total_cost but with zero differences.

#### 3. Gas Station with Refueling at Different Rates

Different problem requiring DP.

### Real-World Applications

| Application | Description |
|-------------|-------------|
| Fleet management | Route planning for delivery trucks |
| Electric vehicles | Finding charging stations for long trips |
| Logistics | Fuel consumption optimization |
| Robotics | Energy management for autonomous robots |