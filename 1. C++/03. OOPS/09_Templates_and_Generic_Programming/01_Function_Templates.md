# Function Templates

## 📖 Overview

Function templates are a powerful C++ feature that allows you to write generic functions that can work with different data types. Instead of writing separate functions for each type, you can write a single template that the compiler can instantiate for any required type.

---

## 🎯 Key Concepts

- **Template Parameter**: Placeholder for data type (`typename T` or `class T`)
- **Type Deduction**: Compiler automatically determines template arguments
- **Function Template Instantiation**: Compiler generates concrete function from template
- **Template Argument List**: Explicit specification of template types

---

## 💻 Basic Syntax

```cpp
template <typename T>
returnType functionName(parameterList) {
    // Function body
}
```

### Alternative Syntax
```cpp
template <class T>
returnType functionName(parameterList) {
    // Function body
}
```

---

## 🔍 Detailed Explanation

### 1. **Simple Function Template**

```cpp
#include <iostream>
using namespace std;

// Basic function template
template <typename T>
T findMaximum(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    // Type deduction - compiler determines T automatically
    cout << "Max of 10 and 20: " << findMaximum(10, 20) << endl;      // T = int
    cout << "Max of 3.14 and 2.71: " << findMaximum(3.14, 2.71) << endl; // T = double
    cout << "Max of 'A' and 'Z': " << findMaximum('A', 'Z') << endl;  // T = char
    
    // Explicit template specification
    cout << "Max (explicit): " << findMaximum<double>(5, 3.7) << endl; // T = double
    
    return 0;
}
```

### 2. **Multiple Template Parameters**

```cpp
#include <iostream>
#include <string>
using namespace std;

// Function with multiple template parameters
template <typename T, typename U>
void printPair(T first, U second) {
    cout << "First: " << first << ", Second: " << second << endl;
}

// Function returning different type
template <typename T, typename R>
R castAndAdd(T a, T b) {
    return static_cast<R>(a) + static_cast<R>(b);
}

int main() {
    printPair(42, "Hello");           // T = int, U = const char*
    printPair(3.14, "Pi");            // T = double, U = const char*
    printPair("Age", 25);             // T = const char*, U = int
    
    // Explicit template arguments
    double result = castAndAdd<int, double>(5, 3);
    cout << "Cast and add result: " << result << endl;
    
    return 0;
}
```

### 3. **Template Parameters with Default Values**

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Template with default parameter
template <typename T, int Size = 10>
class FixedBuffer {
private:
    T buffer[Size];
    int count = 0;
    
public:
    void add(const T& item) {
        if (count < Size) {
            buffer[count++] = item;
        }
    }
    
    void print() const {
        for (int i = 0; i < count; i++) {
            cout << buffer[i] << " ";
        }
        cout << endl;
    }
    
    int getSize() const { return Size; }
    int getCount() const { return count; }
};

// Function template with default type
template <typename T = int>
T getDefault() {
    return T{};
}

int main() {
    // Using default size
    FixedBuffer<int> buffer1;
    buffer1.add(10);
    buffer1.add(20);
    buffer1.add(30);
    
    cout << "Buffer1 (size " << buffer1.getSize() << "): ";
    buffer1.print();
    
    // Explicit size
    FixedBuffer<string, 5> buffer2;
    buffer2.add("Hello");
    buffer2.add("World");
    
    cout << "Buffer2 (size " << buffer2.getSize() << "): ";
    buffer2.print();
    
    // Default type
    cout << "Default int: " << getDefault() << endl;
    cout << "Default double: " << getDefault<double>() << endl;
    
    return 0;
}
```

### 4. **Template Function Overloading**

```cpp
#include <iostream>
#include <cstring>
using namespace std;

// General template
template <typename T>
void printArray(T arr[], int size) {
    cout << "Generic array: ";
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

// Specialized overload for const char*
void printArray(const char* arr[], int size) {
    cout << "String array: ";
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

// Template with different parameter count
template <typename T>
T sum(T a, T b) {
    cout << "Two parameters: ";
    return a + b;
}

template <typename T>
T sum(T a, T b, T c) {
    cout << "Three parameters: ";
    return a + b + c;
}

int main() {
    int intArr[] = {1, 2, 3, 4, 5};
    double doubleArr[] = {1.1, 2.2, 3.3};
    
    printArray(intArr, 5);
    printArray(doubleArr, 3);
    
    const char* strArr[] = {"Hello", "World", "Templates"};
    printArray(strArr, 3);
    
    cout << "Sum: " << sum(5, 3) << endl;
    cout << "Sum: " << sum(1, 2, 3) << endl;
    cout << "Sum: " << sum(2.5, 1.5) << endl;
    cout << "Sum: " << sum(1.0, 2.0, 3.0) << endl;
    
    return 0;
}
```

### 5. **Template Constraints and Requirements**

```cpp
#include <iostream>
#include <type_traits>
using namespace std;

// Template with SFINAE (Substitution Failure Is Not An Error)
template <typename T>
typename enable_if<is_integral<T>::value, T>::type
multiply(T a, T b) {
    cout << "Integral multiplication: ";
    return a * b;
}

template <typename T>
typename enable_if<is_floating_point<T>::value, T>::type
multiply(T a, T b) {
    cout << "Floating point multiplication: ";
    return a * b;
}

// Modern C++20 concepts (if available)
#ifdef __cpp_concepts
template <typename T>
concept Numeric = is_integral_v<T> || is_floating_point_v<T>;

template <Numeric T>
T addNumbers(T a, T b) {
    return a + b;
}
#endif

// Template requiring specific operations
template <typename T>
auto processValue(T value) -> decltype(value * value) {
    static_assert(is_arithmetic<T>::value, "T must be a numeric type");
    cout << "Processing numeric value: ";
    return value * value;
}

int main() {
    cout << multiply(5, 3) << endl;      // Uses integral version
    cout << multiply(3.14, 2.0) << endl; // Uses floating point version
    // multiply("Hello", "World");       // Compilation error
    
    cout << processValue(5) << endl;     // 25
    cout << processValue(3.5) << endl;   // 12.25
    // processValue("Hello");            // Compilation error
    
#ifdef __cpp_concepts
    cout << "With concepts: " << addNumbers(10, 20) << endl;
    cout << "With concepts: " << addNumbers(1.5, 2.5) << endl;
#endif
    
    return 0;
}
```

---

## 🎮 Complete Example: Generic Utilities

```cpp
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

// Generic swap function
template <typename T>
void genericSwap(T& a, T& b) {
    T temp = move(a);
    a = move(b);
    b = move(temp);
}

// Generic bubble sort
template <typename T>
void bubbleSort(T arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                genericSwap(arr[j], arr[j + 1]);
            }
        }
    }
}

