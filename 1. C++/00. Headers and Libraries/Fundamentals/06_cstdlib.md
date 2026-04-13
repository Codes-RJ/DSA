# cstdlib - C++ Standard General Utilities Library

The `cstdlib` header (C++ version of C's `stdlib.h`) provides general-purpose functions for memory management, program control, random number generation, searching, sorting, and numeric conversions.

## 📖 Overview

`cstdlib` is part of the C++ standard library that provides utilities for memory management, program termination, random number generation, string conversion, searching, and sorting. It bridges C-style functionality with C++ programming.

## 🎯 Key Components

### Memory Management
```cpp
#include <cstdlib>
#include <iostream>

int main() {
    // C-style memory allocation
    int* ptr = (int*)malloc(5 * sizeof(int));  // Allocate memory for 5 integers
    
    if (ptr == nullptr) {
        std::cerr << "Memory allocation failed!" << std::endl;
        return 1;
    }
    
    // Use allocated memory
    for (int i = 0; i < 5; i++) {
        ptr[i] = i * 10;
        std::cout << ptr[i] << " ";
    }
    std::cout << std::endl;
    
    // Reallocate memory
    int* newPtr = (int*)realloc(ptr, 10 * sizeof(int));
    if (newPtr != nullptr) {
        ptr = newPtr;
        for (int i = 5; i < 10; i++) {
            ptr[i] = i * 10;
        }
    }
    
    // Free memory
    free(ptr);
    
    return 0;
}
```

### Program Control
```cpp
#include <cstdlib>
#include <iostream>

void cleanup() {
    std::cout << "Performing cleanup operations..." << std::endl;
}

int main() {
    // Register cleanup function to be called at program exit
    atexit(cleanup);
    
    std::cout << "Program is running..." << std::endl;
    
    // Normal termination
    // exit(0);  // Exits with status code 0
    
    // Abnormal termination
    // abort();  // Terminates immediately without cleanup
    
    return 0;
}
```

## 🔧 Core Functions

### 1. Memory Management Functions

#### malloc() - Allocate Memory
```cpp
#include <cstdlib>
#include <iostream>

int main() {
    // Allocate memory for 10 integers
    int* arr = (int*)malloc(10 * sizeof(int));
    
    if (arr == nullptr) {
        std::cerr << "Memory allocation failed" << std::endl;
        return 1;
    }
    
    // Use memory
    for (int i = 0; i < 10; i++) {
        arr[i] = i * 2;
    }
    
    // Free memory
    free(arr);
    
    return 0;
}
```

#### calloc() - Allocate and Zero Initialize
```cpp
#include <cstdlib>
#include <iostream>

int main() {
    // Allocate memory for 5 integers and initialize to 0
    int* arr = (int*)calloc(5, sizeof(int));
    
    // All elements are initialized to 0
    for (int i = 0; i < 5; i++) {
        std::cout << arr[i] << " ";  // Prints: 0 0 0 0 0
    }
    std::cout << std::endl;
    
    // Use memory
    arr[2] = 42;
    
    free(arr);
    
    return 0;
}
```

#### realloc() - Resize Memory
```cpp
#include <cstdlib>
#include <iostream>

int main() {
    int* arr = (int*)malloc(5 * sizeof(int));
    
    // Initialize first 5 elements
    for (int i = 0; i < 5; i++) {
        arr[i] = i;
    }
    
    // Resize to 10 elements
    int* newArr = (int*)realloc(arr, 10 * sizeof(int));
    
    if (newArr != nullptr) {
        arr = newArr;
        
        // Initialize new elements
        for (int i = 5; i < 10; i++) {
            arr[i] = i * 2;
        }
        
        // Print all elements
        for (int i = 0; i < 10; i++) {
            std::cout << arr[i] << " ";
        }
        std::cout << std::endl;
    }
    
    free(arr);
    
    return 0;
}
```

### 2. String Conversion Functions

#### atoi() - Convert String to Integer
```cpp
#include <cstdlib>
#include <iostream>

int main() {
    const char* numStr1 = "123";
    const char* numStr2 = "  456  ";
    const char* numStr3 = "789abc";
    const char* numStr4 = "abc123";
    
    int num1 = atoi(numStr1);
    int num2 = atoi(numStr2);
    int num3 = atoi(numStr3);  // Stops at 'a', returns 789
    int num4 = atoi(numStr4);  // Returns 0
    
    std::cout << "atoi(\"123\"): " << num1 << std::endl;
    std::cout << "atoi(\"  456  \"): " << num2 << std::endl;
    std::cout << "atoi(\"789abc\"): " << num3 << std::endl;
    std::cout << "atoi(\"abc123\"): " << num4 << std::endl;
    
    return 0;
}
```

#### atol(), atoll() - Convert to Long
```cpp
#include <cstdlib>
#include <iostream>

int main() {
    const char* numStr = "1234567890";
    
    long lnum = atol(numStr);
    long long llnum = atoll(numStr);
    
    std::cout << "atol: " << lnum << std::endl;
    std::cout << "atoll: " << llnum << std::endl;
    
    return 0;
}
```

#### atof() - Convert to Double
```cpp
#include <cstdlib>
#include <iostream>

int main() {
    const char* numStr1 = "3.14159";
    const char* numStr2 = "  2.718  ";
    const char* numStr3 = "1.23e-4";
    
    double num1 = atof(numStr1);
    double num2 = atof(numStr2);
    double num3 = atof(numStr3);
    
    std::cout << "atof(\"3.14159\"): " << num1 << std::endl;
    std::cout << "atof(\"  2.718  \"): " << num2 << std::endl;
    std::cout << "atof(\"1.23e-4\"): " << num3 << std::endl;
    
    return 0;
}
```

#### strtol() - Convert String to Long with Error Detection
```cpp
#include <cstdlib>
#include <iostream>
#include <cerrno>

int main() {
    const char* str = "123abc";
    char* endptr;
    
    errno = 0;  // Reset error number
    long val = strtol(str, &endptr, 10);  // Base 10
    
    if (errno == ERANGE) {
        std::cerr << "Value out of range!" << std::endl;
    } else if (endptr == str) {
        std::cerr << "No digits found!" << std::endl;
    } else {
        std::cout << "Converted value: " << val << std::endl;
        std::cout << "Remaining string: " << endptr << std::endl;
    }
    
    // Different bases
    const char* hex = "FF";
    const char* bin = "1010";
    const char* oct = "77";
    
    long hexVal = strtol(hex, nullptr, 16);
    long binVal = strtol(bin, nullptr, 2);
    long octVal = strtol(oct, nullptr, 8);
    
    std::cout << "Hex FF: " << hexVal << std::endl;
    std::cout << "Binary 1010: " << binVal << std::endl;
    std::cout << "Octal 77: " << octVal << std::endl;
    
    return 0;
}
```

#### strtod() - Convert String to Double
```cpp
#include <cstdlib>
#include <iostream>

int main() {
    const char* str = "3.14159extra";
    char* endptr;
    
    double val = strtod(str, &endptr);
    
    std::cout << "Converted value: " << val << std::endl;
    std::cout << "Remaining string: " << endptr << std::endl;
    
    return 0;
}
```

### 3. Random Number Generation

#### rand() and srand()
```cpp
#include <cstdlib>
#include <iostream>
#include <ctime>

int main() {
    // Seed random number generator with current time
    srand(time(nullptr));
    
    // Generate random numbers
    std::cout << "Random numbers: ";
    for (int i = 0; i < 10; i++) {
        std::cout << rand() << " ";
    }
    std::cout << std::endl;
    
    // Generate numbers in specific range
    std::cout << "Random numbers between 1 and 100: ";
    for (int i = 0; i < 10; i++) {
        int random = rand() % 100 + 1;  // 1 to 100
        std::cout << random << " ";
    }
    std::cout << std::endl;
    
    // Generate floating point numbers between 0 and 1
    std::cout << "Random doubles between 0 and 1: ";
    for (int i = 0; i < 10; i++) {
        double random = static_cast<double>(rand()) / RAND_MAX;
        std::cout << random << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
```

### 4. Searching and Sorting

#### qsort() - Quick Sort
```cpp
#include <cstdlib>
#include <iostream>

int compareInt(const void* a, const void* b) {
    int int_a = *(int*)a;
    int int_b = *(int*)b;
    return int_a - int_b;  // Ascending order
}

int compareDouble(const void* a, const void* b) {
    double double_a = *(double*)a;
    double double_b = *(double*)b;
    if (double_a < double_b) return -1;
    if (double_a > double_b) return 1;
    return 0;
}

int compareString(const void* a, const void* b) {
    const char** str_a = (const char**)a;
    const char** str_b = (const char**)b;
    return strcmp(*str_a, *str_b);
}

int main() {
    // Integer array
    int intArr[] = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    int intSize = sizeof(intArr) / sizeof(intArr[0]);
    
    qsort(intArr, intSize, sizeof(int), compareInt);
    
    std::cout << "Sorted integers: ";
    for (int i = 0; i < intSize; i++) {
        std::cout << intArr[i] << " ";
    }
    std::cout << std::endl;
    
    // Double array
    double doubleArr[] = {3.14, 1.41, 2.71, 1.73, 2.23};
    int doubleSize = sizeof(doubleArr) / sizeof(doubleArr[0]);
    
    qsort(doubleArr, doubleSize, sizeof(double), compareDouble);
    
    std::cout << "Sorted doubles: ";
    for (int i = 0; i < doubleSize; i++) {
        std::cout << doubleArr[i] << " ";
    }
    std::cout << std::endl;
    
    // String array
    const char* strArr[] = {"banana", "apple", "cherry", "date", "elderberry"};
    int strSize = sizeof(strArr) / sizeof(strArr[0]);
    
    qsort(strArr, strSize, sizeof(const char*), compareString);
    
    std::cout << "Sorted strings: ";
    for (int i = 0; i < strSize; i++) {
        std::cout << strArr[i] << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
```

#### bsearch() - Binary Search
```cpp
#include <cstdlib>
#include <iostream>

int compareInt(const void* a, const void* b) {
    int int_a = *(int*)a;
    int int_b = *(int*)b;
    return int_a - int_b;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size = sizeof(arr) / sizeof(arr[0]);
    int target = 7;
    
    int* result = (int*)bsearch(&target, arr, size, sizeof(int), compareInt);
    
    if (result != nullptr) {
        std::cout << "Found " << target << " at index: " << (result - arr) << std::endl;
    } else {
        std::cout << target << " not found" << std::endl;
    }
    
    target = 15;
    result = (int*)bsearch(&target, arr, size, sizeof(int), compareInt);
    
    if (result != nullptr) {
        std::cout << "Found " << target << std::endl;
    } else {
        std::cout << target << " not found" << std::endl;
    }
    
    return 0;
}
```

### 5. Program Termination

```cpp
#include <cstdlib>
#include <iostream>

void cleanup1() {
    std::cout << "Cleanup function 1 called" << std::endl;
}

void cleanup2() {
    std::cout << "Cleanup function 2 called" << std::endl;
}

int main() {
    // Register cleanup functions (called in reverse order)
    atexit(cleanup1);
    atexit(cleanup2);
    
    std::cout << "Program running..." << std::endl;
    
    // exit(0);  // Normal termination, cleanup functions called
    
    // abort();  // Abnormal termination, no cleanup
    
    // quick_exit(0);  // Fast termination (C++11)
    
    return 0;
}
```

### 6. Environment Interaction

```cpp
#include <cstdlib>
#include <iostream>

int main() {
    // Get environment variable
    const char* path = getenv("PATH");
    if (path != nullptr) {
        std::cout << "PATH: " << path << std::endl;
    }
    
    const char* home = getenv("HOME");
    if (home != nullptr) {
        std::cout << "HOME: " << home << std::endl;
    }
    
    // Execute system command
    system("echo Hello from system command!");
    system("ls -la");  // Unix/Linux
    // system("dir");  // Windows
    
    return 0;
}
```

## 🎮 Complete Examples

### Example 1: Dynamic Array Manager
```cpp
#include <cstdlib>
#include <iostream>
#include <cstring>

class DynamicArray {
private:
    int* data;
    size_t size;
    size_t capacity;
    
public:
    DynamicArray() : data(nullptr), size(0), capacity(0) {}
    
    ~DynamicArray() {
        if (data != nullptr) {
            free(data);
        }
    }
    
    void push_back(int value) {
        if (size >= capacity) {
            capacity = capacity == 0 ? 1 : capacity * 2;
            int* newData = (int*)realloc(data, capacity * sizeof(int));
            if (newData == nullptr) {
                std::cerr << "Memory allocation failed!" << std::endl;
                return;
            }
            data = newData;
        }
        data[size++] = value;
    }
    
    int* find(int target) {
        for (size_t i = 0; i < size; i++) {
            if (data[i] == target) {
                return &data[i];
            }
        }
        return nullptr;
    }
    
    void sort() {
        if (data == nullptr) return;
        qsort(data, size, sizeof(int), [](const void* a, const void* b) {
            return *(int*)a - *(int*)b;
        });
    }
    
    void display() {
        std::cout << "Array contents: ";
        for (size_t i = 0; i < size; i++) {
            std::cout << data[i] << " ";
        }
        std::cout << std::endl;
    }
    
    size_t getSize() const { return size; }
};

int main() {
    DynamicArray arr;
    
    // Add random numbers
    srand(time(nullptr));
    for (int i = 0; i < 20; i++) {
        arr.push_back(rand() % 100);
    }
    
    std::cout << "Before sorting:" << std::endl;
    arr.display();
    
    arr.sort();
    
    std::cout << "After sorting:" << std::endl;
    arr.display();
    
    // Search for a number
    int target = 50;
    int* result = arr.find(target);
    if (result != nullptr) {
        std::cout << "Found " << target << " at address: " << result << std::endl;
    } else {
        std::cout << target << " not found" << std::endl;
    }
    
    return 0;
}
```

### Example 2: Number Guessing Game
```cpp
#include <cstdlib>
#include <iostream>
#include <ctime>

int main() {
    // Seed random number generator
    srand(time(nullptr));
    
    // Generate random number between 1 and 100
    int secret = rand() % 100 + 1;
    int guess;
    int attempts = 0;
    
    std::cout << "Welcome to the Number Guessing Game!" << std::endl;
    std::cout << "I'm thinking of a number between 1 and 100." << std::endl;
    
    do {
        std::cout << "Enter your guess: ";
        
        // Input validation
        char input[20];
        std::cin >> input;
        guess = atoi(input);
        
        if (guess < 1 || guess > 100) {
            std::cout << "Please enter a number between 1 and 100!" << std::endl;
            continue;
        }
        
        attempts++;
        
        if (guess < secret) {
            std::cout << "Too low! Try again." << std::endl;
        } else if (guess > secret) {
            std::cout << "Too high! Try again." << std::endl;
        } else {
            std::cout << "Congratulations! You guessed it in " << attempts << " attempts!" << std::endl;
        }
        
    } while (guess != secret);
    
    return 0;
}
```

### Example 3: Command-Line Calculator
```cpp
#include <cstdlib>
#include <iostream>
#include <cstring>

int main(int argc, char* argv[]) {
    if (argc != 4) {
        std::cerr << "Usage: " << argv[0] << " <num1> <operator> <num2>" << std::endl;
        std::cerr << "Operators: +, -, *, /" << std::endl;
        return 1;
    }
    
    double num1 = atof(argv[1]);
    double num2 = atof(argv[3]);
    char op = argv[2][0];
    
    double result;
    bool valid = true;
    
    switch (op) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            if (num2 != 0) {
                result = num1 / num2;
            } else {
                std::cerr << "Error: Division by zero!" << std::endl;
                valid = false;
            }
            break;
        default:
            std::cerr << "Error: Invalid operator!" << std::endl;
            valid = false;
    }
    
    if (valid) {
        std::cout << num1 << " " << op << " " << num2 << " = " << result << std::endl;
    }
    
    return valid ? 0 : 1;
}
```

## ⚡ Performance Tips

1. **Prefer C++ memory management** (`new`/`delete`) over C-style (`malloc`/`free`) when possible
2. **Use `rand()` with caution** - It's not cryptographically secure
3. **Consider C++11 random library** for better random number generation
4. **Use `strtol()` for error detection** instead of `atoi()`
5. **Prefer C++ algorithms** (`std::sort`) over `qsort()` for type safety

## 🐛 Common Pitfalls & Solutions

### 1. Memory Leaks
```cpp
// Problem
int* ptr = (int*)malloc(100 * sizeof(int));
// ... use ptr
// Forgot to call free(ptr) - Memory leak!

// Solution
int* ptr = (int*)malloc(100 * sizeof(int));
// ... use ptr
free(ptr);  // Always free memory
ptr = nullptr;  // Good practice
```

### 2. Dangling Pointers
```cpp
// Problem
int* ptr = (int*)malloc(sizeof(int));
free(ptr);
// ptr is now dangling
*ptr = 42;  // Undefined behavior!

// Solution
int* ptr = (int*)malloc(sizeof(int));
free(ptr);
ptr = nullptr;  // Set to null after freeing
```

### 3. Buffer Overflow
```cpp
// Problem
char buffer[10];
strcpy(buffer, "This string is too long");  // Buffer overflow!

// Solution - Use strncpy or prefer C++ strings
char buffer[20];
strncpy(buffer, "This string is fine", sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

## 🎯 Best Practices

1. **Always check return values** of `malloc()`/`calloc()`/`realloc()` for `nullptr`
2. **Free allocated memory** when no longer needed
3. **Use `calloc()` for zero-initialized memory** instead of `malloc()` + manual zeroing
4. **Prefer C++ features** (`new`/`delete`, `std::string`, `std::vector`) over C-style functions
5. **Validate input** when converting strings to numbers
6. **Seed random number generator** with `srand(time(nullptr))` for different sequences
7. **Use `strtol()` for error detection** in string-to-number conversion
8. **Register cleanup functions** with `atexit()` when needed
---

## Next Step

- Go to [07_cctype.md](07_cctype.md) to continue with cctype.
