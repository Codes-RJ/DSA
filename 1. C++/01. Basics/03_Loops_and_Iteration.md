# C++ Loops and Iteration

## Overview

Loops are fundamental control structures that allow repeated execution of code blocks. C++ provides several types of loops and iteration mechanisms, each suited for different scenarios. Understanding loops and their relationship with data structures is crucial for efficient algorithm implementation.

## Types of Loops

### for Loop

#### Traditional for Loop
```cpp
#include <iostream>
#include <vector>

void traditionalForLoop() {
    // Basic for loop
    for (int i = 0; i < 5; i++) {
        std::cout << "Iteration " << i << "\n";
    }
    
    // For loop with multiple variables
    for (int i = 0, j = 10; i < 5 && j > 5; i++, j--) {
        std::cout << "i: " << i << ", j: " << j << "\n";
    }
    
    // For loop with vector
    std::vector<int> numbers = {10, 20, 30, 40, 50};
    for (size_t i = 0; i < numbers.size(); i++) {
        std::cout << "numbers[" << i << "] = " << numbers[i] << "\n";
    }
    
    // Reverse iteration
    for (int i = numbers.size() - 1; i >= 0; i--) {
        std::cout << "Reverse: " << numbers[i] << "\n";
    }
}
```

#### Range-Based for Loop (C++11)
```cpp
#include <iostream>
#include <vector>
#include <map>

void rangeBasedForLoop() {
    // Vector iteration
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    
    std::cout << "By value: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << "\n";
    
    std::cout << "By reference: ";
    for (int& num : numbers) {
        num *= 2;                                         // Modify the original
        std::cout << num << " ";
    }
    std::cout << "\n";
    
    std::cout << "By const reference: ";
    for (const int& num : numbers) {
        std::cout << num << " ";
    }
    std::cout << "\n";
    
    // Map iteration
    std::map<std::string, int> scores = {{"Alice", 95}, {"Bob", 87}, {"Charlie", 92}};
    
    std::cout << "Map contents:\n";
    for (const auto& [name, score] : scores) {            // C++17 structured binding
        std::cout << name << ": " << score << "\n";
    }
    
    // Array iteration
    int arr[] = {10, 20, 30};
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << "\n";
}
```

### while Loop

#### Basic while Loop
```cpp
#include <iostream>
#include <vector>

void basicWhileLoop() {
    // Simple counter
    int count = 0;
    while (count < 5) {
        std::cout << "Count: " << count << "\n";
        count++;
    }
    
    // Reading until condition
    int number;
    std::vector<int> inputs;
    
    std::cout << "Enter numbers (enter 0 to stop):\n";
    while (std::cin >> number && number != 0) {
        inputs.push_back(number);
    }
    
    std::cout << "You entered: ";
    for (int num : inputs) {
        std::cout << num << " ";
    }
    std::cout << "\n";
}
```

#### while Loop with Data Structures
```cpp
#include <iostream>
#include <stack>
#include <queue>

void whileWithDataStructures() {
    // Stack processing
    std::stack<int> stk;
    stk.push(1);
    stk.push(2);
    stk.push(3);
    
    std::cout << "Stack elements: ";
    while (!stk.empty()) {
        std::cout << stk.top() << " ";
        stk.pop();
    }
    std::cout << "\n";
    
    // Queue processing
    std::queue<int> q;
    q.push(10);
    q.push(20);
    q.push(30);
    
    std::cout << "Queue elements: ";
    while (!q.empty()) {
        std::cout << q.front() << " ";
        q.pop();
    }
    std::cout << "\n";
}
```

### do-while Loop

#### Basic do-while Loop
```cpp
#include <iostream>

void basicDoWhileLoop() {
    // Guaranteed at least one execution
    int count = 0;
    do {
        std::cout << "Count: " << count << "\n";
        count++;
    } while (count < 5);
    
    // Menu example
    int choice;
    do {
        std::cout << "\nMenu:\n";
        std::cout << "1. Option 1\n";
        std::cout << "2. Option 2\n";
        std::cout << "3. Exit\n";
        std::cout << "Enter choice: ";
        std::cin >> choice;
        
        switch (choice) {
            case 1:
                std::cout << "You chose Option 1\n";
                break;
            case 2:
                std::cout << "You chose Option 2\n";
                break;
            case 3:
                std::cout << "Exiting...\n";
                break;
            default:
                std::cout << "Invalid choice\n";
        }
    } while (choice != 3);
}
```

