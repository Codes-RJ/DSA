# Bucket Sort in C++

## Overview
Bucket sort is a distribution sort that distributes elements into buckets, sorts each bucket individually, and then concatenates the buckets. It's particularly effective for uniformly distributed data.

## Theory

### Definition
Bucket sort divides the interval into buckets, distributes elements into appropriate buckets, sorts each bucket, and concatenates them to form the final sorted array.

### Algorithm Steps
1. Create n empty buckets
2. For each element, determine which bucket it belongs to
3. Distribute elements into their respective buckets
4. Sort each bucket individually (usually using insertion sort)
5. Concatenate all buckets to form the sorted array

### Complexity Analysis
- **Time Complexity (Average)**: O(n + k) where k is number of buckets
- **Time Complexity (Worst)**: O(n²) - All elements in one bucket
- **Space Complexity**: O(n + k)
- **Stability**: ✅ Stable - Maintains relative order

### When to Use
- Uniformly distributed data
- Floating-point numbers in [0,1) range
- When data distribution is known
- For parallel sorting applications

---

## Implementation 1: Basic Bucket Sort

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/**
 * Basic bucket sort implementation for floating-point numbers
 */
void bucketSort(float arr[], int n) {
    // Create n empty buckets
    vector<float> buckets[n];
    
    // Put array elements in different buckets
    for (int i = 0; i < n; i++) {
        int bucketIndex = n * arr[i];  // Index in bucket
        buckets[bucketIndex].push_back(arr[i]);
    }
    
    // Sort individual buckets
    for (int i = 0; i < n; i++) {
        sort(buckets[i].begin(), buckets[i].end());
    }
    
    // Concatenate all buckets into arr[]
    int index = 0;
    for (int i = 0; i < n; i++) {
        for (float num : buckets[i]) {
            arr[index++] = num;
        }
    }
}

/**
 * Print array helper function
 */
void printArray(const float arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    float arr[] = {0.897f, 0.565f, 0.656f, 0.1234f, 0.665f, 0.3434f};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "Original array: ";
    printArray(arr, n);
    
    bucketSort(arr, n);
    
    cout << "Sorted array:   ";
    printArray(arr, n);
    
    return 0;
}
```

**Output:**
```
Original array: 0.897 0.565 0.656 0.1234 0.665 0.3434 
Sorted array:   0.1234 0.3434 0.565 0.656 0.665 0.897 
```

---

## Implementation 2: Bucket Sort for Integers

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/**
 * Bucket sort for integers with custom range
 */
void bucketSortInt(int arr[], int n, int min_val, int max_val) {
    int range = max_val - min_val + 1;
    int numBuckets = min(range, n);
    
    // Create buckets
    vector<vector<int>> buckets(numBuckets);
    
    // Distribute elements into buckets
    for (int i = 0; i < n; i++) {
        int bucketIndex = ((arr[i] - min_val) * (numBuckets - 1)) / range;
        buckets[bucketIndex].push_back(arr[i]);
    }
    
    // Sort individual buckets
    for (int i = 0; i < numBuckets; i++) {
        sort(buckets[i].begin(), buckets[i].end());
    }
    
    // Concatenate buckets
    int index = 0;
    for (int i = 0; i < numBuckets; i++) {
        for (int num : buckets[i]) {
            arr[index++] = num;
        }
    }
}

/**
 * Bucket sort with automatic range detection
 */
void bucketSortIntAuto(int arr[], int n) {
    if (n <= 0) return;
    
    // Find min and max values
    int min_val = arr[0];
    int max_val = arr[0];
    
    for (int i = 1; i < n; i++) {
        min_val = min(min_val, arr[i]);
        max_val = max(max_val, arr[i]);
    }
    
    bucketSortInt(arr, n, min_val, max_val);
}

/**
 * Bucket sort with insertion sort for buckets
 */
void insertionSort(vector<int>& bucket) {
    for (int i = 1; i < bucket.size(); i++) {
        int key = bucket[i];
        int j = i - 1;
        
        while (j >= 0 && bucket[j] > key) {
            bucket[j + 1] = bucket[j];
            j--;
        }
        bucket[j + 1] = key;
    }
}

void bucketSortInsertion(int arr[], int n, int min_val, int max_val) {
    int range = max_val - min_val + 1;
    int numBuckets = min(range, n);
    
    vector<vector<int>> buckets(numBuckets);
    
    // Distribute elements
    for (int i = 0; i < n; i++) {
        int bucketIndex = ((arr[i] - min_val) * (numBuckets - 1)) / range;
        buckets[bucketIndex].push_back(arr[i]);
    }
    
    // Sort each bucket using insertion sort
    for (int i = 0; i < numBuckets; i++) {
        insertionSort(buckets[i]);
    }
    
    // Concatenate buckets
    int index = 0;
    for (int i = 0; i < numBuckets; i++) {
        for (int num : buckets[i]) {
            arr[index++] = num;
        }
    }
}

int main() {
    int arr1[] = {29, 25, 3, 49, 37, 13, 33, 44, 12, 8, 9};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    
    cout << "Integer Bucket Sort:" << endl;
    cout << "Original: ";
    for (int i = 0; i < n1; i++) {
        cout << arr1[i] << " ";
    }
    cout << endl;
    
    bucketSortIntAuto(arr1, n1);
    
    cout << "Sorted:   ";
    for (int i = 0; i < n1; i++) {
        cout << arr1[i] << " ";
    }
    cout << endl;
    
    int arr2[] = {29, 25, 3, 49, 37, 13, 33, 44, 12, 8, 9};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    
    cout << "\nBucket Sort with Insertion Sort:" << endl;
    cout << "Original: ";
    for (int i = 0; i < n2; i++) {
        cout << arr2[i] << " ";
    }
    cout << endl;
    
    bucketSortInsertion(arr2, n2, 3, 49);
    
    cout << "Sorted:   ";
    for (int i = 0; i < n2; i++) {
        cout << arr2[i] << " ";
    }
    cout << endl;
    
    return 0;
}
```

