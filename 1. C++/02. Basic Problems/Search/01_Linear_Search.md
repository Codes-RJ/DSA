# Linear Search in C++

## Overview
Linear search is the simplest searching algorithm that sequentially checks each element in a container until a match is found or the entire container has been searched. It works on both sorted and unsorted data structures and is the foundation for understanding more complex searching algorithms.

## Theory

### Definition
Linear search, also known as sequential search, traverses a container element by element from the beginning to find a target value. It continues until either the target is found or all elements have been examined.

### Algorithm Steps
1. Start from the first element of the container
2. Compare the current element with the target value
3. If they match, return the position (index)
4. If not, move to the next element
5. Repeat steps 2-4 until the target is found or the end is reached
6. If the end is reached without finding the target, return a sentinel value (e.g., -1)

### Complexity Analysis
- **Time Complexity (Best Case)**: O(1) - when target is the first element
- **Time Complexity (Average Case)**: O(n) - examines approximately n/2 elements
- **Time Complexity (Worst Case)**: O(n) - when target is last or not present
- **Space Complexity**: O(1) - no additional memory required

### When to Use
- Container is unsorted
- Container size is small
- Searching is infrequent
- Implementing simple lookups
- As a building block for other algorithms

### When NOT to Use
- Large datasets (use binary search or hash tables)
- Frequent searches (consider indexing)
- Performance-critical applications

---

## Implementation 1: Basic Linear Search (Array)

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Linear Search on integer array
 * Returns index of target if found, -1 otherwise
 */
int linearSearch(int arr[], int size, int target) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) {
            return i;  // Element found, return index
        }
    }
    return -1;  // Element not found
}

int main() {
    int arr[] = {10, 23, 45, 70, 11, 15, 89, 34};
    int size = sizeof(arr) / sizeof(arr[0]);
    int target = 70;
    
    int result = linearSearch(arr, size, target);
    
    if (result != -1) {
        cout << "Element " << target << " found at index: " << result << endl;
    } else {
        cout << "Element " << target << " not found in array" << endl;
    }
    
    return 0;
}
```

**Output:**
```
Element 70 found at index: 3
```

---

## Implementation 2: Linear Search with Multiple Occurrences

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Finds all occurrences of target in array
 * Returns vector of indices where target appears
 */
vector<int> findAllOccurrences(int arr[], int size, int target) {
    vector<int> indices;
    
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) {
            indices.push_back(i);
        }
    }
    
    return indices;
}

int main() {
    int arr[] = {10, 23, 45, 70, 11, 70, 15, 89, 70, 34};
    int size = sizeof(arr) / sizeof(arr[0]);
    int target = 70;
    
    vector<int> result = findAllOccurrences(arr, size, target);
    
    if (!result.empty()) {
        cout << "Element " << target << " found at indices: ";
        for (int idx : result) {
            cout << idx << " ";
        }
        cout << endl;
        cout << "Total occurrences: " << result.size() << endl;
    } else {
        cout << "Element " << target << " not found in array" << endl;
    }
    
    return 0;
}
```

**Output:**
```
Element 70 found at indices: 3 5 8 
Total occurrences: 3
```

---

## Implementation 3: Linear Search on Vector (Template Version)

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

/**
 * Generic linear search using templates
 * Works with any data type that supports == operator
 */
template<typename T>
int linearSearch(const vector<T>& vec, const T& target) {
    for (size_t i = 0; i < vec.size(); i++) {
        if (vec[i] == target) {
            return i;
        }
    }
    return -1;
}

