# Specialized Containers in C++

## Overview
Specialized containers are designed for specific use cases and provide optimized operations for particular domains. C++ provides two main specialized containers: `std::bitset` for fixed-size bit manipulation and `std::valarray` for numerical array operations. These containers offer specialized functionality not available in general-purpose containers.

## Key Characteristics

| Container | Purpose | Size | Operations | Memory | Performance |
|-----------|---------|------|------------|--------|-------------|
| bitset | Bit manipulation | Fixed at compile-time | Bitwise operations | Compact | Highly optimized |
| valarray | Numerical computing | Dynamic | Mathematical operations | Array-based | Vectorized operations |

---

## 1. std::bitset (Fixed-Size Bit Set)

### Theory
`std::bitset` is a container that stores a fixed-size sequence of bits. It provides efficient bit manipulation operations and is optimized for space (each bit is stored as a single bit). The size must be known at compile time.

**Key Features:**
- Fixed size determined at compile time
- Space-efficient (1 bit per element)
- Provides bitwise operations (AND, OR, XOR, NOT)
- Supports shift operations
- Conversion to/from strings and integers
- Individual bit access with bounds checking

**Use Cases:**
- Flag management (compiler flags, permissions)
- State tracking (visited flags, availability bits)
- Compact representation of boolean arrays
- Bitmask operations
- Set representation for small domains
- Bit manipulation algorithms

### All Functions and Operations

