#!/usr/bin/env python3
"""
Algorithm Templates for Competitive Programming and DSA Practice
Includes comprehensive implementations of common algorithms
"""

import sys
import math
import random
import bisect
import heapq
from collections import defaultdict, Counter, deque, OrderedDict
from typing import List, Dict, Set, Tuple, Optional, Any, Union, Callable
from itertools import permutations, combinations, product, accumulate
from functools import reduce, lru_cache
import time

# Fast I/O
def fast_input():
    """Fast input function for competitive programming"""
    return sys.stdin.readline().strip()

def fast_print(*args, **kwargs):
    """Fast print function for competitive programming"""
    print(*args, **kwargs)
    sys.stdout.flush()

# Constants
MOD = 10**9 + 7
INF = float('inf')
LINF = float('-inf')

# =============================================
# SORTING ALGORITHMS
# =============================================

class SortingAlgorithms:
    """Sorting algorithm implementations"""
    
    @staticmethod
    def bubble_sort(arr: List[int]) -> List[int]:
        """Bubble Sort - O(n^2) time, O(1) space"""
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr
    
    @staticmethod
    def selection_sort(arr: List[int]) -> List[int]:
        """Selection Sort - O(n^2) time, O(1) space"""
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
    
    @staticmethod
    def insertion_sort(arr: List[int]) -> List[int]:
        """Insertion Sort - O(n^2) time, O(1) space"""
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    @staticmethod
    def merge_sort(arr: List[int]) -> List[int]:
        """Merge Sort - O(n log n) time, O(n) space"""
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = SortingAlgorithms.merge_sort(arr[:mid])
        right = SortingAlgorithms.merge_sort(arr[mid:])
        
        return SortingAlgorithms._merge(left, right)
    
    @staticmethod
    def _merge(left: List[int], right: List[int]) -> List[int]:
        """Helper function for merge sort"""
        merged = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
    
    @staticmethod
    def quick_sort(arr: List[int]) -> List[int]:
        """Quick Sort - O(n log n) average, O(n^2) worst, O(log n) space"""
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return SortingAlgorithms.quick_sort(left) + middle + SortingAlgorithms.quick_sort(right)
    
    @staticmethod
    def quick_sort_inplace(arr: List[int]) -> List[int]:
        """In-place Quick Sort - O(n log n) average, O(n^2) worst, O(log n) space"""
        SortingAlgorithms._quick_sort_inplace(arr, 0, len(arr) - 1)
        return arr
    
    @staticmethod
    def _quick_sort_inplace(arr: List[int], low: int, high: int) -> None:
        """Helper function for in-place quick sort"""
        if low < high:
            pi = SortingAlgorithms._partition(arr, low, high)
            SortingAlgorithms._quick_sort_inplace(arr, low, pi - 1)
            SortingAlgorithms._quick_sort_inplace(arr, pi + 1, high)
    
    @staticmethod
    def _partition(arr: List[int], low: int, high: int) -> int:
        """Helper function for quick sort partition"""
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    @staticmethod
    def heap_sort(arr: List[int]) -> List[int]:
        """Heap Sort - O(n log n) time, O(1) space"""
        n = len(arr)
        
        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            SortingAlgorithms._heapify(arr, n, i)
        
        # Extract elements from heap
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            SortingAlgorithms._heapify(arr, i, 0)
        
        return arr
    
    @staticmethod
    def _heapify(arr: List[int], n: int, i: int) -> None:
        """Helper function for heap sort"""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            SortingAlgorithms._heapify(arr, n, largest)
    
    @staticmethod
    def counting_sort(arr: List[int]) -> List[int]:
        """Counting Sort - O(n + k) time, O(k) space"""
        if not arr:
            return []
        
        max_val = max(arr)
        min_val = min(arr)
        range_val = max_val - min_val + 1
        
        count = [0] * range_val
        output = [0] * len(arr)
        
        # Store count of each element
        for num in arr:
            count[num - min_val] += 1
        
        # Store cumulative count
        for i in range(1, range_val):
            count[i] += count[i - 1]
        
        # Build output array
        for num in reversed(arr):
            output[count[num - min_val] - 1] = num
            count[num - min_val] -= 1
        
        return output
    
    @staticmethod
    def radix_sort(arr: List[int]) -> List[int]:
        """Radix Sort - O(d * (n + k)) time, O(n + k) space"""
        if not arr:
            return []
        
        max_val = max(arr)
        exp = 1
        
        while max_val // exp > 0:
            arr = SortingAlgorithms._counting_sort_by_digit(arr, exp)
            exp *= 10
        
        return arr
    
    @staticmethod
    def _counting_sort_by_digit(arr: List[int], exp: int) -> List[int]:
        """Helper function for radix sort"""
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        
        # Store count of occurrences
        for num in arr:
            index = (num // exp) % 10
            count[index] += 1
        
        # Store cumulative count
        for i in range(1, 10):
            count[i] += count[i - 1]
        
        # Build output array
        for i in range(n - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
        
        return output
    
    @staticmethod
    def shell_sort(arr: List[int]) -> List[int]:
        """Shell Sort - O(n^1.5) average, O(n^2) worst, O(1) space"""
        n = len(arr)
        gap = n // 2
        
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                
                arr[j] = temp
            
            gap //= 2
        
        return arr
    
    @staticmethod
    def tim_sort(arr: List[int]) -> List[int]:
        """Tim Sort - Python's built-in sort"""
        return sorted(arr)
    
    @staticmethod
    def cocktail_sort(arr: List[int]) -> List[int]:
        """Cocktail Sort - O(n^2) time, O(1) space"""
        n = len(arr)
        swapped = True
        start = 0
        end = n - 1
        
        while swapped:
            swapped = False
            
            # Left to right pass
            for i in range(start, end):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            
            if not swapped:
                break
            
            swapped = False
            end -= 1
            
            # Right to left pass
            for i in range(end - 1, start - 1, -1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            
            start += 1
        
        return arr

# =============================================
# SEARCHING ALGORITHMS
# =============================================

class SearchingAlgorithms:
    """Searching algorithm implementations"""
    
    @staticmethod
    def linear_search(arr: List[int], target: int) -> int:
        """Linear Search - O(n) time, O(1) space"""
        for i, val in enumerate(arr):
            if val == target:
                return i
        return -1
    
    @staticmethod
    def binary_search(arr: List[int], target: int) -> int:
        """Binary Search (iterative) - O(log n) time, O(1) space"""
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
    @staticmethod
    def binary_search_recursive(arr: List[int], target: int, left: int = 0, right: int = None) -> int:
        """Binary Search (recursive) - O(log n) time, O(log n) space"""
        if right is None:
            right = len(arr) - 1
        
        if left > right:
            return -1
        
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return SearchingAlgorithms.binary_search_recursive(arr, target, mid + 1, right)
        else:
            return SearchingAlgorithms.binary_search_recursive(arr, target, left, mid - 1)
    
    @staticmethod
    def lower_bound(arr: List[int], target: int) -> int:
        """Lower Bound - First index where element >= target"""
        left, right = 0, len(arr)
        
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return left
    
    @staticmethod
    def upper_bound(arr: List[int], target: int) -> int:
        """Upper Bound - First index where element > target"""
        left, right = 0, len(arr)
        
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
        
        return left
    
    @staticmethod
    def jump_search(arr: List[int], target: int) -> int:
        """Jump Search - O(√n) time, O(1) space"""
        n = len(arr)
        step = int(math.sqrt(n))
        prev = 0
        
        # Find the block where element could be
        while prev < n and arr[min(step, n) - 1] < target:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return -1
        
        # Linear search in identified block
        for i in range(prev, min(step, n)):
            if arr[i] == target:
                return i
        
        return -1
    
    @staticmethod
    def interpolation_search(arr: List[int], target: int) -> int:
        """Interpolation Search - O(log log n) average, O(n) worst, O(1) space"""
        left, right = 0, len(arr) - 1
        
        while left <= right and target >= arr[left] and target <= arr[right]:
            if left == right:
                return left if arr[left] == target else -1
            
            # Estimate position
            pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
            
            if arr[pos] == target:
                return pos
            elif arr[pos] < target:
                left = pos + 1
            else:
                right = pos - 1
        
        return -1
    
    @staticmethod
    def exponential_search(arr: List[int], target: int) -> int:
        """Exponential Search - O(log n) time, O(1) space"""
        if len(arr) == 0:
            return -1
        if arr[0] == target:
            return 0
        
        i = 1
        while i < len(arr) and arr[i] <= target:
            i *= 2
        
        return SearchingAlgorithms.binary_search(arr[:min(i, len(arr))], target)
    
    @staticmethod
    def ternary_search(arr: List[int], target: int) -> int:
        """Ternary Search - O(log n) time, O(1) space"""
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3
            
            if arr[mid1] == target:
                return mid1
            if arr[mid2] == target:
                return mid2
            
            if target < arr[mid1]:
                right = mid1 - 1
            elif target > arr[mid2]:
                left = mid2 + 1
            else:
                left = mid1 + 1
                right = mid2 - 1
        
        return -1

# =============================================
# ARRAY ALGORITHMS
# =============================================

class ArrayAlgorithms:
    """Array algorithm implementations"""
    
    @staticmethod
    def kadane_max_subarray_sum(nums: List[int]) -> int:
        """Kadane's Algorithm - Maximum Subarray Sum - O(n) time, O(1) space"""
        max_so_far = nums[0]
        max_ending_here = nums[0]
        
        for i in range(1, len(nums)):
            max_ending_here = max(nums[i], max_ending_here + nums[i])
            max_so_far = max(max_so_far, max_ending_here)
        
        return max_so_far
    
    @staticmethod
    def max_subarray_sum_with_indices(nums: List[int]) -> Tuple[int, int, int]:
        """Kadane's Algorithm with indices - O(n) time, O(1) space"""
        max_so_far = nums[0]
        max_ending_here = nums[0]
        start = end = s = 0
        
        for i in range(1, len(nums)):
            if max_ending_here + nums[i] < nums[i]:
                max_ending_here = nums[i]
                s = i
            else:
                max_ending_here += nums[i]
            
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
                start = s
                end = i
        
        return max_so_far, start, end
    
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        """Two Sum Problem - O(n) time, O(n) space"""
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []
    
    @staticmethod
    def three_sum(nums: List[int]) -> List[List[int]]:
        """Three Sum Problem - O(n^2) time, O(n) space"""
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
    
    @staticmethod
    def four_sum(nums: List[int], target: int) -> List[List[int]]:
        """Four Sum Problem - O(n^3) time, O(n^2) space"""
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left, right = j + 1, n - 1
                    while left < right:
                        total = nums[i] + nums[j] + nums[left] + nums[right]
                        if total == target:
                            result.append([nums[i], nums[j], nums[left], nums[right]])
                            while left < right and nums[left] == nums[left + 1]:
                                left += 1
                            while left < right and nums[right] == nums[right - 1]:
                                right -= 1
                            left += 1
                            right -= 1
                        elif total < target:
                            left += 1
                        else:
                            right -= 1
        
        return result
    
    @staticmethod
    def max_product_subarray(nums: List[int]) -> int:
        """Maximum Product Subarray - O(n) time, O(1) space"""
        max_so_far = nums[0]
        max_ending_here = nums[0]
        min_ending_here = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_ending_here, min_ending_here = min_ending_here, max_ending_here
            
            max_ending_here = max(nums[i], max_ending_here * nums[i])
            min_ending_here = min(nums[i], min_ending_here * nums[i])
            max_so_far = max(max_so_far, max_ending_here)
        
        return max_so_far
    
    @staticmethod
    def find_missing_number(nums: List[int]) -> int:
        """Find Missing Number in [0, n] - O(n) time, O(1) space"""
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
    
    @staticmethod
    def find_duplicate_number(nums: List[int]) -> int:
        """Find Duplicate Number - O(n) time, O(1) space"""
        slow = nums[0]
        fast = nums[0]
        
        # Find intersection point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Find entrance to cycle
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
    
    @staticmethod
    def find_all_duplicates(nums: List[int]) -> List[int]:
        """Find All Duplicates - O(n) time, O(1) space"""
        duplicates = []
        
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                duplicates.append(abs(num))
            else:
                nums[index] = -nums[index]
        
        return duplicates
    
    @staticmethod
    def rotate_array(nums: List[int], k: int) -> List[int]:
        """Rotate Array - O(n) time, O(1) space"""
        n = len(nums)
        k %= n
        if k < 0:
            k += n
        
        # Reverse entire array
        nums.reverse()
        # Reverse first k elements
        nums[:k] = reversed(nums[:k])
        # Reverse remaining elements
        nums[k:] = reversed(nums[k:])
        
        return nums
    
    @staticmethod
    def next_permutation(nums: List[int]) -> List[int]:
        """Next Permutation - O(n) time, O(1) space"""
        n = len(nums)
        i = n - 2
        
        # Find the first decreasing element
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            j = n - 1
            # Find element just larger than nums[i]
            while j > i and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # Reverse the suffix
        nums[i + 1:] = reversed(nums[i + 1:])
        
        return nums
    
    @staticmethod
    def longest_increasing_subsequence(nums: List[int]) -> int:
        """Longest Increasing Subsequence - O(n^2) time, O(n) space"""
        if not nums:
            return 0
        
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
    
    @staticmethod
    def longest_increasing_subsequence_optimized(nums: List[int]) -> int:
        """Longest Increasing Subsequence - O(n log n) time, O(n) space"""
        if not nums:
            return 0
        
        tails = []
        for num in nums:
            idx = bisect.bisect_left(tails, num)
            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num
        
        return len(tails)
    
    @staticmethod
    def container_with_most_water(heights: List[int]) -> int:
        """Container With Most Water - O(n) time, O(1) space"""
        left, right = 0, len(heights) - 1
        max_water = 0
        
        while left < right:
            if heights[left] < heights[right]:
                max_water = max(max_water, heights[left] * (right - left))
                left += 1
            else:
                max_water = max(max_water, heights[right] * (right - left))
                right -= 1
        
        return max_water
    
    @staticmethod
    def trap_rain_water(heights: List[int]) -> int:
        """Trapping Rain Water - O(n) time, O(1) space"""
        if not heights:
            return 0
        
        left, right = 0, len(heights) - 1
        left_max, right_max = heights[left], heights[right]
        water = 0
        
        while left < right:
            if heights[left] < heights[right]:
                left += 1
                left_max = max(left_max, heights[left])
                water += max(0, left_max - heights[left])
            else:
                right -= 1
                right_max = max(right_max, heights[right])
                water += max(0, right_max - heights[right])
        
        return water
    
    @staticmethod
    def subarray_sum_equals_k(nums: List[int], k: int) -> int:
        """Subarray Sum Equals K - O(n) time, O(n) space"""
        prefix_sum = 0
        prefix_sums = {0: -1}
        
        for i, num in enumerate(nums):
            prefix_sum += num
            if (prefix_sum - k) in prefix_sums:
                return 1
            prefix_sums[prefix_sum] = i
        
        return 0
    
    @staticmethod
    def sliding_window_maximum(nums: List[int], k: int) -> List[int]:
        """Sliding Window Maximum - O(n) time, O(k) space"""
        if not nums or k == 0:
            return []
        
        result = []
        window = deque()
        
        for i, num in enumerate(nums):
            # Remove indices outside the window
            while window and window[0] <= i - k:
                window.popleft()
            
            # Remove smaller elements from the right
            while window and nums[window[-1]] < num:
                window.pop()
            
            window.append(i)
            
            # Add maximum to result
            if i >= k - 1:
                result.append(nums[window[0]])
        
        return result

# =============================================
# STRING ALGORITHMS
# =============================================

class StringAlgorithms:
    """String algorithm implementations"""
    
    @staticmethod
    def is_palindrome(s: str) -> bool:
        """Check if string is palindrome - O(n) time, O(1) space"""
        return s == s[::-1]
    
    @staticmethod
    def longest_palindromic_substring(s: str) -> str:
        """Longest Palindromic Substring - O(n^2) time, O(1) space"""
        if not s:
            return ""
        
        start, end = 0, 0
        
        for i in range(len(s)):
            len1 = StringAlgorithms._expand_around_center(s, i, i)
            len2 = StringAlgorithms._expand_around_center(s, i, i + 1)
            max_len = max(len1, len2)
            
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end + 1]
    
    @staticmethod
    def _expand_around_center(s: str, left: int, right: int) -> int:
        """Helper function for palindrome checking"""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    @staticmethod
    def longest_common_prefix(strs: List[str]) -> str:
        """Longest Common Prefix - O(n*m) time, O(1) space"""
        if not strs:
            return ""
        
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    break
        return prefix
    
    @staticmethod
    def is_valid_parentheses(s: str) -> bool:
        """Valid Parentheses - O(n) time, O(n) space"""
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                continue
        
        return not stack
    
    @staticmethod
    def generate_parentheses(n: int) -> List[str]:
        """Generate Parentheses - O(4^n / sqrt(n)) time, O(n) space"""
        result = []
        StringAlgorithms._generate_parentheses(result, "", 0, 0, n)
        return result
    
    @staticmethod
    def _generate_parentheses(result: List[str], current: str, open_count: int, close_count: int, max_pairs: int):
        """Helper function for generate parentheses"""
        if len(current) == max_pairs * 2:
            result.append(current)
            return
        
        if open_count < max_pairs:
            StringAlgorithms._generate_parentheses(result, current + "(", open_count + 1, close_count, max_pairs)
        
        if close_count < open_count:
            StringAlgorithms._generate_parentheses(result, current + ")", open_count, close_count + 1, max_pairs)
    
    @staticmethod
    def word_break(s: str, word_dict: List[str]) -> bool:
        """Word Break - O(n^2) time, O(n) space"""
        word_set = set(word_dict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[len(s)]
    
    @staticmethod
    def edit_distance(word1: str, word2: str) -> int:
        """Edit Distance - O(n*m) time, O(n*m) space"""
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        
        return dp[m][n]
    
    @staticmethod
    def kmp_search(text: str, pattern: str) -> int:
        """KMP Algorithm - O(n + m) time, O(m) space"""
        lps = StringAlgorithms._compute_lps(pattern)
        i = j = 0
        
        while i < len(text):
            if pattern[j] == text[i]:
                i += 1
                j += 1
                
                if j == len(pattern):
                    return i - j
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return -1
    
    @staticmethod
    def _compute_lps(pattern: str) -> List[int]:
        """Helper function for KMP"""
        lps = [0] * len(pattern)
        length = 0
        i = 1
        
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps
    
    @staticmethod
    def rabin_karp(text: str, pattern: str) -> int:
        """Rabin-Karp Algorithm - O(n + m) time, O(1) space"""
        if len(text) < len(pattern):
            return -1
        
        base = 256
        mod = 101
        pattern_hash = 0
        text_hash = 0
        h = 1
        
        # Calculate hash for pattern and first window
        for i in range(len(pattern)):
            pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
            text_hash = (text_hash * base + ord(text[i])) % mod
        
        # Calculate h = pow(m, d-1) % mod
        for i in range(len(pattern) - 1):
            h = (h * base) % mod
        
        for i in range(len(text) - len(pattern) + 1):
            if pattern_hash == text_hash:
                # Check for actual match
                if text[i:i+len(pattern)] == pattern:
                    return i
            
            if i < len(text) - len(pattern):
                text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + len(pattern)])) % mod
        
        return -1
    
    @staticmethod
    def longest_common_subsequence(text1: str, text2: str) -> int:
        """Longest Common Subsequence - O(n*m) time, O(n*m) space"""
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]
    
    @staticmethod
    def shortest_common_supersequence(text1: str, text2: str) -> str:
        """Shortest Common Supersequence - O(n*m) time, O(n*m) space"""
        m, n = len(text1), len(text2)
        dp = [[""] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = text2[:j]
                elif j == 0:
                    dp[i][j] = text1[:i]
                elif text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + text1[i - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + text1[i - 1]
        
        return dp[m][n]

# =============================================
# TREE ALGORITHMS
# =============================================

class TreeNode:
    """Binary Tree Node"""
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class TreeAlgorithms:
    """Tree algorithm implementations"""
    
    @staticmethod
    def inorder_traversal(root: TreeNode) -> List[int]:
        """Inorder Traversal - O(n) time, O(h) space"""
        result = []
        TreeAlgorithms._inorder_recursive(root, result)
        return result
    
    @staticmethod
    def _inorder_recursive(node: TreeNode, result: List[int]) -> None:
        """Helper function for inorder traversal"""
        if node:
            TreeAlgorithms._inorder_recursive(node.left, result)
            result.append(node.val)
            TreeAlgorithms._inorder_recursive(node.right, result)
    
    @staticmethod
    def inorder_iterative(root: TreeNode) -> List[int]:
        """Inorder Traversal (Iterative) - O(n) time, O(h) space"""
        result = []
        stack = []
        current = root
        
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            result.append(current.val)
            current = current.right
        
        return result
    
    @staticmethod
    def preorder_traversal(root: TreeNode) -> List[int]:
        """Preorder Traversal - O(n) time, O(h) space"""
        result = []
        TreeAlgorithms._preorder_recursive(root, result)
        return result
    
    @staticmethod
    def _preorder_recursive(node: TreeNode, result: List[int]) -> None:
        """Helper function for preorder traversal"""
        if node:
            result.append(node.val)
            TreeAlgorithms._preorder_recursive(node.left, result)
            TreeAlgorithms._preorder_recursive(node.right, result)
    
    @staticmethod
    def preorder_iterative(root: TreeNode) -> List[int]:
        """Preorder Traversal (Iterative) - O(n) time, O(h) space"""
        result = []
        stack = [root] if root else []
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result
    
    @staticmethod
    def postorder_traversal(root: TreeNode) -> List[int]:
        """Postorder Traversal - O(n) time, O(h) space"""
        result = []
        TreeAlgorithms._postorder_recursive(root, result)
        return result
    
    @staticmethod
    def _postorder_recursive(node: TreeNode, result: List[int]) -> None:
        """Helper function for postorder traversal"""
        if node:
            TreeAlgorithms._postorder_recursive(node.left, result)
            TreeAlgorithms._postorder_recursive(node.right, result)
            result.append(node.val)
    
    @staticmethod
    def postorder_iterative(root: TreeNode) -> List[int]:
        """Postorder Traversal (Iterative) - O(n) time, O(h) space"""
        result = []
        stack = []
        current = root
        last_visited = None
        
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                node = stack[-1]
                if node.right and node.right != last_visited:
                    current = node.right
                else:
                    result.append(node.val)
                    last_visited = stack.pop()
        
        return result
    
    @staticmethod
    def level_order_traversal(root: TreeNode) -> List[List[int]]:
        """Level Order Traversal - O(n) time, O(n) space"""
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
        
        return result
    
    @staticmethod
    def max_depth(root: TreeNode) -> int:
        """Maximum Depth of Binary Tree - O(n) time, O(h) space"""
        if not root:
            return 0
        return 1 + max(TreeAlgorithms.max_depth(root.left), TreeAlgorithms.max_depth(root.right))
    
    @staticmethod
    def max_depth_iterative(root: TreeNode) -> int:
        """Maximum Depth (Iterative) - O(n) time, O(n) space"""
        if not root:
            return 0
        
        max_depth = 0
        queue = deque([(root, 1)])
        
        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
        return max_depth
    
    @staticmethod
    def is_valid_bst(root: TreeNode) -> bool:
        """Validate Binary Search Tree - O(n) time, O(h) space"""
        return TreeAlgorithms._is_valid_bst_helper(root, None, None)
    
    @staticmethod
    def _is_valid_bst_helper(node: TreeNode, min_val: int, max_val: int) -> bool:
        """Helper function for BST validation"""
        if not node:
            return True
        
        if (min_val is not None and node.val <= min_val) or (max_val is not None and node.val >= max_val):
            return False
        
        return (TreeAlgorithms._is_valid_bst_helper(node.left, min_val, node.val) and
                TreeAlgorithms._is_valid_bst_helper(node.right, node.val, max_val))
    
    @staticmethod
    def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """Lowest Common Ancestor - O(n) time, O(h) space"""
        if not root or root == p or root == q:
            return root
        
        left = TreeAlgorithms.lowest_common_ancestor(root.left, p, q)
        right = TreeAlgorithms.lowest_common_ancestor(root.right, p, q)
        
        if left and right:
            return root
        return left if left else right
    
    @staticmethod
    def serialize(root: TreeNode) -> str:
        """Serialize Binary Tree - O(n) time, O(n) space"""
        if not root:
            return "null"
        
        queue = deque([root])
        result = []
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
        
        return ",".join(result)
    
    @staticmethod
    def deserialize(data: str) -> TreeNode:
        """Deserialize Binary Tree - O(n) time, O(n) space"""
        if not data or data == "null":
            return None
        
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1
        
        while queue and i < len(values):
            node = queue.popleft()
            
            if values[i] != "null":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            else:
                node.left = None
            
            i += 1
            
            if i < len(values) and values[i] != "null":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            else:
                node.right = None
            
            i += 1
        
        return root
    
    @staticmethod
    def zigzag_level_order(root: TreeNode) -> List[List[int]]:
        """Zigzag Level Order Traversal - O(n) time, O(n) space"""
        if not root:
            return []
        
        result = []
        queue = deque([root])
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if not left_to_right:
                current_level.reverse()
            
            result.append(current_level)
            left_to_right = not left_to_right
        
        return result

# =============================================
# GRAPH ALGORITHMS
# =============================================

class GraphNode:
    """Graph Node"""
    def __init__(self, val: int = 0):
        self.val = val
        self.neighbors = []

class GraphAlgorithms:
    """Graph algorithm implementations"""
    
    @staticmethod
    def bfs(start: int, graph: Dict[int, List[int]]) -> List[int]:
        """Breadth-First Search - O(V + E) time, O(V) space"""
        result = []
        if start not in graph:
            return result
        
        queue = deque([start])
        visited = set([start])
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    @staticmethod
    def dfs(start: int, graph: Dict[int, List[int]]) -> List[int]:
        """Depth-First Search - O(V + E) time, O(V) space"""
        result = []
        visited = set()
        GraphAlgorithms._dfs_helper(start, graph, visited, result)
        return result
    
    @staticmethod
    def _dfs_helper(node: int, graph: Dict[int, List[int]], visited: Set[int], result: List[int]) -> None:
        """Helper function for DFS"""
        if node not in graph or node in visited:
            return
        
        visited.add(node)
        result.append(node)
        
        for neighbor in graph[node]:
            GraphAlgorithms._dfs_helper(neighbor, graph, visited, result)
    
    @staticmethod
    def dfs_iterative(start: int, graph: Dict[int, List[int]]) -> List[int]:
        """DFS (Iterative) - O(V + E) time, O(V) space"""
        result = []
        stack = [start]
        visited = set([start])
        
        while stack:
            node = stack.pop()
            result.append(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        
        return result
    
    @staticmethod
    def dijkstra(start: int, graph: Dict[int, List[Tuple[int, int]]]) -> Dict[int, int]:
        """Dijkstra's Algorithm - O((V + E) log V) time, O(V) space"""
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        pq = [(0, start)]
        
        while pq:
            dist, node = heapq.heappop(pq)
            
            if dist > distances[node]:
                continue
            
            for neighbor, weight in graph[node]:
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
        
        return distances
    
    @staticmethod
    def topological_sort(num_courses: int, prerequisites: List[Tuple[int, int]]) -> List[int]:
        """Topological Sort - O(V + E) time, O(V) space"""
        graph = {i: [] for i in range(num_courses)}
        in_degree = [0] * num_courses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
        result = []
        
        while queue:
            course = queue.popleft()
            result.append(course)
            
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result if len(result) == num_courses else []
    
    @staticmethod
    def has_cycle(num_courses: int, prerequisites: List[Tuple[int, int]]) -> bool:
        """Detect Cycle in Directed Graph - O(V + E) time, O(V) space"""
        graph = {i: [] for i in range(num_courses)}
        in_degree = [0] * num_courses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
        visited_count = 0
        
        while queue:
            course = queue.popleft()
            visited_count += 1
            
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return visited_count == num_courses
    
    @staticmethod
    def is_bipartite(graph: Dict[int, List[int]]) -> bool:
        """Check if Graph is Bipartite - O(V + E) time, O(V) space"""
        colors = {}
        
        for node in graph:
            if node not in colors:
                if not GraphAlgorithms._is_bipartite_helper(graph, node, colors, 0):
                    return False
        
        return True
    
    @staticmethod
    def _is_bipartite_helper(graph: Dict[int, List[int]], node: int, colors: Dict[int, int], color: int) -> bool:
        """Helper function for bipartite check"""
        colors[node] = color
        
        for neighbor in graph[node]:
            if neighbor not in colors:
                if not GraphAlgorithms._is_bipartite_helper(graph, neighbor, colors, 1 - color):
                    return False
            elif colors[neighbor] == color:
                return False
        
        return True
    
    @staticmethod
    def kruskal_mst(edges: List[Tuple[int, int, int]]) -> Tuple[List[Tuple[int, int, int]], int]:
        """Kruskal's Algorithm for Minimum Spanning Tree - O(E log E) time, O(V) space"""
        # Sort edges by weight
        edges.sort(key=lambda x: x[2])
        
        parent = list(range(max(max(u, v) for u, v, w in edges) + 1))
        result = []
        total_weight = 0
        
        def find(u):
            while parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        
        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            if root_u != root_v:
                parent[root_v] = root_u
        
        for u, v, w in edges:
            if find(u) != find(v):
                union(u, v)
                result.append((u, v, w))
                total_weight += w
        
        return result, total_weight
    
    @staticmethod
    def prim_mst(n: int, graph: Dict[int, List[Tuple[int, int]]]) -> Tuple[List[Tuple[int, int, int]], int]:
        """Prim's Algorithm for Minimum Spanning Tree - O(E log V) time, O(V) space"""
        visited = set()
        min_heap = []
        result = []
        total_weight = 0
        
        # Start from node 0
        visited.add(0)
        for neighbor, weight in graph[0]:
            heapq.heappush(min_heap, (weight, 0, neighbor))
        
        while len(visited) < n and min_heap:
            weight, u, v = heapq.heappop(min_heap)
            
            if v not in visited:
                visited.add(v)
                result.append((u, v, weight))
                total_weight += weight
                
                for neighbor, w in graph[v]:
                    if neighbor not in visited:
                        heapq.heappush(min_heap, (w, v, neighbor))
        
        return result, total_weight

# =============================================
# DYNAMIC PROGRAMMING
# =============================================

class DynamicProgramming:
    """Dynamic programming implementations"""
    
    @staticmethod
    def fibonacci(n: int) -> int:
        """Fibonacci - O(n) time, O(1) space"""
        if n <= 1:
            return n
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        
        return b
    
    @staticmethod
    def fibonacci_memoized(n: int, memo: Dict[int, int] = None) -> int:
        """Fibonacci with Memoization - O(n) time, O(n) space"""
        if memo is None:
            memo = {}
        
        if n in memo:
            return memo[n]
        
        if n <= 1:
            memo[n] = n
        else:
            memo[n] = DynamicProgramming.fibonacci_memoized(n - 1, memo) + DynamicProgramming.fibonacci_memoized(n - 2, memo)
        
        return memo[n]
    
    @staticmethod
    def coin_change(coins: List[int], amount: int) -> int:
        """Coin Change Problem - O(n * amount) time, O(amount) space"""
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != amount + 1 else -1
    
    @staticmethod
    def longest_increasing_subsequence(nums: List[int]) -> int:
        """Longest Increasing Subsequence - O(n^2) time, O(n) space"""
        if not nums:
            return 0
        
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
    
    @staticmethod
    def longest_increasing_subsequence_optimized(nums: List[int]) -> int:
        """Longest Increasing Subsequence - O(n log n) time, O(n) space"""
        if not nums:
            return 0
        
        tails = []
        for num in nums:
            idx = bisect.bisect_left(tails, num)
            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num
        
        return len(tails)
    
    @staticmethod
    def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
        """0/1 Knapsack - O(n * capacity) time, O(n * capacity) space"""
        n = len(weights)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for w in range(capacity + 1):
                if weights[i - 1] <= w:
                    dp[i][w] = max(dp[i - 1][w], 
                                        values[i - 1] + dp[i - 1][w - weights[i - 1]])
                else:
                    dp[i][w] = dp[i - 1][w]
        
        return dp[n][capacity]
    
    @staticmethod
    def knapsack_unbounded(weights: List[int], values: List[int], capacity: int) -> int:
        """Unbounded Knapsack - O(n * capacity) time, O(capacity) space"""
        dp = [0] * (capacity + 1)
        
        for i in range(len(weights)):
            for w in range(weights[i], capacity + 1):
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
        
        return dp[capacity]
    
    @staticmethod
    def edit_distance(word1: str, word2: str) -> int:
        """Edit Distance - O(n * m) time, O(n * m) space"""
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        
        return dp[m][n]
    
    @staticmethod
    def longest_common_subsequence(text1: str, text2: str) -> int:
        """Longest Common Subsequence - O(n * m) time, O(n * m) space"""
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]
    
    @staticmethod
    def longest_common_substring(text1: str, text2: str) -> int:
        """Longest Common Substring - O(n * m) time, O(n * m) space"""
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_len = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])
                else:
                    dp[i][j] = 0
        
        return max_len
    
    @staticmethod
    def min_path_sum(grid: List[List[int]]) -> int:
        """Minimum Path Sum in Grid - O(n * m) time, O(n * m) space"""
        if not grid or not grid[0]:
            return 0
        
        n, m = len(grid), len(grid[0])
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = grid[0][0]
        
        # Initialize first row
        for j in range(1, m):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        
        # Initialize first column
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        
        # Fill the rest
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        
        return dp[n - 1][m - 1]
    
    @staticmethod
    def unique_paths_with_obstacles(grid: List[List[int]]) -> int:
        """Unique Paths With Obstacles - O(n * m) time, O(n * m) space"""
        if not grid or not grid[0]:
            return 0
        
        n, m = len(grid), len(grid[0])
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1
        
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] if grid[i][0] == 0 else 0
        
        for j in range(1, m):
            dp[0][j] = dp[0][j - 1] if grid[0][j] == 0 else 0
        
        for i in range(1, n):
            for j in range(1, m):
                if grid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0
        
        return dp[n - 1][m - 1]
    
    @staticmethod
    def palindrome_partition(s: str) -> int:
        """Palindrome Partitioning - O(n^2) time, O(n^2) space"""
        n = len(s)
        dp = [True] + [False] * n
        
        for i in range(1, n + 1):
            for j in range(i):
                dp[j] = (s[j:i] == s[j:i][::-1]) and (j <= 1 or dp[j - 1])
        
        return sum(dp)
    
    @staticmethod
    def max_subarray_sum_circular(nums: List[int]) -> int:
        """Maximum Subarray Sum in Circular Array - O(n) time, O(1) space"""
        # Find normal maximum subarray sum
        max_kadane = ArrayAlgorithms.kadane_max_subarray_sum(nums)
        
        # Find minimum subarray sum
        min_kadane = -ArrayAlgorithms.kadane_max_subarray_sum([-x for x in nums])
        
        # Calculate total sum
        total_sum = sum(nums)
        
        # Maximum circular sum is either normal max or total sum - min subarray sum
        return max(max_kadane, total_sum + min_kadane)
    
    @staticmethod
    def max_product_subarray(nums: List[int]) -> int:
        """Maximum Product Subarray - O(n) time, O(1) space"""
        max_so_far = nums[0]
        max_ending_here = nums[0]
        min_ending_here = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_ending_here, min_ending_here = min_ending_here, max_ending_here
            
            max_ending_here = max(nums[i], max_ending_here * nums[i])
            min_ending_here = min(nums[i], min_ending_here * nums[i])
            max_so_far = max(max_so_far, max_ending_here)
        
        return max_so_far

