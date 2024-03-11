#include <bits/stdc++.h>
#include <vector>
#include <unordered_map>
#include <deque>

using namespace std;

#define rep(i, a, b) for (int i = a; i < (b); ++i)
#define For(i, a) for (int i = 0; i < (a); ++i)
#define all(x) begin(x), end(x)
#define is_in(x, s) ((s).find(x) != (s).end())
#define endl '\n'
#define pi acos(-1.0)
typedef long long ll;
template <class T>
using V = vector<T>;
template <class T>
using VV = vector<vector<T>>;
template <class K, class V>
using umap = unordered_map<K, V>;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef unordered_map<int, int> uimap;

// for each tree in forest, find center
// connect centers
// find diameter of final tree

// dfs reusing visited, parent and depth
pii dfs(unordered_map<int, vi> &graph,
        vector<int> &visited,
        vector<int> &parent, 
        vector<int> &dist,
        int a, int visitNum)
{
  deque<pii> s;
  s.push_back(make_pair(a, 0));
  int depth = 0;
  int farthest = a;
  parent[a] = a;
  dist[a] = 0;
  while (!s.empty())
  {
    int node = s.back().first;
    int curr_depth = s.back().second;
    s.pop_back();

    if (visited[node] != visitNum)
    {
      if (curr_depth > depth)
      {
        depth = curr_depth;
        farthest = node;
      }
      visited[node] = visitNum;
      for (auto i : graph[node])
      {
        if (visited[i] != visitNum)
        {
          s.push_back(make_pair(i, curr_depth + 1));
          dist[i] = curr_depth + 1;
          parent[i] = node;
        }
      }
    }
  }

  return make_pair(farthest, depth);
}

int main()
{
  int n, e;

  cin >> n >> e;

  unordered_map<int, vi> graph;

  // make graph
  For(i, e)
  {
    int a, b;
    cin >> a >> b;

    graph[a].push_back(b);
    graph[b].push_back(a);
  }

  vector<int> visited(n);
  vector<int> parent(n);
  vector<int> dist(n);
  vector<pii> diams;
  int counter = 1;
  int total = 0;

  For(i, n)
  {
    // if node hasn't been visited, find diameter of this tree
    if (visited[i] == 0)
    {
      // find farthest node away from current node
      pii current = dfs(graph, visited, parent, dist, i, counter);
      counter++;
      int farthest, depth;
      farthest = current.first;
      depth = current.second;

      // find opposite farthest node for diameter
      current = dfs(graph, visited, parent, dist, farthest, counter);
      counter++;
      depth = current.second;

      // find center node of tree
      int center = current.first;
      int radius = depth / 2;
      while (dist[center] > radius)
      {
        center = parent[center];
      }

      // make pair of diameter, center
      diams.push_back(make_pair(depth, center));
    }
  }

  // always best to have the center of the largest tree as the center
  sort(diams.begin(), diams.end(), greater<pii>());
  int center = diams[0].second;
  rep(i, 1, diams.size())
  {
    // add connections from the largest tree to the other trees
    graph[diams[i].second].push_back(center);
    graph[center].push_back(diams[i].second);
  }

  // go from start to one end of the final tree
  pii current = dfs(graph, visited, parent, dist, 0, counter);
  counter++;

  int farthest, depth;
  farthest = current.first;
  depth = current.second;

  // go to the opposite end of the tree for diameter
  current = dfs(graph, visited, parent, dist, farthest, counter);

  depth = current.second;

  cout << depth;
}