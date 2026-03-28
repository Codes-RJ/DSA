# Template Metaprogramming

## 📖 Overview

Template Metaprogramming (TMP) is a powerful C++ technique that uses templates to perform computations at compile time. It treats templates as a Turing-complete language, enabling you to execute algorithms and make decisions during compilation rather than at runtime, resulting in zero-overhead abstractions.

---

## 🎯 Key Concepts

- **Compile-Time Computation**: Executing code during compilation
- **Template Recursion**: Using recursion to implement loops and algorithms
- **Type Traits**: Analyzing and transforming types at compile time
- **SFINAE**: Substitution Failure Is Not An Error
- **Constexpr**: Compile-time constants and functions
- **Template Specialization**: Providing specific implementations

---

## 💻 Basic Syntax

### Compile-Time Constant
```cpp
template <int N>
struct Factorial {
    static constexpr int value = N * Factorial<N - 1>::value;
};

template <>
struct Factorial<0> {
    static constexpr int value = 1;
};
```

### Type Trait
```cpp
template <typename T>
struct is_pointer : false_type {};

template <typename T>
struct is_pointer<T*> : true_type {};
```

---

## 🔍 Detailed Explanation

### 1. **Basic Compile-Time Computation**

```cpp
#include <iostream>
using namespace std;

// Compile-time factorial
template <int N>
struct Factorial {
    static constexpr int value = N * Factorial<N - 1>::value;
    static void print() {
        cout << "Factorial<" << N << "> = " << value << endl;
    }
};

// Base case
template <>
struct Factorial<0> {
    static constexpr int value = 1;
    static void print() {
        cout << "Factorial<0> = 1" << endl;
    }
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

// Compile-time GCD
template <int A, int B>
struct GCD {
    static constexpr int value = GCD<B, A % B>::value;
};

template <int A>
struct GCD<A, 0> {
    static constexpr int value = A;
};

int main() {
    cout << "=== Basic Compile-Time Computation ===" << endl;
    
    // Factorial
    cout << "Factorial(5) = " << Factorial<5>::value << endl;
    cout << "Factorial(6) = " << Factorial<6>::value << endl;
    cout << "Factorial(10) = " << Factorial<10>::value << endl;
    
    // Power
    cout << "Power(2, 8) = " << Power<2, 8>::value << endl;
    cout << "Power(3, 4) = " << Power<3, 4>::value << endl;
    cout << "Power(5, 3) = " << Power<5, 3>::value << endl;
    
    // Fibonacci
    cout << "Fibonacci(10) = " << Fibonacci<10>::value << endl;
    cout << "Fibonacci(15) = " << Fibonacci<15>::value << endl;
    
    // GCD
    cout << "GCD(48, 18) = " << GCD<48, 18>::value << endl;
    cout << "GCD(1071, 462) = " << GCD<1071, 462>::value << endl;
    
    return 0;
}
```

### 2. **Type Traits and Type Manipulation**

