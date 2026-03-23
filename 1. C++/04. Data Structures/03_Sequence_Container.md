# Sequence Containers in C++

## Overview
Sequence containers store elements in a linear sequence. C++ provides four main sequence containers: `std::vector` (dynamic array), `std::deque` (double-ended queue), `std::list` (doubly-linked list), and `std::forward_list` (singly-linked list). Each has different performance characteristics and use cases.

## Key Characteristics

| Container | Random Access | Insert/Delete at Front | Insert/Delete at Back | Insert/Delete in Middle | Memory Layout |
|-----------|--------------|----------------------|---------------------|------------------------|---------------|
| vector | O(1) | O(n) | O(1)* | O(n) | Contiguous |
| deque | O(1) | O(1) | O(1) | O(n) | Segmented |
| list | O(n) | O(1) | O(1) | O(1)** | Non-contiguous |
| forward_list | O(n) | O(1) | O(n) | O(1)** | Non-contiguous |

*Amortized O(1)  
**With iterator to position

---

## 1. std::vector (Dynamic Array)

### Theory
`std::vector` is a dynamic array that stores elements contiguously. It's the most commonly used sequence container due to its cache-friendly memory layout and excellent performance for most operations.

**Advantages:**
- Contiguous memory (cache-friendly)
- O(1) random access
- Amortized O(1) insertion at the end
- Compatible with C-style APIs via `.data()`
- Excellent for iteration

**When to Use:**
- Default choice for most sequence needs
- When you need random access
- When you primarily add/remove at the end
- When cache performance matters
- When you need to interface with C APIs

### All Functions and Operations

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <iterator>

