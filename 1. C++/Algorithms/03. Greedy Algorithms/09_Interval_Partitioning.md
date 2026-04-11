# 09_Interval_Partitioning.md

## Interval Partitioning (Minimum Number of Rooms)

### Definition

Given a set of intervals, partition them into the minimum number of subsets such that within each subset, no two intervals overlap. This is equivalent to finding the minimum number of resources (rooms, machines, platforms) needed to schedule all intervals.

### Problem Statement

Input:
- An array of intervals with start and end times

Output:
- Minimum number of rooms/resources needed
- Assignment of each interval to a room

### Greedy Strategy

**Strategy:** Process intervals in order of start time. For each interval, assign it to any available room. If no room is available, open a new room.

**Why this works:** The minimum number of rooms needed equals the maximum number of intervals that overlap at any point in time.

### Algorithm

```
Step 1: Sort intervals by start time
Step 2: Use a min-heap (priority queue) to track end times of occupied rooms
Step 3: For each interval in sorted order:
        if heap is not empty and earliest end time <= current start:
            reuse that room (pop and push new end time)
        else:
            open a new room (push current end time)
Step 4: Return heap size (number of rooms used)
```

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

struct Interval {
    int start;
    int end;
};

bool compare(Interval a, Interval b) {
    return a.start < b.start;
}

int intervalPartitioning(vector<Interval>& intervals) {
    if (intervals.empty()) return 0;
    
    // Sort by start time
    sort(intervals.begin(), intervals.end(), compare);
    
    // Min-heap to store end times of rooms
    priority_queue<int, vector<int>, greater<int>> pq;
    
    for (Interval interval : intervals) {
        if (!pq.empty() && pq.top() <= interval.start) {
            // Reuse the room
            pq.pop();
        }
        // Assign this interval to a room (either reused or new)
        pq.push(interval.end);
    }
    
    return pq.size();
}

int main() {
    vector<Interval> intervals = {
        {1, 4}, {2, 5}, {3, 6}, {5, 7}, {6, 9}, {8, 10}
    };
    
    int result = intervalPartitioning(intervals);
    cout << "Minimum rooms needed: " << result << endl;
    
    return 0;
}
```

### Example Walkthrough

```
Intervals: (1,4), (2,5), (3,6), (5,7), (6,9), (8,10)

Step 1: Sort by start time (already sorted)

Step 2: Process (1,4)
    heap empty → new room → heap = [4]

Step 3: Process (2,5)
    earliest end=4, 4 <= 2? No → new room → heap = [4,5]

Step 4: Process (3,6)
    earliest end=4, 4 <= 3? No → new room → heap = [4,5,6]

Step 5: Process (5,7)
    earliest end=4, 4 <= 5? Yes → reuse room, pop 4, push 7 → heap = [5,6,7]

Step 6: Process (6,9)
    earliest end=5, 5 <= 6? Yes → reuse room, pop 5, push 9 → heap = [6,7,9]

Step 7: Process (8,10)
    earliest end=6, 6 <= 8? Yes → reuse room, pop 6, push 10 → heap = [7,9,10]

Result: 3 rooms needed
```

### Assigning Room Numbers

```cpp
vector<int> assignRooms(vector<Interval>& intervals) {
    int n = intervals.size();
    
    // Store original indices
    vector<pair<Interval, int>> indexed;
    for (int i = 0; i < n; i++) {
        indexed.push_back({intervals[i], i});
    }
    
    // Sort by start time
    sort(indexed.begin(), indexed.end(), 
         [](auto a, auto b) { return a.first.start < b.first.start; });
    
    // Min-heap stores {end_time, room_number}
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    
    vector<int> roomAssignment(n);
    int nextRoom = 0;
    
    for (auto& [interval, idx] : indexed) {
        if (!pq.empty() && pq.top().first <= interval.start) {
            // Reuse the room
            int roomNum = pq.top().second;
            pq.pop();
            roomAssignment[idx] = roomNum;
            pq.push({interval.end, roomNum});
        } else {
            // New room
            roomAssignment[idx] = nextRoom;
            pq.push({interval.end, nextRoom});
            nextRoom++;
        }
    }
    
    return roomAssignment;
}
```

### Time Complexity

| Operation | Complexity |
|-----------|------------|
| Sorting | O(n log n) |
| Heap operations (n times) | O(n log n) |
| Total | O(n log n) |

### Space Complexity

O(n) for the heap

### Proof of Optimality

**Lower Bound:** At any point in time, if k intervals are overlapping, we need at least k rooms. The maximum overlap depth is a lower bound.

**Greedy Achieves Lower Bound:** The greedy algorithm never uses more rooms than the maximum overlap depth because:
- When a new room is opened, it's because all existing rooms are occupied
- That means the current interval overlaps with all existing rooms
- Therefore, the number of rooms equals the overlap depth at that moment
- The algorithm never exceeds the maximum overlap depth

### Variations

#### 1. Meeting Rooms II (LeetCode 253)

Same as interval partitioning.

#### 2. Minimum Number of Lecture Halls

Same as interval partitioning.

#### 3. Train Platforms

Same as interval partitioning (covered earlier).

#### 4. Color Intervals with Minimum Colors

Assign colors to intervals so that overlapping intervals have different colors. Minimum colors = maximum overlap depth.

```cpp
int minColors(vector<Interval>& intervals) {
    return intervalPartitioning(intervals);
}
```

### Comparison with Interval Scheduling

| Problem | Goal | Greedy Strategy |
|---------|------|-----------------|
| Interval Scheduling | Maximize non-overlapping intervals | Earliest finish time |
| Interval Partitioning | Minimize rooms for all intervals | Earliest start time + heap |

### Real-World Applications

| Application | Description |
|-------------|-------------|
| Conference rooms | Minimum rooms for all meetings |
| University scheduling | Minimum classrooms for courses |
| Airline gates | Minimum gates for flights |
| Hospital beds | Minimum beds for patients |
| CPU scheduling | Minimum cores for processes |
