# Graphs and DSU

## Graph Basics

- vertex: node
- edge: connection
- directed or undirected
- weighted or unweighted

## Representations

- adjacency list: space-efficient for sparse graphs
- adjacency matrix: easy lookup, expensive in space

## Traversals

- BFS explores level by level
- DFS explores depth-first

## DSU

Disjoint Set Union helps track connected components.

### Core operations

- `find(x)` gets the representative
- `union(a, b)` merges components

### Optimizations

- path compression
- union by rank or size
