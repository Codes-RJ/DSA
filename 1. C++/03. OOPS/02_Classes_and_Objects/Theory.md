# Classes and Objects - Theoretical Foundations

## 📖 Overview

In Object-Oriented C++, a **class** is a blueprint defining a user-defined abstract data type (ADT), while an **object** is a concrete instance of that class instantiated in memory. 

At the theoretical level, an object is characterized by three fundamental aspects:
1. **Identity**: The unique physical address of the object in memory (`&object`). No two distinct active objects in C++ ever share the same address.
2. **State**: The aggregate values of all its non-static data members at any given moment in time.
3. **Behavior**: The set of member functions (methods) that can query or transition the object's state while preserving class invariants.

---

## 🏗️ Memory Layout & Hardware Mechanics

Understanding how classes and objects exist in physical memory demystifies performance, cache efficiency, and compiler optimizations.

```
                           Object Memory in RAM (Stack or Heap)
             ┌─────────────────────────────────────────────────────────────┐
             │ Byte Offset:  0      4       8              16          24  │
             ├──────────────┬───────┬───────┬──────────────┬───────────────┤
             │ Field:       │ id    │ pad   │ balance      │ vptr (if any) │
             │ Type:        │ int   │ [4B]  │ double       │ pointer       │
             │ Size:        │ 4 B   │ 4 B   │ 8 B          │ 8 B           │
             └──────────────┴───────┴───────┴──────────────┴───────────────┘
                                   ▲
                          Hardware Alignment
```

### 1. Structure Alignment and Data Padding
Processors access memory most efficiently when data types are aligned to memory addresses that are multiples of their size:
- A 4-byte `int` must reside at an address divisible by 4.
- An 8-byte `double` or 64-bit pointer must reside at an address divisible by 8.
- To maintain alignment, compilers insert invisible **padding bytes** between data members.
- **Rule of Thumb**: Order class data members in decreasing order of size (`double`, pointers, `int`, `short`, `char`) to minimize padding overhead.

### 2. The 1-Byte Empty Class Rule
What is the output of `sizeof(EmptyClass)`?
In C++, an empty class has `sizeof = 1` byte (not 0):
```cpp
class Empty {};
Empty a, b;
assert(&a != &b); // Guaranteed by language specification!
```
- Every distinct object must possess a unique address in memory. If `sizeof(Empty)` were 0, an array of `Empty[10]` would see all elements sharing the exact same pointer address, breaking pointer arithmetic (`ptr++`).

### 3. The Implicit `this` Pointer
Member functions do **not** duplicate machine code across object instances. A single copy of the function resides in the `.text` code segment.
When calling `account.deposit(500.0)`, the compiler implicitly passes the address of `account` as the first argument:
```cpp
// What you write:
account.deposit(500.0);

// What the compiler emits under the hood:
BankAccount_deposit(&account, 500.0);
```
Inside the member function, the keyword `this` is a `BankAccount* const` pointer holding the instance address.

---

## 🏛️ Class vs. Struct in C++

Unlike languages like C# or Java, in C++ a `struct` and a `class` are **functionally identical** under the hood with only two syntax defaults:

| Feature | `class` | `struct` |
| :--- | :--- | :--- |
| **Default Member Access** | `private` | `public` |
| **Default Base Inheritance** | `private` | `public` |
| **Memory Layout / Vtable** | Identical | Identical |
| **Idiomatic Usage** | Complex domain objects with invariants and private state | Passive Plain-Old-Data (POD) records |

---

## ⚙️ Member Storage & Segmentation

```
 ┌─────────────────────────────────────────────────────────────┐
 │ .text (Code Segment)   : Member functions, const methods    │
 ├─────────────────────────────────────────────────────────────┤
 │ .data / .bss Segment   : static data members (shared by all)│
 ├─────────────────────────────────────────────────────────────┤
 │ Heap                   : Objects allocated via new / malloc │
 ├─────────────────────────────────────────────────────────────┤
 │ Stack                  : Local objects, this pointer params │
 └─────────────────────────────────────────────────────────────┘
```

1. **Static Data Members**:
   - Declared inside the class with `static`, but defined outside in global file scope.
   - Allocated once in the program's static Data/BSS segment.
   - Do **not** increase the `sizeof` individual class instances.
2. **Const Member Functions**:
   - Marked with `const` after the parameter list: `int getValue() const;`
   - Transforms `this` from `T* const` into `const T* const`.
   - Prevents mutation of any non-static data member within the method body, enabling read-only access on `const` object references.
3. **The `mutable` Keyword**:
   - Allows a specific data member to be modified even inside a `const` member function.
   - Used exclusively for auxiliary state that does not affect external logical state (e.g., mutexes, cache memoization, access counters).

---

## 💻 Complete C++ Architecture & Layout Demonstration

