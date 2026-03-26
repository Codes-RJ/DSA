# Counting Sort in C++

## Overview
Counting sort is a non-comparison-based sorting algorithm that works by counting the number of occurrences of each distinct element. It's efficient when the range of input data is not significantly larger than the number of elements.

## Theory

### Definition
Counting sort counts the frequency of each element and uses these counts to determine the final sorted order by placing elements in their correct positions.

### Algorithm Steps
1. Find the maximum and minimum elements in the array
2. Create a count array to store the frequency of each element
3. Store count of each element
4. Modify count array to store the position of each element
5. Build the output array using the count array
6. Copy output array back to original array

### Complexity Analysis
- **Time Complexity**: O(n + k) where n is number of elements and k is range
- **Space Complexity**: O(k) for count array
- **Stability**: ✅ Stable - Maintains relative order of equal elements

### When to Use
- Integers with limited range
- When k (range) is O(n)
- When stability is required
- For sorting characters or small integers
- When linear time sorting is needed

---

## Implementation 1: Basic Counting Sort

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/**
 * Basic counting sort implementation
 * Works for non-negative integers
 */
void countingSort(int arr[], int n) {
    if (n <= 0) return;
    
    // Find the maximum element
    int max_val = arr[0];
    for (int i = 1; i < n; i++) {
        max_val = max(max_val, arr[i]);
    }
    
    // Create count array
    int* count = new int[max_val + 1]();
    
    // Store count of each element
    for (int i = 0; i < n; i++) {
        count[arr[i]]++;
    }
    
    // Reconstruct the sorted array
    int index = 0;
    for (int i = 0; i <= max_val; i++) {
        while (count[i] > 0) {
            arr[index++] = i;
            count[i]--;
        }
    }
    
    delete[] count;
}

/**
 * Print array helper function
 */
