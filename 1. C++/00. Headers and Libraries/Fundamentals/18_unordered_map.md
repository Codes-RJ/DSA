# 18_unordered_map.md - Hash-Based Key-Value Container

The `unordered_map` header provides `std::unordered_map`, an associative container that stores key-value pairs in a hash table for average constant-time lookup.

## 📖 Overview

`std::unordered_map` is an associative container that contains key-value pairs with unique keys, organized using hash tables. It provides average O(1) time complexity for most operations but does not maintain any particular order of elements.

## 🎯 Key Features

- **Hash-based storage** - Uses hash table for efficient lookup
- **Average O(1) operations** - Fast insert, delete, and find operations
- **Unique keys** - No duplicate keys allowed
- **Unordered iteration** - Elements are not stored in any particular order
- **Custom hash functions** - Can define custom hash for complex keys
- **Load factor management** - Automatic resizing based on load factor

## 🔧 Basic Unordered Map Operations

### Creating and Initializing Unordered Maps
```cpp
#include <iostream>
#include <unordered_map>
#include <string>
#include <functional>

int main() {
    // Different ways to create unordered maps
    
    // Empty map
    std::unordered_map<std::string, int> map1;
    
    // From initializer list
    std::unordered_map<std::string, int> map2 = {
        {"apple", 5},
        {"banana", 3},
        {"cherry", 8}
    };
    
    // With initial capacity
    std::unordered_map<std::string, int> map3(100);  // Reserve space for 100 elements
    
    // With custom hash function
    struct StringHash {
        size_t operator()(const std::string& s) const {
            return std::hash<std::string>{}(s);
        }
    };
    
    std::unordered_map<std::string, int, StringHash> map4;
    
    return 0;
}
```

### Insertion and Access
```cpp
void demonstrateBasicOperations() {
    std::unordered_map<std::string, int> scores;
    
    // Insert elements
    scores["alice"] = 95;      // Creates or updates
    scores["bob"] = 87;
    scores.insert({"charlie", 92});
    scores.emplace("diana", 88);  // In-place construction
    
    std::cout << "Scores after insertions:" << std::endl;
    for (const auto& [name, score] : scores) {
        std::cout << name << ": " << score << std::endl;
    }
    
    // Access elements
    std::cout << "\nAlice's score: " << scores["alice"] << std::endl;
    
    // Safe access with at() (throws if key not found)
    try {
        std::cout << "Bob's score: " << scores.at("bob") << std::endl;
        std::cout << "Eve's score: " << scores.at("eve") << std::endl;
    } catch (const std::out_of_range& e) {
        std::cout << "Eve not found: " << e.what() << std::endl;
    }
    
    // Check if key exists
    if (scores.count("charlie")) {
        std::cout << "Charlie exists with score: " << scores["charlie"] << std::endl;
    }
    
    // Find element
    auto it = scores.find("diana");
    if (it != scores.end()) {
        std::cout << "Found Diana: " << it->second << std::endl;
    }
}
```

### Erasure and Modification
```cpp
void demonstrateEraseAndModify() {
    std::unordered_map<std::string, int> inventory = {
        {"sword", 1},
        {"shield", 2},
        {"potion", 5},
        {"armor", 1}
    };
    
    std::cout << "Initial inventory:" << std::endl;
    for (const auto& [item, count] : inventory) {
        std::cout << item << ": " << count << std::endl;
    }
    
    // Erase by key
    inventory.erase("potion");
    
    // Erase by iterator
    auto it = inventory.find("shield");
    if (it != inventory.end()) {
        inventory.erase(it);
    }
    
    // Update value
    inventory["sword"] = 2;
    
    std::cout << "\nAfter modifications:" << std::endl;
    for (const auto& [item, count] : inventory) {
        std::cout << item << ": " << count << std::endl;
    }
}
```

## 🔧 Advanced Unordered Map Operations

### Hash Functions and Custom Keys
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

