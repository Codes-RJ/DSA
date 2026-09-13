#pragma once

#include <string>
#include <unordered_map>
#include <vector>

namespace dsa {

inline std::unordered_map<std::string, std::size_t>
word_frequencies(const std::vector<std::string>& words) {
    std::unordered_map<std::string, std::size_t> counts;
    for (const std::string& word : words) {
        ++counts[word];
    }
    return counts;
}

}  // namespace dsa
