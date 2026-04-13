# Associative Containers in C++

## Overview
Associative containers store elements in a sorted order, allowing fast retrieval based on keys. They are typically implemented as balanced binary search trees (Red-Black Trees), providing logarithmic time complexity for most operations. C++ provides four main associative containers: `std::set`, `std::multiset`, `std::map`, and `std::multimap`.

## Key Characteristics

| Container | Elements | Key-Value | Duplicates | Ordering |
|-----------|----------|-----------|------------|----------|
| set | Unique keys | No | No | Sorted by key |
| multiset | Non-unique keys | No | Yes | Sorted by key |
| map | Unique keys | Yes | No | Sorted by key |
| multimap | Non-unique keys | Yes | Yes | Sorted by key |

**Time Complexity:**
- Insert: O(log n)
- Delete: O(log n)
- Search: O(log n)
- Access: O(log n)

---

## 1. std::set (Ordered Unique Elements)

### Theory
`std::set` is an associative container that stores unique elements in sorted order. It is typically implemented as a Red-Black Tree, providing logarithmic time complexity for insertion, deletion, and lookup. Elements are immutable once inserted; to modify an element, you must remove it and insert a new one.

**Use Cases:**
- Maintaining sorted unique collections
- Set operations (union, intersection, difference)
- Removing duplicates from a collection
- Fast membership testing
- Ordered iteration without duplicates
- Implementing mathematical sets

### All Functions and Operations