## Loop Control Statements

### break Statement
```cpp
#include <iostream>
#include <vector>

void breakStatement() {
    // Break out of loop
    for (int i = 0; i < 10; i++) {
        if (i == 5) {
            std::cout << "Breaking at i = " << i << "\n";
            break;
        }
        std::cout << "i = " << i << "\n";
    }
    
    // Break in nested loops
    std::vector<std::vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    
    std::cout << "Searching for 5:\n";
    bool found = false;
    for (size_t i = 0; i < matrix.size() && !found; i++) {
        for (size_t j = 0; j < matrix[i].size(); j++) {
            if (matrix[i][j] == 5) {
                std::cout << "Found 5 at [" << i << "][" << j << "]\n";
                found = true;
                break;  // Break inner loop
            }
        }
    }
}
```

### continue Statement
```cpp
#include <iostream>
#include <vector>

void continueStatement() {
    // Skip even numbers
    for (int i = 0; i < 10; i++) {
        if (i % 2 == 0) {
            continue;                                 // Skip even numbers
        }
        std::cout << "Odd: " << i << "\n";
    }
    
    // Process only positive numbers
    std::vector<int> numbers = {1, -2, 3, -4, 5, -6};
    
    std::cout << "Positive numbers: ";
    for (int num : numbers) {
        if (num < 0) {
            continue;                                 // Skip negative numbers
        }
        std::cout << num << " ";
    }
    std::cout << "\n";
}
```

### goto Statement (Use Sparingly)
```cpp
#include <iostream>

void gotoStatement() {
    // Example of goto (generally avoided in modern C++)
    int i = 0;
    
    start_loop:
    if (i >= 5) {
        goto end_loop;
    }
    
    std::cout << "i = " << i << "\n";
    i++;
    goto start_loop;
    
    end_loop:
    std::cout << "Loop ended\n";
    
    // Better alternative: use structured loops
    std::cout << "Better approach:\n";
    for (int j = 0; j < 5; j++) {
        std::cout << "j = " << j << "\n";
    }
}
```

## Iterators and Loop Integration

### Iterator-Based Loops
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <list>

