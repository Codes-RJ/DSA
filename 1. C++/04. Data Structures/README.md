# README.md

## Data Structures in C++ - Complete Guide

### Overview

Data structures are specialized formats for organizing, processing, and storing data in computer memory. They provide efficient ways to access and manipulate data, forming the foundation of algorithms and software design. Understanding data structures is essential for writing efficient programs and acing technical interviews.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [00_Basic_Data_Structures_Indexes.md](00_Basic_Data_Structures_Indexes.md) | understand Data Structures Index and Navigation |
| 2. | [01_Array.md](01_Array.md) | understand Array Data Structure |
| 3. | [02_String.md](02_String.md) | understand String Data Structure |
| 4. | [03_Sequence_Container.md](03_Sequence_Container.md) | understand Sequence Containers (vector, list, deque) |
| 5. | [04_Container_Adapters.md](04_Container_Adapters.md) | understand Container Adapters (stack, queue, priority_queue) |
| 6. | [05_Associative_Container.md](05_Associative_Container.md) | understand Associative Containers (set, map, multiset, multimap) |
| 7. | [06_Unassociative_Container.md](06_Unassociative_Container.md) | understand Unordered Associative Containers (unordered_set, unordered_map) |
| 8. | [07_Utility.md](07_Utility.md) | understand Utility Components (pair, tuple) |
| 9. | [08_SpecializedContainers.md](08_SpecializedContainers.md) | understand Specialized Containers (bitset, valarray) |
| 10. | [Theory.md](Theory.md) | understand Theoretical Foundations of Data Structures |

---

## 1. Array

This topic explains the fundamental array data structure for storing fixed-size sequential collections.

**File:** [01_Array.md](01_Array.md)

**What you will learn:**
- What are arrays (fixed-size, contiguous memory)
- Array declaration and initialization
- Accessing elements using indices (0-based indexing)
- Multi-dimensional arrays
- Array bounds and safety issues
- Passing arrays to functions
- C-style arrays vs std::array (C++11)

**Key Concepts:**

| Concept | Description | Example |
|---------|-------------|---------|
| **Contiguous Memory** | Elements stored in consecutive memory locations | `int arr[5];` |
| **Random Access** | Access any element in O(1) time | `arr[i]` |
| **Fixed Size** | Size determined at compile time | `int arr[10];` |
| **Zero-Based Index** | First element at index 0 | `arr[0]` |

**Syntax:**
```cpp
// C-style array
int arr1[5];                    // Uninitialized
int arr2[5] = {1, 2, 3, 4, 5}; // Initialized
int arr3[] = {1, 2, 3};        // Size deduced

// std::array (C++11)
#include <array>
array<int, 5> arr4 = {1, 2, 3, 4, 5};
arr4[0] = 10;
int value = arr4.at(2);  // Bounds checking
```

---

## 2. String

This topic explains string handling in C++, including C-style strings and std::string.

**File:** [02_String.md](02_String.md)

**What you will learn:**
- C-style strings (character arrays)
- String functions (strlen, strcpy, strcat, strcmp)
- std::string class (dynamic strings)
- String operations (concatenation, comparison, substring)
- String searching and manipulation
- String streams for parsing

**Key Concepts:**

| Concept | Description | Example |
|---------|-------------|---------|
| **C-String** | Null-terminated character array | `char str[] = "Hello";` |
| **std::string** | Dynamic string class | `string s = "Hello";` |
| **Null Terminator** | `'\0'` marks end of C-string | |
| **String Operations** | Concatenation, comparison, search | `s1 + s2`, `s1 == s2` |

**Syntax:**
```cpp
// C-style strings
char cstr[] = "Hello";
strlen(cstr);    // Length (excludes '\0')
strcpy(dest, src); // Copy
strcat(dest, src); // Concatenate
strcmp(s1, s2);    // Compare

// std::string
#include <string>
string s1 = "Hello";
string s2 = "World";
string s3 = s1 + " " + s2;  // Concatenation
int len = s1.length();       // Length
char ch = s1[0];             // Access
string sub = s1.substr(1, 3); // Substring
```

---

## 3. Sequence Containers

This topic explains STL sequence containers: vector, list, and deque.

**File:** [03_Sequence_Container.md](03_Sequence_Container.md)

**What you will learn:**
- `vector` - Dynamic array (contiguous, fast random access)
- `list` - Doubly linked list (fast insert/delete anywhere)
- `deque` - Double-ended queue (fast insert/delete at ends)
- `array` - Fixed-size array wrapper (C++11)
- `forward_list` - Singly linked list (C++11)
- Container operations and complexity

