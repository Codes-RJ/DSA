# 14_Longest_Increasing_Subsequence.md

## Longest Increasing Subsequence (LIS)

### Definition

Given an array of integers, find the length of the longest subsequence that is strictly increasing. The subsequence does not need to be contiguous.

### Example

```
Input: [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: LIS is [2, 3, 7, 101] or [2, 5, 7, 101] (length 4)
```

### Problem Statement

Find the length of the longest subsequence where each element is greater than the previous element.

### Method 1: O(n²) DP

```
State: dp[i] = length of LIS ending at index i
Base: dp[i] = 1 for all i (each element alone is an increasing subsequence)
Transition: dp[i] = max(dp[j] + 1) for all j < i where arr[j] < arr[i]
Answer: max(dp[0], dp[1], ..., dp[n-1])
```

```cpp
int lengthOfLIS(vector<int>& nums) {
    int n = nums.size();
    vector<int> dp(n, 1);
    int ans = 1;
    
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        ans = max(ans, dp[i]);
    }
    
    return ans;
}
```

### Method 2: O(n log n) with Binary Search

This method uses patience sorting algorithm. We maintain an array `tails` where `tails[i]` is the smallest possible tail of an increasing subsequence of length `i+1`.

**Algorithm:**
1. Initialize an empty array `tails`
2. For each number x in nums:
   - Find the first index in tails where tails[idx] >= x using binary search
   - If found, replace tails[idx] with x
   - If not found (x is larger than all tails), append x to tails
3. Length of tails is the LIS length

```cpp
int lengthOfLIS(vector<int>& nums) {
    vector<int> tails;
    
    for (int x : nums) {
        auto it = lower_bound(tails.begin(), tails.end(), x);
        if (it == tails.end()) {
            tails.push_back(x);
        } else {
            *it = x;
        }
    }
    
    return tails.size();
}
```

### How the O(n log n) Method Works

**Example: nums = [10, 9, 2, 5, 3, 7, 101, 18]**

```
Step 1: x = 10 → tails = [10]
Step 2: x = 9 → lower_bound finds index 0, replace → tails = [9]
Step 3: x = 2 → lower_bound finds index 0, replace → tails = [2]
Step 4: x = 5 → lower_bound finds index 1 (end), append → tails = [2, 5]
Step 5: x = 3 → lower_bound finds index 1, replace → tails = [2, 3]
Step 6: x = 7 → lower_bound finds index 2 (end), append → tails = [2, 3, 7]
Step 7: x = 101 → lower_bound finds index 3 (end), append → tails = [2, 3, 7, 101]
Step 8: x = 18 → lower_bound finds index 3, replace → tails = [2, 3, 7, 18]

Result: length = 4
```

### Variations of LIS

#### 1. Longest Non-Decreasing Subsequence

**Difference:** Allow equal elements (>= instead of >)

```
Change condition: nums[j] <= nums[i]
```

```cpp
int longestNonDecreasing(vector<int>& nums) {
    vector<int> tails;
    
    for (int x : nums) {
        auto it = upper_bound(tails.begin(), tails.end(), x);
        if (it == tails.end()) {
            tails.push_back(x);
        } else {
            *it = x;
        }
    }
    
    return tails.size();
}
```

**Note:** Use `upper_bound` instead of `lower_bound` to allow equal elements.

#### 2. Longest Decreasing Subsequence

**Difference:** Find decreasing instead of increasing.

**Method 1:** Reverse the array and find LIS.

**Method 2:** Negate all values and find LIS.

```cpp
int longestDecreasing(vector<int>& nums) {
    vector<int> tails;
    
    for (int x : nums) {
        auto it = lower_bound(tails.begin(), tails.end(), -x);
        if (it == tails.end()) {
            tails.push_back(-x);
        } else {
            *it = -x;
        }
    }
    
    return tails.size();
}
```

#### 3. Number of Longest Increasing Subsequence

**Problem:** Count how many LIS exist.

```
State:
    length[i] = length of LIS ending at i
    count[i] = number of LIS ending at i

Base: length[i] = 1, count[i] = 1
Transition:
    for each j < i where nums[j] < nums[i]:
        if length[j] + 1 > length[i]:
            length[i] = length[j] + 1
            count[i] = count[j]
        else if length[j] + 1 == length[i]:
            count[i] += count[j]
Answer: sum of count[i] where length[i] == maxLength
```

```cpp
int findNumberOfLIS(vector<int>& nums) {
    int n = nums.size();
    vector<int> length(n, 1);
    vector<int> count(n, 1);
    
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                if (length[j] + 1 > length[i]) {
                    length[i] = length[j] + 1;
                    count[i] = count[j];
                } else if (length[j] + 1 == length[i]) {
                    count[i] += count[j];
                }
            }
        }
    }
    
    int maxLen = *max_element(length.begin(), length.end());
    int ans = 0;
    for (int i = 0; i < n; i++) {
        if (length[i] == maxLen) {
            ans += count[i];
        }
    }
    
    return ans;
}
```

