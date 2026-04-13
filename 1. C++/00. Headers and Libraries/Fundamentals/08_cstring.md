# 08_cstring.md - C-Style String Library

The `cstring` header provides functions for working with C-style null-terminated strings and memory operations. It's the C++ version of the C library `<string.h>`.

## 📖 Overview

`cstring` contains functions for manipulating character arrays that are terminated by a null character (`'\0'`). While `std::string` is preferred in modern C++, these functions are essential when working with C APIs, legacy code, or performance-critical operations.

## 🎯 Key Categories

1. **String Operations** - Copy, concatenate, compare strings
2. **String Searching** - Find characters and substrings
3. **Memory Operations** - Raw memory manipulation
4. **String Analysis** - Length, tokenization

## 🔧 String Operations

### String Length and Copying
```cpp
#include <cstring>
#include <iostream>
#include <vector>

int main() {
    // String length
    const char* text = "Hello, World!";
    size_t length = std::strlen(text);
    std::cout << "Length: " << length << std::endl;  // 13
    
    // Safe string copying
    char destination[50];
    const char* source = "Safe copy example";
    
    std::strncpy(destination, source, sizeof(destination) - 1);
    destination[sizeof(destination) - 1] = '\0';  // Ensure null termination
    
    std::cout << "Copied: " << destination << std::endl;
    
    return 0;
}
```

### String Concatenation
```cpp
void demonstrateConcatenation() {
    char buffer[100] = "Hello";
    const char* suffix = " World!";
    
    // Check if we have enough space
    if (std::strlen(buffer) + std::strlen(suffix) < sizeof(buffer)) {
        std::strcat(buffer, suffix);
        std::cout << "Concatenated: " << buffer << std::endl;
    } else {
        std::cout << "Not enough space for concatenation!" << std::endl;
    }
    
    // Safe concatenation with bounds checking
    char buffer2[100] = "Hello";
    const char* suffix2 = " Safe World!";
    
    std::strncat(buffer2, suffix2, sizeof(buffer2) - std::strlen(buffer2) - 1);
    std::cout << "Safe concatenation: " << buffer2 << std::endl;
}
```

### String Comparison
```cpp
void demonstrateComparison() {
    const char* str1 = "Apple";
    const char* str2 = "Banana";
    const char* str3 = "Apple";
    
    // String comparison
    int result1 = std::strcmp(str1, str2);  // Negative (str1 < str2)
    int result2 = std::strcmp(str1, str3);  // Zero (equal)
    int result3 = std::strcmp(str2, str1);  // Positive (str2 > str1)
    
    std::cout << "strcmp(\"Apple\", \"Banana\"): " << result1 << std::endl;
    std::cout << "strcmp(\"Apple\", \"Apple\"): " << result2 << std::endl;
    std::cout << "strcmp(\"Banana\", \"Apple\"): " << result3 << std::endl;
    
    // Limited comparison
    const char* str4 = "Apple Pie";
    const char* str5 = "Apple Cake";
    
    int result4 = std::strncmp(str4, str5, 5);  // Compare first 5 characters
    std::cout << "strncmp(\"Apple Pie\", \"Apple Cake\", 5): " << result4 << std::endl;
    
    // Case-insensitive comparison (non-standard but common)
    #ifdef _MSC_VER
    int result5 = _strcmpi(str1, str2);
    #else
    int result5 = strcasecmp(str1, str2);
    #endif
}
```

## 🔧 String Searching

### Character and Substring Search
```cpp
void demonstrateSearching() {
    const char* text = "Hello, World! Hello again!";
    
    // Find first occurrence of character
    const char* first_h = std::strchr(text, 'H');
    if (first_h) {
        std::cout << "First 'H' at position: " << (first_h - text) << std::endl;
    }
    
    // Find last occurrence of character
    const char* last_h = std::strrchr(text, 'H');
    if (last_h) {
        std::cout << "Last 'H' at position: " << (last_h - text) << std::endl;
    }
    
    // Find substring
    const char* substring = std::strstr(text, "World");
    if (substring) {
        std::cout << "Found 'World' at position: " << (substring - text) << std::endl;
    }
    
    // Find first character from set
    const char* charset = "aeiou";
    const char* first_vowel = std::strpbrk(text, charset);
    if (first_vowel) {
        std::cout << "First vowel: " << *first_vowel << " at position: " 
                  << (first_vowel - text) << std::endl;
    }
}
```

## 🔧 Memory Operations

