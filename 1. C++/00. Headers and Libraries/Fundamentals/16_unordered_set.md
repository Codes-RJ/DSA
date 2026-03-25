# 16_unordered_set.md - Hash-Based Unique Container

The `unordered_set` header provides `std::unordered_set`, an associative container that stores unique elements in a hash table for average constant-time lookup.

## 📖 Overview

`std::unordered_set` is an associative container that contains unique elements organized using hash tables. It provides average O(1) time complexity for most operations but does not maintain any particular order of elements.

## 🎯 Key Features

- **Hash-based storage** - Uses hash table for efficient lookup
- **Average O(1) operations** - Fast insert, delete, and find operations
- **Unique elements** - No duplicate values allowed
- **Unordered iteration** - Elements are not stored in any particular order
- **Custom hash functions** - Can define custom hash for complex types
- **Load factor management** - Automatic resizing based on load factor

## 🔧 Basic Unordered Set Operations

### Creating and Initializing Unordered Sets
```cpp
#include <iostream>
#include <unordered_set>
#include <string>
#include <functional>

int main() {
    // Different ways to create unordered sets
    
    // Empty set
    std::unordered_set<int> set1;
    
    // From initializer list
    std::unordered_set<int> set2 = {5, 2, 8, 1, 3};
    
    // Copy constructor
    std::unordered_set<int> set3 = set2;
    
    // From range
    std::vector<int> vec = {4, 1, 6, 2, 5};
    std::unordered_set<int> set4(vec.begin(), vec.end());
    
    // With initial capacity
    std::unordered_set<int> set5(100);  // Reserve space for 100 elements
    
    // With custom hash function
    struct StringHash {
        size_t operator()(const std::string& s) const {
            return std::hash<std::string>{}(s);
        }
    };
    
    std::unordered_set<std::string, StringHash> set6;
    
    return 0;
}
```

### Insertion and Erasure
```cpp
void demonstrateBasicOperations() {
    std::unordered_set<int> s;
    
    // Insert elements
    s.insert(10);
    s.insert(5);
    s.insert(15);
    s.insert(5);  // Duplicate, will be ignored
    
    std::cout << "After insertions: ";
    for (int val : s) std::cout << val << " ";
    std::cout << std::endl;
    
    // Insert with hint
    auto hint = s.begin();
    s.insert(hint, 12);  // Insert with position hint
    
    // Insert range
    std::vector<int> more = {20, 8, 18};
    s.insert(more.begin(), more.end());
    
    std::cout << "After more insertions: ";
    for (int val : s) std::cout << val << " ";
    std::cout << std::endl;
    
    // Erase elements
    s.erase(10);  // Erase by value
    auto it = s.find(12);
    if (it != s.end()) {
        s.erase(it);  // Erase by iterator
    }
    
    // Erase range
    auto start = s.find(8);
    auto end = s.find(20);
    if (start != s.end() && end != s.end()) {
        s.erase(start, ++end);  // Erase [start, end)
    }
    
    std::cout << "After erasures: ";
    for (int val : s) std::cout << val << " ";
    std::cout << std::endl;
}
```

### Searching and Membership
```cpp
void demonstrateSearching() {
    std::unordered_set<int> s = {1, 3, 5, 7, 9, 11, 13};
    
    // Find element
    auto it = s.find(7);
    if (it != s.end()) {
        std::cout << "Found 7" << std::endl;
    } else {
        std::cout << "7 not found" << std::endl;
    }
    
    // Count occurrences (0 or 1 for unordered_set)
    int count = s.count(5);
    std::cout << "Count of 5: " << count << std::endl;
    
    // Check if contains
    if (s.contains(9)) {
        std::cout << "Set contains 9" << std::endl;
    }
    
    // Check membership efficiently
    int value = 11;
    if (s.find(value) != s.end()) {
        std::cout << value << " is in the set" << std::endl;
    }
}
```

## 🔧 Advanced Unordered Set Operations

### Hash Functions and Custom Types
```cpp
struct Point {
    int x, y;
    
    Point(int x_, int y_) : x(x_), y(y_) {}
    
    bool operator==(const Point& other) const {
        return x == other.x && y == other.y;
    }
};

struct PointHash {
    size_t operator()(const Point& p) const {
        // Simple hash combining x and y
        return std::hash<int>{}(p.x) ^ (std::hash<int>{}(p.y) << 1);
    }
};

void demonstrateCustomTypes() {
    std::unordered_set<Point, PointHash> point_set;
    
    point_set.insert(Point(1, 2));
    point_set.insert(Point(10, 20));
    point_set.insert(Point(5, 5));
    point_set.insert(Point(1, 2));  // Duplicate, will be ignored
    
    std::cout << "Points in set:" << std::endl;
    for (const auto& point : point_set) {
        std::cout << "(" << point.x << ", " << point.y << ")" << std::endl;
    }
}
```

