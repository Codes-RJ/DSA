Here is `Theory.md` for the **04. Data Structures** folder.

---

# Theory.md

## Data Structures - Theoretical Foundations

### Overview

Data structures are specialized formats for organizing, processing, retrieving, and storing data. They form the foundation of computer science and algorithm design. This document covers the theoretical foundations of data structures, including abstract data types, complexity analysis, container categories, and selection guidelines.

---

### 1. What is a Data Structure?

A data structure is a particular way of organizing data in computer memory so that it can be used efficiently. Different data structures are suited to different kinds of applications, and some are highly specialized for specific tasks.

**Key Properties of Data Structures:**

| Property | Description |
|----------|-------------|
| **Organization** | How data elements are arranged |
| **Access Method** | How elements can be accessed (random, sequential) |
| **Space Efficiency** | How much memory the structure uses |
| **Time Efficiency** | How fast operations are |

---

### 2. Abstract Data Types (ADTs)

An Abstract Data Type is a mathematical model for data types defined by the behavior (operations) rather than implementation.

**ADT vs Data Structure:**

| Aspect | Abstract Data Type | Data Structure |
|--------|-------------------|----------------|
| **Definition** | What operations are possible | How operations are implemented |
| **Focus** | Interface | Implementation |
| **Example** | Stack (push, pop, top) | Array-based stack, linked stack |
| **Language** | Theoretical concept | Concrete implementation |

**Common ADTs:**

| ADT | Core Operations | Possible Implementations |
|-----|-----------------|--------------------------|
| **List** | insert, delete, get, set | Array, linked list |
| **Stack** | push, pop, top | Array, linked list |
| **Queue** | enqueue, dequeue, front, back | Array, linked list |
| **Priority Queue** | insert, extract_min/max | Heap, balanced BST |
| **Set** | insert, delete, find | Hash table, BST |
| **Map** | insert, delete, lookup | Hash table, BST |

---

### 3. Complexity Analysis

Time and space complexity are measured using Big O notation.

**Common Complexities:**

| Complexity | Name | Example Operation |
|------------|------|-------------------|
| O(1) | Constant | Array access |
| O(log n) | Logarithmic | Binary search, BST lookup |
| O(n) | Linear | Linear search |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Bubble sort |
| O(2ⁿ) | Exponential | Recursive Fibonacci |

**Complexity Hierarchy:**
```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
```

---

### 4. Container Categories

C++ STL containers are classified into several categories:

```
STL Containers
│
├── Sequence Containers
│   ├── array (C++11)
│   ├── vector
│   ├── deque
│   ├── list
│   └── forward_list (C++11)
│
├── Associative Containers (ordered)
│   ├── set
│   ├── multiset
│   ├── map
│   └── multimap
│
├── Unordered Associative Containers (C++11)
│   ├── unordered_set
│   ├── unordered_multiset
│   ├── unordered_map
│   └── unordered_multimap
│
└── Container Adapters
    ├── stack
    ├── queue
    └── priority_queue
```

---

### 5. Sequence Containers

Sequence containers store elements in a linear order.

| Container | Memory Layout | Random Access | Insert/Delete | Iterator Invalidation |
|-----------|---------------|---------------|---------------|----------------------|
| **array** | Contiguous | O(1) | N/A | N/A |
| **vector** | Contiguous | O(1) | O(n) (end O(1)) | On reallocation |
| **deque** | Blocks | O(1) | O(1) ends, O(n) middle | On insert at ends |
| **list** | Non-contiguous | O(n) | O(1)* | None (except erased) |
| **forward_list** | Non-contiguous | O(n) | O(1)* | None (except erased) |

*Given iterator to position

---

### 6. Associative Containers (Ordered)

Ordered associative containers store elements in sorted order using comparison functions.

| Container | Keys Unique | Sorted By | Implementation | Operation Complexity |
|-----------|-------------|-----------|----------------|----------------------|
| **set** | Yes | Key | Red-Black Tree | O(log n) |
| **multiset** | No | Key | Red-Black Tree | O(log n) |
| **map** | Yes (key) | Key | Red-Black Tree | O(log n) |
| **multimap** | No (key) | Key | Red-Black Tree | O(log n) |

