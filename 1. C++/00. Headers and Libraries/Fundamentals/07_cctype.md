# 07_cctype.md - Character Classification Library

The `cctype` header provides functions for character classification and conversion. It's the C++ version of the C library `<ctype.h>`.

## 📖 Overview

`cctype` contains functions for testing and converting individual characters. It's essential for text processing, input validation, and string manipulation tasks.

## 🎯 Key Categories

1. **Classification Functions** - Test character properties
2. **Conversion Functions** - Change character case
3. **Locale-independent** - Works with ASCII characters

## 🔧 Character Classification Functions

### Alphanumeric Checks
```cpp
#include <cctype>
#include <iostream>
#include <string>

int main() {
    char chars[] = {'A', 'b', '1', '@', ' ', '\t'};
    
    for (char c : chars) {
        unsigned char uc = static_cast<unsigned char>(c);
        
        std::cout << "Character '" << c << "':" << std::endl;
        std::cout << "  isalpha: " << std::isalpha(uc) << std::endl;  // Letter
        std::cout << "  isdigit: " << std::isdigit(uc) << std::endl;  // Digit
        std::cout << "  isalnum: " << std::isalnum(uc) << std::endl;  // Letter or digit
        std::cout << "  isxdigit: " << std::isxdigit(uc) << std::endl; // Hex digit
        std::cout << std::endl;
    }
    
    return 0;
}
```

### Whitespace and Control Characters
```cpp
void demonstrateWhitespace() {
    char chars[] = {' ', '\t', '\n', '\r', '\f', '\v', 'A', '1'};
    
    for (char c : chars) {
        unsigned char uc = static_cast<unsigned char>(c);
        
        std::cout << "Character '" << (c == ' ' ? "space" : 
                         c == '\t' ? "tab" : 
                         c == '\n' ? "newline" : 
                         c == '\r' ? "carriage_return" : 
                         c == '\f' ? "form_feed" : 
                         c == '\v' ? "vertical_tab" : std::string(1, c)) << "':" << std::endl;
        std::cout << "  isspace: " << std::isspace(uc) << std::endl;  // Whitespace
        std::cout << "  isblank: " << std::isblank(uc) << std::endl;  // Space or tab
        std::cout << "  iscntrl: " << std::iscntrl(uc) << std::endl;  // Control character
        std::cout << std::endl;
    }
}
```

### Printable and Punctuation Characters
```cpp
void demonstratePrintable() {
    char chars[] = {'A', '1', '!', ' ', '\n'};
    
    for (char c : chars) {
        unsigned char uc = static_cast<unsigned char>(c);
        
        std::cout << "Character '" << c << "':" << std::endl;
        std::cout << "  isprint: " << std::isprint(uc) << std::endl;  // Printable
        std::cout << "  isgraph: " << std::isgraph(uc) << std::endl;  // Printable but not space
        std::cout << "  ispunct: " << std::ispunct(uc) << std::endl;  // Punctuation
        std::cout << std::endl;
    }
}
```

## 🔧 Character Conversion Functions

### Case Conversion
```cpp
void demonstrateConversions() {
    char upper = 'A';
    char lower = 'z';
    char digit = '5';
    
    std::cout << "Original: " << upper << " -> tolower: " 
              << static_cast<char>(std::tolower(static_cast<unsigned char>(upper))) << std::endl;
    
    std::cout << "Original: " << lower << " -> toupper: " 
              << static_cast<char>(std::toupper(static_cast<unsigned char>(lower))) << std::endl;
    
    std::cout << "Original: " << digit << " -> toupper: " 
              << static_cast<char>(std::toupper(static_cast<unsigned char>(digit))) << std::endl;
}
```

## 🎮 Practical Examples