### Bucket Operations and Performance
```cpp
void demonstrateBucketOperations() {
    std::unordered_set<int> data = {1, 2, 3, 4, 5};
    
    std::cout << "Bucket count: " << data.bucket_count() << std::endl;
    std::cout << "Size: " << data.size() << std::endl;
    std::cout << "Load factor: " << data.load_factor() << std::endl;
    std::cout << "Max load factor: " << data.max_load_factor() << std::endl;
    
    // Show bucket distribution
    std::cout << "\nBucket distribution:" << std::endl;
    for (size_t i = 0; i < data.bucket_count(); ++i) {
        std::cout << "Bucket " << i << ": " << data.bucket_size(i) << " elements" << std::endl;
    }
    
    // Reserve space to reduce rehashing
    data.reserve(100);
    std::cout << "\nAfter reserve(100):" << std::endl;
    std::cout << "Bucket count: " << data.bucket_count() << std::endl;
    
    // Force rehash
    data.rehash(20);
    std::cout << "\nAfter rehash(20):" << std::endl;
    std::cout << "Bucket count: " << data.bucket_count() << std::endl;
}
```

## 🎮 Practical Examples

### Example 1: Duplicate Detection System
```cpp
#include <iostream>
#include <unordered_set>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>

class DuplicateDetector {
private:
    std::unordered_set<std::string> m_seen_items;
    std::vector<std::string> m_duplicates;
    
public:
    // Add item and check for duplicates
    bool addItem(const std::string& item) {
        if (m_seen_items.find(item) != m_seen_items.end()) {
            m_duplicates.push_back(item);
            return false;  // Duplicate found
        }
        
        m_seen_items.insert(item);
        return true;  // Unique item
    }
    
    // Add multiple items
    void addItems(const std::vector<std::string>& items) {
        for (const auto& item : items) {
            addItem(item);
        }
    }
    
    // Process items from file
    bool processFile(const std::string& filename) {
        std::ifstream file(filename);
        if (!file.is_open()) {
            std::cerr << "Cannot open file: " << filename << std::endl;
            return false;
        }
        
        std::string line;
        while (std::getline(file, line)) {
            // Trim whitespace
            line.erase(0, line.find_first_not_of(" \t\r\n"));
            line.erase(line.find_last_not_of(" \t\r\n") + 1);
            
            if (!line.empty()) {
                addItem(line);
            }
        }
        
        return true;
    }
    
    // Check if item exists
    bool contains(const std::string& item) const {
        return m_seen_items.find(item) != m_seen_items.end();
    }
    
    // Get unique items
    std::vector<std::string> getUniqueItems() const {
        std::vector<std::string> unique_items(
            m_seen_items.begin(), m_seen_items.end()
        );
        std::sort(unique_items.begin(), unique_items.end());
        return unique_items;
    }
    
    // Get duplicates
    std::vector<std::string> getDuplicates() const {
        std::vector<std::string> unique_duplicates = m_duplicates;
        std::sort(unique_duplicates.begin(), unique_duplicates.end());
        unique_duplicates.erase(
            std::unique(unique_duplicates.begin(), unique_duplicates.end()),
            unique_duplicates.end()
        );
        return unique_duplicates;
    }
    
    // Get statistics
    struct Statistics {
        size_t total_processed;
        size_t unique_count;
        size_t duplicate_count;
        double duplicate_percentage;
    };
    
    Statistics getStatistics() const {
        Statistics stats = {0, 0, 0, 0.0};
        
        stats.total_processed = m_seen_items.size() + m_duplicates.size();
        stats.unique_count = m_seen_items.size();
        stats.duplicate_count = m_duplicates.size();
        
        if (stats.total_processed > 0) {
            stats.duplicate_percentage = 
                (static_cast<double>(stats.duplicate_count) / stats.total_processed) * 100.0;
        }
        
        return stats;
    }
    
    // Clear all data
    void clear() {
        m_seen_items.clear();
        m_duplicates.clear();
    }
    
    // Display results
    void displayResults() const {
        auto stats = getStatistics();
        
        std::cout << "\n=== Duplicate Detection Results ===" << std::endl;
        std::cout << "Total items processed: " << stats.total_processed << std::endl;
        std::cout << "Unique items: " << stats.unique_count << std::endl;
        std::cout << "Duplicate occurrences: " << stats.duplicate_count << std::endl;
        std::cout << "Duplicate percentage: " << std::fixed << std::setprecision(1) 
                  << stats.duplicate_percentage << "%" << std::endl;
        
        auto duplicates = getDuplicates();
        if (!duplicates.empty()) {
            std::cout << "\nDuplicate items:" << std::endl;
            for (const auto& duplicate : duplicates) {
                std::cout << "  " << duplicate << std::endl;
            }
        }
    }
};

int main() {
    DuplicateDetector detector;
    
    std::cout << "=== Duplicate Detection System ===" << std::endl;
    
    // Test with sample data
    std::vector<std::string> items = {
        "apple", "banana", "cherry", "apple", "date",
        "banana", "elderberry", "fig", "grape", "apple"
    };
    
    detector.addItems(items);
    
    std::cout << "Processing items..." << std::endl;
    for (const auto& item : items) {
        bool is_unique = detector.addItem(item);
        std::cout << item << ": " << (is_unique ? "unique" : "duplicate") << std::endl;
    }
    
    detector.displayResults();
    
    // Test individual checks
    std::cout << "\n=== Individual Checks ===" << std::endl;
    std::cout << "Contains 'apple': " << (detector.contains("apple") ? "Yes" : "No") << std::endl;
    std::cout << "Contains 'orange': " << (detector.contains("orange") ? "Yes" : "No") << std::endl;
    
    // Show unique items
    auto unique_items = detector.getUniqueItems();
    std::cout << "\nUnique items (" << unique_items.size() << "):" << std::endl;
    for (const auto& item : unique_items) {
        std::cout << "  " << item << std::endl;
    }
    
    return 0;
}
```

