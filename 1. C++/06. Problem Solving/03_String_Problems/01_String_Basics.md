# String Basics in C++ - Architecture, Memory Layout, and In-Depth Operations

## 📖 Overview

In C++, strings represent contiguous sequences of characters. Unlike languages with a single monolithic string type, C++ provides multiple complementary abstractions tailored for performance, safety, and zero-cost abstraction:
1. **C-Style Strings (`const char*`, `char[]`)**: Null-terminated character arrays inherited from C.
2. **`std::string`**: A dynamic, heap-backed (with SSO optimization) sequence container providing rich mutation operations and automatic memory management.
3. **`std::string_view` (C++17)**: A non-owning, zero-copy view over contiguous character sequences.

Mastering strings in C++ requires understanding **Small String Optimization (SSO)**, cache locality, amortized growth, and pointer lifetime semantics.

---

## 🏗️ `std::string` Internal Memory Architecture & SSO

Modern standard libraries (such as GCC `libstdc++`, Clang `libc++`, and MSVC STL) implement **Small String Optimization (SSO)**. Instead of allocating memory on the heap for every string, the string class uses an internal union that can store short strings directly inside the string object on the stack.

```
                           64-Bit std::string Memory Layout (24 or 32 Bytes)
 ┌────────────────────────────────────────────────────────────────────────────────────────┐
 │ Heap Mode (Size > SSO Capacity):                                                       │
 │  ┌────────────────────────┬────────────────────────┬────────────────────────────────┐  │
 │  │ char* ptr (8 Bytes)    │ size_t size (8 Bytes)  │ size_t capacity (8 Bytes)      │  │
 │  └───────────┬────────────┴────────────────────────┴────────────────────────────────┘  │
 │              │                                                                         │
 │              ▼ Points to Heap Memory                                                   │
 │             [ H | e | l | l | o | , |   | W | o | r | l | d | ! | \0 ]                 │
 ├────────────────────────────────────────────────────────────────────────────────────────┤
 │ SSO Mode (Size <= SSO Capacity, e.g. <= 15 or 22 chars):                               │
 │  ┌─────────────────────────────────────────────────┬────────────────────────────────┐  │
 │  │ char local_buffer[15] (Stack Allocated Buffer)  │ char sso_size_byte             │  │
 │  │ [ C | a | t | \0 | . | . | . | . | . | . | . ]  │ (Encodes size / SSO flag)      │  │
 │  └─────────────────────────────────────────────────┴────────────────────────────────┘  │
 └────────────────────────────────────────────────────────────────────────────────────────┘
```

### SSO Implications:
- **Zero Allocation Overhead**: Short strings (e.g., dictionary keys, short identifiers) require 0 calls to `operator new` or `malloc`.
- **Cache Locality**: Accessing small strings hits the CPU L1 data cache directly on the stack without pointer chasing.
- **Move Semantics**: Moving a heap-allocated string merely swaps 3 pointers ($O(1)$). Moving an SSO string must copy the local buffer into the destination stack object.

---

## ⚡ `std::string` vs. `std::string_view` (C++17 Zero-Copy)

A major source of inefficiency in string processing is unnecessary copying during substring queries and parameter passing.

| Feature | `std::string` | `std::string_view` |
| :--- | :--- | :--- |
| **Ownership** | Owning (manages lifetime of its buffer) | Non-owning (observer / pointer + length) |
| **Memory Allocation** | May allocate on heap (if $>$ SSO buffer) | **Never allocates** ($O(1)$ creation) |
| **Substring (`substr`)** | **$O(K)$** (creates a brand new copy) | **$O(1)$** (pointer arithmetic: `ptr + start`) |
| **Null Termination** | Always null-terminated (`.c_str()`) | Not guaranteed to be null-terminated! |
| **Lifetime Hazard** | Safe (owns its buffer) | **Dangerous**: Can dangle if owner dies |

```
                       std::string (Owning Buffer)
                      [ "Competitive Programming" ]
                                   ▲
                                   │ (Points directly into original memory)
             std::string_view sv = str.substr(12, 11);
                      [ ptr = &str[12], length = 11 ]  --> "Programming"
                      (Zero heap allocations! O(1) time!)
```

> [!WARNING]
> Never return a `std::string_view` bound to a temporary `std::string` returned by value! The temporary string will be destroyed at the end of the full expression, leaving the `string_view` pointing to dangling, invalid memory.

---

## 💻 Custom `DynamicString` Class Implementation

