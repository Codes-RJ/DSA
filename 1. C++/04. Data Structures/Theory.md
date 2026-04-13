# C++ Basic Data Structures - Theory Guide

## Overview

Data structures are fundamental building blocks in computer science that organize and store data in memory. C++ provides both built-in primitive data structures and powerful container classes through the Standard Template Library (STL). Understanding these data structures is essential for writing efficient, maintainable, and scalable code.

## Classification of Data Structures

Data structures in C++ can be broadly classified into:

1. **Primitive Data Structures**: Built-in types (int, char, float, double, bool)
2. **Linear Data Structures**: Elements arranged in sequence
3. **Non-Linear Data Structures**: Elements connected hierarchically
4. **Container Adapters**: Provide restricted interfaces to underlying containers

---

## 1. Arrays

### Definition
An array is a collection of elements of the same data type stored in contiguous memory locations.

### Types of Arrays in C++

#### C-style Arrays
- Traditional arrays inherited from C
- Fixed size determined at compile time
- No bounds checking
- No size information stored

#### std::array (C++11)
- Modern alternative to C-style arrays
- Fixed size known at compile time
- Provides STL-like interface
- Size information available via `.size()`
- Bounds checking with `.at()`

#### std::vector
- Dynamic array that can grow/shrink automatically
- Elements stored contiguously
- Provides random access
- Amortized O(1) insertion at the end
- Cache-friendly due to contiguous memory

### Time Complexity
| Operation | C-style Array | std::array | std::vector |
|-----------|---------------|------------|-------------|
| Access | O(1) | O(1) | O(1) |
| Insert at end | O(1)* | N/A | O(1) amortized |
| Insert at middle | O(n) | O(n) | O(n) |
| Delete at end | O(1)* | N/A | O(1) |
| Delete at middle | O(n) | O(n) | O(n) |
| Search | O(n) | O(n) | O(n) |

*Requires manual size tracking

### Memory Layout
Arrays store elements in contiguous memory:
```
Address:  1000   1004   1008   1012   1016
         +------+------+------+------+------+
         |  10  |  20  |  30  |  40  |  50  |
         +------+------+------+------+------+
         arr[0] arr[1] arr[2] arr[3] arr[4]
```

---

## 2. Strings

### Definition
A string is a sequence of characters used to represent text.

### Types of Strings

#### C-style Strings
- Null-terminated character arrays
- Functions in `<cstring>` header
- Manual memory management required
- Prone to buffer overflow

#### std::string
- Modern C++ string class
- Dynamic size
- Automatic memory management
- Rich member functions
- Safe and easy to use

### Common Operations
- Concatenation: `+`, `+=`
- Length: `.length()`, `.size()`
- Substring: `.substr()`
- Find: `.find()`
- Replace: `.replace()`
- Conversion: `std::stoi()`, `std::to_string()`

---

## 3. Sequence Containers

Sequence containers store elements in a linear sequence.

### std::vector
- Dynamic array with contiguous storage
- Best for most general use cases
- Excellent cache performance

### std::deque (Double-ended Queue)
- Double-ended queue
- Fast insertion/deletion at both ends
- Random access available
- Not contiguous like vector

### std::list
- Doubly-linked list
- Constant time insertion/deletion anywhere
- No random access
- Iterator stability

### std::forward_list
- Singly-linked list (C++11)
- Forward-only traversal
- Minimal memory overhead
- Good for forward-only operations

### Comparison Matrix
| Feature | vector | deque | list | forward_list |
|---------|--------|-------|------|--------------|
| Random Access | Yes | Yes | No | No |
| Insert at Front | O(n) | O(1) | O(1) | O(1) |
| Insert at Back | O(1)* | O(1) | O(1) | No |
| Insert Middle | O(n) | O(n) | O(1) | O(1) |
| Memory Overhead | Low | Medium | High | Medium |
| Iterator Invalidation | Frequent | Less | Never | Never |

---

## 4. Associative Containers

Associative containers store key-value pairs or sorted unique elements.

### Ordered Associative Containers

#### std::map
- Key-value pairs sorted by key
- Implemented as Red-Black Tree
- O(log n) operations
- Keys are unique

#### std::set
- Unique elements sorted
- Implemented as Red-Black Tree
- O(log n) operations