### Example 2: Spell Checker
```cpp
#include <iostream>
#include <unordered_set>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cctype>

class SpellChecker {
private:
    std::unordered_set<std::string> m_dictionary;
    
    std::string normalizeWord(const std::string& word) const {
        std::string normalized;
        for (char c : word) {
            if (std::isalpha(c)) {
                normalized += std::tolower(c);
            }
        }
        return normalized;
    }
    
public:
    // Load dictionary from file
    bool loadDictionary(const std::string& filename) {
        std::ifstream file(filename);
        if (!file.is_open()) {
            std::cerr << "Cannot open dictionary file: " << filename << std::endl;
            return false;
        }
        
        std::string word;
        while (file >> word) {
            std::string normalized = normalizeWord(word);
            if (!normalized.empty()) {
                m_dictionary.insert(normalized);
            }
        }
        
        std::cout << "Loaded " << m_dictionary.size() << " words into dictionary" << std::endl;
        return true;
    }
    
    // Add words to dictionary
    void addWords(const std::vector<std::string>& words) {
        for (const auto& word : words) {
            std::string normalized = normalizeWord(word);
            if (!normalized.empty()) {
                m_dictionary.insert(normalized);
            }
        }
    }
    
    // Check if word is spelled correctly
    bool isCorrect(const std::string& word) const {
        std::string normalized = normalizeWord(word);
        return m_dictionary.find(normalized) != m_dictionary.end();
    }
    
    // Find misspelled words in text
    std::vector<std::string> findMisspelledWords(const std::string& text) const {
        std::vector<std::string> misspelled;
        std::string current_word;
        
        for (char c : text) {
            if (std::isalpha(c)) {
                current_word += c;
            } else if (!current_word.empty()) {
                std::string normalized = normalizeWord(current_word);
                if (!normalized.empty() && m_dictionary.find(normalized) == m_dictionary.end()) {
                    misspelled.push_back(current_word);
                }
                current_word.clear();
            }
        }
        
        // Check last word
        if (!current_word.empty()) {
            std::string normalized = normalizeWord(current_word);
            if (!normalized.empty() && m_dictionary.find(normalized) == m_dictionary.end()) {
                misspelled.push_back(current_word);
            }
        }
        
        return misspelled;
    }
    
    // Get suggestions for misspelled word
    std::vector<std::string> getSuggestions(const std::string& word, size_t max_suggestions = 5) const {
        std::vector<std::pair<std::string, int>> candidates;
        std::string normalized = normalizeWord(word);
        
        // Find words with similar length
        for (const auto& dict_word : m_dictionary) {
            int distance = calculateEditDistance(normalized, dict_word);
            if (distance <= 2) {  // Within 2 edits
                candidates.emplace_back(dict_word, distance);
            }
        }
        
        // Sort by edit distance
        std::sort(candidates.begin(), candidates.end(),
            [](const auto& a, const auto& b) {
                return a.second < b.second;
            });
        
        // Extract suggestions
        std::vector<std::string> suggestions;
        for (size_t i = 0; i < std::min(max_suggestions, candidates.size()); ++i) {
            suggestions.push_back(candidates[i].first);
        }
        
        return suggestions;
    }
    
    // Get dictionary statistics
    struct Statistics {
        size_t total_words;
        size_t average_word_length;
        std::string shortest_word;
        std::string longest_word;
    };
    
    Statistics getStatistics() const {
        Statistics stats = {0, 0, "", ""};
        
        if (m_dictionary.empty()) return stats;
        
        stats.total_words = m_dictionary.size();
        
        size_t total_length = 0;
        size_t min_length = SIZE_MAX;
        size_t max_length = 0;
        
        for (const auto& word : m_dictionary) {
            total_length += word.length();
            
            if (word.length() < min_length) {
                min_length = word.length();
                stats.shortest_word = word;
            }
            
            if (word.length() > max_length) {
                max_length = word.length();
                stats.longest_word = word;
            }
        }
        
        stats.average_word_length = static_cast<double>(total_length) / stats.total_words;
        
        return stats;
    }
    
    // Clear dictionary
    void clear() {
        m_dictionary.clear();
    }
    
private:
    // Calculate Levenshtein distance between two strings
    int calculateEditDistance(const std::string& s1, const std::string& s2) const {
        const size_t m = s1.length();
        const size_t n = s2.length();
        
        if (m == 0) return n;
        if (n == 0) return m;
        
        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1));
        
        for (size_t i = 0; i <= m; ++i) dp[i][0] = i;
        for (size_t j = 0; j <= n; ++j) dp[0][j] = j;
        
        for (size_t i = 1; i <= m; ++i) {
            for (size_t j = 1; j <= n; ++j) {
                if (s1[i - 1] == s2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = 1 + std::min({dp[i - 1][j],    // deletion
                                           dp[i][j - 1],    // insertion
                                           dp[i - 1][j - 1]}); // substitution
                }
            }
        }
        
        return dp[m][n];
    }
};

int main() {
    SpellChecker spellChecker;
    
    std::cout << "=== Spell Checker ===" << std::endl;
    
    // Load basic dictionary
    std::vector<std::string> basic_words = {
        "hello", "world", "programming", "computer", "algorithm",
        "data", "structure", "function", "variable", "class",
        "object", "method", "property", "inheritance", "polymorphism"
    };
    
    spellChecker.addWords(basic_words);
    
    // Test spell checking
    std::cout << "\n=== Spell Check Test ===" << std::endl;
    
    std::vector<std::string> test_words = {
        "hello", "wrold", "progamming", "computr", "algoritm"
    };
    
    for (const auto& word : test_words) {
        bool correct = spellChecker.isCorrect(word);
        std::cout << word << ": " << (correct ? "correct" : "misspelled");
        
        if (!correct) {
            auto suggestions = spellChecker.getSuggestions(word);
            if (!suggestions.empty()) {
                std::cout << " (suggestions: ";
                for (size_t i = 0; i < suggestions.size(); ++i) {
                    if (i > 0) std::cout << ", ";
                    std::cout << suggestions[i];
                }
                std::cout << ")";
            }
        }
        std::cout << std::endl;
    }
    
    // Test with text
    std::cout << "\n=== Text Analysis ===" << std::endl;
    std::string text = "This is a test of the spell cheker. It shoud find mispelled words.";
    
    auto misspelled = spellChecker.findMisspelledWords(text);
    std::cout << "Misspelled words in text:" << std::endl;
    for (const auto& word : misspelled) {
        std::cout << "  " << word;
        
        auto suggestions = spellChecker.getSuggestions(word);
        if (!suggestions.empty()) {
            std::cout << " -> " << suggestions[0];
        }
        std::cout << std::endl;
    }
    
    // Show statistics
    auto stats = spellChecker.getStatistics();
    std::cout << "\n=== Dictionary Statistics ===" << std::endl;
    std::cout << "Total words: " << stats.total_words << std::endl;
    std::cout << "Average word length: " << std::fixed << std::setprecision(1) 
              << stats.average_word_length << std::endl;
    std::cout << "Shortest word: " << stats.shortest_word << std::endl;
    std::cout << "Longest word: " << stats.longest_word << std::endl;
    
    return 0;
}
```

