# Basic Bit Operations

## Introduction
Bit manipulation involves directly working with the binary representation of numbers. Understanding bitwise operations is essential for optimization, low-level programming, and solving many algorithmic problems efficiently.

## Binary Number System

### Number Representation
- **Binary**: Base-2 number system (0, 1)
- **Bit**: Single binary digit (0 or 1)
- **Byte**: 8 bits
- **Word**: Machine-dependent number of bits (typically 32 or 64)

### Signed Number Representation
- **Two's Complement**: Most common signed integer representation
- **Sign Bit**: Most significant bit indicates sign (0 = positive, 1 = negative)
- **Range**: For n bits, range is [-2^(n-1), 2^(n-1)-1]

## Bitwise Operators

### 1. Basic Bitwise Operators
```cpp
class BitwiseOperators {
public:
    // Bitwise AND (&)
    static int bitwiseAnd(int a, int b) {
        return a & b;
    }
    
    // Bitwise OR (|)
    static int bitwiseOr(int a, int b) {
        return a | b;
    }
    
    // Bitwise XOR (^)
    static int bitwiseXor(int a, int b) {
        return a ^ b;
    }
    
    // Bitwise NOT (~)
    static int bitwiseNot(int a) {
        return ~a;
    }
    
    // Left Shift (<<)
    static int leftShift(int a, int k) {
        return a << k;
    }
    
    // Right Shift (>>)
    static int rightShift(int a, int k) {
        return a >> k;
    }
    
    // Demonstration of all operators
    static void demonstrateOperators(int a, int b) {
        std::cout << "a = " << a << " (" << std::bitset<8>(a) << ")" << std::endl;
        std::cout << "b = " << b << " (" << std::bitset<8>(b) << ")" << std::endl;
        std::cout << "a & b = " << (a & b) << " (" << std::bitset<8>(a & b) << ")" << std::endl;
        std::cout << "a | b = " << (a | b) << " (" << std::bitset<8>(a | b) << ")" << std::endl;
        std::cout << "a ^ b = " << (a ^ b) << " (" << std::bitset<8>(a ^ b) << ")" << std::endl;
        std::cout << "~a = " << (~a) << " (" << std::bitset<8>(~a) << ")" << std::endl;
        std::cout << "a << 2 = " << (a << 2) << " (" << std::bitset<8>(a << 2) << ")" << std::endl;
        std::cout << "a >> 2 = " << (a >> 2) << " (" << std::bitset<8>(a >> 2) << ")" << std::endl;
    }
};
```

### 2. Operator Properties
```cpp
class BitwiseProperties {
public:
    // Commutative properties
    static bool testCommutative() {
        int a = 5, b = 3;
        return (a & b) == (b & a) && 
               (a | b) == (b | a) && 
               (a ^ b) == (b ^ a);
    }
    
    // Associative properties
    static bool testAssociative() {
        int a = 5, b = 3, c = 1;
        return ((a & b) & c) == (a & (b & c)) && 
               ((a | b) | c) == (a | (b | c)) && 
               ((a ^ b) ^ c) == (a ^ (b ^ c));
    }
    
    // Distributive properties
    static bool testDistributive() {
        int a = 5, b = 3, c = 1;
        return (a & (b | c)) == ((a & b) | (a & c)) && 
               (a | (b & c)) == ((a | b) & (a | c));
    }
    
    // Identity elements
    static void testIdentity() {
        int a = 5;
        std::cout << "a & ~0 = " << (a & ~0) << " (should be " << a << ")" << std::endl;
        std::cout << "a | 0 = " << (a | 0) << " (should be " << a << ")" << std::endl;
        std::cout << "a ^ 0 = " << (a ^ 0) << " (should be " << a << ")" << std::endl;
    }
};
```

## Bit Manipulation Techniques

