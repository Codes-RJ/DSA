# Multithreading - Concurrent Execution in C++

The C++11 thread library (`<thread>`, `<mutex>`, `<atomic>`, `<condition_variable>`) provides portable, type-safe primitives for writing concurrent programs.

## 📖 Overview

Multithreading lets multiple tasks run concurrently on multiple CPU cores, improving throughput for CPU-bound work and responsiveness for I/O-bound applications. However, shared mutable state requires careful synchronisation — otherwise you get data races and undefined behaviour.

Core concerns:
- **Thread creation and lifecycle** — launching, joining, detaching
- **Mutual exclusion** — protecting shared data from simultaneous access
- **Condition variables** — coordinating work between threads
- **Atomics** — lock-free operations on individual variables

## 🎯 Key Components

### Headers
| Header | Contents |
|--------|----------|
| `<thread>` | `std::thread`, `std::this_thread` |
| `<mutex>` | `mutex`, `recursive_mutex`, `timed_mutex`, `lock_guard`, `unique_lock`, `scoped_lock` |
| `<shared_mutex>` | `shared_mutex`, `shared_lock` (C++14/17) |
| `<atomic>` | `std::atomic<T>`, memory order |
| `<condition_variable>` | `condition_variable`, `condition_variable_any` |
| `<future>` | `std::future`, `std::promise`, `std::async`, `std::packaged_task` |
| `<semaphore>` | `counting_semaphore`, `binary_semaphore` (C++20) |

### Key Classes
- `std::thread` — represents a single OS thread
- `std::mutex` — non-recursive mutual exclusion lock
- `std::lock_guard<M>` — RAII mutex lock (no unlock control)
- `std::unique_lock<M>` — RAII mutex lock (with unlock/re-lock control)
- `std::scoped_lock<M...>` — RAII multi-mutex lock (deadlock-free, C++17)
- `std::atomic<T>` — atomic read-modify-write on a single object
- `std::condition_variable` — thread coordination via wait/notify

## 🔧 Basic Operations

### Creating and Joining Threads
```cpp
#include <iostream>
#include <thread>
#include <vector>

void worker(int id, int iterations) {
    for (int i = 0; i < iterations; i++) {
        std::cout << "Thread " << id << ": step " << i << "\n";
    }
}

int main() {
    const int NUM_THREADS = 4;
    std::vector<std::thread> threads;

    // Launch threads
    for (int i = 0; i < NUM_THREADS; i++) {
        threads.emplace_back(worker, i, 3); // pass args after the callable
    }

    // MUST join or detach every thread before it is destroyed
    for (auto& t : threads) {
        t.join(); // block until thread finishes
    }

    std::cout << "All threads done.\n";
    return 0;
}
```

### Protecting Shared Data with `mutex`
```cpp
#include <iostream>
#include <thread>
#include <mutex>
#include <vector>

class ThreadSafeCounter {
    int value_ = 0;
    mutable std::mutex mtx_;

public:
    void increment() {
        std::lock_guard<std::mutex> lock(mtx_); // locks; auto-unlocks at end of scope
        value_++;
    }

    int get() const {
        std::lock_guard<std::mutex> lock(mtx_);
        return value_;
    }
};

int main() {
    ThreadSafeCounter counter;
    std::vector<std::thread> threads;

    for (int i = 0; i < 10; i++) {
        threads.emplace_back([&counter]() {
            for (int j = 0; j < 1000; j++) counter.increment();
        });
    }

    for (auto& t : threads) t.join();

    std::cout << "Counter: " << counter.get() << "\n"; // always 10000
    return 0;
}
```

### Condition Variables (Producer–Consumer)
```cpp
#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <queue>

std::queue<int>         jobQueue;
std::mutex              qMtx;
std::condition_variable cv;
bool                    done = false;

void producer(int count) {
    for (int i = 1; i <= count; i++) {
        {
            std::lock_guard<std::mutex> lock(qMtx);
            jobQueue.push(i);
            std::cout << "Produced: " << i << "\n";
        }
        cv.notify_one();
    }
    {
        std::lock_guard<std::mutex> lock(qMtx);
        done = true;
    }
    cv.notify_all();
}

void consumer(int id) {
    while (true) {
        std::unique_lock<std::mutex> lock(qMtx);
        cv.wait(lock, [] { return !jobQueue.empty() || done; });

        if (jobQueue.empty() && done) break;

        int job = jobQueue.front();
        jobQueue.pop();
        lock.unlock();
        std::cout << "Consumer " << id << " processed job " << job << "\n";
    }
}

int main() {
    std::thread prod(producer, 5);
    std::thread cons1(consumer, 1);
    std::thread cons2(consumer, 2);

    prod.join();
    cons1.join();
    cons2.join();
    return 0;
}
```

