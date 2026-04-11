# Graph Algorithm - Bipartite Matching (Hopcroft-Karp Algorithm)

## 📖 Overview

Bipartite matching finds the maximum set of edges in a bipartite graph such that no two edges share a common vertex. The Hopcroft-Karp algorithm efficiently finds maximum matching in O(E√V) time, making it suitable for large bipartite graphs. This has applications in job assignment, marriage problems, and resource allocation.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Bipartite Graph** | Graph with two disjoint vertex sets (U and V) |
| **Matching** | Set of edges without common vertices |
| **Maximum Matching** | Matching with maximum number of edges |
| **Perfect Matching** | Matching that covers all vertices |
| **Augmenting Path** | Path alternating between unmatched and matched edges |

---

## 📊 Bipartite Matching Visualization

```
Left Set (U)     Right Set (V)
    0               3
    |\              |
    | \             |
    |  \            |
    1---4           5
    |               |
    |               |
    2               6

Matching: (0,3), (1,4), (2,5)
Maximum matching size = 3
```

---

## 📝 Complete Implementation

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <list>
#include <algorithm>
#include <climits>
#include <iomanip>
using namespace std;

class BipartiteGraph {
private:
    int leftSize;
    int rightSize;
    vector<list<int>> adj;  // Adjacency list from left to right
    
public:
    BipartiteGraph(int left, int right) : leftSize(left), rightSize(right) {
        adj.resize(left);
    }
    
    void addEdge(int u, int v) {
        adj[u].push_back(v);
    }
    
    // ============ BASIC DFS MATCHING (O(V * E)) ============
    int maxMatchingDFS() {
        vector<int> matchRight(rightSize, -1);
        int result = 0;
        
        for (int u = 0; u < leftSize; u++) {
            vector<bool> visited(rightSize, false);
            if (dfs(u, visited, matchRight)) {
                result++;
            }
        }
        
        return result;
    }
    
private:
    bool dfs(int u, vector<bool>& visited, vector<int>& matchRight) {
        for (int v : adj[u]) {
            if (!visited[v]) {
                visited[v] = true;
                
                if (matchRight[v] == -1 || dfs(matchRight[v], visited, matchRight)) {
                    matchRight[v] = u;
                    return true;
                }
            }
        }
        return false;
    }
    
public:
    // ============ HOPCROFT-KARP ALGORITHM (O(E * sqrt(V))) ============
    int hopcroftKarp() {
        vector<int> pairU(leftSize, -1);
        vector<int> pairV(rightSize, -1);
        vector<int> dist(leftSize);
        
        int matching = 0;
        
        while (bfs(pairU, pairV, dist)) {
            for (int u = 0; u < leftSize; u++) {
                if (pairU[u] == -1) {
                    if (dfsHopcroftKarp(u, pairU, pairV, dist)) {
                        matching++;
                    }
                }
            }
        }
        
        return matching;
    }
    
private:
    bool bfs(vector<int>& pairU, vector<int>& pairV, vector<int>& dist) {
        queue<int> q;
        
        for (int u = 0; u < leftSize; u++) {
            if (pairU[u] == -1) {
                dist[u] = 0;
                q.push(u);
            } else {
                dist[u] = INT_MAX;
            }
        }
        
        bool found = false;
        
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            
            for (int v : adj[u]) {
                if (pairV[v] != -1 && dist[pairV[v]] == INT_MAX) {
                    dist[pairV[v]] = dist[u] + 1;
                    q.push(pairV[v]);
                } else if (pairV[v] == -1) {
                    found = true;
                }
            }
        }
        
        return found;
    }
    
    bool dfsHopcroftKarp(int u, vector<int>& pairU, vector<int>& pairV, vector<int>& dist) {
        for (int v : adj[u]) {
            if (pairV[v] == -1 || (dist[pairV[v]] == dist[u] + 1 && 
                dfsHopcroftKarp(pairV[v], pairU, pairV, dist))) {
                pairU[u] = v;
                pairV[v] = u;
                return true;
            }
        }
        
        dist[u] = INT_MAX;
        return false;
    }
    
