# 24_numeric.md - Numeric Algorithms

The `numeric` header provides algorithms for accumulating and transforming numeric ranges, complementing `<algorithm>` with operations focused on numerical computations.

## 📖 Overview

The `numeric` header contains a collection of algorithms specifically designed for numerical operations on ranges. These algorithms provide efficient, well-tested implementations of common mathematical operations like summation, products, and sequential number generation.

## 🎯 Key Features

- **Accumulation operations** - Sum, product, and custom accumulation
- **Inner product operations** - Vector dot products and custom operations
- **Prefix operations** - Partial sums and differences
- **Sequential generation** - Fill ranges with sequential values
- **Custom operations** - Flexible binary operations for all algorithms
- **Mathematical precision** - Proper handling of numeric types

## 🔧 Basic Numeric Operations

### accumulate - Summation
```cpp
#include <iostream>
#include <numeric>
#include <vector>
#include <string>

void demonstrateAccumulate() {
    std::cout << "=== accumulate Examples ===" << std::endl;
    
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    
    // Basic sum
    int sum = std::accumulate(numbers.begin(), numbers.end(), 0);
    std::cout << "Sum: " << sum << std::endl;
    
    // Sum with different initial value
    int sum_with_init = std::accumulate(numbers.begin(), numbers.end(), 10);
    std::cout << "Sum with initial value 10: " << sum_with_init << std::endl;
    
    // Product using multiplication
    int product = std::accumulate(numbers.begin(), numbers.end(), 1, 
                                 [](int acc, int x) { return acc * x; });
    std::cout << "Product: " << product << std::endl;
    
    // String concatenation
    std::vector<std::string> words = {"Hello", " ", "World", "!"};
    std::string sentence = std::accumulate(words.begin(), words.end(), 
                                          std::string(),
                                          [](const std::string& acc, const std::string& word) {
                                              return acc + word;
                                          });
    std::cout << "Concatenated: " << sentence << std::endl;
    
    // Maximum element
    int max_val = std::accumulate(numbers.begin(), numbers.end(), numbers[0],
                                 [](int acc, int x) { return std::max(acc, x); });
    std::cout << "Maximum: " << max_val << std::endl;
}
```

### iota - Sequential Generation
```cpp
void demonstrateIota() {
    std::cout << "\n=== iota Examples ===" << std::endl;
    
    // Fill with sequential numbers starting from 0
    std::vector<int> vec1(10);
    std::iota(vec1.begin(), vec1.end(), 0);
    std::cout << "0 to 9: ";
    for (int x : vec1) std::cout << x << " ";
    std::cout << std::endl;
    
    // Fill with sequential numbers starting from 5
    std::vector<int> vec2(5);
    std::iota(vec2.begin(), vec2.end(), 5);
    std::cout << "5 to 9: ";
    for (int x : vec2) std::cout << x << " ";
    std::cout << std::endl;
    
    // Fill with sequential characters
    std::vector<char> chars(5);
    std::iota(chars.begin(), chars.end(), 'A');
    std::cout << "A to E: ";
    for (char c : chars) std::cout << c << " ";
    std::cout << std::endl;
    
    // Create index array
    std::vector<size_t> indices(8);
    std::iota(indices.begin(), indices.end(), 0);
    std::cout << "Indices: ";
    for (size_t idx : indices) std::cout << idx << " ";
    std::cout << std::endl;
}
```

## 🔧 Advanced Numeric Operations

### inner_product - Vector Operations
```cpp
void demonstrateInnerProduct() {
    std::cout << "\n=== inner_product Examples ===" << std::endl;
    
    std::vector<int> vec1 = {1, 2, 3, 4};
    std::vector<int> vec2 = {5, 6, 7, 8};
    
    // Dot product
    int dot_product = std::inner_product(vec1.begin(), vec1.end(),
                                       vec2.begin(), 0);
    std::cout << "Dot product: " << dot_product << std::endl;
    std::cout << "Manual: 1*5 + 2*6 + 3*7 + 4*8 = " << dot_product << std::endl;
    
    // Custom operations - sum of absolute differences
    int abs_diff_sum = std::inner_product(vec1.begin(), vec1.end(),
                                         vec2.begin(), 0,
                                         std::plus<>(),
                                         [](int a, int b) { return std::abs(a - b); });
    std::cout << "Sum of absolute differences: " << abs_diff_sum << std::endl;
    
    // Count matching elements
    int matches = std::inner_product(vec1.begin(), vec1.end(),
                                    vec2.begin(), 0,
                                    std::plus<>(),
                                    [](int a, int b) { return a == b ? 1 : 0; });
    std::cout << "Number of matching elements: " << matches << std::endl;
    
    // Custom product with different operations
    int custom_result = std::inner_product(vec1.begin(), vec1.end(),
                                          vec2.begin(), 1,
                                          [](int acc, int x) { return acc * x; },
                                          [](int a, int b) { return a + b; });
    std::cout << "Product of sums: " << custom_result << std::endl;
}
```

