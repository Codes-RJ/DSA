# 28_fstream - File Stream Library

The `fstream` header provides input and output file streams in C++, letting you read from and write to files using the same familiar stream syntax as `iostream`.

## 📖 Overview

`<fstream>` contains three main classes that model files as streams:

- **`ifstream`** — Input file stream (read-only)
- **`ofstream`** — Output file stream (write-only)
- **`fstream`** — Bidirectional file stream (read and write)

All three are derived from the same base as `cin`/`cout`, so operators `>>`, `<<`, and functions like `getline()` work identically.

## 🎯 Key Components

### Classes
- `std::ifstream` — opens a file for reading
- `std::ofstream` — opens a file for writing (creates if not present)
- `std::fstream` — opens a file for reading and writing

### Open Modes (bitmask flags)
| Flag | Meaning |
|------|---------|
| `ios::in` | Open for reading |
| `ios::out` | Open for writing |
| `ios::app` | Append to end |
| `ios::trunc` | Truncate existing content |
| `ios::binary` | Binary mode (no newline translation) |
| `ios::ate` | Seek to end on open |

### Key Methods
- `open(filename, mode)` — open a file
- `close()` — close the file
- `is_open()` — check if file opened successfully
- `eof()` — check end-of-file
- `fail()` — check for stream errors
- `seekg(pos)` / `seekp(pos)` — seek read/write position
- `tellg()` / `tellp()` — get current position

## 🔧 Basic Operations

### Writing to a File
```cpp
#include <fstream>
#include <iostream>

int main() {
    std::ofstream outFile("data.txt");

    if (!outFile.is_open()) {
        std::cerr << "Error: Could not open file for writing!\n";
        return 1;
    }

    outFile << "Hello, File!\n";
    outFile << "Line 2\n";
    outFile << 42 << " " << 3.14 << "\n";

    outFile.close(); // flush and close
    std::cout << "File written successfully.\n";

    return 0;
}
```

### Reading from a File
```cpp
#include <fstream>
#include <iostream>
#include <string>

int main() {
    std::ifstream inFile("data.txt");

    if (!inFile.is_open()) {
        std::cerr << "Error: Could not open file for reading!\n";
        return 1;
    }

    std::string line;
    while (std::getline(inFile, line)) {
        std::cout << line << "\n";
    }

    inFile.close();
    return 0;
}
```

### Appending to a File
```cpp
#include <fstream>
#include <iostream>

int main() {
    std::ofstream logFile("log.txt", std::ios::app);

    if (!logFile.is_open()) {
        std::cerr << "Cannot open log file!\n";
        return 1;
    }

    logFile << "[INFO] Application started\n";
    logFile << "[WARN] Low memory\n";

    logFile.close();
    std::cout << "Log updated.\n";
    return 0;
}
```

### Binary File I/O
```cpp
#include <fstream>
#include <iostream>

struct Point {
    double x, y;
};

int main() {
    // Write binary
    std::ofstream out("points.bin", std::ios::binary);
    Point p1 = {3.14, 2.71};
    out.write(reinterpret_cast<char*>(&p1), sizeof(p1));
    out.close();

    // Read binary
    std::ifstream in("points.bin", std::ios::binary);
    Point p2;
    in.read(reinterpret_cast<char*>(&p2), sizeof(p2));
    in.close();

    std::cout << "x=" << p2.x << " y=" << p2.y << "\n";
    return 0;
}
```

## 🎮 Practical Examples

### Example 1: Word Frequency Counter
```cpp
#include <fstream>
#include <iostream>
#include <map>
#include <string>

int main() {
    std::ifstream inFile("text.txt");
    if (!inFile.is_open()) {
        std::cerr << "Cannot open text.txt\n";
        return 1;
    }

    std::map<std::string, int> freq;
    std::string word;

    while (inFile >> word) {
        // Strip punctuation
        while (!word.empty() && !isalpha(word.back())) word.pop_back();
        if (!word.empty()) freq[word]++;
    }
    inFile.close();

    std::cout << "Word frequencies:\n";
    for (const auto& [w, count] : freq) {
        std::cout << "  " << w << ": " << count << "\n";
    }

    return 0;
}
```

