#!/usr/bin/env python3
"""
Basic Python Template for Competitive Programming and DSA Practice
Includes common utilities, data structures, and algorithms
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
# MATHEMATICAL UTILITIES
# =============================================

class MathUtils:
    """Mathematical utility functions"""
    
    @staticmethod
    def gcd(a: int, b: int) -> int:
        """Greatest Common Divisor using Euclidean algorithm"""
        return math.gcd(a, b)
    
    @staticmethod
    def lcm(a: int, b: int) -> int:
        """Least Common Multiple"""
        return a // MathUtils.gcd(a, b) * b
    
    @staticmethod
    def is_prime(n: int) -> bool:
        """Check if a number is prime"""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True
    
    @staticmethod
    def sieve_of_eratosthenes(n: int) -> List[bool]:
        """Sieve of Eratosthenes to find primes up to n"""
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        
        for p in range(2, int(n**0.5) + 1):
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
        
        return is_prime
    
    @staticmethod
    def factorial(n: int) -> int:
        """Calculate factorial"""
        return math.factorial(n)
    
    @staticmethod
    def fibonacci(n: int) -> int:
        """Calculate nth Fibonacci number"""
        if n <= 1:
            return n
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    @staticmethod
    def nCr(n: int, r: int) -> int:
        """Calculate combinations (n choose r)"""
        if r > n or r < 0:
            return 0
        if r == 0 or r == n:
            return 1
        
        r = min(r, n - r)
        result = 1
        for i in range(r):
            result = result * (n - i) // (i + 1)
        return result
    
    @staticmethod
    def nPr(n: int, r: int) -> int:
        """Calculate permutations (n permute r)"""
        if r > n or r < 0:
            return 0
        
        result = 1
        for i in range(r):
            result *= (n - i)
        return result
    
    @staticmethod
    def power(a: int, b: int, mod: int = MOD) -> int:
        """Fast exponentiation (a^b % mod)"""
        result = 1
        a %= mod
        
        while b > 0:
            if b & 1:
                result = (result * a) % mod
            a = (a * a) % mod
            b >>= 1
        
        return result
    
    @staticmethod
    def mod_inverse(a: int, mod: int = MOD) -> int:
        """Modular inverse using Fermat's little theorem (mod must be prime)"""
        return MathUtils.power(a, mod - 2, mod)
    
    @staticmethod
    def is_power_of_two(n: int) -> bool:
        """Check if n is a power of 2"""
        return n > 0 and (n & (n - 1)) == 0
    
    @staticmethod
    def count_set_bits(n: int) -> int:
        """Count set bits in binary representation"""
        return bin(n).count('1')
    
    @staticmethod
    def prime_factors(n: int) -> List[int]:
        """Get prime factors of n"""
        factors = []
        
        # Handle 2 separately
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        
        # Check odd divisors
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 2
        
        # If remaining n is prime
        if n > 2:
            factors.append(n)
        
        return factors

# =============================================
# STRING UTILITIES
# =============================================

class StringUtils:
    """String utility functions"""
    
    @staticmethod
    def is_palindrome(s: str) -> bool:
        """Check if string is palindrome"""
        return s == s[::-1]
    
    @staticmethod
    def is_palindrome_ignoring_case(s: str) -> bool:
        """Check if string is palindrome ignoring case"""
        s = s.lower()
        return s == s[::-1]
    
    @staticmethod
    def is_palindrome_ignoring_spaces_and_case(s: str) -> bool:
        """Check if string is palindrome ignoring spaces and case"""
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]
    
    @staticmethod
    def reverse_string(s: str) -> str:
        """Reverse a string"""
        return s[::-1]
    
    @staticmethod
    def are_anagrams(s1: str, s2: str) -> bool:
        """Check if two strings are anagrams"""
        return Counter(s1) == Counter(s2)
    
    @staticmethod
    def to_lower_case(s: str) -> str:
        """Convert string to lowercase"""
        return s.lower()
    
    @staticmethod
    def to_upper_case(s: str) -> str:
        """Convert string to uppercase"""
        return s.upper()
    
    @staticmethod
    def count_vowels(s: str) -> int:
        """Count vowels in string"""
        vowels = set('aeiouAEIOU')
        return sum(1 for c in s if c in vowels)
    
    @staticmethod
    def count_consonants(s: str) -> int:
        """Count consonants in string"""
        return sum(1 for c in s if c.isalpha() and c not in 'aeiouAEIOU')
    
    @staticmethod
    def remove_duplicates(s: str) -> str:
        """Remove duplicate characters from string"""
        seen = set()
        result = []
        for c in s:
            if c not in seen:
                seen.add(c)
                result.append(c)
        return ''.join(result)
    
    @staticmethod
    def get_all_substrings(s: str) -> List[str]:
        """Get all substrings of a string"""
        substrings = []
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n + 1):
                substrings.append(s[i:j])
        return substrings
    
    @staticmethod
    def longest_palindromic_substring(s: str) -> str:
        """Find longest palindromic substring"""
        if not s:
            return ""
        
        start, end = 0, 0
        
        for i in range(len(s)):
            len1 = StringUtils.expand_around_center(s, i, i)
            len2 = StringUtils.expand_around_center(s, i, i + 1)
            max_len = max(len1, len2)
            
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end + 1]
    
    @staticmethod
    def expand_around_center(s: str, left: int, right: int) -> int:
        """Expand around center for palindrome checking"""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    @staticmethod
    def longest_common_prefix(strs: List[str]) -> str:
        """Find longest common prefix among strings"""
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
        """Check if parentheses are valid"""
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
    def edit_distance(word1: str, word2: str) -> int:
        """Calculate edit distance between two strings"""
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

