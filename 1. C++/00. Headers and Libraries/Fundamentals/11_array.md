# 11_array.md - Fixed-Size Sequence Container

The `array` header provides `std::array`, a container that encapsulates fixed-size arrays with the performance of a C-style array but with the benefits of a standard container.

## 📖 Overview

`std::array` is a container that encapsulates static arrays with a fixed size known at compile time. It combines the performance and contiguous storage of C-style arrays with the interface and safety of STL containers.

## 🎯 Key Features

- **Fixed size** - Size determined at compile time
- **Contiguous storage** - Elements stored in contiguous memory
- **No dynamic allocation** - Stack allocation like C arrays
- **STL compatible** - Works with algorithms and iterators
- **Bounds checking** - `at()` method provides safe access
- **Zero overhead** - Same performance as C arrays

## 🔧 Basic Array Operations

### Creating and Initializing Arrays
```cpp
#include <iostream>
#include <array>
#include <algorithm>

int main() {
    // Different ways to create arrays
    
    // Aggregate initialization
    std::array<int, 5> arr1 = {1, 2, 3, 4, 5};
    
    // Default initialization (zero for built-in types)
    std::array<int, 5> arr2{};  // All elements are 0
    
    // Partial initialization
    std::array<int, 5> arr3 = {1, 2};  // {1, 2, 0, 0, 0}
    
    // Copy initialization
    std::array<int, 5> arr4 = arr1;
    
    // CTAD - Class Template Argument Deduction (C++17)
    std::array arr5 = {1, 2, 3, 4, 5};  // Deduces std::array<int, 5>
    
    return 0;
}
```

### Accessing Elements
```cpp
void demonstrateAccess() {
    std::array<int, 5> arr = {10, 20, 30, 40, 50};
    
    // Random access (no bounds checking)
    std::cout << "arr[2] = " << arr[2] << std::endl;  // 30
    
    // Safe access with bounds checking
    try {
        std::cout << "arr.at(2) = " << arr.at(2) << std::endl;  // 30
        std::cout << "arr.at(10) = " << arr.at(10) << std::endl; // Throws exception
    } catch (const std::out_of_range& e) {
        std::cout << "Out of range: " << e.what() << std::endl;
    }
    
    // Front and back access
    std::cout << "Front: " << arr.front() << std::endl;  // 10
    std::cout << "Back: " << arr.back() << std::endl;    // 50
    
    // Data pointer access
    int* ptr = arr.data();
    std::cout << "First element via data(): " << *ptr << std::endl;  // 10
}
```

### Array Properties
```cpp
void demonstrateProperties() {
    std::array<double, 10> arr = {1.1, 2.2, 3.3};
    
    std::cout << "Size: " << arr.size() << std::endl;           // 10
    std::cout << "Max size: " << arr.max_size() << std::endl;   // 10
    std::cout << "Empty: " << arr.empty() << std::endl;         // false
    
    // Size is known at compile time
    constexpr size_t size = std::array<int, 5>::size();  // Compile-time constant
    
    std::cout << "Compile-time size: " << size << std::endl;
}
```

## 🔧 Array Iteration and Algorithms

### Iterator-based Operations
```cpp
#include <algorithm>
#include <numeric>

void demonstrateIteration() {
    std::array<int, 5> arr = {5, 2, 8, 1, 3};
    
    // Range-based for loop
    std::cout << "Elements: ";
    for (int val : arr) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
    
    // Iterator loop
    std::cout << "Elements (iterator): ";
    for (auto it = arr.begin(); it != arr.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
    
    // Reverse iteration
    std::cout << "Elements (reverse): ";
    for (auto it = arr.rbegin(); it != arr.rend(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
}

void demonstrateAlgorithms() {
    std::array<int, 8> arr = {3, 1, 4, 1, 5, 9, 2, 6};
    
    // Sort
    std::sort(arr.begin(), arr.end());
    std::cout << "Sorted: ";
    for (int val : arr) std::cout << val << " ";
    std::cout << std::endl;
    
    // Reverse
    std::reverse(arr.begin(), arr.end());
    std::cout << "Reversed: ";
    for (int val : arr) std::cout << val << " ";
    std::cout << std::endl;
    
    // Find
    auto it = std::find(arr.begin(), arr.end(), 5);
    if (it != arr.end()) {
        std::cout << "Found 5 at position: " << std::distance(arr.begin(), it) << std::endl;
    }
    
    // Count
    int count = std::count(arr.begin(), arr.end(), 1);
    std::cout << "Count of 1s: " << count << std::endl;
    
    // Accumulate
    int sum = std::accumulate(arr.begin(), arr.end(), 0);
    std::cout << "Sum: " << sum << std::endl;
    
    // Min/Max
    auto [min_it, max_it] = std::minmax_element(arr.begin(), arr.end());
    std::cout << "Min: " << *min_it << ", Max: " << *max_it << std::endl;
}
```

