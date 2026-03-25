# 26_chrono.md - Time Utilities

The `chrono` header provides time points, durations, and clocks for precise time measurement and manipulation in C++.

## 📖 Overview

The `chrono` library is the standard C++ solution for handling time-related operations. It provides a type-safe, precision-independent way to measure time intervals, represent specific moments in time, and work with different time units without losing precision.

## 🎯 Key Features

- **Type-safe duration arithmetic** - Prevents unit mixing errors at compile time
- **Multiple clock types** - System, steady, and high-resolution clocks
- **Flexible time units** - From nanoseconds to hours with automatic conversions
- **Time point manipulation** - Arithmetic operations on specific moments
- **Sleep utilities** - Portable thread sleeping functionality
- **Clock synchronization** - Convert between different clock epochs

## 🔧 Clock Types

### System Clock
```cpp
#include <iostream>
#include <chrono>
#include <ctime>
#include <iomanip>

void demonstrateSystemClock() {
    std::cout << "=== System Clock Examples ===" << std::endl;
    
    // Get current time
    auto now = std::chrono::system_clock::now();
    
    // Convert to time_t for display
    std::time_t now_time = std::chrono::system_clock::to_time_t(now);
    std::cout << "Current time: " << std::put_time(std::localtime(&now_time), "%Y-%m-%d %H:%M:%S") << std::endl;
    
    // Convert from time_t
    std::tm tm = {};
    tm.tm_year = 124;  // 2024
    tm.tm_mon = 0;     // January
    tm.tm_mday = 1;    // 1st
    tm.tm_hour = 0;    // Midnight
    tm.tm_min = 0;
    tm.tm_sec = 0;
    
    std::time_t new_year_time = std::mktime(&tm);
    auto new_year = std::chrono::system_clock::from_time_t(new_year_time);
    
    // Calculate duration until New Year
    auto duration = new_year - now;
    auto days = std::chrono::duration_cast<std::chrono::hours>(duration).count() / 24.0;
    std::cout << "Days until New Year: " << days << std::endl;
    
    // System clock epoch
    auto epoch = std::chrono::system_clock::time_point{};
    auto since_epoch = now - epoch;
    auto days_since_epoch = std::chrono::duration_cast<std::chrono::days>(since_epoch);
    std::cout << "Days since epoch: " << days_since_epoch.count() << std::endl;
}
```

### Steady Clock
```cpp
void demonstrateSteadyClock() {
    std::cout << "\n=== Steady Clock Examples ===" << std::endl;
    
    // Measure execution time
    auto start = std::chrono::steady_clock::now();
    
    // Simulate some work
    volatile long sum = 0;
    for (int i = 0; i < 1000000; ++i) {
        sum += i;
    }
    
    auto end = std::chrono::steady_clock::now();
    auto elapsed = end - start;
    
    // Convert to different units
    auto nanoseconds = std::chrono::duration_cast<std::chrono::nanoseconds>(elapsed);
    auto microseconds = std::chrono::duration_cast<std::chrono::microseconds>(elapsed);
    auto milliseconds = std::chrono::duration_cast<std::chrono::milliseconds>(elapsed);
    
    std::cout << "Elapsed time:" << std::endl;
    std::cout << "  Nanoseconds: " << nanoseconds.count() << std::endl;
    std::cout << "  Microseconds: " << microseconds.count() << std::endl;
    std::cout << "  Milliseconds: " << milliseconds.count() << std::endl;
    
    // Check if steady clock is truly steady
    std::cout << "Is steady: " << std::chrono::steady_clock::is_steady << std::endl;
    
    // Steady clock cannot be converted to time_t
    // auto time = std::chrono::steady_clock::to_time_t(now); // ERROR!
}
```

### High Resolution Clock
```cpp
void demonstrateHighResolutionClock() {
    std::cout << "\n=== High Resolution Clock Examples ===" << std::endl;
    
    // High resolution timing
    auto start = std::chrono::high_resolution_clock::now();
    
    // Very short operation
    volatile int x = 42;
    x = x * 2;
    
    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = end - start;
    
    std::cout << "High resolution timing: " 
              << std::chrono::duration_cast<std::chrono::nanoseconds>(elapsed).count() 
              << " nanoseconds" << std::endl;
    
    // Check if it's steady (usually aliases steady_clock)
    std::cout << "Is steady: " << std::chrono::high_resolution_clock::is_steady << std::endl;
    std::cout << "Period: " << std::chrono::high_resolution_clock::period::num 
              << "/" << std::chrono::high_resolution_clock::period::den << " seconds" << std::endl;
}
```