**Key Concepts:**

| Container | Memory Layout | Random Access | Insert/Delete | Use Case |
|-----------|---------------|---------------|---------------|----------|
| **vector** | Contiguous | O(1) | O(n) at ends, O(n) middle | General purpose |
| **list** | Non-contiguous | O(n) | O(1) (given iterator) | Frequent insert/delete |
| **deque** | Blocks | O(1) | O(1) at ends, O(n) middle | Queue operations |

**Syntax:**
```cpp
#include <vector>
#include <list>
#include <deque>

// vector - dynamic array
vector<int> vec = {1, 2, 3, 4, 5};
vec.push_back(6);        // Add at end
vec.pop_back();          // Remove from end
vec.insert(vec.begin(), 0); // Insert at beginning
int x = vec[2];          // Random access

// list - doubly linked list
list<int> lst = {1, 2, 3};
lst.push_front(0);       // Add at front
lst.push_back(4);        // Add at back
lst.pop_front();         // Remove from front

// deque - double-ended queue
deque<int> dq = {1, 2, 3};
dq.push_front(0);        // Add at front
dq.push_back(4);         // Add at back
```

---

## 4. Container Adapters

This topic explains container adapters that provide restricted interfaces: stack, queue, and priority_queue.

**File:** [04_Container_Adapters.md](04_Container_Adapters.md)

**What you will learn:**
- `stack` - LIFO (Last-In-First-Out) container
- `queue` - FIFO (First-In-First-Out) container
- `priority_queue` - Element with highest priority first
- Underlying containers (deque, vector, list)
- Operations (push, pop, top, front, back)

**Key Concepts:**

| Adapter | Principle | Operations | Use Case |
|---------|-----------|------------|----------|
| **stack** | LIFO | push, pop, top | Undo/Redo, expression evaluation |
| **queue** | FIFO | push, pop, front, back | Task scheduling, BFS |
| **priority_queue** | Priority | push, pop, top | Dijkstra, Huffman coding |

**Syntax:**
```cpp
#include <stack>
#include <queue>

// Stack
stack<int> st;
st.push(10);     // Add element
st.push(20);
int top = st.top();  // Access top (20)
st.pop();        // Remove top

// Queue
queue<int> q;
q.push(10);      // Add to back
q.push(20);
int front = q.front(); // Access front (10)
q.pop();         // Remove front

// Priority Queue (max-heap by default)
priority_queue<int> pq;
pq.push(10);
pq.push(30);
pq.push(20);
int max = pq.top();  // 30
pq.pop();

// Min-heap priority queue
priority_queue<int, vector<int>, greater<int>> minHeap;
```

---

## 5. Associative Containers

This topic explains ordered associative containers: set, map, multiset, multimap.

**File:** [05_Associative_Container.md](05_Associative_Container.md)

**What you will learn:**
- `set` - Unique keys, sorted order
- `map` - Key-value pairs, unique keys, sorted by key
- `multiset` - Multiple equal keys allowed
- `multimap` - Multiple equal keys allowed in key-value pairs
- Red-Black tree implementation
- Binary search operations (lower_bound, upper_bound, equal_range)

**Key Concepts:**

| Container | Keys Unique | Ordered | Implementation | Use Case |
|-----------|-------------|---------|----------------|----------|
| **set** | Yes | Yes | Red-Black Tree | Unique sorted elements |
| **map** | Yes (key) | Yes | Red-Black Tree | Dictionary, lookup |
| **multiset** | No | Yes | Red-Black Tree | Sorted elements with duplicates |
| **multimap** | No (key) | Yes | Red-Black Tree | Multiple values per key |

**Syntax:**
```cpp
#include <set>
#include <map>

// Set
set<int> s = {3, 1, 4, 1, 5};  // {1, 3, 4, 5}
s.insert(2);                     // {1, 2, 3, 4, 5}
s.erase(3);                      // Remove 3
auto it = s.find(4);             // Find element

// Map
map<string, int> ages;
ages["Alice"] = 25;
ages["Bob"] = 30;
ages.insert({"Charlie", 35});
int age = ages["Alice"];         // 25

// Multiset (allows duplicates)
multiset<int> ms = {1, 2, 2, 3};
ms.count(2);  // 2

// Multimap
multimap<string, int> mm;
mm.insert({"Math", 90});
mm.insert({"Math", 95});
mm.insert({"Science", 85});
```

---

## 6. Unordered Associative Containers

This topic explains unordered associative containers: unordered_set, unordered_map, unordered_multiset, unordered_multimap.

