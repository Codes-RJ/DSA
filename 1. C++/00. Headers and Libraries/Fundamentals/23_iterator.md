# 23_iterator.md - Iterator Utilities

The `iterator` header provides helper utilities for working with iterators, including iterator adapters, distance calculations, and iterator category support.

## 📖 Overview

The `iterator` header contains essential utilities that make working with iterators easier and safer. It provides functions for moving iterators, calculating distances, and creating iterator adapters that work seamlessly with STL algorithms.

## 🎯 Key Features

- **Iterator movement** - Safe iterator advancement and retreat
- **Distance calculation** - Calculate distance between iterators
- **Iterator adapters** - Create specialized iterators (back_insert, front_insert, etc.)
- **Iterator categories** - Type traits for iterator capabilities
- **Stream iterators** - Connect iterators to I/O streams
- **Reverse iterators** - Iterate containers in reverse

## 🔧 Iterator Categories

### Iterator Tags
```cpp
#include <iostream>
#include <iterator>
#include <vector>
#include <list>
#include <forward_list>
#include <type_traits>

template<typename Iterator>
void printIteratorCategory(Iterator it) {
    if constexpr (std::is_same_v<typename std::iterator_traits<Iterator>::iterator_category, 
                                std::random_access_iterator_tag>) {
        std::cout << "Random Access Iterator" << std::endl;
    } else if constexpr (std::is_same_v<typename std::iterator_traits<Iterator>::iterator_category,
                                        std::bidirectional_iterator_tag>) {
        std::cout << "Bidirectional Iterator" << std::endl;
    } else if constexpr (std::is_same_v<typename std::iterator_traits<Iterator>::iterator_category,
                                        std::forward_iterator_tag>) {
        std::cout << "Forward Iterator" << std::endl;
    } else if constexpr (std::is_same_v<typename std::iterator_traits<Iterator>::iterator_category,
                                        std::input_iterator_tag>) {
        std::cout << "Input Iterator" << std::endl;
    } else if constexpr (std::is_same_v<typename std::iterator_traits<Iterator>::iterator_category,
                                        std::output_iterator_tag>) {
        std::cout << "Output Iterator" << std::endl;
    }
}

void demonstrateIteratorCategories() {
    std::cout << "=== Iterator Categories ===" << std::endl;
    
    std::vector<int> vec = {1, 2, 3};
    std::list<int> lst = {1, 2, 3};
    std::forward_list<int> fwd = {1, 2, 3};
    
    std::cout << "Vector iterator: ";
    printIteratorCategory(vec.begin());
    
    std::cout << "List iterator: ";
    printIteratorCategory(lst.begin());
    
    std::cout << "Forward list iterator: ";
    printIteratorCategory(fwd.begin());
}
```

### Iterator Movement Operations
```cpp
void demonstrateIteratorMovement() {
    std::cout << "\n=== Iterator Movement ===" << std::endl;
    
    std::vector<int> vec = {10, 20, 30, 40, 50};
    
    // distance - calculate distance between iterators
    auto dist = std::distance(vec.begin(), vec.end());
    std::cout << "Distance from begin to end: " << dist << std::endl;
    
    // advance - move iterator by n positions
    auto it = vec.begin();
    std::advance(it, 2);
    std::cout << "After advancing 2 positions: " << *it << std::endl;
    
    // next - get iterator advanced by n positions (doesn't modify original)
    auto it2 = std::next(vec.begin(), 3);
    std::cout << "Iterator 3 positions from begin: " << *it2 << std::endl;
    std::cout << "Original begin iterator still points to: " << *vec.begin() << std::endl;
    
    // prev - get iterator moved back by n positions
    auto it3 = std::prev(vec.end(), 2);
    std::cout << "Iterator 2 positions before end: " << *it3 << std::endl;
    
    // Note: advance works with bidirectional iterators
    auto list_it = std::list<int>{1, 2, 3, 4, 5}.begin();
    std::advance(list_it, 2);  // Works with list
    std::cout << "List iterator after advance: " << *list_it << std::endl;
}
```

## 🔧 Iterator Adapters

