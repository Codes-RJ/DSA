# C++ Basic Data Structures

## Overview

C++ provides a rich set of built-in data structures and the Standard Template Library (STL) offers powerful container classes. Understanding these fundamental data structures is essential for efficient algorithm implementation and problem-solving.

## Built-in Data Structures

### Arrays

#### Static Arrays
```cpp
#include <iostream>
#include <array>    // For std::array (C++11)

void demonstrateStaticArrays() {
    // C-style arrays
    int c_array[5] = {1, 2, 3, 4, 5};
    char char_array[] = "Hello";  // Null-terminated string
    
    // std::array (C++11) - safer alternative
    std::array<int, 5> modern_array = {1, 2, 3, 4, 5};
    
    // Access elements
    std::cout << "C-array[2]: " << c_array[2] << "\n";
    std::cout << "std::array[2]: " << modern_array[2] << "\n";
    
    // Size information
    std::cout << "C-array size: " << sizeof(c_array) / sizeof(c_array[0]) << "\n";
    std::cout << "std::array size: " << modern_array.size() << "\n";
    
    // Bounds checking with .at() (throws exception if out of bounds)
    try {
        std::cout << "Safe access: " << modern_array.at(2) << "\n";
        // std::cout << modern_array.at(10) << "\n"; // Throws exception
    } catch (const std::out_of_range& e) {
        std::cout << "Out of range: " << e.what() << "\n";
    }
}
```

#### Dynamic Arrays
```cpp
#include <iostream>
#include <vector>

void demonstrateDynamicArrays() {
    // std::vector - dynamic array
    std::vector<int> numbers;
    
    // Add elements
    numbers.push_back(10);
    numbers.push_back(20);
    numbers.push_back(30);
    
    // Initialize with values
    std::vector<int> more_numbers = {1, 2, 3, 4, 5};
    std::vector<int> sized_vector(10, 0);  // 10 elements, all 0
    
    // Access elements
    std::cout << "First element: " << numbers[0] << "\n";
    std::cout << "Last element: " << numbers.back() << "\n";
    
    // Iterator access
    for (auto it = numbers.begin(); it != numbers.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    // Range-based for loop (C++11)
    for (const auto& num : numbers) {
        std::cout << num << " ";
    }
    std::cout << "\n";
    
    // Size and capacity
    std::cout << "Size: " << numbers.size() << "\n";
    std::cout << "Capacity: " << numbers.capacity() << "\n";
    
    // Reserve capacity for efficiency
    numbers.reserve(100);
    std::cout << "New capacity: " << numbers.capacity() << "\n";
}
```

### Strings

#### C-style Strings
```cpp
#include <iostream>
#include <cstring>  // For C-string functions

void demonstrateCStrings() {
    // C-style strings (character arrays)
    char greeting[] = "Hello";
    char name[20];
    
    // Safe string copy
    strcpy_s(name, sizeof(name), "World");  // Windows
    // strcpy(name, "World");  // Cross-platform
    
    // String concatenation
    char combined[50];
    strcpy_s(combined, sizeof(combined), greeting);
    strcat_s(combined, sizeof(combined), ", ");
    strcat_s(combined, sizeof(combined), name);
    
    std::cout << "Combined: " << combined << "\n";
    
    // String length
    std::cout << "Length: " << strlen(combined) << "\n";
    
    // String comparison
    if (strcmp(greeting, "Hello") == 0) {
        std::cout << "Strings are equal\n";
    }
}
```