### Unordered Associative Containers

#### std::unordered_map
- Key-value pairs stored in hash table
- Average O(1) operations
- Keys are unique
- Order not guaranteed

#### std::unordered_set
- Unique elements in hash table
- Average O(1) operations
- Order not guaranteed

### Time Complexity Comparison
| Operation | map/set | unordered_map/unordered_set |
|-----------|---------|----------------------------|
| Insert | O(log n) | O(1) average, O(n) worst |
| Delete | O(log n) | O(1) average, O(n) worst |
| Search | O(log n) | O(1) average, O(n) worst |
| Access | O(log n) | O(1) average, O(n) worst |

---

## 5. Container Adapters

Container adapters provide restricted interfaces to underlying containers.

### std::stack
- LIFO (Last In, First Out) data structure
- Operations: push, pop, top
- Default underlying container: deque

### std::queue
- FIFO (First In, First Out) data structure
- Operations: push, pop, front, back
- Default underlying container: deque

### std::priority_queue
- Elements ordered by priority
- Max-heap by default
- Operations: push, pop, top
- Default underlying container: vector

---

## 6. Utility Data Structures

### std::pair
- Holds two heterogeneous values
- Accessed via .first and .second
- Used in map insertions and returns

### std::tuple (C++11)
- Holds multiple heterogeneous values
- Accessed via std::get<index>()
- Can be used for returning multiple values

### std::optional (C++17)
- Represents optional value that may or may not exist
- Safer than using sentinel values or pointers
- Check with .has_value() or bool conversion

### std::variant (C++17)
- Type-safe union
- Holds one of several specified types
- Accessed via std::get or std::visit

---

## Memory Management in C++ Data Structures

### Stack vs Heap Allocation
- **Stack**: Automatic allocation, fast, limited size
- **Heap**: Manual allocation, slower, flexible size

### RAII (Resource Acquisition Is Initialization)
- Resources acquired in constructor, released in destructor
- STL containers follow RAII principles
- Automatic memory management for containers

### Iterator Invalidation Rules
- **vector**: Insert/erase may invalidate all iterators
- **deque**: Insert at front/back invalidates iterators
- **list**: Insert/erase only affects iterators at that position
- **map/set**: Insert/erase doesn't invalidate existing iterators
- **unordered containers**: Rehashing may invalidate all iterators

---

## Choosing the Right Container - Decision Tree

```
Do you need ordered elements?
    ├── Yes → Need key-value pairs?
    │         ├── Yes → std::map
    │         └── No → std::set
    └── No → Need key-value pairs?
              ├── Yes → std::unordered_map
              └── No → std::unordered_set

Do you need sequential access?
    ├── Need random access?
    │   ├── Yes → std::vector (most cases)
    │   └── No → Need fast insertion at both ends?
    │             ├── Yes → std::deque
    │             └── No → std::list
    └── Need LIFO/FIFO access?
        ├── LIFO → std::stack
        └── FIFO → std::queue
```

---

## Performance Guidelines

1. **Use std::vector as default container** - It's cache-friendly and versatile
2. **Use .reserve()** when you know the approximate size
3. **Use .shrink_to_fit()** to reduce memory after removals
4. **Choose unordered containers** when hash collisions are rare
5. **Use ordered containers** when range queries are needed
6. **Avoid frequent insertions in the middle of vectors** - O(n) operations
7. **Use list when iterators must remain valid** after modifications
8. **Use emplace() instead of push()** to avoid unnecessary copies

---

## Common Pitfalls

1. **Out-of-bounds access** - Use .at() for bounds checking
2. **Iterator invalidation** - Know when iterators become invalid
3. **Copy overhead** - Use move semantics and references
4. **Memory fragmentation** - Frequent reallocation in vectors
5. **Hash collisions** - Choose good hash functions for unordered containers
6. **Comparison function requirements** - Strict weak ordering for ordered containers

---

## Conclusion

C++ provides a comprehensive set of data structures catering to different use cases. Understanding the characteristics, time complexities, and memory layouts of these containers enables developers to make informed decisions and write efficient, maintainable code. Modern C++ continues to enhance these data structures with features like move semantics, perfect forwarding, and improved safety guarantees.
---

## Next Step

- Go to [README.md](README.md) to continue.
