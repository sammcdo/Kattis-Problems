#include <bits/stdc++.h>
#include <string>

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

void find_permuts(int n, int m, VV<string>& problems, VV<int>& permuts) {
   rep(i, 0, 1<<n) {
    if (__builtin_popcount(i) == m) {
      V<int> temp;
      for (int j = 0; j < n; j++) {
        int x = 1<<j;
        if (i & x) {
          temp.push_back(j);
        }
      }
      permuts.push_back(temp);
    }
   }
}

int main() {
  // cin.tie(0)->sync_with_stdio(0);
  int n, m;

  cin >> n >> m;

  VV<string> problems(n);

  VV<int> permuts;
  
  rep(i, 0, n) {
    int x;
    cin >> x;
    rep(j, 0, x) {
      string temp;
      cin >> temp;
      problems[i].push_back(temp);
    }
  }

  find_permuts(n, m, problems, permuts);

  int count = 0;
  rep(i, 0, permuts.size()) {
    umap<string, int> table;
    for (int k : permuts[i]) {
      for (string x : problems[k]) {
        if (table.find(x) == table.end()) {
          table[x] = 1;
        } else {
          table[x]++;
        }
      }
    }
    bool failed = false;
      for (auto [k, v] : table) {
        if (v > m / 2) {
          failed = true;
        }
      }
      if (!failed) {
        count++;
      }
  }

  cout << count;

}