### Insert Iterators
```cpp
#include <iterator>
#include <vector>
#include <list>
#include <deque>
#include <algorithm>

void demonstrateInsertIterators() {
    std::cout << "\n=== Insert Iterators ===" << std::endl;
    
    // back_inserter - inserts at the end
    std::vector<int> vec = {1, 2, 3};
    std::vector<int> source = {4, 5, 6};
    
    std::copy(source.begin(), source.end(), std::back_inserter(vec));
    std::cout << "Vector after back_inserter: ";
    for (int x : vec) std::cout << x << " ";
    std::cout << std::endl;
    
    // front_inserter - inserts at the front (requires push_front)
    std::list<int> lst = {1, 2, 3};
    std::copy(source.begin(), source.end(), std::front_inserter(lst));
    std::cout << "List after front_inserter: ";
    for (int x : lst) std::cout << x << " ";
    std::cout << std::endl;
    
    // inserter - inserts at specific position
    std::deque<int> deq = {1, 2, 5};
    auto insert_pos = deq.begin() + 2;  // Insert before position 2
    std::copy(source.begin(), source.end(), std::inserter(deq, insert_pos));
    std::cout << "Deque after inserter: ";
    for (int x : deq) std::cout << x << " ";
    std::cout << std::endl;
}
```

### Stream Iterators
```cpp
#include <fstream>
#include <sstream>
#include <iterator>

void demonstrateStreamIterators() {
    std::cout << "\n=== Stream Iterators ===" << std::endl;
    
    // ostream_iterator - write to output stream
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    std::cout << "Writing to cout with ostream_iterator: ";
    std::copy(numbers.begin(), numbers.end(), 
              std::ostream_iterator<int>(std::cout, ", "));
    std::cout << std::endl;
    
    // istream_iterator - read from input stream
    std::istringstream input("10 20 30 40 50");
    std::vector<int> read_numbers;
    std::copy(std::istream_iterator<int>(input),
              std::istream_iterator<int>(),
              std::back_inserter(read_numbers));
    
    std::cout << "Read from stringstream: ";
    for (int x : read_numbers) std::cout << x << " ";
    std::cout << std::endl;
    
    // Writing to file with ostream_iterator
    std::ofstream outfile("temp_output.txt");
    if (outfile) {
        std::copy(numbers.begin(), numbers.end(),
                  std::ostream_iterator<int>(outfile, "\n"));
        outfile.close();
        std::cout << "Numbers written to file" << std::endl;
    }
    
    // Reading from file with istream_iterator
    std::ifstream infile("temp_output.txt");
    if (infile) {
        std::vector<int> file_numbers;
        std::copy(std::istream_iterator<int>(infile),
                  std::istream_iterator<int>(),
                  std::back_inserter(file_numbers));
        std::cout << "Numbers read from file: ";
        for (int x : file_numbers) std::cout << x << " ";
        std::cout << std::endl;
        infile.close();
    }
}
```

### Reverse Iterators
```cpp
void demonstrateReverseIterators() {
    std::cout << "\n=== Reverse Iterators ===" << std::endl;
    
    std::vector<int> vec = {1, 2, 3, 4, 5};
    
    // Using rbegin() and rend()
    std::cout << "Vector in reverse: ";
    for (auto it = vec.rbegin(); it != vec.rend(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
    
    // reverse_iterator adapter
    std::cout << "Using reverse_iterator: ";
    std::reverse_iterator<std::vector<int>::iterator> rev_it(vec.end());
    std::reverse_iterator<std::vector<int>::iterator> rev_end(vec.begin());
    
    for (; rev_it != rev_end; ++rev_it) {
        std::cout << *rev_it << " ";
    }
    std::cout << std::endl;
    
    // Algorithms with reverse iterators
    std::cout << "Reverse copy using algorithms: ";
    std::vector<int> reversed;
    std::copy(vec.rbegin(), vec.rend(), std::back_inserter(reversed));
    for (int x : reversed) std::cout << x << " ";
    std::cout << std::endl;
    
    // Converting reverse iterator to regular iterator
    auto rev_it2 = vec.rbegin();
    auto normal_it = rev_it2.base();
    std::cout << "Reverse iterator points to: " << *rev_it2 << std::endl;
    std::cout << "Base iterator points to: " << *normal_it << std::endl;
    std::cout << "Base iterator - 1 points to: " << *(normal_it - 1) << std::endl;
}
```

