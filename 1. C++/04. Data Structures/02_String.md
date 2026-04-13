# Strings in C++

## Overview
Strings are sequences of characters used to represent text. C++ provides two types of strings: C-style strings (character arrays) and the modern `std::string` class. `std::string` is part of the STL and provides dynamic memory management, rich member functions, and safety features.

## Key Characteristics
- **Dynamic Size**: `std::string` grows automatically as needed
- **Null-terminated**: C-style strings end with `\0`; `std::string` manages this internally
- **Copyable and Assignable**: Strings can be copied, moved, and assigned
- **Rich Interface**: Provides over 100 member functions for manipulation
- **STL Compatible**: Works with algorithms, iterators, and range-based loops

---

## 1. C-Style Strings (Character Arrays)

### Theory
C-style strings are null-terminated character arrays inherited from C. They require manual memory management and are prone to buffer overflows. Understanding them is important for legacy code and low-level programming.

**Use Cases:**
- Working with legacy C code
- Embedded systems with memory constraints
- Low-level string manipulation
- When maximum performance is critical

**Limitations:**
- Manual memory management
- No bounds checking (dangerous)
- Fixed size or dynamic allocation required
- Complex operations require multiple function calls

### All Functions and Operations

```cpp
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cctype>

void demonstrateCStyleStrings() {
    std::cout << "\n========== C-STYLE STRINGS ==========\n";
    
    // ==================== DECLARATION & INITIALIZATION ====================
    std::cout << "\n--- Declaration & Initialization ---\n";
    
    // Static allocation
    char str1[20];                              // Uninitialized, 20 chars
    char str2[] = "Hello";                      // Size 6 ('H','e','l','l','o','\0')
    char str3[10] = "World";                   // Size 10, "World\0" followed by zeros
    char str4[5] = {'A', 'B', 'C', 'D', '\0'}; // Explicit null termination
    
    // Dynamic allocation
    char* dyn_str = new char[100];
    strcpy(dyn_str, "Dynamic string");
    
    // String literals (read-only)
    const char* literal = "String literal";
    // literal[0] = 's';                       // Undefined behavior - string literals are read-only
    
    // ==================== SIZE INFORMATION ====================
    std::cout << "\n--- Size Information ---\n";
    
    char str[] = "Hello, World!";
    size_t total_bytes = sizeof(str);           // Includes null terminator
    size_t length = strlen(str);                // Excludes null terminator
    size_t allocated_size = 50;
    char* buffer = new char[allocated_size];
    
    std::cout << "String: " << str << "\n";
    std::cout << "Length (strlen): " << length << "\n";
    std::cout << "Size (sizeof): " << total_bytes << " bytes\n";
    std::cout << "Allocated size: " << allocated_size << "\n";
    
    // ==================== COPYING ====================
    std::cout << "\n--- Copying ---\n";
    
    char source[] = "Hello";
    char dest1[20];
    char dest2[20];
    
    // strcpy - unsafe (no bounds checking)
    strcpy(dest1, source);
    std::cout << "strcpy result: " << dest1 << "\n";
    
    // strncpy - safer (specifies max characters)
    strncpy(dest2, source, sizeof(dest2) - 1);
    dest2[sizeof(dest2) - 1] = '\0';            // Ensure null termination
    std::cout << "strncpy result: " << dest2 << "\n";
    
    // strcpy_s (C11) - bounds checking (Windows)
    #ifdef _WIN32
    char dest3[20];
    strcpy_s(dest3, sizeof(dest3), source);
    std::cout << "strcpy_s result: " << dest3 << "\n";
    #endif
    
    // ==================== CONCATENATION ====================
    std::cout << "\n--- Concatenation ---\n";
    
    char greeting[50] = "Hello";
    char name[] = " World";
    
    // strcat - unsafe (no bounds checking)
    strcat(greeting, name);
    std::cout << "strcat result: " << greeting << "\n";
    
    // strncat - safer
    char greeting2[50] = "Hello";
    strncat(greeting2, " Beautiful World", sizeof(greeting2) - strlen(greeting2) - 1);
    std::cout << "strncat result: " << greeting2 << "\n";
    
    // ==================== COMPARISON ====================
    std::cout << "\n--- Comparison ---\n";
    
    char str_a[] = "Apple";
    char str_b[] = "Apple";
    char str_c[] = "Banana";
    
    int cmp1 = strcmp(str_a, str_b);            // 0 (equal)
    int cmp2 = strcmp(str_a, str_c);            // Negative (< 0)
    int cmp3 = strcmp(str_c, str_a);            // Positive (> 0)
    
    std::cout << "strcmp(\"Apple\", \"Apple\"): " << cmp1 << "\n";
    std::cout << "strcmp(\"Apple\", \"Banana\"): " << cmp2 << "\n";
    std::cout << "strcmp(\"Banana\", \"Apple\"): " << cmp3 << "\n";
    
    // strncmp - compare first n characters
    int cmp4 = strncmp("Apple", "Apples", 5);   // 0 (first 5 chars equal)
    std::cout << "strncmp(\"Apple\", \"Apples\", 5): " << cmp4 << "\n";
    
    // ==================== SEARCHING ====================
    std::cout << "\n--- Searching ---\n";
    
    char text[] = "The quick brown fox jumps over the lazy dog";
    
    // strchr - find first occurrence of character
    char* first_o = strchr(text, 'o');
    if (first_o) {
        std::cout << "First 'o' at position: " << (first_o - text) << "\n";
    }
    
    // strrchr - find last occurrence of character
    char* last_o = strrchr(text, 'o');
    if (last_o) {
        std::cout << "Last 'o' at position: " << (last_o - text) << "\n";
    }
    
    // strstr - find substring
    char* fox_pos = strstr(text, "fox");
    if (fox_pos) {
        std::cout << "Found 'fox' at position: " << (fox_pos - text) << "\n";
    }
    
    // ==================== TOKENIZATION ====================
    std::cout << "\n--- Tokenization ---\n";
    
    char sentence[] = "Hello,World,C++,Programming";
    char* token = strtok(sentence, ",");
    
    std::cout << "Tokens: ";
    while (token != nullptr) {
        std::cout << token << " ";
        token = strtok(nullptr, ",");
    }
    std::cout << "\n";
    
    // ==================== CONVERSION FUNCTIONS ====================
    std::cout << "\n--- Conversion Functions ---\n";
    
    // String to integer
    char num_str1[] = "123";
    char num_str2[] = "456abc";
    int num1 = atoi(num_str1);                  // 123
    int num2 = atoi(num_str2);                  // 456 (stops at non-digit)
    long num3 = atol("1234567890");
    double num4 = atof("3.14159");
    
    std::cout << "atoi(\"123\"): " << num1 << "\n";
    std::cout << "atoi(\"456abc\"): " << num2 << "\n";
    std::cout << "atof(\"3.14159\"): " << num4 << "\n";
    
    // strtol - safer conversion with error checking
    char* endptr;
    long val = strtol("123abc", &endptr, 10);
    std::cout << "strtol result: " << val << ", leftover: " << endptr << "\n";
    
    // Integer to string
    char buffer[50];
    sprintf(buffer, "%d", 42);
    std::cout << "sprintf result: " << buffer << "\n";
    
    // ==================== CHARACTER CLASSIFICATION ====================
    std::cout << "\n--- Character Classification ---\n";
    
    char test_chars[] = "A1b2c3!@#";
    
    std::cout << "Character classification:\n";
    for (int i = 0; test_chars[i] != '\0'; i++) {
        char c = test_chars[i];
        std::cout << "'" << c << "' - ";
        if (isalpha(c)) std::cout << "alpha ";
        if (isdigit(c)) std::cout << "digit ";
        if (isalnum(c)) std::cout << "alnum ";
        if (isspace(c)) std::cout << "space ";
        if (isupper(c)) std::cout << "upper ";
        if (islower(c)) std::cout << "lower ";
        if (ispunct(c)) std::cout << "punct ";
        std::cout << "\n";
    }
    
    // Case conversion
    char upper_str[] = "hello world";
    for (int i = 0; upper_str[i] != '\0'; i++) {
        upper_str[i] = toupper(upper_str[i]);
    }
    std::cout << "Uppercase: " << upper_str << "\n";
    
    // ==================== MEMORY OPERATIONS ====================
    std::cout << "\n--- Memory Operations ---\n";
    
    char mem1[20] = "Hello";
    char mem2[20];
    
    // memcpy - copy bytes
    memcpy(mem2, mem1, sizeof(mem1));
    std::cout << "memcpy result: " << mem2 << "\n";
    
    // memset - fill with value
    memset(mem2, '*', 5);
    mem2[5] = '\0';
    std::cout << "memset result: " << mem2 << "\n";
    
    // memmove - safe overlapping copy
    char overlap[] = "123456789";
    memmove(overlap + 2, overlap, 5);
    std::cout << "memmove result: " << overlap << "\n";
    
    // memcmp - compare memory blocks
    char cmp1[] = "Hello";
    char cmp2[] = "Hello";
    int mem_cmp = memcmp(cmp1, cmp2, 5);
    std::cout << "memcmp result: " << mem_cmp << "\n";
    
    // ==================== DYNAMIC STRINGS ====================
    std::cout << "\n--- Dynamic Strings ---\n";
    
    char* dynamic = new char[100];
    strcpy(dynamic, "Dynamic string");
    
    // Resize (requires new allocation)
    char* new_dynamic = new char[200];
    strcpy(new_dynamic, dynamic);
    strcat(new_dynamic, " - expanded");
    delete[] dynamic;
    dynamic = new_dynamic;
    
    std::cout << "Dynamic string: " << dynamic << "\n";
    
    // Clean up
    delete[] dynamic;
}
```

