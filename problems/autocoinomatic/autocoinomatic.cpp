#include 

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define For(i, a) for(int i = 0; i < (a); ++i)
#define all(x) begin(x), end(x)
#define is_in(x, s) ((s).find(x) != (s).end())
#define endl '\n'
#define pi acos(-1.0)
typedef long long ll;
template using V=vector;
template using VV=vector>;
template using umap=unordered_map;
template using uset=unordered_set;
typedef pair Point;
typedef vector vi;
typedef unordered_map uimap;


int main() {
  cin.tie(0)->sync_with_stdio(0);

    int n;
    int m;
    cin >> n >> m;

    uset coins;
    For(i, n) {
        int a;
        cin >> a;
        coins.insert(a);
    }

    V> queries;
    uset removed;
    For(i,m) {
        char a;
        int b;
        cin >> a >> b;
        queries.push_back(make_pair(a,b));
        if (a == 'X') {
            removed.insert(b);
        }
    }

    vi always;
    for (auto x : coins) {
        if (removed.find(x) == removed.end()) {
            always.push_back(x);
        }
    }

    sort(always.begin(),always.end());

    vi dp(1E5+1, 1E6);
    dp[0] = 0;
    for (auto x : always) {
        rep(i,x,1E5+1) {
            dp[i] = min(dp[i], dp[i-x]+1);
        }
    }
    vi ans;
    for (int i = queries.size()-1; i >= 0; i--) {
        pair cmd = queries[i];
        if (cmd.first == 'Q') {
            ans.push_back(dp[cmd.second]);
        } else {
            rep(i, cmd.second, 1E5+1) {
                dp[i] = min(dp[i], dp[i-cmd.second]+1);
            }
        }
    }
    for (int i = ans.size()-1; i >= 0; i--) {
        if (1E6 == ans[i]) {
            cout << -1 << endl;
        } else {
            cout << ans[i] << endl;
        }
    }
}