#### 4. Maximum Sum Increasing Subsequence

**Problem:** Find the maximum sum of an increasing subsequence (not necessarily longest).

```
State: dp[i] = max sum of increasing subsequence ending at i
Base: dp[i] = nums[i]
Transition: dp[i] = max(dp[j] + nums[i]) for all j < i where nums[j] < nums[i]
Answer: max(dp[0..n-1])
```

```cpp
int maxSumIS(vector<int>& nums) {
    int n = nums.size();
    vector<int> dp = nums;
    int ans = nums[0];
    
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                dp[i] = max(dp[i], dp[j] + nums[i]);
            }
        }
        ans = max(ans, dp[i]);
    }
    
    return ans;
}
```

#### 5. Longest Bitonic Subsequence

**Problem:** Find longest subsequence that first increases then decreases.

```
Step 1: Compute LIS from left (inc[i])
Step 2: Compute LIS from right (dec[i]) - decreasing from left = increasing from right
Step 3: bitonic[i] = inc[i] + dec[i] - 1
Answer: max(bitonic[i])
```

```cpp
int longestBitonicSubsequence(vector<int>& nums) {
    int n = nums.size();
    vector<int> inc(n, 1);
    vector<int> dec(n, 1);
    
    // LIS from left
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                inc[i] = max(inc[i], inc[j] + 1);
            }
        }
    }
    
    // LIS from right (decreasing from left)
    for (int i = n-2; i >= 0; i--) {
        for (int j = n-1; j > i; j--) {
            if (nums[j] < nums[i]) {
                dec[i] = max(dec[i], dec[j] + 1);
            }
        }
    }
    
    int ans = 0;
    for (int i = 0; i < n; i++) {
        ans = max(ans, inc[i] + dec[i] - 1);
    }
    
    return ans;
}
```

#### 6. Minimum Number of Removals to Make Mountain Array

**Problem:** Minimum removals to make array a mountain (bitonic).

```
Answer = n - longestBitonicSubsequence(nums)
```

#### 7. Longest Increasing Subsequence in 2D (Russian Doll Envelopes)

**Problem:** You have envelopes with width and height. You can put envelope A inside envelope B if both width and height are strictly smaller. Find maximum number of envelopes you can nest.

**Solution:**
1. Sort by width ascending, and for same width sort by height descending
2. Find LIS of heights

```cpp
int maxEnvelopes(vector<vector<int>>& envelopes) {
    sort(envelopes.begin(), envelopes.end(), 
         [](const vector<int>& a, const vector<int>& b) {
             if (a[0] == b[0]) return a[1] > b[1];
             return a[0] < b[0];
         });
    
    vector<int> heights;
    for (auto& e : envelopes) {
        heights.push_back(e[1]);
    }
    
    return lengthOfLIS(heights);
}
```

#### 8. Minimum Insertions to Make Array Sorted

**Problem:** Minimum insertions to make array sorted.

```
Answer = n - LIS(nums)
```

#### 9. Minimum Deletions to Make Array Sorted

**Problem:** Minimum deletions to make array sorted.

```
Answer = n - LIS(nums)
```

### Comparison of LIS Methods

| Method | Time Complexity | Space Complexity | Use Case |
|--------|----------------|------------------|----------|
| O(n²) DP | O(n²) | O(n) | Small n (n <= 5000) |
| O(n log n) | O(n log n) | O(n) | Large n (n up to 10^5) |
| O(n log n) with reconstruction | O(n log n) | O(n) | Need actual subsequence |

### Reconstructing the LIS (O(n log n) Method)

To get the actual subsequence, we need to store predecessor information.

```cpp
vector<int> reconstructLIS(vector<int>& nums) {
    int n = nums.size();
    vector<int> tails;  // actual values
    vector<int> tailsIndex;  // indices of those values
    vector<int> parent(n, -1);  // predecessor of each index
    
    for (int i = 0; i < n; i++) {
        auto it = lower_bound(tails.begin(), tails.end(), nums[i]);
        int pos = it - tails.begin();
        
        if (it == tails.end()) {
            tails.push_back(nums[i]);
            tailsIndex.push_back(i);
        } else {
            tails[pos] = nums[i];
            tailsIndex[pos] = i;
        }
        
        if (pos > 0) {
            parent[i] = tailsIndex[pos - 1];
        }
    }
    
    // Reconstruct
    vector<int> lis;
    int idx = tailsIndex.back();
    while (idx != -1) {
        lis.push_back(nums[idx]);
        idx = parent[idx];
    }
    reverse(lis.begin(), lis.end());
    
    return lis;
}
```
---

## Next Step

- Go to [15_Edit_Distance.md](15_Edit_Distance.md) to continue with Edit Distance.