### Example 3: Cache with Bloom Filter
```cpp
#include <iostream>
#include <unordered_set>
#include <vector>
#include <functional>
#include <cmath>

class BloomFilter {
private:
    std::vector<bool> m_bits;
    size_t m_size;
    size_t m_hash_count;
    
public:
    BloomFilter(size_t expected_items, double false_positive_rate = 0.01) {
        // Calculate optimal size and hash count
        m_size = static_cast<size_t>(
            -expected_items * std::log(false_positive_rate) / (std::log(2) * std::log(2))
        );
        
        m_hash_count = static_cast<size_t>(
            (m_size / expected_items) * std::log(2)
        );
        
        m_bits.resize(m_size, false);
        
        std::cout << "Bloom filter initialized:" << std::endl;
        std::cout << "  Size: " << m_size << " bits" << std::endl;
        std::cout << "  Hash functions: " << m_hash_count << std::endl;
    }
    
    void add(const std::string& item) {
        for (size_t i = 0; i < m_hash_count; ++i) {
            size_t hash = hashFunction(item, i) % m_size;
            m_bits[hash] = true;
        }
    }
    
    bool mightContain(const std::string& item) const {
        for (size_t i = 0; i < m_hash_count; ++i) {
            size_t hash = hashFunction(item, i) % m_size;
            if (!m_bits[hash]) {
                return false;  // Definitely not present
            }
        }
        return true;  // Might be present
    }
    
    double getFalsePositiveRate(size_t items_added) const {
        return std::pow(1.0 - std::exp(-static_cast<double>(m_hash_count * items_added) / m_size), 
                       m_hash_count);
    }
    
private:
    size_t hashFunction(const std::string& item, size_t seed) const {
        size_t hash = seed;
        for (char c : item) {
            hash = hash * 31 + static_cast<size_t>(c);
        }
        return hash;
    }
};

class CacheWithBloomFilter {
private:
    std::unordered_set<std::string> m_cache;
    BloomFilter m_bloom_filter;
    size_t m_max_size;
    
public:
    CacheWithBloomFilter(size_t max_size, double false_positive_rate = 0.01)
        : m_bloom_filter(max_size * 2, false_positive_rate), m_max_size(max_size) {}
    
    bool add(const std::string& item) {
        if (m_cache.find(item) != m_cache.end()) {
            return false;  // Already exists
        }
        
        if (m_cache.size() >= m_max_size) {
            return false;  // Cache full
        }
        
        m_cache.insert(item);
        m_bloom_filter.add(item);
        return true;
    }
    
    bool contains(const std::string& item) const {
        // Quick check with bloom filter
        if (!m_bloom_filter.mightContain(item)) {
            return false;  // Definitely not in cache
        }
        
        // Verify with actual set
        return m_cache.find(item) != m_cache.end();
    }
    
    bool remove(const std::string& item) {
        auto it = m_cache.find(item);
        if (it != m_cache.end()) {
            m_cache.erase(it);
            // Note: Bloom filter doesn't support removal
            return true;
        }
        return false;
    }
    
    size_t size() const {
        return m_cache.size();
    }
    
    bool isFull() const {
        return m_cache.size() >= m_max_size;
    }
    
    void displayStats() const {
        std::cout << "Cache Statistics:" << std::endl;
        std::cout << "  Current size: " << m_cache.size() << "/" << m_max_size << std::endl;
        std::cout << "  Bloom filter false positive rate: " 
                  << (m_bloom_filter.getFalsePositiveRate(m_cache.size()) * 100) << "%" << std::endl;
    }
};

int main() {
    CacheWithBloomFilter cache(1000, 0.01);
    
    std::cout << "=== Cache with Bloom Filter ===" << std::endl;
    
    // Add some items
    std::vector<std::string> items = {
        "apple", "banana", "cherry", "date", "elderberry",
        "fig", "grape", "honeydew", "kiwi", "lemon"
    };
    
    std::cout << "\nAdding items to cache:" << std::endl;
    for (const auto& item : items) {
        bool added = cache.add(item);
        std::cout << item << ": " << (added ? "added" : "failed") << std::endl;
    }
    
    cache.displayStats();
    
    // Test lookups
    std::cout << "\n=== Lookup Tests ===" << std::endl;
    
    std::vector<std::string> test_items = {
        "apple", "banana", "orange", "grape", "mango"
    };
    
    for (const auto& item : test_items) {
        bool found = cache.contains(item);
        std::cout << item << ": " << (found ? "found" : "not found") << std::endl;
    }
    
    // Test performance with many lookups
    std::cout << "\n=== Performance Test ===" << std::endl;
    
    // Add more items
    for (int i = 0; i < 500; ++i) {
        cache.add("item_" + std::to_string(i));
    }
    
    cache.displayStats();
    
    // Test many lookups (including non-existent items)
    int found_count = 0;
    int lookup_count = 1000;
    
    for (int i = 0; i < lookup_count; ++i) {
        std::string item = "item_" + std::to_string(i % 600);  // Some will not exist
        if (cache.contains(item)) {
            found_count++;
        }
    }
    
    std::cout << "Lookups performed: " << lookup_count << std::endl;
    std::cout << "Items found: " << found_count << std::endl;
    std::cout << "Cache hit rate: " << (static_cast<double>(found_count) / lookup_count * 100) << "%" << std::endl;
    
    return 0;
}
```