```cpp
#include <iostream>
#include <type_traits>
#include <string>
#include <vector>
using namespace std;

// Basic type traits
template <typename T>
struct is_pointer : false_type {
    static constexpr bool value = false;
};

template <typename T>
struct is_pointer<T*> : true_type {
    static constexpr bool value = true;
};

// Remove pointer
template <typename T>
struct remove_pointer {
    using type = T;
};

template <typename T>
struct remove_pointer<T*> {
    using type = T;
};

// Add const
template <typename T>
struct add_const {
    using type = const T;
};

// Remove const
template <typename T>
struct remove_const {
    using type = T;
};

template <typename T>
struct remove_const<const T> {
    using type = T;
};

// Is same type
template <typename T, typename U>
struct is_same : false_type {
    static constexpr bool value = false;
};

template <typename T>
struct is_same<T, T> : true_type {
    static constexpr bool value = true;
};

// Conditional type selection
template <bool condition, typename TrueType, typename FalseType>
struct conditional_type {
    using type = TrueType;
};

template <typename TrueType, typename FalseType>
struct conditional_type<false, TrueType, FalseType> {
    using type = FalseType;
};

// Enable if (basic version)
template <bool condition, typename T = void>
struct enable_if {
    using type = T;
};

template <typename T>
struct enable_if<false, T> {};

// Type printer helper
template <typename T>
void printType() {
    if constexpr (is_pointer_v<T>) {
        cout << "Pointer type" << endl;
    } else if constexpr (is_const_v<T>) {
        cout << "Const type" << endl;
    } else if constexpr (is_reference_v<T>) {
        cout << "Reference type" << endl;
    } else {
        cout << "Regular type" << endl;
    }
}

int main() {
    cout << "=== Type Traits and Type Manipulation ===" << endl;
    
    // Pointer detection
    cout << "is_pointer<int>::value = " << is_pointer<int>::value << endl;
    cout << "is_pointer<int*>::value = " << is_pointer<int*>::value << endl;
    cout << "is_pointer<string*>::value = " << is_pointer<string*>::value << endl;
    
    cout << endl;
    
    // Remove pointer
    using IntPtr = int*;
    using IntType = remove_pointer<IntPtr>::type;
    cout << "remove_pointer<int*>::type is int: " << is_same<IntType, int>::value << endl;
    
    cout << endl;
    
    // Add const
    using ConstInt = add_const<int>::type;
    cout << "add_const<int>::type is const int: " << is_same<ConstInt, const int>::value << endl;
    
    cout << endl;
    
    // Remove const
    using NormalInt = remove_const<const int>::type;
    cout << "remove_const<const int>::type is int: " << is_same<NormalInt, int>::value << endl;
    
    cout << endl;
    
    // Conditional type
    using SelectedType = conditional_type<true, int, double>::type;
    cout << "conditional_type<true, int, double>::type is int: " << is_same<SelectedType, int>::value << endl;
    
    using SelectedType2 = conditional_type<false, int, double>::type;
    cout << "conditional_type<false, int, double>::type is double: " << is_same<SelectedType2, double>::value << endl;
    
    cout << endl;
    
    // Print type information
    cout << "Type analysis:" << endl;
    printType<int>();
    printType<const int>();
    printType<int*>();
    printType<const int*>();
    printType<int&>();
    
    return 0;
}
```

### 3. **SFINAE and Template Constraints**

```cpp
#include <iostream>
#include <type_traits>
#include <vector>
#include <string>
using namespace std;

// Basic SFINAE example
template <typename T>
typename enable_if<is_integral<T>::value, T>::type
doubleValue(T value) {
    cout << "Integral version: ";
    return value * 2;
}

template <typename T>
typename enable_if<is_floating_point<T>::value, T>::type
doubleValue(T value) {
    cout << "Floating point version: ";
    return value * 2.0;
}

// Advanced SFINAE with decltype
template <typename T>
auto hasBeginEnd(int) -> decltype(
    declval<T>().begin(),
    declval<T>().end(),
    true_type{}
) {
    return true_type{};
}

template <typename T>
false_type hasBeginEnd(...) {
    return false_type{};
}

template <typename T>
struct is_container {
    static constexpr bool value = decltype(hasBeginEnd<T>(0))::value;
};

// Container-specific operations
template <typename T>
typename enable_if<is_container<T>::value, size_t>::type
getSize(const T& container) {
    cout << "Container version: ";
    return container.size();
}

template <typename T>
typename enable_if<!is_container<T>::value, size_t>::type
getSize(const T& value) {
    cout << "Non-container version: ";
    return sizeof(T);
}

// Check if type has specific method
template <typename T>
class HasSizeMethod {
private:
    template <typename U>
    static auto test(int) -> decltype(declval<U>().size(), true_type{});
    
    template <typename>
    static false_type test(...);
    
public:
    static constexpr bool value = decltype(test<T>(0))::value;
};

// Method existence-based dispatch
template <typename T>
typename enable_if<HasSizeMethod<T>::value, size_t>::type
getSizeMethod(const T& obj) {
    cout << "Using size() method: ";
    return obj.size();
}

template <typename T>
typename enable_if<!HasSizeMethod<T>::value, size_t>::type
getSizeMethod(const T& obj) {
    cout << "Using sizeof: ";
    return sizeof(T);
}

// Compile-time if with constexpr
template <typename T>
auto processValue(T value) {
    if constexpr (is_integral_v<T>) {
        cout << "Processing integral: ";
        return value * value;
    } else if constexpr (is_floating_point_v<T>) {
        cout << "Processing floating point: ";
        return value * 2.0;
    } else if constexpr (is_same_v<T, string>) {
        cout << "Processing string: ";
        return value.length();
    } else {
        cout << "Processing other type: ";
        return sizeof(T);
    }
}

int main() {
    cout << "=== SFINAE and Template Constraints ===" << endl;
    
    // Basic SFINAE
    cout << doubleValue(5) << endl;      // Integral version
    cout << doubleValue(3.14) << endl;   // Floating point version
    
    cout << endl;
    
    // Container detection
    cout << "is_container<vector<int>>::value = " << is_container<vector<int>>::value << endl;
    cout << "is_container<int>::value = " << is_container<int>::value << endl;
    cout << "is_container<string>::value = " << is_container<string>::value << endl;
    
    cout << endl;
    
    // Container-specific operations
    vector<int> vec = {1, 2, 3, 4, 5};
    cout << "Vector size: " << getSize(vec) << endl;
    cout << "Int size: " << getSize(42) << endl;
    cout << "String size: " << getSize(string("Hello")) << endl;
    
    cout << endl;
    
    // Method existence check
    cout << "HasSizeMethod<vector<int>>::value = " << HasSizeMethod<vector<int>>::value << endl;
    cout << "HasSizeMethod<int>::value = " << HasSizeMethod<int>::value << endl;
    
    cout << "Vector size via method: " << getSizeMethod(vec) << endl;
    cout << "Int size via method: " << getSizeMethod(42) << endl;
    
    cout << endl;
    
    // Compile-time if
    cout << processValue(5) << endl;
    cout << processValue(3.14) << endl;
    cout << processValue(string("Hello World")) << endl;
    cout << processValue('A') << endl;
    
    return 0;
}
```

