# 15_set.md - Ordered Unique Container

The `set` header provides `std::set`, an associative container that stores unique elements in sorted order. It implements a balanced binary search tree (typically Red-Black Tree).

## 📖 Overview

`std::set` is an associative container that contains a sorted set of unique objects. It provides logarithmic time complexity for most operations and maintains elements in ascending order by default.

## 🎯 Key Features

- **Unique elements** - No duplicate values allowed
- **Ordered storage** - Elements always kept in sorted order
- **Logarithmic operations** - O(log n) for insert, delete, find
- **Bidirectional iterators** - Can traverse both forward and backward
- **Automatic sorting** - Elements inserted in any order, stored sorted
- **Efficient range queries** - Excellent for finding ranges of values

## 🔧 Basic Set Operations

### Creating and Initializing Sets
```cpp
#include <iostream>
#include <set>
#include <algorithm>

int main() {
    // Different ways to create sets
    
    // Empty set
    std::set<int> set1;
    
    // From initializer list
    std::set<int> set2 = {5, 2, 8, 1, 3};
    
    // Copy constructor
    std::set<int> set3 = set2;
    
    // From range
    std::vector<int> vec = {4, 1, 6, 2, 5};
    std::set<int> set4(vec.begin(), vec.end());
    
    // With custom comparator
    std::set<int, std::greater<int>> set5 = {1, 3, 2, 5, 4};  // Descending order
    
    return 0;
}
```