### Example 4: Graph Cycle Detection
```cpp
#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <stack>

class Graph {
private:
    std::unordered_map<int, std::vector<int>> m_adjacency_list;
    
public:
    // Add directed edge
    void addEdge(int from, int to) {
        m_adjacency_list[from].push_back(to);
    }
    
    // Add undirected edge
    void addUndirectedEdge(int u, int v) {
        m_adjacency_list[u].push_back(v);
        m_adjacency_list[v].push_back(u);
    }
    
    // Check if graph has cycle using DFS
    bool hasCycle() const {
        std::unordered_set<int> visited;
        std::unordered_set<int> recursion_stack;
        
        for (const auto& [node, neighbors] : m_adjacency_list) {
            if (visited.find(node) == visited.end()) {
                if (hasCycleDFS(node, visited, recursion_stack)) {
                    return true;
                }
            }
        }
        
        return false;
    }
    
    // Find all nodes in cycles
    std::vector<int> findNodesInCycles() const {
        std::unordered_set<int> visited;
        std::unordered_set<int> recursion_stack;
        std::vector<int> nodes_in_cycles;
        
        for (const auto& [node, neighbors] : m_adjacency_list) {
            if (visited.find(node) == visited.end()) {
                std::unordered_set<int> path_nodes;
                if (findCycleNodesDFS(node, visited, recursion_stack, path_nodes)) {
                    nodes_in_cycles.insert(nodes_in_cycles.end(), 
                                        path_nodes.begin(), path_nodes.end());
                }
            }
        }
        
        // Remove duplicates
        std::unordered_set<int> unique_nodes(nodes_in_cycles.begin(), nodes_in_cycles.end());
        return std::vector<int>(unique_nodes.begin(), unique_nodes.end());
    }
    
    // Check if graph is a tree
    bool isTree() const {
        if (m_adjacency_list.empty()) return true;
        
        // Tree must be connected and have no cycles
        if (hasCycle()) return false;
        
        // Check connectivity
        std::unordered_set<int> visited;
        int start_node = m_adjacency_list.begin()->first;
        DFS(start_node, visited);
        
        return visited.size() == m_adjacency_list.size();
    }
    
    // Get topological sort (if graph is DAG)
    std::vector<int> topologicalSort() const {
        if (hasCycle()) {
            return {};  // No topological sort for graphs with cycles
        }
        
        std::unordered_map<int, int> in_degree;
        std::vector<int> result;
        
        // Calculate in-degrees
        for (const auto& [node, neighbors] : m_adjacency_list) {
            in_degree[node] = 0;  // Ensure all nodes are in the map
        }
        
        for (const auto& [node, neighbors] : m_adjacency_list) {
            for (int neighbor : neighbors) {
                in_degree[neighbor]++;
            }
        }
        
        // Find nodes with no incoming edges
        std::vector<int> zero_in_degree;
        for (const auto& [node, degree] : in_degree) {
            if (degree == 0) {
                zero_in_degree.push_back(node);
            }
        }
        
        // Process nodes
        while (!zero_in_degree.empty()) {
            int current = zero_in_degree.back();
            zero_in_degree.pop_back();
            result.push_back(current);
            
            for (int neighbor : m_adjacency_list.at(current)) {
                in_degree[neighbor]--;
                if (in_degree[neighbor] == 0) {
                    zero_in_degree.push_back(neighbor);
                }
            }
        }
        
        return result;
    }
    
    // Display graph
    void display() const {
        std::cout << "Graph adjacency list:" << std::endl;
        for (const auto& [node, neighbors] : m_adjacency_list) {
            std::cout << node << " -> ";
            for (int neighbor : neighbors) {
                std::cout << neighbor << " ";
            }
            std::cout << std::endl;
        }
    }
    
    // Get graph statistics
    struct Statistics {
        size_t num_nodes;
        size_t num_edges;
        bool has_cycle;
        bool is_tree;
        bool is_dag;
    };
    
    Statistics getStatistics() const {
        Statistics stats = {0, 0, false, false, false};
        
        stats.num_nodes = m_adjacency_list.size();
        
        for (const auto& [node, neighbors] : m_adjacency_list) {
            stats.num_edges += neighbors.size();
        }
        
        stats.has_cycle = hasCycle();
        stats.is_tree = isTree();
        stats.is_dag = !stats.has_cycle;
        
        return stats;
    }
    
private:
    bool hasCycleDFS(int node, std::unordered_set<int>& visited, 
                    std::unordered_set<int>& recursion_stack) const {
        visited.insert(node);
        recursion_stack.insert(node);
        
        auto it = m_adjacency_list.find(node);
        if (it != m_adjacency_list.end()) {
            for (int neighbor : it->second) {
                if (visited.find(neighbor) == visited.end()) {
                    if (hasCycleDFS(neighbor, visited, recursion_stack)) {
                        return true;
                    }
                } else if (recursion_stack.find(neighbor) != recursion_stack.end()) {
                    return true;  // Back edge found
                }
            }
        }
        
        recursion_stack.erase(node);
        return false;
    }
    
    bool findCycleNodesDFS(int node, std::unordered_set<int>& visited,
                          std::unordered_set<int>& recursion_stack,
                          std::unordered_set<int>& path_nodes) const {
        visited.insert(node);
        recursion_stack.insert(node);
        
        auto it = m_adjacency_list.find(node);
        if (it != m_adjacency_list.end()) {
            for (int neighbor : it->second) {
                if (visited.find(neighbor) == visited.end()) {
                    if (findCycleNodesDFS(neighbor, visited, recursion_stack, path_nodes)) {
                        return true;
                    }
                } else if (recursion_stack.find(neighbor) != recursion_stack.end()) {
                    // Cycle detected - collect nodes in cycle
                    path_nodes.insert(node);
                    path_nodes.insert(neighbor);
                    return true;
                }
            }
        }
        
        recursion_stack.erase(node);
        return false;
    }
    
    void DFS(int node, std::unordered_set<int>& visited) const {
        visited.insert(node);
        
        auto it = m_adjacency_list.find(node);
        if (it != m_adjacency_list.end()) {
            for (int neighbor : it->second) {
                if (visited.find(neighbor) == visited.end()) {
                    DFS(neighbor, visited);
                }
            }
        }
    }
};

int main() {
    Graph graph;
    
    std::cout << "=== Graph Cycle Detection ===" << std::endl;
    
    // Create a graph with a cycle
    graph.addEdge(0, 1);
    graph.addEdge(1, 2);
    graph.addEdge(2, 3);
    graph.addEdge(3, 0);  // Creates a cycle: 0 -> 1 -> 2 -> 3 -> 0
    
    graph.addEdge(4, 5);
    graph.addEdge(5, 6);
    
    graph.display();
    
    // Test cycle detection
    std::cout << "\n=== Cycle Analysis ===" << std::endl;
    bool has_cycle = graph.hasCycle();
    std::cout << "Graph has cycle: " << (has_cycle ? "Yes" : "No") << std::endl;
    
    if (has_cycle) {
        auto nodes_in_cycles = graph.findNodesInCycles();
        std::cout << "Nodes in cycles: ";
        for (int node : nodes_in_cycles) {
            std::cout << node << " ";
        }
        std::cout << std::endl;
    }
    
    // Test tree property
    bool is_tree = graph.isTree();
    std::cout << "Graph is a tree: " << (is_tree ? "Yes" : "No") << std::endl;
    
    // Test topological sort
    auto topo_sort = graph.topologicalSort();
    if (topo_sort.empty()) {
        std::cout << "No topological sort (graph has cycle)" << std::endl;
    } else {
        std::cout << "Topological sort: ";
        for (int node : topo_sort) {
            std::cout << node << " ";
        }
        std::cout << std::endl;
    }
    
    // Test with a DAG
    std::cout << "\n=== Testing with DAG ===" << std::endl;
    Graph dag;
    
    dag.addEdge(0, 1);
    dag.addEdge(0, 2);
    dag.addEdge(1, 3);
    dag.addEdge(2, 3);
    
    dag.display();
    
    auto dag_stats = dag.getStatistics();
    std::cout << "\nDAG Statistics:" << std::endl;
    std::cout << "Nodes: " << dag_stats.num_nodes << std::endl;
    std::cout << "Edges: " << dag_stats.num_edges << std::endl;
    std::cout << "Has cycle: " << (dag_stats.has_cycle ? "Yes" : "No") << std::endl;
    std::cout << "Is tree: " << (dag_stats.is_tree ? "Yes" : "No") << std::endl;
    std::cout << "Is DAG: " << (dag_stats.is_dag ? "Yes" : "No") << std::endl;
    
    auto dag_topo = dag.topologicalSort();
    std::cout << "Topological sort: ";
    for (int node : dag_topo) {
        std::cout << node << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
```