# =============================================
# BIT MANIPULATION
# =============================================

class BitManipulation:
    """Bit manipulation utilities"""
    
    @staticmethod
    def count_set_bits(n: int) -> int:
        """Count set bits in binary representation"""
        return bin(n).count('1')
    
    @staticmethod
    def is_power_of_two(n: int) -> bool:
        """Check if n is a power of 2"""
        return n > 0 and (n & (n - 1)) == 0
    
    @staticmethod
    def single_number(nums: List[int]) -> int:
        """Single Number (XOR) - O(n) time, O(1) space"""
        result = 0
        for num in nums:
            result ^= num
        return result
    
    @staticmethod
    def reverse_bits(n: int) -> int:
        """Reverse bits of 32-bit integer"""
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result
    
    @staticmethod
    def hamming_distance(x: int, y: int) -> int:
        """Hamming Distance - O(1) time, O(1) space"""
        return BitManipulation.count_set_bits(x ^ y)
    
    @staticmethod
    def get_bit(n: int, pos: int) -> bool:
        """Get bit at position (0-indexed)"""
        return (n >> pos) & 1 == 1
    
    @staticmethod
    def set_bit(n: int, pos: int) -> int:
        """Set bit at position (0-indexed)"""
        return n | (1 << pos)
    
    @staticmethod
    def clear_bit(n: int, pos: int) -> int:
        """Clear bit at position (0-indexed)"""
        return n & ~(1 << pos)
    
    @staticmethod
    def toggle_bit(n: int, pos: int) -> int:
        """Toggle bit at position (0-indexed)"""
        return n ^ (1 << pos)
    
    @staticmethod
    def count_total_bits(n: int) -> int:
        """Count total bits from 1 to n"""
        count = 0
        i = 1
        while i <= n:
            count += BitManipulation.count_set_bits(i)
            i += 1
        return count
    
    @staticmethod
    def find_rightmost_set_bit(n: int) -> int:
        """Find rightmost set bit"""
        return n & -n
    
    @staticmethod
    def find_leftmost_set_bit(n: int) -> int:
        """Find leftmost set bit"""
        n |= n >> 1
        n += 1
        return n & -n

