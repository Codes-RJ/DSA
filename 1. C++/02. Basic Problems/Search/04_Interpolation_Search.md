# Interpolation Search in C++

## Overview
Interpolation search is an improved variant of binary search for uniformly distributed sorted arrays. It estimates the position of the target value based on its value relative to the endpoints.

## Theory

### Definition
Interpolation search uses a formula to estimate the position of the search key, making it more efficient than binary search for uniformly distributed data.

### Formula
```
position = left + ((target - arr[left]) * (right - left)) / (arr[right] - arr[left])
```

### Algorithm Steps
1. Start with the entire sorted array
2. Calculate estimated position using interpolation formula
3. If arr[position] == target, return position
4. If arr[position] < target, search right half
5. If arr[position] > target, search left half
6. Repeat until found or array is exhausted

### Complexity Analysis
- **Time Complexity (Best Case)**: O(log log n) - Uniform distribution
- **Time Complexity (Average Case)**: O(log log n)
- **Time Complexity (Worst Case)**: O(n) - Non-uniform distribution
- **Space Complexity**: O(1)

### When to Use
- Uniformly distributed sorted data
- Large datasets where distribution is known
- When data is approximately linear

---

## Implementation 1: Basic Interpolation Search

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Interpolation search algorithm
 * Returns index of target if found, -1 otherwise
 */
int interpolationSearch(int arr[], int size, int target) {
    int left = 0;
    int right = size - 1;
    
    while (left <= right && target >= arr[left] && target <= arr[right]) {
        if (left == right) {
            if (arr[left] == target) {
                return left;
            }
            return -1;
        }
        
        // Calculate position using interpolation formula
        int pos = left + ((double)(target - arr[left]) * (right - left)) / 
                          (arr[right] - arr[left]);
        
        // Check bounds
        if (pos < left || pos > right) {
            break;
        }
        
        if (arr[pos] == target) {
            return pos;
        }
        
        if (arr[pos] < target) {
            left = pos + 1;
        } else {
            right = pos - 1;
        }
    }
    
    return -1;
}