```cpp
#include <iostream>
#include <set>
#include <string>
#include <algorithm>
#include <iterator>

void demonstrateSet() {
    std::cout << "\n========== STD::SET ==========\n";
    
    // ==================== CONSTRUCTORS & INITIALIZATION ====================
    std::cout << "\n--- Constructors & Initialization ---\n";
    
    // Default constructor
    std::set<int> s1;
    
    // Initializer list
    std::set<int> s2 = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    // Range constructor
    std::vector<int> vec = {1, 2, 3, 4, 5};
    std::set<int> s3(vec.begin(), vec.end());
    
    // Copy constructor
    std::set<int> s4(s2);
    
    // Move constructor (C++11)
    std::set<int> s5(std::move(s4));
    
    // Custom comparator (descending order)
    std::set<int, std::greater<int>> s6 = {1, 2, 3, 4, 5};
    
    // ==================== INSERTION ====================
    std::cout << "\n--- Insertion ---\n";
    
    std::set<int> insert_set;
    
    // insert single element
    auto result = insert_set.insert(10);
    std::cout << "Inserted 10: " << (result.second ? "Success" : "Failed") << "\n";
    
    // insert duplicate (will fail)
    result = insert_set.insert(10);
    std::cout << "Insert duplicate 10: " << (result.second ? "Success" : "Failed") << "\n";
    
    // insert with hint (for optimization)
    auto hint = insert_set.begin();
    insert_set.insert(hint, 20);
    
    // insert multiple elements
    insert_set.insert({30, 40, 50});
    
    // insert range
    std::vector<int> more = {60, 70, 80};
    insert_set.insert(more.begin(), more.end());
    
    // emplace (C++11) - construct in place
    struct Person {
        std::string name;
        int age;
        Person(std::string n, int a) : name(std::move(n)), age(a) {}
        bool operator<(const Person& other) const {
            return age < other.age;
        }
    };
    
    std::set<Person> person_set;
    person_set.emplace("Alice", 25);
    person_set.emplace("Bob", 30);
    person_set.emplace("Charlie", 20);
    
    std::cout << "Set after insertions: ";
    for (int x : insert_set) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== DELETION ====================
    std::cout << "\n--- Deletion ---\n";
    
    std::set<int> delete_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    // erase by value
    size_t erased = delete_set.erase(5);
    std::cout << "Erased 5: " << erased << " element(s)\n";
    
    // erase by iterator
    auto it = delete_set.find(3);
    if (it != delete_set.end()) {
        delete_set.erase(it);
        std::cout << "Erased element at iterator (3)\n";
    }
    
    // erase range
    auto first = delete_set.find(7);
    auto last = delete_set.find(9);
    if (first != delete_set.end() && last != delete_set.end()) {
        delete_set.erase(first, std::next(last));
        std::cout << "Erased range [7, 9]\n";
    }
    
    // clear all
    delete_set.clear();
    std::cout << "After clear - Size: " << delete_set.size() << "\n";
    
    // ==================== SEARCHING & LOOKUP ====================
    std::cout << "\n--- Searching & Lookup ---\n";
    
    std::set<int> search_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    
    // find
    auto find_it = search_set.find(30);
    if (find_it != search_set.end()) {
        std::cout << "Found 30 at position: " << std::distance(search_set.begin(), find_it) << "\n";
    }
    
    // count (returns 0 or 1 for set)
    std::cout << "Count of 30: " << search_set.count(30) << "\n";
    std::cout << "Count of 35: " << search_set.count(35) << "\n";
    
    // contains (C++20)
    #if __cplusplus >= 202002L
    std::cout << "Contains 30? " << (search_set.contains(30) ? "Yes" : "No") << "\n";
    #endif
    
    // lower_bound (first element >= key)
    auto lb = search_set.lower_bound(55);
    if (lb != search_set.end()) {
        std::cout << "lower_bound(55): " << *lb << "\n";
    }
    
    // upper_bound (first element > key)
    auto ub = search_set.upper_bound(55);
    if (ub != search_set.end()) {
        std::cout << "upper_bound(55): " << *ub << "\n";
    }
    
    // equal_range (pair of lower_bound and upper_bound)
    auto range = search_set.equal_range(55);
    std::cout << "equal_range(55): [" 
              << (range.first != search_set.end() ? std::to_string(*range.first) : "end") 
              << ", " 
              << (range.second != search_set.end() ? std::to_string(*range.second) : "end") 
              << "]\n";
    
    // ==================== SIZE & CAPACITY ====================
    std::cout << "\n--- Size & Capacity ---\n";
    
    std::set<int> size_set = {1, 2, 3, 4, 5};
    
    std::cout << "Size: " << size_set.size() << "\n";
    std::cout << "Max size: " << size_set.max_size() << "\n";
    std::cout << "Empty? " << (size_set.empty() ? "Yes" : "No") << "\n";
    
    // ==================== ITERATORS ====================
    std::cout << "\n--- Iterators ---\n";
    
    std::set<int> iter_set = {10, 20, 30, 40, 50};
    
    // Forward iteration
    std::cout << "Forward: ";
    for (auto it = iter_set.begin(); it != iter_set.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    // Reverse iteration
    std::cout << "Reverse: ";
    for (auto it = iter_set.rbegin(); it != iter_set.rend(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    // Const iterators
    std::cout << "Const iteration: ";
    for (auto it = iter_set.cbegin(); it != iter_set.cend(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    // Range-based for loop
    std::cout << "Range-based for: ";
    for (const auto& elem : iter_set) {
        std::cout << elem << " ";
    }
    std::cout << "\n";
    
    // ==================== SET OPERATIONS ====================
    std::cout << "\n--- Set Operations ---\n";
    
    std::set<int> A = {1, 2, 3, 4, 5};
    std::set<int> B = {4, 5, 6, 7, 8};
    
    // Union
    std::set<int> union_set;
    std::set_union(A.begin(), A.end(),
                   B.begin(), B.end(),
                   std::inserter(union_set, union_set.begin()));
    std::cout << "Union: ";
    for (int x : union_set) std::cout << x << " ";
    std::cout << "\n";
    
    // Intersection
    std::set<int> intersect_set;
    std::set_intersection(A.begin(), A.end(),
                          B.begin(), B.end(),
                          std::inserter(intersect_set, intersect_set.begin()));
    std::cout << "Intersection: ";
    for (int x : intersect_set) std::cout << x << " ";
    std::cout << "\n";
    
    // Difference (A - B)
    std::set<int> diff_set;
    std::set_difference(A.begin(), A.end(),
                        B.begin(), B.end(),
                        std::inserter(diff_set, diff_set.begin()));
    std::cout << "Difference (A - B): ";
    for (int x : diff_set) std::cout << x << " ";
    std::cout << "\n";
    
    // Symmetric Difference
    std::set<int> sym_diff_set;
    std::set_symmetric_difference(A.begin(), A.end(),
                                   B.begin(), B.end(),
                                   std::inserter(sym_diff_set, sym_diff_set.begin()));
    std::cout << "Symmetric Difference: ";
    for (int x : sym_diff_set) std::cout << x << " ";
    std::cout << "\n";
    
    // Subset check
    std::set<int> C = {1, 2, 3};
    bool is_subset = std::includes(A.begin(), A.end(), C.begin(), C.end());
    std::cout << "C is subset of A: " << (is_subset ? "Yes" : "No") << "\n";
    
    // ==================== SWAPPING ====================
    std::cout << "\n--- Swapping ---\n";
    
    std::set<int> swap1 = {1, 2, 3};
    std::set<int> swap2 = {10, 20, 30, 40, 50};
    
    swap1.swap(swap2);
    std::cout << "After swap - swap1: ";
    for (int x : swap1) std::cout << x << " ";
    std::cout << "\nAfter swap - swap2: ";
    for (int x : swap2) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== COMPARISON ====================
    std::cout << "\n--- Comparison ---\n";
    
    std::set<int> comp1 = {1, 2, 3, 4, 5};
    std::set<int> comp2 = {1, 2, 3, 4, 5};
    std::set<int> comp3 = {1, 2, 3, 4, 6};
    
    std::cout << "comp1 == comp2: " << (comp1 == comp2 ? "Yes" : "No") << "\n";
    std::cout << "comp1 == comp3: " << (comp1 == comp3 ? "Yes" : "No") << "\n";
    std::cout << "comp1 < comp3: " << (comp1 < comp3 ? "Yes" : "No") << "\n";
    
    // ==================== PRACTICAL EXAMPLES ====================
    
    // Example 1: Remove Duplicates from Vector
    std::cout << "\n--- Example 1: Remove Duplicates ---\n";
    
    std::vector<int> duplicates = {5, 2, 8, 2, 5, 3, 8, 1, 9, 3, 5};
    std::set<int> unique(duplicates.begin(), duplicates.end());
    
    std::cout << "Original: ";
    for (int x : duplicates) std::cout << x << " ";
    std::cout << "\nUnique: ";
    for (int x : unique) std::cout << x << " ";
    std::cout << "\n";
    
    // Example 2: Custom Comparator (Descending Order)
    std::cout << "\n--- Example 2: Custom Comparator ---\n";
    
    std::set<int, std::greater<int>> desc_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    std::cout << "Descending order set: ";
    for (int x : desc_set) std::cout << x << " ";
    std::cout << "\n";
    
    // Example 3: Set of Strings
    std::cout << "\n--- Example 3: Set of Strings ---\n";
    
    std::set<std::string> words = {"apple", "banana", "cherry", "date", "elderberry"};
    
    // Case-insensitive search example
    std::cout << "Words in alphabetical order: ";
    for (const auto& word : words) std::cout << word << " ";
    std::cout << "\n";
    
    // Example 4: Custom Object Set
    std::cout << "\n--- Example 4: Custom Object Set ---\n";
    
    struct Student {
        int id;
        std::string name;
        double gpa;
        
        bool operator<(const Student& other) const {
            return id < other.id;  // Sort by ID
        }
    };
    
    std::set<Student> students;
    students.insert({101, "Alice", 3.8});
    students.insert({102, "Bob", 3.5});
    students.insert({103, "Charlie", 3.9});
    students.insert({104, "Diana", 4.0});
    
    std::cout << "Students sorted by ID:\n";
    for (const auto& s : students) {
        std::cout << "  ID: " << s.id << ", Name: " << s.name << ", GPA: " << s.gpa << "\n";
    }
    
    // Example 5: Finding Next Greater Element
    std::cout << "\n--- Example 5: Next Greater Element ---\n";
    
    std::set<int> numbers_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    int query = 45;
    
    auto next_greater = numbers_set.upper_bound(query);
    if (next_greater != numbers_set.end()) {
        std::cout << "Next greater than " << query << ": " << *next_greater << "\n";
    } else {
        std::cout << "No greater element found\n";
    }
    
    // Example 6: Range Queries
    std::cout << "\n--- Example 6: Range Queries ---\n";
    
    std::set<int> range_set = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
    int low = 5, high = 15;
    
    auto start = range_set.lower_bound(low);
    auto end = range_set.upper_bound(high);
    
    std::cout << "Elements in [" << low << ", " << high << "]: ";
    for (auto it = start; it != end; ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
}
```

