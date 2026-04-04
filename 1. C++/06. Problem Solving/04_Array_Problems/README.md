# Array Problems

## Overview
Array problems are fundamental in programming and appear frequently in technical interviews and competitive programming. This section covers essential array manipulation techniques, patterns, and problem-solving strategies.

## Topics Covered

### 1. Array Basics (`01_Array_Basics.md`)
- Array fundamentals and properties
- Array operations and complexity
- Multi-dimensional arrays
- Dynamic arrays vs static arrays
- Common array pitfalls

### 2. Two Pointer Technique (`02_Two_Pointer_Technique.md`)
- Two pointer approach and applications
- Opposite direction pointers
- Same direction pointers
- Sliding window vs two pointers
- Problem patterns and solutions

### 3. Sliding Window (`03_Sliding_Window.md`)
- Fixed-size sliding window
- Variable-size sliding window
- Window expansion and contraction
- Applications in subarray problems
- Optimization techniques

### 4. Array Rotation (`04_Array_Rotation.md`)
- Left and right rotation algorithms
- Reversal algorithm for rotation
- Juggling algorithm
- Block swap algorithm
- Rotation by k positions

### 5. Subarray Problems (`05_Subarray_Problems.md`)
- Maximum subarray sum (Kadane's algorithm)
- Subarray with given sum
- Count of subarrays
- Subarray constraints
- Prefix sum techniques

## Key Concepts

### Array Properties
- **Indexing**: 0-based or 1-based access
- **Contiguous Memory**: Elements stored in consecutive memory locations
- **Random Access**: O(1) time complexity for element access
- **Fixed Size**: Static arrays have fixed size
- **Type Homogeneity**: All elements have same data type

### Time Complexity
| Operation | Time Complexity |
|-----------|-----------------|
| Access | O(1) |
| Search (unsorted) | O(n) |
| Search (sorted) | O(log n) |
| Insertion (at end) | O(1) |
| Insertion (at position) | O(n) |
| Deletion (at end) | O(1) |
| Deletion (at position) | O(n) |

## Basic Array Operations

### 1. Array Utilities
```cpp
class ArrayUtils {
public:
    // Print array
    static void printArray(const std::vector<int>& arr) {
        for (int num : arr) {
            std::cout << num << " ";
        }
        std::cout << std::endl;
    }
    
    // Find maximum element
    static int findMax(const std::vector<int>& arr) {
        if (arr.empty()) return INT_MIN;
        
        int maxVal = arr[0];
        for (int i = 1; i < arr.size(); i++) {
            maxVal = std::max(maxVal, arr[i]);
        }
        return maxVal;
    }
    
    // Find minimum element
    static int findMin(const std::vector<int>& arr) {
        if (arr.empty()) return INT_MAX;
        
        int minVal = arr[0];
        for (int i = 1; i < arr.size(); i++) {
            minVal = std::min(minVal, arr[i]);
        }
        return minVal;
    }
    
    // Reverse array
    static void reverseArray(std::vector<int>& arr) {
        int left = 0, right = arr.size() - 1;
        while (left < right) {
            std::swap(arr[left], arr[right]);
            left++;
            right--;
        }
    }
    
    // Check if array is sorted
    static bool isSorted(const std::vector<int>& arr) {
        for (int i = 1; i < arr.size(); i++) {
            if (arr[i] < arr[i - 1]) {
                return false;
            }
        }
        return true;
    }
};
```

### 2. Array Searching
```cpp
class ArraySearch {
public:
    // Linear search
    static int linearSearch(const std::vector<int>& arr, int target) {
        for (int i = 0; i < arr.size(); i++) {
            if (arr[i] == target) {
                return i;
            }
        }
        return -1;
    }
    
    // Binary search (array must be sorted)
    static int binarySearch(const std::vector<int>& arr, int target) {
        int left = 0, right = arr.size() - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return -1;
    }
    
    // Find first occurrence of target
    static int findFirstOccurrence(const std::vector<int>& arr, int target) {
        int left = 0, right = arr.size() - 1;
        int result = -1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (arr[mid] == target) {
                result = mid;
                right = mid - 1; // Look for earlier occurrence
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return result;
    }
    
    // Find last occurrence of target
    static int findLastOccurrence(const std::vector<int>& arr, int target) {
        int left = 0, right = arr.size() - 1;
        int result = -1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (arr[mid] == target) {
                result = mid;
                left = mid + 1; // Look for later occurrence
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return result;
    }
};
```

## Two Pointer Technique

### 1. Opposite Direction Pointers
```cpp
class TwoPointer {
public:
    // Two sum problem (sorted array)
    static std::pair<int, int> twoSum(const std::vector<int>& arr, int target) {
        int left = 0, right = arr.size() - 1;
        
        while (left < right) {
            int sum = arr[left] + arr[right];
            
            if (sum == target) {
                return {left, right};
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        
        return {-1, -1}; // No solution found
    }
    
    // Check if array is palindrome
    static bool isPalindrome(const std::vector<int>& arr) {
        int left = 0, right = arr.size() - 1;
        
        while (left < right) {
            if (arr[left] != arr[right]) {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
    }
    
    // Container with most water
    static int maxArea(const std::vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int maxWater = 0;
        
        while (left < right) {
            int width = right - left;
            int currentHeight = std::min(height[left], height[right]);
            maxWater = std::max(maxWater, width * currentHeight);
            
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        
        return maxWater;
    }
};
```

### 2. Same Direction Pointers
```cpp
class SameDirectionPointers {
public:
    // Remove duplicates from sorted array
    static int removeDuplicates(std::vector<int>& arr) {
        if (arr.empty()) return 0;
        
        int writeIndex = 1;
        
        for (int readIndex = 1; readIndex < arr.size(); readIndex++) {
            if (arr[readIndex] != arr[readIndex - 1]) {
                arr[writeIndex] = arr[readIndex];
                writeIndex++;
            }
        }
        
        return writeIndex;
    }
    
    // Move zeros to end
    static void moveZeros(std::vector<int>& arr) {
        int writeIndex = 0;
        
        // Move non-zero elements forward
        for (int readIndex = 0; readIndex < arr.size(); readIndex++) {
            if (arr[readIndex] != 0) {
                arr[writeIndex] = arr[readIndex];
                writeIndex++;
            }
        }
        
        // Fill remaining positions with zeros
        while (writeIndex < arr.size()) {
            arr[writeIndex] = 0;
            writeIndex++;
        }
    }
};
```

## Sliding Window Technique

### 1. Fixed Size Window
```cpp
class FixedSizeSlidingWindow {
public:
    // Maximum sum of subarray of size k
    static int maxSumSubarray(const std::vector<int>& arr, int k) {
        if (arr.size() < k) return -1;
        
        int windowSum = 0;
        int maxSum = INT_MIN;
        
        // Calculate sum of first window
        for (int i = 0; i < k; i++) {
            windowSum += arr[i];
        }
        maxSum = windowSum;
        
        // Slide the window
        for (int i = k; i < arr.size(); i++) {
            windowSum += arr[i] - arr[i - k];
            maxSum = std::max(maxSum, windowSum);
        }
        
        return maxSum;
    }
    
    // Count subarrays with exactly k distinct elements
    static int countSubarraysWithKDistinct(const std::vector<int>& arr, int k) {
        return countAtMostKDistinct(arr, k) - countAtMostKDistinct(arr, k - 1);
    }
    
private:
    static int countAtMostKDistinct(const std::vector<int>& arr, int k) {
        if (k < 0) return 0;
        
        std::unordered_map<int, int> freq;
        int left = 0, count = 0;
        
        for (int right = 0; right < arr.size(); right++) {
            freq[arr[right]]++;
            
            while (freq.size() > k) {
                freq[arr[left]]--;
                if (freq[arr[left]] == 0) {
                    freq.erase(arr[left]);
                }
                left++;
            }
            
            count += right - left + 1;
        }
        
        return count;
    }
};
```

### 2. Variable Size Window
```cpp
class VariableSizeSlidingWindow {
public:
    // Longest subarray with sum <= k
    static int longestSubarrayWithSumAtMostK(const std::vector<int>& arr, int k) {
        int maxLength = 0;
        int currentSum = 0;
        int left = 0;
        
        for (int right = 0; right < arr.size(); right++) {
            currentSum += arr[right];
            
            // Shrink window from left if sum exceeds k
            while (currentSum > k && left <= right) {
                currentSum -= arr[left];
                left++;
            }
            
            maxLength = std::max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
    
    // Longest substring with at most k distinct characters
    static int longestSubstringAtMostKDistinct(const std::string& s, int k) {
        if (k == 0) return 0;
        
        std::unordered_map<char, int> freq;
        int left = 0, maxLength = 0;
        
        for (int right = 0; right < s.length(); right++) {
            freq[s[right]]++;
            
            while (freq.size() > k) {
                freq[s[left]]--;
                if (freq[s[left]] == 0) {
                    freq.erase(s[left]);
                }
                left++;
            }
            
            maxLength = std::max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
};
```

## Array Rotation

### 1. Rotation Algorithms
```cpp
class ArrayRotation {
public:
    // Left rotation by k positions (using extra space)
    static std::vector<int> rotateLeft(const std::vector<int>& arr, int k) {
        int n = arr.size();
        if (n == 0) return arr;
        
        k = k % n;
        std::vector<int> result(n);
        
        for (int i = 0; i < n; i++) {
            result[i] = arr[(i + k) % n];
        }
        
        return result;
    }
    
    // Right rotation by k positions (using reversal algorithm)
    static void rotateRight(std::vector<int>& arr, int k) {
        int n = arr.size();
        if (n == 0) return;
        
        k = k % n;
        if (k == 0) return;
        
        // Reverse entire array
        reverse(arr, 0, n - 1);
        
        // Reverse first k elements
        reverse(arr, 0, k - 1);
        
        // Reverse remaining elements
        reverse(arr, k, n - 1);
    }
    
    // Search in rotated sorted array
    static int searchRotated(const std::vector<int>& arr, int target) {
        int left = 0, right = arr.size() - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (arr[mid] == target) {
                return mid;
            }
            
            // Check if left half is sorted
            if (arr[left] <= arr[mid]) {
                if (arr[left] <= target && target < arr[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                // Right half is sorted
                if (arr[mid] < target && target <= arr[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        
        return -1;
    }
    
private:
    static void reverse(std::vector<int>& arr, int start, int end) {
        while (start < end) {
            std::swap(arr[start], arr[end]);
            start++;
            end--;
        }
    }
};
```

## Subarray Problems

### 1. Maximum Subarray
```cpp
class SubarrayProblems {
public:
    // Kadane's algorithm for maximum subarray sum
    static int maxSubarraySum(const std::vector<int>& arr) {
        if (arr.empty()) return 0;
        
        int maxSoFar = arr[0];
        int maxEndingHere = arr[0];
        
        for (int i = 1; i < arr.size(); i++) {
            maxEndingHere = std::max(arr[i], maxEndingHere + arr[i]);
            maxSoFar = std::max(maxSoFar, maxEndingHere);
        }
        
        return maxSoFar;
    }
    
    // Maximum subarray sum with indices
    static std::tuple<int, int, int> maxSubarrayWithIndices(const std::vector<int>& arr) {
        if (arr.empty()) return {0, -1, -1};
        
        int maxSoFar = arr[0];
        int maxEndingHere = arr[0];
        int start = 0, end = 0, tempStart = 0;
        
        for (int i = 1; i < arr.size(); i++) {
            if (maxEndingHere + arr[i] < arr[i]) {
                maxEndingHere = arr[i];
                tempStart = i;
            } else {
                maxEndingHere += arr[i];
            }
            
            if (maxEndingHere > maxSoFar) {
                maxSoFar = maxEndingHere;
                start = tempStart;
                end = i;
            }
        }
        
        return {maxSoFar, start, end};
    }
    
    // Subarray sum equals k
    static int subarraySumEqualsK(const std::vector<int>& arr, int k) {
        std::unordered_map<int, int> prefixSumCount;
        prefixSumCount[0] = 1;
        
        int currentSum = 0;
        int count = 0;
        
        for (int num : arr) {
            currentSum += num;
            
            if (prefixSumCount.find(currentSum - k) != prefixSumCount.end()) {
                count += prefixSumCount[currentSum - k];
            }
            
            prefixSumCount[currentSum]++;
        }
        
        return count;
    }
};
```

### 2. Prefix Sum Techniques
```cpp
class PrefixSum {
public:
    // Build prefix sum array
    static std::vector<int> buildPrefixSum(const std::vector<int>& arr) {
        std::vector<int> prefixSum(arr.size() + 1, 0);
        
        for (int i = 0; i < arr.size(); i++) {
            prefixSum[i + 1] = prefixSum[i] + arr[i];
        }
        
        return prefixSum;
    }
    
    // Range sum query using prefix sum
    static int rangeSum(const std::vector<int>& prefixSum, int left, int right) {
        return prefixSum[right + 1] - prefixSum[left];
    }
    
    // Build 2D prefix sum
    static std::vector<std::vector<int>> build2DPrefixSum(
        const std::vector<std::vector<int>>& matrix) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        
        std::vector<std::vector<int>> prefixSum(rows + 1, 
                                               std::vector<int>(cols + 1, 0));
        
        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= cols; j++) {
                prefixSum[i][j] = matrix[i - 1][j - 1] 
                                 + prefixSum[i - 1][j] 
                                 + prefixSum[i][j - 1] 
                                 - prefixSum[i - 1][j - 1];
            }
        }
        
        return prefixSum;
    }
    
    // 2D range sum query
    static int rangeSum2D(const std::vector<std::vector<int>>& prefixSum,
                         int row1, int col1, int row2, int col2) {
        return prefixSum[row2 + 1][col2 + 1] 
               - prefixSum[row1][col2 + 1] 
               - prefixSum[row2 + 1][col1] 
               + prefixSum[row1][col1];
    }
};
```

## Advanced Array Problems

### 1. Merge Intervals
```cpp
class MergeIntervals {
public:
    static std::vector<std::vector<int>> merge(
        std::vector<std::vector<int>> intervals) {
        if (intervals.empty()) return {};
        
        // Sort intervals by start time
        std::sort(intervals.begin(), intervals.end(),
                 [](const auto& a, const auto& b) {
                     return a[0] < b[0];
                 });
        
        std::vector<std::vector<int>> merged;
        merged.push_back(intervals[0]);
        
        for (int i = 1; i < intervals.size(); i++) {
            auto& last = merged.back();
            
            if (intervals[i][0] <= last[1]) {
                // Overlapping intervals, merge them
                last[1] = std::max(last[1], intervals[i][1]);
            } else {
                // Non-overlapping interval, add to result
                merged.push_back(intervals[i]);
            }
        }
        
        return merged;
    }
};
```

### 2. Next Permutation
```cpp
class NextPermutation {
public:
    static std::vector<int> nextPermutation(std::vector<int> nums) {
        int n = nums.size();
        int i = n - 2;
        
        // Find the first element that is smaller than the element after it
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }
        
        if (i >= 0) {
            int j = n - 1;
            
            // Find the first element that is greater than nums[i]
            while (j >= 0 && nums[j] <= nums[i]) {
                j--;
            }
            
            std::swap(nums[i], nums[j]);
        }
        
        // Reverse the suffix
        std::reverse(nums.begin() + i + 1, nums.end());
        
        return nums;
    }
};
```

## Performance Analysis

### Time Complexity Summary
| Technique | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| Linear Search | O(n) | O(1) |
| Binary Search | O(log n) | O(1) |
| Two Pointer | O(n) | O(1) |
| Sliding Window | O(n) | O(k) |
| Array Rotation | O(n) | O(1) |
| Kadane's Algorithm | O(n) | O(1) |
| Prefix Sum | O(n) | O(n) |

## Best Practices

### 1. Algorithm Selection
- Use binary search for sorted arrays
- Apply two-pointer technique for sorted arrays
- Use sliding window for subarray problems
- Consider prefix sums for range queries

### 2. Implementation Tips
- Handle edge cases (empty array, single element)
- Check array bounds before access
- Use appropriate data types for large numbers
- Optimize for space when possible

### 3. Problem-Solving Strategies
- Identify patterns in array problems
- Consider multiple approaches before coding
- Test with various input sizes
- Optimize after getting correct solution

## Common Applications

### 1. Data Processing
- Finding patterns in data streams
- Statistical analysis
- Signal processing

### 2. Algorithm Design
- Dynamic programming base cases
- Greedy algorithm implementations
- Divide and conquer problems

### 3. System Design
- Buffer management
- Cache implementations
- Memory allocation

## Summary

Array problems form the foundation of algorithmic problem-solving. Mastering various array manipulation techniques, from basic operations to advanced patterns like two-pointer and sliding window, is essential for technical interviews and competitive programming. Understanding the time and space complexity of different approaches enables optimal solution selection.
