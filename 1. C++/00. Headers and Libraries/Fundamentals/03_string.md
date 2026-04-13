# string - String Handling Library

The `string` library provides a powerful and flexible way to handle text in C++. It's much safer and more convenient than C-style character arrays.

## 📖 Overview

`std::string` is a container class that encapsulates character sequences and provides numerous operations for string manipulation, comparison, and conversion.

## 🎯 Key Features

- **Dynamic sizing** - Automatically manages memory
- **Rich functionality** - Built-in methods for common operations
- **Safe operations** - Bounds checking and automatic null-termination
- **Iterator support** - Works with STL algorithms
- **Conversion support** - Easy conversion to/from numbers

## 🔧 Basic Operations

### Declaration and Initialization
```cpp
#include <string>
#include <iostream>

int main() {
    // Different ways to create strings
    
    string s1;                          // Empty string
    string s2 = "Hello";                // Direct initialization
    string s3("World");                 // Constructor
    string s4(5, 'A');                  // "AAAAA" (5 copies of 'A')
    string s5(s2);                      // Copy constructor
    string s6(s2, 1, 3);                // "ell" (substring from s2)
    string s7("C++ Strings", 0, 3);     // "C++"
    
    return 0;
}
```

### Assignment and Concatenation
```cpp
string s1, s2, s3;

s1 = "Hello";
s2 = " World";
s3 = s1 + s2;              // "Hello World"

s1 += s2;                  // Append to s1
s1.append("!!!");          // Another way to append

// String stream concatenation
string result = s1 + " " + s2 + " " + s3;
```

### Accessing Characters
```cpp
string text = "Hello World";

// Individual character access
char first = text[0];       // 'H'
char last = text.back();    // 'd'
char second = text.at(1);   // 'e' (with bounds checking)

// Modify characters
text[0] = 'J';              // "Jello World"
text.at(text.length() - 1) = '!';  // "Jello World!"
```

## 📊 String Properties

```cpp
string text = "Hello World";

cout << "Length: " << text.length() << endl;      // 11
cout << "Size: " << text.size() << endl;          // 11
cout << "Capacity: " << text.capacity() << endl;  // >= 11
cout << "Empty: " << text.empty() << endl;        // false

text.resize(15);              // Resize to 15 characters
text.reserve(20);             // Reserve capacity for 20 characters
text.shrink_to_fit();         // Reduce capacity to fit size
```

## 🎮 Practical Examples

### Example 1: Basic String Operations
```cpp
#include <iostream>
#include <string>
#include <algorithm>

int main() {
    string name;
    
    cout << "Enter your name: ";
    getline(cin, name);  // Read full line including spaces
    
    // Convert to uppercase
    string upper_name = name;
    transform(upper_name.begin(), upper_name.end(), upper_name.begin(), ::toupper);
    
    cout << "Original: " << name << endl;
    cout << "Uppercase: " << upper_name << endl;
    
    // Count vowels
    int vowels = 0;
    for (char c : name) {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
            vowels++;
        }
    }
    
    cout << "Number of vowels: " << vowels << endl;
    
    return 0;
}
```

### Example 2: String Searching and Replacement
```cpp
#include <iostream>
#include <string>

int main() {
    string text = "The quick brown fox jumps over the lazy dog";
    
    // Find substring
    size_t pos = text.find("fox");
    if (pos != string::npos) {
        cout << "Found 'fox' at position: " << pos << endl;
    }
    
    // Replace substring
    text.replace(pos, 3, "cat");
    cout << "After replacement: " << text << endl;
    
    // Find all occurrences
    string word = "the";
    pos = text.find(word);
    while (pos != string::npos) {
        cout << "Found '" << word << "' at position: " << pos << endl;
        pos = text.find(word, pos + 1);
    }
    
    return 0;
}
```

### Example 3: String Tokenization
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <sstream>

vector<string> split(const string& s, char delimiter) {
    vector<string> tokens;
    string token;
    istringstream tokenStream(s);
    
    while (getline(tokenStream, token, delimiter)) {
        tokens.push_back(token);
    }
    
    return tokens;
}

int main() {
    string sentence = "This,is,a,comma,separated,sentence";
    vector<string> words = split(sentence, ',');
    
    cout << "Words:" << endl;
    for (const string& word : words) {
        cout << "- " << word << endl;
    }
    
    return 0;
}
```

### Example 4: String Validation and Processing
```cpp
#include <iostream>
#include <string>
#include <cctype>

bool isPalindrome(const string& s) {
    int left = 0;
    int right = s.length() - 1;
    
    while (left < right) {
        // Skip non-alphanumeric characters
        while (left < right && !isalnum(s[left])) left++;
        while (left < right && !isalnum(s[right])) right--;
        
        if (tolower(s[left]) != tolower(s[right])) {
            return false;
        }
        
        left++;
        right--;
    }
    
    return true;
}

bool isValidEmail(const string& email) {
    size_t at_pos = email.find('@');
    size_t dot_pos = email.find('.');
    
    return (at_pos != string::npos && 
            dot_pos != string::npos && 
            at_pos < dot_pos &&
            at_pos > 0 &&
            dot_pos < email.length() - 1);
}

