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

bool sort_(const pii& a, const pii& b) {
  return (a.second < b.second);
}


int main() {
  int n;

  cin >> n;

  vector minions;

  For(i, n) {
    int a,b;
    cin >> a >> b;

    minions.push_back(pii(a,b));
  }

  vector rooms;

  sort(minions.begin(), minions.end(), sort_);

  For(i, n) {
    bool found = false;
    pii a = minions[i];
    for (int j = rooms.size()-1; j > -1; j--) {
      pii b = rooms[j];
      if (a.first <= b.second && b.first <= a.second) {
        rooms[j] = pii(max(a.first, b.first), min(a.second, b.second));
        found = true;
        break;
      }
    }
    if (!found) {
      rooms.push_back(a);
    }
  }

  // for (pii x : rooms) {
  //   cout << x.first << " " << x.second << endl;
  // }

  cout << rooms.size() << endl;
  
}