# Concurrency - Higher-Level Concurrency Tools

C++ provides high-level concurrency abstractions (`<future>`, `<async>`, `<promise>`) on top of raw threads, letting you express *what* result you want without manually managing thread lifecycles and shared state.

## 📖 Overview

While `<thread>` gives you raw threads, the future/promise/async layer provides a **task-based** model:
- Launch a task (produce a value asynchronously)
- Retrieve the result later (when needed)
- Propagate exceptions across thread boundaries automatically

This model is easier, safer, and often more efficient than manually managing threads with mutexes.

## 🎯 Key Components

### `<future>` and `<async>`
| Type | Role |
|------|------|
| `std::future<T>` | Receives a single future value; read-once |
| `std::shared_future<T>` | Shareable future; can be `get()`-called from multiple threads |
| `std::promise<T>` | Write end of a future; set value or exception |
| `std::async(fn, ...)` | Runs `fn` (possibly on a new thread), returns a `future<T>` |
| `std::packaged_task<T()>` | Wraps a callable, produces a `future<T>` |

### Launch Policies for `std::async`
| Policy | Meaning |
|--------|---------|
| `std::launch::async` | Always run in a new thread |
| `std::launch::deferred` | Run in the calling thread when `get()`/`wait()` is called (lazy) |
| `std::launch::async \| std::launch::deferred` | Implementation decides (default) |

### `std::atomic` Memory Orders (Quick Reference)
| Order | Guarantees |
|-------|-----------|
| `memory_order_relaxed` | No synchronisation, just atomicity |
| `memory_order_acquire` | Subsequent loads see all writes before a matching release |
| `memory_order_release` | Prior writes are visible to threads that acquire |
| `memory_order_seq_cst` | Total sequential consistency (default, safest) |

## 🔧 Basic Operations

### `std::async` — Fire and Forget Style
```cpp
#include <iostream>
#include <future>
#include <string>

std::string fetchData(const std::string& url) {
    // Simulate network I/O
    std::this_thread::sleep_for(std::chrono::milliseconds(200));
    return "Response from " + url;
}

int main() {
    // Launch asynchronously; get back a future
    auto fut1 = std::async(std::launch::async, fetchData, "https://api.example.com/users");
    auto fut2 = std::async(std::launch::async, fetchData, "https://api.example.com/products");

    std::cout << "Requests launched, doing other work...\n";

    // Block and retrieve results when needed
    std::string res1 = fut1.get();
    std::string res2 = fut2.get();

    std::cout << res1 << "\n";
    std::cout << res2 << "\n";
    return 0;
}
```

### `std::promise` and `std::future` — Manual Control
```cpp
#include <iostream>
#include <future>
#include <thread>

void compute(std::promise<int> promise, int a, int b) {
    try {
        if (b == 0) throw std::invalid_argument("Division by zero");
        promise.set_value(a / b);
    } catch (...) {
        promise.set_exception(std::current_exception()); // forward exception
    }
}

int main() {
    std::promise<int> p;
    std::future<int>  f = p.get_future();

    std::thread t(compute, std::move(p), 42, 6);
    t.join();

    try {
        std::cout << "Result: " << f.get() << "\n"; // 7
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << "\n";
    }

    // Exception propagation example
    std::promise<int> p2;
    std::future<int>  f2 = p2.get_future();
    std::thread t2(compute, std::move(p2), 10, 0);
    t2.join();

    try {
        f2.get(); // re-throws the exception from the worker thread
    } catch (const std::exception& e) {
        std::cerr << "Caught: " << e.what() << "\n";
    }

    return 0;
}
```

### `std::packaged_task` — Wrapping Callables
```cpp
#include <iostream>
#include <future>
#include <thread>

int heavyWork(int x) {
    std::this_thread::sleep_for(std::chrono::milliseconds(100));
    return x * x;
}

int main() {
    std::packaged_task<int(int)> task(heavyWork);
    std::future<int> fut = task.get_future();

    // Execute the task on a separate thread
    std::thread t(std::move(task), 7);

    std::cout << "Waiting for result...\n";
    std::cout << "Result: " << fut.get() << "\n"; // 49
    t.join();

    return 0;
}
```

