# 05_Template_Metaprogramming.md

## Template Metaprogramming in C++

### Overview

Template metaprogramming (TMP) is a technique that uses templates to perform computations at compile time rather than at runtime. It treats templates as a functional programming language embedded within C++. TMP enables compile-time decisions, type computations, code generation, and optimizations that would be impossible or inefficient at runtime.

---

### What is Template Metaprogramming?

Template metaprogramming is a paradigm where templates are used to generate code and perform computations during compilation. The results are computed before the program runs, leading to faster execution and smaller binaries.

**Key Characteristics:**

| Characteristic | Description |
|----------------|-------------|
| **Compile-Time Execution** | Computations happen during compilation |
| **Type-Level Programming** | Operations on types rather than values |
| **Functional Style** | Recursion and specialization (no mutable state) |
| **Zero Runtime Overhead** | Results are constants embedded in code |

**Example: Compile-Time Factorial**
```cpp
#include <iostream>
using namespace std;

// Primary template - recursive case
template <int N>
struct Factorial {
    static constexpr int value = N * Factorial<N - 1>::value;
};

// Base case - specialization for 0
template <>
struct Factorial<0> {
    static constexpr int value = 1;
};

int main() {
    // Computed at compile time
    cout << "Factorial of 5: " << Factorial<5>::value << endl;  // 120
    cout << "Factorial of 10: " << Factorial<10>::value << endl; // 3628800
    
    // Compile-time assertion
    static_assert(Factorial<5>::value == 120, "Factorial calculation error");
    
    return 0;
}
```

**Output:**
```
Factorial of 5: 120
Factorial of 10: 3628800
```

---

### Compile-Time Computations

Template metaprogramming can perform various mathematical computations at compile time.

```cpp
#include <iostream>
using namespace std;

// Compile-time Fibonacci
template <int N>
struct Fibonacci {
    static constexpr int value = Fibonacci<N - 1>::value + Fibonacci<N - 2>::value;
};

template <>
struct Fibonacci<0> {
    static constexpr int value = 0;
};

template <>
struct Fibonacci<1> {
    static constexpr int value = 1;
};

// Compile-time power
template <int Base, int Exp>
struct Power {
    static constexpr int value = Base * Power<Base, Exp - 1>::value;
};

template <int Base>
struct Power<Base, 0> {
    static constexpr int value = 1;
};

// Compile-time sum of squares
template <int N>
struct SumOfSquares {
    static constexpr int value = N * N + SumOfSquares<N - 1>::value;
};

template <>
struct SumOfSquares<0> {
    static constexpr int value = 0;
};

// Compile-time prime checking
template <int N, int D>
struct IsPrimeHelper {
    static constexpr bool value = (N % D != 0) && IsPrimeHelper<N, D - 1>::value;
};

template <int N>
struct IsPrimeHelper<N, 1> {
    static constexpr bool value = true;
};

template <int N>
struct IsPrime {
    static constexpr bool value = IsPrimeHelper<N, N / 2>::value;
};

template <>
struct IsPrime<0> { static constexpr bool value = false; };
template <>
struct IsPrime<1> { static constexpr bool value = false; };
template <>
struct IsPrime<2> { static constexpr bool value = true; };
template <>
struct IsPrime<3> { static constexpr bool value = true; };

int main() {
    cout << "Fibonacci(10): " << Fibonacci<10>::value << endl;  // 55
    cout << "Power(2, 10): " << Power<2, 10>::value << endl;    // 1024
    cout << "Sum of squares (1-5): " << SumOfSquares<5>::value << endl; // 55
    
    cout << "IsPrime(17): " << IsPrime<17>::value << endl;  // true
    cout << "IsPrime(100): " << IsPrime<100>::value << endl; // false
    
    return 0;
}
```

**Output:**
```
Fibonacci(10): 55
Power(2, 10): 1024
Sum of squares (1-5): 55
IsPrime(17): 1
IsPrime(100): 0
```

---

### Type Traits

Type traits are template metaprogramming utilities that query or modify type properties at compile time.