---

## 2. std::string (Modern C++ String)

### Theory
`std::string` is the modern C++ string class that provides automatic memory management, bounds checking, and a rich set of member functions. It's part of the STL and works seamlessly with algorithms and iterators.

**Advantages:**
- Automatic memory management
- Dynamic sizing
- Bounds checking with `.at()`
- Rich member functions (100+)
- STL compatible (iterators, algorithms)
- Copyable, movable, assignable
- Safe and easy to use

**When to Use:**
- Default choice for string handling in C++
- When you need dynamic strings
- When working with STL algorithms
- For text processing and manipulation
- When safety is important

### All Functions and Operations

```cpp
#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
#include <sstream>
#include <iomanip>

void demonstrateStdString() {
    std::cout << "\n========== STD::STRING ==========\n";
    
    // ==================== DECLARATION & INITIALIZATION ====================
    std::cout << "\n--- Declaration & Initialization ---\n";
    
    // Various initialization methods
    std::string s1;                                 // Empty string
    std::string s2 = "Hello";                       // Copy initialization
    std::string s3("World");                        // Direct initialization
    std::string s4(5, 'A');                         // 5 copies of 'A' → "AAAAA"
    std::string s5(s2);                             // Copy constructor
    std::string s6(std::move(s5));                  // Move constructor (C++11)
    std::string s7(s2, 1, 3);                       // Substring: from index 1, length 3 → "ell"
    std::string s8("Hello World", 5);               // First 5 chars → "Hello"
    std::string s9 = "Hello" + std::string(" World"); // Concatenation
    
    // Using string literals (C++14)
    using namespace std::string_literals;
    std::string s10 = "Hello World"s;               // std::string literal
    
    // ==================== SIZE & CAPACITY ====================
    std::cout << "\n--- Size & Capacity ---\n";
    
    std::string str = "Hello, World!";
    
    std::cout << "String: " << str << "\n";
    std::cout << "Length: " << str.length() << "\n";
    std::cout << "Size: " << str.size() << "\n";
    std::cout << "Capacity: " << str.capacity() << "\n";
    std::cout << "Max size: " << str.max_size() << "\n";
    std::cout << "Empty? " << (str.empty() ? "Yes" : "No") << "\n";
    
    // Reserve capacity
    str.reserve(100);
    std::cout << "After reserve(100) - Capacity: " << str.capacity() << "\n";
    
    // Shrink to fit
    str.shrink_to_fit();
    std::cout << "After shrink_to_fit - Capacity: " << str.capacity() << "\n";
    
    // Resize
    str.resize(20, '*');
    std::cout << "After resize(20, '*'): " << str << "\n";
    str.resize(10);
    std::cout << "After resize(10): " << str << "\n";
    
    // Clear
    str.clear();
    std::cout << "After clear - Size: " << str.size() << ", Empty? " << (str.empty() ? "Yes" : "No") << "\n";
    
    // ==================== ACCESSING ELEMENTS ====================
    std::cout << "\n--- Accessing Elements ---\n";
    
    std::string access = "Hello";
    
    // Using operator[]
    std::cout << "access[1]: " << access[1] << "\n";
    
    // Using .at() (with bounds checking)
    try {
        std::cout << "access.at(1): " << access.at(1) << "\n";
        // std::cout << access.at(10) << "\n";      // Throws std::out_of_range
    } catch (const std::out_of_range& e) {
        std::cout << "Out of range: " << e.what() << "\n";
    }
    
    // Using .front() and .back()
    std::cout << "Front: " << access.front() << "\n";
    std::cout << "Back: " << access.back() << "\n";
    
    // Using .data() (C++11) - C-style string access
    const char* c_str = access.data();
    std::cout << "C-string: " << c_str << "\n";
    
    // ==================== MODIFYING STRINGS ====================
    std::cout << "\n--- Modifying Strings ---\n";
    
    std::string mod = "Hello";
    
    // Assignment
    mod = "World";
    std::cout << "After assignment: " << mod << "\n";
    
    // Append
    mod.append("!");
    std::cout << "After append: " << mod << "\n";
    
    mod += "!!";
    std::cout << "After +=: " << mod << "\n";
    
    mod.push_back('?');
    std::cout << "After push_back: " << mod << "\n";
    
    // Insert
    mod.insert(5, " Beautiful");
    std::cout << "After insert: " << mod << "\n";
    
    // Replace
    mod.replace(6, 9, "Amazing");
    std::cout << "After replace: " << mod << "\n";
    
    // Erase
    mod.erase(5, 8);
    std::cout << "After erase: " << mod << "\n";
    
    // Pop back (C++11)
    mod.pop_back();
    std::cout << "After pop_back: " << mod << "\n";
    
    // ==================== CONCATENATION ====================
    std::cout << "\n--- Concatenation ---\n";
    
    std::string concat1 = "Hello";
    std::string concat2 = " World";
    
    // Using + operator
    std::string result1 = concat1 + concat2;
    std::cout << "concat1 + concat2: " << result1 << "\n";
    
    // Using +=
    concat1 += concat2;
    std::cout << "concat1 += concat2: " << concat1 << "\n";
    
    // Using append
    std::string result2 = concat1.append("!");
    std::cout << "append result: " << result2 << "\n";
    
    // ==================== COMPARISON ====================
    std::cout << "\n--- Comparison ---\n";
    
    std::string comp1 = "Apple";
    std::string comp2 = "Apple";
    std::string comp3 = "Banana";
    
    // Using relational operators
    std::cout << "comp1 == comp2: " << (comp1 == comp2 ? "Yes" : "No") << "\n";
    std::cout << "comp1 == comp3: " << (comp1 == comp3 ? "Yes" : "No") << "\n";
    std::cout << "comp1 < comp3: " << (comp1 < comp3 ? "Yes" : "No") << "\n";
    std::cout << "comp1 > comp3: " << (comp1 > comp3 ? "Yes" : "No") << "\n";
    
    // Using compare() method
    int cmp = comp1.compare(comp3);
    std::cout << "compare(comp3): " << cmp << "\n";
    
    // Compare substrings
    int cmp_sub = comp1.compare(0, 3, comp3, 0, 3);  // "App" vs "Ban"
    std::cout << "compare substrings: " << cmp_sub << "\n";
    
    // ==================== SEARCHING ====================
    std::cout << "\n--- Searching ---\n";
    
    std::string text = "The quick brown fox jumps over the lazy dog";
    
    // find - find first occurrence
    size_t pos1 = text.find("fox");
    if (pos1 != std::string::npos) {
        std::cout << "Found 'fox' at index: " << pos1 << "\n";
    }
    
    // rfind - find last occurrence
    size_t pos2 = text.rfind("the");
    std::cout << "Last 'the' at index: " << pos2 << "\n";
    
    // find_first_of - find first occurrence of any character in set
    size_t pos3 = text.find_first_of("aeiou");
    std::cout << "First vowel at index: " << pos3 << " ('" << text[pos3] << "')\n";
    
    // find_last_of - find last occurrence of any character in set
    size_t pos4 = text.find_last_of("aeiou");
    std::cout << "Last vowel at index: " << pos4 << " ('" << text[pos4] << "')\n";
    
    // find_first_not_of - find first character not in set
    size_t pos5 = text.find_first_not_of("The quick ");
    std::cout << "First char not in set at index: " << pos5 << " ('" << text[pos5] << "')\n";
    
    // find_last_not_of - find last character not in set
    size_t pos6 = text.find_last_not_of("dog");
    std::cout << "Last char not in set at index: " << pos6 << " ('" << text[pos6] << "')\n";
    
    // ==================== SUBSTRINGS ====================
    std::cout << "\n--- Substrings ---\n";
    
    std::string original = "Hello, World!";
    
    // substr - extract substring
    std::string sub1 = original.substr(7, 5);        // "World"
    std::string sub2 = original.substr(7);           // "World!"
    std::string sub3 = original.substr(0, 5);        // "Hello"
    
    std::cout << "Original: " << original << "\n";
    std::cout << "substr(7,5): " << sub1 << "\n";
    std::cout << "substr(7): " << sub2 << "\n";
    std::cout << "substr(0,5): " << sub3 << "\n";
    
    // ==================== ITERATORS ====================
    std::cout << "\n--- Iterators ---\n";
    
    std::string iter_str = "Hello, World!";
    
    // Forward iteration
    std::cout << "Forward: ";
    for (auto it = iter_str.begin(); it != iter_str.end(); ++it) {
        std::cout << *it;
    }
    std::cout << "\n";
    
    // Reverse iteration
    std::cout << "Reverse: ";
    for (auto it = iter_str.rbegin(); it != iter_str.rend(); ++it) {
        std::cout << *it;
    }
    std::cout << "\n";
    
    // Range-based for loop
    std::cout << "Range-based: ";
    for (char c : iter_str) {
        std::cout << c;
    }
    std::cout << "\n";
    
    // ==================== CONVERSION FUNCTIONS ====================
    std::cout << "\n--- Conversion Functions ---\n";
    
    // String to numeric
    std::string num_str1 = "123";
    std::string num_str2 = "456.789";
    std::string num_str3 = "0x1A";
    
    int int_val = std::stoi(num_str1);
    long long_val = std::stol(num_str1);
    unsigned long ulong_val = std::stoul(num_str1);
    float float_val = std::stof(num_str2);
    double double_val = std::stod(num_str2);
    
    std::cout << "stoi: " << int_val << "\n";
    std::cout << "stof: " << float_val << "\n";
    
    // stoi with base
    int hex_val = std::stoi(num_str3, nullptr, 16);
    std::cout << "stoi(hex, 16): " << hex_val << "\n";
    
    // Numeric to string
    std::string int_str = std::to_string(42);
    std::string float_str = std::to_string(3.14159);
    std::string long_str = std::to_string(1234567890L);
    
    std::cout << "to_string(42): " << int_str << "\n";
    std::cout << "to_string(3.14159): " << float_str << "\n";
    
    // ==================== CASE CONVERSION ====================
    std::cout << "\n--- Case Conversion ---\n";
    
    std::string mixed = "Hello World";
    
    // Using std::transform
    std::string upper = mixed;
    std::transform(upper.begin(), upper.end(), upper.begin(), ::toupper);
    std::cout << "Uppercase: " << upper << "\n";
    
    std::string lower = mixed;
    std::transform(lower.begin(), lower.end(), lower.begin(), ::tolower);
    std::cout << "Lowercase: " << lower << "\n";
    
    // ==================== TRIMMING ====================
    std::cout << "\n--- Trimming ---\n";
    
    std::string with_spaces = "   Hello, World!   ";
    
    // Trim left
    size_t start = with_spaces.find_first_not_of(" \t\n\r");
    std::string trimmed_left = (start == std::string::npos) ? "" : with_spaces.substr(start);
    
    // Trim right
    size_t end = trimmed_left.find_last_not_of(" \t\n\r");
    std::string trimmed = (end == std::string::npos) ? "" : trimmed_left.substr(0, end + 1);
    
    std::cout << "Original: '" << with_spaces << "'\n";
    std::cout << "Trimmed: '" << trimmed << "'\n";
    
    // ==================== SPLITTING ====================
    std::cout << "\n--- Splitting ---\n";
    
    std::string csv = "apple,banana,orange,grape";
    std::string delimiter = ",";
    size_t pos = 0;
    
    std::cout << "Split tokens: ";
    while ((pos = csv.find(delimiter)) != std::string::npos) {
        std::string token = csv.substr(0, pos);
        std::cout << token << " ";
        csv.erase(0, pos + delimiter.length());
    }
    std::cout << csv << "\n";
    
    // ==================== JOINING ====================
    std::cout << "\n--- Joining ---\n";
    
    std::vector<std::string> words = {"Hello", "World", "from", "C++"};
    std::string joined;
    
    for (size_t i = 0; i < words.size(); i++) {
        if (i > 0) joined += " ";
        joined += words[i];
    }
    
    std::cout << "Joined: " << joined << "\n";
    
    // ==================== STREAM OPERATIONS ====================
    std::cout << "\n--- Stream Operations ---\n";
    
    std::stringstream ss;
    ss << "Value: " << 42 << " and PI: " << 3.14159;
    std::string stream_result = ss.str();
    std::cout << "Stringstream: " << stream_result << "\n";
    
    // Parsing with stringstream
    std::string data = "123 456 789";
    std::stringstream parser(data);
    int a, b, c;
    parser >> a >> b >> c;
    std::cout << "Parsed: " << a << ", " << b << ", " << c << "\n";
    
    // ==================== FIND AND REPLACE ====================
    std::cout << "\n--- Find and Replace ---\n";
    
    std::string text2 = "The quick brown fox jumps over the lazy dog";
    std::string search = "fox";
    std::string replace = "cat";
    
    size_t pos_replace = text2.find(search);
    if (pos_replace != std::string::npos) {
        text2.replace(pos_replace, search.length(), replace);
    }
    std::cout << "After replace: " << text2 << "\n";
    
    // Replace all occurrences
    std::string text3 = "one two three two four two five";
    std::string search_all = "two";
    std::string replace_all = "TWO";
    
    size_t pos_all = 0;
    while ((pos_all = text3.find(search_all, pos_all)) != std::string::npos) {
        text3.replace(pos_all, search_all.length(), replace_all);
        pos_all += replace_all.length();
    }
    std::cout << "Replace all: " << text3 << "\n";
    
    // ==================== FORMATTING (C++20) ====================
    std::cout << "\n--- Formatting ---\n";
    
    // Using stringstream for formatting
    std::stringstream fmt;
    fmt << std::setw(10) << std::left << "Name" 
        << std::setw(5) << "Age" << "\n";
    fmt << std::setw(10) << std::left << "Alice" 
        << std::setw(5) << 25 << "\n";
    fmt << std::setw(10) << std::left << "Bob" 
        << std::setw(5) << 30 << "\n";
    
    std::cout << "Formatted table:\n" << fmt.str();
    
    // ==================== STRING VIEW (C++17) ====================
    std::cout << "\n--- String View (C++17) ---\n";
    
    #if __cplusplus >= 201703L
    std::string large_string = "This is a very large string";
    std::string_view view(large_string.data() + 10, 5);  // View of "very "
    std::cout << "String view: " << view << "\n";
    #endif
    
    // ==================== RAW STRING LITERALS (C++11) ====================
    std::cout << "\n--- Raw String Literals ---\n";
    
    std::string raw = R"(This is a "raw" string with \n literal backslashes)";
    std::cout << "Raw string: " << raw << "\n";
    
    std::string raw_with_delimiter = R"delimiter(This contains )" and ( and )delimiter)delimiter";
    std::cout << "Raw string with delimiter: " << raw_with_delimiter << "\n";
    
    // ==================== PERFORMANCE ====================
    std::cout << "\n--- Performance Considerations ---\n";
    
    // Reserve capacity for repeated concatenation
    std::string result;
    result.reserve(1000);  // Pre-allocate to avoid reallocations
    
    for (int i = 0; i < 100; i++) {
        result += std::to_string(i) + " ";
    }
    std::cout << "Result size: " << result.size() << ", capacity: " << result.capacity() << "\n";
}
```

