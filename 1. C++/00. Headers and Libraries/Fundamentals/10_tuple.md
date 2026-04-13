# 10_tuple.md - Fixed-Size Heterogeneous Container

The `tuple` header provides a fixed-size container that can hold elements of different types. It's an extension of `std::pair` that can handle any number of elements.

## 📖 Overview

`std::tuple` is a general-purpose container that groups multiple values of potentially different types into a single object. It's particularly useful for returning multiple values from functions and creating temporary data structures.

## 🎯 Key Features

- **Heterogeneous types** - Can store different types together
- **Fixed size** - Size determined at compile time
- **Zero overhead** - No runtime cost compared to individual variables
- **Structured bindings** - Easy unpacking (C++17)
- **Tuple concatenation** - Combine tuples

## 🔧 Basic Tuple Operations

### Creating Tuples
```cpp
#include <iostream>
#include <tuple>
#include <string>
#include <utility>

int main() {
    // Different ways to create tuples
    
    // Using make_tuple (type deduction)
    auto t1 = std::make_tuple(42, 3.14, std::string("Hello"));
    
    // Direct construction
    std::tuple<int, double, std::string> t2(100, 2.71, "World");
    
    // CTAD - Class Template Argument Deduction (C++17)
    std::tuple t3(1, 2.0, std::string("CTAD"));
    
    // Empty tuple
    std::tuple<> empty;
    
    return 0;
}
```

### Accessing Tuple Elements
```cpp
void demonstrateAccess() {
    auto person = std::make_tuple("Alice", 25, 5.6);
    
    // Access by index (compile-time)
    std::cout << "Name: " << std::get<0>(person) << std::endl;
    std::cout << "Age: " << std::get<1>(person) << std::endl;
    std::cout << "Height: " << std::get<2>(person) << std::endl;
    
    // Access by type (if type is unique)
    std::cout << "Age by type: " << std::get<int>(person) << std::endl;
    std::cout << "Name by type: " << std::get<std::string>(person) << std::endl;
    
    // Structured bindings (C++17)
    auto [name, age, height] = person;
    std::cout << "Structured binding - Name: " << name << ", Age: " << age << std::endl;
}
```

### Tuple Assignment and Comparison
```cpp
void demonstrateOperations() {
    auto t1 = std::make_tuple(1, 2, 3);
    auto t2 = std::make_tuple(1, 2, 3);
    auto t3 = std::make_tuple(1, 2, 4);
    
    // Comparison (lexicographical)
    std::cout << "t1 == t2: " << (t1 == t2) << std::endl;  // true
    std::cout << "t1 < t3: " << (t1 < t3) << std::endl;     // true
    
    // Assignment
    t1 = t3;
    std::cout << "After assignment t1 == t3: " << (t1 == t3) << std::endl;
    
    // Swap
    std::swap(t1, t2);
}
```

## 🔧 Advanced Tuple Operations

### std::tie and Unpacking
```cpp
#include <iostream>
#include <tuple>
#include <string>

void demonstrateTie() {
    auto student = std::make_tuple("John", 85, 92);
    
    // Unpack into existing variables
    std::string name;
    int mathScore, englishScore;
    
    std::tie(name, mathScore, englishScore) = student;
    
    std::cout << "Name: " << name << std::endl;
    std::cout << "Math: " << mathScore << std::endl;
    std::cout << "English: " << englishScore << std::endl;
    
    // Ignore certain values with std::ignore
    std::tie(std::ignore, mathScore, std::ignore) = student;
    std::cout << "Only math score: " << mathScore << std::endl;
}

// Function returning multiple values
std::tuple<int, int, int> calculateStats(const std::vector<int>& data) {
    if (data.empty()) {
        return {0, 0, 0};
    }
    
    int sum = 0, min_val = data[0], max_val = data[0];
    
    for (int val : data) {
        sum += val;
        min_val = std::min(min_val, val);
        max_val = std::max(max_val, val);
    }
    
    return {sum, min_val, max_val};
}

void demonstrateReturnValues() {
    std::vector<int> numbers = {5, 2, 8, 1, 9};
    
    auto [sum, min_val, max_val] = calculateStats(numbers);
    
    std::cout << "Sum: " << sum << std::endl;
    std::cout << "Min: " << min_val << std::endl;
    std::cout << "Max: " << max_val << std::endl;
}
```