void demonstrateCustomKeys() {
    std::unordered_map<Point, std::string, PointHash> point_names;
    
    point_names[Point(1, 2)] = "Origin";
    point_names[Point(10, 20)] = "Target";
    point_names[Point(5, 5)] = "Center";
    
    std::cout << "Point names:" << std::endl;
    for (const auto& [point, name] : point_names) {
        std::cout << "(" << point.x << ", " << point.y << "): " << name << std::endl;
    }
}
```

### Bucket Operations and Performance
```cpp
void demonstrateBucketOperations() {
    std::unordered_map<int, std::string> data = {
        {1, "one"}, {2, "two"}, {3, "three"}, {4, "four"}, {5, "five"}
    };
    
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

### Example 1: Word Frequency Counter
```cpp
#include <iostream>
#include <unordered_map>
#include <string>
#include <fstream>
#include <algorithm>
#include <cctype>

class WordFrequencyCounter {
private:
    std::unordered_map<std::string, size_t> m_word_counts;
    
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
    // Process text from string
    void processText(const std::string& text) {
        std::string current_word;
        
        for (char c : text) {
            if (std::isalpha(c)) {
                current_word += c;
            } else if (!current_word.empty()) {
                std::string normalized = normalizeWord(current_word);
                if (!normalized.empty()) {
                    m_word_counts[normalized]++;
                }
                current_word.clear();
            }
        }
        
        if (!current_word.empty()) {
            std::string normalized = normalizeWord(current_word);
            if (!normalized.empty()) {
                m_word_counts[normalized]++;
            }
        }
    }
    
    // Process text from file
    bool processFile(const std::string& filename) {
        std::ifstream file(filename);
        if (!file.is_open()) {
            std::cerr << "Cannot open file: " << filename << std::endl;
            return false;
        }
        
        std::string word;
        while (file >> word) {
            std::string normalized = normalizeWord(word);
            if (!normalized.empty()) {
                m_word_counts[normalized]++;
            }
        }
        
        return true;
    }
    
    // Get word count
    size_t getWordCount(const std::string& word) const {
        std::string normalized = normalizeWord(word);
        auto it = m_word_counts.find(normalized);
        return it != m_word_counts.end() ? it->second : 0;
    }
    
    // Get top N words
    std::vector<std::pair<std::string, size_t>> getTopWords(size_t n) const {
        std::vector<std::pair<std::string, size_t>> all_words(
            m_word_counts.begin(), m_word_counts.end()
        );
        
        std::sort(all_words.begin(), all_words.end(),
            [](const auto& a, const auto& b) {
                return a.second > b.second;
            });
        
        if (n < all_words.size()) {
            all_words.resize(n);
        }
        
        return all_words;
    }
    
    // Get statistics
    struct Statistics {
        size_t total_words;
        size_t unique_words;
        std::string most_frequent_word;
        size_t most_frequent_count;
    };
    
    Statistics getStatistics() const {
        Statistics stats = {0, 0, "", 0};
        
        if (m_word_counts.empty()) return stats;
        
        stats.total_words = 0;
        stats.unique_words = m_word_counts.size();
        
        for (const auto& [word, count] : m_word_counts) {
            stats.total_words += count;
            if (count > stats.most_frequent_count) {
                stats.most_frequent_count = count;
                stats.most_frequent_word = word;
            }
        }
        
        return stats;
    }
    
    // Display results
    void displayResults(size_t top_n = 10) const {
        auto stats = getStatistics();
        
        std::cout << "\n=== Word Frequency Statistics ===" << std::endl;
        std::cout << "Total words: " << stats.total_words << std::endl;
        std::cout << "Unique words: " << stats.unique_words << std::endl;
        std::cout << "Most frequent word: '" << stats.most_frequent_word 
                  << "' (" << stats.most_frequent_count << " times)" << std::endl;
        
        auto top_words = getTopWords(top_n);
        std::cout << "\n=== Top " << top_n << " Most Frequent Words ===" << std::endl;
        for (size_t i = 0; i < top_words.size(); ++i) {
            std::cout << (i + 1) << ". " << top_words[i].first 
                      << " (" << top_words[i].second << " times)" << std::endl;
        }
    }
    
    // Clear all data
    void clear() {
        m_word_counts.clear();
    }
};

int main() {
    WordFrequencyCounter counter;
    
    // Sample text
    std::string text = R"(
        The quick brown fox jumps over the lazy dog.
        The dog was not amused by the jumping fox.
        Quick thinking saved the day for the brown fox.
        Dogs and foxes have a complicated relationship.
        The quick, the brown, and the fox formed an alliance.
    )";
    
    counter.processText(text);
    counter.displayResults(10);
    
    return 0;
}
```

### Example 2: Memoization Cache
```cpp
#include <iostream>
#include <unordered_map>
#include <functional>
#include <chrono>

class MemoizationCache {
private:
    template<typename ReturnType, typename... Args>
    class FunctionCache {
    private:
        struct ArgsHash {
            size_t operator()(const std::tuple<Args...>& args) const {
                return hashTuple(args, std::index_sequence_for<Args...>{});
            }
            
        private:
            template<size_t... Is>
            size_t hashTuple(const std::tuple<Args...>& tuple, std::index_sequence<Is...>) const {
                size_t hash = 0;
                ((hash ^= std::hash<Args>{}(std::get<Is>(tuple)) + 0x9e3779b9 + (hash << 6) + (hash >> 2)), ...);
                return hash;
            }
        };
        
        std::unordered_map<std::tuple<Args...>, ReturnType, ArgsHash> m_cache;
        std::function<ReturnType(Args...)> m_func;
        size_t m_hits;
        size_t m_misses;
        
    public:
        FunctionCache(std::function<ReturnType(Args...)> func) 
            : m_func(func), m_hits(0), m_misses(0) {}
        
        ReturnType operator()(Args... args) {
            std::tuple<Args...> key(args...);
            
            auto it = m_cache.find(key);
            if (it != m_cache.end()) {
                m_hits++;
                return it->second;
            }
            
            m_misses++;
            ReturnType result = m_func(args...);
            m_cache[key] = result;
            return result;
        }
        
        void clear() {
            m_cache.clear();
            m_hits = m_misses = 0;
        }
        
        double getHitRate() const {
            size_t total = m_hits + m_misses;
            return total > 0 ? static_cast<double>(m_hits) / total : 0.0;
        }
        
        size_t getCacheSize() const {
            return m_cache.size();
        }
        
        void displayStats() const {
            std::cout << "Cache Statistics:" << std::endl;
            std::cout << "  Hits: " << m_hits << std::endl;
            std::cout << "  Misses: " << m_misses << std::endl;
            std::cout << "  Hit rate: " << (getHitRate() * 100) << "%" << std::endl;
            std::cout << "  Cache size: " << getCacheSize() << std::endl;
        }
    };
    
public:
    // Create memoized function
    template<typename ReturnType, typename... Args>
    static auto memoize(std::function<ReturnType(Args...)> func) {
        return FunctionCache<ReturnType, Args...>(func);
    }
    
    // Create memoized function from lambda
    template<typename Func>
    static auto memoize(Func func) {
        return memoize(std::function(func));
    }
};

// Example usage with expensive computations
int main() {
    // Expensive fibonacci function
    auto fib = MemoizationCache::memoize([](int n) -> int {
        if (n <= 1) return n;
        
        // Simulate expensive computation
        std::this_thread::sleep_for(std::chrono::milliseconds(10));
        
        return fib(n - 1) + fib(n - 2);
    });
    
    std::cout << "=== Fibonacci with Memoization ===" << std::endl;
    
    auto start = std::chrono::high_resolution_clock::now();
    
    // Calculate fibonacci numbers
    for (int i = 0; i < 35; ++i) {
        std::cout << "fib(" << i << ") = " << fib(i) << std::endl;
    }
    
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    
    std::cout << "\nTotal time: " << duration.count() << " ms" << std::endl;
    fib.displayStats();
    
    // Test cache effectiveness
    std::cout << "\n=== Testing Cache Effectiveness ===" << std::endl;
    
    start = std::chrono::high_resolution_clock::now();
    for (int i = 30; i < 35; ++i) {
        std::cout << "fib(" << i << ") = " << fib(i) << std::endl;
    }
    end = std::chrono::high_resolution_clock::now();
    duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    
    std::cout << "\nCached computation time: " << duration.count() << " ms" << std::endl;
    fib.displayStats();
    
    return 0;
}
```

### Example 3: Contact Management System
```cpp
#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>

class ContactManager {
private:
    struct Contact {
        std::string name;
        std::string phone;
        std::string email;
        std::string address;
        
        Contact(const std::string& n, const std::string& p, 
                const std::string& e, const std::string& a)
            : name(n), phone(p), email(e), address(a) {}
    };
    
    std::unordered_map<std::string, Contact> m_contacts_by_name;
    std::unordered_map<std::string, std::string> m_phone_to_name;
    std::unordered_map<std::string, std::string> m_email_to_name;
    
public:
    // Add contact
    bool addContact(const std::string& name, const std::string& phone, 
                   const std::string& email, const std::string& address = "") {
        if (m_contacts_by_name.find(name) != m_contacts_by_name.end()) {
            std::cerr << "Contact with name '" << name << "' already exists" << std::endl;
            return false;
        }
        
        if (m_phone_to_name.find(phone) != m_phone_to_name.end()) {
            std::cerr << "Phone number '" << phone << "' already exists" << std::endl;
            return false;
        }
        
        if (m_email_to_name.find(email) != m_email_to_name.end()) {
            std::cerr << "Email '" << email << "' already exists" << std::endl;
            return false;
        }
        
        m_contacts_by_name.emplace(name, Contact(name, phone, email, address));
        m_phone_to_name[phone] = name;
        m_email_to_name[email] = name;
        
        std::cout << "Added contact: " << name << std::endl;
        return true;
    }
    
    // Find contact by name
    bool findByName(const std::string& name, Contact& contact) const {
        auto it = m_contacts_by_name.find(name);
        if (it != m_contacts_by_name.end()) {
            contact = it->second;
            return true;
        }
        return false;
    }
    
    // Find contact by phone
    bool findByPhone(const std::string& phone, Contact& contact) const {
        auto it = m_phone_to_name.find(phone);
        if (it != m_phone_to_name.end()) {
            return findByName(it->second, contact);
        }
        return false;
    }
    
    // Find contact by email
    bool findByEmail(const std::string& email, Contact& contact) const {
        auto it = m_email_to_name.find(email);
        if (it != m_email_to_name.end()) {
            return findByName(it->second, contact);
        }
        return false;
    }
    
    // Update contact
    bool updateContact(const std::string& name, const std::string& new_phone,
                      const std::string& new_email, const std::string& new_address = "") {
        auto it = m_contacts_by_name.find(name);
        if (it == m_contacts_by_name.end()) {
            std::cerr << "Contact '" << name << "' not found" << std::endl;
            return false;
        }
        
        Contact& contact = it->second;
        
        // Update phone if changed
        if (contact.phone != new_phone) {
            m_phone_to_name.erase(contact.phone);
            m_phone_to_name[new_phone] = name;
            contact.phone = new_phone;
        }
        
        // Update email if changed
        if (contact.email != new_email) {
            m_email_to_name.erase(contact.email);
            m_email_to_name[new_email] = name;
            contact.email = new_email;
        }
        
        // Update address
        contact.address = new_address;
        
        std::cout << "Updated contact: " << name << std::endl;
        return true;
    }
    
    // Remove contact
    bool removeContact(const std::string& name) {
        auto it = m_contacts_by_name.find(name);
        if (it == m_contacts_by_name.end()) {
            std::cerr << "Contact '" << name << "' not found" << std::endl;
            return false;
        }
        
        const Contact& contact = it->second;
        
        m_phone_to_name.erase(contact.phone);
        m_email_to_name.erase(contact.email);
        m_contacts_by_name.erase(it);
        
        std::cout << "Removed contact: " << name << std::endl;
        return true;
    }
    
    // Search contacts by name pattern
    std::vector<Contact> searchByName(const std::string& pattern) const {
        std::vector<Contact> results;
        
        for (const auto& [name, contact] : m_contacts_by_name) {
            if (name.find(pattern) != std::string::npos) {
                results.push_back(contact);
            }
        }
        
        return results;
    }
    
    // Get all contacts
    std::vector<Contact> getAllContacts() const {
        std::vector<Contact> contacts;
        contacts.reserve(m_contacts_by_name.size());
        
        for (const auto& [name, contact] : m_contacts_by_name) {
            contacts.push_back(contact);
        }
        
        std::sort(contacts.begin(), contacts.end(),
            [](const Contact& a, const Contact& b) {
                return a.name < b.name;
            });
        
        return contacts;
    }
    
    // Get statistics
    struct Statistics {
        size_t total_contacts;
        size_t unique_phones;
        size_t unique_emails;
    };
    
    Statistics getStatistics() const {
        return {
            m_contacts_by_name.size(),
            m_phone_to_name.size(),
            m_email_to_name.size()
        };
    }
    
    // Display contact
    void displayContact(const Contact& contact) const {
        std::cout << "Name: " << contact.name << std::endl;
        std::cout << "Phone: " << contact.phone << std::endl;
        std::cout << "Email: " << contact.email << std::endl;
        if (!contact.address.empty()) {
            std::cout << "Address: " << contact.address << std::endl;
        }
        std::cout << std::endl;
    }
    
    // Display all contacts
    void displayAllContacts() const {
        auto contacts = getAllContacts();
        
        std::cout << "\n=== All Contacts (" << contacts.size() << ") ===" << std::endl;
        for (const auto& contact : contacts) {
            displayContact(contact);
        }
    }
    
    // Clear all contacts
    void clear() {
        m_contacts_by_name.clear();
        m_phone_to_name.clear();
        m_email_to_name.clear();
    }
};

int main() {
    ContactManager manager;
    
    std::cout << "=== Contact Management System ===" << std::endl;
    
    // Add contacts
    manager.addContact("Alice Johnson", "555-0101", "alice@email.com", "123 Main St");
    manager.addContact("Bob Smith", "555-0102", "bob@email.com", "456 Oak Ave");
    manager.addContact("Charlie Brown", "555-0103", "charlie@email.com", "789 Pine Rd");
    manager.addContact("Diana Prince", "555-0104", "diana@email.com", "321 Elm St");
    
    manager.displayAllContacts();
    
    // Search operations
    std::cout << "=== Search Operations ===" << std::endl;
    
    Contact contact;
    if (manager.findByName("Alice Johnson", contact)) {
        std::cout << "Found by name:" << std::endl;
        manager.displayContact(contact);
    }
    
    if (manager.findByPhone("555-0102", contact)) {
        std::cout << "Found by phone:" << std::endl;
        manager.displayContact(contact);
    }
    
    // Search by pattern
    auto results = manager.searchByName("Ali");
    std::cout << "Contacts matching 'Ali':" << std::endl;
    for (const auto& c : results) {
        std::cout << "  " << c.name << std::endl;
    }
    
    // Update contact
    std::cout << "=== Update Contact ===" << std::endl;
    manager.updateContact("Bob Smith", "555-9999", "bob.smith@newemail.com", "999 New Address");
    
    // Display updated contact
    if (manager.findByName("Bob Smith", contact)) {
        manager.displayContact(contact);
    }
    
    // Show statistics
    auto stats = manager.getStatistics();
    std::cout << "=== Statistics ===" << std::endl;
    std::cout << "Total contacts: " << stats.total_contacts << std::endl;
    std::cout << "Unique phones: " << stats.unique_phones << std::endl;
    std::cout << "Unique emails: " << stats.unique_emails << std::endl;
    
    return 0;
}
```

### Example 4: Cache with LRU Eviction
```cpp
#include <iostream>
#include <unordered_map>
#include <list>
#include <optional>

template<typename Key, typename Value>
class LRUCache {
private:
    struct CacheNode {
        Key key;
        Value value;
        
        CacheNode(const Key& k, const Value& v) : key(k), value(v) {}
    };
    
    std::list<CacheNode> m_usage_list;
    std::unordered_map<Key, typename std::list<CacheNode>::iterator> m_cache_map;
    size_t m_capacity;
    
public:
    LRUCache(size_t capacity) : m_capacity(capacity) {}
    
    // Get value by key
    std::optional<Value> get(const Key& key) {
        auto it = m_cache_map.find(key);
        if (it == m_cache_map.end()) {
            return std::nullopt;
        }
        
        // Move to front (most recently used)
        m_usage_list.splice(m_usage_list.begin(), m_usage_list, it->second);
        
        return it->second->value;
    }
    
    // Put or update value
    void put(const Key& key, const Value& value) {
        auto it = m_cache_map.find(key);
        
        if (it != m_cache_map.end()) {
            // Update existing item
            it->second->value = value;
            // Move to front
            m_usage_list.splice(m_usage_list.begin(), m_usage_list, it->second);
        } else {
            // Add new item
            if (m_usage_list.size() >= m_capacity) {
                // Remove least recently used (back of list)
                const Key& lru_key = m_usage_list.back().key;
                m_cache_map.erase(lru_key);
                m_usage_list.pop_back();
            }
            
            m_usage_list.emplace_front(key, value);
            m_cache_map[key] = m_usage_list.begin();
        }
    }
    
    // Remove key
    bool remove(const Key& key) {
        auto it = m_cache_map.find(key);
        if (it == m_cache_map.end()) {
            return false;
        }
        
        m_usage_list.erase(it->second);
        m_cache_map.erase(it);
        return true;
    }
    
    // Check if key exists
    bool contains(const Key& key) const {
        return m_cache_map.find(key) != m_cache_map.end();
    }
    
    // Get current size
    size_t size() const {
        return m_usage_list.size();
    }
    
    // Check if empty
    bool empty() const {
        return m_usage_list.empty();
    }
    
    // Clear cache
    void clear() {
        m_usage_list.clear();
        m_cache_map.clear();
    }
    
    // Get all keys in order of recency
    std::vector<Key> getKeysInOrder() const {
        std::vector<Key> keys;
        for (const auto& node : m_usage_list) {
            keys.push_back(node.key);
        }
        return keys;
    }
    
    // Display cache contents
    void display() const {
        std::cout << "Cache contents (MRU -> LRU): ";
        for (const auto& node : m_usage_list) {
            std::cout << "[" << node.key << ": " << node.value << "] ";
        }
        std::cout << std::endl;
    }
    
    // Get cache statistics
    struct Statistics {
        size_t capacity;
        size_t current_size;
        double utilization;
    };
    
    Statistics getStatistics() const {
        return {
            m_capacity,
            m_usage_list.size(),
            m_capacity > 0 ? static_cast<double>(m_usage_list.size()) / m_capacity : 0.0
        };
    }
};

int main() {
    LRUCache<std::string, int> cache(3);
    
    std::cout << "=== LRU Cache Test ===" << std::endl;
    
    // Add items
    cache.put("apple", 10);
    cache.put("banana", 20);
    cache.put("cherry", 30);
    cache.display();
    
    // Access existing item (moves to MRU)
    auto value = cache.get("apple");
    if (value) {
        std::cout << "Found apple: " << *value << std::endl;
        cache.display();
    }
    
    // Add new item (should evict LRU)
    cache.put("date", 40);
    cache.display();
    
    // Try to access evicted item
    value = cache.get("banana");
    if (!value) {
        std::cout << "banana was evicted from cache" << std::endl;
    }
    
    // Update existing item
    cache.put("apple", 15);
    cache.display();
    
    // Remove item
    cache.remove("cherry");
    cache.display();
    
    // Show statistics
    auto stats = cache.getStatistics();
    std::cout << "\n=== Statistics ===" << std::endl;
    std::cout << "Capacity: " << stats.capacity << std::endl;
    std::cout << "Current size: " << stats.current_size << std::endl;
    std::cout << "Utilization: " << (stats.utilization * 100) << "%" << std::endl;
    
    // Test with integer keys
    std::cout << "\n=== Integer Key Test ===" << std::endl;
    LRUCache<int, std::string> int_cache(2);
    
    int_cache.put(1, "one");
    int_cache.put(2, "two");
    int_cache.display();
    
    int_cache.put(3, "three");  // Should evict key 1
    int_cache.display();
    
    auto str_value = int_cache.get(1);
    if (!str_value) {
        std::cout << "Key 1 was evicted" << std::endl;
    }
    
    return 0;
}
```

## 📊 Complete Function Reference

### Element Access
| Function | Description | Complexity |
|----------|-------------|------------|
| `operator[]` | Access/insert element (creates if missing) | Average O(1) |
| `at()` | Access element with bounds checking | Average O(1) |
| `find()` | Find element by key | Average O(1) |
| `count()` | Count occurrences of key | Average O(1) |

### Modifiers
| Function | Description | Complexity |
|----------|-------------|------------|
| `insert()` | Insert element(s) | Average O(1) |
| `insert_or_assign()` | Insert or update element | Average O(1) |
| `erase()` | Remove element(s) | Average O(1) |
| `clear()` | Remove all elements | O(n) |
| `swap()` | Swap contents | O(1) |

### Bucket Operations
| Function | Description | Complexity |
|----------|-------------|------------|
| `bucket_count()` | Number of buckets | O(1) |
| `bucket_size()` | Elements in specific bucket | O(bucket_size) |
| `bucket()` | Bucket index for key | O(1) |
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
    size_t operator()(int key) const {
        return std::hash<int>{}(key);
    }
};

