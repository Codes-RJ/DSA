# 30_iomanip - I/O Stream Manipulators

The `iomanip` header provides a set of *manipulators* — special objects you insert into a stream with `<<` or extract with `>>` — that control how subsequent data is formatted.

## 📖 Overview

Manipulators work by modifying persistent stream flags or by inserting/consuming special characters. They can be divided into two categories:

- **Sticky manipulators** — their effect persists for all future output until changed (e.g., `setprecision`, `setfill`, `left`, `fixed`)
- **Non-sticky manipulators** — their effect applies only to the very next value (e.g., `setw`)

`<iomanip>` supplements the basic manipulators already in `<ios>` (`boolalpha`, `hex`, `dec`, `oct`, `endl`).

## 🎯 Key Components

| Manipulator | Effect | Sticky? |
|---|---|---|
| `setw(n)` | Set field width to n | ❌ One time |
| `setprecision(n)` | Set decimal precision to n | ✅ |
| `setfill(c)` | Set fill character to c | ✅ |
| `fixed` | Fixed-point notation | ✅ |
| `scientific` | Scientific notation | ✅ |
| `defaultfloat` | Reset to default float format | ✅ |
| `left` | Left-align output | ✅ |
| `right` | Right-align output (default) | ✅ |
| `internal` | Sign left, value right | ✅ |
| `hex` | Hexadecimal integers | ✅ |
| `oct` | Octal integers | ✅ |
| `dec` | Decimal integers (default) | ✅ |
| `uppercase` | Uppercase hex digits / E in sci | ✅ |
| `boolalpha` | Print bools as `true`/`false` | ✅ |
| `showbase` | Prefix `0x`/`0` for hex/oct | ✅ |
| `showpoint` | Always show decimal point | ✅ |
| `showpos` | Show `+` for positive numbers | ✅ |
| `setbase(n)` | Set integer base (8, 10, or 16) | ✅ |

## 🔧 Basic Operations

### Width and Fill
```cpp
#include <iomanip>
#include <iostream>

int main() {
    // setw sets the minimum field width for the NEXT value only
    std::cout << std::setw(10) << "hello"    << "\n"; // "     hello"
    std::cout << std::setw(10) << 42         << "\n"; // "        42"

    // setfill changes the padding character (sticky)
    std::cout << std::setfill('*') << std::setw(10) << "hi" << "\n"; // "********hi"

    // alignment
    std::cout << std::left  << std::setw(10) << "left"  << "|\n"; // "left      |"
    std::cout << std::right << std::setw(10) << "right" << "|\n"; // "     right|"

    return 0;
}
```

### Floating-Point Precision
```cpp
#include <iomanip>
#include <iostream>

int main() {
    double pi = 3.14159265358979;

    std::cout << pi << "\n";                                        // 3.14159
    std::cout << std::fixed       << std::setprecision(2) << pi << "\n"; // 3.14
    std::cout << std::fixed       << std::setprecision(6) << pi << "\n"; // 3.141593
    std::cout << std::scientific  << std::setprecision(3) << pi << "\n"; // 3.142e+00
    std::cout << std::defaultfloat                         << pi << "\n"; // 3.14159

    return 0;
}
```

### Integer Bases
```cpp
#include <iomanip>
#include <iostream>

int main() {
    int value = 255;

    std::cout << std::dec      << value << "\n"; // 255
    std::cout << std::hex      << value << "\n"; // ff
    std::cout << std::uppercase << std::hex << value << "\n"; // FF
    std::cout << std::showbase  << std::hex << value << "\n"; // 0xFF
    std::cout << std::showbase  << std::oct << value << "\n"; // 0377

    return 0;
}
```

### Boolean and Sign Display
```cpp
#include <iomanip>
#include <iostream>

int main() {
    bool flag = true;

    std::cout << flag            << "\n"; // 1
    std::cout << std::boolalpha  << flag << "\n"; // true
    std::cout << std::noboolalpha;

    std::cout << std::showpos    << 42 << "\n"; // +42
    std::cout << std::showpos    << -5 << "\n"; // -5
    std::cout << std::noshowpos;

    return 0;
}
```

## 🎮 Practical Examples

### Example 1: Pretty-Printed Table
```cpp
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

struct Student {
    std::string name;
    int age;
    double gpa;
};

int main() {
    std::vector<Student> students = {
        {"Alice",   21, 3.95},
        {"Bob",     22, 3.40},
        {"Charlie", 20, 3.78},
    };

    // Header
    std::cout << std::left
              << std::setw(12) << "Name"
              << std::setw(6)  << "Age"
              << std::setw(8)  << "GPA"
              << "\n";
    std::cout << std::setfill('-') << std::setw(26) << "" << "\n";
    std::cout << std::setfill(' ');

    // Rows
    for (const auto& s : students) {
        std::cout << std::left
                  << std::setw(12) << s.name
                  << std::setw(6)  << s.age
                  << std::fixed << std::setprecision(2)
                  << std::setw(8)  << s.gpa
                  << "\n";
    }

    return 0;
}
```

