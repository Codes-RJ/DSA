# Fundamentals - C++ Headers and Libraries

This section covers the fundamental C++ headers and libraries that every C++ programmer should know. These are the building blocks for most C++ applications, especially in data structures and algorithms.

## 📚 List of Fundamental Headers

### Core Input/Output
- **[`iostream.md`](iostream.md)** - Standard input/output streams
- **[`fstream.md`](fstream.md)** - File input/output streams
- **[`sstream.md`](sstream.md)** - String streams
- **[`iomanip.md`](iomanip.md)** - Input/output manipulators

### Containers
- **[`vector.md`](vector.md)** - Dynamic array container
- **[`string.md`](string.md)** - String class and operations
- **[`array.md`](array.md)** - Fixed-size array container
- **[`deque.md`](deque.md)** - Double-ended queue
- **[`list.md`](list.md)** - Doubly linked list
- **[`forward_list.md`](forward_list.md)** - Singly linked list
- **[`stack.md`](stack.md)** - Stack container adapter
- **[`queue.md`](queue.md)** - Queue container adapter
- **[`priority_queue.md`](priority_queue.md)** - Priority queue
- **[`set.md`](set.md)** - Ordered unique elements
- **[`unordered_set.md`](unordered_set.md)** - Hash set
- **[`map.md`](map.md)** - Ordered key-value pairs
- **[`unordered_map.md`](unordered_map.md)** - Hash map

### Algorithms
- **[`algorithm.md`](algorithm.md)** - Standard algorithms (sort, search, etc.)
- **[`numeric.md`](numeric.md)** - Numeric operations
- **[`iterator.md`](iterator.md)** - Iterator utilities

### Utilities
- **[`utility.md`](utility.md)** - Utility functions (pair, swap, etc.)
- **[`tuple.md`](tuple.md)** - Tuple container
- **[`functional.md`](functional.md)** - Function objects
- **[`memory.md`](memory.md)** - Memory management
- **[`chrono.md`](chrono.md)** - Time utilities
- **[`random.md`](random.md)** - Random number generation

### C Standard Libraries
- **[`cmath.md`](cmath.md)** - Mathematical functions
- **[`cstdlib.md`](cstdlib.md)** - Standard library functions
- **[`cctype.md`](cctype.md)** - Character handling
- **[`cstring.md`](cstring.md)** - C-style string functions

### Advanced
- **[`exception.md`](exception.md)** - Exception handling
- **[`typeinfo.md`](typeinfo.md)** - Type information
- **[`type_traits.md`](type_traits.md)** - Type traits
- **[`limits.md`](limits.md)** - Numeric limits

## 🎯 Learning Priority

### ⭐ Must Know (Essential for DSA)
1. `iostream` - Basic input/output
2. `vector` - Most used container
3. `string` - String handling
4. `algorithm` - Sorting and searching
5. `cmath` - Mathematical operations

### ⭐⭐ Should Know (Very Useful)
1. `stack`, `queue` - Essential data structures
2. `map`, `set` - Associative containers
3. `utility` - Pair and other utilities
4. `memory` - Smart pointers

### ⭐⭐⭐ Good to Know (Advanced)
1. `chrono` - Time measurements
2. `random` - Random numbers
3. `functional` - Function objects
4. `iterator` - Advanced iterator usage

## 📋 Quick Reference Cheat Sheet

```cpp
// Essential includes for most DSA problems
#include <iostream>     // cin, cout
#include <vector>       // vector
#include <string>       // string
#include <algorithm>    // sort, find, etc.
#include <cmath>        // math functions
#include <stack>        // stack
#include <queue>        // queue
#include <map>          // map
#include <set>          // set

using namespace std;

int main() {
    // Common patterns
    vector<int> arr;
    string s;
    map<string, int> mp;
    set<int> st;
    stack<int> stk;
    queue<int> q;
    
    return 0;
}
```

## 🔗 Common Header Combinations

### For Array Problems:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
```

### For String Problems:
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
```

### For Graph Problems:
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
```

### For Mathematical Problems:
```cpp
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
```

## 💡 Usage Tips

1. **Include only what you need** - Avoid unnecessary includes
2. **Use `using namespace std;` carefully** - In competitive programming it's fine, but avoid in large projects
3. **Learn the common patterns** - Most DSA problems use similar header combinations
4. **Check examples first** - Each header file contains practical examples
5. **Practice progressively** - Start with basic headers, then move to advanced ones

## 🚀 Getting Started

1. **Start with `iostream.md`** - Learn basic input/output
2. **Move to `vector.md`** - Understand dynamic arrays
3. **Study `algorithm.md`** - Learn sorting and searching
4. **Explore containers** - Pick one container at a time
5. **Practice with problems** - Apply what you learn

## 📖 Recommended Learning Order

1. **Input/Output**: `iostream` → `sstream` → `fstream`
2. **Basic Containers**: `vector` → `string` → `array`
3. **Adapters**: `stack` → `queue` → `priority_queue`
4. **Associative**: `map` → `set` → `unordered_map` → `unordered_set`
5. **Algorithms**: `algorithm` → `numeric`
6. **Advanced**: `memory` → `chrono` → `functional`

Choose a header from the list above to start learning! 🎯

---

**Next Steps**: Start with [`iostream.md`](iostream.md) for basic input/output operations.