```cpp
#include <iostream>
#include <type_traits>
using namespace std;

// Custom type trait: check if type is integer
template <typename T>
struct IsInteger {
    static constexpr bool value = false;
};

template <>
struct IsInteger<int> { static constexpr bool value = true; };
template <>
struct IsInteger<short> { static constexpr bool value = true; };
template <>
struct IsInteger<long> { static constexpr bool value = true; };
template <>
struct IsInteger<long long> { static constexpr bool value = true; };
template <>
struct IsInteger<unsigned int> { static constexpr bool value = true; };
template <>
struct IsInteger<unsigned short> { static constexpr bool value = true; };
template <>
struct IsInteger<unsigned long> { static constexpr bool value = true; };
template <>
struct IsInteger<unsigned long long> { static constexpr bool value = true; };

// Custom type trait: remove const
template <typename T>
struct RemoveConst {
    using type = T;
};

template <typename T>
struct RemoveConst<const T> {
    using type = T;
};

// Custom type trait: add pointer
template <typename T>
struct AddPointer {
    using type = T*;
};

// Custom type trait: check if types are same
template <typename T, typename U>
struct IsSame {
    static constexpr bool value = false;
};

template <typename T>
struct IsSame<T, T> {
    static constexpr bool value = true;
};

// Using type traits with enable_if (SFINAE)
template <typename T>
typename enable_if<IsInteger<T>::value, T>::type
half(T value) {
    return value / 2;
}

template <typename T>
typename enable_if<!IsInteger<T>::value, T>::type
half(T value) {
    return value / 2.0;
}

int main() {
    cout << boolalpha;
    
    cout << "IsInteger<int>: " << IsInteger<int>::value << endl;
    cout << "IsInteger<double>: " << IsInteger<double>::value << endl;
    
    RemoveConst<const int>::type x = 42;  // x is int
    cout << "RemoveConst: " << typeid(x).name() << endl;
    
    AddPointer<int>::type ptr = nullptr;   // ptr is int*
    cout << "AddPointer: " << typeid(ptr).name() << endl;
    
    cout << "IsSame<int, int>: " << IsSame<int, int>::value << endl;
    cout << "IsSame<int, double>: " << IsSame<int, double>::value << endl;
    
    cout << "half(10): " << half(10) << endl;       // Integer version: 5
    cout << "half(3.14): " << half(3.14) << endl;   // Floating version: 1.57
    
    return 0;
}
```

---

### Conditional Type Selection

Template metaprogramming can select types based on compile-time conditions.

```cpp
#include <iostream>
#include <type_traits>
using namespace std;

// Compile-time conditional type
template <bool Condition, typename TrueType, typename FalseType>
struct Conditional {
    using type = TrueType;
};

template <typename TrueType, typename FalseType>
struct Conditional<false, TrueType, FalseType> {
    using type = FalseType;
};

// Helper for conditional type
template <bool Condition, typename T, typename F>
using ConditionalType = typename Conditional<Condition, T, F>::type;

// Practical example: choose appropriate integer type
template <int N>
struct ChooseIntegerType {
    using type = ConditionalType<(N <= 127), signed char,
                  ConditionalType<(N <= 32767), short,
                  ConditionalType<(N <= 2147483647), int,
                  long long>>>;
};

// Type selection based on size
template <size_t Size>
struct IntegerOfSize {
    using type = ConditionalType<(Size == 1), uint8_t,
                  ConditionalType<(Size == 2), uint16_t,
                  ConditionalType<(Size == 4), uint32_t,
                  uint64_t>>>;
};

int main() {
    // Conditional type selection
    ConditionalType<true, int, double>::type a = 42;    // a is int
    ConditionalType<false, int, double>::type b = 3.14; // b is double
    
    cout << "a type: " << typeid(a).name() << endl;
    cout << "b type: " << typeid(b).name() << endl;
    
    // Choose integer type based on value
    ChooseIntegerType<100>::type small = 100;      // signed char
    ChooseIntegerType<10000>::type medium = 10000; // short
    ChooseIntegerType<1000000>::type large = 1000000; // int
    
    cout << "size of small: " << sizeof(small) << " bytes" << endl;
    cout << "size of medium: " << sizeof(medium) << " bytes" << endl;
    cout << "size of large: " << sizeof(large) << " bytes" << endl;
    
    // Integer of specific size
    IntegerOfSize<1>::type i8 = 255;
    IntegerOfSize<2>::type i16 = 65535;
    IntegerOfSize<4>::type i32 = 4294967295U;
    
    cout << "i8 size: " << sizeof(i8) << ", value: " << (int)i8 << endl;
    cout << "i16 size: " << sizeof(i16) << ", value: " << i16 << endl;
    cout << "i32 size: " << sizeof(i32) << ", value: " << i32 << endl;
    
    return 0;
}
```

