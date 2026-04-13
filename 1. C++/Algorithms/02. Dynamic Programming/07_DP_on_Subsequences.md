# 07_DP_on_Subsequences.md

## DP on Subsequences

### Definition

Subsequence problems involve selecting a subset of elements from an array or string while maintaining relative order (but not necessarily contiguous). DP on subsequences typically tracks the index and some additional state.

### Subsequence vs Subarray

| Property | Subarray | Subsequence |
|----------|----------|-------------|
| Contiguous | Yes | No |
| Order preserved | Yes | Yes |
| Number of possibilities | O(n²) | O(2ⁿ) |
| DP complexity | O(n²) | O(n²) typically |

### Classic Subsequence Problems

#### 1. Longest Increasing Subsequence (LIS)

**Problem:** Find the length of the longest subsequence where elements are strictly increasing.

```
State: dp[i] = length of LIS ending at index i
Base: dp[i] = 1 for all i
Transition: dp[i] = max(dp[j] + 1) for all j < i where arr[j] < arr[i]
Answer: max(dp[0..n-1])
```

**Implementation (O(n²)):**

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

**Implementation (O(n log n) - Patience Sorting):**

```cpp
int lengthOfLIS(vector<int>& nums) {
    vector<int> tails;
    for (int num : nums) {
        auto it = lower_bound(tails.begin(), tails.end(), num);
        if (it == tails.end()) {
            tails.push_back(num);
        } else {
            *it = num;
        }
    }
    return tails.size();
}
```

#### 2. Maximum Sum Increasing Subsequence

**Problem:** Find the maximum sum of an increasing subsequence.

```
State: dp[i] = max sum of increasing subsequence ending at i
Base: dp[i] = arr[i]
Transition: dp[i] = max(dp[j] + arr[i]) for all j < i where arr[j] < arr[i]
Answer: max(dp[0..n-1])
```

```cpp
int maxSumIS(vector<int>& arr) {
    int n = arr.size();
    vector<int> dp = arr;
    int ans = arr[0];
    
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (arr[j] < arr[i]) {
                dp[i] = max(dp[i], dp[j] + arr[i]);
            }
        }
        ans = max(ans, dp[i]);
    }
    
    return ans;
}
```

#### 3. Longest Bitonic Subsequence

**Problem:** Find longest subsequence that first increases then decreases.

```
Step 1: Compute LIS from left (incLIS[i])
Step 2: Compute LDS from right (decLDS[i]) - LIS from right
Step 3: bitonic[i] = incLIS[i] + decLDS[i] - 1
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
    
    // LIS from right (decreasing from left perspective)
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

#### 4. Number of Longest Increasing Subsequence

**Problem:** Count how many LIS exist.

```
State: 
    length[i] = length of LIS ending at i
    count[i] = number of LIS ending at i

Base: length[i] = 1, count[i] = 1
Transition:
    if nums[j] < nums[i]:
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

#### 5. Subset Sum Problem

**Problem:** Is there a subset with sum equal to target?

```
State: dp[i][s] = true if subset of first i elements has sum s
Base: dp[0][0] = true
Transition:
    dp[i][s] = dp[i-1][s] or (s >= arr[i-1] and dp[i-1][s-arr[i-1]])
Answer: dp[n][target]
```

**Implementation (2D):**

```cpp
bool subsetSum(vector<int>& nums, int target) {
    int n = nums.size();
    vector<vector<bool>> dp(n+1, vector<bool>(target+1, false));
    dp[0][0] = true;
    
    for (int i = 1; i <= n; i++) {
        for (int s = 0; s <= target; s++) {
            dp[i][s] = dp[i-1][s];
            if (s >= nums[i-1]) {
                dp[i][s] = dp[i][s] || dp[i-1][s-nums[i-1]];
            }
        }
    }
    
    return dp[n][target];
}
```

**Implementation (1D - space optimized):**

```cpp
bool subsetSum(vector<int>& nums, int target) {
    vector<bool> dp(target+1, false);
    dp[0] = true;
    
    for (int num : nums) {
        for (int s = target; s >= num; s--) {
            dp[s] = dp[s] || dp[s-num];
        }
    }
    
    return dp[target];
}
```

#### 6. Partition Equal Subset Sum

**Problem:** Can the array be partitioned into two subsets with equal sum?

```
total = sum(nums)
if total is odd: return false
target = total / 2
return subsetSum(nums, target)
```

#### 7. Minimum Subset Sum Difference

**Problem:** Partition array into two subsets such that absolute difference of sums is minimized.

```
State: dp[s] = true if subset sum s is possible
Process: Find all possible subset sums
Answer: min over s of abs(total - 2*s)
```

```cpp
int minSubsetSumDiff(vector<int>& nums) {
    int total = accumulate(nums.begin(), nums.end(), 0);
    vector<bool> dp(total+1, false);
    dp[0] = true;
    
    for (int num : nums) {
        for (int s = total; s >= num; s--) {
            dp[s] = dp[s] || dp[s-num];
        }
    }
    
    int ans = total;
    for (int s = 0; s <= total; s++) {
        if (dp[s]) {
            ans = min(ans, abs(total - 2*s));
        }
    }
    
    return ans;
}
```

#### 8. Count of Subsets with Given Sum

**Problem:** Count number of subsets that sum to target.

```
State: dp[i][s] = number of subsets of first i elements with sum s
Base: dp[0][0] = 1
Transition:
    dp[i][s] = dp[i-1][s] + (s >= arr[i-1] ? dp[i-1][s-arr[i-1]] : 0)
Answer: dp[n][target]
```

```cpp
int countSubsetsWithSum(vector<int>& nums, int target) {
    int n = nums.size();
    vector<vector<int>> dp(n+1, vector<int>(target+1, 0));
    dp[0][0] = 1;
    
    for (int i = 1; i <= n; i++) {
        for (int s = 0; s <= target; s++) {
            dp[i][s] = dp[i-1][s];
            if (s >= nums[i-1]) {
                dp[i][s] += dp[i-1][s-nums[i-1]];
            }
        }
    }
    
    return dp[n][target];
}
```

#### 9. Target Sum

**Problem:** Assign + or - to each number to reach target sum.

```
This is equivalent to finding subset with sum = (target + total)/2
So same as countSubsetsWithSum
```

```cpp
int findTargetSumWays(vector<int>& nums, int target) {
    int total = accumulate(nums.begin(), nums.end(), 0);
    if (abs(target) > total) return 0;
    if ((target + total) % 2 != 0) return 0;
    int subsetSum = (target + total) / 2;
    return countSubsetsWithSum(nums, subsetSum);
}
```

### Comparison of Subsequence Problems

| Problem | State | Transition Complexity |
|---------|-------|----------------------|
| LIS (O(n²)) | dp[i] | O(n) per state |
| LIS (O(n log n)) | tails array | O(log n) per element |
| Subset Sum | dp[i][s] | O(1) per state |
| Count Subsets | dp[i][s] | O(1) per state |
| LCS | dp[i][j] | O(1) per state |
---

## Next Step

- Go to [08_DP_on_Strings.md](08_DP_on_Strings.md) to continue with DP on Strings.