### 4. **Advanced Template Metaprogramming**

```cpp
#include <iostream>
#include <type_traits>
#include <tuple>
#include <string>
using namespace std;

// Compile-time list operations
template <int...>
struct IntList {};

// Append to list
template <typename List, int New>
struct Append;

template <int... Items, int New>
struct Append<IntList<Items...>, New> {
    using type = IntList<Items..., New>;
};

// List length
template <typename List>
struct Length;

template <int... Items>
struct Length<IntList<Items...>> {
    static constexpr int value = sizeof...(Items);
};

// Sum of list elements
template <typename List>
struct Sum;

template <>
struct Sum<IntList<>> {
    static constexpr int value = 0;
};

template <int First, int... Rest>
struct Sum<IntList<First, Rest...>> {
    static constexpr int value = First + Sum<IntList<Rest...>>::value;
};

// Filter list (keep only even numbers)
template <typename List>
struct FilterEven;

template <>
struct FilterEven<IntList<>> {
    using type = IntList<>;
};

template <int First, int... Rest>
struct FilterEven<IntList<First, Rest...>> {
    using type = typename conditional_t<
        First % 2 == 0,
        typename Append<typename FilterEven<IntList<Rest...>>::type, First>::type,
        typename FilterEven<IntList<Rest...>>::type
    >;
};

// Type list operations
template <typename...>
struct TypeList {};

template <typename List, typename NewType>
struct TypeAppend;

template <typename... Types, typename NewType>
struct TypeAppend<TypeList<Types...>, NewType> {
    using type = TypeList<Types..., NewType>;
};

// Find first occurrence of type
template <typename List, typename Target>
struct FindFirst;

template <typename Target>
struct FindFirst<TypeList<>, Target> {
    static constexpr int value = -1;
};

template <typename Target, typename... Rest>
struct FindFirst<TypeList<Target, Rest...>, Target> {
    static constexpr int value = 0;
};

template <typename First, typename... Rest, typename Target>
struct FindFirst<TypeList<First, Rest...>, Target> {
    static constexpr int value = FindFirst<TypeList<Rest...>, Target>::value == -1 ? 
        -1 : 1 + FindFirst<TypeList<Rest...>, Target>::value;
};

// Compile-time string processing
template <size_t N>
struct ConstexprString {
    constexpr ConstexprString(const char (&str)[N]) {
        for (size_t i = 0; i < N; ++i) {
            data[i] = str[i];
        }
    }
    
    constexpr char operator[](size_t i) const {
        return data[i];
    }
    
    constexpr size_t size() const {
        return N - 1; // Exclude null terminator
    }
    
    char data[N];
};

// Compile-time string length
template <size_t N>
constexpr size_t stringLength(const char (&)[N]) {
    return N - 1;
}

// Compile-time string comparison
template <size_t N1, size_t N2>
constexpr bool stringsEqual(const char (&str1)[N1], const char (&str2)[N2]) {
    if (N1 != N2) return false;
    for (size_t i = 0; i < N1; ++i) {
        if (str1[i] != str2[i]) return false;
    }
    return true;
}

// Matrix operations at compile time
template <int Rows, int Cols>
struct Matrix {
    int data[Rows][Cols];
    
    constexpr Matrix() : data{} {
        for (int i = 0; i < Rows; ++i) {
            for (int j = 0; j < Cols; ++j) {
                data[i][j] = 0;
            }
        }
    }
    
    constexpr int& operator()(int i, int j) {
        return data[i][j];
    }
    
    constexpr const int& operator()(int i, int j) const {
        return data[i][j];
    }
    
    constexpr Matrix<Rows, Cols> operator+(const Matrix& other) const {
        Matrix<Rows, Cols> result;
        for (int i = 0; i < Rows; ++i) {
            for (int j = 0; j < Cols; ++j) {
                result(i, j) = data[i][j] + other(i, j);
            }
        }
        return result;
    }
};

int main() {
    cout << "=== Advanced Template Metaprogramming ===" << endl;
    
    // IntList operations
    using MyList = IntList<1, 2, 3, 4, 5>;
    cout << "List length: " << Length<MyList>::value << endl;
    cout << "List sum: " << Sum<MyList>::value << endl;
    
    using EvenList = typename FilterEven<MyList>::type;
    cout << "Even numbers sum: " << Sum<EvenList>::value << endl;
    
    cout << endl;
    
    // TypeList operations
    using MyTypes = TypeList<int, double, string, char>;
    cout << "Find int: " << FindFirst<MyTypes, int>::value << endl;
    cout << "Find double: " << FindFirst<MyTypes, double>::value << endl;
    cout << "Find string: " << FindFirst<MyTypes, string>::value << endl;
    cout << "Find bool: " << FindFirst<MyTypes, bool>::value << endl;
    
    cout << endl;
    
    // Compile-time string processing
    constexpr ConstexprString<6> hello("Hello");
    cout << "String size: " << hello.size() << endl;
    cout << "String[1]: " << hello[1] << endl;
    
    constexpr bool isEqual = stringsEqual("Hello", "Hello");
    constexpr bool isNotEqual = stringsEqual("Hello", "World");
    cout << "Hello == Hello: " << isEqual << endl;
    cout << "Hello == World: " << isNotEqual << endl;
    
    cout << endl;
    
    // Compile-time matrix operations
    constexpr Matrix<2, 2> mat1;
    constexpr Matrix<2, 2> mat2;
    
    // Note: In a real scenario, you'd initialize matrices with values
    // This is just to demonstrate the concept
    cout << "Matrix operations available at compile time" << endl;
    cout << "Matrix dimensions: 2x2" << endl;
    
    return 0;
}
```