### partial_sum - Prefix Operations
```cpp
void demonstratePartialSum() {
    std::cout << "\n=== partial_sum Examples ===" << std::endl;
    
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    std::vector<int> result;
    
    // Running total
    std::partial_sum(numbers.begin(), numbers.end(),
                    std::back_inserter(result));
    std::cout << "Running total: ";
    for (int x : result) std::cout << x << " ";
    std::cout << std::endl;
    
    // Running product
    result.clear();
    std::partial_sum(numbers.begin(), numbers.end(),
                    std::back_inserter(result),
                    std::multiplies<>());
    std::cout << "Running product: ";
    for (int x : result) std::cout << x << " ";
    std::cout << std::endl;
    
    // Running maximum
    result.clear();
    std::partial_sum(numbers.begin(), numbers.end(),
                    std::back_inserter(result),
                    [](int a, int b) { return std::max(a, b); });
    std::cout << "Running maximum: ";
    for (int x : result) std::cout << x << " ";
    std::cout << std::endl;
    
    // Fibonacci sequence generation
    std::vector<int> fib(10);
    fib[0] = 0;
    fib[1] = 1;
    std::partial_sum(fib.begin(), fib.end() - 2,
                    fib.begin() + 2,
                    [](int a, int b) { return a + b; });
    std::cout << "Fibonacci sequence: ";
    for (int x : fib) std::cout << x << " ";
    std::cout << std::endl;
}
```

### adjacent_difference - Difference Operations
```cpp
void demonstrateAdjacentDifference() {
    std::cout << "\n=== adjacent_difference Examples ===" << std::endl;
    
    std::vector<int> numbers = {1, 4, 9, 16, 25};
    std::vector<int> result;
    
    // Differences between consecutive elements
    std::adjacent_difference(numbers.begin(), numbers.end(),
                            std::back_inserter(result));
    std::cout << "Differences: ";
    for (int x : result) std::cout << x << " ";
    std::cout << std::endl;
    std::cout << "Note: First element is always the original first element" << std::endl;
    
    // Ratios between consecutive elements
    result.clear();
    std::adjacent_difference(numbers.begin(), numbers.end(),
                            std::back_inserter(result),
                            std::divides<>());
    std::cout << "Ratios: ";
    for (int x : result) std::cout << x << " ";
    std::cout << std::endl;
    
    // Maximum of consecutive pairs
    result.clear();
    std::adjacent_difference(numbers.begin(), numbers.end(),
                            std::back_inserter(result),
                            [](int a, int b) { return std::max(a, b); });
    std::cout << "Max of consecutive pairs: ";
    for (int x : result) std::cout << x << " ";
    std::cout << std::endl;
    
    // Check if sequence is increasing
    result.clear();
    std::adjacent_difference(numbers.begin(), numbers.end(),
                            std::back_inserter(result),
                            [](int a, int b) { return b > a ? 1 : 0; });
    bool is_increasing = std::all_of(result.begin() + 1, result.end(),
                                   [](int x) { return x == 1; });
    std::cout << "Is sequence increasing: " << (is_increasing ? "Yes" : "No") << std::endl;
}
```

## 🎮 Practical Examples

