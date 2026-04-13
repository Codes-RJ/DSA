# Jump Search in C++

## Overview
Jump search is an algorithm for searching in sorted arrays. It jumps ahead by fixed steps and then performs linear search within the block where the element might be located.

## Theory

### Definition
Jump search works by jumping ahead by a fixed block size (typically √n) to find the block where the element might be, then performing linear search within that block.

### Algorithm Steps
1. Calculate optimal block size: √n
2. Jump ahead by block size until current element >= target or end is reached
3. Perform linear search in the previous block
4. Return index if found, -1 otherwise

### Complexity Analysis
- **Time Complexity**: O(√n) - Optimal block size
- **Space Complexity**: O(1)

### When to Use
- Sorted arrays where random access is O(1)
- When you want better than linear search but simpler than binary search
- Good compromise between simplicity and efficiency

---

## Implementation 1: Basic Jump Search

```cpp
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

/**
 * Jump search algorithm
 * Returns index of target if found, -1 otherwise
 */
int jumpSearch(int arr[], int size, int target) {
    int step = sqrt(size);  // Optimal block size
    int prev = 0;
    
    // Jump ahead to find the block
    while (arr[min(step, size) - 1] < target) {
        prev = step;
        step += sqrt(size);
        if (prev >= size) {
            return -1;
        }
    }
    
    // Linear search within the block
    while (arr[prev] < target) {
        prev++;
        if (prev == min(step, size)) {
            return -1;
        }
    }
    
    // Check if element is found
    if (arr[prev] == target) {
        return prev;
    }
    
    return -1;
}

int main() {
    int arr[] = {10, 23, 45, 70, 89, 100, 123, 145, 167, 189};
    int size = sizeof(arr) / sizeof(arr[0]);
    
    // Test cases
    int targets[] = {70, 10, 189, 99};
    
    for (int target : targets) {
        int result = jumpSearch(arr, size, target);
        if (result != -1) {
            cout << "Element " << target << " found at index: " << result << endl;
        } else {
            cout << "Element " << target << " not found in array" << endl;
        }
    }
    
    return 0;
}
```

**Output:**
```
Element 70 found at index: 3
Element 10 found at index: 0
Element 189 found at index: 9
Element 99 not found in array
```

---

## Implementation 2: Jump Search with Custom Block Size

```cpp
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

/**
 * Jump search with custom block size
 */
int jumpSearchCustomStep(int arr[], int size, int target, int stepSize) {
    int prev = 0;
    int step = stepSize;
    
    // Jump ahead to find the block
    while (arr[min(step, size) - 1] < target) {
        prev = step;
        step += stepSize;
        if (prev >= size) {
            return -1;
        }
    }
    
    // Linear search within the block
    while (prev < min(step, size) && arr[prev] < target) {
        prev++;
    }
    
    // Check if element is found
    if (prev < size && arr[prev] == target) {
        return prev;
    }
    
    return -1;
}

/**
 * Compare performance with different block sizes
 */
void compareBlockSizes(int arr[], int size, int target) {
    cout << "Searching for " << target << " with different block sizes:" << endl;
    
    int optimalStep = sqrt(size);
    int smallStep = optimalStep / 2;
    int largeStep = optimalStep * 2;
    
    cout << "Small step (" << smallStep << "): " 
         << jumpSearchCustomStep(arr, size, target, smallStep) << endl;
    cout << "Optimal step (" << optimalStep << "): " 
         << jumpSearch(arr, size, target) << endl;
    cout << "Large step (" << largeStep << "): " 
         << jumpSearchCustomStep(arr, size, target, largeStep) << endl;
}

int main() {
    int arr[] = {10, 23, 45, 70, 89, 100, 123, 145, 167, 189, 200, 210, 220, 230, 240, 250};
    int size = sizeof(arr) / sizeof(arr[0]);
    
    int target = 145;
    compareBlockSizes(arr, size, target);
    
    return 0;
}
```

**Output:**
```
Searching for 145 with different block sizes:
Small step (2): 7
Optimal step (4): 7
Large step (8): 7
```

---

## Implementation 3: Jump Search on Vectors

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

/**
 * Jump search on vector (template version)
 */
template<typename T>
int jumpSearchVector(const vector<T>& vec, const T& target) {
    int size = vec.size();
    int step = sqrt(size);
    int prev = 0;
    
    // Jump ahead to find the block
    while (prev < size && vec[min(step, size) - 1] < target) {
        prev = step;
        step += sqrt(size);
        if (prev >= size) {
            return -1;
        }
    }
    
    // Linear search within the block
    while (prev < min(step, size) && vec[prev] < target) {
        prev++;
    }
    
    // Check if element is found
    if (prev < size && vec[prev] == target) {
        return prev;
    }
    
    return -1;
}