## 🔧 Durations

### Duration Types and Operations
```cpp
void demonstrateDurations() {
    std::cout << "\n=== Duration Examples ===" << std::endl;
    
    // Creating durations
    std::chrono::seconds sec(30);
    std::chrono::milliseconds ms(1500);
    std::chrono::microseconds us(2500000);
    std::chrono::nanoseconds ns(1000000000);
    
    std::cout << "30 seconds = " << sec.count() << " seconds" << std::endl;
    std::cout << "1500 milliseconds = " << ms.count() << " ms" << std::endl;
    std::cout << "2500000 microseconds = " << us.count() << " μs" << std::endl;
    std::cout << "1000000000 nanoseconds = " << ns.count() << " ns" << std::endl;
    
    // Duration arithmetic
    auto sum = sec + ms;
    auto diff = us - ms;
    auto product = sec * 2;
    auto quotient = ms / 3;
    
    std::cout << "30s + 1500ms = " << std::chrono::duration_cast<std::chrono::milliseconds>(sum).count() << " ms" << std::endl;
    std::cout << "2500000μs - 1500ms = " << std::chrono::duration_cast<std::chrono::milliseconds>(diff).count() << " ms" << std::endl;
    std::cout << "30s * 2 = " << product.count() << " seconds" << std::endl;
    std::cout << "1500ms / 3 = " << quotient.count() << " ms" << std::endl;
    
    // Duration literals (C++14+)
    using namespace std::chrono_literals;
    
    auto duration1 = 5s;      // 5 seconds
    auto duration2 = 500ms;   // 500 milliseconds
    auto duration3 = 2min;    // 2 minutes
    auto duration4 = 1h;      // 1 hour
    
    std::cout << "Using literals:" << std::endl;
    std::cout << "5s = " << duration1.count() << " seconds" << std::endl;
    std::cout << "500ms = " << duration2.count() << " ms" << std::endl;
    std::cout << "2min = " << duration3.count() << " minutes" << std::endl;
    std::cout << "1h = " << duration4.count() << " hours" << std::endl;
    
    // Duration comparisons
    if (duration1 < duration3) {
        std::cout << "5 seconds is less than 2 minutes" << std::endl;
    }
    
    // Duration casting
    auto precise = 1.5s;
    auto whole_seconds = std::chrono::duration_cast<std::chrono::seconds>(precise);
    auto floor_seconds = std::chrono::floor<std::chrono::seconds>(precise);
    auto ceil_seconds = std::chrono::ceil<std::chrono::seconds>(precise);
    auto round_seconds = std::chrono::round<std::chrono::seconds>(precise);
    
    std::cout << "1.5s cast to seconds: " << whole_seconds.count() << std::endl;
    std::cout << "1.5s floor: " << floor_seconds.count() << std::endl;
    std::cout << "1.5s ceil: " << ceil_seconds.count() << std::endl;
    std::cout << "1.5s round: " << round_seconds.count() << std::endl;
}
```

## 🔧 Time Points

### Time Point Operations
```cpp
void demonstrateTimePoints() {
    std::cout << "\n=== Time Point Examples ===" << std::endl;
    
    using namespace std::chrono;
    
    // Create time points
    auto now = steady_clock::now();
    auto future = now + 5s;
    auto past = now - 2s;
    
    std::cout << "Current time point" << std::endl;
    std::cout << "Future (5s later): " << (future - now).count() << " ticks" << std::endl;
    std::cout << "Past (2s ago): " << (now - past).count() << " ticks" << std::endl;
    
    // Time point arithmetic
    auto later = now + 10min;
    auto earlier = now - 30s;
    
    // Time point comparisons
    if (later > now) {
        std::cout << "Later time point is indeed later" << std::endl;
    }
    
    if (earlier < now) {
        std::cout << "Earlier time point is indeed earlier" << std::endl;
    }
    
    // Calculate time between points
    auto duration_until_future = future - now;
    auto duration_since_past = now - past;
    
    std::cout << "Duration until future: " 
              << duration_cast<milliseconds>(duration_until_future).count() << " ms" << std::endl;
    std::cout << "Duration since past: " 
              << duration_cast<milliseconds>(duration_since_past).count() << " ms" << std::endl;
    
    // Time point with different clock
    auto system_now = system_clock::now();
    auto steady_now = steady_clock::now();
    
    // Cannot directly compare different clocks
    // if (system_now > steady_now) // ERROR!
    
    std::cout << "System clock time: " << system_clock::to_time_t(system_now) << std::endl;
    std::cout << "Steady clock ticks: " << steady_now.time_since_epoch().count() << std::endl;
}
```