### Example 1: Statistical Analysis
```cpp
#include <iostream>
#include <numeric>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>

class StatisticsCalculator {
private:
    std::vector<double> data;
    
public:
    StatisticsCalculator(const std::vector<double>& d) : data(d) {}
    
    // Calculate mean
    double mean() const {
        if (data.empty()) return 0.0;
        double sum = std::accumulate(data.begin(), data.end(), 0.0);
        return sum / data.size();
    }
    
    // Calculate median
    double median() const {
        if (data.empty()) return 0.0;
        
        std::vector<double> sorted = data;
        std::sort(sorted.begin(), sorted.end());
        
        size_t n = sorted.size();
        if (n % 2 == 0) {
            return (sorted[n/2 - 1] + sorted[n/2]) / 2.0;
        } else {
            return sorted[n/2];
        }
    }
    
    // Calculate variance
    double variance() const {
        if (data.size() <= 1) return 0.0;
        
        double m = mean();
        double sum_sq_diff = std::accumulate(data.begin(), data.end(), 0.0,
                                           [m](double acc, double x) {
                                               double diff = x - m;
                                               return acc + diff * diff;
                                           });
        return sum_sq_diff / (data.size() - 1);
    }
    
    // Calculate standard deviation
    double stdDeviation() const {
        return std::sqrt(variance());
    }
    
    // Calculate correlation coefficient
    double correlation(const std::vector<double>& other) const {
        if (data.size() != other.size() || data.empty()) return 0.0;
        
        double mean1 = mean();
        double mean2 = std::accumulate(other.begin(), other.end(), 0.0) / other.size();
        
        double sum_xy = std::inner_product(data.begin(), data.end(),
                                         other.begin(), 0.0,
                                         std::plus<>(),
                                         [mean1, mean2](double x, double y) {
                                             return (x - mean1) * (y - mean2);
                                         });
        
        double sum_x2 = std::accumulate(data.begin(), data.end(), 0.0,
                                      [mean1](double acc, double x) {
                                          double diff = x - mean1;
                                          return acc + diff * diff;
                                      });
        
        double sum_y2 = std::accumulate(other.begin(), other.end(), 0.0,
                                      [mean2](double acc, double y) {
                                          double diff = y - mean2;
                                          return acc + diff * diff;
                                      });
        
        return sum_xy / std::sqrt(sum_x2 * sum_y2);
    }
    
    // Calculate percentiles
    double percentile(double p) const {
        if (data.empty() || p < 0 || p > 100) return 0.0;
        
        std::vector<double> sorted = data;
        std::sort(sorted.begin(), sorted.end());
        
        double index = (p / 100.0) * (sorted.size() - 1);
        size_t lower = static_cast<size_t>(std::floor(index));
        size_t upper = static_cast<size_t>(std::ceil(index));
        
        if (lower == upper) {
            return sorted[lower];
        }
        
        double weight = index - lower;
        return sorted[lower] * (1 - weight) + sorted[upper] * weight;
    }
    
    // Display statistics
    void displayStatistics() const {
        std::cout << std::fixed << std::setprecision(2);
        std::cout << "Statistical Analysis:" << std::endl;
        std::cout << "  Count: " << data.size() << std::endl;
        std::cout << "  Mean: " << mean() << std::endl;
        std::cout << "  Median: " << median() << std::endl;
        std::cout << "  Variance: " << variance() << std::endl;
        std::cout << "  Std Deviation: " << stdDeviation() << std::endl;
        std::cout << "  Min: " << *std::min_element(data.begin(), data.end()) << std::endl;
        std::cout << "  Max: " << *std::max_element(data.begin(), data.end()) << std::endl;
        std::cout << "  25th percentile: " << percentile(25) << std::endl;
        std::cout << "  75th percentile: " << percentile(75) << std::endl;
    }
};

int main() {
    std::cout << "=== Statistical Analysis ===" << std::endl;
    
    // Sample data
    std::vector<double> data = {65, 70, 75, 80, 85, 90, 95, 100, 105, 110};
    
    StatisticsCalculator stats(data);
    stats.displayStatistics();
    
    // Correlation example
    std::vector<double> data2 = {60, 68, 72, 78, 82, 88, 92, 98, 102, 108};
    double corr = stats.correlation(data2);
    std::cout << "Correlation with second dataset: " << corr << std::endl;
    
    return 0;
}
```