### Waiting Without Blocking Indefinitely
```cpp
#include <iostream>
#include <future>
#include <chrono>

int slowTask() {
    std::this_thread::sleep_for(std::chrono::seconds(2));
    return 42;
}

int main() {
    auto fut = std::async(std::launch::async, slowTask);

    // Poll with timeout
    while (fut.wait_for(std::chrono::milliseconds(100)) != std::future_status::ready) {
        std::cout << "Still waiting...\n";
    }

    std::cout << "Done: " << fut.get() << "\n";
    return 0;
}
```

## 🎮 Practical Examples

### Example 1: Parallel Fan-Out Computation
```cpp
#include <iostream>
#include <future>
#include <vector>
#include <numeric>
#include <cmath>

// Compute sum of squares for a range
long long sumSquares(int from, int to) {
    long long sum = 0;
    for (int i = from; i < to; i++) sum += (long long)i * i;
    return sum;
}

int main() {
    const int N = 1'000'000;
    const int K = 4; // number of parallel tasks

    std::vector<std::future<long long>> futures;
    int chunk = N / K;

    for (int i = 0; i < K; i++) {
        int lo = i * chunk + 1;
        int hi = (i == K - 1) ? N + 1 : lo + chunk;
        futures.push_back(std::async(std::launch::async, sumSquares, lo, hi));
    }

    long long total = 0;
    for (auto& f : futures) total += f.get();

    std::cout << "Sum of squares 1…" << N << " = " << total << "\n";
    return 0;
}
```

### Example 2: Timeout and Cancellation Pattern
```cpp
#include <iostream>
#include <future>
#include <atomic>
#include <thread>
#include <chrono>

std::atomic<bool> cancelFlag{false};

int cancellableTask(int id) {
    for (int i = 0; i < 10; i++) {
        if (cancelFlag.load()) {
            std::cout << "Task " << id << " cancelled at step " << i << "\n";
            return -1;
        }
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }
    return id * 100;
}

int main() {
    auto fut1 = std::async(std::launch::async, cancellableTask, 1);
    auto fut2 = std::async(std::launch::async, cancellableTask, 2);

    // Cancel after 350ms
    std::this_thread::sleep_for(std::chrono::milliseconds(350));
    cancelFlag.store(true);

    std::cout << "Task 1 returned: " << fut1.get() << "\n";
    std::cout << "Task 2 returned: " << fut2.get() << "\n";
    return 0;
}
```

### Example 3: `shared_future` — Multiple Readers
```cpp
#include <iostream>
#include <future>
#include <vector>
#include <thread>

int main() {
    std::promise<std::string> config_promise;
    std::shared_future<std::string> shared_cfg = config_promise.get_future().share();

    // Multiple consumers waiting on the same config value
    std::vector<std::thread> consumers;
    for (int i = 0; i < 4; i++) {
        consumers.emplace_back([shared_cfg, i]() {
            std::string cfg = shared_cfg.get(); // all threads can call get()
            std::cout << "Consumer " << i << " got config: " << cfg << "\n";
        });
    }

    // Simulate slow config load
    std::this_thread::sleep_for(std::chrono::milliseconds(200));
    config_promise.set_value("database=localhost;port=5432");

    for (auto& t : consumers) t.join();
    return 0;
}
```

### Example 4: Pipeline Using Futures
```cpp
#include <iostream>
#include <future>
#include <string>
#include <algorithm>
#include <cctype>

std::string stage1_fetch(const std::string& url) {
    std::this_thread::sleep_for(std::chrono::milliseconds(50));
    return "raw:hello world from " + url;
}

std::string stage2_parse(const std::string& raw) {
    std::string result = raw.substr(4); // strip "raw:"
    return result;
}

std::string stage3_uppercase(const std::string& text) {
    std::string result = text;
    std::transform(result.begin(), result.end(), result.begin(), ::toupper);
    return result;
}

int main() {
    // Chain futures as a pipeline
    auto f1 = std::async(std::launch::async, stage1_fetch, "example.com");
    auto f2 = std::async(std::launch::async, [&f1]() {
        return stage2_parse(f1.get());
    });
    auto f3 = std::async(std::launch::async, [&f2]() {
        return stage3_uppercase(f2.get());
    });

    std::cout << "Pipeline result: " << f3.get() << "\n";
    return 0;
}
```