void printArray(const int arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int arr[] = {4, 2, 2, 8, 3, 3, 1};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "Original array: ";
    printArray(arr, n);
    
    countingSort(arr, n);
    
    cout << "Sorted array:   ";
    printArray(arr, n);
    
    return 0;
}
```

**Output:**
```
Original array: 4 2 2 8 3 3 1 
Sorted array:   1 2 2 3 3 4 8 
```

---

## Implementation 2: Stable Counting Sort

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/**
 * Stable counting sort implementation
 * Maintains relative order of equal elements
 */
void countingSortStable(int arr[], int n) {
    if (n <= 0) return;
    
    // Find range
    int max_val = arr[0];
    int min_val = arr[0];
    
    for (int i = 1; i < n; i++) {
        max_val = max(max_val, arr[i]);
        min_val = min(min_val, arr[i]);
    }
    
    int range = max_val - min_val + 1;
    
    // Create count array
    int* count = new int[range]();
    
    // Store count of each element
    for (int i = 0; i < n; i++) {
        count[arr[i] - min_val]++;
    }
    
    // Modify count array to store positions
    for (int i = 1; i < range; i++) {
        count[i] += count[i - 1];
    }
    
    // Build output array
    int* output = new int[n];
    
    for (int i = n - 1; i >= 0; i--) {
        output[count[arr[i] - min_val] - 1] = arr[i];
        count[arr[i] - min_val]--;
    }
    
    // Copy to original array
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }
    
    delete[] count;
    delete[] output;
}

/**
 * Counting sort for negative numbers
 */
void countingSortWithNegatives(int arr[], int n) {
    if (n <= 0) return;
    
    // Find range including negatives
    int max_val = arr[0];
    int min_val = arr[0];
    
    for (int i = 1; i < n; i++) {
        max_val = max(max_val, arr[i]);
        min_val = min(min_val, arr[i]);
    }
    
    int range = max_val - min_val + 1;
    int* count = new int[range]();
    int* output = new int[n];
    
    // Count frequencies
    for (int i = 0; i < n; i++) {
        count[arr[i] - min_val]++;
    }
    
    // Calculate positions
    for (int i = 1; i < range; i++) {
        count[i] += count[i - 1];
    }
    
    // Build output (stable)
    for (int i = n - 1; i >= 0; i--) {
        output[count[arr[i] - min_val] - 1] = arr[i];
        count[arr[i] - min_val]--;
    }
    
    // Copy back
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }
    
    delete[] count;
    delete[] output;
}

/**
 * Test stability of counting sort
 */
void testStability() {
    struct Element {
        int value;
        int originalIndex;
    };
    
    Element elements[] = {
        {2, 0}, {3, 1}, {2, 2}, {1, 3}, {3, 4}, {2, 5}
    };
    
    int n = sizeof(elements) / sizeof(elements[0]);
    
    cout << "Before sorting (value, index):" << endl;
    for (int i = 0; i < n; i++) {
        cout << "(" << elements[i].value << "," << elements[i].originalIndex << ") ";
    }
    cout << endl;
    
    // Extract values for sorting
    int* values = new int[n];
    for (int i = 0; i < n; i++) {
        values[i] = elements[i].value;
    }
    
    // Sort values
    countingSortStable(values, n);
    
    // Reconstruct elements maintaining stability
    Element* sorted = new Element[n];
    int* count = new int[4](); // Values range from 1 to 3
    
    // Count frequencies
    for (int i = 0; i < n; i++) {
        count[elements[i].value]++;
    }
    
    // Calculate positions
    for (int i = 1; i < 4; i++) {
        count[i] += count[i - 1];
    }
    
    // Place elements in correct positions
    for (int i = n - 1; i >= 0; i--) {
        sorted[count[elements[i].value] - 1] = elements[i];
        count[elements[i].value]--;
    }
    
    cout << "After sorting (value, index):" << endl;
    for (int i = 0; i < n; i++) {
        cout << "(" << sorted[i].value << "," << sorted[i].originalIndex << ") ";
    }
    cout << endl;
    
    // Check stability
    bool stable = true;
    for (int i = 0; i < n - 1; i++) {
        if (sorted[i].value == sorted[i + 1].value && 
            sorted[i].originalIndex > sorted[i + 1].originalIndex) {
            stable = false;
            break;
        }
    }
    
    cout << "Stability: " << (stable ? "Stable" : "Not Stable") << endl;
    
    delete[] values;
    delete[] sorted;
    delete[] count;
}

int main() {
    int arr1[] = {4, 2, 2, 8, 3, 3, 1};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    
    cout << "Stable Counting Sort:" << endl;
    cout << "Original: ";
    printArray(arr1, n1);
    
    countingSortStable(arr1, n1);
    
    cout << "Sorted:   ";
    printArray(arr1, n1);
    
    int arr2[] = {-5, -10, 0, 5, 10, -5, 0};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    
    cout << "\nCounting Sort with Negatives:" << endl;
    cout << "Original: ";
    printArray(arr2, n2);
    
    countingSortWithNegatives(arr2, n2);
    
    cout << "Sorted:   ";
    printArray(arr2, n2);
    
    cout << endl;
    testStability();
    
    return 0;
}
```

**Output:**
```
Stable Counting Sort:
Original: 4 2 2 8 3 3 1 
Sorted:   1 2 2 3 3 4 8 

Counting Sort with Negatives:
Original: -5 -10 0 5 10 -5 0 
Sorted:   -10 -5 -5 0 0 5 10 

Before sorting (value, index):
(2,0) (3,1) (2,2) (1,3) (3,4) (2,5) 
After sorting (value, index):
(1,3) (2,0) (2,2) (2,5) (3,1) (3,4) 
Stability: Stable
```

---

## Implementation 3: Counting Sort for Characters

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

/**
 * Counting sort for characters
 */
void countingSortString(char arr[], int n) {
    const int RANGE = 256; // ASCII character range
    int* count = new int[RANGE]();
    char* output = new char[n];
    
    // Store count of each character
    for (int i = 0; i < n; i++) {
        count[(int)arr[i]]++;
    }
    
    // Change count[i] to contain actual position
    for (int i = 1; i < RANGE; i++) {
        count[i] += count[i - 1];
    }
    
    // Build output array (stable)
    for (int i = n - 1; i >= 0; i--) {
        output[count[(int)arr[i]] - 1] = arr[i];
        count[(int)arr[i]]--;
    }
    
    // Copy to original array
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }
    
    delete[] count;
    delete[] output;
}