### Memory Manipulation
```cpp
void demonstrateMemoryOperations() {
    // Memory set
    char buffer[100];
    std::memset(buffer, 0, sizeof(buffer));  // Fill with zeros
    std::cout << "Buffer after memset: " << (buffer[0] ? "Not zero" : "Zero") << std::endl;
    
    // Memory copy
    char source[] = "Memory copy example";
    char destination[50];
    
    std::memcpy(destination, source, std::strlen(source) + 1);  // +1 for null terminator
    std::cout << "Copied: " << destination << std::endl;
    
    // Memory move (handles overlapping regions)
    char buffer2[] = "Hello World";
    std::memmove(buffer2 + 6, buffer2, 5);  // Move "Hello" after space
    std::cout << "After memmove: " << buffer2 << std::endl;
    
    // Memory compare
    char data1[] = {1, 2, 3, 4, 5};
    char data2[] = {1, 2, 3, 4, 6};
    
    int cmp_result = std::memcmp(data1, data2, 5);
    std::cout << "Memory comparison result: " << cmp_result << std::endl;
}
```

## 🎮 Practical Examples

### Example 1: Safe String Class Wrapper
```cpp
#include <cstring>
#include <iostream>
#include <stdexcept>

class SafeString {
private:
    char* m_data;
    size_t m_capacity;
    
public:
    // Constructor
    SafeString(const char* str = "") {
        size_t len = std::strlen(str);
        m_capacity = len + 1;
        m_data = new char[m_capacity];
        std::strcpy(m_data, str);
    }
    
    // Copy constructor
    SafeString(const SafeString& other) {
        m_capacity = other.m_capacity;
        m_data = new char[m_capacity];
        std::strcpy(m_data, other.m_data);
    }
    
    // Destructor
    ~SafeString() {
        delete[] m_data;
    }
    
    // Assignment operator
    SafeString& operator=(const SafeString& other) {
        if (this != &other) {
            delete[] m_data;
            m_capacity = other.m_capacity;
            m_data = new char[m_capacity];
            std::strcpy(m_data, other.m_data);
        }
        return *this;
    }
    
    // Concatenation
    SafeString operator+(const SafeString& other) const {
        SafeString result;
        delete[] result.m_data;
        
        result.m_capacity = std::strlen(m_data) + std::strlen(other.m_data) + 1;
        result.m_data = new char[result.m_capacity];
        
        std::strcpy(result.m_data, m_data);
        std::strcat(result.m_data, other.m_data);
        
        return result;
    }
    
    // Get C-style string
    const char* c_str() const {
        return m_data;
    }
    
    // Get length
    size_t length() const {
        return std::strlen(m_data);
    }
    
    // Find substring
    int find(const char* substr) const {
        const char* found = std::strstr(m_data, substr);
        return found ? (found - m_data) : -1;
    }
    
    // Display
    void display() const {
        std::cout << "SafeString(\"" << m_data << "\")" << std::endl;
    }
};

int main() {
    SafeString s1("Hello");
    SafeString s2(" World");
    
    SafeString s3 = s1 + s2;
    s3.display();
    
    std::cout << "Length: " << s3.length() << std::endl;
    std::cout << "Find 'World': " << s3.find("World") << std::endl;
    
    return 0;
}
```

### Example 2: String Tokenizer
```cpp
#include <cstring>
#include <iostream>
#include <vector>
#include <string>

class Tokenizer {
public:
    static std::vector<std::string> tokenize(char* str, const char* delimiters) {
        std::vector<std::string> tokens;
        char* token = std::strtok(str, delimiters);
        
        while (token != nullptr) {
            tokens.emplace_back(token);
            token = std::strtok(nullptr, delimiters);
        }
        
        return tokens;
    }
    
    static std::vector<std::string> safeTokenize(const std::string& input, const char* delimiters) {
        // Create a mutable copy for strtok
        char* buffer = new char[input.length() + 1];
        std::strcpy(buffer, input.c_str());
        
        auto tokens = tokenize(buffer, delimiters);
        
        delete[] buffer;
        return tokens;
    }
    
    // Advanced tokenizer with multiple delimiter sets
    static std::vector<std::string> advancedTokenize(const std::string& input) {
        std::vector<std::string> tokens;
        char* buffer = new char[input.length() + 1];
        std::strcpy(buffer, input.c_str());
        
        // First tokenize by spaces
        char* token = std::strtok(buffer, " ");
        while (token != nullptr) {
            // Further tokenize each token by punctuation
            char* subtoken = std::strtok(token, ",.;:!?");
            while (subtoken != nullptr) {
                if (std::strlen(subtoken) > 0) {
                    tokens.emplace_back(subtoken);
                }
                subtoken = std::strtok(nullptr, ",.;:!?");
            }
            
            token = std::strtok(nullptr, " ");
        }
        
        delete[] buffer;
        return tokens;
    }
};

int main() {
    char text[] = "Hello,World;This:is!a?test";
    auto tokens1 = Tokenizer::tokenize(text, ",;:!?");
    
    std::cout << "Tokens from strtok:" << std::endl;
    for (const auto& token : tokens1) {
        std::cout << "- " << token << std::endl;
    }
    
    std::string text2 = "Hello World, this is a test";
    auto tokens2 = Tokenizer::safeTokenize(text2, " ");
    
    std::cout << "\nSafe tokenization:" << std::endl;
    for (const auto& token : tokens2) {
        std::cout << "- " << token << std::endl;
    }
    
    std::string text3 = "Hello, World! This is: a test.";
    auto tokens3 = Tokenizer::advancedTokenize(text3);
    
    std::cout << "\nAdvanced tokenization:" << std::endl;
    for (const auto& token : tokens3) {
        std::cout << "- " << token << std::endl;
    }
    
    return 0;
}
```