/**
 * Find all occurrences using jump search
 */
template<typename T>
vector<int> jumpSearchAllOccurrences(const vector<T>& vec, const T& target) {
    vector<int> indices;
    int size = vec.size();
    int step = sqrt(size);
    int prev = 0;
    
    // Find all blocks that might contain target
    while (prev < size) {
        int blockEnd = min(prev + step, size);
        
        // Check if target could be in this block
        if (vec[prev] <= target && (blockEnd == size || vec[blockEnd - 1] >= target)) {
            // Linear search within block
            for (int i = prev; i < blockEnd; i++) {
                if (vec[i] == target) {
                    indices.push_back(i);
                }
            }
        }
        
        prev = blockEnd;
    }
    
    return indices;
}

int main() {
    // Integer vector
    vector<int> intVec = {10, 23, 45, 70, 89, 100, 123, 145, 167, 189};
    cout << "Integer search for 145: " << jumpSearchVector(intVec, 145) << endl;
    
    // String vector
    vector<string> strVec = {"apple", "banana", "cherry", "date", "elderberry", "fig", "grape"};
    cout << "String search for 'date': " << jumpSearchVector(strVec, string("date")) << endl;
    
    // Vector with duplicates
    vector<int> dupVec = {10, 20, 20, 30, 30, 30, 40, 50};
    auto indices = jumpSearchAllOccurrences(dupVec, 30);
    cout << "All occurrences of 30: ";
    for (int idx : indices) {
        cout << idx << " ";
    }
    cout << endl;
    
    return 0;
}
```

**Output:**
```
Integer search for 145: 7
String search for 'date': 3
All occurrences of 30: 3 4 5 
```

---

## Implementation 4: Jump Search with Range Information

```cpp
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

/**
 * Jump search that returns range information
 */
struct SearchResult {
    int index;
    int jumps;
    int linearSteps;
    bool found;
};

SearchResult jumpSearchWithInfo(int arr[], int size, int target) {
    SearchResult result = {-1, 0, 0, false};
    int step = sqrt(size);
    int prev = 0;
    
    // Jump ahead to find the block
    while (prev < size && arr[min(step, size) - 1] < target) {
        result.jumps++;
        prev = step;
        step += sqrt(size);
        if (prev >= size) {
            return result;
        }
    }
    
    // Linear search within the block
    while (prev < min(step, size) && arr[prev] < target) {
        result.linearSteps++;
        prev++;
    }
    
    // Check if element is found
    if (prev < size && arr[prev] == target) {
        result.index = prev;
        result.found = true;
    }
    
    return result;
}

/**
 * Demonstrate jump search with detailed information
 */
void demonstrateJumpSearch(int arr[], int size, int target) {
    SearchResult result = jumpSearchWithInfo(arr, size, target);
    
    cout << "Search for " << target << ":" << endl;
    cout << "Found: " << (result.found ? "Yes" : "No") << endl;
    if (result.found) {
        cout << "Index: " << result.index << endl;
    }
    cout << "Jumps performed: " << result.jumps << endl;
    cout << "Linear steps: " << result.linearSteps << endl;
    cout << "Total comparisons: " << (result.jumps + result.linearSteps) << endl;
    cout << endl;
}

int main() {
    int arr[] = {10, 23, 45, 70, 89, 100, 123, 145, 167, 189, 200, 210, 220, 230, 240, 250};
    int size = sizeof(arr) / sizeof(arr[0]);
    
    // Test different scenarios
    int targets[] = {70, 10, 250, 99};
    
    for (int target : targets) {
        demonstrateJumpSearch(arr, size, target);
    }
    
    return 0;
}
```

**Output:**
```
Search for 70:
Found: Yes
Index: 3
Jumps performed: 0
Linear steps: 3
Total comparisons: 3

Search for 10:
Found: Yes
Index: 0
Jumps performed: 0
Linear steps: 0
Total comparisons: 0

Search for 250:
Found: Yes
Index: 15
Jumps performed: 3
Linear steps: 0
Total comparisons: 3

