#include <bits/stdc++.h>
using namespace std;
 
// Class representing a undirected
// graph using matrix
// representation
class Graph {
    int V;
    int** g;
 
public:
    Graph(int V);
 
    // Function to add an edge to graph
    void addEdge(int v, int w);
 
    // Function to check if
    // there exists a path or not
    bool isReachable(int s, int d);
 
    // function to compute paths
    // in the matrix using
    // Floyd Warshall Algorithm
    void computePaths();
};
 
Graph::Graph(int V)
{
    this->V = V;
    g = new int*[V + 1];
    for (int i = 1; i < V + 1; i++) {
        // Rows may not be contiguous
        g[i] = new int[V + 1];
 
        // Initialize all entries
        // as false to indicate
        // that there are
        // no edges initially
        memset(g[i], 0, (V + 1) * sizeof(int));
    }
 
    // Initializing node to itself
    // as it is always reachable
    for (int i = 1; i <= V; i++)
        g[i][i] = 1;
}
 
// Function to add edge between nodes
void Graph::addEdge(int v, int w)
{
    g[v][w] = 1;
    g[w][v] = 1;
}
 
// Function to compute the path
void Graph::computePaths()
{
    // Use Floyd Warshall algorithm
    // to detect if a path exists
    for (int k = 1; k <= V; k++) {
 
        // Try every vertex as an
        // intermediate vertex
        // to check if a path exists
        for (int i = 1; i <= V; i++) {
            for (int j = 1; j <= V; j++)
                g[i][j] = g[i][j]
                          | (g[i][k]
                             && g[k][j]);
        }
    }
}
 
// Function to check if nodes are reachable
bool Graph::isReachable(int s, int d)
{
 
    if (g[s][d] == 1)
        return true;
    else
        return false;
}
 
// Driver code
int main()
{
 
    Graph _g(4);
    _g.addEdge(1, 2);
    _g.addEdge(1, 3);
    _g.addEdge(2, 4);
    _g.computePaths();
 
    int u = 4, v = 3;
    if (_g.isReachable(u, v))
        cout << "Yes\n";
    else
        cout << "No\n";
 
    return 0;
}