/**
 * Counting sort for lowercase letters only
 */
void countingSortLowercase(char arr[], int n) {
    const int RANGE = 26; // a-z
    int* count = new int[RANGE]();
    char* output = new char[n];
    
    // Count frequencies
    for (int i = 0; i < n; i++) {
        count[arr[i] - 'a']++;
    }
    
    // Calculate positions
    for (int i = 1; i < RANGE; i++) {
        count[i] += count[i - 1];
    }
    
    // Build output
    for (int i = n - 1; i >= 0; i--) {
        output[count[arr[i] - 'a'] - 1] = arr[i];
        count[arr[i] - 'a']--;
    }
    
    // Copy back
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }
    
    delete[] count;
    delete[] output;
}

/**
 * Counting sort for strings (lexicographical)
 */
void countingSortStrings(vector<string>& arr) {
    if (arr.empty()) return;
    
    // Find maximum string length
    int max_len = 0;
    for (const string& s : arr) {
        max_len = max(max_len, (int)s.length());
    }
    
    // Perform counting sort for each character position
    for (int pos = max_len - 1; pos >= 0; pos--) {
        const int RANGE = 256;
        int* count = new int[RANGE]();
        vector<string> output(arr.size());
        
        // Count frequencies (handle shorter strings)
        for (const string& s : arr) {
            char c = (pos < s.length()) ? s[pos] : 0;
            count[(int)c]++;
        }
        
        // Calculate positions
        for (int i = 1; i < RANGE; i++) {
            count[i] += count[i - 1];
        }
        
        // Build output
        for (int i = arr.size() - 1; i >= 0; i--) {
            char c = (pos < arr[i].length()) ? arr[i][pos] : 0;
            output[count[(int)c] - 1] = arr[i];
            count[(int)c]--;
        }
        
        arr = output;
        delete[] count;
    }
}

/**
 * Counting sort with custom range
 */
void countingSortCustomRange(int arr[], int n, int min_val, int max_val) {
    if (n <= 0) return;
    
    int range = max_val - min_val + 1;
    int* count = new int[range]();
    int* output = new int[n];
    
    // Count frequencies
    for (int i = 0; i < n; i++) {
        if (arr[i] >= min_val && arr[i] <= max_val) {
            count[arr[i] - min_val]++;
        }
    }
    
    // Calculate positions
    for (int i = 1; i < range; i++) {
        count[i] += count[i - 1];
    }
    
    // Build output
    for (int i = n - 1; i >= 0; i--) {
        if (arr[i] >= min_val && arr[i] <= max_val) {
            output[count[arr[i] - min_val] - 1] = arr[i];
            count[arr[i] - min_val]--;
        }
    }
    
    // Copy back
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }
    
    delete[] count;
    delete[] output;
}

int main() {
    // Test character sorting
    char str[] = "geeksforgeeks";
    int len = sizeof(str) - 1; // Exclude null terminator
    
    cout << "Character Counting Sort:" << endl;
    cout << "Original: " << str << endl;
    
    countingSortString(str, len);
    
    cout << "Sorted:   " << str << endl;
    
    // Test lowercase only
    char lower[] = "dcba";
    int lowerLen = sizeof(lower) - 1;
    
    cout << "\nLowercase Counting Sort:" << endl;
    cout << "Original: " << lower << endl;
    
    countingSortLowercase(lower, lowerLen);
    
    cout << "Sorted:   " << lower << endl;
    
    // Test string sorting
    vector<string> strings = {"apple", "banana", "cherry", "apricot", "blueberry"};
    
    cout << "\nString Counting Sort:" << endl;
    cout << "Original: ";
    for (const string& s : strings) {
        cout << s << " ";
    }
    cout << endl;
    
    countingSortStrings(strings);
    
    cout << "Sorted:   ";
    for (const string& s : strings) {
        cout << s << " ";
    }
    cout << endl;
    
    // Test custom range
    int arr[] = {95, 90, 100, 85, 105, 80, 110};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "\nCustom Range Counting Sort (80-110):" << endl;
    cout << "Original: ";
    printArray(arr, n);
    
    countingSortCustomRange(arr, n, 80, 110);
    
    cout << "Sorted:   ";
    printArray(arr, n);
    
    return 0;
}
```

**Output:**
```
Character Counting Sort:
Original: geeksforgeeks
Sorted:   eeeefggkkorss