**File:** [06_Unassociative_Container.md](06_Unassociative_Container.md)

**What you will learn:**
- `unordered_set` - Unique keys, hash table implementation
- `unordered_map` - Key-value pairs, hash table
- Hash functions and bucket management
- Average O(1) operations vs ordered O(log n)
- When to use unordered vs ordered containers

**Key Concepts:**

| Container | Keys Unique | Ordered | Implementation | Average Access |
|-----------|-------------|---------|----------------|----------------|
| **unordered_set** | Yes | No | Hash Table | O(1) |
| **unordered_map** | Yes (key) | No | Hash Table | O(1) |
| **unordered_multiset** | No | No | Hash Table | O(1) |
| **unordered_multimap** | No (key) | No | Hash Table | O(1) |

**Syntax:**
```cpp
#include <unordered_set>
#include <unordered_map>

// Unordered Set
unordered_set<int> us = {3, 1, 4, 1, 5};
us.insert(2);
us.erase(3);
auto it = us.find(4);

// Unordered Map
unordered_map<string, int> um;
um["Alice"] = 25;
um["Bob"] = 30;
int age = um["Alice"];  // 25

// Bucket interface
int bucketCount = us.bucket_count();
int bucket = us.bucket(4);
float loadFactor = us.load_factor();
```

**When to Use Which:**

| Criteria | Ordered (set/map) | Unordered (unordered_set/unordered_map) |
|----------|-------------------|------------------------------------------|
| Need sorted order | Yes | No |
| Need range queries | Yes | No |
| Performance requirement | O(log n) | O(1) average |
| Memory usage | Lower | Higher |
| Hash function available | Not needed | Required |

---

## 7. Utility Components

This topic explains utility components: pair and tuple.

**File:** [07_Utility.md](07_Utility.md)

**What you will learn:**
- `pair` - Container for two heterogeneous values
- `tuple` - Container for multiple heterogeneous values (C++11)
- `make_pair` and `make_tuple` functions
- Structured bindings (C++17)
- Comparison operators for pairs and tuples

**Key Concepts:**

| Component | Number of Elements | Access | Use Case |
|-----------|-------------------|--------|----------|
| **pair** | 2 | `.first`, `.second` | Return two values, map elements |
| **tuple** | Any | `std::get<N>` | Multiple return values |

**Syntax:**
```cpp
#include <utility>
#include <tuple>

// Pair
pair<int, string> p1 = {1, "Alice"};
pair<int, string> p2 = make_pair(2, "Bob");
int id = p1.first;
string name = p1.second;

// Tuple
tuple<int, string, double> t1 = {1, "Alice", 3.14};
auto t2 = make_tuple(2, "Bob", 2.71);
int id = get<0>(t1);
string name = get<1>(t1);
double val = get<2>(t1);

// Structured bindings (C++17)
auto [id, name] = p1;
auto [id, name, val] = t1;
```

---

## 8. Specialized Containers

This topic explains specialized containers: bitset and valarray.

**File:** [08_SpecializedContainers.md](08_SpecializedContainers.md)

**What you will learn:**
- `bitset` - Fixed-size sequence of bits
- `valarray` - Numeric array with mathematical operations
- Bitwise operations on bitset
- Mathematical operations on valarray
- Specialized use cases

**Key Concepts:**

| Container | Size | Operations | Use Case |
|-----------|------|------------|----------|
| **bitset** | Fixed (compile-time) | Bitwise, shift, test | Flags, bit manipulation |
| **valarray** | Fixed/Runtime | Element-wise math | Numerical computing |

**Syntax:**
```cpp
#include <bitset>
#include <valarray>

// bitset
bitset<8> bs1("10101010");
bitset<8> bs2(0b11110000);
bs1.set(3);           // Set bit at position 3
bs1.reset(2);         // Clear bit at position 2
bs1.flip(1);          // Toggle bit at position 1
bool b = bs1.test(0); // Test bit 0
string s = bs1.to_string();

// Bitwise operations
bitset<8> bs3 = bs1 & bs2;
bitset<8> bs4 = bs1 | bs2;
bitset<8> bs5 = bs1 ^ bs2;
bitset<8> bs6 = ~bs1;

// valarray
valarray<int> va1 = {1, 2, 3, 4, 5};
valarray<int> va2 = {5, 4, 3, 2, 1};

// Element-wise operations
valarray<int> sum = va1 + va2;     // {6, 6, 6, 6, 6}
valarray<int> product = va1 * va2; // {5, 8, 9, 8, 5}
valarray<int> shifted = va1.shift(2); // {3, 4, 5, 0, 0}
valarray<int> rolled = va1.cshift(1); // {2, 3, 4, 5, 1}
```

