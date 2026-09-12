# Array Basics in C++ - Memory Layout, Cache Locality, and Custom Dynamic Array

## 1. Introduction & Theoretical Foundations

An **array** is the most fundamental data structure in computer science—a contiguous block of memory storing elements of homogeneous type accessible via 0-based indexing.

Understanding arrays requires understanding physical hardware mechanics:
- **Spatial Locality**: Because array elements reside in contiguous memory addresses, loading `arr[0]` loads the entire $64$-byte CPU cache line, making subsequent sequential accesses orders of magnitude faster than pointer-chasing node structures.
- **Random Access**: Any element's memory address is computed via a single arithmetic operation in $O(1)$ time:
$$\text{Address}(\text{arr}[i]) = \text{Base Address} + i \times \text{sizeof}(T)$$

```
Memory Layout of int arr[5] (4 bytes per element):
┌──────────┬──────────┬──────────┬──────────┬──────────┐
│  arr[0]  │  arr[1]  │  arr[2]  │  arr[3]  │  arr[4]  │
├──────────┼──────────┼──────────┼──────────┼──────────┤
│ 0x1000   │ 0x1004   │ 0x1008   │ 0x100C   │ 0x1010   │
└──────────┴──────────┴──────────┴──────────┴──────────┘
```

---

## 2. Row-Major vs. Column-Major Cache Locality

In C++, 2D arrays and matrices are stored in **Row-Major order**: contiguous rows placed back-to-back in memory:
$$\text{Address}(\text{matrix}[r][c]) = \text{Base} + (r \times \text{COLS} + c) \times \text{sizeof}(T)$$

Traversing row-by-row leverages CPU hardware prefetchers, whereas traversing column-by-column induces **cache thrashing** (cache misses on every access), causing significant performance degradation on large datasets.

```
Row-Major in Memory:
[ Row 0, Col 0 ][ Row 0, Col 1 ][ Row 0, Col 2 ] ... [ Row 1, Col 0 ][ Row 1, Col 1 ] ...
◄──────────── Cache Line 1 ────────────►           ◄──────────── Cache Line 2 ────────────►
```

---

## 3. Production-Grade Custom Dynamic Array Class (`DynamicArray<T>`)

To understand how `std::vector` functions under the hood, we implement a complete, generic `DynamicArray<T>` featuring:
- Geometric growth factor ($2\times$) guaranteeing **amortized $O(1)$** insertions.
- The **Rule of Five** (Deep Copy Constructor, Copy Assignment, Move Constructor, Move Assignment, Destructor).
- Bounds checking via `.at()`.
- Range-based `for` loop support via custom pointer iterators.

