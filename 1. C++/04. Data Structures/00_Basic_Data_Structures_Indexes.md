# C++ Basic Data Structures - Complete Index

## Overview
This comprehensive documentation covers all core C++ data structures, from primitive arrays to advanced associative containers. Each file provides complete theoretical foundations, exhaustive function coverage, practical real-world examples, performance analysis, and professional best practices. The series is designed for both beginners learning C++ data structures and experienced developers seeking a complete reference.

---

## Complete File Structure

### 01_Arrays.md

**Covers:** C-style arrays, `std::array` (C++11), `std::vector`

#### Detailed Topics Covered:

| Section | Content |
|---------|---------|
| **C-style Arrays** | Declaration, initialization, memory layout, pointer arithmetic, multi-dimensional arrays, size calculation, passing to functions, limitations and dangers |
| **std::array** | Modern fixed-size arrays, STL interface, bounds checking with `.at()`, iterators, tuple interface, structured bindings (C++17), compile-time size |
| **std::vector** | Dynamic arrays, automatic resizing, capacity management, memory allocation strategies, emplacement vs insertion, iterator invalidation rules, shrink_to_fit, reserve |

#### Key Operations Demonstrated:
- 20+ initialization methods
- All access methods (`[]`, `.at()`, `.front()`, `.back()`, `.data()`)
- Insertion (`push_back`, `insert`, `emplace_back`, `emplace`)
- Deletion (`pop_back`, `erase`, `clear`)
- Capacity management (`size`, `capacity`, `reserve`, `shrink_to_fit`, `resize`)
- Algorithms integration (sort, find, reverse, transform, accumulate)
- Memory optimization techniques
- 2D and jagged vector operations

#### Time Complexity:
| Operation | C-style Array | std::array | std::vector |
|-----------|---------------|------------|-------------|
| Access | O(1) | O(1) | O(1) |
| Insert at End | O(1)* | N/A | O(1) amortized |
| Insert at Middle | O(n) | O(n) | O(n) |
| Delete at End | O(1)* | N/A | O(1) |
| Search | O(n) | O(n) | O(n) |

*Requires manual size tracking

#### Practical Examples:
- Browser history implementation
- Balanced parentheses checker
- Postfix expression evaluation
- Dynamic array resizing simulation

---

### 02_Strings.md

**Covers:** C-style strings, `std::string`

#### Detailed Topics Covered:

| Section | Content |
|---------|---------|
| **C-style Strings** | Character arrays, null termination, string literals, `cstring` functions (`strcpy`, `strcat`, `strcmp`, `strlen`, `strchr`, `strstr`), buffer overflow risks, safe alternatives |
| **std::string** | Modern string class, automatic memory management, copy-on-write (COW) vs small string optimization (SSO), character encoding (ASCII, UTF-8, UTF-16, UTF-32) |

#### Key Operations Demonstrated:
- 10+ initialization methods
- Access methods (`[]`, `.at()`, `.front()`, `.back()`, `.data()`, `.c_str()`)
- Modification (`append`, `insert`, `replace`, `erase`, `push_back`, `pop_back`)
- Searching (`find`, `rfind`, `find_first_of`, `find_last_of`, `find_first_not_of`, `find_last_not_of`)
- Comparison (operators, `.compare()`)
- Substring extraction (`.substr()`)
- Conversion (`std::stoi`, `std::stod`, `std::to_string`)
- Case conversion (with `std::transform`)
- Splitting and joining
- Regular expressions (C++11)
- Unicode support

#### Practical Examples:
- Word frequency counter
- Palindrome detection
- Anagram detection
- Longest common prefix
- String builder pattern
- URL parsing
- CSV parsing
- Case-insensitive string operations

---

### 03_SequenceContainers.md

**Covers:** `std::deque`, `std::list`, `std::forward_list`

#### Detailed Topics Covered:

| Container | Content |
|-----------|---------|
| **deque** | Double-ended queue implementation (segmented memory), fast front/back operations, random access, memory layout (blocks of arrays), when to use over vector |
| **list** | Doubly-linked list implementation, node-based storage, iterator stability, constant-time insertion anywhere, memory overhead, when to use |
| **forward_list** | Singly-linked list (C++11), forward-only traversal, minimal memory overhead, no `size()` member, optimized for forward operations |