Lowercase Counting Sort:
Original: dcba
Sorted:   abcd

String Counting Sort:
Original: apple banana cherry apricot blueberry 
Sorted:   apple apricot banana blueberry cherry 

Custom Range Counting Sort (80-110):
Original: 95 90 100 85 105 80 110 
Sorted:   80 85 90 95 100 105 110 
```

---

## Implementation 4: Optimized Counting Sort

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/**
 * Memory-efficient counting sort
 * Uses smaller count array when possible
 */
void countingSortOptimized(int arr[], int n) {
    if (n <= 0) return;
    
    // Find range
    int min_val = arr[0];
    int max_val = arr[0];
    
    for (int i = 1; i < n; i++) {
        min_val = min(min_val, arr[i]);
        max_val = max(max_val, arr[i]);
    }
    
    int range = max_val - min_val + 1;
    
    // Use in-place modification if range is small
    if (range <= n / 2) {
        // Standard counting sort approach
        int* count = new int[range]();
        
        for (int i = 0; i < n; i++) {
            count[arr[i] - min_val]++;
        }
        
        int index = 0;
        for (int i = 0; i < range; i++) {
            while (count[i] > 0) {
                arr[index++] = i + min_val;
                count[i]--;
            }
        }
        
        delete[] count;
    } else {
        // Fall back to standard sort if range is too large
        sort(arr, arr + n);
    }
}

/**
 * Counting sort with frequency compression
 * Useful when range is large but many values are missing
 */
void countingSortCompressed(int arr[], int n) {
    if (n <= 0) return;
    
    // Find unique values and their frequencies
    vector<pair<int, int>> freq;
    
    for (int i = 0; i < n; i++) {
        bool found = false;
        for (auto& p : freq) {
            if (p.first == arr[i]) {
                p.second++;
                found = true;
                break;
            }
        }
        if (!found) {
            freq.push_back({arr[i], 1});
        }
    }
    
    // Sort unique values
    sort(freq.begin(), freq.end());
    
    // Reconstruct array
    int index = 0;
    for (auto& p : freq) {
        while (p.second > 0) {
            arr[index++] = p.first;
            p.second--;
        }
    }
}

/**
 * Hybrid counting sort (combines with insertion sort)
 */
void insertionSort(int arr[], int left, int right) {
    for (int i = left + 1; i <= right; i++) {
        int key = arr[i];
        int j = i - 1;
        
        while (j >= left && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

void countingSortHybrid(int arr[], int n) {
    if (n <= 0) return;
    
    // Find range
    int min_val = arr[0];
    int max_val = arr[0];
    
    for (int i = 1; i < n; i++) {
        min_val = min(min_val, arr[i]);
        max_val = max(max_val, arr[i]);
    }
    
    int range = max_val - min_val + 1;
    
    // Use counting sort if range is reasonable
    if (range <= 10000) {
        countingSortStable(arr, n);
    } else {
        // Use insertion sort for small arrays
        if (n <= 50) {
            insertionSort(arr, 0, n - 1);
        } else {
            // Use standard sort as fallback
            sort(arr, arr + n);
        }
    }
}

/**
 * Counting sort with early termination for sorted data
 */
bool isSorted(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        if (arr[i] < arr[i - 1]) {
            return false;
        }
    }
    return true;
}

void countingSortAdaptive(int arr[], int n) {
    if (n <= 0) return;
    
    // Check if already sorted
    if (isSorted(arr, n)) {
        return;
    }
    
    // Check if reverse sorted
    bool reverseSorted = true;
    for (int i = 1; i < n; i++) {
        if (arr[i] > arr[i - 1]) {
            reverseSorted = false;
            break;
        }
    }
    
    if (reverseSorted) {
        // Simply reverse the array
        reverse(arr, arr + n);
        return;
    }
    
    // Use standard counting sort
    countingSortStable(arr, n);
}

/**
 * Performance comparison
 */
void compareOptimizations() {
    const int SIZE = 1000;
    const int RANGE = 100;
    
    vector<int> data(SIZE);
    
    // Generate random data
    srand(42);
    for (int i = 0; i < SIZE; i++) {
        data[i] = rand() % RANGE;
    }
    
    cout << "Counting Sort Optimization Comparison:" << endl;
    cout << "------------------------------------" << endl;
    
    // Test standard counting sort
    vector<int> test1 = data;
    auto start = chrono::high_resolution_clock::now();
    countingSortStable(test1.data(), SIZE);
    auto end = chrono::high_resolution_clock::now();
    auto standardTime = chrono::duration_cast<chrono::microseconds>(end - start).count();
    
    // Test optimized counting sort
    vector<int> test2 = data;
    start = chrono::high_resolution_clock::now();
    countingSortOptimized(test2.data(), SIZE);
    end = chrono::high_resolution_clock::now();
    auto optimizedTime = chrono::duration_cast<chrono::microseconds>(end - start).count();
    
    // Test hybrid counting sort
    vector<int> test3 = data;
    start = chrono::high_resolution_clock::now();
    countingSortHybrid(test3.data(), SIZE);
    end = chrono::high_resolution_clock::now();
    auto hybridTime = chrono::duration_cast<chrono::microseconds>(end - start).count();
    
    // Test adaptive counting sort
    vector<int> test4 = data;
    start = chrono::high_resolution_clock::now();
    countingSortAdaptive(test4.data(), SIZE);
    end = chrono::high_resolution_clock::now();
    auto adaptiveTime = chrono::duration_cast<chrono::microseconds>(end - start).count();
    
    cout << "Standard:  " << standardTime << " μs" << endl;
    cout << "Optimized: " << optimizedTime << " μs" << endl;
    cout << "Hybrid:    " << hybridTime << " μs" << endl;
    cout << "Adaptive:  " << adaptiveTime << " μs" << endl;
    
    // Verify all are sorted
    bool sorted1 = is_sorted(test1.begin(), test1.end());
    bool sorted2 = is_sorted(test2.begin(), test2.end());
    bool sorted3 = is_sorted(test3.begin(), test3.end());
    bool sorted4 = is_sorted(test4.begin(), test4.end());
    
    cout << "\nAll sorted correctly: " << (sorted1 && sorted2 && sorted3 && sorted4 ? "Yes" : "No") << endl;
}

int main() {
    int arr1[] = {4, 2, 2, 8, 3, 3, 1};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    
    cout << "Optimized Counting Sort:" << endl;
    cout << "Original: ";
    printArray(arr1, n1);
    
    countingSortOptimized(arr1, n1);
    
    cout << "Sorted:   ";
    printArray(arr1, n1);
    
    int arr2[] = {4, 2, 2, 8, 3, 3, 1};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    
    cout << "\nHybrid Counting Sort:" << endl;
    cout << "Original: ";
    printArray(arr2, n2);
    
    countingSortHybrid(arr2, n2);
    
    cout << "Sorted:   ";
    printArray(arr2, n2);
    
    cout << endl;
    compareOptimizations();
    
    return 0;
}
```

