# C++ Basic Problems - Complete Guide

## Overview

This section contains fundamental programming problems that help build problem-solving skills in C++. These problems cover patterns, searching algorithms, and sorting algorithms. Mastering these problems is essential for understanding how to translate logic into working C++ code before moving to advanced data structures and algorithms.

---

## Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [Patterns_Making.md](Patterns_Making.md) | understand Pattern Making in C++ |
| 2. | [Search/README.md](Search/README.md) | understand Searching Algorithms |
| 3. | [Sorting/README.md](Sorting/README.md) | understand Sorting Algorithms |

---

## 1. Patterns Making

Pattern making problems involve printing various shapes, numbers, and characters in specific arrangements using loops. These problems help develop logical thinking and understanding of nested loops.

### What you will learn:
- Nested loop structures (for, while, do-while)
- Controlling output format using `setw()` and manipulators
- Printing triangles, pyramids, diamonds, and number patterns
- Floyd's triangle, Pascal's triangle, and other mathematical patterns
- Star patterns, number patterns, and character patterns

### Key Concepts:
- Loop initialization, condition, and increment
- Relationship between row number and column count
- Spaces vs characters in pattern printing
- Using `cout` with manipulators for alignment

### Common Patterns Covered:

| Pattern Type | Examples |
|--------------|----------|
| Star Patterns | Right triangle, Pyramid, Diamond, Hourglass |
| Number Patterns | Floyd's triangle, Pascal's triangle, Number pyramid |
| Character Patterns | Alphabet triangle, ASCII art |
| Matrix Patterns | Spiral matrix, Magic square, Multiplication table |

---

## 2. Searching Algorithms

Searching algorithms are used to find the position of a target element within a collection of data. Different algorithms have different time complexities and are suitable for different scenarios.

### What you will learn:
- Linear search in unsorted arrays
- Binary search in sorted arrays
- Jump search and interpolation search
- Exponential search for unbounded arrays
- Ternary search for unimodal functions
- Hash-based search using unordered_set
- Tree-based search using BST

### Key Concepts:
- Time complexity analysis (Best, Average, Worst case)
- Space complexity trade-offs
- When to use which search algorithm
- Recursive vs iterative implementation
- Search on different data structures

### Search Algorithms Covered:

| # | Algorithm | Best For | Time Complexity |
| --- | --- | --- | --- |
| 1. | Linear Search | Small or unsorted arrays | O(n) |
| 2. | Binary Search | Sorted arrays | O(log n) |
| 3. | Jump Search | Sorted arrays (better than linear) | O(√n) |
| 4. | Interpolation Search | Uniformly distributed sorted data | O(log log n) |
| 5. | Exponential Search | Infinite or unbounded arrays | O(log n) |
| 6. | Fibonacci Search | Sorted arrays (reduces division) | O(log n) |
| 7. | Ternary Search | Unimodal functions | O(log n) |
| 8. | Sublist Search | Searching in linked lists | O(n) |
| 9. | Hash Search | Fast lookups with known keys | O(1) average |
| 10. | Tree Search | Dynamic data with ordering | O(log n) |

---

## 3. Sorting Algorithms

Sorting algorithms arrange elements in a specific order (ascending or descending). Understanding sorting algorithms is fundamental to computer science and algorithm design.

### What you will learn:
- Comparison-based vs non-comparison sorting
- Stable vs unstable sorting
- In-place vs out-of-place sorting
- Time and space complexity analysis
- When to use each sorting algorithm
- Adaptive sorting algorithms

### Key Concepts:
- Stability in sorting (preserving original order of equal elements)
- In-place sorting (no extra memory)
- Divide and conquer approach (Merge Sort, Quick Sort)
- Recursive vs iterative implementation
- Best, average, and worst-case scenarios

### Sorting Algorithms Covered:

| # | Algorithm | Type | Time (Avg) | Time (Worst) | Space | Stable |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Bubble Sort | Comparison | O(n²) | O(n²) | O(1) | Yes |
| 2. | Insertion Sort | Comparison | O(n²) | O(n²) | O(1) | Yes |
| 3. | Selection Sort | Comparison | O(n²) | O(n²) | O(1) | No |
| 4. | Merge Sort | Divide & Conquer | O(n log n) | O(n log n) | O(n) | Yes |
| 5. | Quick Sort | Divide & Conquer | O(n log n) | O(n²) | O(log n) | No |
| 6. | Heap Sort | Comparison | O(n log n) | O(n log n) | O(1) | No |
| 7. | Radix Sort | Non-comparison | O(d × n) | O(d × n) | O(n) | Yes |
| 8. | Counting Sort | Non-comparison | O(n + k) | O(n + k) | O(k) | Yes |
| 9. | Bucket Sort | Non-comparison | O(n + k) | O(n²) | O(n) | Yes |
| 10. | Shell Sort | Comparison | O(n log² n) | O(n²) | O(1) | No |
| 11. | Tim Sort | Hybrid | O(n log n) | O(n log n) | O(n) | Yes |
| 12. | Intro Sort | Hybrid | O(n log n) | O(n log n) | O(log n) | No |
| 13. | Cocktail Sort | Comparison | O(n²) | O(n²) | O(1) | Yes |
| 14. | Comb Sort | Comparison | O(n²) | O(n²) | O(1) | No |
| 15. | Gnome Sort | Comparison | O(n²) | O(n²) | O(1) | Yes |
| 16. | Odd-Even Sort | Comparison | O(n²) | O(n²) | O(1) | Yes |
| 17. | Bitonic Sort | Parallel | O(log² n) | O(log² n) | O(n log² n) | No |
| 18. | Pancake Sort | Comparison | O(n²) | O(n²) | O(1) | No |
| 19. | Cycle Sort | Comparison | O(n²) | O(n²) | O(1) | No |
| 20. | Bogo Sort | Comparison | O(n × n!) | O(∞) | O(1) | No |

---

## Algorithm Selection Guide

### By Input Size

| Input Size | Recommended Algorithms |
|------------|------------------------|
| n ≤ 50 | Any algorithm works (even O(n²)) |
| n ≤ 10⁵ | O(n log n) algorithms (Merge, Quick, Heap Sort) |
| n ≤ 10⁷ | O(n) or O(n log n) with low constant |
| n very large | External sorting algorithms |

### By Data Characteristics

| Data Type | Recommended Algorithm |
|-----------|----------------------|
| Already partially sorted | Insertion Sort, Tim Sort |
| Small range of values | Counting Sort, Radix Sort |
| Uniformly distributed | Bucket Sort |
| Linked list | Merge Sort |
| Small memory available | Heap Sort, Quick Sort |
| Need stable sort | Merge Sort, Bubble Sort, Insertion Sort |

### By Search Requirement

| Scenario | Recommended Algorithm |
|----------|----------------------|
| Unsorted array | Linear Search |
| Sorted array (single search) | Binary Search |
| Sorted array (multiple searches) | Binary Search or Hash Table |
| Large sorted array | Interpolation Search (uniform data) |
| Infinite/unknown size array | Exponential Search |
| Unimodal function | Ternary Search |

---

## Prerequisites

Before starting this section, you should have completed:

- [01. Basics](../01.%20Basics/README.md) - Variables, loops, functions, arrays
- Basic understanding of time complexity
- Familiarity with recursion (for some algorithms)

---

## Sample Problem Structure

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Function to implement the algorithm
void algorithmName(vector<int>& arr) {
    // Implementation
}

int main() {
    // Input
    vector<int> arr = {5, 2, 8, 1, 9};
    
    // Process
    algorithmName(arr);
    
    // Output
    for (int x : arr) {
        cout << x << " ";
    }
    
    return 0;
}
```

---

## Learning Path

```
Level 1: Pattern Making
├── Star Patterns (Triangle, Pyramid, Diamond)
├── Number Patterns (Floyd's Triangle, Pascal's Triangle)
└── Character Patterns

Level 2: Basic Searching
├── Linear Search
├── Binary Search
└── Jump Search

Level 3: Basic Sorting
├── Bubble Sort
├── Insertion Sort
└── Selection Sort

Level 4: Advanced Sorting
├── Merge Sort
├── Quick Sort
└── Heap Sort

Level 5: Specialized Sorting
├── Counting Sort
├── Radix Sort
└── Bucket Sort
```

---

## Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Off-by-one errors in loops | Carefully check loop boundaries |
| Not handling empty arrays | Add edge case checks |
| Using unstable sort when stability needed | Choose stable algorithm (Merge Sort) |
| Implementing binary search on unsorted array | Sort first or use linear search |
| Integer overflow in mid calculation | Use `left + (right - left) / 2` |
| Recursion depth too high | Use iterative version or increase stack |
| Not considering best/worst case | Analyze algorithm before choosing |

---

## Practice Problems

After completing this section, you should be able to:

1. Print a diamond pattern of stars for given height
2. Print Floyd's triangle for n rows
3. Search for an element in an unsorted array (Linear Search)
4. Search for an element in a sorted array (Binary Search)
5. Sort an array using Bubble Sort
6. Sort an array using Merge Sort
7. Sort an array using Quick Sort
8. Find the kth smallest element using Quick Select
9. Count the number of inversions in an array using Merge Sort
10. Sort an array of strings by length using Stable Sort

---

## Next Steps

- Go to [Patterns_Making.md](Patterns_Making.md) to understand Pattern Making in C++.