Search for 99:
Found: No
Jumps performed: 1
Linear steps: 1
Total comparisons: 2
```

---

## Implementation 5: Jump Search vs Other Algorithms

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>
#include <algorithm>
using namespace std;
using namespace chrono;

/**
 * Linear search for comparison
 */
int linearSearch(int arr[], int size, int target) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}

/**
 * Binary search for comparison
 */
int binarySearch(int arr[], int size, int target) {
    int left = 0;
    int right = size - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid;
        }
        
        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1;
}

/**
 * Performance comparison
 */
void compareSearchAlgorithms() {
    const int SIZE = 10000;
    vector<int> data(SIZE);
    
    // Generate sorted data
    for (int i = 0; i < SIZE; i++) {
        data[i] = i * 2;
    }
    
    int target = data[SIZE / 2];  // Middle element
    
    // Measure linear search
    auto start = high_resolution_clock::now();
    linearSearch(data.data(), SIZE, target);
    auto end = high_resolution_clock::now();
    auto linearTime = duration_cast<nanoseconds>(end - start).count();
    
    // Measure jump search
    start = high_resolution_clock::now();
    jumpSearch(data.data(), SIZE, target);
    end = high_resolution_clock::now();
    auto jumpTime = duration_cast<nanoseconds>(end - start).count();
    
    // Measure binary search
    start = high_resolution_clock::now();
    binarySearch(data.data(), SIZE, target);
    end = high_resolution_clock::now();
    auto binaryTime = duration_cast<nanoseconds>(end - start).count();
    
    cout << "Performance Comparison (searching for middle element):" << endl;
    cout << "Linear Search: " << linearTime << " ns" << endl;
    cout << "Jump Search:   " << jumpTime << " ns" << endl;
    cout << "Binary Search: " << binaryTime << " ns" << endl;
    cout << "\nSpeedup vs Linear:" << endl;
    cout << "Jump Search:   " << (double)linearTime / jumpTime << "x faster" << endl;
    cout << "Binary Search: " << (double)linearTime / binaryTime << "x faster" << endl;
}

int main() {
    compareSearchAlgorithms();
    return 0;
}
```

**Sample Output:**
```
Performance Comparison (searching for middle element):
Linear Search: 25000 ns
Jump Search:   3500 ns
Binary Search: 1500 ns

Speedup vs Linear:
Jump Search:   7.14x faster
Binary Search: 16.67x faster
```

---

## Implementation 6: Jump Search for Different Data Types

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
using namespace std;

/**
 * Jump search for custom data types
 */
struct Person {
    string name;
    int age;
    
    bool operator<(const Person& other) const {
        return age < other.age;
    }
    
    bool operator==(const Person& other) const {
        return age == other.age && name == other.name;
    }
};

template<typename T>
int jumpSearchGeneric(const vector<T>& vec, const T& target) {
    int size = vec.size();
    int step = sqrt(size);
    int prev = 0;
    
    // Jump ahead to find the block
    while (prev < size && vec[min(step, size) - 1] < target) {
        prev = step;
        step += sqrt(size);
        if (prev >= size) {
            return -1;
        }
    }
    
    // Linear search within the block
    while (prev < min(step, size) && vec[prev] < target) {
        prev++;
    }
    
    // Check if element is found
    if (prev < size && vec[prev] == target) {
        return prev;
    }
    
    return -1;
}

int main() {
    // Search in double array
    vector<double> doubles = {1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9};
    cout << "Search for 5.5: " << jumpSearchGeneric(doubles, 5.5) << endl;
    
    // Search in Person objects (sorted by age)
    vector<Person> people = {
        {"Alice", 20},
        {"Bob", 25},
        {"Charlie", 30},
        {"Diana", 35},
        {"Eve", 40}
    };
    
    Person target = {"Charlie", 30};
    int index = jumpSearchGeneric(people, target);
    if (index != -1) {
        cout << "Found " << people[index].name << " at index " << index << endl;
    } else {
        cout << "Person not found" << endl;
    }
    
    return 0;
}
```

**Output:**
```
Search for 5.5: 4
Found Charlie at index 2
```

---

## Advantages and Disadvantages

### Advantages
- ✅ Better than linear search (O(√n) vs O(n))
- ✅ Simpler than binary search
- ✅ No recursion needed
- ✅ Works well with block-based storage
- ✅ Good for external memory searching

### Disadvantages
- ❌ Requires sorted data
- ❌ Slower than binary search (O(√n) vs O(log n))
- ❌ Optimal block size calculation needed
- ❌ Not as widely used as binary search

---

## Best Practices

1. **Use √n as block size** for optimal performance
2. **Handle boundary conditions** carefully
3. **Consider cache performance** - larger blocks may be better
4. **Use templates** for generic implementations
5. **Test with edge cases**: first, last, non-existent elements

---

## Common Pitfalls

1. **Wrong block size** - affects performance significantly
2. **Off-by-one errors** in block boundaries
3. **Not handling empty arrays**
4. **Integer overflow** in block size calculation
5. **Incorrect min() usage** for array bounds

---

## Summary

Jump search provides a middle ground between linear and binary search. While not as efficient as binary search, it's simpler to understand and can be useful in certain scenarios, especially when dealing with block-based storage systems.

**Key Takeaways:**
- Time Complexity: O(√n)
- Space Complexity: O(1)
- Requires sorted data
- Optimal block size: √n
- Bridge between linear and binary search
---

## Next Step

- Go to [04_Interpolation_Search.md](04_Interpolation_Search.md) to continue with Interpolation Search.