int main() {
    string text;
    
    cout << "Enter text to check for palindrome: ";
    getline(cin, text);
    
    if (isPalindrome(text)) {
        cout << "It's a palindrome!" << endl;
    } else {
        cout << "Not a palindrome." << endl;
    }
    
    string email;
    cout << "Enter email: ";
    getline(cin, email);
    
    if (isValidEmail(email)) {
        cout << "Valid email format!" << endl;
    } else {
        cout << "Invalid email format!" << endl;
    }
    
    return 0;
}
```

## ⚡ String Manipulation Functions

### Substring Operations
```cpp
string text = "Hello World";

string sub1 = text.substr(0, 5);      // "Hello"
string sub2 = text.substr(6);         // "World"
string sub3 = text.substr(3, 4);      // "lo W"
```

### Comparison Operations
```cpp
string s1 = "apple";
string s2 = "Apple";

if (s1 == s2) cout << "Equal" << endl;        // false
if (s1 != s2) cout << "Not equal" << endl;    // true
if (s1 < s2) cout << "s1 < s2" << endl;       // false (lexicographic)

// Case-insensitive comparison
if (equal(s1.begin(), s1.end(), s2.begin(), 
          [](char a, char b){ return tolower(a) == tolower(b); })) {
    cout << "Equal (case-insensitive)" << endl;
}
```

### Modification Operations
```cpp
string text = "Hello World";

text.insert(5, " Beautiful");     // "Hello Beautiful World"
text.erase(5, 10);               // "Hello World"
text.replace(6, 5, "C++");       // "Hello C++ World"

text.clear();                     // Empty string
```

## 🎯 Common String Patterns

### Pattern 1: Removing Leading/Trailing Spaces
```cpp
string trim(const string& s) {
    size_t start = s.find_first_not_of(" \t\n\r");
    if (start == string::npos) return "";
    
    size_t end = s.find_last_not_of(" \t\n\r");
    return s.substr(start, end - start + 1);
}
```

### Pattern 2: Converting to Number
```cpp
int stringToInt(const string& s) {
    try {
        return stoi(s);
    } catch (const invalid_argument&) {
        cerr << "Invalid number format!" << endl;
        return 0;
    } catch (const out_of_range&) {
        cerr << "Number out of range!" << endl;
        return 0;
    }
}

double stringToDouble(const string& s) {
    try {
        return stod(s);
    } catch (...) {
        cerr << "Invalid double format!" << endl;
        return 0.0;
    }
}
```

### Pattern 3: Number to String
```cpp
string intToString(int num) {
    return to_string(num);
}

string doubleToString(double num, int precision = 2) {
    string result = to_string(num);
    return result.substr(0, result.find('.') + precision + 1);
}
```

## 🐛 Common Pitfalls & Solutions

### 1. String vs Character Literals
```cpp
// Problem
string s = 'A';  // Error: can't convert char to string

// Solution
string s = "A";  // Correct
string s2(1, 'A'); // Also correct: string with 1 'A'
```

### 2. Input with Spaces
```cpp
// Problem
string name;
cin >> name;  // Only reads first word

// Solution
getline(cin, name);  // Reads entire line

// When mixing cin and getline
int age;
cin >> age;
cin.ignore();  // Clear newline
getline(cin, name);
```

### 3. String Comparison Issues
```cpp
// Problem
string s1 = "hello", s2 = "HELLO";
if (s1 == s2) { /* never true */ }

// Solution
if (s1.size() == s2.size() && 
    equal(s1.begin(), s1.end(), s2.begin(),
          [](char a, char b){ return tolower(a) == tolower(b); })) {
    // case-insensitive comparison
}
```

## 🎨 Advanced Techniques

### Custom String Class
```cpp
class SafeString {
private:
    string data;
    
public:
    SafeString(const string& s = "") : data(s) {}
    
    SafeString operator+(const SafeString& other) const {
        return SafeString(data + other.data);
    }
    
    bool contains(const string& substr) const {
        return data.find(substr) != string::npos;
    }
    
    // Conversion operator
    operator string() const { return data; }
};
```

### String Pool for Optimization
```cpp
class StringPool {
private:
    unordered_map<string, const string*> pool;
    
public:
    const string* intern(const string& s) {
        auto it = pool.find(s);
        if (it != pool.end()) {
            return it->second;
        }
        
        const string* ptr = new string(s);
        pool[s] = ptr;
        return ptr;
    }
};
```

## 📚 String Conversion Functions

### Numeric Conversions
```cpp
#include <string>

// String to numbers
int i = stoi("123");
long l = stol("123456");
float f = stof("3.14");
double d = stod("3.14159");

// Numbers to string
string s1 = to_string(123);
string s2 = to_string(3.14);
```

### Character Conversions
```cpp
#include <cctype>

char c = 'A';
char lower = tolower(c);  // 'a'
char upper = toupper(c);  // 'A'

bool is_digit = isdigit('5');    // true
bool is_alpha = isalpha('A');    // true
bool is_space = isspace(' ');    // true
```

## 🚀 Best Practices

1. **Use `getline()` for input with spaces**
2. **Prefer `string` over C-style char arrays**
3. **Use `at()` for bounds-checked access**
4. **Leverage STL algorithms** for string processing
5. **Be careful with string comparisons** (case sensitivity)
6. **Use `reserve()` for large string concatenations**

## 🎯 When to Use String

✅ **Use string when:**
- Handling text input/output
- Need dynamic string operations
- Working with file paths or names
- Processing user input
- Need built-in string manipulation

❌ **Consider alternatives when:**
- Need maximum performance (use string_view in C++17)
- Working with read-only string data
- Need substring references without copying
---

## Next Step

- Go to [04_algorithm.md](04_algorithm.md) to continue with algorithm.