### 1. Bit Checking and Setting
```cpp
class BitManipulation {
public:
    // Check if bit k is set (0-indexed from right)
    static bool isBitSet(int n, int k) {
        return (n & (1 << k)) != 0;
    }
    
    // Set bit k
    static int setBit(int n, int k) {
        return n | (1 << k);
    }
    
    // Clear bit k
    static int clearBit(int n, int k) {
        return n & ~(1 << k);
    }
    
    // Toggle bit k
    static int toggleBit(int n, int k) {
        return n ^ (1 << k);
    }
    
    // Get value of bit k
    static int getBit(int n, int k) {
        return (n >> k) & 1;
    }
    
    // Update bit k to value v (0 or 1)
    static int updateBit(int n, int k, int v) {
        int mask = 1 << k;
        return (n & ~mask) | ((v << k) & mask);
    }
    
    // Demonstration
    static void demonstrateBitManipulation() {
        int n = 10; // Binary: 1010
        
        std::cout << "Original number: " << n << " (" << std::bitset<8>(n) << ")" << std::endl;
        std::cout << "Bit 2 is set: " << isBitSet(n, 2) << std::endl;
        std::cout << "Set bit 1: " << setBit(n, 1) << " (" << std::bitset<8>(setBit(n, 1)) << ")" << std::endl;
        std::cout << "Clear bit 3: " << clearBit(n, 3) << " (" << std::bitset<8>(clearBit(n, 3)) << ")" << std::endl;
        std::cout << "Toggle bit 0: " << toggleBit(n, 0) << " (" << std::bitset<8>(toggleBit(n, 0)) << ")" << std::endl;
    }
};
```

### 2. Bit Counting Operations
```cpp
class BitCounting {
public:
    // Count set bits (naive approach)
    static int countSetBitsNaive(int n) {
        int count = 0;
        while (n > 0) {
            count += n & 1;
            n >>= 1;
        }
        return count;
    }
    
    // Count set bits (Brian Kernighan's algorithm)
    static int countSetBits(int n) {
        int count = 0;
        while (n) {
            n &= (n - 1); // Clear the rightmost set bit
            count++;
        }
        return count;
    }
    
    // Count set bits using built-in function
    static int countSetBitsBuiltIn(int n) {
        return __builtin_popcount(n);
    }
    
    // Count clear bits
    static int countClearBits(int n) {
        int bitCount = sizeof(n) * 8;
        return bitCount - countSetBits(n);
    }
    
    // Count leading zeros
    static int countLeadingZeros(int n) {
        if (n == 0) return sizeof(n) * 8;
        return __builtin_clz(n);
    }
    
    // Count trailing zeros
    static int countTrailingZeros(int n) {
        if (n == 0) return sizeof(n) * 8;
        return __builtin_ctz(n);
    }
    
    // Find position of rightmost set bit (1-indexed)
    static int getRightmostSetBitPosition(int n) {
        if (n == 0) return -1;
        return __builtin_ctz(n) + 1;
    }
    
    // Find position of leftmost set bit (1-indexed)
    static int getLeftmostSetBitPosition(int n) {
        if (n == 0) return -1;
        return sizeof(n) * 8 - __builtin_clz(n);
    }
};
```

### 3. Bit Extraction and Modification
```cpp
class BitExtraction {
public:
    // Extract k bits starting from position p
    static int extractBits(int n, int p, int k) {
        return (n >> p) & ((1 << k) - 1);
    }
    
    // Replace k bits starting from position p with value m
    static int replaceBits(int n, int p, int k, int m) {
        int mask = ((1 << k) - 1) << p;
        return (n & ~mask) | ((m << p) & mask);
    }
    
    // Swap two bits at positions p and q
    static int swapBits(int n, int p, int q) {
        if (((n >> p) & 1) != ((n >> q) & 1)) {
            int mask = (1 << p) | (1 << q);
            n ^= mask;
        }
        return n;
    }
    
    // Get most significant bit (MSB)
    static int getMSB(int n) {
        if (n == 0) return 0;
        return 1 << (31 - __builtin_clz(n));
    }
    
    // Clear all bits except MSB
    static int keepOnlyMSB(int n) {
        return getMSB(n);
    }
    
    // Clear MSB
    static int clearMSB(int n) {
        return n & (n - 1);
    }
};
```

## Mathematical Operations Using Bits

### 1. Arithmetic Operations
```cpp
class BitArithmetic {
public:
    // Add two numbers using bitwise operations
    static int add(int a, int b) {
        while (b != 0) {
            int carry = a & b;
            a = a ^ b;
            b = carry << 1;
        }
        return a;
    }
    
    // Subtract two numbers using bitwise operations
    static int subtract(int a, int b) {
        while (b != 0) {
            int borrow = (~a) & b;
            a = a ^ b;
            b = borrow << 1;
        }
        return a;
    }
    
    // Multiply two numbers using bitwise operations
    static int multiply(int a, int b) {
        int result = 0;
        
        while (b > 0) {
            if (b & 1) {
                result = add(result, a);
            }
            a <<= 1;
            b >>= 1;
        }
        
        return result;
    }
    
    // Divide two numbers using bitwise operations
    static std::pair<int, int> divide(int dividend, int divisor) {
        if (divisor == 0) return {INT_MAX, 0};
        
        bool negative = (dividend < 0) ^ (divisor < 0);
        long long dvd = abs(dividend);
        long long dvs = abs(divisor);
        
        int quotient = 0;
        for (int i = 31; i >= 0; i--) {
            if ((dvs << i) <= dvd) {
                dvd -= (dvs << i);
                quotient += (1 << i);
            }
        }
        
        if (negative) quotient = -quotient;
        return {quotient, static_cast<int>(dvd)};
    }
    
    // Absolute value without branching
    static int absoluteValue(int n) {
        int mask = n >> (sizeof(int) * 8 - 1);
        return (n ^ mask) - mask;
    }
};
```