### Example 1: Password Validator
```cpp
#include <cctype>
#include <iostream>
#include <string>

class PasswordValidator {
public:
    static bool validatePassword(const std::string& password) {
        if (password.length() < 8) {
            std::cout << "Password must be at least 8 characters" << std::endl;
            return false;
        }
        
        bool hasUpper = false, hasLower = false, hasDigit = false, hasSpecial = false;
        
        for (char c : password) {
            unsigned char uc = static_cast<unsigned char>(c);
            
            if (std::isupper(uc)) hasUpper = true;
            else if (std::islower(uc)) hasLower = true;
            else if (std::isdigit(uc)) hasDigit = true;
            else if (std::ispunct(uc)) hasSpecial = true;
        }
        
        if (!hasUpper) std::cout << "Password must contain uppercase letter" << std::endl;
        if (!hasLower) std::cout << "Password must contain lowercase letter" << std::endl;
        if (!hasDigit) std::cout << "Password must contain digit" << std::endl;
        if (!hasSpecial) std::cout << "Password must contain special character" << std::endl;
        
        return hasUpper && hasLower && hasDigit && hasSpecial;
    }
};

int main() {
    std::string password;
    std::cout << "Enter password: ";
    std::cin >> password;
    
    if (PasswordValidator::validatePassword(password)) {
        std::cout << "Password is valid!" << std::endl;
    } else {
        std::cout << "Password is invalid!" << std::endl;
    }
    
    return 0;
}
```

### Example 2: String Tokenizer
```cpp
#include <cctype>
#include <iostream>
#include <vector>
#include <string>

class Tokenizer {
public:
    static std::vector<std::string> tokenize(const std::string& input) {
        std::vector<std::string> tokens;
        std::string currentToken;
        
        for (char c : input) {
            unsigned char uc = static_cast<unsigned char>(c);
            
            if (std::isspace(uc)) {
                if (!currentToken.empty()) {
                    tokens.push_back(currentToken);
                    currentToken.clear();
                }
            } else {
                currentToken += c;
            }
        }
        
        if (!currentToken.empty()) {
            tokens.push_back(currentToken);
        }
        
        return tokens;
    }
    
    static std::vector<std::string> tokenizeByType(const std::string& input) {
        std::vector<std::string> tokens;
        std::string currentToken;
        char currentType = '\0';
        
        for (char c : input) {
            unsigned char uc = static_cast<unsigned char>(c);
            
            char newType;
            if (std::isdigit(uc)) newType = 'd';      // digit
            else if (std::isalpha(uc)) newType = 'a'; // alpha
            else if (std::ispunct(uc)) newType = 'p'; // punctuation
            else newType = 'o';                       // other (whitespace handled separately)
            
            if (newType != currentType && !currentToken.empty()) {
                tokens.push_back(currentToken);
                currentToken.clear();
            }
            
            if (!std::isspace(uc)) {
                currentToken += c;
                currentType = newType;
            }
        }
        
        if (!currentToken.empty()) {
            tokens.push_back(currentToken);
        }
        
        return tokens;
    }
};

int main() {
    std::string text = "Hello123 World! 456Test";
    
    std::cout << "Original text: " << text << std::endl;
    
    auto tokens = Tokenizer::tokenize(text);
    std::cout << "Tokens by whitespace: ";
    for (const auto& token : tokens) {
        std::cout << "[" << token << "] ";
    }
    std::cout << std::endl;
    
    auto typeTokens = Tokenizer::tokenizeByType(text);
    std::cout << "Tokens by type: ";
    for (const auto& token : typeTokens) {
        std::cout << "[" << token << "] ";
    }
    std::cout << std::endl;
    
    return 0;
}
```

