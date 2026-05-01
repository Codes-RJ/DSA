# 04_Binary_Representation.md

## Binary Representation

### Overview

Binary representation is the fundamental way computers store and process information. Understanding how numbers are represented in binary, octal, and hexadecimal is essential for bit manipulation, debugging, and low-level programming. This topic covers number systems, conversions, signed integer representations, and practical techniques for working with binary data.

---

### 1. Number Systems

Computers use binary (base-2) internally, but programmers often work with decimal (base-10), octal (base-8), and hexadecimal (base-16) for convenience.

**Common Number Systems:**

| System | Base | Digits | Prefix | Example |
|--------|------|--------|--------|---------|
| **Binary** | 2 | 0,1 | `0b` or `0B` (C++14) | `0b1010` (10) |
| **Octal** | 8 | 0-7 | `0` | `012` (10) |
| **Decimal** | 10 | 0-9 | (none) | `10` |
| **Hexadecimal** | 16 | 0-9, A-F | `0x` or `0X` | `0xA` (10) |

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int number = 42;
    
    cout << "Number: " << number << endl;
    cout << "Binary:  " << bitset<8>(number) << endl;
    cout << "Octal:   " << oct << number << dec << endl;
    cout << "Decimal: " << dec << number << endl;
    cout << "Hex:     0x" << hex << number << dec << endl;
    
    // Literal representations (C++14 and later)
    int binary = 0b101010;   // Binary literal
    int octal = 052;         // Octal literal
    int hex = 0x2A;          // Hexadecimal literal
    
    cout << "\nLiterals:" << endl;
    cout << "0b101010 = " << binary << endl;
    cout << "052 = " << octal << endl;
    cout << "0x2A = " << hex << endl;
    
    return 0;
}
```

**Output:**
```
Number: 42
Binary:  00101010
Octal:   52
Decimal: 42
Hex:     0x2a

Literals:
0b101010 = 42
052 = 42
0x2A = 42
```

---

### 2. Binary to Decimal Conversion

**Method:** Multiply each bit by its place value (2ⁿ) and sum the results.

```
Binary: 1 0 1 0 1 (5 bits)
Places: 16 8 4 2 1
Result: 16 + 0 + 4 + 0 + 1 = 21
```

```cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int binaryToDecimal(const string& binary) {
    int result = 0;
    int power = 1;  // 2^0
    
    for (int i = binary.length() - 1; i >= 0; i--) {
        if (binary[i] == '1') {
            result += power;
        }
        power <<= 1;  // Multiply by 2
    }
    
    return result;
}

int binaryToDecimalAlternative(const string& binary) {
    return stoi(binary, nullptr, 2);
}

int main() {
    string binaries[] = {"0", "1", "10", "11", "100", "101", "111", "1000", "101010"};
    
    cout << "Binary to Decimal conversion:" << endl;
    for (const string& b : binaries) {
        int dec = binaryToDecimal(b);
        cout << b << " (binary) = " << dec << " (decimal)" << endl;
    }
    
    return 0;
}
```

**Output:**
```
Binary to Decimal conversion:
0 (binary) = 0 (decimal)
1 (binary) = 1 (decimal)
10 (binary) = 2 (decimal)
11 (binary) = 3 (decimal)
100 (binary) = 4 (decimal)
101 (binary) = 5 (decimal)
111 (binary) = 7 (decimal)
1000 (binary) = 8 (decimal)
101010 (binary) = 42 (decimal)
```

---

### 3. Decimal to Binary Conversion

**Method 1: Division by 2** (repeatedly divide by 2, collect remainders)

**Method 2: Bit manipulation** (using shifts)

```cpp
#include <iostream>
#include <string>
#include <algorithm>
#include <bitset>
using namespace std;

string decimalToBinaryDivision(int n) {
    if (n == 0) return "0";
    
    string binary = "";
    while (n > 0) {
        binary += (n % 2) ? '1' : '0';
        n /= 2;
    }
    reverse(binary.begin(), binary.end());
    return binary;
}

string decimalToBinaryShift(int n) {
    if (n == 0) return "0";
    
    string binary = "";
    int bitCount = sizeof(n) * 8;
    bool started = false;
    
    for (int i = bitCount - 1; i >= 0; i--) {
        if ((n >> i) & 1) {
            binary += '1';
            started = true;
        } else if (started) {
            binary += '0';
        }
    }
    return binary;
}