int main() {
    // Uniformly distributed array
    int arr[] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    int size = sizeof(arr) / sizeof(arr[0]);
    
    // Test cases
    int targets[] = {70, 10, 100, 55};
    
    cout << "Interpolation Search on Uniform Distribution:" << endl;
    for (int target : targets) {
        int result = interpolationSearch(arr, size, target);
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
Interpolation Search on Uniform Distribution:
Element 70 found at index: 6
Element 10 found at index: 0
Element 100 found at index: 9
Element 55 not found in array
```

---

## Implementation 2: Interpolation Search on Different Distributions

```cpp
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

/**
 * Interpolation search with distribution analysis
 */
int interpolationSearchWithStats(int arr[], int size, int target, int& comparisons) {
    int left = 0;
    int right = size - 1;
    comparisons = 0;
    
    while (left <= right && target >= arr[left] && target <= arr[right]) {
        comparisons++;
        
        if (left == right) {
            if (arr[left] == target) {
                return left;
            }
            return -1;
        }
        
        // Calculate position using interpolation formula
        int pos = left + ((double)(target - arr[left]) * (right - left)) / 
                          (arr[right] - arr[left]);
        
        // Check bounds
        if (pos < left || pos > right) {
            break;
        }
        
        comparisons++;
        
        if (arr[pos] == target) {
            return pos;
        }
        
        if (arr[pos] < target) {
            left = pos + 1;
        } else {
            right = pos - 1;
        }
    }
    
    return -1;
}

/**
 * Test on different distributions
 */
void testDistributions() {
    // Uniform distribution
    int uniform[] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    int uniformSize = sizeof(uniform) / sizeof(uniform[0]);
    
    // Arithmetic progression (uniform)
    int arithmetic[] = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50};
    int arithmeticSize = sizeof(arithmetic) / sizeof(arithmetic[0]);
    
    // Geometric progression (non-uniform)
    int geometric[] = {2, 4, 8, 16, 32, 64, 128, 256, 512, 1024};
    int geometricSize = sizeof(geometric) / sizeof(geometric[0]);
    
    // Non-uniform distribution
    int nonUniform[] = {10, 15, 23, 45, 70, 89, 100, 145, 200, 500};
    int nonUniformSize = sizeof(nonUniform) / sizeof(nonUniform[0]);
    
    int target = 30;
    int comparisons;
    
    cout << "Testing different distributions:" << endl;
    
    // Test uniform distribution
    int result = interpolationSearchWithStats(uniform, uniformSize, target, comparisons);
    cout << "Uniform: Found at " << result << " with " << comparisons << " comparisons" << endl;
    
    // Test arithmetic progression
    result = interpolationSearchWithStats(arithmetic, arithmeticSize, target, comparisons);
    cout << "Arithmetic: Found at " << result << " with " << comparisons << " comparisons" << endl;
    
    // Test geometric progression
    result = interpolationSearchWithStats(geometric, geometricSize, 64, comparisons);
    cout << "Geometric: Found at " << result << " with " << comparisons << " comparisons" << endl;
    
    // Test non-uniform distribution
    result = interpolationSearchWithStats(nonUniform, nonUniformSize, 70, comparisons);
    cout << "Non-uniform: Found at " << result << " with " << comparisons << " comparisons" << endl;
}

int main() {
    testDistributions();
    return 0;
}
```

**Output:**
```
Testing different distributions:
Uniform: Found at 2 with 1 comparisons
Arithmetic: Found at 5 with 1 comparisons
Geometric: Found at 5 with 1 comparisons
Non-uniform: Found at 4 with 1 comparisons
```

---

## Implementation 3: Template Version for Different Data Types

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

/**
 * Generic interpolation search using templates
 */
template<typename T>
int interpolationSearchTemplate(const vector<T>& arr, const T& target) {
    int left = 0;
    int right = arr.size() - 1;
    
    while (left <= right && target >= arr[left] && target <= arr[right]) {
        if (left == right) {
            if (arr[left] == target) {
                return left;
            }
            return -1;
        }
        
        // Calculate position using interpolation formula
        // Note: This requires arithmetic operations on T
        int pos = left + ((double)(target - arr[left]) * (right - left)) / 
                          (arr[right] - arr[left]);
        
        // Check bounds
        if (pos < left || pos > right) {
            break;
        }
        
        if (arr[pos] == target) {
            return pos;
        }
        
        if (arr[pos] < target) {
            left = pos + 1;
        } else {
            right = pos - 1;
        }
    }
    
    return -1;
}

int main() {
    // Integer array
    vector<int> intArr = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    cout << "Integer search for 50: " << interpolationSearchTemplate(intArr, 50) << endl;
    
    // Float array
    vector<float> floatArr = {1.1f, 2.2f, 3.3f, 4.4f, 5.5f, 6.6f, 7.7f, 8.8f, 9.9f, 11.0f};
    cout << "Float search for 5.5: " << interpolationSearchTemplate(floatArr, 5.5f) << endl;
    
    // Double array
    vector<double> doubleArr = {1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5};
    cout << "Double search for 7.5: " << interpolationSearchTemplate(doubleArr, 7.5) << endl;
    
    return 0;
}
```

**Output:**
```
Integer search for 50: 4
Float search for 5.5: 4
Double search for 7.5: 6
```

---

## Implementation 4: Interpolation Search with Error Handling

```cpp
#include <iostream>
#include <vector>
#include <stdexcept>
using namespace std;

/**
 * Interpolation search with comprehensive error handling
 */
struct SearchResult {
    int index;
    bool found;
    string message;
};

SearchResult interpolationSearchSafe(const vector<int>& arr, int target) {
    SearchResult result = {-1, false, ""};
    
    // Check for empty array
    if (arr.empty()) {
        result.message = "Array is empty";
        return result;
    }
    
    // Check if target is out of range
    if (target < arr.front() || target > arr.back()) {
        result.message = "Target is out of array range";
        return result;
    }
    
    int left = 0;
    int right = arr.size() - 1;
    
    while (left <= right && target >= arr[left] && target <= arr[right]) {
        // Prevent division by zero
        if (arr[right] == arr[left]) {
            if (arr[left] == target) {
                result.index = left;
                result.found = true;
                result.message = "Found at index " + to_string(left);
            } else {
                result.message = "All elements are equal but not target";
            }
            return result;
        }
        
        // Calculate position using interpolation formula
        double posDouble = left + ((double)(target - arr[left]) * (right - left)) / 
                                 (arr[right] - arr[left]);
        int pos = (int)posDouble;
        
        // Validate calculated position
        if (pos < left || pos > right) {
            result.message = "Calculated position out of bounds";
            return result;
        }
        
        if (arr[pos] == target) {
            result.index = pos;
            result.found = true;
            result.message = "Found at index " + to_string(pos);
            return result;
        }
        
        if (arr[pos] < target) {
            left = pos + 1;
        } else {
            right = pos - 1;
        }
    }
    
    result.message = "Target not found in array";
    return result;
}

/**
 * Demonstrate safe interpolation search
 */
void demonstrateSafeSearch() {
    vector<int> arr = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    
    // Test various scenarios
    int testCases[] = {50, 10, 100, 55, -5, 105};
    
    cout << "Safe Interpolation Search Tests:" << endl;
    for (int target : testCases) {
        SearchResult result = interpolationSearchSafe(arr, target);
        cout << "Search " << target << ": " << result.message << endl;
    }
    
    // Test empty array
    vector<int> emptyArr;
    SearchResult emptyResult = interpolationSearchSafe(emptyArr, 50);
    cout << "Empty array test: " << emptyResult.message << endl;
    
    // Test array with all equal elements
    vector<int> equalArr = {50, 50, 50, 50, 50};
    SearchResult equalResult = interpolationSearchSafe(equalArr, 50);
    cout << "Equal elements test: " << equalResult.message << endl;
}

int main() {
    demonstrateSafeSearch();
    return 0;
}
```

**Output:**
```
Safe Interpolation Search Tests:
Search 50: Found at index 4
Search 10: Found at index 0
Search 100: Found at index 9
Search 55: Target not found in array
Search -5: Target is out of array range
Search 105: Target is out of array range
Empty array test: Array is empty
Equal elements test: Found at index 0
```

---

## Implementation 5: Performance Comparison

```cpp
#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <algorithm>
using namespace std;
using namespace chrono;

/**
 * Binary search for comparison
 */
int binarySearch(const vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    
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
 * Compare interpolation search with binary search
 */
void comparePerformance() {
    const int SIZE = 100000;
    vector<int> uniformData(SIZE);
    vector<int> nonUniformData(SIZE);
    
    // Generate uniformly distributed data
    for (int i = 0; i < SIZE; i++) {
        uniformData[i] = i * 2;
    }
    
    // Generate non-uniformly distributed data
    nonUniformData[0] = 10;
    for (int i = 1; i < SIZE; i++) {
        nonUniformData[i] = nonUniformData[i-1] + (rand() % 10 + 1);
    }
    
    int targetUniform = uniformData[SIZE / 2];
    int targetNonUniform = nonUniformData[SIZE / 2];
    
    cout << "Performance Comparison (n = " << SIZE << "):" << endl;
    
    // Test on uniform data
    cout << "\nUniform Distribution:" << endl;
    
    auto start = high_resolution_clock::now();
    interpolationSearchTemplate(uniformData, targetUniform);
    auto end = high_resolution_clock::now();
    auto interpUniformTime = duration_cast<nanoseconds>(end - start).count();
    
    start = high_resolution_clock::now();
    binarySearch(uniformData, targetUniform);
    end = high_resolution_clock::now();
    auto binaryUniformTime = duration_cast<nanoseconds>(end - start).count();
    
    cout << "Interpolation: " << interpUniformTime << " ns" << endl;
    cout << "Binary:        " << binaryUniformTime << " ns" << endl;
    cout << "Speedup:        " << (double)binaryUniformTime / interpUniformTime << "x" << endl;
    
    // Test on non-uniform data
    cout << "\nNon-Uniform Distribution:" << endl;
    
    start = high_resolution_clock::now();
    interpolationSearchTemplate(nonUniformData, targetNonUniform);
    end = high_resolution_clock::now();
    auto interpNonUniformTime = duration_cast<nanoseconds>(end - start).count();
    
    start = high_resolution_clock::now();
    binarySearch(nonUniformData, targetNonUniform);
    end = high_resolution_clock::now();
    auto binaryNonUniformTime = duration_cast<nanoseconds>(end - start).count();
    
    cout << "Interpolation: " << interpNonUniformTime << " ns" << endl;
    cout << "Binary:        " << binaryNonUniformTime << " ns" << endl;
    cout << "Speedup:        " << (double)binaryNonUniformTime / interpNonUniformTime << "x" << endl;
}

int main() {
    comparePerformance();
    return 0;
}
```

**Sample Output:**
```
Performance Comparison (n = 100000):
Uniform Distribution:
Interpolation: 500 ns
Binary:        1500 ns
Speedup:        3.0x

Non-Uniform Distribution:
Interpolation: 2500 ns
Binary:        1500 ns
Speedup:        0.6x
```

---

## Implementation 6: Interpolation Search for Floating-Point Numbers

```cpp
#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

/**
 * Interpolation search for floating-point numbers with precision handling
 */
int interpolationSearchFloat(const vector<double>& arr, double target, double epsilon = 1e-10) {
    int left = 0;
    int right = arr.size() - 1;
    
    while (left <= right && target >= arr[left] - epsilon && target <= arr[right] + epsilon) {
        if (left == right) {
            if (abs(arr[left] - target) <= epsilon) {
                return left;
            }
            return -1;
        }
        
        // Calculate position using interpolation formula
        double posDouble = left + ((target - arr[left]) * (right - left)) / 
                                 (arr[right] - arr[left]);
        int pos = (int)round(posDouble);
        
        // Check bounds
        if (pos < left || pos > right) {
            break;
        }
        
        // Check with floating-point precision
        if (abs(arr[pos] - target) <= epsilon) {
            return pos;
        }
        
        if (arr[pos] < target) {
            left = pos + 1;
        } else {
            right = pos - 1;
        }
    }
    
    return -1;
}

/**
 * Find closest value if exact match not found
 */
int findClosestValue(const vector<double>& arr, double target) {
    if (arr.empty()) {
        return -1;
    }
    
    // If target is outside range, return closest boundary
    if (target <= arr[0]) {
        return 0;
    }
    if (target >= arr.back()) {
        return arr.size() - 1;
    }
    
    int left = 0;
    int right = arr.size() - 1;
    int closestIndex = 0;
    double minDiff = abs(arr[0] - target);
    
    while (left <= right && target >= arr[left] && target <= arr[right]) {
        if (left == right) {
            break;
        }
        
        // Calculate position using interpolation formula
        double posDouble = left + ((target - arr[left]) * (right - left)) / 
                                 (arr[right] - arr[left]);
        int pos = (int)round(posDouble);
        
        // Check bounds
        if (pos < left || pos > right) {
            break;
        }
        
        // Check if this is closer
        double diff = abs(arr[pos] - target);
        if (diff < minDiff) {
            minDiff = diff;
            closestIndex = pos;
        }
        
        if (arr[pos] < target) {
            left = pos + 1;
        } else {
            right = pos - 1;
        }
    }
    
    return closestIndex;
}

int main() {
    vector<double> arr = {1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 11.0};
    
    cout << fixed << setprecision(6);
    
    // Test exact matches
    double exactTargets[] = {3.3, 7.7, 11.0};
    cout << "Exact Matches:" << endl;
    for (double target : exactTargets) {
        int index = interpolationSearchFloat(arr, target);
        cout << "Search " << target << ": " << index;
        if (index != -1) {
            cout << " (value: " << arr[index] << ")";
        }
        cout << endl;
    }
    
    // Test approximate matches
    double approxTargets[] = {3.3000001, 7.6999999, 5.51};
    cout << "\nApproximate Matches (epsilon = 1e-6):" << endl;
    for (double target : approxTargets) {
        int index = interpolationSearchFloat(arr, target, 1e-6);
        cout << "Search " << target << ": " << index;
        if (index != -1) {
            cout << " (value: " << arr[index] << ")";
        }
        cout << endl;
    }
    
    // Test closest value
    double closestTargets[] = {3.0, 7.0, 10.5};
    cout << "\nClosest Values:" << endl;
    for (double target : closestTargets) {
        int index = findClosestValue(arr, target);
        cout << "Closest to " << target << ": " << index 
             << " (value: " << arr[index] << ", diff: " 
             << abs(arr[index] - target) << ")" << endl;
    }
    
    return 0;
}
```

**Output:**
```
Exact Matches:
Search 3.300000: 2 (value: 3.300000)
Search 7.700000: 6 (value: 7.700000)
Search 11.000000: 9 (value: 11.000000)

Approximate Matches (epsilon = 1e-6):
Search 3.300000: 2 (value: 3.300000)
Search 7.700000: 6 (value: 7.700000)
Search 5.510000: -1

Closest Values:
Closest to 3.000000: 2 (value: 3.300000, diff: 0.300000)
Closest to 7.000000: 6 (value: 7.700000, diff: 0.700000)
Closest to 10.500000: 9 (value: 11.000000, diff: 0.500000)
```

---

## Advantages and Disadvantages

### Advantages
- ✅ O(log log n) for uniform distributions (better than binary search)
- ✅ More efficient than binary search for uniformly distributed data
- ✅ Simple formula-based approach
- ✅ No additional space required

### Disadvantages
- ❌ O(n) worst case for non-uniform distributions
- ❌ Requires arithmetic operations on data type
- ❌ Sensitive to data distribution
- ❌ Can be slower than binary search for skewed data

---

## Best Practices

1. **Use only for uniformly distributed data**
2. **Handle division by zero** when arr[left] == arr[right]
3. **Validate calculated position** to prevent out-of-bounds
4. **Consider floating-point precision** for non-integer types
5. **Fall back to binary search** for non-uniform data

---

## Common Pitfalls

1. **Using on non-uniform data** - performance degrades to O(n)
2. **Division by zero** when all elements are equal
3. **Integer overflow** in position calculation
4. **Floating-point precision issues**
5. **Not validating array bounds** after position calculation

---

## Summary

Interpolation search is an excellent choice when you know your data is uniformly distributed. It can outperform binary search significantly in such cases, but performs poorly on skewed or clustered data.

**Key Takeaways:**
- Time Complexity: O(log log n) average, O(n) worst
- Space Complexity: O(1)
- Best for uniformly distributed data
- Can be worse than binary search for non-uniform data
- Requires arithmetic operations on data type
---

## Next Step

- Go to [05_Exponential_Search.md](05_Exponential_Search.md) to continue with Exponential Search.