### Array Filling and Transformation
```cpp
void demonstrateFilling() {
    std::array<int, 5> arr;
    
    // Fill with value
    arr.fill(42);
    std::cout << "After fill(42): ";
    for (int val : arr) std::cout << val << " ";
    std::cout << std::endl;
    
    // Generate sequence
    int counter = 1;
    std::generate(arr.begin(), arr.end(), [&counter]() { return counter++; });
    std::cout << "After generate: ";
    for (int val : arr) std::cout << val << " ";
    std::cout << std::endl;
    
    // Transform
    std::array<int, 5> doubled;
    std::transform(arr.begin(), arr.end(), doubled.begin(), 
                   [](int x) { return x * 2; });
    std::cout << "Doubled: ";
    for (int val : doubled) std::cout << val << " ";
    std::cout << std::endl;
}
```

## 🎮 Practical Examples

### Example 1: Mathematical Matrix Operations
```cpp
#include <iostream>
#include <array>
#include <algorithm>
#include <numeric>
#include <iomanip>

class Matrix {
private:
    static constexpr size_t ROWS = 3;
    static constexpr size_t COLS = 3;
    using Row = std::array<double, COLS>;
    using Data = std::array<Row, ROWS>;
    
    Data m_data;
    
public:
    // Constructor
    Matrix() {
        m_data.fill(Row{});  // Fill with zero-initialized rows
    }
    
    // Constructor with initializer list
    Matrix(std::initializer_list<std::initializer_list<double>> init) {
        size_t i = 0;
        for (const auto& row : init) {
            if (i >= ROWS) break;
            size_t j = 0;
            for (double val : row) {
                if (j >= COLS) break;
                m_data[i][j] = val;
                j++;
            }
            i++;
        }
    }
    
    // Access operators
    Row& operator[](size_t row) { return m_data[row]; }
    const Row& operator[](size_t row) const { return m_data[row]; }
    
    // Matrix addition
    Matrix operator+(const Matrix& other) const {
        Matrix result;
        for (size_t i = 0; i < ROWS; ++i) {
            for (size_t j = 0; j < COLS; ++j) {
                result[i][j] = m_data[i][j] + other[i][j];
            }
        }
        return result;
    }
    
    // Matrix subtraction
    Matrix operator-(const Matrix& other) const {
        Matrix result;
        for (size_t i = 0; i < ROWS; ++i) {
            for (size_t j = 0; j < COLS; ++j) {
                result[i][j] = m_data[i][j] - other[i][j];
            }
        }
        return result;
    }
    
    // Scalar multiplication
    Matrix operator*(double scalar) const {
        Matrix result;
        for (size_t i = 0; i < ROWS; ++i) {
            for (size_t j = 0; j < COLS; ++j) {
                result[i][j] = m_data[i][j] * scalar;
            }
        }
        return result;
    }
    
    // Matrix multiplication
    Matrix operator*(const Matrix& other) const {
        Matrix result;
        for (size_t i = 0; i < ROWS; ++i) {
            for (size_t j = 0; j < COLS; ++j) {
                for (size_t k = 0; k < COLS; ++k) {
                    result[i][j] += m_data[i][k] * other[k][j];
                }
            }
        }
        return result;
    }
    
    // Transpose
    Matrix transpose() const {
        Matrix result;
        for (size_t i = 0; i < ROWS; ++i) {
            for (size_t j = 0; j < COLS; ++j) {
                result[i][j] = m_data[j][i];
            }
        }
        return result;
    }
    
    // Determinant (for 3x3)
    double determinant() const {
        if constexpr (ROWS == 3 && COLS == 3) {
            return m_data[0][0] * (m_data[1][1] * m_data[2][2] - m_data[1][2] * m_data[2][1])
                 - m_data[0][1] * (m_data[1][0] * m_data[2][2] - m_data[1][2] * m_data[2][0])
                 + m_data[0][2] * (m_data[1][0] * m_data[2][1] - m_data[1][1] * m_data[2][0]);
        }
        return 0.0;
    }
    
    // Trace (sum of diagonal elements)
    double trace() const {
        double sum = 0.0;
        for (size_t i = 0; i < std::min(ROWS, COLS); ++i) {
            sum += m_data[i][i];
        }
        return sum;
    }
    
    // Check if matrix is symmetric
    bool isSymmetric() const {
        if constexpr (ROWS != COLS) return false;
        
        for (size_t i = 0; i < ROWS; ++i) {
            for (size_t j = i + 1; j < COLS; ++j) {
                if (std::abs(m_data[i][j] - m_data[j][i]) > 1e-10) {
                    return false;
                }
            }
        }
        return true;
    }
    
    // Display matrix
    void display(const std::string& name = "Matrix") const {
        std::cout << name << ":\n";
        for (const auto& row : m_data) {
            for (double val : row) {
                std::cout << std::setw(8) << std::fixed << std::setprecision(2) << val << " ";
            }
            std::cout << "\n";
        }
        std::cout << std::endl;
    }
    
    // Get dimensions
    static constexpr std::pair<size_t, size_t> dimensions() {
        return {ROWS, COLS};
    }
};

int main() {
    // Create matrices
    Matrix m1({{1, 2, 3},
               {4, 5, 6},
               {7, 8, 9}});
    
    Matrix m2({{9, 8, 7},
               {6, 5, 4},
               {3, 2, 1}});
    
    m1.display("Matrix 1");
    m2.display("Matrix 2");
    
    // Matrix operations
    Matrix sum = m1 + m2;
    sum.display("Sum");
    
    Matrix diff = m1 - m2;
    diff.display("Difference");
    
    Matrix product = m1 * m2;
    product.display("Product");
    
    Matrix scaled = m1 * 2.5;
    scaled.display("Scaled by 2.5");
    
    Matrix transposed = m1.transpose();
    transposed.display("Transpose of Matrix 1");
    
    // Properties
    std::cout << "Matrix 1 determinant: " << m1.determinant() << std::endl;
    std::cout << "Matrix 1 trace: " << m1.trace() << std::endl;
    std::cout << "Matrix 1 is symmetric: " << (m1.isSymmetric() ? "Yes" : "No") << std::endl;
    
    // Create symmetric matrix
    Matrix symmetric({{1, 2, 3},
                     {2, 5, 6},
                     {3, 6, 9}});
    symmetric.display("Symmetric Matrix");
    std::cout << "Is symmetric: " << (symmetric.isSymmetric() ? "Yes" : "No") << std::endl;
    
    return 0;
}
```

