# 01_Introduction_to_Divide_and_Conquer.md

## Introduction to Divide and Conquer

### What is Divide and Conquer?

Divide and Conquer is an algorithmic paradigm that solves a problem by breaking it into smaller subproblems, solving each subproblem recursively, and then combining the results to form the solution to the original problem.

The name comes from military strategy: divide the enemy into smaller parts and conquer them individually.

### The Three Steps

```
Step 1: DIVIDE
        Break the problem into smaller subproblems of the same type
        │
        ▼
Step 2: CONQUER
        Solve each subproblem recursively
        If subproblem is small enough, solve directly (base case)
        │
        ▼
Step 3: COMBINE
        Merge the solutions of subproblems into solution of original problem
```

### Simple Example: Finding Maximum in an Array

**Problem:** Find the maximum element in an array.

**Divide and Conquer Approach:**

```
Divide: Split array into two halves
Conquer: Recursively find max in left half and right half
Combine: Return the larger of the two maxima

Base case: If array has 1 element, return that element
```

```cpp
int findMax(int arr[], int left, int right) {
    if (left == right) {
        return arr[left];  // base case
    }
    
    int mid = (left + right) / 2;
    int leftMax = findMax(arr, left, mid);
    int rightMax = findMax(arr, mid + 1, right);
    
    return max(leftMax, rightMax);
}
```

### Visual Example

```
Array: [3, 8, 1, 9, 4, 2, 7, 5]

Step 1: Divide into halves
[3, 8, 1, 9]  and  [4, 2, 7, 5]

Step 2: Further divide
[3, 8] and [1, 9]    [4, 2] and [7, 5]

Step 3: Further divide (base cases)
[3] [8] [1] [9]      [4] [2] [7] [5]

Step 4: Conquer (combine upwards)
[3,8] → max=8    [1,9] → max=9    [4,2] → max=4    [7,5] → max=7
[3,8,1,9] → max=9                     [4,2,7,5] → max=7
[3,8,1,9,4,2,7,5] → max=9

Result: 9
```

### Simple Example: Sum of Array

```cpp
int sumArray(int arr[], int left, int right) {
    if (left == right) {
        return arr[left];
    }
    
    int mid = (left + right) / 2;
    int leftSum = sumArray(arr, left, mid);
    int rightSum = sumArray(arr, mid + 1, right);
    
    return leftSum + rightSum;
}
```

### When to Use Divide and Conquer

| Condition | Description |
|-----------|-------------|
| Independent Subproblems | Subproblems should not overlap |
| Smaller Instances | Subproblems must be smaller instances of the same problem |
| Efficient Combine | Combining step must be efficient |
| Recursive Structure | Problem should have natural recursive breakdown |

### Divide and Conquer vs Brute Force

**Example: Maximum Subarray Sum**

| Approach | Time Complexity | Approach |
|----------|----------------|----------|
| Brute Force | O(n²) | Check all subarrays |
| Divide and Conquer | O(n log n) | Split and combine |
| Kadane's Algorithm | O(n) | Greedy/DP |

### Divide and Conquer vs Dynamic Programming

| Aspect | Divide and Conquer | Dynamic Programming |
|--------|--------------------|---------------------|
| Subproblems | Independent | Overlapping |
| Storage | No storage of subproblems | Stores results to reuse |
| Example | Merge Sort | Fibonacci |
| Typical complexity | O(n log n) | O(n²) |

### Common Divide and Conquer Algorithms

| Algorithm | Problem | Time Complexity |
|-----------|---------|-----------------|
| Merge Sort | Sorting | O(n log n) |
| Quick Sort | Sorting | O(n log n) average |
| Binary Search | Searching in sorted array | O(log n) |
| Power Exponentiation | Compute x^n | O(log n) |
| Strassen's | Matrix Multiplication | O(n^2.81) |
| Closest Pair | Find closest points | O(n log n) |
| Karatsuba | Multiply large numbers | O(n^1.585) |
| Quick Select | Find kth smallest | O(n) average |

### Implementation Template

```cpp
ResultType divideAndConquer(ProblemType problem) {
    // Base case
    if (problem is small enough) {
        return solveDirectly(problem);
    }
    
    // Divide
    auto subproblems = divide(problem);
    
    // Conquer
    ResultType leftResult = divideAndConquer(subproblems.left);
    ResultType rightResult = divideAndConquer(subproblems.right);
    
    // Combine
    return combine(leftResult, rightResult);
}
```

### Advantages

1. Often leads to efficient algorithms (O(n log n) vs O(n²))
2. Naturally parallelizable
3. Works well with cache memory
4. Clear and elegant recursive structure

### Disadvantages

1. Recursion overhead
2. Stack memory usage
3. May be overkill for small inputs
4. Harder to debug than iterative solutions

### Simple Problems to Start With

1. Find maximum element in array
2. Find sum of array elements
3. Count occurrences of a number
4. Check if array is sorted
5. Find power of a number

---