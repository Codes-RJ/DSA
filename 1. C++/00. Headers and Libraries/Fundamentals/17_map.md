# 17_map.md - Ordered Key-Value Container

The `map` header provides `std::map`, an associative container that stores key-value pairs in sorted order by key. It implements a balanced binary search tree (typically Red-Black Tree).

## 📖 Overview

`std::map` is an associative container that contains sorted key-value pairs with unique keys. It provides logarithmic time complexity for most operations and maintains elements in ascending order by key.

## 🎯 Key Features

- **Unique keys** - No duplicate keys allowed
- **Ordered storage** - Elements always kept sorted by key
- **Key-value pairs** - Each key maps to exactly one value
- **Logarithmic operations** - O(log n) for insert, delete, find
- **Bidirectional iterators** - Can traverse both forward and backward
- **Automatic sorting** - Elements inserted in any order, stored sorted
- **Efficient range queries** - Excellent for finding ranges of keys

## 🔧 Basic Map Operations

### Creating and Initializing Maps
```cpp
#include <iostream>
#include <map>
#include <string>
#include <algorithm>

int main() {
    // Different ways to create maps
    
    // Empty map
    std::map<std::string, int> map1;
    
    // From initializer list
    std::map<std::string, int> map2 = {
        {"apple", 5},
        {"banana", 3},
        {"cherry", 8}
    };
    
    // Copy constructor
    std::map<std::string, int> map3 = map2;
    
    // From range
    std::vector<std::pair<std::string, int>> vec = {
        {"dog", 2}, {"elephant", 4}
    };
    std::map<std::string, int> map4(vec.begin(), vec.end());
    
    // With custom comparator
    std::map<std::string, int, std::greater<std::string>> map5 = {
        {"zebra", 1}, {"yak", 2}, {"xenon", 3}
    };  // Descending order
    
    return 0;
}
```

### Insertion and Access
```cpp
void demonstrateBasicOperations() {
    std::map<std::string, int> scores;
    
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
    std::map<std::string, int> inventory = {
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
    
    // Erase range
    auto start = inventory.find("armor");
    if (start != inventory.end()) {
        inventory.erase(start, inventory.end());
    }
    
    std::cout << "\nAfter erasures:" << std::endl;
    for (const auto& [item, count] : inventory) {
        std::cout << item << ": " << count << std::endl;
    }
    
    // Update value
    inventory["sword"] = 2;
    
    std::cout << "\nSword count updated: " << inventory["sword"] << std::endl;
}
```

## 🔧 Advanced Map Operations

### Range Queries and Bounds
```cpp
void demonstrateRangeQueries() {
    std::map<int, std::string> students = {
        {1001, "Alice"},
        {1003, "Bob"},
        {1005, "Charlie"},
        {1007, "Diana"},
        {1009, "Eve"}
    };
    
    // Lower bound (first element >= key)
    auto lb = students.lower_bound(1004);
    if (lb != students.end()) {
        std::cout << "Lower bound of 1004: " << lb->first << " -> " << lb->second << std::endl;
    }
    
    // Upper bound (first element > key)
    auto ub = students.upper_bound(1005);
    if (ub != students.end()) {
        std::cout << "Upper bound of 1005: " << ub->first << " -> " << ub->second << std::endl;
    }
    
    // Equal range (range of elements equal to key)
    auto range = students.equal_range(1005);
    std::cout << "Equal range of 1005: ";
    for (auto it = range.first; it != range.second; ++it) {
        std::cout << it->second << " ";
    }
    std::cout << std::endl;
    
    // Get all students in ID range
    std::cout << "\nStudents with IDs 1003-1007:" << std::endl;
    auto start = students.lower_bound(1003);
    auto end = students.upper_bound(1007);
    
    for (auto it = start; it != end; ++it) {
        std::cout << it->first << " -> " << it->second << std::endl;
    }
}
```

### Custom Comparators and Complex Keys
```cpp
struct Person {
    std::string name;
    int age;
    double salary;
    
    Person(const std::string& n, int a, double s) 
        : name(n), age(a), salary(s) {}
    
    bool operator<(const Person& other) const {
        return age < other.age;  // Sort by age
    }
};

struct PersonComparator {
    bool operator()(const Person& a, const Person& b) const {
        return a.salary > b.salary;  // Sort by salary descending
    }
};

void demonstrateCustomKeys() {
    // Using default comparison (by age)
    std::map<Person, std::string> jobs_by_age;
    jobs_by_age[Person("Alice", 25, 50000)] = "Developer";
    jobs_by_age[Person("Bob", 30, 60000)] = "Manager";
    jobs_by_age[Person("Charlie", 20, 45000)] = "Intern";
    
    std::cout << "People sorted by age:" << std::endl;
    for (const auto& [person, job] : jobs_by_age) {
        std::cout << person.name << " (age " << person.age << "): " << job << std::endl;
    }
    
    // Using custom comparator (by salary)
    std::map<Person, std::string, PersonComparator> jobs_by_salary;
    jobs_by_salary[Person("Alice", 25, 50000)] = "Developer";
    jobs_by_salary[Person("Bob", 30, 60000)] = "Manager";
    jobs_by_salary[Person("Charlie", 20, 45000)] = "Intern";
    
    std::cout << "\nPeople sorted by salary (descending):" << std::endl;
    for (const auto& [person, job] : jobs_by_salary) {
        std::cout << person.name << " (salary $" << person.salary << "): " << job << std::endl;
    }
}
```

## 🎮 Practical Examples

