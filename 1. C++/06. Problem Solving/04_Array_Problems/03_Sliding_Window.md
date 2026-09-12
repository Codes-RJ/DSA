# Sliding Window Technique in C++ - Masterclass in Multi-Point Navigation

## 📖 Overview

The **Sliding Window Technique** is an optimization paradigm that transforms computational operations across contiguous subsegments (subarrays, substrings) from brute-force **$O(N^2)$** or **$O(N \cdot K)$** into linear **$O(N)$** time. 

By reusing the overlapping state between adjacent windows (adding the incoming element and evicting the outgoing element), each step executes in **$O(1)$ amortized time**.

---

## 🎯 Taxonomy: Fixed vs. Dynamic Windows

```
  1. Fixed-Size Window (Width = K)            2. Dynamic Window (Condition-Driven)
     [ a, b, c ] d  e  f                         [ a, b ] c  d  e  f   (Expand right)
        ├── Evict 'a'                              [ a, b, c, d ] e  f   (Violates condition!)
        └── Add 'd'                                   [ b, c, d ] e  f   (Shrink left to restore)
     a [ b, c, d ] e  f
```

### 1. Fixed-Size Sliding Window
- The window maintains a strictly fixed length $K$.
- As the window slides from index $i$ to $i+1$:
  $$\text{State}_{i+1} = \text{State}_i + \text{Element}[i + K] - \text{Element}[i]$$
- **Canonical Use Cases**: Maximum sum subarray of size $K$, moving averages, string anagram search.

### 2. Dynamic Sliding Window
- The window dynamically expands (`right++`) to accumulate elements until a constraint is reached, then contracts (`left++`) to restore invariants.
- **Canonical Use Cases**: Longest substring with $K$ unique characters, Minimum window substring, Subarray product less than $K$.

### 3. Monotonic Deque Sliding Window
- Maintains a **monotonically decreasing double-ended queue (`std::deque`)** of indices to report the current maximum/minimum of an arbitrary window in **$O(1)$ amortized time**.

---

## 📐 Amortized Proof: Monotonic Deque Sliding Window Maximum

> **Theorem**: Finding the maximum element across all $N - K + 1$ sliding windows of size $K$ using a monotonic deque runs in strictly **$O(N)$** total time.

**Proof:**
1. Each index $i \in [0, N-1]$ enters the back of the deque exactly **once**.
2. An index is removed from the back when an incoming larger element arrives (`pop_back()`), or from the front when it slides out of the window boundary $i - K$ (`pop_front()`).
3. Because each index can be pushed at most once and popped at most once, the total number of push and pop operations across the entire algorithm is bounded by $2N$.
4. Thus, the amortized cost per element is:
   $$\frac{2N \text{ operations}}{N \text{ elements}} = O(1) \text{ per element}$$
   Total time complexity: **$O(N)$**. $\blacksquare$

---

## 💻 Complete C++ Implementation

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <deque>
#include <unordered_map>
#include <algorithm>
#include <climits>
#include <cassert>

class SlidingWindowMasterclass {
public:
    // -------------------------------------------------------------
    // Problem 1: Monotonic Deque Sliding Window Maximum (O(N))
    // -------------------------------------------------------------
    static std::vector<int> maxSlidingWindow(const std::vector<int>& nums, int k) {
        int n = static_cast<int>(nums.size());
        if (n == 0 || k <= 0) return {};

        std::deque<int> dq; // Stores indices, maintaining strictly decreasing values
        std::vector<int> result;
        result.reserve(n - k + 1);

        for (int i = 0; i < n; i++) {
            // Step 1: Remove indices that are outside the current window [i - k + 1, i]
            if (!dq.empty() && dq.front() <= i - k) {
                dq.pop_front();
            }

            // Step 2: Maintain monotonic decreasing order:
            // Discard all indices whose values are <= nums[i]
            while (!dq.empty() && nums[dq.back()] <= nums[i]) {
                dq.pop_back();
            }

            // Step 3: Append current index
            dq.push_back(i);

            // Step 4: Record current window max once first k elements are processed
            if (i >= k - 1) {
                result.push_back(nums[dq.front()]);
            }
        }

        return result;
    }

    // -------------------------------------------------------------
    // Problem 2: Minimum Window Substring (Hard)
    // -------------------------------------------------------------
    static std::string minWindow(const std::string& s, const std::string& t) {
        if (s.empty() || t.empty() || s.length() < t.length()) return "";

        int targetFreq[128] = {0};
        for (char c : t) targetFreq[static_cast<unsigned char>(c)]++;

        int requiredDistinct = 0;
        for (int i = 0; i < 128; i++) {
            if (targetFreq[i] > 0) requiredDistinct++;
        }

        int windowFreq[128] = {0};
        int formedDistinct = 0;

        int left = 0;
        int minLen = INT_MAX;
        int startIdx = 0;

        for (int right = 0; right < static_cast<int>(s.length()); right++) {
            char c = s[right];
            windowFreq[static_cast<unsigned char>(c)]++;

            if (targetFreq[static_cast<unsigned char>(c)] > 0 &&
                windowFreq[static_cast<unsigned char>(c)] == targetFreq[static_cast<unsigned char>(c)]) {
                formedDistinct++;
            }

            // Contract window from left while all characters are satisfied
            while (left <= right && formedDistinct == requiredDistinct) {
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    startIdx = left;
                }

                char leftChar = s[left];
                windowFreq[static_cast<unsigned char>(leftChar)]--;

                if (targetFreq[static_cast<unsigned char>(leftChar)] > 0 &&
                    windowFreq[static_cast<unsigned char>(leftChar)] < targetFreq[static_cast<unsigned char>(leftChar)]) {
                    formedDistinct--;
                }

                left++;
            }
        }

