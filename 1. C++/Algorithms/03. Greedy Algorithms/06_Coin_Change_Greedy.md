# 06_Coin_Change_Greedy.md

## Coin Change (Greedy Approach)

### Definition

Given a set of coin denominations and a target amount, find the minimum number of coins needed to make that amount. The greedy approach works only for certain coin systems (canonical coin systems).

### Problem Statement

Input:
- An array of coin denominations coins[0..n-1]
- A target amount A

Output:
- Minimum number of coins needed (using greedy)
- Or indication that greedy fails

### Greedy Strategy

**Strategy:** Always take the largest coin that does not exceed the remaining amount.

**Works for:** Standard currency systems (1, 2, 5, 10, 20, 50, 100, 500, 1000)

**Fails for:** Arbitrary denominations like {1, 3, 4}

### Algorithm

```
Step 1: Sort coins in descending order
Step 2: Initialize count = 0, remaining = amount
Step 3: For each coin in sorted order:
        while remaining >= coin:
            remaining -= coin
            count++
Step 4: Return count
```

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int coinChangeGreedy(vector<int>& coins, int amount) {
    // Sort in descending order
    sort(coins.begin(), coins.end(), greater<int>());
    
    int count = 0;
    int remaining = amount;
    
    for (int coin : coins) {
        if (remaining >= coin) {
            int numCoins = remaining / coin;
            count += numCoins;
            remaining -= numCoins * coin;
        }
    }
    
    if (remaining > 0) {
        return -1;  // Cannot make exact amount
    }
    
    return count;
}

int main() {
    vector<int> coins = {1, 2, 5, 10, 20, 50, 100, 500, 1000};
    int amount = 93;
    
    int result = coinChangeGreedy(coins, amount);
    cout << "Minimum coins: " << result << endl;
    
    return 0;
}
```

### Example Walkthrough (Standard Coins)

```
Coins: [1000, 500, 100, 50, 20, 10, 5, 2, 1]
Amount: 93

Step 1: coin = 100, remaining=93 < 100 → skip
Step 2: coin = 50, 93/50 = 1 coin, remaining = 43, count=1
Step 3: coin = 20, 43/20 = 2 coins, remaining = 3, count=3
Step 4: coin = 10, 3 < 10 → skip
Step 5: coin = 5, 3 < 5 → skip
Step 6: coin = 2, 3/2 = 1 coin, remaining = 1, count=4
Step 7: coin = 1, 1/1 = 1 coin, remaining = 0, count=5

Result: 5 coins (50 + 20 + 20 + 2 + 1)
```

### Example Where Greedy Fails

```
Coins: [1, 3, 4]
Amount: 6

Greedy approach:
    coin=4 → 1 coin, remaining=2
    coin=1 → 2 coins, total=3 coins (4+1+1)

Optimal:
    3 + 3 = 2 coins

Greedy fails because 4+1+1 is worse than 3+3
```

### Checking if a Coin System is Canonical

A coin system is canonical if greedy always gives optimal solution.

```cpp
bool isCanonical(vector<int>& coins) {
    sort(coins.begin(), coins.end());
    int n = coins.size();
    
    for (int i = 1; i < n; i++) {
        int coin = coins[i];
        int maxCheck = coins[i] + coins[i-1] - 1;
        
        // Check all amounts up to maxCheck
        for (int amount = coins[i-1] + 1; amount <= maxCheck; amount++) {
            int greedyCount = coinChangeGreedy(coins, amount);
            int dpCount = coinChangeDP(coins, amount);
            
            if (greedyCount != dpCount) {
                return false;
            }
        }
    }
    
    return true;
}
```

### Greedy vs Dynamic Programming

| Aspect | Greedy | Dynamic Programming |
|--------|--------|---------------------|
| Time complexity | O(n log n) | O(n × amount) |
| Space complexity | O(1) | O(amount) |
| Optimality | Only for canonical systems | Always optimal |
| Use case | Standard currencies | Arbitrary denominations |

### Coin Change with Unlimited Coins (Greedy Version)

```cpp
vector<int> coinCombinationGreedy(vector<int>& coins, int amount) {
    sort(coins.begin(), coins.end(), greater<int>());
    
    vector<int> result;
    int remaining = amount;
    
    for (int coin : coins) {
        while (remaining >= coin) {
            result.push_back(coin);
            remaining -= coin;
        }
    }
    
    if (remaining > 0) {
        return {};  // Cannot make exact amount
    }
    
    return result;
}
```

### Minimizing Number of Different Coins

```cpp
pair<int, vector<int>> coinChangeWithDetails(vector<int>& coins, int amount) {
    sort(coins.begin(), coins.end(), greater<int>());
    
    vector<int> usedCoins;
    int remaining = amount;
    int totalCoins = 0;
    
    for (int coin : coins) {
        if (remaining >= coin) {
            int num = remaining / coin;
            totalCoins += num;
            for (int i = 0; i < num; i++) {
                usedCoins.push_back(coin);
            }
            remaining %= coin;
        }
    }
    
    return {remaining == 0 ? totalCoins : -1, usedCoins};
}
```

### Known Canonical Coin Systems

| Currency | Denominations |
|----------|---------------|
| Indian Rupee | 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000 |
| US Dollar | 1, 5, 10, 25, 50, 100 |
| Euro | 1, 2, 5, 10, 20, 50, 100, 200 |
| British Pound | 1, 2, 5, 10, 20, 50, 100, 200 |

### When Greedy Works

Greedy works when each coin is at least twice the previous coin:

```
If coins[i] >= 2 * coins[i-1] for all i, then greedy is optimal.

Example: 1, 2, 4, 8, 16, 32 (binary system)
```

### When Greedy Fails

Greedy fails when there is a "counterexample" amount where a combination of smaller coins beats the greedy choice.

Common failing systems:
- {1, 3, 4} (counterexample: 6)
- {1, 5, 10, 25} (works actually, this is US)
- {1, 6, 10} (counterexample: 12 → greedy: 10+1+1=3, optimal: 6+6=2)
---

## Next Step

- Go to [07_Minimum_Number_of_Platforms.md](07_Minimum_Number_of_Platforms.md) to continue with Minimum Number of Platforms.