### `std::atomic` — Lock-Free Shared Variables
```cpp
#include <iostream>
#include <thread>
#include <atomic>
#include <vector>

std::atomic<int> globalCounter{0};

void incrementAtomic(int times) {
    for (int i = 0; i < times; i++) {
        globalCounter.fetch_add(1, std::memory_order_relaxed);
    }
}

int main() {
    std::vector<std::thread> threads;
    for (int i = 0; i < 8; i++)
        threads.emplace_back(incrementAtomic, 10000);

    for (auto& t : threads) t.join();

    std::cout << "Atomic counter: " << globalCounter.load() << "\n"; // always 80000
    return 0;
}
```

## 🎮 Practical Examples

### Example 1: Parallel Array Sum
```cpp
#include <iostream>
#include <thread>
#include <vector>
#include <numeric>
#include <functional>

long long parallelSum(const std::vector<int>& data, int numThreads) {
    size_t n = data.size();
    size_t chunkSize = (n + numThreads - 1) / numThreads;

    std::vector<long long> partials(numThreads, 0);
    std::vector<std::thread> threads;

    for (int t = 0; t < numThreads; t++) {
        size_t start = t * chunkSize;
        size_t end   = std::min(start + chunkSize, n);

        threads.emplace_back([&data, &partials, t, start, end]() {
            for (size_t i = start; i < end; i++)
                partials[t] += data[i];
        });
    }

    for (auto& th : threads) th.join();

    return std::accumulate(partials.begin(), partials.end(), 0LL);
}

int main() {
    std::vector<int> data(1'000'000, 1); // 1M ones
    long long result = parallelSum(data, 4);
    std::cout << "Parallel sum: " << result << "\n"; // 1000000
    return 0;
}
```

### Example 2: Thread Pool (Simplified)
```cpp
#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <queue>
#include <functional>
#include <vector>

class ThreadPool {
    std::vector<std::thread> workers_;
    std::queue<std::function<void()>> tasks_;
    std::mutex mtx_;
    std::condition_variable cv_;
    bool stop_ = false;

public:
    ThreadPool(int n) {
        for (int i = 0; i < n; i++) {
            workers_.emplace_back([this]() {
                while (true) {
                    std::function<void()> task;
                    {
                        std::unique_lock<std::mutex> lock(mtx_);
                        cv_.wait(lock, [this]{ return stop_ || !tasks_.empty(); });
                        if (stop_ && tasks_.empty()) return;
                        task = std::move(tasks_.front());
                        tasks_.pop();
                    }
                    task();
                }
            });
        }
    }

    void submit(std::function<void()> task) {
        { std::lock_guard<std::mutex> lock(mtx_); tasks_.push(std::move(task)); }
        cv_.notify_one();
    }

    ~ThreadPool() {
        { std::lock_guard<std::mutex> lock(mtx_); stop_ = true; }
        cv_.notify_all();
        for (auto& w : workers_) w.join();
    }
};

int main() {
    ThreadPool pool(4);

    for (int i = 0; i < 10; i++) {
        pool.submit([i]() {
            std::cout << "Task " << i << " on thread "
                      << std::this_thread::get_id() << "\n";
        });
    }

    std::this_thread::sleep_for(std::chrono::milliseconds(200));
    return 0;
}
```

### Example 3: Reader-Writer Lock (`shared_mutex`)
```cpp
#include <iostream>
#include <thread>
#include <shared_mutex>
#include <vector>
#include <string>

class SharedConfig {
    std::string value_ = "initial";
    mutable std::shared_mutex rw_;

public:
    // Multiple readers can hold shared_lock simultaneously
    std::string read() const {
        std::shared_lock<std::shared_mutex> lock(rw_);
        return value_;
    }

    // Only one writer at a time; blocks all readers
    void write(const std::string& v) {
        std::unique_lock<std::shared_mutex> lock(rw_);
        value_ = v;
    }
};

int main() {
    SharedConfig config;
    std::vector<std::thread> threads;

    // 3 readers
    for (int i = 0; i < 3; i++) {
        threads.emplace_back([&config, i]() {
            for (int j = 0; j < 3; j++) {
                std::cout << "Reader " << i << " sees: " << config.read() << "\n";
                std::this_thread::sleep_for(std::chrono::milliseconds(10));
            }
        });
    }

    // 1 writer
    threads.emplace_back([&config]() {
        for (const auto& v : {"update1", "update2", "update3"}) {
            std::this_thread::sleep_for(std::chrono::milliseconds(15));
            config.write(v);
            std::cout << "Writer updated to: " << v << "\n";
        }
    });

    for (auto& t : threads) t.join();
    return 0;
}
```