### Example 2: Financial Calculations
```cpp
#include <iostream>
#include <numeric>
#include <vector>
#include <iomanip>

class FinancialCalculator {
public:
    // Calculate compound interest
    static double compoundInterest(double principal, double rate, int years, int compounds_per_year = 1) {
        std::vector<double> factors(years * compounds_per_year);
        std::iota(factors.begin(), factors.end(), 1);
        
        double amount = principal;
        for (int factor : factors) {
            amount *= (1 + rate / compounds_per_year);
        }
        
        return amount;
    }
    
    // Calculate Net Present Value (NPV)
    static double npv(const std::vector<double>& cashflows, double discount_rate) {
        std::vector<double> discount_factors(cashflows.size());
        std::iota(discount_factors.begin(), discount_factors.end(), 0);
        
        return std::inner_product(cashflows.begin(), cashflows.end(),
                                 discount_factors.begin(), 0.0,
                                 std::plus<>(),
                                 [discount_rate](double cf, double period) {
                                     return cf / std::pow(1 + discount_rate, period);
                                 });
    }
    
    // Calculate Internal Rate of Return (IRR) - simplified Newton-Raphson
    static double irr(const std::vector<double>& cashflows, double guess = 0.1, double tolerance = 1e-6) {
        double rate = guess;
        
        for (int i = 0; i < 100; ++i) {
            double npv_value = npv(cashflows, rate);
            
            std::vector<double> periods(cashflows.size());
            std::iota(periods.begin(), periods.end(), 0);
            
            double d_npv = std::inner_product(cashflows.begin(), cashflows.end(),
                                            periods.begin(), 0.0,
                                            std::plus<>(),
                                            [rate](double cf, double period) {
                                                return -period * cf / std::pow(1 + rate, period + 1);
                                            });
            
            double new_rate = rate - npv_value / d_npv;
            
            if (std::abs(new_rate - rate) < tolerance) {
                return new_rate;
            }
            
            rate = new_rate;
        }
        
        return rate; // Return best estimate if not converged
    }
    
    // Calculate moving average
    static std::vector<double> movingAverage(const std::vector<double>& prices, int window) {
        std::vector<double> result;
        
        if (window <= 0 || prices.size() < static_cast<size_t>(window)) {
            return result;
        }
        
        for (size_t i = window - 1; i < prices.size(); ++i) {
            double sum = std::accumulate(prices.begin() + i - window + 1,
                                       prices.begin() + i + 1, 0.0);
            result.push_back(sum / window);
        }
        
        return result;
    }
    
    // Calculate returns
    static std::vector<double> returns(const std::vector<double>& prices) {
        std::vector<double> result;
        
        if (prices.size() < 2) {
            return result;
        }
        
        std::adjacent_difference(prices.begin(), prices.end(),
                                std::back_inserter(result),
                                [](double current, double previous) {
                                    return (current - previous) / previous;
                                });
        
        // Remove first element (it's just the first price)
        result.erase(result.begin());
        return result;
    }
    
    // Calculate volatility (standard deviation of returns)
    static double volatility(const std::vector<double>& prices) {
        auto ret = returns(prices);
        if (ret.empty()) return 0.0;
        
        double mean_return = std::accumulate(ret.begin(), ret.end(), 0.0) / ret.size();
        
        double variance = std::accumulate(ret.begin(), ret.end(), 0.0,
                                        [mean_return](double acc, double r) {
                                            double diff = r - mean_return;
                                            return acc + diff * diff;
                                        }) / (ret.size() - 1);
        
        return std::sqrt(variance);
    }
};

int main() {
    std::cout << "=== Financial Calculations ===" << std::endl;
    std::cout << std::fixed << std::setprecision(2);
    
    // Compound interest
    double principal = 1000.0;
    double rate = 0.05; // 5%
    int years = 10;
    
    double future_value = FinancialCalculator::compoundInterest(principal, rate, years);
    std::cout << "Compound Interest:" << std::endl;
    std::cout << "  Principal: $" << principal << std::endl;
    std::cout << "  Rate: " << (rate * 100) << "%" << std::endl;
    std::cout << "  Years: " << years << std::endl;
    std::cout << "  Future Value: $" << future_value << std::endl;
    
    // NPV and IRR
    std::vector<double> cashflows = {-1000, 200, 300, 400, 500, 600};
    double discount_rate = 0.08;
    
    double npv_value = FinancialCalculator::npv(cashflows, discount_rate);
    double irr_value = FinancialCalculator::irr(cashflows);
    
    std::cout << "\nInvestment Analysis:" << std::endl;
    std::cout << "  Cashflows: ";
    for (double cf : cashflows) std::cout << "$" << cf << " ";
    std::cout << std::endl;
    std::cout << "  NPV (8% discount): $" << npv_value << std::endl;
    std::cout << "  IRR: " << (irr_value * 100) << "%" << std::endl;
    
    // Stock analysis
    std::vector<double> stock_prices = {100, 105, 102, 108, 110, 115, 112, 118, 120, 125};
    
    auto ma = FinancialCalculator::movingAverage(stock_prices, 3);
    auto ret = FinancialCalculator::returns(stock_prices);
    double vol = FinancialCalculator::volatility(stock_prices);
    
    std::cout << "\nStock Analysis:" << std::endl;
    std::cout << "  Prices: ";
    for (double price : stock_prices) std::cout << "$" << price << " ";
    std::cout << std::endl;
    
    std::cout << "  3-day Moving Average: ";
    for (double avg : ma) std::cout << "$" << avg << " ";
    std::cout << std::endl;
    
    std::cout << "  Volatility: " << (vol * 100) << "%" << std::endl;
    
    return 0;
}
```

