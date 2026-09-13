#include <cassert>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>

#include "dsa/binary_search_tree.hpp"
#include "dsa/bit_count.hpp"
#include "dsa/dijkstra.hpp"
#include "dsa/disjoint_set_union.hpp"
#include "dsa/merge_sort.hpp"
#include "dsa/prime.hpp"
#include "dsa/score_board.hpp"
#include "dsa/word_frequencies.hpp"

namespace {

void test_standard_library_example() {
    const auto counts = dsa::word_frequencies({"tree", "graph", "tree"});
    assert(counts.at("tree") == 2U);
    assert(counts.at("graph") == 1U);
}

void test_basics_example() {
    assert(!dsa::is_prime(-5));
    assert(!dsa::is_prime(1));
    assert(dsa::is_prime(2));
    assert(dsa::is_prime(97));
    assert(!dsa::is_prime(100));
}

void test_sorting_example() {
    std::vector<int> values{5, -1, 5, 3, 0};
    dsa::merge_sort(values);
    assert((values == std::vector<int>{-1, 0, 3, 5, 5}));
    std::vector<int> empty;
    dsa::merge_sort(empty);
    assert(empty.empty());
}

void test_oop_example() {
    dsa::ScoreBoard board;
    board.record("Ada", 90);
    board.record("Grace", 95);
    assert(board.size() == 2U);
    assert(board.highest() == std::make_pair(std::string("Grace"), 95));
    bool rejected = false;
    try {
        board.record("", 10);
    } catch (const std::invalid_argument&) {
        rejected = true;
    }
    assert(rejected);
}

void test_dsu_example() {
    dsa::DisjointSetUnion sets(5U);
    assert(sets.component_count() == 5U);
    assert(sets.unite(0U, 1U));
    assert(sets.unite(1U, 2U));
    assert(!sets.unite(0U, 2U));
    assert(sets.connected(0U, 2U));
    assert(sets.component_size(1U) == 3U);
    assert(sets.component_count() == 3U);
}

void test_tree_example() {
    dsa::BinarySearchTree tree;
    assert(tree.insert(4));
    assert(tree.insert(2));
    assert(tree.insert(6));
    assert(tree.insert(5));
    assert(!tree.insert(4));
    assert(tree.contains(5));
    assert(!tree.contains(9));
    assert((tree.inorder() == std::vector<int>{2, 4, 5, 6}));
}

void test_bit_example() {
    assert(dsa::count_set_bits(0U) == 0U);
    assert(dsa::count_set_bits(0b101101U) == 4U);
}

void test_graph_example() {
    const dsa::WeightedGraph graph{
        {{1U, 4}, {2U, 1}},
        {{3U, 1}},
        {{1U, 2}, {3U, 5}},
        {}};
    const auto distance = dsa::dijkstra(graph, 0U);
    assert((distance == std::vector<long long>{0, 3, 1, 4}));

    const dsa::WeightedGraph disconnected{{}, {}};
    const auto unreachable = dsa::dijkstra(disconnected, 0U);
    assert(unreachable[1] == std::numeric_limits<long long>::max());

    bool rejected = false;
    try {
        static_cast<void>(dsa::dijkstra({{{0U, -1}}}, 0U));
    } catch (const std::invalid_argument&) {
        rejected = true;
    }
    assert(rejected);
}

}  // namespace

int main() {
    test_standard_library_example();
    test_basics_example();
    test_sorting_example();
    test_oop_example();
    test_dsu_example();
    test_tree_example();
    test_bit_example();
    test_graph_example();
}