### 5. **Practical Template Metaprogramming Applications**

```cpp
#include <iostream>
#include <type_traits>
#include <string>
#include <vector>
#include <array>
using namespace std;

// Compile-time configuration system
template <bool Debug, bool Logging, bool Validation>
struct Config {
    static constexpr bool debug = Debug;
    static constexpr bool logging = Logging;
    static constexpr bool validation = Validation;
    
    template <typename T>
    static void process(T value) {
        if constexpr (debug) {
            cout << "[DEBUG] Processing: " << value << endl;
        }
        
        if constexpr (logging) {
            cout << "[LOG] Processed value: " << value << endl;
        }
        
        if constexpr (validation) {
            if constexpr (is_arithmetic_v<T>) {
                cout << "[VALIDATION] Value is numeric: " << value << endl;
            } else {
                cout << "[VALIDATION] Value is non-numeric" << endl;
            }
        }
    }
};

// Compile-time policy system
template <typename T>
class SafeContainer {
private:
    T data;
    
public:
    SafeContainer(T value) : data(value) {}
    
    template <bool EnableChecks = true>
    T get() {
        if constexpr (EnableChecks) {
            if constexpr (is_pointer_v<T>) {
                if (!data) {
                    throw runtime_error("Null pointer access");
                }
            }
        }
        return data;
    }
    
    template <bool EnableChecks = true>
    void set(T value) {
        if constexpr (EnableChecks) {
            if constexpr (is_pointer_v<T>) {
                if (!value) {
                    throw runtime_error("Cannot set null pointer");
                }
            }
        }
        data = value;
    }
};

// Compile-time factory with type registration
template <typename T>
struct FactoryRegistry {
    static constexpr bool registered = true;
};

template <typename T>
constexpr bool isRegistered() {
    return FactoryRegistry<T>::registered;
}

template <typename T>
enable_if_t<isRegistered<T>(), unique_ptr<T>>
createObject() {
    return make_unique<T>();
}

// Registered types
struct MyClass {
    void sayHello() { cout << "Hello from MyClass!" << endl; }
};

template <>
struct FactoryRegistry<MyClass> {
    static constexpr bool registered = true;
};

// Compile-time validation framework
template <typename T>
struct Validator {
    static constexpr bool validate(const T&) {
        if constexpr (is_arithmetic_v<T>) {
            return true; // All arithmetic values are valid
        } else if constexpr (is_same_v<T, string>) {
            return true; // All strings are valid
        } else {
            return false; // Unknown types are invalid
        }
    }
};

template <>
struct Validator<int> {
    static constexpr bool validate(const int& value) {
        return value >= 0 && value <= 100;
    }
};

template <typename T>
constexpr bool isValid(const T& value) {
    return Validator<T>::validate(value);
}

// Compile-time dimension system
template <int Length, int Width, int Height>
struct Dimensions {
    static constexpr int length = Length;
    static constexpr int width = Width;
    static constexpr int height = Height;
    
    static constexpr int volume() {
        return Length * Width * Height;
    }
    
    template <int NewLength, int NewWidth, int NewHeight>
    using Resized = Dimensions<NewLength, NewWidth, NewHeight>;
};

// Compile-time unit conversion
template <int From, int To>
struct UnitConverter {
    static constexpr double convert(double value) {
        return value * static_cast<double>(To) / static_cast<double>(From);
    }
};

// Specializations for common conversions
template <>
struct UnitConverter<1, 1000> { // meters to millimeters
    static constexpr double convert(double value) {
        return value * 1000.0;
    }
};

template <>
struct UnitConverter<1000, 1> { // millimeters to meters
    static constexpr double convert(double value) {
        return value / 1000.0;
    }
};

int main() {
    cout << "=== Practical Template Metaprogramming Applications ===" << endl;
    
    // Configuration system
    cout << "Configuration System:" << endl;
    using DebugConfig = Config<true, true, false>;
    using ReleaseConfig = Config<false, false, true>;
    
    DebugConfig::process(42);
    DebugConfig::process("Hello");
    
    ReleaseConfig::process(3.14);
    ReleaseConfig::process("World");
    
    cout << endl;
    
    // Safe container
    cout << "Safe Container:" << endl;
    SafeContainer<int> intContainer(42);
    SafeContainer<int*> ptrContainer(new int(100));
    
    cout << "Int value: " << intContainer.get() << endl;
    cout << "Ptr value: " << *ptrContainer.get() << endl;
    
    delete ptrContainer.get();
    
    cout << endl;
    
    // Factory registration
    cout << "Factory Registration:" << endl;
    cout << "MyClass registered: " << isRegistered<MyClass>() << endl;
    cout << "int registered: " << isRegistered<int>() << endl;
    
    if (auto obj = createObject<MyClass>()) {
        obj->sayHello();
    }
    
    cout << endl;
    
    // Validation framework
    cout << "Validation Framework:" << endl;
    cout << "isValid(50): " << isValid(50) << endl;
    cout << "isValid(150): " << isValid(150) << endl;
    cout << "isValid(3.14): " << isValid(3.14) << endl;
    cout << "isValid(\"Hello\"): " << isValid(string("Hello")) << endl;
    
    cout << endl;
    
    // Dimension system
    cout << "Dimension System:" << endl;
    using BoxSize = Dimensions<10, 5, 3>;
    cout << "Box volume: " << BoxSize::volume() << endl;
    
    using ResizedBox = BoxSize::template Resized<20, 10, 6>;
    cout << "Resized box volume: " << ResizedBox::volume() << endl;
    
    cout << endl;
    
    // Unit conversion
    cout << "Unit Conversion:" << endl;
    cout << "1 meter to millimeters: " << UnitConverter<1, 1000>::convert(1.0) << endl;
    cout << "1000 millimeters to meters: " << UnitConverter<1000, 1>::convert(1000.0) << endl;
    
    return 0;
}
```