int main() {
    // Integer vector
    vector<int> intVec = {10, 23, 45, 70, 11, 15, 89, 34};
    cout << "Searching for 70 in integer vector: ";
    int intResult = linearSearch(intVec, 70);
    if (intResult != -1) {
        cout << "Found at index " << intResult << endl;
    } else {
        cout << "Not found" << endl;
    }
    
    // String vector
    vector<string> strVec = {"apple", "banana", "cherry", "date", "elderberry"};
    cout << "Searching for 'cherry' in string vector: ";
    int strResult = linearSearch(strVec, string("cherry"));
    if (strResult != -1) {
        cout << "Found at index " << strResult << endl;
    } else {
        cout << "Not found" << endl;
    }
    
    // Double vector
    vector<double> doubleVec = {3.14, 2.71, 1.41, 1.73, 2.23};
    cout << "Searching for 2.71 in double vector: ";
    int doubleResult = linearSearch(doubleVec, 2.71);
    if (doubleResult != -1) {
        cout << "Found at index " << doubleResult << endl;
    } else {
        cout << "Not found" << endl;
    }
    
    return 0;
}
```

**Output:**
```
Searching for 70 in integer vector: Found at index 3
Searching for 'cherry' in string vector: Found at index 2
Searching for 2.71 in double vector: Found at index 1
```

---

## Implementation 4: Linear Search with Iterator (STL Style)

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
using namespace std;

/**
 * Linear search using iterators (similar to std::find)
 * Returns iterator to found element or end() if not found
 */
template<typename Iterator, typename T>
Iterator linearSearchIterator(Iterator begin, Iterator end, const T& target) {
    for (Iterator it = begin; it != end; ++it) {
        if (*it == target) {
            return it;
        }
    }
    return end;
}

int main() {
    // Vector example
    vector<int> vec = {10, 23, 45, 70, 11, 15, 89, 34};
    auto vecIt = linearSearchIterator(vec.begin(), vec.end(), 70);
    
    if (vecIt != vec.end()) {
        cout << "Found in vector at position: " << distance(vec.begin(), vecIt) << endl;
    } else {
        cout << "Not found in vector" << endl;
    }
    
    // List example
    list<string> lst = {"apple", "banana", "cherry", "date"};
    auto lstIt = linearSearchIterator(lst.begin(), lst.end(), string("cherry"));
    
    if (lstIt != lst.end()) {
        cout << "Found in list: " << *lstIt << endl;
    } else {
        cout << "Not found in list" << endl;
    }
    
    // Using with std::find (built-in)
    cout << "\nUsing std::find (built-in):" << endl;
    auto stdIt = find(vec.begin(), vec.end(), 70);
    if (stdIt != vec.end()) {
        cout << "std::find found at index: " << distance(vec.begin(), stdIt) << endl;
    }
    
    return 0;
}
```

**Output:**
```
Found in vector at position: 3
Found in list: cherry

Using std::find (built-in):
std::find found at index: 3
```

---

## Implementation 5: Sentinal Linear Search (Optimized)

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Sentinel Linear Search - eliminates boundary check in loop
 * Places target at the end to guarantee finding it
 */
int sentinelLinearSearch(int arr[], int size, int target) {
    int last = arr[size - 1];
    arr[size - 1] = target;  // Place target at end (sentinel)
    
    int i = 0;
    while (arr[i] != target) {
        i++;
    }
    
    arr[size - 1] = last;  // Restore original last element
    
    if (i < size - 1 || arr[size - 1] == target) {
        return i;
    }
    
    return -1;
}

int main() {
    int arr[] = {10, 23, 45, 70, 11, 15, 89, 34};
    int size = sizeof(arr) / sizeof(arr[0]);
    
    // Test with existing element
    int result1 = sentinelLinearSearch(arr, size, 70);
    cout << "Search for 70: ";
    if (result1 != -1) {
        cout << "Found at index " << result1 << endl;
    } else {
        cout << "Not found" << endl;
    }
    
    // Test with non-existing element
    int result2 = sentinelLinearSearch(arr, size, 99);
    cout << "Search for 99: ";
    if (result2 != -1) {
        cout << "Found at index " << result2 << endl;
    } else {
        cout << "Not found" << endl;
    }
    
    return 0;
}
```

**Output:**
```
Search for 70: Found at index 3
Search for 99: Not found
```

---

## Implementation 6: Linear Search on Linked List

```cpp
#include <iostream>
using namespace std;

/**
 * Node structure for singly linked list
 */
struct Node {
    int data;
    Node* next;
    
    Node(int val) : data(val), next(nullptr) {}
};

/**
 * Linked List class with linear search
 */
class LinkedList {
private:
    Node* head;
    
public:
    LinkedList() : head(nullptr) {}
    
    void insert(int val) {
        Node* newNode = new Node(val);
        newNode->next = head;
        head = newNode;
    }
    
    /**
     * Linear search in linked list
     * Returns pointer to node if found, nullptr otherwise
     */
    Node* search(int target) {
        Node* current = head;
        int position = 0;
        
        while (current != nullptr) {
            if (current->data == target) {
                cout << "Found at position: " << position << endl;
                return current;
            }
            current = current->next;
            position++;
        }
        
        cout << "Not found" << endl;
        return nullptr;
    }
    
