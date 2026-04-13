# algorithm - Standard Algorithms Library

The `algorithm` header is one of the most powerful headers in C++ STL, providing a collection of functions for operating on ranges of elements.

## 📖 Overview

The `algorithm` header contains numerous template functions that work with iterators to perform operations like searching, sorting, modifying, and manipulating sequences of elements.

## 🎯 Key Categories

1. **Non-modifying sequence operations** - Examine elements without changing them
2. **Modifying sequence operations** - Change the order or values of elements
3. **Sorting operations** - Sort and merge sequences
4. **Binary search operations** - Search in sorted sequences
5. **Set operations** - Perform set-like operations on sorted sequences
6. **Heap operations** - Work with heap data structures
7. **Minimum/maximum operations** - Find min/max values
8. **Numeric operations** - Some numeric algorithms (also in `<numeric>`)

## 🔧 Essential Algorithms

### Sorting Algorithms
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    vector<int> vec = {5, 2, 8, 1, 9, 3};
    
    // Sort in ascending order
    sort(vec.begin(), vec.end());
    
    // Sort in descending order
    sort(vec.begin(), vec.end(), greater<int>());
    
    // Sort with custom comparator
    sort(vec.begin(), vec.end(), [](int a, int b) {
        return a % 3 < b % 3;  // Sort by remainder when divided by 3
    });
    
    return 0;
}
```

### Searching Algorithms
```cpp
vector<int> vec = {1, 3, 5, 7, 9, 11};
int target = 7;

// Linear search (works on unsorted data)
auto it = find(vec.begin(), vec.end(), target);
if (it != vec.end()) {
    cout << "Found at position: " << distance(vec.begin(), it) << endl;
}

// Binary search (requires sorted data)
bool found = binary_search(vec.begin(), vec.end(), target);

// Find position in sorted data
auto lower = lower_bound(vec.begin(), vec.end(), target);
auto upper = upper_bound(vec.begin(), vec.end(), target);
```

### Modifying Algorithms
```cpp
vector<int> vec = {1, 2, 3, 4, 5};

// Reverse
reverse(vec.begin(), vec.end());  // {5, 4, 3, 2, 1}

// Rotate
rotate(vec.begin(), vec.begin() + 2, vec.end());  // {3, 4, 5, 1, 2}

// Shuffle
random_shuffle(vec.begin(), vec.end());  // Random order

// Fill and generate
vector<int> vec2(10);
fill(vec2.begin(), vec2.end(), 42);  // All elements become 42
```

## 🎮 Practical Examples

### Example 1: Complete Sorting Demonstration
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

struct Student {
    string name;
    int score;
};

bool compareByScore(const Student& a, const Student& b) {
    return a.score > b.score;  // Descending order
}

int main() {
    // Basic sorting
    vector<int> numbers = {5, 2, 8, 1, 9, 3};
    sort(numbers.begin(), numbers.end());
    
    cout << "Sorted numbers: ";
    for (int num : numbers) {
        cout << num << " ";
    }
    cout << endl;
    
    // Sorting custom objects
    vector<Student> students = {
        {"Alice", 85},
        {"Bob", 92},
        {"Charlie", 78},
        {"Diana", 88}
    };
    
    sort(students.begin(), students.end(), compareByScore);
    
    cout << "Students by score (descending):" << endl;
    for (const Student& s : students) {
        cout << s.name << ": " << s.score << endl;
    }
    
    // Partial sort
    vector<int> large_vec = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    partial_sort(large_vec.begin(), large_vec.begin() + 3, large_vec.end());
    
    cout << "Top 3 elements: ";
    for (int i = 0; i < 3; i++) {
        cout << large_vec[i] << " ";
    }
    cout << endl;
    
    return 0;
}
```

### Example 2: Searching and Counting
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

