# Exception Context and Nesting

## Translate at Abstraction Boundaries

Low-level exceptions may expose details that do not belong in a public API. Catch them where the abstraction changes, add relevant context, and preserve the original failure.

```cpp
#include <exception>
#include <stdexcept>
#include <string>

void load_profile(const std::string& path) {
    try {
        parse_profile_file(path);
    } catch (...) {
        std::throw_with_nested(
            std::runtime_error("failed to load profile: " + path));
    }
}
```

`std::throw_with_nested` attaches the active exception to the new one when possible. This retains the causal chain without flattening everything into one message.

## Inspecting a Nested Chain

```cpp
#include <iostream>

void print_exception(const std::exception& error, int depth = 0) {
    std::cerr << std::string(static_cast<std::size_t>(depth) * 2U, ' ')
              << error.what() << '\n';
    try {
        std::rethrow_if_nested(error);
    } catch (const std::exception& nested) {
        print_exception(nested, depth + 1);
    } catch (...) {
        std::cerr << "unknown nested exception\n";
    }
}
```

## Rethrowing

Inside a handler, use `throw;` to preserve the active exception's dynamic type. Writing `throw error;` throws a new expression and may slice or otherwise change what propagates.

## Context Policy

Add information that identifies the failed operation:

- the resource or logical record involved;
- the stage of a multi-step operation;
- a source position or request identifier;
- the expected contract.

Do not duplicate the same phrase at every layer, expose credentials, or catch merely to log and immediately rethrow at many levels. Choose one diagnostic boundary to avoid repeated messages.

## Next Step

Continue to [Choosing an Error Model](04_Choosing_an_Error_Model.md).
