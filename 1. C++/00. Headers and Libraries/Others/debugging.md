# Debugging - Practical Debugging Techniques in C++

Debugging is the systematic process of finding and fixing bugs. C++ offers compile-time checks, assertions, sanitisers, and interactive debuggers to help you locate problems efficiently.

## 📖 Overview

Effective debugging follows a disciplined workflow:
1. **Reproduce** — reliably trigger the bug before changing any code
2. **Isolate** — narrow down which function/line is responsible
3. **Understand** — know *why* it fails, not just *where*
4. **Fix** — apply the minimal correct change
5. **Verify** — confirm the fix and run all tests

Never guess. Every step should be driven by evidence.

## 🎯 Key Tools

### Compile-Time Checks
| Tool | Purpose |
|------|---------|
| `-Wall -Wextra -Wpedantic` | Enable all helpful compiler warnings |
| `-Werror` | Treat warnings as errors |
| `static_assert` | Assert type/value conditions at compile time |
| `<type_traits>` | Compile-time type checks in templates |

### Runtime Checks
| Tool | Purpose |
|------|---------|
| `assert` / `<cassert>` | Abort on false assumption in debug builds |
| `-fsanitize=address` (ASan) | Detect heap overflows, use-after-free |
| `-fsanitize=undefined` (UBSan) | Detect signed overflow, null deref, etc. |
| `-fsanitize=thread` (TSan) | Detect data races |
| `Valgrind` | Memory leak and error detection |

### Debuggers
| Tool | Platform |
|------|---------|
| `gdb` | Linux / macOS |
| `lldb` | macOS / Linux (LLVM) |
| Visual Studio Debugger | Windows |

## 🔧 Basic Operations

### `assert` and `static_assert`
```cpp
#include <cassert>
#include <type_traits>
#include <iostream>
#include <vector>

// Compile-time assertion
static_assert(sizeof(int) == 4, "int must be 4 bytes");

template <typename T>
T divide(T a, T b) {
    static_assert(std::is_arithmetic_v<T>, "divide requires arithmetic type");
    assert(b != 0 && "Division by zero!");
    return a / b;
}

int main() {
    std::cout << divide(10, 2) << "\n"; // 5

    std::vector<int> v = {1, 2, 3};
    assert(v.size() == 3);
    std::cout << "All assertions passed\n";
    return 0;
}
```

### Debug Log Macros
```cpp
#include <iostream>

#ifdef NDEBUG
    #define LOG_DEBUG(msg) ((void)0)
#else
    #define LOG_DEBUG(msg) \
        std::cerr << "[DEBUG] " << __FILE__ << ":" << __LINE__ \
                  << " (" << __func__ << ") " << msg << "\n"
#endif

#define LOG_ERROR(msg) \
    std::cerr << "[ERROR] " << __FILE__ << ":" << __LINE__ << " " << msg << "\n"

int processValue(int x) {
    LOG_DEBUG("called with x=" << x);
    if (x < 0) { LOG_ERROR("Negative input: " << x); return -1; }
    int result = x * x;
    LOG_DEBUG("Result: " << result);
    return result;
}

int main() {
    processValue(5);
    processValue(-3);
    return 0;
}
```

### Using GDB (Compile with `-g -O0`)
```cpp
// Compile: g++ -g -O0 -Wall prog.cpp -o prog
// Run:     gdb ./prog
//
// Key GDB commands:
//   run                  — start program
//   break main           — breakpoint at main
//   break file.cpp:42    — breakpoint at line 42
//   next / step          — step over / step into
//   print x              — print variable x
//   info locals          — show all local variables
//   backtrace (bt)       — print call stack
//   watch x              — break when x changes
//   continue (c)         — resume execution
//   quit                 — exit gdb

int sum(int a, int b) { return a + b; }

int main() {
    int x = 10, y = 20;
    int result = sum(x, y);
    std::cout << result << "\n";
    return 0;
}
```

