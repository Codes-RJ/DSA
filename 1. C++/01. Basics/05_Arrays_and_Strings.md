# Arrays and Strings

## Overview
Arrays and strings are fundamental data structures in C++ that store collections of elements. Arrays provide fixed-size sequential storage, while strings are specialized arrays for character data.

## Arrays

### 1. One-Dimensional Arrays

#### Declaration and Initialization
```cpp
// Different ways to declare and initialize arrays
int arr1[5];                    // Uninitialized array
int arr2[5] = {1, 2, 3, 4, 5};  // Fully initialized
int arr3[] = {1, 2, 3, 4, 5};   // Size inferred from initializer
int arr4[5] = {1, 2, 3};        // Partially initialized (rest = 0)
int arr5[5] = {0};              // All elements initialized to 0

// C++11 uniform initialization
int arr6[]{1, 2, 3, 4, 5};
std::vector<int> vec = {1, 2, 3, 4, 5};  // Dynamic alternative
```

#### Accessing Elements
```cpp
int arr[5] = {10, 20, 30, 40, 50};

// Access elements
std::cout << arr[0] << std::endl;  // 10
std::cout << arr[2] << std::endl;  // 30

// Modify elements
arr[1] = 25;
arr[4] = 55;

// Iterate through array
for (int i = 0; i < 5; i++) {
    std::cout << arr[i] << " ";
}
std::cout << std::endl;

// Range-based for loop (C++11)
for (int val : arr) {
    std::cout << val << " ";
}
std::cout << std::endl;
```

#### Array Size and Bounds
```cpp
int arr[5] = {1, 2, 3, 4, 5};

// Get array size
int size = sizeof(arr) / sizeof(arr[0]);
std::cout << "Array size: " << size << std::endl;

// Bounds checking (C++ doesn't do this automatically)
int index = 2;
if (index >= 0 && index < 5) {
    std::cout << arr[index] << std::endl;
} else {
    std::cout << "Index out of bounds!" << std::endl;
}

// Using std::array for bounds checking (C++11)
std::array<int, 5> safeArr = {1, 2, 3, 4, 5};
std::cout << safeArr.at(2) << std::endl;  // Bounds checked
// std::cout << safeArr.at(10) << std::endl;  // Throws exception
```

### 2. Multi-Dimensional Arrays

#### Two-Dimensional Arrays
```cpp
// Declaration and initialization
int matrix[3][4] = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}
};

// Accessing elements
std::cout << matrix[1][2] << std::endl;  // 7

// Iterating through 2D array
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 4; j++) {
        std::cout << matrix[i][j] << " ";
    }
    std::cout << std::endl;
}

// Using range-based for loops
for (const auto& row : matrix) {
    for (int val : row) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
}
```

#### Dynamic 2D Arrays
```cpp
// Using vectors
std::vector<std::vector<int>> dynamicMatrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

// Using raw pointers (manual memory management)
int** createMatrix(int rows, int cols) {
    int** matrix = new int*[rows];
    for (int i = 0; i < rows; i++) {
        matrix[i] = new int[cols];
    }
    return matrix;
}

void deleteMatrix(int** matrix, int rows) {
    for (int i = 0; i < rows; i++) {
        delete[] matrix[i];
    }
    delete[] matrix;
}
```

### 3. Common Array Operations

#### Searching
```cpp
// Linear search
int linearSearch(const int arr[], int size, int target) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) {
            return i;  // Found at index i
        }
    }
    return -1;  // Not found
}

// Binary search (requires sorted array)
int binarySearch(const int arr[], int size, int target) {
    int left = 0, right = size - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1;  // Not found
}
```

#### Sorting
```cpp
// Bubble sort
void bubbleSort(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
            }
        }
    }
}

// Using std::sort
#include <algorithm>
void sortArray(int arr[], int size) {
    std::sort(arr, arr + size);
}

// Sorting vectors
std::vector<int> vec = {5, 2, 8, 1, 9};
std::sort(vec.begin(), vec.end());
```

## Strings

### 1. C-Style Strings