### Example 4: `std::once_flag` — Thread-Safe One-Time Initialisation
```cpp
#include <iostream>
#include <thread>
#include <mutex>
#include <vector>

class Singleton {
    static Singleton* instance_;
    static std::once_flag flag_;

    Singleton() { std::cout << "Singleton created on thread " << std::this_thread::get_id() << "\n"; }

public:
    static Singleton* getInstance() {
        std::call_once(flag_, []() { instance_ = new Singleton(); });
        return instance_;
    }

    void doWork() { std::cout << "Working...\n"; }
};

Singleton* Singleton::instance_ = nullptr;
std::once_flag Singleton::flag_;

int main() {
    std::vector<std::thread> threads;
    for (int i = 0; i < 5; i++) {
        threads.emplace_back([]() {
            Singleton::getInstance()->doWork();
        });
    }
    for (auto& t : threads) t.join();
    // "Singleton created" appears exactly once
    return 0;
}
```

## ⚡ Performance Tips

### Minimise Time Holding a Lock
```cpp
// Bad: holding the lock while doing slow work
std::lock_guard<std::mutex> lock(mtx);
int result = heavyComputation(); // other threads blocked during this!
data_ = result;

// Good: compute outside the lock, lock only for the write
int result = heavyComputation();
std::lock_guard<std::mutex> lock(mtx);
data_ = result; // fast, minimal contention
```

### Prefer `scoped_lock` for Locking Multiple Mutexes
```cpp
// Avoids deadlock from inconsistent lock ordering
std::scoped_lock lock(mtx1, mtx2); // acquires both atomically (C++17)
```

### Use `atomic` for Simple Shared Flags
```cpp
// Prefer atomic<bool> over mutex for a simple stop flag
std::atomic<bool> running{true};
// No mutex needed for simple reads/writes to a flag
```

## 🐛 Common Pitfalls & Solutions

### 1. Forgetting to `join()` or `detach()`
```cpp
// Problem: std::thread destructor calls terminate() if still joinable
{
    std::thread t([]{ doWork(); });
} // terminate() called if t not joined!

// Solution 1: always join
t.join();

// Solution 2: use a RAII wrapper (e.g., jthread in C++20 auto-joins)
std::jthread t([]{ doWork(); }); // auto-joins on destruction
```

### 2. Data Race — Accessing Shared Data Without a Lock
```cpp
int counter = 0;
// Bad: reading and incrementing without synchronisation — data race!
std::thread t1([&]{ counter++; });
std::thread t2([&]{ counter++; });

// Fix: use mutex or std::atomic<int>
std::atomic<int> safeCounter{0};
std::thread t3([&]{ safeCounter++; });
std::thread t4([&]{ safeCounter++; });
```

### 3. Deadlock from Inconsistent Lock Order
```cpp
// Thread A: lock(mtx1) then lock(mtx2)
// Thread B: lock(mtx2) then lock(mtx1) → DEADLOCK

// Fix: use std::scoped_lock which deadlock-safe acquires multiple mutexes
std::scoped_lock lock(mtx1, mtx2);
```

### 4. Spurious Wakeups with `condition_variable`
```cpp
// Bad: wait without a predicate — may wake up spuriously
cv.wait(lock);

// Good: always use a predicate
cv.wait(lock, []{ return !queue.empty() || done; });
```

## 🎯 Best Practices

1. **Always `join()` or `detach()`** every thread before it is destroyed
2. **Use RAII locks** (`lock_guard`, `unique_lock`) — never manually call `unlock()`
3. **Use `std::atomic`** for simple flags and counters; mutex for compound operations
4. **Minimise lock scope** — compute outside the lock, lock only for the atomic read/write
5. **Use `scoped_lock`** when acquiring multiple mutexes to prevent deadlock
6. **Always use a predicate with `condition_variable::wait`** to handle spurious wakeups

## 📚 Related Topics

- [`concurrency.md`](concurrency.md) — Higher-level tools: `std::async`, `future`, `promise`
- [`smart_pointers.md`](smart_pointers.md) — `shared_ptr` reference counting is thread-safe
- [`memory_management.md`](memory_management.md) — Memory ordering and RAII in threaded contexts

## 🚀 Next Steps

1. Write a bounded thread-safe queue using `mutex` + `condition_variable`
2. Implement a simple parallel `map` that distributes work across N threads
3. Explore C++20 `std::jthread` — auto-joining thread with stop token
4. Study memory order (`relaxed`, `acquire`, `release`, `seq_cst`) for lock-free programming

---

**Examples in this file**: 4 complete programs  
**Key Types**: `std::thread`, `std::mutex`, `std::lock_guard`, `std::unique_lock`, `std::atomic`, `std::condition_variable`  
**Key Patterns**: Producer–Consumer, Thread Pool, Reader-Writer, One-Time Init  
**Common Use Cases**: Parallel computation, background tasks, event processing, shared state management
