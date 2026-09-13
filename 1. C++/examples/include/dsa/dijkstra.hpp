#pragma once

#include <cstddef>
#include <functional>
#include <limits>
#include <queue>
#include <stdexcept>
#include <utility>
#include <vector>

namespace dsa {

struct WeightedEdge {
    std::size_t to;
    int weight;
};

using WeightedGraph = std::vector<std::vector<WeightedEdge>>;

inline std::vector<long long> dijkstra(const WeightedGraph& graph,
                                       std::size_t source) {
    if (source >= graph.size()) {
        throw std::out_of_range("source vertex is out of range");
    }
    for (const auto& edges : graph) {
        for (const WeightedEdge& edge : edges) {
            if (edge.to >= graph.size()) {
                throw std::out_of_range("edge endpoint is out of range");
            }
            if (edge.weight < 0) {
                throw std::invalid_argument("Dijkstra requires non-negative weights");
            }
        }
    }

    const long long infinity = std::numeric_limits<long long>::max();
    std::vector<long long> distance(graph.size(), infinity);
    using QueueEntry = std::pair<long long, std::size_t>;
    std::priority_queue<QueueEntry,
                        std::vector<QueueEntry>,
                        std::greater<QueueEntry>> frontier;

    distance[source] = 0;
    frontier.emplace(0, source);

    while (!frontier.empty()) {
        const QueueEntry current = frontier.top();
        frontier.pop();
        const long long current_distance = current.first;
        const std::size_t vertex = current.second;
        if (current_distance != distance[vertex]) {
            continue;
        }

        for (const WeightedEdge& edge : graph[vertex]) {
            if (current_distance > infinity - edge.weight) {
                continue;
            }
            const long long candidate = current_distance + edge.weight;
            if (candidate < distance[edge.to]) {
                distance[edge.to] = candidate;
                frontier.emplace(candidate, edge.to);
            }
        }
    }
    return distance;
}

}  // namespace dsa