### Example 2: CSV Reader
```cpp
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int main() {
    std::ifstream file("students.csv");
    if (!file.is_open()) {
        std::cerr << "Cannot open students.csv\n";
        return 1;
    }

    std::string line;
    std::getline(file, line); // skip header

    while (std::getline(file, line)) {
        std::istringstream ss(line);
        std::string name, scoreStr;

        std::getline(ss, name,      ',');
        std::getline(ss, scoreStr,  ',');

        int score = std::stoi(scoreStr);
        std::cout << name << " scored " << score << "\n";
    }

    file.close();
    return 0;
}
```

### Example 3: File Copy Utility
```cpp
#include <fstream>
#include <iostream>

int main() {
    std::ifstream src("source.txt", std::ios::binary);
    std::ofstream dst("destination.txt", std::ios::binary);

    if (!src.is_open() || !dst.is_open()) {
        std::cerr << "Error opening files!\n";
        return 1;
    }

    dst << src.rdbuf(); // single-line copy of entire stream buffer

    src.close();
    dst.close();
    std::cout << "File copied successfully.\n";
    return 0;
}
```

### Example 4: Random Access with `fstream`
```cpp
#include <fstream>
#include <iostream>
#include <string>

int main() {
    // Write some fixed-width records
    std::fstream file("records.txt", std::ios::in | std::ios::out | std::ios::trunc);
    file << "Alice  " << "Bob    " << "Charlie";
    file.flush();

    // Seek back to beginning and read second record (7 chars in)
    file.seekg(7);
    char name[8] = {};
    file.read(name, 7);
    std::cout << "Record 2: " << name << "\n"; // Bob

    file.close();
    return 0;
}
```

## ⚡ Performance Tips

### Use `rdbuf()` for Bulk Copies
```cpp
// Fastest way to copy: let the stream buffer do it
std::ifstream src("big.bin", std::ios::binary);
std::ofstream dst("copy.bin", std::ios::binary);
dst << src.rdbuf();
```

### Read Entire File Into a String
```cpp
#include <fstream>
#include <sstream>
#include <string>

std::string readAll(const std::string& path) {
    std::ifstream file(path);
    std::ostringstream ss;
    ss << file.rdbuf();
    return ss.str();
}
```

### Reduce Flush Overhead
```cpp
// endl flushes the buffer every call — expensive in a loop
for (int i = 0; i < 10000; i++)
    outFile << i << "\n";  // '\n' only, not endl

outFile.flush(); // flush once at the end
```

## 🐛 Common Pitfalls & Solutions

### 1. Not Checking `is_open()`
```cpp
// Problem: silently writes nothing if file can't be opened
std::ofstream f("readonly.txt");
f << "data"; // may silently fail

// Solution
if (!f.is_open()) {
    std::cerr << "Could not open file!\n";
    return 1;
}
```

### 2. Forgetting `ios::app` — Overwriting Accidentally
```cpp
// Problem: truncates existing log
std::ofstream log("log.txt"); // reopens & empties the file!

// Solution
std::ofstream log("log.txt", std::ios::app); // appends safely
```

### 3. Not Closing Files
```cpp
// Problem: close() may be skipped on early return
{
    std::ofstream f("data.txt");
    if (someError) return 1; // f.close() never called!
}
// Solution: RAII — file is closed automatically when f goes out of scope
```

### 4. Reading After `eof()`
```cpp
// Problem: using eof() as a loop condition reads the last element twice
while (!file.eof()) {
    file >> value; // reads garbage after last valid token
}

// Solution: use the read operation as the condition
while (file >> value) { /* safe */ }
```

## 🎯 Best Practices

1. **Always check `is_open()`** before reading or writing
2. **Rely on RAII** — let the destructor close the file for you
3. **Use `ios::app`** when writing logs to avoid accidentally overwriting
4. **Use binary mode** for non-text data (structs, images, audio)
5. **Prefer `'\n'` over `endl`** in tight write loops to avoid unnecessary flushing
6. **Check the stream state** with `file.fail()` after critical reads

## 📚 Related Headers

- [`iostream.md`](01_iostream.md) — Same stream model for stdin/stdout
- [`sstream.md`](29_sstream.md) — In-memory string streams
- [`iomanip.md`](30_iomanip.md) — Formatting manipulators for file output

---

## Next Step

- Go to [29_sstream.md](29_sstream.md) to continue with sstream.
