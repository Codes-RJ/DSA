# 04_Fractional_Knapsack.md

## Fractional Knapsack

### Definition

Given items with weight and value, fill a knapsack of capacity W to maximize total value. Unlike 0/1 knapsack, you can take fractions of items.

### Problem Statement

Input:
- Capacity W of the knapsack
- Array of weights w[0..n-1]
- Array of values v[0..n-1]

Output:
- Maximum total value achievable (can take fractions)

### Greedy Strategy

**Strategy:** Take items with the highest value-to-weight ratio first.

**Why this works:** Since items are divisible, the best strategy is to fill the knapsack with the most valuable substance per unit weight.

### Algorithm

```
Step 1: Calculate value/weight ratio for each item
Step 2: Sort items by ratio in descending order
Step 3: For each item in sorted order:
        if remaining capacity >= weight of item:
            take entire item
            remaining capacity -= weight
        else:
            take fraction = remaining capacity / weight
            add value = fraction * value
            break
Step 4: Return total value
```

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

struct Item {
    int weight;
    int value;
    double ratio;
};

bool compare(Item a, Item b) {
    return a.ratio > b.ratio;
}

double fractionalKnapsack(int W, vector<Item>& items) {
    // Calculate value/weight ratio
    for (auto& item : items) {
        item.ratio = (double)item.value / item.weight;
    }
    
    // Sort by ratio descending
    sort(items.begin(), items.end(), compare);
    
    double totalValue = 0.0;
    int remainingCapacity = W;
    
    for (Item item : items) {
        if (remainingCapacity >= item.weight) {
            // Take whole item
            totalValue += item.value;
            remainingCapacity -= item.weight;
        } else {
            // Take fraction of item
            double fraction = (double)remainingCapacity / item.weight;
            totalValue += item.value * fraction;
            break;
        }
    }
    
    return totalValue;
}

int main() {
    int W = 50;
    vector<Item> items = {
        {10, 60},   // weight=10, value=60, ratio=6.0
        {20, 100},  // weight=20, value=100, ratio=5.0
        {30, 120}   // weight=30, value=120, ratio=4.0
    };
    
    double result = fractionalKnapsack(W, items);
    cout << fixed << setprecision(2);
    cout << "Maximum value: " << result << endl;
    
    return 0;
}
```

### Example Walkthrough

```
Knapsack capacity = 50

Items:
Item 1: weight=10, value=60, ratio=6.0
Item 2: weight=20, value=100, ratio=5.0
Item 3: weight=30, value=120, ratio=4.0

Step 1: Sort by ratio (already sorted)
Item 1 (ratio 6.0)
Item 2 (ratio 5.0)
Item 3 (ratio 4.0)

Step 2: Process Item 1
    capacity=50 >= weight=10 → take whole
    value = 60, remaining capacity = 40

Step 3: Process Item 2
    capacity=40 >= weight=20 → take whole
    value = 60 + 100 = 160, remaining capacity = 20

Step 4: Process Item 3
    capacity=20 < weight=30 → take fraction
    fraction = 20/30 = 2/3
    value = 160 + 120 * (2/3) = 160 + 80 = 240

Result: Maximum value = 240
```

### With Fraction Tracking

```cpp
struct TakeItem {
    int index;
    double fraction;
};

vector<TakeItem> getFractionalSelection(int W, vector<Item>& items) {
    for (auto& item : items) {
        item.ratio = (double)item.value / item.weight;
    }
    
    sort(items.begin(), items.end(), compare);
    
    vector<TakeItem> selected;
    int remainingCapacity = W;
    
    for (int i = 0; i < items.size(); i++) {
        if (remainingCapacity >= items[i].weight) {
            selected.push_back({i, 1.0});
            remainingCapacity -= items[i].weight;
        } else if (remainingCapacity > 0) {
            double fraction = (double)remainingCapacity / items[i].weight;
            selected.push_back({i, fraction});
            break;
        }
    }
    
    return selected;
}
```

### Time Complexity

| Operation | Complexity |
|-----------|------------|
| Ratio calculation | O(n) |
| Sorting | O(n log n) |
| Selection | O(n) |
| Total | O(n log n) |

### Space Complexity

O(1) extra space (excluding input)

### Fractional vs 0/1 Knapsack

| Aspect | Fractional Knapsack | 0/1 Knapsack |
|--------|--------------------|--------------|
| Item divisibility | Yes | No |
| Solution method | Greedy | Dynamic Programming |
| Time complexity | O(n log n) | O(n × W) |
| Optimality | Always optimal | Always optimal |

### Why Greedy Works for Fractional but Not for 0/1

In fractional knapsack, if you have two items with different value/weight ratios, you can always replace part of a lower-ratio item with a higher-ratio item to increase total value. This exchange property does not hold for 0/1 knapsack because you cannot take partial items.

### Variations

#### 1. Fractional Knapsack with Constraints

Some items may have maximum take limits.

#### 2. Minimization Problem

Fill knapsack to exactly capacity with minimum value.

#### 3. Multiple Knapsacks

Distribute items across multiple knapsacks.

#### 4. Profit Maximization with Minimum Weight

Achieve minimum profit with maximum weight.

### Real-World Applications

| Application | Description |
|-------------|-------------|
| Resource Allocation | Distribute limited resources for maximum return |
| Investment Portfolio | Allocate funds to investments with best returns |
| Diet Planning | Maximize nutrition within calorie limits |
| Inventory Management | Stock highest margin products first |
| Oil Refining | Mix different crude oils for maximum profit |

### Proof of Optimality

**Exchange Argument:**

Let O be an optimal solution.
Let G be the greedy solution.

If O and G differ, there exists an item i with higher ratio taken in G that is not fully taken in O, and an item j with lower ratio taken in O.

Replace some amount of j with same amount of i.
Since ratio(i) > ratio(j), the total value increases.

This contradicts optimality of O.
Therefore, G must be optimal.
