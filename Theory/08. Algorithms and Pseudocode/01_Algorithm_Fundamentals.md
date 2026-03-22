# Algorithm Fundamentals

## Overview

An algorithm is a finite sequence of well-defined, computer-implementable instructions, typically to solve a class of problems or to perform a computation. Understanding algorithm fundamentals is crucial for developing efficient and effective solutions to computational problems.

## What is an Algorithm?

### Definition and Characteristics
```text
An algorithm is a step-by-step procedure for solving a problem in a finite amount of time.

Key Characteristics:
1. Finiteness: Algorithm must terminate after a finite number of steps
2. Definiteness: Each step must be precisely defined and unambiguous
3. Input: Algorithm has zero or more well-defined inputs
4. Output: Algorithm produces one or more well-defined outputs
5. Effectiveness: Every instruction must be basic enough to be carried out
```

### Algorithm Example: Finding Maximum Element
```text
Problem: Find the maximum element in an array

Algorithm:
1. Start
2. Assume first element is maximum
3. For each element in the array:
   a. Compare current element with current maximum
   b. If current element is greater, update maximum
4. Return the maximum element
5. End

Time Complexity: O(n)
Space Complexity: O(1)
```

## Pseudocode Fundamentals

### What is Pseudocode?
```text
Pseudocode is a simplified, programming-language-agnostic algorithm description
that uses the structural conventions of a programming language but is intended
for human reading rather than machine reading.
```

### Pseudocode Conventions
```text
Common Pseudocode Elements:
- START/END: Begin and end of algorithm
- INPUT/OUTPUT: Data input and output operations
- IF/THEN/ELSE: Conditional statements
- FOR/WHILE: Loop constructs
- ASSIGNMENT: Variable assignment using ← or :=
- RETURN: Function return value
- COMMENTS: Explanatory notes (often in parentheses or with //)
```

### Basic Pseudocode Structure
```text
ALGORITHM FindMaximum(A[0..n-1])
BEGIN
    // Step 1: Initialize maximum
    max ← A[0]
    
    // Step 2: Iterate through array
    FOR i ← 1 TO n-1 DO
        // Step 3: Compare and update
        IF A[i] > max THEN
            max ← A[i]
        END IF
    END FOR
    
    // Step 4: Return result
    RETURN max
END
```

## Algorithm Design Principles

### 1. Divide and Conquer
```text
Principle: Break a complex problem into smaller subproblems, solve each independently,
and combine the results.

Example: Binary Search
- Divide: Split the search space in half
- Conquer: Search in the appropriate half
- Combine: Return the result

Pseudocode:
ALGORITHM BinarySearch(A[0..n-1], target)
BEGIN
    left ← 0
    right ← n-1
    
    WHILE left ≤ right DO
        mid ← left + (right - left) / 2
        
        IF A[mid] = target THEN
            RETURN mid
        ELSE IF A[mid] < target THEN
            left ← mid + 1
        ELSE
            right ← mid - 1
        END IF
    END WHILE
    
    RETURN -1  // Not found
END
```

### 2. Greedy Approach
```text
Principle: Make the locally optimal choice at each step with the hope of finding
a global optimum.

Example: Coin Change Problem (with standard denominations)
- Always choose the largest possible coin that doesn't exceed the remaining amount

Pseudocode:
ALGORITHM GreedyCoinChange(amount, coins[0..m-1])
BEGIN
    result ← empty list
    
    FOR i ← 0 TO m-1 DO
        WHILE amount ≥ coins[i] DO
            ADD coins[i] TO result
            amount ← amount - coins[i]
        END WHILE
    END FOR
    
    RETURN result
END
```

### 3. Dynamic Programming
```text
Principle: Break down a problem into simpler subproblems and store the results of
subproblems to avoid recomputation.

Example: Fibonacci Sequence
- Store previously computed values to avoid redundant calculations

Pseudocode:
ALGORITHM FibonacciDP(n)
BEGIN
    IF n ≤ 1 THEN
        RETURN n
    END IF
    
    // Create array to store results
    fib[0] ← 0
    fib[1] ← 1
    
    FOR i ← 2 TO n DO
        fib[i] ← fib[i-1] + fib[i-2]
    END FOR
    
    RETURN fib[n]
END
```

## Algorithm Analysis

### Time Complexity
```text
Time complexity measures how the running time of an algorithm grows with input size.

Common Time Complexities:
- O(1): Constant time
- O(log n): Logarithmic time
- O(n): Linear time
- O(n log n): Linearithmic time
- O(n²): Quadratic time
- O(2^n): Exponential time
- O(n!): Factorial time

Big O Notation Rules:
1. Drop constant factors: O(2n) = O(n)
2. Drop lower order terms: O(n² + n) = O(n²)
3. Consider worst-case scenario
```

### Space Complexity
```text
Space complexity measures how the memory usage of an algorithm grows with input size.

Common Space Complexities:
- O(1): Constant space
- O(n): Linear space
- O(n²): Quadratic space
- O(log n): Logarithmic space
```