### Example 2: Data Processing Pipeline
```cpp
#include <iostream>
#include <array>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <vector>

class DataProcessor {
public:
    static constexpr size_t BUFFER_SIZE = 1024;
    using Buffer = std::array<double, BUFFER_SIZE>;
    
private:
    Buffer m_data;
    size_t m_count;
    
public:
    DataProcessor() : m_count(0) {
        m_data.fill(0.0);
    }
    
    // Add data point
    bool addData(double value) {
        if (m_count < BUFFER_SIZE) {
            m_data[m_count] = value;
            m_count++;
            return true;
        }
        return false;  // Buffer full
    }
    
    // Add multiple data points
    template<size_t N>
    size_t addData(const std::array<double, N>& values) {
        size_t added = 0;
        for (double value : values) {
            if (addData(value)) {
                added++;
            } else {
                break;
            }
        }
        return added;
    }
    
    // Get active data slice
    std::array<double, BUFFER_SIZE> getActiveData() const {
        std::array<double, BUFFER_SIZE> result;
        std::copy_n(m_data.begin(), m_count, result.begin());
        std::fill(result.begin() + m_count, result.end(), 0.0);
        return result;
    }
    
    // Calculate statistics
    struct Statistics {
        double mean;
        double variance;
        double std_dev;
        double min_val;
        double max_val;
        double median;
    };
    
    Statistics calculateStatistics() const {
        if (m_count == 0) {
            return {0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
        }
        
        // Create working copy
        std::array<double, BUFFER_SIZE> working = getActiveData();
        auto end = working.begin() + m_count;
        
        // Calculate mean
        double sum = std::accumulate(working.begin(), end, 0.0);
        double mean = sum / m_count;
        
        // Calculate variance
        double variance = 0.0;
        for (auto it = working.begin(); it != end; ++it) {
            variance += (*it - mean) * (*it - mean);
        }
        variance /= m_count;
        
        // Calculate min and max
        auto [min_it, max_it] = std::minmax_element(working.begin(), end);
        
        // Calculate median
        std::sort(working.begin(), end);
        double median;
        if (m_count % 2 == 0) {
            median = (working[m_count/2 - 1] + working[m_count/2]) / 2.0;
        } else {
            median = working[m_count/2];
        }
        
        return {
            mean,
            variance,
            std::sqrt(variance),
            *min_it,
            *max_it,
            median
        };
    }
    
    // Apply filter (remove outliers)
    size_t removeOutliers(double threshold = 2.0) {
        if (m_count == 0) return 0;
        
        auto stats = calculateStatistics();
        double lower_bound = stats.mean - threshold * stats.std_dev;
        double upper_bound = stats.mean + threshold * stats.std_dev;
        
        // Remove outliers
        auto new_end = std::remove_if(m_data.begin(), m_data.begin() + m_count,
            [lower_bound, upper_bound](double x) {
                return x < lower_bound || x > upper_bound;
            });
        
        size_t removed = m_count - (new_end - m_data.begin());
        m_count = new_end - m_data.begin();
        
        // Fill remaining positions with 0
        std::fill(m_data.begin() + m_count, m_data.end(), 0.0);
        
        return removed;
    }
    
    // Apply moving average filter
    void applyMovingAverage(size_t window_size) {
        if (window_size >= m_count || window_size == 0) return;
        
        std::array<double, BUFFER_SIZE> filtered;
        
        for (size_t i = 0; i < m_count; ++i) {
            size_t start = (i >= window_size) ? i - window_size : 0;
            size_t end = i + 1;
            
            double sum = 0.0;
            for (size_t j = start; j < end; ++j) {
                sum += m_data[j];
            }
            
            filtered[i] = sum / (end - start);
        }
        
        std::copy_n(filtered.begin(), m_count, m_data.begin());
    }
    
    // Normalize data to [0, 1] range
    void normalize() {
        if (m_count == 0) return;
        
        auto [min_it, max_it] = std::minmax_element(m_data.begin(), m_data.begin() + m_count);
        double min_val = *min_it;
        double max_val = *max_it;
        
        if (max_val == min_val) {
            // All values are the same
            std::fill(m_data.begin(), m_data.begin() + m_count, 0.5);
            return;
        }
        
        for (size_t i = 0; i < m_count; ++i) {
            m_data[i] = (m_data[i] - min_val) / (max_val - min_val);
        }
    }
    
    // Display data
    void display(size_t max_items = 20) const {
        std::cout << "Data (" << m_count << " items): ";
        
        size_t display_count = std::min(m_count, max_items);
        for (size_t i = 0; i < display_count; ++i) {
            std::cout << m_data[i] << " ";
        }
        
        if (m_count > max_items) {
            std::cout << "... (" << (m_count - max_items) << " more)";
        }
        std::cout << std::endl;
    }
    
    // Get count
    size_t count() const { return m_count; }
    
    // Clear data
    void clear() {
        m_data.fill(0.0);
        m_count = 0;
    }
};

int main() {
    DataProcessor processor;
    
    // Add sample data with some outliers
    std::array<double, 20> sample_data = {
        1.0, 1.2, 1.1, 0.9, 1.3,  // Normal data
        1.0, 1.1, 1.2, 0.8, 1.4,  // Normal data
        10.0,                      // Outlier
        1.1, 1.0, 1.3, 0.9, 1.2,  // Normal data
        -5.0,                      // Outlier
        1.1, 1.0                   // Normal data
    };
    
    processor.addData(sample_data);
    processor.display();
    
    // Calculate initial statistics
    auto stats = processor.calculateStatistics();
    std::cout << "\nInitial Statistics:" << std::endl;
    std::cout << "Mean: " << stats.mean << std::endl;
    std::cout << "Std Dev: " << stats.std_dev << std::endl;
    std::cout << "Min: " << stats.min_val << std::endl;
    std::cout << "Max: " << stats.max_val << std::endl;
    std::cout << "Median: " << stats.median << std::endl;
    
    // Remove outliers
    size_t removed = processor.removeOutliers(2.0);
    std::cout << "\nRemoved " << removed << " outliers" << std::endl;
    processor.display();
    
    // Calculate new statistics
    stats = processor.calculateStatistics();
    std::cout << "\nStatistics after outlier removal:" << std::endl;
    std::cout << "Mean: " << stats.mean << std::endl;
    std::cout << "Std Dev: " << stats.std_dev << std::endl;
    std::cout << "Min: " << stats.min_val << std::endl;
    std::cout << "Max: " << stats.max_val << std::endl;
    std::cout << "Median: " << stats.median << std::endl;
    
    // Apply moving average
    processor.applyMovingAverage(3);
    std::cout << "\nAfter moving average filter:" << std::endl;
    processor.display();
    
    // Normalize data
    processor.normalize();
    std::cout << "\nAfter normalization:" << std::endl;
    processor.display();
    
    return 0;
}
```