### Example 3: Text Analyzer
```cpp
#include <cctype>
#include <iostream>
#include <map>
#include <string>

class TextAnalyzer {
private:
    std::map<char, int> charCount;
    int totalChars = 0;
    int letters = 0;
    int digits = 0;
    int spaces = 0;
    int punctuation = 0;
    int words = 0;
    
public:
    void analyze(const std::string& text) {
        bool inWord = false;
        
        for (char c : text) {
            unsigned char uc = static_cast<unsigned char>(c);
            
            totalChars++;
            charCount[uc]++;
            
            if (std::isalpha(uc)) {
                letters++;
                if (!inWord) {
                    words++;
                    inWord = true;
                }
            } else if (std::isdigit(uc)) {
                digits++;
            } else if (std::isspace(uc)) {
                spaces++;
                inWord = false;
            } else if (std::ispunct(uc)) {
                punctuation++;
            }
        }
    }
    
    void displayStatistics() {
        std::cout << "=== Text Analysis ===" << std::endl;
        std::cout << "Total characters: " << totalChars << std::endl;
        std::cout << "Letters: " << letters << std::endl;
        std::cout << "Digits: " << digits << std::endl;
        std::cout << "Spaces: " << spaces << std::endl;
        std::cout << "Punctuation: " << punctuation << std::endl;
        std::cout << "Words: " << words << std::endl;
        
        std::cout << "\nMost frequent characters:" << std::endl;
        for (const auto& pair : charCount) {
            if (pair.second > 1 && std::isprint(static_cast<unsigned char>(pair.first))) {
                std::cout << "'" << pair.first << "': " << pair.second << std::endl;
            }
        }
    }
};

int main() {
    std::string text = "Hello, World! This is a test. 123 numbers!";
    
    TextAnalyzer analyzer;
    analyzer.analyze(text);
    analyzer.displayStatistics();
    
    return 0;
}
```

### Example 4: Case Insensitive String Comparison
```cpp
#include <cctype>
#include <iostream>
#include <string>

class StringComparator {
public:
    static bool equalsIgnoreCase(const std::string& str1, const std::string& str2) {
        if (str1.length() != str2.length()) {
            return false;
        }
        
        for (size_t i = 0; i < str1.length(); i++) {
            unsigned char c1 = static_cast<unsigned char>(str1[i]);
            unsigned char c2 = static_cast<unsigned char>(str2[i]);
            
            if (std::tolower(c1) != std::tolower(c2)) {
                return false;
            }
        }
        
        return true;
    }
    
    static std::string toLower(const std::string& str) {
        std::string result;
        result.reserve(str.length());
        
        for (char c : str) {
            result += static_cast<char>(std::tolower(static_cast<unsigned char>(c)));
        }
        
        return result;
    }
    
    static std::string toUpper(const std::string& str) {
        std::string result;
        result.reserve(str.length());
        
        for (char c : str) {
            result += static_cast<char>(std::toupper(static_cast<unsigned char>(c)));
        }
        
        return result;
    }
    
    static bool startsWithIgnoreCase(const std::string& str, const std::string& prefix) {
        if (prefix.length() > str.length()) {
            return false;
        }
        
        for (size_t i = 0; i < prefix.length(); i++) {
            unsigned char c1 = static_cast<unsigned char>(str[i]);
            unsigned char c2 = static_cast<unsigned char>(prefix[i]);
            
            if (std::tolower(c1) != std::tolower(c2)) {
                return false;
            }
        }
        
        return true;
    }
};

int main() {
    std::string str1 = "Hello World";
    std::string str2 = "HELLO WORLD";
    std::string str3 = "hello world";
    
    std::cout << "String comparison:" << std::endl;
    std::cout << "\"" << str1 << "\" == \"" << str2 << "\" (ignore case): " 
              << StringComparator::equalsIgnoreCase(str1, str2) << std::endl;
    
    std::cout << "To lowercase: " << StringComparator::toLower(str1) << std::endl;
    std::cout << "To uppercase: " << StringComparator::toUpper(str1) << std::endl;
    
    std::cout << "Starts with \"HELLO\": " 
              << StringComparator::startsWithIgnoreCase(str1, "HELLO") << std::endl;
    
    return 0;
}
```

## 📊 Complete Function Reference

### Classification Functions
| Function | Description | Example |
|----------|-------------|---------|
| `isalnum()` | Alphanumeric (letter or digit) | `isalnum('A')` → true |
| `isalpha()` | Alphabetic character | `isalpha('z')` → true |
| `isblank()` | Blank character (space or tab) | `isblank(' ')` → true |
| `iscntrl()` | Control character | `iscntrl('\n')` → true |
| `isdigit()` | Decimal digit | `isdigit('5')` → true |
| `isgraph()` | Printable character except space | `isgraph('!')` → true |
| `islower()` | Lowercase letter | `islower('a')` → true |
| `isprint()` | Printable character | `isprint('A')` → true |
| `ispunct()` | Punctuation character | `ispunct('!')` → true |
| `isspace()` | Whitespace character | `isspace(' ')` → true |
| `isupper()` | Uppercase letter | `isupper('A')` → true |
| `isxdigit()` | Hexadecimal digit | `isxdigit('F')` → true |