#### Key Operations Demonstrated:

**All Containers:**
- Construction and initialization
- Push/pop front and back (where applicable)
- Insert and erase operations
- Iterators (forward, reverse, const)
- Size and capacity operations
- Swapping
- Comparison operators

**list Specific:**
- Splice (move elements between lists)
- Merge (merge sorted lists)
- Sort (member function, not `std::sort`)
- Reverse
- Unique (remove consecutive duplicates)
- Remove/remove_if

#### Time Complexity:

| Operation | vector | deque | list | forward_list |
|-----------|--------|-------|------|--------------|
| Random Access | O(1) | O(1) | O(n) | O(n) |
| Insert at Front | O(n) | O(1) | O(1) | O(1) |
| Insert at Back | O(1)* | O(1) | O(1) | O(n) |
| Insert at Middle | O(n) | O(n) | O(1)** | O(1)** |
| Memory Overhead | Low | Medium | High | Medium |

*Amortized  
**With iterator to position

#### Practical Examples:
- **deque:** Sliding window maximum, job scheduling queue
- **list:** LRU cache implementation, polynomial representation
- **forward_list:** Adjacency list for graphs, memory-constrained applications

---

### 04_ContainerAdapters.md

**Covers:** `std::stack`, `std::queue`, `std::priority_queue`

#### Detailed Topics Covered:

| Adapter | Pattern | Underlying Container | Key Operations | Use Cases |
|---------|---------|---------------------|----------------|-----------|
| stack | LIFO | deque (default), vector, list | push, pop, top, empty, size | Function calls, undo/redo, DFS, expression evaluation |
| queue | FIFO | deque (default), list | push, pop, front, back, empty, size | BFS, printer queue, task scheduling, message queues |
| priority_queue | Heap | vector (default), deque | push, pop, top, empty, size | Dijkstra, Huffman coding, scheduling, median maintenance |

#### Key Operations Demonstrated:
- Construction with different underlying containers
- Custom comparators (min-heap, max-heap)
- Emplacement vs insertion (C++11)
- Element access (top, front, back)
- Size and empty checks
- Swapping

#### Time Complexity:

| Operation | stack | queue | priority_queue |
|-----------|-------|-------|----------------|
| push | O(1) | O(1) | O(log n) |
| pop | O(1) | O(1) | O(log n) |
| top/front/back | O(1) | O(1) | O(1) |
| size | O(1) | O(1) | O(1) |

#### Practical Examples:
- Browser history (back/forward)
- Balanced parentheses validator
- Postfix expression evaluator
- BFS graph traversal
- Printer queue simulation
- Dijkstra's shortest path
- Find K largest elements
- Merge K sorted lists
- Median in a data stream

---

### 05_AssociativeContainers.md

**Covers:** `std::set`, `std::multiset`, `std::map`, `std::multimap`

#### Detailed Topics Covered:

| Container | Elements | Key-Value | Duplicates | Implementation | Use Cases |
|-----------|----------|-----------|------------|----------------|-----------|
| set | Unique keys | No | No | Red-Black Tree | Unique sorted collections, set operations |
| multiset | Non-unique keys | No | Yes | Red-Black Tree | Frequency counting, multisets |
| map | Unique keys | Yes | No | Red-Black Tree | Dictionaries, associative arrays |
| multimap | Non-unique keys | Yes | Yes | Red-Black Tree | One-to-many relationships |

#### Key Operations Demonstrated:
- 10+ insertion methods (`insert`, `emplace`, `emplace_hint`, `try_emplace` (C++17))
- Access methods (`[]`, `.at()`, iterators)
- Deletion (`erase` by key, by iterator, by range)
- Searching (`find`, `count`, `contains` (C++20), `lower_bound`, `upper_bound`, `equal_range`)
- Iterators (forward, reverse, const)
- Custom comparators
- Set operations (union, intersection, difference, symmetric difference)
- Structured bindings (C++17)

#### Time Complexity:
| Operation | set/map | multiset/multimap |
|-----------|---------|-------------------|
| Insert | O(log n) | O(log n) |
| Delete | O(log n) | O(log n) |
| Find | O(log n) | O(log n) |
| Lower/Upper Bound | O(log n) | O(log n) |