public:
    // ============ MAXIMUM MATCHING WITH DETAILS ============
    struct MatchingInfo {
        int leftVertex;
        int rightVertex;
    };
    
    vector<MatchingInfo> getMaximumMatching() {
        vector<int> pairU(leftSize, -1);
        vector<int> pairV(rightSize, -1);
        vector<int> dist(leftSize);
        
        while (bfs(pairU, pairV, dist)) {
            for (int u = 0; u < leftSize; u++) {
                if (pairU[u] == -1) {
                    dfsHopcroftKarp(u, pairU, pairV, dist);
                }
            }
        }
        
        vector<MatchingInfo> matching;
        for (int u = 0; u < leftSize; u++) {
            if (pairU[u] != -1) {
                matching.push_back({u, pairU[u]});
            }
        }
        
        return matching;
    }
    
    // ============ CHECK PERFECT MATCHING ============
    bool hasPerfectMatching() {
        int maxMatch = hopcroftKarp();
        return maxMatch == min(leftSize, rightSize);
    }
    
    // ============ VERTEX COVER (Kőnig's Theorem) ============
    vector<int> minimumVertexCover() {
        // First find maximum matching
        vector<int> pairU(leftSize, -1);
        vector<int> pairV(rightSize, -1);
        vector<int> dist(leftSize);
        
        while (bfs(pairU, pairV, dist)) {
            for (int u = 0; u < leftSize; u++) {
                if (pairU[u] == -1) {
                    dfsHopcroftKarp(u, pairU, pairV, dist);
                }
            }
        }
        
        // Find vertices reachable from unmatched left vertices in residual graph
        vector<bool> visitedLeft(leftSize, false);
        vector<bool> visitedRight(rightSize, false);
        queue<int> q;
        
        for (int u = 0; u < leftSize; u++) {
            if (pairU[u] == -1) {
                visitedLeft[u] = true;
                q.push(u);
            }
        }
        
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            
            for (int v : adj[u]) {
                if (!visitedRight[v]) {
                    visitedRight[v] = true;
                    if (pairV[v] != -1 && !visitedLeft[pairV[v]]) {
                        visitedLeft[pairV[v]] = true;
                        q.push(pairV[v]);
                    }
                }
            }
        }
        
        // Minimum vertex cover = (Left \ Z) ∪ (Right ∩ Z)
        vector<int> vertexCover;
        for (int u = 0; u < leftSize; u++) {
            if (!visitedLeft[u]) {
                vertexCover.push_back(u);
            }
        }
        for (int v = 0; v < rightSize; v++) {
            if (visitedRight[v]) {
                vertexCover.push_back(leftSize + v);
            }
        }
        
        return vertexCover;
    }
    
    // ============ MAXIMUM INDEPENDENT SET ============
    vector<int> maximumIndependentSet() {
        vector<int> vertexCover = minimumVertexCover();
        vector<bool> inCover(vertexCover.size(), false);
        
        for (int v : vertexCover) {
            inCover[v] = true;
        }
        
        vector<int> independentSet;
        for (int i = 0; i < leftSize + rightSize; i++) {
            if (!inCover[i]) {
                independentSet.push_back(i);
            }
        }
        
        return independentSet;
    }
    
    // ============ DISPLAY ============
    void display() {
        cout << "\nBipartite Graph (Left: 0-" << leftSize-1 << ", Right: " 
             << leftSize << "-" << leftSize+rightSize-1 << "):\n";
        for (int u = 0; u < leftSize; u++) {
            cout << u << " -> ";
            for (int v : adj[u]) {
                cout << v + leftSize << " ";
            }
            cout << endl;
        }
    }
    
    void displayMatching() {
        vector<MatchingInfo> matching = getMaximumMatching();
        
        cout << "\nMaximum Matching (" << matching.size() << " edges):\n";
        for (auto& edge : matching) {
            cout << "  " << edge.leftVertex << " -> " << edge.leftVertex + edge.rightVertex << endl;
        }
    }
};

