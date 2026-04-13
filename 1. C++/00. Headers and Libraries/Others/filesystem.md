# filesystem - File System Utilities (`<filesystem>`)

The `<filesystem>` header (C++17) provides a portable, object-oriented API for path manipulation, file/directory queries, iteration, and file operations — replacing fragile platform-specific code with a single clean interface.

## 📖 Overview

`std::filesystem` (namespace alias: `fs`) wraps OS file system calls in a type-safe, exception-aware C++ API. Key design choices:
- **`path`** is the central type — it knows about separators, extensions, stems, and parent directories
- **Free functions** (not methods) perform operations: `exists()`, `copy()`, `remove()`, `rename()`
- **Exceptions** or **error codes** — every function has both throwing and non-throwing overloads
- **Iterators** — `directory_iterator` and `recursive_directory_iterator` for traversal

> **Compiler note**: compile with `-std=c++17` and link with `-lstdc++fs` (older GCC) or just `-std=c++17` on MSVC/Clang.

## 🎯 Key Components

### `filesystem::path`
```
path components example:
  /home/user/docs/report.final.txt
  ├── root_name():   ""  (or "C:" on Windows)
  ├── root_directory(): "/"
  ├── parent_path(): "/home/user/docs"
  ├── filename():    "report.final.txt"
  ├── stem():        "report.final"
  └── extension():   ".txt"
```

### File Status Query Functions
| Function | Returns |
|----------|---------|
| `exists(p)` | Does the path exist? |
| `is_regular_file(p)` | Is it a regular file? |
| `is_directory(p)` | Is it a directory? |
| `is_symlink(p)` | Is it a symbolic link? |
| `file_size(p)` | File size in bytes |
| `last_write_time(p)` | Last modification time |

### File/Directory Operations
| Function | Purpose |
|----------|---------|
| `create_directory(p)` | Create one directory |
| `create_directories(p)` | Create all missing parent dirs |
| `copy(from, to)` | Copy file or directory |
| `copy_file(from, to)` | Copy only files |
| `remove(p)` | Remove file or empty directory |
| `remove_all(p)` | Remove directory tree |
| `rename(from, to)` | Move / rename |
| `absolute(p)` | Get absolute path |
| `canonical(p)` | Resolve symlinks and `.`/`..` |
| `current_path()` | Get/set working directory |
| `temp_directory_path()` | Get system temp directory |

### Iterators
- `fs::directory_iterator` — one level only
- `fs::recursive_directory_iterator` — full subtree

## 🔧 Basic Operations

### Path Manipulation
```cpp
#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

int main() {
    fs::path p = "/home/user/docs/report.final.txt";

    std::cout << "Full path:  " << p              << "\n";
    std::cout << "Filename:   " << p.filename()   << "\n"; // report.final.txt
    std::cout << "Stem:       " << p.stem()       << "\n"; // report.final
    std::cout << "Extension:  " << p.extension()  << "\n"; // .txt
    std::cout << "Parent:     " << p.parent_path()<< "\n"; // /home/user/docs

    // Building paths portably
    fs::path base = "/home/user";
    fs::path full = base / "docs" / "notes.md"; // operator/ joins paths
    std::cout << "Built:      " << full          << "\n";

    // Modifying paths
    fs::path changed = p;
    changed.replace_extension(".pdf");
    std::cout << "PDF:        " << changed        << "\n";

    return 0;
}
```

### Querying File Properties
```cpp
#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

void inspect(const fs::path& p) {
    std::error_code ec;

    if (!fs::exists(p, ec)) {
        std::cout << p << " does not exist\n";
        return;
    }

    if (fs::is_regular_file(p))  std::cout << p << " is a file, size=" << fs::file_size(p) << " bytes\n";
    else if (fs::is_directory(p)) std::cout << p << " is a directory\n";
    else if (fs::is_symlink(p))   std::cout << p << " is a symlink\n";
}

int main() {
    inspect("/etc/hosts");      // probably a file
    inspect("/etc");            // a directory
    inspect("/nonexistent");    // does not exist
    inspect(fs::temp_directory_path()); // temp dir
    return 0;
}
```

### Creating and Removing
```cpp
#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

int main() {
    fs::path sandbox = fs::temp_directory_path() / "cpp_fs_demo";

    // Create directory tree
    fs::create_directories(sandbox / "a" / "b" / "c");
    std::cout << "Created: " << sandbox << "\n";

    // Create a file inside
    {
        std::ofstream f(sandbox / "a" / "hello.txt");
        f << "Hello, filesystem!\n";
    }

    std::cout << "File exists: " << std::boolalpha
              << fs::exists(sandbox / "a" / "hello.txt") << "\n";

    // Copy file
    fs::copy_file(sandbox / "a" / "hello.txt",
                  sandbox / "a" / "hello_copy.txt",
                  fs::copy_options::overwrite_existing);

    // Remove entire tree
    auto removed = fs::remove_all(sandbox);
    std::cout << "Removed " << removed << " entries\n";

    return 0;
}
```