### Example 3: Fixed-Size Cache System
```cpp
#include <iostream>
#include <array>
#include <string>
#include <optional>
#include <algorithm>
#include <chrono>

template<typename Key, typename Value, size_t Size>
class FixedCache {
private:
    struct CacheEntry {
        Key key;
        Value value;
        std::chrono::steady_clock::time_point last_access;
        uint64_t access_count;
        
        CacheEntry(const Key& k, const Value& v) 
            : key(k), value(v), last_access(std::chrono::steady_clock::now()), access_count(1) {}
    };
    
    std::array<std::optional<CacheEntry>, Size> m_cache;
    size_t m_count;
    uint64_t m_total_accesses;
    uint64_t m_hits;
    
public:
    FixedCache() : m_count(0), m_total_accesses(0), m_hits(0) {
        m_cache.fill(std::nullopt);
    }
    
    // Insert or update a value
    bool put(const Key& key, const Value& value) {
        // Check if key already exists
        for (auto& entry : m_cache) {
            if (entry && entry->key == key) {
                entry->value = value;
                entry->last_access = std::chrono::steady_clock::now();
                entry->access_count++;
                return true;
            }
        }
        
        // Find empty slot
        for (auto& entry : m_cache) {
            if (!entry) {
                entry = CacheEntry(key, value);
                m_count++;
                return true;
            }
        }
        
        // Cache full, use LRU replacement
        evictLRU();
        return put(key, value);
    }
    
    // Get a value
    std::optional<Value> get(const Key& key) {
        m_total_accesses++;
        
        for (auto& entry : m_cache) {
            if (entry && entry->key == key) {
                entry->last_access = std::chrono::steady_clock::now();
                entry->access_count++;
                m_hits++;
                return entry->value;
            }
        }
        
        return std::nullopt;
    }
    
    // Check if key exists
    bool contains(const Key& key) const {
        for (const auto& entry : m_cache) {
            if (entry && entry->key == key) {
                return true;
            }
        }
        return false;
    }
    
    // Remove a key
    bool remove(const Key& key) {
        for (auto& entry : m_cache) {
            if (entry && entry->key == key) {
                entry = std::nullopt;
                m_count--;
                return true;
            }
        }
        return false;
    }
    
    // Clear cache
    void clear() {
        m_cache.fill(std::nullopt);
        m_count = 0;
        m_total_accesses = 0;
        m_hits = 0;
    }
    
    // Get cache statistics
    struct Statistics {
        size_t size;
        size_t capacity;
        double hit_rate;
        uint64_t total_accesses;
        uint64_t hits;
    };
    
    Statistics getStatistics() const {
        double hit_rate = (m_total_accesses > 0) ? 
            static_cast<double>(m_hits) / m_total_accesses : 0.0;
        
        return {
            m_count,
            Size,
            hit_rate,
            m_total_accesses,
            m_hits
        };
    }
    
    // Display cache contents
    void display() const {
        std::cout << "Cache Contents (" << m_count << "/" << Size << "):" << std::endl;
        
        for (size_t i = 0; i < Size; ++i) {
            const auto& entry = m_cache[i];
            if (entry) {
                auto now = std::chrono::steady_clock::now();
                auto age = std::chrono::duration_cast<std::chrono::seconds>(now - entry->last_access);
                
                std::cout << "  [" << i << "] Key: " << entry->key 
                          << ", Value: " << entry->value
                          << ", Accesses: " << entry->access_count
                          << ", Last access: " << age.count() << "s ago"
                          << std::endl;
            } else {
                std::cout << "  [" << i << "] Empty" << std::endl;
            }
        }
    }
    
    // Get most frequently accessed items
    std::vector<std::pair<Key, Value>> getMostFrequent(size_t count = 5) const {
        std::vector<std::pair<Key, uint64_t>> items;
        
        for (const auto& entry : m_cache) {
            if (entry) {
                items.emplace_back(entry->key, entry->access_count);
            }
        }
        
        std::sort(items.begin(), items.end(), 
                 [](const auto& a, const auto& b) { return a.second > b.second; });
        
        std::vector<std::pair<Key, Value>> result;
        for (size_t i = 0; i < std::min(count, items.size()); ++i) {
            if (auto value = get(items[i].first)) {
                result.emplace_back(items[i].first, *value);
            }
        }
        
        return result;
    }
    
private:
    // Evict least recently used item
    void evictLRU() {
        if (m_count == 0) return;
        
        auto oldest = m_cache.begin();
        for (auto it = m_cache.begin(); it != m_cache.end(); ++it) {
            if (*it && (!*oldest || it->last_access < oldest->last_access)) {
                oldest = it;
            }
        }
        
        if (*oldest) {
            std::cout << "Evicting LRU item: Key " << oldest->key << std::endl;
            *oldest = std::nullopt;
            m_count--;
        }
    }
};

int main() {
    FixedCache<std::string, int, 5> cache;
    
    // Test basic operations
    std::cout << "=== Basic Operations ===" << std::endl;
    cache.put("apple", 10);
    cache.put("banana", 20);
    cache.put("cherry", 30);
    
    if (auto value = cache.get("apple")) {
        std::cout << "Apple value: " << *value << std::endl;
    }
    
    if (auto value = cache.get("orange")) {
        std::cout << "Orange value: " << *value << std::endl;
    } else {
        std::cout << "Orange not found in cache" << std::endl;
    }
    
    cache.display();
    
    // Fill cache to capacity
    std::cout << "\n=== Filling Cache ===" << std::endl;
    cache.put("date", 40);
    cache.put("elderberry", 50);
    cache.display();
    
    // Add one more to trigger LRU eviction
    std::cout << "\n=== Triggering LRU Eviction ===" << std::endl;
    cache.put("fig", 60);
    cache.display();
    
    // Access some items multiple times
    std::cout << "\n=== Access Pattern ===" << std::endl;
    for (int i = 0; i < 3; ++i) {
        cache.get("banana");
        cache.get("cherry");
    }
    for (int i = 0; i < 5; ++i) {
        cache.get("fig");
    }
    
    // Show most frequent items
    auto frequent = cache.getMostFrequent(3);
    std::cout << "Most frequent items:" << std::endl;
    for (const auto& [key, value] : frequent) {
        std::cout << "  " << key << " = " << value << std::endl;
    }
    
    // Show final statistics
    auto stats = cache.getStatistics();
    std::cout << "\n=== Final Statistics ===" << std::endl;
    std::cout << "Size: " << stats.size << "/" << stats.capacity << std::endl;
    std::cout << "Hit rate: " << (stats.hit_rate * 100) << "%" << std::endl;
    std::cout << "Total accesses: " << stats.total_accesses << std::endl;
    std::cout << "Hits: " << stats.hits << std::endl;
    
    return 0;
}
```