### Example 3: Signal Processing
```cpp
#include <iostream>
#include <numeric>
#include <vector>
#include <complex>
#include <cmath>
#include <algorithm>

class SignalProcessor {
public:
    using Complex = std::complex<double>;
    
    // Generate sine wave
    static std::vector<double> generateSineWave(double frequency, double amplitude, 
                                               double duration, double sample_rate) {
        size_t num_samples = static_cast<size_t>(duration * sample_rate);
        std::vector<double> signal(num_samples);
        
        std::iota(signal.begin(), signal.end(), 0);
        std::transform(signal.begin(), signal.end(), signal.begin(),
                      [frequency, amplitude, sample_rate](size_t i) {
                          return amplitude * std::sin(2 * M_PI * frequency * i / sample_rate);
                      });
        
        return signal;
    }
    
    // Convolution
    static std::vector<double> convolve(const std::vector<double>& signal,
                                       const std::vector<double>& kernel) {
        size_t signal_size = signal.size();
        size_t kernel_size = kernel.size();
        size_t result_size = signal_size + kernel_size - 1;
        
        std::vector<double> result(result_size, 0.0);
        
        for (size_t i = 0; i < result_size; ++i) {
            double sum = 0.0;
            for (size_t j = 0; j < kernel_size; ++j) {
                if (i >= j && i - j < signal_size) {
                    sum += signal[i - j] * kernel[j];
                }
            }
            result[i] = sum;
        }
        
        return result;
    }
    
    // Moving average filter
    static std::vector<double> movingAverageFilter(const std::vector<double>& signal, int window_size) {
        std::vector<double> kernel(window_size, 1.0 / window_size);
        return convolve(signal, kernel);
    }
    
    // Calculate RMS (Root Mean Square)
    static double rms(const std::vector<double>& signal) {
        if (signal.empty()) return 0.0;
        
        double sum_squares = std::accumulate(signal.begin(), signal.end(), 0.0,
                                           [](double acc, double x) {
                                               return acc + x * x;
                                           });
        
        return std::sqrt(sum_squares / signal.size());
    }
    
    // Calculate peak-to-peak value
    static double peakToPeak(const std::vector<double>& signal) {
        if (signal.empty()) return 0.0;
        
        auto min_max = std::minmax_element(signal.begin(), signal.end());
        return *min_max.second - *min_max.first;
    }
    
    // Calculate zero crossing rate
    static double zeroCrossingRate(const std::vector<double>& signal) {
        if (signal.size() < 2) return 0.0;
        
        int crossings = std::inner_product(signal.begin(), signal.end() - 1,
                                         signal.begin() + 1, 0,
                                         std::plus<>(),
                                         [](double a, double b) {
                                             return (a * b < 0) ? 1 : 0;
                                         });
        
        return static_cast<double>(crossings) / (signal.size() - 1);
    }
    
    // Simple DFT (Discrete Fourier Transform)
    static std::vector<Complex> dft(const std::vector<double>& signal) {
        size_t N = signal.size();
        std::vector<Complex> spectrum(N);
        
        for (size_t k = 0; k < N; ++k) {
            Complex sum(0.0, 0.0);
            
            for (size_t n = 0; n < N; ++n) {
                double angle = -2.0 * M_PI * k * n / N;
                sum += signal[n] * Complex(std::cos(angle), std::sin(angle));
            }
            
            spectrum[k] = sum;
        }
        
        return spectrum;
    }
    
    // Calculate power spectrum
    static std::vector<double> powerSpectrum(const std::vector<Complex>& spectrum) {
        std::vector<double> power;
        
        std::transform(spectrum.begin(), spectrum.end(),
                      std::back_inserter(power),
                      [](const Complex& c) {
                          return std::norm(c); // |c|^2
                      });
        
        return power;
    }
    
    // Display signal statistics
    static void displaySignalStats(const std::vector<double>& signal, const std::string& name) {
        std::cout << "\n" << name << " Statistics:" << std::endl;
        std::cout << "  Length: " << signal.size() << " samples" << std::endl;
        std::cout << "  RMS: " << rms(signal) << std::endl;
        std::cout << "  Peak-to-Peak: " << peakToPeak(signal) << std::endl;
        std::cout << "  Zero Crossing Rate: " << zeroCrossingRate(signal) << std::endl;
    }
};

int main() {
    std::cout << "=== Signal Processing ===" << std::endl;
    
    // Generate test signal
    double frequency = 5.0; // 5 Hz
    double amplitude = 1.0;
    double duration = 1.0; // 1 second
    double sample_rate = 100.0; // 100 Hz
    
    auto signal = SignalProcessor::generateSineWave(frequency, amplitude, duration, sample_rate);
    
    // Add some noise
    std::vector<double> noisy_signal = signal;
    for (auto& sample : noisy_signal) {
        sample += (std::rand() % 100 - 50) / 500.0; // Add small random noise
    }
    
    // Apply moving average filter
    auto filtered_signal = SignalProcessor::movingAverageFilter(noisy_signal, 5);
    
    // Display statistics
    SignalProcessor::displaySignalStats(signal, "Original Signal");
    SignalProcessor::displaySignalStats(noisy_signal, "Noisy Signal");
    SignalProcessor::displaySignalStats(filtered_signal, "Filtered Signal");
    
    // Frequency analysis
    auto spectrum = SignalProcessor::dft(signal);
    auto power = SignalProcessor::powerSpectrum(spectrum);
    
    std::cout << "\nFrequency Analysis:" << std::endl;
    std::cout << "  DC Component: " << power[0] << std::endl;
    
    // Find dominant frequency (excluding DC)
    auto max_it = std::max_element(power.begin() + 1, power.begin() + power.size() / 2);
    size_t dominant_freq_index = std::distance(power.begin() + 1, max_it) + 1;
    double dominant_frequency = dominant_freq_index * sample_rate / signal.size();
    
    std::cout << "  Dominant Frequency: " << dominant_frequency << " Hz" << std::endl;
    std::cout << "  Expected Frequency: " << frequency << " Hz" << std::endl;
    
    return 0;
}
```