## 🎮 Practical Examples

### Example 1: Performance Benchmarking
```cpp
#include <iostream>
#include <chrono>
#include <vector>
#include <algorithm>
#include <random>
#include <iomanip>

class PerformanceBenchmark {
private:
    std::vector<int> test_data;
    
public:
    PerformanceBenchmark(size_t size) {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<> dis(1, 1000);
        
        test_data.resize(size);
        for (auto& val : test_data) {
            val = dis(gen);
        }
    }
    
    // Benchmark sorting algorithms
    void benchmarkSorting() {
        std::cout << "=== Sorting Algorithm Benchmark ===" << std::endl;
        std::cout << std::fixed << std::setprecision(3);
        
        const size_t iterations = 100;
        
        // Benchmark std::sort
        auto sort_time = measureTime<std::chrono::microseconds>([&]() {
            auto data = test_data;
            std::sort(data.begin(), data.end());
        }, iterations);
        
        // Benchmark std::stable_sort
        auto stable_sort_time = measureTime<std::chrono::microseconds>([&]() {
            auto data = test_data;
            std::stable_sort(data.begin(), data.end());
        }, iterations);
        
        // Benchmark std::make_heap + std::sort_heap
        auto heap_sort_time = measureTime<std::chrono::microseconds>([&]() {
            auto data = test_data;
            std::make_heap(data.begin(), data.end());
            std::sort_heap(data.begin(), data.end());
        }, iterations);
        
        std::cout << "Data size: " << test_data.size() << " elements" << std::endl;
        std::cout << "Iterations: " << iterations << std::endl;
        std::cout << "std::sort:        " << sort_time << " μs avg" << std::endl;
        std::cout << "std::stable_sort: " << stable_sort_time << " μs avg" << std::endl;
        std::cout << "heap sort:        " << heap_sort_time << " μs avg" << std::endl;
    }
    
    // Benchmark search algorithms
    void benchmarkSearching() {
        std::cout << "\n=== Search Algorithm Benchmark ===" << std::endl;
        
        auto sorted_data = test_data;
        std::sort(sorted_data.begin(), sorted_data.end());
        
        int target = test_data[test_data.size() / 2];
        const size_t iterations = 10000;
        
        // Benchmark linear search
        auto linear_time = measureTime<std::chrono::nanoseconds>([&]() {
            auto it = std::find(test_data.begin(), test_data.end(), target);
            (void)it; // Prevent optimization
        }, iterations);
        
        // Benchmark binary search
        auto binary_time = measureTime<std::chrono::nanoseconds>([&]() {
            auto it = std::lower_bound(sorted_data.begin(), sorted_data.end(), target);
            (void)it; // Prevent optimization
        }, iterations);
        
        std::cout << "Target value: " << target << std::endl;
        std::cout << "Linear search:  " << linear_time << " ns avg" << std::endl;
        std::cout << "Binary search:  " << binary_time << " ns avg" << std::endl;
        std::cout << "Speedup: " << static_cast<double>(linear_time) / binary_time << "x" << std::endl;
    }
    
private:
    template<typename Duration, typename Func>
    double measureTime(Func func, size_t iterations) {
        auto total_time = Duration{0};
        
        for (size_t i = 0; i < iterations; ++i) {
            auto start = std::chrono::high_resolution_clock::now();
            func();
            auto end = std::chrono::high_resolution_clock::now();
            total_time += std::chrono::duration_cast<Duration>(end - start);
        }
        
        return static_cast<double>(total_time.count()) / iterations;
    }
};

int main() {
    std::cout << "=== Performance Benchmarking ===" << std::endl;
    
    PerformanceBenchmark benchmark(100000);
    benchmark.benchmarkSorting();
    benchmark.benchmarkSearching();
    
    return 0;
}
```