# =============================================
# ARRAY UTILITIES
# =============================================

class ArrayUtils:
    """Array utility functions"""
    
    @staticmethod
    def binary_search(arr: List[int], target: int) -> int:
        """Binary search in sorted array"""
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
    def lower_bound(arr: List[int], target: int) -> int:
        """Find first index where element >= target"""
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
        """Find first index where element > target"""
        left, right = 0, len(arr)
        
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
        
        return left
    
    @staticmethod
    def rotate_array(arr: List[int], k: int) -> None:
        """Rotate array by k positions to the right"""
        n = len(arr)
        k %= n
        if k < 0:
            k += n
        
        arr[:] = arr[-k:] + arr[:-k]
    
    @staticmethod
    def reverse_array(arr: List[int]) -> None:
        """Reverse array in-place"""
        arr.reverse()
    
    @staticmethod
    def find_max(arr: List[int]) -> int:
        """Find maximum element in array"""
        return max(arr) if arr else float('-inf')
    
    @staticmethod
    def find_min(arr: List[int]) -> int:
        """Find minimum element in array"""
        return min(arr) if arr else float('inf')
    
    @staticmethod
    def is_sorted(arr: List[int]) -> bool:
        """Check if array is sorted in non-decreasing order"""
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    
    @staticmethod
    def sum_array(arr: List[int]) -> int:
        """Calculate sum of array elements"""
        return sum(arr)
    
    @staticmethod
    def product_array(arr: List[int]) -> int:
        """Calculate product of array elements"""
        result = 1
        for num in arr:
            result *= num
        return result
    
    @staticmethod
    def merge_sorted_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
        """Merge two sorted arrays"""
        merged = []
        i, j = 0, 0
        
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        
        merged.extend(arr1[i:])
        merged.extend(arr2[j:])
        return merged
    
    @staticmethod
    def generate_random_array(n: int, min_val: int, max_val: int) -> List[int]:
        """Generate random array"""
        return [random.randint(min_val, max_val) for _ in range(n)]
    
    @staticmethod
    def print_array(arr: List[Any]) -> None:
        """Print array elements"""
        print(' '.join(map(str, arr)))

# =============================================
# SORTING ALGORITHMS
# =============================================

class SortingAlgorithms:
    """Sorting algorithm implementations"""
    
    @staticmethod
    def bubble_sort(arr: List[int]) -> List[int]:
        """Bubble sort"""
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
        """Selection sort"""
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
        """Insertion sort"""
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
        """Merge sort"""
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
        """Quick sort"""
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return SortingAlgorithms.quick_sort(left) + middle + SortingAlgorithms.quick_sort(right)
    
    @staticmethod
    def heap_sort(arr: List[int]) -> List[int]:
        """Heap sort"""
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
        """Counting sort"""
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
        """Radix sort"""
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

# =============================================
# SEARCHING ALGORITHMS
# =============================================

class SearchingAlgorithms:
    """Searching algorithm implementations"""
    
    @staticmethod
    def linear_search(arr: List[int], target: int) -> int:
        """Linear search"""
        for i, val in enumerate(arr):
            if val == target:
                return i
        return -1
    
    @staticmethod
    def binary_search(arr: List[int], target: int) -> int:
        """Binary search (iterative)"""
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
        """Binary search (recursive)"""
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
    def jump_search(arr: List[int], target: int) -> int:
        """Jump search"""
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
        """Interpolation search"""
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
        """Exponential search"""
        if len(arr) == 0:
            return -1
        if arr[0] == target:
            return 0
        
        i = 1
        while i < len(arr) and arr[i] <= target:
            i *= 2
        
        return SearchingAlgorithms.binary_search(arr[:min(i, len(arr))], target)

# =============================================
# DATA STRUCTURES
# =============================================

