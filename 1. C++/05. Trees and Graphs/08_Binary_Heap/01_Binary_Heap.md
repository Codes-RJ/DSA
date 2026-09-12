# Binary Heap Implementation

## 📖 Overview

A **Binary Heap** is a complete binary tree stored inside a contiguous array. It provides logarithmic-time insertion and deletion of the extremal (minimum or maximum) element while allowing constant-time inspection of that element.

This implementation provides a generic, template-driven `BinaryHeap<T, Compare>` supporting:
- Configurable ordering (`MinHeap` via `std::less<T>`, `MaxHeap` via `std::greater<T>`).
- Floyd's linear-time ($O(N)$) heapification from arbitrary arrays.
- Priority queue dynamic operations (`push`, `pop`, `top`, `decreaseKey`, `deleteKey`).
- Cache-friendly in-place **Heap Sort** ($O(N \log N)$ time, $O(1)$ auxiliary memory).
- Visual tree printing and invariant verification.

---

## 🏗️ Structure & Index Arithmetic

```
                Node Index: i
                ├── Parent:        (i - 1) / 2
                ├── Left Child:    2 * i + 1
                └── Right Child:   2 * i + 2
```

```
Level 0:                 [0]
                     /         \
Level 1:           [1]         [2]
                 /     \     /     \
Level 2:       [3]     [4] [5]     [6]
```

Every level except the last is full. Nodes on the last level occupy leftmost positions, allowing contiguous flat-array packing with zero pointer overhead.

---

## 💻 Complete C++ Implementation