---

### Type Transformations

Template metaprogramming can transform types in various ways.

```cpp
#include <iostream>
#include <tuple>
#include <type_traits>
using namespace std;

// Remove all const and volatile qualifiers
template <typename T>
struct RemoveCV {
    using type = T;
};

template <typename T>
struct RemoveCV<const T> {
    using type = T;
};

template <typename T>
struct RemoveCV<volatile T> {
    using type = T;
};

template <typename T>
struct RemoveCV<const volatile T> {
    using type = T;
};

// Remove reference
template <typename T>
struct RemoveReference {
    using type = T;
};

template <typename T>
struct RemoveReference<T&> {
    using type = T;
};

template <typename T>
struct RemoveReference<T&&> {
    using type = T;
};

// Add lvalue reference
template <typename T>
struct AddLValueReference {
    using type = T&;
};

// Decay type (array to pointer, remove cv, etc.)
template <typename T>
struct Decay {
private:
    using U = typename RemoveReference<T>::type;
public:
    using type = typename Conditional<is_array_v<U>, 
                typename remove_extent<U>::type*,
                typename Conditional<is_function_v<U>, 
                typename add_pointer<U>::type,
                typename RemoveCV<U>::type>::type>::type;
};

// Get function return type
template <typename Func>
struct ReturnType;

template <typename Ret, typename... Args>
struct ReturnType<Ret(Args...)> {
    using type = Ret;
};

template <typename Ret, typename... Args>
struct ReturnType<Ret(Args...) const> {
    using type = Ret;
};

template <typename Ret, typename... Args>
struct ReturnType<Ret(*)(Args...)> {
    using type = Ret;
};

// Get function argument count
template <typename Func>
struct ArgumentCount;

template <typename Ret, typename... Args>
struct ArgumentCount<Ret(Args...)> {
    static constexpr size_t value = sizeof...(Args);
};

int foo(int x, double y, char z) { return 0; }

int main() {
    RemoveCV<const volatile int>::type a = 42;  // a is int
    cout << "RemoveCV: " << typeid(a).name() << endl;
    
    RemoveReference<int&>::type b = 100;  // b is int
    cout << "RemoveReference: " << typeid(b).name() << endl;
    
    AddLValueReference<int>::type c = b;  // c is int&
    cout << "AddLValueReference: " << typeid(c).name() << endl;
    
    // Return type deduction
    ReturnType<decltype(foo)>::type d = 42;  // d is int
    cout << "ReturnType: " << typeid(d).name() << endl;
    
    // Argument count
    cout << "ArgumentCount: " << ArgumentCount<decltype(foo)>::value << endl;
    
    return 0;
}
```

---

### SFINAE (Substitution Failure Is Not An Error)

SFINAE is a principle that allows templates to be conditionally enabled based on type properties.