To master string mechanics for technical interviews and systems engineering, the following implementation constructs a custom `DynamicString` supporting the **Rule of 5**, geometric capacity doubling, and character indexing.

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>
#include <utility>
#include <stdexcept>
#include <cassert>

// Lightweight portable StringView demonstrating zero-copy slicing
class StringView {
private:
    const char* strData;
    size_t strLen;

public:
    constexpr StringView() : strData(nullptr), strLen(0) {}
    constexpr StringView(const char* s, size_t count) : strData(s), strLen(count) {}
    StringView(const char* s) : strData(s), strLen(s ? std::strlen(s) : 0) {}
    StringView(const std::string& s) : strData(s.data()), strLen(s.size()) {}

    constexpr const char* data() const noexcept { return strData; }
    constexpr size_t size() const noexcept { return strLen; }
    constexpr bool empty() const noexcept { return strLen == 0; }
    constexpr char operator[](size_t idx) const { return strData[idx]; }

    StringView substr(size_t pos, size_t count = npos) const {
        if (pos > strLen) throw std::out_of_range("StringView substr out of range");
        size_t rcount = std::min(count, strLen - pos);
        return StringView(strData + pos, rcount);
    }

    bool operator==(const StringView& other) const noexcept {
        if (strLen != other.strLen) return false;
        return std::memcmp(strData, other.strData, strLen) == 0;
    }
    bool operator==(const char* other) const noexcept {
        return *this == StringView(other);
    }

    friend std::ostream& operator<<(std::ostream& os, const StringView& sv) {
        for (size_t i = 0; i < sv.strLen; i++) os << sv.strData[i];
        return os;
    }

    static constexpr size_t npos = static_cast<size_t>(-1);
};

class DynamicString {
private:
    char* data;
    size_t length;
    size_t capacity;

    void reallocate(size_t newCap) {
        char* newData = new char[newCap + 1];
        if (data) {
            std::memcpy(newData, data, length);
            delete[] data;
        }
        data = newData;
        data[length] = '\0';
        capacity = newCap;
    }

public:
    // Default Constructor
    DynamicString() : data(new char[1]), length(0), capacity(0) {
        data[0] = '\0';
    }

    // C-String Constructor
    DynamicString(const char* str) {
        if (!str) {
            data = new char[1];
            data[0] = '\0';
            length = 0;
            capacity = 0;
            return;
        }
        length = std::strlen(str);
        capacity = length;
        data = new char[capacity + 1];
        std::memcpy(data, str, length + 1);
    }

    // Destructor (Rule of 5 - 1)
    ~DynamicString() {
        delete[] data;
    }

    // Copy Constructor (Rule of 5 - 2: Deep Copy)
    DynamicString(const DynamicString& other) 
        : length(other.length), capacity(other.capacity) {
        data = new char[capacity + 1];
        std::memcpy(data, other.data, length + 1);
    }

    // Move Constructor (Rule of 5 - 3: Resource Pilfering)
    DynamicString(DynamicString&& other) noexcept 
        : data(other.data), length(other.length), capacity(other.capacity) {
        other.data = nullptr;
        other.length = 0;
        other.capacity = 0;
    }

    // Friend Swap for Copy-and-Swap
    friend void swap(DynamicString& a, DynamicString& b) noexcept {
        using std::swap;
        swap(a.data, b.data);
        swap(a.length, b.length);
        swap(a.capacity, b.capacity);
    }

    // Unified Assignment Operator (Rule of 5 - 4 & 5)
    DynamicString& operator=(DynamicString other) noexcept {
        swap(*this, other);
        return *this;
    }

    // Appending a character (Amortized O(1))
    void push_back(char c) {
        if (length >= capacity) {
            size_t newCap = capacity == 0 ? 8 : capacity * 2;
            reallocate(newCap);
        }
        data[length++] = c;
        data[length] = '\0';
    }

    // Appending another string
    void append(const char* str) {
        if (!str) return;
        size_t strLen = std::strlen(str);
        if (length + strLen > capacity) {
            size_t newCap = std::max(capacity * 2, length + strLen);
            reallocate(newCap);
        }
        std::memcpy(data + length, str, strLen + 1);
        length += strLen;
    }

    // Element Access with bounds checking
    char& at(size_t index) {
        if (index >= length) throw std::out_of_range("DynamicString index out of range.");
        return data[index];
    }

    const char& at(size_t index) const {
        if (index >= length) throw std::out_of_range("DynamicString index out of range.");
        return data[index];
    }

    char& operator[](size_t index) { return data[index]; }
    const char& operator[](size_t index) const { return data[index]; }

    size_t size() const { return length; }
    size_t getCapacity() const { return capacity; }
    const char* c_str() const { return data ? data : ""; }
    bool empty() const { return length == 0; }