## 🔧 Custom Iterators

### Simple Custom Iterator
```cpp
template<typename T>
class RangeIterator {
private:
    T current;
    T step;
    
public:
    using iterator_category = std::forward_iterator_tag;
    using value_type = T;
    using difference_type = std::ptrdiff_t;
    using pointer = const T*;
    using reference = const T&;
    
    RangeIterator(T start, T s = 1) : current(start), step(s) {}
    
    reference operator*() const { return current; }
    pointer operator->() const { return &current; }
    
    RangeIterator& operator++() {
        current += step;
        return *this;
    }
    
    RangeIterator operator++(int) {
        RangeIterator tmp = *this;
        current += step;
        return tmp;
    }
    
    bool operator==(const RangeIterator& other) const {
        return current == other.current;
    }
    
    bool operator!=(const RangeIterator& other) const {
        return current != other.current;
    }
};

template<typename T>
class Range {
private:
    T start, end, step;
    
public:
    Range(T s, T e, T st = 1) : start(s), end(e), step(st) {}
    
    RangeIterator<T> begin() const {
        return RangeIterator<T>(start, step);
    }
    
    RangeIterator<T> end() const {
        return RangeIterator<T>(end, step);
    }
};

void demonstrateCustomIterator() {
    std::cout << "\n=== Custom Iterator ===" << std::endl;
    
    // Use custom range with range-based for loop
    std::cout << "Range 1 to 5: ";
    for (int x : Range<int>(1, 6)) {
        std::cout << x << " ";
    }
    std::cout << std::endl;
    
    std::cout << "Range 0 to 10 step 2: ";
    for (int x : Range<int>(0, 11, 2)) {
        std::cout << x << " ";
    }
    std::cout << std::endl;
    
    // Use with STL algorithms
    std::vector<int> result;
    std::copy(Range<int>(5, 11).begin(), Range<int>(5, 11).end(),
              std::back_inserter(result));
    
    std::cout << "Copied to vector: ";
    for (int x : result) std::cout << x << " ";
    std::cout << std::endl;
}
```

### Filter Iterator
```cpp
template<typename Iterator, typename Predicate>
class FilterIterator {
private:
    Iterator current;
    Iterator end;
    Predicate pred;
    
    void findNextValid() {
        while (current != end && !pred(*current)) {
            ++current;
        }
    }
    
public:
    using iterator_category = std::forward_iterator_tag;
    using value_type = typename std::iterator_traits<Iterator>::value_type;
    using difference_type = typename std::iterator_traits<Iterator>::difference_type;
    using pointer = typename std::iterator_traits<Iterator>::pointer;
    using reference = typename std::iterator_traits<Iterator>::reference;
    
    FilterIterator(Iterator begin, Iterator end, Predicate p) 
        : current(begin), end(end), pred(p) {
        findNextValid();
    }
    
    reference operator*() const { return *current; }
    pointer operator->() const { return &*current; }
    
    FilterIterator& operator++() {
        ++current;
        findNextValid();
        return *this;
    }
    
    FilterIterator operator++(int) {
        FilterIterator tmp = *this;
        ++current;
        findNextValid();
        return tmp;
    }
    
    bool operator==(const FilterIterator& other) const {
        return current == other.current;
    }
    
    bool operator!=(const FilterIterator& other) const {
        return current != other.current;
    }
};

template<typename Container, typename Predicate>
auto make_filter_range(Container& container, Predicate pred) {
    return std::make_pair(
        FilterIterator(container.begin(), container.end(), pred),
        FilterIterator(container.end(), container.end(), pred)
    );
}

void demonstrateFilterIterator() {
    std::cout << "\n=== Filter Iterator ===" << std::endl;
    
    std::vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    // Filter even numbers
    auto is_even = [](int x) { return x % 2 == 0; };
    
    std::cout << "Even numbers: ";
    auto even_range = make_filter_range(numbers, is_even);
    for (auto it = even_range.first; it != even_range.second; ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
    
    // Filter numbers greater than 5
    auto greater_than_5 = [](int x) { return x > 5; };
    
    std::cout << "Numbers > 5: ";
    auto gt5_range = make_filter_range(numbers, greater_than_5);
    for (auto it = gt5_range.first; it != gt5_range.second; ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
}
```