### Analysis Example
```text
Algorithm: Find sum of array elements

Pseudocode:
ALGORITHM ArraySum(A[0..n-1])
BEGIN
    sum ← 0
    FOR i ← 0 TO n-1 DO
        sum ← sum + A[i]
    END FOR
    RETURN sum
END

Time Complexity Analysis:
- Initialization: O(1)
- Loop runs n times: O(n)
- Each iteration: O(1)
- Total: O(1 + n*1) = O(n)

Space Complexity Analysis:
- sum variable: O(1)
- Loop variable i: O(1)
- Total: O(1)
```

## Algorithm Correctness

### Proof Techniques
```text
1. Mathematical Induction:
   - Base case: Prove for smallest input
   - Inductive step: Assume true for k, prove for k+1

2. Loop Invariants:
   - Property that holds before, during, and after loop execution
   - Used to prove correctness of iterative algorithms

3. Contradiction:
   - Assume algorithm is incorrect, derive contradiction
```

### Loop Invariant Example
```text
Algorithm: Find maximum in array

Loop Invariant: At the start of each iteration i, max contains the maximum
of elements A[0] through A[i-1].

Initialization:
- Before first iteration (i=1), max = A[0]
- max is maximum of A[0] through A[0] ✓

Maintenance:
- Assume invariant holds at start of iteration i
- Compare A[i] with current max
- If A[i] > max, update max
- Now max is maximum of A[0] through A[i] ✓

Termination:
- When loop ends (i=n), max is maximum of A[0] through A[n-1]
- This is exactly what we want ✓
```

## Algorithm Design Patterns

### 1. Brute Force
```text
Approach: Try all possible solutions and pick the best one

Example: Maximum Subarray Problem (Brute Force)

Pseudocode:
ALGORITHM MaxSubarrayBrute(A[0..n-1])
BEGIN
    max_sum ← -∞
    
    FOR i ← 0 TO n-1 DO
        FOR j ← i TO n-1 DO
            current_sum ← 0
            FOR k ← i TO j DO
                current_sum ← current_sum + A[k]
            END FOR
            IF current_sum > max_sum THEN
                max_sum ← current_sum
            END IF
        END FOR
    END FOR
    
    RETURN max_sum
END

Time Complexity: O(n³)
Space Complexity: O(1)
```

### 2. Two Pointers
```text
Approach: Use two pointers to traverse data structure efficiently

Example: Find if array contains two numbers that sum to target

Pseudocode:
ALGORITHM TwoSum(A[0..n-1], target)
BEGIN
    left ← 0
    right ← n-1
    
    WHILE left < right DO
        sum ← A[left] + A[right]
        
        IF sum = target THEN
            RETURN (A[left], A[right])
        ELSE IF sum < target THEN
            left ← left + 1
        ELSE
            right ← right - 1
        END IF
    END WHILE
    
    RETURN null  // No solution found
END

Time Complexity: O(n log n) with sorting, O(n) if sorted
Space Complexity: O(1)
```

### 3. Sliding Window
```text
Approach: Maintain a window of elements that slides through the data structure

Example: Maximum sum of subarray of size k

Pseudocode:
ALGORITHM MaxWindowSum(A[0..n-1], k)
BEGIN
    IF k > n THEN
        RETURN "Invalid window size"
    END IF
    
    // Calculate sum of first window
    window_sum ← 0
    FOR i ← 0 TO k-1 DO
        window_sum ← window_sum + A[i]
    END FOR
    
    max_sum ← window_sum
    
    // Slide the window
    FOR i ← k TO n-1 DO
        window_sum ← window_sum + A[i] - A[i-k]
        IF window_sum > max_sum THEN
            max_sum ← window_sum
        END IF
    END FOR
    
    RETURN max_sum
END

Time Complexity: O(n)
Space Complexity: O(1)
```

## Algorithm Optimization Techniques

### 1. Memoization
```text
Technique: Store results of expensive function calls and reuse when same inputs occur

Example: Recursive Fibonacci with memoization

Pseudocode:
ALGORITHM FibonacciMemo(n, memo)
BEGIN
    IF n ≤ 1 THEN
        RETURN n
    END IF
    
    IF n in memo THEN
        RETURN memo[n]
    END IF
    
    memo[n] ← FibonacciMemo(n-1, memo) + FibonacciMemo(n-2, memo)
    RETURN memo[n]
END

Time Complexity: O(n) (without memoization: O(2^n))
Space Complexity: O(n)
```

### 2. Early Termination
```text
Technique: Stop algorithm execution early when solution is found or impossible

Example: Linear search with early termination

Pseudocode:
ALGORITHM LinearSearch(A[0..n-1], target)
BEGIN
    FOR i ← 0 TO n-1 DO
        IF A[i] = target THEN
            RETURN i  // Early termination
        END IF
    END FOR
    
    RETURN -1  // Not found
END
```