### Tuple Concatenation and Manipulation
```cpp
#include <tuple>
#include <utility>

// Concatenate two tuples
template<typename... T1, typename... T2>
auto tuple_cat(const std::tuple<T1...>& t1, const std::tuple<T2...>& t2) {
    return std::tuple_cat(t1, t2);
}

void demonstrateConcatenation() {
    auto t1 = std::make_tuple(1, 2);
    auto t2 = std::make_tuple(3.14, "Hello");
    
    auto combined = std::tuple_cat(t1, t2);
    
    std::cout << "Combined tuple size: " << std::tuple_size_v<decltype(combined)> << std::endl;
    std::cout << "Elements: " << std::get<0>(combined) << ", " 
              << std::get<1>(combined) << ", "
              << std::get<2>(combined) << ", "
              << std::get<3>(combined) << std::endl;
}

// Get first N elements of a tuple
template<std::size_t N, typename... Ts>
auto tuple_head(const std::tuple<Ts...>& t) {
    return [&]<std::size_t... Is>(std::index_sequence<Is...>) {
        return std::make_tuple(std::get<Is>(t)...);
    }(std::make_index_sequence<N>{});
}

void demonstrateHead() {
    auto t = std::make_tuple(1, 2.5, "hello", true);
    
    auto head3 = tuple_head<3>(t);
    std::cout << "First 3 elements: " << std::get<0>(head3) << ", "
              << std::get<1>(head3) << ", "
              << std::get<2>(head3) << std::endl;
}
```

## 🎮 Practical Examples

### Example 1: Database Record Management
```cpp
#include <iostream>
#include <tuple>
#include <vector>
#include <string>
#include <chrono>
#include <iomanip>

class DatabaseManager {
public:
    using Record = std::tuple<int, std::string, std::string, std::chrono::system_clock::time_point>;
    using QueryResult = std::tuple<bool, std::vector<Record>, std::string>;
    
private:
    std::vector<Record> m_records;
    
public:
    // Add a record
    void addRecord(int id, const std::string& name, const std::string& email) {
        auto now = std::chrono::system_clock::now();
        m_records.emplace_back(id, name, email, now);
        std::cout << "Added record: ID=" << id << ", Name=" << name << std::endl;
    }
    
    // Find record by ID
    QueryResult findById(int id) {
        for (const auto& record : m_records) {
            if (std::get<0>(record) == id) {
                std::vector<Record> result = {record};
                return {true, result, "Record found"};
            }
        }
        return {false, {}, "Record not found"};
    }
    
    // Find records by name
    QueryResult findByName(const std::string& name) {
        std::vector<Record> results;
        
        for (const auto& record : m_records) {
            if (std::get<1>(record) == name) {
                results.push_back(record);
            }
        }
        
        if (results.empty()) {
            return {false, {}, "No records found with name: " + name};
        }
        
        return {true, results, "Found " + std::to_string(results.size()) + " records"};
    }
    
    // Display record
    void displayRecord(const Record& record) const {
        auto [id, name, email, timestamp] = record;
        
        // Convert timestamp to readable format
        auto time_t = std::chrono::system_clock::to_time_t(timestamp);
        auto tm = *std::localtime(&time_t);
        
        std::cout << "ID: " << id 
                  << ", Name: " << name 
                  << ", Email: " << email
                  << ", Created: " << std::put_time(&tm, "%Y-%m-%d %H:%M:%S")
                  << std::endl;
    }
    
    // Display all records
    void displayAll() const {
        std::cout << "\n=== All Records ===" << std::endl;
        for (const auto& record : m_records) {
            displayRecord(record);
        }
    }
    
    // Get statistics
    std::tuple<size_t, std::chrono::system_clock::time_point, std::chrono::system_clock::time_point> 
    getStatistics() const {
        if (m_records.empty()) {
            return {0, {}, {}};
        }
        
        auto oldest = std::get<3>(m_records[0]);
        auto newest = std::get<3>(m_records[0]);
        
        for (const auto& record : m_records) {
            auto timestamp = std::get<3>(record);
            oldest = std::min(oldest, timestamp);
            newest = std::max(newest, timestamp);
        }
        
        return {m_records.size(), oldest, newest};
    }
};

int main() {
    DatabaseManager db;
    
    // Add some records
    db.addRecord(1, "Alice Johnson", "alice@email.com");
    db.addRecord(2, "Bob Smith", "bob@email.com");
    db.addRecord(3, "Charlie Brown", "charlie@email.com");
    db.addRecord(4, "Alice Johnson", "alice2@email.com");  // Duplicate name
    
    db.displayAll();
    
    // Find by ID
    std::cout << "\n=== Find by ID ===" << std::endl;
    auto [found1, records1, message1] = db.findById(2);
    if (found1) {
        std::cout << message1 << ":" << std::endl;
        db.displayRecord(records1[0]);
    } else {
        std::cout << message1 << std::endl;
    }
    
    // Find by name
    std::cout << "\n=== Find by Name ===" << std::endl;
    auto [found2, records2, message2] = db.findByName("Alice Johnson");
    if (found2) {
        std::cout << message2 << ":" << std::endl;
        for (const auto& record : records2) {
            db.displayRecord(record);
        }
    } else {
        std::cout << message2 << std::endl;
    }
    
    // Get statistics
    std::cout << "\n=== Statistics ===" << std::endl;
    auto [count, oldest, newest] = db.getStatistics();
    std::cout << "Total records: " << count << std::endl;
    
    if (count > 0) {
        auto old_time = std::chrono::system_clock::to_time_t(oldest);
        auto new_time = std::chrono::system_clock::to_time_t(newest);
        
        std::cout << "Oldest: " << std::put_time(std::localtime(&old_time), "%Y-%m-%d %H:%M:%S") << std::endl;
        std::cout << "Newest: " << std::put_time(std::localtime(&new_time), "%Y-%m-%d %H:%M:%S") << std::endl;
    }
    
    return 0;
}
```

