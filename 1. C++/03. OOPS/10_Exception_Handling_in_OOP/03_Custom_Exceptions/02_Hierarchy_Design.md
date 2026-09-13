# Exception Hierarchy Design

## Organize by Recovery Policy

An exception hierarchy should help callers decide what to do. Do not mirror every internal class with a matching exception class.

```text
std::exception
`-- std::runtime_error
    `-- StorageError
        |-- ConnectionError
        `-- QueryError
```

A caller that can retry connection failures catches `ConnectionError`. A boundary that handles every storage failure catches `StorageError`. A top-level diagnostic boundary may catch `std::exception`.

## Example

```cpp
#include <stdexcept>
#include <string>
#include <utility>

class StorageError : public std::runtime_error {
public:
    using std::runtime_error::runtime_error;
};

class ConnectionError : public StorageError {
public:
    ConnectionError(std::string endpoint, std::string message)
        : StorageError(std::move(message)), endpoint_(std::move(endpoint)) {}

    const std::string& endpoint() const noexcept { return endpoint_; }

private:
    std::string endpoint_;
};
```

## Handler Order

```cpp
try {
    synchronize();
} catch (const ConnectionError& error) {
    retry(error.endpoint());
} catch (const StorageError& error) {
    abort_storage_operation(error.what());
} catch (const std::exception& error) {
    report_unexpected(error.what());
}
```

## Avoid Deep Taxonomies

Add a subtype only if at least one caller benefits from catching it separately or inspecting distinct fields. Otherwise, an error code or field on a smaller set of types is easier to evolve.

Public inheritance is appropriate here because each derived object is substitutable for its base failure category. Give polymorphic base types a virtual destructor; `std::exception` already does.

## Review Questions

1. What recovery decision does each type enable?
2. Can callers handle the base category without knowing derived details?
3. Could one enum field replace several nearly empty subclasses?
4. Are any handlers catching a base before a derived type?
5. Does every exception own the data exposed by its accessors?

## Next Step

Continue to [Context and Nesting](03_Context_and_Nesting.md).
