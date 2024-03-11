#include <bits/stdc++.h>
#include <string>
#include <stack>

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
  int n;
  cin >> n;

  V<int> indents(n);
  V<pair<int, int>> counts(n);

  stack<int> s;
  

  // count the spaces and indent level
  For(i, n) {
    string temp;
    cin >> temp;
    
    char x = temp.back();
    temp.pop_back();

    // increase or decrease indent at position i
    if (x == '{') {
      indents[i] = s.size();
      s.push(1);
    } else {
      s.pop();
      indents[i] = s.size();

    }

    // count tabs and spaces at i
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

  // worst case is 1 tab is worth 999 spaces
  rep(i, 1, 1000) {
    bool works = true;
    int guess = -1;

    // check if each line would be valid for this tab value (i)
    For(j, n) {
      int tabs = counts[j].first;
      int spaces = counts[j].second;
      int indent = indents[j];
      int total = spaces + (tabs * i);

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