```cpp
#include <iostream>
#include <bitset>
#include <string>
#include <climits>

void demonstrateBitset() {
    std::cout << "\n========== STD::BITSET ==========\n";
    
    // ==================== CONSTRUCTORS & INITIALIZATION ====================
    std::cout << "\n--- Constructors & Initialization ---\n";
    
    // Default constructor (all bits 0)
    std::bitset<8> b1;
    std::cout << "b1 (default): " << b1 << "\n";
    
    // From unsigned long long
    std::bitset<8> b2(42);          // 42 decimal = 00101010 binary
    std::bitset<8> b3(0b10101010);  // Binary literal
    std::cout << "b2 (42): " << b2 << "\n";
    std::cout << "b3 (0b10101010): " << b3 << "\n";
    
    // From string (C++11)
    std::bitset<8> b4(std::string("10101010"));
    std::bitset<8> b5("11001100");  // Direct string literal
    std::cout << "b4 (string): " << b4 << "\n";
    
    // From string with custom characters
    std::bitset<8> b6(std::string("1010"), 0, 4, '0', '1');
    std::cout << "b6 (partial string): " << b6 << "\n";
    
    // Copy constructor
    std::bitset<8> b7(b2);
    std::cout << "b7 (copy of b2): " << b7 << "\n";
    
    // ==================== ACCESSING BITS ====================
    std::cout << "\n--- Accessing Bits ---\n";
    
    std::bitset<8> bits("10101010");
    
    // operator[] - access individual bit (returns reference for lvalue)
    std::cout << "Bit at position 0: " << bits[0] << "\n";
    std::cout << "Bit at position 1: " << bits[1] << "\n";
    std::cout << "Bit at position 2: " << bits[2] << "\n";
    
    // Modifying bits
    bits[0] = 1;
    bits[1] = 0;
    std::cout << "After modifying bits: " << bits << "\n";
    
    // test() - access with bounds checking
    std::cout << "test(2): " << bits.test(2) << "\n";
    try {
        std::cout << "test(10): " << bits.test(10) << "\n";  // Throws exception
    } catch (const std::out_of_range& e) {
        std::cout << "Exception: " << e.what() << "\n";
    }
    
    // ==================== BIT OPERATIONS ====================
    std::cout << "\n--- Bit Operations ---\n";
    
    std::bitset<8> a("10101010");
    std::bitset<8> b("11001100");
    
    std::cout << "a: " << a << "\n";
    std::cout << "b: " << b << "\n";
    
    // Bitwise operators
    std::cout << "a & b: " << (a & b) << "\n";
    std::cout << "a | b: " << (a | b) << "\n";
    std::cout << "a ^ b: " << (a ^ b) << "\n";
    std::cout << "~a: " << (~a) << "\n";
    
    // Shift operations
    std::cout << "a << 2: " << (a << 2) << "\n";
    std::cout << "a >> 2: " << (a >> 2) << "\n";
    
    // Compound assignment operators
    a &= b;
    std::cout << "a &= b: " << a << "\n";
    
    // ==================== BITSET OPERATIONS ====================
    std::cout << "\n--- Bitset Operations ---\n";
    
    std::bitset<8> ops("10101010");
    
    // set() - set bits
    ops.set();                    // Set all bits to 1
    std::cout << "set all: " << ops << "\n";
    
    ops.set(2);                   // Set specific bit
    std::cout << "set bit 2: " << ops << "\n";
    
    ops.set(3, 0);                // Set bit with value
    std::cout << "set bit 3 to 0: " << ops << "\n";
    
    // reset() - clear bits
    ops.reset();                  // Reset all bits to 0
    std::cout << "reset all: " << ops << "\n";
    
    ops.set(4);
    ops.reset(4);                 // Reset specific bit
    std::cout << "reset bit 4: " << ops << "\n";
    
    // flip() - toggle bits
    ops = std::bitset<8>("10101010");
    ops.flip();                   // Flip all bits
    std::cout << "flip all: " << ops << "\n";
    
    ops.flip(3);                  // Flip specific bit
    std::cout << "flip bit 3: " << ops << "\n";
    
    // ==================== QUERY OPERATIONS ====================
    std::cout << "\n--- Query Operations ---\n";
    
    std::bitset<8> query("10101010");
    
    std::cout << "any(): " << query.any() << "\n";        // Any bit set?
    std::cout << "all(): " << query.all() << "\n";        // All bits set?
    std::cout << "none(): " << query.none() << "\n";      // No bits set?
    std::cout << "count(): " << query.count() << "\n";    // Number of set bits
    std::cout << "size(): " << query.size() << "\n";      // Total bits
    
    // ==================== CONVERSIONS ====================
    std::cout << "\n--- Conversions ---\n";
    
    std::bitset<8> convert("10101010");
    
    // to_string()
    std::string str = convert.to_string();
    std::cout << "to_string(): " << str << "\n";
    std::cout << "to_string('O','I'): " << convert.to_string('O', 'I') << "\n";
    
    // to_ulong() - convert to unsigned long
    unsigned long ul = convert.to_ulong();
    std::cout << "to_ulong(): " << ul << "\n";
    
    // to_ullong() - convert to unsigned long long (C++11)
    unsigned long long ull = convert.to_ullong();
    std::cout << "to_ullong(): " << ull << "\n";
    
    // ==================== COMPARISON ====================
    std::cout << "\n--- Comparison ---\n";
    
    std::bitset<8> comp1("10101010");
    std::bitset<8> comp2("10101010");
    std::bitset<8> comp3("11001100");
    
    std::cout << "comp1 == comp2: " << (comp1 == comp2) << "\n";
    std::cout << "comp1 == comp3: " << (comp1 == comp3) << "\n";
    std::cout << "comp1 != comp3: " << (comp1 != comp3) << "\n";
    
    // ==================== PRACTICAL EXAMPLES ====================
    
    // Example 1: Permission Flags
    std::cout << "\n--- Example 1: Permission Flags ---\n";
    
    // Define permission bits
    const int READ = 0;
    const int WRITE = 1;
    const int EXECUTE = 2;
    const int DELETE = 3;
    const int ADMIN = 4;
    
    std::bitset<8> permissions;
    permissions[READ] = 1;
    permissions[WRITE] = 1;
    permissions[EXECUTE] = 0;
    
    std::cout << "Permissions: " << permissions << "\n";
    std::cout << "Can read: " << permissions[READ] << "\n";
    std::cout << "Can write: " << permissions[WRITE] << "\n";
    std::cout << "Can execute: " << permissions[EXECUTE] << "\n";
    
    // Grant execute permission
    permissions[EXECUTE] = 1;
    std::cout << "After granting execute: " << permissions << "\n";
    
    // Check admin permission
    if (!permissions[ADMIN]) {
        std::cout << "Admin access not granted\n";
    }
    
    // Example 2: Set Operations (for small universes)
    std::cout << "\n--- Example 2: Set Operations ---\n";
    
    // Universe: {0,1,2,3,4,5,6,7}
    std::bitset<8> setA("10101010");  // {1,3,5,7}
    std::bitset<8> setB("11001100");  // {2,3,6,7}
    
    std::cout << "Set A: " << setA << "\n";
    std::cout << "Set B: " << setB << "\n";
    
    // Set operations
    std::cout << "Union (A ∪ B): " << (setA | setB) << "\n";
    std::cout << "Intersection (A ∩ B): " << (setA & setB) << "\n";
    std::cout << "Difference (A \\ B): " << (setA & ~setB) << "\n";
    std::cout << "Symmetric difference (A Δ B): " << (setA ^ setB) << "\n";
    std::cout << "Complement of A: " << ~setA << "\n";
    
    // Subset check
    std::bitset<8> subset("10100000");  // {5,7}
    if ((subset & ~setA).none()) {
        std::cout << "subset is subset of A\n";
    }
    
    // Example 3: Error Code Flags
    std::cout << "\n--- Example 3: Error Code Flags ---\n";
    
    enum ErrorFlags {
        ERR_NONE = 0,
        ERR_MEMORY = 1 << 0,      // 1
        ERR_DISK = 1 << 1,        // 2
        ERR_NETWORK = 1 << 2,     // 4
        ERR_TIMEOUT = 1 << 3,     // 8
        ERR_PERMISSION = 1 << 4,  // 16
        ERR_CORRUPTION = 1 << 5   // 32
    };
    
    std::bitset<8> errors;
    errors.set(ERR_MEMORY);
    errors.set(ERR_NETWORK);
    errors.set(ERR_TIMEOUT);
    
    std::cout << "Error flags: " << errors << "\n";
    
    // Check specific errors
    if (errors[ERR_MEMORY]) std::cout << "Memory error detected!\n";
    if (errors[ERR_DISK]) std::cout << "Disk error detected!\n";
    if (errors[ERR_NETWORK]) std::cout << "Network error detected!\n";
    
    // Clear specific error
    errors[ERR_NETWORK] = 0;
    std::cout << "After clearing network error: " << errors << "\n";
    
    // Example 4: Bloom Filter Simulation (Simplified)
    std::cout << "\n--- Example 4: Bloom Filter Simulation ---\n";
    
    class SimpleBloomFilter {
    private:
        std::bitset<64> bits;
        
        // Simple hash functions
        size_t hash1(const std::string& s) {
            size_t h = 0;
            for (char c : s) h = (h * 131) + c;
            return h % 64;
        }
        
        size_t hash2(const std::string& s) {
            size_t h = 0;
            for (char c : s) h = (h * 31) + c;
            return h % 64;
        }
        
    public:
        void add(const std::string& item) {
            bits.set(hash1(item));
            bits.set(hash2(item));
        }
        
        bool mightContain(const std::string& item) {
            return bits.test(hash1(item)) && bits.test(hash2(item));
        }
        
        void display() {
            std::cout << "Bloom filter: " << bits << "\n";
        }
    };
    
    SimpleBloomFilter bloom;
    bloom.add("apple");
    bloom.add("banana");
    bloom.add("cherry");
    bloom.display();
    
    std::cout << "Contains 'apple': " << bloom.mightContain("apple") << "\n";
    std::cout << "Contains 'date': " << bloom.mightContain("date") << "\n";
    
    // Example 5: Sieve of Eratosthenes (Prime Numbers)
    std::cout << "\n--- Example 5: Sieve of Eratosthenes ---\n";
    
    const int MAX_NUM = 100;
    std::bitset<MAX_NUM + 1> sieve;
    sieve.set();  // Initially all true
    
    sieve[0] = sieve[1] = 0;  // 0 and 1 are not prime
    
    for (int i = 2; i * i <= MAX_NUM; i++) {
        if (sieve[i]) {
            for (int j = i * i; j <= MAX_NUM; j += i) {
                sieve[j] = 0;
            }
        }
    }
    
    std::cout << "Prime numbers up to " << MAX_NUM << ": ";
    for (int i = 2; i <= MAX_NUM; i++) {
        if (sieve[i]) std::cout << i << " ";
    }
    std::cout << "\n";
    
    // Example 6: Gray Code Generation
    std::cout << "\n--- Example 6: Gray Code Generation ---\n";
    
    auto grayCode = [](int n) {
        std::vector<std::bitset<4>> result;
        for (int i = 0; i < (1 << n); i++) {
            int gray = i ^ (i >> 1);
            result.push_back(std::bitset<4>(gray));
        }
        return result;
    };
    
    auto gray = grayCode(4);
    std::cout << "Gray code for 4 bits:\n";
    for (const auto& code : gray) {
        std::cout << "  " << code << " (" << code.to_ulong() << ")\n";
    }
    
    // Example 7: Circular Shift
    std::cout << "\n--- Example 7: Circular Shift ---\n";
    
    auto circularLeft = [](std::bitset<8> bits, int shift) {
        shift %= 8;
        return (bits << shift) | (bits >> (8 - shift));
    };
    
    auto circularRight = [](std::bitset<8> bits, int shift) {
        shift %= 8;
        return (bits >> shift) | (bits << (8 - shift));
    };
    
    std::bitset<8> original("10101010");
    std::cout << "Original: " << original << "\n";
    std::cout << "Circular left 2: " << circularLeft(original, 2) << "\n";
    std::cout << "Circular right 2: " << circularRight(original, 2) << "\n";
    
    // Example 8: Parity Check
    std::cout << "\n--- Example 8: Parity Check ---\n";
    
    auto parity = [](std::bitset<8> bits) -> int {
        return bits.count() % 2;
    };
    
    std::bitset<8> even_parity("10101010");  // 4 ones -> even
    std::bitset<8> odd_parity("10101011");   // 5 ones -> odd
    
    std::cout << "Even parity: " << even_parity << " -> " << parity(even_parity) << "\n";
    std::cout << "Odd parity: " << odd_parity << " -> " << parity(odd_parity) << "\n";
    
    // Example 9: Hamming Distance
    std::cout << "\n--- Example 9: Hamming Distance ---\n";
    
    auto hammingDistance = [](std::bitset<8> a, std::bitset<8> b) {
        return (a ^ b).count();
    };
    
    std::bitset<8> code1("10101010");
    std::bitset<8> code2("11001100");
    std::cout << "Hamming distance: " << hammingDistance(code1, code2) << "\n";
}
```