### Example 1: Student Information System
```cpp
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>

class StudentInfoSystem {
private:
    struct Student {
        std::string name;
        int age;
        double gpa;
        std::string major;
        
        Student(const std::string& n, int a, double g, const std::string& m)
            : name(n), age(a), gpa(g), major(m) {}
    };
    
    std::map<int, Student> m_students;  // Key: student ID
    std::map<std::string, std::vector<int>> m_students_by_major;
    
public:
    // Add student
    bool addStudent(int id, const std::string& name, int age, double gpa, const std::string& major) {
        if (m_students.find(id) != m_students.end()) {
            return false;  // Student already exists
        }
        
        m_students.emplace(id, Student(name, age, gpa, major));
        m_students_by_major[major].push_back(id);
        
        std::cout << "Added student " << id << ": " << name << std::endl;
        return true;
    }
    
    // Update student GPA
    bool updateGPA(int id, double new_gpa) {
        auto it = m_students.find(id);
        if (it == m_students.end()) return false;
        
        it->second.gpa = new_gpa;
        std::cout << "Updated GPA for student " << id << " to " << new_gpa << std::endl;
        return true;
    }
    
    // Change student major
    bool changeMajor(int id, const std::string& new_major) {
        auto it = m_students.find(id);
        if (it == m_students.end()) return false;
        
        // Remove from old major
        std::string old_major = it->second.major;
        auto& old_major_students = m_students_by_major[old_major];
        old_major_students.erase(
            std::remove(old_major_students.begin(), old_major_students.end(), id),
            old_major_students.end()
        );
        
        // Add to new major
        it->second.major = new_major;
        m_students_by_major[new_major].push_back(id);
        
        std::cout << "Changed major for student " << id << " to " << new_major << std::endl;
        return true;
    }
    
    // Get student info
    std::optional<Student> getStudent(int id) const {
        auto it = m_students.find(id);
        if (it != m_students.end()) {
            return it->second;
        }
        return std::nullopt;
    }
    
    // Get students by major
    std::vector<Student> getStudentsByMajor(const std::string& major) const {
        std::vector<Student> result;
        
        auto it = m_students_by_major.find(major);
        if (it != m_students_by_major.end()) {
            for (int student_id : it->second) {
                auto student_it = m_students.find(student_id);
                if (student_it != m_students.end()) {
                    result.push_back(student_it->second);
                }
            }
        }
        
        return result;
    }
    
    // Get top N students by GPA
    std::vector<std::pair<int, Student>> getTopStudents(size_t n) const {
        std::vector<std::pair<int, Student>> all_students(
            m_students.begin(), m_students.end()
        );
        
        std::sort(all_students.begin(), all_students.end(),
            [](const auto& a, const auto& b) {
                return a.second.gpa > b.second.gpa;
            });
        
        if (n < all_students.size()) {
            all_students.resize(n);
        }
        
        return all_students;
    }
    
    // Get students in GPA range
    std::vector<std::pair<int, Student>> getStudentsByGPARange(double min_gpa, double max_gpa) const {
        std::vector<std::pair<int, Student>> result;
        
        for (const auto& [id, student] : m_students) {
            if (student.gpa >= min_gpa && student.gpa <= max_gpa) {
                result.emplace_back(id, student);
            }
        }
        
        return result;
    }
    
    // Get statistics
    struct Statistics {
        size_t total_students;
        double average_gpa;
        double highest_gpa;
        double lowest_gpa;
        std::string most_popular_major;
        std::map<std::string, size_t> major_counts;
    };
    
    Statistics getStatistics() const {
        Statistics stats = {0, 0.0, 0.0, 0.0, "", {}};
        
        if (m_students.empty()) return stats;
        
        stats.total_students = m_students.size();
        
        double gpa_sum = 0.0;
        for (const auto& [id, student] : m_students) {
            gpa_sum += student.gpa;
            stats.major_counts[student.major]++;
            
            if (student.gpa > stats.highest_gpa) {
                stats.highest_gpa = student.gpa;
            }
            if (stats.lowest_gpa == 0.0 || student.gpa < stats.lowest_gpa) {
                stats.lowest_gpa = student.gpa;
            }
        }
        
        stats.average_gpa = gpa_sum / stats.total_students;
        
        // Find most popular major
        auto max_it = std::max_element(stats.major_counts.begin(), stats.major_counts.end(),
            [](const auto& a, const auto& b) {
                return a.second < b.second;
            });
        
        if (max_it != stats.major_counts.end()) {
            stats.most_popular_major = max_it->first;
        }
        
        return stats;
    }
    
    // Remove student
    bool removeStudent(int id) {
        auto it = m_students.find(id);
        if (it == m_students.end()) return false;
        
        std::string major = it->second.major;
        
        // Remove from students map
        m_students.erase(it);
        
        // Remove from major map
        auto& major_students = m_students_by_major[major];
        major_students.erase(
            std::remove(major_students.begin(), major_students.end(), id),
            major_students.end()
        );
        
        std::cout << "Removed student " << id << std::endl;
        return true;
    }
    
    // Display all students
    void displayAllStudents() const {
        std::cout << "\n=== All Students (" << m_students.size() << ") ===" << std::endl;
        std::cout << std::left << std::setw(8) << "ID" 
                  << std::setw(20) << "Name" 
                  << std::setw(6) << "Age"
                  << std::setw(8) << "GPA"
                  << std::setw(15) << "Major" << std::endl;
        std::cout << std::string(57, '-') << std::endl;
        
        for (const auto& [id, student] : m_students) {
            std::cout << std::left << std::setw(8) << id
                      << std::setw(20) << student.name
                      << std::setw(6) << student.age
                      << std::setw(8) << std::fixed << std::setprecision(2) << student.gpa
                      << std::setw(15) << student.major << std::endl;
        }
    }
    
    // Display students by major
    void displayByMajor(const std::string& major) const {
        auto students = getStudentsByMajor(major);
        std::cout << "\n=== " << major << " Students (" << students.size() << ") ===" << std::endl;
        
        for (const auto& student : students) {
            std::cout << student.name << " (GPA: " << student.gpa << ")" << std::endl;
        }
    }
};

int main() {
    StudentInfoSystem sis;
    
    // Add students
    sis.addStudent(1001, "Alice Johnson", 20, 3.8, "Computer Science");
    sis.addStudent(1002, "Bob Smith", 21, 3.5, "Mathematics");
    sis.addStudent(1003, "Charlie Brown", 19, 3.9, "Computer Science");
    sis.addStudent(1004, "Diana Prince", 22, 3.7, "Physics");
    sis.addStudent(1005, "Eve Wilson", 20, 3.6, "Mathematics");
    sis.addStudent(1006, "Frank Miller", 21, 3.4, "Computer Science");
    
    sis.displayAllStudents();
    
    // Display by major
    sis.displayByMajor("Computer Science");
    sis.displayByMajor("Mathematics");
    
    // Show statistics
    auto stats = sis.getStatistics();
    std::cout << "\n=== Statistics ===" << std::endl;
    std::cout << "Total students: " << stats.total_students << std::endl;
    std::cout << "Average GPA: " << std::fixed << std::setprecision(2) << stats.average_gpa << std::endl;
    std::cout << "Highest GPA: " << stats.highest_gpa << std::endl;
    std::cout << "Lowest GPA: " << stats.lowest_gpa << std::endl;
    std::cout << "Most popular major: " << stats.most_popular_major << std::endl;
    
    std::cout << "\nMajor distribution:" << std::endl;
    for (const auto& [major, count] : stats.major_counts) {
        std::cout << major << ": " << count << " students" << std::endl;
    }
    
    // Show top students
    auto top_students = sis.getTopStudents(3);
    std::cout << "\n=== Top 3 Students by GPA ===" << std::endl;
    for (size_t i = 0; i < top_students.size(); ++i) {
        std::cout << (i + 1) << ". " << top_students[i].second.name 
                  << " (ID: " << top_students[i].first << ", GPA: " << top_students[i].second.gpa << ")" << std::endl;
    }
    
    // Update some student information
    std::cout << "\n=== Updates ===" << std::endl;
    sis.updateGPA(1002, 3.8);  // Bob improves
    sis.changeMajor(1004, "Computer Science");  // Diana switches majors
    
    // Show students in GPA range
    std::cout << "\n=== Students with GPA 3.7-4.0 ===" << std::endl;
    auto high_gpa_students = sis.getStudentsByGPARange(3.7, 4.0);
    for (const auto& [id, student] : high_gpa_students) {
        std::cout << student.name << " (ID: " << id << ", GPA: " << student.gpa << ")" << std::endl;
    }
    
    return 0;
}
```