### 2. Power and Logarithm Operations
```cpp
class BitPower {
public:
    // Calculate power using bitwise operations
    static long long power(int base, int exp) {
        long long result = 1;
        
        while (exp > 0) {
            if (exp & 1) {
                result *= base;
            }
            base *= base;
            exp >>= 1;
        }
        
        return result;
    }
    
    // Check if number is power of 2
    static bool isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }
    
    // Get next power of 2 greater than n
    static int nextPowerOfTwo(int n) {
        if (n <= 1) return 2;
        
        n--;
        n |= n >> 1;
        n |= n >> 2;
        n |= n >> 4;
        n |= n >> 8;
        n |= n >> 16;
        n++;
        
        return n;
    }
    
    // Get previous power of 2 less than or equal to n
    static int previousPowerOfTwo(int n) {
        if (n <= 1) return 1;
        
        n |= n >> 1;
        n |= n >> 2;
        n |= n >> 4;
        n |= n >> 8;
        n |= n >> 16;
        
        return n - (n >> 1);
    }
    
    // Calculate log2 (floor)
    static int log2Floor(int n) {
        if (n <= 0) return -1;
        return 31 - __builtin_clz(n);
    }
    
    // Calculate log2 (ceil)
    static int log2Ceil(int n) {
        if (n <= 1) return 0;
        return 32 - __builtin_clz(n - 1);
    }
};
```

## Bit Tricks and Optimizations

### 1. Common Bit Tricks
```cpp
class BitTricks {
public:
    // Swap two numbers without temporary variable
    static void swapNumbers(int& a, int& b) {
        a ^= b;
        b ^= a;
        a ^= b;
    }
    
    // Find maximum of two numbers without branching
    static int max(int a, int b) {
        return b ^ ((a ^ b) & -(a < b));
    }
    
    // Find minimum of two numbers without branching
    static int min(int a, int b) {
        return a ^ ((a ^ b) & -(a < b));
    }
    
    // Check if numbers have opposite signs
    static bool oppositeSigns(int a, int b) {
        return (a ^ b) < 0;
    }
    
    // Check if number is even
    static bool isEven(int n) {
        return (n & 1) == 0;
    }
    
    // Check if number is odd
    static bool isOdd(int n) {
        return (n & 1) == 1;
    }
    
    // Multiply by 2 using left shift
    static int multiplyBy2(int n) {
        return n << 1;
    }
    
    // Divide by 2 using right shift
    static int divideBy2(int n) {
        return n >> 1;
    }
    
    // Check if kth bit is set in multiple numbers
    static bool checkBitInMultiple(const std::vector<int>& nums, int k) {
        for (int num : nums) {
            if ((num & (1 << k)) == 0) {
                return false;
            }
        }
        return true;
    }
};
```

