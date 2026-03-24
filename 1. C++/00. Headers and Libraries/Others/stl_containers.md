# STL Containers - Comprehensive Guide

This guide provides a comprehensive overview of all STL containers, their characteristics, use cases, and performance considerations.

## 📊 Container Overview

| Container | Category | Time Complexity | Memory | Ordered | Duplicates |
|-----------|----------|-----------------|--------|---------|------------|
| `vector` | Sequence | O(1) access, O(1) push_back | Contiguous | ✅ | ✅ |
| `deque` | Sequence | O(1) access, O(1) push_front/back | Non-contiguous | ✅ | ✅ |
| `list` | Sequence | O(n) access, O(1) insert/delete | Node-based | ✅ | ✅ |
| `forward_list` | Sequence | O(n) access, O(1) insert/delete | Node-based | ✅ | ✅ |
| `array` | Sequence | O(1) access | Contiguous | ✅ | ✅ |
| `set` | Associative | O(log n) all operations | Node-based | ✅ | ❌ |
| `multiset` | Associative | O(log n) all operations | Node-based | ✅ | ✅ |
| `map` | Associative | O(log n) all operations | Node-based | ✅ | ❌ (keys) |
| `multimap` | Associative | O(log n) all operations | Node-based | ✅ | ✅ (keys) |
| `unordered_set` | Associative | O(1) average | Hash table | ❌ | ❌ |
| `unordered_map` | Associative | O(1) average | Hash table | ❌ | ❌ (keys) |
| `stack` | Container Adapter | O(1) push/pop | Depends | ✅ | ✅ |
| `queue` | Container Adapter | O(1) push/pop | Depends | ✅ | ✅ |
| `priority_queue` | Container Adapter | O(log n) push, O(1) top | Depends | ❌ | ✅ |

## 🎮 Practical Examples

### Example 1: Container Selection Guide
```cpp
#include <iostream>
#include <vector>
#include <deque>
#include <list>
#include <forward_list>
#include <array>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <stack>
#include <queue>
#include <chrono>

class ContainerPerformance {
public:
    // Test vector performance (random access)
    static void testVector() {
        std::vector<int> vec;
        auto start = std::chrono::high_resolution_clock::now();
        
        for (int i = 0; i < 100000; i++) {
            vec.push_back(i);
        }
        
        // Random access test
        long long sum = 0;
        for (int i = 0; i < 100000; i++) {
            sum += vec[i];
        }
        
        auto end = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
        
        std::cout << "Vector (100k elements): " << duration.count() << " μs" << std::endl;
    }
    
    // Test list performance (frequent insertion/deletion)
    static void testList() {
        std::list<int> lst;
        auto start = std::chrono::high_resolution_clock::now();
        
        for (int i = 0; i < 10000; i++) {
            lst.push_back(i);
        }
        
        // Insert in middle
        auto it = lst.begin();
        std::advance(it, 5000);
        for (int i = 0; i < 1000; i++) {
            lst.insert(it, i);
        }
        
        auto end = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
        
        std::cout << "List (insertion test): " << duration.count() << " μs" << std::endl;
    }
    
    // Test unordered_map performance
    static void testUnorderedMap() {
        std::unordered_map<std::string, int> umap;
        auto start = std::chrono::high_resolution_clock::now();
        
        // Insert
        for (int i = 0; i < 10000; i++) {
            umap["key" + std::to_string(i)] = i;
        }
        
        // Lookup
        long long sum = 0;
        for (int i = 0; i < 10000; i++) {
            sum += umap["key" + std::to_string(i)];
        }
        
        auto end = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
        
        std::cout << "Unordered Map (10k ops): " << duration.count() << " μs" << std::endl;
    }
};

int main() {
    std::cout << "=== Container Performance Test ===" << std::endl;
    ContainerPerformance::testVector();
    ContainerPerformance::testList();
    ContainerPerformance::testUnorderedMap();
    
    return 0;
}
```

### Example 2: Real-World Container Usage Patterns
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <unordered_map>
#include <set>
#include <deque>

