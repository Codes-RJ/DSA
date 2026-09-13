# `std::bitset` — Fixed-Size Bit Sequences

> **Minimum standard:** C++17 for the examples in this lesson
>
> **Canonical location:** Standard-library reference.

## std::bitset (Fixed-Size Bit Set)

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

## Next Step

Return to the [standard-library index](README.md) or continue along the [C++ and DSA learning path](../../LEARNING_PATH.md).

