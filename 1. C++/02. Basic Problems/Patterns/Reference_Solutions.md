# Pattern Reference Solutions

> Attempt the exercises before reading this page. These references demonstrate decomposition and testable return values; they are not the only correct implementations.

## Shared Helper

```cpp
#include <stdexcept>
#include <string>

void require_positive(int size) {
    if (size <= 0) {
        throw std::invalid_argument("size must be positive");
    }
}

void append_repeated(std::string& output, int count, char value) {
    if (count > 0) {
        output.append(static_cast<std::size_t>(count), value);
    }
}
```

## Left Triangle

```cpp
std::string left_triangle(int size) {
    require_positive(size);
    std::string output;
    for (int row = 1; row <= size; ++row) {
        append_repeated(output, row, '*');
        output += '\n';
    }
    return output;
}
```

## Hollow Square

```cpp
std::string hollow_square(int size) {
    require_positive(size);
    std::string output;
    for (int row = 0; row < size; ++row) {
        for (int column = 0; column < size; ++column) {
            const bool edge = row == 0 || row == size - 1 ||
                              column == 0 || column == size - 1;
            output += edge ? '*' : ' ';
        }
        output += '\n';
    }
    return output;
}
```

## Centered Pyramid

```cpp
std::string centered_pyramid(int size) {
    require_positive(size);
    std::string output;
    for (int row = 1; row <= size; ++row) {
        append_repeated(output, size - row, ' ');
        append_repeated(output, 2 * row - 1, '*');
        output += '\n';
    }
    return output;
}
```

## Floyd's Triangle

```cpp
std::string floyd_triangle(int size) {
    require_positive(size);
    std::string output;
    int value = 1;
    for (int row = 1; row <= size; ++row) {
        for (int column = 0; column < row; ++column) {
            if (column != 0) {
                output += ' ';
            }
            output += std::to_string(value++);
        }
        output += '\n';
    }
    return output;
}
```

## What to Compare

- Are invalid inputs handled consistently?
- Is output generation separate from console I/O?
- Can each formula be explained from row and column boundaries?
- Does the implementation perform work proportional to its output?
- Would the chosen integer type overflow for the accepted input range?

Return to the [Pattern Exercises](README.md) index when finished.