class DataProcessor {
private:
    std::vector<int> mainData;           // Main storage
    std::queue<int> processingQueue;     // FIFO processing
    std::stack<int> undoStack;           // Undo operations
    std::unordered_map<int, std::string> metadata;  // Quick lookups
    std::set<int> uniqueValues;          // Unique values only
    std::deque<int> slidingWindow;       // Sliding window algorithm
    
public:
    // Add data with metadata
    void addData(int value, const std::string& info) {
        mainData.push_back(value);
        metadata[value] = info;
        processingQueue.push(value);
        undoStack.push(value);
        uniqueValues.insert(value);
        
        // Maintain sliding window of last 5 elements
        slidingWindow.push_back(value);
        if (slidingWindow.size() > 5) {
            slidingWindow.pop_front();
        }
    }
    
    // Process data in FIFO order
    void processData() {
        while (!processingQueue.empty()) {
            int current = processingQueue.front();
            processingQueue.pop();
            
            std::cout << "Processing: " << current 
                      << " (" << metadata[current] << ")" << std::endl;
        }
    }
    
    // Undo last operation
    void undo() {
        if (!undoStack.empty()) {
            int last = undoStack.top();
            undoStack.pop();
            
            // Remove from main data
            auto it = std::find(mainData.begin(), mainData.end(), last);
            if (it != mainData.end()) {
                mainData.erase(it);
            }
            
            metadata.erase(last);
            uniqueValues.erase(last);
            
            std::cout << "Undone: " << last << std::endl;
        }
    }
    
    // Find max in sliding window
    int maxInSlidingWindow() {
        if (slidingWindow.empty()) return -1;
        return *std::max_element(slidingWindow.begin(), slidingWindow.end());
    }
    
    // Display all unique values
    void displayUnique() {
        std::cout << "Unique values: ";
        for (int val : uniqueValues) {
            std::cout << val << " ";
        }
        std::cout << std::endl;
    }
    
    // Display current state
    void displayState() {
        std::cout << "=== Current State ===" << std::endl;
        std::cout << "Main data size: " << mainData.size() << std::endl;
        std::cout << "Queue size: " << processingQueue.size() << std::endl;
        std::cout << "Undo stack size: " << undoStack.size() << std::endl;
        std::cout << "Unique values: " << uniqueValues.size() << std::endl;
        std::cout << "Sliding window: ";
        for (int val : slidingWindow) {
            std::cout << val << " ";
        }
        std::cout << std::endl;
    }
};