### Example 2: Mathematical Point System
```cpp
#include <iostream>
#include <tuple>
#include <vector>
#include <cmath>
#include <algorithm>

class GeometrySystem {
public:
    using Point2D = std::tuple<double, double>;
    using Point3D = std::tuple<double, double, double>;
    using Triangle = std::tuple<Point2D, Point2D, Point2D>;
    using Circle = std::tuple<Point2D, double>;
    
    // Create points
    static Point2D makePoint2D(double x, double y) {
        return {x, y};
    }
    
    static Point3D makePoint3D(double x, double y, double z) {
        return {x, y, z};
    }
    
    // Distance calculations
    static double distance(const Point2D& p1, const Point2D& p2) {
        auto [x1, y1] = p1;
        auto [x2, y2] = p2;
        return std::sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
    }
    
    static double distance3D(const Point3D& p1, const Point3D& p2) {
        auto [x1, y1, z1] = p1;
        auto [x2, y2, z2] = p2;
        return std::sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) + (z2 - z1) * (z2 - z1));
    }
    
    // Triangle operations
    static double perimeter(const Triangle& triangle) {
        const auto& [p1, p2, p3] = triangle;
        return distance(p1, p2) + distance(p2, p3) + distance(p3, p1);
    }
    
    static double area(const Triangle& triangle) {
        const auto& [p1, p2, p3] = triangle;
        auto [x1, y1] = p1;
        auto [x2, y2] = p2;
        auto [x3, y3] = p3;
        
        // Using cross product formula
        return 0.5 * std::abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1));
    }
    
    // Circle operations
    static bool pointInCircle(const Point2D& point, const Circle& circle) {
        auto [px, py] = point;
        auto [cx, cy, radius] = circle;
        return distance(point, makePoint2D(cx, cy)) <= radius;
    }
    
    static Circle circumcircle(const Triangle& triangle) {
        const auto& [p1, p2, p3] = triangle;
        auto [x1, y1] = p1;
        auto [x2, y2] = p2;
        auto [x3, y3] = p3;
        
        // Calculate circumcenter and radius
        double d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2));
        
        if (std::abs(d) < 1e-10) {
            // Points are collinear, return degenerate circle
            return {makePoint2D(0, 0), 0};
        }
        
        double ux = ((x1 * x1 + y1 * y1) * (y2 - y3) + 
                    (x2 * x2 + y2 * y2) * (y3 - y1) + 
                    (x3 * x3 + y3 * y3) * (y1 - y2)) / d;
        
        double uy = ((x1 * x1 + y1 * y1) * (x3 - x2) + 
                    (x2 * x2 + y2 * y2) * (x1 - x3) + 
                    (x3 * x3 + y3 * y3) * (x2 - x1)) / d;
        
        double radius = distance(makePoint2D(ux, uy), p1);
        
        return {makePoint2D(ux, uy), radius};
    }
    
    // Display functions
    static void displayPoint(const Point2D& p) {
        auto [x, y] = p;
        std::cout << "(" << x << ", " << y << ")";
    }
    
    static void displayPoint3D(const Point3D& p) {
        auto [x, y, z] = p;
        std::cout << "(" << x << ", " << y << ", " << z << ")";
    }
    
    static void displayTriangle(const Triangle& t) {
        const auto& [p1, p2, p3] = t;
        std::cout << "Triangle: ";
        displayPoint(p1);
        std::cout << ", ";
        displayPoint(p2);
        std::cout << ", ";
        displayPoint(p3);
        std::cout << std::endl;
    }
};

int main() {
    // 2D points
    auto p1 = GeometrySystem::makePoint2D(0, 0);
    auto p2 = GeometrySystem::makePoint2D(3, 4);
    auto p3 = GeometrySystem::makePoint2D(6, 0);
    
    std::cout << "Distance between ";
    GeometrySystem::displayPoint(p1);
    std::cout << " and ";
    GeometrySystem::displayPoint(p2);
    std::cout << ": " << GeometrySystem::distance(p1, p2) << std::endl;
    
    // Triangle operations
    GeometrySystem::Triangle triangle = {p1, p2, p3};
    GeometrySystem::displayTriangle(triangle);
    
    std::cout << "Perimeter: " << GeometrySystem::perimeter(triangle) << std::endl;
    std::cout << "Area: " << GeometrySystem::area(triangle) << std::endl;
    
    // Circle operations
    auto circle = GeometrySystem::circumcircle(triangle);
    auto [center, radius] = circle;
    
    std::cout << "Circumcircle: ";
    GeometrySystem::displayPoint(center);
    std::cout << ", radius: " << radius << std::endl;
    
    // Test point in circle
    auto testPoint = GeometrySystem::makePoint2D(2, 1);
    bool inside = GeometrySystem::pointInCircle(testPoint, circle);
    
    std::cout << "Point ";
    GeometrySystem::displayPoint(testPoint);
    std::cout << " is " << (inside ? "inside" : "outside") << " the circle" << std::endl;
    
    // 3D points
    auto p3d1 = GeometrySystem::makePoint3D(0, 0, 0);
    auto p3d2 = GeometrySystem::makePoint3D(1, 2, 2);
    
    std::cout << "\n3D distance between ";
    GeometrySystem::displayPoint3D(p3d1);
    std::cout << " and ";
    GeometrySystem::displayPoint3D(p3d2);
    std::cout << ": " << GeometrySystem::distance3D(p3d1, p3d2) << std::endl;
    
    return 0;
}
```