// Poor hash function: causes collisions
struct BadHash {
    size_t operator()(int key) const {
        return key % 10;  // Only 10 buckets!
    }
};
```

### Load Factor Management
```cpp
std::unordered_map<int, std::string> map;

// Set maximum load factor (default is 1.0)
map.max_load_factor(0.75);

// Reserve space to avoid rehashing
map.reserve(1000);  // Good for known sizes

// Monitor performance
std::cout << "Load factor: " << map.load_factor() << std::endl;
std::cout << "Bucket count: " << map.bucket_count() << std::endl;
```

## 🎯 Common Patterns

### Pattern 1: Frequency Counter
```cpp
class FrequencyCounter {
private:
    std::unordered_map<std::string, int> m_counts;
    
public:
    void add(const std::string& item) {
        m_counts[item]++;
    }
    
    int get(const std::string& item) const {
        auto it = m_counts.find(item);
        return it != m_counts.end() ? it->second : 0;
    }
};
```

### Pattern 2: Cache Implementation
```cpp
template<typename K, typename V>
class SimpleCache {
private:
    std::unordered_map<K, V> m_cache;
    
public:
    std::optional<V> get(const K& key) {
        auto it = m_cache.find(key);
        return it != m_cache.end() ? std::optional<V>{it->second} : std::nullopt;
    }
    
