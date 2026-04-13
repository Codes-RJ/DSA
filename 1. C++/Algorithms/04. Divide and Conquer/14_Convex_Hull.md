# 14_Convex_Hull.md

## Convex Hull (Graham Scan and Divide and Conquer)

### Definition

The convex hull of a set of points is the smallest convex polygon that contains all the points. It is the boundary of the convex set containing all points.

### Problem Statement

Input:
- A set of n points in 2D plane

Output:
- The vertices of the convex hull in counterclockwise order

### Visual Example

```
Points: (0,0), (1,1), (2,2), (3,1), (4,0), (2,-1)

Convex hull vertices: (0,0), (4,0), (3,1), (2,2), (1,1) - wait, need correct order

Actually: (0,0) → (4,0) → (3,1) → (2,2) → (1,1) → back to (0,0)
```

### Divide and Conquer Approach

```
Step 1: Sort points by x-coordinate
Step 2: Divide points into left and right halves
Step 3: Recursively find convex hull of left half
Step 4: Recursively find convex hull of right half
Step 5: Merge the two convex hulls into one
```

### Implementation (Divide and Conquer)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

struct Point {
    double x, y;
    
    Point(double x = 0, double y = 0) : x(x), y(y) {}
    
    bool operator==(const Point& other) const {
        return x == other.x && y == other.y;
    }
};

// Cross product (orientation)
double cross(const Point& O, const Point& A, const Point& B) {
    return (A.x - O.x) * (B.y - O.y) - (A.y - O.y) * (B.x - O.x);
}

// Distance squared
double distSq(const Point& A, const Point& B) {
    return (A.x - B.x) * (A.x - B.x) + (A.y - B.y) * (A.y - B.y);
}

// Compare points by polar angle
bool compareAngle(const Point& pivot, const Point& a, const Point& b) {
    double crossVal = cross(pivot, a, b);
    if (crossVal == 0) {
        return distSq(pivot, a) < distSq(pivot, b);
    }
    return crossVal > 0;
}

// Graham Scan for convex hull of a set of points
vector<Point> grahamScan(vector<Point>& points) {
    if (points.size() <= 1) return points;
    
    // Find point with lowest y (and leftmost if tie)
    int bottom = 0;
    for (int i = 1; i < points.size(); i++) {
        if (points[i].y < points[bottom].y ||
            (points[i].y == points[bottom].y && points[i].x < points[bottom].x)) {
            bottom = i;
        }
    }
    
    swap(points[0], points[bottom]);
    Point pivot = points[0];
    
    // Sort by polar angle
    sort(points.begin() + 1, points.end(),
         [&pivot](const Point& a, const Point& b) {
             return compareAngle(pivot, a, b);
         });
    
    // Build hull
    vector<Point> hull;
    hull.push_back(points[0]);
    hull.push_back(points[1]);
    
    for (int i = 2; i < points.size(); i++) {
        while (hull.size() >= 2 &&
               cross(hull[hull.size() - 2], hull.back(), points[i]) <= 0) {
            hull.pop_back();
        }
        hull.push_back(points[i]);
    }
    
    return hull;
}

// Merge two convex hulls
vector<Point> mergeHulls(vector<Point>& leftHull, vector<Point>& rightHull) {
    int n = leftHull.size();
    int m = rightHull.size();
    
    // Find rightmost point in left hull and leftmost point in right hull
    int leftRightmost = 0;
    int rightLeftmost = 0;
    
    for (int i = 1; i < n; i++) {
        if (leftHull[i].x > leftHull[leftRightmost].x) {
            leftRightmost = i;
        }
    }
    
    for (int i = 1; i < m; i++) {
        if (rightHull[i].x < rightHull[rightLeftmost].x) {
            rightLeftmost = i;
        }
    }
    
    // Find upper tangent
    int upperLeft = leftRightmost;
    int upperRight = rightLeftmost;
    bool changed = true;
    
    while (changed) {
        changed = false;
        
        while (cross(rightHull[upperRight], leftHull[upperLeft],
                     leftHull[(upperLeft - 1 + n) % n]) > 0) {
            upperLeft = (upperLeft - 1 + n) % n;
            changed = true;
        }
        
        while (cross(leftHull[upperLeft], rightHull[upperRight],
                     rightHull[(upperRight + 1) % m]) < 0) {
            upperRight = (upperRight + 1) % m;
            changed = true;
        }
    }
    
    // Find lower tangent
    int lowerLeft = leftRightmost;
    int lowerRight = rightLeftmost;
    changed = true;
    
    while (changed) {
        changed = false;
        
        while (cross(rightHull[lowerRight], leftHull[lowerLeft],
                     leftHull[(lowerLeft + 1) % n]) < 0) {
            lowerLeft = (lowerLeft + 1) % n;
            changed = true;
        }
        
        while (cross(leftHull[lowerLeft], rightHull[lowerRight],
                     rightHull[(lowerRight - 1 + m) % m]) > 0) {
            lowerRight = (lowerRight - 1 + m) % m;
            changed = true;
        }
    }
    
    // Build merged hull
    vector<Point> merged;
    
    // Add left hull from upperLeft to lowerLeft
    int i = upperLeft;
    while (true) {
        merged.push_back(leftHull[i]);
        if (i == lowerLeft) break;
        i = (i + 1) % n;
    }
    
    // Add right hull from lowerRight to upperRight
    int j = lowerRight;
    while (true) {
        merged.push_back(rightHull[j]);
        if (j == upperRight) break;
        j = (j + 1) % m;
    }
    
    return merged;
}