### Example 2: Configuration Manager
```cpp
#include <iostream>
#include <map>
#include <string>
#include <fstream>
#include <sstream>
#include <variant>
#include <functional>

class ConfigManager {
private:
    using ConfigValue = std::variant<int, double, bool, std::string>;
    std::map<std::string, ConfigValue> m_config;
    std::map<std::string, std::function<void(const ConfigValue&)>> m_callbacks;
    
public:
    // Set configuration values
    template<typename T>
    void set(const std::string& key, const T& value) {
        ConfigValue old_value;
        bool has_old = false;
        
        auto it = m_config.find(key);
        if (it != m_config.end()) {
            old_value = it->second;
            has_old = true;
        }
        
        m_config[key] = value;
        
        // Trigger callback if value changed
        if (!has_old || old_value != value) {
            auto callback_it = m_callbacks.find(key);
            if (callback_it != m_callbacks.end()) {
                callback_it->second(value);
            }
        }
    }
    
    // Get configuration values
    template<typename T>
    std::optional<T> get(const std::string& key) const {
        auto it = m_config.find(key);
        if (it != m_config.end()) {
            if (auto val = std::get_if<T>(&it->second)) {
                return *val;
            }
        }
        return std::nullopt;
    }
    
    // Get with default value
    template<typename T>
    T getOrDefault(const std::string& key, const T& default_value) const {
        auto result = get<T>(key);
        return result ? *result : default_value;
    }
    
    // Check if key exists
    bool has(const std::string& key) const {
        return m_config.find(key) != m_config.end();
    }
    
    // Remove configuration
    bool remove(const std::string& key) {
        auto it = m_config.find(key);
        if (it != m_config.end()) {
            m_config.erase(it);
            return true;
        }
        return false;
    }
    
    // Register callback for value changes
    void on_change(const std::string& key, std::function<void(const ConfigValue&)> callback) {
        m_callbacks[key] = callback;
    }
    
    // Load from file
    bool loadFromFile(const std::string& filename) {
        std::ifstream file(filename);
        if (!file.is_open()) {
            std::cerr << "Cannot open config file: " << filename << std::endl;
            return false;
        }
        
        std::string line;
        while (std::getline(file, line)) {
            // Skip empty lines and comments
            if (line.empty() || line[0] == '#') continue;
            
            size_t eq_pos = line.find('=');
            if (eq_pos == std::string::npos) continue;
            
            std::string key = line.substr(0, eq_pos);
            std::string value = line.substr(eq_pos + 1);
            
            // Trim whitespace
            key.erase(0, key.find_first_not_of(" \t"));
            key.erase(key.find_last_not_of(" \t") + 1);
            value.erase(0, value.find_first_not_of(" \t"));
            value.erase(value.find_last_not_of(" \t") + 1);
            
            // Parse value type
            if (value == "true" || value == "false") {
                set(key, value == "true");
            } else if (value.find('.') != std::string::npos) {
                try {
                    set(key, std::stod(value));
                } catch (...) {
                    set(key, value);
                }
            } else {
                try {
                    set(key, std::stoi(value));
                } catch (...) {
                    set(key, value);
                }
            }
        }
        
        std::cout << "Loaded configuration from " << filename << std::endl;
        return true;
    }
    
    // Save to file
    bool saveToFile(const std::string& filename) const {
        std::ofstream file(filename);
        if (!file.is_open()) {
            std::cerr << "Cannot create config file: " << filename << std::endl;
            return false;
        }
        
        file << "# Configuration File\n";
        file << "# Generated by ConfigManager\n\n";
        
        for (const auto& [key, value] : m_config) {
            file << key << " = ";
            
            std::visit([&file](const auto& v) {
                using T = std::decay_t<decltype(v)>;
                if constexpr (std::is_same_v<T, bool>) {
                    file << (v ? "true" : "false");
                } else if constexpr (std::is_same_v<T, std::string>) {
                    file << v;
                } else {
                    file << v;
                }
            }, value);
            
            file << "\n";
        }
        
        std::cout << "Saved configuration to " << filename << std::endl;
        return true;
    }
    
    // Get all keys
    std::vector<std::string> getKeys() const {
        std::vector<std::string> keys;
        for (const auto& [key, value] : m_config) {
            keys.push_back(key);
        }
        return keys;
    }
    
    // Get keys in range
    std::vector<std::string> getKeysInRange(const std::string& start, const std::string& end) const {
        std::vector<std::string> keys;
        
        auto lower = m_config.lower_bound(start);
        auto upper = m_config.upper_bound(end);
        
        for (auto it = lower; it != upper; ++it) {
            keys.push_back(it->first);
        }
        
        return keys;
    }
    
    // Display configuration
    void display() const {
        std::cout << "\n=== Configuration (" << m_config.size() << " settings) ===" << std::endl;
        
        for (const auto& [key, value] : m_config) {
            std::cout << key << " = ";
            
            std::visit([](const auto& v) {
                using T = std::decay_t<decltype(v)>;
                if constexpr (std::is_same_v<T, bool>) {
                    std::cout << (v ? "true" : "false");
                } else if constexpr (std::is_same_v<T, std::string>) {
                    std::cout << "\"" << v << "\"";
                } else {
                    std::cout << v;
                }
            }, value);
            
            std::cout << std::endl;
        }
    }
    
    // Clear all configuration
    void clear() {
        m_config.clear();
        m_callbacks.clear();
    }
};

int main() {
    ConfigManager config;
    
    // Set up callbacks
    config.on_change("debug", [](const ConfigManager::ConfigValue& value) {
        if (auto debug = std::get_if<bool>(&value)) {
            std::cout << "Debug mode " << (*debug ? "enabled" : "disabled") << std::endl;
        }
    });
    
    config.on_change("max_connections", [](const ConfigManager::ConfigValue& value) {
        if (auto max_conn = std::get_if<int>(&value)) {
            std::cout << "Max connections set to " << *max_conn << std::endl;
        }
    });
    
    // Set some configuration values
    config.set("debug", true);
    config.set("max_connections", 100);
    config.set("timeout", 30.5);
    config.set("server_name", std::string("MyServer"));
    config.set("enable_ssl", true);
    
    config.display();
    
    // Test getting values
    std::cout << "\n=== Getting Values ===" << std::endl;
    
    auto debug = config.get<bool>("debug");
    if (debug) std::cout << "Debug: " << (*debug ? "enabled" : "disabled") << std::endl;
    
    auto timeout = config.get<double>("timeout");
    if (timeout) std::cout << "Timeout: " << *timeout << " seconds" << std::endl;
    
    auto server_name = config.get<std::string>("server_name");
    if (server_name) std::cout << "Server: " << *server_name << std::endl;
    
    // Test default values
    auto port = config.getOrDefault<int>("port", 8080);
    std::cout << "Port: " << port << std::endl;
    
    // Update some values (should trigger callbacks)
    std::cout << "\n=== Updating Values ===" << std::endl;
    config.set("debug", false);
    config.set("max_connections", 200);
    
    // Save to file
    config.saveToFile("config.txt");
    
    // Clear and reload
    std::cout << "\n=== Clearing and Reloading ===" << std::endl;
    config.clear();
    config.display();
    
    config.loadFromFile("config.txt");
    config.display();
    
    // Test range queries
    std::cout << "\n=== Range Query ===" << std::endl;
    auto keys = config.getKeysInRange("m", "t");
    std::cout << "Keys between 'm' and 't': ";
    for (const auto& key : keys) {
        std::cout << key << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
```