## 🎮 Practical Examples

### Example 1: File Processing Pipeline
```cpp
#include <iostream>
#include <iterator>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>

class TextFileProcessor {
private:
    std::string filename;
    
public:
    TextFileProcessor(const std::string& file) : filename(file) {}
    
    // Read all lines from file
    std::vector<std::string> readLines() {
        std::ifstream file(filename);
        std::vector<std::string> lines;
        
        if (file) {
            std::copy(std::istream_iterator<std::string>(file),
                      std::istream_iterator<std::string>(),
                      std::back_inserter(lines));
        }
        
        return lines;
    }
    
    // Filter lines containing specific keyword
    std::vector<std::string> filterLines(const std::vector<std::string>& lines,
                                         const std::string& keyword) {
        std::vector<std::string> filtered;
        
        std::copy_if(lines.begin(), lines.end(),
                    std::back_inserter(filtered),
                    [&keyword](const std::string& line) {
                        return line.find(keyword) != std::string::npos;
                    });
        
        return filtered;
    }
    
    // Transform lines to uppercase
    std::vector<std::string> toUpper(const std::vector<std::string>& lines) {
        std::vector<std::string> upper_lines;
        
        std::transform(lines.begin(), lines.end(),
                      std::back_inserter(upper_lines),
                      [](const std::string& line) {
                          std::string upper = line;
                          std::transform(upper.begin(), upper.end(),
                                        upper.begin(), ::toupper);
                          return upper;
                      });
        
        return upper_lines;
    }
    
    // Write lines to file
    void writeLines(const std::vector<std::string>& lines, 
                   const std::string& output_file) {
        std::ofstream out(output_file);
        if (out) {
            std::copy(lines.begin(), lines.end(),
                      std::ostream_iterator<std::string>(out, "\n"));
        }
    }
    
    // Process pipeline
    void process(const std::string& keyword, const std::string& output_file) {
        std::cout << "Processing file: " << filename << std::endl;
        
        // Read
        auto lines = readLines();
        std::cout << "Read " << lines.size() << " lines" << std::endl;
        
        // Filter
        auto filtered = filterLines(lines, keyword);
        std::cout << "Filtered to " << filtered.size() << " lines containing '" 
                  << keyword << "'" << std::endl;
        
        // Transform
        auto upper = toUpper(filtered);
        
        // Write
        writeLines(upper, output_file);
        std::cout << "Wrote results to: " << output_file << std::endl;
    }
};

int main() {
    std::cout << "=== File Processing Pipeline ===" << std::endl;
    
    // Create a sample file
    std::ofstream sample_file("sample.txt");
    sample_file << "Hello world\n";
    sample_file << "This is a test file\n";
    sample_file << "Testing iterators\n";
    sample_file << "Hello again\n";
    sample_file << "Final line\n";
    sample_file.close();
    
    TextFileProcessor processor("sample.txt");
    processor.process("Hello", "output.txt");
    
    // Show output
    std::ifstream output("output.txt");
    std::cout << "\nOutput file content:" << std::endl;
    std::copy(std::istream_iterator<char>(output),
              std::istream_iterator<char>(),
              std::ostream_iterator<char>(std::cout));
    
    return 0;
}
```