### Example 2: Timer and Timeout Utilities
```cpp
#include <iostream>
#include <chrono>
#include <thread>
#include <functional>
#include <atomic>
#include <mutex>
#include <condition_variable>

class Timer {
private:
    std::atomic<bool> running{false};
    std::thread timer_thread;
    std::mutex mtx;
    std::condition_variable cv;
    
public:
    ~Timer() {
        stop();
    }
    
    // Execute function after specified duration
    void setTimeout(std::function<void()> callback, std::chrono::milliseconds delay) {
        std::thread([callback, delay]() {
            std::this_thread::sleep_for(delay);
            callback();
        }).detach();
    }
    
    // Execute function repeatedly at interval
    void setInterval(std::function<void()> callback, std::chrono::milliseconds interval) {
        running = true;
        timer_thread = std::thread([this, callback, interval]() {
            while (running) {
                std::unique_lock<std::mutex> lock(mtx);
                if (cv.wait_for(lock, interval, [this] { return !running; })) {
                    break;
                }
                callback();
            }
        });
    }
    
    void stop() {
        running = false;
        cv.notify_all();
        if (timer_thread.joinable()) {
            timer_thread.join();
        }
    }
};

class TimeoutGuard {
private:
    std::atomic<bool> completed{false};
    std::thread timeout_thread;
    
public:
    template<typename Func>
    TimeoutGuard(Func func, std::chrono::milliseconds timeout) {
        timeout_thread = std::thread([this, func, timeout]() {
            auto start = std::chrono::steady_clock::now();
            
            std::thread worker([this, func]() {
                func();
                completed = true;
            });
            
            while (!completed) {
                std::this_thread::sleep_for(std::chrono::milliseconds(10));
                auto elapsed = std::chrono::steady_clock::now() - start;
                if (elapsed >= timeout) {
                    std::cout << "⚠️  Operation timed out after " 
                              << std::chrono::duration_cast<std::chrono::milliseconds>(elapsed).count() 
                              << " ms" << std::endl;
                    break;
                }
            }
            
            if (completed) {
                auto elapsed = std::chrono::steady_clock::now() - start;
                std::cout << "✅ Operation completed in " 
                          << std::chrono::duration_cast<std::chrono::milliseconds>(elapsed).count() 
                          << " ms" << std::endl;
            }
            
            worker.detach();
        });
    }
    
    ~TimeoutGuard() {
        if (timeout_thread.joinable()) {
            timeout_thread.join();
        }
    }
    
    bool isCompleted() const { return completed; }
};

int main() {
    std::cout << "=== Timer and Timeout Utilities ===" << std::endl;
    
    // Timer examples
    Timer timer;
    
    std::cout << "Setting timeout for 2 seconds..." << std::endl;
    timer.setTimeout([]() {
        std::cout << "⏰ Timeout callback executed!" << std::endl;
    }, std::chrono::seconds(2));
    
    std::cout << "Setting interval every 1 second (3 times)..." << std::endl;
    int count = 0;
    timer.setInterval([&count]() {
        count++;
        std::cout << "⏰ Interval callback #" << count << std::endl;
        if (count >= 3) {
            timer.stop();
        }
    }, std::chrono::seconds(1));
    
    // Wait for interval to complete
    std::this_thread::sleep_for(std::chrono::seconds(4));
    
    // Timeout guard examples
    std::cout << "\n--- Timeout Guard Examples ---" << std::endl;
    
    // Fast operation
    std::cout << "Testing fast operation (1s timeout)..." << std::endl;
    {
        TimeoutGuard guard([]() {
            std::this_thread::sleep_for(std::chrono::milliseconds(500));
        }, std::chrono::seconds(1));
        std::this_thread::sleep_for(std::chrono::seconds(2));
    }
    
    // Slow operation
    std::cout << "Testing slow operation (1s timeout)..." << std::endl;
    {
        TimeoutGuard guard([]() {
            std::this_thread::sleep_for(std::chrono::milliseconds(1500));
        }, std::chrono::seconds(1));
        std::this_thread::sleep_for(std::chrono::seconds(2));
    }
    
    return 0;
}
```