int main() {
    cout << "=== Bipartite Matching (Hopcroft-Karp) Demo ===" << endl;
    
    // Example 1: Standard bipartite graph
    cout << "\n1. Standard Bipartite Graph:" << endl;
    BipartiteGraph g1(3, 3);
    g1.addEdge(0, 0);
    g1.addEdge(0, 1);
    g1.addEdge(1, 1);
    g1.addEdge(1, 2);
    g1.addEdge(2, 2);
    
    g1.display();
    cout << "\nDFS Matching: " << g1.maxMatchingDFS() << endl;
    cout << "Hopcroft-Karp Matching: " << g1.hopcroftKarp() << endl;
    g1.displayMatching();
    cout << "Perfect matching? " << (g1.hasPerfectMatching() ? "Yes" : "No") << endl;
    
    // Example 2: Complete bipartite graph K3,3
    cout << "\n2. Complete Bipartite Graph K3,3:" << endl;
    BipartiteGraph g2(3, 3);
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            g2.addEdge(i, j);
        }
    }
    
    g2.display();
    cout << "\nMaximum Matching: " << g2.hopcroftKarp() << endl;
    g2.displayMatching();
    cout << "Perfect matching? " << (g2.hasPerfectMatching() ? "Yes" : "No") << endl;
    
    // Example 3: Graph with no perfect matching
    cout << "\n3. Graph with No Perfect Matching:" << endl;
    BipartiteGraph g3(3, 3);
    g3.addEdge(0, 0);
    g3.addEdge(0, 1);
    g3.addEdge(1, 1);
    
    g3.display();
    cout << "\nMaximum Matching: " << g3.hopcroftKarp() << endl;
    g3.displayMatching();
    cout << "Perfect matching? " << (g3.hasPerfectMatching() ? "Yes" : "No") << endl;
    
    // Example 4: Unbalanced bipartite graph
    cout << "\n4. Unbalanced Bipartite Graph (Left=4, Right=3):" << endl;
    BipartiteGraph g4(4, 3);
    g4.addEdge(0, 0);
    g4.addEdge(0, 1);
    g4.addEdge(1, 1);
    g4.addEdge(1, 2);
    g4.addEdge(2, 0);
    g4.addEdge(2, 2);
    g4.addEdge(3, 1);
    
    g4.display();
    cout << "\nMaximum Matching: " << g4.hopcroftKarp() << endl;
    g4.displayMatching();
    
    // Example 5: Job assignment problem
    cout << "\n5. Job Assignment Problem:" << endl;
    BipartiteGraph g5(4, 4);
    // Workers (0-3) and Jobs (0-3)
    g5.addEdge(0, 0);  // Worker 0 can do Job 0
    g5.addEdge(0, 1);  // Worker 0 can do Job 1
    g5.addEdge(1, 1);  // Worker 1 can do Job 1
    g5.addEdge(1, 2);  // Worker 1 can do Job 2
    g5.addEdge(2, 2);  // Worker 2 can do Job 2
    g5.addEdge(2, 3);  // Worker 2 can do Job 3
    g5.addEdge(3, 0);  // Worker 3 can do Job 0
    g5.addEdge(3, 3);  // Worker 3 can do Job 3
    
    g5.display();
    cout << "\nMaximum Job Assignment: " << g5.hopcroftKarp() << endl;
    g5.displayMatching();
    
    // Example 6: Vertex cover and independent set
    cout << "\n6. Minimum Vertex Cover & Maximum Independent Set:" << endl;
    BipartiteGraph g6(3, 3);
    g6.addEdge(0, 0);
    g6.addEdge(0, 1);
    g6.addEdge(1, 1);
    g6.addEdge(1, 2);
    g6.addEdge(2, 2);
    
    g6.display();
    cout << "\nMaximum Matching: " << g6.hopcroftKarp() << endl;
    
    vector<int> vertexCover = g6.minimumVertexCover();
    cout << "Minimum Vertex Cover (" << vertexCover.size() << " vertices): ";
    for (int v : vertexCover) cout << v << " ";
    cout << endl;
    
    vector<int> independentSet = g6.maximumIndependentSet();
    cout << "Maximum Independent Set (" << independentSet.size() << " vertices): ";
    for (int v : independentSet) cout << v << " ";
    cout << endl;
    
    // Example 7: Large graph for performance test
    cout << "\n7. Performance Test (Large Graph):" << endl;
    BipartiteGraph g7(100, 100);
    for (int i = 0; i < 100; i++) {
        for (int j = max(0, i-10); j < min(100, i+11); j++) {
            g7.addEdge(i, j);
        }
    }
    
    cout << "Graph: 100 left, 100 right, ~2000 edges" << endl;
    
    auto start = chrono::high_resolution_clock::now();
    int match = g7.hopcroftKarp();
    auto end = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::microseconds>(end - start).count();
    
    cout << "Maximum Matching: " << match << endl;
    cout << "Time taken: " << duration << " μs" << endl;
    
    return 0;
}
```

---

## 📊 Complexity Analysis

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **DFS Matching** | O(V × E) | O(V) |
| **Hopcroft-Karp** | O(E × √V) | O(V) |

---

## 🎯 Applications

| Application | Description |
|-------------|-------------|
| **Job Assignment** | Assign workers to tasks |
| **Marriage Problem** | Stable matching |
| **Course Scheduling** | Assign students to courses |
| **Network Flow** | Bipartite matching via max flow |
| **Image Segmentation** | Pixel labeling |
| **DNA Sequence Alignment** | Pattern matching |

---

## ✅ Key Takeaways

1. **Bipartite matching** finds maximum edge set without shared vertices
2. **Hopcroft-Karp** is O(E√V) - faster than DFS matching
3. **Perfect matching** covers all vertices
4. **König's theorem**: Vertex cover size = matching size
5. **Maximum independent set** = total vertices - minimum vertex cover

---