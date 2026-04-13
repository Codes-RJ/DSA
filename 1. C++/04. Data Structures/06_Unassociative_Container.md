# Unordered Associative Containers in C++

## Overview
Unordered associative containers are hash-based containers that provide average constant-time complexity for insertion, deletion, and lookup. Unlike ordered associative containers (set, map), they do not maintain elements in sorted order. C++ provides four unordered containers: `std::unordered_set`, `std::unordered_multiset`, `std::unordered_map`, and `std::unordered_multimap`.

## Key Characteristics

| Container | Elements | Key-Value | Duplicates | Ordering | Implementation |
|-----------|----------|-----------|------------|----------|----------------|
| unordered_set | Unique keys | No | No | Unordered | Hash Table |
| unordered_multiset | Non-unique keys | No | Yes | Unordered | Hash Table |
| unordered_map | Unique keys | Yes | No | Unordered | Hash Table |
| unordered_multimap | Non-unique keys | Yes | Yes | Unordered | Hash Table |

**Time Complexity:**
- Insert: O(1) average, O(n) worst case
- Delete: O(1) average, O(n) worst case
- Search: O(1) average, O(n) worst case
- Access: O(1) average, O(n) worst case

---

## 1. std::unordered_set (Hash-Based Unique Elements)

### Theory
`std::unordered_set` is a hash-based container that stores unique elements in no particular order. It provides constant-time average complexity for most operations. Elements are hashed using a hash function, and collisions are handled through chaining.

**Use Cases:**
- Fast membership testing (O(1) average)
- Removing duplicates from a collection
- Implementing sets where order doesn't matter
- Caching and lookup tables
- Graph algorithms (visited set)

### All Functions and Operations