    /**
     * Find and return position (index) of target
     */
    int searchPosition(int target) {
        Node* current = head;
        int position = 0;
        
        while (current != nullptr) {
            if (current->data == target) {
                return position;
            }
            current = current->next;
            position++;
        }
        
        return -1;
    }
    
    void display() {
        Node* current = head;
        while (current != nullptr) {
            cout << current->data << " -> ";
            current = current->next;
        }
        cout << "NULL" << endl;
    }
    
    ~LinkedList() {
        Node* current = head;
        while (current != nullptr) {
            Node* next = current->next;
            delete current;
            current = next;
        }
    }
};

int main() {
    LinkedList list;
    
    // Insert elements
    list.insert(10);
    list.insert(23);
    list.insert(45);
    list.insert(70);
    list.insert(11);
    list.insert(15);
    
    cout << "Linked List: ";
    list.display();
    
    cout << "\nSearching for 70: ";
    Node* result1 = list.search(70);
    if (result1) {
        cout << "Node found with value: " << result1->data << endl;
    }
    
    cout << "\nSearching for 99: ";
    Node* result2 = list.search(99);
    
    cout << "\nPosition of 11: " << list.searchPosition(11) << endl;
    cout << "Position of 100: " << list.searchPosition(100) << endl;
    
    return 0;
}
```

**Output:**
```
Linked List: 15 -> 11 -> 70 -> 45 -> 23 -> 10 -> NULL

Searching for 70: Found at position: 2
Node found with value: 70

Searching for 99: Not found

Position of 11: 1
Position of 100: -1
```

---

## Implementation 7: Recursive Linear Search

```cpp
#include <iostream>
#include <vector>
using namespace std;

/**
 * Recursive linear search on array
 */
int recursiveLinearSearch(int arr[], int index, int size, int target) {
    // Base case: reached end of array
    if (index >= size) {
        return -1;
    }
    
    // Base case: found target
    if (arr[index] == target) {
        return index;
    }
    
    // Recursive case: search remaining array
    return recursiveLinearSearch(arr, index + 1, size, target);
}

/**
 * Recursive linear search for multiple occurrences
 */
void recursiveFindAll(int arr[], int index, int size, int target, vector<int>& indices) {
    // Base case: reached end of array
    if (index >= size) {
        return;
    }
    
    // If found, add to indices
    if (arr[index] == target) {
        indices.push_back(index);
    }
    
    // Recursively search remaining
    recursiveFindAll(arr, index + 1, size, target, indices);
}

int main() {
    int arr[] = {10, 23, 45, 70, 11, 70, 15, 89, 70, 34};
    int size = sizeof(arr) / sizeof(arr[0]);
    
    // Single occurrence search
    int target1 = 70;
    int result = recursiveLinearSearch(arr, 0, size, target1);
    
    cout << "Recursive search for " << target1 << ": ";
    if (result != -1) {
        cout << "Found at index " << result << endl;
    } else {
        cout << "Not found" << endl;
    }
    
    // Multiple occurrences search
    int target2 = 70;
    vector<int> indices;
    recursiveFindAll(arr, 0, size, target2, indices);
    
    cout << "\nRecursive search for all " << target2 << ": ";
    if (!indices.empty()) {
        cout << "Found at indices: ";
        for (int idx : indices) {
            cout << idx << " ";
        }
        cout << "\nTotal occurrences: " << indices.size() << endl;
    } else {
        cout << "Not found" << endl;
    }
    
    // Search for non-existent element
    int target3 = 99;
    int result3 = recursiveLinearSearch(arr, 0, size, target3);
    cout << "\nRecursive search for " << target3 << ": ";
    if (result3 != -1) {
        cout << "Found at index " << result3 << endl;
    } else {
        cout << "Not found" << endl;
    }
    
    return 0;
}
```

**Output:**
```
Recursive search for 70: Found at index 3

Recursive search for all 70: Found at indices: 3 5 8 
Total occurrences: 3

Recursive search for 99: Not found
```

---

## Implementation 8: Linear Search on 2D Array

```cpp
#include <iostream>
#include <utility>
using namespace std;

/**
 * Linear search on 2D array
 * Returns pair of indices (row, col) if found
 */
pair<int, int> linearSearch2D(int arr[][4], int rows, int cols, int target) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (arr[i][j] == target) {
                return {i, j};
            }
        }
    }
    return {-1, -1};
}