## 📊 Complete Function Reference

### Modifiers
| Function | Description | Complexity |
|----------|-------------|------------|
| `insert()` | Insert element(s) | Average O(1) |
| `erase()` | Remove element(s) | Average O(1) |
| `clear()` | Remove all elements | O(n) |
| `swap()` | Swap contents | O(1) |

### Lookup Operations
| Function | Description | Complexity |
|----------|-------------|------------|
| `find()` | Find element | Average O(1) |
| `count()` | Count occurrences | Average O(1) |
| `contains()` | Check if element exists (C++20) | Average O(1) |

### Bucket Operations
| Function | Description | Complexity |
|----------|-------------|------------|
| `bucket_count()` | Number of buckets | O(1) |
| `bucket_size()` | Elements in specific bucket | O(bucket_size) |
| `bucket()` | Bucket index for element | O(1) |
| `rehash()` | Change bucket count | O(n) |
| `reserve()` | Reserve space for elements | O(n) |

### Hash Policy
| Function | Description | Complexity |
|----------|-------------|------------|
| `load_factor()` | Current load factor | O(1) |
| `max_load_factor()` | Get/set max load factor | O(1) |

## ⚡ Performance Considerations

### Hash Function Quality
```cpp
// Good hash function: distributes keys evenly
struct GoodHash {
    size_t operator()(const std::string& s) const {
        return std::hash<std::string>{}(s);
    }
};

// Poor hash function: causes collisions
struct BadHash {
    size_t operator()(const std::string& s) const {
        return s.length();  // Many strings have same length
    }
};
```