class Stack:
    """Stack implementation using list"""
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Push item onto stack"""
        self.items.append(item)
    
    def pop(self):
        """Pop item from stack"""
        if self.empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """Peek at top item"""
        if self.empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def empty(self) -> bool:
        """Check if stack is empty"""
        return len(self.items) == 0
    
    def size(self) -> int:
        """Get stack size"""
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

class Queue:
    """Queue implementation using deque"""
    
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        """Add item to queue"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove item from queue"""
        if self.empty():
            raise IndexError("Queue is empty")
        return self.items.popleft()
    
    def front(self):
        """Get front item"""
        if self.empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def empty(self) -> bool:
        """Check if queue is empty"""
        return len(self.items) == 0
    
    def size(self) -> int:
        """Get queue size"""
        return len(self.items)
    
    def __str__(self):
        return str(list(self.items))

class MinHeap:
    """Min-heap implementation"""
    
    def __init__(self):
        self.heap = []
    
    def push(self, item):
        """Add item to heap"""
        heapq.heappush(self.heap, item)
    
    def pop(self):
        """Remove and return smallest item"""
        if self.empty():
            raise IndexError("Heap is empty")
        return heapq.heappop(self.heap)
    
    def peek(self):
        """Peek at smallest item"""
        if self.empty():
            raise IndexError("Heap is empty")
        return self.heap[0]
    
    def empty(self) -> bool:
        """Check if heap is empty"""
        return len(self.heap) == 0
    
    def size(self) -> int:
        """Get heap size"""
        return len(self.heap)
    
    def __str__(self):
        return str(self.heap)

class MaxHeap:
    """Max-heap implementation"""
    
    def __init__(self):
        self.heap = []
    
    def push(self, item):
        """Add item to heap"""
        heapq.heappush(self.heap, -item)
    
    def pop(self):
        """Remove and return largest item"""
        if self.empty():
            raise IndexError("Heap is empty")
        return -heapq.heappop(self.heap)
    
    def peek(self):
        """Peek at largest item"""
        if self.empty():
            raise IndexError("Heap is empty")
        return -self.heap[0]
    
    def empty(self) -> bool:
        """Check if heap is empty"""
        return len(self.heap) == 0
    
    def size(self) -> int:
        """Get heap size"""
        return len(self.heap)
    
    def __str__(self):
        return str([-x for x in self.heap])