### Example 4: Mathematical Series and Sequences
```cpp
#include <iostream>
#include <numeric>
#include <vector>
#include <iomanip>

class SeriesCalculator {
public:
    // Arithmetic series
    static std::vector<int> arithmeticSeries(int first, int difference, int count) {
        std::vector<int> series(count);
        series[0] = first;
        
        std::adjacent_difference(series.begin(), series.end() - 1,
                                series.begin() + 1,
                                [difference](int, int) { return difference; });
        
        return series;
    }
    
    // Geometric series
    static std::vector<double> geometricSeries(double first, double ratio, int count) {
        std::vector<double> series(count);
        series[0] = first;
        
        std::adjacent_difference(series.begin(), series.end() - 1,
                                series.begin() + 1,
                                [ratio](double, double prev) { return prev * ratio; });
        
        return series;
    }
    
    // Fibonacci sequence
    static std::vector<long long> fibonacci(int count) {
        if (count <= 0) return {};
        if (count == 1) return {0};
        
        std::vector<long long> fib(count);
        fib[0] = 0;
        fib[1] = 1;
        
        std::partial_sum(fib.begin(), fib.end() - 2,
                        fib.begin() + 2,
                        [](long long a, long long b) { return a + b; });
        
        return fib;
    }
    
    // Prime numbers using Sieve of Eratosthenes
    static std::vector<int> primes(int n) {
        if (n < 2) return {};
        
        std::vector<bool> is_prime(n + 1, true);
        is_prime[0] = is_prime[1] = false;
        
        for (int p = 2; p * p <= n; ++p) {
            if (is_prime[p]) {
                for (int multiple = p * p; multiple <= n; multiple += p) {
                    is_prime[multiple] = false;
                }
            }
        }
        
        std::vector<int> primes_list;
        for (int i = 2; i <= n; ++i) {
            if (is_prime[i]) {
                primes_list.push_back(i);
            }
        }
        
        return primes_list;
    }
    
    // Triangular numbers
    static std::vector<int> triangularNumbers(int count) {
        std::vector<int> numbers(count);
        std::iota(numbers.begin(), numbers.end(), 1);
        
        std::partial_sum(numbers.begin(), numbers.end(),
                        numbers.begin());
        
        return numbers;
    }
    
    // Factorial sequence
    static std::vector<long long> factorials(int count) {
        if (count <= 0) return {};
        
        std::vector<long long> facts(count);
        facts[0] = 1;
        
        std::vector<int> multipliers(count);
        std::iota(multipliers.begin(), multipliers.end(), 1);
        
        std::partial_sum(multipliers.begin(), multipliers.end(),
                        facts.begin(),
                        std::multiplies<long long>());
        
        return facts;
    }
    
    // Calculate series sum
    template<typename T>
    static T seriesSum(const std::vector<T>& series) {
        return std::accumulate(series.begin(), series.end(), T{0});
    }
    
    // Calculate series product
    template<typename T>
    static T seriesProduct(const std::vector<T>& series) {
        return std::accumulate(series.begin(), series.end(), T{1}, std::multiplies<T>());
    }
    
    // Check if series is arithmetic
    static bool isArithmetic(const std::vector<int>& series) {
        if (series.size() < 2) return true;
        
        int diff = series[1] - series[0];
        
        return std::adjacent_find(series.begin(), series.end(),
                                [diff](int a, int b) {
                                    return (b - a) != diff;
                                }) == series.end();
    }
    
    // Check if series is geometric
    static bool isGeometric(const std::vector<double>& series) {
        if (series.size() < 2) return true;
        
        double ratio = series[1] / series[0];
        
        return std::adjacent_find(series.begin(), series.end(),
                                [ratio](double a, double b) {
                                    return std::abs(b / a - ratio) > 1e-10;
                                }) == series.end();
    }
    
    // Display series
    template<typename T>
    static void displaySeries(const std::vector<T>& series, const std::string& name) {
        std::cout << name << ": ";
        for (size_t i = 0; i < std::min(series.size(), size_t(10)); ++i) {
            std::cout << series[i];
            if (i < std::min(series.size(), size_t(10)) - 1) {
                std::cout << ", ";
            }
        }
        if (series.size() > 10) {
            std::cout << ", ...";
        }
        std::cout << std::endl;
    }
};

int main() {
    std::cout << "=== Mathematical Series and Sequences ===" << std::endl;
    
    // Arithmetic series
    auto arithmetic = SeriesCalculator::arithmeticSeries(2, 3, 10);
    SeriesCalculator::displaySeries(arithmetic, "Arithmetic (2, 3, 10)");
    std::cout << "Sum: " << SeriesCalculator::seriesSum(arithmetic) << std::endl;
    std::cout << "Is arithmetic: " << (SeriesCalculator::isArithmetic(arithmetic) ? "Yes" : "No") << std::endl;
    
    // Geometric series
    auto geometric = SeriesCalculator::geometricSeries(2, 2, 8);
    SeriesCalculator::displaySeries(geometric, "Geometric (2, 2, 8)");
    std::cout << "Sum: " << SeriesCalculator::seriesSum(geometric) << std::endl;
    std::cout << "Product: " << SeriesCalculator::seriesProduct(geometric) << std::endl;
    std::cout << "Is geometric: " << (SeriesCalculator::isGeometric(geometric) ? "Yes" : "No") << std::endl;
    
    // Fibonacci sequence
    auto fib = SeriesCalculator::fibonacci(15);
    SeriesCalculator::displaySeries(fib, "Fibonacci (15)");
    std::cout << "Sum: " << SeriesCalculator::seriesSum(fib) << std::endl;
    
    // Prime numbers
    auto primes = SeriesCalculator::primes(30);
    SeriesCalculator::displaySeries(primes, "Primes up to 30");
    std::cout << "Count: " << primes.size() << std::endl;
    
    // Triangular numbers
    auto triangular = SeriesCalculator::triangularNumbers(10);
    SeriesCalculator::displaySeries(triangular, "Triangular numbers (10)");
    std::cout << "Sum: " << SeriesCalculator::seriesSum(triangular) << std::endl;
    
    // Factorials
    auto factorials = SeriesCalculator::factorials(10);
    SeriesCalculator::displaySeries(factorials, "Factorials (10)");
    std::cout << "Sum: " << SeriesCalculator::seriesSum(factorials) << std::endl;
    
    return 0;
}
```