### Example 2: Data Aggregation with Iterators
```cpp
#include <iostream>
#include <iterator>
#include <vector>
#include <numeric>
#include <algorithm>
#include <complex>

class DataAnalyzer {
private:
    std::vector<double> data;
    
public:
    DataAnalyzer(const std::vector<double>& d) : data(d) {}
    
    // Calculate moving average
    std::vector<double> movingAverage(size_t window_size) {
        std::vector<double> averages;
        
        if (window_size == 0 || window_size > data.size()) {
            return averages;
        }
        
        for (size_t i = 0; i <= data.size() - window_size; ++i) {
            double sum = std::accumulate(data.begin() + i, 
                                       data.begin() + i + window_size, 0.0);
            averages.push_back(sum / window_size);
        }
        
        return averages;
    }
    
    // Find local maxima
    std::vector<size_t> findLocalMaxima() {
        std::vector<size_t> maxima;
        
        if (data.size() < 3) {
            return maxima;
        }
        
        for (size_t i = 1; i < data.size() - 1; ++i) {
            if (data[i] > data[i-1] && data[i] > data[i+1]) {
                maxima.push_back(i);
            }
        }
        
        return maxima;
    }
    
    // Calculate differences between consecutive elements
    std::vector<double> differences() {
        std::vector<double> diffs;
        
        if (data.size() < 2) {
            return diffs;
        }
        
        std::adjacent_difference(data.begin(), data.end(),
                                std::back_inserter(diffs));
        
        // Remove first element (it's just the first value)
        if (!diffs.empty()) {
            diffs.erase(diffs.begin());
        }
        
        return diffs;
    }
    
    // Group data into chunks
    std::vector<std::vector<double>> chunk(size_t chunk_size) {
        std::vector<std::vector<double>> chunks;
        
        for (auto it = data.begin(); it != data.end(); 
             std::advance(it, std::min(chunk_size, 
                                      static_cast<size_t>(std::distance(it, data.end()))))) {
            auto end_it = it;
            std::advance(end_it, std::min(chunk_size, 
                                         static_cast<size_t>(std::distance(it, data.end()))));
            
            chunks.emplace_back(it, end_it);
        }
        
        return chunks;
    }
    
    // Display data
    void displayData(const std::string& label) const {
        std::cout << label << ": ";
        std::copy(data.begin(), data.end(),
                  std::ostream_iterator<double>(std::cout, " "));
        std::cout << std::endl;
    }
    
    // Display vector
    static void displayVector(const std::vector<double>& vec, 
                             const std::string& label) {
        std::cout << label << ": ";
        std::copy(vec.begin(), vec.end(),
                  std::ostream_iterator<double>(std::cout, " "));
        std::cout << std::endl;
    }
    
    static void displayVector(const std::vector<size_t>& vec, 
                             const std::string& label) {
        std::cout << label << ": ";
        std::copy(vec.begin(), vec.end(),
                  std::ostream_iterator<size_t>(std::cout, " "));
        std::cout << std::endl;
    }
};

int main() {
    std::cout << "=== Data Aggregation with Iterators ===" << std::endl;
    
    std::vector<double> data = {1.0, 3.0, 2.0, 5.0, 4.0, 7.0, 3.0, 8.0, 6.0, 9.0};
    DataAnalyzer analyzer(data);
    
    analyzer.displayData("Original data");
    
    // Moving average
    auto moving_avg = analyzer.movingAverage(3);
    DataAnalyzer::displayVector(moving_avg, "Moving average (window=3)");
    
    // Local maxima
    auto maxima = analyzer.findLocalMaxima();
    DataAnalyzer::displayVector(maxima, "Local maxima indices");
    
    // Differences
    auto diffs = analyzer.differences();
    DataAnalyzer::displayVector(diffs, "Differences");
    
    // Chunks
    auto chunks = analyzer.chunk(3);
    std::cout << "Data chunks (size=3):" << std::endl;
    for (size_t i = 0; i < chunks.size(); ++i) {
        std::cout << "  Chunk " << i << ": ";
        std::copy(chunks[i].begin(), chunks[i].end(),
                  std::ostream_iterator<double>(std::cout, " "));
        std::cout << std::endl;
    }
    
    return 0;
}
```