#### std::string
```cpp
#include <iostream>
#include <string>

void demonstrateStdString() {
    // String creation
    std::string greeting = "Hello";
    std::string name = "World";
    std::string combined = greeting + ", " + name + "!";
    
    std::cout << "Combined: " << combined << "\n";
    
    // String methods
    std::cout << "Length: " << combined.length() << "\n";
    std::cout << "Size: " << combined.size() << "\n";
    std::cout << "Empty: " << combined.empty() << "\n";
    
    // Substring
    std::string sub = combined.substr(0, 5);
    std::cout << "Substring: " << sub << "\n";
    
    // Find and replace
    size_t pos = combined.find("World");
    if (pos != std::string::npos) {
        combined.replace(pos, 5, "C++");
        std::cout << "Replaced: " << combined << "\n";
    }
    
    // Character access
    std::cout << "First char: " << combined[0] << "\n";
    std::cout << "Last char: " << combined.back() << "\n";
    
    // String to number conversion
    std::string number_str = "42";
    int number = std::stoi(number_str);
    std::cout << "Number: " << number << "\n";
    
    // Number to string
    std::string pi_str = std::to_string(3.14159);
    std::cout << "PI string: " << pi_str << "\n";
}
```

## STL Containers

### Sequence Containers

#### std::vector
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