### Example 3: Cache System with TTL
```cpp
#include <iostream>
#include <map>
#include <string>
#include <chrono>
#include <optional>
#include <thread>

class TTLCache {
private:
    struct CacheEntry {
        std::string value;
        std::chrono::steady_clock::time_point expiry;
        
        CacheEntry(const std::string& v, std::chrono::milliseconds ttl)
            : value(v), expiry(std::chrono::steady_clock::now() + ttl) {}
        
        bool isExpired() const {
            return std::chrono::steady_clock::now() > expiry;
        }
    };
    
    std::map<std::string, CacheEntry> m_cache;
    std::chrono::milliseconds m_default_ttl;
    
    // Clean up expired entries
    void cleanup() {
        auto it = m_cache.begin();
        while (it != m_cache.end()) {
            if (it->second.isExpired()) {
                it = m_cache.erase(it);
            } else {
                ++it;
            }
        }
    }
    
public:
    TTLCache(std::chrono::milliseconds default_ttl = std::chrono::minutes(5))
        : m_default_ttl(default_ttl) {}
    
    // Put value with default TTL
    void put(const std::string& key, const std::string& value) {
        cleanup();
        m_cache[key] = CacheEntry(value, m_default_ttl);
    }
    
    // Put value with custom TTL
    void put(const std::string& key, const std::string& value, std::chrono::milliseconds ttl) {
        cleanup();
        m_cache[key] = CacheEntry(value, ttl);
    }
    
    // Get value
    std::optional<std::string> get(const std::string& key) {
        cleanup();
        
        auto it = m_cache.find(key);
        if (it != m_cache.end() && !it->second.isExpired()) {
            return it->second.value;
        }
        
        return std::nullopt;
    }
    
    // Check if key exists and is not expired
    bool contains(const std::string& key) {
        cleanup();
        auto it = m_cache.find(key);
        return it != m_cache.end() && !it->second.isExpired();
    }
    
    // Remove key
    bool remove(const std::string& key) {
        cleanup();
        return m_cache.erase(key) > 0;
    }
    
    // Get time remaining for key
    std::optional<std::chrono::milliseconds> getTimeRemaining(const std::string& key) {
        auto it = m_cache.find(key);
        if (it != m_cache.end() && !it->second.isExpired()) {
            auto remaining = std::chrono::duration_cast<std::chrono::milliseconds>(
                it->second.expiry - std::chrono::steady_clock::now()
            );
            return remaining;
        }
        return std::nullopt;
    }
    
    // Get all non-expired keys
    std::vector<std::string> getKeys() const {
        std::vector<std::string> keys;
        
        for (const auto& [key, entry] : m_cache) {
            if (!entry.isExpired()) {
                keys.push_back(key);
            }
        }
        
        return keys;
    }
    
    // Clear all entries
    void clear() {
        m_cache.clear();
    }
    
    // Get cache statistics
    struct Statistics {
        size_t total_entries;
        size_t expired_entries;
        size_t valid_entries;
    };
    
    Statistics getStatistics() const {
        Statistics stats = {0, 0, 0};
        
        for (const auto& [key, entry] : m_cache) {
            stats.total_entries++;
            if (entry.isExpired()) {
                stats.expired_entries++;
            } else {
                stats.valid_entries++;
            }
        }
        
        return stats;
    }
    
    // Display cache contents
    void display() const {
        std::cout << "\n=== Cache Contents ===" << std::endl;
        
        for (const auto& [key, entry] : m_cache) {
            bool expired = entry.isExpired();
            auto remaining = std::chrono::duration_cast<std::chrono::seconds>(
                entry.expiry - std::chrono::steady_clock::now()
            );
            
            std::cout << key << " = \"" << entry.value << "\"";
            if (expired) {
                std::cout << " [EXPIRED]";
            } else {
                std::cout << " [" << remaining.count() << "s remaining]";
            }
            std::cout << std::endl;
        }
    }
};

int main() {
    TTLCache cache(std::chrono::seconds(3));  // 3 second default TTL
    
    std::cout << "=== TTL Cache Test ===" << std::endl;
    
    // Add some entries
    cache.put("user:1", "Alice");
    cache.put("user:2", "Bob", std::chrono::seconds(5));  // Custom TTL
    cache.put("session:abc", "active", std::chrono::seconds(2));
    
    cache.display();
    
    // Test retrieval
    std::cout << "\n=== Testing Retrieval ===" << std::endl;
    
    auto user1 = cache.get("user:1");
    if (user1) {
        std::cout << "user:1 = " << *user1 << std::endl;
    }
    
    auto session = cache.get("session:abc");
    if (session) {
        std::cout << "session:abc = " << *session << std::endl;
    }
    
    // Check time remaining
    auto time_left = cache.getTimeRemaining("user:1");
    if (time_left) {
        std::cout << "user:1 expires in " << time_left->count() << "ms" << std::endl;
    }
    
    // Wait for some entries to expire
    std::cout << "\n=== Waiting for expiration ===" << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(3));
    
    cache.display();
    
    // Test after expiration
    std::cout << "\n=== Testing After Expiration ===" << std::endl;
    
    user1 = cache.get("user:1");
    if (user1) {
        std::cout << "user:1 = " << *user1 << std::endl;
    } else {
        std::cout << "user:1 not found or expired" << std::endl;
    }
    
    session = cache.get("session:abc");
    if (session) {
        std::cout << "session:abc = " << *session << std::endl;
    } else {
        std::cout << "session:abc not found or expired" << std::endl;
    }
    
    auto user2 = cache.get("user:2");
    if (user2) {
        std::cout << "user:2 = " << *user2 << std::endl;
    } else {
        std::cout << "user:2 not found or expired" << std::endl;
    }
    
    // Show statistics
    auto stats = cache.getStatistics();
    std::cout << "\n=== Statistics ===" << std::endl;
    std::cout << "Total entries: " << stats.total_entries << std::endl;
    std::cout << "Expired entries: " << stats.expired_entries << std::endl;
    std::cout << "Valid entries: " << stats.valid_entries << std::endl;
    
    // Add more entries and test cleanup
    std::cout << "\n=== Adding More Entries ===" << std::endl;
    cache.put("temp:1", "data1", std::chrono::seconds(1));
    cache.put("temp:2", "data2", std::chrono::seconds(1));
    cache.put("persistent:1", "important", std::chrono::seconds(10));
    
    cache.display();
    
    std::this_thread::sleep_for(std::chrono::seconds(2));
    
    std::cout << "\n=== After Cleanup ===" << std::endl;
    cache.display();
    
    // Test contains
    std::cout << "\n=== Contains Test ===" << std::endl;
    std::cout << "Contains user:2: " << (cache.contains("user:2") ? "Yes" : "No") << std::endl;
    std::cout << "Contains temp:1: " << (cache.contains("temp:1") ? "Yes" : "No") << std::endl;
    std::cout << "Contains persistent:1: " << (cache.contains("persistent:1") ? "Yes" : "No") << std::endl;
    
    return 0;
}
```