int main() {
    int numbers[] = {0, 1, 2, 5, 10, 16, 31, 32, 42, 100, 255};
    
    cout << "Decimal to Binary conversion:" << endl;
    for (int n : numbers) {
        string bin = decimalToBinaryDivision(n);
        cout << n << " = " << bin << " (binary)" << endl;
    }
    
    cout << "\nUsing bitset:" << endl;
    for (int n : numbers) {
        cout << n << " = " << bitset<8>(n) << " (8-bit binary)" << endl;
    }
    
    return 0;
}
```

**Output:**
```
Decimal to Binary conversion:
0 = 0 (binary)
1 = 1 (binary)
2 = 10 (binary)
5 = 101 (binary)
10 = 1010 (binary)
16 = 10000 (binary)
31 = 11111 (binary)
32 = 100000 (binary)
42 = 101010 (binary)
100 = 1100100 (binary)
255 = 11111111 (binary)

Using bitset:
0 = 00000000 (8-bit binary)
1 = 00000001 (8-bit binary)
2 = 00000010 (8-bit binary)
5 = 00000101 (8-bit binary)
10 = 00001010 (8-bit binary)
16 = 00010000 (8-bit binary)
31 = 00011111 (8-bit binary)
32 = 00100000 (8-bit binary)
42 = 00101010 (8-bit binary)
100 = 01100100 (8-bit binary)
255 = 11111111 (8-bit binary)
```

---

### 4. Hexadecimal Representation

Hexadecimal (base-16) uses digits 0-9 and A-F (10-15). Each hex digit represents 4 bits (a nibble).

**Hex to Binary Mapping:**

| Hex | Binary | Hex | Binary |
|-----|--------|-----|--------|
| 0 | 0000 | 8 | 1000 |
| 1 | 0001 | 9 | 1001 |
| 2 | 0010 | A | 1010 |
| 3 | 0011 | B | 1011 |
| 4 | 0100 | C | 1100 |
| 5 | 0101 | D | 1101 |
| 6 | 0110 | E | 1110 |
| 7 | 0111 | F | 1111 |

```cpp
#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

string decimalToHex(int n) {
    if (n == 0) return "0";
    
    string hex = "";
    const char* digits = "0123456789ABCDEF";
    
    while (n > 0) {
        hex = digits[n % 16] + hex;
        n /= 16;
    }
    return hex;
}

int hexToDecimal(const string& hex) {
    return stoi(hex, nullptr, 16);
}

int main() {
    int numbers[] = {0, 10, 15, 16, 31, 32, 42, 255, 256, 4095};
    
    cout << "Decimal to Hexadecimal:" << endl;
    for (int n : numbers) {
        cout << n << " = 0x" << decimalToHex(n) << endl;
    }
    
    cout << "\nHexadecimal to Decimal:" << endl;
    string hexes[] = {"0", "A", "F", "10", "1F", "20", "2A", "FF", "100", "FFF"};
    
    for (const string& h : hexes) {
        int dec = hexToDecimal(h);
        cout << "0x" << h << " = " << dec << endl;
    }
    
    return 0;
}
```

**Output:**
```
Decimal to Hexadecimal:
0 = 0x0
10 = 0xA
15 = 0xF
16 = 0x10
31 = 0x1F
32 = 0x20
42 = 0x2A
255 = 0xFF
256 = 0x100
4095 = 0xFFF

Hexadecimal to Decimal:
0x0 = 0
0xA = 10
0xF = 15
0x10 = 16
0x1F = 31
0x20 = 32
0x2A = 42
0xFF = 255
0x100 = 256
0xFFF = 4095
```

---

### 5. Signed Integer Representation (Two's Complement)

Most computers use two's complement to represent signed integers.

**Properties:**
- Positive numbers: same as unsigned binary
- Negative numbers: two's complement = (bitwise NOT) + 1
- Range for n-bit: -2ⁿ⁻¹ to 2ⁿ⁻¹ - 1

```cpp
#include <iostream>
#include <bitset>
#include <cstdint>
using namespace std;

