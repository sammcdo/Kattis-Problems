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


int binsearch(int a, vi& list) {
    int l = 0;
    int r = list.size()-1;
    int m;
    int ans = -1;
    while (l <= r) {
        m = (l + r) / 2;
        if (list[m] > a) {
            r = m-1;
            ans = m;
        } else {
            l = m+1;
        }
    }
    if (ans != -1) {
        return list[ans];
    } else {
        return list[0];
    }
}

int main() {
    int n, k;
    cin >> n >> k;

    unordered_map contests;

    For(i, n) {
        int x;
        cin >> x;

        contests[x].push_back(i);
    }

    // For(i, k+1) {
    //     for (auto j : contests[i]) {
    //         cout << j << " ";
    //     }
    //     cout << endl;
    // }

    ll best = -1;
    For(i, contests[1].size()) {
        int pos = contests[1][i];
        ll total = 1;
        rep(j, 2, k+1) {
            int next, delta;
            next = binsearch(pos, contests[j]);
            if (next > pos) {
                delta = next - pos;
            } else {
                delta = n - pos + next;
            }
            // cout << total << " ";
            // cout << pos << " ";
            // cout << next << " ";
            // cout << delta << endl;

            total += delta;
            pos = next;
        }
        if (best == -1) {
            best = total;
        }
        else {
            best = min(best, total);

        }
    }

    cout << best << endl;
}