# =============================================
# DECORATORS AND UTILITIES
# =============================================

def timer(func):
    """Timer decorator to measure execution time"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def memoize(func):
    """Memoization decorator"""
    cache = {}
    
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    
    return wrapper

def debug_print(*args, **kwargs):
    """Debug print function"""
    if __debug__:
        print(f"[DEBUG] {' '.join(map(str, args))}", **kwargs)

# =============================================
# MAIN SOLVE FUNCTION
# =============================================

def solve():
    """Main solve function - modify this for each problem"""
    fast_print("=== Algorithm Templates Demonstration ===\n")
    
    # Example usage of algorithm templates
    
    # Sorting algorithms example
    arr = [64, 34, 25, 12, 22, 11, 90]
    fast_print("Original array:")
    fast_print(' '.join(map(str, arr)))
    
    # Test different sorting algorithms
    test_arr = arr.copy()
    SortingAlgorithms.bubble_sort(test_arr)
    fast_print("Bubble Sort:")
    fast_print(' '.join(map(str, test_arr)))
    
    test_arr = arr.copy()
    SortingAlgorithms.selection_sort(test_arr)
    fast_print("Selection Sort:")
    fast_print(' '.join(map(str, test_arr)))
    
    test_arr = arr.copy()
    SortingAlgorithms.insertion_sort(test_arr)
    fast_print("Insertion Sort:")
    fast_print(' '.join(map(str, test_arr)))
    
    test_arr = arr.copy()
    SortingAlgorithms.merge_sort(test_arr)
    fast_print("Merge Sort:")
    fast_print(' '.join(map(str, test_arr)))
    
    test_arr = arr.copy()
    SortingAlgorithms.quick_sort(test_arr)
    fast_print("Quick Sort:")
    fast_print(' '.join(map(str, test_arr)))
    
    test_arr = arr.copy()
    SortingAlgorithms.heap_sort(test_arr)
    fast_print("Heap Sort:")
    fast_print(' '.join(map(str, test_arr)))
    
    # Searching algorithms example
    sorted_arr = sorted(arr)
    target = 25
    fast_print(f"Linear search for {target}: {SearchingAlgorithms.linear_search(sorted_arr, target)}")
    fast_print(f"Binary search for {target}: {SearchingAlgorithms.binary_search(sorted_arr, target)}")
    fast_print(f"Lower bound for {target}: {SearchingAlgorithms.lower_bound(sorted_arr, target)}")
    fast_print(f"Upper bound for {target}: {SearchingAlgorithms.upper_bound(sorted_arr, target)}")
    
    # Array algorithms example
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    fast_print(f"Maximum subarray sum: {ArrayAlgorithms.kadane_max_subarray_sum(nums)}")
    
    two_sum_arr = [2, 7, 11, 15]
    two_sum_result = ArrayAlgorithms.two_sum(two_sum_arr, 9)
    fast_print(f"Two sum result: {two_sum_result}")
    
    three_sum_result = ArrayAlgorithms.three_sum([-1, 0, 1, 2, -1, -4])
    fast_print(f"Three sum result: {three_sum_result}")
    
    fast_print(f"Maximum product subarray: {ArrayAlgorithms.max_product_subarray(nums)}")
    fast_print(f"Find missing number in [0, 9]: {ArrayAlgorithms.find_missing_number([0, 1, 2, 3, 5, 6, 7, 8, 9])}")
    fast_print(f"Find duplicate number: {ArrayAlgorithms.find_duplicate_number([1, 3, 4, 2, 2])}")
    
    # String algorithms example
    text = "racecar"
    fast_print(f"Is '{text}' palindrome: {StringAlgorithms.is_palindrome(text)}")
    fast_print(f"Longest palindromic substring in 'babad': {StringAlgorithms.longest_palindromic_substring('babad')}")
    fast_print(f"Longest common prefix of ['flower', 'flow', 'flight']: {StringAlgorithms.longest_common_prefix(['flower', 'flow', 'flight'])}")
    fast_print(f"Valid parentheses '()[]{}': {StringAlgorithms.is_valid_parentheses('()[]{}')}")
    
    # Tree algorithms example
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    
    fast_print(f"Inorder traversal: {TreeAlgorithms.inorder_traversal(root)}")
    fast_print(f"Preorder traversal: {TreeAlgorithms.preorder_traversal(root)}")
    fast_print(f"Postorder traversal: {TreeAlgorithms.postorder_traversal(root)}")
    fast_print(f"Level order traversal: {TreeAlgorithms.level_order_traversal(root)}")
    fast_print(f"Max depth: {TreeAlgorithms.max_depth(root)}")
    fast_print(f"Is BST: {TreeAlgorithms.is_valid_bst(root)}")
    
    # Graph algorithms example
    graph = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: [4],
        4: []
    }
    
    fast_print(f"BFS from 0: {GraphAlgorithms.bfs(0, graph)}")
    fast_print(f"DFS from 0: {GraphAlgorithms.dfs(0, graph)}")
    
    weighted_graph = {
        0: [(1, 2), (2, 4)],
        1: [(3, 1)],
        2: [(3, 5)],
        3: [(4, 2)]
    }
    
    distances = GraphAlgorithms.dijkstra(0, weighted_graph)
    fast_print(f"Dijkstra from 0: {distances}")
    
    # Dynamic programming example
    fast_print(f"Fibonacci(10): {DynamicProgramming.fibonacci(10)}")
    fast_print(f"Coin change for 11 with [1,2,5]: {DynamicProgramming.coin_change([1, 2, 5], 11)}")
    fast_print(f"LCS of 'AGGTAB' and 'GXTXAYB': {DynamicProgramming.longest_common_subsequence('AGGTAB', 'GXTXAYB')}")
    fast_print(f"Edit distance between 'kitten' and 'sitting': {DynamicProgramming.edit_distance('kitten', 'sitting')}")
    
    # Bit manipulation example
    fast_print(f"Set bits in 13: {BitManipulation.count_set_bits(13)}")
    fast_print(f"Is 16 power of 2: {BitManipulation.is_power_of_two(16)}")
    fast_print(f"Single number in [2,2,1]: {BitManipulation.single_number([2, 2, 1])}")
    fast_print(f"Hamming distance between 10 and 20: {BitManipulation.hamming_distance(10, 20)}")

if __name__ == "__main__":
    try:
        solve()
    except Exception as e:
        fast_print(f"Error: {e}")
        sys.exit(1)