### Example 3: Configuration System with Variants
```cpp
#include <iostream>
#include <tuple>
#include <variant>
#include <string>
#include <map>
#include <vector>
#include <any>

class AdvancedConfig {
public:
    using ConfigValue = std::variant<int, double, std::string, bool, std::vector<int>>;
    using ConfigEntry = std::tuple<std::string, ConfigValue, std::string, bool>; // key, value, description, modified
    
private:
    std::map<std::string, ConfigEntry> m_config;
    
public:
    // Set configuration value
    template<typename T>
    void set(const std::string& key, T&& value, const std::string& description = "") {
        auto it = m_config.find(key);
        if (it != m_config.end()) {
            // Update existing
            std::get<1>(it->second) = std::forward<T>(value);
            std::get<3>(it->second) = true;  // Mark as modified
        } else {
            // Add new
            m_config[key] = std::make_tuple(key, std::forward<T>(value), description, false);
        }
    }
    
    // Get configuration value
    template<typename T>
    T get(const std::string& key, const T& defaultValue = T{}) const {
        auto it = m_config.find(key);
        if (it != m_config.end()) {
            if (auto val = std::get_if<T>(&std::get<1>(it->second))) {
                return *val;
            }
        }
        return defaultValue;
    }
    
    // Get all configuration as tuples
    std::vector<std::tuple<std::string, std::string, std::string, bool>> getAll() const {
        std::vector<std::tuple<std::string, std::string, std::string, bool>> result;
        
        for (const auto& [key, entry] : m_config) {
            const auto& [k, value, description, modified] = entry;
            
            std::string valueStr;
            std::visit([&valueStr](const auto& arg) {
                using T = std::decay_t<decltype(arg)>;
                if constexpr (std::is_same_v<T, bool>) {
                    valueStr = arg ? "true" : "false";
                } else if constexpr (std::is_same_v<T, std::vector<int>>) {
                    valueStr = "[";
                    for (size_t i = 0; i < arg.size(); ++i) {
                        valueStr += std::to_string(arg[i]);
                        if (i < arg.size() - 1) valueStr += ", ";
                    }
                    valueStr += "]";
                } else {
                    valueStr = std::to_string(arg);
                }
            }, value);
            
            result.emplace_back(k, valueStr, description, modified);
        }
        
        return result;
    }
    
    // Get modified entries
    std::vector<ConfigEntry> getModified() const {
        std::vector<ConfigEntry> modified;
        
        for (const auto& [key, entry] : m_config) {
            if (std::get<3>(entry)) {  // modified flag
                modified.push_back(entry);
            }
        }
        
        return modified;
    }
    
    // Reset all modified flags
    void resetModifiedFlags() {
        for (auto& [key, entry] : m_config) {
            std::get<3>(entry) = false;
        }
    }
    
    // Export configuration to tuple structure
    std::tuple<std::vector<std::string>, std::vector<ConfigValue>, std::vector<std::string>> 
    exportConfig() const {
        std::vector<std::string> keys;
        std::vector<ConfigValue> values;
        std::vector<std::string> descriptions;
        
        for (const auto& [key, entry] : m_config) {
            const auto& [k, value, description, modified] = entry;
            
            keys.push_back(k);
            values.push_back(value);
            descriptions.push_back(description);
        }
        
        return {keys, values, descriptions};
    }
    
    // Display configuration
    void display() const {
        auto all = getAll();
        
        std::cout << "=== Configuration ===" << std::endl;
        for (const auto& [key, value, description, modified] : all) {
            std::cout << key << " = " << value;
            if (modified) std::cout << " [MODIFIED]";
            if (!description.empty()) std::cout << " // " << description;
            std::cout << std::endl;
        }
    }
    
    // Display modified entries
    void displayModified() const {
        auto modified = getModified();
        
        if (modified.empty()) {
            std::cout << "No modified configuration entries." << std::endl;
            return;
        }
        
        std::cout << "=== Modified Entries ===" << std::endl;
        for (const auto& entry : modified) {
            const auto& [key, value, description, modifiedFlag] = entry;
            
            std::cout << key << " = ";
            std::visit([](const auto& arg) {
                using T = std::decay_t<decltype(arg)>;
                if constexpr (std::is_same_v<T, bool>) {
                    std::cout << (arg ? "true" : "false");
                } else if constexpr (std::is_same_v<T, std::vector<int>>) {
                    std::cout << "[";
                    for (size_t i = 0; i < arg.size(); ++i) {
                        std::cout << arg[i];
                        if (i < arg.size() - 1) std::cout << ", ";
                    }
                    std::cout << "]";
                } else {
                    std::cout << arg;
                }
            }, value);
            
            if (!description.empty()) std::cout << " // " << description;
            std::cout << std::endl;
        }
    }
};

int main() {
    AdvancedConfig config;
    
    // Set various configuration values
    config.set("debug", true, "Enable debug mode");
    config.set("version", 2, "Application version");
    config.set("threshold", 0.75, "Processing threshold");
    config.set("name", std::string("MyApp"), "Application name");
    config.set("allowed_ports", std::vector<int>{80, 443, 8080}, "Allowed network ports");
    
    std::cout << "Initial configuration:" << std::endl;
    config.display();
    
    // Modify some values
    config.set("debug", false);
    config.set("version", 3);
    config.set("threshold", 0.85);
    
    std::cout << "\nAfter modifications:" << std::endl;
    config.display();
    
    std::cout << "\nModified entries:" << std::endl;
    config.displayModified();
    
    // Get values
    std::cout << "\nRetrieved values:" << std::endl;
    std::cout << "Debug: " << config.get<bool>("debug") << std::endl;
    std::cout << "Version: " << config.get<int>("version") << std::endl;
    std::cout << "Threshold: " << config.get<double>("threshold") << std::endl;
    std::cout << "Name: " << config.get<std::string>("name") << std::endl;
    
    auto ports = config.get<std::vector<int>>("allowed_ports");
    std::cout << "Ports: ";
    for (int port : ports) {
        std::cout << port << " ";
    }
    std::cout << std::endl;
    
    // Export configuration
    auto [keys, values, descriptions] = config.exportConfig();
    std::cout << "\nExported configuration (" << keys.size() << " entries):" << std::endl;
    for (size_t i = 0; i < keys.size(); ++i) {
        std::cout << keys[i] << " = " << descriptions[i] << std::endl;
    }
    
    // Reset modified flags
    config.resetModifiedFlags();
    std::cout << "\nAfter resetting modified flags:" << std::endl;
    config.displayModified();
    
    return 0;
}
```