## 📊 Complete Function Reference

### Accumulation Operations
| Function | Description | Complexity |
|----------|-------------|------------|
| `accumulate(first, last, init)` | Sum elements with init | O(n) |
| `accumulate(first, last, init, op)` | Custom accumulation | O(n) |

### Sequential Operations
| Function | Description | Complexity |
|----------|-------------|------------|
| `iota(first, last, value)` | Fill with sequential values | O(n) |

### Vector Operations
| Function | Description | Complexity |
|----------|-------------|------------|
| `inner_product(first1, last1, first2, init)` | Dot product | O(n) |
| `inner_product(first1, last1, first2, init, op1, op2)` | Custom inner product | O(n) |

### Prefix Operations
| Function | Description | Complexity |
|----------|-------------|------------|
| `partial_sum(first, last, result)` | Running total | O(n) |
| `partial_sum(first, last, result, op)` | Custom prefix operation | O(n) |

### Difference Operations
| Function | Description | Complexity |
|----------|-------------|------------|
| `adjacent_difference(first, last, result)` | Consecutive differences | O(n) |
| `adjacent_difference(first, last, result, op)` | Custom difference | O(n) |

## ⚡ Performance Considerations

### Type Selection
```cpp
// Choose appropriate initial value type
std::vector<int> large_numbers(1000, 1000000);

// Problem - potential overflow
int sum_int = std::accumulate(large_numbers.begin(), large_numbers.end(), 0);

// Solution - use larger type
long long sum_ll = std::accumulate(large_numbers.begin(), large_numbers.end(), 0LL);

// Or use double for floating point
double sum_d = std::accumulate(large_numbers.begin(), large_numbers.end(), 0.0);
```