---

## 3. Advanced String Operations

### Theory
Advanced string operations include working with Unicode, regular expressions, and custom string algorithms. While `std::string` handles ASCII and UTF-8 well, Unicode requires additional care.

### Code Examples

```cpp
#include <iostream>
#include <string>
#include <regex>
#include <codecvt>
#include <locale>

void demonstrateAdvancedStrings() {
    std::cout << "\n========== ADVANCED STRING OPERATIONS ==========\n";
    
    // ==================== REGULAR EXPRESSIONS (C++11) ====================
    std::cout << "\n--- Regular Expressions ---\n";
    
    std::string text = "The quick brown fox jumps over the lazy dog";
    
    // Search for pattern
    std::regex word_regex("\\b\\w{3}\\b");  // 3-letter words
    std::smatch matches;
    
    std::cout << "3-letter words: ";
    auto words_begin = std::sregex_iterator(text.begin(), text.end(), word_regex);
    auto words_end = std::sregex_iterator();
    
    for (auto it = words_begin; it != words_end; ++it) {
        std::cout << it->str() << " ";
    }
    std::cout << "\n";
    
    // Replace pattern
    std::string email = "user@example.com";
    std::regex email_regex(R"((\w+)@(\w+\.\w+))");
    std::string replaced = std::regex_replace(email, email_regex, "$1@domain.$2");
    std::cout << "Email replacement: " << replaced << "\n";
    
    // Validate format
    std::regex phone_regex(R"(\d{3}-\d{3}-\d{4})");
    std::string phone1 = "123-456-7890";
    std::string phone2 = "12-345-6789";
    
    std::cout << phone1 << " is valid: " << std::regex_match(phone1, phone_regex) << "\n";
    std::cout << phone2 << " is valid: " << std::regex_match(phone2, phone_regex) << "\n";
    
    // ==================== UNICODE SUPPORT ====================
    std::cout << "\n--- Unicode Support ---\n";
    
    // UTF-8 string (C++11)
    std::string utf8 = u8"Hello 世界 🌍";
    std::cout << "UTF-8 string: " << utf8 << "\n";
    std::cout << "UTF-8 length (bytes): " << utf8.size() << "\n";
    
    // UTF-16 string (C++11)
    std::u16string utf16 = u"Hello 世界";
    std::cout << "UTF-16 length (code units): " << utf16.size() << "\n";
    
    // UTF-32 string (C++11)
    std::u32string utf32 = U"Hello 世界";
    std::cout << "UTF-32 length (code points): " << utf32.size() << "\n";
    
    // Conversion between encodings (C++11)
    std::wstring_convert<std::codecvt_utf8<char32_t>, char32_t> converter;
    std::string utf8_str = converter.to_bytes(U"Hello 世界");
    std::cout << "Converted to UTF-8: " << utf8_str << "\n";
    
    // ==================== STRING ALGORITHMS ====================
    std::cout << "\n--- Custom String Algorithms ---\n";
    
    // Palindrome check
    auto isPalindrome = [](const std::string& s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s[left] != s[right]) return false;
            left++;
            right--;
        }
        return true;
    };
    
    std::cout << "\"racecar\" is palindrome: " << isPalindrome("racecar") << "\n";
    std::cout << "\"hello\" is palindrome: " << isPalindrome("hello") << "\n";
    
    // Anagram check
    auto isAnagram = [](const std::string& s1, const std::string& s2) {
        if (s1.length() != s2.length()) return false;
        std::string sorted1 = s1;
        std::string sorted2 = s2;
        std::sort(sorted1.begin(), sorted1.end());
        std::sort(sorted2.begin(), sorted2.end());
        return sorted1 == sorted2;
    };
    
    std::cout << "\"listen\" and \"silent\" are anagrams: " 
              << isAnagram("listen", "silent") << "\n";
    
    // Longest common prefix
    auto longestCommonPrefix = [](const std::vector<std::string>& strs) {
        if (strs.empty()) return std::string();
        std::string prefix = strs[0];
        for (size_t i = 1; i < strs.size(); i++) {
            size_t j = 0;
            while (j < prefix.size() && j < strs[i].size() && prefix[j] == strs[i][j]) {
                j++;
            }
            prefix = prefix.substr(0, j);
            if (prefix.empty()) break;
        }
        return prefix;
    };
    
    std::vector<std::string> words2 = {"flower", "flow", "flight"};
    std::cout << "Longest common prefix: " << longestCommonPrefix(words2) << "\n";
    
    // ==================== STRING BUILDER PATTERN ====================
    std::cout << "\n--- StringBuilder Pattern ---\n";
    
    class StringBuilder {
    private:
        std::string buffer;
        
    public:
        StringBuilder& append(const std::string& str) {
            buffer += str;
            return *this;
        }
        
        StringBuilder& append(int num) {
            buffer += std::to_string(num);
            return *this;
        }
        
        StringBuilder& append(char c) {
            buffer += c;
            return *this;
        }
        
        StringBuilder& appendLine(const std::string& str) {
            buffer += str + "\n";
            return *this;
        }
        
        std::string toString() const {
            return buffer;
        }
        
        void clear() {
            buffer.clear();
        }
        
        size_t length() const {
            return buffer.length();
        }
    };
    
    StringBuilder sb;
    sb.append("Hello").append(", ").append(42).append("!").appendLine(" World");
    sb.append("This is a multi-line string builder");
    
    std::cout << "StringBuilder result:\n" << sb.toString() << "\n";
    std::cout << "Length: " << sb.length() << "\n";
}
```