### Insertion and Erasure
```cpp
void demonstrateBasicOperations() {
    std::set<int> s;
    
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

### Searching and Accessing
```cpp
void demonstrateSearching() {
    std::set<int> s = {1, 3, 5, 7, 9, 11, 13};
    
    // Find element
    auto it = s.find(7);
    if (it != s.end()) {
        std::cout << "Found 7 at position: " << std::distance(s.begin(), it) << std::endl;
    } else {
        std::cout << "7 not found" << std::endl;
    }
    
    // Count occurrences (0 or 1 for set)
    int count = s.count(5);
    std::cout << "Count of 5: " << count << std::endl;
    
    // Lower bound (first element >= value)
    auto lb = s.lower_bound(6);
    if (lb != s.end()) {
        std::cout << "Lower bound of 6: " << *lb << std::endl;
    }
    
    // Upper bound (first element > value)
    auto ub = s.upper_bound(7);
    if (ub != s.end()) {
        std::cout << "Upper bound of 7: " << *ub << std::endl;
    }
    
    // Equal range (range of elements equal to value)
    auto range = s.equal_range(7);
    std::cout << "Equal range of 7: ";
    for (auto it = range.first; it != range.second; ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
}
```

## 🔧 Advanced Set Operations

### Set Operations and Algorithms
```cpp
void demonstrateSetOperations() {
    std::set<int> set1 = {1, 2, 3, 4, 5};
    std::set<int> set2 = {4, 5, 6, 7, 8};
    
    // Union
    std::set<int> union_set;
    std::set_union(set1.begin(), set1.end(),
                   set2.begin(), set2.end(),
                   std::inserter(union_set, union_set.begin()));
    
    std::cout << "Union: ";
    for (int val : union_set) std::cout << val << " ";
    std::cout << std::endl;
    
    // Intersection
    std::set<int> intersection_set;
    std::set_intersection(set1.begin(), set1.end(),
                         set2.begin(), set2.end(),
                         std::inserter(intersection_set, intersection_set.begin()));
    
    std::cout << "Intersection: ";
    for (int val : intersection_set) std::cout << val << " ";
    std::cout << std::endl;
    
    // Difference
    std::set<int> difference_set;
    std::set_difference(set1.begin(), set1.end(),
                       set2.begin(), set2.end(),
                       std::inserter(difference_set, difference_set.begin()));
    
    std::cout << "Difference (set1 - set2): ";
    for (int val : difference_set) std::cout << val << " ";
    std::cout << std::endl;
    
    // Symmetric difference
    std::set<int> sym_diff_set;
    std::set_symmetric_difference(set1.begin(), set1.end(),
                                 set2.begin(), set2.end(),
                                 std::inserter(sym_diff_set, sym_diff_set.begin()));
    
    std::cout << "Symmetric difference: ";
    for (int val : sym_diff_set) std::cout << val << " ";
    std::cout << std::endl;
}
```

### Custom Comparators and Objects
```cpp
struct Person {
    std::string name;
    int age;
    
    Person(const std::string& n, int a) : name(n), age(a) {}
    
    bool operator<(const Person& other) const {
        return age < other.age;  // Sort by age
    }
};

struct PersonComparator {
    bool operator()(const Person& a, const Person& b) const {
        return a.name < b.name;  // Sort by name
    }
};

void demonstrateCustomObjects() {
    // Using default comparison (by age)
    std::set<Person> people_by_age = {
        Person("Alice", 25),
        Person("Bob", 30),
        Person("Charlie", 20)
    };
    
    std::cout << "People sorted by age:" << std::endl;
    for (const auto& person : people_by_age) {
        std::cout << person.name << " (" << person.age << ")" << std::endl;
    }
    
    // Using custom comparator (by name)
    std::set<Person, PersonComparator> people_by_name = {
        Person("Alice", 25),
        Person("Bob", 30),
        Person("Charlie", 20)
    };
    
    std::cout << "\nPeople sorted by name:" << std::endl;
    for (const auto& person : people_by_name) {
        std::cout << person.name << " (" << person.age << ")" << std::endl;
    }
}
```

## 🎮 Practical Examples

### Example 1: Student Grade Management System
```cpp
#include <iostream>
#include <set>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>

class GradeManager {
private:
    struct Student {
        int id;
        std::string name;
        double grade;
        
        Student(int i, const std::string& n, double g) 
            : id(i), name(n), grade(g) {}
        
        bool operator<(const Student& other) const {
            return grade > other.grade;  // Sort by grade descending
        }
    };
    
    std::set<Student> m_students;
    std::set<Student> m_failed_students;
    
public:
    // Add student
    void addStudent(int id, const std::string& name, double grade) {
        Student student(id, name, grade);
        m_students.insert(student);
        
        if (grade < 60.0) {
            m_failed_students.insert(student);
        }
    }
    
    // Update student grade
    bool updateGrade(int id, double new_grade) {
        // Find student
        auto it = std::find_if(m_students.begin(), m_students.end(),
                              [id](const Student& s) { return s.id == id; });
        
        if (it == m_students.end()) return false;
        
        Student old_student = *it;
        m_students.erase(it);
        
        // Update and reinsert
        Student updated_student(id, old_student.name, new_grade);
        m_students.insert(updated_student);
        
        // Update failed students set
        auto failed_it = m_failed_students.find(old_student);
        if (failed_it != m_failed_students.end()) {
            m_failed_students.erase(failed_it);
        }
        
        if (new_grade < 60.0) {
            m_failed_students.insert(updated_student);
        }
        
        return true;
    }
    
    // Get top N students
    std::vector<Student> getTopStudents(size_t n) const {
        std::vector<Student> top_students;
        auto it = m_students.begin();
        
        for (size_t i = 0; i < std::min(n, m_students.size()); ++i) {
            top_students.push_back(*it++);
        }
        
        return top_students;
    }
    
    // Get students in grade range
    std::vector<Student> getStudentsInRange(double min_grade, double max_grade) const {
        std::vector<Student> result;
        
        // Create temporary students for bounds
        Student max_bound(0, "", max_grade);
        Student min_bound(0, "", min_grade - 0.001);
        
        auto start = m_students.lower_bound(min_bound);
        auto end = m_students.upper_bound(max_bound);
        
        for (auto it = start; it != end; ++it) {
            result.push_back(*it);
        }
        
        return result;
    }
    
    // Get class statistics
    struct Statistics {
        double average;
        double median;
        double highest;
        double lowest;
        size_t total_students;
        size_t passed_count;
        size_t failed_count;
    };
    
    Statistics getStatistics() const {
        Statistics stats = {0.0, 0.0, 0.0, 0.0, 0, 0, 0};
        
        if (m_students.empty()) return stats;
        
        stats.total_students = m_students.size();
        stats.highest = m_students.begin()->grade;
        stats.lowest = m_students.rbegin()->grade;
        stats.failed_count = m_failed_students.size();
        stats.passed_count = stats.total_students - stats.failed_count;
        
        // Calculate average
        double sum = 0.0;
        for (const auto& student : m_students) {
            sum += student.grade;
        }
        stats.average = sum / stats.total_students;
        
        // Calculate median
        if (stats.total_students % 2 == 1) {
            auto it = std::next(m_students.begin(), stats.total_students / 2);
            stats.median = it->grade;
        } else {
            auto it1 = std::next(m_students.begin(), stats.total_students / 2 - 1);
            auto it2 = std::next(m_students.begin(), stats.total_students / 2);
            stats.median = (it1->grade + it2->grade) / 2.0;
        }
        
        return stats;
    }
    
    // Display students
    void displayStudents(const std::string& title = "All Students") const {
        std::cout << "\n" << title << " (" << m_students.size() << "):" << std::endl;
        std::cout << std::left << std::setw(8) << "ID" 
                  << std::setw(20) << "Name" 
                  << std::setw(8) << "Grade" << std::endl;
        std::cout << std::string(36, '-') << std::endl;
        
        for (const auto& student : m_students) {
            std::cout << std::left << std::setw(8) << student.id
                      << std::setw(20) << student.name
                      << std::setw(8) << std::fixed << std::setprecision(1) << student.grade
                      << std::endl;
        }
    }
    
    // Display failed students
    void displayFailedStudents() const {
        std::cout << "\nFailed Students (" << m_failed_students.size() << "):" << std::endl;
        for (const auto& student : m_failed_students) {
            std::cout << student.name << " (" << student.grade << ")" << std::endl;
        }
    }
};

int main() {
    GradeManager manager;
    
    // Add students
    manager.addStudent(1, "Alice Johnson", 85.5);
    manager.addStudent(2, "Bob Smith", 72.3);
    manager.addStudent(3, "Charlie Brown", 58.7);
    manager.addStudent(4, "Diana Prince", 91.2);
    manager.addStudent(5, "Eve Wilson", 45.8);
    manager.addStudent(6, "Frank Miller", 78.9);
    manager.addStudent(7, "Grace Lee", 62.1);
    manager.addStudent(8, "Henry Ford", 55.3);
    
    manager.displayStudents();
    manager.displayFailedStudents();
    
    // Show statistics
    auto stats = manager.getStatistics();
    std::cout << "\n=== Class Statistics ===" << std::endl;
    std::cout << "Total Students: " << stats.total_students << std::endl;
    std::cout << "Passed: " << stats.passed_count << std::endl;
    std::cout << "Failed: " << stats.failed_count << std::endl;
    std::cout << "Average Grade: " << std::fixed << std::setprecision(1) << stats.average << std::endl;
    std::cout << "Median Grade: " << stats.median << std::endl;
    std::cout << "Highest Grade: " << stats.highest << std::endl;
    std::cout << "Lowest Grade: " << stats.lowest << std::endl;
    
    // Show top 3 students
    auto top_students = manager.getTopStudents(3);
    std::cout << "\n=== Top 3 Students ===" << std::endl;
    for (size_t i = 0; i < top_students.size(); ++i) {
        std::cout << (i + 1) << ". " << top_students[i].name 
                  << " (" << top_students[i].grade << ")" << std::endl;
    }
    
    // Show students in B grade range (70-79)
    auto b_students = manager.getStudentsInRange(70.0, 79.9);
    std::cout << "\n=== B Grade Students (70-79.9) ===" << std::endl;
    for (const auto& student : b_students) {
        std::cout << student.name << " (" << student.grade << ")" << std::endl;
    }
    
    // Update a student's grade
    std::cout << "\n=== Grade Updates ===" << std::endl;
    manager.updateGrade(3, 75.5);  // Charlie Brown passes
    manager.updateGrade(8, 82.0);  // Henry Ford improves significantly
    
    manager.displayStudents("Updated Students");
    manager.displayFailedStudents();
    
    return 0;
}
```

### Example 2: Interval Scheduler
```cpp
#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

class IntervalScheduler {
private:
    struct Interval {
        int start;
        int end;
        std::string description;
        
        Interval(int s, int e, const std::string& desc) 
            : start(s), end(e), description(desc) {}
        
        bool operator<(const Interval& other) const {
            return end < other.end;  // Sort by end time
        }
    };
    
    std::set<Interval> m_intervals;
    
public:
    // Add interval
    bool addInterval(int start, int end, const std::string& description) {
        if (start >= end) return false;
        
        Interval interval(start, end, description);
        m_intervals.insert(interval);
        return true;
    }
    
    // Check for overlaps
    bool hasOverlap() const {
        if (m_intervals.size() < 2) return false;
        
        auto it = m_intervals.begin();
        int prev_end = it->end;
        ++it;
        
        for (; it != m_intervals.end(); ++it) {
            if (it->start < prev_end) {
                return true;  // Overlap found
            }
            prev_end = it->end;
        }
        
        return false;
    }
    
    // Get maximum non-overlapping intervals
    std::vector<Interval> getMaxNonOverlappingIntervals() const {
        std::vector<Interval> result;
        
        if (m_intervals.empty()) return result;
        
        auto it = m_intervals.begin();
        result.push_back(*it);
        int last_end = it->end;
        ++it;
        
        for (; it != m_intervals.end(); ++it) {
            if (it->start >= last_end) {
                result.push_back(*it);
                last_end = it->end;
            }
        }
        
        return result;
    }
    
    // Get intervals overlapping with given interval
    std::vector<Interval> getOverlappingIntervals(int start, int end) const {
        std::vector<Interval> result;
        
        for (const auto& interval : m_intervals) {
            if (!(interval.end <= start || interval.start >= end)) {
                result.push_back(interval);
            }
        }
        
        return result;
    }
    
    // Get intervals in time range
    std::vector<Interval> getIntervalsInRange(int start, int end) const {
        std::vector<Interval> result;
        
        Interval start_bound(start, start, "");
        Interval end_bound(end, end, "");
        
        auto lower = m_intervals.lower_bound(start_bound);
        auto upper = m_intervals.upper_bound(end_bound);
        
        for (auto it = lower; it != upper; ++it) {
            result.push_back(*it);
        }
        
        return result;
    }
    
    // Find gaps in schedule
    std::vector<std::pair<int, int>> findGaps(int day_start = 0, int day_end = 24) const {
        std::vector<std::pair<int, int>> gaps;
        
        if (m_intervals.empty()) {
            gaps.emplace_back(day_start, day_end);
            return gaps;
        }
        
        // Gap before first interval
        auto first = m_intervals.begin();
        if (first->start > day_start) {
            gaps.emplace_back(day_start, first->start);
        }
        
        // Gaps between intervals
        auto prev = m_intervals.begin();
        auto curr = std::next(m_intervals.begin());
        
        for (; curr != m_intervals.end(); ++prev, ++curr) {
            if (curr->start > prev->end) {
                gaps.emplace_back(prev->end, curr->start);
            }
        }
        
        // Gap after last interval
        auto last = std::prev(m_intervals.end());
        if (last->end < day_end) {
            gaps.emplace_back(last->end, day_end);
        }
        
        return gaps;
    }
    
    // Display schedule
    void displaySchedule() const {
        std::cout << "\nSchedule (" << m_intervals.size() << " intervals):" << std::endl;
        for (const auto& interval : m_intervals) {
            std::cout << "[" << interval.start << ":00 - " << interval.end << ":00] " 
                      << interval.description << std::endl;
        }
    }
    
    // Display optimal schedule
    void displayOptimalSchedule() const {
        auto optimal = getMaxNonOverlappingIntervals();
        std::cout << "\nOptimal Schedule (" << optimal.size() << " intervals):" << std::endl;
        for (const auto& interval : optimal) {
            std::cout << "[" << interval.start << ":00 - " << interval.end << ":00] " 
                      << interval.description << std::endl;
        }
    }
    
    // Display gaps
    void displayGaps() const {
        auto gaps = findGaps();
        std::cout << "\nAvailable Gaps:" << std::endl;
        for (const auto& gap : gaps) {
            std::cout << "[" << gap.first << ":00 - " << gap.second << ":00]" << std::endl;
        }
    }
};

int main() {
    IntervalScheduler scheduler;
    
    // Add intervals
    scheduler.addInterval(9, 11, "Team Meeting");
    scheduler.addInterval(10, 12, "Project Review");  // Overlaps with Team Meeting
    scheduler.addInterval(13, 15, "Client Call");
    scheduler.addInterval(14, 16, "Code Review");    // Overlaps with Client Call
    scheduler.addInterval(16, 17, "Documentation");
    scheduler.addInterval(18, 19, "Planning Session");
    
    scheduler.displaySchedule();
    
    // Check for overlaps
    std::cout << "\nSchedule has overlaps: " << (scheduler.hasOverlap() ? "Yes" : "No") << std::endl;
    
    // Show optimal schedule
    scheduler.displayOptimalSchedule();
    
    // Show available gaps
    scheduler.displayGaps();
    
    // Find intervals in specific range
    std::cout << "\n=== Intervals between 10:00 and 16:00 ===" << std::endl;
    auto range_intervals = scheduler.getIntervalsInRange(10, 16);
    for (const auto& interval : range_intervals) {
        std::cout << "[" << interval.start << ":00 - " << interval.end << ":00] " 
                  << interval.description << std::endl;
    }
    
    // Find overlapping intervals for a new meeting
    std::cout << "\n=== Checking overlap for 14:00-15:00 ===" << std::endl;
    auto overlapping = scheduler.getOverlappingIntervals(14, 15);
    if (overlapping.empty()) {
        std::cout << "No overlaps found" << std::endl;
    } else {
        std::cout << "Overlaps with:" << std::endl;
        for (const auto& interval : overlapping) {
            std::cout << "[" << interval.start << ":00 - " << interval.end << ":00] " 
                      << interval.description << std::endl;
        }
    }
    
    return 0;
}
```

### Example 3: Word Frequency Counter
```cpp
#include <iostream>
#include <set>
#include <map>
#include <string>
#include <fstream>
#include <algorithm>
#include <cctype>

class WordFrequencyCounter {
private:
    struct WordInfo {
        std::string word;
        size_t frequency;
        size_t first_position;
        
        WordInfo(const std::string& w, size_t pos) 
            : word(w), frequency(1), first_position(pos) {}
        
        bool operator<(const WordInfo& other) const {
            if (frequency != other.frequency) {
                return frequency > other.frequency;  // Sort by frequency descending
            }
            return word < other.word;  // Then alphabetically
        }
    };
    
    std::map<std::string, size_t> m_word_counts;
    std::map<std::string, size_t> m_word_positions;
    std::set<WordInfo> m_sorted_words;
    
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
    // Process text
    void processText(const std::string& text) {
        std::string current_word;
        size_t position = 0;
        
        for (char c : text) {
            if (std::isalpha(c)) {
                current_word += c;
            } else if (!current_word.empty()) {
                addWord(current_word, position);
                current_word.clear();
            }
            position++;
        }
        
        if (!current_word.empty()) {
            addWord(current_word, position);
        }
    }
    
    // Process file
    bool processFile(const std::string& filename) {
        std::ifstream file(filename);
        if (!file.is_open()) {
            std::cerr << "Cannot open file: " << filename << std::endl;
            return false;
        }
        
        std::string word;
        size_t position = 0;
        
        while (file >> word) {
            addWord(word, position);
            position += word.length() + 1;  // +1 for space
        }
        
        return true;
    }
    
    // Add word
    void addWord(const std::string& word, size_t position) {
        std::string normalized = normalizeWord(word);
        if (normalized.empty()) return;
        
        auto it = m_word_counts.find(normalized);
        if (it == m_word_counts.end()) {
            m_word_counts[normalized] = 1;
            m_word_positions[normalized] = position;
        } else {
            it->second++;
        }
    }
    
    // Build sorted set
    void buildSortedSet() {
        m_sorted_words.clear();
        
        for (const auto& pair : m_word_counts) {
            WordInfo info(pair.first, m_word_positions[pair.first]);
            info.frequency = pair.second;
            m_sorted_words.insert(info);
        }
    }
    
    // Get top N words
    std::vector<WordInfo> getTopWords(size_t n) const {
        std::vector<WordInfo> result;
        auto it = m_sorted_words.begin();
        
        for (size_t i = 0; i < std::min(n, m_sorted_words.size()); ++i) {
            result.push_back(*it++);
        }
        
        return result;
    }
    
    // Get words with specific frequency
    std::vector<WordInfo> getWordsWithFrequency(size_t frequency) const {
        std::vector<WordInfo> result;
        
        for (const auto& word_info : m_sorted_words) {
            if (word_info.frequency == frequency) {
                result.push_back(word_info);
            }
        }
        
        return result;
    }
    
    // Get words in alphabetical order
    std::vector<std::string> getWordsAlphabetical() const {
        std::vector<std::string> result;
        
        for (const auto& pair : m_word_counts) {
            result.push_back(pair.first);
        }
        
        std::sort(result.begin(), result.end());
        return result;
    }
    
    // Get statistics
    struct Statistics {
        size_t total_words;
        size_t unique_words;
        size_t most_frequent_count;
        std::string most_frequent_word;
        double average_frequency;
    };
    
    Statistics getStatistics() const {
        Statistics stats = {0, 0, 0, "", 0.0};
        
        stats.total_words = 0;
        stats.unique_words = m_word_counts.size();
        
        if (m_word_counts.empty()) return stats;
        
        size_t max_count = 0;
        for (const auto& pair : m_word_counts) {
            stats.total_words += pair.second;
            if (pair.second > max_count) {
                max_count = pair.second;
                stats.most_frequent_word = pair.first;
            }
        }
        
        stats.most_frequent_count = max_count;
        stats.average_frequency = static_cast<double>(stats.total_words) / stats.unique_words;
        
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
        std::cout << "Average frequency: " << std::fixed << std::setprecision(2) 
                  << stats.average_frequency << std::endl;
        
        std::cout << "\n=== Top " << top_n << " Most Frequent Words ===" << std::endl;
        auto top_words = getTopWords(top_n);
        for (size_t i = 0; i < top_words.size(); ++i) {
            std::cout << (i + 1) << ". " << top_words[i].word 
                      << " (" << top_words[i].frequency << " times)" << std::endl;
        }
    }
    
    // Display words that appear exactly once
    void displayUniqueWords() const {
        auto unique_words = getWordsWithFrequency(1);
        std::cout << "\n=== Words That Appear Once (" << unique_words.size() << ") ===" << std::endl;
        for (const auto& word_info : unique_words) {
            std::cout << word_info.word << std::endl;
        }
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
    counter.buildSortedSet();
    
    counter.displayResults(10);
    counter.displayUniqueWords();
    
    // Show alphabetical order
    std::cout << "\n=== Words in Alphabetical Order ===" << std::endl;
    auto alphabetical = counter.getWordsAlphabetical();
    for (const auto& word : alphabetical) {
        std::cout << word << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
```

### Example 4: Range Query System
```cpp
#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
#include <random>

class RangeQuerySystem {
private:
    struct Point {
        int x, y;
        int id;
        
        Point(int x_coord, int y_coord, int point_id) 
            : x(x_coord), y(y_coord), id(point_id) {}
        
        bool operator<(const Point& other) const {
            if (x != other.x) return x < other.x;
            return y < other.y;
        }
    };
    
    std::set<Point> m_points;
    
public:
    // Add point
    int addPoint(int x, int y) {
        static int next_id = 1;
        Point point(x, y, next_id++);
        m_points.insert(point);
        return point.id;
    }
    
    // Remove point by ID
    bool removePoint(int id) {
        auto it = std::find_if(m_points.begin(), m_points.end(),
                              [id](const Point& p) { return p.id == id; });
        
        if (it != m_points.end()) {
            m_points.erase(it);
            return true;
        }
        return false;
    }
    
    // Query points in rectangle [x1, x2] x [y1, y2]
    std::vector<Point> queryRectangle(int x1, int y1, int x2, int y2) const {
        std::vector<Point> result;
        
        if (x1 > x2) std::swap(x1, x2);
        if (y1 > y2) std::swap(y1, y2);
        
        // Find points with x in range
        Point min_point(x1, y1, 0);
        Point max_point(x2, y2, INT_MAX);
        
        auto lower = m_points.lower_bound(min_point);
        auto upper = m_points.upper_bound(max_point);
        
        for (auto it = lower; it != upper; ++it) {
            if (it->y >= y1 && it->y <= y2) {
                result.push_back(*it);
            }
        }
        
        return result;
    }
    
    // Query points in circle (center, radius)
    std::vector<Point> queryCircle(int center_x, int center_y, int radius) const {
        std::vector<Point> result;
        int radius_sq = radius * radius;
        
        // Check all points (inefficient but simple)
        for (const auto& point : m_points) {
            int dx = point.x - center_x;
            int dy = point.y - center_y;
            if (dx * dx + dy * dy <= radius_sq) {
                result.push_back(point);
            }
        }
        
        return result;
    }
    
    // Find nearest neighbor
    std::optional<Point> findNearest(int x, int y) const {
        if (m_points.empty()) return std::nullopt;
        
        Point target(x, y, 0);
        auto it = m_points.lower_bound(target);
        
        Point nearest = *m_points.begin();
        int min_dist_sq = (nearest.x - x) * (nearest.x - x) + 
                         (nearest.y - y) * (nearest.y - y);
        
        // Check nearby points
        for (auto check_it = it; check_it != m_points.end() && 
             std::abs(check_it->x - x) <= min_dist_sq; ++check_it) {
            int dist_sq = (check_it->x - x) * (check_it->x - x) + 
                         (check_it->y - y) * (check_it->y - y);
            if (dist_sq < min_dist_sq) {
                min_dist_sq = dist_sq;
                nearest = *check_it;
            }
        }
        
        // Check points before
        for (auto check_it = it; check_it != m_points.begin(); ) {
            --check_it;
            if (std::abs(check_it->x - x) > min_dist_sq) break;
            
            int dist_sq = (check_it->x - x) * (check_it->x - x) + 
                         (check_it->y - y) * (check_it->y - y);
            if (dist_sq < min_dist_sq) {
                min_dist_sq = dist_sq;
                nearest = *check_it;
            }
        }
        
        return nearest;
    }
    
    // Get convex hull (simplified)
    std::vector<Point> getConvexHull() const {
        std::vector<Point> points(m_points.begin(), m_points.end());
        
        if (points.size() < 3) return points;
        
        // Sort by x, then y
        std::sort(points.begin(), points.end());
        
        // Build lower hull
        std::vector<Point> lower;
        for (const auto& p : points) {
            while (lower.size() >= 2) {
                auto last = lower.back();
                lower.pop_back();
                auto second_last = lower.back();
                
                // Cross product
                int cross = (last.x - second_last.x) * (p.y - second_last.y) -
                           (last.y - second_last.y) * (p.x - second_last.x);
                
                if (cross <= 0) {
                    lower.push_back(last);
                    break;
                }
            }
            lower.push_back(p);
        }
        
        // Build upper hull
        std::vector<Point> upper;
        for (auto it = points.rbegin(); it != points.rend(); ++it) {
            while (upper.size() >= 2) {
                auto last = upper.back();
                upper.pop_back();
                auto second_last = upper.back();
                
                int cross = (last.x - second_last.x) * (it->y - second_last.y) -
                           (last.y - second_last.y) * (it->x - second_last.x);
                
                if (cross <= 0) {
                    upper.push_back(last);
                    break;
                }
            }
            upper.push_back(*it);
        }
        
        // Combine hulls
        lower.pop_back();
        upper.pop_back();
        lower.insert(lower.end(), upper.begin(), upper.end());
        
        return lower;
    }
    
    // Display all points
    void displayPoints() const {
        std::cout << "\nPoints (" << m_points.size() << "):" << std::endl;
        for (const auto& point : m_points) {
            std::cout << "ID " << point.id << ": (" << point.x << ", " << point.y << ")" << std::endl;
        }
    }
    
    // Display query results
    void displayQueryResults(const std::vector<Point>& results, const std::string& query_type) const {
        std::cout << "\n" << query_type << " (" << results.size() << " points):" << std::endl;
        for (const auto& point : results) {
            std::cout << "ID " << point.id << ": (" << point.x << ", " << point.y << ")" << std::endl;
        }
    }
};

int main() {
    RangeQuerySystem rqs;
    
    // Generate random points
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(-10, 10);
    
    std::cout << "=== Adding Random Points ===" << std::endl;
    for (int i = 0; i < 20; ++i) {
        int x = dis(gen);
        int y = dis(gen);
        int id = rqs.addPoint(x, y);
        std::cout << "Added point " << id << ": (" << x << ", " << y << ")" << std::endl;
    }
    
    rqs.displayPoints();
    
    // Rectangle query
    std::cout << "\n=== Rectangle Query ===" << std::endl;
    auto rect_results = rqs.queryRectangle(-5, -5, 5, 5);
    rqs.displayQueryResults(rect_results, "Points in rectangle [-5,5] x [-5,5]");
    
    // Circle query
    std::cout << "\n=== Circle Query ===" << std::endl;
    auto circle_results = rqs.queryCircle(0, 0, 7);
    rqs.displayQueryResults(circle_results, "Points in circle (0,0) radius 7");
    
    // Nearest neighbor
    std::cout << "\n=== Nearest Neighbor ===" << std::endl;
    auto nearest = rqs.findNearest(3, 4);
    if (nearest) {
        std::cout << "Nearest to (3,4): ID " << nearest->id 
                  << " (" << nearest->x << ", " << nearest->y << ")" << std::endl;
    }
    
    // Convex hull
    std::cout << "\n=== Convex Hull ===" << std::endl;
    auto hull = rqs.getConvexHull();
    std::cout << "Convex hull vertices (" << hull.size() << "):" << std::endl;
    for (const auto& point : hull) {
        std::cout << "ID " << point.id << ": (" << point.x << ", " << point.y << ")" << std::endl;
    }
    
    return 0;
}
```

## 📊 Complete Function Reference

### Modifiers
| Function | Description | Complexity |
|----------|-------------|------------|
| `insert()` | Insert element(s) | O(log n) |
| `erase()` | Remove element(s) | O(log n) |
| `clear()` | Remove all elements | O(n) |
| `swap()` | Swap contents | O(1) |

### Lookup Operations
| Function | Description | Complexity |
|----------|-------------|------------|
| `find()` | Find element | O(log n) |
| `count()` | Count occurrences | O(log n) |
| `lower_bound()` | First element >= value | O(log n) |
| `upper_bound()` | First element > value | O(log n) |
| `equal_range()` | Range of equal elements | O(log n) |

### Capacity
| Function | Description | Complexity |
|----------|-------------|------------|
| `size()` | Number of elements | O(1) |
| `empty()` | Check if empty | O(1) |
| `max_size()` | Maximum possible size | O(1) |

### Iterators
| Function | Description |
|----------|-------------|
| `begin()/cbegin()` | Beginning iterator |
| `end()/cend()` | End iterator |
| `rbegin()/crbegin()` | Reverse beginning |
| `rend()/crend()` | Reverse end |

## ⚡ Performance Considerations

### Memory Layout
```cpp
// Set uses balanced binary tree (Red-Black Tree)
// Each node contains: value, color, parent, left, right pointers
// Logarithmic height guarantees O(log n) operations

std::set<int> s = {1, 2, 3, 4, 5};
// Internal structure (simplified):
//       3(black)
//      /       \
//   2(red)    4(red)
//   /           \
// 1(black)     5(black)
```

### Iterator Invalidation
```cpp
// Set iterators remain valid except for erased elements
std::set<int> s = {1, 2, 3, 4, 5};
auto it = s.find(3);

s.insert(6);    // it still valid
s.erase(1);     // it still valid
s.erase(3);     // it becomes invalid
```

## 🎯 Common Patterns

### Pattern 1: Unique Collection with Ordering
```cpp
class UniqueSortedList {
private:
    std::set<int> m_data;
    
public:
    void add(int value) {
        m_data.insert(value);  // Automatically handles duplicates
    }
    
    bool contains(int value) const {
        return m_data.find(value) != m_data.end();
    }
    
    std::vector<int> getSorted() const {
        return std::vector<int>(m_data.begin(), m_data.end());
    }
};
```

### Pattern 2: Range Queries
```cpp
class RangeIndex {
private:
    std::set<int> m_values;
    
public:
    std::vector<int> getRange(int min_val, int max_val) {
        std::vector<int> result;
        auto lower = m_values.lower_bound(min_val);
        auto upper = m_values.upper_bound(max_val);
        
        for (auto it = lower; it != upper; ++it) {
            result.push_back(*it);
        }
        
        return result;
    }
};
```

## 🐛 Common Pitfalls & Solutions

### 1. Modifying Elements
```cpp
// Problem
std::set<int> s = {1, 2, 3};
*it = 10;  // Error: set elements are const

// Solution
s.erase(it);
s.insert(10);
```

### 2. Performance with Large Objects
```cpp
// Problem - copying large objects
std::set<LargeObject> s;  // Expensive copies

// Solution - use pointers or move semantics
std::set<std::unique_ptr<LargeObject>> s;
// or
s.insert(std::move(obj));
```

### 3. Custom Comparator Issues
```cpp
// Problem - inconsistent comparator
struct BadComparator {
    bool operator()(int a, int b) const {
        return a < b;  // OK
        // But missing equality case handling
    }
};

// Solution - ensure strict weak ordering
struct GoodComparator {
    bool operator()(int a, int b) const {
        return a < b;
    }
};
```

## 📚 Related Headers

- `unordered_set.md` - Hash-based unique container
- `map.md` - Ordered key-value pairs
- `unordered_map.md` - Hash-based key-value pairs
- `algorithm.md` - Set operations algorithms

## 🚀 Best Practices

1. **Use set** when you need unique, ordered elements
2. **Use unordered_set** for better performance when order doesn't matter
3. **Leverage range operations** for efficient queries
4. **Consider memory overhead** for large objects
5. **Use emplace()** for in-place construction
6. **Prefer set algorithms** for set operations

## 🎯 When to Use set

✅ **Use set when:**
- Need unique elements
- Elements must be sorted
- Frequent range queries
- Need ordered iteration
- Logarithmic performance is acceptable

❌ **Avoid when:**
- Need constant-time lookup (use `unordered_set`)
- Order doesn't matter (use `unordered_set`)
- Duplicates are allowed (use `multiset`)
- Need random access (use `vector`)

---

**Examples in this file**: 4 complete programs  
**Key Functions**: `insert()`, `find()`, `erase()`, `lower_bound()`, `upper_bound()`  
**Time Complexity**: O(log n) for most operations  
**Space Complexity**: O(n) where n is number of elements