### 2. Advanced Bit Operations
```cpp
class AdvancedBitOps {
public:
    // Reverse bits of a number
    static unsigned int reverseBits(unsigned int n) {
        unsigned int result = 0;
        int bitCount = sizeof(n) * 8;
        
        for (int i = 0; i < bitCount; i++) {
            result <<= 1;
            result |= (n & 1);
            n >>= 1;
        }
        
        return result;
    }
    
    // Rotate bits left by k positions
    static unsigned int rotateLeft(unsigned int n, int k) {
        int bitCount = sizeof(n) * 8;
        k %= bitCount;
        
        return (n << k) | (n >> (bitCount - k));
    }
    
    // Rotate bits right by k positions
    static unsigned int rotateRight(unsigned int n, int k) {
        int bitCount = sizeof(n) * 8;
        k %= bitCount;
        
        return (n >> k) | (n << (bitCount - k));
    }
    
    // Swap odd and even bits
    static unsigned int swapOddEvenBits(unsigned int n) {
        unsigned int evenBits = n & 0xAAAAAAAA; // Mask for even positions
        unsigned int oddBits = n & 0x55555555;  // Mask for odd positions
        
        evenBits >>= 1;
        oddBits <<= 1;
        
        return evenBits | oddBits;
    }
    
    // Find the only non-duplicate element in array where others appear twice
    static int findUnique(const std::vector<int>& arr) {
        int result = 0;
        for (int num : arr) {
            result ^= num;
        }
        return result;
    }
    
    // Find two unique elements where others appear twice
    static std::pair<int, int> findTwoUnique(const std::vector<int>& arr) {
        int xorAll = 0;
        for (int num : arr) {
            xorAll ^= num;
        }
        
        // Find rightmost set bit
        int rightmostSet = xorAll & -xorAll;
        
        int num1 = 0, num2 = 0;
        for (int num : arr) {
            if (num & rightmostSet) {
                num1 ^= num;
            } else {
                num2 ^= num;
            }
        }
        
        return {num1, num2};
    }
};
```

## Bit Masks and Flags

### 1. Bit Mask Operations
```cpp
class BitMasks {
public:
    // Create mask with k bits set
    static int createMask(int k) {
        return (1 << k) - 1;
    }
    
    // Create mask with bits from l to r set
    static int createRangeMask(int l, int r) {
        return ((1 << (r - l + 1)) - 1) << l;
    }
    
    // Check if all bits in mask are set
    static bool areAllBitsSet(int n, int mask) {
        return (n & mask) == mask;
    }
    
    // Check if any bit in mask is set
    static bool isAnyBitSet(int n, int mask) {
        return (n & mask) != 0;
    }
    
    // Clear all bits in mask
    static int clearMaskBits(int n, int mask) {
        return n & ~mask;
    }
    
    // Toggle all bits in mask
    static int toggleMaskBits(int n, int mask) {
        return n ^ mask;
    }
};
```

### 2. Flag Management
```cpp
class FlagManager {
private:
    int flags;
    
public:
    FlagManager() : flags(0) {}
    
    // Set flag
    void setFlag(int flag) {
        flags |= (1 << flag);
    }
    
    // Clear flag
    void clearFlag(int flag) {
        flags &= ~(1 << flag);
    }
    
    // Toggle flag
    void toggleFlag(int flag) {
        flags ^= (1 << flag);
    }
    
    // Check if flag is set
    bool isFlagSet(int flag) const {
        return (flags & (1 << flag)) != 0;
    }
    
    // Set multiple flags
    void setFlags(int mask) {
        flags |= mask;
    }
    
    // Clear multiple flags
    void clearFlags(int mask) {
        flags &= ~mask;
    }
    
    // Get all flags
    int getFlags() const {
        return flags;
    }
};
```

## Performance Analysis

### Time Complexity
| Operation | Time Complexity |
|-----------|-----------------|
| Bit Check/Set/Clear | O(1) |
| Bit Count (Kernighan) | O(number of set bits) |
| Bit Count (Built-in) | O(1) |
| Bit Reversal | O(log n) |
| Bit Rotation | O(1) |
| Arithmetic Operations | O(log n) |

### Space Complexity
- Most bit operations: O(1)
- Bit counting with lookup table: O(1) with O(2^k) space

## Best Practices

### 1. Code Readability
- Use meaningful variable names
- Add comments explaining bit operations
- Use functions for complex bit manipulations
- Consider using bit fields for structure members

### 2. Performance Optimization
- Use built-in functions when available
- Consider lookup tables for repeated operations
- Minimize branching in bit operations
- Use appropriate data types

### 3. Portability
- Be careful with signed vs unsigned
- Consider endianness for multi-byte operations
- Use fixed-width integers when size matters
- Test on different platforms

## Common Applications

### 1. Optimization
- Fast multiplication/division by powers of 2
- Efficient modulo operations for powers of 2
- Compact data storage
- Fast mathematical operations

### 2. Algorithms
- Graph algorithms (bitmask DP)
- Subset generation
- Permutation generation
- Compression algorithms

### 3. System Programming
- Device driver programming
- Network protocol implementation
- File system operations
- Memory management

## Summary

Bit manipulation is a powerful technique for writing efficient and optimized code. Understanding bitwise operations, their properties, and common patterns enables developers to solve complex problems elegantly and efficiently. Mastering bit operations is essential for systems programming, competitive programming, and performance-critical applications.