### Example 3: Custom Container with Iterators
```cpp
#include <iostream>
#include <iterator>
#include <vector>
#include <algorithm>

template<typename T>
class CircularBuffer {
private:
    std::vector<T> buffer;
    size_t head;
    size_t tail;
    size_t count;
    bool full;
    
public:
    CircularBuffer(size_t capacity) 
        : buffer(capacity), head(0), tail(0), count(0), full(false) {}
    
    void push(const T& item) {
        buffer[head] = item;
        
        if (full) {
            tail = (tail + 1) % buffer.size();
        } else {
            count++;
        }
        
        head = (head + 1) % buffer.size();
        full = count == buffer.size();
    }
    
    size_t size() const { return count; }
    size_t capacity() const { return buffer.size(); }
    bool isFull() const { return full; }
    bool isEmpty() const { return count == 0; }
    
    // Iterator implementation
    class Iterator {
    private:
        const CircularBuffer* cb;
        size_t index;
        size_t position;
        
    public:
        using iterator_category = std::forward_iterator_tag;
        using value_type = T;
        using difference_type = std::ptrdiff_t;
        using pointer = const T*;
        using reference = const T&;
        
        Iterator(const CircularBuffer* buffer, size_t idx, size_t pos)
            : cb(buffer), index(idx), position(pos) {}
        
        reference operator*() const {
            return cb->buffer[index];
        }
        
        pointer operator->() const {
            return &cb->buffer[index];
        }
        
        Iterator& operator++() {
            if (position < cb->count) {
                index = (index + 1) % cb->buffer.size();
                position++;
            }
            return *this;
        }
        
        Iterator operator++(int) {
            Iterator tmp = *this;
            ++(*this);
            return tmp;
        }
        
        bool operator==(const Iterator& other) const {
            return position == other.position;
        }
        
        bool operator!=(const Iterator& other) const {
            return position != other.position;
        }
    };
    
    Iterator begin() const {
        if (isEmpty()) {
            return end();
        }
        
        size_t start_index = full ? head : 0;
        return Iterator(this, start_index, 0);
    }
    
    Iterator end() const {
        return Iterator(this, head, count);
    }
};

int main() {
    std::cout << "=== Custom Container with Iterators ===" << std::endl;
    
    CircularBuffer<int> buffer(5);
    
    // Add elements
    for (int i = 1; i <= 8; ++i) {
        buffer.push(i);
        std::cout << "Pushed " << i << ", buffer size: " << buffer.size() 
                  << ", full: " << (buffer.isFull() ? "yes" : "no") << std::endl;
    }
    
    // Iterate using range-based for loop
    std::cout << "Buffer contents: ";
    for (int x : buffer) {
        std::cout << x << " ";
    }
    std::cout << std::endl;
    
    // Use with STL algorithms
    std::vector<int> copy;
    std::copy(buffer.begin(), buffer.end(), std::back_inserter(copy));
    
    std::cout << "Copied to vector: ";
    for (int x : copy) std::cout << x << " ";
    std::cout << std::endl;
    
    // Find elements
    auto it = std::find(buffer.begin(), buffer.end(), 6);
    if (it != buffer.end()) {
        std::cout << "Found 6 in buffer" << std::endl;
    }
    
    // Count elements
    auto count = std::count(buffer.begin(), buffer.end(), 4);
    std::cout << "Count of 4: " << count << std::endl;
    
    // Calculate sum
    auto sum = std::accumulate(buffer.begin(), buffer.end(), 0);
    std::cout << "Sum of elements: " << sum << std::endl;
    
    return 0;
}
```

