# 07_Closest_Pair_of_Points.md

## Closest Pair of Points

### Definition

Given n points in a 2D plane, find the pair of points with the smallest Euclidean distance between them.

### Problem Statement

Input:
- An array of n points (x, y coordinates)

Output:
- The minimum distance between any two points
- The pair of points that achieve this distance

### Brute Force Approach

Check all pairs: O(n²) time

### Divide and Conquer Approach

```
Step 1: Sort points by x-coordinate
Step 2: Divide points into left and right halves
Step 3: Recursively find closest pair in left half and right half
Step 4: Let d = min(d_left, d_right)
Step 5: Consider points within d of the dividing line (strip)
Step 6: Sort strip points by y-coordinate
Step 7: Check each point in strip against next 7 points
Step 8: Return minimum distance
```

### Visual Example

```
Points: (2,3), (12,30), (40,50), (5,1), (12,10), (3,4)

Sorted by x: (2,3), (3,4), (5,1), (12,10), (12,30), (40,50)

Divide at x ≈ 8.5

Left: (2,3), (3,4), (5,1)
Right: (12,10), (12,30), (40,50)

Recursively find:
d_left = distance((2,3), (3,4)) = sqrt(2) ≈ 1.414
d_right = distance((12,10), (12,30)) = 20

d = min(1.414, 20) = 1.414

Strip: points with |x - 8.5| < 1.414 → only left points (no cross pairs)
Minimum remains 1.414
```

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <limits>
using namespace std;

struct Point {
    double x, y;
    int id;  // optional: to identify the point
};

bool compareX(Point a, Point b) {
    return a.x < b.x;
}

bool compareY(Point a, Point b) {
    return a.y < b.y;
}

double distance(Point a, Point b) {
    double dx = a.x - b.x;
    double dy = a.y - b.y;
    return sqrt(dx*dx + dy*dy);
}

double bruteForce(vector<Point>& points, int left, int right, pair<Point, Point>& closest) {
    double minDist = numeric_limits<double>::max();
    
    for (int i = left; i <= right; i++) {
        for (int j = i + 1; j <= right; j++) {
            double dist = distance(points[i], points[j]);
            if (dist < minDist) {
                minDist = dist;
                closest = {points[i], points[j]};
            }
        }
    }
    
    return minDist;
}

double stripClosest(vector<Point>& strip, double d, pair<Point, Point>& closest) {
    double minDist = d;
    int n = strip.size();
    
    // Sort strip by y-coordinate
    sort(strip.begin(), strip.end(), compareY);
    
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n && (strip[j].y - strip[i].y) < minDist; j++) {
            double dist = distance(strip[i], strip[j]);
            if (dist < minDist) {
                minDist = dist;
                closest = {strip[i], strip[j]};
            }
        }
    }
    
    return minDist;
}

double closestPair(vector<Point>& points, int left, int right, pair<Point, Point>& closest) {
    if (right - left <= 3) {
        return bruteForce(points, left, right, closest);
    }
    
    int mid = left + (right - left) / 2;
    Point midPoint = points[mid];
    
    double dLeft = closestPair(points, left, mid, closest);
    double dRight = closestPair(points, mid + 1, right, closest);
    
    double d = min(dLeft, dRight);
    
    // Build strip
    vector<Point> strip;
    for (int i = left; i <= right; i++) {
        if (abs(points[i].x - midPoint.x) < d) {
            strip.push_back(points[i]);
        }
    }
    
    return min(d, stripClosest(strip, d, closest));
}

int main() {
    vector<Point> points = {
        {2, 3}, {12, 30}, {40, 50}, {5, 1}, {12, 10}, {3, 4}
    };
    
    // Sort by x-coordinate
    sort(points.begin(), points.end(), compareX);
    
    pair<Point, Point> closest;
    double minDist = closestPair(points, 0, points.size() - 1, closest);
    
    cout << "Closest distance: " << minDist << endl;
    cout << "Points: (" << closest.first.x << "," << closest.first.y << ")";
    cout << " and (" << closest.second.x << "," << closest.second.y << ")" << endl;
    
    return 0;
}
```

### Why Check Only 7 Points

In the strip, for any point, the next points within distance d in y-direction can be at most 7. This is because within a d × 2d rectangle, there can be at most 6 points (by the pigeonhole principle).

```
Rectangle of size d × 2d:
┌─────────────────────┐
│     d    │    d     │
│          │          │
│    •     │     •    │
│          │          │
│    •     │     •    │
│          │          │
│    •     │     •    │
└─────────────────────┘
Maximum 6 points (plus the current point)
```

### Time Complexity

| Step | Complexity |
|------|------------|
| Sorting by x | O(n log n) |
| Recursive division | O(log n) levels |
| Strip processing | O(n) per level |
| Total | O(n log n) |

### Space Complexity

O(n) for storing points and strip

### Variations

#### 1. Closest Pair in 3D

Extend to 3 dimensions (more complex, O(n log² n) using kd-trees)

#### 2. Closest Pair with Integer Coordinates

Can use bucketing for O(n) expected time

#### 3. All Pairs within Distance

Find all pairs with distance < threshold

#### 4. Farthest Pair (Diameter)

Different problem, uses rotating calipers

### Proof of Correctness

**Correctness:** The algorithm checks all possible pairs that could be closer than d. Any pair with distance < d must have both points within d of the dividing line (otherwise they'd be > d apart horizontally). Within that strip, they must be within d vertically. Since we check all points within vertical distance d, we find the minimum.

### Practice Problems

1. Find closest pair of points in 2D plane
2. Find closest pair of points on a line (simpler: sort and check neighbors)
3. Find closest pair of points with integer coordinates
4. Find all pairs with distance less than given threshold
5. Find the pair with maximum distance (diameter)