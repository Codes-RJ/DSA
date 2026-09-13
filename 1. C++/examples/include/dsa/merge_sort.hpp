#pragma once

#include <algorithm>
#include <cstddef>
#include <vector>

namespace dsa {
namespace detail {

inline void merge_sort_range(std::vector<int>& values,
                             std::vector<int>& buffer,
                             std::size_t first,
                             std::size_t last) {
    if (last - first < 2U) {
        return;
    }

    const std::size_t middle = first + (last - first) / 2U;
    merge_sort_range(values, buffer, first, middle);
    merge_sort_range(values, buffer, middle, last);
    std::merge(values.begin() + static_cast<std::ptrdiff_t>(first),
               values.begin() + static_cast<std::ptrdiff_t>(middle),
               values.begin() + static_cast<std::ptrdiff_t>(middle),
               values.begin() + static_cast<std::ptrdiff_t>(last),
               buffer.begin() + static_cast<std::ptrdiff_t>(first));
    std::copy(buffer.begin() + static_cast<std::ptrdiff_t>(first),
              buffer.begin() + static_cast<std::ptrdiff_t>(last),
              values.begin() + static_cast<std::ptrdiff_t>(first));
}

}  // namespace detail

inline void merge_sort(std::vector<int>& values) {
    std::vector<int> buffer(values.size());
    detail::merge_sort_range(values, buffer, 0U, values.size());
}

}  // namespace dsa