int main() {
    vector<string> words = {"apple", "banana", "cherry", "date", "elderberry"};
    
    // Find specific element
    auto it = find(words.begin(), words.end(), "cherry");
    if (it != words.end()) {
        cout << "Found 'cherry' at position: " << distance(words.begin(), it) << endl;
    }
    
    // Find first element matching condition
    auto long_word = find_if(words.begin(), words.end(),
                           [](const string& s) { return s.length() > 6; });
    if (long_word != words.end()) {
        cout << "First long word: " << *long_word << endl;
    }
    
    // Count occurrences
    vector<int> numbers = {1, 2, 3, 2, 4, 2, 5};
    int count_twos = count(numbers.begin(), numbers.end(), 2);
    cout << "Number of 2s: " << count_twos << endl;
    
    // Count elements matching condition
    int even_count = count_if(numbers.begin(), numbers.end(),
                             [](int x) { return x % 2 == 0; });
    cout << "Number of even elements: " << even_count << endl;
    
    // Check if all elements satisfy condition
    bool all_positive = all_of(numbers.begin(), numbers.end(),
                              [](int x) { return x > 0; });
    cout << "All elements positive: " << (all_positive ? "Yes" : "No") << endl;
    
    return 0;
}
```

### Example 3: Modifying and Transforming
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    vector<int> original = {1, 2, 3, 4, 5};
    vector<int> result;
    
    // Copy
    copy(original.begin(), original.end(), back_inserter(result));
    
    // Transform elements
    vector<int> doubled;
    transform(original.begin(), original.end(), back_inserter(doubled),
              [](int x) { return x * 2; });
    
    cout << "Original: ";
    for (int x : original) cout << x << " ";
    cout << endl;
    
    cout << "Doubled: ";
    for (int x : doubled) cout << x << " ";
    cout << endl;
    
    // Remove elements
    vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    // Remove even numbers (erase-remove idiom)
    numbers.erase(remove_if(numbers.begin(), numbers.end(),
                          [](int x) { return x % 2 == 0; }),
                 numbers.end());
    
    cout << "After removing evens: ";
    for (int x : numbers) cout << x << " ";
    cout << endl;
    
    // Replace elements
    vector<int> data = {1, 2, 3, 2, 4, 2, 5};
    replace(data.begin(), data.end(), 2, 99);
    
    cout << "After replacing 2 with 99: ";
    for (int x : data) cout << x << " ";
    cout << endl;
    
    return 0;
}
```

### Example 4: Set Operations and Binary Search
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    // Sorted vectors for set operations
    vector<int> set1 = {1, 3, 5, 7, 9};
    vector<int> set2 = {3, 4, 5, 6, 7};
    
    vector<int> intersection;
    set_intersection(set1.begin(), set1.end(),
                    set2.begin(), set2.end(),
                    back_inserter(intersection));
    
    cout << "Intersection: ";
    for (int x : intersection) cout << x << " ";
    cout << endl;
    
    vector<int> union_set;
    set_union(set1.begin(), set1.end(),
             set2.begin(), set2.end(),
             back_inserter(union_set));
    
    cout << "Union: ";
    for (int x : union_set) cout << x << " ";
    cout << endl;
    
    vector<int> difference;
    set_difference(set1.begin(), set1.end(),
                  set2.begin(), set2.end(),
                  back_inserter(difference));
    
    cout << "Difference (set1 - set2): ";
    for (int x : difference) cout << x << " ";
    cout << endl;
    
    // Binary search operations
    vector<int> sorted = {1, 3, 5, 7, 9, 11, 13};
    int target = 7;
    
    if (binary_search(sorted.begin(), sorted.end(), target)) {
        cout << target << " found in the sorted array" << endl;
        
        auto lower = lower_bound(sorted.begin(), sorted.end(), target);
        auto upper = upper_bound(sorted.begin(), sorted.end(), target);
        
        cout << "First position: " << distance(sorted.begin(), lower) << endl;
        cout << "Last position: " << distance(sorted.begin(), upper - 1) << endl;
    }
    
    return 0;
}
```

## ⚡ Performance Considerations

### Time Complexity of Common Algorithms
| Algorithm | Time Complexity | Notes |
|-----------|-----------------|-------|
| `sort` | O(n log n) | Introsort (quick + heap + insertion) |
| `find` | O(n) | Linear search |
| `binary_search` | O(log n) | Requires sorted data |
| `lower_bound/upper_bound` | O(log n) | Requires sorted data |
| `reverse` | O(n) | In-place reversal |
| `rotate` | O(n) | In-place rotation |
| `nth_element` | O(n) average | Partial sorting |

### Choosing the Right Algorithm
```cpp
vector<int> data = {5, 2, 8, 1, 9, 3};

// For completely sorting
sort(data.begin(), data.end());

