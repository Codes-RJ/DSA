# Toolchain, Builds, and Verification

> **Stage:** 0 of the [C++ and DSA learning path](LEARNING_PATH.md)
>
> **Core standard:** C++17
>
> **Goal:** Build, diagnose, and test a multi-file C++ program before studying data structures.

## 1. What the Toolchain Does

A typical build has four conceptual steps:

1. **Preprocessing** expands `#include` directives and macros for each source file.
2. **Compilation** checks C++ syntax and semantics and produces assembly or object code.
3. **Assembly** produces an object file; compiler drivers normally perform this automatically.
4. **Linking** combines object files and libraries, resolves external names, and produces an executable.

A **translation unit** is one source file after preprocessing. Headers are normally included into translation units; they are not independently linked implementation containers.

This distinction explains two common diagnostic classes:

- a compiler error normally identifies invalid code within one translation unit;
- an undefined-reference or unresolved-external error normally means compilation succeeded but the linker could not find one required definition.

## 2. A Minimal Multi-File Layout

```text
project/
|-- CMakeLists.txt
|-- include/
|   `-- statistics.hpp
|-- src/
|   |-- statistics.cpp
|   `-- main.cpp
`-- tests/
    `-- statistics_tests.cpp
```

Place public declarations and small templates in headers. Place non-template definitions in source files unless there is a reason to make them inline. Every file should include what it directly uses.

## 3. Headers and the One Definition Rule

Use an include guard or `#pragma once` in every project header. Avoid non-inline function definitions and mutable global objects in headers: including such a header from multiple translation units can violate the One Definition Rule (ODR).

Templates usually need their complete definitions visible at the point of instantiation, which is why template definitions commonly live in headers. Ordinary functions do not have that requirement.

## 4. Selecting the Language Standard

This curriculum's core is C++17. With common compiler drivers:

```text
g++ -std=c++17 -Wall -Wextra -Wpedantic main.cpp -o app
clang++ -std=c++17 -Wall -Wextra -Wpedantic main.cpp -o app
cl /std:c++17 /W4 /permissive- main.cpp
```

Compiler names and output switches vary by platform. See [STANDARDS.md](STANDARDS.md) before enabling a newer standard for one lesson.

## 5. Building This Curriculum's Verified Examples

From the `1. C++` directory:

```text
cmake -S . -B build -DBUILD_TESTING=ON
cmake --build build --config Release
ctest --test-dir build --output-on-failure -C Release
```

The `-C Release` argument is needed by multi-configuration generators such as Visual Studio and is harmless to omit with many single-configuration generators. See [`examples/README.md`](examples/README.md) for the verified-source convention.

## 6. Warnings Are Part of the Feedback Loop

Compile new work with strong warnings. Do not suppress a warning until you can explain:

- what condition the compiler detected;
- whether the behavior is wrong, risky, or merely intentional;
- why a code change cannot express the intent more clearly;
- why any suppression is narrow enough not to hide unrelated defects.

Warnings do not prove correctness. A clean build can still contain invalid assumptions, undefined behavior, leaks, races, or algorithmic errors.

## 7. Debuggers and Sanitizers

A debugger helps inspect control flow, call stacks, variables, and memory at a reproducible failure. Learn to set a breakpoint, step into and over a call, inspect the current stack frame, and add a conditional breakpoint.

On supported GCC and Clang configurations, this curriculum can enable AddressSanitizer and UndefinedBehaviorSanitizer:

```text
cmake -S . -B build-sanitize -DBUILD_TESTING=ON -DDSA_ENABLE_SANITIZERS=ON
cmake --build build-sanitize
ctest --test-dir build-sanitize --output-on-failure
```

Sanitizers increase detection, not certainty. They only inspect paths that execute, so pair them with boundary tests and randomized tests.

## 8. Stage Exercise

Create a function declaration in a header, its definition in a source file, and a call from `main.cpp`. Then deliberately produce and diagnose each of these failures:

1. a syntax error;
2. a missing include;
3. an undefined linker reference;
4. a duplicate definition;
5. an out-of-bounds access detected by a sanitizer.

## Exit Criteria

Continue only when you can explain a translation unit, distinguish compiler and linker failures, build the verified examples, run their tests, and interpret at least one debugger or sanitizer report.

## Next Step

Continue to [Language Basics](01.%20Basics/README.md).