---

## 2. std::valarray (Numerical Array)

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
        x[i] = 2 * M_PI * i / N;
    }
    
    std::valarray<double> square_wave(0.0, N);
    
    // Approximate square wave using Fourier series
    for (int n = 1; n <= harmonics; n += 2) {
        square_wave += (4.0 / (n * M_PI)) * sin(n * x);
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

## Performance Comparison

| Container | Memory Layout | Access Time | Modification | Best For |
|-----------|--------------|-------------|--------------|----------|
| bitset | Compact (1 bit/element) | O(1) | O(1) | Bit flags, sets of small size |
| valarray | Contiguous array | O(1) | O(1) | Numerical computations |

---

## Best Practices

### For bitset:
1. **Use for fixed-size bit flags** - More efficient than vector<bool>
2. **Use bitwise operations** - Leverage optimized bit operations
3. **Use `test()` for bounds checking** - Safer than `operator[]` in debug
4. **Use `to_string()` for debugging** - Easy visualization
5. **Use `count()` for population count** - Efficient hardware implementation
6. **Use `any()`/`none()` for emptiness checks** - More expressive

### For valarray:
1. **Use for numerical computations** - Optimized for vectorization
2. **Leverage element-wise operations** - Cleaner than loops
3. **Use slices for subarray operations** - Efficient views
4. **Use masks for conditional operations** - No explicit loops
5. **Combine with STL algorithms** - When appropriate
6. **Use mathematical functions** - Optimized implementations

---

## Common Pitfalls

### For bitset:
1. **Out-of-bounds access** - Use `test()` for safety
2. **Forgetting size is compile-time** - Cannot be resized at runtime
3. **Assuming bitset is dynamic** - Size is fixed
4. **Using `to_ulong()` with too many bits** - Throws overflow_error
5. **Bit ordering confusion** - Index 0 is least significant bit

### For valarray:
1. **Not using element-wise operations** - Missing the point of valarray
2. **Assuming valarray is like vector** - Different API and behavior
3. **Not handling empty valarrays** - Some operations may fail
4. **Performance misconceptions** - May not be faster than simple loops
5. **Limited compiler optimization** - Vectorization depends on compiler
---

## Next Step

- Go to [Trees and Graphs](../05.%20Trees%20and%20Graphs/README.md) to continue to next topic.