**Red-Black Tree Properties:**

| Property | Description |
|----------|-------------|
| **Color** | Each node is red or black |
| **Root** | Root is black |
| **Leaves** | Leaves (null) are black |
| **Red Rule** | Red nodes cannot have red children |
| **Black Rule** | Every path from root to leaf has same number of black nodes |

---

### 7. Unordered Associative Containers

Unordered associative containers use hash tables for O(1) average access.

| Container | Keys Unique | Implementation | Average Complexity | Worst Case |
|-----------|-------------|----------------|--------------------|------------|
| **unordered_set** | Yes | Hash Table | O(1) | O(n) |
| **unordered_multiset** | No | Hash Table | O(1) | O(n) |
| **unordered_map** | Yes (key) | Hash Table | O(1) | O(n) |
| **unordered_multimap** | No (key) | Hash Table | O(1) | O(n) |

**Hash Table Components:**

| Component | Description |
|-----------|-------------|
| **Bucket** | Slot in hash table that holds elements |
| **Hash Function** | Maps key to bucket index |
| **Load Factor** | Ratio of elements to buckets |
| **Rehashing** | Resizing when load factor exceeds threshold |

**Hash Function Requirements:**

| Requirement | Description |
|-------------|-------------|
| **Deterministic** | Same key always produces same hash |
| **Uniform Distribution** | Keys distributed evenly across buckets |
| **Fast** | Computation should be O(1) |

---

### 8. Container Adapters

Container adapters provide restricted interfaces to underlying containers.

| Adapter | Underlying Container (default) | Principle | Key Operations |
|---------|-------------------------------|-----------|----------------|
| **stack** | deque | LIFO | push, pop, top |
| **queue** | deque | FIFO | push, pop, front, back |
| **priority_queue** | vector | Priority | push, pop, top |

**Stack Principle (LIFO - Last In, First Out):**
```
push(1) → [1]
push(2) → [1, 2]
push(3) → [1, 2, 3]
pop()   → returns 3, stack becomes [1, 2]
top()   → returns 2
```

**Queue Principle (FIFO - First In, First Out):**
```
push(1) → [1]
push(2) → [1, 2]
push(3) → [1, 2, 3]
pop()   → returns 1, queue becomes [2, 3]
front() → returns 2
back()  → returns 3
```

**Priority Queue Principle:**
```
push(10) → [10]
push(30) → [10, 30] (max-heap: 30 at top)
push(20) → [10, 20, 30]
top()    → returns 30
pop()    → removes 30, heap becomes [10, 20]
```

---

### 9. Iterators

Iterators provide a uniform way to traverse elements in containers.

**Iterator Categories:**

| Category | Operations | Supported Containers |
|----------|------------|---------------------|
| **Input** | ++, *, ->, ==, != | istream |
| **Output** | ++, * = | ostream |
| **Forward** | Input + Output + multi-pass | forward_list, unordered_set |
| **Bidirectional** | Forward + -- | list, set, map |
| **Random Access** | Bidirectional + +, -, [], <, > | vector, deque, array |

**Iterator Hierarchy:**
```
          Input Iterator
               │
          Forward Iterator
               │
       ┌───────┴───────┐
       │               │
Bidirectional      Random Access
    Iterator          Iterator
```

---

### 10. Allocators

Allocators manage memory allocation for containers.

| Aspect | Description |
|--------|-------------|
| **Purpose** | Separate memory management from container logic |
| **Default** | `std::allocator<T>` uses `new` and `delete` |
| **Custom** | Can provide custom allocators for pools, tracking |
| **Interface** | `allocate()`, `deallocate()`, `construct()`, `destroy()` |

**Custom Allocator Use Cases:**

| Use Case | Description |
|----------|-------------|
| **Memory Pool** | Pre-allocated blocks for fast allocation |
| **Tracking** | Count allocations for debugging |
| **Shared Memory** | Allocate in shared memory segment |
| **Stack Allocation** | Allocate from stack instead of heap |

---

### 11. Container Selection Guidelines

**By Access Pattern:**

| Access Pattern | Recommended Container |
|----------------|----------------------|
| Random access required | vector, deque, array |
| Sequential access only | list, forward_list |
| Insert/delete at ends | deque, vector (end only) |
| Insert/delete anywhere | list, forward_list |