### Example 2: Hex Memory Dump
```cpp
#include <iomanip>
#include <iostream>
#include <cstdint>

void hexDump(const unsigned char* buf, size_t len) {
    for (size_t i = 0; i < len; i++) {
        if (i % 16 == 0)
            std::cout << std::setw(4) << std::setfill('0') << std::hex << i << ": ";

        std::cout << std::setw(2) << std::setfill('0') << std::hex
                  << static_cast<int>(buf[i]) << " ";

        if ((i + 1) % 16 == 0) std::cout << "\n";
    }
    std::cout << "\n" << std::dec; // restore decimal
}

int main() {
    unsigned char data[] = "Hello, World!";
    hexDump(data, sizeof(data) - 1);
    return 0;
}
```

### Example 3: Invoice / Receipt Formatter
```cpp
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

struct LineItem {
    std::string desc;
    int qty;
    double price;
};

int main() {
    std::vector<LineItem> items = {
        {"Widget A", 3,  4.99},
        {"Gadget B", 1, 24.99},
        {"Doohickey", 5, 1.50},
    };

    std::cout << std::left << std::setw(16) << "Item"
              << std::right << std::setw(5) << "Qty"
              << std::setw(10) << "Price"
              << std::setw(12) << "Subtotal" << "\n";
    std::cout << std::setfill('-') << std::setw(43) << "" << "\n";
    std::cout << std::setfill(' ');

    double total = 0;
    for (const auto& item : items) {
        double sub = item.qty * item.price;
        total += sub;
        std::cout << std::left  << std::setw(16) << item.desc
                  << std::right << std::setw(5)  << item.qty
                  << std::fixed << std::setprecision(2)
                  << std::setw(10) << item.price
                  << std::setw(12) << sub << "\n";
    }

    std::cout << std::setfill('-') << std::setw(43) << "" << "\n";
    std::cout << std::setfill(' ') << std::right
              << std::setw(38) << "TOTAL: $"
              << std::fixed << std::setprecision(2) << total << "\n";

    return 0;
}
```

### Example 4: Scientific Data Reporter
```cpp
#include <iomanip>
#include <iostream>

int main() {
    double measurements[] = {0.000123, 45678.9, 3.14159e-10, 2.998e8};
    int n = 4;

    std::cout << "Measurements in different formats:\n";
    std::cout << std::setw(20) << "Default"
              << std::setw(20) << "Fixed(4)"
              << std::setw(20) << "Scientific(3)" << "\n";

    for (int i = 0; i < n; i++) {
        std::cout << std::defaultfloat
                  << std::setw(20) << measurements[i]
                  << std::fixed     << std::setprecision(4)
                  << std::setw(20) << measurements[i]
                  << std::scientific << std::setprecision(3)
                  << std::setw(20) << measurements[i] << "\n";
    }

    return 0;
}
```

## ⚡ Performance Tips

### Reset Sticky Flags After Use
```cpp
// After using fixed + setprecision, reset to avoid unwanted trailing zeros
std::cout << std::fixed << std::setprecision(2) << 3.14 << "\n"; // 3.14
std::cout << std::defaultfloat; // back to default
std::cout << 3.14 << "\n"; // 3.14 (no trailing zeros forced)
```

### Save and Restore Stream State
```cpp
#include <iomanip>
#include <iostream>

void printHex(int value) {
    // Save current state
    std::ios_base::fmtflags old_flags = std::cout.flags();
    char old_fill = std::cout.fill();

    std::cout << std::hex << std::showbase << std::uppercase << value << "\n";

    // Restore state
    std::cout.flags(old_flags);
    std::cout.fill(old_fill);
}

int main() {
    std::cout << 255 << "\n"; // 255
    printHex(255);             // 0XFF
    std::cout << 255 << "\n"; // 255 (restored)
    return 0;
}
```

## 🐛 Common Pitfalls & Solutions

### 1. `setw` is NOT Sticky
```cpp
// Problem: setw only affects ONE output item
std::cout << std::setw(10) << "a" << "b" << "\n";
// Output: "         ab" — 'b' is NOT padded

// Solution: repeat setw for every field
std::cout << std::setw(10) << "a" << std::setw(10) << "b" << "\n";
```

### 2. Forgetting `std::dec` After Hex Output
```cpp
std::cout << std::hex << 255 << "\n"; // ff
std::cout << 255 << "\n";             // ff (still hex! — bug)

// Fix
std::cout << std::dec;
std::cout << 255 << "\n";             // 255
```

### 3. `setprecision` Without `fixed` Changes Significant Digits, Not Decimal Places
```cpp
double pi = 3.14159;
std::cout << std::setprecision(3) << pi << "\n"; // 3.14  (3 sig figs)
std::cout << std::fixed << std::setprecision(3) << pi << "\n"; // 3.142 (3 decimal places)
```

## 🎯 Best Practices

1. **Save and restore stream flags** when writing utility functions that change formatting
2. **Apply `setw` immediately before** the value it should affect (it's non-sticky)
3. **Use `std::fixed` with `setprecision`** when you need a specific number of decimal places
4. **Restore `std::dec`** after hex/oct output to avoid hard-to-find bugs
5. **Combine with `ostringstream`** to build formatted strings without touching `cout`

## 📚 Related Headers

- [`iostream.md`](01_iostream.md) — Stream objects (`cout`, `cin`)
- [`sstream.md`](29_sstream.md) — String streams (manipulators work there too)
- [`fstream.md`](28_fstream.md) — File streams (manipulators work there too)

---

## Next Step

- Go to [31_exception.md](31_exception.md) to continue with exception.