#### Character Arrays
```cpp
// C-style string declaration
char str1[] = "Hello";           // Automatically null-terminated
char str2[6] = {'H', 'e', 'l', 'l', 'o', '\0'};  // Manual null termination
char str3[10];                   // Uninitialized

// String functions from <cstring>
#include <cstring>

char source[] = "Hello, World!";
char destination[50];

// Copy string
strcpy(destination, source);     // Unsafe (no bounds checking)
strncpy(destination, source, 49); // Safe version
destination[49] = '\0';         // Ensure null termination

// Concatenate strings
strcat(destination, " How are you?");
strncat(destination, " Fine.", 6);

// String length
size_t len = strlen(destination);

// Compare strings
char strA[] = "Hello";
char strB[] = "Hello";
if (strcmp(strA, strB) == 0) {
    std::cout << "Strings are equal" << std::endl;
}

// Find substring
char* found = strstr(destination, "World");
if (found != nullptr) {
    std::cout << "Found at position: " << (found - destination) << std::endl;
}
```

### 2. std::string (C++ Style)

#### Basic Operations
```cpp
#include <string>

// Creating strings
std::string str1 = "Hello";
std::string str2("World");
std::string str3(5, 'A');  // "AAAAA"

// Concatenation
std::string result = str1 + ", " + str2 + "!";
str1 += " and " + str2;

// Accessing characters
char first = str1[0];
char last = str1.back();
str1[0] = 'h';  // Modify character

// String length
size_t len = str1.length();  // or str1.size()

// Substring
std::string sub = str1.substr(0, 5);  // "Hello"

// Finding substrings
size_t pos = str1.find("World");
if (pos != std::string::npos) {
    std::cout << "Found at position: " << pos << std::endl;
}

// Replacing substrings
str1.replace(pos, 5, "C++");

// Erasing and inserting
str1.erase(0, 6);  // Remove first 6 characters
str1.insert(0, "Hi");  // Insert at beginning
```

#### String Comparison
```cpp
std::string str1 = "Hello";
std::string str2 = "hello";

// Case-sensitive comparison
if (str1 == str2) {
    std::cout << "Strings are equal" << std::endl;
}

// Case-insensitive comparison
#include <algorithm>
#include <cctype>

bool caseInsensitiveCompare(const std::string& a, const std::string& b) {
    if (a.length() != b.length()) return false;
    
    return std::equal(a.begin(), a.end(), b.begin(), [](char a, char b) {
        return std::tolower(a) == std::tolower(b);
    });
}
```

#### String Conversion
```cpp
// String to number
std::string numStr = "123";
int intValue = std::stoi(numStr);
double doubleValue = std::stod(numStr);
long longValue = std::stol(numStr);

// Number to string
int number = 42;
std::string intStr = std::to_string(number);
std::string doubleStr = std::to_string(3.14159);

// String streams for complex formatting
#include <sstream>

std::string formatString(int num, double val, const std::string& text) {
    std::ostringstream oss;
    oss << "Number: " << num << ", Value: " << std::fixed << std::setprecision(2) 
        << val << ", Text: " << text;
    return oss.str();
}
```

### 3. String Algorithms

#### Palindrome Check
```cpp
bool isPalindrome(const std::string& str) {
    int left = 0, right = str.length() - 1;
    
    while (left < right) {
        if (str[left] != str[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

// Case-insensitive palindrome
bool isPalindromeIgnoreCase(const std::string& str) {
    int left = 0, right = str.length() - 1;
    
    while (left < right) {
        if (std::tolower(str[left]) != std::tolower(str[right])) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
```

#### String Tokenization
```cpp
#include <sstream>

// Using stringstream
std::vector<std::string> tokenize(const std::string& str, char delimiter) {
    std::vector<std::string> tokens;
    std::stringstream ss(str);
    std::string token;
    
    while (std::getline(ss, token, delimiter)) {
        tokens.push_back(token);
    }
    
    return tokens;
}

// Manual tokenization
std::vector<std::string> split(const std::string& str, const std::string& delimiter) {
    std::vector<std::string> tokens;
    size_t start = 0, end = str.find(delimiter);
    
    while (end != std::string::npos) {
        tokens.push_back(str.substr(start, end - start));
        start = end + delimiter.length();
        end = str.find(delimiter, start);
    }
    
    tokens.push_back(str.substr(start));
    return tokens;
}
```

#### Pattern Matching
```cpp
// Naive pattern matching
int findPattern(const std::string& text, const std::string& pattern) {
    size_t textLen = text.length();
    size_t patternLen = pattern.length();
    
    for (size_t i = 0; i <= textLen - patternLen; i++) {
        bool found = true;
        for (size_t j = 0; j < patternLen; j++) {
            if (text[i + j] != pattern[j]) {
                found = false;
                break;
            }
        }
        if (found) {
            return i;
        }
    }
    
    return -1;
}

// Count occurrences
int countOccurrences(const std::string& text, const std::string& pattern) {
    int count = 0;
    size_t pos = 0;
    
    while ((pos = text.find(pattern, pos)) != std::string::npos) {
        count++;
        pos += pattern.length();
    }
    
    return count;
}
```