```cpp
#include <iostream>
#include <unordered_set>
#include <string>
#include <vector>
#include <algorithm>

void demonstrateUnorderedSet() {
    std::cout << "\n========== STD::UNORDERED_SET ==========\n";
    
    // ==================== CONSTRUCTORS & INITIALIZATION ====================
    std::cout << "\n--- Constructors & Initialization ---\n";
    
    // Default constructor
    std::unordered_set<int> us1;
    
    // Initializer list
    std::unordered_set<int> us2 = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    // Range constructor
    std::vector<int> vec = {1, 2, 3, 4, 5};
    std::unordered_set<int> us3(vec.begin(), vec.end());
    
    // Copy constructor
    std::unordered_set<int> us4(us2);
    
    // Move constructor (C++11)
    std::unordered_set<int> us5(std::move(us4));
    
    // Constructor with custom hash and bucket count
    std::unordered_set<int> us6(100);  // Reserve 100 buckets
    
    // ==================== HASH FUNCTIONS & BUCKETS ====================
    std::cout << "\n--- Hash Functions & Buckets ---\n";
    
    std::unordered_set<int> bucket_us = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    std::cout << "Bucket count: " << bucket_us.bucket_count() << "\n";
    std::cout << "Load factor: " << bucket_us.load_factor() << "\n";
    std::cout << "Max load factor: " << bucket_us.max_load_factor() << "\n";
    
    // Show which bucket each element is in
    std::cout << "Element distribution:\n";
    for (int x : bucket_us) {
        std::cout << "  " << x << " -> bucket " << bucket_us.bucket(x) << "\n";
    }
    
    // Reserve buckets (rehashes if needed)
    bucket_us.reserve(100);
    std::cout << "After reserve(100) - Bucket count: " << bucket_us.bucket_count() << "\n";
    
    // Rehash to a specific bucket count
    bucket_us.rehash(50);
    std::cout << "After rehash(50) - Bucket count: " << bucket_us.bucket_count() << "\n";
    
    // ==================== INSERTION ====================
    std::cout << "\n--- Insertion ---\n";
    
    std::unordered_set<int> insert_us;
    
    // insert single element
    auto result = insert_us.insert(10);
    std::cout << "Inserted 10: " << (result.second ? "Success" : "Failed") << "\n";
    
    // insert duplicate (will fail)
    result = insert_us.insert(10);
    std::cout << "Insert duplicate 10: " << (result.second ? "Success" : "Failed") << "\n";
    
    // insert with hint (hint is ignored in unordered_set)
    insert_us.insert(insert_us.begin(), 20);
    
    // insert multiple elements
    insert_us.insert({30, 40, 50});
    
    // insert range
    std::vector<int> more = {60, 70, 80};
    insert_us.insert(more.begin(), more.end());
    
    // emplace (C++11) - construct in place
    struct Person {
        std::string name;
        int age;
        Person(std::string n, int a) : name(std::move(n)), age(a) {}
        
        bool operator==(const Person& other) const {
            return name == other.name && age == other.age;
        }
    };
    
    // Custom hash for Person
    struct PersonHash {
        std::size_t operator()(const Person& p) const {
            return std::hash<std::string>()(p.name) ^ 
                   (std::hash<int>()(p.age) << 1);
        }
    };
    
    std::unordered_set<Person, PersonHash> person_set;
    person_set.emplace("Alice", 25);
    person_set.emplace("Bob", 30);
    person_set.emplace("Charlie", 20);
    
    std::cout << "Set after insertions: ";
    for (int x : insert_us) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== DELETION ====================
    std::cout << "\n--- Deletion ---\n";
    
    std::unordered_set<int> delete_us = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    // erase by value
    size_t erased = delete_us.erase(5);
    std::cout << "Erased 5: " << erased << " element(s)\n";
    
    // erase by iterator
    auto it = delete_us.find(3);
    if (it != delete_us.end()) {
        delete_us.erase(it);
        std::cout << "Erased element at iterator (3)\n";
    }
    
    // erase range
    auto first = delete_us.begin();
    auto last = delete_us.begin();
    std::advance(first, 2);
    std::advance(last, 5);
    delete_us.erase(first, last);
    std::cout << "Erased range [2nd, 5th) elements\n";
    
    // clear all
    delete_us.clear();
    std::cout << "After clear - Size: " << delete_us.size() << "\n";
    
    // ==================== SEARCHING & LOOKUP ====================
    std::cout << "\n--- Searching & Lookup ---\n";
    
    std::unordered_set<int> search_us = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    
    // find
    auto find_it = search_us.find(30);
    if (find_it != search_us.end()) {
        std::cout << "Found 30\n";
    }
    
    // count (returns 0 or 1 for unordered_set)
    std::cout << "Count of 30: " << search_us.count(30) << "\n";
    std::cout << "Count of 35: " << search_us.count(35) << "\n";
    
    // contains (C++20)
    #if __cplusplus >= 202002L
    std::cout << "Contains 30? " << (search_us.contains(30) ? "Yes" : "No") << "\n";
    #endif
    
    // ==================== SIZE & CAPACITY ====================
    std::cout << "\n--- Size & Capacity ---\n";
    
    std::unordered_set<int> size_us = {1, 2, 3, 4, 5};
    
    std::cout << "Size: " << size_us.size() << "\n";
    std::cout << "Empty? " << (size_us.empty() ? "Yes" : "No") << "\n";
    std::cout << "Bucket count: " << size_us.bucket_count() << "\n";
    std::cout << "Load factor: " << size_us.load_factor() << "\n";
    
    // ==================== ITERATORS ====================
    std::cout << "\n--- Iterators (Order Not Guaranteed) ---\n";
    
    std::unordered_set<int> iter_us = {10, 20, 30, 40, 50};
    
    // Forward iteration (order is arbitrary)
    std::cout << "Elements (order may vary): ";
    for (auto it = iter_us.begin(); it != iter_us.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    // Range-based for loop
    std::cout << "Range-based for: ";
    for (const auto& elem : iter_us) {
        std::cout << elem << " ";
    }
    std::cout << "\n";
    
    // ==================== SWAPPING ====================
    std::cout << "\n--- Swapping ---\n";
    
    std::unordered_set<int> swap1 = {1, 2, 3};
    std::unordered_set<int> swap2 = {10, 20, 30, 40, 50};
    
    swap1.swap(swap2);
    std::cout << "After swap - swap1: ";
    for (int x : swap1) std::cout << x << " ";
    std::cout << "\nAfter swap - swap2: ";
    for (int x : swap2) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== PRACTICAL EXAMPLES ====================
    
    // Example 1: Fast Membership Testing
    std::cout << "\n--- Example 1: Fast Membership Testing ---\n";
    
    std::unordered_set<int> numbers_set;
    for (int i = 0; i < 1000000; i++) {
        numbers_set.insert(i);
    }
    
    auto testMembership = [&](int value) {
        auto start = std::chrono::high_resolution_clock::now();
        bool found = numbers_set.find(value) != numbers_set.end();
        auto end = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start);
        std::cout << "  " << value << ": " << (found ? "Found" : "Not found") 
                  << " (took " << duration.count() << " ns)\n";
    };
    
    testMembership(500000);
    testMembership(1500000);
    
    // Example 2: Remove Duplicates from Vector
    std::cout << "\n--- Example 2: Remove Duplicates ---\n";
    
    std::vector<int> dup_vec = {5, 2, 8, 2, 5, 3, 8, 1, 9, 3, 5, 7, 1, 4, 6, 9};
    std::unordered_set<int> unique_set(dup_vec.begin(), dup_vec.end());
    std::vector<int> unique_vec(unique_set.begin(), unique_set.end());
    
    std::cout << "Original: ";
    for (int x : dup_vec) std::cout << x << " ";
    std::cout << "\nUnique: ";
    for (int x : unique_vec) std::cout << x << " ";
    std::cout << "\n";
    
    // Example 3: Custom Hash for Strings (Case-Insensitive)
    std::cout << "\n--- Example 3: Case-Insensitive String Set ---\n";
    
    struct CaseInsensitiveHash {
        std::size_t operator()(const std::string& s) const {
            std::string lower;
            for (char c : s) {
                lower += std::tolower(c);
            }
            return std::hash<std::string>()(lower);
        }
    };
    
    struct CaseInsensitiveEqual {
        bool operator()(const std::string& a, const std::string& b) const {
            if (a.size() != b.size()) return false;
            for (size_t i = 0; i < a.size(); i++) {
                if (std::tolower(a[i]) != std::tolower(b[i])) return false;
            }
            return true;
        }
    };
    
    std::unordered_set<std::string, CaseInsensitiveHash, CaseInsensitiveEqual> case_insensitive_set;
    case_insensitive_set.insert("Hello");
    case_insensitive_set.insert("WORLD");
    case_insensitive_set.insert("hello");  // Duplicate, won't insert
    
    std::cout << "Case-insensitive set: ";
    for (const auto& s : case_insensitive_set) {
        std::cout << s << " ";
    }
    std::cout << "\n";
    
    // Example 4: Graph Visited Set for DFS
    std::cout << "\n--- Example 4: Graph DFS with Visited Set ---\n";
    
    std::vector<std::vector<int>> graph = {
        {1, 2},     // 0 -> 1,2
        {0, 3, 4},  // 1 -> 0,3,4
        {0, 5},     // 2 -> 0,5
        {1},        // 3 -> 1
        {1},        // 4 -> 1
        {2}         // 5 -> 2
    };
    
    auto dfs = [&](int start) {
        std::unordered_set<int> visited;
        std::stack<int> stack;
        stack.push(start);
        
        std::cout << "DFS traversal: ";
        while (!stack.empty()) {
            int node = stack.top();
            stack.pop();
            
            if (visited.find(node) == visited.end()) {
                visited.insert(node);
                std::cout << node << " ";
                
                for (int neighbor : graph[node]) {
                    if (visited.find(neighbor) == visited.end()) {
                        stack.push(neighbor);
                    }
                }
            }
        }
        std::cout << "\n";
    };
    
    dfs(0);
    
    // Example 5: Set of Custom Objects
    std::cout << "\n--- Example 5: Custom Object Set ---\n";
    
    struct Point {
        int x, y;
        
        bool operator==(const Point& other) const {
            return x == other.x && y == other.y;
        }
    };
    
    struct PointHash {
        std::size_t operator()(const Point& p) const {
            return std::hash<int>()(p.x) ^ (std::hash<int>()(p.y) << 1);
        }
    };
    
    std::unordered_set<Point, PointHash> points;
    points.insert({1, 2});
    points.insert({3, 4});
    points.insert({1, 2});  // Duplicate, won't insert
    
    std::cout << "Points in set: ";
    for (const auto& p : points) {
        std::cout << "(" << p.x << "," << p.y << ") ";
    }
    std::cout << "\n";
}
```

