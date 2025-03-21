#include 

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define sort_desc(x) sort(x.rbegin(), x.rend())
#define sz(x) (int)(x).size()
#define endl '\n'
template using V=vector;
template using VV=vector>;
typedef long long ll;
typedef long double ld;
typedef pair pii;
typedef vector vi;
typedef vector vll;
typedef unordered_map uimap;


ll MOD = pow(2, 31) - 1;

ll dfs_d_r(VV& grid, VV& dp, pii coords) {
    int size = grid.size();
    int x = coords.first;
    int y = coords.second;

    if (x < 0 || x >= size || y < 0 || y >= size) return 0;

    if (grid[y][x] == '#') return 0;

    if (dp[y][x] != -1) return dp[y][x];

    dp[y][x] = (dfs_d_r(grid, dp, {x + 1, y}) + dfs_d_r(grid, dp, {x, y + 1})) % MOD;
    return dp[y][x];
}

void dfs_all(VV& grid, pii coords) {
    int size = grid.size();
    int x = coords.first;
    int y = coords.second;

    if (x < 0 || x >= size || y < 0 || y >= size) return;
    if (grid[y][x] == '#') return;
    grid[y][x] = '#';
    if (x == size - 1 && y == size - 1) return;

    V directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    for (auto& direction : directions) {
        dfs_all(grid, {x + direction.first, y + direction.second});
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int size;
    cin >> size;
    VV grid(size, V(size));
    
    rep(i, 0, size) {
        rep(j, 0, size) {
            cin >> grid[i][j];
        }
    }

    VV dp(size, V(size, -1));

    dp[size - 1][size - 1] = 1;
    ll result = dfs_d_r(grid, dp, {0, 0});
    
    if (result > 0) {
        cout << result << endl;
    } else {
        dfs_all(grid, {0, 0});
        if (grid[size - 1][size - 1] == '#') {
            cout << "THE GAME IS A LIE" << endl;
        } else {
            cout << "INCONCEIVABLE" << endl;
        }
    }

}