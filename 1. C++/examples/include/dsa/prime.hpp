#pragma once

namespace dsa {

inline bool is_prime(int value) noexcept {
    if (value < 2) {
        return false;
    }
    for (int divisor = 2; divisor <= value / divisor; ++divisor) {
        if (value % divisor == 0) {
            return false;
        }
    }
    return true;
}

}  // namespace dsa