### Example 4: Symbol Table for Compiler
```cpp
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <variant>
#include <optional>

enum class SymbolType {
    VARIABLE,
    FUNCTION,
    CLASS,
    CONSTANT,
    PARAMETER
};

enum class DataType {
    INT,
    FLOAT,
    STRING,
    BOOL,
    VOID,
    CUSTOM
};

class SymbolTable {
private:
    struct SymbolInfo {
        SymbolType type;
        DataType data_type;
        std::string custom_type;  // For CUSTOM data type
        int scope_level;
        size_t line_number;
        bool is_defined;
        
        // For functions
        std::vector<DataType> param_types;
        DataType return_type;
        
        // For variables/constants
        std::variant<int, double, std::string, bool> constant_value;
        
        SymbolInfo(SymbolType t, DataType dt, int scope, size_t line)
            : type(t), data_type(dt), scope_level(scope), line_number(line), is_defined(false) {}
    };
    
    std::map<std::string, SymbolInfo> m_symbols;
    std::map<int, std::vector<std::string>> m_scope_symbols;  // scope -> symbols
    int m_current_scope;
    
public:
    SymbolTable() : m_current_scope(0) {}
    
    // Enter new scope
    void enterScope() {
        m_current_scope++;
        std::cout << "Entered scope level " << m_current_scope << std::endl;
    }
    
    // Exit scope
    void exitScope() {
        if (m_current_scope > 0) {
            // Remove symbols in current scope
            auto it = m_scope_symbols.find(m_current_scope);
            if (it != m_scope_symbols.end()) {
                for (const auto& symbol_name : it->second) {
                    m_symbols.erase(symbol_name);
                }
                m_scope_symbols.erase(it);
            }
            
            std::cout << "Exited scope level " << m_current_scope << std::endl;
            m_current_scope--;
        }
    }
    
    // Add variable
    bool addVariable(const std::string& name, DataType data_type, size_t line) {
        if (m_symbols.find(name) != m_symbols.end()) {
            std::cerr << "Error: Symbol '" << name << "' already exists at line " << line << std::endl;
            return false;
        }
        
        SymbolInfo info(SymbolType::VARIABLE, data_type, m_current_scope, line);
        m_symbols[name] = info;
        m_scope_symbols[m_current_scope].push_back(name);
        
        std::cout << "Added variable '" << name << "' of type " << dataTypeToString(data_type) 
                  << " at scope " << m_current_scope << std::endl;
        return true;
    }
    
    // Add function
    bool addFunction(const std::string& name, const std::vector<DataType>& param_types, 
                    DataType return_type, size_t line) {
        if (m_symbols.find(name) != m_symbols.end()) {
            std::cerr << "Error: Symbol '" << name << "' already exists at line " << line << std::endl;
            return false;
        }
        
        SymbolInfo info(SymbolType::FUNCTION, return_type, m_current_scope, line);
        info.param_types = param_types;
        info.return_type = return_type;
        m_symbols[name] = info;
        m_scope_symbols[m_current_scope].push_back(name);
        
        std::cout << "Added function '" << name << "' returning " << dataTypeToString(return_type) << std::endl;
        return true;
    }
    
    // Add class
    bool addClass(const std::string& name, size_t line) {
        if (m_symbols.find(name) != m_symbols.end()) {
            std::cerr << "Error: Symbol '" << name << "' already exists at line " << line << std::endl;
            return false;
        }
        
        SymbolInfo info(SymbolType::CLASS, DataType::CUSTOM, m_current_scope, line);
        info.custom_type = name;
        m_symbols[name] = info;
        m_scope_symbols[m_current_scope].push_back(name);
        
        std::cout << "Added class '" << name << "' at scope " << m_current_scope << std::endl;
        return true;
    }
    
    // Add constant
    template<typename T>
    bool addConstant(const std::string& name, DataType data_type, const T& value, size_t line) {
        if (m_symbols.find(name) != m_symbols.end()) {
            std::cerr << "Error: Symbol '" << name << "' already exists at line " << line << std::endl;
            return false;
        }
        
        SymbolInfo info(SymbolType::CONSTANT, data_type, m_current_scope, line);
        info.constant_value = value;
        info.is_defined = true;
        m_symbols[name] = info;
        m_scope_symbols[m_current_scope].push_back(name);
        
        std::cout << "Added constant '" << name << "' with value ";
        std::visit([](const auto& v) { std::cout << v; }, value);
        std::cout << std::endl;
        return true;
    }
    
    // Mark symbol as defined
    bool markDefined(const std::string& name) {
        auto it = m_symbols.find(name);
        if (it != m_symbols.end()) {
            it->second.is_defined = true;
            std::cout << "Marked '" << name << "' as defined" << std::endl;
            return true;
        }
        return false;
    }
    
    // Lookup symbol
    std::optional<SymbolInfo> lookup(const std::string& name) const {
        auto it = m_symbols.find(name);
        if (it != m_symbols.end()) {
            return it->second;
        }
        return std::nullopt;
    }
    
    // Check if symbol exists
    bool exists(const std::string& name) const {
        return m_symbols.find(name) != m_symbols.end();
    }
    
    // Get symbols in current scope
    std::vector<std::string> getScopeSymbols() const {
        std::vector<std::string> result;
        
        auto it = m_scope_symbols.find(m_current_scope);
        if (it != m_scope_symbols.end()) {
            result = it->second;
        }
        
        return result;
    }
    
    // Get all symbols
    std::vector<std::pair<std::string, SymbolInfo>> getAllSymbols() const {
        std::vector<std::pair<std::string, SymbolInfo>> result;
        
        for (const auto& [name, info] : m_symbols) {
            result.emplace_back(name, info);
        }
        
        return result;
    }
    
    // Helper function to convert DataType to string
    std::string dataTypeToString(DataType type) const {
        switch (type) {
            case DataType::INT: return "int";
            case DataType::FLOAT: return "float";
            case DataType::STRING: return "string";
            case DataType::BOOL: return "bool";
            case DataType::VOID: return "void";
            case DataType::CUSTOM: return "custom";
            default: return "unknown";
        }
    }
    
    std::string symbolTypeToString(SymbolType type) const {
        switch (type) {
            case SymbolType::VARIABLE: return "variable";
            case SymbolType::FUNCTION: return "function";
            case SymbolType::CLASS: return "class";
            case SymbolType::CONSTANT: return "constant";
            case SymbolType::PARAMETER: return "parameter";
            default: return "unknown";
        }
    }
    
    // Display symbol table
    void display() const {
        std::cout << "\n=== Symbol Table (Scope " << m_current_scope << ") ===" << std::endl;
        std::cout << std::left << std::setw(15) << "Name"
                  << std::setw(12) << "Type"
                  << std::setw(12) << "Data Type"
                  << std::setw(8) << "Scope"
                  << std::setw(8) << "Line"
                  << std::setw(10) << "Defined"
                  << "Details" << std::endl;
        std::cout << std::string(75, '-') << std::endl;
        
        for (const auto& [name, info] : m_symbols) {
            std::cout << std::left << std::setw(15) << name
                      << std::setw(12) << symbolTypeToString(info.type)
                      << std::setw(12) << dataTypeToString(info.data_type)
                      << std::setw(8) << info.scope_level
                      << std::setw(8) << info.line_number
                      << std::setw(10) << (info.is_defined ? "Yes" : "No");
            
            if (info.type == SymbolType::FUNCTION) {
                std::cout << "Params: ";
                for (size_t i = 0; i < info.param_types.size(); ++i) {
                    if (i > 0) std::cout << ", ";
                    std::cout << dataTypeToString(info.param_types[i]);
                }
                std::cout << " -> " << dataTypeToString(info.return_type);
            } else if (info.type == SymbolType::CONSTANT) {
                std::cout << "Value: ";
                std::visit([](const auto& v) { std::cout << v; }, info.constant_value);
            }
            
            std::cout << std::endl;
        }
    }
    
    // Get current scope level
    int getCurrentScope() const {
        return m_current_scope;
    }
};

int main() {
    SymbolTable symtab;
    
    std::cout << "=== Symbol Table Demo ===" << std::endl;
    
    // Global scope
    symtab.addConstant("PI", DataType::FLOAT, 3.14159, 1);
    symtab.addVariable("global_counter", DataType::INT, 2);
    symtab.addClass("MyClass", 3);
    symtab.addFunction("main", {}, DataType::INT, 4);
    symtab.addFunction("calculate", {DataType::INT, DataType::FLOAT}, DataType::FLOAT, 5);
    
    symtab.display();
    
    // Enter function scope
    symtab.enterScope();
    
    symtab.addVariable("local_var", DataType::STRING, 6);
    symtab.addVariable("result", DataType::FLOAT, 7);
    symtab.markDefined("local_var");
    
    std::cout << "\n=== Inside Function Scope ===" << std::endl;
    symtab.display();
    
    // Test lookup
    std::cout << "\n=== Symbol Lookup ===" << std::endl;
    
    auto pi = symtab.lookup("PI");
    if (pi) {
        std::cout << "Found PI: " << symtab.symbolTypeToString(pi->type) 
                  << " of type " << symtab.dataTypeToString(pi->data_type) << std::endl;
    }
    
    auto local_var = symtab.lookup("local_var");
    if (local_var) {
        std::cout << "Found local_var: defined=" << local_var->is_defined 
                  << ", scope=" << local_var->scope_level << std::endl;
    }
    
    // Enter nested scope
    symtab.enterScope();
    
    symtab.addVariable("nested_var", DataType::BOOL, 8);
    symtab.addVariable("result", DataType::INT, 9);  // Shadows outer result
    
    std::cout << "\n=== Inside Nested Scope ===" << std::endl;
    symtab.display();
    
    // Exit nested scope
    symtab.exitScope();
    
    std::cout << "\n=== Back to Function Scope ===" << std::endl;
    symtab.display();
    
    // Exit function scope
    symtab.exitScope();
    
    std::cout << "\n=== Back to Global Scope ===" << std::endl;
    symtab.display();
    
    // Test scope-specific symbols
    std::cout << "\n=== Current Scope Symbols ===" << std::endl;
    auto scope_symbols = symtab.getScopeSymbols();
    std::cout << "Symbols in scope " << symtab.getCurrentScope() << ": ";
    for (const auto& symbol : scope_symbols) {
        std::cout << symbol << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
```