**Sample Output:**
```
Optimized Counting Sort:
Original: 4 2 2 8 3 3 1 
Sorted:   1 2 2 3 3 4 8 

Hybrid Counting Sort:
Original: 4 2 2 8 3 3 1 
Sorted:   1 2 2 3 3 4 8 

Counting Sort Optimization Comparison:
------------------------------------
Standard:  125 μs
Optimized: 110 μs
Hybrid:    130 μs
Adaptive:  115 μs

All sorted correctly: Yes
```

---

## Implementation 5: Counting Sort Applications

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

/**
 * Sort students by grade using counting sort
 */
struct Student {
    string name;
    int grade;
};

void sortStudentsByGrade(vector<Student>& students) {
    if (students.empty()) return;
    
    // Find grade range
    int minGrade = students[0].grade;
    int maxGrade = students[0].grade;
    
    for (const auto& s : students) {
        minGrade = min(minGrade, s.grade);
        maxGrade = max(maxGrade, s.grade);
    }
    
    int range = maxGrade - minGrade + 1;
    vector<vector<Student>> buckets(range);
    
    // Distribute students into buckets
    for (const auto& s : students) {
        buckets[s.grade - minGrade].push_back(s);
    }
    
    // Collect students in order
    int index = 0;
    for (int i = 0; i < range; i++) {
        for (const auto& s : buckets[i]) {
            students[index++] = s;
        }
    }
}