---

## Performance Summary

| Operation | C-style String | std::string |
|-----------|---------------|-------------|
| Length | O(n) (strlen) | O(1) |
| Access | O(1) | O(1) |
| Copy | O(n) | O(n) |
| Concatenate | O(n) | O(n) |
| Find | O(n) | O(n) |
| Compare | O(n) | O(n) |
| Memory Safety | Poor | Excellent |
| Ease of Use | Poor | Excellent |

---

## Best Practices

1. **Prefer `std::string` over C-style strings** - Safer and more feature-rich
2. **Use `.reserve()` for repeated concatenation** - Avoids reallocations
3. **Use `.at()` for bounds checking** - Safer than `[]` operator
4. **Use `const auto&` in range loops** - Avoids unnecessary copying
5. **Use `std::string_view` (C++17) for read-only access** - No copying overhead
6. **Use raw string literals for paths and regex** - No escaping needed
7. **Use `std::regex` for pattern matching** - Powerful and standardized
8. **Use `std::stringstream` for complex formatting** - Flexible and type-safe
9. **Prefer `empty()` over `size() == 0`** - More readable
10. **Use `find` with `std::string::npos` for existence checks**

---

## Common Pitfalls

1. **Forgetting null terminator** - C-style strings must be null-terminated
2. **Buffer overflows** - C-style strings have no bounds checking
3. **Using `==` for C-string comparison** - Compares pointers, not content
4. **Modifying string literals** - Undefined behavior
5. **Memory leaks** - C-style strings require manual deallocation
6. **Iterator invalidation** - Modifying string may invalidate iterators
7. **Assuming `.data()` returns null-terminated** - C++11 guarantees this
8. **Unicode handling** - `std::string` works with UTF-8 but length is bytes, not characters
---

## Next Step

- Go to [03_Sequence_Container.md](03_Sequence_Container.md) to continue with Sequence Container.
