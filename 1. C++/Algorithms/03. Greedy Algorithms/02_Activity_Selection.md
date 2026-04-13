# 02_Activity_Selection.md

## Activity Selection Problem

### Definition

Given n activities with start time and finish time, select the maximum number of activities that can be performed by a single person assuming that a person can only work on one activity at a time.

### Problem Statement

Input:
- An array of start times s[0..n-1]
- An array of finish times f[0..n-1]

Output:
- Maximum number of non-overlapping activities

### Greedy Strategy

**Strategy:** Always select the activity with the earliest finish time.

**Why this works:** Choosing the activity that finishes earliest leaves the maximum remaining time for other activities.

### Algorithm

```
Step 1: Sort activities by finish time
Step 2: Select the first activity (earliest finish)
Step 3: For each remaining activity:
    if start time >= last selected finish time:
        select this activity
        update last finish time
```

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Activity {
    int start;
    int finish;
};

bool compare(Activity a, Activity b) {
    return a.finish < b.finish;
}

int activitySelection(vector<Activity>& activities) {
    // Sort by finish time
    sort(activities.begin(), activities.end(), compare);
    
    int count = 1;  // First activity is always selected
    int lastFinish = activities[0].finish;
    
    for (int i = 1; i < activities.size(); i++) {
        if (activities[i].start >= lastFinish) {
            count++;
            lastFinish = activities[i].finish;
        }
    }
    
    return count;
}

int main() {
    vector<Activity> activities = {
        {1, 3}, {2, 5}, {3, 9}, {6, 8}, {8, 10}, {5, 7}, {4, 6}
    };
    
    int result = activitySelection(activities);
    cout << "Maximum number of activities: " << result << endl;
    
    return 0;
}
```

### Example Walkthrough

```
Activities:
(1, 3), (2, 5), (3, 9), (6, 8), (8, 10), (5, 7), (4, 6)

Step 1: Sort by finish time
(1, 3), (2, 5), (4, 6), (5, 7), (6, 8), (3, 9), (8, 10)

Step 2: Select (1, 3), lastFinish = 3

Step 3: Check (2, 5): start=2 < lastFinish=3 → skip

Step 4: Check (4, 6): start=4 >= lastFinish=3 → select, lastFinish=6

Step 5: Check (5, 7): start=5 < lastFinish=6 → skip

Step 6: Check (6, 8): start=6 >= lastFinish=6 → select, lastFinish=8

Step 7: Check (3, 9): start=3 < lastFinish=8 → skip

Step 8: Check (8, 10): start=8 >= lastFinish=8 → select, lastFinish=10

Result: 4 activities selected
Selected activities: (1,3), (4,6), (6,8), (8,10)
```

### Printing Selected Activities

```cpp
vector<Activity> getSelectedActivities(vector<Activity>& activities) {
    sort(activities.begin(), activities.end(), compare);
    
    vector<Activity> selected;
    selected.push_back(activities[0]);
    
    int lastFinish = activities[0].finish;
    
    for (int i = 1; i < activities.size(); i++) {
        if (activities[i].start >= lastFinish) {
            selected.push_back(activities[i]);
            lastFinish = activities[i].finish;
        }
    }
    
    return selected;
}
```

### Time Complexity

| Operation | Complexity |
|-----------|------------|
| Sorting | O(n log n) |
| Selection | O(n) |
| Total | O(n log n) |

### Space Complexity

O(1) extra space (excluding input storage)

### Variations

#### 1. Weighted Activity Selection

**Problem:** Each activity has a weight (profit). Maximize total profit instead of count.

**Solution:** Use dynamic programming (not greedy).

#### 2. Minimum Number of Rooms Required

**Problem:** Find minimum number of rooms to schedule all activities.

**Solution:** Use interval partitioning (covered later).

#### 3. Activity Selection with Multiple Persons

**Problem:** k persons available to perform activities.

**Solution:** Use greedy with multiple tracks.

#### 4. Maximum Length of Chain of Pairs

**Problem:** Form the longest chain of pairs where second element < first element of next.

**Solution:** Same as activity selection (sort by end time).

### Proof of Optimality

**Exchange Argument:**

Let O be an optimal solution with activities sorted by finish time.
Let G be the greedy solution.

Let the first activity in O be a (finish time f_a)
Let the first activity in G be g (finish time f_g)

Since g has the earliest finish time among all activities, f_g ≤ f_a.

Replace a with g in O. The new solution O' is still valid because:
- g finishes earlier than a, so it conflicts with fewer activities
- The number of activities in O' is same as O

By induction, the greedy solution is optimal.
---

## Next Step

- Go to [03_Job_Sequencing.md](03_Job_Sequencing.md) to continue with Job Sequencing.