int main() {
    // 8-bit signed integers (-128 to 127)
    cout << "Two's Complement Representation (8-bit):" << endl;
    
    for (int i = -16; i <= 16; i++) {
        cout << i << " = " << bitset<8>(i) << endl;
    }
    
    cout << "\nSpecial values:" << endl;
    cout << "0 = " << bitset<8>(0) << endl;
    cout << "127 = " << bitset<8>(127) << endl;
    cout << "-128 = " << bitset<8>(-128) << endl;
    cout << "-1 = " << bitset<8>(-1) << endl;
    
    // Two's complement conversion
    cout << "\nTwo's complement conversion:" << endl;
    int x = 42;
    int y = -42;
    
    cout << "Positive " << x << ": " << bitset<8>(x) << endl;
    cout << "Negative " << y << ": " << bitset<8>(y) << endl;
    cout << "Bitwise NOT of " << x << ": " << bitset<8>(~x) << endl;
    
    // Verify: -x = ~x + 1
    cout << "~" << x << " + 1 = " << (~x + 1) << " (which is " << -x << ")" << endl;
    
    return 0;
}
```

**Output:**
```
Two's Complement Representation (8-bit):
-16 = 11110000
-15 = 11110001
-14 = 11110010
-13 = 11110011
-12 = 11110100
-11 = 11110101
-10 = 11110110
-9 = 11110111
-8 = 11111000
-7 = 11111001
-6 = 11111010
-5 = 11111011
-4 = 11111100
-3 = 11111101
-2 = 11111110
-1 = 11111111
0 = 00000000
1 = 00000001
2 = 00000010
3 = 00000011
4 = 00000100
5 = 00000101
6 = 00000110
7 = 00000111
8 = 00001000
9 = 00001001
10 = 00001010
11 = 00001011
12 = 00001100
13 = 00001101
14 = 00001110
15 = 00001111
16 = 00010000

Special values:
0 = 00000000
127 = 01111111
-128 = 10000000
-1 = 11111111

Two's complement conversion:
Positive 42: 00101010
Negative -42: 11010110
Bitwise NOT of 42: 11010101
~42 + 1 = -42 (which is -42)
```

---

### 6. Bit Manipulation for Binary Representation

```cpp
#include <iostream>
#include <bitset>
using namespace std;

// Get bit at position i (0-indexed from LSB)
int getBit(int n, int i) {
    return (n >> i) & 1;
}

// Set bit at position i to 1
int setBit(int n, int i) {
    return n | (1 << i);
}

// Clear bit at position i to 0
int clearBit(int n, int i) {
    return n & ~(1 << i);
}

// Toggle bit at position i
int toggleBit(int n, int i) {
    return n ^ (1 << i);
}

// Update bit at position i to value (0 or 1)
int updateBit(int n, int i, int value) {
    return (n & ~(1 << i)) | (value << i);
}

// Extract bits from position i to j (inclusive)
int extractBits(int n, int i, int j) {
    int mask = ((1 << (j - i + 1)) - 1) << i;
    return (n & mask) >> i;
}

int main() {
    int n = 0b10101010;  // 170
    
    cout << "Original: " << bitset<8>(n) << " (0x" << hex << n << dec << ")" << endl;
    
    cout << "\nGet bit at position 3: " << getBit(n, 3) << endl;
    cout << "Set bit at position 2: " << bitset<8>(setBit(n, 2)) << endl;
    cout << "Clear bit at position 1: " << bitset<8>(clearBit(n, 1)) << endl;
    cout << "Toggle bit at position 4: " << bitset<8>(toggleBit(n, 4)) << endl;
    cout << "Update bit at position 5 to 0: " << bitset<8>(updateBit(n, 5, 0)) << endl;
    cout << "Extract bits 2-5: " << extractBits(n, 2, 5) << endl;
    
    return 0;
}
```

**Output:**
```
Original: 10101010 (0xaa)

Get bit at position 3: 1
Set bit at position 2: 10101110
Clear bit at position 1: 10101000
Toggle bit at position 4: 10111010
Update bit at position 5 to 0: 10101010
Extract bits 2-5: 10
```

---

### 7. Endianness

Endianness refers to the byte order of multi-byte values in memory.

- **Little-endian:** Least significant byte stored first (x86, x86_64)
- **Big-endian:** Most significant byte stored first (network protocols, some architectures)

```cpp
#include <iostream>
#include <cstdint>
using namespace std;