### Address Sanitiser — Compile with `-fsanitize=address -g`
```cpp
#include <iostream>
#include <memory>
#include <vector>

void detectHeapOverflow() {
    std::vector<int> v(5);
    // v[10] = 42;  // ASan catches heap-buffer-overflow

    v.at(2) = 42;  // safe: throws if out of range
    std::cout << v[2] << "\n";
}

void detectUseAfterFree() {
    // int* p = new int(42); delete p; std::cout << *p; // ASan catches use-after-free

    auto p = std::make_unique<int>(42);
    std::cout << *p << "\n"; // safe
}

int main() {
    detectHeapOverflow();
    detectUseAfterFree();
    return 0;
}
```

## 🎮 Practical Examples

### Example 1: Structured Logger Class
```cpp
#include <iostream>
#include <sstream>
#include <string>
#include <chrono>
#include <iomanip>

enum class LogLevel { DEBUG, INFO, WARN, ERROR };

class Logger {
    std::ostream& out_;
    LogLevel minLevel_;

    const char* levelStr(LogLevel lv) const {
        switch (lv) {
            case LogLevel::DEBUG: return "DEBUG";
            case LogLevel::INFO:  return "INFO ";
            case LogLevel::WARN:  return "WARN ";
            case LogLevel::ERROR: return "ERROR";
        }
        return "?????";
    }

public:
    Logger(std::ostream& out = std::cerr, LogLevel min = LogLevel::DEBUG)
        : out_(out), minLevel_(min) {}

    template <typename T>
    void log(LogLevel lv, const T& msg, const char* file, int line) {
        if (lv < minLevel_) return;
        out_ << "[" << levelStr(lv) << "] " << file << ":" << line << " " << msg << "\n";
    }
};

#define LOG(logger, level, msg) \
    do { \
        std::ostringstream _ss; _ss << msg; \
        (logger).log(level, _ss.str(), __FILE__, __LINE__); \
    } while (0)

int main() {
    Logger logger;
    LOG(logger, LogLevel::INFO,  "Application started");
    LOG(logger, LogLevel::DEBUG, "Processing " << 42 << " items");
    LOG(logger, LogLevel::WARN,  "Low memory: 512 MB remaining");
    LOG(logger, LogLevel::ERROR, "Failed to open file: data.csv");
    return 0;
}
```

### Example 2: Minimal Reproducer — Bisect Debugging
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

// Buggy: doesn't guard against n > v.size()
int findMaxBuggy(const std::vector<int>& v, int n) {
    int max = v[0];
    for (int i = 1; i < n; i++) {  // may read past end!
        if (v[i] > max) max = v[i];
    }
    return max;
}

// Fixed: clamp n to actual size
int findMaxFixed(const std::vector<int>& v, int n) {
    assert(!v.empty() && "Vector must not be empty");
    int safeN = std::min(n, (int)v.size());
    int max = v[0];
    for (int i = 1; i < safeN; i++) {
        if (v[i] > max) max = v[i];
    }
    return max;
}

int main() {
    std::vector<int> v = {3, 1, 4, 1, 5, 9, 2, 6};

    std::cout << "Max of 4: " << findMaxFixed(v, 4)              << "\n"; // 4
    std::cout << "Max of all: " << findMaxFixed(v, (int)v.size()) << "\n"; // 9
    return 0;
}
```

### Example 3: UBSan — Catching Undefined Behaviour
```cpp
// Compile: g++ -fsanitize=undefined -g prog.cpp
#include <iostream>
#include <climits>

void integerOverflow() {
    int x = INT_MAX;
    // UBSan reports: signed integer overflow
    // int overflow = x + 1; // UB!

    if (x < INT_MAX) {
        int safe = x + 1;
        std::cout << safe << "\n";
    } else {
        std::cout << "Would overflow INT_MAX!\n";
    }
}

void nullPointerDeref() {
    int* p = nullptr;
    // UBSan reports: null pointer dereference
    // int val = *p; // UB!

    if (p) std::cout << *p << "\n";
    else   std::cout << "Null pointer — skipped\n";
}

void arrayOutOfBounds() {
    int arr[4] = {1, 2, 3, 4};
    // UBSan reports: index 10 is out of bounds
    // arr[10] = 99; // UB!
    for (int i = 0; i < 4; i++) std::cout << arr[i] << " ";
    std::cout << "\n";
}