```cpp
#include <iostream>
#include <string>
#include <cassert>
#include <iomanip>

class EmptyClass {};

class OptimizedAccount {
private:
    // Ordered to minimize alignment padding
    double balance;            // 8 bytes (offset 0)
    int accountNumber;         // 4 bytes (offset 8)
    char accountTier;          // 1 byte  (offset 12)
    // 3 bytes padding inserted here by compiler (total = 16 bytes)

    mutable int queryCount;    // mutable: modifiable in const methods
    static int totalAccounts;  // Stored in Data segment, not in instance!

public:
    OptimizedAccount(int accNum, double initialBal, char tier)
        : balance(initialBal), accountNumber(accNum), 
          accountTier(tier), queryCount(0) {
        totalAccounts++;
    }

    ~OptimizedAccount() {
        totalAccounts--;
    }

    // Const member function: guarantees no mutation of logical state
    double getBalance() const {
        queryCount++; // Allowed because queryCount is mutable
        return balance;
    }

    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    int getQueryCount() const { return queryCount; }
    int getAccountNumber() const { return accountNumber; }
    char getTier() const { return accountTier; }

    static int getTotalAccounts() {
        return totalAccounts;
    }

    void printMemoryAddresses() const {
        std::cout << "  Instance Address (this) : " << this << "\n";
        std::cout << "  Offset of balance       : " << (void*)&balance << "\n";
        std::cout << "  Offset of accountNumber : " << (void*)&accountNumber << "\n";
        std::cout << "  Offset of accountTier   : " << (void*)&accountTier << "\n";
        std::cout << "  Offset of queryCount    : " << (void*)&queryCount << "\n";
    }
};

// Definition of static member variable
int OptimizedAccount::totalAccounts = 0;

int main() {
    std::cout << "=== Classes and Objects Theoretical Foundations ===\n\n";

    std::cout << "--- 1. Object Size & Memory Alignment ---\n";
    std::cout << "  sizeof(EmptyClass)         : " << sizeof(EmptyClass) 
              << " byte (1-byte rule for unique identity)\n";
    std::cout << "  sizeof(OptimizedAccount)   : " << sizeof(OptimizedAccount) 
              << " bytes (includes data + padding)\n\n";

    std::cout << "--- 2. Object Identity & Addresses ---\n";
    EmptyClass e1, e2;
    std::cout << "  Address of e1: " << &e1 << "\n";
    std::cout << "  Address of e2: " << &e2 << "\n";
    assert(&e1 != &e2);
    std::cout << "  Identity uniqueness check: PASSED\n\n";

    std::cout << "--- 3. Instance Memory Layout & Alignment Offsets ---\n";
    OptimizedAccount acc1(1001, 2500.50, 'G');
    acc1.printMemoryAddresses();
    std::cout << "\n";

    std::cout << "--- 4. Const Correctness & Mutable Diagnostics ---\n";
    const OptimizedAccount constAcc(1002, 10000.0, 'P');
    std::cout << "  Initial query count: " << constAcc.getQueryCount() << "\n";
    std::cout << "  Reading balance of const object: $" << constAcc.getBalance() << "\n";
    std::cout << "  Reading balance again: $" << constAcc.getBalance() << "\n";
    std::cout << "  Updated query count (via mutable): " << constAcc.getQueryCount() << "\n\n";

    std::cout << "--- 5. Static Class-Wide Members ---\n";
    std::cout << "  Total Active Accounts: " << OptimizedAccount::getTotalAccounts() << "\n";
    {
        OptimizedAccount accTemp(1003, 50.0, 'S');
        std::cout << "  Inside scope, Total Accounts: " << OptimizedAccount::getTotalAccounts() << "\n";
    }
    std::cout << "  Outside scope, Total Accounts: " << OptimizedAccount::getTotalAccounts() << "\n";

    std::cout << "\n=== All Classes and Objects Foundations Verified Successfully! ===\n";
    return 0;
}
```

---

## 📊 Theoretical Summary Matrix

| Concept | Location in Memory | Affects `sizeof(Object)`? | Key Invariant |
| :--- | :--- | :--- | :--- |
| **Instance Data Members** | Object payload (Stack/Heap) | **Yes** (Member size + padding) | Defines object state |
| **Static Data Members** | `.data` / `.bss` segment | **No** | Shared by all instances |
| **Member Functions** | `.text` code segment | **No** | Shared executable instructions |
| **Virtual Functions** | `.text` + `vtable` | **Yes** (Adds 8-byte `vptr`) | Dynamic polymorphic dispatch |
| **Empty Class** | Stack/Heap | **Yes** (Guaranteed 1 byte) | Unique object addressability |
| **`mutable` Members** | Object payload | **Yes** (Counted in data size) | Modifiable in `const` methods |