---

## 🎮 Complete Example: Compile-Time Game Engine

```cpp
#include <iostream>
#include <type_traits>
#include <string>
#include <array>
using namespace std;

// Component system using template metaprogramming
struct Component {
    virtual ~Component() = default;
};

struct Position : Component {
    float x, y;
    Position(float x = 0, float y = 0) : x(x), y(y) {}
};

struct Velocity : Component {
    float vx, vy;
    Velocity(float vx = 0, float vy = 0) : vx(vx), vy(vy) {}
};

struct Health : Component {
    int value;
    Health(int value = 100) : value(value) {}
};

// Component ID system
template <typename T>
struct ComponentID {
    static constexpr size_t value = 0;
};

template <>
struct ComponentID<Position> {
    static constexpr size_t value = 0;
};

template <>
struct ComponentID<Velocity> {
    static constexpr size_t value = 1;
};

template <>
struct ComponentID<Health> {
    static constexpr size_t value = 2;
};

// Compile-time component mask
template <typename... Components>
struct ComponentMask {
    static constexpr size_t mask = 0;
};

template <typename First, typename... Rest>
struct ComponentMask<First, Rest...> {
    static constexpr size_t mask = (1ULL << ComponentID<First>::value) | 
                                  ComponentMask<Rest...>::mask;
};

// Entity system
class Entity {
private:
    size_t componentMask = 0;
    array<Component*, 3> components{}; // Max 3 components for simplicity
    
public:
    template <typename T>
    void addComponent(T* component) {
        constexpr size_t id = ComponentID<T>::value;
        components[id] = component;
        componentMask |= (1ULL << id);
    }
    
    template <typename T>
    T* getComponent() {
        constexpr size_t id = ComponentID<T>::value;
        return static_cast<T*>(components[id]);
    }
    
    template <typename T>
    bool hasComponent() const {
        constexpr size_t id = ComponentID<T>::value;
        return (componentMask & (1ULL << id)) != 0;
    }
    
    template <typename... Components>
    bool hasComponents() const {
        constexpr size_t requiredMask = ComponentMask<Components...>::mask;
        return (componentMask & requiredMask) == requiredMask;
    }
};

// System base class
template <typename... RequiredComponents>
class System {
public:
    virtual void update(float deltaTime) = 0;
    
    bool canProcessEntity(const Entity& entity) const {
        return entity.hasComponents<RequiredComponents...>();
    }
};

// Movement system
class MovementSystem : public System<Position, Velocity> {
public:
    void update(float deltaTime) override {
        cout << "MovementSystem updating entities with Position and Velocity" << endl;
    }
};

// Health system
class HealthSystem : public System<Health> {
public:
    void update(float deltaTime) override {
        cout << "HealthSystem updating entities with Health" << endl;
    }
};

// Compile-time entity factory
template <typename... Components>
class EntityFactory {
public:
    static Entity create() {
        Entity entity;
        (entity.addComponent(new Components()), ...);
        return entity;
    }
    
    template <typename... Args>
    static Entity createWithArgs(Args&&... args) {
        Entity entity;
        createWithArgsHelper<0>(entity, forward<Args>(args)...);
        return entity;
    }
    
private:
    template <size_t Index, typename T, typename... Rest>
    static void createWithArgsHelper(Entity& entity, T&& component, Rest&&... rest) {
        entity.addComponent(new T(forward<T>(component)));
        if constexpr (sizeof...(Rest) > 0) {
            createWithArgsHelper<Index + 1>(entity, forward<Rest>(rest)...);
        }
    }
};

// Compile-time game configuration
template <bool EnablePhysics, bool EnableRendering, bool EnableAudio>
struct GameConfig {
    static constexpr bool physics = EnablePhysics;
    static constexpr bool rendering = EnableRendering;
    static constexpr bool audio = EnableAudio;
    
    template <typename SystemType>
    static constexpr bool isSystemEnabled() {
        if constexpr (is_same_v<SystemType, MovementSystem>) {
            return EnablePhysics;
        } else if constexpr (is_same_v<SystemType, HealthSystem>) {
            return true; // Always enabled
        }
        return false;
    }
};

int main() {
    cout << "=== Compile-Time Game Engine ===" << endl;
    
    // Create entities using factory
    auto player = EntityFactory<Position, Velocity, Health>::createWithArgs(
        Position(0.0f, 0.0f),
        Velocity(1.0f, 0.0f),
        Health(100)
    );
    
    auto enemy = EntityFactory<Position, Health>::createWithArgs(
        Position(10.0f, 5.0f),
        Health(50)
    );
    
    // Check component masks
    cout << "Player has Position: " << player.hasComponent<Position>() << endl;
    cout << "Player has Velocity: " << player.hasComponent<Velocity>() << endl;
    cout << "Player has Health: " << player.hasComponent<Health>() << endl;
    cout << "Player has all required: " << player.hasComponents<Position, Velocity, Health>() << endl;
    
    cout << endl;
    
    cout << "Enemy has Position: " << enemy.hasComponent<Position>() << endl;
    cout << "Enemy has Velocity: " << enemy.hasComponent<Velocity>() << endl;
    cout << "Enemy has Health: " << enemy.hasComponent<Health>() << endl;
    
    cout << endl;
    
    // Test systems
    MovementSystem movementSystem;
    HealthSystem healthSystem;
    
    cout << "MovementSystem can process player: " << movementSystem.canProcessEntity(player) << endl;
    cout << "MovementSystem can process enemy: " << movementSystem.canProcessEntity(enemy) << endl;
    cout << "HealthSystem can process player: " << healthSystem.canProcessEntity(player) << endl;
    cout << "HealthSystem can process enemy: " << healthSystem.canProcessEntity(enemy) << endl;
    
    cout << endl;
    
    // Game configuration
    using GameSettings = GameConfig<true, false, true>;
    cout << "Physics enabled: " << GameSettings::physics << endl;
    cout << "Rendering enabled: " << GameSettings::rendering << endl;
    cout << "Audio enabled: " << GameSettings::audio << endl;
    cout << "MovementSystem enabled: " << GameSettings::isSystemEnabled<MovementSystem>() << endl;
    cout << "HealthSystem enabled: " << GameSettings::isSystemEnabled<HealthSystem>() << endl;
    
    cout << endl;
    
    // Update enabled systems
    if constexpr (GameSettings::isSystemEnabled<MovementSystem>()) {
        movementSystem.update(1.0f / 60.0f);
    }
    
    if constexpr (GameSettings::isSystemEnabled<HealthSystem>()) {
        healthSystem.update(1.0f / 60.0f);
    }
    
    // Cleanup (in real engine, would use smart pointers)
    delete player.getComponent<Position>();
    delete player.getComponent<Velocity>();
    delete player.getComponent<Health>();
    delete enemy.getComponent<Position>();
    delete enemy.getComponent<Health>();
    
    return 0;
}
```

