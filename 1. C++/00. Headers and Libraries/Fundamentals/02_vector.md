# 02_vector.md - Vector Container

The `vector` is one of the most commonly used containers in C++ STL. It provides a dynamic array that can grow or shrink in size.

## 📖 Overview

`vector` is a sequence container that encapsulates dynamic size arrays. Elements are stored contiguously in memory, allowing fast random access and efficient cache utilization.

## 🎯 Key Features

- **Dynamic sizing** - Can grow and shrink at runtime
- **Contiguous memory** - Elements stored in consecutive memory locations
- **Random access** - O(1) access time with `[]` operator
- **Automatic memory management** - Handles allocation and deallocation
- **Iterator support** - Works with STL algorithms

## 🔧 Basic Operations

### Declaration and Initialization
```cpp
#include <vector>
#include <iostream>

int main() {
    // Different ways to create vectors
    
    vector<int> v1;                    // Empty vector
    vector<int> v2(5);                 // Vector with 5 elements (all 0)
    vector<int> v3(5, 10);             // Vector with 5 elements (all 10)
    vector<int> v4 = {1, 2, 3, 4, 5}; // Initializer list
    vector<int> v5(v4);                // Copy constructor
    vector<int> v6(v4.begin(), v4.end()); // Range constructor
    
    return 0;
}
```

### Adding Elements
```cpp
vector<int> vec;

vec.push_back(10);     // Add element to end
vec.push_back(20);
vec.push_back(30);

vec.insert(vec.begin() + 1, 15);  // Insert at position 1

// Using emplace_back (more efficient)
vec.emplace_back(40);  // Construct in-place
```

### Accessing Elements
```cpp
vector<int> vec = {10, 20, 30, 40, 50};

// Random access
cout << vec[0] << endl;      // 10 (no bounds checking)
cout << vec.at(1) << endl;   // 20 (with bounds checking)

// Front and back
cout << vec.front() << endl; // 10
cout << vec.back() << endl;  // 50

// Iterator access
auto it = vec.begin();
cout << *it << endl;         // 10
```

### Removing Elements
```cpp
vector<int> vec = {10, 20, 30, 40, 50};

vec.pop_back();              // Remove last element
vec.erase(vec.begin() + 1);  // Remove element at position 1
vec.erase(vec.begin(), vec.begin() + 2); // Remove range

vec.clear();                 // Remove all elements
```

## 📊 Size and Capacity

```cpp
vector<int> vec = {1, 2, 3, 4, 5};

cout << "Size: " << vec.size() << endl;           // 5
cout << "Capacity: " << vec.capacity() << endl;   // >= 5
cout << "Max size: " << vec.max_size() << endl;   // Very large number
cout << "Empty: " << vec.empty() << endl;         // false

vec.resize(10);             // Resize to 10 elements
vec.reserve(20);            // Reserve capacity for 20 elements
vec.shrink_to_fit();        // Reduce capacity to fit size
```

## 🎮 Practical Examples

### Example 1: Basic Vector Operations
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    vector<int> numbers;
    
    // Add elements
    for (int i = 1; i <= 5; i++) {
        numbers.push_back(i * 10);
    }
    
    // Display elements
    cout << "Elements: ";
    for (int num : numbers) {
        cout << num << " ";
    }
    cout << endl;
    
    // Access and modify
    numbers[2] = 35;
    cout << "After modification: ";
    for (int num : numbers) {
        cout << num << " ";
    }
    cout << endl;
    
    // Find element
    auto it = find(numbers.begin(), numbers.end(), 35);
    if (it != numbers.end()) {
        cout << "Found 35 at position: " << distance(numbers.begin(), it) << endl;
    }
    
    return 0;
}
```

### Example 2: Vector of Strings
```cpp
#include <iostream>
#include <vector>
#include <string>

int main() {
    vector<string> names;
    
    names.push_back("Alice");
    names.push_back("Bob");
    names.push_back("Charlie");
    
    // Display names
    cout << "Names:" << endl;
    for (const string& name : names) {
        cout << "- " << name << endl;
    }
    
    // Sort names
    sort(names.begin(), names.end());
    
    cout << "\nSorted names:" << endl;
    for (const string& name : names) {
        cout << "- " << name << endl;
    }
    
    return 0;
}
```

### Example 3: 2D Vector (Matrix)
```cpp
#include <iostream>
#include <vector>

int main() {
    // Create 3x4 matrix
    vector<vector<int>> matrix(3, vector<int>(4));
    
    // Fill matrix with values
    int value = 1;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            matrix[i][j] = value++;
        }
    }
    
    // Display matrix
    cout << "3x4 Matrix:" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            cout << matrix[i][j] << "\t";
        }
        cout << endl;
    }
    
    return 0;
}
```

### Example 4: Vector as Stack
```cpp
#include <iostream>
#include <vector>

