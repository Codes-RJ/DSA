# Comparison of Graph Representations

## Overview
Choosing the right graph representation depends on the nature of the graph (dense vs. sparse) and the operations most frequently performed.

## Comparison Table

| Feature | Adjacency Matrix | Adjacency List | Edge List |
|---------|------------------|----------------|-----------|
| **Space** | O(V²) | O(V + E) | O(E) |
| **Check Edge (u,v)** | O(1) | O(degree(u)) | O(E) |
| **Find Neighbors** | O(V) | O(degree(u)) | O(E) |
| **Add Edge** | O(1) | O(1) | O(1) |
| **Delete Edge** | O(1) | O(degree(u)) | O(E) |
| **Best For** | Dense Graphs | Sparse Graphs | Edge-based Algorithms |

## Decision Criteria

### 1. Graph Density
- **Dense Graphs (E ≈ V²)**: Adjacency Matrix is often better as it provides O(1) edge checks and the space overhead is comparable to other methods.
- **Sparse Graphs (E ≪ V²)**: Adjacency List is far superior due to significantly lower space requirements and better performance for traversals.

### 2. Common Operations
- **Edge Queries**: If you frequently need to check if vertex `u` is connected to `v`, use Adjacency Matrix.
- **Neighbor Iteration**: If you need to visit all neighbors (traversal), Adjacency List is faster as it only stores actual connections.
- **Edge Processing**: If you need to sort edges or iterate over all edges (like in Kruskal's), Edge List is the most direct representation.

### 3. Memory Constraints
- For massive graphs (billions of nodes), an Adjacency Matrix is impossible (requires Petabytes).
- Adjacency Lists are the standard for large-scale graph databases and social networking graphs.

## Summary Checklist

- [ ] **Sparse Graph?** → Adjacency List
- [ ] **Dense Graph?** → Adjacency Matrix
- [ ] **Edge Weights only?** → Edge List
- [ ] **Frequent BFS/DFS?** → Adjacency List
- [ ] **Floyd-Warshall Algorithm?** → Adjacency Matrix
- [ ] **Kruskal's Algorithm?** → Edge List

## Specialized Representations
In some advanced cases, you might use:
- **Compressed Sparse Row (CSR)**: More memory-efficient version of adjacency list for static graphs.
- **Spatial Graphs**: Using R-trees or Quadtrees for graphs based on geographic or spatial data.
- **Hash Map Adjacency List**: Using `std::unordered_map<int, std::unordered_set<int>>` for O(1) average edge checks while maintaining space efficiency.
