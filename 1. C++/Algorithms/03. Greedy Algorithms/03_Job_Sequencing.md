# 03_Job_Sequencing.md

## Job Sequencing with Deadlines

### Definition

Given a set of jobs, each with a deadline and profit, schedule the jobs to maximize total profit. Each job takes one unit of time. Only one job can be scheduled at a time.

### Problem Statement

Input:
- An array of deadlines d[0..n-1]
- An array of profits p[0..n-1]
- Each job takes exactly 1 unit of time

Output:
- Maximum profit achievable
- Sequence of jobs to schedule

### Greedy Strategy

**Strategy:** Sort jobs by profit in descending order. For each job, schedule it at the latest available slot before its deadline.

**Why this works:** Higher profit jobs should be prioritized, and scheduling them as late as possible leaves earlier slots for other jobs.

### Algorithm

```
Step 1: Sort jobs by profit in descending order
Step 2: Find maximum deadline to determine number of slots
Step 3: Create an array to track occupied slots (size = max deadline)
Step 4: For each job in sorted order:
        Find the latest free slot before deadline
        If found, assign job to that slot
        Add profit to total
Step 5: Return total profit
```

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

struct Job {
    int id;
    int deadline;
    int profit;
};

bool compare(Job a, Job b) {
    return a.profit > b.profit;
}

int jobSequencing(vector<Job>& jobs) {
    // Sort jobs by profit descending
    sort(jobs.begin(), jobs.end(), compare);
    
    // Find maximum deadline
    int maxDeadline = 0;
    for (Job j : jobs) {
        maxDeadline = max(maxDeadline, j.deadline);
    }
    
    // Array to track occupied slots (-1 means empty)
    vector<int> slot(maxDeadline + 1, -1);
    
    int totalProfit = 0;
    
    for (Job j : jobs) {
        // Find latest free slot before deadline
        for (int t = j.deadline; t >= 1; t--) {
            if (slot[t] == -1) {
                slot[t] = j.id;
                totalProfit += j.profit;
                break;
            }
        }
    }
    
    return totalProfit;
}

int main() {
    vector<Job> jobs = {
        {1, 4, 20},
        {2, 1, 10},
        {3, 1, 40},
        {4, 1, 30},
        {5, 3, 35}
    };
    
    int result = jobSequencing(jobs);
    cout << "Maximum profit: " << result << endl;
    
    return 0;
}
```

### Example Walkthrough

```
Jobs: (id, deadline, profit)
1: (1, 4, 20)
2: (2, 1, 10)
3: (3, 1, 40)
4: (4, 1, 30)
5: (5, 3, 35)

Step 1: Sort by profit descending
(3, 1, 40)
(5, 3, 35)
(4, 1, 30)
(1, 4, 20)
(2, 1, 10)

Step 2: maxDeadline = 4, slots[1..4] = empty

Step 3: Process Job 3 (deadline=1, profit=40)
    Check t=1 → empty, assign Job 3 to slot 1, profit=40

Step 4: Process Job 5 (deadline=3, profit=35)
    Check t=3 → empty, assign Job 5 to slot 3, profit=75

Step 5: Process Job 4 (deadline=1, profit=30)
    Check t=1 → occupied, skip

Step 6: Process Job 1 (deadline=4, profit=20)
    Check t=4 → empty, assign Job 1 to slot 4, profit=95

Step 7: Process Job 2 (deadline=1, profit=10)
    Check t=1 → occupied, skip

Result: Total profit = 95
Scheduled jobs: Slot1=Job3, Slot3=Job5, Slot4=Job1
```

### Printing the Schedule

```cpp
vector<int> getSchedule(vector<Job>& jobs) {
    sort(jobs.begin(), jobs.end(), compare);
    
    int maxDeadline = 0;
    for (Job j : jobs) {
        maxDeadline = max(maxDeadline, j.deadline);
    }
    
    vector<int> slot(maxDeadline + 1, -1);
    
    for (Job j : jobs) {
        for (int t = j.deadline; t >= 1; t--) {
            if (slot[t] == -1) {
                slot[t] = j.id;
                break;
            }
        }
    }
    
    return slot;
}
```

### Time Complexity

| Operation | Complexity |
|-----------|------------|
| Sorting | O(n log n) |
| Finding slots (naive) | O(n × d) where d = max deadline |
| Total | O(n log n + n × d) |

### Optimization with Disjoint Set Union (DSU)

We can optimize slot finding to O(1) using DSU.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Job {
    int id;
    int deadline;
    int profit;
};

bool compare(Job a, Job b) {
    return a.profit > b.profit;
}

vector<int> parent;

int find(int x) {
    if (parent[x] == x) return x;
    return parent[x] = find(parent[x]);
}

void unionSet(int x, int y) {
    parent[x] = y;
}

int jobSequencingOptimized(vector<Job>& jobs) {
    sort(jobs.begin(), jobs.end(), compare);
    
    int maxDeadline = 0;
    for (Job j : jobs) {
        maxDeadline = max(maxDeadline, j.deadline);
    }
    
    // Initialize DSU: parent[i] points to the latest free slot <= i
    parent.resize(maxDeadline + 2);
    for (int i = 0; i <= maxDeadline + 1; i++) {
        parent[i] = i;
    }
    
    vector<int> result(maxDeadline + 1, -1);
    int totalProfit = 0;
    
    for (Job j : jobs) {
        int availableSlot = find(j.deadline);
        
        if (availableSlot > 0) {
            result[availableSlot] = j.id;
            totalProfit += j.profit;
            unionSet(availableSlot, find(availableSlot - 1));
        }
    }
    
    return totalProfit;
}
```

### Complexity with DSU Optimization

| Operation | Complexity |
|-----------|------------|
| Sorting | O(n log n) |
| DSU operations | O(n × α(n)) where α is inverse Ackermann |
| Total | O(n log n) |

### Variations

#### 1. Jobs with Different Processing Times

If each job takes variable time, use DP instead of greedy.

#### 2. Jobs with Equal Profits

When profits are equal, any order works, but schedule as many as possible.

#### 3. Maximize Number of Jobs

If all profits are equal, schedule maximum number of jobs by earliest deadline first.

#### 4. Loss Minimization

If jobs have penalties instead of profits, minimize total penalty.

### Proof of Optimality

**Exchange Argument:**

Let O be an optimal schedule sorted by time slot.
Let G be the greedy schedule.

Consider the highest profit job j that is in O but not in G.
G scheduled some other job k in j's slot because j couldn't fit.
But profit(j) > profit(k) because greedy takes highest profit first.
Swapping j and k would increase profit, contradicting optimality of O.

Therefore, greedy must be optimal.