### Example 4: Polynomial Operations
```cpp
#include <iostream>
#include <array>
#include <complex>
#include <algorithm>
#include <cmath>

template<size_t Degree>
class Polynomial {
public:
    static constexpr size_t degree = Degree;
    using Coefficient = double;
    using CoeffArray = std::array<Coefficient, Degree + 1>;
    
private:
    CoeffArray m_coeffs;
    
public:
    // Constructor
    Polynomial() {
        m_coeffs.fill(0.0);
    }
    
    // Constructor with coefficients
    Polynomial(const CoeffArray& coeffs) : m_coeffs(coeffs) {}
    
    // Constructor from initializer list
    Polynomial(std::initializer_list<Coefficient> coeffs) {
        m_coeffs.fill(0.0);
        std::copy_n(coeffs.begin(), std::min(coeffs.size(), Degree + 1), m_coeffs.begin());
    }
    
    // Access coefficient
    Coefficient& operator[](size_t index) { return m_coeffs[index]; }
    const Coefficient& operator[](size_t index) const { return m_coeffs[index]; }
    
    // Evaluate polynomial at x
    Coefficient evaluate(Coefficient x) const {
        Coefficient result = 0.0;
        Coefficient x_power = 1.0;
        
        for (Coefficient coeff : m_coeffs) {
            result += coeff * x_power;
            x_power *= x;
        }
        
        return result;
    }
    
    // Evaluate using Horner's method (more efficient)
    Coefficient evaluateHorner(Coefficient x) const {
        Coefficient result = m_coeffs[Degree];
        
        for (int i = Degree - 1; i >= 0; --i) {
            result = result * x + m_coeffs[i];
        }
        
        return result;
    }
    
    // Polynomial addition
    Polynomial operator+(const Polynomial& other) const {
        Polynomial result;
        for (size_t i = 0; i <= Degree; ++i) {
            result[i] = m_coeffs[i] + other[i];
        }
        return result;
    }
    
    // Polynomial subtraction
    Polynomial operator-(const Polynomial& other) const {
        Polynomial result;
        for (size_t i = 0; i <= Degree; ++i) {
            result[i] = m_coeffs[i] - other[i];
        }
        return result;
    }
    
    // Scalar multiplication
    Polynomial operator*(Coefficient scalar) const {
        Polynomial result;
        for (size_t i = 0; i <= Degree; ++i) {
            result[i] = m_coeffs[i] * scalar;
        }
        return result;
    }
    
    // Polynomial multiplication (returns higher degree polynomial)
    template<size_t OtherDegree>
    auto operator*(const Polynomial<OtherDegree>& other) const {
        constexpr size_t ResultDegree = Degree + OtherDegree;
        Polynomial<ResultDegree> result;
        
        for (size_t i = 0; i <= Degree; ++i) {
            for (size_t j = 0; j <= OtherDegree; ++j) {
                result[i + j] += m_coeffs[i] * other[j];
            }
        }
        
        return result;
    }
    
    // Derivative
    auto derivative() const {
        if constexpr (Degree == 0) {
            return Polynomial<0>{};
        } else {
            Polynomial<Degree - 1> result;
            for (size_t i = 1; i <= Degree; ++i) {
                result[i - 1] = m_coeffs[i] * i;
            }
            return result;
        }
    }
    
    // Integral (constant term is 0)
    auto integral() const {
        Polynomial<Degree + 1> result;
        for (size_t i = 0; i <= Degree; ++i) {
            result[i + 1] = m_coeffs[i] / (i + 1);
        }
        result[0] = 0.0;  // Constant of integration
        return result;
    }
    
    // Find roots using Newton's method (for real roots)
    std::vector<Coefficient> findRoots(int max_iterations = 100, Coefficient tolerance = 1e-10) const {
        std::vector<Coefficient> roots;
        
        if constexpr (Degree == 0) {
            return roots;  // Constant polynomial has no roots
        }
        
        // Try different initial guesses
        for (Coefficient guess = -10.0; guess <= 10.0; guess += 2.0) {
            Coefficient x = guess;
            auto deriv = derivative();
            
            for (int iter = 0; iter < max_iterations; ++iter) {
                Coefficient fx = evaluateHorner(x);
                Coefficient dfx = deriv.evaluateHorner(x);
                
                if (std::abs(dfx) < tolerance) break;
                
                Coefficient x_new = x - fx / dfx;
                
                if (std::abs(x_new - x) < tolerance) {
                    // Check if root is already found
                    bool found = false;
                    for (Coefficient root : roots) {
                        if (std::abs(root - x_new) < tolerance) {
                            found = true;
                            break;
                        }
                    }
                    
                    if (!found) {
                        roots.push_back(x_new);
                    }
                    break;
                }
                
                x = x_new;
            }
        }
        
        return roots;
    }
    
    // Calculate definite integral using Simpson's rule
    Coefficient integrateDefinite(Coefficient a, Coefficient b, int n = 1000) const {
        if (n % 2 != 0) n++;  // Make n even
        
        Coefficient h = (b - a) / n;
        auto integral_poly = integral();
        
        Coefficient result = integral_poly.evaluateHorner(b) - integral_poly.evaluateHorner(a);
        return result;
    }
    
    // Display polynomial
    void display(const std::string& name = "P(x)") const {
        std::cout << name << " = ";
        bool first_term = true;
        
        for (int i = Degree; i >= 0; --i) {
            if (std::abs(m_coeffs[i]) < 1e-10) continue;
            
            if (!first_term && m_coeffs[i] > 0) {
                std::cout << " + ";
            } else if (!first_term && m_coeffs[i] < 0) {
                std::cout << " - ";
            } else if (m_coeffs[i] < 0) {
                std::cout << "-";
            }
            
            Coefficient coeff = std::abs(m_coeffs[i]);
            
            if (!first_term || m_coeffs[i] < 0) {
                if (std::abs(coeff - 1.0) > 1e-10) {
                    std::cout << coeff;
                }
            } else {
                if (std::abs(coeff - 1.0) > 1e-10) {
                    std::cout << coeff;
                }
            }
            
            if (i == 0) {
                // Constant term
            } else if (i == 1) {
                std::cout << "x";
            } else {
                std::cout << "x^" << i;
            }
            
            first_term = false;
        }
        
        if (first_term) {
            std::cout << "0";
        }
        std::cout << std::endl;
    }
    
    // Get coefficients
    const CoeffArray& coefficients() const { return m_coeffs; }
};

int main() {
    // Create polynomials
    Polynomial<2> quad({1, -3, 2});  // x^2 - 3x + 2
    Polynomial<1> linear({2, -1});   // 2x - 1
    Polynomial<3> cubic({1, 0, -2, 1}); // x^3 - 2x + 1
    
    quad.display("P1(x) = x^2 - 3x + 2");
    linear.display("P2(x) = 2x - 1");
    cubic.display("P3(x) = x^3 - 2x + 1");
    
    // Evaluation
    std::cout << "\n=== Evaluation ===" << std::endl;
    std::cout << "P1(2) = " << quad.evaluate(2) << std::endl;
    std::cout << "P1(2) (Horner) = " << quad.evaluateHorner(2) << std::endl;
    std::cout << "P2(3) = " << linear.evaluate(3) << std::endl;
    std::cout << "P3(1) = " << cubic.evaluate(1) << std::endl;
    
    // Polynomial operations
    std::cout << "\n=== Operations ===" << std::endl;
    auto sum = quad + linear;
    sum.display("P1 + P2");
    
    auto diff = quad - linear;
    diff.display("P1 - P2");
    
    auto scaled = quad * 3.0;
    scaled.display("3 * P1");
    
    auto product = quad * linear;
    product.display("P1 * P2");
    
    // Derivatives and integrals
    std::cout << "\n=== Calculus ===" << std::endl;
    auto quad_deriv = quad.derivative();
    quad_deriv.display("P1'(x)");
    
    auto quad_integral = quad.integral();
    quad_integral.display("∫P1(x)dx");
    
    // Roots
    std::cout << "\n=== Roots ===" << std::endl;
    auto roots = quad.findRoots();
    std::cout << "Roots of P1: ";
    for (double root : roots) {
        std::cout << root << " ";
    }
    std::cout << std::endl;
    
    // Definite integral
    std::cout << "\n=== Definite Integral ===" << std::endl;
    double integral_value = quad.integrateDefinite(0, 2);
    std::cout << "∫[0,2] P1(x)dx = " << integral_value << std::endl;
    
    return 0;
}
```