---

## 2. std::unordered_multiset (Hash-Based Non-Unique Elements)

### Theory
`std::unordered_multiset` is similar to `unordered_set` but allows duplicate elements. It provides constant-time average complexity for most operations and maintains elements in no particular order.

**Use Cases:**
- Frequency counting with hash-based storage
- Multiset implementation where order doesn't matter
- Bag data structure
- Histogram with fast lookups

### All Functions and Operations

```cpp
#include <iostream>
#include <unordered_set>
#include <string>
#include <vector>

void demonstrateUnorderedMultiset() {
    std::cout << "\n========== STD::UNORDERED_MULTISET ==========\n";
    
    // ==================== CONSTRUCTORS & INITIALIZATION ====================
    std::cout << "\n--- Constructors & Initialization ---\n";
    
    // Default constructor
    std::unordered_multiset<int> ums1;
    
    // Initializer list (allows duplicates)
    std::unordered_multiset<int> ums2 = {5, 2, 8, 2, 5, 3, 8, 1, 9, 3, 5};
    
    // Range constructor
    std::vector<int> vec = {1, 2, 2, 3, 3, 3};
    std::unordered_multiset<int> ums3(vec.begin(), vec.end());
    
    // Copy constructor
    std::unordered_multiset<int> ums4(ums2);
    
    // ==================== INSERTION ====================
    std::cout << "\n--- Insertion (Allows Duplicates) ---\n";
    
    std::unordered_multiset<int> insert_ums;
    
    // insert single element
    insert_ums.insert(10);
    insert_ums.insert(10);  // Duplicate allowed
    insert_ums.insert(20);
    insert_ums.insert(20);
    insert_ums.insert(20);
    
    // insert with hint (hint is ignored)
    insert_ums.insert(insert_ums.begin(), 15);
    
    // insert multiple elements
    insert_ums.insert({30, 30, 40, 50});
    
    // insert range
    std::vector<int> more = {5, 5, 5, 6, 6};
    insert_ums.insert(more.begin(), more.end());
    
    // emplace (C++11)
    insert_ums.emplace(25);
    
    std::cout << "Multiset after insertions (order may vary): ";
    for (int x : insert_ums) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== DELETION ====================
    std::cout << "\n--- Deletion ---\n";
    
    std::unordered_multiset<int> delete_ums = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5};
    
    std::cout << "Original multiset: ";
    for (int x : delete_ums) std::cout << x << " ";
    std::cout << "\n";
    
    // erase all occurrences of a value
    size_t erased = delete_ums.erase(3);
    std::cout << "Erased " << erased << " occurrences of 3\n";
    
    // erase single occurrence using iterator
    auto it = delete_ums.find(4);
    if (it != delete_ums.end()) {
        delete_ums.erase(it);
        std::cout << "Erased one occurrence of 4\n";
    }
    
    // erase range
    auto first = delete_ums.begin();
    auto last = delete_ums.begin();
    std::advance(first, 2);
    std::advance(last, 5);
    delete_ums.erase(first, last);
    std::cout << "Erased range of elements\n";
    
    // clear all
    delete_ums.clear();
    std::cout << "After clear - Size: " << delete_ums.size() << "\n";
    
    // ==================== SEARCHING & LOOKUP ====================
    std::cout << "\n--- Searching & Lookup ---\n";
    
    std::unordered_multiset<int> search_ums = {10, 20, 20, 30, 30, 30, 40, 40, 40, 40, 50};
    
    // find (returns first occurrence)
    auto find_it = search_ums.find(30);
    if (find_it != search_ums.end()) {
        std::cout << "Found a 30\n";
    }
    
    // count (returns number of occurrences)
    std::cout << "Count of 30: " << search_ums.count(30) << "\n";
    std::cout << "Count of 40: " << search_ums.count(40) << "\n";
    std::cout << "Count of 35: " << search_ums.count(35) << "\n";
    
    // equal_range (range of all elements equal to key)
    auto range = search_ums.equal_range(30);
    std::cout << "All 30s: ";
    for (auto it = range.first; it != range.second; ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    // ==================== SIZE & CAPACITY ====================
    std::cout << "\n--- Size & Capacity ---\n";
    
    std::unordered_multiset<int> size_ums = {1, 1, 2, 2, 2, 3, 3, 3, 3};
    
    std::cout << "Size: " << size_ums.size() << "\n";
    std::cout << "Bucket count: " << size_ums.bucket_count() << "\n";
    std::cout << "Load factor: " << size_ums.load_factor() << "\n";
    std::cout << "Empty? " << (size_ums.empty() ? "Yes" : "No") << "\n";
    
    // ==================== PRACTICAL EXAMPLES ====================
    
    // Example 1: Frequency Counter (Unordered)
    std::cout << "\n--- Example 1: Frequency Counter ---\n";
    
    std::vector<int> data = {1, 2, 3, 2, 1, 3, 3, 4, 5, 4, 3, 2, 1, 1, 1};
    std::unordered_multiset<int> freq_ums(data.begin(), data.end());
    
    // Get unique values (using unordered_set)
    std::unordered_set<int> unique_vals(data.begin(), data.end());
    std::cout << "Element frequencies:\n";
    for (int val : unique_vals) {
        std::cout << "  " << val << ": " << freq_ums.count(val) << " times\n";
    }
    
    // Example 2: Bag/Multiset Implementation
    std::cout << "\n--- Example 2: Shopping Cart (Bag) ---\n";
    
    class ShoppingCart {
    private:
        std::unordered_multiset<std::string> items;
        
    public:
        void addItem(const std::string& item) {
            items.insert(item);
            std::cout << "Added: " << item << "\n";
        }
        
        void removeItem(const std::string& item) {
            auto it = items.find(item);
            if (it != items.end()) {
                items.erase(it);
                std::cout << "Removed: " << item << "\n";
            } else {
                std::cout << "Item not found: " << item << "\n";
            }
        }
        
        void removeAll(const std::string& item) {
            size_t count = items.erase(item);
            std::cout << "Removed " << count << " copies of " << item << "\n";
        }
        
        int getCount(const std::string& item) const {
            return items.count(item);
        }
        
        void display() const {
            if (items.empty()) {
                std::cout << "Cart is empty\n";
                return;
            }
            
            std::cout << "Cart contents:\n";
            std::unordered_set<std::string> unique_items;
            for (const auto& item : items) {
                unique_items.insert(item);
            }
            
            for (const auto& item : unique_items) {
                std::cout << "  " << item << ": " << items.count(item) << "x\n";
            }
        }
    };
    
    ShoppingCart cart;
    cart.addItem("Apple");
    cart.addItem("Apple");
    cart.addItem("Banana");
    cart.addItem("Apple");
    cart.addItem("Orange");
    cart.display();
    
    std::cout << "\nApple count: " << cart.getCount("Apple") << "\n";
    cart.removeItem("Apple");
    cart.display();
    cart.removeAll("Apple");
    cart.display();
    
    // Example 3: Histogram with Buckets
    std::cout << "\n--- Example 3: Grade Histogram ---\n";
    
    std::vector<int> grades = {85, 92, 78, 85, 91, 92, 85, 78, 90, 85, 92, 91, 88, 95, 87, 89};
    std::unordered_multiset<int> grade_multiset(grades.begin(), grades.end());
    
    auto gradeToLetter = [](int grade) -> char {
        if (grade >= 90) return 'A';
        if (grade >= 80) return 'B';
        if (grade >= 70) return 'C';
        if (grade >= 60) return 'D';
        return 'F';
    };
    
    std::unordered_map<char, int> letter_counts;
    for (int g : grades) {
        letter_counts[gradeToLetter(g)]++;
    }
    
    std::cout << "Grade distribution:\n";
    for (char letter : {'A', 'B', 'C', 'D', 'F'}) {
        std::cout << "  " << letter << ": " << std::string(letter_counts[letter], '*') 
                  << " (" << letter_counts[letter] << ")\n";
    }
}
```