void demonstrateVector() {
    // Vector with different initialization methods
    std::vector<int> vec1 = {1, 2, 3, 4, 5};
    std::vector<int> vec2(10, 0);  // 10 zeros
    std::vector<int> vec3(vec1.begin(), vec1.end());  // Copy from iterator range
    
    // Common operations
    vec1.push_back(6);           // Add to end
    vec1.insert(vec1.begin(), 0); // Insert at beginning
    vec1.pop_back();             // Remove last element
    vec1.erase(vec1.begin());    // Remove first element
    
    // Access elements
    std::cout << "Element at index 2: " << vec1[2] << "\n";
    std::cout << "Front: " << vec1.front() << "\n";
    std::cout << "Back: " << vec1.back() << "\n";
    
    // Iteration
    std::cout << "Using iterators: ";
    for (auto it = vec1.begin(); it != vec1.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    // Range-based for loop
    std::cout << "Range-based: ";
    for (const auto& elem : vec1) {
        std::cout << elem << " ";
    }
    std::cout << "\n";
    
    // Algorithms
    std::sort(vec1.begin(), vec1.end());
    std::reverse(vec1.begin(), vec1.end());
    
    // Check if element exists
    auto find_it = std::find(vec1.begin(), vec1.end(), 3);
    if (find_it != vec1.end()) {
        std::cout << "Found element 3\n";
    }
}
```

#### std::deque
```cpp
#include <iostream>
#include <deque>

void demonstrateDeque() {
    // Double-ended queue
    std::deque<int> dq;
    
    // Add elements at both ends
    dq.push_back(10);  // Add to back
    dq.push_front(5);  // Add to front
    dq.push_back(15);
    dq.push_front(0);
    
    std::cout << "Deque elements: ";
    for (const auto& elem : dq) {
        std::cout << elem << " ";
    }
    std::cout << "\n";
    
    // Remove from both ends
    dq.pop_front();  // Remove from front
    dq.pop_back();   // Remove from back
    
    // Random access (like vector)
    std::cout << "Element at index 1: " << dq[1] << "\n";
    
    // Insert in the middle
    dq.insert(dq.begin() + 1, 7);
    
    std::cout << "After insertion: ";
    for (const auto& elem : dq) {
        std::cout << elem << " ";
    }
    std::cout << "\n";
}
```

#### std::list
```cpp
#include <iostream>
#include <list>

void demonstrateList() {
    // Doubly-linked list
    std::list<int> lst = {1, 2, 3, 4, 5};
    
    // Add elements
    lst.push_front(0);    // Add to front
    lst.push_back(6);     // Add to back
    
    // Insert at specific position
    auto it = lst.begin();
    std::advance(it, 3);  // Move iterator to position 3
    lst.insert(it, 99);   // Insert 99 at position 3
    
    std::cout << "List elements: ";
    for (const auto& elem : lst) {
        std::cout << elem << " ";
    }
    std::cout << "\n";
    
    // Remove elements
    lst.remove(99);       // Remove all occurrences of 99
    lst.pop_front();      // Remove first element
    lst.pop_back();       // Remove last element
    
    // Remove based on condition
    lst.remove_if([](int x) { return x % 2 == 0; }); // Remove even numbers
    
    std::cout << "After removals: ";
    for (const auto& elem : lst) {
        std::cout << elem << " ";
    }
    std::cout << "\n";
    
    // Splice (move elements from one list to another)
    std::list<int> source = {10, 20, 30};
    lst.splice(lst.begin(), source);  // Move all elements from source to lst
    
    std::cout << "After splice: ";
    for (const auto& elem : lst) {
        std::cout << elem << " ";
    }
    std::cout << "\n";
}
```

#### std::forward_list
```cpp
#include <iostream>
#include <forward_list>

void demonstrateForwardList() {
    // Singly-linked list (C++11)
    std::forward_list<int> flist = {1, 2, 3, 4, 5};
    
    // Add elements
    flist.push_front(0);  // Only push_front, no push_back
    
    // Insert after position
    auto it = flist.begin();
    std::advance(it, 2);
    flist.insert_after(it, 99);
    
    std::cout << "Forward list: ";
    for (const auto& elem : flist) {
        std::cout << elem << " ";
    }
    std::cout << "\n";
    
    // Remove elements
    flist.pop_front();  // Remove first element
    
    // Remove after position
    it = flist.begin();
    flist.erase_after(it);
    
    std::cout << "After operations: ";
    for (const auto& elem : flist) {
        std::cout << elem << " ";
    }
    std::cout << "\n";
}
```

### Associative Containers

#### std::map
```cpp
#include <iostream>
#include <map>
#include <string>

void demonstrateMap() {
    // Ordered key-value pairs (sorted by key)
    std::map<std::string, int> scores;
    
    // Insert elements
    scores["Alice"] = 95;
    scores["Bob"] = 87;
    scores["Charlie"] = 92;
    
    // Alternative insertion methods
    scores.insert({"David", 88});
    scores.insert(std::make_pair("Eve", 91));
    
    // Access elements
    std::cout << "Alice's score: " << scores["Alice"] << "\n";
    
    // Safe access (doesn't create element if not found)
    auto it = scores.find("Bob");
    if (it != scores.end()) {
        std::cout << "Bob's score: " << it->second << "\n";
    }
    
    // Check existence
    if (scores.count("Frank") > 0) {
        std::cout << "Frank exists\n";
    } else {
        std::cout << "Frank doesn't exist\n";
    }
    
    // Iterate over map
    std::cout << "All scores:\n";
    for (const auto& [name, score] : scores) {  // C++17 structured binding
        std::cout << name << ": " << score << "\n";
    }
    
    // Size and operations
    std::cout << "Map size: " << scores.size() << "\n";
    scores.erase("Charlie");
    std::cout << "After erase: " << scores.size() << "\n";
    
    // Clear all elements
    scores.clear();
    std::cout << "After clear: " << scores.size() << "\n";
}
```

#### std::unordered_map
```cpp
#include <iostream>
#include <unordered_map>
#include <string>

void demonstrateUnorderedMap() {
    // Hash table - faster than map but unordered
    std::unordered_map<std::string, int> cache;
    
    // Insert elements
    cache["user1"] = 1001;
    cache["user2"] = 1002;
    cache["user3"] = 1003;
    
    // Access (average O(1) time complexity)
    std::cout << "user2 ID: " << cache["user2"] << "\n";
    
    // Bucket information (for understanding hash distribution)
    std::cout << "Bucket count: " << cache.bucket_count() << "\n";
    std::cout << "Load factor: " << cache.load_factor() << "\n";
    
    // Iterate (order is not guaranteed)
    std::cout << "Cache contents:\n";
    for (const auto& [user, id] : cache) {
        std::cout << user << ": " << id << "\n";
    }
}
```

#### std::set
```cpp
#include <iostream>
#include <set>

void demonstrateSet() {
    // Ordered unique elements
    std::set<int> numbers;
    
    // Insert elements (duplicates are ignored)
    numbers.insert(5);
    numbers.insert(3);
    numbers.insert(8);
    numbers.insert(3);  // Duplicate, won't be inserted
    numbers.insert(1);
    
    std::cout << "Set elements: ";
    for (const auto& num : numbers) {
        std::cout << num << " ";
    }
    std::cout << "\n";
    
    // Check existence
    if (numbers.count(3)) {
        std::cout << "3 exists in the set\n";
    }
    
    // Find element
    auto it = numbers.find(8);
    if (it != numbers.end()) {
        std::cout << "Found 8\n";
    }
    
    // Remove element
    numbers.erase(3);
    
    std::cout << "After removing 3: ";
    for (const auto& num : numbers) {
        std::cout << num << " ";
    }
    std::cout << "\n";
    
    // Set operations
    std::set<int> set1 = {1, 2, 3, 4, 5};
    std::set<int> set2 = {4, 5, 6, 7, 8};
    
    std::set<int> intersection;
    std::set_intersection(set1.begin(), set1.end(),
                          set2.begin(), set2.end(),
                          std::inserter(intersection, intersection.begin()));
    
    std::cout << "Intersection: ";
    for (const auto& num : intersection) {
        std::cout << num << " ";
    }
    std::cout << "\n";
}
```

#### std::unordered_set
```cpp
#include <iostream>
#include <unordered_set>

void demonstrateUnorderedSet() {
    // Hash-based unique elements
    std::unordered_set<std::string> unique_words;
    
    // Insert elements
    unique_words.insert("hello");
    unique_words.insert("world");
    unique_words.insert("hello");  // Duplicate, ignored
    unique_words.insert("c++");
    
    std::cout << "Unique words: ";
    for (const auto& word : unique_words) {
        std::cout << word << " ";
    }
    std::cout << "\n";
    
    // Fast membership testing
    std::string test_word = "hello";
    if (unique_words.find(test_word) != unique_words.end()) {
        std::cout << test_word << " exists\n";
    }
}
```

### Container Adapters

#### std::stack
```cpp
#include <iostream>
#include <stack>
#include <vector>

void demonstrateStack() {
    // LIFO (Last In, First Out)
    std::stack<int> stk;
    
    // Push elements
    stk.push(10);
    stk.push(20);
    stk.push(30);
    
    std::cout << "Top element: " << stk.top() << "\n";
    std::cout << "Stack size: " << stk.size() << "\n";
    
    // Pop elements
    while (!stk.empty()) {
        std::cout << "Popping: " << stk.top() << "\n";
        stk.pop();
    }
    
    // Stack with different underlying container
    std::stack<int, std::vector<int>> vector_stack;
    vector_stack.push(1);
    vector_stack.push(2);
}
```

#### std::queue
```cpp
#include <iostream>
#include <queue>

void demonstrateQueue() {
    // FIFO (First In, First Out)
    std::queue<int> q;
    
    // Enqueue elements
    q.push(10);
    q.push(20);
    q.push(30);
    
    std::cout << "Front element: " << q.front() << "\n";
    std::cout << "Back element: " << q.back() << "\n";
    std::cout << "Queue size: " << q.size() << "\n";
    
    // Dequeue elements
    while (!q.empty()) {
        std::cout << "Dequeuing: " << q.front() << "\n";
        q.pop();
    }
}
```

#### std::priority_queue
```cpp
#include <iostream>
#include <queue>
#include <vector>

void demonstratePriorityQueue() {
    // Max-heap by default
    std::priority_queue<int> pq;
    
    // Insert elements
    pq.push(30);
    pq.push(10);
    pq.push(50);
    pq.push(20);
    
    std::cout << "Priority queue (max-heap):\n";
    while (!pq.empty()) {
        std::cout << pq.top() << " ";  // Always the largest element
        pq.pop();
    }
    std::cout << "\n";
    
    // Min-heap using custom comparator
    std::priority_queue<int, std::vector<int>, std::greater<int>> min_pq;
    min_pq.push(30);
    min_pq.push(10);
    min_pq.push(50);
    min_pq.push(20);
    
    std::cout << "Priority queue (min-heap):\n";
    while (!min_pq.empty()) {
        std::cout << min_pq.top() << " ";  // Always the smallest element
        min_pq.pop();
    }
    std::cout << "\n";
}
```

## Advanced Data Structures

### std::pair
```cpp
#include <iostream>
#include <utility>
#include <string>

void demonstratePair() {
    // Pair of values
    std::pair<std::string, int> student("Alice", 95);
    
    // Access elements
    std::cout << "Name: " << student.first << "\n";
    std::cout << "Score: " << student.second << "\n";
    
    // Create pairs
    auto pair1 = std::make_pair("Bob", 87);
    std::pair<std::string, int> pair2 = {"Charlie", 92};  // C++11
    
    // Comparison
    if (student > pair1) {
        std::cout << "Student > pair1\n";
    }
    
    // Structured binding (C++17)
    auto [name, score] = student;
    std::cout << "Structured binding - Name: " << name << ", Score: " << score << "\n";
}
```

### std::tuple
```cpp
#include <iostream>
#include <tuple>
#include <string>

void demonstrateTuple() {
    // Tuple of multiple values
    std::tuple<std::string, int, double, bool> person("Alice", 25, 3.8, true);
    
    // Access elements
    std::cout << "Name: " << std::get<0>(person) << "\n";
    std::cout << "Age: " << std::get<1>(person) << "\n";
    std::cout << "GPA: " << std::get<2>(person) << "\n";
    std::cout << "Employed: " << std::get<3>(person) << "\n";
    
    // Create tuples
    auto tuple1 = std::make_tuple("Bob", 30, 3.5, false);
    
    // Structured binding (C++17)
    auto [name, age, gpa, employed] = person;
    std::cout << "Structured binding - Name: " << name << ", Age: " << age << "\n";
    
    // Tuple operations
    auto tuple2 = std::tuple_cat(person, tuple1);  // Concatenate tuples
    
    // Compare tuples
    if (person == tuple1) {
        std::cout << "Tuples are equal\n";
    }
}
```

### std::optional (C++17)
```cpp
#include <iostream>
#include <optional>
#include <string>

void demonstrateOptional() {
    // Optional value (may or may not contain a value)
    std::optional<int> maybe_value;
    std::optional<std::string> maybe_name = "Alice";
    
    // Check if value exists
    if (maybe_value) {
        std::cout << "Value exists: " << *maybe_value << "\n";
    } else {
        std::cout << "No value\n";
    }
    
    if (maybe_name.has_value()) {
        std::cout << "Name: " << maybe_name.value() << "\n";
    }
    
    // Provide default value
    int result = maybe_value.value_or(0);
    std::cout << "Result with default: " << result << "\n";
    
    // Reset optional
    maybe_name.reset();
    
    if (!maybe_name) {
        std::cout << "Name has been reset\n";
    }
}
```

### std::variant (C++17)
```cpp
#include <iostream>
#include <variant>
#include <string>

void demonstrateVariant() {
    // Type-safe union
    std::variant<int, double, std::string> value;
    
    // Assign different types
    value = 42;
    std::cout << "Holds int: " << std::get<int>(value) << "\n";
    
    value = 3.14;
    std::cout << "Holds double: " << std::get<double>(value) << "\n";
    
    value = "Hello";
    std::cout << "Holds string: " << std::get<std::string>(value) << "\n";
    
    // Safe access with get_if
    if (auto int_ptr = std::get_if<int>(&value)) {
        std::cout << "Contains int: " << *int_ptr << "\n";
    } else if (auto str_ptr = std::get_if<std::string>(&value)) {
        std::cout << "Contains string: " << *str_ptr << "\n";
    }
    
    // Visit variant
    std::visit([](auto&& arg) {
        std::cout << "Visited value: " << arg << "\n";
    }, value);
}
```

## Performance Considerations

### Time Complexity Summary
```cpp
#include <iostream>

void complexitySummary() {
    std::cout << "=== Time Complexity Summary ===\n";
    std::cout << "std::vector:\n";
    std::cout << "  Access: O(1)\n";
    std::cout << "  Push back: O(1) amortized\n";
    std::cout << "  Insert: O(n)\n";
    std::cout << "  Delete: O(n)\n";
    std::cout << "  Search: O(n)\n\n";
    
    std::cout << "std::deque:\n";
    std::cout << "  Access: O(1)\n";
    std::cout << "  Push front/back: O(1)\n";
    std::cout << "  Insert: O(n)\n";
    std::cout << "  Delete: O(n)\n\n";
    
    std::cout << "std::list:\n";
    std::cout << "  Access: O(n)\n";
    std::cout << "  Push front/back: O(1)\n";
    std::cout << "  Insert: O(1) (with iterator)\n";
    std::cout << "  Delete: O(1) (with iterator)\n";
    std::cout << "  Search: O(n)\n\n";
    
    std::cout << "std::map:\n";
    std::cout << "  Access: O(log n)\n";
    std::cout << "  Insert: O(log n)\n";
    std::cout << "  Delete: O(log n)\n";
    std::cout << "  Search: O(log n)\n\n";
    
    std::cout << "std::unordered_map:\n";
    std::cout << "  Access: O(1) average\n";
    std::cout << "  Insert: O(1) average\n";
    std::cout << "  Delete: O(1) average\n";
    std::cout << "  Search: O(1) average\n\n";
}
```

## Choosing the Right Container

### Decision Guidelines
```cpp
#include <iostream>

void containerSelectionGuide() {
    std::cout << "=== Container Selection Guide ===\n\n";
    
    std::cout << "Use std::vector when:\n";
    std::cout << "- You need random access\n";
    std::cout << "- Elements are stored contiguously\n";
    std::cout << "- You mostly add/remove from the end\n";
    std::cout << "- Cache performance is important\n\n";
    
    std::cout << "Use std::deque when:\n";
    std::cout << "- You need fast insertion at both ends\n";
    std::cout << "- You need random access\n";
    std::cout << "- Elements don't need to be contiguous\n\n";
    
    std::cout << "Use std::list when:\n";
    std::cout << "- You need frequent insertions/deletions in the middle\n";
    std::cout << "- Random access is not required\n";
    std::cout << "- Iterator validity is important\n\n";
    
    std::cout << "Use std::map when:\n";
    std::cout << "- You need ordered key-value pairs\n";
    std::cout << "- You need range queries\n";
    std::cout << "- Logarithmic performance is acceptable\n\n";
    
    std::cout << "Use std::unordered_map when:\n";
    std::cout << "- You need fast key-value lookup\n";
    std::cout << "- Order doesn't matter\n";
    std::cout << "- Average O(1) performance is needed\n\n";
    
    std::cout << "Use std::set when:\n";
    std::cout << "- You need unique, ordered elements\n";
    std::cout << "- You need fast membership testing\n";
    std::cout << "- You need set operations\n\n";
}
```

## Best Practices

1. **Prefer std::vector** over C-style arrays for safety and functionality
2. **Use std::string** instead of char* for string handling
3. **Choose containers based on usage patterns**, not just convenience
4. **Use reserve()** with vectors when you know the size in advance
5. **Prefer std::unordered_map** over std::map for performance when order doesn't matter
6. **Use appropriate iterator types** (const_iterator when not modifying)
7. **Be aware of iterator invalidation** when modifying containers
8. **Use range-based for loops** for cleaner iteration
9. **Consider move semantics** for efficient container operations
10. **Use structured bindings** (C++17) for cleaner tuple/pair access

## Conclusion

C++ provides a comprehensive set of data structures through both built-in types and the STL. Understanding the characteristics, performance implications, and appropriate use cases for each container is essential for writing efficient and maintainable code. Modern C++ continues to enhance these data structures with new features and improved safety.