    void put(const K& key, const V& value) {
        m_cache[key] = value;
    }
};
```

## 🐛 Common Pitfalls & Solutions

### 1. Poor Hash Function Performance
```cpp
// Problem - using pointers as keys without custom hash
std::unordered_map<int*, std::string> map;  // Uses pointer address, not value

// Solution - custom hash for pointer values
struct IntPtrHash {
    size_t operator()(const int* ptr) const {
        return std::hash<int>{}(*ptr);
    }
};

std::unordered_map<int*, std::string, IntPtrHash> good_map;
```

### 2. Iterator Invalidation
```cpp
// Problem - rehashing invalidates iterators
std::unordered_map<int, std::string> map;
auto it = map.begin();
map.insert({100, "value"});  // Might cause rehash
// it may be invalid

// Solution - be cautious with iterators during modifications
```

### 3. Unordered Iteration
```cpp
// Problem - relying on iteration order
for (const auto& [key, value] : map) {
    // Order is not guaranteed!
}

// Solution - use ordered container if order matters
std::map<int, std::string> ordered_map;  // Maintains order
```

## 📚 Related Headers

- `map.md` - Ordered key-value container
- `unordered_set.md` - Hash-based unique container
- `set.md` - Ordered unique container
- `functional.md` - Hash function objects

## 🚀 Best Practices

1. **Use unordered_map** for average O(1) lookup performance
2. **Reserve space** when you know the expected size
3. **Choose good hash functions** for custom keys
4. **Monitor load factor** for performance tuning
5. **Use map** when iteration order matters
6. **Consider custom allocators** for memory-constrained environments

## 🎯 When to Use unordered_map

✅ **Use unordered_map when:**
- Need fast average O(1) lookup/insertion/deletion
- Order of elements doesn't matter
- Keys have good hash distribution
- Memory usage is not critical
- Frequent random access by key

❌ **Avoid when:**
- Need ordered iteration (use `map`)
- Keys have poor hash properties
- Memory is severely constrained
- Need range queries by key
- Worst-case performance is critical

---

**Examples in this file**: 4 complete programs  
**Key Functions**: `operator[]`, `at()`, `find()`, `insert()`, `erase()`, `rehash()`, `reserve()`  
**Time Complexity**: Average O(1), Worst-case O(n)  
**Space Complexity**: O(n) where n is number of elements