void iteratorLoops() {
    // Vector with iterators
    std::vector<int> numbers = {10, 20, 30, 40, 50};
    
    std::cout << "Forward iteration: ";
    for (auto it = numbers.begin(); it != numbers.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    std::cout << "Reverse iteration: ";
    for (auto it = numbers.rbegin(); it != numbers.rend(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    // Map with iterators
    std::map<std::string, int> scores = {{"Alice", 95}, {"Bob", 87}};
    
    std::cout << "Map iteration: ";
    for (auto it = scores.begin(); it != scores.end(); ++it) {
        std::cout << it->first << ":" << it->second << " ";
    }
    std::cout << "\n";
    
    // List with iterators (efficient for insertion/deletion)
    std::list<int> linked_list = {1, 2, 3, 4, 5};
    
    std::cout << "List iteration: ";
    for (auto it = linked_list.begin(); it != linked_list.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    // Modifying while iterating
    for (auto it = numbers.begin(); it != numbers.end(); ++it) {
        if (*it % 20 == 0) {
            *it *= 2;                                              // Double multiples of 20
        }
    }
    
    std::cout << "After modification: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << "\n";
}
```

### Const Iterators
```cpp
#include <iostream>
#include <vector>

void constIterators() {
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    
    // Const iterator for read-only access
    std::cout << "Const iteration: ";
    for (auto it = numbers.cbegin(); it != numbers.cend(); ++it) {
        std::cout << *it << " ";
        // *it = 10;                                  // Error: cannot modify through const iterator
    }
    std::cout << "\n";
    
    // Const reference in range-based for loop
    std::cout << "Const reference iteration: ";
    for (const int& num : numbers) {
        std::cout << num << " ";
        // num = 10;                                  // Error: cannot modify const reference
    }
    std::cout << "\n";
}
```

## Advanced Loop Patterns

### Nested Loops
```cpp
#include <iostream>
#include <vector>

void nestedLoops() {
    // 2D array processing
    std::vector<std::vector<int>> matrix = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    
    std::cout << "Matrix:\n";
    for (size_t i = 0; i < matrix.size(); i++) {
        for (size_t j = 0; j < matrix[i].size(); j++) {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << "\n";
    }
    
    // Pattern printing
    std::cout << "Triangle pattern:\n";
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= i; j++) {
            std::cout << "* ";
        }
        std::cout << "\n";
    }
    
    // Cartesian product
    std::vector<int> set1 = {1, 2};
    std::vector<int> set2 = {3, 4, 5};
    
    std::cout << "Cartesian product:\n";
    for (int a : set1) {
        for (int b : set2) {
            std::cout << "(" << a << ", " << b << ") ";
        }
        std::cout << "\n";
    }
}
```

### Loop with Algorithms
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

void loopsWithAlgorithms() {
    std::vector<int> numbers = {5, 2, 8, 1, 9, 3};
    
    // Find and loop
    auto it = std::find(numbers.begin(), numbers.end(), 8);
    if (it != numbers.end()) {
        std::cout << "Found 8 at position: " << std::distance(numbers.begin(), it) << "\n";
    }
    
    // For each algorithm
    std::cout << "Square each number: ";
    std::for_each(numbers.begin(), numbers.end(), [](int& n) { n *= n; });
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << "\n";
    
    // Count if
    int even_count = std::count_if(numbers.begin(), numbers.end(), 
                                 [](int n) { return n % 2 == 0; });
    std::cout << "Even numbers: " << even_count << "\n";
    
    // Transform algorithm
    std::vector<int> doubled;
    std::transform(numbers.begin(), numbers.end(), std::back_inserter(doubled),
                  [](int n) { return n * 2; });
    
    std::cout << "Doubled numbers: ";
    for (int num : doubled) {
        std::cout << num << " ";
    }
    std::cout << "\n";
}
```

## Loops with Different Data Structures

### Array Loops
```cpp
#include <iostream>
#include <array>

void arrayLoops() {
    // C-style array
    int c_array[] = {1, 2, 3, 4, 5};
    int size = sizeof(c_array) / sizeof(c_array[0]);
    
    std::cout << "C-style array: ";
    for (int i = 0; i < size; i++) {
        std::cout << c_array[i] << " ";
    }
    std::cout << "\n";
    
    // std::array
    std::array<int, 5> modern_array = {10, 20, 30, 40, 50};
    
    std::cout << "std::array: ";
    for (int num : modern_array) {
        std::cout << num << " ";
    }
    std::cout << "\n";
    
    // Pointer arithmetic
    std::cout << "Pointer iteration: ";
    int* ptr = c_array;
    int* end = c_array + size;
    while (ptr != end) {
        std::cout << *ptr << " ";
        ptr++;
    }
    std::cout << "\n";
}
```

### Vector Loops
```cpp
#include <iostream>
#include <vector>

void vectorLoops() {
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    
    // Index-based access
    std::cout << "Index-based: ";
    for (size_t i = 0; i < numbers.size(); i++) {
        std::cout << numbers[i] << " ";
    }
    std::cout << "\n";
    
    // Iterator-based
    std::cout << "Iterator-based: ";
    for (auto it = numbers.begin(); it != numbers.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    // Range-based
    std::cout << "Range-based: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << "\n";
    
    // Modifying while iterating
    std::cout << "Doubling elements: ";
    for (int& num : numbers) {
        num *= 2;
        std::cout << num << " ";
    }
    std::cout << "\n";
    
    // Safe removal (erase-remove idiom)
    numbers.erase(std::remove(numbers.begin(), numbers.end(), 6), numbers.end());
    
    std::cout << "After removal: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << "\n";
}
```

### Map Loops
```cpp
#include <iostream>
#include <map>
#include <unordered_map>

void mapLoops() {
    // Ordered map
    std::map<std::string, int> ordered_scores = {
        {"Alice", 95}, {"Bob", 87}, {"Charlie", 92}
    };
    
    std::cout << "Ordered map:\n";
    for (const auto& [name, score] : ordered_scores) {
        std::cout << name << ": " << score << "\n";
    }
    
    // Unordered map
    std::unordered_map<std::string, int> unordered_scores = {
        {"Alice", 95}, {"Bob", 87}, {"Charlie", 92}
    };
    
    std::cout << "Unordered map:\n";
    for (const auto& pair : unordered_scores) {
        std::cout << pair.first << ": " << pair.second << "\n";
    }
    
    // Finding and iterating from position
    auto it = ordered_scores.find("Bob");
    if (it != ordered_scores.end()) {
        std::cout << "From Bob onwards:\n";
        for (auto map_it = it; map_it != ordered_scores.end(); ++map_it) {
            std::cout << map_it->first << ": " << map_it->second << "\n";
        }
    }
}
```

### Set Loops
```cpp
#include <iostream>
#include <set>
#include <unordered_set>

void setLoops() {
    // Ordered set
    std::set<int> ordered_numbers = {3, 1, 4, 1, 5, 9, 2, 6, 5};
    
    std::cout << "Ordered set (unique, sorted): ";
    for (int num : ordered_numbers) {
        std::cout << num << " ";
    }
    std::cout << "\n";
    
    // Unordered set
    std::unordered_set<int> unordered_numbers = {3, 1, 4, 1, 5, 9, 2, 6, 5};
    
    std::cout << "Unordered set (unique, unsorted): ";
    for (int num : unordered_numbers) {
        std::cout << num << " ";
    }
    std::cout << "\n";
    
    // Range iteration
    auto lower = ordered_numbers.lower_bound(3);
    auto upper = ordered_numbers.upper_bound(6);
    
    std::cout << "Range [3, 6]: ";
    for (auto it = lower; it != upper; ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
}
```

## Performance Considerations

### Loop Optimization
```cpp
#include <iostream>
#include <vector>
#include <chrono>

void loopPerformance() {
    std::vector<int> large_vector(1000000, 1);
    
    // Method 1: Index-based loop
    auto start = std::chrono::high_resolution_clock::now();
    long long sum1 = 0;
    for (size_t i = 0; i < large_vector.size(); i++) {
        sum1 += large_vector[i];
    }
    auto end = std::chrono::high_resolution_clock::now();
    auto duration1 = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    
    // Method 2: Iterator-based loop
    start = std::chrono::high_resolution_clock::now();
    long long sum2 = 0;
    for (auto it = large_vector.begin(); it != large_vector.end(); ++it) {
        sum2 += *it;
    }
    end = std::chrono::high_resolution_clock::now();
    auto duration2 = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    
    // Method 3: Range-based loop
    start = std::chrono::high_resolution_clock::now();
    long long sum3 = 0;
    for (int num : large_vector) {
        sum3 += num;
    }
    end = std::chrono::high_resolution_clock::now();
    auto duration3 = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    
    std::cout << "Index-based: " << duration1.count() << " μs\n";
    std::cout << "Iterator-based: " << duration2.count() << " μs\n";
    std::cout << "Range-based: " << duration3.count() << " μs\n";
    
    std::cout << "All sums equal: " << (sum1 == sum2 && sum2 == sum3) << "\n";
}
```

### Cache-Friendly Loops
```cpp
#include <iostream>
#include <vector>

void cacheFriendlyLoops() {
    // Row-major vs column-major access
    std::vector<std::vector<int>> matrix(1000, std::vector<int>(1000, 1));
    
    // Cache-friendly (row-major)
    auto start = std::chrono::high_resolution_clock::now();
    long long sum1 = 0;
    for (size_t i = 0; i < matrix.size(); i++) {
        for (size_t j = 0; j < matrix[i].size(); j++) {
            sum1 += matrix[i][j];
        }
    }
    auto end = std::chrono::high_resolution_clock::now();
    auto duration1 = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    
    // Cache-unfriendly (column-major)
    start = std::chrono::high_resolution_clock::now();
    long long sum2 = 0;
    for (size_t j = 0; j < matrix[0].size(); j++) {
        for (size_t i = 0; i < matrix.size(); i++) {
            sum2 += matrix[i][j];
        }
    }
    end = std::chrono::high_resolution_clock::now();
    auto duration2 = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    
    std::cout << "Row-major (cache-friendly): " << duration1.count() << " μs\n";
    std::cout << "Column-major (cache-unfriendly): " << duration2.count() << " μs\n";
}
```

## Modern C++ Loop Features

### std::for_each with Lambda
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

void forEachWithLambda() {
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    
    // Simple for_each
    std::cout << "Numbers: ";
    std::for_each(numbers.begin(), numbers.end(), 
                  [](int n) { std::cout << n << " "; });
    std::cout << "\n";
    
    // For_each with mutable lambda
    int counter = 0;
    std::for_each(numbers.begin(), numbers.end(), 
                  [counter](int n) mutable { 
                      std::cout << counter++ << ": " << n << "\n"; 
                  });
    
    // Transform with for_each
    std::for_each(numbers.begin(), numbers.end(), 
                  [](int& n) { n *= 2; });
    
    std::cout << "Doubled: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << "\n";
}
```

### Parallel Algorithms (C++17)
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <execution>

void parallelAlgorithms() {
    std::vector<int> numbers(1000000);
    for (size_t i = 0; i < numbers.size(); i++) {
        numbers[i] = i;
    }
    
    // Parallel sort
    std::sort(std::execution::par, numbers.begin(), numbers.end());
    
    // Parallel for_each
    std::for_each(std::execution::par, numbers.begin(), numbers.end(),
                  [](int& n) { n *= 2; });
    
    std::cout << "First 10 elements after parallel processing: ";
    for (int i = 0; i < 10; i++) {
        std::cout << numbers[i] << " ";
    }
    std::cout << "\n";
}
```

## Common Loop Patterns and Idioms

### Erase-Remove Idiom
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

void eraseRemoveIdiom() {
    std::vector<int> numbers = {1, 2, 3, 4, 5, 2, 6, 2, 7};
    
    std::cout << "Original: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << "\n";
    
    // Remove all 2s
    numbers.erase(std::remove(numbers.begin(), numbers.end(), 2), numbers.end());
    
    std::cout << "After removing 2s: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << "\n";
    
    // Remove based on condition
    numbers.erase(std::remove_if(numbers.begin(), numbers.end(),
                                [](int n) { return n % 2 == 0; }), 
                  numbers.end());
    
    std::cout << "After removing evens: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << "\n";
}
```

### Safe Container Modification
```cpp
#include <iostream>
#include <vector>
#include <list>

void safeModification() {
    // Vector: use index-based loop when removing
    std::vector<int> vec = {1, 2, 3, 4, 5, 6};
    
    std::cout << "Vector before: ";
    for (int num : vec) {
        std::cout << num << " ";
    }
    std::cout << "\n";
    
    for (size_t i = 0; i < vec.size(); ) {
        if (vec[i] % 2 == 0) {
            vec.erase(vec.begin() + i);
        } else {
            i++;
        }
    }
    
    std::cout << "Vector after removing evens: ";
    for (int num : vec) {
        std::cout << num << " ";
    }
    std::cout << "\n";
    
    // List: safe to remove while iterating
    std::list<int> lst = {1, 2, 3, 4, 5, 6};
    
    std::cout << "List before: ";
    for (int num : lst) {
        std::cout << num << " ";
    }
    std::cout << "\n";
    
    for (auto it = lst.begin(); it != lst.end(); ) {
        if (*it % 2 == 0) {
            it = lst.erase(it);
        } else {
            ++it;
        }
    }
    
    std::cout << "List after removing evens: ";
    for (int num : lst) {
        std::cout << num << " ";
    }
    std::cout << "\n";
}
```

## Best Practices

1. **Prefer range-based for loops** for simple iteration
2. **Use const iterators** when not modifying elements
3. **Be careful with iterator invalidation** when modifying containers
4. **Use erase-remove idiom** for efficient element removal
5. **Consider cache locality** for performance-critical loops
6. **Use appropriate loop type** based on the use case
7. **Avoid infinite loops** with clear exit conditions
8. **Use meaningful variable names** for loop counters
9. **Minimize loop overhead** by moving invariant code outside
10. **Consider parallel algorithms** for large datasets (C++17+)

## Conclusion

Loops are fundamental to programming and C++ provides various iteration mechanisms optimized for different scenarios. Understanding the relationship between loops and data structures, along with modern C++ features, enables writing efficient, readable, and maintainable code. The choice of loop type and iteration method can significantly impact both performance and code clarity.