---

## 3. std::unordered_map (Hash-Based Key-Value Pairs)

### Theory
`std::unordered_map` is a hash-based associative container that stores key-value pairs with unique keys. It provides constant-time average complexity for insertion, deletion, and lookup. Keys are hashed, and elements are stored in no particular order.

**Use Cases:**
- Fast dictionary/lookup tables (O(1) average)
- Caching systems
- Symbol tables
- Frequency counters
- Graph adjacency lists (when order doesn't matter)

### All Functions and Operations

```cpp
#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>
#include <chrono>

void demonstrateUnorderedMap() {
    std::cout << "\n========== STD::UNORDERED_MAP ==========\n";
    
    // ==================== CONSTRUCTORS & INITIALIZATION ====================
    std::cout << "\n--- Constructors & Initialization ---\n";
    
    // Default constructor
    std::unordered_map<std::string, int> um1;
    
    // Initializer list
    std::unordered_map<std::string, int> um2 = {
        {"Alice", 95},
        {"Bob", 87},
        {"Charlie", 92}
    };
    
    // Range constructor
    std::vector<std::pair<std::string, int>> vec = {{"David", 88}, {"Eve", 91}};
    std::unordered_map<std::string, int> um3(vec.begin(), vec.end());
    
    // Copy constructor
    std::unordered_map<std::string, int> um4(um2);
    
    // ==================== HASH FUNCTIONS & BUCKETS ====================
    std::cout << "\n--- Hash Functions & Buckets ---\n";
    
    std::unordered_map<std::string, int> bucket_um = {
        {"Alice", 95}, {"Bob", 87}, {"Charlie", 92},
        {"David", 88}, {"Eve", 91}, {"Frank", 85}
    };
    
    std::cout << "Bucket count: " << bucket_um.bucket_count() << "\n";
    std::cout << "Load factor: " << bucket_um.load_factor() << "\n";
    std::cout << "Max load factor: " << bucket_um.max_load_factor() << "\n";
    
    // Show which bucket each key is in
    std::cout << "Key distribution:\n";
    for (const auto& [key, value] : bucket_um) {
        std::cout << "  " << key << " -> bucket " << bucket_um.bucket(key) << "\n";
    }
    
    // Reserve buckets
    bucket_um.reserve(100);
    std::cout << "After reserve(100) - Bucket count: " << bucket_um.bucket_count() << "\n";
    
    // ==================== INSERTION ====================
    std::cout << "\n--- Insertion ---\n";
    
    std::unordered_map<std::string, int> insert_um;
    
    // Using operator[]
    insert_um["Alice"] = 95;
    insert_um["Bob"] = 87;
    
    // Using insert with pair
    insert_um.insert(std::pair<std::string, int>("Charlie", 92));
    insert_um.insert({"David", 88});  // C++11
    
    // Insert returns pair<iterator, bool> indicating success
    auto result = insert_um.insert({"Alice", 100});  // Duplicate key
    if (!result.second) {
        std::cout << "Key 'Alice' already exists with value: " << result.first->second << "\n";
    }
    
    // Insert with hint (hint is ignored)
    insert_um.insert(insert_um.begin(), std::make_pair("Eve", 91));
    
    // Insert range
    std::unordered_map<std::string, int> more = {{"Frank", 85}, {"Grace", 89}};
    insert_um.insert(more.begin(), more.end());
    
    // emplace (C++11)
    insert_um.emplace("Henry", 93);
    
    // emplace_hint (C++11)
    insert_um.emplace_hint(insert_um.begin(), "Ivy", 86);
    
    // try_emplace (C++17) - doesn't move arguments if insertion fails
    insert_um.try_emplace("Jack", 90);
    
    std::cout << "Map after insertions:\n";
    for (const auto& [key, value] : insert_um) {
        std::cout << "  " << key << ": " << value << "\n";
    }
    
    // ==================== ACCESSING ELEMENTS ====================
    std::cout << "\n--- Accessing Elements ---\n";
    
    std::unordered_map<std::string, int> access_um = {
        {"Alice", 95}, {"Bob", 87}, {"Charlie", 92}
    };
    
    // Using operator[] (creates element if not exists)
    std::cout << "Alice's score: " << access_um["Alice"] << "\n";
    
    // Using .at() (throws exception if key not found)
    try {
        std::cout << "Bob's score: " << access_um.at("Bob") << "\n";
        // std::cout << access_um.at("Unknown") << "\n";  // Throws exception
    } catch (const std::out_of_range& e) {
        std::cout << "Key not found: " << e.what() << "\n";
    }
    
    // ==================== MODIFYING VALUES ====================
    std::cout << "\n--- Modifying Values ---\n";
    
    std::unordered_map<std::string, int> modify_um = {
        {"Alice", 95}, {"Bob", 87}, {"Charlie", 92}
    };
    
    // Modify using operator[]
    modify_um["Alice"] = 98;
    
    // Modify using iterator
    auto mod_it = modify_um.find("Bob");
    if (mod_it != modify_um.end()) {
        mod_it->second = 90;
    }
    
    std::cout << "After modifications:\n";
    for (const auto& [key, value] : modify_um) {
        std::cout << "  " << key << ": " << value << "\n";
    }
    
    // ==================== DELETION ====================
    std::cout << "\n--- Deletion ---\n";
    
    std::unordered_map<std::string, int> delete_um = {
        {"Alice", 95}, {"Bob", 87}, {"Charlie", 92},
        {"David", 88}, {"Eve", 91}, {"Frank", 85}
    };
    
    // erase by key
    size_t erased = delete_um.erase("Charlie");
    std::cout << "Erased Charlie: " << erased << " element\n";
    
    // erase by iterator
    auto erase_it = delete_um.find("David");
    if (erase_it != delete_um.end()) {
        delete_um.erase(erase_it);
        std::cout << "Erased David\n";
    }
    
    // erase range
    auto first = delete_um.begin();
    auto last = delete_um.begin();
    std::advance(first, 2);
    std::advance(last, 4);
    delete_um.erase(first, last);
    std::cout << "Erased range of elements\n";
    
    // clear all
    delete_um.clear();
    std::cout << "After clear - Size: " << delete_um.size() << "\n";
    
    // ==================== SEARCHING & LOOKUP ====================
    std::cout << "\n--- Searching & Lookup ---\n";
    
    std::unordered_map<std::string, int> search_um = {
        {"Alice", 95}, {"Bob", 87}, {"Charlie", 92},
        {"David", 88}, {"Eve", 91}, {"Frank", 85}
    };
    
    // find
    auto find_it = search_um.find("Charlie");
    if (find_it != search_um.end()) {
        std::cout << "Found Charlie with score: " << find_it->second << "\n";
    }
    
    // count (returns 0 or 1 for unordered_map)
    std::cout << "Count of Bob: " << search_um.count("Bob") << "\n";
    std::cout << "Count of Unknown: " << search_um.count("Unknown") << "\n";
    
    // ==================== SIZE & CAPACITY ====================
    std::cout << "\n--- Size & Capacity ---\n";
    
    std::unordered_map<std::string, int> size_um = {
        {"A", 1}, {"B", 2}, {"C", 3}, {"D", 4}, {"E", 5}
    };
    
    std::cout << "Size: " << size_um.size() << "\n";
    std::cout << "Empty? " << (size_um.empty() ? "Yes" : "No") << "\n";
    std::cout << "Bucket count: " << size_um.bucket_count() << "\n";
    std::cout << "Load factor: " << size_um.load_factor() << "\n";
    
    // ==================== ITERATORS ====================
    std::cout << "\n--- Iterators (Order Not Guaranteed) ---\n";
    
    std::unordered_map<std::string, int> iter_um = {
        {"Alice", 95}, {"Bob", 87}, {"Charlie", 92}
    };
    
    // Forward iteration
    std::cout << "Iteration (order may vary):\n";
    for (auto it = iter_um.begin(); it != iter_um.end(); ++it) {
        std::cout << "  " << it->first << ": " << it->second << "\n";
    }
    
    // Range-based for loop (C++17 structured binding)
    std::cout << "Range-based for:\n";
    for (const auto& [key, value] : iter_um) {
        std::cout << "  " << key << ": " << value << "\n";
    }
    
    // ==================== PRACTICAL EXAMPLES ====================
    
    // Example 1: Word Frequency Counter (Unordered)
    std::cout << "\n--- Example 1: Word Frequency Counter ---\n";
    
    std::string text = "the quick brown fox jumps over the lazy dog the fox jumps";
    std::unordered_map<std::string, int> word_count;
    
    std::string word;
    std::stringstream ss(text);
    while (ss >> word) {
        word_count[word]++;
    }
    
    std::cout << "Word frequencies (unordered):\n";
    for (const auto& [w, count] : word_count) {
        std::cout << "  " << w << ": " << count << "\n";
    }
    
    // Example 2: Cache with LRU (Least Recently Used) using unordered_map
    std::cout << "\n--- Example 2: LRU Cache ---\n";
    
    class LRUCache {
    private:
        struct Node {
            int key;
            int value;
            Node* prev;
            Node* next;
            Node(int k, int v) : key(k), value(v), prev(nullptr), next(nullptr) {}
        };
        
        int capacity;
        std::unordered_map<int, Node*> cache;
        Node* head;
        Node* tail;
        
        void moveToFront(Node* node) {
            if (node == head) return;
            
            // Remove node from current position
            if (node->prev) node->prev->next = node->next;
            if (node->next) node->next->prev = node->prev;
            if (node == tail) tail = node->prev;
            
            // Move to front
            node->next = head;
            node->prev = nullptr;
            if (head) head->prev = node;
            head = node;
            if (!tail) tail = head;
        }
        
        void removeTail() {
            if (!tail) return;
            cache.erase(tail->key);
            if (tail == head) {
                delete tail;
                head = tail = nullptr;
            } else {
                Node* new_tail = tail->prev;
                new_tail->next = nullptr;
                delete tail;
                tail = new_tail;
            }
        }
        
    public:
        LRUCache(int cap) : capacity(cap), head(nullptr), tail(nullptr) {}
        
        ~LRUCache() {
            Node* current = head;
            while (current) {
                Node* next = current->next;
                delete current;
                current = next;
            }
        }
        
        int get(int key) {
            auto it = cache.find(key);
            if (it == cache.end()) return -1;
            
            Node* node = it->second;
            moveToFront(node);
            return node->value;
        }
        
        void put(int key, int value) {
            auto it = cache.find(key);
            if (it != cache.end()) {
                // Update existing key
                Node* node = it->second;
                node->value = value;
                moveToFront(node);
            } else {
                // Insert new key
                Node* node = new Node(key, value);
                cache[key] = node;
                
                if (!head) {
                    head = tail = node;
                } else {
                    node->next = head;
                    head->prev = node;
                    head = node;
                }
                
                if (cache.size() > capacity) {
                    removeTail();
                }
            }
        }
        
        void display() {
            std::cout << "Cache (most recent first): ";
            Node* current = head;
            while (current) {
                std::cout << "[" << current->key << ":" << current->value << "] ";
                current = current->next;
            }
            std::cout << "\n";
        }
    };
    
    LRUCache lru(3);
    lru.put(1, 10);
    lru.put(2, 20);
    lru.put(3, 30);
    lru.display();
    lru.get(2);
    lru.display();
    lru.put(4, 40);
    lru.display();
    lru.get(1);  // Should return -1 (evicted)
    std::cout << "Get key 1: " << lru.get(1) << "\n";
    
    // Example 3: Two-Sum Problem
    std::cout << "\n--- Example 3: Two-Sum Problem ---\n";
    
    auto twoSum = [](const std::vector<int>& nums, int target) -> std::pair<int, int> {
        std::unordered_map<int, int> seen;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (seen.find(complement) != seen.end()) {
                return {seen[complement], i};
            }
            seen[nums[i]] = i;
        }
        return {-1, -1};
    };
    
    std::vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    auto [idx1, idx2] = twoSum(nums, target);
    std::cout << "Two sum indices: " << idx1 << ", " << idx2 << " (values: " 
              << nums[idx1] << " + " << nums[idx2] << " = " << target << ")\n";
    
    // Example 4: Custom Hash for Complex Keys
    std::cout << "\n--- Example 4: Custom Hash for Complex Keys ---\n";
    
    struct Person {
        std::string name;
        int age;
        
        bool operator==(const Person& other) const {
            return name == other.name && age == other.age;
        }
    };
    
    struct PersonHash {
        std::size_t operator()(const Person& p) const {
            return std::hash<std::string>()(p.name) ^ 
                   (std::hash<int>()(p.age) << 1);
        }
    };
    
    std::unordered_map<Person, int, PersonHash> person_map;
    person_map[{"Alice", 25}] = 100;
    person_map[{"Bob", 30}] = 200;
    person_map[{"Charlie", 20}] = 150;
    
    std::cout << "Person scores:\n";
    for (const auto& [person, score] : person_map) {
        std::cout << "  " << person.name << " (age " << person.age << "): " << score << "\n";
    }
    
    // Example 5: Performance Comparison (unordered_map vs map)
    std::cout << "\n--- Example 5: Performance Comparison ---\n";
    
    const int NUM_OPERATIONS = 1000000;
    
    // Test unordered_map
    std::unordered_map<int, int> unordered_test;
    auto start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < NUM_OPERATIONS; i++) {
        unordered_test[i] = i;
    }
    for (int i = 0; i < NUM_OPERATIONS; i++) {
        auto it = unordered_test.find(i);
        if (it == unordered_test.end()) std::cout << "Error\n";
    }
    auto end = std::chrono::high_resolution_clock::now();
    auto unordered_time = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    
    // Test ordered map
    std::map<int, int> ordered_test;
    start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < NUM_OPERATIONS; i++) {
        ordered_test[i] = i;
    }
    for (int i = 0; i < NUM_OPERATIONS; i++) {
        auto it = ordered_test.find(i);
        if (it == ordered_test.end()) std::cout << "Error\n";
    }
    end = std::chrono::high_resolution_clock::now();
    auto ordered_time = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    
    std::cout << "Performance for " << NUM_OPERATIONS << " operations:\n";
    std::cout << "  unordered_map: " << unordered_time.count() << " ms\n";
    std::cout << "  map: " << ordered_time.count() << " ms\n";
    std::cout << "  unordered_map is " << (ordered_time.count() / unordered_time.count()) 
              << "x faster\n";
}
```

---

## 4. std::unordered_multimap (Hash-Based Key-Value Pairs with Duplicates)

### Theory
`std::unordered_multimap` is similar to `unordered_map` but allows multiple elements with the same key. It provides constant-time average complexity and is useful for one-to-many relationships where order doesn't matter.

**Use Cases:**
- One-to-many relationships with fast lookup
- Indexing with duplicate keys
- Phone directory with multiple numbers per person
- Tagging systems

### All Functions and Operations

```cpp
#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>

void demonstrateUnorderedMultimap() {
    std::cout << "\n========== STD::UNORDERED_MULTIMAP ==========\n";
    
    // ==================== CONSTRUCTORS & INITIALIZATION ====================
    std::cout << "\n--- Constructors & Initialization ---\n";
    
    // Default constructor
    std::unordered_multimap<std::string, int> umm1;
    
    // Initializer list (allows duplicate keys)
    std::unordered_multimap<std::string, int> umm2 = {
        {"Alice", 95}, {"Bob", 87}, {"Alice", 92}, {"Bob", 88},
        {"Charlie", 91}, {"Alice", 98}
    };
    
    // Range constructor
    std::vector<std::pair<std::string, int>> vec = {{"David", 88}, {"David", 89}, {"Eve", 91}};
    std::unordered_multimap<std::string, int> umm3(vec.begin(), vec.end());
    
    // Copy constructor
    std::unordered_multimap<std::string, int> umm4(umm2);
    
    // ==================== INSERTION ====================
    std::cout << "\n--- Insertion (Allows Duplicate Keys) ---\n";
    
    std::unordered_multimap<std::string, int> insert_umm;
    
    // Insert with pair
    insert_umm.insert(std::pair<std::string, int>("Alice", 95));
    insert_umm.insert({"Alice", 92});   // Duplicate key allowed
    insert_umm.insert({"Bob", 87});
    insert_umm.insert({"Bob", 88});
    
    // Insert with make_pair
    insert_umm.insert(std::make_pair("Charlie", 91));
    
    // Insert with hint (hint is ignored)
    insert_umm.insert(insert_umm.begin(), std::make_pair("Alice", 98));
    
    // Insert range
    std::unordered_multimap<std::string, int> more = {{"David", 88}, {"David", 89}};
    insert_umm.insert(more.begin(), more.end());
    
    // emplace (C++11)
    insert_umm.emplace("Eve", 90);
    
    std::cout << "Multimap after insertions:\n";
    for (const auto& [key, value] : insert_umm) {
        std::cout << "  " << key << ": " << value << "\n";
    }
    
    // ==================== DELETION ====================
    std::cout << "\n--- Deletion ---\n";
    
    std::unordered_multimap<std::string, int> delete_umm = {
        {"Alice", 95}, {"Alice", 92}, {"Alice", 98},
        {"Bob", 87}, {"Bob", 88},
        {"Charlie", 91}
    };
    
    std::cout << "Original multimap:\n";
    for (const auto& [k, v] : delete_umm) std::cout << "  " << k << ": " << v << "\n";
    
    // erase all occurrences of a key
    size_t erased = delete_umm.erase("Alice");
    std::cout << "Erased " << erased << " entries for key 'Alice'\n";
    
    // erase single occurrence using iterator
    auto it = delete_umm.find("Bob");
    if (it != delete_umm.end()) {
        delete_umm.erase(it);
        std::cout << "Erased one occurrence of 'Bob'\n";
    }
    
    // erase range
    auto first = delete_umm.begin();
    auto last = delete_umm.begin();
    std::advance(first, 2);
    std::advance(last, 4);
    delete_umm.erase(first, last);
    std::cout << "Erased range of elements\n";
    
    // clear all
    delete_umm.clear();
    std::cout << "After clear - Size: " << delete_umm.size() << "\n";
    
    // ==================== SEARCHING & LOOKUP ====================
    std::cout << "\n--- Searching & Lookup ---\n";
    
    std::unordered_multimap<std::string, int> search_umm = {
        {"Alice", 95}, {"Alice", 92}, {"Alice", 98},
        {"Bob", 87}, {"Bob", 88},
        {"Charlie", 91}, {"Charlie", 93}
    };
    
    // find (returns first occurrence)
    auto find_it = search_umm.find("Alice");
    if (find_it != search_umm.end()) {
        std::cout << "First Alice entry: " << find_it->second << "\n";
    }
    
    // count (returns number of occurrences)
    std::cout << "Count of Alice: " << search_umm.count("Alice") << "\n";
    std::cout << "Count of Bob: " << search_umm.count("Bob") << "\n";
    std::cout << "Count of Unknown: " << search_umm.count("Unknown") << "\n";
    
    // equal_range (range of all elements with given key)
    auto range = search_umm.equal_range("Alice");
    std::cout << "All Alice scores: ";
    for (auto it = range.first; it != range.second; ++it) {
        std::cout << it->second << " ";
    }
    std::cout << "\n";
    
    // ==================== SIZE & CAPACITY ====================
    std::cout << "\n--- Size & Capacity ---\n";
    
    std::unordered_multimap<std::string, int> size_umm = {
        {"A", 1}, {"A", 2}, {"B", 3}, {"B", 4}, {"C", 5}
    };
    
    std::cout << "Size: " << size_umm.size() << "\n";
    std::cout << "Bucket count: " << size_umm.bucket_count() << "\n";
    std::cout << "Load factor: " << size_umm.load_factor() << "\n";
    std::cout << "Empty? " << (size_umm.empty() ? "Yes" : "No") << "\n";
    
    // ==================== PRACTICAL EXAMPLES ====================
    
    // Example 1: Phone Directory with Multiple Numbers
    std::cout << "\n--- Example 1: Phone Directory ---\n";
    
    std::unordered_multimap<std::string, std::string> phone_dir;
    
    phone_dir.insert({"Alice", "555-0101"});
    phone_dir.insert({"Alice", "555-0102"});
    phone_dir.insert({"Bob", "555-0201"});
    phone_dir.insert({"Bob", "555-0202"});
    phone_dir.insert({"Bob", "555-0203"});
    phone_dir.insert({"Charlie", "555-0301"});
    
    auto printNumbersFast = [&](const std::string& name) {
        auto range = phone_dir.equal_range(name);
        std::cout << name << "'s numbers: ";
        for (auto it = range.first; it != range.second; ++it) {
            std::cout << it->second << " ";
        }
        std::cout << "\n";
    };
    
    printNumbersFast("Alice");
    printNumbersFast("Bob");
    printNumbersFast("Charlie");
    
    // Example 2: Student Course Enrollment (Fast Lookup)
    std::cout << "\n--- Example 2: Course Enrollment ---\n";
    
    std::unordered_multimap<std::string, std::string> enrollments;
    
    enrollments.insert({"CS101", "Alice"});
    enrollments.insert({"CS101", "Bob"});
    enrollments.insert({"CS101", "Charlie"});
    enrollments.insert({"MATH201", "Alice"});
    enrollments.insert({"MATH201", "Diana"});
    enrollments.insert({"PHYS101", "Bob"});
    enrollments.insert({"PHYS101", "Eve"});
    
    auto getCourseStudents = [&](const std::string& course) {
        auto range = enrollments.equal_range(course);
        std::cout << "Students in " << course << ": ";
        for (auto it = range.first; it != range.second; ++it) {
            std::cout << it->second << " ";
        }
        std::cout << "\n";
    };
    
    auto getStudentCourses = [&](const std::string& student) {
        std::cout << student << "'s courses: ";
        for (const auto& [course, s] : enrollments) {
            if (s == student) std::cout << course << " ";
        }
        std::cout << "\n";
    };
    
    getCourseStudents("CS101");
    getCourseStudents("MATH201");
    getStudentCourses("Alice");
    getStudentCourses("Bob");
    
    // Example 3: Tagging System
    std::cout << "\n--- Example 3: Tagging System ---\n";
    
    std::unordered_multimap<std::string, std::string> tags;
    
    tags.insert({"Programming", "C++"});
    tags.insert({"Programming", "Python"});
    tags.insert({"Programming", "Java"});
    tags.insert({"Web", "HTML"});
    tags.insert({"Web", "CSS"});
    tags.insert({"Web", "JavaScript"});
    tags.insert({"Database", "SQL"});
    tags.insert({"Database", "MongoDB"});
    tags.insert({"Database", "PostgreSQL"});
    
    auto getItemsByTag = [&](const std::string& tag) {
        auto range = tags.equal_range(tag);
        std::cout << "Items with tag '" << tag << "': ";
        for (auto it = range.first; it != range.second; ++it) {
            std::cout << it->second << " ";
        }
        std::cout << "\n";
    };
    
    getItemsByTag("Programming");
    getItemsByTag("Web");
    getItemsByTag("Database");
    
    // Example 4: Multimap with Custom Hash
    std::cout << "\n--- Example 4: Custom Hash for Case-Insensitive Keys ---\n";
    
    struct CaseInsensitiveHashMM {
        std::size_t operator()(const std::string& s) const {
            std::string lower;
            for (char c : s) {
                lower += std::tolower(c);
            }
            return std::hash<std::string>()(lower);
        }
    };
    
    struct CaseInsensitiveEqualMM {
        bool operator()(const std::string& a, const std::string& b) const {
            if (a.size() != b.size()) return false;
            for (size_t i = 0; i < a.size(); i++) {
                if (std::tolower(a[i]) != std::tolower(b[i])) return false;
            }
            return true;
        }
    };
    
    std::unordered_multimap<std::string, int, CaseInsensitiveHashMM, CaseInsensitiveEqualMM> ci_multimap;
    ci_multimap.insert({"Apple", 1});
    ci_multimap.insert({"apple", 2});   // Different case, but considered same key
    ci_multimap.insert({"APPLE", 3});   // Same key in hash perspective
    
    std::cout << "Case-insensitive multimap:\n";
    auto ci_range = ci_multimap.equal_range("apple");
    for (auto it = ci_range.first; it != ci_range.second; ++it) {
        std::cout << "  " << it->first << ": " << it->second << "\n";
    }
}
```

---

## Performance Comparison

| Operation | unordered_set/map | set/map |
|-----------|------------------|---------|
| Insert | O(1) average, O(n) worst | O(log n) |
| Delete | O(1) average, O(n) worst | O(log n) |
| Find | O(1) average, O(n) worst | O(log n) |
| Iteration | O(n) (unordered) | O(n) (ordered) |
| Memory Overhead | Higher (buckets) | Lower |
| Order | No | Yes |

---

## Best Practices

1. **Choose unordered containers for speed** - When order doesn't matter and you need O(1) operations
2. **Choose ordered containers for range queries** - When you need lower/upper bound operations
3. **Reserve capacity when size is known** - Prevents rehashing overhead
4. **Use `reserve()` and `rehash()`** - To control bucket count and load factor
5. **Provide custom hash for user-defined types** - To enable use as keys
6. **Use `try_emplace()` (C++17)** - More efficient than `emplace()` when keys may already exist
7. **Use `equal_range()` for multimap** - To get all values for a key efficiently
8. **Monitor load factor** - High load factor degrades performance
9. **Use `contains()` (C++20)** - Cleaner existence checking

---

## Common Pitfalls

1. **Assuming order is preserved** - Unordered containers have no guaranteed order
2. **Poor hash functions causing collisions** - Can degrade to O(n) performance
3. **Not providing hash for custom types** - Compilation error
4. **Rehashing causing iterator invalidation** - Operations that rehash invalidate all iterators
5. **Using `operator[]` on const unordered_map** - Not allowed; use `at()` or `find()`
6. **High load factor** - Causes more collisions and slower performance
7. **Using unordered containers for range queries** - No lower_bound/upper_bound
8. **Modifying keys** - Keys are immutable; must remove and reinsert

---
---

## Next Step

- Go to [07_Utility.md](07_Utility.md) to continue with Utility.