## 📊 Complete Function Reference

### Element Access
| Function | Description | Complexity |
|----------|-------------|------------|
| `operator[]` | Access/insert element (creates if missing) | O(log n) |
| `at()` | Access element with bounds checking | O(log n) |
| `find()` | Find element by key | O(log n) |
| `count()` | Count occurrences of key | O(log n) |

### Modifiers
| Function | Description | Complexity |
|----------|-------------|------------|
| `insert()` | Insert element(s) | O(log n) |
| `insert_or_assign()` | Insert or update element | O(log n) |
| `erase()` | Remove element(s) | O(log n) |
| `clear()` | Remove all elements | O(n) |
| `swap()` | Swap contents | O(1) |

### Operations
| Function | Description | Complexity |
|----------|-------------|------------|
| `lower_bound()` | First element >= key | O(log n) |
| `upper_bound()` | First element > key | O(log n) |
| `equal_range()` | Range of equal elements | O(log n) |

### Capacity
| Function | Description | Complexity |
|----------|-------------|------------|
| `size()` | Number of elements | O(1) |
| `empty()` | Check if empty | O(1) |
| `max_size()` | Maximum possible size | O(1) |

## ⚡ Performance Considerations

### Memory Layout
```cpp
// Map uses balanced binary tree (Red-Black Tree)
// Each node contains: key, value, color, parent, left, right pointers
// Logarithmic height guarantees O(log n) operations

std::map<std::string, int> m = {{"a", 1}, {"b", 2}, {"c", 3}};
// Internal structure (simplified):
//       "b"(black)
//      /        \
//   "a"(red)   "c"(red)
```