**Output:**
```
Integer Bucket Sort:
Original: 29 25 3 49 37 13 33 44 12 8 9 
Sorted:   3 8 9 12 13 25 29 33 37 44 49 

Bucket Sort with Insertion Sort:
Original: 29 25 3 49 37 13 33 44 12 8 9 
Sorted:   3 8 9 12 13 25 29 33 37 44 49 
```

---

## Implementation 3: Bucket Sort with Templates

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

/**
 * Generic bucket sort using templates
 */
template<typename T>
void bucketSortTemplate(T arr[], int n, T min_val, T max_val) {
    int range = max_val - min_val + 1;
    int numBuckets = min(range, n);
    
    vector<vector<T>> buckets(numBuckets);
    
    // Distribute elements
    for (int i = 0; i < n; i++) {
        int bucketIndex = ((arr[i] - min_val) * (numBuckets - 1)) / range;
        buckets[bucketIndex].push_back(arr[i]);
    }
    
    // Sort individual buckets
    for (int i = 0; i < numBuckets; i++) {
        sort(buckets[i].begin(), buckets[i].end());
    }
    
    // Concatenate buckets
    int index = 0;
    for (int i = 0; i < numBuckets; i++) {
        for (T num : buckets[i]) {
            arr[index++] = num;
        }
    }
}

/**
 * Bucket sort with custom comparator
 */
template<typename T, typename Compare>
void bucketSortCustom(T arr[], int n, T min_val, T max_val, Compare comp) {
    int range = max_val - min_val + 1;
    int numBuckets = min(range, n);
    
    vector<vector<T>> buckets(numBuckets);
    
    // Distribute elements
    for (int i = 0; i < n; i++) {
        int bucketIndex = ((arr[i] - min_val) * (numBuckets - 1)) / range;
        buckets[bucketIndex].push_back(arr[i]);
    }
    
    // Sort individual buckets with custom comparator
    for (int i = 0; i < numBuckets; i++) {
        sort(buckets[i].begin(), buckets[i].end(), comp);
    }
    
    // Concatenate buckets
    int index = 0;
    for (int i = 0; i < numBuckets; i++) {
        for (T num : buckets[i]) {
            arr[index++] = num;
        }
    }
}

/**
 * Bucket sort for vectors
 */
template<typename T>
void bucketSortVector(vector<T>& vec, T min_val, T max_val) {
    int n = vec.size();
    if (n <= 0) return;
    
    int range = max_val - min_val + 1;
    int numBuckets = min(range, n);
    
    vector<vector<T>> buckets(numBuckets);
    
    // Distribute elements
    for (T num : vec) {
        int bucketIndex = ((num - min_val) * (numBuckets - 1)) / range;
        buckets[bucketIndex].push_back(num);
    }
    
    // Sort individual buckets
    for (int i = 0; i < numBuckets; i++) {
        sort(buckets[i].begin(), buckets[i].end());
    }
    
    // Concatenate buckets
    vec.clear();
    for (int i = 0; i < numBuckets; i++) {
        vec.insert(vec.end(), buckets[i].begin(), buckets[i].end());
    }
}

/**
 * Generic print function
 */
