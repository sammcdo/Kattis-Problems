#include 
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

int main() {
    string rains;
    cin >> rains;

    vi rain_map;

    For(i, rains.size()) {
        if (rains[i] == 'R') {
            rain_map.push_back(1);
        } else {
            rain_map.push_back(-1);
        }
    }

    pii indexes;
    int best = -1000000;
    int sum = 0;
    int othersum = 0;
    int start = 0;
    int otherstart = 0;
    rep(i, 0, rain_map.size()) {
        // cout << rain_map[i] << endl;
        sum += rain_map[i];
        othersum -= rain_map[i];

        if (sum < 0) {
            start = i+1;
            sum = 0;
        } else {
            while(true) {
                if (start < i && sum - rain_map[start] > sum) {
                    sum -= rain_map[start];
                    start++;
                } else {
                    break;
                }
            }
        }

        
        if (othersum < 0) {
            otherstart = i+1;
            othersum = 0;
        } else {
            while(true) {
                if (otherstart < i && othersum + rain_map[otherstart] > othersum) {
                    othersum += rain_map[otherstart];
                    otherstart++;
                } else {
                    break;
                }
            }
        }

        if (sum >= best) {
            if (sum == best) {
                indexes = min(indexes, make_pair(start, i));
            } else {
                indexes = make_pair(start, i);
            }
            best = sum;
        }
        if (othersum > best) {
            if (othersum == best) {
                indexes = min(indexes, make_pair(otherstart, i));
            } else {
                indexes = make_pair(otherstart, i);
            }
            best = othersum;
        }

        // cout << start << " " << i << " " << sum << endl;
        // cout << otherstart << " " << i << " " << othersum << endl;
        // cout << endl;
    }

    // cout << best << endl;
    cout << indexes.first+1 << " " << indexes.second+1 << endl;

    return 0;
}