#pragma once

#include <cstddef>
#include <numeric>
#include <stdexcept>
#include <vector>

namespace dsa {

class DisjointSetUnion {
public:
    explicit DisjointSetUnion(std::size_t size)
        : parent_(size), component_size_(size, 1U), components_(size) {
        std::iota(parent_.begin(), parent_.end(), 0U);
    }

    std::size_t find(std::size_t value) {
        require_valid(value);
        std::size_t root = value;
        while (root != parent_[root]) {
            root = parent_[root];
        }
        while (value != root) {
            const std::size_t next = parent_[value];
            parent_[value] = root;
            value = next;
        }
        return root;
    }

    bool unite(std::size_t left, std::size_t right) {
        std::size_t left_root = find(left);
        std::size_t right_root = find(right);
        if (left_root == right_root) {
            return false;
        }
        if (component_size_[left_root] < component_size_[right_root]) {
            const std::size_t temporary = left_root;
            left_root = right_root;
            right_root = temporary;
        }
        parent_[right_root] = left_root;
        component_size_[left_root] += component_size_[right_root];
        --components_;
        return true;
    }

    bool connected(std::size_t left, std::size_t right) {
        return find(left) == find(right);
    }

    std::size_t component_size(std::size_t value) {
        return component_size_[find(value)];
    }

    std::size_t component_count() const noexcept { return components_; }

private:
    void require_valid(std::size_t value) const {
        if (value >= parent_.size()) {
            throw std::out_of_range("DSU index is out of range");
        }
    }

    std::vector<std::size_t> parent_;
    std::vector<std::size_t> component_size_;
    std::size_t components_;
};

}  // namespace dsa