### Example 3: Configuration Parser
```cpp
#include <cstring>
#include <iostream>
#include <map>
#include <fstream>

class ConfigParser {
private:
    std::map<std::string, std::string> m_config;
    
    void trim(char* str) {
        // Remove leading whitespace
        char* start = str;
        while (*start && std::isspace(*start)) {
            start++;
        }
        
        if (start != str) {
            std::memmove(str, start, std::strlen(start) + 1);
        }
        
        // Remove trailing whitespace
        char* end = str + std::strlen(str) - 1;
        while (end >= str && std::isspace(*end)) {
            *end = '\0';
            end--;
        }
    }
    
public:
    bool loadFromFile(const char* filename) {
        std::ifstream file(filename);
        if (!file.is_open()) {
            std::cerr << "Cannot open config file: " << filename << std::endl;
            return false;
        }
        
        char line[256];
        while (file.getline(line, sizeof(line))) {
            // Skip empty lines and comments
            if (line[0] == '\0' || line[0] == '#') {
                continue;
            }
            
            // Find the '=' separator
            char* separator = std::strchr(line, '=');
            if (!separator) {
                continue;  // Skip invalid lines
            }
            
            *separator = '\0';  // Split the line
            char* key = line;
            char* value = separator + 1;
            
            // Trim whitespace
            trim(key);
            trim(value);
            
            m_config[std::string(key)] = std::string(value);
        }
        
        return true;
    }
    
    std::string getValue(const char* key, const std::string& defaultValue = "") const {
        auto it = m_config.find(key);
        return (it != m_config.end()) ? it->second : defaultValue;
    }
    
    int getInt(const char* key, int defaultValue = 0) const {
        std::string value = getValue(key);
        try {
            return std::stoi(value);
        } catch (...) {
            return defaultValue;
        }
    }
    
    double getDouble(const char* key, double defaultValue = 0.0) const {
        std::string value = getValue(key);
        try {
            return std::stod(value);
        } catch (...) {
            return defaultValue;
        }
    }
    
    bool getBool(const char* key, bool defaultValue = false) const {
        std::string value = getValue(key);
        std::transform(value.begin(), value.end(), value.begin(), ::tolower);
        
        if (value == "true" || value == "1" || value == "yes" || value == "on") {
            return true;
        } else if (value == "false" || value == "0" || value == "no" || value == "off") {
            return false;
        }
        
        return defaultValue;
    }
    
    void display() const {
        std::cout << "Configuration:" << std::endl;
        for (const auto& pair : m_config) {
            std::cout << "  " << pair.first << " = " << pair.second << std::endl;
        }
    }
};

int main() {
    // Create a sample config file
    const char* configContent = 
        "# Sample Configuration File\n"
        "server_host = localhost\n"
        "server_port = 8080\n"
        "debug_mode = true\n"
        "max_connections = 100\n"
        "timeout = 30.5\n"
        "# End of config\n";
    
    const char* filename = "config.txt";
    std::ofstream outFile(filename);
    outFile << configContent;
    outFile.close();
    
    ConfigParser parser;
    if (parser.loadFromFile(filename)) {
        parser.display();
        
        std::cout << "\nParsed values:" << std::endl;
        std::cout << "Server: " << parser.getValue("server_host") << std::endl;
        std::cout << "Port: " << parser.getInt("server_port") << std::endl;
        std::cout << "Debug: " << (parser.getBool("debug_mode") ? "true" : "false") << std::endl;
        std::cout << "Timeout: " << parser.getDouble("timeout") << std::endl;
    }
    
    std::remove(filename);  // Clean up
    return 0;
}
```