### Directory Iteration
```cpp
#include <filesystem>
#include <iostream>
#include <string>
namespace fs = std::filesystem;

void listDirectory(const fs::path& dir, int depth = 0) {
    std::string indent(depth * 2, ' ');
    for (const auto& entry : fs::directory_iterator(dir)) {
        std::cout << indent;
        if (entry.is_directory()) {
            std::cout << "[DIR] " << entry.path().filename() << "\n";
            listDirectory(entry.path(), depth + 1);
        } else {
            std::cout << entry.path().filename()
                      << " (" << entry.file_size() << " bytes)\n";
        }
    }
}

int main() {
    fs::path target = fs::current_path();
    std::cout << "Contents of " << target << ":\n";
    listDirectory(target);
    return 0;
}
```

## 🎮 Practical Examples

### Example 1: File Search Utility
```cpp
#include <filesystem>
#include <iostream>
#include <string>
#include <vector>
namespace fs = std::filesystem;

std::vector<fs::path> findFiles(const fs::path& root,
                                const std::string& extension) {
    std::vector<fs::path> results;
    std::error_code ec;

    for (const auto& entry : fs::recursive_directory_iterator(root,
             fs::directory_options::skip_permission_denied, ec)) {
        if (entry.is_regular_file() && entry.path().extension() == extension)
            results.push_back(entry.path());
    }
    return results;
}

int main() {
    auto cppFiles = findFiles(fs::current_path(), ".cpp");
    std::cout << "Found " << cppFiles.size() << " .cpp files:\n";
    for (const auto& f : cppFiles)
        std::cout << "  " << f.filename() << "\n";

    return 0;
}
```

### Example 2: Directory Size Calculator
```cpp
#include <filesystem>
#include <iostream>
#include <string>
#include <iomanip>
namespace fs = std::filesystem;

struct DirStats {
    uintmax_t totalBytes = 0;
    size_t    fileCount  = 0;
    size_t    dirCount   = 0;
};

DirStats calcStats(const fs::path& root) {
    DirStats stats;
    std::error_code ec;

    for (const auto& entry : fs::recursive_directory_iterator(root,
             fs::directory_options::skip_permission_denied, ec)) {
        if (entry.is_regular_file()) {
            stats.totalBytes += entry.file_size(ec);
            stats.fileCount++;
        } else if (entry.is_directory()) {
            stats.dirCount++;
        }
    }
    return stats;
}

std::string humanSize(uintmax_t bytes) {
    const char* units[] = {"B","KB","MB","GB","TB"};
    int i = 0;
    double size = static_cast<double>(bytes);
    while (size >= 1024.0 && i < 4) { size /= 1024.0; i++; }
    std::ostringstream oss;
    oss << std::fixed << std::setprecision(2) << size << " " << units[i];
    return oss.str();
}

int main() {
    fs::path target = fs::current_path();
    auto stats = calcStats(target);

    std::cout << "Directory: " << target        << "\n";
    std::cout << "Files:     " << stats.fileCount << "\n";
    std::cout << "Dirs:      " << stats.dirCount  << "\n";
    std::cout << "Total:     " << humanSize(stats.totalBytes) << "\n";
    return 0;
}
```

### Example 3: Backup / Copy Directory Tree
```cpp
#include <filesystem>
#include <iostream>
#include <string>
#include <chrono>
#include <iomanip>
namespace fs = std::filesystem;

fs::path makeBackupPath(const fs::path& source) {
    auto now    = std::chrono::system_clock::now();
    auto time_t = std::chrono::system_clock::to_time_t(now);
    std::ostringstream oss;
    oss << source.filename().string() << "_backup_"
        << std::put_time(std::localtime(&time_t), "%Y%m%d_%H%M%S");
    return source.parent_path() / oss.str();
}

void backupDirectory(const fs::path& src, const fs::path& dst) {
    std::error_code ec;
    fs::copy(src, dst,
             fs::copy_options::recursive |
             fs::copy_options::overwrite_existing, ec);
    if (ec) std::cerr << "Backup error: " << ec.message() << "\n";
    else    std::cout << "Backed up to: " << dst << "\n";
}

int main() {
    fs::path source = fs::current_path();
    fs::path backup = makeBackupPath(source);

    std::cout << "Source: " << source << "\n";
    std::cout << "Backup: " << backup << "\n";
    // backupDirectory(source, backup); // uncomment to run
    return 0;
}
```