class DisjointSetUnion:
    """Disjoint Set Union (Union-Find) implementation"""
    
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x: int) -> int:
        """Find with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> None:
        """Union with rank optimization"""
        x_root = self.find(x)
        y_root = self.find(y)
        
        if x_root == y_root:
            return
        
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1
    
    def connected(self, x: int, y: int) -> bool:
        """Check if two elements are connected"""
        return self.find(x) == self.find(y)

class TrieNode:
    """Trie node implementation"""
    
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """Trie implementation"""
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """Insert word into trie"""
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        """Search word in trie"""
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word
    
    def starts_with(self, prefix: str) -> bool:
        """Check if any word starts with prefix"""
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
    
    def remove(self, word: str) -> None:
        """Remove word from trie"""
        self._remove(self.root, word, 0)
    
    def _remove(self, node: TrieNode, word: str, depth: int) -> bool:
        """Helper function for remove"""
        if depth == len(word):
            if not node.is_end_of_word:
                return False
            node.is_end_of_word = False
            return len(node.children) == 0
        
        char = word[depth]
        if char not in node.children:
            return False
        
        child_node = node.children[char]
        should_delete_child = self._remove(child_node, word, depth + 1)
        
        if should_delete_child:
            del node.children[char]
            return len(node.children) == 0 and not node.is_end_of_word
        
        return False

# =============================================
# COMMON ALGORITHMS
# =============================================

class CommonAlgorithms:
    """Common algorithm implementations"""
    
    @staticmethod
    def kadane_max_subarray_sum(nums: List[int]) -> int:
        """Kadane's algorithm for maximum subarray sum"""
        max_so_far = nums[0]
        max_ending_here = nums[0]
        
        for i in range(1, len(nums)):
            max_ending_here = max(nums[i], max_ending_here + nums[i])
            max_so_far = max(max_so_far, max_ending_here)
        
        return max_so_far
    
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        """Two sum problem"""
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []
    
    @staticmethod
    def three_sum(nums: List[int]) -> List[List[int]]:
        """Three sum problem"""
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
    def max_product_subarray(nums: List[int]) -> int:
        """Maximum product subarray"""
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
        """Find missing number in array [0, n]"""
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
    
    @staticmethod
    def find_duplicate_number(nums: List[int]) -> int:
        """Find duplicate number in array"""
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
    def longest_increasing_subsequence(nums: List[int]) -> int:
        """Longest increasing subsequence"""
        if not nums:
            return 0
        
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
    
    @staticmethod
    def coin_change(coins: List[int], amount: int) -> int:
        """Coin change problem"""
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != amount + 1 else -1
    
    @staticmethod
    def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
        """0/1 knapsack problem"""
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
    def longest_common_subsequence(text1: str, text2: str) -> int:
        """Longest common subsequence"""
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]

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
    fast_print("=== Python Template Demonstration ===\n")
    
    # Example usage of the template
    
    # Read input example
    fast_print("Enter number of elements:")
    n = int(fast_input())
    
    arr = list(map(int, fast_input().split()))
    if len(arr) != n:
        arr = arr[:n]  # Ensure we have exactly n elements
    
    fast_print("Original array:")
    ArrayUtils.print_array(arr)
    
    # Sorting example
    sorted_arr = SortingAlgorithms.merge_sort(arr.copy())
    fast_print("Sorted array:")
    ArrayUtils.print_array(sorted_arr)
    
    # Search example
    fast_print("Enter target to search:")
    target = int(fast_input())
    index = SearchingAlgorithms.binary_search(sorted_arr, target)
    if index != -1:
        fast_print(f"Found at index: {index}")
    else:
        fast_print("Not found")
    
    # Math utilities example
    fast_print(f"GCD of 48 and 18: {MathUtils.gcd(48, 18)}")
    fast_print(f"LCM of 48 and 18: {MathUtils.lcm(48, 18)}")
    fast_print(f"Is 17 prime: {MathUtils.is_prime(17)}")
    
    # String utilities example
    text = "racecar"
    fast_print(f"Is '{text}' palindrome: {StringUtils.is_palindrome(text)}")
    fast_print(f"Longest palindromic substring in 'babad': {StringUtils.longest_palindromic_substring('babad')}")
    
    # Array algorithms example
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    fast_print(f"Maximum subarray sum: {CommonAlgorithms.kadane_max_subarray_sum(nums)}")
    
    two_sum_arr = [2, 7, 11, 15]
    two_sum_result = CommonAlgorithms.two_sum(two_sum_arr, 9)
    fast_print(f"Two sum result: {two_sum_result}")
    
    # Data structures example
    fast_print("\n=== Data Structure Demonstrations ===")
    
    # Stack example
    stack = Stack()
    for i in [10, 20, 30]:
        stack.push(i)
    
    fast_print("Stack elements:")
    while not stack.empty():
        fast_print(stack.peek(), end=" ")
        stack.pop()
    fast_print()
    
    # Queue example
    queue = Queue()
    for i in [10, 20, 30]:
        queue.enqueue(i)
    
    fast_print("Queue elements:")
    while not queue.empty():
        fast_print(queue.front(), end=" ")
        queue.dequeue()
    fast_print()
    
    # Min-Heap example
    min_heap = MinHeap()
    for i in [30, 10, 20, 40]:
        min_heap.push(i)
    
    fast_print("Min-heap elements:")
    while not min_heap.empty():
        fast_print(min_heap.peek(), end=" ")
        min_heap.pop()
    fast_print()
    
    # Max-Heap example
    max_heap = MaxHeap()
    for i in [30, 10, 20, 40]:
        max_heap.push(i)
    
    fast_print("Max-heap elements:")
    while not max_heap.empty():
        fast_print(max_heap.peek(), end=" ")
        max_heap.pop()
    fast_print()
    
    # DSU example
    dsu = DisjointSetUnion(5)
    dsu.union(0, 1)
    dsu.union(1, 2)
    dsu.union(3, 4)
    fast_print(f"Is 0 connected to 2: {dsu.connected(0, 2)}")
    fast_print(f"Is 0 connected to 3: {dsu.connected(0, 3)}")
    
    # Trie example
    trie = Trie()
    for word in ["hello", "world", "help"]:
        trie.insert(word)
    
    fast_print(f"Search 'hello': {trie.search('hello')}")
    fast_print(f"Search 'hell': {trie.search('hell')}")
    fast_print(f"Starts with 'hel': {trie.starts_with('hel')}")
    trie.remove("hello")
    fast_print(f"Search 'hello' after removal: {trie.search('hello')}")
    
    # Common algorithms example
    fast_print(f"Fibonacci(10): {MathUtils.fibonacci(10)}")
    fast_print(f"Coin change for 11: {CommonAlgorithms.coin_change([1, 2, 5], 11)}")
    
    # Bit manipulation example
    fast_print(f"Set bits in 13: {MathUtils.count_set_bits(13)}")
    fast_print(f"Is 16 power of 2: {MathUtils.is_power_of_two(16)}")

if __name__ == "__main__":
    try:
        solve()
    except Exception as e:
        fast_print(f"Error: {e}")
        sys.exit(1)