### Example 4: Binary Data Processor
```cpp
#include <cstring>
#include <iostream>
#include <vector>
#include <fstream>

class BinaryDataProcessor {
public:
    struct Header {
        char signature[4];
        uint32_t version;
        uint32_t dataCount;
    };
    
    struct DataRecord {
        uint32_t id;
        char name[32];
        double value;
    };
    
    bool writeBinaryFile(const char* filename, const std::vector<DataRecord>& records) {
        std::ofstream file(filename, std::ios::binary);
        if (!file.is_open()) {
            return false;
        }
        
        // Write header
        Header header;
        std::strcpy(header.signature, "BIN\0");  // 3 chars + null
        header.version = 1;
        header.dataCount = static_cast<uint32_t>(records.size());
        
        file.write(reinterpret_cast<const char*>(&header), sizeof(header));
        
        // Write data records
        for (const auto& record : records) {
            file.write(reinterpret_cast<const char*>(&record), sizeof(record));
        }
        
        return true;
    }
    
    std::vector<DataRecord> readBinaryFile(const char* filename) {
        std::vector<DataRecord> records;
        std::ifstream file(filename, std::ios::binary);
        
        if (!file.is_open()) {
            std::cerr << "Cannot open file: " << filename << std::endl;
            return records;
        }
        
        // Read header
        Header header;
        file.read(reinterpret_cast<char*>(&header), sizeof(header));
        
        // Validate signature
        if (std::strncmp(header.signature, "BIN", 3) != 0) {
            std::cerr << "Invalid file signature" << std::endl;
            return records;
        }
        
        std::cout << "File version: " << header.version << std::endl;
        std::cout << "Data count: " << header.dataCount << std::endl;
        
        // Read data records
        records.resize(header.dataCount);
        file.read(reinterpret_cast<char*>(records.data()), 
                 sizeof(DataRecord) * header.dataCount);
        
        return records;
    }
    
    void displayRecords(const std::vector<DataRecord>& records) {
        std::cout << "\nData Records:" << std::endl;
        for (const auto& record : records) {
            std::cout << "ID: " << record.id 
                      << ", Name: " << record.name 
                      << ", Value: " << record.value << std::endl;
        }
    }
};

int main() {
    BinaryDataProcessor processor;
    
    // Create sample data
    std::vector<BinaryDataProcessor::DataRecord> records = {
        {1, "Alice", 3.14},
        {2, "Bob", 2.71},
        {3, "Charlie", 1.41}
    };
    
    const char* filename = "data.bin";
    
    // Write binary file
    if (processor.writeBinaryFile(filename, records)) {
        std::cout << "Binary file written successfully" << std::endl;
    }
    
    // Read binary file
    auto readRecords = processor.readBinaryFile(filename);
    processor.displayRecords(readRecords);
    
    std::remove(filename);  // Clean up
    return 0;
}
```

## 📊 Complete Function Reference

### String Functions
| Function | Description | Safety Notes |
|----------|-------------|-------------|
| `strlen()` | Get string length | Safe |
| `strcpy()` | Copy string | Unsafe (no bounds checking) |
| `strncpy()` | Copy string with limit | Must add null terminator manually |
| `strcat()` | Concatenate strings | Unsafe (no bounds checking) |
| `strncat()` | Concatenate with limit | Safe |
| `strcmp()` | Compare strings | Safe |
| `strncmp()` | Compare strings with limit | Safe |
| `strchr()` | Find character | Safe |
| `strrchr()` | Find last character | Safe |
| `strstr()` | Find substring | Safe |
| `strpbrk()` | Find first character from set | Safe |
| `strtok()` | Tokenize string | Modifies original string |

### Memory Functions
| Function | Description | Safety Notes |
|----------|-------------|-------------|
| `memset()` | Fill memory with value | Safe |
| `memcpy()` | Copy memory block | Unsafe for overlapping regions |
| `memmove()` | Copy memory block safely | Safe for overlapping regions |
| `memcmp()` | Compare memory blocks | Safe |

## ⚡ Performance Considerations