```cpp
#include <iostream>
#include <vector>
#include <functional>
#include <stdexcept>
#include <algorithm>
#include <iomanip>
#include <string>

template <typename T, typename Compare = std::less<T>>
class BinaryHeap {
private:
    std::vector<T> data;
    Compare comp;

    size_t parent(size_t i) const { return (i - 1) / 2; }
    size_t leftChild(size_t i) const { return 2 * i + 1; }
    size_t rightChild(size_t i) const { return 2 * i + 2; }

    void siftUp(size_t i) {
        while (i > 0 && comp(data[i], data[parent(i)])) {
            std::swap(data[i], data[parent(i)]);
            i = parent(i);
        }
    }

    void siftDown(size_t i) {
        size_t best = i;
        size_t left = leftChild(i);
        size_t right = rightChild(i);

        if (left < data.size() && comp(data[left], data[best])) {
            best = left;
        }
        if (right < data.size() && comp(data[right], data[best])) {
            best = right;
        }

        if (best != i) {
            std::swap(data[i], data[best]);
            siftDown(best);
        }
    }

    void printTreeHelper(size_t idx, const std::string& prefix, bool isLeft) const {
        if (idx < data.size()) {
            std::cout << prefix;
            std::cout << (isLeft ? "├── " : "└── ");
            std::cout << data[idx] << "\n";

            size_t left = leftChild(idx);
            size_t right = rightChild(idx);

            if (left < data.size() || right < data.size()) {
                printTreeHelper(left, prefix + (isLeft ? "│   " : "    "), true);
                if (right < data.size()) {
                    printTreeHelper(right, prefix + (isLeft ? "│   " : "    "), false);
                }
            }
        }
    }

public:
    BinaryHeap(const Compare& comparator = Compare()) : comp(comparator) {}

    // Floyd's O(N) buildHeap constructor
    explicit BinaryHeap(const std::vector<T>& elements, const Compare& comparator = Compare())
        : data(elements), comp(comparator) {
        if (!data.empty()) {
            for (int i = static_cast<int>(data.size() / 2) - 1; i >= 0; i--) {
                siftDown(static_cast<size_t>(i));
            }
        }
    }

    size_t size() const { return data.size(); }
    bool empty() const { return data.empty(); }
    void clear() { data.clear(); }

    const T& top() const {
        if (empty()) {
            throw std::underflow_error("Heap is empty: cannot access top element.");
        }
        return data[0];
    }

    void push(const T& value) {
        data.push_back(value);
        siftUp(data.size() - 1);
    }

    T pop() {
        if (empty()) {
            throw std::underflow_error("Heap is empty: cannot pop element.");
        }
        T topElement = data[0];
        data[0] = data.back();
        data.pop_back();

        if (!data.empty()) {
            siftDown(0);
        }
        return topElement;
    }

    void decreaseKey(size_t index, const T& newValue) {
        if (index >= data.size()) {
            throw std::out_of_range("Index out of range in decreaseKey.");
        }
        if (!comp(newValue, data[index])) {
            throw std::invalid_argument("New value does not satisfy decrease condition according to comparator.");
        }
        data[index] = newValue;
        siftUp(index);
    }

    void deleteKey(size_t index) {
        if (index >= data.size()) {
            throw std::out_of_range("Index out of range in deleteKey.");
        }
        // Move element to end by swapping with last, then sift
        if (index == data.size() - 1) {
            data.pop_back();
            return;
        }

        T removed = data[index];
        data[index] = data.back();
        data.pop_back();

        // Depending on new element value, sift up or down
        if (comp(data[index], removed)) {
            siftUp(index);
        } else {
            siftDown(index);
        }
    }

    bool isHeap() const {
        for (size_t i = 0; i < data.size() / 2; i++) {
            size_t left = leftChild(i);
            size_t right = rightChild(i);

            if (left < data.size() && comp(data[left], data[i])) {
                return false;
            }
            if (right < data.size() && comp(data[right], data[i])) {
                return false;
            }
        }
        return true;
    }

    void printTree() const {
        if (empty()) {
            std::cout << "[Empty Heap]\n";
            return;
        }
        printTreeHelper(0, "", false);
    }

    void printRawArray() const {
        std::cout << "[ ";
        for (size_t i = 0; i < data.size(); i++) {
            std::cout << data[i] << (i + 1 < data.size() ? ", " : " ");
        }
        std::cout << "]\n";
    }

    // In-place Heap Sort algorithm (O(N log N) time, O(1) space)
    static void heapSort(std::vector<T>& arr, bool ascending = true) {
        int n = static_cast<int>(arr.size());
        if (n <= 1) return;

        // Step 1: Build Max-Heap in-place for ascending sort (or Min-Heap for descending)
        // Using lambda for max-heap condition
        auto heapify = [&](int heapSize, int rootIdx, auto& self) -> void {
            int target = rootIdx;
            int left = 2 * rootIdx + 1;
            int right = 2 * rootIdx + 2;

            if (ascending) {
                // Max-heap logic: parent >= child
                if (left < heapSize && arr[left] > arr[target]) target = left;
                if (right < heapSize && arr[right] > arr[target]) target = right;
            } else {
                // Min-heap logic: parent <= child
                if (left < heapSize && arr[left] < arr[target]) target = left;
                if (right < heapSize && arr[right] < arr[target]) target = right;
            }

            if (target != rootIdx) {
                std::swap(arr[rootIdx], arr[target]);
                self(heapSize, target, self);
            }
        };

        // Build heap (Floyd's algorithm)
        for (int i = (n / 2) - 1; i >= 0; i--) {
            heapify(n, i, heapify);
        }

        // Step 2: Repeatedly extract root to the sorted partition at the end
        for (int i = n - 1; i > 0; i--) {
            std::swap(arr[0], arr[i]);
            heapify(i, 0, heapify);
        }
    }
};

// Aliases for convenience
template <typename T>
using MinHeap = BinaryHeap<T, std::less<T>>;

template <typename T>
using MaxHeap = BinaryHeap<T, std::greater<T>>;

// -------------------------------------------------------------
// Practical Application: Priority Task Scheduler
// -------------------------------------------------------------
struct Task {
    std::string name;
    int priority; // Lower integer = higher priority
    int estimatedMinutes;

    bool operator<(const Task& other) const {
        return priority < other.priority; // For MinHeap: lower priority integer comes first
    }
    bool operator>(const Task& other) const {
        return priority > other.priority;
    }
};

std::ostream& operator<<(std::ostream& os, const Task& t) {
    os << "Task(" << t.name << ", Priority=" << t.priority << ", Time=" << t.estimatedMinutes << "m)";
    return os;
}

int main() {
    std::cout << "=== Binary Heap Comprehensive Test Harness ===\n\n";

    std::cout << "--- 1. Min-Heap Push & Pop Operations ---\n";
    MinHeap<int> minH;
    std::vector<int> values = {15, 10, 20, 8, 12, 25, 6, 17};
    for (int v : values) {
        minH.push(v);
    }

    std::cout << "Min-Heap Raw Array: ";
    minH.printRawArray();
    std::cout << "Min-Heap Tree Structure:\n";
    minH.printTree();
    std::cout << "Is valid min-heap? " << (minH.isHeap() ? "YES" : "NO") << "\n\n";

    std::cout << "Extracting top 3 minimum elements:\n";
    for (int i = 0; i < 3; i++) {
        std::cout << "  Popped min: " << minH.pop() << "\n";
    }
    std::cout << "Remaining Min-Heap Tree:\n";
    minH.printTree();
    std::cout << "Is valid min-heap? " << (minH.isHeap() ? "YES" : "NO") << "\n\n";

    std::cout << "--- 2. Floyd's O(N) buildHeap vs Naive Push ---\n";
    std::vector<int> unsorted = {45, 20, 14, 12, 31, 7, 11, 13, 7};
    MinHeap<int> floydHeap(unsorted);
    std::cout << "Heapified Array in O(N): ";
    floydHeap.printRawArray();
    std::cout << "Is valid min-heap? " << (floydHeap.isHeap() ? "YES" : "NO") << "\n\n";

    std::cout << "--- 3. Decrease-Key & Delete-Key Operations ---\n";
    std::cout << "Current Heap Array: ";
    floydHeap.printRawArray();
    std::cout << "Decreasing element at index 4 (originally 31) to 3...\n";
    floydHeap.decreaseKey(4, 3);
    std::cout << "New Top (should be 3): " << floydHeap.top() << "\n";
    floydHeap.printRawArray();
    std::cout << "Is valid min-heap? " << (floydHeap.isHeap() ? "YES" : "NO") << "\n\n";

    std::cout << "Deleting element at index 2...\n";
    floydHeap.deleteKey(2);
    floydHeap.printRawArray();
    std::cout << "Is valid min-heap? " << (floydHeap.isHeap() ? "YES" : "NO") << "\n\n";

    std::cout << "--- 4. In-Place Heap Sort (Ascending & Descending) ---\n";
    std::vector<int> sortArray = {64, 34, 25, 12, 22, 11, 90, 42, 8};
    std::cout << "Original Array: ";
    for (int x : sortArray) std::cout << x << " ";
    std::cout << "\n";

    BinaryHeap<int>::heapSort(sortArray, true);
    std::cout << "Sorted Ascending: ";
    for (int x : sortArray) std::cout << x << " ";
    std::cout << "\n";

    BinaryHeap<int>::heapSort(sortArray, false);
    std::cout << "Sorted Descending: ";
    for (int x : sortArray) std::cout << x << " ";
    std::cout << "\n\n";

    std::cout << "--- 5. Application: Real-Time Task Scheduler ---\n";
    MinHeap<Task> scheduler;
    scheduler.push({"System Kernel Flush", 0, 5});
    scheduler.push({"Backup Database", 3, 60});
    scheduler.push({"Render UI Frame", 1, 16});
    scheduler.push({"Poll Network Socket", 1, 10});
    scheduler.push({"Run Garbage Collector", 2, 25});

    std::cout << "Executing tasks by priority order:\n";
    while (!scheduler.empty()) {
        Task current = scheduler.pop();
        std::cout << "  [DISPATCHED] " << current << "\n";
    }

    std::cout << "\n=== All Binary Heap Tests Completed Successfully! ===\n";
    return 0;
}
```