## 📊 Complete Function Reference

### Member Functions
| Function | Description | Complexity |
|----------|-------------|------------|
| `at(index)` | Access with bounds checking | O(1) |
| `operator[]` | Random access | O(1) |
| `front()` | First element | O(1) |
| `back()` | Last element | O(1) |
| `data()` | Pointer to underlying array | O(1) |
| `size()` | Number of elements | O(1) |
| `empty()` | Check if empty | O(1) |
| `fill(value)` | Fill all elements | O(n) |
| `begin()/end()` | Iterators | O(1) |

### Iterators
| Iterator | Description |
|----------|-------------|
| `begin()/cbegin()` | Beginning iterator |
| `end()/cend()` | End iterator |
| `rbegin()/crbegin()` | Reverse beginning |
| `rend()/crend()` | Reverse end |

## ⚡ Performance Considerations

### Memory Layout
```cpp
// std::array has the same memory layout as C arrays
std::array<int, 5> arr = {1, 2, 3, 4, 5};
int c_arr[5] = {1, 2, 3, 4, 5};

// Both have the same size and alignment
static_assert(sizeof(arr) == sizeof(c_arr));
static_assert(alignof(arr) == alignof(c_arr));
```

### Compile-Time Benefits
```cpp
// Size is known at compile time
constexpr size_t SIZE = 10;
std::array<int, SIZE> arr;

// Can be used in constexpr contexts
constexpr std::array<int, 3> getArray() {
    return {1, 2, 3};
}

// Compile-time bounds checking with constexpr
constexpr bool checkBounds() {
    constexpr std::array<int, 3> arr = {1, 2, 3};
    return arr.at(2) == 3;  // Compile-time checked
}
```