---

## 9. Theoretical Foundations

This topic covers the theoretical concepts behind data structures.

**File:** [Theory.md](Theory.md)

**What you will learn:**
- Abstract Data Types (ADTs)
- Time and space complexity analysis
- Container categories (sequence, associative, unordered)
- Iterator categories and usage
- Allocators and memory management
- Container selection guidelines

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Abstract Data Type** | Mathematical model for data types defined by behavior |
| **Complexity** | Time and space requirements as input grows |
| **Iterator** | Object that enables traversal of containers |
| **Allocator** | Memory management policy for containers |

---

### Container Complexity Summary

| Container | Access | Insert | Delete | Search | Memory |
|-----------|--------|--------|--------|--------|--------|
| **array** | O(1) | N/A | N/A | O(n) | Fixed |
| **vector** | O(1) | O(n) (end O(1)) | O(n) (end O(1)) | O(n) | Dynamic |
| **list** | O(n) | O(1)* | O(1)* | O(n) | Per node |
| **deque** | O(1) | O(1) (ends), O(n) (middle) | O(1) (ends), O(n) (middle) | O(n) | Blocked |
| **set/map** | O(log n) | O(log n) | O(log n) | O(log n) | Per node |
| **unordered_set/map** | O(1) avg | O(1) avg | O(1) avg | O(1) avg | Table + nodes |

*Given iterator to position

---

### Container Selection Guide

| Requirement | Recommended Container |
|-------------|----------------------|
| Fixed size, fast random access | `array` |
| Dynamic size, fast random access, insert at end | `vector` |
| Frequent insert/delete anywhere | `list` |
| Fast insert/delete at both ends | `deque` |
| LIFO access | `stack` |
| FIFO access | `queue` |
| Priority-based access | `priority_queue` |
| Unique sorted elements | `set` |
| Key-value pairs, sorted by key | `map` |
| Unique elements, fast lookup | `unordered_set` |
| Key-value pairs, fast lookup | `unordered_map` |

---

### Prerequisites

Before starting this section, you should have completed:

- [01. Basics](../01.%20Basics/README.md) - Arrays, pointers, dynamic memory
- [02. Basic Problems](../02.%20Basic%20Problems/README.md) - Basic problem-solving

---

### Sample Data Structure Usage

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <unordered_set>
#include <stack>
#include <queue>
using namespace std;

int main() {
    // Vector - dynamic array
    vector<int> vec = {1, 2, 3, 4, 5};
    vec.push_back(6);
    for (int x : vec) cout << x << " ";
    cout << endl;
    
    // Map - key-value pairs
    map<string, int> ages;
    ages["Alice"] = 25;
    ages["Bob"] = 30;
    for (auto& [name, age] : ages) {
        cout << name << ": " << age << endl;
    }
    
    // Unordered set - fast lookup
    unordered_set<int> us = {1, 2, 3, 4, 5};
    if (us.find(3) != us.end()) {
        cout << "3 found" << endl;
    }
    
    // Stack - LIFO
    stack<int> st;
    st.push(10);
    st.push(20);
    st.push(30);
    while (!st.empty()) {
        cout << st.top() << " ";
        st.pop();
    }
    cout << endl;
    
    return 0;
}
```

---

### Learning Path

```
Level 1: Basic Data Structures
├── Array
├── String
└── Utility Components (pair, tuple)

Level 2: Sequence Containers
├── vector
├── list
└── deque

Level 3: Container Adapters
├── stack
├── queue
└── priority_queue

Level 4: Associative Containers
├── set / multiset
├── map / multimap
└── Unordered versions

Level 5: Specialized Containers
├── bitset
└── valarray
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Array out-of-bounds access | Use `std::array` or `vector::at()` |
| Using vector when list is better | Understand insert/delete complexity |
| Invalidating iterators | Know which operations invalidate |
| Using ordered containers when unordered suffices | Use unordered for O(1) lookup |
| Forgetting to reserve vector capacity | Use `reserve()` when size known |
| Using `list` when `deque` is better | Deque has O(1) random access |

---

### Practice Questions

After completing this section, you should be able to:

1. Choose the appropriate container for a given scenario
2. Implement a stack using vector or list
3. Use map to count frequency of elements
4. Use unordered_set for O(1) lookups
5. Iterate through containers using iterators
6. Compare performance of different containers
7. Handle iterator invalidation correctly

---

### Next Steps

- Finally visit [Theory.md](Theory.md) to learn about theoretical foundations.