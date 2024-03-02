#include <bits/stdc++.h>

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

ll pow_mod(ll base, ll exp, ll mod) {
   base %= mod;
   ll result = 1;
   while (exp > 0) {
       if (exp & 1) result = (result * base) % mod;
       base = (base * base) % mod;
       exp >>= 1;
   }
   return result;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  ll r, c;
  cin >> r >> c;

  ll mod = 998244353;

  cout << r * pow_mod(r-1, c-1, mod) % mod << endl;
}