## ⚡ Performance Tips

### Prefer `std::launch::async` to Force a New Thread
```cpp
// Default launch policy may defer execution to the calling thread!
auto f = std::async(slowFn);        // may run lazily on get()
auto g = std::async(std::launch::async, slowFn); // guaranteed new thread
```

### Use `shared_future` Only When Multiple Threads Must `get()`
```cpp
// future::get() can only be called ONCE — it moves the value out
std::future<int> f = std::async(compute);
int v = f.get(); // OK
// int v2 = f.get(); // throws std::future_error — already consumed

// Use shared_future for multiple readers
std::shared_future<int> sf = std::async(compute).share();
sf.get(); sf.get(); // both calls valid
```

### Batch Small Tasks to Amortise Thread Creation Overhead
```cpp
// Each std::async may create a thread (OS overhead ~10–50μs)
// For many tiny tasks, use a thread pool (see multithreading.md) instead
```

## 🐛 Common Pitfalls & Solutions

### 1. Forgetting That `std::async` Future Blocks on Destruction
```cpp
// Problem: the future returned by async blocks until the task finishes!
{
    auto f = std::async(std::launch::async, slowTask); // f is not used
} // destructor of f BLOCKS here — not "fire and forget"!

// Solution: explicitly disconnect with detach via packaged_task + thread
```

### 2. Calling `get()` Twice on a `future`
```cpp
std::future<int> f = std::async(compute);
int a = f.get(); // OK
int b = f.get(); // throws std::future_error: no state

// Fix: store the result, use shared_future if multiple reads needed
```

### 3. Ignoring Exceptions from Async Tasks
```cpp
auto f = std::async(std::launch::async, riskyTask);
// If you never call f.get(), any exception in riskyTask is silently lost
// Always call f.get() and wrap it in try/catch
try { f.get(); } catch (const std::exception& e) { /* handle */ }
```

### 4. Using Deferred Launch When You Expect Parallelism
```cpp
// With default policy, the task might run on the calling thread when get() is called
auto f = std::async(heavyWork); // might be deferred!
doOtherStuff();
f.get(); // possibly runs NOW, not in parallel

// Fix: specify async explicitly
auto f = std::async(std::launch::async, heavyWork);
```

## 🎯 Best Practices

1. **Specify `std::launch::async`** explicitly when parallelism is required
2. **Always call `get()` or `wait()`** on futures — unhandled exceptions will be swallowed
3. **Use `shared_future`** when multiple threads need to read the same result
4. **Use `std::promise`** for manual producer/consumer patterns across threads
5. **Prefer task-based concurrency** (`async`/`future`) over raw `thread` for simple parallel work
6. **For many short tasks**, use a thread pool instead of one `async` per task

## 📚 Related Topics

- [`multithreading.md`](multithreading.md) — Raw `thread`, `mutex`, `condition_variable`
- [`functional.md`](../Fundamentals/25_functional.md) — Callables and `std::function` used with `async`
- [`lambda_expressions.md`](lambda_expressions.md) — Lambdas as tasks for `std::async`

## 🚀 Next Steps

1. Write a parallel image processing pipeline using `std::async` stages
2. Implement a timeout-aware version of `future::get()` using `wait_for`
3. Build a `when_all` helper that waits for a `vector<future<T>>` to all complete
4. Explore C++23 `std::execution` policy extensions for parallel algorithms

---

**Examples in this file**: 4 complete programs  
**Key Types**: `std::future`, `std::shared_future`, `std::promise`, `std::async`, `std::packaged_task`  
**Key Patterns**: Fan-out parallel, pipeline, cancellation, shared results  
**Common Use Cases**: Async I/O, parallel data processing, background computations, result aggregation