**By Lookup Requirement:**

| Lookup Requirement | Recommended Container |
|--------------------|----------------------|
| Sorted order needed | set, map |
| Range queries needed | set, map |
| Fast lookup only | unordered_set, unordered_map |
| Duplicate keys allowed | multiset, multimap, unordered_multiset |

**By Size:**

| Size Characteristic | Recommended Container |
|--------------------|----------------------|
| Fixed size known at compile time | array |
| Dynamic, unpredictable | vector |
| Very large, many insert/delete | list, deque |

---

### 12. Memory Layout Comparison

**Contiguous Memory (array, vector):**
```
Address: 1000 1004 1008 1012 1016
Value:   [10] [20] [30] [40] [50]
```
Pros: Cache friendly, fast random access
Cons: Expensive insert/delete in middle

**Linked Memory (list, forward_list):**
```
Node1: [10] → Node2: [20] → Node3: [30] → nullptr
Address: 1000    Address: 2000    Address: 1500
```
Pros: Fast insert/delete anywhere
Cons: Poor cache locality, extra memory for pointers

**Blocked Memory (deque):**
```
Block 0: [10] [11] [12] [13]
Block 1: [20] [21] [22] [23]
Block 2: [30] [31] [32] [33]
```
Pros: O(1) random access, O(1) insert at ends
Cons: Slightly slower than vector for random access

---

### 13. Iterator Invalidation Rules

| Container | Insert | Erase | Reallocation |
|-----------|--------|-------|--------------|
| **vector** | Invalidates after insertion point | Invalidates after erase point | All iterators if reallocation occurs |
| **deque** | Invalidates all (ends may preserve) | Invalidates erased | N/A |
| **list** | No invalidation | Invalidates erased only | N/A |
| **set/map** | No invalidation | Invalidates erased only | N/A |
| **unordered_set** | May invalidate on rehash | Invalidates erased only | On rehash |

---

### 14. Big O Complexity Summary

| Container | Access | Insert | Delete | Search | Memory |
|-----------|--------|--------|--------|--------|--------|
| **array** | O(1) | N/A | N/A | O(n) | O(n) fixed |
| **vector** | O(1) | O(n)* | O(n)* | O(n) | O(n) |
| **deque** | O(1) | O(1)** | O(1)** | O(n) | O(n) |
| **list** | O(n) | O(1)† | O(1)† | O(n) | O(n) |
| **set/map** | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| **unordered_set/map** | O(1) avg | O(1) avg | O(1) avg | O(1) avg | O(n) |

* O(1) at end, O(n) elsewhere
** O(1) at ends, O(n) elsewhere
† Given iterator to position

---

### 15. When to Use Which Container

| Scenario | Recommended Container |
|----------|----------------------|
| Need fixed-size array known at compile time | `array` |
| Need dynamic array with fast random access | `vector` |
| Need frequent insert/delete at both ends | `deque` |
| Need frequent insert/delete anywhere | `list` |
| Need LIFO access | `stack` |
| Need FIFO access | `queue` |
| Need priority-based access | `priority_queue` |
| Need unique sorted elements | `set` |
| Need key-value pairs sorted by key | `map` |
| Need fast lookup, order doesn't matter | `unordered_set` |
| Need fast key-value lookup | `unordered_map` |
| Need bit manipulation | `bitset` |
| Need numerical array operations | `valarray` |

---

### Key Takeaways

1. **Data structures** organize data for efficient access and manipulation
2. **Abstract Data Types** define behavior; **data structures** define implementation
3. **Complexity analysis** helps choose the right data structure
4. **Sequence containers** store linear sequences (vector, list, deque)
5. **Associative containers** store key-value pairs in sorted order (set, map)
6. **Unordered containers** use hash tables for O(1) average access
7. **Container adapters** provide restricted interfaces (stack, queue)
8. **Iterators** provide uniform traversal across containers
9. **Iterator invalidation** rules vary by container
10. **Container selection** depends on access patterns and requirements

---

### Next Steps

- Go to [00_Basic_Data_Structures_Indexes.md](00_Basic_Data_Structures_Indexes.md) to understand Data Structures Index and Navigation.