---

## 2. std::multiset (Ordered Non-Unique Elements)

### Theory
`std::multiset` is similar to `std::set` but allows duplicate elements. Multiple elements with the same value can be stored. Like `set`, it maintains elements in sorted order and is implemented as a Red-Black Tree.

**Use Cases:**
- Maintaining sorted collections with duplicates
- Counting frequencies while maintaining order
- Implementing multisets (bags)
- Histogram-like data structures
- Maintaining multiple identical keys

### All Functions and Operations

```cpp
#include <iostream>
#include <set>
#include <string>

void demonstrateMultiset() {
    std::cout << "\n========== STD::MULTISET ==========\n";
    
    // ==================== CONSTRUCTORS & INITIALIZATION ====================
    std::cout << "\n--- Constructors & Initialization ---\n";
    
    // Default constructor
    std::multiset<int> ms1;
    
    // Initializer list (allows duplicates)
    std::multiset<int> ms2 = {5, 2, 8, 2, 5, 3, 8, 1, 9, 3, 5};
    
    // Range constructor
    std::vector<int> vec = {1, 2, 2, 3, 3, 3};
    std::multiset<int> ms3(vec.begin(), vec.end());
    
    // Copy constructor
    std::multiset<int> ms4(ms2);
    
    // ==================== INSERTION ====================
    std::cout << "\n--- Insertion (Allows Duplicates) ---\n";
    
    std::multiset<int> insert_ms;
    
    // insert single element
    insert_ms.insert(10);
    insert_ms.insert(10);  // Duplicate allowed
    insert_ms.insert(20);
    insert_ms.insert(20);
    insert_ms.insert(20);
    
    std::cout << "After inserting duplicates: ";
    for (int x : insert_ms) std::cout << x << " ";
    std::cout << "\n";
    
    // insert with hint
    auto hint = insert_ms.begin();
    insert_ms.insert(hint, 15);
    
    // insert range
    std::vector<int> more = {5, 5, 5, 6, 6};
    insert_ms.insert(more.begin(), more.end());
    
    // emplace (C++11)
    insert_ms.emplace(25);
    
    std::cout << "After more insertions: ";
    for (int x : insert_ms) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== DELETION ====================
    std::cout << "\n--- Deletion ---\n";
    
    std::multiset<int> delete_ms = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5};
    
    std::cout << "Original multiset: ";
    for (int x : delete_ms) std::cout << x << " ";
    std::cout << "\n";
    
    // erase all occurrences of a value
    size_t erased = delete_ms.erase(3);
    std::cout << "Erased " << erased << " occurrences of 3\n";
    
    // erase single occurrence using iterator
    auto it = delete_ms.find(4);
    if (it != delete_ms.end()) {
        delete_ms.erase(it);
        std::cout << "Erased one occurrence of 4\n";
    }
    
    // erase range
    auto first = delete_ms.find(5);
    auto last = delete_ms.upper_bound(5);
    if (first != delete_ms.end()) {
        delete_ms.erase(first, last);
        std::cout << "Erased all remaining 5s\n";
    }
    
    std::cout << "After deletions: ";
    for (int x : delete_ms) std::cout << x << " ";
    std::cout << "\n";
    
    // clear all
    delete_ms.clear();
    std::cout << "After clear - Size: " << delete_ms.size() << "\n";
    
    // ==================== SEARCHING & LOOKUP ====================
    std::cout << "\n--- Searching & Lookup ---\n";
    
    std::multiset<int> search_ms = {10, 20, 20, 30, 30, 30, 40, 40, 40, 40, 50};
    
    // find (returns first occurrence)
    auto find_it = search_ms.find(30);
    if (find_it != search_ms.end()) {
        std::cout << "Found first 30 at position: " 
                  << std::distance(search_ms.begin(), find_it) << "\n";
    }
    
    // count (returns number of occurrences)
    std::cout << "Count of 30: " << search_ms.count(30) << "\n";
    std::cout << "Count of 40: " << search_ms.count(40) << "\n";
    std::cout << "Count of 35: " << search_ms.count(35) << "\n";
    
    // lower_bound (first element >= key)
    auto lb = search_ms.lower_bound(25);
    if (lb != search_ms.end()) {
        std::cout << "lower_bound(25): " << *lb << "\n";
    }
    
    // upper_bound (first element > key)
    auto ub = search_ms.upper_bound(30);
    if (ub != search_ms.end()) {
        std::cout << "upper_bound(30): " << *ub << "\n";
    }
    
    // equal_range (range of all elements equal to key)
    auto range = search_ms.equal_range(30);
    std::cout << "equal_range(30): ";
    for (auto it = range.first; it != range.second; ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
    
    // ==================== SIZE & CAPACITY ====================
    std::cout << "\n--- Size & Capacity ---\n";
    
    std::multiset<int> size_ms = {1, 1, 2, 2, 2, 3, 3, 3, 3};
    
    std::cout << "Size: " << size_ms.size() << "\n";
    std::cout << "Empty? " << (size_ms.empty() ? "Yes" : "No") << "\n";
    
    // ==================== PRACTICAL EXAMPLES ====================
    
    // Example 1: Frequency Counter
    std::cout << "\n--- Example 1: Frequency Counter ---\n";
    
    std::vector<int> data = {1, 2, 3, 2, 1, 3, 3, 4, 5, 4, 3, 2, 1, 1, 1};
    std::multiset<int> freq_set(data.begin(), data.end());
    
    std::set<int> unique_vals(data.begin(), data.end());
    std::cout << "Element frequencies:\n";
    for (int val : unique_vals) {
        std::cout << "  " << val << ": " << freq_set.count(val) << " times\n";
    }
    
    // Example 2: Histogram
    std::cout << "\n--- Example 2: Histogram ---\n";
    
    std::vector<int> grades = {85, 92, 78, 85, 91, 92, 85, 78, 90, 85, 92, 91};
    std::multiset<int> grade_set(grades.begin(), grades.end());
    
    std::cout << "Grade distribution:\n";
    for (int grade : {78, 85, 90, 91, 92}) {
        int count = grade_set.count(grade);
        std::cout << "  " << grade << ": " << std::string(count, '*') << " (" << count << ")\n";
    }
    
    // Example 3: Maintaining a Multi-set of Scores
    std::cout << "\n--- Example 3: Score Tracker ---\n";
    
    class ScoreTracker {
    private:
        std::multiset<int> scores;
        
    public:
        void addScore(int score) {
            scores.insert(score);
            std::cout << "Added score: " << score << "\n";
        }
        
        void removeScore(int score) {
            auto it = scores.find(score);
            if (it != scores.end()) {
                scores.erase(it);
                std::cout << "Removed score: " << score << "\n";
            } else {
                std::cout << "Score " << score << " not found\n";
            }
        }
        
        double getAverage() const {
            if (scores.empty()) return 0;
            int sum = 0;
            for (int s : scores) sum += s;
            return static_cast<double>(sum) / scores.size();
        }
        
        void printScores() const {
            std::cout << "Scores: ";
            for (int s : scores) std::cout << s << " ";
            std::cout << "\n";
        }
        
        int getMin() const {
            return scores.empty() ? 0 : *scores.begin();
        }
        
        int getMax() const {
            return scores.empty() ? 0 : *scores.rbegin();
        }
    };
    
    ScoreTracker tracker;
    tracker.addScore(85);
    tracker.addScore(92);
    tracker.addScore(78);
    tracker.addScore(85);
    tracker.addScore(91);
    tracker.printScores();
    std::cout << "Average: " << tracker.getAverage() << "\n";
    std::cout << "Min: " << tracker.getMin() << ", Max: " << tracker.getMax() << "\n";
    
    tracker.removeScore(85);
    tracker.printScores();
    
    // Example 4: Sliding Window Median
    std::cout << "\n--- Example 4: Sliding Window Median ---\n";
    
    auto slidingWindowMedian = [](const std::vector<int>& nums, int k) {
        std::multiset<int> window;
        std::vector<double> medians;
        
        for (size_t i = 0; i < nums.size(); i++) {
            window.insert(nums[i]);
            
            if (window.size() > k) {
                window.erase(window.find(nums[i - k]));
            }
            
            if (window.size() == k) {
                auto it = window.begin();
                std::advance(it, k / 2);
                if (k % 2 == 1) {
                    medians.push_back(*it);
                } else {
                    auto it2 = it;
                    --it2;
                    medians.push_back((*it2 + *it) / 2.0);
                }
            }
        }
        
        return medians;
    };
    
    std::vector<int> window_nums = {1, 3, -1, -3, 5, 3, 6, 7};
    int k = 3;
    auto medians = slidingWindowMedian(window_nums, k);
    
    std::cout << "Sliding window medians (k=" << k << "): ";
    for (double m : medians) std::cout << m << " ";
    std::cout << "\n";
    
    // Example 5: Custom Comparator for Multiset
    std::cout << "\n--- Example 5: Custom Comparator ---\n";
    
    struct Person {
        std::string name;
        int age;
        
        bool operator<(const Person& other) const {
            return age < other.age;  // Sort by age
        }
    };
    
    std::multiset<Person> people;
    people.insert({"Alice", 25});
    people.insert({"Bob", 30});
    people.insert({"Charlie", 25});  // Same age as Alice - allowed in multiset
    people.insert({"Diana", 25});    // Another with age 25
    
    std::cout << "People sorted by age:\n";
    for (const auto& p : people) {
        std::cout << "  " << p.name << " (" << p.age << ")\n";
    }
}
```