### Example 4: Function Result Processing
```cpp
#include <iostream>
#include <tuple>
#include <optional>
#include <vector>
#include <string>
#include <algorithm>

class DataProcessor {
public:
    // Process result with success/failure and data
    template<typename T>
    using ProcessResult = std::tuple<bool, T, std::string>;
    
    // Multiple return values
    using AnalysisResult = std::tuple<double, double, int, std::vector<size_t>>; // mean, std_dev, outlier_count, outlier_indices
    
private:
    std::vector<double> m_data;
    
public:
    DataProcessor(const std::vector<double>& data) : m_data(data) {}
    
    // Calculate statistics
    AnalysisResult analyze() const {
        if (m_data.empty()) {
            return {0.0, 0.0, 0, {}};
        }
        
        // Calculate mean
        double sum = 0.0;
        for (double val : m_data) {
            sum += val;
        }
        double mean = sum / m_data.size();
        
        // Calculate standard deviation
        double variance = 0.0;
        for (double val : m_data) {
            variance += (val - mean) * (val - mean);
        }
        variance /= m_data.size();
        double std_dev = std::sqrt(variance);
        
        // Find outliers (more than 2 standard deviations from mean)
        std::vector<size_t> outlier_indices;
        for (size_t i = 0; i < m_data.size(); ++i) {
            if (std::abs(m_data[i] - mean) > 2 * std_dev) {
                outlier_indices.push_back(i);
            }
        }
        
        return {mean, std_dev, static_cast<int>(outlier_indices.size()), outlier_indices};
    }
    
    // Filter data with result
    ProcessResult<std::vector<double>> filter(double min_val, double max_val) const {
        std::vector<double> filtered;
        
        for (double val : m_data) {
            if (val >= min_val && val <= max_val) {
                filtered.push_back(val);
            }
        }
        
        if (filtered.empty()) {
            return {false, {}, "No values in specified range"};
        }
        
        return {true, filtered, "Filtering successful"};
    }
    
    // Normalize data
    ProcessResult<std::vector<double>> normalize() const {
        if (m_data.empty()) {
            return {false, {}, "No data to normalize"};
        }
        
        auto [min_it, max_it] = std::minmax_element(m_data.begin(), m_data.end());
        double min_val = *min_it;
        double max_val = *max_it;
        
        if (max_val == min_val) {
            return {false, {}, "All values are the same"};
        }
        
        std::vector<double> normalized;
        normalized.reserve(m_data.size());
        
        for (double val : m_data) {
            normalized.push_back((val - min_val) / (max_val - min_val));
        }
        
        return {true, normalized, "Normalization successful"};
    }
    
    // Batch processing with multiple results
    std::tuple<ProcessResult<AnalysisResult>, ProcessResult<std::vector<double>>, ProcessResult<std::vector<double>>> 
    batchProcess(double filter_min, double filter_max) const {
        auto analysis_result = std::make_tuple(true, analyze(), "Analysis complete");
        auto filter_result = filter(filter_min, filter_max);
        auto normalize_result = normalize();
        
        return {analysis_result, filter_result, normalize_result};
    }
    
    // Display results
    void displayAnalysis(const AnalysisResult& result) const {
        auto [mean, std_dev, outlier_count, outlier_indices] = result;
        
        std::cout << "Analysis Results:" << std::endl;
        std::cout << "  Mean: " << mean << std::endl;
        std::cout << "  Std Dev: " << std_dev << std::endl;
        std::cout << "  Outliers: " << outlier_count << std::endl;
        
        if (!outlier_indices.empty()) {
            std::cout << "  Outlier indices: ";
            for (size_t idx : outlier_indices) {
                std::cout << idx << " ";
            }
            std::cout << std::endl;
        }
    }
    
    template<typename T>
    void displayProcessResult(const ProcessResult<T>& result) const {
        auto [success, data, message] = result;
        
        std::cout << "Result: " << (success ? "SUCCESS" : "FAILURE") << std::endl;
        std::cout << "Message: " << message << std::endl;
        
        if (success) {
            std::cout << "Data: ";
            if constexpr (std::is_same_v<T, std::vector<double>>) {
                for (size_t i = 0; i < data.size(); ++i) {
                    std::cout << data[i];
                    if (i < data.size() - 1) std::cout << ", ";
                }
            } else {
                std::cout << data;
            }
            std::cout << std::endl;
        }
    }
};

int main() {
    std::vector<double> data = {1.2, 2.5, 3.8, 4.1, 5.0, 15.0, 2.8, 3.2, 4.5, 5.5};
    
    DataProcessor processor(data);
    
    std::cout << "Original data: ";
    for (double val : data) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
    
    // Single analysis
    std::cout << "\n=== Single Analysis ===" << std::endl;
    auto analysis = processor.analyze();
    processor.displayAnalysis(analysis);
    
    // Single filter
    std::cout << "\n=== Filter (2.0 - 5.0) ===" << std::endl;
    auto filter_result = processor.filter(2.0, 5.0);
    processor.displayProcessResult(filter_result);
    
    // Single normalization
    std::cout << "\n=== Normalization ===" << std::endl;
    auto normalize_result = processor.normalize();
    processor.displayProcessResult(normalize_result);
    
    // Batch processing
    std::cout << "\n=== Batch Processing ===" << std::endl;
    auto [analysis_res, filter_res, normalize_res] = processor.batchProcess(2.0, 5.0);
    
    std::cout << "\nAnalysis:" << std::endl;
    processor.displayProcessResult(analysis_res);
    
    std::cout << "\nFilter:" << std::endl;
    processor.displayProcessResult(filter_res);
    
    std::cout << "\nNormalize:" << std::endl;
    processor.displayProcessResult(normalize_res);
    
    return 0;
}
```