### Iterator Invalidation
```cpp
// Map iterators remain valid except for erased elements
std::map<int, std::string> m = {{1, "one"}, {2, "two"}, {3, "three"}};
auto it = m.find(2);

m.insert({4, "four"});  // it still valid
m.erase(1);             // it still valid
m.erase(2);             // it becomes invalid
```

## 🎯 Common Patterns

### Pattern 1: Dictionary/Lookup Table
```cpp
class Dictionary {
private:
    std::map<std::string, std::string> m_data;
    
public:
    void add(const std::string& key, const std::string& value) {
        m_data[key] = value;
    }
    
    std::optional<std::string> get(const std::string& key) const {
        auto it = m_data.find(key);
        return it != m_data.end() ? std::optional<std::string>{it->second} : std::nullopt;
    }
};
```

### Pattern 2: Frequency Counter
```cpp
class FrequencyCounter {
private:
    std::map<std::string, int> m_counts;
    
public:
    void add(const std::string& item) {
        m_counts[item]++;
    }
    
    std::vector<std::pair<std::string, int>> getSorted() const {
        std::vector<std::pair<std::string, int>> result(
            m_counts.begin(), m_counts.end()
        );
        std::sort(result.begin(), result.end(),
            [](const auto& a, const auto& b) { return a.second > b.second; });
        return result;
    }
};
```