### Example 3: Date and Time Utilities
```cpp
#include <iostream>
#include <chrono>
#include <iomanip>
#include <sstream>
#include <string>

class DateTimeUtils {
public:
    // Format system_clock time_point to string
    static std::string formatTime(const std::chrono::system_clock::time_point& tp, 
                                 const std::string& format = "%Y-%m-%d %H:%M:%S") {
        std::time_t time = std::chrono::system_clock::to_time_t(tp);
        std::stringstream ss;
        ss << std::put_time(std::localtime(&time), format.c_str());
        return ss.str();
    }
    
    // Parse string to time_point (simplified)
    static std::chrono::system_clock::time_point parseTime(const std::string& time_str,
                                                         const std::string& format = "%Y-%m-%d %H:%M:%S") {
        std::tm tm = {};
        std::istringstream ss(time_str);
        ss >> std::get_time(&tm, format.c_str());
        return std::chrono::system_clock::from_time_t(std::mktime(&tm));
    }
    
    // Add time units to time_point
    template<typename Duration>
    static std::chrono::system_clock::time_point addTime(
        const std::chrono::system_clock::time_point& tp, Duration duration) {
        return tp + duration;
    }
    
    // Calculate difference between time points
    static std::string formatDuration(const std::chrono::system_clock::duration& duration) {
        auto total_seconds = std::chrono::duration_cast<std::chrono::seconds>(duration);
        auto days = std::chrono::duration_cast<std::chrono::days>(total_seconds);
        auto hours = std::chrono::duration_cast<std::chrono::hours>(total_seconds % std::chrono::days(1));
        auto minutes = std::chrono::duration_cast<std::chrono::minutes>(total_seconds % std::chrono::hours(1));
        auto seconds = total_seconds % std::chrono::minutes(1);
        
        std::stringstream ss;
        if (days.count() > 0) {
            ss << days.count() << "d ";
        }
        if (hours.count() > 0 || days.count() > 0) {
            ss << hours.count() << "h ";
        }
        if (minutes.count() > 0 || hours.count() > 0 || days.count() > 0) {
            ss << minutes.count() << "m ";
        }
        ss << seconds.count() << "s";
        
        return ss.str();
    }
    
    // Get age from birth date
    static int calculateAge(const std::chrono::system_clock::time_point& birth_date) {
        auto now = std::chrono::system_clock::now();
        auto duration = now - birth_date;
        auto years = std::chrono::duration_cast<std::chrono::hours>(duration).count() / 8760.0;
        return static_cast<int>(years);
    }
    
    // Check if time point is in the past
    static bool isPast(const std::chrono::system_clock::time_point& tp) {
        return tp < std::chrono::system_clock::now();
    }
    
    // Check if time point is in the future
    static bool isFuture(const std::chrono::system_clock::time_point& tp) {
        return tp > std::chrono::system_clock::now();
    }
    
    // Get start of day
    static std::chrono::system_clock::time_point startOfDay(const std::chrono::system_clock::time_point& tp) {
        std::time_t time = std::chrono::system_clock::to_time_t(tp);
        std::tm* tm = std::localtime(&time);
        tm->tm_hour = 0;
        tm->tm_min = 0;
        tm->tm_sec = 0;
        return std::chrono::system_clock::from_time_t(std::mktime(tm));
    }
    
    // Get end of day
    static std::chrono::system_clock::time_point endOfDay(const std::chrono::system_clock::time_point& tp) {
        auto start = startOfDay(tp);
        return start + std::chrono::hours(24) - std::chrono::seconds(1);
    }
};

int main() {
    std::cout << "=== Date and Time Utilities ===" << std::endl;
    
    using namespace std::chrono;
    
    // Current time
    auto now = system_clock::now();
    std::cout << "Current time: " << DateTimeUtils::formatTime(now) << std::endl;
    
    // Start and end of day
    auto day_start = DateTimeUtils::startOfDay(now);
    auto day_end = DateTimeUtils::endOfDay(now);
    std::cout << "Start of day: " << DateTimeUtils::formatTime(day_start) << std::endl;
    std::cout << "End of day: " << DateTimeUtils::formatTime(day_end) << std::endl;
    
    // Time arithmetic
    auto future = DateTimeUtils::addTime(now, hours(5) + minutes(30));
    std::cout << "In 5.5 hours: " << DateTimeUtils::formatTime(future) << std::endl;
    
    auto past = DateTimeUtils::addTime(now, -days(7));
    std::cout << "7 days ago: " << DateTimeUtils::formatTime(past) << std::endl;
    
    // Duration formatting
    auto duration = future - past;
    std::cout << "Duration between past and future: " 
              << DateTimeUtils::formatDuration(duration) << std::endl;
    
    // Age calculation
    auto birth_date = DateTimeUtils::parseTime("1990-05-15 00:00:00");
    int age = DateTimeUtils::calculateAge(birth_date);
    std::cout << "Age for birth date 1990-05-15: " << age << " years" << std::endl;
    
    // Past/future checks
    std::cout << "Is past date in the past? " << (DateTimeUtils::isPast(past) ? "Yes" : "No") << std::endl;
    std::cout << "Is future date in the future? " << (DateTimeUtils::isFuture(future) ? "Yes" : "No") << std::endl;
    
    // Different formats
    std::cout << "ISO format: " << DateTimeUtils::formatTime(now, "%Y-%m-%dT%H:%M:%S") << std::endl;
    std::cout << "US format: " << DateTimeUtils::formatTime(now, "%m/%d/%Y %I:%M:%S %p") << std::endl;
    std::cout << "European format: " << DateTimeUtils::formatTime(now, "%d.%m.%Y %H:%M") << std::endl;
    
    return 0;
}
```