### Example 4: Iterator-Based Data Processing
```cpp
#include <iostream>
#include <iterator>
#include <vector>
#include <list>
#include <algorithm>
#include <random>
#include <chrono>

class DataProcessor {
private:
    std::mt19937 rng;
    
public:
    DataProcessor() : rng(std::chrono::steady_clock::now().time_since_epoch().count()) {}
    
    // Generate random data
    std::vector<int> generateRandomData(size_t count, int min_val, int max_val) {
        std::uniform_int_distribution<int> dist(min_val, max_val);
        std::vector<int> data(count);
        
        std::generate(data.begin(), data.end(),
                     [this, &dist]() { return dist(rng); });
        
        return data;
    }
    
    // Process data pipeline
    template<typename InputIt, typename OutputIt>
    void processData(InputIt first, InputIt last, OutputIt result) {
        // Step 1: Filter out negative numbers
        std::vector<int> filtered;
        std::copy_if(first, last, std::back_inserter(filtered),
                    [](int x) { return x >= 0; });
        
        // Step 2: Square each number
        std::vector<int> squared;
        std::transform(filtered.begin(), filtered.end(),
                      std::back_inserter(squared),
                      [](int x) { return x * x; });
        
        // Step 3: Sort
        std::sort(squared.begin(), squared.end());
        
        // Step 4: Remove duplicates
        auto unique_end = std::unique(squared.begin(), squared.end());
        squared.erase(unique_end, squared.end());
        
        // Step 5: Copy to result
        std::copy(squared.begin(), squared.end(), result);
    }
    
    // Benchmark different container types
    void benchmarkContainers() {
        std::cout << "=== Container Performance Benchmark ===" << std::endl;
        
        const size_t data_size = 100000;
        auto data = generateRandomData(data_size, -1000, 1000);
        
        // Vector processing
        auto start = std::chrono::high_resolution_clock::now();
        std::vector<int> vec_result;
        processData(data.begin(), data.end(), std::back_inserter(vec_result));
        auto end = std::chrono::high_resolution_clock::now();
        auto vec_time = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
        
        // List processing
        start = std::chrono::high_resolution_clock::now();
        std::list<int> lst_result;
        processData(data.begin(), data.end(), std::back_inserter(lst_result));
        end = std::chrono::high_resolution_clock::now();
        auto lst_time = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
        
        std::cout << "Vector processing time: " << vec_time.count() << " μs" << std::endl;
        std::cout << "List processing time: " << lst_time.count() << " μs" << std::endl;
        std::cout << "Vector result size: " << vec_result.size() << std::endl;
        std::cout << "List result size: " << lst_result.size() << std::endl;
    }
    
    // Demonstrate iterator invalidation safety
    void demonstrateIteratorSafety() {
        std::cout << "\n=== Iterator Safety ===" << std::endl;
        
        std::vector<int> data = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        
        // Safe way to remove elements while iterating
        std::cout << "Original: ";
        std::copy(data.begin(), data.end(),
                  std::ostream_iterator<int>(std::cout, " "));
        std::cout << std::endl;
        
        // Remove even numbers safely
        auto new_end = std::remove_if(data.begin(), data.end(),
                                    [](int x) { return x % 2 == 0; });
        data.erase(new_end, data.end());
        
        std::cout << "After removing evens: ";
        std::copy(data.begin(), data.end(),
                  std::ostream_iterator<int>(std::cout, " "));
        std::cout << std::endl;
        
        // Using iterator operations safely
        auto it = std::find(data.begin(), data.end(), 5);
        if (it != data.end()) {
            std::cout << "Found 5 at position: " 
                      << std::distance(data.begin(), it) << std::endl;
            
            // Advance safely
            std::advance(it, 2);
            if (it != data.end()) {
                std::cout << "Two positions ahead: " << *it << std::endl;
            }
        }
    }
};

int main() {
    std::cout << "=== Iterator-Based Data Processing ===" << std::endl;
    
    DataProcessor processor;
    
    // Generate and process data
    auto data = processor.generateRandomData(20, -10, 10);
    
    std::cout << "Generated data: ";
    std::copy(data.begin(), data.end(),
              std::ostream_iterator<int>(std::cout, " "));
    std::cout << std::endl;
    
    // Process data
    std::vector<int> result;
    processor.processData(data.begin(), data.end(), std::back_inserter(result));
    
    std::cout << "Processed result: ";
    std::copy(result.begin(), result.end(),
              std::ostream_iterator<int>(std::cout, " "));
    std::cout << std::endl;
    
    // Benchmark
    processor.benchmarkContainers();
    
    // Iterator safety
    processor.demonstrateIteratorSafety();
    
    return 0;
}
```

## 📊 Complete Function Reference

### Iterator Movement
| Function | Description | Iterator Category |
|----------|-------------|------------------|
| `advance(it, n)` | Move iterator by n positions | Input, Forward, Bidirectional, Random |
| `distance(first, last)` | Calculate distance between iterators | Input, Forward, Bidirectional, Random |
| `next(it, n)` | Return iterator advanced by n | Input, Forward, Bidirectional, Random |
| `prev(it, n)` | Return iterator moved back by n | Bidirectional, Random |

### Iterator Adapters
| Function | Description | Requirements |
|----------|-------------|-------------|
| `back_inserter(container)` | Creates back insert iterator | Container has `push_back` |
| `front_inserter(container)` | Creates front insert iterator | Container has `push_front` |
| `inserter(container, pos)` | Creates insert iterator at position | Container has `insert` |
| `reverse_iterator(it)` | Creates reverse iterator | Bidirectional or Random |

### Stream Iterators
| Function | Description | Direction |
|----------|-------------|----------|
| `istream_iterator<T>()` | Input stream iterator | Input |
| `ostream_iterator<T>(stream, delim)` | Output stream iterator | Output |
| `istreambuf_iterator<C>()` | Stream buffer input iterator | Input |
| `ostreambuf_iterator<C>(stream)` | Stream buffer output iterator | Output |

