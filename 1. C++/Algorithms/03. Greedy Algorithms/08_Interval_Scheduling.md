# 08_Interval_Scheduling.md

## Interval Scheduling

### Definition

Given a set of intervals (start time, end time), select the maximum number of non-overlapping intervals. This is identical to the activity selection problem.

### Problem Statement

Input:
- An array of intervals with start and end times

Output:
- Maximum number of non-overlapping intervals that can be scheduled

### Greedy Strategy

**Strategy:** Always select the interval with the earliest finish time.

**Why this works:** Choosing the interval that finishes earliest leaves the maximum remaining time for other intervals.

### Algorithm

```
Step 1: Sort intervals by finish time
Step 2: Select the first interval
Step 3: For each remaining interval:
        if start time >= last selected finish time:
            select it
            update last finish time
```

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Interval {
    int start;
    int end;
};

bool compare(Interval a, Interval b) {
    return a.end < b.end;
}

int intervalScheduling(vector<Interval>& intervals) {
    if (intervals.empty()) return 0;
    
    // Sort by finish time
    sort(intervals.begin(), intervals.end(), compare);
    
    int count = 1;
    int lastEnd = intervals[0].end;
    
    for (int i = 1; i < intervals.size(); i++) {
        if (intervals[i].start >= lastEnd) {
            count++;
            lastEnd = intervals[i].end;
        }
    }
    
    return count;
}

int main() {
    vector<Interval> intervals = {
        {1, 3}, {2, 5}, {3, 9}, {6, 8}, {8, 10}, {5, 7}, {4, 6}
    };
    
    int result = intervalScheduling(intervals);
    cout << "Maximum non-overlapping intervals: " << result << endl;
    
    return 0;
}
```

### Example Walkthrough

```
Intervals: (1,3), (2,5), (3,9), (6,8), (8,10), (5,7), (4,6)

Step 1: Sort by finish time
(1,3), (2,5), (4,6), (5,7), (6,8), (3,9), (8,10)

Step 2: Select (1,3), lastEnd = 3

Step 3: Check (2,5): start=2 < lastEnd=3 → skip
Step 4: Check (4,6): start=4 >= 3 → select, lastEnd=6
Step 5: Check (5,7): start=5 < 6 → skip
Step 6: Check (6,8): start=6 >= 6 → select, lastEnd=8
Step 7: Check (3,9): start=3 < 8 → skip
Step 8: Check (8,10): start=8 >= 8 → select, lastEnd=10

Result: 4 intervals selected
```

### Getting the Selected Intervals

```cpp
vector<Interval> getSelectedIntervals(vector<Interval>& intervals) {
    sort(intervals.begin(), intervals.end(), compare);
    
    vector<Interval> selected;
    selected.push_back(intervals[0]);
    
    int lastEnd = intervals[0].end;
    
    for (int i = 1; i < intervals.size(); i++) {
        if (intervals[i].start >= lastEnd) {
            selected.push_back(intervals[i]);
            lastEnd = intervals[i].end;
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

O(1) extra space (excluding output)

### Variations

#### 1. Weighted Interval Scheduling

**Problem:** Each interval has a weight. Maximize total weight instead of count.

**Solution:** Use dynamic programming (not greedy).

```cpp
struct WeightedInterval {
    int start, end, weight;
};

int weightedIntervalScheduling(vector<WeightedInterval>& intervals) {
    sort(intervals.begin(), intervals.end(), 
         [](WeightedInterval a, WeightedInterval b) {
             return a.end < b.end;
         });
    
    int n = intervals.size();
    vector<int> dp(n + 1, 0);
    
    for (int i = 1; i <= n; i++) {
        // Find last interval that doesn't conflict with i
        int lastNonConflict = 0;
        for (int j = i - 1; j >= 1; j--) {
            if (intervals[j-1].end <= intervals[i-1].start) {
                lastNonConflict = j;
                break;
            }
        }
        
        dp[i] = max(dp[i-1], dp[lastNonConflict] + intervals[i-1].weight);
    }
    
    return dp[n];
}
```

#### 2. Minimum Number of Intervals to Remove

**Problem:** Remove minimum intervals to make all non-overlapping.

**Solution:** Total intervals - maximum non-overlapping intervals.

```cpp
int minRemoveIntervals(vector<Interval>& intervals) {
    int n = intervals.size();
    int maxKeep = intervalScheduling(intervals);
    return n - maxKeep;
}
```

#### 3. Maximum Length of Non-Overlapping Intervals

**Problem:** Maximize total length of selected non-overlapping intervals.

**Solution:** Use DP (not greedy).

#### 4. Interval Scheduling with Machine Constraints

**Problem:** Schedule intervals on multiple identical machines.

**Solution:** Use interval partitioning (covered next).

### Proof of Optimality

**Greedy Choice Property:** There exists an optimal solution that includes the interval with the earliest finish time.

**Proof:**
- Let O be an optimal solution
- Let g be the interval with earliest finish time
- If g is in O, done
- If g is not in O, let f be the first interval in O (earliest finish in O)
- Since g finishes earlier than f, replacing f with g gives a new solution O'
- O' is still valid (g finishes earlier, so conflicts with fewer intervals)
- O' has the same number of intervals as O
- Therefore, there exists an optimal solution containing g

### Comparison with Other Strategies

| Strategy | Result | Optimal? |
|----------|--------|----------|
| Earliest start time | Not optimal | No |
| Shortest duration | Not optimal | No |
| Earliest finish time | Optimal | Yes |
| Latest start time | Not optimal | No |

### Real-World Applications

| Application | Description |
|-------------|-------------|
| Task scheduling | Schedule tasks on a single machine |
| TV program scheduling | Record maximum shows |
| Hotel room booking | Maximize bookings |
| Exam scheduling | Schedule exams without conflict |
| Flight scheduling | Assign runways to flights |
---

## Next Step

- Go to [09_Interval_Partitioning.md](09_Interval_Partitioning.md) to continue with Interval Partitioning.
