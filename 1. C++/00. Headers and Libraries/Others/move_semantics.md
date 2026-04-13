# Move Semantics - Transfer of Ownership

Move semantics (C++11) allow resources — heap memory, file handles, network connections — to be *transferred* rather than *copied*, eliminating expensive deep copies and enabling types that cannot be copied at all.

## 📖 Overview

Before C++11 every value was either copied or passed by reference. Move semantics introduce a third option: **steal** the internal resources of a temporary (or explicitly-moved) object, leaving it in a valid but unspecified state.

Key ideas:
- **lvalue** — has a name / address; can appear on the left of `=`
- **rvalue** — temporary; no persistent identity; can be "stolen from"
- **rvalue reference** (`T&&`) — binds to rvalues; used in move constructors and move assignment
- **`std::move`** — casts any object to an rvalue reference (doesn't actually move anything)
- **Perfect forwarding** — forwards arguments preserving their value category

## 🎯 Key Components

### Value Categories
```
expressions
├── lvalue  — has identity, not movable by default (variables, references)
├── xvalue  — has identity AND is movable (result of std::move, function returning T&&)
└── prvalue — no identity, movable (temporaries, literals)
    xvalue + prvalue = rvalue  (can bind to T&&)
```

### The Rule of Five (C++11)
If you define any of these, consider defining all five:
1. Destructor
2. Copy constructor
3. Copy assignment operator
4. **Move constructor**
5. **Move assignment operator**

## 🔧 Basic Operations

### Writing a Move Constructor and Move Assignment
```cpp
#include <iostream>
#include <cstring>
#include <utility>

class Buffer {
    char* data_;
    size_t size_;

public:
    // Constructor
    explicit Buffer(size_t n) : data_(new char[n]), size_(n) {
        std::fill(data_, data_ + n, 0);
        std::cout << "Buffer(" << n << ") constructed\n";
    }

    // Destructor
    ~Buffer() {
        delete[] data_;
        std::cout << "Buffer destroyed\n";
    }

    // Copy constructor — deep copy (expensive)
    Buffer(const Buffer& other) : data_(new char[other.size_]), size_(other.size_) {
        std::memcpy(data_, other.data_, size_);
        std::cout << "Buffer copy-constructed (deep copy)\n";
    }

    // Move constructor — steal the pointer (cheap)
    Buffer(Buffer&& other) noexcept
        : data_(other.data_), size_(other.size_) {
        other.data_ = nullptr; // leave other in valid state
        other.size_ = 0;
        std::cout << "Buffer move-constructed (transfer)\n";
    }

    // Copy assignment
    Buffer& operator=(const Buffer& other) {
        if (this != &other) {
            delete[] data_;
            data_ = new char[other.size_];
            size_ = other.size_;
            std::memcpy(data_, other.data_, size_);
        }
        std::cout << "Buffer copy-assigned\n";
        return *this;
    }

    // Move assignment
    Buffer& operator=(Buffer&& other) noexcept {
        if (this != &other) {
            delete[] data_;
            data_ = other.data_;
            size_ = other.size_;
            other.data_ = nullptr;
            other.size_ = 0;
        }
        std::cout << "Buffer move-assigned\n";
        return *this;
    }

    size_t size() const { return size_; }
};

int main() {
    Buffer a(1024);           // construct
    Buffer b(std::move(a));   // move construct — no deep copy
    std::cout << "a.size=" << a.size() << " b.size=" << b.size() << "\n";

    Buffer c(512);
    c = std::move(b);         // move assign
    std::cout << "b.size=" << b.size() << " c.size=" << c.size() << "\n";
    return 0;
}
```

### `std::move` — Explicit Move
```cpp
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::string s1 = "Hello, World!";
    std::string s2 = std::move(s1); // s1 is now empty (valid but unspecified)

    std::cout << "s1: '" << s1 << "'\n"; // "" (moved-from state)
    std::cout << "s2: '" << s2 << "'\n"; // "Hello, World!"

    // Moving into a container avoids copying
    std::vector<std::string> words;
    std::string word = "expensive_string_data";
    words.push_back(std::move(word)); // no copy made
    std::cout << "word is now: '" << word << "'\n"; // empty

    return 0;
}
```

### Perfect Forwarding with `std::forward`
```cpp
#include <iostream>
#include <utility>
#include <string>

void process(std::string& s)  { std::cout << "lvalue: " << s << "\n"; }
void process(std::string&& s) { std::cout << "rvalue: " << s << "\n"; }

// Without perfect forwarding:
template <typename T>
void forwardBad(T arg) { process(arg); } // always calls lvalue version

// With perfect forwarding:
template <typename T>
void forwardGood(T&& arg) { process(std::forward<T>(arg)); } // preserves category

int main() {
    std::string s = "hello";
    forwardBad(s);              // lvalue: hello
    forwardBad(std::move(s));   // lvalue: hello (WRONG — rvalue treated as lvalue)

    s = "hello";
    forwardGood(s);             // lvalue: hello  (correct)
    forwardGood(std::move(s));  // rvalue: hello  (correct)
    return 0;
}
```

## 🎮 Practical Examples

### Example 1: Return Value Optimisation and Move
```cpp
#include <iostream>
#include <vector>
#include <string>

// The compiler applies NRVO (Named Return Value Optimisation)
// If NRVO doesn't apply, the move constructor is used automatically
std::vector<int> buildLargeVector(int n) {
    std::vector<int> result;
    result.reserve(n);
    for (int i = 0; i < n; i++) result.push_back(i);
    return result; // NRVO or implicit move — no copy
}

std::string concatenate(std::string a, const std::string& b) {
    a += b; // a is already a local copy — modify and move out
    return a; // implicit move (a is about to die)
}

int main() {
    auto v = buildLargeVector(1'000'000); // zero copies
    std::cout << "Vector size: " << v.size() << "\n";

    std::string result = concatenate("Hello", ", World!");
    std::cout << result << "\n";
    return 0;
}
```

### Example 2: Move-Only Type (Unique Ownership)
```cpp
#include <iostream>
#include <memory>
#include <vector>

class FileHandle {
    int fd_;

public:
    explicit FileHandle(int fd) : fd_(fd) {
        std::cout << "FileHandle(" << fd_ << ") opened\n";
    }

    ~FileHandle() {
        if (fd_ >= 0) {
            std::cout << "FileHandle(" << fd_ << ") closed\n";
        }
    }

    // Move-only: delete copy, allow move
    FileHandle(const FileHandle&)            = delete;
    FileHandle& operator=(const FileHandle&) = delete;

    FileHandle(FileHandle&& other) noexcept : fd_(other.fd_) {
        other.fd_ = -1; // mark as "moved-from"
        std::cout << "FileHandle moved\n";
    }

    FileHandle& operator=(FileHandle&& other) noexcept {
        if (this != &other) {
            if (fd_ >= 0) std::cout << "FileHandle(" << fd_ << ") closed\n";
            fd_ = other.fd_;
            other.fd_ = -1;
        }
        return *this;
    }

    int fd() const { return fd_; }
};

int main() {
    FileHandle f1(42);
    FileHandle f2(std::move(f1)); // transfer ownership
    std::cout << "f1.fd=" << f1.fd() << " f2.fd=" << f2.fd() << "\n";

    std::vector<FileHandle> handles;
    handles.push_back(FileHandle(10));
    handles.push_back(FileHandle(11));

    std::cout << "Handles stored: " << handles.size() << "\n";
    return 0;
}
```

### Example 3: `emplace_back` vs `push_back`
```cpp
#include <iostream>
#include <vector>
#include <string>

struct Person {
    std::string name;
    int age;

    Person(const std::string& n, int a) : name(n), age(a) {
        std::cout << "Constructed: " << name << "\n";
    }

    Person(const Person& other) : name(other.name), age(other.age) {
        std::cout << "Copy: " << name << "\n";
    }

    Person(Person&& other) noexcept : name(std::move(other.name)), age(other.age) {
        std::cout << "Move: " << name << "\n";
    }
};

int main() {
    std::vector<Person> people;
    people.reserve(4);

    // push_back with temporary: constructs, then moves into vector
    std::cout << "--- push_back ---\n";
    people.push_back(Person("Alice", 30)); // construct + move

    // emplace_back: constructs *in place* — only one construction
    std::cout << "--- emplace_back ---\n";
    people.emplace_back("Bob", 25); // only one construction

    std::cout << "People: " << people.size() << "\n";
    return 0;
}
```

### Example 4: Swap via Move
```cpp
#include <iostream>
#include <string>
#include <utility>

// Classic swap copies twice; move-based swap moves twice (3 operations, no heap alloc)
template <typename T>
void mySwap(T& a, T& b) noexcept(std::is_nothrow_move_constructible_v<T> &&
                                  std::is_nothrow_move_assignable_v<T>) {
    T tmp = std::move(a);
    a     = std::move(b);
    b     = std::move(tmp);
}

int main() {
    std::string x = "Hello";
    std::string y = "World";

    std::cout << "Before: x=" << x << " y=" << y << "\n";
    mySwap(x, y);
    std::cout << "After:  x=" << x << " y=" << y << "\n";

    // std::swap uses move semantics internally too
    std::swap(x, y);
    std::cout << "After std::swap: x=" << x << " y=" << y << "\n";

    return 0;
}
```

## ⚡ Performance Tips

### Mark Move Operations `noexcept`
```cpp
// STL containers (vector, map, etc.) can use move instead of copy during reallocation
// ONLY if the move constructor is noexcept
// Without noexcept: vector falls back to copy for exception safety

class MyType {
public:
    MyType(MyType&&) noexcept;            // vector WILL use this
    MyType& operator=(MyType&&) noexcept; // vector WILL use this
};
```

### Return Local Variables by Value (Let Compiler Optimise)
```cpp
// Don't write std::move on a return statement — it DISABLES NRVO
std::string bad() {
    std::string result = "hello";
    return std::move(result); // WRONG: disables NRVO, forces a move instead of elision
}

std::string good() {
    std::string result = "hello";
    return result; // compiler can elide (zero-cost) or at worst moves
}
```

### Prefer `emplace_back` Over `push_back` for In-Place Construction
```cpp
std::vector<std::string> v;
v.push_back("hello");   // constructs temporary, then moves
v.emplace_back("hello"); // constructs directly in vector's memory
```

## 🐛 Common Pitfalls & Solutions

### 1. Using a Moved-From Object
```cpp
std::string s = "hello";
std::string t = std::move(s);
std::cout << s; // OK syntactically, but s is in a valid but unspecified state
// Never assume what a moved-from object contains

// Solution: don't use moved-from objects, or reassign them first
s = "new value"; // safe to use again after reassignment
```

### 2. `std::move` on a `const` Object Is a Copy
```cpp
const std::string s = "hello";
std::string t = std::move(s); // COPIES s — can't move a const!
// Solution: remove const, or accept a copy is necessary
```

### 3. Forgetting `noexcept` on Move Operations
```cpp
class Problematic {
public:
    Problematic(Problematic&&) {} // no noexcept — vector won't use this during resize
};

class Correct {
public:
    Correct(Correct&&) noexcept {} // vector will use this safely
};
```

### 4. Moving in a Loop Index Variable
```cpp
// Problem: loop variable moved in loop body
for (auto item : collection) {
    process(std::move(item)); // OK only if item is freshly copied each iteration
}

// Problem: moving from a reference
for (auto& item : collection) {
    process(std::move(item)); // DANGEROUS — leaves collection elements in moved-from state!
}
```

## 🎯 Best Practices

1. **Mark move constructors and move assignment `noexcept`** — STL containers require it for optimisations
2. **Don't `std::move` on a return statement** — you'll disable NRVO
3. **Follow the Rule of Five** — if you write one special member, write all five
4. **Use `= default`** for move operations when the compiler can synthesise them correctly
5. **Prefer `emplace_back`** over `push_back` when constructing in place
6. **Don't use moved-from objects** — reassign before reuse

## 📚 Related Topics

- [`smart_pointers.md`](smart_pointers.md) — `unique_ptr` is the canonical move-only type
- [`templates.md`](templates.md) — Perfect forwarding (`std::forward`) in template contexts
- [`lambda_expressions.md`](lambda_expressions.md) — Init captures (`[p = std::move(p)]`)
- [`memory_management.md`](memory_management.md) — RAII and ownership

## 🚀 Next Steps

1. Add move constructor and move assignment to your own resource-owning classes
2. Profile `push_back` vs `emplace_back` in a tight loop
3. Explore `std::exchange` — a utility that moves a new value in and returns the old one
4. Study Copy-and-Swap idiom and how move semantics simplify it
---

## Next Step

- Go to [multithreading.md](multithreading.md) to continue with multithreading.