/**
 * Find all occurrences in 2D array
 */
void findAllOccurrences2D(int arr[][4], int rows, int cols, int target) {
    int count = 0;
    cout << "Found at positions: ";
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (arr[i][j] == target) {
                cout << "(" << i << "," << j << ") ";
                count++;
            }
        }
    }
    if (count == 0) {
        cout << "None";
    }
    cout << "\nTotal occurrences: " << count << endl;
}

int main() {
    int matrix[3][4] = {
        {10, 23, 45, 70},
        {11, 70, 15, 89},
        {34, 70, 92, 70}
    };
    
    int target = 70;
    
    // Single occurrence search (returns first)
    auto result = linearSearch2D(matrix, 3, 4, target);
    
    if (result.first != -1) {
        cout << "First occurrence of " << target << " found at: (" 
             << result.first << ", " << result.second << ")" << endl;
    } else {
        cout << target << " not found in matrix" << endl;
    }
    
    // Find all occurrences
    cout << "\nAll occurrences of " << target << ":" << endl;
    findAllOccurrences2D(matrix, 3, 4, target);
    
    // Search for non-existent element
    int target2 = 99;
    cout << "\nSearching for " << target2 << ":" << endl;
    findAllOccurrences2D(matrix, 3, 4, target2);
    
    return 0;
}
```

**Output:**
```
First occurrence of 70 found at: (0, 3)

All occurrences of 70:
Found at positions: (0,3) (1,1) (2,1) (2,3) 
Total occurrences: 4

Searching for 99:
Found at positions: None
Total occurrences: 0
```

---

## Implementation 9: Linear Search with Custom Comparator

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <functional>
using namespace std;

/**
 * Linear search with custom comparison function
 */
template<typename T>
int linearSearchWithComparator(const vector<T>& vec, const T& target, 
                                function<bool(const T&, const T&)> comparator) {
    for (size_t i = 0; i < vec.size(); i++) {
        if (comparator(vec[i], target)) {
            return i;
        }
    }
    return -1;
}

/**
 * Linear search for objects with member field
 */
struct Person {
    string name;
    int age;
    
    Person(string n, int a) : name(n), age(a) {}
};

int main() {
    // Example 1: Case-insensitive string search
    vector<string> words = {"Apple", "Banana", "Cherry", "Date", "Elderberry"};
    
    auto caseInsensitiveCompare = [](const string& a, const string& b) {
        if (a.length() != b.length()) return false;
        for (size_t i = 0; i < a.length(); i++) {
            if (tolower(a[i]) != tolower(b[i])) return false;
        }
        return true;
    };
    
    int result = linearSearchWithComparator(words, string("cherry"), caseInsensitiveCompare);
    cout << "Case-insensitive search for 'cherry': ";
    if (result != -1) {
        cout << "Found at index " << result << " (" << words[result] << ")" << endl;
    } else {
        cout << "Not found" << endl;
    }
    
    // Example 2: Search by age in Person objects
    vector<Person> people = {
        {"Alice", 25},
        {"Bob", 30},
        {"Charlie", 35},
        {"Diana", 28}
    };
    
    auto ageComparator = [](const Person& p, int age) {
        return p.age == age;
    };
    
    // Need to adapt for vector<Person> vs int target
    int ageToFind = 30;
    int pos = -1;
    for (size_t i = 0; i < people.size(); i++) {
        if (people[i].age == ageToFind) {
            pos = i;
            break;
        }
    }
    
    cout << "\nSearching for person with age " << ageToFind << ": ";
    if (pos != -1) {
        cout << "Found " << people[pos].name << " at index " << pos << endl;
    } else {
        cout << "Not found" << endl;
    }
    
    // Example 3: Search using greater than (find first > threshold)
    vector<int> numbers = {10, 23, 45, 70, 11, 15, 89, 34};
    int threshold = 50;
    
    auto greaterThanComparator = [threshold](int a, int b) {
        return a > threshold;
    };
    
    // Find first element greater than threshold
    int firstGreater = -1;
    for (size_t i = 0; i < numbers.size(); i++) {
        if (numbers[i] > threshold) {
            firstGreater = i;
            break;
        }
    }
    
    cout << "\nFirst element greater than " << threshold << ": ";
    if (firstGreater != -1) {
        cout << numbers[firstGreater] << " at index " << firstGreater << endl;
    } else {
        cout << "None found" << endl;
    }
    
    return 0;
}
```

