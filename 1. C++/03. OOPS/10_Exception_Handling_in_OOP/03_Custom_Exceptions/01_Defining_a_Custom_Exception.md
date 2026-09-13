# Defining a Custom Exception

## Start with a Standard Type

Before creating a type, ask whether `std::invalid_argument`, `std::out_of_range`, `std::logic_error`, `std::runtime_error`, or `std::system_error` already communicates the contract. Standard types reduce API surface and are familiar to callers.

Create a domain type when code must catch the category independently or inspect structured context.

## A Small Domain Exception

```cpp
#include <stdexcept>
#include <string>
#include <utility>

class ParseError : public std::runtime_error {
public:
    ParseError(std::string message, std::size_t line)
        : std::runtime_error(std::move(message)), line_(line) {}

    std::size_t line() const noexcept { return line_; }

private:
    std::size_t line_;
};
```

Usage:

```cpp
int parse_positive(std::string_view token, std::size_t line) {
    // Parsing omitted for focus.
    if (token.empty()) {
        throw ParseError("expected a positive integer", line);
    }
    return 1;
}
```

The example uses `std::string_view`, so the complete translation unit must include `<string_view>`. The exception stores its message through `std::runtime_error` and stores the line number by value; it does not retain the view.

## Catch Correctly

```cpp
try {
    load_document();
} catch (const ParseError& error) {
    report(error.line(), error.what());
} catch (const std::exception& error) {
    report_general(error.what());
}
```

Catching by value can slice a derived exception. Catching a general base first makes later specific handlers unreachable.

## What Belongs in the Type?

Good structured fields are values a caller can act on, such as:

- source position;
- invalid identifier;
- requested and allowed sizes;
- operation name;
- portable error code.

Avoid storing secrets, entire payloads, references into temporary buffers, or unstable implementation details.

## Next Step

Continue to [Hierarchy Design](02_Hierarchy_Design.md).