```cpp
#include <iostream>
#include <stdexcept>
#include <algorithm>
#include <utility>

template <typename T>
class DynamicArray {
private:
    T* data;
    size_t size_;
    size_t capacity_;

    void reallocate(size_t newCapacity) {
        T* newData = new T[newCapacity];
        for (size_t i = 0; i < size_; ++i) {
            newData[i] = std::move(data[i]);
        }
        delete[] data;
        data = newData;
        capacity_ = newCapacity;
    }

public:
    // Default Constructor
    DynamicArray() : data(nullptr), size_(0), capacity_(0) {
        reallocate(2);
    }

    // Parameterized Constructor
    explicit DynamicArray(size_t initialCapacity) 
        : data(nullptr), size_(0), capacity_(0) {
        reallocate(initialCapacity == 0 ? 2 : initialCapacity);
    }

    // Destructor
    ~DynamicArray() {
        delete[] data;
    }

    // Copy Constructor (Deep Copy)
    DynamicArray(const DynamicArray& other) 
        : data(new T[other.capacity_]), size_(other.size_), capacity_(other.capacity_) {
        for (size_t i = 0; i < size_; ++i) {
            data[i] = other.data[i];
        }
    }

    // Copy Assignment Operator
    DynamicArray& operator=(const DynamicArray& other) {
        if (this != &other) {
            T* newData = new T[other.capacity_];
            for (size_t i = 0; i < other.size_; ++i) {
                newData[i] = other.data[i];
            }
            delete[] data;
            data = newData;
            size_ = other.size_;
            capacity_ = other.capacity_;
        }
        return *this;
    }

    // Move Constructor
    DynamicArray(DynamicArray&& other) noexcept 
        : data(other.data), size_(other.size_), capacity_(other.capacity_) {
        other.data = nullptr;
        other.size_ = 0;
        other.capacity_ = 0;
    }

    // Move Assignment Operator
    DynamicArray& operator=(DynamicArray&& other) noexcept {
        if (this != &other) {
            delete[] data;
            data = other.data;
            size_ = other.size_;
            capacity_ = other.capacity_;
            other.data = nullptr;
            other.size_ = 0;
            other.capacity_ = 0;
        }
        return *this;
    }

    // Insertion at end: Amortized O(1)
    void push_back(const T& value) {
        if (size_ >= capacity_) {
            reallocate(capacity_ * 2);
        }
        data[size_++] = value;
    }

    void push_back(T&& value) {
        if (size_ >= capacity_) {
            reallocate(capacity_ * 2);
        }
        data[size_++] = std::move(value);
    }

    // Removal at end: O(1)
    void pop_back() {
        if (size_ == 0) {
            throw std::underflow_error("Array is empty");
        }
        size_--;
    }

    // Insert at arbitrary position: O(N)
    void insert(size_t index, const T& value) {
        if (index > size_) {
            throw std::out_of_range("Index out of range");
        }
        if (size_ >= capacity_) {
            reallocate(capacity_ * 2);
        }
        for (size_t i = size_; i > index; --i) {
            data[i] = std::move(data[i - 1]);
        }
        data[index] = value;
        size_++;
    }

    // Remove at arbitrary position: O(N)
    void erase(size_t index) {
        if (index >= size_) {
            throw std::out_of_range("Index out of range");
        }
        for (size_t i = index; i < size_ - 1; ++i) {
            data[i] = std::move(data[i + 1]);
        }
        size_--;
    }

    // Element Access
    T& operator[](size_t index) { return data[index]; }
    const T& operator[](size_t index) const { return data[index]; }

    T& at(size_t index) {
        if (index >= size_) throw std::out_of_range("Index out of range");
        return data[index];
    }
    const T& at(size_t index) const {
        if (index >= size_) throw std::out_of_range("Index out of range");
        return data[index];
    }

    size_t size() const { return size_; }
    size_t capacity() const { return capacity_; }
    bool empty() const { return size_ == 0; }

    // Iterator support
    T* begin() { return data; }
    const T* begin() const { return data; }
    T* end() { return data + size_; }
    const T* end() const { return data + size_; }
};
```

---

## 4. Complete Runnable Verification Suite

