# 07_Minimum_Number_of_Platforms.md

## Minimum Number of Platforms

### Definition

Given arrival and departure times of trains at a railway station, find the minimum number of platforms required so that no train has to wait.

### Problem Statement

Input:
- An array of arrival times arr[0..n-1]
- An array of departure times dep[0..n-1]

Output:
- Minimum number of platforms needed

### Greedy Strategy

**Strategy:** Sort both arrival and departure times separately. Use two pointers to simulate the timeline. When a train arrives, increase platform count. When a train departs, decrease platform count.

**Why this works:** This approach tracks the maximum number of overlapping intervals at any point in time.

### Algorithm

```
Step 1: Sort arrival array
Step 2: Sort departure array
Step 3: Initialize platforms = 0, maxPlatforms = 0
Step 4: Initialize i = 0 (arrival pointer), j = 0 (departure pointer)
Step 5: While i < n:
        if arr[i] <= dep[j]:
            platforms++
            maxPlatforms = max(maxPlatforms, platforms)
            i++
        else:
            platforms--
            j++
Step 6: Return maxPlatforms
```

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int findMinPlatforms(vector<int>& arr, vector<int>& dep) {
    int n = arr.size();
    
    // Sort arrival and departure times
    sort(arr.begin(), arr.end());
    sort(dep.begin(), dep.end());
    
    int platforms = 0;
    int maxPlatforms = 0;
    int i = 0;  // pointer for arrivals
    int j = 0;  // pointer for departures
    
    while (i < n) {
        if (arr[i] <= dep[j]) {
            platforms++;
            maxPlatforms = max(maxPlatforms, platforms);
            i++;
        } else {
            platforms--;
            j++;
        }
    }
    
    return maxPlatforms;
}

int main() {
    vector<int> arr = {900, 940, 950, 1100, 1500, 1800};
    vector<int> dep = {910, 1200, 1120, 1130, 1900, 2000};
    
    int result = findMinPlatforms(arr, dep);
    cout << "Minimum platforms needed: " << result << endl;
    
    return 0;
}
```

### Example Walkthrough

```
Trains:
Train 1: arr=900,  dep=910
Train 2: arr=940,  dep=1200
Train 3: arr=950,  dep=1120
Train 4: arr=1100, dep=1130
Train 5: arr=1500, dep=1900
Train 6: arr=1800, dep=2000

Step 1: Sort arrivals:  900, 940, 950, 1100, 1500, 1800
Step 2: Sort departures: 910, 1120, 1130, 1200, 1900, 2000

Timeline simulation:

i=0, j=0: arr=900 <= dep=910 → platforms=1, max=1, i=1
i=1, j=0: arr=940 <= dep=910? No → platforms=0, j=1
i=1, j=1: arr=940 <= dep=1120 → platforms=1, max=1, i=2
i=2, j=1: arr=950 <= dep=1120 → platforms=2, max=2, i=3
i=3, j=1: arr=1100 <= dep=1120 → platforms=3, max=3, i=4
i=4, j=1: arr=1500 <= dep=1120? No → platforms=2, j=2
i=4, j=2: arr=1500 <= dep=1130? No → platforms=1, j=3
i=4, j=3: arr=1500 <= dep=1200? No → platforms=0, j=4
i=4, j=4: arr=1500 <= dep=1900 → platforms=1, max=3, i=5
i=5, j=4: arr=1800 <= dep=1900 → platforms=2, max=3, i=6

Result: 3 platforms needed
```

### Printing Platform Assignment

```cpp
struct Train {
    int arr;
    int dep;
    int id;
};

vector<int> assignPlatforms(vector<Train>& trains) {
    int n = trains.size();
    
    // Sort trains by arrival time
    sort(trains.begin(), trains.end(), 
         [](Train a, Train b) { return a.arr < b.arr; });
    
    // Priority queue to track departure times of occupied platforms
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    
    vector<int> platformAssign(n);
    int nextPlatform = 0;
    
    for (Train train : trains) {
        if (!pq.empty() && pq.top().first <= train.arr) {
            // Free up a platform
            int freedPlatform = pq.top().second;
            pq.pop();
            platformAssign[train.id] = freedPlatform;
            pq.push({train.dep, freedPlatform});
        } else {
            // Need a new platform
            platformAssign[train.id] = nextPlatform;
            pq.push({train.dep, nextPlatform});
            nextPlatform++;
        }
    }
    
    return platformAssign;
}
```

### Time Complexity

| Operation | Complexity |
|-----------|------------|
| Sorting arrivals | O(n log n) |
| Sorting departures | O(n log n) |
| Two pointer scan | O(n) |
| Total | O(n log n) |

### Space Complexity

O(1) extra space (excluding input)

### Variations

#### 1. Minimum Platforms with Different Time Units

If times are not integers, same algorithm works with comparison operators.

#### 2. Minimum Meeting Rooms

Same as minimum platforms. Given meeting start and end times, find minimum rooms.

```cpp
int minMeetingRooms(vector<pair<int, int>>& meetings) {
    vector<int> starts, ends;
    for (auto& m : meetings) {
        starts.push_back(m.first);
        ends.push_back(m.second);
    }
    return findMinPlatforms(starts, ends);
}
```

#### 3. Maximum Number of Trains at Any Time

Same as minimum platforms (the maximum concurrent trains).

#### 4. Minimum Platforms with Buffer Time

Add buffer time before next train can use same platform.

```cpp
int findMinPlatformsWithBuffer(vector<int>& arr, vector<int>& dep, int buffer) {
    int n = arr.size();
    sort(arr.begin(), arr.end());
    sort(dep.begin(), dep.end());
    
    int platforms = 0;
    int maxPlatforms = 0;
    int i = 0, j = 0;
    
    while (i < n) {
        if (arr[i] <= dep[j] + buffer) {
            platforms++;
            maxPlatforms = max(maxPlatforms, platforms);
            i++;
        } else {
            platforms--;
            j++;
        }
    }
    
    return maxPlatforms;
}
```

### Proof of Optimality

**Greedy Choice Property:** At any point, if a train arrives, we need to assign it a platform. The optimal strategy is to always assign it to any available platform. The number of platforms needed at any time equals the number of overlapping intervals.

**Argument:** The maximum number of overlapping intervals is a lower bound on platforms needed. The algorithm achieves this bound by counting overlaps directly.

### Real-World Applications

| Application | Description |
|-------------|-------------|
| Railway stations | Schedule train platforms |
| Conference centers | Assign meeting rooms |
| Airport gates | Assign arrival/departure gates |
| Hospital emergency | Assign beds to patients |
| Call centers | Assign agents to calls |