### Example 4: File Watcher (Polling)
```cpp
#include <filesystem>
#include <iostream>
#include <map>
#include <chrono>
#include <thread>
namespace fs = std::filesystem;
using Clock = fs::file_time_type::clock;

class FileWatcher {
    fs::path watchDir_;
    std::map<fs::path, fs::file_time_type> timestamps_;

public:
    FileWatcher(const fs::path& dir) : watchDir_(dir) {
        // Snapshot current state
        for (const auto& e : fs::directory_iterator(dir))
            if (e.is_regular_file())
                timestamps_[e.path()] = e.last_write_time();
    }

    void check() {
        // Detect new and modified files
        for (const auto& e : fs::directory_iterator(watchDir_)) {
            if (!e.is_regular_file()) continue;
            auto t = e.last_write_time();
            auto it = timestamps_.find(e.path());
            if (it == timestamps_.end()) {
                std::cout << "[NEW]      " << e.path().filename() << "\n";
                timestamps_[e.path()] = t;
            } else if (it->second != t) {
                std::cout << "[MODIFIED] " << e.path().filename() << "\n";
                it->second = t;
            }
        }
        // Detect deleted files
        for (auto it = timestamps_.begin(); it != timestamps_.end(); ) {
            if (!fs::exists(it->first)) {
                std::cout << "[DELETED]  " << it->first.filename() << "\n";
                it = timestamps_.erase(it);
            } else { ++it; }
        }
    }
};

int main() {
    FileWatcher watcher(fs::current_path());
    std::cout << "Watching " << fs::current_path() << " for 5s...\n";

    for (int i = 0; i < 5; i++) {
        std::this_thread::sleep_for(std::chrono::seconds(1));
        watcher.check();
    }
    return 0;
}
```

## ⚡ Performance Tips

### Use Error Codes Instead of Exceptions in Loops
```cpp
std::error_code ec;
for (const auto& entry : fs::recursive_directory_iterator(root,
         fs::directory_options::skip_permission_denied, ec)) {
    // ec is set per entry; no exception thrown
    if (ec) { std::cerr << ec.message(); ec.clear(); continue; }
    // process entry
}
```

### Cache `file_size()` — Don't Call It Twice
```cpp
auto sz = entry.file_size(); // call once from the cached directory_entry
totalBytes += sz;            // use the cached value
```

### `directory_entry` Methods Are Cached
```cpp
// entry.is_regular_file(), entry.file_size() use the cached stat from the iterator
// fs::is_regular_file(path) makes a fresh stat call — slower in a loop
for (const auto& entry : fs::directory_iterator(dir)) {
    if (entry.is_regular_file()) { /* uses cache */ }
}
```

## 🐛 Common Pitfalls & Solutions

### 1. Paths Are Platform-Dependent Strings
```cpp
// Windows: "C:\\Users\\Alice"
// Linux:   "/home/alice"
// Always use operator/ to join paths — it uses the correct separator
fs::path p = base / "subdir" / "file.txt"; // portable
// NOT: base + "\\subdir\\file.txt"         // Windows-only, brittle
```

### 2. `directory_iterator` Throws on Permission Errors
```cpp
// Default: throws std::filesystem::filesystem_error on permission-denied
for (const auto& e : fs::recursive_directory_iterator(root)) { /* may throw! */ }

// Fix: use skip_permission_denied option
for (const auto& e : fs::recursive_directory_iterator(root,
         fs::directory_options::skip_permission_denied)) { /* safe */ }
```

### 3. `remove_all` Returns 0 When Path Doesn't Exist (C++17) but Throws (C++20)
```cpp
// Safe: check existence before remove_all
if (fs::exists(path)) fs::remove_all(path);

// Or use the error_code overload
std::error_code ec;
fs::remove_all(path, ec);
```

### 4. Iterating and Modifying the Same Directory
```cpp
// Avoid creating/deleting files while iterating the same directory
// Collect paths first, then modify
std::vector<fs::path> toDelete;
for (const auto& e : fs::directory_iterator(dir))
    if (e.path().extension() == ".tmp") toDelete.push_back(e.path());
for (const auto& p : toDelete) fs::remove(p);
```

## 🎯 Best Practices

1. **Always use `operator/`** to join path segments — never string concatenation
2. **Use `skip_permission_denied`** when recursively traversing directories you don't own
3. **Prefer `error_code` overloads** in performance-sensitive loops to avoid exception overhead
4. **Check `exists()` before file operations** when the path might not be there
5. **Use `fs::temp_directory_path()`** for temporary files — portable across platforms
6. **Use `canonical()` or `absolute()`** before storing or displaying paths to users

## 📚 Related Topics

- [`fstream.md`](../Fundamentals/28_fstream.md) — Reading and writing file contents
- [`string.md`](../Fundamentals/03_string.md) — `path::string()`, extension parsing
- [`exception.md`](../Fundamentals/31_exception.md) — `filesystem_error` exception handling

## 🚀 Next Steps

1. Write a utility that mirrors one directory tree to another, skipping unchanged files
2. Build a recursive file search CLI tool using `recursive_directory_iterator`
3. Explore `std::filesystem::space()` to query disk usage
4. Implement a log rotator that deletes files older than N days using `last_write_time()`
---

## Next Step

- Go to [lambda_expressions.md](lambda_expressions.md) to continue with lambda expressions.
