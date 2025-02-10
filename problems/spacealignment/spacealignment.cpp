#include 
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


int main() {
  int n;
  cin >> n;

  V indents(n);
  V> counts(n);

  stack s;
  // string s = "";
  


  For(i, n) {
    string temp;
    cin >> temp;
    
    char x = temp.back();
    // cout << x << endl;
    temp.pop_back();

    
    if (x == '{') {
      indents[i] = s.size();
      s.push(1);
    } else {
      s.pop();
      indents[i] = s.size();

    }


    int spaces = 0;
    int tabs = 0;
    For(j, temp.size()) {
      if (temp[j] == 's') {
        spaces++;
      } else {
        tabs++;
      }
    }

    counts[i] = make_pair(tabs, spaces);

  }

  // For(i, n) {
  //   cout << i << " " << indents[i] << " " << counts[i].first << " " << counts[i].second << endl;
  // }

  rep(i, 1, 1000) {
    bool works = true;
    int guess = -1;
    // cout << i << endl;
    For(j, n) {
      // cout << "J" << j << endl;
      int tabs = counts[j].first;
      int spaces = counts[j].second;
      int indent = indents[j];
      int total = spaces + (tabs * i);
      // cout << total << endl;

      if (indent == 0 || total % indent != 0 || (guess != -1 && total / indent != guess)) {
        if (indent == 0 && total == 0) {
          continue;
        }
        works = false;
        break;
      } else {
        guess = total / indent;
      }
    }
    if (works) {
      cout << i << endl;
      return 0;
    }
  }
  cout << -1 << endl;

}