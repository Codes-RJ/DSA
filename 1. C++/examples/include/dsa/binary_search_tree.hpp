#pragma once

#include <cstddef>
#include <memory>
#include <vector>

namespace dsa {

class BinarySearchTree {
public:
    bool insert(int value) {
        std::unique_ptr<Node>* link = &root_;
        while (*link) {
            if (value == (*link)->value) {
                return false;
            }
            link = value < (*link)->value ? &(*link)->left : &(*link)->right;
        }
        *link = std::make_unique<Node>(value);
        ++size_;
        return true;
    }

    bool contains(int value) const noexcept {
        const Node* node = root_.get();
        while (node != nullptr) {
            if (value == node->value) {
                return true;
            }
            node = value < node->value ? node->left.get() : node->right.get();
        }
        return false;
    }

    std::vector<int> inorder() const {
        std::vector<int> result;
        result.reserve(size_);
        append_inorder(root_.get(), result);
        return result;
    }

    std::size_t size() const noexcept { return size_; }

private:
    struct Node {
        explicit Node(int initial_value) : value(initial_value) {}

        int value;
        std::unique_ptr<Node> left;
        std::unique_ptr<Node> right;
    };

    static void append_inorder(const Node* node, std::vector<int>& result) {
        if (node == nullptr) {
            return;
        }
        append_inorder(node->left.get(), result);
        result.push_back(node->value);
        append_inorder(node->right.get(), result);
    }

    std::unique_ptr<Node> root_;
    std::size_t size_ = 0U;
};

}  // namespace dsa