### Conversion Functions
| Function | Description | Example |
|----------|-------------|---------|
| `tolower()` | Convert to lowercase | `tolower('A')` → 'a' |
| `toupper()` | Convert to uppercase | `toupper('a')` → 'A' |

## ⚡ Performance Considerations

### Efficiency Tips
```cpp
// Efficient character processing
void processText(const std::string& text) {
    for (char c : text) {
        unsigned char uc = static_cast<unsigned char>(c);
        
        // Use lookup table for frequent operations
        static const bool isDigitTable[256] = {};
        // Initialize table once...
        
        if (isDigitTable[uc]) {
            // Process digit
        }
    }
}

// Batch processing for better cache performance
void batchValidation(const std::vector<std::string>& strings) {
    for (const auto& str : strings) {
        bool allValid = true;
        for (char c : str) {
            unsigned char uc = static_cast<unsigned char>(c);
            if (!std::isalnum(uc) && uc != '_') {
                allValid = false;
                break;
            }
        }
        
        if (allValid) {
            // Process valid string
        }
    }
}
```

## 🎯 Common Patterns

### Pattern 1: Input Validation
```cpp
bool isValidIdentifier(const std::string& str) {
    if (str.empty()) return false;
    
    unsigned char first = static_cast<unsigned char>(str[0]);
    if (!std::isalpha(first) && first != '_') {
        return false;
    }
    
    for (size_t i = 1; i < str.length(); i++) {
        unsigned char c = static_cast<unsigned char>(str[i]);
        if (!std::isalnum(c) && c != '_') {
            return false;
        }
    }
    
    return true;
}
```

### Pattern 2: Text Normalization
```cpp
std::string normalizeText(const std::string& text) {
    std::string normalized;
    normalized.reserve(text.length());
    
    for (char c : text) {
        unsigned char uc = static_cast<unsigned char>(c);
        
        if (std::isalnum(uc)) {
            normalized += std::tolower(uc);
        }
        // Skip non-alphanumeric characters
    }
    
    return normalized;
}
```

## 🐛 Common Pitfalls & Solutions

### 1. Undefined Behavior with Negative Characters
```cpp
// Problem
char c = -1;
if (std::isalpha(c)) { /* undefined behavior */ }

// Solution
char c = -1;
if (std::isalpha(static_cast<unsigned char>(c))) { /* safe */ }
```

### 2. Locale Issues
```cpp
// cctype functions are locale-independent
// For locale-aware operations, use <locale> header
```

### 3. Performance Issues with Repeated Calls
```cpp
// Inefficient
for (char c : text) {
    if (std::isalpha(c) || std::isdigit(c)) { /* ... */ }
}

// More efficient
for (char c : text) {
    unsigned char uc = static_cast<unsigned char>(c);
    if (std::isalnum(uc)) { /* ... */ }
}
```

## 📚 Related Headers

- `string.md` - String operations
- `algorithm.md` - String algorithms
- `locale.md` - Locale-dependent operations

## 🚀 Best Practices

1. **Always cast to `unsigned char`** before classification functions
2. **Use `isalnum()`** instead of `isalpha() || isdigit()` for better performance
3. **Consider lookup tables** for high-performance character processing
4. **Be aware of locale limitations** - use `<locale>` for internationalization
5. **Validate input** early using classification functions

## 🎯 When to Use cctype

✅ **Use cctype when:**
- Validating user input
- Parsing text files
- Implementing custom string operations
- Creating tokenizers
- Normalizing text data

❌ **Avoid when:**
- Working with Unicode text (use appropriate Unicode libraries)
- Need locale-aware processing (use `<locale>`)
- Processing large amounts of text efficiently (consider optimized libraries)
---

## Next Step

- Go to [08_cstring.md](08_cstring.md) to continue with cstring.