---

## ⚡ Performance Considerations

### Advantages
- ✅ **Zero Runtime Overhead**: All computation happens at compile time
- ✅ **Optimized Code**: Compiler can optimize based on known values
- ✅ **Type Safety**: Compile-time checking prevents runtime errors
- ✅ **Code Generation**: Generate specialized code for different configurations

### Considerations
- ⚠️ **Compilation Time**: Can significantly increase build time
- ⚠️ **Memory Usage**: High memory consumption during compilation
- ⚠️ **Debugging**: Difficult to debug template metaprograms
- ⚠️ **Compiler Limits**: May hit recursion depth or template instantiation limits

---

## 🐛 Common Pitfalls

| Problem | Solution |
|---------|----------|
| **Recursion depth exceeded** | Use iterative approaches or increase compiler limits |
| **Long compilation times** | Use constexpr functions instead of templates when possible |
| **Cryptic error messages** | Use static_assert for clearer error messages |
| **Template instantiation explosion** | Use common base classes and inheritance |

---

## ✅ Best Practices

1. **Prefer `constexpr` functions** over template recursion when possible
2. **Use `static_assert`** for better error messages
3. **Keep metaprograms simple** and well-documented
4. **Use concepts (C++20)** instead of SFINAE when available
5. **Test compilation time** impact of complex metaprograms
6. **Use type traits** from the standard library when possible
7. **Document compile-time requirements** and constraints

---

## 📚 Related Topics

- [Function Templates](01_Function_Templates.md)
- [Class Templates](02_Class_Templates.md)
- [Template Specialization](03_Template_Specialization.md)
- [Variadic Templates](04_Variadic_Templates.md)

---

## 🚀 Next Steps

Continue learning about:
- **C++20 Concepts**: Modern template constraints
- **Constexpr Everything**: Compile-time programming with constexpr
- **Advanced SFINAE Techniques**: More sophisticated template tricks
- **Standard Library Implementation**: How the STL uses template metaprogramming

---
