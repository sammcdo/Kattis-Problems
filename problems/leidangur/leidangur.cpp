#include 
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
    string map;

    vector bag;

    cin >> map;

    For(i, map.size()) {
        bag.push_back(map[i]);
        if (map[i] == 'P' || map[i] == 'G' || map[i] == 'O') {
            char target = tolower(map[i]);
            bool found = false;
            for (int j = bag.size()-1; j >= 0; j--) {
                if (bag[j] == target) {
                    bag.erase(bag.begin()+j, bag.end());
                    found = true;
                    break;
                }
            }
            if (!found) {
                cout << "Neibb" << endl;
                return 0;
            }
        }
    }

    // For (i, bag.size()) {
    //     cout << bag[i];
    // }
    // cout << endl;

    ll dp[] = {0, 0, 0};
    For(i, bag.size()) {
        if (bag[i] == 'p') {dp[0]++;}
        if (bag[i] == 'g') {dp[1]++;}
        if (bag[i] == 'o') {dp[2]++;}
    }

    cout << dp[0] << endl;
    cout << dp[1] << endl;
    cout << dp[2] << endl;

    return 0;
}