    // Fast zero-copy conversion to StringView
    StringView view() const {
        return StringView(data, length);
    }
};

int main() {
    std::cout << "=== String Basics & Architecture Comprehensive Test Harness ===\n\n";

    std::cout << "--- 1. Testing DynamicString Creation and Amortized Growth ---\n";
    DynamicString ds("Hello");
    std::cout << "  Initial string: \"" << ds.c_str() << "\" (Length: " << ds.size() 
              << ", Capacity: " << ds.getCapacity() << ")\n";

    ds.append(", World!");
    std::cout << "  Appended string: \"" << ds.c_str() << "\" (Length: " << ds.size() 
              << ", Capacity: " << ds.getCapacity() << ")\n";
    assert(ds.size() == 13);

    std::cout << "--- 2. Testing Rule of 5 (Copy and Move Semantics) ---\n";
    DynamicString copyStr = ds; // Copy constructor
    assert(copyStr.size() == ds.size());
    std::cout << "  Deep copy successfully created.\n";

    DynamicString moveStr = std::move(ds); // Move constructor
    assert(moveStr.size() == 13);
    assert(ds.empty()); // Original pilfered
    std::cout << "  Move constructor pilfered pointer. Original is empty: " 
              << (ds.empty() ? "YES" : "NO") << "\n\n";

    std::cout << "--- 3. Zero-Copy StringView Slicing ---\n";
    std::string fullText = "Algorithms and Data Structures in C++";
    StringView sv1(fullText);
    StringView subView = sv1.substr(15, 15); // "Data Structures"

    std::cout << "  Original std::string: \"" << fullText << "\"\n";
    std::cout << "  Zero-copy Substring View: \"" << subView << "\" (Size: " << subView.size() << ")\n";
    assert(subView == "Data Structures");

    // Pointer address verification: subView points directly into fullText!
    std::cout << "  Address of fullText[15] : " << static_cast<const void*>(&fullText[15]) << "\n";
    std::cout << "  Address inside subView  : " << static_cast<const void*>(subView.data()) << "\n";
    assert(&fullText[15] == subView.data());
    std::cout << "  Zero-copy address match: VERIFIED (Exact same memory address!)\n\n";

    std::cout << "--- 4. String Character Encoding & Bitwise Operations ---\n";
    char upper = 'G';
    char lower = upper | 32; // Fast ASCII lowercase conversion
    std::cout << "  Bitwise lowercase: '" << upper << "' | 32 = '" << lower << "'\n";
    assert(lower == 'g');

    char backUpper = lower & ~32; // Fast ASCII uppercase conversion
    std::cout << "  Bitwise uppercase: '" << lower << "' & ~32 = '" << backUpper << "'\n";
    assert(backUpper == 'G');

    std::cout << "\n=== All String Basics Tests Completed Successfully! ===\n";
    return 0;
}
```

---

## 📊 Complexity Analysis of String Operations

| Operation | `std::string` | `std::string_view` | C-Style String (`char*`) |
| :--- | :--- | :--- | :--- |
| **Length (`size()`)** | $O(1)$ (stored counter) | $O(1)$ (stored counter) | $O(N)$ (requires `strlen` scan to `\0`) |
| **Character Access (`[]`)**| $O(1)$ | $O(1)$ | $O(1)$ |
| **Substring (`substr`)** | **$O(K)$** (Heap allocate + copy)| **$O(1)$** (Pointer shift) | $O(K)$ (Requires manual buffer copy) |
| **Append (`+=`, `push_back`)**| $O(1)$ amortized | N/A (Immutable view) | $O(N + M)$ (`strcat` scan + copy) |
| **Concatenation (`+`)** | $O(N + M)$ | N/A | $O(N + M)$ |
| **Comparison (`==`, `<`)**| $O(\min(N, M))$ | $O(\min(N, M))$ | $O(\min(N, M))$ (`strcmp`) |

---

## 💡 Practical Interview Insights

1. **Pass by `std::string_view` vs `const std::string&`**:
   - Prefer `std::string_view` for read-only parameters: it accepts `const char*`, string literals, and `std::string` without forcing string literal allocations.
2. **Pre-allocating with `reserve()`**:
   - If string size is known beforehand (e.g., reading a line or constructing output), call `s.reserve(expectedSize)` to avoid intermediate geometric reallocations.
3. **Small String Optimization Threshold**:
   - On 64-bit systems, strings of up to 15 characters (libstdc++) or 22 characters (MSVC) allocate zero heap memory.
