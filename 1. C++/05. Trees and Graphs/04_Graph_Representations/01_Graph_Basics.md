# Graph Basics

## Overview
A Graph is a non-linear data structure consisting of **vertices** (also known as nodes) and **edges** that connect these vertices. Graphs are used to model real-world networks such as social networks, road maps, communication networks, and the internet.

## Graph Terminology

- **Vertex (Node)**: A fundamental unit of a graph.
- **Edge**: A connection between two vertices.
- **Degree**: The number of edges incident to a vertex.
- **Path**: A sequence of vertices connected by edges.
- **Cycle**: A path that starts and ends at the same vertex.
- **Connected**: A graph where all vertices are reachable from each other.

## Types of Graphs

- **Undirected Graph**: Edges have no direction. If there's an edge between `(u, v)`, it goes both ways.
- **Directed Graph (Digraph)**: Edges have direction. An edge `(u, v)` is not the same as `(v, u)`.
- **Weighted Graph**: Each edge has an associated numerical weight (e.g., distance, cost, or time).
- **Unweighted Graph**: All edges have equal weight, often implicitly 1.
- **Simple Graph**: A graph with no self-loops or multiple edges between the same pair of vertices.
- **Multigraph**: A graph that allows multiple edges between vertices.

## Representation of Graphs
Graphs can be stored in memory using several methods, each with its own trade-offs:

1.  **Adjacency Matrix**
2.  **Adjacency List**
3.  **Edge List**
4.  **Implicit Graphs**

## Real-World Applications
Graphs are used everywhere, from social media (connections between friends) to Google Maps (routes between cities). They also help in modeling chemical molecules, circuit boards, and task dependencies in projects.

## Graph Characteristics

| Concept     | Description                                           |
|-------------|-------------------------------------------------------|
| Vertices (V)| Total nodes in the graph                              |
| Edges (E)   | Total connections in the graph                        |
| Density     | Ratio of edges to the maximum possible edges          |
| Sparsity    | A graph where `E` is much smaller than `V^2`          |

## Summary
- A graph is a set of vertices and edges.
- Different types of graphs are used to represent different relationship structures.
- Graphs are essential for modeling real-world networks and solving complex problems.
