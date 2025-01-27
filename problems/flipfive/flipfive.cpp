#include 
#include 
#include 
#include 

using namespace std;

#define rep(i, a, b) for (int i = a; i < (b); ++i)
#define For(i, a) for (int i = 0; i < (a); ++i)
#define all(x) begin(x), end(x)
#define is_in(x, s) ((s).find(x) != (s).end())
#define endl '\n'
#define pi acos(-1.0)
typedef long long ll;
template 
using V = vector;
template 
using VV = vector>;
template 
using umap = unordered_map;
typedef pair pii;
typedef vector vi;
typedef unordered_map uimap;

int flips[][5] = {
    {0,1,3,9,9},
    {0,1,2,4,9},
    {1,2,5,9,9},
    {0,3,4,6,9},
    {1,3,4,5,7},
    {2,4,5,8,9},
    {3,6,7,9,9},
    {4,6,7,8,9},
    {5,7,8,9,9},
};

string flip(string str, int i) {
    if (str[i] == '*') {
        str[i] = '.';
    } else {
        str[i] = '*';
    }
    return str;
}

int main() {
    int counts;
    cin >> counts;

    unordered_map maps;

    maps["........."] = 0;

    queue> q;
    q.push(make_pair(".........", 0));
    while (q.size()) {
        pair curr = q.front();
        q.pop();
        For(i, 9) {
            string next = curr.first;
            For(j, 5) {
                if (flips[i][j] < 9) {
                    next = flip(next, flips[i][j]);
                }
            }
            if (maps.find(next) == maps.end()) {
                maps[next] = curr.second+1;
                q.push(make_pair(next, curr.second+1));
            }
        }
    }

    For(i, counts) {
        string grid = "---------";
        For(j, 9) {
            char temp;
            cin >> temp;
            grid[j] = temp;
        }

        cout << maps[grid] << endl;
    }

    return 0;
}