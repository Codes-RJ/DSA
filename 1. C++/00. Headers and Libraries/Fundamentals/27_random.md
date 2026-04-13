# 27_random - Random Number Generation Library

The `random` header provides a modern, flexible, and statistically robust framework for random number generation in C++, replacing the old `rand()` / `srand()` approach.

## 📖 Overview

`<random>` separates the concern of *generating* random bits (engines) from the concern of *mapping* them to a useful range (distributions). This two-part design makes it easy to swap algorithms without changing the rest of your code.

- **Engines** — produce a stream of pseudo-random integers
- **Distributions** — transform engine output into numbers with a specific statistical shape
- **`random_device`** — provides a non-deterministic seed from the OS

## 🎯 Key Components

### Engines
- `mt19937` — Mersenne Twister (32-bit); most common choice
- `mt19937_64` — Mersenne Twister (64-bit)
- `default_random_engine` — implementation-defined
- `minstd_rand` — Linear Congruential Generator (fast, lower quality)

### Distributions
- `uniform_int_distribution<T>` — integers in [a, b]
- `uniform_real_distribution<T>` — reals in [a, b)
- `normal_distribution<T>` — Gaussian / bell curve
- `bernoulli_distribution` — true/false with probability p
- `poisson_distribution<T>` — Poisson-distributed integers
- `discrete_distribution<T>` — weighted random choice

### Utilities
- `random_device` — non-deterministic seed source
- `shuffle()` — randomly reorders a range (from `<algorithm>`)
- `sample()` — randomly selects k elements from a range (C++17)

## 🔧 Basic Operations

### Setting Up an Engine and Distribution
```cpp
#include <iostream>
#include <random>

int main() {
    // 1. Create a seed from the hardware
    std::random_device rd;

    // 2. Seed a Mersenne Twister engine
    std::mt19937 gen(rd());

    // 3. Define a distribution: uniform integers in [1, 6]
    std::uniform_int_distribution<int> dice(1, 6);

    // 4. Generate numbers
    for (int i = 0; i < 5; i++) {
        std::cout << dice(gen) << " ";
    }
    std::cout << "\n";

    return 0;
}
```

### Real-Valued Distribution
```cpp
#include <iostream>
#include <random>

int main() {
    std::mt19937 gen(std::random_device{}());
    std::uniform_real_distribution<double> dist(0.0, 1.0);

    for (int i = 0; i < 5; i++) {
        std::cout << dist(gen) << "\n";
    }

    return 0;
}
```

### Normal Distribution
```cpp
#include <iostream>
#include <random>

int main() {
    std::mt19937 gen(std::random_device{}());
    std::normal_distribution<double> dist(0.0, 1.0); // mean=0, stddev=1

    for (int i = 0; i < 5; i++) {
        std::cout << dist(gen) << "\n";
    }

    return 0;
}
```

## 📊 Distribution Reference

| Distribution | Header | Parameters | Typical Use |
|---|---|---|---|
| `uniform_int_distribution` | `<random>` | [a, b] | Dice rolls, random index |
| `uniform_real_distribution` | `<random>` | [a, b) | Probabilities, floats |
| `normal_distribution` | `<random>` | mean, stddev | Simulation, noise |
| `bernoulli_distribution` | `<random>` | p | Coin flip |
| `poisson_distribution` | `<random>` | mean | Event counting |
| `discrete_distribution` | `<random>` | weights | Weighted choice |

## 🎮 Practical Examples

### Example 1: Simulating a Dice Game
```cpp
#include <iostream>
#include <random>

int rollDice(std::mt19937& gen) {
    std::uniform_int_distribution<int> dist(1, 6);
    return dist(gen);
}

int main() {
    std::mt19937 gen(std::random_device{}());

    int player1 = rollDice(gen);
    int player2 = rollDice(gen);

    std::cout << "Player 1 rolled: " << player1 << "\n";
    std::cout << "Player 2 rolled: " << player2 << "\n";

    if (player1 > player2)      std::cout << "Player 1 wins!\n";
    else if (player2 > player1) std::cout << "Player 2 wins!\n";
    else                         std::cout << "It's a tie!\n";

    return 0;
}
```

### Example 2: Shuffling a Deck of Cards
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <string>

int main() {
    std::vector<std::string> deck;
    std::vector<std::string> suits = {"♠", "♥", "♦", "♣"};
    std::vector<std::string> ranks = {"2","3","4","5","6","7","8","9","10","J","Q","K","A"};

    for (const auto& suit : suits)
        for (const auto& rank : ranks)
            deck.push_back(rank + suit);

    std::mt19937 gen(std::random_device{}());
    std::shuffle(deck.begin(), deck.end(), gen);

    std::cout << "Top 5 cards after shuffle:\n";
    for (int i = 0; i < 5; i++)
        std::cout << "  " << deck[i] << "\n";

    return 0;
}
```

### Example 3: Weighted Random Choice
```cpp
#include <iostream>
#include <random>
#include <vector>
#include <string>

