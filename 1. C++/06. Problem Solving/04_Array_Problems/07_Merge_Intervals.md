# Merge Intervals in C++ - Sorting, Boundary Merging, and Range Intersections

## 1. Introduction & Theoretical Foundations

An **interval** is represented as a pair $[start, end]$ where $start \le end$, describing a continuous range on the real number line.
Interval problems occur extensively in calendar scheduling, database query optimization, resource allocation, and computational geometry.

The **Merge Intervals** problem requires taking an array of intervals and merging all overlapping intervals, returning an array of non-overlapping intervals that cover all the intervals in the input.

```
Input:   [1, 3], [2, 6], [8, 10], [15, 18]

Visual Timeline:
   0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
   ───[─────]───────────────[──────]─────────────[─────────]──  [1, 3], [8, 10], [15, 18]
   ──────[─────────]──────────────────────────────────────────  [2, 6] (Overlaps [1, 3]!)

Merged:
   ───[────────────]────────[──────]─────────────[─────────]──
      [1, 6]                 [8, 10]              [15, 18]
```

---

## 2. Mathematical Sorting & Overlap Invariant

Two intervals $A = [s_A, e_A]$ and $B = [s_B, e_B]$ with $s_A \le s_B$ overlap if and only if:
$$s_B \le e_A$$

### The 3 Overlap Cases:
1. **Disjoint ($s_B > e_A$)**: No overlap. $B$ begins strictly after $A$ ends.
2. **Partial Overlap ($s_A \le s_B \le e_A < e_B$)**: $B$ extends $A$. Merged interval is $[s_A, e_B]$.
3. **Complete Containment ($s_A \le s_B \le e_B \le e_A$)**: $B$ is entirely inside $A$. Merged interval is $[s_A, e_A]$.

By pre-sorting all intervals in ascending order of their start times:
$$s_0 \le s_1 \le s_2 \le \dots \le s_{N-1}$$
We guarantee that any interval can only ever overlap with its immediate preceding merged interval!

---

## 3. Production-Grade C++ Implementation

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

struct Interval {
    int start;
    int end;

    bool operator==(const Interval& other) const {
        return start == other.start && end == other.end;
    }
};

class IntervalOperations {
public:
    // 1. Merge Overlapping Intervals: O(N log N) time, O(1) auxiliary space (excluding result)
    static std::vector<Interval> merge(std::vector<Interval>& intervals) {
        if (intervals.size() <= 1) return intervals;

        // Sort intervals strictly by start time
        std::sort(intervals.begin(), intervals.end(), [](const Interval& a, const Interval& b) {
            return a.start < b.start;
        });

        std::vector<Interval> merged;
        merged.push_back(intervals[0]);

        for (size_t i = 1; i < intervals.size(); ++i) {
            Interval& last = merged.back();
            const Interval& curr = intervals[i];

            if (curr.start <= last.end) {
                // Overlap detected: extend the end of the last merged interval
                last.end = std::max(last.end, curr.end);
            } else {
                // Disjoint interval: push as new entry
                merged.push_back(curr);
            }
        }
        return merged;
    }

    // 2. Insert Interval into Sorted Non-Overlapping List: O(N) time, O(1) space
    static std::vector<Interval> insert(const std::vector<Interval>& intervals, Interval newInterval) {
        std::vector<Interval> result;
        size_t i = 0;
        size_t n = intervals.size();

        // Phase 1: Add all intervals ending strictly before newInterval starts
        while (i < n && intervals[i].end < newInterval.start) {
            result.push_back(intervals[i++]);
        }

        // Phase 2: Merge all overlapping intervals with newInterval
        while (i < n && intervals[i].start <= newInterval.end) {
            newInterval.start = std::min(newInterval.start, intervals[i].start);
            newInterval.end = std::max(newInterval.end, intervals[i].end);
            i++;
        }
        result.push_back(newInterval);

        // Phase 3: Add all remaining intervals starting after newInterval ends
        while (i < n) {
            result.push_back(intervals[i++]);
        }

        return result;
    }