```cpp
#include <iostream>
#include <type_traits>
using namespace std;

// Check if type has a member function 'size'
template <typename T>
struct HasSizeMethod {
private:
    // Helper to detect if T has a size() method
    template <typename U>
    static auto check(int) -> decltype(declval<U>().size(), true_type{});
    
    template <typename U>
    static auto check(...) -> false_type;
    
public:
    static constexpr bool value = decltype(check<T>(0))::value;
};

// Enable only if T has begin() and end() (is iterable)
template <typename T, typename = void>
struct IsIterable : false_type {};

template <typename T>
struct IsIterable<T, void_t<decltype(begin(declval<T>())),
                           decltype(end(declval<T>()))>> : true_type {};

// SFINAE in function overloading
template <typename T>
typename enable_if<is_integral<T>::value, T>::type
process(T value) {
    cout << "Integral version: ";
    return value * 2;
}

template <typename T>
typename enable_if<is_floating_point<T>::value, T>::type
process(T value) {
    cout << "Floating-point version: ";
    return value * 2.0;
}

template <typename T>
typename enable_if<is_class<T>::value, T>::type
process(T value) {
    cout << "Class version: ";
    return value;
}

// SFINAE with class templates
template <typename T, typename Enable = void>
class Printer {
public:
    static void print(const T& value) {
        cout << "Generic printer: " << value << endl;
    }
};

template <typename T>
class Printer<T, typename enable_if<is_pointer<T>::value>::type> {
public:
    static void print(const T& value) {
        cout << "Pointer printer: " << *value << endl;
    }
};

struct MyClass {
    int data = 42;
};

int main() {
    cout << process(10) << endl;      // Integral version: 20
    cout << process(3.14) << endl;    // Floating-point version: 6.28
    cout << process(MyClass{}) << endl; // Class version: (MyClass object)
    
    Printer<int>::print(100);
    int x = 50;
    Printer<int*>::print(&x);
    
    cout << "HasSizeMethod<vector<int>>: " << HasSizeMethod<vector<int>>::value << endl;
    cout << "HasSizeMethod<int>: " << HasSizeMethod<int>::value << endl;
    
    return 0;
}
```

---

### Compile-Time Recursion and Loops

Template metaprogramming uses recursion instead of loops.

```cpp
#include <iostream>
#include <array>
using namespace std;

// Compile-time sum of array elements
template <typename T, size_t N, size_t Index = 0>
struct ArraySum {
    static constexpr T value = ArraySum<T, N, Index + 1>::value + T();
};

template <typename T, size_t N>
struct ArraySum<T, N, N> {
    static constexpr T value = 0;
};

// Compile-time for loop (using integer sequence)
template <int... Is>
struct IndexSequence {};

template <int N, int... Is>
struct MakeIndexSequence : MakeIndexSequence<N - 1, N - 1, Is...> {};

template <int... Is>
struct MakeIndexSequence<0, Is...> {
    using type = IndexSequence<Is...>;
};

// Apply function to each element at compile time
template <typename T, T... Is>
constexpr array<T, sizeof...(Is)> makeArray(IndexSequence<Is...>) {
    return {Is...};
}

// Compile-time factorial using constexpr (modern alternative)
constexpr int factorial(int n) {
    return (n <= 1) ? 1 : n * factorial(n - 1);
}

// Compile-time loop using constexpr (C++14)
constexpr int sumUpTo(int n) {
    int sum = 0;
    for (int i = 1; i <= n; ++i) {
        sum += i;
    }
    return sum;
}

int main() {
    // Compile-time array creation
    constexpr auto arr = makeArray<int>(MakeIndexSequence<5>::type{});
    static_assert(arr[0] == 0, "");
    static_assert(arr[1] == 1, "");
    static_assert(arr[2] == 2, "");
    static_assert(arr[3] == 3, "");
    static_assert(arr[4] == 4, "");
    
    for (int x : arr) {
        cout << x << " ";
    }
    cout << endl;
    
    // constexpr functions (modern alternative to TMP)
    constexpr int fact10 = factorial(10);
    constexpr int sum100 = sumUpTo(100);
    
    cout << "factorial(10): " << fact10 << endl;
    cout << "sumUpTo(100): " << sum100 << endl;
    
    static_assert(fact10 == 3628800, "Factorial error");
    static_assert(sum100 == 5050, "Sum error");
    
    return 0;
}
```

---

### Real-World Applications

#### 1. Unit System (Compile-Time Units)