## Advanced Array Operations

### 1. Array Algorithms

#### Finding Maximum/Minimum
```cpp
int findMax(const int arr[], int size) {
    if (size <= 0) throw std::invalid_argument("Empty array");
    
    int maxVal = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > maxVal) {
            maxVal = arr[i];
        }
    }
    return maxVal;
}

std::pair<int, int> findMinMax(const int arr[], int size) {
    if (size <= 0) throw std::invalid_argument("Empty array");
    
    int minVal = arr[0], maxVal = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] < minVal) minVal = arr[i];
        if (arr[i] > maxVal) maxVal = arr[i];
    }
    return {minVal, maxVal};
}
```

#### Array Reversal
```cpp
void reverseArray(int arr[], int size) {
    int left = 0, right = size - 1;
    while (left < right) {
        std::swap(arr[left], arr[right]);
        left++;
        right--;
    }
}

// In-place string reversal
void reverseString(std::string& str) {
    int left = 0, right = str.length() - 1;
    while (left < right) {
        std::swap(str[left], str[right]);
        left++;
        right--;
    }
}
```

#### Array Rotation
```cpp
// Rotate array left by k positions
void rotateLeft(int arr[], int size, int k) {
    k = k % size;  // Handle k > size
    
    // Reverse first k elements
    std::reverse(arr, arr + k);
    // Reverse remaining elements
    std::reverse(arr + k, arr + size);
    // Reverse entire array
    std::reverse(arr, arr + size);
}

// Rotate array right by k positions
void rotateRight(int arr[], int size, int k) {
    k = k % size;
    rotateLeft(arr, size, size - k);
}
```

### 2. Matrix Operations

#### Matrix Multiplication
```cpp
std::vector<std::vector<int>> matrixMultiply(
    const std::vector<std::vector<int>>& a,
    const std::vector<std::vector<int>>& b) {
    
    int rowsA = a.size();
    int colsA = a[0].size();
    int colsB = b[0].size();
    
    std::vector<std::vector<int>> result(rowsA, std::vector<int>(colsB, 0));
    
    for (int i = 0; i < rowsA; i++) {
        for (int j = 0; j < colsB; j++) {
            for (int k = 0; k < colsA; k++) {
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    
    return result;
}
```

#### Matrix Transpose
```cpp
std::vector<std::vector<int>> transposeMatrix(
    const std::vector<std::vector<int>>& matrix) {
    
    int rows = matrix.size();
    int cols = matrix[0].size();
    
    std::vector<std::vector<int>> result(cols, std::vector<int>(rows));
    
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            result[j][i] = matrix[i][j];
        }
    }
    
    return result;
}
```

## Best Practices

### 1. Array Usage
- Use `std::vector` instead of C-style arrays when possible
- Use `std::array` for fixed-size arrays with bounds checking
- Prefer range-based for loops for iteration
- Be careful with array bounds to avoid buffer overflows

### 2. String Usage
- Prefer `std::string` over C-style strings
- Use `std::string_view` for read-only string references (C++17)
- Be aware of string copy overhead
- Use `const std::string&` for function parameters

### 3. Memory Management
- Use RAII principles with containers
- Avoid manual memory management when possible
- Use smart pointers for dynamic arrays
- Be aware of the "Rule of Three/Five/Zero"

## Common Pitfalls

### 1. Array Issues
```cpp
// Wrong: Array bounds violation
int arr[5];
arr[10] = 42;  // Undefined behavior

// Wrong: Returning pointer to local array
int* badFunction() {
    int localArr[5] = {1, 2, 3, 4, 5};
    return localArr;  // Error: local array destroyed
}

// Correct: Use static or dynamic allocation
int* goodFunction() {
    static int localArr[5] = {1, 2, 3, 4, 5};
    return localArr;
}
```

### 2. String Issues
```cpp
// Wrong: C-style string without null termination
char badStr[] = {'H', 'e', 'l', 'l', 'o'};  // Missing '\0'

// Wrong: Returning pointer to string literal
char* badStringFunction() {
    return "Hello";  // Warning: returning const char*
}

// Correct: Use std::string
std::string goodStringFunction() {
    return "Hello";
}
```

---

*This guide provides a comprehensive overview of arrays and strings in C++, covering fundamental operations, advanced algorithms, and best practices for effective usage.*