### Load Factor Management
```cpp
std::unordered_set<int> set;

// Set maximum load factor (default is 1.0)
set.max_load_factor(0.75);

// Reserve space to avoid rehashing
set.reserve(1000);  // Good for known sizes

// Monitor performance
std::cout << "Load factor: " << set.load_factor() << std::endl;
std::cout << "Bucket count: " << set.bucket_count() << std::endl;
```

## 🎯 Common Patterns

### Pattern 1: Membership Testing
```cpp
class MembershipTester {
private:
    std::unordered_set<int> m_allowed_values;
    
public:
    MembershipTester(const std::vector<int>& allowed) {
        for (int value : allowed) {
            m_allowed_values.insert(value);
        }
    }
    
    bool isAllowed(int value) const {
        return m_allowed_values.find(value) != m_allowed_values.end();
    }
};
```

### Pattern 2: Duplicate Removal
```cpp
template<typename T>
std::vector<T> removeDuplicates(const std::vector<T>& items) {
    std::unordered_set<T> seen;
    std::vector<T> unique;
    
    for (const auto& item : items) {
        if (seen.insert(item).second) {
            unique.push_back(item);
        }
    }
    
    return unique;
}
```

## 🐛 Common Pitfalls & Solutions

### 1. Poor Hash Function Performance
```cpp
// Problem - using pointers as keys without custom hash
std::unordered_set<int*> set;  // Uses pointer address, not value

// Solution - custom hash for pointer values
struct IntPtrHash {
    size_t operator()(const int* ptr) const {
        return std::hash<int>{}(*ptr);
    }
};

struct IntPtrEqual {
    bool operator()(const int* a, const int* b) const {
        return *a == *b;
    }
};

std::unordered_set<int*, IntPtrHash, IntPtrEqual> good_set;
```