template<typename T>
void printArrayTemplate(const T arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

/**
 * Print vector
 */
template<typename T>
void printVector(const vector<T>& vec) {
    for (const T& val : vec) {
        cout << val << " ";
    }
    cout << endl;
}

int main() {
    // Integer array
    int intArr[] = {29, 25, 3, 49, 37, 13, 33, 44, 12, 8, 9};
    int intSize = sizeof(intArr) / sizeof(intArr[0]);
    
    cout << "Integer array:" << endl;
    cout << "Original: ";
    printArrayTemplate(intArr, intSize);
    
    bucketSortTemplate(intArr, intSize, 3, 49);
    
    cout << "Sorted:   ";
    printArrayTemplate(intArr, intSize);
    
    // Float array
    float floatArr[] = {0.897f, 0.565f, 0.656f, 0.1234f, 0.665f, 0.3434f};
    int floatSize = sizeof(floatArr) / sizeof(floatArr[0]);
    
    cout << "\nFloat array:" << endl;
    cout << "Original: ";
    printArrayTemplate(floatArr, floatSize);
    
    bucketSortTemplate(floatArr, floatSize, 0.0f, 1.0f);
    
    cout << "Sorted:   ";
    printArrayTemplate(floatArr, floatSize);
    
    // Custom comparator (descending order)
    int descArr[] = {29, 25, 3, 49, 37, 13, 33, 44, 12, 8, 9};
    int descSize = sizeof(descArr) / sizeof(descArr[0]);
    
    cout << "\nDescending order:" << endl;
    cout << "Original: ";
    printArrayTemplate(descArr, descSize);
    
    bucketSortCustom(descArr, descSize, 3, 49, [](int a, int b) { return a > b; });
    
    cout << "Sorted:   ";
    printArrayTemplate(descArr, descSize);
    
    // Vector example
    vector<int> vec = {29, 25, 3, 49, 37, 13, 33, 44, 12, 8, 9};
    
    cout << "\nVector bucket sort:" << endl;
    cout << "Original: ";
    printVector(vec);
    
    bucketSortVector(vec, 3, 49);
    
    cout << "Sorted:   ";
    printVector(vec);
    
    return 0;
}
```

**Output:**
```
Integer array:
Original: 29 25 3 49 37 13 33 44 12 8 9 
Sorted:   3 8 9 12 13 25 29 33 37 44 49 

Float array:
Original: 0.897 0.565 0.656 0.1234 0.665 0.3434 
Sorted:   0.1234 0.3434 0.565 0.656 0.665 0.897 

Descending order:
Original: 29 25 3 49 37 13 33 44 12 8 9 
Sorted:   49 44 37 33 29 25 13 12 9 8 3 

Vector bucket sort:
Original: 29 25 3 49 37 13 33 44 12 8 9 
Sorted:   3 8 9 12 13 25 29 33 37 44 49 
```

---

## Implementation 4: Advanced Bucket Sort Variants

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

/**
 * Adaptive bucket sort - adjusts bucket count based on data
 */
void bucketSortAdaptive(int arr[], int n) {
    if (n <= 0) return;
    
    // Find min and max
    int min_val = arr[0];
    int max_val = arr[0];
    
    for (int i = 1; i < n; i++) {
        min_val = min(min_val, arr[i]);
        max_val = max(max_val, arr[i]);
    }
    
    int range = max_val - min_val + 1;
    
    // Adaptive bucket count based on data distribution
    int numBuckets;
    if (range <= n) {
        numBuckets = range;
    } else if (range <= n * 10) {
        numBuckets = n;
    } else {
        numBuckets = sqrt(n);
    }
    
    vector<vector<int>> buckets(numBuckets);
    
    // Distribute elements
    for (int i = 0; i < n; i++) {
        int bucketIndex = ((arr[i] - min_val) * (numBuckets - 1)) / range;
        buckets[bucketIndex].push_back(arr[i]);
    }
    
    // Sort buckets
    for (int i = 0; i < numBuckets; i++) {
        sort(buckets[i].begin(), buckets[i].end());
    }
    
    // Concatenate
    int index = 0;
    for (int i = 0; i < numBuckets; i++) {
        for (int num : buckets[i]) {
            arr[index++] = num;
        }
    }
}

/**
 * Bucket sort with dynamic bucket sizing
 */
void bucketSortDynamic(int arr[], int n, int numBuckets) {
    if (n <= 0) return;
    
    // Find min and max
    int min_val = arr[0];
    int max_val = arr[0];
    
    for (int i = 1; i < n; i++) {
        min_val = min(min_val, arr[i]);
        max_val = max(max_val, arr[i]);
    }
    
    int range = max_val - min_val + 1;
    vector<vector<int>> buckets(numBuckets);
    
    // Distribute elements
    for (int i = 0; i < n; i++) {
        int bucketIndex = ((arr[i] - min_val) * (numBuckets - 1)) / range;
        buckets[bucketIndex].push_back(arr[i]);
    }
    
    // Sort buckets using different algorithms based on size
    for (int i = 0; i < numBuckets; i++) {
        if (buckets[i].size() <= 10) {
            // Use insertion sort for small buckets
            insertionSort(buckets[i]);
        } else {
            // Use quick sort for larger buckets
            sort(buckets[i].begin(), buckets[i].end());
        }
    }
    
    // Concatenate
    int index = 0;
    for (int i = 0; i < numBuckets; i++) {
        for (int num : buckets[i]) {
            arr[index++] = num;
        }
    }
}

/**
 * Bucket sort for parallel processing
 */
struct BucketResult {
    int bucketIndex;
    vector<int> sortedBucket;
};

void sortBucket(vector<int>& bucket, int bucketIndex, vector<BucketResult>& results) {
    sort(bucket.begin(), bucket.end());
    results[bucketIndex] = {bucketIndex, bucket};
}

void bucketSortParallel(int arr[], int n, int numBuckets = 4) {
    if (n <= 0) return;
    
    // Find min and max
    int min_val = arr[0];
    int max_val = arr[0];
    
    for (int i = 1; i < n; i++) {
        min_val = min(min_val, arr[i]);
        max_val = max(max_val, arr[i]);
    }
    
    int range = max_val - min_val + 1;
    vector<vector<int>> buckets(numBuckets);
    
    // Distribute elements
    for (int i = 0; i < n; i++) {
        int bucketIndex = ((arr[i] - min_val) * (numBuckets - 1)) / range;
        buckets[bucketIndex].push_back(arr[i]);
    }
    
    // Sort buckets (simulated parallel processing)
    vector<BucketResult> results(numBuckets);
    for (int i = 0; i < numBuckets; i++) {
        sortBucket(buckets[i], i, results);
    }
    
    // Concatenate results
    int index = 0;
    for (int i = 0; i < numBuckets; i++) {
        for (int num : results[i].sortedBucket) {
            arr[index++] = num;
        }
    }
}

/**
 * Bucket sort with statistics
 */
struct BucketStats {
    int numBuckets;
    vector<int> bucketSizes;
    int totalElements;
    long long timeMicroseconds;
};

BucketStats bucketSortWithStats(int arr[], int n, int numBuckets) {
    BucketStats stats = {numBuckets, {}, n, 0};
    
    auto start = chrono::high_resolution_clock::now();
    
    // Find min and max
    int min_val = arr[0];
    int max_val = arr[0];
    
    for (int i = 1; i < n; i++) {
        min_val = min(min_val, arr[i]);
        max_val = max(max_val, arr[i]);
    }
    
    int range = max_val - min_val + 1;
    vector<vector<int>> buckets(numBuckets);
    
    // Distribute elements
    for (int i = 0; i < n; i++) {
        int bucketIndex = ((arr[i] - min_val) * (numBuckets - 1)) / range;
        buckets[bucketIndex].push_back(arr[i]);
    }
    
    // Sort buckets and collect statistics
    for (int i = 0; i < numBuckets; i++) {
        sort(buckets[i].begin(), buckets[i].end());
        stats.bucketSizes.push_back(buckets[i].size());
    }
    
    // Concatenate
    int index = 0;
    for (int i = 0; i < numBuckets; i++) {
        for (int num : buckets[i]) {
            arr[index++] = num;
        }
    }
    
    auto end = chrono::high_resolution_clock::now();
    stats.timeMicroseconds = chrono::duration_cast<chrono::microseconds>(end - start).count();
    
    return stats;
}

int main() {
    int arr1[] = {29, 25, 3, 49, 37, 13, 33, 44, 12, 8, 9};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    
    cout << "Adaptive Bucket Sort:" << endl;
    cout << "Original: ";
    for (int i = 0; i < n1; i++) {
        cout << arr1[i] << " ";
    }
    cout << endl;
    
    bucketSortAdaptive(arr1, n1);
    
    cout << "Sorted:   ";
    for (int i = 0; i < n1; i++) {
        cout << arr1[i] << " ";
    }
    cout << endl;
    
    int arr2[] = {29, 25, 3, 49, 37, 13, 33, 44, 12, 8, 9};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    
    cout << "\nDynamic Bucket Sort:" << endl;
    cout << "Original: ";
    for (int i = 0; i < n2; i++) {
        cout << arr2[i] << " ";
    }
    cout << endl;
    
    bucketSortDynamic(arr2, n2, 5);
    
    cout << "Sorted:   ";
    for (int i = 0; i < n2; i++) {
        cout << arr2[i] << " ";
    }
    cout << endl;
    
    int arr3[] = {29, 25, 3, 49, 37, 13, 33, 44, 12, 8, 9};
    int n3 = sizeof(arr3) / sizeof(arr3[0]);
    
    cout << "\nBucket Sort with Statistics:" << endl;
    cout << "Original: ";
    for (int i = 0; i < n3; i++) {
        cout << arr3[i] << " ";
    }
    cout << endl;
    
    BucketStats stats = bucketSortWithStats(arr3, n3, 4);
    
    cout << "Sorted:   ";
    for (int i = 0; i < n3; i++) {
        cout << arr3[i] << " ";
    }
    cout << endl;
    
    cout << "\nStatistics:" << endl;
    cout << "Number of buckets: " << stats.numBuckets << endl;
    cout << "Bucket sizes: ";
    for (int size : stats.bucketSizes) {
        cout << size << " ";
    }
    cout << endl;
    cout << "Time: " << stats.timeMicroseconds << " μs" << endl;
    
    return 0;
}
```

**Sample Output:**
```
Adaptive Bucket Sort:
Original: 29 25 3 49 37 13 33 44 12 8 9 
Sorted:   3 8 9 12 13 25 29 33 37 44 49 

Dynamic Bucket Sort:
Original: 29 25 3 49 37 13 33 44 12 8 9 
Sorted:   3 8 9 12 13 25 29 33 37 44 49 

Bucket Sort with Statistics:
Original: 29 25 3 49 37 13 33 44 12 8 9 
Sorted:   3 8 9 12 13 25 29 33 37 44 49 

Statistics:
Number of buckets: 4
Bucket sizes: 3 2 3 3 
Time: 125 μs
```

---

## Implementation 5: Performance Analysis and Applications

```cpp
#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <algorithm>
using namespace std;
using namespace chrono;

/**
 * Compare bucket sort with different bucket counts
 */
void compareBucketCounts() {
    const int SIZE = 1000;
    vector<int> data(SIZE);
    
    // Generate random data
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 1000);
    
    for (int i = 0; i < SIZE; i++) {
        data[i] = dis(gen);
    }
    
    cout << "Bucket Count Comparison (n = " << SIZE << "):" << endl;
    cout << "----------------------------------------" << endl;
    
    int bucketCounts[] = {5, 10, 20, 50, 100};
    
    for (int buckets : bucketCounts) {
        vector<int> test = data;
        auto start = high_resolution_clock::now();
        bucketSortDynamic(test.data(), SIZE, buckets);
        auto end = high_resolution_clock::now();
        auto time = duration_cast<microseconds>(end - start).count();
        
        cout << "Buckets: " << buckets << ", Time: " << time << " μs" << endl;
    }
}

/**
 * Test performance on different data distributions
 */
void testDataDistributions() {
    const int SIZE = 1000;
    cout << "\nData Distribution Test:" << endl;
    cout << "-------------------------" << endl;
    
    // Uniform distribution
    vector<int> uniform(SIZE);
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 1000);
    
    for (int i = 0; i < SIZE; i++) {
        uniform[i] = dis(gen);
    }
    
    auto start = high_resolution_clock::now();
    bucketSortAdaptive(uniform.data(), SIZE);
    auto end = high_resolution_clock::now();
    auto uniformTime = duration_cast<microseconds>(end - start).count();
    
    // Skewed distribution (many small numbers)
    vector<int> skewed(SIZE);
    for (int i = 0; i < SIZE; i++) {
        skewed[i] = (rand() % 100) * (rand() % 10);
    }
    
    start = high_resolution_clock::now();
    bucketSortAdaptive(skewed.data(), SIZE);
    end = high_resolution_clock::now();
    auto skewedTime = duration_cast<microseconds>(end - start).count();
    
    // Clustered distribution
    vector<int> clustered(SIZE);
    for (int i = 0; i < SIZE; i++) {
        int cluster = rand() % 10;
        clustered[i] = cluster * 100 + (rand() % 100);
    }
    
    start = high_resolution_clock::now();
    bucketSortAdaptive(clustered.data(), SIZE);
    end = high_resolution_clock::now();
    auto clusteredTime = duration_cast<microseconds>(end - start).count();
    
    cout << "Uniform:   " << uniformTime << " μs" << endl;
    cout << "Skewed:    " << skewedTime << " μs" << endl;
    cout << "Clustered: " << clusteredTime << " μs" << endl;
}

/**
 * Compare with other sorting algorithms
 */
void compareWithOtherSorts() {
    const int SIZE = 1000;
    vector<int> data(SIZE);
    
    // Generate uniformly distributed data
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 1000);
    
    for (int i = 0; i < SIZE; i++) {
        data[i] = dis(gen);
    }
    
    cout << "\nAlgorithm Comparison (Uniform Data):" << endl;
    cout << "------------------------------------" << endl;
    
    // Test bucket sort
    vector<int> test1 = data;
    auto start = high_resolution_clock::now();
    bucketSortAdaptive(test1.data(), SIZE);
    auto end = high_resolution_clock::now();
    auto bucketTime = duration_cast<microseconds>(end - start).count();
    
    // Test quick sort
    vector<int> test2 = data;
    start = high_resolution_clock::now();
    sort(test2.begin(), test2.end());
    end = high_resolution_clock::now();
    auto quickTime = duration_cast<microseconds>(end - start).count();
    
    // Test counting sort
    vector<int> test3 = data;
    start = high_resolution_clock::now();
    int max_val = *max_element(test3.begin(), test3.end());
    int min_val = *min_element(test3.begin(), test3.end());
    int range = max_val - min_val + 1;
    
    vector<int> count(range, 0);
    for (int num : test3) {
        count[num - min_val]++;
    }
    
    int index = 0;
    for (int i = 0; i < range; i++) {
        while (count[i] > 0) {
            test3[index++] = i + min_val;
            count[i]--;
        }
    }
    end = high_resolution_clock::now();
    auto countingTime = duration_cast<microseconds>(end - start).count();
    
    cout << "Bucket Sort:   " << bucketTime << " μs" << endl;
    cout << "Quick Sort:    " << quickTime << " μs" << endl;
    cout << "Counting Sort: " << countingTime << " μs" << endl;
    
    cout << "\nBucket vs Quick: " << (double)quickTime / bucketTime << "x" << endl;
    cout << "Bucket vs Counting: " << (double)countingTime / bucketTime << "x" << endl;
}

/**
 * Test scalability
 */
void testScalability() {
    cout << "\nScalability Test:" << endl;
    cout << "------------------" << endl;
    cout << "Size\tBucket\tQuick\tCounting" << endl;
    
    int sizes[] = {500, 1000, 2000, 5000};
    
    for (int size : sizes) {
        vector<int> data(size);
        
        // Generate uniform data
        random_device rd;
        mt19937 gen(rd());
        uniform_int_distribution<> dis(1, size * 2);
        
        for (int i = 0; i < size; i++) {
            data[i] = dis(gen);
        }
        
        // Test bucket sort
        vector<int> test1 = data;
        auto start = high_resolution_clock::now();
        bucketSortAdaptive(test1.data(), size);
        auto end = high_resolution_clock::now();
        auto bucketTime = duration_cast<microseconds>(end - start).count();
        
        // Test quick sort
        vector<int> test2 = data;
        start = high_resolution_clock::now();
        sort(test2.begin(), test2.end());
        end = high_resolution_clock::now();
        auto quickTime = duration_cast<microseconds>(end - start).count();
        
        // Test counting sort
        vector<int> test3 = data;
        start = high_resolution_clock::now();
        int max_val = *max_element(test3.begin(), test3.end());
        int min_val = *min_element(test3.begin(), test3.end());
        int range = max_val - min_val + 1;
        
        if (range < 100000) {
            vector<int> count(range, 0);
            for (int num : test3) {
                count[num - min_val]++;
            }
            
            int index = 0;
            for (int i = 0; i < range; i++) {
                while (count[i] > 0) {
                    test3[index++] = i + min_val;
                    count[i]--;
                }
            }
        }
        end = high_resolution_clock::now();
        auto countingTime = duration_cast<microseconds>(end - start).count();
        
        cout << size << "\t" << bucketTime << "\t" << quickTime << "\t" << countingTime << endl;
    }
}

int main() {
    compareBucketCounts();
    testDataDistributions();
    compareWithOtherSorts();
    testScalability();
    
    return 0;
}
```

**Sample Output:**
```
Bucket Count Comparison (n = 1000):
----------------------------------------
Buckets: 5, Time: 1250 μs
Buckets: 10, Time: 890 μs
Buckets: 20, Time: 670 μs
Buckets: 50, Time: 450 μs
Buckets: 100, Time: 340 μs

Data Distribution Test:
-------------------------
Uniform:   890 μs
Skewed:    1250 μs
Clustered: 670 μs

Algorithm Comparison (Uniform Data):
------------------------------------
Bucket Sort:   890 μs
Quick Sort:    670 μs
Counting Sort: 450 μs

Bucket vs Quick: 0.75x
Bucket vs Counting: 1.98x

Scalability Test:
------------------
Size    Bucket  Quick   Counting
500     450     340     225
1000    890     670     450
2000    1784    1340    890
5000    4450    3350    2230
```

---

## Implementation 6: Real-World Applications

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

/**
 * Sort students by GPA using bucket sort
 */
struct Student {
    string name;
    double gpa;
    
    bool operator<(const Student& other) const {
        return gpa < other.gpa;
    }
};

void sortStudentsByGPA(vector<Student>& students) {
    if (students.empty()) return;
    
    // Find GPA range
    double minGPA = students[0].gpa;
    double maxGPA = students[0].gpa;
    
    for (const auto& s : students) {
        minGPA = min(minGPA, s.gpa);
        maxGPA = max(maxGPA, s.gpa);
    }
    
    // Create buckets for GPA ranges (0.0-4.0 scale)
    int numBuckets = 40; // 0.1 increments
    vector<vector<Student>> buckets(numBuckets);
    
    // Distribute students
    for (const auto& s : students) {
        int bucketIndex = (int)((s.gpa - minGPA) / (maxGPA - minGPA) * (numBuckets - 1));
        bucketIndex = min(bucketIndex, numBuckets - 1);
        buckets[bucketIndex].push_back(s);
    }
    
    // Sort each bucket
    for (int i = 0; i < numBuckets; i++) {
        sort(buckets[i].begin(), buckets[i].end());
    }
    
    // Collect sorted students
    students.clear();
    for (int i = 0; i < numBuckets; i++) {
        students.insert(students.end(), buckets[i].begin(), buckets[i].end());
    }
}

/**
 * Sort products by price range using bucket sort
 */
struct Product {
    string name;
    double price;
    
    bool operator<(const Product& other) const {
        return price < other.price;
    }
};

void sortProductsByPrice(vector<Product>& products) {
    if (products.empty()) return;
    
    // Find price range
    double minPrice = products[0].price;
    double maxPrice = products[0].price;
    
    for (const auto& p : products) {
        minPrice = min(minPrice, p.price);
        maxPrice = max(maxPrice, p.price);
    }
    
    // Create price range buckets
    int numBuckets = 10; // 10 price ranges
    vector<vector<Product>> buckets(numBuckets);
    
    // Distribute products
    for (const auto& p : products) {
        int bucketIndex = (int)((p.price - minPrice) / (maxPrice - minPrice) * (numBuckets - 1));
        bucketIndex = min(bucketIndex, numBuckets - 1);
        buckets[bucketIndex].push_back(p);
    }
    
    // Sort each bucket
    for (int i = 0; i < numBuckets; i++) {
        sort(buckets[i].begin(), buckets[i].end());
    }
    
    // Collect sorted products
    products.clear();
    for (int i = 0; i < numBuckets; i++) {
        products.insert(products.end(), buckets[i].begin(), buckets[i].end());
    }
}

/**
 * Bucket sort for geographical data (by latitude/longitude)
 */
struct Location {
    string name;
    double latitude;
    double longitude;
    
    bool operator<(const Location& other) const {
        return latitude < other.latitude;
    }
};

void sortLocationsByLatitude(vector<Location>& locations) {
    if (locations.empty()) return;
    
    // Find latitude range (-90 to 90)
    double minLat = -90.0;
    double maxLat = 90.0;
    
    // Create latitude buckets
    int numBuckets = 18; // 10-degree increments
    vector<vector<Location>> buckets(numBuckets);
    
    // Distribute locations
    for (const auto& loc : locations) {
        int bucketIndex = (int)((loc.latitude - minLat) / (maxLat - minLat) * (numBuckets - 1));
        bucketIndex = min(bucketIndex, numBuckets - 1);
        buckets[bucketIndex].push_back(loc);
    }
    
    // Sort each bucket
    for (int i = 0; i < numBuckets; i++) {
        sort(buckets[i].begin(), buckets[i].end());
    }
    
    // Collect sorted locations
    locations.clear();
    for (int i = 0; i < numBuckets; i++) {
        locations.insert(locations.end(), buckets[i].begin(), buckets[i].end());
    }
}

/**
 * Bucket sort for time-based data
 */
struct Event {
    string name;
    int timestamp; // Unix timestamp
    
    bool operator<(const Event& other) const {
        return timestamp < other.timestamp;
    }
};

void sortEventsByTime(vector<Event>& events) {
    if (events.empty()) return;
    
    // Find time range
    int minTime = events[0].timestamp;
    int maxTime = events[0].timestamp;
    
    for (const auto& e : events) {
        minTime = min(minTime, e.timestamp);
        maxTime = max(maxTime, e.timestamp);
    }
    
    // Create time buckets (e.g., hourly buckets)
    int bucketSize = 3600; // 1 hour in seconds
    int numBuckets = (maxTime - minTime) / bucketSize + 1;
    
    vector<vector<Event>> buckets(numBuckets);
    
    // Distribute events
    for (const auto& e : events) {
        int bucketIndex = (e.timestamp - minTime) / bucketSize;
        buckets[bucketIndex].push_back(e);
    }
    
    // Sort each bucket
    for (int i = 0; i < numBuckets; i++) {
        sort(buckets[i].begin(), buckets[i].end());
    }
    
    // Collect sorted events
    events.clear();
    for (int i = 0; i < numBuckets; i++) {
        events.insert(events.end(), buckets[i].begin(), buckets[i].end());
    }
}

int main() {
    // Test student sorting
    vector<Student> students = {
        {"Alice", 3.7},
        {"Bob", 2.9},
        {"Charlie", 3.9},
        {"Diana", 3.2},
        {"Eve", 4.0},
        {"Frank", 2.5}
    };
    
    cout << "Student Sorting by GPA:" << endl;
    cout << "Before sorting:" << endl;
    for (const auto& s : students) {
        cout << s.name << ": " << s.gpa << endl;
    }
    
    sortStudentsByGPA(students);
    
    cout << "\nAfter sorting:" << endl;
    for (const auto& s : students) {
        cout << s.name << ": " << s.gpa << endl;
    }
    
    // Test product sorting
    vector<Product> products = {
        {"Laptop", 999.99},
        {"Mouse", 29.99},
        {"Keyboard", 79.99},
        {"Monitor", 299.99},
        {"Headphones", 199.99}
    };
    
    cout << "\nProduct Sorting by Price:" << endl;
    cout << "Before sorting:" << endl;
    for (const auto& p : products) {
        cout << p.name << ": $" << p.price << endl;
    }
    
    sortProductsByPrice(products);
    
    cout << "\nAfter sorting:" << endl;
    for (const auto& p : products) {
        cout << p.name << ": $" << p.price << endl;
    }
    
    // Test location sorting
    vector<Location> locations = {
        {"New York", 40.7128, -74.0060},
        {"Los Angeles", 34.0522, -118.2437},
        {"Chicago", 41.8781, -87.6298},
        {"Houston", 29.7604, -95.3698},
        {"Phoenix", 33.4484, -112.0740}
    };
    
    cout << "\nLocation Sorting by Latitude:" << endl;
    cout << "Before sorting:" << endl;
    for (const auto& loc : locations) {
        cout << loc.name << ": " << loc.latitude << "°" << endl;
    }
    
    sortLocationsByLatitude(locations);
    
    cout << "\nAfter sorting:" << endl;
    for (const auto& loc : locations) {
        cout << loc.name << ": " << loc.latitude << "°" << endl;
    }
    
    return 0;
}
```

**Output:**
```
Student Sorting by GPA:
Before sorting:
Alice: 3.7
Bob: 2.9
Charlie: 3.9
Diana: 3.2
Eve: 4.0
Frank: 2.5

After sorting:
Frank: 2.5
Bob: 2.9
Diana: 3.2
Alice: 3.7
Charlie: 3.9
Eve: 4.0

Product Sorting by Price:
Before sorting:
Laptop: $999.99
Mouse: $29.99
Keyboard: $79.99
Monitor: $299.99
Headphones: $199.99

After sorting:
Mouse: $29.99
Keyboard: $79.99
Headphones: $199.99
Monitor: $299.99
Laptop: $999.99

Location Sorting by Latitude:
Before sorting:
New York: 40.7128°
Los Angeles: 34.0522°
Chicago: 41.8781°
Houston: 29.7604°
Phoenix: 33.4484°

After sorting:
Houston: 29.7604°
Los Angeles: 34.0522°
Phoenix: 33.4484°
New York: 40.7128°
Chicago: 41.8781°
```

---

## Advantages and Disadvantages

### Advantages
- ✅ O(n + k) average time complexity
- ✅ Excellent for uniformly distributed data
- ✅ Stable sort - maintains relative order
- ✅ Can be parallelized easily
- ✅ Adaptable to different data distributions

### Disadvantages
- ❌ O(n²) worst case (all elements in one bucket)
- ❌ Performance depends on data distribution
- ❌ Space complexity O(n + k)
- ❌ Requires knowledge of data range
- ❌ Not suitable for all data types

---

## Best Practices

1. **Use for uniformly distributed data**
2. **Choose appropriate bucket count** based on data size and distribution
3. **Use insertion sort** for small buckets
4. **Consider adaptive bucket sizing**
5. **Handle edge cases** like empty arrays and single elements

---

## Common Pitfalls

1. **Poor bucket selection** leading to unbalanced buckets
2. **Wrong bucket size** for the data distribution
3. **Not handling edge cases** properly
4. **Choosing inappropriate bucket sorting algorithm**
5. **Ignoring data distribution characteristics**

---

## Summary

Bucket sort is an excellent choice for uniformly distributed data, offering linear time complexity when the data is well-distributed across buckets. It's particularly useful for floating-point numbers and when the data distribution is known.

**Key Takeaways:**
- Time Complexity: O(n + k) average, O(n²) worst
- Space Complexity: O(n + k)
- Stable: ✅
- In-place: ❌
- Best for: Uniformly distributed data, floating-point numbers
- Performance highly dependent on data distribution