## ⚡ Performance Considerations

### Iterator Category Performance
```cpp
// Random access iterators - O(1) movement
std::vector<int>::iterator vec_it;
std::advance(vec_it, 1000);  // O(1)

// Bidirectional iterators - O(n) movement
std::list<int>::iterator list_it;
std::advance(list_it, 1000); // O(1000)
```

### Cache Locality
```cpp
// Vector iterators - good cache locality
std::vector<int> vec = /* ... */;
for (auto it = vec.begin(); it != vec.end(); ++it) {
    // Sequential memory access
}

// List iterators - poor cache locality
std::list<int> lst = /* ... */;
for (auto it = lst.begin(); it != lst.end(); ++it) {
    // Random memory access
}
```

## 🎯 Common Patterns

### Pattern 1: Safe Container Modification
```cpp
// Remove elements while iterating
container.erase(
    std::remove_if(container.begin(), container.end(), predicate),
    container.end()
);
```

### Pattern 2: Iterator-Based Output
```cpp
// Write to any output iterator
template<typename OutputIt>
void generateNumbers(OutputIt out, int count) {
    for (int i = 0; i < count; ++i) {
        *out++ = i;
    }
}
```

### Pattern 3: Iterator Pair Processing
```cpp
// Process ranges with iterator pairs
template<typename InputIt, typename OutputIt>
OutputIt copyTransform(InputIt first, InputIt last, OutputIt result, TransformFunc func) {
    return std::transform(first, last, result, func);
}
```

## 🐛 Common Pitfalls & Solutions

### 1. Iterator Invalidation
```cpp
// Problem - iterator becomes invalid after modification
std::vector<int> vec = {1, 2, 3, 4, 5};
for (auto it = vec.begin(); it != vec.end(); ++it) {
    if (*it % 2 == 0) {
        vec.erase(it);  // Iterator becomes invalid!
    }
}

// Solution - use erase-remove idiom
vec.erase(
    std::remove_if(vec.begin(), vec.end(), [](int x) { return x % 2 == 0; }),
    vec.end()
);
```

### 2. Advancing Past End
```cpp
// Problem - undefined behavior
std::vector<int> vec = {1, 2, 3};
auto it = vec.begin();
std::advance(it, 10);  // Undefined behavior!

// Solution - check bounds
auto dist = std::distance(it, vec.end());
if (dist >= 10) {
    std::advance(it, 10);
}
```

### 3. Using Wrong Iterator Category
```cpp
// Problem - using random access operations on forward iterator
std::forward_list<int> fwd = {1, 2, 3};
auto it = fwd.begin();
auto it2 = it + 2;  // Error: forward_list doesn't support + operator

// Solution - use advance or next
std::advance(it, 2);  // Works
auto it3 = std::next(fwd.begin(), 2);  // Also works
```

## 📚 Related Headers

- `algorithm.md` - Algorithms that work with iterators
- `numeric.md` - Numeric algorithms
- `memory.md` - Memory management utilities
- `functional.md` - Function objects for algorithms

## 🚀 Best Practices

1. **Use iterator adapters** instead of manual loops when possible
2. **Check iterator category** before using category-specific operations
3. **Prefer range-based for loops** for simple iteration
4. **Use erase-remove idiom** for safe element removal
5. **Be aware of iterator invalidation** when modifying containers
6. **Use std::next/std::prev** instead of manual arithmetic when possible
7. **Choose appropriate iterator** for the task (input, output, forward, etc.)

## 🎯 When to Use Iterator Utilities

✅ **Use when:**
- Working with STL algorithms
- Need to insert elements into containers
- Processing streams as sequences
- Creating custom containers
- Implementing generic algorithms
- Need safe iterator movement

❌ **Avoid when:**
- Simple index-based access suffices
- Performance-critical inner loops
- Working with raw arrays exclusively
- Simple container traversal (use range-based for)

---

**Examples in this file**: 4 complete programs  
**Key Functions**: `advance`, `distance`, `next`, `prev`, `back_inserter`, `front_inserter`  
**Iterator Categories**: Input, Output, Forward, Bidirectional, Random Access  
**Performance**: Category-dependent operations