### 2. Iterator Invalidation
```cpp
// Problem - rehashing invalidates iterators
std::unordered_set<int> set;
auto it = set.begin();
set.insert(100);  // Might cause rehash
// it may be invalid

// Solution - be cautious with iterators during modifications
```

### 3. Unordered Iteration
```cpp
// Problem - relying on iteration order
for (int value : set) {
    // Order is not guaranteed!
}

// Solution - use ordered container if order matters
std::set<int> ordered_set;  // Maintains order
```

## 📚 Related Headers

- `set.md` - Ordered unique container
- `unordered_map.md` - Hash-based key-value container
- `map.md` - Ordered key-value container
- `functional.md` - Hash function objects

## 🚀 Best Practices

1. **Use unordered_set** for average O(1) lookup performance
2. **Reserve space** when you know the expected size
3. **Choose good hash functions** for custom types
4. **Monitor load factor** for performance tuning
5. **Use set** when iteration order matters
6. **Consider custom allocators** for memory-constrained environments

## 🎯 When to Use unordered_set

✅ **Use unordered_set when:**
- Need fast average O(1) lookup/insertion/deletion
- Need to ensure uniqueness of elements
- Order of elements doesn't matter
- Elements have good hash distribution
- Frequent membership testing

❌ **Avoid when:**
- Need ordered iteration (use `set`)
- Elements have poor hash properties
- Memory is severely constrained
- Need range queries
- Worst-case performance is critical

---

**Examples in this file**: 4 complete programs  
**Key Functions**: `insert()`, `find()`, `erase()`, `count()`, `contains()`, `rehash()`, `reserve()`  
**Time Complexity**: Average O(1), Worst-case O(n)  
**Space Complexity**: O(n) where n is number of elements