**Output:**
```
Case-insensitive search for 'cherry': Found at index 2 (Cherry)

Searching for person with age 30: Found Bob at index 1

First element greater than 50: 70 at index 3
```

---

## Performance Analysis

### Benchmark Comparison

```cpp
#include <iostream>
#include <chrono>
#include <vector>
#include <algorithm>
using namespace std;
using namespace chrono;

/**
 * Measure execution time of linear search
 */
template<typename Func>
long long measureTime(Func func) {
    auto start = high_resolution_clock::now();
    func();
    auto end = high_resolution_clock::now();
    return duration_cast<nanoseconds>(end - start).count();
}

int main() {
    const int SIZE = 10000000;  // 10 million elements
    vector<int> data(SIZE);
    
    // Initialize array
    for (int i = 0; i < SIZE; i++) {
        data[i] = i;
    }
    
    int targetPresent = SIZE / 2;  // Element in middle
    int targetAbsent = SIZE + 1;    // Element not present
    
    // Test 1: Best case (first element)
    auto bestTime = measureTime([&]() {
        for (int i = 0; i < data.size(); i++) {
            if (data[i] == data[0]) break;
        }
    });
    
    // Test 2: Average case (middle element)
    auto avgTime = measureTime([&]() {
        for (int i = 0; i < data.size(); i++) {
            if (data[i] == targetPresent) break;
        }
    });
    
    // Test 3: Worst case (element not present)
    auto worstTime = measureTime([&]() {
        for (int i = 0; i < data.size(); i++) {
            if (data[i] == targetAbsent) break;
        }
    });
    
    cout << "Linear Search Performance (10 million elements):" << endl;
    cout << "Best Case (first element):   " << bestTime << " ns" << endl;
    cout << "Average Case (middle):       " << avgTime << " ns" << endl;
    cout << "Worst Case (not present):    " << worstTime << " ns" << endl;
    
    // Compare with std::find
    auto stdFindTime = measureTime([&]() {
        find(data.begin(), data.end(), targetPresent);
    });
    
    cout << "\nstd::find (middle element):   " << stdFindTime << " ns" << endl;
    
    return 0;
}
```

---

## Advantages and Disadvantages

### Advantages
- ✅ Works on unsorted data
- ✅ Simple to implement and understand
- ✅ No preprocessing required
- ✅ Works on any data structure (arrays, linked lists, etc.)
- ✅ Suitable for small datasets
- ✅ Can find first occurrence efficiently

### Disadvantages
- ❌ Inefficient for large datasets (O(n))
- ❌ Not suitable for frequent searches
- ❌ Cannot leverage sorted order
- ❌ Slower than binary search for sorted data
- ❌ Performance degrades linearly with size

---

## When to Use Linear Search

| Scenario | Recommendation |
|----------|----------------|
| Data is unsorted | ✅ Use linear search |
| Dataset size < 100 | ✅ Linear search is fine |
| Searching infrequently | ✅ Simple implementation wins |
| Need first occurrence | ✅ Linear search works |
| Data in linked list | ✅ Linear search only option |
| Data size > 1,000,000 | ❌ Consider binary search or hash tables |
| Frequent searches | ❌ Consider indexing |
| Sorted data | ❌ Binary search is better |

---

## Best Practices

1. **Use for small datasets** - O(n) is acceptable when n is small
2. **Consider sentinel optimization** - Reduces comparisons in loops
3. **Use `std::find` for STL containers** - Leverages optimized implementations
4. **Return early when found** - Don't continue searching unnecessarily
5. **Consider data structure** - Linear search may be only option for some structures
6. **Profile before optimizing** - Linear search may be sufficient for your use case

---

## Common Pitfalls

1. **Using on large datasets** - Performance degrades significantly
2. **Not handling not-found case** - Always check return value
3. **Searching sorted data with linear search** - Binary search would be faster
4. **Not considering multiple occurrences** - Decide if first or all are needed
5. **Using with custom objects** - Ensure `==` operator is defined

---

## Summary

Linear search is the most fundamental searching algorithm. While it's simple and works on any data structure, its O(n) time complexity makes it unsuitable for large datasets. However, for small, unsorted collections or when simplicity is prioritized over performance, linear search remains a valid choice.

**Key Takeaways:**
- Time Complexity: O(n)
- Space Complexity: O(1)
- Works on unsorted data
- Simple to implement
- Use for small datasets or when data is unsorted
