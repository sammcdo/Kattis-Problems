#include 
#include 
#include 
#include 

using namespace std;

#define rep(i, a, b) for (int i = a; i < (b); ++i)
#define For(i, a) for (int i = 0; i < (a); ++i)
#define all(x) begin(x), end(x)
#define is_in(x, s) ((s).find(x) != (s).end())
#define endl '\n'
#define pi acos(-1.0)
typedef long long ll;
template 
using V = vector;
template 
using VV = vector>;
template 
using umap = unordered_map;
typedef pair pii;
typedef vector vi;
typedef unordered_map uimap;

int graph[62][62], rgraph[62][62], prevs[62];
int inf = 10000007;

bool bfs(int source, int sink, int a) {
    queue q;
    q.push(source);
    while (q.size()) {
        int curr = q.front();
        q.pop();
        For(i, 2*a+2) {
            if (rgraph[curr][i] > 0 && prevs[i] == -1) {
                prevs[i] = curr;
                if (i == sink) {
                    return true;
                }
                q.push(i);
            }
        }
    }
    return false;
}

int EdmondsKarp(int source, int sink, int a) {
    int flow = 0;
    while (true) {
        For(i, 2*a+2) {
            prevs[i] = -1;
        }

        if (!bfs(source, sink, a)) {
            break;
        }

        int mod = inf;
        for(int i = sink; i != source; i = prevs[i]) {
            mod = min(mod, rgraph[prevs[i]][i]);
        }
        flow += mod;
        for(int i = sink; i != source; i = prevs[i]) {
            rgraph[prevs[i]][i] -= mod;
            rgraph[i][prevs[i]] += mod;
        }
    }

    return flow;
}

int main() {
    int a = 0;
    cin >> a;

    For(i, a) {
        For(j, a) {
            cin >> graph[i][j];
        }
    }

    int l, r, m, best;
    l = 1;
    r = 1000000;
    best = 0;
    while (l <= r) {
        m = (l+r)/2;
        // cout << m  << ":" << l << " " << r << endl;

        memset(rgraph, 0, sizeof(rgraph));

        for(int i = 0; i < a; i++)
            for(int j = 0; j < a; j++)
                rgraph[i][j+a] = graph[i][j] >= m;
        
        for(int i = 0; i < a; i++) rgraph[2*a][i] = 1;
        for(int j = 0; j < a; j++) rgraph[j+a][2*a+1] = 1;

        if (EdmondsKarp(2*a, 2*a+1, a) == a) {
            l = m+1;
            best = max(best, m);
        } else {
            r = m-1;
        }

    }

    cout << best << endl;

    return 0;
}