void demonstrateVector() {
    std::cout << "\n========== STD::VECTOR ==========\n";
    
    // ==================== CONSTRUCTORS & INITIALIZATION ====================
    std::cout << "\n--- Constructors & Initialization ---\n";
    
    std::vector<int> v1;                                    // Empty vector
    std::vector<int> v2(10);                                // 10 elements, value-initialized (0)
    std::vector<int> v3(10, 42);                            // 10 elements, all 42
    std::vector<int> v4 = {1, 2, 3, 4, 5};                 // Initializer list (C++11)
    std::vector<int> v5(v4);                                // Copy constructor
    std::vector<int> v6(std::move(v5));                     // Move constructor (C++11)
    std::vector<int> v7(v4.begin(), v4.end());              // Iterator range constructor
    
    // Using assign()
    std::vector<int> assign_vec;
    assign_vec.assign(5, 100);                              // 5 elements, all 100
    assign_vec.assign({1, 2, 3, 4, 5});                     // From initializer list
    assign_vec.assign(v4.begin(), v4.end());                // From iterator range
    
    // ==================== CAPACITY & SIZE ====================
    std::cout << "\n--- Capacity & Size ---\n";
    
    std::vector<int> cap_vec = {1, 2, 3, 4, 5};
    
    std::cout << "Size: " << cap_vec.size() << "\n";
    std::cout << "Capacity: " << cap_vec.capacity() << "\n";
    std::cout << "Max size: " << cap_vec.max_size() << "\n";
    std::cout << "Empty? " << (cap_vec.empty() ? "Yes" : "No") << "\n";
    
    // Reserve capacity (pre-allocate memory)
    cap_vec.reserve(100);
    std::cout << "After reserve(100) - Capacity: " << cap_vec.capacity() << "\n";
    
    // Shrink to fit (reduce capacity to size)
    cap_vec.shrink_to_fit();
    std::cout << "After shrink_to_fit - Capacity: " << cap_vec.capacity() << "\n";
    
    // Resize
    cap_vec.resize(10);
    std::cout << "After resize(10): ";
    for (int x : cap_vec) std::cout << x << " ";
    std::cout << "\n";
    
    cap_vec.resize(3);
    std::cout << "After resize(3): ";
    for (int x : cap_vec) std::cout << x << " ";
    std::cout << "\n";
    
    cap_vec.resize(7, 99);
    std::cout << "After resize(7, 99): ";
    for (int x : cap_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== ACCESSING ELEMENTS ====================
    std::cout << "\n--- Accessing Elements ---\n";
    
    std::vector<int> access_vec = {10, 20, 30, 40, 50};
    
    // Using operator[]
    std::cout << "operator[](2): " << access_vec[2] << "\n";
    
    // Using .at() (with bounds checking)
    try {
        std::cout << ".at(2): " << access_vec.at(2) << "\n";
        // std::cout << access_vec.at(10) << "\n";        // Throws std::out_of_range
    } catch (const std::out_of_range& e) {
        std::cout << "Out of range: " << e.what() << "\n";
    }
    
    // Front and back
    std::cout << "front(): " << access_vec.front() << "\n";
    std::cout << "back(): " << access_vec.back() << "\n";
    
    // Data pointer (C-style array access)
    int* data_ptr = access_vec.data();
    std::cout << "data()[2]: " << data_ptr[2] << "\n";
    
    // ==================== ADDING ELEMENTS ====================
    std::cout << "\n--- Adding Elements ---\n";
    
    std::vector<int> add_vec;
    
    // push_back - add to end
    add_vec.push_back(10);
    add_vec.push_back(20);
    add_vec.push_back(30);
    std::cout << "After push_back: ";
    for (int x : add_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // emplace_back (C++11) - construct in place
    add_vec.emplace_back(40);
    std::cout << "After emplace_back: ";
    for (int x : add_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // insert at position
    auto it = add_vec.begin() + 2;
    add_vec.insert(it, 25);
    std::cout << "After insert at position 2: ";
    for (int x : add_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // insert multiple copies
    add_vec.insert(add_vec.begin(), 3, 5);
    std::cout << "After insert 3 copies of 5: ";
    for (int x : add_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // insert from initializer list
    add_vec.insert(add_vec.end(), {100, 200, 300});
    std::cout << "After insert from initializer list: ";
    for (int x : add_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // insert from iterator range
    std::vector<int> source = {1000, 2000, 3000};
    add_vec.insert(add_vec.begin(), source.begin(), source.end());
    std::cout << "After insert from range: ";
    for (int x : add_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // emplace (C++11) - construct in place at position
    add_vec.emplace(add_vec.begin() + 2, 999);
    std::cout << "After emplace at position 2: ";
    for (int x : add_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== REMOVING ELEMENTS ====================
    std::cout << "\n--- Removing Elements ---\n";
    
    std::vector<int> remove_vec = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    // pop_back - remove last element
    remove_vec.pop_back();
    std::cout << "After pop_back: ";
    for (int x : remove_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // erase at position
    remove_vec.erase(remove_vec.begin() + 2);
    std::cout << "After erase at index 2: ";
    for (int x : remove_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // erase range
    remove_vec.erase(remove_vec.begin() + 1, remove_vec.begin() + 3);
    std::cout << "After erase range [1, 3): ";
    for (int x : remove_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // clear - remove all elements
    remove_vec.clear();
    std::cout << "After clear - Size: " << remove_vec.size() << "\n";
    
    // ==================== ALGORITHMS WITH VECTOR ====================
    std::cout << "\n--- Algorithms ---\n";
    
    std::vector<int> algo_vec = {5, 2, 8, 1, 9, 3, 7, 4, 6, 10};
    
    // Sorting
    std::sort(algo_vec.begin(), algo_vec.end());
    std::cout << "Sorted ascending: ";
    for (int x : algo_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // Sorting descending
    std::sort(algo_vec.begin(), algo_vec.end(), std::greater<int>());
    std::cout << "Sorted descending: ";
    for (int x : algo_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // Reverse
    std::reverse(algo_vec.begin(), algo_vec.end());
    std::cout << "Reversed: ";
    for (int x : algo_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // Find
    auto found = std::find(algo_vec.begin(), algo_vec.end(), 5);
    if (found != algo_vec.end()) {
        std::cout << "Found 5 at index: " << (found - algo_vec.begin()) << "\n";
    }
    
    // Count
    int count = std::count(algo_vec.begin(), algo_vec.end(), 5);
    std::cout << "Count of 5: " << count << "\n";
    
    // Count with condition
    int odd_count = std::count_if(algo_vec.begin(), algo_vec.end(), 
                                   [](int x) { return x % 2 != 0; });
    std::cout << "Count of odd numbers: " << odd_count << "\n";
    
    // Accumulate (sum)
    int sum = std::accumulate(algo_vec.begin(), algo_vec.end(), 0);
    std::cout << "Sum: " << sum << "\n";
    
    // Min and max
    auto min_it = std::min_element(algo_vec.begin(), algo_vec.end());
    auto max_it = std::max_element(algo_vec.begin(), algo_vec.end());
    std::cout << "Min: " << *min_it << ", Max: " << *max_it << "\n";
    
    // Transform
    std::vector<int> squares(algo_vec.size());
    std::transform(algo_vec.begin(), algo_vec.end(), squares.begin(),
                   [](int x) { return x * x; });
    std::cout << "Squares: ";
    for (int x : squares) std::cout << x << " ";
    std::cout << "\n";
    
    // Remove-Erase Idiom (remove elements by value)
    std::vector<int> remove_erase_vec = {1, 2, 3, 2, 4, 2, 5, 2, 6};
    remove_erase_vec.erase(
        std::remove(remove_erase_vec.begin(), remove_erase_vec.end(), 2),
        remove_erase_vec.end()
    );
    std::cout << "After remove-erase (remove 2s): ";
    for (int x : remove_erase_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // Remove-Erase Idiom with condition
    std::vector<int> remove_if_vec = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    remove_if_vec.erase(
        std::remove_if(remove_if_vec.begin(), remove_if_vec.end(),
                       [](int x) { return x % 2 == 0; }),
        remove_if_vec.end()
    );
    std::cout << "After remove_if (remove evens): ";
    for (int x : remove_if_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // Unique (remove consecutive duplicates)
    std::vector<int> dup_vec = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5};
    auto last = std::unique(dup_vec.begin(), dup_vec.end());
    dup_vec.erase(last, dup_vec.end());
    std::cout << "After unique (remove consecutive duplicates): ";
    for (int x : dup_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== ITERATORS ====================
    std::cout << "\n--- Iterators ---\n";
    
    std::vector<int> iter_vec = {10, 20, 30, 40, 50};
    
    // Regular iterators
    std::cout << "Forward iteration: ";
    for (auto it = iter_vec.begin(); it != iter_vec.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    // Reverse iterators
    std::cout << "Reverse iteration: ";
    for (auto it = iter_vec.rbegin(); it != iter_vec.rend(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    // Const iterators
    std::cout << "Const iteration: ";
    for (auto it = iter_vec.cbegin(); it != iter_vec.cend(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    // Range-based for loop
    std::cout << "Range-based for: ";
    for (const auto& elem : iter_vec) {
        std::cout << elem << " ";
    }
    std::cout << "\n";
    
    // ==================== COMPARISON ====================
    std::cout << "\n--- Comparison ---\n";
    
    std::vector<int> comp1 = {1, 2, 3, 4, 5};
    std::vector<int> comp2 = {1, 2, 3, 4, 5};
    std::vector<int> comp3 = {1, 2, 3, 4, 6};
    
    std::cout << "comp1 == comp2: " << (comp1 == comp2 ? "Yes" : "No") << "\n";
    std::cout << "comp1 == comp3: " << (comp1 == comp3 ? "Yes" : "No") << "\n";
    std::cout << "comp1 < comp3: " << (comp1 < comp3 ? "Yes" : "No") << "\n";
    
    // ==================== SWAPPING ====================
    std::cout << "\n--- Swapping ---\n";
    
    std::vector<int> swap1 = {1, 2, 3};
    std::vector<int> swap2 = {10, 20, 30, 40, 50};
    
    swap1.swap(swap2);
    std::cout << "After swap - swap1: ";
    for (int x : swap1) std::cout << x << " ";
    std::cout << "\nAfter swap - swap2: ";
    for (int x : swap2) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== 2D VECTOR ====================
    std::cout << "\n--- 2D Vector ---\n";
    
    // Create 3x4 matrix
    std::vector<std::vector<int>> mat(3, std::vector<int>(4, 0));
    
    // Fill with values
    int val = 1;
    for (size_t i = 0; i < mat.size(); i++) {
        for (size_t j = 0; j < mat[i].size(); j++) {
            mat[i][j] = val++;
        }
    }
    
    std::cout << "2D Matrix (3x4):\n";
    for (const auto& row : mat) {
        for (int elem : row) {
            std::cout << elem << " ";
        }
        std::cout << "\n";
    }
    
    // Jagged vector (rows of different lengths)
    std::vector<std::vector<int>> jagged = {
        {1, 2, 3},
        {4, 5},
        {6, 7, 8, 9}
    };
    
    std::cout << "Jagged array:\n";
    for (const auto& row : jagged) {
        for (int elem : row) {
            std::cout << elem << " ";
        }
        std::cout << "\n";
    }
}
```

---

## 2. std::deque (Double-Ended Queue)

### Theory
`std::deque` (double-ended queue) is a sequence container that allows fast insertion and deletion at both ends. It provides random access like vector but with segmented storage.

**Advantages:**
- O(1) insertion/deletion at both ends
- O(1) random access
- No reallocation when adding at ends
- No need to reserve capacity

**When to Use:**
- When you need fast insertion/deletion at both ends
- When random access is required
- When you don't want reallocation overhead
- For implementing queues and deques

### All Functions and Operations

```cpp
#include <iostream>
#include <deque>
#include <algorithm>

void demonstrateDeque() {
    std::cout << "\n========== STD::DEQUE ==========\n";
    
    // ==================== CONSTRUCTORS & INITIALIZATION ====================
    std::cout << "\n--- Constructors & Initialization ---\n";
    
    std::deque<int> dq1;                                    // Empty deque
    std::deque<int> dq2(10);                                // 10 elements, value-initialized (0)
    std::deque<int> dq3(10, 42);                            // 10 elements, all 42
    std::deque<int> dq4 = {1, 2, 3, 4, 5};                 // Initializer list
    std::deque<int> dq5(dq4);                               // Copy constructor
    std::deque<int> dq6(dq4.begin(), dq4.end());            // Iterator range constructor
    
    // ==================== ADDING ELEMENTS ====================
    std::cout << "\n--- Adding Elements ---\n";
    
    std::deque<int> add_dq;
    
    // Add to back
    add_dq.push_back(10);
    add_dq.push_back(20);
    add_dq.push_back(30);
    
    // Add to front
    add_dq.push_front(5);
    add_dq.push_front(0);
    
    std::cout << "After push_front/push_back: ";
    for (int x : add_dq) std::cout << x << " ";
    std::cout << "\n";
    
    // emplace_back and emplace_front (C++11)
    add_dq.emplace_back(40);
    add_dq.emplace_front(-5);
    std::cout << "After emplace: ";
    for (int x : add_dq) std::cout << x << " ";
    std::cout << "\n";
    
    // Insert at position
    auto it = add_dq.begin() + 3;
    add_dq.insert(it, 99);
    std::cout << "After insert at position 3: ";
    for (int x : add_dq) std::cout << x << " ";
    std::cout << "\n";
    
    // Insert multiple copies
    add_dq.insert(add_dq.begin(), 3, 100);
    std::cout << "After insert 3 copies of 100: ";
    for (int x : add_dq) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== REMOVING ELEMENTS ====================
    std::cout << "\n--- Removing Elements ---\n";
    
    std::deque<int> remove_dq = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    
    // Remove from back
    remove_dq.pop_back();
    std::cout << "After pop_back: ";
    for (int x : remove_dq) std::cout << x << " ";
    std::cout << "\n";
    
    // Remove from front
    remove_dq.pop_front();
    std::cout << "After pop_front: ";
    for (int x : remove_dq) std::cout << x << " ";
    std::cout << "\n";
    
    // Erase at position
    remove_dq.erase(remove_dq.begin() + 2);
    std::cout << "After erase at index 2: ";
    for (int x : remove_dq) std::cout << x << " ";
    std::cout << "\n";
    
    // Erase range
    remove_dq.erase(remove_dq.begin() + 1, remove_dq.begin() + 3);
    std::cout << "After erase range [1, 3): ";
    for (int x : remove_dq) std::cout << x << " ";
    std::cout << "\n";
    
    // Clear
    remove_dq.clear();
    std::cout << "After clear - Size: " << remove_dq.size() << "\n";
    
    // ==================== ACCESSING ELEMENTS ====================
    std::cout << "\n--- Accessing Elements ---\n";
    
    std::deque<int> access_dq = {10, 20, 30, 40, 50};
    
    // Using operator[]
    std::cout << "operator[](2): " << access_dq[2] << "\n";
    
    // Using .at() (with bounds checking)
    try {
        std::cout << ".at(2): " << access_dq.at(2) << "\n";
    } catch (const std::out_of_range& e) {
        std::cout << "Out of range: " << e.what() << "\n";
    }
    
    // Front and back
    std::cout << "front(): " << access_dq.front() << "\n";
    std::cout << "back(): " << access_dq.back() << "\n";
    
    // ==================== SIZE & CAPACITY ====================
    std::cout << "\n--- Size & Capacity ---\n";
    
    std::deque<int> size_dq = {1, 2, 3, 4, 5};
    
    std::cout << "Size: " << size_dq.size() << "\n";
    std::cout << "Max size: " << size_dq.max_size() << "\n";
    std::cout << "Empty? " << (size_dq.empty() ? "Yes" : "No") << "\n";
    
    // Resize
    size_dq.resize(10);
    std::cout << "After resize(10): ";
    for (int x : size_dq) std::cout << x << " ";
    std::cout << "\n";
    
    size_dq.resize(3);
    std::cout << "After resize(3): ";
    for (int x : size_dq) std::cout << x << " ";
    std::cout << "\n";
    
    size_dq.resize(7, 99);
    std::cout << "After resize(7, 99): ";
    for (int x : size_dq) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== ALGORITHMS WITH DEQUE ====================
    std::cout << "\n--- Algorithms ---\n";
    
    std::deque<int> algo_dq = {5, 2, 8, 1, 9, 3, 7, 4, 6, 10};
    
    // Sorting (deque supports random access iterators)
    std::sort(algo_dq.begin(), algo_dq.end());
    std::cout << "Sorted: ";
    for (int x : algo_dq) std::cout << x << " ";
    std::cout << "\n";
    
    // Reverse
    std::reverse(algo_dq.begin(), algo_dq.end());
    std::cout << "Reversed: ";
    for (int x : algo_dq) std::cout << x << " ";
    std::cout << "\n";
    
    // Find
    auto found = std::find(algo_dq.begin(), algo_dq.end(), 5);
    if (found != algo_dq.end()) {
        std::cout << "Found 5 at position: " << (found - algo_dq.begin()) << "\n";
    }
    
    // ==================== ITERATORS ====================
    std::cout << "\n--- Iterators ---\n";
    
    std::deque<int> iter_dq = {10, 20, 30, 40, 50};
    
    std::cout << "Forward: ";
    for (auto it = iter_dq.begin(); it != iter_dq.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    std::cout << "Reverse: ";
    for (auto it = iter_dq.rbegin(); it != iter_dq.rend(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    // ==================== SWAPPING ====================
    std::cout << "\n--- Swapping ---\n";
    
    std::deque<int> swap1 = {1, 2, 3};
    std::deque<int> swap2 = {10, 20, 30, 40, 50};
    
    swap1.swap(swap2);
    std::cout << "After swap - swap1: ";
    for (int x : swap1) std::cout << x << " ";
    std::cout << "\nAfter swap - swap2: ";
    for (int x : swap2) std::cout << x << " ";
    std::cout << "\n";
}
```

---

## 3. std::list (Doubly-Linked List)

### Theory
`std::list` is a doubly-linked list that allows constant-time insertion and deletion at any position. It does not support random access but provides excellent iterator stability.

**Advantages:**
- O(1) insertion/deletion anywhere (with iterator)
- Iterators remain valid after modifications
- No reallocation
- Efficient merging and splicing

**When to Use:**
- When you need frequent insertions/deletions in the middle
- When random access is not required
- When iterator stability is important
- When implementing complex data structures

### All Functions and Operations

```cpp
#include <iostream>
#include <list>
#include <algorithm>

void demonstrateList() {
    std::cout << "\n========== STD::LIST ==========\n";
    
    // ==================== CONSTRUCTORS & INITIALIZATION ====================
    std::cout << "\n--- Constructors & Initialization ---\n";
    
    std::list<int> lst1;                                    // Empty list
    std::list<int> lst2(10);                                // 10 elements, value-initialized (0)
    std::list<int> lst3(10, 42);                            // 10 elements, all 42
    std::list<int> lst4 = {1, 2, 3, 4, 5};                 // Initializer list
    std::list<int> lst5(lst4);                              // Copy constructor
    std::list<int> lst6(lst4.begin(), lst4.end());          // Iterator range constructor
    
    // ==================== ADDING ELEMENTS ====================
    std::cout << "\n--- Adding Elements ---\n";
    
    std::list<int> add_lst;
    
    // Add to back
    add_lst.push_back(10);
    add_lst.push_back(20);
    add_lst.push_back(30);
    
    // Add to front
    add_lst.push_front(5);
    add_lst.push_front(0);
    
    std::cout << "After push_front/push_back: ";
    for (int x : add_lst) std::cout << x << " ";
    std::cout << "\n";
    
    // emplace_back and emplace_front (C++11)
    add_lst.emplace_back(40);
    add_lst.emplace_front(-5);
    std::cout << "After emplace: ";
    for (int x : add_lst) std::cout << x << " ";
    std::cout << "\n";
    
    // Insert at position
    auto it = add_lst.begin();
    std::advance(it, 3);                                     // Move iterator to position 3
    add_lst.insert(it, 99);
    std::cout << "After insert at position 3: ";
    for (int x : add_lst) std::cout << x << " ";
    std::cout << "\n";
    
    // Insert multiple copies
    add_lst.insert(add_lst.begin(), 3, 100);
    std::cout << "After insert 3 copies of 100: ";
    for (int x : add_lst) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== REMOVING ELEMENTS ====================
    std::cout << "\n--- Removing Elements ---\n";
    
    std::list<int> remove_lst = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    
    // Remove from back
    remove_lst.pop_back();
    std::cout << "After pop_back: ";
    for (int x : remove_lst) std::cout << x << " ";
    std::cout << "\n";
    
    // Remove from front
    remove_lst.pop_front();
    std::cout << "After pop_front: ";
    for (int x : remove_lst) std::cout << x << " ";
    std::cout << "\n";
    
    // Erase at position
    auto erase_it = remove_lst.begin();
    std::advance(erase_it, 2);
    remove_lst.erase(erase_it);
    std::cout << "After erase at index 2: ";
    for (int x : remove_lst) std::cout << x << " ";
    std::cout << "\n";
    
    // Erase range
    auto start = remove_lst.begin();
    auto end = remove_lst.begin();
    std::advance(start, 1);
    std::advance(end, 3);
    remove_lst.erase(start, end);
    std::cout << "After erase range [1, 3): ";
    for (int x : remove_lst) std::cout << x << " ";
    std::cout << "\n";
    
    // Remove by value (removes all occurrences)
    remove_lst.remove(5);
    std::cout << "After remove(5): ";
    for (int x : remove_lst) std::cout << x << " ";
    std::cout << "\n";
    
    // Remove with condition
    remove_lst.remove_if([](int x) { return x % 2 == 0; });
    std::cout << "After remove_if (remove evens): ";
    for (int x : remove_lst) std::cout << x << " ";
    std::cout << "\n";
    
    // Clear
    remove_lst.clear();
    std::cout << "After clear - Size: " << remove_lst.size() << "\n";
    
    // ==================== ACCESSING ELEMENTS ====================
    std::cout << "\n--- Accessing Elements ---\n";
    
    std::list<int> access_lst = {10, 20, 30, 40, 50};
    
    // Front and back
    std::cout << "front(): " << access_lst.front() << "\n";
    std::cout << "back(): " << access_lst.back() << "\n";
    
    // No random access - need to advance iterator
    auto access_it = access_lst.begin();
    std::advance(access_it, 2);
    std::cout << "Element at index 2: " << *access_it << "\n";
    
    // ==================== SIZE & CAPACITY ====================
    std::cout << "\n--- Size & Capacity ---\n";
    
    std::list<int> size_lst = {1, 2, 3, 4, 5};
    
    std::cout << "Size: " << size_lst.size() << "\n";
    std::cout << "Max size: " << size_lst.max_size() << "\n";
    std::cout << "Empty? " << (size_lst.empty() ? "Yes" : "No") << "\n";
    
    // Resize
    size_lst.resize(10);
    std::cout << "After resize(10): ";
    for (int x : size_lst) std::cout << x << " ";
    std::cout << "\n";
    
    size_lst.resize(3);
    std::cout << "After resize(3): ";
    for (int x : size_lst) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== SPLICING (Moving Elements) ====================
    std::cout << "\n--- Splicing (Moving Elements) ---\n";
    
    std::list<int> source = {100, 200, 300};
    std::list<int> target = {1, 2, 3, 4, 5};
    
    // Splice entire source into target at position
    auto splice_pos = target.begin();
    std::advance(splice_pos, 2);
    target.splice(splice_pos, source);
    
    std::cout << "After splicing source into target: ";
    for (int x : target) std::cout << x << " ";
    std::cout << "\n";
    std::cout << "Source after splice: ";
    for (int x : source) std::cout << x << " ";
    std::cout << "\n";
    
    // Splice single element
    std::list<int> source2 = {1000, 2000, 3000};
    std::list<int> target2 = {1, 2, 3, 4, 5};
    
    auto splice_elem = source2.begin();
    auto target_pos = target2.begin();
    std::advance(target_pos, 3);
    target2.splice(target_pos, source2, splice_elem);
    
    std::cout << "After splicing single element: ";
    for (int x : target2) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== LIST OPERATIONS ====================
    std::cout << "\n--- List Operations ---\n";
    
    std::list<int> sort_lst = {5, 2, 8, 1, 9, 3, 7, 4, 6, 10};
    
    // Sort (list provides its own sort, not std::sort)
    sort_lst.sort();
    std::cout << "Sorted: ";
    for (int x : sort_lst) std::cout << x << " ";
    std::cout << "\n";
    
    // Sort with custom comparator
    sort_lst.sort(std::greater<int>());
    std::cout << "Sorted descending: ";
    for (int x : sort_lst) std::cout << x << " ";
    std::cout << "\n";
    
    // Reverse
    sort_lst.reverse();
    std::cout << "Reversed: ";
    for (int x : sort_lst) std::cout << x << " ";
    std::cout << "\n";
    
    // Unique (remove consecutive duplicates)
    std::list<int> dup_lst = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5};
    dup_lst.unique();
    std::cout << "After unique: ";
    for (int x : dup_lst) std::cout << x << " ";
    std::cout << "\n";
    
    // Merge two sorted lists
    std::list<int> merge1 = {1, 3, 5, 7, 9};
    std::list<int> merge2 = {2, 4, 6, 8, 10};
    merge1.merge(merge2);
    std::cout << "After merge: ";
    for (int x : merge1) std::cout << x << " ";
    std::cout << "\n";
    std::cout << "Merged list size: " << merge1.size() << "\n";
    
    // ==================== ITERATORS ====================
    std::cout << "\n--- Iterators ---\n";
    
    std::list<int> iter_lst = {10, 20, 30, 40, 50};
    
    std::cout << "Forward: ";
    for (auto it = iter_lst.begin(); it != iter_lst.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    std::cout << "Reverse: ";
    for (auto it = iter_lst.rbegin(); it != iter_lst.rend(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    // Bidirectional iterators - can move forward and backward
    auto bidir_it = iter_lst.begin();
    std::advance(bidir_it, 2);
    std::cout << "Element at position 2: " << *bidir_it << "\n";
    --bidir_it;
    std::cout << "Previous element: " << *bidir_it << "\n";
}
```

---

## 4. std::forward_list (Singly-Linked List)

### Theory
`std::forward_list` is a singly-linked list introduced in C++11. It provides forward-only traversal and is more memory-efficient than `std::list`.

**Advantages:**
- Memory efficient (only one pointer per node)
- O(1) insertion/deletion at front
- No random access
- Forward-only iteration

**When to Use:**
- When forward traversal is sufficient
- When memory is a constraint
- When you need constant-time insertion at front
- When you don't need backward traversal

### All Functions and Operations

```cpp
#include <iostream>
#include <forward_list>
#include <algorithm>

void demonstrateForwardList() {
    std::cout << "\n========== STD::FORWARD_LIST ==========\n";
    
    // ==================== CONSTRUCTORS & INITIALIZATION ====================
    std::cout << "\n--- Constructors & Initialization ---\n";
    
    std::forward_list<int> fl1;                             // Empty forward_list
    std::forward_list<int> fl2(10);                         // 10 elements, value-initialized (0)
    std::forward_list<int> fl3(10, 42);                     // 10 elements, all 42
    std::forward_list<int> fl4 = {1, 2, 3, 4, 5};          // Initializer list
    std::forward_list<int> fl5(fl4);                        // Copy constructor
    std::forward_list<int> fl6(fl4.begin(), fl4.end());     // Iterator range constructor
    
    // ==================== ADDING ELEMENTS ====================
    std::cout << "\n--- Adding Elements ---\n";
    
    std::forward_list<int> add_fl;
    
    // Add to front (only push_front, no push_back)
    add_fl.push_front(10);
    add_fl.push_front(20);
    add_fl.push_front(30);
    
    std::cout << "After push_front: ";
    for (int x : add_fl) std::cout << x << " ";
    std::cout << "\n";
    
    // emplace_front (C++11)
    add_fl.emplace_front(40);
    std::cout << "After emplace_front: ";
    for (int x : add_fl) std::cout << x << " ";
    std::cout << "\n";
    
    // Insert after position (no insert at specific position)
    auto insert_pos = add_fl.begin();
    add_fl.insert_after(insert_pos, 99);
    std::cout << "After insert_after first element: ";
    for (int x : add_fl) std::cout << x << " ";
    std::cout << "\n";
    
    // Insert multiple copies after position
    add_fl.insert_after(add_fl.begin(), 3, 100);
    std::cout << "After insert_after 3 copies: ";
    for (int x : add_fl) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== REMOVING ELEMENTS ====================
    std::cout << "\n--- Removing Elements ---\n";
    
    std::forward_list<int> remove_fl = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    
    // Remove from front
    remove_fl.pop_front();
    std::cout << "After pop_front: ";
    for (int x : remove_fl) std::cout << x << " ";
    std::cout << "\n";
    
    // Erase after position
    auto erase_pos = remove_fl.begin();
    remove_fl.erase_after(erase_pos);
    std::cout << "After erase_after first element: ";
    for (int x : remove_fl) std::cout << x << " ";
    std::cout << "\n";
    
    // Erase range
    auto start = remove_fl.begin();
    auto end = remove_fl.begin();
    std::advance(start, 1);
    std::advance(end, 3);
    remove_fl.erase_after(start, end);
    std::cout << "After erase range: ";
    for (int x : remove_fl) std::cout << x << " ";
    std::cout << "\n";
    
    // Remove by value
    remove_fl.remove(5);
    std::cout << "After remove(5): ";
    for (int x : remove_fl) std::cout << x << " ";
    std::cout << "\n";
    
    // Remove with condition
    remove_fl.remove_if([](int x) { return x % 2 == 0; });
    std::cout << "After remove_if (remove evens): ";
    for (int x : remove_fl) std::cout << x << " ";
    std::cout << "\n";
    
    // Clear
    remove_fl.clear();
    std::cout << "After clear - Empty? " << (remove_fl.empty() ? "Yes" : "No") << "\n";
    
    // ==================== ACCESSING ELEMENTS ====================
    std::cout << "\n--- Accessing Elements ---\n";
    
    std::forward_list<int> access_fl = {10, 20, 30, 40, 50};
    
    // Front element only (no back)
    std::cout << "front(): " << access_fl.front() << "\n";
    
    // No random access - need to traverse
    auto access_it = access_fl.begin();
    std::advance(access_it, 2);
    std::cout << "Element at index 2: " << *access_it << "\n";
    
    // ==================== SIZE & CAPACITY ====================
    std::cout << "\n--- Size & Capacity ---\n";
    
    std::forward_list<int> size_fl = {1, 2, 3, 4, 5};
    
    // Note: forward_list does NOT have size() member
    // Must calculate size manually
    int size = std::distance(size_fl.begin(), size_fl.end());
    std::cout << "Size (calculated): " << size << "\n";
    std::cout << "Empty? " << (size_fl.empty() ? "Yes" : "No") << "\n";
    std::cout << "Max size: " << size_fl.max_size() << "\n";
    
    // Resize
    size_fl.resize(10);
    std::cout << "After resize(10): ";
    for (int x : size_fl) std::cout << x << " ";
    std::cout << "\n";
    
    size_fl.resize(3);
    std::cout << "After resize(3): ";
    for (int x : size_fl) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== SPLICING ====================
    std::cout << "\n--- Splicing ---\n";
    
    std::forward_list<int> source_fl = {100, 200, 300};
    std::forward_list<int> target_fl = {1, 2, 3, 4, 5};
    
    // Splice after position
    auto splice_pos_fl = target_fl.begin();
    std::advance(splice_pos_fl, 2);
    target_fl.splice_after(splice_pos_fl, source_fl);
    
    std::cout << "After splicing: ";
    for (int x : target_fl) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== FORWARD_LIST OPERATIONS ====================
    std::cout << "\n--- Forward List Operations ---\n";
    
    std::forward_list<int> sort_fl = {5, 2, 8, 1, 9, 3, 7, 4, 6, 10};
    
    // Sort
    sort_fl.sort();
    std::cout << "Sorted: ";
    for (int x : sort_fl) std::cout << x << " ";
    std::cout << "\n";
    
    // Sort with custom comparator
    sort_fl.sort(std::greater<int>());
    std::cout << "Sorted descending: ";
    for (int x : sort_fl) std::cout << x << " ";
    std::cout << "\n";
    
    // Reverse
    sort_fl.reverse();
    std::cout << "Reversed: ";
    for (int x : sort_fl) std::cout << x << " ";
    std::cout << "\n";
    
    // Unique (remove consecutive duplicates)
    std::forward_list<int> dup_fl = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5};
    dup_fl.unique();
    std::cout << "After unique: ";
    for (int x : dup_fl) std::cout << x << " ";
    std::cout << "\n";
    
    // Merge
    std::forward_list<int> merge1_fl = {1, 3, 5, 7, 9};
    std::forward_list<int> merge2_fl = {2, 4, 6, 8, 10};
    merge1_fl.merge(merge2_fl);
    std::cout << "After merge: ";
    for (int x : merge1_fl) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== ITERATORS ====================
    std::cout << "\n--- Iterators ---\n";
    
    std::forward_list<int> iter_fl = {10, 20, 30, 40, 50};
    
    std::cout << "Forward-only iteration: ";
    for (auto it = iter_fl.begin(); it != iter_fl.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    // Range-based for loop
    std::cout << "Range-based for: ";
    for (const auto& elem : iter_fl) {
        std::cout << elem << " ";
    }
    std::cout << "\n";
}
```

---

## Performance Comparison Summary

| Operation | vector | deque | list | forward_list |
|-----------|--------|-------|------|--------------|
| Random Access | O(1) | O(1) | O(n) | O(n) |
| Insert/Delete at Front | O(n) | O(1) | O(1) | O(1) |
| Insert/Delete at Back | O(1)* | O(1) | O(1) | O(n) |
| Insert/Delete in Middle | O(n) | O(n) | O(1)** | O(1)** |
| Memory Overhead | Low | Medium | High | Medium |
| Iterator Invalidation | Frequent | Less | Never | Never |
| Cache Performance | Excellent | Good | Poor | Poor |

*Amortized O(1)  
**With iterator to position

---

## Best Practices

1. **Default to `std::vector`** - It's the most versatile and cache-friendly
2. **Use `std::deque` for double-ended operations** - When you need fast insertion at both ends
3. **Use `std::list` for frequent middle insertions** - When you need O(1) insert/delete anywhere
4. **Use `std::forward_list` for memory-constrained forward-only operations**
5. **Use `reserve()` with vectors** - Prevents reallocation overhead
6. **Prefer `emplace_back()` over `push_back()`** - More efficient for complex objects
7. **Use iterators correctly** - Know when they get invalidated
8. **Consider cache performance** - Contiguous containers are faster for iteration

---

## Common Pitfalls

1. **Iterator invalidation** - Vector reallocation invalidates all iterators
2. **Using list when vector would suffice** - Lists have poor cache performance
3. **Assuming `list::size()` is O(1)** - In older implementations, it could be O(n)
4. **Forgetting that forward_list has no `size()`** - Must calculate manually
5. **Using `std::sort` on list** - Lists have their own `sort()` member function
6. **Accessing elements by index in list** - O(n) operation, use iterators
7. **Not reserving capacity** - Can cause multiple reallocations

---