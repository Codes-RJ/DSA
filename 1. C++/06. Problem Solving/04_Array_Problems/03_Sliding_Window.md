# Sliding Window: Masterclass in Multi-Point Navigation

## Overview
A sliding window is a powerful optimization pattern that reduces the number of operations in problems involving sub-ranges or subarrays. The main goal is to reuse the mathematical or logical state of the previous window to calculate the next one in $O(1)$ time, thereby reducing a global $O(N^2)$ problem down to $O(N)$.

---

## 1. Sliding Window with a Monotonic Queue
Finding the **Maximum of all subarrays of size K** in $O(N)$ is a common challenge.

**Strategy**: Use a `deque` to store indices of elements in the current window. Keep the deque **monotonic decreasing** so that the front always has the index of the largest element.

```cpp
#include <deque>
vector<int> maxSlidingWindow(vector<int>& arr, int k) {
    deque<int> dq;
    vector<int> res;

    for (int i = 0; i < arr.size(); i++) {
        // Remove elements that are out of this window
        if (!dq.empty() && dq.front() == i - k) dq.pop_front();

        // Remove elements smaller than the current one (they will never be the max)
        while (!dq.empty() && arr[dq.back()] < arr[i]) dq.pop_back();

        dq.push_back(i);

        // Store result once window is at size k
        if (i >= k - 1) res.push_back(arr[dq.front()]);
    }
    return res;
}
```

---

## 2. Dynamic Window: Longest Substring with K Distinct Characters
Use a `unordered_map` or frequency array to track counts and shrink the `left` boundary when the number of keys exceeds `k`.

```cpp
int longestSubstringKDistinct(string s, int k) {
    unordered_map<char, int> freq;
    int left = 0, maxLen = 0;

    for (int right = 0; right < s.length(); right++) {
        freq[s[right]]++;
        while (freq.size() > k) {
            if (--freq[s[left]] == 0) freq.erase(s[left]);
            left++;
        }
        maxLen = max(maxLen, right - left + 1);
    }
    return maxLen;
}
```

---

## 3. Minimum Window Substring: The Gold Standard
**Problem**: Find the smallest substring of `S` that contains all characters in `T`.

**The Three Step Solution**:
1. Increment `right` until the window contains all target characters.
2. Store the current window if smaller than the minimum found.
3. Increment `left` until the window no longer satisfies the condition, then repeat.

```cpp
string minWindow(string s, string t) {
    vector<int> target(128, 0), current(128, 0);
    for (char c : t) target[c]++;

    int left = 0, minLen = INT_MAX, count = 0, startIdx = -1;
    for (int right = 0; right < s.length(); right++) {
        if (++current[s[right]] <= target[s[right]]) count++;

        while (count == t.length()) { // Window is valid
            if (right - left + 1 < minLen) {
                minLen = right - left + 1;
                startIdx = left;
            }
            if (--current[s[left]] < target[s[left]]) count--;
            left++;
        }
    }
    return startIdx == -1 ? "" : s.substr(startIdx, minLen);
}
```

---

## 4. Key Considerations & Optimization
1. **At most K vs. Exactly K**: Often, "Exactly K" problems can be solved as `(At most K) - (At most K-1)`.
2. **Space vs. Time**: For ASCII strings, use `vector<int> freq(128, 0)` instead of `unordered_map` to avoid hashing overhead and speed up the $O(1)$ operations significantly.
3. **Array as Counter**: If possible, use direct indexing of an array for counts to improve cache locality.

---

## 5. Performance Comparison

| Type | Space Case | Time Case | Typical Complexity |
|------|------------|-----------|--------------------|
| **Fixed Window** | Subarray sum | $O(N)$ and $O(1)$ Space | $O(N)$ |
| **Monotonic Window** | Sliding Max/Min | $O(N)$ and $O(K)$ Space | $O(N)$ |
| **Variable Window** | Substring patterns | $O(N)$ and $O(\Sigma)$ Space | $O(N)$ |

*$\Sigma$ = size of alphabet.*

---

## Final Checklist
- [ ] Are indices verified to be within `[0, N-1]`?
- [ ] Is the update logic for the **outbound** element correct?
- [ ] Is the `left` pointer correctly advanced when the condition is violated?
- [ ] Handled edge cases: `k > n`, `empty string`, `target not in source`.
---

## Next Step

- Go to [04_Array_Rotation.md](04_Array_Rotation.md) to continue with Array Rotation.