#### Practical Examples:
- Word frequency counter (with `map`)
- Student database (`map<int, StudentInfo>`)
- Cache implementation (LRU with `map`)
- Course enrollment system (`multimap<string, string>`)
- Phone directory (`multimap<string, string>`)
- Dictionary with multiple definitions (`multimap<string, string>`)
- Prime number sieve (`set`)
- Set operations on mathematical sets
- Range queries on sorted data

---

### 06_UnorderedAssociativeContainers.md

**Covers:** `std::unordered_set`, `std::unordered_multiset`, `std::unordered_map`, `std::unordered_multimap`

#### Detailed Topics Covered:

| Container | Elements | Key-Value | Duplicates | Implementation | Hash Requirements |
|-----------|----------|-----------|------------|----------------|-------------------|
| unordered_set | Unique keys | No | No | Hash Table | Hash function + equality |
| unordered_multiset | Non-unique keys | No | Yes | Hash Table | Hash function + equality |
| unordered_map | Unique keys | Yes | No | Hash Table | Hash function + equality |
| unordered_multimap | Non-unique keys | Yes | Yes | Hash Table | Hash function + equality |

#### Key Operations Demonstrated:
- Construction with custom hash functions
- Bucket management (`bucket_count`, `bucket_size`, `bucket`, `load_factor`, `max_load_factor`)
- Rehashing (`reserve`, `rehash`)
- All insertion methods (`insert`, `emplace`, `emplace_hint`)
- All deletion methods (`erase`, `clear`)
- Searching (`find`, `count`, `contains` (C++20), `equal_range`)
- Custom hash functions for user-defined types
- Custom equality comparators

#### Time Complexity:
| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Insert | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Find | O(1) | O(n) |
| Rehash | O(n) | O(n) |

#### Practical Examples:
- Fast membership testing (millions of operations)
- Removing duplicates from vector
- Case-insensitive string set
- Graph DFS with visited set
- Word frequency counter (faster than `map`)
- LRU cache implementation
- Two-sum problem O(n) solution
- Performance comparison vs `std::map`
- Custom hash for complex keys (Person struct)
- Tagging system (`unordered_multimap`)

---

### 07_UtilityDataStructures.md

**Covers:** `std::pair`, `std::tuple`, `std::optional`, `std::variant`, `std::any`

#### Detailed Topics Covered:

| Structure | C++ Version | Purpose | Key Features | Use Cases |
|-----------|-------------|---------|--------------|-----------|
| pair | C++98 | Two-value container | .first, .second, make_pair, structured bindings | Map elements, returning two values |
| tuple | C++11 | Multiple-value container | std::get, std::apply, tuple_cat, structured bindings | Returning multiple values, compile-time lists |
| optional | C++17 | Optional value | value_or, has_value, emplace, monadic operations | Safe returns, configuration, parsing |
| variant | C++17 | Type-safe union | std::visit, get_if, holds_alternative, index | State machines, JSON-like data, error handling |
| any | C++17 | Type-safe any type | any_cast, type, emplace, reset | Configuration systems, heterogeneous containers |

#### Key Operations Demonstrated:

**pair:**
- Construction (direct, `make_pair`, brace initialization)
- Access (`.first`, `.second`, `std::get`, structured bindings)
- Comparison (lexicographical)
- Swapping
- Vector of pairs with sorting

**tuple:**
- Construction (`make_tuple`, `forward_as_tuple`, `tie`)
- Access (`std::get`, structured bindings)
- Tuple operations (`tuple_cat`, `std::apply`)
- Compile-time iteration
- Tuple of references

**optional:**
- Construction (empty, with value, `std::nullopt`)
- Value checking (`has_value`, bool conversion)
- Access (`*`, `->`, `.value()`, `.value_or()`)
- Modification (`=`, `emplace`, `reset`)
- Monadic operations (`.and_then`, `.transform`, `.or_else`) - C++23

**variant:**
- Construction (direct, `std::in_place_type`, `std::in_place_index`)
- Type checking (`.index()`, `std::holds_alternative`)
- Access (`std::get`, `std::get_if`)
- Type-safe visitation (`std::visit` with overloaded pattern)

**any:**
- Construction (empty, with value, `std::make_any`)
- Type checking (`.type()`)
- Access (`std::any_cast`)
- Modification (`=`, `emplace`, `reset`)