```cpp
#include <iostream>
#include <vector>
#include <chrono>

int main() {
    std::cout << "=====================================================" << std::endl;
    std::cout << "         DYNAMIC ARRAY & CACHE BENCHMARK SUITE       " << std::endl;
    std::cout << "=====================================================" << std::endl;

    // --- 1. Custom Dynamic Array Demonstration ---
    std::cout << "\n[1] CUSTOM DYNAMIC ARRAY OPERATIONS:" << std::endl;
    DynamicArray<int> arr;
    for (int i = 1; i <= 5; ++i) {
        arr.push_back(i * 10);
    }
    std::cout << "  Initial Array (size=" << arr.size() << ", cap=" << arr.capacity() << "): ";
    for (int val : arr) std::cout << val << " ";
    std::cout << std::endl;

    arr.insert(2, 25); // Insert 25 at index 2
    std::cout << "  After insert(2, 25): ";
    for (int val : arr) std::cout << val << " ";
    std::cout << std::endl;

    arr.erase(3); // Erase element at index 3 (30)
    std::cout << "  After erase(3):      ";
    for (int val : arr) std::cout << val << " ";
    std::cout << std::endl;

    // --- 2. Cache Locality Simulation: Row-Major vs Col-Major ---
    std::cout << "\n[2] 2D ROW-MAJOR VS COLUMN-MAJOR LOCALITY:" << std::endl;
    const int ROWS = 1000;
    const int COLS = 1000;
    std::vector<std::vector<int>> matrix(ROWS, std::vector<int>(COLS, 1));

    // Row-major access (Cache friendly)
    auto startRow = std::chrono::high_resolution_clock::now();
    long long sumRow = 0;
    for (int r = 0; r < ROWS; ++r) {
        for (int c = 0; c < COLS; ++c) {
            sumRow += matrix[r][c];
        }
    }
    auto endRow = std::chrono::high_resolution_clock::now();
    auto elapsedRow = std::chrono::duration_cast<std::chrono::microseconds>(endRow - startRow).count();

    // Column-major access (Cache unfriendly)
    auto startCol = std::chrono::high_resolution_clock::now();
    long long sumCol = 0;
    for (int c = 0; c < COLS; ++c) {
        for (int r = 0; r < ROWS; ++r) {
            sumCol += matrix[r][c];
        }
    }
    auto endCol = std::chrono::high_resolution_clock::now();
    auto elapsedCol = std::chrono::duration_cast<std::chrono::microseconds>(endCol - startCol).count();

    std::cout << "  Row-major traversal time: " << elapsedRow << " microseconds (Sum=" << sumRow << ")" << std::endl;
    std::cout << "  Col-major traversal time: " << elapsedCol << " microseconds (Sum=" << sumCol << ")" << std::endl;
    std::cout << "  Notice how row-major access is significantly faster due to CPU cache line prefetching." << std::endl;

    std::cout << "\n=====================================================" << std::endl;
    return 0;
}
```

---

## 5. Complexity Analysis Table

| Operation | C-Style Array | `std::array` | Custom `DynamicArray<T>` | `std::vector` |
| :--- | :--- | :--- | :--- | :--- |
| **Random Access (`[]`)** | $O(1)$ | $O(1)$ | $O(1)$ | $O(1)$ |
| **Bounds-Checked Access (`.at()`)** | N/A | $O(1)$ | $O(1)$ | $O(1)$ |
| **Insert at End (`push_back`)** | N/A | N/A | $O(1)$ amortized | $O(1)$ amortized |
| **Insert at Arbitrary Index** | N/A | N/A | $O(N)$ | $O(N)$ |
| **Delete from End (`pop_back`)** | N/A | N/A | $O(1)$ | $O(1)$ |
| **Delete at Arbitrary Index** | N/A | N/A | $O(N)$ | $O(N)$ |
| **Memory Allocation** | Stack/Static | Stack | Dynamic Heap | Dynamic Heap |

---

## 6. Common Pitfalls & Best Practices

1. **Index Out-of-Bounds Undefined Behavior**: `operator[]` performs no bounds checking for speed. In debug builds or untrusted input paths, prefer `.at()`, which throws `std::out_of_range`.
2. **Failure to Pre-allocate (`reserve`)**: Repeatedly calling `push_back()` without reserving causes $\log_2(N)$ heap allocations, copying all existing elements each time. When final size $N$ is known, always call `vec.reserve(N)`.
3. **Iterator Invalidation**: Inserting into or resizing an array invalidates pointers and iterators to all subsequent elements (or all elements if reallocation occurs).
4. **Shallow Copy Pointer Leaks**: Writing a dynamic array class without a custom copy constructor or copy assignment operator leads to multiple deletions of the same heap buffer (Double Free).

---

## Next Step

- Proceed to [02_Two_Pointer_Technique.md](02_Two_Pointer_Technique.md) to explore multi-pointer convergence and window partitioning in C++.
