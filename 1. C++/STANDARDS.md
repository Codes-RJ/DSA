# C++ Standards and Portability Policy

## Supported Tracks

| Track | Purpose | Policy |
|---|---|---|
| C++17 core | Required language, standard-library, OOP, and DSA curriculum | Canonical verified examples must build as C++17 |
| C++20 extension | Concepts, ranges, `std::span`, `<numbers>`, and selected modern facilities | Every page and code block must be labeled C++20 |
| C++23 extension | Facilities such as `std::expected`, `std::print`, and newer ranges support | Optional reference material; never an unexplained prerequisite for the core path |

Using a newer compiler does not permit an unlabeled C++20 or C++23 feature in a C++17 lesson.

## Validation Environments

Automated verification runs the C++17 example suite on:

- the GCC version supplied by GitHub's current Ubuntu hosted runner;
- the Clang version supplied by the same runner;
- MSVC on GitHub's current Windows hosted runner;
- GCC with AddressSanitizer and UndefinedBehaviorSanitizer.

These rolling environments describe what CI tests; they are not a promise that every illustrative Markdown fragment has already been extracted or verified. The local CMake requirement is version 3.16 or newer.

## Portability Rules

Canonical C++17 examples must:

- avoid variable-length arrays, compiler-specific aggregate headers, and non-standard mathematical macros;
- use fixed-width integer types when width is part of the algorithm's contract;
- distinguish language guarantees from common implementation behavior;
- avoid assuming a cache-line size, container growth factor, short-string layout, object layout, or ABI;
- avoid signed-overflow assumptions and check arithmetic where the input domain can exceed the representation;
- state any operating-system, terminal, filesystem, or locale dependency.

## Version Labels

Place a version note near the beginning of each lesson:

```text
> Minimum standard: C++17
```

If only one section needs a newer standard, label that section and keep the rest of the lesson on its declared baseline. Prefer a separate extension page when the newer feature changes the teaching path substantially.

## Verification Labels

- **Verified** means an extracted source is built and tested automatically in the declared standard.
- **Illustrative** means the code explains an idea but is not yet part of automated verification.
- **Pseudocode** means the block is intentionally not C++ and should use a non-C++ fence label.
- **Historical** means the facility is deprecated, removed, or retained only to interpret older code.

See [`examples/README.md`](examples/README.md) for the current verified examples and [`REPORT.md`](REPORT.md) for the audit status.
