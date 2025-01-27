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