vector<Point> convexHullDC(vector<Point>& points, int left, int right) {
    if (right - left <= 2) {
        // Base case: small set, use brute force or Graham Scan
        vector<Point> subset(points.begin() + left, points.begin() + right + 1);
        return grahamScan(subset);
    }
    
    int mid = left + (right - left) / 2;
    
    vector<Point> leftHull = convexHullDC(points, left, mid);
    vector<Point> rightHull = convexHullDC(points, mid + 1, right);
    
    return mergeHulls(leftHull, rightHull);
}

int main() {
    vector<Point> points = {
        {0, 0}, {1, 1}, {2, 2}, {3, 1}, {4, 0}, {2, -1}
    };
    
    // Sort by x-coordinate
    sort(points.begin(), points.end(),
         [](const Point& a, const Point& b) {
             return a.x < b.x;
         });
    
    vector<Point> hull = convexHullDC(points, 0, points.size() - 1);
    
    cout << "Convex Hull vertices:" << endl;
    for (Point p : hull) {
        cout << "(" << p.x << ", " << p.y << ")" << endl;
    }
    
    return 0;
}
```

### Graham Scan (Simpler Alternative)

```cpp
vector<Point> convexHullGraham(vector<Point>& points) {
    int n = points.size();
    if (n <= 1) return points;
    
    // Find bottom-most point
    int bottom = 0;
    for (int i = 1; i < n; i++) {
        if (points[i].y < points[bottom].y ||
            (points[i].y == points[bottom].y && points[i].x < points[bottom].x)) {
            bottom = i;
        }
    }
    
    swap(points[0], points[bottom]);
    Point pivot = points[0];
    
    // Sort by polar angle
    sort(points.begin() + 1, points.end(),
         [&pivot](const Point& a, const Point& b) {
             double crossVal = cross(pivot, a, b);
             if (crossVal == 0) {
                 return distSq(pivot, a) < distSq(pivot, b);
             }
             return crossVal > 0;
         });
    
    // Build hull
    vector<Point> hull;
    hull.push_back(points[0]);
    hull.push_back(points[1]);
    
    for (int i = 2; i < n; i++) {
        while (hull.size() >= 2 &&
               cross(hull[hull.size() - 2], hull.back(), points[i]) <= 0) {
            hull.pop_back();
        }
        hull.push_back(points[i]);
    }
    
    return hull;
}
```

### Time Complexity

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Brute Force | O(n³) | O(n) |
| Graham Scan | O(n log n) | O(n) |
| Divide and Conquer | O(n log n) | O(n log n) |
| Jarvis March | O(nh) where h is hull size | O(n) |

### Applications

| Application | Description |
|-------------|-------------|
| Image processing | Shape analysis |
| Computer graphics | Collision detection |
| Geographic information systems | Finding boundaries |
| Pattern recognition | Shape classification |
| Robotics | Path planning |

### Practice Problems

1. Find convex hull of given points
2. Check if a point is inside convex hull
3. Find area of convex hull
4. Find farthest pair of points (diameter of convex hull)
5. Find minimum area enclosing rectangle
---

## Next Step

- Go to [15_Master_Theorem.md](15_Master_Theorem.md) to continue with Master Theorem.