## 🎯 Common Patterns

### Pattern 1: Fixed-Size Buffer
```cpp
class NetworkBuffer {
private:
    static constexpr size_t BUFFER_SIZE = 1024;
    std::array<uint8_t, BUFFER_SIZE> m_buffer;
    size_t m_used;
    
public:
    bool append(const uint8_t* data, size_t length) {
        if (m_used + length > BUFFER_SIZE) return false;
        
        std::copy_n(data, length, m_buffer.begin() + m_used);
        m_used += length;
        return true;
    }
};
```

### Pattern 2: Lookup Table
```cpp
class TrigTable {
private:
    static constexpr size_t TABLE_SIZE = 360;
    std::array<double, TABLE_SIZE> m_sin_table;
    std::array<double, TABLE_SIZE> m_cos_table;
    
public:
    TrigTable() {
        for (size_t i = 0; i < TABLE_SIZE; ++i) {
            double radians = i * M_PI / 180.0;
            m_sin_table[i] = std::sin(radians);
            m_cos_table[i] = std::cos(radians);
        }
    }
    
    double sin(int degrees) const {
        return m_sin_table[degrees % TABLE_SIZE];
    }
};
```

## 🐛 Common Pitfalls & Solutions

### 1. Size Must Be Known at Compile Time
```cpp
// Problem
int size;
std::cin >> size;
std::array<int, size> arr;  // Error: size not constant

// Solution
constexpr int MAX_SIZE = 100;
std::array<int, MAX_SIZE> arr;
// Or use std::vector for dynamic size
```