### Example 4: Frame Rate Limiter and Animation Timer
```cpp
#include <iostream>
#include <chrono>
#include <thread>
#include <vector>
#include <algorithm>
#include <cmath>

class FrameRateLimiter {
private:
    std::chrono::steady_clock::time_point last_frame;
    std::chrono::nanoseconds frame_duration;
    std::vector<double> frame_times;
    static constexpr size_t MAX_SAMPLES = 100;
    
public:
    FrameRateLimiter(double target_fps) 
        : frame_duration(std::chrono::nanoseconds(
            static_cast<long long>(1e9 / target_fps))) {
        last_frame = std::chrono::steady_clock::now();
    }
    
    // Wait until it's time for next frame
    void waitForNextFrame() {
        auto now = std::chrono::steady_clock::now();
        auto next_frame = last_frame + frame_duration;
        
        if (now < next_frame) {
            std::this_thread::sleep_until(next_frame);
        }
        
        auto actual_frame_time = std::chrono::steady_clock::now() - last_frame;
        frame_times.push_back(std::chrono::duration<double>(actual_frame_time).count());
        
        if (frame_times.size() > MAX_SAMPLES) {
            frame_times.erase(frame_times.begin());
        }
        
        last_frame = std::chrono::steady_clock::now();
    }
    
    // Get actual FPS
    double getActualFPS() const {
        if (frame_times.empty()) return 0.0;
        
        double avg_frame_time = 0.0;
        for (double time : frame_times) {
            avg_frame_time += time;
        }
        avg_frame_time /= frame_times.size();
        
        return 1.0 / avg_frame_time;
    }
    
    // Get frame time statistics
    struct FrameStats {
        double min_fps;
        double max_fps;
        double avg_fps;
        double frame_variance;
    };
    
    FrameStats getFrameStats() const {
        if (frame_times.size() < 2) {
            return {getActualFPS(), getActualFPS(), getActualFPS(), 0.0};
        }
        
        std::vector<double> fps_values;
        fps_values.reserve(frame_times.size());
        
        for (double frame_time : frame_times) {
            fps_values.push_back(1.0 / frame_time);
        }
        
        auto min_max = std::minmax_element(fps_values.begin(), fps_values.end());
        double min_fps = *min_max.first;
        double max_fps = *min_max.second;
        
        double sum = std::accumulate(fps_values.begin(), fps_values.end(), 0.0);
        double avg_fps = sum / fps_values.size();
        
        double variance = 0.0;
        for (double fps : fps_values) {
            variance += (fps - avg_fps) * (fps - avg_fps);
        }
        variance /= fps_values.size();
        
        return {min_fps, max_fps, avg_fps, variance};
    }
};

class AnimationTimer {
private:
    std::chrono::steady_clock::time_point start_time;
    double duration_seconds;
    
public:
    AnimationTimer(double duration) : duration_seconds(duration) {
        start_time = std::chrono::steady_clock::now();
    }
    
    // Reset animation
    void reset() {
        start_time = std::chrono::steady_clock::now();
    }
    
    // Get normalized progress (0.0 to 1.0)
    double getProgress() const {
        auto elapsed = std::chrono::steady_clock::now() - start_time;
        double elapsed_seconds = std::chrono::duration<double>(elapsed).count();
        return std::min(1.0, elapsed_seconds / duration_seconds);
    }
    
    // Check if animation is complete
    bool isComplete() const {
        return getProgress() >= 1.0;
    }
    
    // Get elapsed time
    double getElapsedTime() const {
        auto elapsed = std::chrono::steady_clock::now() - start_time;
        return std::chrono::duration<double>(elapsed).count();
    }
    
    // Get remaining time
    double getRemainingTime() const {
        return std::max(0.0, duration_seconds - getElapsedTime());
    }
    
    // Ease-in-out animation curve
    static double easeInOut(double t) {
        return t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t;
    }
    
    // Get animated value with easing
    double getAnimatedValue(double start, double end, bool use_easing = true) const {
        double progress = getProgress();
        if (use_easing) {
            progress = easeInOut(progress);
        }
        return start + (end - start) * progress;
    }
};

int main() {
    std::cout << "=== Frame Rate Limiter and Animation Timer ===" << std::endl;
    
    // Frame rate limiter test
    std::cout << "\n--- Frame Rate Limiter Test ---" << std::endl;
    
    FrameRateLimiter limiter(60.0); // 60 FPS target
    
    std::cout << "Running for 3 seconds at 60 FPS target..." << std::endl;
    auto test_start = std::chrono::steady_clock::now();
    
    int frame_count = 0;
    while (std::chrono::steady_clock::now() - test_start < std::chrono::seconds(3)) {
        limiter.waitForNextFrame();
        frame_count++;
        
        if (frame_count % 60 == 0) { // Print every second
            auto stats = limiter.getFrameStats();
            std::cout << "Frame " << frame_count << " | "
                      << "Actual FPS: " << std::fixed << std::setprecision(1) << limiter.getActualFPS()
                      << " | Min: " << stats.min_fps
                      << " | Max: " << stats.max_fps
                      << " | Avg: " << stats.avg_fps << std::endl;
        }
    }
    
    auto final_stats = limiter.getFrameStats();
    std::cout << "\nFinal Statistics:" << std::endl;
    std::cout << "Total frames: " << frame_count << std::endl;
    std::cout << "Average FPS: " << final_stats.avg_fps << std::endl;
    std::cout << "FPS variance: " << final_stats.frame_variance << std::endl;
    
    // Animation timer test
    std::cout << "\n--- Animation Timer Test ---" << std::endl;
    
    AnimationTimer anim_timer(2.0); // 2 second animation
    
    std::cout << "Running 2-second animation with progress updates..." << std::endl;
    
    while (!anim_timer.isComplete()) {
        double progress = anim_timer.getProgress() * 100.0;
        double value = anim_timer.getAnimatedValue(0.0, 100.0);
        double eased_value = anim_timer.getAnimatedValue(0.0, 100.0, true);
        
        std::cout << "Progress: " << std::setw(5) << std::fixed << std::setprecision(1) << progress << "% | "
                  << "Linear: " << std::setw(6) << value << " | "
                  << "Eased: " << std::setw(6) << eased_value << " | "
                  << "Remaining: " << std::setw(5) << anim_timer.getRemainingTime() << "s" << std::endl;
        
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }
    
    std::cout << "Animation complete!" << std::endl;
    
    return 0;
}
```