---

## 📊 Complexity Analysis

| Operation | Average Case | Worst Case | Space Complexity | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Peek Top** | $O(1)$ | $O(1)$ | $O(1)$ | Inspect `data[0]` |
| **Push** | $O(1)$ amortized | $O(\log N)$ | $O(1)$ | Append + sift-up |
| **Pop** | $O(\log N)$ | $O(\log N)$ | $O(1)$ | Root replacement + sift-down |
| **Decrease Key** | $O(\log N)$ | $O(\log N)$ | $O(1)$ | Value reduction + sift-up |
| **Delete Key** | $O(\log N)$ | $O(\log N)$ | $O(1)$ | Swap with last + sift |
| **Build Heap** | $O(N)$ | $O(N)$ | $O(1)$ | Floyd's sift-down algorithm |
| **Heap Sort** | $O(N \log N)$ | $O(N \log N)$ | $O(1)$ | Optimal in-place sorting |

---

## 💡 Practical Engineering Insights

1. **Cache Locality vs Pointer Trees**:
   - Because all elements are laid out consecutively in an array, parent-child traversals enjoy spatial locality. However, as the heap size exceeds the L1/L2 cache capacity, jumps to index $2i$ span larger strides. In high-performance systems, **$d$-ary heaps** (e.g., 4-ary heaps) improve cache line utilization by packing 4 children into one cache line.
2. **Floyd's Algorithm vs Sequential Push**:
   - Never build a heap from an array by calling `push` $N$ times. Sequential insertion takes $O(N \log N)$ and incurs repeated vector reallocation. Floyd's bottom-up method takes $O(N)$ and does zero reallocations.
3. **Decrease-Key & Dijkstra's Algorithm**:
   - In graph algorithms like Dijkstra or Prim, vertices must be updated as shorter paths are discovered. To support $O(\log V)$ `decreaseKey`, maintain an auxiliary hash map or position array mapping `VertexId -> HeapIndex`.