## 🐛 Common Pitfalls & Solutions

### 1. operator[] Creates Missing Keys
```cpp
// Problem
std::map<std::string, int> counts;
int value = counts["missing"];  // Creates key with default value 0

// Solution
auto it = counts.find("missing");
if (it != counts.end()) {
    int value = it->second;
}
// or use at()
int value = counts.at("missing");  // Throws if not found
```

### 2. Modifying Keys
```cpp
// Problem
std::map<std::string, int> m;
auto it = m.find("key");
it->first = "new_key";  // Error: keys are const

// Solution
int value = it->second;
m.erase(it);
m["new_key"] = value;
```

### 3. Performance with Large Objects
```cpp
// Problem - copying large values
std::map<int, LargeObject> m;  // Expensive copies

// Solution - use pointers or move semantics
std::map<int, std::unique_ptr<LargeObject>> m;
// or
m.emplace(key, std::move(obj));
```

## 📚 Related Headers

- `unordered_map.md` - Hash-based key-value container
- `set.md` - Ordered unique keys
- `unordered_set.md` - Hash-based unique keys
- `algorithm.md` - Generic algorithms

## 🚀 Best Practices

1. **Use map** when you need ordered key-value pairs
2. **Use unordered_map** for better performance when order doesn't matter
3. **Prefer at()** over operator[] for safe access
4. **Use emplace()** for in-place construction
5. **Leverage range operations** for efficient queries
6. **Consider move semantics** for large values

## 🎯 When to Use map

✅ **Use map when:**
- Need ordered key-value pairs
- Frequent range queries by key
- Need sorted iteration
- Keys must be unique
- Logarithmic performance is acceptable

❌ **Avoid when:**
- Need constant-time lookup (use `unordered_map`)
- Order doesn't matter (use `unordered_map`)
- Need duplicate keys (use `multimap`)
- Keys are expensive to compare
---

## Next Step

- Go to [18_unordered_map.md](18_unordered_map.md) to continue with unordered map.