---

## 3. std::map (Ordered Key-Value Pairs)

### Theory
`std::map` is an associative container that stores key-value pairs in sorted order by key. Each key must be unique, and keys are immutable once inserted. Values can be modified. Like `set`, it's implemented as a Red-Black Tree.

**Use Cases:**
- Dictionaries and lookup tables
- Associative arrays
- Database indexing
- Frequency counters
- Caching mechanisms
- Symbol tables in compilers

### All Functions and Operations

```cpp
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>

void demonstrateMap() {
    std::cout << "\n========== STD::MAP ==========\n";
    
    // ==================== CONSTRUCTORS & INITIALIZATION ====================
    std::cout << "\n--- Constructors & Initialization ---\n";
    
    // Default constructor
    std::map<std::string, int> m1;
    
    // Initializer list
    std::map<std::string, int> m2 = {
        {"Alice", 95},
        {"Bob", 87},
        {"Charlie", 92}
    };
    
    // Range constructor
    std::vector<std::pair<std::string, int>> vec = {{"David", 88}, {"Eve", 91}};
    std::map<std::string, int> m3(vec.begin(), vec.end());
    
    // Copy constructor
    std::map<std::string, int> m4(m2);
    
    // Custom comparator (descending order)
    std::map<int, std::string, std::greater<int>> m5 = {
        {1, "One"}, {2, "Two"}, {3, "Three"}
    };
    
    // ==================== INSERTION ====================
    std::cout << "\n--- Insertion ---\n";
    
    std::map<std::string, int> insert_map;
    
    // Using operator[]
    insert_map["Alice"] = 95;
    insert_map["Bob"] = 87;
    
    // Using insert with pair
    insert_map.insert(std::pair<std::string, int>("Charlie", 92));
    insert_map.insert({"David", 88});  // C++11
    
    // Using insert with make_pair
    insert_map.insert(std::make_pair("Eve", 91));
    
    // Insert with hint (optimization)
    auto hint = insert_map.begin();
    insert_map.insert(hint, std::make_pair("Frank", 85));
    
    // Insert returns pair<iterator, bool> indicating success
    auto result = insert_map.insert({"Alice", 100});  // Duplicate key
    if (!result.second) {
        std::cout << "Key 'Alice' already exists with value: " << result.first->second << "\n";
    }
    
    // Insert range
    std::map<std::string, int> more = {{"Grace", 89}, {"Henry", 93}};
    insert_map.insert(more.begin(), more.end());
    
    // emplace (C++11) - construct in place
    insert_map.emplace("Ivy", 86);
    
    // emplace_hint
    insert_map.emplace_hint(insert_map.begin(), "Jack", 90);
    
    std::cout << "Map after insertions:\n";
    for (const auto& [key, value] : insert_map) {
        std::cout << "  " << key << ": " << value << "\n";
    }
    
    // ==================== ACCESSING ELEMENTS ====================
    std::cout << "\n--- Accessing Elements ---\n";
    
    std::map<std::string, int> access_map = {
        {"Alice", 95}, {"Bob", 87}, {"Charlie", 92}
    };
    
    // Using operator[] (creates element if not exists)
    std::cout << "Alice's score: " << access_map["Alice"] << "\n";
    
    // Using .at() (throws exception if key not found)
    try {
        std::cout << "Bob's score: " << access_map.at("Bob") << "\n";
        // std::cout << access_map.at("Unknown") << "\n";  // Throws exception
    } catch (const std::out_of_range& e) {
        std::cout << "Key not found: " << e.what() << "\n";
    }
    
    // ==================== MODIFYING VALUES ====================
    std::cout << "\n--- Modifying Values ---\n";
    
    std::map<std::string, int> modify_map = {
        {"Alice", 95}, {"Bob", 87}, {"Charlie", 92}
    };
    
    // Modify using operator[]
    modify_map["Alice"] = 98;
    
    // Modify using iterator
    auto it = modify_map.find("Bob");
    if (it != modify_map.end()) {
        it->second = 90;
    }
    
    std::cout << "After modifications:\n";
    for (const auto& [key, value] : modify_map) {
        std::cout << "  " << key << ": " << value << "\n";
    }
    
    // ==================== DELETION ====================
    std::cout << "\n--- Deletion ---\n";
    
    std::map<std::string, int> delete_map = {
        {"Alice", 95}, {"Bob", 87}, {"Charlie", 92},
        {"David", 88}, {"Eve", 91}, {"Frank", 85}
    };
    
    // erase by key
    size_t erased = delete_map.erase("Charlie");
    std::cout << "Erased Charlie: " << erased << " element\n";
    
    // erase by iterator
    auto erase_it = delete_map.find("David");
    if (erase_it != delete_map.end()) {
        delete_map.erase(erase_it);
        std::cout << "Erased David\n";
    }
    
    // erase range
    auto first = delete_map.find("Bob");
    auto last = delete_map.find("Eve");
    if (first != delete_map.end() && last != delete_map.end()) {
        delete_map.erase(first, std::next(last));
        std::cout << "Erased range [Bob, Eve]\n";
    }
    
    // clear all
    delete_map.clear();
    std::cout << "After clear - Size: " << delete_map.size() << "\n";
    
    // ==================== SEARCHING & LOOKUP ====================
    std::cout << "\n--- Searching & Lookup ---\n";
    
    std::map<std::string, int> search_map = {
        {"Alice", 95}, {"Bob", 87}, {"Charlie", 92},
        {"David", 88}, {"Eve", 91}, {"Frank", 85}
    };
    
    // find
    auto find_it = search_map.find("Charlie");
    if (find_it != search_map.end()) {
        std::cout << "Found Charlie with score: " << find_it->second << "\n";
    }
    
    // count (returns 0 or 1 for map)
    std::cout << "Count of Bob: " << search_map.count("Bob") << "\n";
    std::cout << "Count of Unknown: " << search_map.count("Unknown") << "\n";
    
    // lower_bound (first key >= given key)
    auto lb = search_map.lower_bound("Dave");
    if (lb != search_map.end()) {
        std::cout << "lower_bound('Dave'): " << lb->first << ": " << lb->second << "\n";
    }
    
    // upper_bound (first key > given key)
    auto ub = search_map.upper_bound("Dave");
    if (ub != search_map.end()) {
        std::cout << "upper_bound('Dave'): " << ub->first << ": " << ub->second << "\n";
    }
    
    // equal_range (range of keys equal to given key)
    auto range = search_map.equal_range("David");
    if (range.first != search_map.end()) {
        std::cout << "equal_range('David'): " << range.first->first << ": " << range.first->second << "\n";
    }
    
    // ==================== SIZE & CAPACITY ====================
    std::cout << "\n--- Size & Capacity ---\n";
    
    std::map<std::string, int> size_map = {
        {"A", 1}, {"B", 2}, {"C", 3}, {"D", 4}, {"E", 5}
    };
    
    std::cout << "Size: " << size_map.size() << "\n";
    std::cout << "Max size: " << size_map.max_size() << "\n";
    std::cout << "Empty? " << (size_map.empty() ? "Yes" : "No") << "\n";
    
    // ==================== ITERATORS ====================
    std::cout << "\n--- Iterators ---\n";
    
    std::map<std::string, int> iter_map = {
        {"Alice", 95}, {"Bob", 87}, {"Charlie", 92}
    };
    
    // Forward iteration
    std::cout << "Forward iteration:\n";
    for (auto it = iter_map.begin(); it != iter_map.end(); ++it) {
        std::cout << "  " << it->first << ": " << it->second << "\n";
    }
    
    // Reverse iteration
    std::cout << "Reverse iteration:\n";
    for (auto it = iter_map.rbegin(); it != iter_map.rend(); ++it) {
        std::cout << "  " << it->first << ": " << it->second << "\n";
    }
    
    // Range-based for loop (C++17 structured binding)
    std::cout << "Range-based for:\n";
    for (const auto& [key, value] : iter_map) {
        std::cout << "  " << key << ": " << value << "\n";
    }
    
    // ==================== SWAPPING ====================
    std::cout << "\n--- Swapping ---\n";
    
    std::map<std::string, int> swap1 = {{"A", 1}, {"B", 2}};
    std::map<std::string, int> swap2 = {{"X", 10}, {"Y", 20}, {"Z", 30}};
    
    swap1.swap(swap2);
    std::cout << "After swap - swap1: ";
    for (const auto& [key, val] : swap1) std::cout << key << ":" << val << " ";
    std::cout << "\nAfter swap - swap2: ";
    for (const auto& [key, val] : swap2) std::cout << key << ":" << val << " ";
    std::cout << "\n";
    
    // ==================== PRACTICAL EXAMPLES ====================
    
    // Example 1: Word Frequency Counter
    std::cout << "\n--- Example 1: Word Frequency Counter ---\n";
    
    std::string text = "the quick brown fox jumps over the lazy dog the fox jumps";
    std::map<std::string, int> word_count;
    
    std::string word;
    std::stringstream ss(text);
    while (ss >> word) {
        word_count[word]++;
    }
    
    std::cout << "Word frequencies:\n";
    for (const auto& [w, count] : word_count) {
        std::cout << "  " << w << ": " << count << "\n";
    }
    
    // Example 2: Student Database
    std::cout << "\n--- Example 2: Student Database ---\n";
    
    struct StudentInfo {
        std::string name;
        int age;
        double gpa;
    };
    
    std::map<int, StudentInfo> students_db;
    students_db[101] = {"Alice", 20, 3.8};
    students_db[102] = {"Bob", 21, 3.5};
    students_db[103] = {"Charlie", 19, 3.9};
    
    // Insert using insert
    students_db.insert({104, {"Diana", 22, 4.0}});
    
    // Find and modify
    auto stu_it = students_db.find(102);
    if (stu_it != students_db.end()) {
        stu_it->second.gpa = 3.7;
    }
    
    std::cout << "Student records:\n";
    for (const auto& [id, info] : students_db) {
        std::cout << "  ID: " << id << ", Name: " << info.name 
                  << ", Age: " << info.age << ", GPA: " << info.gpa << "\n";
    }
    
    // Example 3: Cache with LRU Simulation
    std::cout << "\n--- Example 3: Cache Simulation ---\n";
    
    class SimpleCache {
    private:
        std::map<std::string, std::string> cache;
        size_t max_size;
        
    public:
        SimpleCache(size_t size) : max_size(size) {}
        
        void put(const std::string& key, const std::string& value) {
            if (cache.size() >= max_size) {
                // Simple eviction: remove first element
                cache.erase(cache.begin());
            }
            cache[key] = value;
        }
        
        std::string get(const std::string& key) {
            auto it = cache.find(key);
            if (it != cache.end()) {
                return it->second;
            }
            return "NOT_FOUND";
        }
        
        void display() {
            std::cout << "Cache contents:\n";
            for (const auto& [k, v] : cache) {
                std::cout << "  " << k << " -> " << v << "\n";
            }
        }
    };
    
    SimpleCache cache(3);
    cache.put("user1", "Alice");
    cache.put("user2", "Bob");
    cache.put("user3", "Charlie");
    cache.display();
    cache.put("user4", "Diana");
    cache.display();
    std::cout << "Get user2: " << cache.get("user2") << "\n";
    
    // Example 4: Custom Comparator for Map
    std::cout << "\n--- Example 4: Custom Comparator ---\n";
    
    // Map with case-insensitive keys
    struct CaseInsensitiveCompare {
        bool operator()(const std::string& a, const std::string& b) const {
            return std::lexicographical_compare(
                a.begin(), a.end(),
                b.begin(), b.end(),
                [](char c1, char c2) {
                    return std::tolower(c1) < std::tolower(c2);
                }
            );
        }
    };
    
    std::map<std::string, int, CaseInsensitiveCompare> case_insensitive_map;
    case_insensitive_map["Apple"] = 10;
    case_insensitive_map["apple"] = 20;  // This will update the existing key
    
    std::cout << "Case-insensitive map:\n";
    for (const auto& [key, value] : case_insensitive_map) {
        std::cout << "  " << key << ": " << value << "\n";
    }
    
    // Example 5: Range Queries on Map
    std::cout << "\n--- Example 5: Range Queries ---\n";
    
    std::map<int, std::string> number_names = {
        {1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"},
        {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"},
        {9, "Nine"}, {10, "Ten"}
    };
    
    int low = 3, high = 7;
    auto start_range = number_names.lower_bound(low);
    auto end_range = number_names.upper_bound(high);
    
    std::cout << "Numbers between " << low << " and " << high << ":\n";
    for (auto it = start_range; it != end_range; ++it) {
        std::cout << "  " << it->first << ": " << it->second << "\n";
    }
    
    // Example 6: Map of Vectors (Grouping Data)
    std::cout << "\n--- Example 6: Grouping Data ---\n";
    
    std::vector<std::pair<std::string, int>> scores = {
        {"Alice", 95}, {"Bob", 87}, {"Alice", 92}, {"Bob", 88},
        {"Charlie", 91}, {"Alice", 98}, {"Bob", 85}, {"Charlie", 89}
    };
    
    std::map<std::string, std::vector<int>> grouped_scores;
    for (const auto& [name, score] : scores) {
        grouped_scores[name].push_back(score);
    }
    
    std::cout << "Grouped scores:\n";
    for (const auto& [name, score_list] : grouped_scores) {
        std::cout << "  " << name << ": ";
        for (int s : score_list) std::cout << s << " ";
        double avg = std::accumulate(score_list.begin(), score_list.end(), 0.0) / score_list.size();
        std::cout << "(Average: " << avg << ")\n";
    }
}
```