int main() {
    integerOverflow();
    nullPointerDeref();
    arrayOutOfBounds();
    return 0;
}
```

### Example 4: Watchdog for Detecting Hangs
```cpp
#include <iostream>
#include <thread>
#include <atomic>
#include <chrono>
#include <functional>

class Watchdog {
    std::atomic<bool> running_{true};
    std::atomic<bool> petted_{true};
    std::thread monitor_;

public:
    Watchdog(int timeoutMs, std::function<void()> onTimeout) {
        monitor_ = std::thread([this, timeoutMs, onTimeout]() {
            while (running_.load()) {
                std::this_thread::sleep_for(std::chrono::milliseconds(timeoutMs));
                if (!petted_.exchange(false)) {
                    std::cerr << "[WATCHDOG] Timeout! Task appears hung.\n";
                    onTimeout();
                    return;
                }
            }
        });
    }

    void pet() { petted_.store(true); } // prove alive

    ~Watchdog() {
        running_.store(false);
        if (monitor_.joinable()) monitor_.join();
    }
};

void longTask(Watchdog& wd) {
    for (int i = 0; i < 8; i++) {
        std::cout << "Step " << i << "\n";
        wd.pet();
        std::this_thread::sleep_for(std::chrono::milliseconds(60));
    }
}

int main() {
    bool timedOut = false;
    Watchdog wd(200, [&timedOut]() { timedOut = true; });

    longTask(wd);

    if (!timedOut) std::cout << "Task completed successfully\n";
    return 0;
}
```

## ⚡ Performance Tips

### Debug vs Release Builds
```bash
# Full debug: all checks, no optimisation
g++ -g -O0 -DDEBUG -Wall -Wextra -fsanitize=address,undefined prog.cpp

# Release: no debug, full optimisation, assertions disabled
g++ -O3 -DNDEBUG prog.cpp
```

### `assert` Is Free in Release
```cpp
// assert() becomes a no-op when NDEBUG is defined
// Use it liberally — it costs nothing in production
assert(ptr != nullptr); // compiled out with -DNDEBUG
```

### Fix Warnings Before Running
```bash
# Many bugs are caught at compile time with proper warning flags
g++ -Wall -Wextra -Wshadow -Wnull-dereference -Wformat=2 prog.cpp
```

## 🐛 Common Debugging Mistakes

### 1. Modifying Code While Debugging
```cpp
// Adding print statements changes timing — can hide or create bugs (Heisenbug)
// Use a debugger to inspect state without modifying the program
```

### 2. Ignoring Compiler Warnings
```bash
# Uninitialized variable, sign comparison, unused variable — all are real bugs
# Enable -Wall -Wextra and fix every warning
```

### 3. Debugging Optimised Builds
```bash
# -O2 reorders and inlines code — stepping is confusing and inaccurate
# Always debug with -O0 -g
```

### 4. Not Isolating the Minimal Case
```cpp
// Large codebases have too many variables
// Create the SMALLEST possible program that reproduces the bug
// This clarifies the root cause and makes it reproducible for others
```

## 🎯 Best Practices

1. **Reproduce first** — before touching code, make the bug appear reliably
2. **Use sanitisers** (`-fsanitize=address,undefined`) in every test build
3. **Enable all warnings** and fix them — they are bug reports from the compiler
4. **Use `assert` liberally** to document and enforce invariants
5. **Use a real debugger** (gdb/lldb) for complex bugs instead of print-debugging
6. **Write a test before fixing** — prove the bug exists, then prove it's fixed

## 📚 Related Topics

- [`exception.md`](../Fundamentals/31_exception.md) — Exception-based error reporting
- [`type_traits.md`](../Fundamentals/33_type_traits.md) — `static_assert` with type traits
- [`memory_management.md`](memory_management.md) — Preventing the bugs ASan catches

## 🚀 Next Steps

1. Enable `-fsanitize=address,undefined` on an existing project and fix every finding
2. Learn 10 essential GDB commands by debugging a program with a deliberate bug
3. Write a failing test *before* fixing the bug (TDD-style)
4. Explore Valgrind for comprehensive memory analysis: `valgrind --leak-check=full`
---

## Next Step

- Go to [design_patterns.md](design_patterns.md) to continue with design patterns.