int main() {
    DataProcessor processor;
    
    // Add some data
    processor.addData(10, "First value");
    processor.addData(20, "Second value");
    processor.addData(15, "Third value");
    processor.addData(10, "Duplicate value");
    processor.addData(25, "Fourth value");
    
    processor.displayState();
    processor.displayUnique();
    
    std::cout << "Max in sliding window: " << processor.maxInSlidingWindow() << std::endl;
    
    // Process data
    processor.processData();
    
    // Undo operations
    processor.undo();
    processor.undo();
    
    processor.displayState();
    
    return 0;
}
```

### Example 3: Advanced Container Techniques
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <algorithm>
#include <iterator>

class AdvancedContainerTechniques {
public:
    // Custom comparator for map
    struct CustomCompare {
        bool operator()(const std::string& a, const std::string& b) const {
            return a.length() < b.length();  // Sort by string length
        }
    };
    
    void demonstrateCustomComparators() {
        std::map<std::string, int, CustomCompare> lengthMap;
        
        lengthMap["short"] = 1;
        lengthMap["medium"] = 2;
        lengthMap["very_long"] = 3;
        
        std::cout << "Map sorted by string length:" << std::endl;
        for (const auto& pair : lengthMap) {
            std::cout << pair.first << " (" << pair.second << ")" << std::endl;
        }
    }
    
    // Container of containers
    void demonstrateNestedContainers() {
        std::vector<std::vector<int>> matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        
        std::cout << "Matrix:" << std::endl;
        for (const auto& row : matrix) {
            for (int val : row) {
                std::cout << val << " ";
            }
            std::cout << std::endl;
        }
        
        // Map of vectors
        std::map<std::string, std::vector<int>> dataMap;
        dataMap["even"] = {2, 4, 6, 8};
        dataMap["odd"] = {1, 3, 5, 7};
        dataMap["primes"] = {2, 3, 5, 7, 11};
        
        std::cout << "\nData map:" << std::endl;
        for (const auto& pair : dataMap) {
            std::cout << pair.first << ": ";
            for (int val : pair.second) {
                std::cout << val << " ";
            }
            std::cout << std::endl;
        }
    }
    
    // Efficient container operations
    void demonstrateEfficientOperations() {
        std::vector<int> vec = {5, 2, 8, 1, 9, 3};
        
        // Efficient removal of elements
        vec.erase(
            std::remove_if(vec.begin(), vec.end(),
                          [](int x) { return x % 2 == 0; }),
            vec.end()
        );
        
        std::cout << "After removing evens: ";
        for (int val : vec) {
            std::cout << val << " ";
        }
        std::cout << std::endl;
        
        // Set operations
        std::set<int> set1 = {1, 2, 3, 4, 5};
        std::set<int> set2 = {4, 5, 6, 7, 8};
        
        std::vector<int> intersection;
        std::set_intersection(set1.begin(), set1.end(),
                             set2.begin(), set2.end(),
                             std::back_inserter(intersection));
        
        std::cout << "Intersection: ";
        for (int val : intersection) {
            std::cout << val << " ";
        }
        std::cout << std::endl;
    }
    
    // Memory-efficient container usage
    void demonstrateMemoryEfficiency() {
        // Reserve space to avoid reallocations
        std::vector<int> vec;
        vec.reserve(1000);  // Reserve space for 1000 elements
        
        for (int i = 0; i < 1000; i++) {
            vec.push_back(i);
        }
        
        std::cout << "Vector size: " << vec.size() << std::endl;
        std::cout << "Vector capacity: " << vec.capacity() << std::endl;
        
        // Shrink to fit when done
        vec.shrink_to_fit();
        std::cout << "After shrink_to_fit: " << vec.capacity() << std::endl;
        
        // Use unordered_map for better cache locality
        std::unordered_map<int, std::string> cache;
        cache.reserve(100);  // Reserve buckets
        
        for (int i = 0; i < 100; i++) {
            cache[i] = "Value " + std::to_string(i);
        }
        
        std::cout << "Unordered map bucket count: " << cache.bucket_count() << std::endl;
    }
};

int main() {
    AdvancedContainerTechniques demo;
    
    std::cout << "=== Custom Comparators ===" << std::endl;
    demo.demonstrateCustomComparators();
    
    std::cout << "\n=== Nested Containers ===" << std::endl;
    demo.demonstrateNestedContainers();
    
    std::cout << "\n=== Efficient Operations ===" << std::endl;
    demo.demonstrateEfficientOperations();
    
    std::cout << "\n=== Memory Efficiency ===" << std::endl;
    demo.demonstrateMemoryEfficiency();
    
    return 0;
}
```

## ⚡ Performance Guidelines

### When to Use Each Container

#### Vector
✅ **Use when:**
- Random access is frequent
- Elements are added/removed at the end
- Cache performance is important
- Memory overhead must be minimal

❌ **Avoid when:**
- Frequent insertion/deletion in middle
- Need stable iterators/pointers
- Elements are very large

#### Deque
✅ **Use when:**
- Need insertion at both ends
- Random access is required
- Memory fragmentation is a concern

❌ **Avoid when:**
- Maximum performance is critical
- Elements are very large

#### List
✅ **Use when:**
- Frequent insertion/deletion anywhere
- Iterator stability is required
- Splicing operations are needed

❌ **Avoid when:**
- Random access is frequent
- Memory overhead is a concern
- Cache performance is critical

#### Set/Map
✅ **Use when:**
- Need ordered storage
- Frequent lookups
- Need range queries

❌ **Avoid when:**
- Order doesn't matter (use unordered versions)
- Maximum performance is critical
- Memory overhead is a concern

#### Unordered Set/Map
✅ **Use when:**
- Order doesn't matter
- Maximum lookup performance is needed
- Average case performance is acceptable

❌ **Avoid when:**
- Worst-case performance must be guaranteed
- Need range queries
- Order is important

## 🎯 Best Practices

1. **Choose the right container** for your use case
2. **Reserve space** when you know the size beforehand
3. **Use emplace operations** for complex objects
4. **Prefer range-based for loops** for readability
5. **Understand iterator invalidation** rules
6. **Use appropriate algorithms** from `<algorithm>`

## 🐛 Common Pitfalls

1. **Using wrong container** for the use case
2. **Not reserving space** causing reallocations
3. **Iterator invalidation** during modifications
4. **Using ordered containers** when unordered would be better
5. **Memory leaks** with raw pointers in containers

---

**Examples in this file**: 3 comprehensive programs  
**Key Concepts**: Container selection, performance optimization, advanced techniques  
**Time Complexity**: Varies by container and operation  
**Space Complexity**: Varies by container