### Custom Operations
```cpp
// Efficient custom operations
auto sum_squares = std::accumulate(vec.begin(), vec.end(), 0,
                                 [](int acc, int x) { return acc + x * x; });

// More efficient than separate transform then accumulate
```

## 🎯 Common Patterns

### Pattern 1: Running Statistics
```cpp
// Calculate running average
std::vector<double> running_average;
std::partial_sum(data.begin(), data.end(),
                std::back_inserter(running_average),
                [](double sum, double x) { return sum + x; });

// Convert sums to averages
std::transform(running_average.begin(), running_average.end(),
              running_average.begin(),
              [n = 1](double sum) mutable { return sum / n++; });
```

### Pattern 2: Custom Aggregation
```cpp
// Find minimum and maximum in one pass
struct MinMax {
    int min_val, max_val;
    MinMax(int val) : min_val(val), max_val(val) {}
};

MinMax result = std::accumulate(data.begin() + 1, data.end(),
                              MinMax(data[0]),
                              [](MinMax acc, int x) {
                                  acc.min_val = std::min(acc.min_val, x);
                                  acc.max_val = std::max(acc.max_val, x);
                                  return acc;
                              });
```

### Pattern 3: Mathematical Series
```cpp
// Generate arithmetic progression
std::vector<int> arithmetic(n);
std::iota(arithmetic.begin(), arithmetic.end(), first);
std::transform(arithmetic.begin(), arithmetic.end(),
              arithmetic.begin(),
              [difference](int x) { return x * difference; });
```

## 🐛 Common Pitfalls & Solutions

### 1. Wrong Initial Value Type
```cpp
// Problem - overflow with large numbers
std::vector<int> big_numbers(1000, 1000000);
int sum = std::accumulate(big_numbers.begin(), big_numbers.end(), 0); // Overflow!

// Solution - use appropriate type
long long sum = std::accumulate(big_numbers.begin(), big_numbers.end(), 0LL);
```

### 2. Floating Point Precision
```cpp
// Problem - precision loss with integers
std::vector<int> numbers = {1, 2, 3};
double average = std::accumulate(numbers.begin(), numbers.end(), 0) / numbers.size(); // Integer division!

// Solution - use floating point
double average = std::accumulate(numbers.begin(), numbers.end(), 0.0) / numbers.size();
```

### 3. adjacent_difference First Element
```cpp
// Problem - misunderstanding first element
std::vector<int> nums = {1, 3, 5, 7};
std::vector<int> diffs;
std::adjacent_difference(nums.begin(), nums.end(), std::back_inserter(diffs));
// diffs = {1, 2, 2, 2} - first element is original, not difference!

// Solution - handle first element separately
if (!diffs.empty()) {
    diffs.erase(diffs.begin()); // Remove first element if you want only differences
}
```

## 📚 Related Headers

- `algorithm.md` - General algorithms
- `iterator.md` - Iterator utilities
- `cmath.md` - Mathematical functions
- `functional.md` - Function objects

## 🚀 Best Practices

1. **Choose appropriate initial value type** to avoid overflow
2. **Use custom operations** for complex aggregations
3. **Prefer numeric algorithms** over manual loops for clarity
4. **Be aware of floating point precision** issues
5. **Understand adjacent_difference behavior** with first element
6. **Use iota for sequential initialization** instead of manual loops
7. **Consider performance** for large datasets

## 🎯 When to Use numeric Algorithms

✅ **Use when:**
- Performing mathematical operations on ranges
- Calculating statistics and aggregates
- Working with time series data
- Implementing financial calculations
- Signal processing applications
- Generating mathematical sequences

❌ **Avoid when:**
- Simple arithmetic with small datasets
- Non-numeric operations
- Need for complex mathematical functions (use `<cmath>`)
- Performance-critical inner loops with custom optimizations

---

**Examples in this file**: 4 complete programs  
**Key Functions**: `accumulate`, `iota`, `inner_product`, `partial_sum`, `adjacent_difference`  
**Time Complexity**: O(n) for all operations  
**Space Complexity**: O(1) additional (except where output iterator creates new range)
