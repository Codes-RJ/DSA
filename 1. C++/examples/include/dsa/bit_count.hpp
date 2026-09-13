#pragma once

namespace dsa {

inline unsigned int count_set_bits(unsigned int value) noexcept {
    unsigned int count = 0U;
    while (value != 0U) {
        value &= value - 1U;
        ++count;
    }
    return count;
}

}  // namespace dsa