---

## 4. std::multimap (Ordered Key-Value Pairs with Duplicates)

### Theory
`std::multimap` is similar to `std::map` but allows multiple elements with the same key. Keys are still sorted, and you can store multiple values for the same key. It's useful for one-to-many relationships.

**Use Cases:**
- One-to-many relationships (like students in courses)
- Indexing with duplicate keys
- Implementing dictionaries with multiple definitions
- Phone book with multiple numbers per person
- Event scheduling with multiple events at same time

### All Functions and Operations

```cpp
#include <iostream>
#include <map>
#include <string>
#include <vector>

void demonstrateMultimap() {
    std::cout << "\n========== STD::MULTIMAP ==========\n";
    
    // ==================== CONSTRUCTORS & INITIALIZATION ====================
    std::cout << "\n--- Constructors & Initialization ---\n";
    
    // Default constructor
    std::multimap<std::string, int> mm1;
    
    // Initializer list (allows duplicate keys)
    std::multimap<std::string, int> mm2 = {
        {"Alice", 95}, {"Bob", 87}, {"Alice", 92}, {"Bob", 88},
        {"Charlie", 91}, {"Alice", 98}
    };
    
    // Range constructor
    std::vector<std::pair<std::string, int>> vec = {{"David", 88}, {"David", 89}, {"Eve", 91}};
    std::multimap<std::string, int> mm3(vec.begin(), vec.end());
    
    // ==================== INSERTION ====================
    std::cout << "\n--- Insertion (Allows Duplicate Keys) ---\n";
    
    std::multimap<std::string, int> insert_mm;
    
    // Insert with pair
    insert_mm.insert(std::pair<std::string, int>("Alice", 95));
    insert_mm.insert({"Alice", 92});   // Duplicate key allowed
    insert_mm.insert({"Bob", 87});
    insert_mm.insert({"Bob", 88});
    
    // Insert with make_pair
    insert_mm.insert(std::make_pair("Charlie", 91));
    
    // Insert with hint
    auto hint = insert_mm.begin();
    insert_mm.insert(hint, std::make_pair("Alice", 98));
    
    // Insert range
    std::multimap<std::string, int> more = {{"David", 88}, {"David", 89}};
    insert_mm.insert(more.begin(), more.end());
    
    // emplace (C++11)
    insert_mm.emplace("Eve", 90);
    
    std::cout << "Multimap after insertions:\n";
    for (const auto& [key, value] : insert_mm) {
        std::cout << "  " << key << ": " << value << "\n";
    }
    
    // ==================== DELETION ====================
    std::cout << "\n--- Deletion ---\n";
    
    std::multimap<std::string, int> delete_mm = {
        {"Alice", 95}, {"Alice", 92}, {"Alice", 98},
        {"Bob", 87}, {"Bob", 88},
        {"Charlie", 91}
    };
    
    std::cout << "Original multimap:\n";
    for (const auto& [k, v] : delete_mm) std::cout << "  " << k << ": " << v << "\n";
    
    // erase all occurrences of a key
    size_t erased = delete_mm.erase("Alice");
    std::cout << "Erased " << erased << " entries for key 'Alice'\n";
    
    // erase single occurrence using iterator
    auto it = delete_mm.find("Bob");
    if (it != delete_mm.end()) {
        delete_mm.erase(it);
        std::cout << "Erased one occurrence of 'Bob'\n";
    }
    
    // erase range
    auto first = delete_mm.find("Bob");
    auto last = delete_mm.upper_bound("Bob");
    if (first != delete_mm.end()) {
        delete_mm.erase(first, last);
        std::cout << "Erased all remaining 'Bob' entries\n";
    }
    
    std::cout << "After deletions:\n";
    for (const auto& [k, v] : delete_mm) std::cout << "  " << k << ": " << v << "\n";
    
    // ==================== SEARCHING & LOOKUP ====================
    std::cout << "\n--- Searching & Lookup ---\n";
    
    std::multimap<std::string, int> search_mm = {
        {"Alice", 95}, {"Alice", 92}, {"Alice", 98},
        {"Bob", 87}, {"Bob", 88},
        {"Charlie", 91}, {"Charlie", 93}
    };
    
    // find (returns first occurrence)
    auto find_it = search_mm.find("Alice");
    if (find_it != search_mm.end()) {
        std::cout << "First Alice entry: " << find_it->second << "\n";
    }
    
    // count (returns number of occurrences)
    std::cout << "Count of Alice: " << search_mm.count("Alice") << "\n";
    std::cout << "Count of Bob: " << search_mm.count("Bob") << "\n";
    std::cout << "Count of Unknown: " << search_mm.count("Unknown") << "\n";
    
    // equal_range (range of all elements with given key)
    auto range = search_mm.equal_range("Alice");
    std::cout << "All Alice scores: ";
    for (auto it = range.first; it != range.second; ++it) {
        std::cout << it->second << " ";
    }
    std::cout << "\n";
    
    // lower_bound and upper_bound for multimap
    auto lb = search_mm.lower_bound("Bob");
    auto ub = search_mm.upper_bound("Bob");
    std::cout << "Bob scores: ";
    for (auto it = lb; it != ub; ++it) {
        std::cout << it->second << " ";
    }
    std::cout << "\n";
    
    // ==================== SIZE & CAPACITY ====================
    std::cout << "\n--- Size & Capacity ---\n";
    
    std::multimap<std::string, int> size_mm = {
        {"A", 1}, {"A", 2}, {"B", 3}, {"B", 4}, {"C", 5}
    };
    
    std::cout << "Size: " << size_mm.size() << "\n";
    std::cout << "Empty? " << (size_mm.empty() ? "Yes" : "No") << "\n";
    
    // ==================== PRACTICAL EXAMPLES ====================
    
    // Example 1: Course Enrollment System
    std::cout << "\n--- Example 1: Course Enrollment System ---\n";
    
    std::multimap<std::string, std::string> course_enrollment;
    
    course_enrollment.insert({"CS101", "Alice"});
    course_enrollment.insert({"CS101", "Bob"});
    course_enrollment.insert({"CS101", "Charlie"});
    course_enrollment.insert({"MATH201", "Alice"});
    course_enrollment.insert({"MATH201", "Diana"});
    course_enrollment.insert({"PHYS101", "Bob"});
    course_enrollment.insert({"PHYS101", "Eve"});
    
    std::cout << "Course enrollment:\n";
    for (const auto& [course, student] : course_enrollment) {
        std::cout << "  " << course << ": " << student << "\n";
    }
    
    // List students in a specific course
    std::string course = "CS101";
    auto cs_range = course_enrollment.equal_range(course);
    std::cout << "\nStudents in " << course << ": ";
    for (auto it = cs_range.first; it != cs_range.second; ++it) {
        std::cout << it->second << " ";
    }
    std::cout << "\n";
    
    // List all courses for a student
    std::string student = "Alice";
    std::cout << student << "'s courses: ";
    for (const auto& [c, s] : course_enrollment) {
        if (s == student) std::cout << c << " ";
    }
    std::cout << "\n";
    
    // Example 2: Phone Directory with Multiple Numbers
    std::cout << "\n--- Example 2: Phone Directory ---\n";
    
    std::multimap<std::string, std::string> phone_dir;
    
    phone_dir.insert({"Alice", "555-0101"});
    phone_dir.insert({"Alice", "555-0102"});
    phone_dir.insert({"Bob", "555-0201"});
    phone_dir.insert({"Bob", "555-0202"});
    phone_dir.insert({"Bob", "555-0203"});
    phone_dir.insert({"Charlie", "555-0301"});
    
    auto printNumbers = [&](const std::string& name) {
        auto range = phone_dir.equal_range(name);
        std::cout << name << "'s numbers: ";
        for (auto it = range.first; it != range.second; ++it) {
            std::cout << it->second << " ";
        }
        std::cout << "\n";
    };
    
    printNumbers("Alice");
    printNumbers("Bob");
    printNumbers("Charlie");
    
    // Example 3: Dictionary with Multiple Definitions
    std::cout << "\n--- Example 3: Dictionary with Multiple Definitions ---\n";
    
    std::multimap<std::string, std::string> dictionary;
    
    dictionary.insert({"run", "to move quickly on foot"});
    dictionary.insert({"run", "to operate or function"});
    dictionary.insert({"run", "to manage or be in charge"});
    dictionary.insert({"run", "a sequence or series"});
    dictionary.insert({"set", "to put in place"});
    dictionary.insert({"set", "a collection of items"});
    dictionary.insert({"set", "to establish or fix"});
    
    std::string word = "run";
    auto def_range = dictionary.equal_range(word);
    std::cout << "Definitions of '" << word << "':\n";
    int i = 1;
    for (auto it = def_range.first; it != def_range.second; ++it) {
        std::cout << "  " << i++ << ". " << it->second << "\n";
    }
    
    // Example 4: Event Calendar
    std::cout << "\n--- Example 4: Event Calendar ---\n";
    
    std::multimap<std::string, std::string> calendar;
    
    calendar.insert({"2024-01-15", "Meeting with team"});
    calendar.insert({"2024-01-15", "Project deadline"});
    calendar.insert({"2024-01-20", "Client presentation"});
    calendar.insert({"2024-01-20", "Lunch with client"});
    calendar.insert({"2024-02-01", "Conference call"});
    
    std::string date = "2024-01-20";
    auto events = calendar.equal_range(date);
    std::cout << "Events on " << date << ":\n";
    for (auto it = events.first; it != events.second; ++it) {
        std::cout << "  - " << it->second << "\n";
    }
    
    // Example 5: Finding Best Score for Each Student
    std::cout << "\n--- Example 5: Best Score for Each Student ---\n";
    
    std::multimap<std::string, int> all_scores = {
        {"Alice", 95}, {"Alice", 92}, {"Alice", 98},
        {"Bob", 87}, {"Bob", 88}, {"Bob", 85},
        {"Charlie", 91}, {"Charlie", 93}, {"Charlie", 89}
    };
    
    std::map<std::string, int> best_scores;
    for (const auto& [name, score] : all_scores) {
        if (best_scores.find(name) == best_scores.end() || score > best_scores[name]) {
            best_scores[name] = score;
        }
    }
    
    std::cout << "Best scores:\n";
    for (const auto& [name, score] : best_scores) {
        std::cout << "  " << name << ": " << score << "\n";
    }
    
    // Example 6: Multimap with Custom Comparator
    std::cout << "\n--- Example 6: Multimap with Custom Comparator ---\n";
    
    // Sort by key length (case-insensitive)
    struct CompareByLength {
        bool operator()(const std::string& a, const std::string& b) const {
            if (a.length() != b.length()) {
                return a.length() < b.length();
            }
            return a < b;  // If lengths equal, compare lexicographically
        }
    };
    
    std::multimap<std::string, int, CompareByLength> length_map;
    length_map.insert({"apple", 1});
    length_map.insert({"banana", 2});
    length_map.insert({"car", 3});
    length_map.insert({"dog", 4});
    length_map.insert({"elephant", 5});
    length_map.insert({"ant", 6});
    
    std::cout << "Words sorted by length:\n";
    for (const auto& [word, value] : length_map) {
        std::cout << "  " << word << " (length: " << word.length() << "): " << value << "\n";
    }
}
```

