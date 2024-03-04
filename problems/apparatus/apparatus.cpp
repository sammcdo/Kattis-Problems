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


int main() {
  int n, m;
  vector<bitset<1000>> switches;
  vector<bitset<1000>> lights;
  vector<bitset<1000>> works;

  cin >> n >> m;

  For(i, m) {
    bitset<1000> pic;
    For(j, n) {
      char c;
      cin >> c;
      int x = c - '0';
      if (x) {
        pic.set(j);
      }
    }
    switches.push_back(pic);

    int c1 = pic.count();
    
    bitset<1000> pic2;
    For(j, n) {
      char c;
      cin >> c;
      int x = c - '0';
      if (x) {
        pic2.set(j);
      }
    }
    lights.push_back(pic2);

    if (c1 != pic2.count()) {
      cout << "0" << endl;
      return 0;
    }
  }

  For(i, n) {
    bitset<1000> bs;
    For(j, n) {
      bs.set(j);
    }
    works.push_back(bs);
  }

  For(i, m) {
    For(j, n) {
      if (switches[i][j]) {
        works[j] &= lights[i];
      } else {
        works[j] &= ~lights[i];
      }
    }
  }

  vector<ll> fact(n+1);
  fact[0] = 1;
  rep(i, 1, n+1) {
    fact[i] = fact[i-1] * i % 1000003;
  }

  bitset<1000> seen;
  int out = 1;
  For(i, n) {
    if (!works[i].count()) {
      cout << 0 << endl;
      return 0;
    }
    if ((seen & works[i]).count() == 0) {
      out = out * fact[works[i].count()] % 1000003;
      seen |= works[i];
    }
  }

  cout << out;

}