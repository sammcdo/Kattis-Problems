#include <bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define For(i, a) for(int i = 0; i < (a); i++)
#define all(x) begin(x), end(x)
#define is_in(x, s) ((s).find(x) != (s).end())
#define endl '\n'
#define pi acos(-1.0)
typedef long long ll;
template<typename T> using V=vector<T>;
template<typename T> using VV=vector<vector<T>>;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef unordered_map<int, int> uimap;

int walk(int node, unordered_map<int, vi>& tree, int (&visited)[], deque<char>& str_stack, string& values, int status) {
    int count = 0;

    if (visited[node] > status) {
        return 0;
    }

    bool added = false;
    char removed = ' ';
    visited[node] = status+1;

    if (str_stack.size() == 0) {
        if (values[node] == '}' || values[node] == ']' || values[node] == ')') {
            return 0;
        }
        str_stack.push_back(values[node]);
        added = true;
    } else {
        char last = str_stack.back();
        char curr = values[node];

        if ((last == '{' && curr == '}') || (last == '(' && curr == ')') || (last == '[' && curr == ']')) {
            str_stack.pop_back();
            removed = last;
            added = false;
        } else {
            if (false) {}
            if (curr == '}' || curr == ']' || curr == ')') {
                return count;
            }
            else {
                str_stack.push_back(curr);
                added = true;
            }
        }

        if (str_stack.size() == 0) {
            count++;
        }
    }

    for (int neighbor : tree[node]) {
        if (visited[neighbor] <= status) {
            count += walk(neighbor, tree, visited, str_stack, values, status);
        }
    }

    if (added) {
        str_stack.pop_back();
    }
    
    if (removed != ' ')
        str_stack.push_back(removed);

    return count;
}

int main() {
    int n;
    cin >> n;
    string x;
    cin >> x;

    unordered_map<int, vi> tree;

    For(i, n-1) {
        int a, b;
        cin >> a >> b;
        a--; b--;
        tree[a].push_back(b);
        tree[b].push_back(a);
    }

    int count = 0;
    int visited[500001] = {0};
    For(i, n) {
        deque<char> str_stack;
        int v = walk(i, tree, visited, str_stack, x, i);
        if (v != -1)
            count += v;
    }
    cout << count << endl;
}