// For finding top k elements
nth_element(data.begin(), data.begin() + k, data.end());
// First k elements are the k smallest, but not sorted

// For checking existence in sorted data
if (binary_search(data.begin(), data.end(), target)) { /* ... */ }

// For finding range in sorted data
auto range = equal_range(data.begin(), data.end(), target);
```

## 🎯 Common Algorithm Patterns

### Pattern 1: Remove-Remove Idiom
```cpp
// Remove all elements matching a condition
vector<int> vec = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

vec.erase(remove_if(vec.begin(), vec.end(),
                   [](int x) { return x % 2 == 0; }),  // Remove evens
          vec.end());
```

### Pattern 2: Custom Comparator
```cpp
// Sort by multiple criteria
struct Person {
    string name;
    int age;
    double score;
};

vector<Person> people = {/* ... */};

sort(people.begin(), people.end(),
     [](const Person& a, const Person& b) {
         if (a.score != b.score) return a.score > b.score;
         return a.age < b.age;
     });
```

### Pattern 3: Efficient Copying
```cpp
vector<int> source = {1, 2, 3, 4, 5};
vector<int> dest;

// Reserve space first for efficiency
dest.reserve(source.size());
copy(source.begin(), source.end(), back_inserter(dest));
```

## 🐛 Common Pitfalls & Solutions

### 1. Using `find` on Sorted Data
```cpp
// Inefficient
vector<int> sorted = {1, 3, 5, 7, 9};
auto it = find(sorted.begin(), sorted.end(), 7);  // O(n)

// Efficient
auto it = lower_bound(sorted.begin(), sorted.end(), 7);  // O(log n)
```

### 2. Not Sorting Before Binary Search
```cpp
vector<int> data = {5, 2, 8, 1, 9};
// binary_search(data.begin(), data.end(), 5);  // Undefined behavior!

sort(data.begin(), data.end());
binary_search(data.begin(), data.end(), 5);  // Now it works
```

### 3. Iterator Invalidation
```cpp
vector<int> vec = {1, 2, 3, 4, 5};

// Problem
for (auto it = vec.begin(); it != vec.end(); it++) {
    if (*it % 2 == 0) {
        vec.erase(it);  // Iterator becomes invalid!
    }
}

// Solution
for (auto it = vec.begin(); it != vec.end(); ) {
    if (*it % 2 == 0) {
        it = vec.erase(it);  // Update iterator
    } else {
        it++;
    }
}
```

## 🎨 Advanced Techniques

### Custom Predicates and Functors
```cpp
// Complex condition
auto is_prime = [](int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
};

vector<int> numbers = {2, 3, 4, 5, 6, 7, 8, 9, 10};
auto prime_it = find_if(numbers.begin(), numbers.end(), is_prime);
```

### Chaining Operations
```cpp
vector<int> data = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

// Square all numbers, then filter evens, then sort
vector<int> result;
transform(data.begin(), data.end(), back_inserter(result),
          [](int x) { return x * x; });

result.erase(remove_if(result.begin(), result.end(),
                      [](int x) { return x % 2 != 0; }),
            result.end());

sort(result.begin(), result.end());
```

## 📚 Related Headers

- [`numeric.md`](numeric.md) - Numeric operations
- [`iterator.md`](iterator.md) - Iterator utilities
- [`functional.md`](functional.md) - Function objects

## 🚀 Best Practices

1. **Choose the right algorithm** for the data (sorted vs unsorted)
2. **Use binary search** on sorted data instead of linear search
3. **Master the erase-remove idiom** for filtering
4. **Prefer STL algorithms** over manual loops
5. **Understand iterator invalidation** when modifying containers
6. **Use appropriate comparators** for custom sorting

## 🎯 Algorithm Selection Guide

| Task | Algorithm | Data Requirement |
|------|-----------|------------------|
| Sort entire container | `sort` | Any |
| Find top k elements | `partial_sort` | Any |
| Find kth element | `nth_element` | Any |
| Search for element | `binary_search` | Sorted |
| Find insertion point | `lower_bound` | Sorted |
| Remove elements | `erase-remove` | Any |
| Transform elements | `transform` | Any |
| Copy elements | `copy` | Any |
---

## Next Step

- Go to [05_cmath.md](05_cmath.md) to continue with cmath.