## 📊 Complete Function Reference

### Tuple Creation
| Function | Description | Example |
|----------|-------------|---------|
| `std::make_tuple()` | Create tuple with type deduction | `auto t = make_tuple(1, "hello")` |
| `std::tuple()` | Direct construction | `tuple<int, string> t(1, "hello")` |
| `std::tuple_cat()` | Concatenate tuples | `auto t3 = tuple_cat(t1, t2)` |

### Element Access
| Function | Description | Example |
|----------|-------------|---------|
| `std::get<I>(tuple)` | Access by index | `get<0>(t)` |
| `std::get<T>(tuple)` | Access by type | `get<int>(t)` |
| `std::tie()` | Unpack to variables | `tie(a, b) = t` |
| Structured bindings | Unpack (C++17) | `auto [a, b] = t` |

### Tuple Utilities
| Function | Description | Example |
|----------|-------------|---------|
| `std::tuple_size_v<T>` | Get size | `tuple_size_v<decltype(t)>` |
| `std::tuple_element_t<I, T>` | Get element type | `tuple_element_t<0, decltype(t)>` |
| `std::forward_as_tuple()` | Forward as tuple | `forward_as_tuple(a, b)` |

## ⚡ Performance Considerations

### Compile-Time Optimization
```cpp
// Tuple operations are compile-time
// No runtime overhead compared to individual variables

// Structured bindings are optimized away
auto [x, y, z] = getTuple();  // No overhead compared to separate variables

// Use constexpr for compile-time tuple operations
constexpr auto ct = std::make_tuple(1, 2, 3);
static_assert(std::get<0>(ct) == 1);
```

