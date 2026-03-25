# Optimization - Performance Tuning in C++

C++ gives you the tools to write code that runs at near-hardware speed. Effective optimisation starts with measurement, focuses on algorithmic complexity, then applies language-level techniques.

## 📖 Overview

The optimisation process follows three phases:
1. **Measure** — profile to find the actual bottleneck (don't guess)
2. **Algorithmic** — replace O(n²) with O(n log n); no low-level trick beats this
3. **Implementation** — eliminate copies, reduce allocations, exploit cache, use SIMD hints

Key principle: **premature optimisation is the root of all evil** (Knuth). Write correct, clean code first; optimise only the proven hot paths.

## 🎯 Key Concepts

### Complexity Classes
| Complexity | Name | 10⁶ ops at 10⁹/s |
|------------|------|-------------------|
| O(1) | Constant | ~1 ns |
| O(log n) | Logarithmic | ~20 ns |
| O(n) | Linear | ~1 ms |
| O(n log n) | Log-linear | ~20 ms |
| O(n²) | Quadratic | ~1000 s! |

### Profiling Tools
- `gprof` — GNU profiler (sampling)
- `perf` — Linux performance counters
- `Valgrind/Callgrind` — cycle-accurate profiling, cache simulation
- `Instruments` — macOS profiler
- Visual Studio Profiler — Windows
- `std::chrono` — manual micro-benchmarking

## 🔧 Core Optimisation Techniques

### 1. Choose the Right Container
```cpp
#include <iostream>
#include <vector>
#include <list>
#include <unordered_map>
#include <map>
#include <chrono>
#include <algorithm>

int main() {
    const int N = 100'000;

    // random access: vector O(1) vs list O(n)
    std::vector<int> vec(N);
    std::iota(vec.begin(), vec.end(), 0);
    int sum_v = vec[N / 2]; // O(1)

    // lookup: unordered_map O(1) vs map O(log n)
    std::unordered_map<int, int> umap;
    std::map<int, int>           omap;
    for (int i = 0; i < N; i++) { umap[i] = i; omap[i] = i; }
    // umap[key] is faster for frequent lookups

    // insertion at front: list O(1) vs vector O(n)
    std::list<int> lst;
    lst.push_front(42); // O(1)
    // vec.insert(vec.begin(), 42); // O(n) — shifts all elements

    std::cout << "Container choice matters. \n";
    (void)sum_v;
    return 0;
}
```

### 2. Avoid Unnecessary Copies
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

// BAD: copies the entire vector and string on each call
int sumBad(std::vector<int> v, std::string label) {
    int sum = 0;
    for (int n : v) sum += n;
    return sum;
}

// GOOD: const reference — zero copies
int sumGood(const std::vector<int>& v, const std::string& label) {
    int sum = 0;
    for (int n : v) sum += n;
    return sum;
}

// GOOD: move expensive temporaries into containers
void addNames(std::vector<std::string>& names) {
    std::string tmp = "expensive string to compute...";
    names.push_back(std::move(tmp)); // no copy
}

int main() {
    std::vector<int> data(10000, 1);
    std::cout << sumGood(data, "test") << "\n"; // 10000
    return 0;
}
```

### 3. Reserve Memory When Size Is Known
```cpp
#include <vector>
#include <string>
#include <iostream>
#include <chrono>

int main() {
    const int N = 1'000'000;

    auto start = std::chrono::high_resolution_clock::now();
    std::vector<int> slow;
    for (int i = 0; i < N; i++) slow.push_back(i); // ~20 reallocations
    auto t1 = std::chrono::high_resolution_clock::now();

    std::vector<int> fast;
    fast.reserve(N); // one allocation
    for (int i = 0; i < N; i++) fast.push_back(i); // zero reallocations
    auto t2 = std::chrono::high_resolution_clock::now();

    auto slow_ms = std::chrono::duration_cast<std::chrono::microseconds>(t1 - start).count();
    auto fast_ms = std::chrono::duration_cast<std::chrono::microseconds>(t2 - t1).count();

    std::cout << "Without reserve: " << slow_ms << " μs\n";
    std::cout << "With reserve:    " << fast_ms << " μs\n";
    return 0;
}
```

### 4. Use `emplace_back` Instead of `push_back`
```cpp
#include <vector>
#include <string>
#include <iostream>

struct Point {
    double x, y;
    Point(double x, double y) : x(x), y(y) {}
};

int main() {
    std::vector<Point> points;
    points.reserve(3);

    // push_back: constructs a temporary, then copies/moves into vector
    points.push_back(Point(1.0, 2.0)); // unnecessary temporary

    // emplace_back: constructs directly in the vector's memory
    points.emplace_back(3.0, 4.0); // one construction only
    points.emplace_back(5.0, 6.0);

    for (const auto& p : points)
        std::cout << "(" << p.x << ", " << p.y << ")\n";
    return 0;
}
```

## 🎮 Practical Examples

### Example 1: Cache-Friendly vs Cache-Unfriendly Access
```cpp
#include <iostream>
#include <vector>
#include <chrono>

// Column-major access (cache-unfriendly for row-major storage)
long long sumColMajor(const std::vector<std::vector<int>>& matrix, int N) {
    long long s = 0;
    for (int j = 0; j < N; j++)
        for (int i = 0; i < N; i++)
            s += matrix[i][j]; // jumps N rows per iteration — cache miss every time
    return s;
}

// Row-major access (cache-friendly for row-major storage)
long long sumRowMajor(const std::vector<std::vector<int>>& matrix, int N) {
    long long s = 0;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            s += matrix[i][j]; // sequential access — cache lines stay hot
    return s;
}

int main() {
    const int N = 1000;
    std::vector<std::vector<int>> matrix(N, std::vector<int>(N, 1));

    auto t0 = std::chrono::high_resolution_clock::now();
    auto s1 = sumColMajor(matrix, N);
    auto t1 = std::chrono::high_resolution_clock::now();
    auto s2 = sumRowMajor(matrix, N);
    auto t2 = std::chrono::high_resolution_clock::now();

    std::cout << "Col-major: "
              << std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count()
              << " μs (sum=" << s1 << ")\n";
    std::cout << "Row-major: "
              << std::chrono::duration_cast<std::chrono::microseconds>(t2 - t1).count()
              << " μs (sum=" << s2 << ")\n";
    return 0;
}
```

### Example 2: String Building — `+` vs `ostringstream` vs `reserve`
```cpp
#include <iostream>
#include <string>
#include <sstream>
#include <chrono>

template <typename Fn>
long long time_us(Fn fn) {
    auto t0 = std::chrono::high_resolution_clock::now();
    fn();
    auto t1 = std::chrono::high_resolution_clock::now();
    return std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
}

int main() {
    const int N = 10000;

    // Method 1: repeated + (O(n²) copies)
    auto t1 = time_us([&]() {
        std::string result;
        for (int i = 0; i < N; i++) result = result + "x";
    });

    // Method 2: ostringstream
    auto t2 = time_us([&]() {
        std::ostringstream oss;
        for (int i = 0; i < N; i++) oss << "x";
        std::string result = oss.str();
    });

    // Method 3: reserve + append (fastest)
    auto t3 = time_us([&]() {
        std::string result;
        result.reserve(N);
        for (int i = 0; i < N; i++) result += 'x';
    });

    std::cout << "Repeated +:   " << t1 << " μs\n";
    std::cout << "ostringstream:" << t2 << " μs\n";
    std::cout << "reserve+append:" << t3 << " μs\n";
    return 0;
}
```

### Example 3: Algorithmic Improvement — O(n²) to O(n log n)
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <random>

// O(n²) naive: check all pairs
int countPairsNaive(std::vector<int> v, int target) {
    int count = 0;
    int n = v.size();
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (v[i] + v[j] == target) count++;
    return count;
}

// O(n log n): sort + two-pointer
int countPairsFast(std::vector<int> v, int target) {
    std::sort(v.begin(), v.end());
    int count = 0;
    int lo = 0, hi = (int)v.size() - 1;
    while (lo < hi) {
        int sum = v[lo] + v[hi];
        if (sum == target) { count++; lo++; hi--; }
        else if (sum < target) lo++;
        else hi--;
    }
    return count;
}

int main() {
    std::mt19937 gen(42);
    std::uniform_int_distribution<int> dist(1, 100);

    std::vector<int> data(5000);
    std::generate(data.begin(), data.end(), [&]{ return dist(gen); });

    auto t0 = std::chrono::high_resolution_clock::now();
    int r1 = countPairsNaive(data, 50);
    auto t1 = std::chrono::high_resolution_clock::now();
    int r2 = countPairsFast(data, 50);
    auto t2 = std::chrono::high_resolution_clock::now();

    std::cout << "Naive O(n²): "   << std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count() << " μs, result=" << r1 << "\n";
    std::cout << "Fast O(n log n): " << std::chrono::duration_cast<std::chrono::microseconds>(t2 - t1).count() << " μs, result=" << r2 << "\n";
    return 0;
}
```

### Example 4: Move Semantics in Containers
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <chrono>

template <typename Fn>
long long time_us(Fn fn) {
    auto t0 = std::chrono::high_resolution_clock::now();
    fn();
    return std::chrono::duration_cast<std::chrono::microseconds>(
               std::chrono::high_resolution_clock::now() - t0).count();
}

int main() {
    const int N = 100000;

    // Copying strings
    auto t1 = time_us([&]() {
        std::vector<std::string> v;
        v.reserve(N);
        for (int i = 0; i < N; i++) {
            std::string s(50, 'x');
            v.push_back(s); // copy
        }
    });

    // Moving strings
    auto t2 = time_us([&]() {
        std::vector<std::string> v;
        v.reserve(N);
        for (int i = 0; i < N; i++) {
            std::string s(50, 'x');
            v.push_back(std::move(s)); // move — no character copy
        }
    });

    std::cout << "Copy: " << t1 << " μs\n";
    std::cout << "Move: " << t2 << " μs\n";
    return 0;
}
```

## ⚡ Compiler Optimisation Tips

### Enable Optimisation Flags
```bash
# Debug (no optimisation, full debug info)
g++ -O0 -g prog.cpp

# Release (aggressive optimisation)
g++ -O2 prog.cpp           # safe optimisations  
g++ -O3 prog.cpp           # more aggressive
g++ -O3 -march=native prog.cpp  # target CPU architecture (fastest)
```

### `inline`, `constexpr`, and `noexcept` Hints
```cpp
// inline: suggest inlining (compiler may ignore)
inline int square(int x) { return x * x; }

// constexpr: computed at compile time — zero runtime cost
constexpr int factorial(int n) { return n <= 1 ? 1 : n * factorial(n - 1); }
constexpr int f5 = factorial(5); // computed at compile time: 120

// noexcept: enables optimisations in STL (e.g., move during vector resize)
void safe_op() noexcept { /* ... */ }
```

### Branch Prediction Hints (GCC/Clang)
```cpp
// Tell the compiler which branch is more likely
if (__builtin_expect(errorCode != 0, 0)) { // unlikely
    handleError();
}
```

## 🐛 Common Pitfalls & Solutions

### 1. Optimising Without Profiling
```cpp
// Don't guess — measure first
// Use std::chrono for micro-benchmarks or a profiler for system-level analysis
```

### 2. Pessimising the Return Value
```cpp
// BAD: std::move on a return disables NRVO — may actually be slower!
std::vector<int> bad() {
    std::vector<int> v{1, 2, 3};
    return std::move(v); // forces a move instead of allowing elision
}

// GOOD: just return — NRVO may eliminate the move entirely
std::vector<int> good() {
    std::vector<int> v{1, 2, 3};
    return v; // compiler may elide copy/move completely
}
```

### 3. Micro-Optimising the Wrong Thing
```cpp
// Changing O(n²) to O(n log n) on N=10000 gives 10000/13 ≈ 770x improvement
// No micro-optimisation can match that

// Profile → fix algorithm → then micro-optimise if needed
```

### 4. Ignoring `const` and Reference Parameters
```cpp
// Extra copies compile fast but run slow
void process(std::vector<int> v);         // BAD: copies
void process(const std::vector<int>& v);  // GOOD: no copy
void process(std::vector<int>&& v);       // GOOD: move-only
```

## 🎯 Best Practices

1. **Profile before you optimise** — find the real bottleneck
2. **Improve the algorithm first** — O(n log n) beats any O(n²) micro-optimisation
3. **Pass by `const` reference** for non-trivial objects
4. **Use `reserve()`** when you know the final container size
5. **Prefer `emplace_back`** for in-place construction
6. **Compile with `-O2`/`-O3`** for production builds

## 📚 Related Topics

- [`move_semantics.md`](move_semantics.md) — Eliminating copies with moves
- [`memory_management.md`](memory_management.md) — Custom allocators, pool allocation
- [`multithreading.md`](multithreading.md) — Parallel speedup for CPU-bound work
- [`algorithm.md`](../Fundamentals/04_algorithm.md) — Efficient STL algorithms
- [`chrono.md`](../Fundamentals/26_chrono.md) — Timing code for micro-benchmarks

## 🚀 Next Steps

1. Add `std::chrono` timing around your hot loops and compare before/after changes
2. Use `valgrind --tool=callgrind` to find which function consumes the most time
3. Experiment with `std::sort` vs hand-written sort on real data
4. Read "Computer Architecture: A Quantitative Approach" for cache and pipeline fundamentals

---

**Examples in this file**: 4 complete programs  
**Key Rules**: Measure first, fix algorithms, then micro-optimise  
**Key Techniques**: `reserve`, `emplace_back`, move semantics, cache-friendly access, `const&`  
**Common Use Cases**: High-throughput data processing, game engines, real-time systems, competitive programming