#### Practical Examples:
- **pair:** Min-max return, map insertion, coordinate system, edge representation, priority queue with pairs
- **tuple:** Database records, statistical analysis, heterogeneous containers, function argument packing
- **optional:** Safe division, configuration lookup, cache implementation, parsing with error handling, chaining operations
- **variant:** JSON-like data structures, calculator with multiple types, state machine, error handling with multiple types
- **any:** Configuration system, heterogeneous container, event system, type-safe printing

---

### 08_SpecializedContainers.md

**Covers:** `std::bitset`, `std::valarray`

#### Detailed Topics Covered:

| Container | Purpose | Size | Memory | Performance | Use Cases |
|-----------|---------|------|--------|-------------|-----------|
| bitset | Fixed-size bit manipulation | Compile-time | 1 bit/element | Highly optimized | Flags, masks, compact sets, bit algorithms |
| valarray | Numerical computing | Dynamic | Array-based | Vectorized ops | Scientific computing, signal processing |

#### Key Operations Demonstrated:

**bitset:**
- Construction (from integer, from string, default)
- Bit access (`[]`, `.test()`)
- Bit operations (`set`, `reset`, `flip`)
- Bitwise operators (`&`, `|`, `^`, `~`, `<<`, `>>`)
- Queries (`any`, `all`, `none`, `count`, `size`)
- Conversions (`to_string`, `to_ulong`, `to_ullong`)
- Comparison operators

**valarray:**
- Construction (size, value, initializer list)
- Element-wise arithmetic (+, -, *, /, %)
- Scalar operations
- Compound assignment
- Aggregate functions (`sum`, `min`, `max`)
- Mathematical functions (`sin`, `cos`, `exp`, `log`, `sqrt`, `abs`)
- Slicing (`std::slice`, `std::gslice`)
- Masked operations
- Indirect addressing

#### Practical Examples:

**bitset:**
- Permission flags system
- Set operations for small universes
- Error code tracking
- Bloom filter simulation
- Sieve of Eratosthenes (prime numbers)
- Gray code generation
- Circular shift operations
- Parity check
- Hamming distance calculation

**valarray:**
- Vector dot product
- Matrix multiplication using slices
- Polynomial evaluation
- Moving average (signal processing)
- Fourier series approximation
- Statistical analysis (mean, variance, std deviation)
- Data normalization
- Convolution operation
- Image processing (kernel convolution)

---

## Quick Reference Tables

### Complete Container Comparison

| Container | Random Access | Insert Front | Insert Back | Insert Middle | Memory Layout | Iterator Type |
|-----------|--------------|--------------|-------------|---------------|---------------|---------------|
| vector | O(1) | O(n) | O(1)* | O(n) | Contiguous | Random Access |
| deque | O(1) | O(1) | O(1) | O(n) | Segmented | Random Access |
| list | O(n) | O(1) | O(1) | O(1)** | Non-contiguous | Bidirectional |
| forward_list | O(n) | O(1) | O(n) | O(1)** | Non-contiguous | Forward |
| set/map | O(log n) | O(log n) | O(log n) | O(log n) | Tree nodes | Bidirectional |
| unordered_set/map | O(1)† | O(1)† | O(1)† | O(1)† | Hash buckets | Forward |
| stack | - | - | O(1) | - | Depends | - |
| queue | - | - | O(1) | - | Depends | - |
| priority_queue | - | - | O(log n) | - | Depends | - |

*Amortized O(1)  
**With iterator to position  
†Average case; worst case O(n)

### Memory Overhead Comparison

| Container | Per Element Overhead | Additional Overhead |
|-----------|---------------------|---------------------|
| vector | 0 bytes | Capacity tracking |
| deque | ~0 bytes (blocked) | Block pointers |
| list | 2 pointers (16-32 bytes) | None |
| forward_list | 1 pointer (8-16 bytes) | None |
| set/map | 3 pointers + color (24-40 bytes) | None |
| unordered_* | Hash bucket pointer | Bucket array |

---

## Best Practices Summary

### Selection Decision Tree