```cpp
#include <iostream>
using namespace std;

// Unit tags
struct Meter {};
struct Second {};
struct Kilogram {};

// Unit arithmetic
template <typename T1, typename T2>
struct MultiplyUnits;

template <>
struct MultiplyUnits<Meter, Second> {
    using type = void;  // Meter-Second (not a standard unit)
};

// Value with compile-time unit
template <typename T, typename Unit>
class Quantity {
private:
    T value_;
    
public:
    constexpr Quantity(T value) : value_(value) { }
    
    T value() const { return value_; }
    
    // Multiplication of quantities
    template <typename U>
    auto operator*(const Quantity<T, U>& other) const {
        using ResultUnit = typename MultiplyUnits<Unit, U>::type;
        return Quantity<T, ResultUnit>(value_ * other.value());
    }
};

// Distance in meters
using Distance = Quantity<double, Meter>;
// Time in seconds
using Time = Quantity<double, Second>;

int main() {
    Distance d(100.0);   // 100 meters
    Time t(9.58);        // 9.58 seconds
    
    // Speed = Distance / Time
    double speed = d.value() / t.value();
    cout << "Speed: " << speed << " m/s" << endl;
    
    return 0;
}
```

#### 2. Compile-Time Assertions

```cpp
#include <iostream>
#include <type_traits>
using namespace std;

// Custom static assert with message
template <bool Condition>
struct StaticAssert;

template <>
struct StaticAssert<true> {
    static constexpr void check() { }
};

#define STATIC_ASSERT(cond, msg) \
    static_assert(cond, msg)

// Compile-time size check
template <typename T, size_t ExpectedSize>
struct CheckSize {
    static_assert(sizeof(T) == ExpectedSize, "Unexpected size");
};

int main() {
    // Compile-time checks
    static_assert(sizeof(int) >= 2, "int too small");
    static_assert(sizeof(char) == 1, "char must be 1 byte");
    
    CheckSize<int, 4> checkInt;  // Succeeds on typical 32/64-bit systems
    
    // Check type properties at compile time
    static_assert(is_integral<int>::value, "int should be integral");
    static_assert(!is_pointer<int>::value, "int should not be pointer");
    
    cout << "All compile-time assertions passed!" << endl;
    
    return 0;
}
```

---

### Template Metaprogramming vs constexpr

| Aspect | Template Metaprogramming | constexpr (C++11/14/17) |
|--------|-------------------------|-------------------------|
| **Readability** | Poor (complex syntax) | Good (normal function syntax) |
| **Debugging** | Very difficult | Easier (constexpr functions) |
| **Type Operations** | Excellent | Limited |
| **Value Computations** | Possible | Preferred |
| **Recursion Depth** | Compiler dependent | Compiler dependent |
| **C++ Standard** | C++98 onward | C++11 onward |

**Modern Alternative - constexpr:**
```cpp
// TMP version (old style)
template <int N>
struct FactorialTMP {
    static constexpr int value = N * FactorialTMP<N - 1>::value;
};

// constexpr version (modern style)
constexpr int factorial(int n) {
    return (n <= 1) ? 1 : n * factorial(n - 1);
}

// Both compute at compile time when called with constant
int main() {
    constexpr int tmpResult = FactorialTMP<5>::value;
    constexpr int modernResult = factorial(5);
    static_assert(tmpResult == modernResult, "Results differ");
    return 0;
}
```

---

### Summary

| Concept | Key Point |
|---------|-----------|
| **Compile-Time Computation** | Calculations performed during compilation |
| **Type Traits** | Query and modify type properties |
| **SFINAE** | Enable/disable templates based on conditions |
| **Recursion** | Template metaprogramming uses recursive instantiation |
| **Specialization** | Base cases for recursion |
| **constexpr Alternative** | Modern C++ alternative for value computations |

---

### Key Takeaways

1. **Template metaprogramming** performs computations at compile time
2. **Type traits** are the foundation of compile-time type introspection
3. **SFINAE** enables conditional template selection
4. **Recursion and specialization** replace loops and conditions
5. **constexpr functions** are preferred for value computations (C++11/14)
6. **Template metaprogramming** is still needed for type-level operations
7. **Zero runtime overhead** is the main benefit

---

### Next Steps

- Go to [10_Exception_Handling_in_OOP](../10_Exception_Handling_in_OOP/README.md) for understanding it's foundation.