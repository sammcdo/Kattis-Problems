#include <bits/stdc++.h>
#include <string>
#include <cctype>

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
  string n = "";
  getline(cin, n);

  // cout << n << endl;

  string check = "";

  for (char& i : n) {
    if (isalpha(i)) {
      check = check + tolower(i, locale());
    }
  }

  // cout << check << endl;

  bool found = false;
  if (check.size() >= 2) {
    for (int i = 0; i <= check.size()-2; i++) {
      if (check[i] == check[i+1]) {
        found = true;
      }
      if (check[i] == check[i+2]) {
        found = true;
      }
    }
  }
  
  // cout << found << endl;
  if (found) {
    cout << "Palindrome" << endl;
  }
  else {
    cout << "Anti-palindrome" << endl;
  }
  
  // cout << check;

}