int main() {
    vector<int> stack;
    
    // Push operations
    stack.push_back(10);
    stack.push_back(20);
    stack.push_back(30);
    
    cout << "Top element: " << stack.back() << endl;
    
    // Pop operations
    while (!stack.empty()) {
        cout << "Popped: " << stack.back() << endl;
        stack.pop_back();
    }
    
    return 0;
}
```

## ⚡ Performance Considerations

### Time Complexity
| Operation | Time Complexity |
|-----------|-----------------|
| Access (`[]`, `at`) | O(1) |
| Push/Pop Back | O(1) amortized |
| Insert/Erase | O(n) |
| Front/Back | O(1) |
| Size/Empty | O(1) |

### Memory Management
```cpp
vector<int> vec;

// Bad: Multiple reallocations
for (int i = 0; i < 1000; i++) {
    vec.push_back(i);  // May cause multiple reallocations
}

// Good: Reserve space beforehand
vector<int> vec2;
vec2.reserve(1000);    // Reserve capacity
for (int i = 0; i < 1000; i++) {
    vec2.push_back(i);  // No reallocations
}
```

## 🎯 Common Vector Patterns

### Pattern 1: Reading Unknown Number of Inputs
```cpp
vector<int> readNumbers() {
    vector<int> numbers;
    int num;
    
    while (cin >> num) {  // Read until EOF
        numbers.push_back(num);
    }
    
    return numbers;
}
```

### Pattern 2: Filtering Elements
```cpp
vector<int> filterEven(const vector<int>& numbers) {
    vector<int> even;
    
    for (int num : numbers) {
        if (num % 2 == 0) {
            even.push_back(num);
        }
    }
    
    return even;
}
```

### Pattern 3: Removing Elements While Iterating
```cpp
void removeMultiplesOfThree(vector<int>& numbers) {
    numbers.erase(
        remove_if(numbers.begin(), numbers.end(),
                 [](int x) { return x % 3 == 0; }),
        numbers.end()
    );
}
```

## 🐛 Common Pitfalls & Solutions

### 1. Iterator Invalidation
```cpp
// Problem
vector<int> vec = {1, 2, 3, 4, 5};
for (auto it = vec.begin(); it != vec.end(); it++) {
    if (*it % 2 == 0) {
        vec.erase(it);  // Iterator becomes invalid!
    }
}

// Solution
for (auto it = vec.begin(); it != vec.end(); ) {
    if (*it % 2 == 0) {
        it = vec.erase(it);  // Update iterator
    } else {
        it++;
    }
}
```

### 2. Out of Bounds Access
```cpp
vector<int> vec = {1, 2, 3};

// Dangerous - no bounds checking
int x = vec[10];  // Undefined behavior

// Safe - with bounds checking
try {
    int y = vec.at(10);  // Throws exception
} catch (const out_of_range& e) {
    cerr << "Index out of range!" << endl;
}
```

### 3. Reference Invalidation
```cpp
vector<int> vec = {1, 2, 3};
int& ref = vec[0];
vec.push_back(4);  // May reallocate and invalidate ref
// ref is now invalid!
```

## 🎨 Advanced Techniques

### Custom Vector with Custom Allocator
```cpp
template<typename T>
class SafeVector {
private:
    vector<T> data;
    
public:
    void safe_push_back(const T& value) {
        // Ensure capacity before pushing
        if (data.size() == data.capacity()) {
            data.reserve(data.capacity() * 2);
        }
        data.push_back(value);
    }
    
    // Other safe operations...
};
```

### Vector of Pointers
```cpp
vector<unique_ptr<int>> ptr_vec;
ptr_vec.push_back(make_unique<int>(42));

// Automatic memory management
for (auto& ptr : ptr_vec) {
    cout << *ptr << " ";
}
```

## 📚 Related Containers

- `array.md` - Fixed-size array
- `deque.md` - Double-ended queue
- `list.md` - Doubly linked list
- `string.md` - String container

## 🚀 Best Practices

1. **Use `reserve()`** when you know approximate size
2. **Prefer `at()` over `[]`** when bounds checking is needed
3. **Use range-based for loops** for clean iteration
4. **Be careful with iterator invalidation** during modifications
5. **Consider `emplace_back()`** over `push_back()` for complex objects

## 🎯 When to Use Vector

✅ **Use vector when:**
- You need random access
- Elements are stored contiguously
- You need fast iteration
- Size changes frequently
- Cache performance is important

❌ **Avoid vector when:**
- You need frequent insertion/deletion in middle
- You need guaranteed reference stability
- Memory overhead is critical
- You need O(1) insertion at front
---

## Next Step

- Go to [03_string.md](03_string.md) to continue with string.