    // 3. Interval List Intersections: O(N + M) time
    static std::vector<Interval> intervalIntersection(const std::vector<Interval>& firstList,
                                                      const std::vector<Interval>& secondList) {
        std::vector<Interval> intersections;
        size_t i = 0, j = 0;

        while (i < firstList.size() && j < secondList.size()) {
            // Find intersection boundary
            int startBound = std::max(firstList[i].start, secondList[j].start);
            int endBound = std::min(firstList[i].end, secondList[j].end);

            if (startBound <= endBound) {
                intersections.push_back({startBound, endBound});
            }

            // Advance the pointer whose interval ends first
            if (firstList[i].end < secondList[j].end) {
                i++;
            } else {
                j++;
            }
        }
        return intersections;
    }
};
```

---

## 4. Complete Runnable Verification Suite

```cpp
#include <iostream>
#include <vector>

void printIntervals(const std::vector<Interval>& list) {
    std::cout << "[ ";
    for (size_t i = 0; i < list.size(); ++i) {
        std::cout << "[" << list[i].start << ", " << list[i].end << "]";
        if (i + 1 < list.size()) std::cout << ", ";
    }
    std::cout << " ]" << std::endl;
}

int main() {
    std::cout << "=====================================================" << std::endl;
    std::cout << "          INTERVAL MERGING ALGORITHMIC SUITE         " << std::endl;
    std::cout << "=====================================================" << std::endl;

    // --- 1. Classic Overlapping Merge ---
    std::cout << "\n[1] MERGE OVERLAPPING INTERVALS:" << std::endl;
    std::vector<Interval> intervals = {{1, 3}, {2, 6}, {8, 10}, {15, 18}};
    std::cout << "  Input:  ";
    printIntervals(intervals);
    auto merged = IntervalOperations::merge(intervals);
    std::cout << "  Merged: ";
    printIntervals(merged);

    // --- 2. Insert Interval ---
    std::cout << "\n[2] INSERT INTERVAL:" << std::endl;
    std::vector<Interval> sortedList = {{1, 2}, {3, 5}, {6, 7}, {8, 10}, {12, 16}};
    Interval toInsert = {4, 8};
    std::cout << "  Existing:   ";
    printIntervals(sortedList);
    std::cout << "  To Insert:  [" << toInsert.start << ", " << toInsert.end << "]" << std::endl;
    auto afterInsert = IntervalOperations::insert(sortedList, toInsert);
    std::cout << "  Result:     ";
    printIntervals(afterInsert);

    // --- 3. Interval List Intersections ---
    std::cout << "\n[3] INTERVAL LIST INTERSECTIONS:" << std::endl;
    std::vector<Interval> listA = {{0, 2}, {5, 10}, {13, 23}, {24, 25}};
    std::vector<Interval> listB = {{1, 5}, {8, 12}, {15, 24}, {25, 26}};
    std::cout << "  List A: ";
    printIntervals(listA);
    std::cout << "  List B: ";
    printIntervals(listB);
    auto intersects = IntervalOperations::intervalIntersection(listA, listB);
    std::cout << "  Intersect: ";
    printIntervals(intersects);

    std::cout << "\n=====================================================" << std::endl;
    return 0;
}
```

---

## 5. Complexity Analysis Table

| Problem | Algorithm | Time Complexity | Auxiliary Space | Bottleneck |
| :--- | :--- | :--- | :--- | :--- |
| **Merge Intervals** | Sort + 1-Pass Linear Scan | $O(N \log N)$ | $O(1)$ extra | Sorting intervals by start time |
| **Insert Interval** | 3-Phase Linear Partition | $O(N)$ | $O(1)$ extra | Single pass over array |
| **Interval Intersection**| Two Pointers Synchronous | $O(N + M)$ | $O(1)$ extra | Single pass across both lists |

---

## 6. Common Pitfalls & Interview Traps

1. **Sorting by End Time Fallacy**: Sorting by `end` time works for Activity Selection (Greedy), but **fails** for merging intervals because an interval starting very early but ending late would swallow earlier intervals.
2. **Forgetting `std::max` on Merged Ends**: Assuming `last.end = curr.end` fails when `curr` is completely contained within `last` (e.g., `[1, 5]` and `[2, 3]` merged should remain `[1, 5]`, not `[1, 3]`). Always write `last.end = std::max(last.end, curr.end)`.
3. **Missing Equality on Boundary Touches**: In problems where $[1, 2]$ and $[2, 3]$ overlap, using strict `<` fails to merge them. The condition must be `curr.start <= last.end`.

---

## Next Step

- Proceed to [08_Container_With_Most_Water.md](08_Container_With_Most_Water.md) to explore the optimal two-pointer area shrinking strategy in C++.