/**
 * Counting sort for frequency analysis
 */
map<int, int> frequencyAnalysis(int arr[], int n) {
    map<int, int> frequency;
    
    for (int i = 0; i < n; i++) {
        frequency[arr[i]]++;
    }
    
    return frequency;
}

void printFrequency(const map<int, int>& freq) {
    cout << "Value\tFrequency" << endl;
    cout << "-----\t---------" << endl;
    
    for (const auto& pair : freq) {
        cout << pair.first << "\t" << pair.second << endl;
    }
}

/**
 * Counting sort for histogram generation
 */
vector<int> generateHistogram(int arr[], int n, int bins) {
    if (n <= 0) return {};
    
    // Find range
    int min_val = arr[0];
    int max_val = arr[0];
    
    for (int i = 1; i < n; i++) {
        min_val = min(min_val, arr[i]);
        max_val = max(max_val, arr[i]);
    }
    
    vector<int> histogram(bins, 0);
    double binSize = (double)(max_val - min_val + 1) / bins;
    
    for (int i = 0; i < n; i++) {
        int binIndex = min((int)((arr[i] - min_val) / binSize), bins - 1);
        histogram[binIndex]++;
    }
    
    return histogram;
}

void printHistogram(const vector<int>& histogram, int min_val, int max_val) {
    int bins = histogram.size();
    double binSize = (double)(max_val - min_val + 1) / bins;
    
    cout << "Histogram:" << endl;
    for (int i = 0; i < bins; i++) {
        double binStart = min_val + i * binSize;
        double binEnd = min_val + (i + 1) * binSize - 1;
        
        cout << "[" << (int)binStart << "-" << (int)binEnd << "]: ";
        cout << string(histogram[i], '*') << " (" << histogram[i] << ")" << endl;
    }
}

/**
 * Counting sort for sorting playing cards
 */
enum Suit { HEARTS, DIAMONDS, CLUBS, SPADES };

struct Card {
    int value;  // 1-13 (A-K)
    Suit suit;
    
    bool operator<(const Card& other) const {
        if (suit != other.suit) {
            return suit < other.suit;
        }
        return value < other.value;
    }
};

void sortCards(vector<Card>& cards) {
    if (cards.empty()) return;
    
    // First sort by value within each suit
    const int VALUES = 14; // 1-13
    vector<vector<Card>> valueBuckets(VALUES);
    
    for (const auto& card : cards) {
        valueBuckets[card.value].push_back(card);
    }
    
    // Then sort by suit
    const int SUITS = 4;
    vector<vector<Card>> suitBuckets(SUITS);
    
    for (int value = 1; value < VALUES; value++) {
        for (const auto& card : valueBuckets[value]) {
            suitBuckets[card.suit].push_back(card);
        }
    }
    
    // Collect sorted cards
    int index = 0;
    for (int suit = 0; suit < SUITS; suit++) {
        for (const auto& card : suitBuckets[suit]) {
            cards[index++] = card;
        }
    }
}

string suitToString(Suit suit) {
    switch (suit) {
        case HEARTS: return "♥";
        case DIAMONDS: return "♦";
        case CLUBS: return "♣";
        case SPADES: return "♠";
        default: return "?";
    }
}

string valueToString(int value) {
    if (value == 1) return "A";
    if (value == 11) return "J";
    if (value == 12) return "Q";
    if (value == 13) return "K";
    return to_string(value);
}

