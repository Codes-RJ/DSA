# `std::valarray` — Numerical Arrays

> **Minimum standard:** C++17 for the examples in this lesson
>
> **Canonical location:** Standard-library reference.

## std::valarray (Numerical Array)

### Theory
`std::valarray` is a container designed for efficient numerical computations. It supports element-wise operations, mathematical functions, and is optimized for vectorized operations. The design focuses on performance for scientific and mathematical computing.

**Key Features:**
- Element-wise operations (+, -, *, /, etc.)
- Mathematical functions (sin, cos, exp, log, etc.)
- Array slicing and gslice (generalized slice)
- Masked operations
- Indirect addressing
- Optimized for vectorization

**Use Cases:**
- Scientific computing
- Signal processing
- Financial calculations
- Image processing
- Numerical simulations
- Mathematical transformations

### All Functions and Operations

```cpp
#include <iostream>
#include <valarray>
#include <cmath>
#include <numeric>

void demonstrateValarray() {
    std::cout << "\n========== STD::VALARRAY ==========\n";
    
    // ==================== CONSTRUCTORS & INITIALIZATION ====================
    std::cout << "\n--- Constructors & Initialization ---\n";
    
    // Default constructor
    std::valarray<int> v1;
    std::cout << "v1 size: " << v1.size() << "\n";
    
    // Size constructor
    std::valarray<int> v2(10);  // 10 elements, default-initialized
    std::cout << "v2 size: " << v2.size() << "\n";
    
    // Size and value constructor
    std::valarray<int> v3(5, 10);  // 10 elements, all 5
    std::cout << "v3: ";
    for (int x : v3) std::cout << x << " ";
    std::cout << "\n";
    
    // Initializer list (C++11)
    std::valarray<int> v4 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    std::cout << "v4: ";
    for (int x : v4) std::cout << x << " ";
    std::cout << "\n";
    
    // Copy constructor
    std::valarray<int> v5(v4);
    
    // ==================== BASIC OPERATIONS ====================
    std::cout << "\n--- Basic Operations ---\n";
    
    std::valarray<int> a = {1, 2, 3, 4, 5};
    std::valarray<int> b = {5, 4, 3, 2, 1};
    
    // Element-wise arithmetic
    std::cout << "a + b: ";
    auto sum = a + b;
    for (int x : sum) std::cout << x << " ";
    std::cout << "\n";
    
    std::cout << "a - b: ";
    auto diff = a - b;
    for (int x : diff) std::cout << x << " ";
    std::cout << "\n";
    
    std::cout << "a * b: ";
    auto prod = a * b;
    for (int x : prod) std::cout << x << " ";
    std::cout << "\n";
    
    std::cout << "a / b: ";
    auto quot = a / b;
    for (int x : quot) std::cout << x << " ";
    std::cout << "\n";
    
    std::cout << "a % b: ";
    auto mod = a % b;
    for (int x : mod) std::cout << x << " ";
    std::cout << "\n";
    
    // Scalar operations
    std::cout << "a + 10: ";
    auto add_scalar = a + 10;
    for (int x : add_scalar) std::cout << x << " ";
    std::cout << "\n";
    
    std::cout << "a * 2: ";
    auto mul_scalar = a * 2;
    for (int x : mul_scalar) std::cout << x << " ";
    std::cout << "\n";
    
    // Compound assignment
    auto c = a;
    c += b;
    std::cout << "c += b: ";
    for (int x : c) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== ACCESSING ELEMENTS ====================
    std::cout << "\n--- Accessing Elements ---\n";
    
    std::valarray<int> access = {10, 20, 30, 40, 50};
    
    // operator[]
    std::cout << "access[2]: " << access[2] << "\n";
    
    // Modify element
    access[2] = 99;
    std::cout << "After modification: ";
    for (int x : access) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== AGGREGATE FUNCTIONS ====================
    std::cout << "\n--- Aggregate Functions ---\n";
    
    std::valarray<int> agg = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    std::cout << "sum(): " << agg.sum() << "\n";
    std::cout << "min(): " << agg.min() << "\n";
    std::cout << "max(): " << agg.max() << "\n";
    
    // ==================== MATHEMATICAL FUNCTIONS ====================
    std::cout << "\n--- Mathematical Functions ---\n";
    
    std::valarray<double> math = {1.0, 2.0, 3.0, 4.0, 5.0};
    
    std::cout << "sqrt: ";
    for (double x : sqrt(math)) std::cout << x << " ";
    std::cout << "\n";
    
    std::cout << "exp: ";
    for (double x : exp(math)) std::cout << x << " ";
    std::cout << "\n";
    
    std::cout << "log: ";
    for (double x : log(math)) std::cout << x << " ";
    std::cout << "\n";
    
    std::cout << "sin: ";
    for (double x : sin(math)) std::cout << x << " ";
    std::cout << "\n";
    
    std::cout << "cos: ";
    for (double x : cos(math)) std::cout << x << " ";
    std::cout << "\n";
    
    std::cout << "abs: ";
    std::valarray<double> neg = {-1.0, -2.0, -3.0, -4.0, -5.0};
    for (double x : abs(neg)) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== SLICING ====================
    std::cout << "\n--- Slicing ---\n";
    
    std::valarray<int> slice_data = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    
    // std::slice(start, size, stride)
    std::slice slice1(2, 4, 2);  // Start at 2, take 4 elements, stride 2
    std::valarray<int> sliced1 = slice_data[slice1];
    
    std::cout << "Original: ";
    for (int x : slice_data) std::cout << x << " ";
    std::cout << "\n";
    
    std::cout << "Slice (start=2, size=4, stride=2): ";
    for (int x : sliced1) std::cout << x << " ";
    std::cout << "\n";
    
    // Modifying through slice
    slice_data[slice1] = 99;
    std::cout << "After modification: ";
    for (int x : slice_data) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== GSLCICE (Generalized Slice) ====================
    std::cout << "\n--- Generalized Slice (gslice) ---\n";
    
    // Create a 2D-like structure from 1D array
    std::valarray<int> matrix = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
    
    // Define a 3x4 matrix (3 rows, 4 columns)
    std::valarray<size_t> lengths = {3, 4};  // Number of elements in each dimension
    std::valarray<size_t> strides = {4, 1};  // Stride for each dimension
    
    std::gslice gs(0, lengths, strides);  // Start at index 0
    std::valarray<int> matrix_view = matrix[gs];
    
    std::cout << "Original 1D array: ";
    for (int x : matrix) std::cout << x << " ";
    std::cout << "\n";
    
    std::cout << "As 3x4 matrix:\n";
    for (size_t i = 0; i < lengths[0]; i++) {
        for (size_t j = 0; j < lengths[1]; j++) {
            std::cout << matrix_view[i * lengths[1] + j] << " ";
        }
        std::cout << "\n";
    }
    
    // ==================== MASKED OPERATIONS ====================
    std::cout << "\n--- Masked Operations ---\n";
    
    std::valarray<int> masked_data = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    std::valarray<bool> mask = {0, 1, 0, 1, 0, 1, 0, 1, 0, 1};  // Even indices
    
    std::valarray<int> masked = masked_data[mask];
    std::cout << "Original: ";
    for (int x : masked_data) std::cout << x << " ";
    std::cout << "\n";
    
    std::cout << "Masked (even indices): ";
    for (int x : masked) std::cout << x << " ";
    std::cout << "\n";
    
    // Conditional mask
    std::valarray<bool> greater_than_5 = masked_data > 5;
    std::valarray<int> filtered = masked_data[greater_than_5];
    
    std::cout << "Values > 5: ";
    for (int x : filtered) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== INDIRECT ADDRESSING ====================
    std::cout << "\n--- Indirect Addressing ---\n";
    
    std::valarray<int> indirect_data = {100, 101, 102, 103, 104, 105, 106, 107, 108, 109};
    std::valarray<size_t> indices = {0, 2, 4, 6, 8};  // Select specific indices
    
    std::valarray<int> selected = indirect_data[indices];
    std::cout << "Original: ";
    for (int x : indirect_data) std::cout << x << " ";
    std::cout << "\n";
    
    std::cout << "Selected indices (0,2,4,6,8): ";
    for (int x : selected) std::cout << x << " ";
    std::cout << "\n";
    
    // ==================== PRACTICAL EXAMPLES ====================
    
    // Example 1: Vector Dot Product
    std::cout << "\n--- Example 1: Vector Dot Product ---\n";
    
    std::valarray<double> vec1 = {1.0, 2.0, 3.0, 4.0, 5.0};
    std::valarray<double> vec2 = {5.0, 4.0, 3.0, 2.0, 1.0};
    
    double dot_product = (vec1 * vec2).sum();
    std::cout << "Dot product: " << dot_product << "\n";
    
    // Example 2: Matrix Multiplication (using slices)
    std::cout << "\n--- Example 2: Matrix Multiplication ---\n";
    
    // Create 2x3 matrix A and 3x2 matrix B
    std::valarray<double> A = {1, 2, 3, 4, 5, 6};  // 2x3
    std::valarray<double> B = {7, 8, 9, 10, 11, 12};  // 3x2
    
    size_t rowsA = 2, colsA = 3;
    size_t rowsB = 3, colsB = 2;
    
    std::valarray<double> C(rowsA * colsB);
    
    for (size_t i = 0; i < rowsA; i++) {
        for (size_t j = 0; j < colsB; j++) {
            std::valarray<double> rowA = A[std::slice(i * colsA, colsA, 1)];
            std::valarray<double> colB = B[std::slice(j, rowsB, colsB)];
            C[i * colsB + j] = (rowA * colB).sum();
        }
    }
    
    std::cout << "Matrix A (2x3):\n";
    for (size_t i = 0; i < rowsA; i++) {
        for (size_t j = 0; j < colsA; j++) {
            std::cout << A[i * colsA + j] << " ";
        }
        std::cout << "\n";
    }
    
    std::cout << "Matrix B (3x2):\n";
    for (size_t i = 0; i < rowsB; i++) {
        for (size_t j = 0; j < colsB; j++) {
            std::cout << B[i * colsB + j] << " ";
        }
        std::cout << "\n";
    }
    
    std::cout << "Result C = A * B (2x2):\n";
    for (size_t i = 0; i < rowsA; i++) {
        for (size_t j = 0; j < colsB; j++) {
            std::cout << C[i * colsB + j] << " ";
        }
        std::cout << "\n";
    }
    
    // Example 3: Polynomial Evaluation
    std::cout << "\n--- Example 3: Polynomial Evaluation ---\n";
    
    auto evaluatePolynomial = [](const std::valarray<double>& coeffs, double x) {
        std::valarray<double> powers(coeffs.size());
        for (size_t i = 0; i < coeffs.size(); i++) {
            powers[i] = std::pow(x, i);
        }
        return (coeffs * powers).sum();
    };
    
    std::valarray<double> coeffs = {1.0, 2.0, 3.0};  // 1 + 2x + 3x^2
    std::cout << "P(2) = " << evaluatePolynomial(coeffs, 2) << "\n";  // 1 + 4 + 12 = 17
    
    // Example 4: Signal Processing (Moving Average)
    std::cout << "\n--- Example 4: Moving Average ---\n";
    
    std::valarray<double> signal = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int window_size = 3;
    
    std::valarray<double> moving_avg(signal.size() - window_size + 1);
    
    for (size_t i = 0; i < moving_avg.size(); i++) {
        moving_avg[i] = signal[std::slice(i, window_size, 1)].sum() / window_size;
    }
    
    std::cout << "Original signal: ";
    for (double x : signal) std::cout << x << " ";
    std::cout << "\n";
    
    std::cout << "Moving average (window=3): ";
    for (double x : moving_avg) std::cout << x << " ";
    std::cout << "\n";
    
    // Example 5: Fourier Series Approximation
    std::cout << "\n--- Example 5: Fourier Series Approximation ---\n";
    
    const int N = 100;
    const int harmonics = 5;
    
    std::valarray<double> x = std::valarray<double>(0.0, N);
    for (int i = 0; i < N; i++) {
        x[i] = 2 * std::acos(-1.0) * i / N;
    }
    
    std::valarray<double> square_wave(0.0, N);
    
    // Approximate square wave using Fourier series
    for (int n = 1; n <= harmonics; n += 2) {
        square_wave += (4.0 / (n * std::acos(-1.0))) * sin(n * x);
    }
    
    std::cout << "Fourier approximation of square wave (first 5 harmonics):\n";
    for (int i = 0; i < std::min(10, N); i++) {
        std::cout << "  x=" << x[i] << ", f(x)=" << square_wave[i] << "\n";
    }
    
    // Example 6: Statistical Analysis
    std::cout << "\n--- Example 6: Statistical Analysis ---\n";
    
    std::valarray<double> data = {2.5, 3.7, 4.1, 3.9, 4.5, 3.2, 4.8, 3.3, 4.2, 3.6};
    
    double mean = data.sum() / data.size();
    std::valarray<double> deviations = data - mean;
    double variance = (deviations * deviations).sum() / data.size();
    double stddev = std::sqrt(variance);
    
    std::cout << "Data: ";
    for (double d : data) std::cout << d << " ";
    std::cout << "\n";
    std::cout << "Mean: " << mean << "\n";
    std::cout << "Variance: " << variance << "\n";
    std::cout << "Standard Deviation: " << stddev << "\n";
    
    // Example 7: Normalization
    std::cout << "\n--- Example 7: Data Normalization ---\n";
    
    std::valarray<double> raw_data = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    double min_val = raw_data.min();
    double max_val = raw_data.max();
    
    std::valarray<double> normalized = (raw_data - min_val) / (max_val - min_val);
    
    std::cout << "Original: ";
    for (double d : raw_data) std::cout << d << " ";
    std::cout << "\n";
    
    std::cout << "Normalized [0,1]: ";
    for (double d : normalized) std::cout << d << " ";
    std::cout << "\n";
    
    // Example 8: Convolution
    std::cout << "\n--- Example 8: Convolution ---\n";
    
    auto convolve = [](const std::valarray<double>& a, const std::valarray<double>& b) {
        size_t n = a.size() + b.size() - 1;
        std::valarray<double> result(0.0, n);
        
        for (size_t i = 0; i < a.size(); i++) {
            for (size_t j = 0; j < b.size(); j++) {
                result[i + j] += a[i] * b[j];
            }
        }
        return result;
    };
    
    std::valarray<double> kernel = {0.25, 0.5, 0.25};  // Smoothing kernel
    std::valarray<double> signal_conv = {1, 2, 3, 4, 5, 4, 3, 2, 1};
    
    auto smoothed = convolve(signal_conv, kernel);
    
    std::cout << "Original signal: ";
    for (double d : signal_conv) std::cout << d << " ";
    std::cout << "\n";
    
    std::cout << "Smoothed signal: ";
    for (double d : smoothed) std::cout << d << " ";
    std::cout << "\n";
}
```

---

## Next Step

Return to the [standard-library index](README.md) or continue along the [C++ and DSA learning path](../../LEARNING_PATH.md).