## 📊 Complete Function Reference

### Clock Types
| Clock | Description | Steady | Epoch |
|-------|-------------|--------|-------|
| `system_clock` | System-wide wall clock | No | Unix epoch (1970-01-01) |
| `steady_clock` | Monotonic clock | Yes | Implementation-defined |
| `high_resolution_clock` | Highest resolution clock | Implementation-dependent | Implementation-dependent |

### Duration Types
| Type | Description | Example |
|------|-------------|---------|
| `duration<Rep, Period>` | Duration with representation and period | `duration<int, std::ratio<1,1000>>` |
| `nanoseconds` | Duration in nanoseconds | `1000ns` |
| `microseconds` | Duration in microseconds | `500us` |
| `milliseconds` | Duration in milliseconds | `100ms` |
| `seconds` | Duration in seconds | `5s` |
| `minutes` | Duration in minutes | `2min` |
| `hours` | Duration in hours | `1h` |

### Duration Operations
| Operation | Description |
|-----------|-------------|
| `duration_cast<D>(d)` | Convert duration to different unit |
| `floor<D>(d)` | Round duration down |
| `ceil<D>(d)` | Round duration up |
| `round<D>(d)` | Round duration to nearest |
| `count()` | Get tick count |
| `zero()` | Zero duration |
| `min()` | Minimum duration |
| `max()` | Maximum duration |