        return minLen == INT_MAX ? "" : s.substr(startIdx, minLen);
    }

    // -------------------------------------------------------------
    // Problem 3: Longest Substring Without Repeating Characters (O(N))
    // -------------------------------------------------------------
    static int lengthOfLongestSubstring(const std::string& s) {
        int lastPos[128];
        std::fill(lastPos, lastPos + 128, -1);

        int maxLen = 0;
        int left = 0;

        for (int right = 0; right < static_cast<int>(s.length()); right++) {
            char c = s[right];
            if (lastPos[static_cast<unsigned char>(c)] >= left) {
                left = lastPos[static_cast<unsigned char>(c)] + 1;
            }
            lastPos[static_cast<unsigned char>(c)] = right;
            maxLen = std::max(maxLen, right - left + 1);
        }

        return maxLen;
    }

    // -------------------------------------------------------------
    // Problem 4: Subarray Product Less Than K
    // -------------------------------------------------------------
    static int numSubarrayProductLessThanK(const std::vector<int>& nums, int k) {
        if (k <= 1) return 0;

        long long currentProduct = 1;
        int count = 0;
        int left = 0;

        for (int right = 0; right < static_cast<int>(nums.size()); right++) {
            currentProduct *= nums[right];

            while (currentProduct >= k && left <= right) {
                currentProduct /= nums[left];
                left++;
            }

            // Invariant: If window [left..right] is valid, exactly
            // (right - left + 1) subarrays ending at 'right' are valid!
            count += (right - left + 1);
        }

        return count;
    }
};

int main() {
    std::cout << "=== Sliding Window Comprehensive Test Harness ===\n\n";

    std::cout << "--- 1. Testing Monotonic Deque Sliding Window Maximum ---\n";
    std::vector<int> nums1 = {1, 3, -1, -3, 5, 3, 6, 7};
    int k1 = 3;
    auto maxWindow = SlidingWindowMasterclass::maxSlidingWindow(nums1, k1);
    std::cout << "  Input: [1, 3, -1, -3, 5, 3, 6, 7], K = 3\n";
    std::cout << "  Sliding Window Maxima: [ ";
    for (int m : maxWindow) std::cout << m << " ";
    std::cout << "]\n";
    assert((maxWindow == std::vector<int>{3, 3, 5, 5, 6, 7}));
    std::cout << "  Sliding Window Maximum: PASSED\n\n";

    std::cout << "--- 2. Testing Minimum Window Substring ---\n";
    std::string s1 = "ADOBECODEBANC";
    std::string t1 = "ABC";
    std::string minWin = SlidingWindowMasterclass::minWindow(s1, t1);
    std::cout << "  S = \"" << s1 << "\", T = \"" << t1 << "\"\n";
    std::cout << "  Minimum Window: \"" << minWin << "\" (Expected: \"BANC\")\n";
    assert(minWin == "BANC");
    std::cout << "  Minimum Window Substring: PASSED\n\n";

    std::cout << "--- 3. Testing Longest Substring Without Repeating Characters ---\n";
    std::string s2 = "abcabcbb";
    int l1 = SlidingWindowMasterclass::lengthOfLongestSubstring(s2);
    assert(l1 == 3); // "abc"

    std::string s3 = "pwwkew";
    int l2 = SlidingWindowMasterclass::lengthOfLongestSubstring(s3);
    assert(l2 == 3); // "wke"
    std::cout << "  Longest Substring Without Repeating: PASSED\n\n";

    std::cout << "--- 4. Testing Subarray Product Less Than K ---\n";
    std::vector<int> nums2 = {10, 5, 2, 6};
    int k2 = 100;
    int subCount = SlidingWindowMasterclass::numSubarrayProductLessThanK(nums2, k2);
    std::cout << "  Input: [10, 5, 2, 6], K = 100\n";
    std::cout << "  Subarrays with product < 100: " << subCount << " (Expected: 8)\n";
    assert(subCount == 8);
    std::cout << "  Subarray Product Less Than K: PASSED\n\n";

    std::cout << "=== All Sliding Window Tests Completed Successfully! ===\n";
    return 0;
}
```

---

## 📊 Complexity Analysis

| Problem / Variant | Time Complexity | Auxiliary Space | Key Data Structure |
| :--- | :--- | :--- | :--- |
| **Fixed Window Max** | $O(N)$ amortized | $O(K)$ | Monotonic `std::deque` |
| **Minimum Window Substring** | $O(N + M)$ | $O(\Sigma) = O(1)$ | Direct frequency array (`int[128]`) |
| **Longest Substring Without Repeats**| $O(N)$ | $O(\Sigma) = O(1)$ | Direct last-seen array (`int[128]`) |
| **Subarray Product $< K$** | $O(N)$ | $O(1)$ | Dual-pointer dynamic product tracker |

---

## 💡 Practical Insights & Pitfalls

1. **Subarray Counting Formula**:
   - In dynamic sliding windows, every time `right` advances to a valid window $[left, right]$, the count of new valid subarrays ending at `right` is exactly $right - left + 1$.
2. **Frequency Map Optimization**:
   - For standard ASCII inputs (characters $0 \dots 127$), avoid `std::unordered_map<char, int>` due to hash collisions and dynamic allocations. A flat fixed-size array `int freq[128] = {0}` provides $O(1)$ memory access directly inside the L1 cache.