### 3. Preprocessing
```text
Technique: Perform initial processing to enable faster queries

Example: Range sum queries with prefix sum array

Pseudocode:
ALGORITHM PreprocessSum(A[0..n-1])
BEGIN
    prefix[0] ← 0
    FOR i ← 1 TO n DO
        prefix[i] ← prefix[i-1] + A[i-1]
    END FOR
    RETURN prefix
END

ALGORITHM RangeSum(prefix, left, right)
BEGIN
    RETURN prefix[right+1] - prefix[left]
END

Time Complexity: O(n) preprocessing, O(1) query
Space Complexity: O(n)
```

## Common Algorithm Categories

### 1. Sorting Algorithms
```text
Bubble Sort:
- Repeatedly swap adjacent elements if they're in wrong order
- Time: O(n²), Space: O(1)

Selection Sort:
- Find minimum element and place at beginning
- Time: O(n²), Space: O(1)

Insertion Sort:
- Build sorted array one element at a time
- Time: O(n²), Space: O(1)

Merge Sort:
- Divide array, sort halves, merge
- Time: O(n log n), Space: O(n)

Quick Sort:
- Partition array around pivot, recursively sort
- Time: O(n log n) average, O(n²) worst, Space: O(log n)
```

### 2. Searching Algorithms
```text
Linear Search:
- Sequential search through array
- Time: O(n), Space: O(1)

Binary Search:
- Search in sorted array by dividing search space
- Time: O(log n), Space: O(1)

Hash Table Search:
- Use hash function for direct access
- Time: O(1) average, Space: O(n)
```

### 3. Graph Algorithms
```text
Breadth-First Search (BFS):
- Level-by-level traversal
- Time: O(V+E), Space: O(V)

Depth-First Search (DFS):
- Go as deep as possible before backtracking
- Time: O(V+E), Space: O(V)

Dijkstra's Algorithm:
- Shortest path from source to all vertices
- Time: O(E log V), Space: O(V)

Prim's Algorithm:
- Minimum spanning tree
- Time: O(E log V), Space: O(V)
```

## Algorithm Implementation Tips

### 1. Start with Pseudocode
```text
Before coding:
1. Write clear pseudocode
2. Identify edge cases
3. Plan input/output format
4. Consider constraints
```

### 2. Handle Edge Cases
```text
Common Edge Cases:
- Empty input
- Single element
- All elements same
- Already sorted/reversed
- Minimum/maximum values
- Negative numbers
```

### 3. Test Incrementally
```text
Testing Strategy:
1. Test with small inputs
2. Test with edge cases
3. Test with random inputs
4. Test with large inputs (performance)
5. Compare with known solutions
```

### 4. Optimize Step by Step
```text
Optimization Process:
1. Get correct solution first
2. Identify bottlenecks
3. Optimize time complexity
4. Optimize space complexity
5. Consider constant factors
```

## Algorithm Problem-Solving Framework

### 1. Understand the Problem
```text
Questions to ask:
- What are the inputs and their constraints?
- What are the expected outputs?
- What are the edge cases?
- What are the time/space constraints?
```

### 2. Design Algorithm
```text
Design Process:
- Start with brute force solution
- Identify inefficiencies
- Apply appropriate techniques
- Write pseudocode
- Analyze complexity
```

### 3. Implement and Test
```text
Implementation Steps:
- Translate pseudocode to code
- Handle edge cases
- Write test cases
- Debug and fix issues
```

### 4. Optimize
```text
Optimization Checklist:
- Can we reduce time complexity?
- Can we reduce space complexity?
- Can we use better data structures?
- Can we apply known algorithms?
```

## Best Practices

### Algorithm Design
1. **Start Simple**: Begin with brute force, then optimize
2. **Use Appropriate Data Structures**: Choose based on operations needed
3. **Consider All Cases**: Handle edge cases and constraints
4. **Analyze Complexity**: Understand time and space requirements
5. **Test Thoroughly**: Verify correctness with various inputs

### Pseudocode Writing
1. **Be Clear and Unambiguous**: Use precise language
2. **Use Consistent Notation**: Follow standard conventions
3. **Include Comments**: Explain complex steps
4. **Handle Edge Cases**: Mention special cases
5. **Specify I/O**: Clearly define inputs and outputs

### Implementation
1. **Follow Pseudocode**: Implement as designed
2. **Use Meaningful Names**: Make code self-documenting
3. **Add Comments**: Explain non-obvious logic
4. **Handle Errors**: Include validation and error handling
5. **Optimize Gradually**: Improve performance step by step

## Conclusion

Algorithm fundamentals form the foundation of computer science and programming. Understanding how to design, analyze, and implement algorithms is essential for solving computational problems efficiently. Pseudocode provides a language-agnostic way to express algorithms, while various design patterns and optimization techniques help create efficient solutions. Mastering these fundamentals enables developers to tackle complex problems and write optimal code across different programming languages and domains.