---

## Performance Summary

| Operation | set | multiset | map | multimap |
|-----------|-----|----------|-----|----------|
| Insert | O(log n) | O(log n) | O(log n) | O(log n) |
| Delete | O(log n) | O(log n) | O(log n) | O(log n) |
| Find | O(log n) | O(log n) | O(log n) | O(log n) |
| Access | O(log n) | O(log n) | O(log n) | O(log n) |
| Lower/Upper Bound | O(log n) | O(log n) | O(log n) | O(log n) |
| Iteration | O(n) | O(n) | O(n) | O(n) |
| Memory Overhead | Medium | Medium | Medium | Medium |

---

## Best Practices

1. **Use `set` for unique sorted elements** - When you need uniqueness and order
2. **Use `multiset` when duplicates are allowed** - For frequency counting with order
3. **Use `map` for key-value associations** - When keys are unique
4. **Use `multimap` for one-to-many relationships** - When keys can repeat
5. **Prefer `operator[]` for map insertion** - When you're sure key doesn't exist or want to update
6. **Use `at()` for safe access** - When key might not exist (throws exception)
7. **Use `equal_range()` for multimap** - To iterate over all values for a key
8. **Use `lower_bound/upper_bound` for range queries** - Efficient range searches
9. **Use `emplace()` over `insert()`** - For complex objects to avoid copies
10. **Use `contains()` in C++20** - For cleaner existence checking

---

## Common Pitfalls

1. **Using `operator[]` on const map** - Not allowed; use `at()` or `find()`
2. **Modifying keys directly** - Keys are immutable; must remove and reinsert
3. **Assuming `find()` returns value** - Returns iterator, check against `end()`
4. **Forgetting to include `<map>` or `<set>`** - Common compilation error
5. **Using `count()` for existence in map** - Works but `find()` is more efficient
6. **Not providing custom comparator correctly** - Must satisfy strict weak ordering
7. **Expecting linear iteration to be O(1)** - Iteration is O(n), but that's fine
8. **Modifying map while iterating** - Can invalidate iterators

---
---

## Next Step

- Go to [06_Unassociative_Container.md](06_Unassociative_Container.md) to continue with Unassociative Container.