```
Need to store data?
│
├── Need order preservation?
│   ├── Yes → Sequence Container
│   │   ├── Need random access?
│   │   │   ├── Yes → Need dynamic size?
│   │   │   │   ├── Yes → std::vector (default)
│   │   │   │   └── No → std::array (fixed size)
│   │   │   └── No → Need fast insertion at both ends?
│   │   │       ├── Yes → std::deque
│   │   │       └── No → Need fast insertion anywhere?
│   │   │           ├── Yes → std::list
│   │   │           └── No → std::forward_list
│   │   └── No → Container Adapter
│   │       ├── LIFO → std::stack
│   │       ├── FIFO → std::queue
│   │       └── Priority-based → std::priority_queue
│   │
│   └── No → Associative Container
│       ├── Need key-value pairs?
│       │   ├── Yes → Need order?
│       │   │   ├── Yes → std::map
│       │   │   └── No → std::unordered_map (faster)
│       │   └── No → Need order?
│       │       ├── Yes → std::set
│       │       └── No → std::unordered_set (faster)
│       │
│       └── Duplicate keys allowed?
│           ├── Yes → Use multiset/multimap version
│           └── No → Use set/map version
│
└── Need specialized functionality?
    ├── Bit manipulation → std::bitset
    └── Numerical computing → std::valarray
```

### Memory Management Guidelines

1. **Use `std::vector` as default** - Most versatile and cache-friendly
2. **Use `.reserve()` when size known** - Prevents multiple reallocations
3. **Use `.shrink_to_fit()` after removals** - Reduces memory footprint
4. **Use `emplace()` over `push()`** - Avoids unnecessary copies
5. **Use `std::optional` for nullable values** - More expressive than sentinel values
6. **Use `std::variant` for type-safe unions** - Safer than C unions
7. **Use `std::any` only when type truly unknown** - Has runtime overhead

### Performance Optimization Guidelines

1. **Choose unordered containers for speed** - O(1) average operations
2. **Choose ordered containers for range queries** - `lower_bound`, `upper_bound`
3. **Use `reserve()` for hash containers** - Prevents rehashing
4. **Use list when iterators must remain valid** - No invalidation on insert/erase
5. **Use `std::string_view` for read-only strings** - No copying overhead
6. **Use `std::span` for array views** - Non-owning contiguous view (C++20)
7. **Profile before optimizing** - Know where bottlenecks are

---

## Version Support Summary

| Feature | C++ Version | File Reference |
|---------|-------------|----------------|
| `std::array` | C++11 | 01_Arrays.md |
| `std::forward_list` | C++11 | 03_SequenceContainers.md |
| `std::unordered_*` | C++11 | 06_UnorderedAssociativeContainers.md |
| `std::tuple` | C++11 | 07_UtilityDataStructures.md |
| Structured bindings | C++17 | All files |
| `std::optional` | C++17 | 07_UtilityDataStructures.md |
| `std::variant` | C++17 | 07_UtilityDataStructures.md |
| `std::any` | C++17 | 07_UtilityDataStructures.md |
| `std::string_view` | C++17 | 02_Strings.md |
| `std::filesystem` | C++17 | Not covered (not core DS) |
| `std::span` | C++20 | Not covered (view, not core DS) |
| `std::flat_set`/`flat_map` | C++23 | Not covered (new additions) |

---

## Conclusion

This 8-file series provides **complete coverage of all core C++ data structures**:

### Foundations (Files 1-2)
1. **Arrays** - The most fundamental data structure
2. **Strings** - Text representation and manipulation

### Linear Containers (Files 3-4)
3. **Sequence Containers** - deque, list, forward_list
4. **Container Adapters** - stack, queue, priority_queue

### Associative Containers (Files 5-6)
5. **Ordered Associative** - set, map, multiset, multimap
6. **Unordered Associative** - hash-based versions

### Utilities & Specialized (Files 7-8)
7. **Utility Structures** - pair, tuple, optional, variant, any
8. **Specialized Containers** - bitset, valarray

### What Each File Includes:
- ✅ Complete theory and characteristics
- ✅ All functions and operations with code examples
- ✅ Time and space complexity analysis
- ✅ Memory layout and iterator invalidation rules
- ✅ 5-10 practical real-world examples per file
- ✅ Best practices and common pitfalls
- ✅ Performance optimization techniques
- ✅ Selection guidelines and decision trees

This documentation serves as a **complete reference** for:
- **Beginners** learning C++ data structures
- **Intermediate developers** seeking deeper understanding
- **Advanced programmers** needing quick reference
- **Interview preparation** covering all essential containers
- **System design** choosing appropriate data structures