### Time Point Operations
| Operation | Description |
|-----------|-------------|
| `time_point_cast<D>(tp)` | Convert time point to different duration |
| `floor<D>(tp)` | Round time point down |
| `ceil<D>(tp)` | Round time point up |
| `round<D>(tp)` | Round time point to nearest |
| `time_since_epoch()` | Duration since clock's epoch |

## ⚡ Performance Considerations

### Clock Selection
```cpp
// Use steady_clock for measuring intervals
auto start = std::chrono::steady_clock::now();
// ... code to measure ...
auto elapsed = std::chrono::steady_clock::now() - start;

// Use system_clock for calendar time
auto now = std::chrono::system_clock::now();
std::time_t time = std::chrono::system_clock::to_time_t(now);
```

### Duration Precision
```cpp
// Use appropriate precision to avoid overhead
auto precise = std::chrono::high_resolution_clock::now(); // High precision
auto fast = std::chrono::steady_clock::now(); // Usually sufficient
```

## 🎯 Common Patterns

### Pattern 1: Code Benchmarking
```cpp
auto start = std::chrono::high_resolution_clock::now();
// Code to benchmark
auto end = std::chrono::high_resolution_clock::now();
auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
```

### Pattern 2: Timeout Implementation
```cpp
auto deadline = std::chrono::steady_clock::now() + std::chrono::seconds(30);
while (condition && std::chrono::steady_clock::now() < deadline) {
    // Process with timeout
}
```

### Pattern 3: Frame Rate Control
```cpp
std::chrono::steady_clock::time_point next_frame = std::chrono::steady_clock::now();
while (running) {
    next_frame += std::chrono::milliseconds(16); // ~60 FPS
    std::this_thread::sleep_until(next_frame);
    // Render frame
}
```

## 🐛 Common Pitfalls & Solutions

### 1. Mixing Clock Types
```cpp
// Problem - comparing different clocks
auto system_now = std::chrono::system_clock::now();
auto steady_now = std::chrono::steady_clock::now();
if (system_now > steady_now) // ERROR! Different clocks

// Solution - use same clock type
auto start = std::chrono::steady_clock::now();
auto end = std::chrono::steady_clock::now();
if (end > start) // Correct
```

### 2. Duration Truncation
```cpp
// Problem - losing precision
auto duration = std::chrono::milliseconds(1500);
auto seconds = std::chrono::duration_cast<std::chrono::seconds>(duration); // Results in 1 second

// Solution - use floating point or proper rounding
auto precise_seconds = std::chrono::duration<double, std::ratio<1>>(duration);
auto rounded_seconds = std::chrono::round<std::chrono::seconds>(duration);
```

### 3. System Clock Adjustments
```cpp
// Problem - system_clock can jump backward
auto start = std::chrono::system_clock::now();
// System time changes
auto end = std::chrono::system_clock::now();
auto elapsed = end - start; // Could be negative!

// Solution - use steady_clock for intervals
auto steady_start = std::chrono::steady_clock::now();
auto steady_end = std::chrono::steady_clock::now();
auto steady_elapsed = steady_end - steady_start; // Always positive
```

## 📚 Related Headers

- `thread.md` - Thread sleeping utilities
- `ratio.md` - Compile-time rational arithmetic
- `ctime.md` - C-style time functions
- `iomanip.md` - Time formatting utilities

## 🚀 Best Practices

1. **Use steady_clock** for measuring time intervals
2. **Use system_clock** for calendar time and timestamps
3. **Choose appropriate duration precision** to avoid unnecessary overhead
4. **Be aware of clock monotonicity** - system_clock can jump
5. **Use duration literals** (C++14+) for better readability
6. **Prefer std::chrono over platform-specific APIs** for portability
7. **Consider high_resolution_clock** for precise measurements but test actual resolution

## 🎯 When to Use chrono Utilities

✅ **Use when:**
- Measuring code execution time
- Implementing timeouts and delays
- Working with timestamps and calendar time
- Creating frame rate limiters
- Implementing animation systems
- Benchmarking and performance analysis

❌ **Avoid when:**
- Simple millisecond delays (use platform-specific sleep)
- High-frequency trading nanosecond precision (use specialized hardware)
- Real-time systems with guaranteed timing (use RTOS features)

---

**Examples in this file**: 4 complete programs  
**Key Components**: Clock types, durations, time points, literals  
**Performance**: High-resolution timing with minimal overhead  
**Portability**: Cross-platform time handling