### Memory Layout
```cpp
// Tuples have no additional overhead
// Elements are stored contiguously (implementation-defined)

// For better cache locality, consider struct for frequently accessed data
struct Point {
    double x, y, z;
};  // Better than tuple<double, double, double> for performance
```

## 🎯 Common Patterns

### Pattern 1: Multiple Return Values
```cpp
std::tuple<bool, int, std::string> parseInput(const std::string& input) {
    try {
        int value = std::stoi(input);
        return {true, value, ""};
    } catch (const std::exception& e) {
        return {false, 0, e.what()};
    }
}

// Usage
auto [success, value, error] = parseInput("123");
```

### Pattern 2: Function Composition
```cpp
auto process1() { return std::make_tuple(1, 2); }
auto process2(int a, int b) { return a + b; }

// Compose functions
auto [a, b] = process1();
int result = process2(a, b);
```

## 🐛 Common Pitfalls & Solutions

### 1. Type Ambiguity in get<T>()
```cpp
// Problem - duplicate types
auto t = std::make_tuple(1, 2, 3);
auto val = std::get<int>(t);  // Error: which int?

// Solution - use index
auto val = std::get<0>(t);
```

### 2. std::tie and std::ignore
```cpp
// Problem - unpacking wrong number of elements
int a, b;
std::tie(a, b) = std::make_tuple(1, 2, 3);  // Error

// Solution - use std::ignore
int a, b;
std::tie(a, b, std::ignore) = std::make_tuple(1, 2, 3);
```

### 3. Tuple Size Limits
```cpp
// Problem - too many elements
auto t = std::make_tuple(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12);  // May exceed implementation limits

// Solution - use struct or multiple tuples
struct Data {
    int a, b, c, d, e, f;
    // ...
};
```

## 📚 Related Headers

- `utility.md` - For pairs (2-element tuples)
- `variant.md` - For type-safe unions
- `any.md` - For type-erased values
- `functional.md` - For function objects

## 🚀 Best Practices

1. **Use structured bindings** (C++17) for cleaner code
2. **Prefer structs** when elements need meaningful names
3. **Keep tuples small** - avoid more than 4-5 elements
4. **Use `make_tuple`** for type deduction
5. **Use `std::tie`** with `std::ignore` for selective unpacking
6. **Consider `std::variant`** for mutually exclusive alternatives

## 🎯 When to Use tuple

✅ **Use tuple when:**
- Returning multiple values from functions
- Creating temporary data structures
- Working with generic algorithms
- Need heterogeneous container
- Implementing compile-time computations

❌ **Avoid when:**
- Elements need meaningful names (use struct)
- Many elements (consider custom type)
- Performance-critical inner loops
- Need runtime type information
---

## Next Step

- Go to [11_array.md](11_array.md) to continue with array.