int main() {
    std::mt19937 gen(std::random_device{}());

    std::vector<std::string> items = {"Rare Item", "Common Item", "Epic Item"};
    // Weights: Rare=1, Common=8, Epic=1
    std::discrete_distribution<int> dist({1, 8, 1});

    std::cout << "Loot drops (10 rolls):\n";
    for (int i = 0; i < 10; i++) {
        std::cout << "  Got: " << items[dist(gen)] << "\n";
    }

    return 0;
}
```

### Example 4: Monte Carlo Pi Estimation
```cpp
#include <iostream>
#include <random>
#include <cmath>

int main() {
    std::mt19937 gen(std::random_device{}());
    std::uniform_real_distribution<double> dist(-1.0, 1.0);

    int inside = 0;
    int total  = 1'000'000;

    for (int i = 0; i < total; i++) {
        double x = dist(gen);
        double y = dist(gen);
        if (x * x + y * y <= 1.0) inside++;
    }

    double pi_estimate = 4.0 * inside / total;
    std::cout << "Estimated Pi: " << pi_estimate << "\n";
    std::cout << "Actual Pi:    " << 3.14159265358979 << "\n";

    return 0;
}
```

## ⚡ Performance Tips

### Reuse Your Engine — Don't Create It Each Call
```cpp
// Bad: creates and seeds a new engine on every call (slow, poor randomness)
int badRand() {
    std::mt19937 gen(std::random_device{}()); // seeded fresh every time!
    std::uniform_int_distribution<int> d(1, 100);
    return d(gen);
}

// Good: engine lives as long as the program
std::mt19937 globalGen(std::random_device{}());

int goodRand() {
    std::uniform_int_distribution<int> d(1, 100);
    return d(globalGen);
}
```

### Thread Safety
```cpp
// mt19937 is NOT thread-safe. Give each thread its own engine:
#include <thread>
#include <random>

void workerThread(int id) {
    std::mt19937 gen(std::random_device{}()); // per-thread engine
    std::uniform_int_distribution<int> dist(1, 100);
    std::cout << "Thread " << id << ": " << dist(gen) << "\n";
}
```

### Reproducible Runs (Testing / Debugging)
```cpp
// Use a fixed seed for reproducibility
std::mt19937 gen(42); // same sequence every run
```

## 🐛 Common Pitfalls & Solutions

### 1. Using `rand()` in New Code
```cpp
// Bad: rand() has poor statistical properties and a global state
int x = rand() % 100;

// Good: use <random>
std::mt19937 gen(std::random_device{}());
std::uniform_int_distribution<int> dist(0, 99);
int x = dist(gen);
```

### 2. Modulo Bias with `rand()`
```cpp
// Problem: uneven distribution when RAND_MAX+1 is not divisible by range
int biased = rand() % 6; // wrong

// Solution: use uniform_int_distribution which eliminates bias
std::uniform_int_distribution<int> dice(0, 5); // correct
```

### 3. Forgetting to Seed the Engine
```cpp
// Will produce the SAME sequence every run
std::mt19937 gen; // default seed = 0
std::uniform_int_distribution<int> dist(1, 100);
std::cout << dist(gen); // always the same first value

// Fix: seed with random_device
std::mt19937 gen(std::random_device{}());
```

### 4. Seeding `mt19937_64` with a 32-bit Device
```cpp
// Weak: 64-bit engine seeded with only 32 bits
std::mt19937_64 gen(std::random_device{}()); // only 32-bit seed!

// Strong: use seed_seq for full 64-bit seeding
std::random_device rd;
std::seed_seq seed{rd(), rd()};
std::mt19937_64 gen(seed);
```

## 🎯 Best Practices

1. **Always use `random_device` to seed** your engine unless you need reproducibility
2. **Reuse engines** — create them once and pass by reference
3. **Match the distribution to the task** — don't use `uniform_int` for normally-distributed noise
4. **Use `shuffle()` instead of writing your own** Fisher-Yates implementation
5. **Fix the seed during testing** so results are reproducible
6. **Use `mt19937`** for general purpose; `mt19937_64` for 64-bit outputs

## 📚 Related Headers

- [`algorithm.md`](04_algorithm.md) — `std::shuffle` and `std::sample`
- [`cstdlib.md`](06_cstdlib.md) — Legacy `rand()` / `srand()`
- [`numeric.md`](24_numeric.md) — Numeric algorithms that pair well with random data

---

## Next Step

- Go to [28_fstream.md](28_fstream.md) to continue with fstream.