### 2. Forgetting to Initialize
```cpp
// Problem
std::array<int, 5> arr;  // Elements contain garbage values

// Solution
std::array<int, 5> arr{};  // All elements zero-initialized
std::array<int, 5> arr = {1, 2, 3};  // Partial initialization
```

### 3. Bounds Checking
```cpp
// Problem
std::array<int, 5> arr;
int val = arr[10];  // Undefined behavior

// Solution
try {
    int val = arr.at(10);  // Throws exception
} catch (const std::out_of_range& e) {
    std::cout << "Index out of range" << std::endl;
}
```

## 📚 Related Headers

- `vector.md` - Dynamic size array
- `algorithm.md` - Algorithms for arrays
- `numeric.md` - Numeric operations
- `iterator.md` - Iterator utilities

## 🚀 Best Practices

1. **Use `std::array`** instead of C arrays for better safety
2. **Prefer aggregate initialization** with `{}`
3. **Use `at()`** when bounds checking is needed
4. **Leverage STL algorithms** for array operations
5. **Use `constexpr`** for compile-time array operations
6. **Consider `std::vector`** when size is not known at compile time

## 🎯 When to Use std::array

✅ **Use std::array when:**
- Size is known at compile time
- You need stack allocation
- Performance is critical
- You want STL compatibility
- You need bounds checking option

❌ **Avoid when:**
- Size needs to change at runtime (use `std::vector`)
- You need very large arrays (consider heap allocation)
- You need dynamic resizing

---

**Examples in this file**: 4 complete programs  
**Key Functions**: `at()`, `fill()`, `size()`, `data()`, `begin()/end()`  
**Time Complexity**: O(1) access, O(n) fill/transform  
**Space Complexity**: O(n) where n is array size