### Efficient String Operations
```cpp
// Efficient string building
void efficientStringBuilding() {
    const char* parts[] = {"Hello", " ", "World", "!"};
    const int numParts = 4;
    
    // Calculate total length first
    size_t totalLength = 0;
    for (int i = 0; i < numParts; i++) {
        totalLength += std::strlen(parts[i]);
    }
    
    // Allocate once
    char* result = new char[totalLength + 1];
    result[0] = '\0';
    
    // Build string
    for (int i = 0; i < numParts; i++) {
        std::strcat(result, parts[i]);
    }
    
    std::cout << "Built string: " << result << std::endl;
    delete[] result;
}

// Fast memory operations
void fastMemoryOperations() {
    const size_t size = 1024;
    char* buffer1 = new char[size];
    char* buffer2 = new char[size];
    
    // Initialize with pattern
    std::memset(buffer1, 0xAA, size);
    std::memset(buffer2, 0x55, size);
    
    // Fast copy
    std::memcpy(buffer2, buffer1, size);
    
    // Verify
    if (std::memcmp(buffer1, buffer2, size) == 0) {
        std::cout << "Memory operations successful" << std::endl;
    }
    
    delete[] buffer1;
    delete[] buffer2;
}
```

## 🎯 Common Patterns

### Pattern 1: Safe String Copy
```cpp
bool safeStringCopy(char* dest, size_t destSize, const char* src) {
    if (!dest || !src || destSize == 0) {
        return false;
    }
    
    size_t srcLen = std::strlen(src);
    if (srcLen >= destSize) {
        return false;  // Not enough space
    }
    
    std::strcpy(dest, src);
    return true;
}
```

### Pattern 2: String Builder
```cpp
class StringBuilder {
private:
    char* m_buffer;
    size_t m_capacity;
    size_t m_length;
    
public:
    StringBuilder(size_t initialCapacity = 256) {
        m_capacity = initialCapacity;
        m_buffer = new char[m_capacity];
        m_buffer[0] = '\0';
        m_length = 0;
    }
    
    ~StringBuilder() {
        delete[] m_buffer;
    }
    
    bool append(const char* str) {
        size_t strLen = std::strlen(str);
        size_t needed = m_length + strLen + 1;
        
        if (needed > m_capacity) {
            size_t newCapacity = m_capacity * 2;
            while (newCapacity < needed) {
                newCapacity *= 2;
            }
            
            char* newBuffer = new char[newCapacity];
            std::strcpy(newBuffer, m_buffer);
            delete[] m_buffer;
            
            m_buffer = newBuffer;
            m_capacity = newCapacity;
        }
        
        std::strcat(m_buffer, str);
        m_length += strLen;
        return true;
    }
    
    const char* toString() const {
        return m_buffer;
    }
};
```

## 🐛 Common Pitfalls & Solutions

### 1. Buffer Overflow
```cpp
// Problem
char buffer[10];
std::strcpy(buffer, "This is too long");  // Buffer overflow!

// Solution
char buffer[10];
std::strncpy(buffer, "This is too long", sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### 2. Forgetting Null Terminator
```cpp
// Problem
char buffer[10];
std::memcpy(buffer, "Hello", 5);  // No null terminator
std::cout << std::strlen(buffer);  // Undefined behavior

// Solution
char buffer[10];
std::memcpy(buffer, "Hello", 5);
buffer[5] = '\0';  // Add null terminator
```

### 3. strtok Thread Safety
```cpp
// Problem - strtok uses static internal state
char str1[] = "token1,token2";
char str2[] = "token3,token4";
char* token1 = std::strtok(str1, ",");  // Modifies internal state
char* token2 = std::strtok(str2, ",");  // Interferes with previous call

// Solution - use strtok_r (POSIX) or make copies
```

## 📚 Related Headers

- `string.md` - Modern C++ string class
- `memory.md` - Memory management utilities
- `algorithm.md` - String algorithms

## 🚀 Best Practices

1. **Prefer `std::string`** over C-style strings in modern C++
2. **Always check buffer sizes** when using C-style string functions
3. **Use bounded functions** like `strncpy` and `strncat`
4. **Ensure null termination** after memory operations
5. **Be careful with `strtok`** - it modifies the original string
6. **Use `memmove`** instead of `memcpy` for overlapping regions

## 🎯 When to Use cstring

✅ **Use cstring when:**
- Working with C APIs
- Performance-critical string operations
- Binary data processing
- Legacy code maintenance
- Low-level memory manipulation

❌ **Avoid when:**
- Modern C++ development (use `std::string`)
- Complex string manipulation
- Unicode text processing
- Safety-critical applications
---

## Next Step

- Go to [09_utility.md](09_utility.md) to continue with utility.
