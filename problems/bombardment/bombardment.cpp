#include <bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for (int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sort_desc(x) sort(x.rbegin(), x.rend())
#define sz(x) (int)(x).size()
#define endl '\n'
template <typename T>
using V = vector<T>;
template <typename T>
using VV = vector<vector<T>>;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef unordered_map<int, int> uimap;


int main() {
    cin.tie(0)->sync_with_stdio(0);
    
    int n, r;
    cin >> n >> r;

    int x;

    uimap data;
    
    while (cin >> x) {
        data[x]++;
        
        if (data.find(x-r) == data.end())
            data[x-r] = 0;
    }

    V<pii> points;
    int total = 0;

    for (pii p : data) {
        points.push_back(make_pair(p.first, p.second));
        total += p.second;
    }

    sort(points.begin(), points.end());


    vi moves;

    while (true) {

        int coord = 0;
        int val = 0;
        int start = 0;
        int end = 0;
        int temp = 0;
        pii d;

        while (end < points.size() && points[end].first <= points[start].first+r) {
            temp += points[end].second;
            end++;
        }

        end--;

        rep(i, 0, points.size()) {
            pii p = points[i];
            int k = p.first;

            while (points[start].first < k-r) {
                temp -= points[start].second;
                start++;
            }
            end++;

            while (end < points.size() && points[end].first <= k+r) {
                temp += points[end].second;
                end++;
            }
            end--;

            if (temp > val) {
                coord = i;
                val = temp;
                d = make_pair(start, end);
            }
        }

        if (val == 0)
            break;
        
        rep(i, d.first, d.second+1) {
            total -= points[i].second;
            points[i].second = 0;
        }

        moves.push_back(coord);

        if (total <= 0) 
            break;
        
    }

    cout << moves.size() << endl;
    for (int v : moves) {
        cout << points[v].first << " ";
    }
    cout << endl;

}