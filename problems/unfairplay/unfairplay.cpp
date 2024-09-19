#include <bits/stdc++.h>
#include <deque>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define For(i, a) for(int i = 0; i < (a); ++i)
#define all(x) begin(x), end(x)
#define is_in(x, s) ((s).find(x) != (s).end())
#define endl '\n'
#define pi acos(-1.0)
typedef long long ll;
template<class T> using V=vector<T>;
template<class T> using VV=vector<vector<T>>;
template<class K, class V> using umap=unordered_map<K, V>;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef unordered_map<int, int> uimap;

using namespace std;


int graph[1202][1202] = {0};
int parent[12002] = {0};

int INF = 999999999;

int bfs(int s, int t, int nodes) {
    for (int i = 0; i < nodes; i++) {
        parent[i] = -1;
    }
    deque<pii> q;
    q.push_back(make_pair(s, INF));
    parent[s] = 0;
    while (!q.empty()) {
        pii item = q.front();
        q.pop_front();
        for (int v = 0; v < nodes; v++) {
            if (parent[v] == -1 && graph[item.first][v] > 0) {
                parent[v] = item.first;
                q.push_back(make_pair(v, min(item.second, graph[item.first][v])));
                if (v == t) {
                    return min(item.second, graph[item.first][v]);
                }
            }
        }
    }
    return 0;
};

int FF(int s, int t) {
    // cout << "here" << endl;
    int nodes = t+1;
    int maxFlow = 0;
    while (true) {
        int pathFlow = bfs(s, t, nodes);
        // break;
        if (pathFlow == 0) break;

        int v = t;
        int u;
        while (v != s) {
            u = parent[v];
            graph[u][v] -= pathFlow;
            graph[v][u] += pathFlow;
            v = parent[v];
        }
        maxFlow += pathFlow;
    }
    return maxFlow;
}

int getEdgeFlow(int a, int b) {
    return graph[b][a];
}


int main() {
    cin.tie(nullptr)->ios::sync_with_stdio(false);
    int n;
    int m;
    int tmp;

    while (true) {
        cin >> n;
        if (n == -1) {
            break;
        }
        cin >> m;
        vi scores;
        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;
            scores.push_back(x);
        }



        V<pii> matches;
        V<pii> matchesLeft;
        int myMaxScore = scores[n-1];
        int myTeam = n-1;

        for (int i = 0; i < m; i++) {
            int a; int b;
            cin >> a >> b;
            a--; b--;
            matches.push_back(make_pair(a,b));
            if (a==myTeam || b==myTeam) {
                myMaxScore += 2;
            } else {
                matchesLeft.push_back(make_pair(a,b));
            }
        }

        int source = n+matchesLeft.size();
        int sink = n+matchesLeft.size() + 1;

        for (int i = 0; i < sink+1; i++) {
            for (int j = 0; j < sink+1; j++) {
                graph[i][j] = 0;
            }
        }

        for (int i = 0; i < matchesLeft.size(); i++) {
            pii teams = matchesLeft[i];
            graph[source][n+i] = 2;
            graph[n+i][teams.first] = 2;
            graph[n+i][teams.second] = 2;
        }

        bool done = false;
        for (int i = 0; i < n; i++) {
            if (myMaxScore - scores[i] - 1 < 0) {
                cout << "NO" << endl;
                done = true;
                break;
            }
            graph[i][sink] = myMaxScore - scores[i] - 1;
        }
        if (done) continue;

        // For(i, 100) {
        //     For(j, 100) {
        //         cout << graph[i][j] << " ";
        //     }
        //     cout << endl;
        // }

        int maxF = FF(source, sink);

        if (maxF < 2*matchesLeft.size()) {
            cout << "NO" << endl;
            continue;
        } else {
            int c = 0;
            for (int i = 0; i < m; i++) {
                pii match = matches[i];
                if (match.first == myTeam) {
                    cout << "0 ";
                } else if (match.second == myTeam) {
                    cout << "2 ";
                } else {
                    int matchNode = n+c;
                    if (getEdgeFlow(matchNode, match.first) == 2) {
                        cout << "0 ";
                    } else if (getEdgeFlow(matchNode, match.second) == 2) {
                        cout << "2 ";
                    } else {
                        cout << "1 ";
                    }
                    c++;
                }
            }
            cout << endl;
        }
    }


    
    return 0;
}