bool isLittleEndian() {
    uint16_t x = 1;
    return *reinterpret_cast<uint8_t*>(&x) == 1;
}

void printEndianness() {
    if (isLittleEndian()) {
        cout << "System is Little-endian" << endl;
    } else {
        cout << "System is Big-endian" << endl;
    }
}

template <typename T>
void printBytes(const T& value) {
    const uint8_t* bytes = reinterpret_cast<const uint8_t*>(&value);
    cout << "Bytes: ";
    for (size_t i = 0; i < sizeof(T); i++) {
        printf("%02X ", bytes[i]);
    }
    cout << endl;
}

int main() {
    printEndianness();
    
    uint32_t value = 0x12345678;
    cout << "\nValue: 0x" << hex << value << dec << endl;
    printBytes(value);
    
    if (isLittleEndian()) {
        cout << "LSB (78) stored at lowest address" << endl;
    } else {
        cout << "MSB (12) stored at lowest address" << endl;
    }
    
    return 0;
}
```

---

### 8. Practical Applications

#### a) Color Representation (RGB)

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

struct Color {
    uint8_t r, g, b;
};

uint32_t packColor(uint8_t r, uint8_t g, uint8_t b) {
    return (r << 16) | (g << 8) | b;
}

Color unpackColor(uint32_t color) {
    Color c;
    c.r = (color >> 16) & 0xFF;
    c.g = (color >> 8) & 0xFF;
    c.b = color & 0xFF;
    return c;
}

int main() {
    uint8_t r = 255, g = 128, b = 64;
    uint32_t packed = packColor(r, g, b);
    
    cout << "RGB: (" << (int)r << ", " << (int)g << ", " << (int)b << ")" << endl;
    cout << "Packed: 0x" << hex << packed << dec << endl;
    
    Color unpacked = unpackColor(packed);
    cout << "Unpacked: (" << (int)unpacked.r << ", " << (int)unpacked.g << ", " << (int)unpacked.b << ")" << endl;
    
    return 0;
}
```

#### b) IP Address Representation

```cpp
#include <iostream>
#include <cstdint>
using namespace std;

uint32_t ipToInt(int a, int b, int c, int d) {
    return (a << 24) | (b << 16) | (c << 8) | d;
}

void intToIp(uint32_t ip, int& a, int& b, int& c, int& d) {
    a = (ip >> 24) & 0xFF;
    b = (ip >> 16) & 0xFF;
    c = (ip >> 8) & 0xFF;
    d = ip & 0xFF;
}

int main() {
    uint32_t ip = ipToInt(192, 168, 1, 1);
    cout << "IP as integer: " << ip << endl;
    cout << "IP as hex: 0x" << hex << ip << dec << endl;
    
    int a, b, c, d;
    intToIp(ip, a, b, c, d);
    cout << "IP address: " << a << "." << b << "." << c << "." << d << endl;
    
    return 0;
}
```

---

### Key Takeaways

1. **Binary** is base-2, using digits 0 and 1
2. **Octal** is base-8, using digits 0-7 (prefix `0`)
3. **Hexadecimal** is base-16, using digits 0-9 and A-F (prefix `0x`)
4. **Two's complement** is used for signed integers
5. **Endianness** determines byte order in memory
6. **Bit manipulation** allows packing/unpacking data efficiently
7. **Prefixes** in C++14: `0b` for binary, `0` for octal, `0x` for hex

---

### Practice Questions

1. Convert binary `1101101` to decimal
2. Convert decimal `97` to binary and hex
3. Convert hex `1F4` to binary and decimal
4. Write a function to count the number of 1 bits in a number
5. Write a function to reverse the bits of a 32-bit integer
6. Determine if your system is little-endian or big-endian
7. Pack 4 small integers (0-255) into a 32-bit integer
8. Unpack a 32-bit integer into 4 separate bytes

---

### Next Steps

- Go to [05_Bit_Manipulation_Problems.md](05_Bit_Manipulation_Problems.md) for Bit Manipulation Problems.