// Generic binary search
template <typename T>
int binarySearch(const T arr[], int size, const T& target) {
    int left = 0, right = size - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid;
        }
        
        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1; // Not found
}

// Generic print function
template <typename T>
void printArray(const string& label, T arr[], int size) {
    cout << label << ": ";
    for (int i = 0; i < size; i++) {
        cout << arr[i];
        if (i < size - 1) cout << ", ";
    }
    cout << endl;
}

// Generic comparison function
template <typename T>
bool compareArrays(const T arr1[], const T arr2[], int size) {
    for (int i = 0; i < size; i++) {
        if (arr1[i] != arr2[i]) {
            return false;
        }
    }
    return true;
}

int main() {
    cout << "=== Generic Utilities Demo ===" << endl;
    
    // Test with integers
    int intArr[] = {64, 34, 25, 12, 22, 11, 90};
    int intSize = sizeof(intArr) / sizeof(intArr[0]);
    
    printArray("Original integers", intArr, intSize);
    bubbleSort(intArr, intSize);
    printArray("Sorted integers", intArr, intSize);
    
    int target = 25;
    int index = binarySearch(intArr, intSize, target);
    cout << "Binary search for " << target << ": ";
    if (index != -1) {
        cout << "Found at index " << index << endl;
    } else {
        cout << "Not found" << endl;
    }
    
    cout << endl;
    
    // Test with doubles
    double doubleArr[] = {3.14, 1.59, 2.65, 0.99, 5.89};
    int doubleSize = sizeof(doubleArr) / sizeof(doubleArr[0]);
    
    printArray("Original doubles", doubleArr, doubleSize);
    bubbleSort(doubleArr, doubleSize);
    printArray("Sorted doubles", doubleArr, doubleSize);
    
    // Test with strings
    string strArr[] = {"Zebra", "Apple", "Orange", "Banana", "Grape"};
    int strSize = sizeof(strArr) / sizeof(strArr[0]);
    
    printArray("Original strings", strArr, strSize);
    bubbleSort(strArr, strSize);
    printArray("Sorted strings", strArr, strSize);
    
    string searchTarget = "Orange";
    index = binarySearch(strArr, strSize, searchTarget);
    cout << "Binary search for \"" << searchTarget << "\": ";
    if (index != -1) {
        cout << "Found at index " << index << endl;
    } else {
        cout << "Not found" << endl;
    }
    
    cout << endl;
    
    // Test array comparison
    int arr1[] = {1, 2, 3, 4, 5};
    int arr2[] = {1, 2, 3, 4, 5};
    int arr3[] = {1, 2, 3, 4, 6};
    
    cout << "arr1 == arr2: " << (compareArrays(arr1, arr2, 5) ? "True" : "False") << endl;
    cout << "arr1 == arr3: " << (compareArrays(arr1, arr3, 5) ? "True" : "False") << endl;
    
    return 0;
}
```

---

## ⚡ Performance Considerations

### Advantages
- ✅ **Zero Runtime Overhead**: Templates generate optimized code
- ✅ **Type Safety**: Compile-time type checking
- ✅ **Code Reuse**: Single implementation for multiple types
- ✅ **Inline Optimization**: Template functions are often inlined

### Considerations
- ⚠️ **Code Bloat**: Each instantiation generates separate code
- ⚠️ **Compilation Time**: Longer build times for complex templates
- ⚠️ **Binary Size**: Increased executable size

---

## 🐛 Common Pitfalls

| Problem | Solution |
|---------|----------|
| **Template definition in .cpp file** | Move definition to header file |
| **Type deduction ambiguity** | Use explicit template arguments |
| **Missing template arguments** | Provide default template parameters |
| **Linker errors** | Ensure template is visible to all translation units |

---

## ✅ Best Practices

1. **Use descriptive template parameter names** (`T` for type, `N` for number)
2. **Prefer `typename` over `class`** for template parameters
3. **Add `const` and `&`** for large objects to avoid copying
4. **Use `static_assert`** for better error messages
5. **Consider move semantics** for performance
6. **Document template requirements** and constraints

---

## 📚 Related Topics

- [Class Templates](02_Class_Templates.md)
- [Template Specialization](03_Template_Specialization.md)
- [Variadic Templates](04_Variadic_Templates.md)
- [Template Metaprogramming](05_Template_Metaprogramming.md)

---

## 🚀 Next Steps

Continue learning about:
- **Class Templates**: Generic classes and containers
- **Template Specialization**: Custom behavior for specific types
- **Advanced Template Techniques**: SFINAE, concepts, and metaprogramming

---
