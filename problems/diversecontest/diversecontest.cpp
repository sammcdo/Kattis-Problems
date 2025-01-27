#include 
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
typedef pair pii;
typedef vector vi;
typedef unordered_map uimap;

void find_permuts(int n, int m, VV& problems, VV& permuts) {
   rep(i, 0, 1< temp;
      for (int j = 0; j < n; j++) {
        int x = 1<sync_with_stdio(0);
  int n, m;

  cin >> n >> m;

  VV problems(n);

  VV permuts;
  
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
    umap table;
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