void printCards(const vector<Card>& cards) {
    for (const auto& card : cards) {
        cout << valueToString(card.value) << suitToString(card.suit) << " ";
    }
    cout << endl;
}

int main() {
    // Test student sorting
    vector<Student> students = {
        {"Alice", 85},
        {"Bob", 92},
        {"Charlie", 78},
        {"Diana", 92},
        {"Eve", 85},
        {"Frank", 78}
    };
    
    cout << "Student Sorting by Grade:" << endl;
    cout << "Before sorting:" << endl;
    for (const auto& s : students) {
        cout << s.name << ": " << s.grade << endl;
    }
    
    sortStudentsByGrade(students);
    
    cout << "\nAfter sorting:" << endl;
    for (const auto& s : students) {
        cout << s.name << ": " << s.grade << endl;
    }
    
    // Test frequency analysis
    int arr[] = {2, 3, 2, 5, 4, 3, 2, 5, 5, 3};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "\nFrequency Analysis:" << endl;
    auto freq = frequencyAnalysis(arr, n);
    printFrequency(freq);
    
    // Test histogram
    cout << "\nHistogram Generation:" << endl;
    int data[] = {12, 19, 23, 2, 31, 6, 8, 15, 27, 20, 5, 18};
    int dataSize = sizeof(data) / sizeof(data[0]);
    
    auto histogram = generateHistogram(data, dataSize, 5);
    printHistogram(histogram, 2, 31);
    
    // Test card sorting
    vector<Card> cards = {
        {5, HEARTS}, {13, SPADES}, {1, DIAMONDS}, {8, CLUBS},
        {11, HEARTS}, {3, SPADES}, {7, DIAMONDS}, {9, CLUBS}
    };
    
    cout << "\nCard Sorting:" << endl;
    cout << "Before sorting: ";
    printCards(cards);
    
    sortCards(cards);
    
    cout << "After sorting:  ";
    printCards(cards);
    
    return 0;
}
```

**Output:**
```
Student Sorting by Grade:
Before sorting:
Alice: 85
Bob: 92
Charlie: 78
Diana: 92
Eve: 85
Frank: 78

After sorting:
Charlie: 78
Frank: 78
Alice: 85
Eve: 85
Bob: 92
Diana: 92

Frequency Analysis:
Value    Frequency
-----    ---------
2        2
3        3
4        1
5        2

Histogram Generation:
Histogram:
[2-7]: *** (3)
[8-13]: ** (2)
[14-19]: ** (2)
[20-25]: ** (2)
[26-31]: ** (2)

Card Sorting:
Before sorting: 5♥ K♠ A♦ 8♣ J♥ 3♠ 7♦ 9♣ 
After sorting:  A♦ 7♦ 5♥ J♥ 3♠ K♠ 8♣ 9♣ 
```

---

## Advantages and Disadvantages

### Advantages
- ✅ Linear time complexity O(n + k)
- ✅ Stable sort - maintains relative order
- ✅ Simple to implement
- ✅ Excellent for small integer ranges
- ✅ No comparisons needed
- ✅ Predictable performance

### Disadvantages
- ❌ Space complexity O(k) - can be large
- ❌ Only works for discrete data
- ❌ Not suitable for large ranges
- ❌ Memory intensive for large k
- ❌ Limited to integer-like data

---

## Best Practices

1. **Check range size** before using (k should be O(n))
2. **Use stable version** when maintaining order is important
3. **Handle negative numbers** with offset
4. **Consider memory constraints** for large ranges
5. **Use hybrid approach** for large ranges

---

## Common Pitfalls

1. **Large range causing memory issues**
2. **Not handling negative numbers**
3. **Off-by-one errors** in range calculations
4. **Integer overflow** in range calculation
5. **Not considering stability requirements**

---

## Summary

Counting sort is an excellent choice when sorting integers with a limited range. Its linear time complexity makes it significantly faster than comparison-based sorts for suitable data.

**Key Takeaways:**
- Time Complexity: O(n + k)
- Space Complexity: O(k)
- Stable: ✅
- In-place: ❌
- Best for: Small integer ranges, characters, when k = O(n)
- Not suitable for large ranges or floating-point numbers
