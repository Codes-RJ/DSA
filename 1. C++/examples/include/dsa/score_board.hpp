#pragma once

#include <algorithm>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

namespace dsa {

class ScoreBoard {
public:
    void record(std::string name, int score) {
        if (name.empty()) {
            throw std::invalid_argument("name must not be empty");
        }
        entries_.emplace_back(std::move(name), score);
    }

    std::pair<std::string, int> highest() const {
        if (entries_.empty()) {
            throw std::logic_error("score board is empty");
        }
        return *std::max_element(
            entries_.begin(), entries_.end(),
            [](const auto& left, const auto& right) {
                return left.second < right.second;
            });
    }

    std::size_t size() const noexcept { return entries_.size(); }

private:
    std::vector<std::pair<std::string, int>> entries_;
};

}  // namespace dsa
