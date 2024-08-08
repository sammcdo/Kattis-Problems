#include <bits/stdc++.h>
#include <vector>
#include <unordered_map>
#include <queue>
#include <deque>

using namespace std;

#define rep(i, a, b) for (int i = a; i < (b); ++i)
#define For(i, a) for (int i = 0; i < (a); ++i)
#define all(x) begin(x), end(x)
#define is_in(x, s) ((s).find(x) != (s).end())
#define endl '\n'
#define pi acos(-1.0)
typedef long long ll;
template <class T>
using V = vector<T>;
template <class T>
using VV = vector<vector<T>>;
template <class K, class V>
using umap = unordered_map<K, V>;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef unordered_map<int, int> uimap;

int main() {
    int c;
    cin >> c;

    For(scenario, c) {
        int depth;
        cin >> depth;

        int lanecount, lanelen;
        cin >> lanecount >> lanelen;
        lanecount+=2;

        vector<deque<char>> lanes;
        For(i, lanecount) {
            deque<char> curr;
            char temp;
            For(j, lanelen) {
                cin >> temp;
                curr.emplace_back(temp);
            }
            lanes.push_back(curr);
        }
        
        int finishInd = 0;
        VV<bool> possible(lanecount, V<bool>(lanelen, 0));
        VV<bool> next(lanecount, V<bool>(lanelen, 0));

        For(i, lanelen){
            if (lanes[lanecount-1][i] == 'F') {
                possible[lanecount-1][i] = 1;
            }
            if (lanes[0][i] == 'G') {
                finishInd = i;
            }
        }

        bool found = false;
        rep(d, 1, depth+1) {
            // move cars
            For(i, lanecount-2) {
                if (i%2 == 0) {
                    char first = lanes[lanecount-2-i].back();
                    lanes[lanecount-2-i].pop_back();
                    lanes[lanecount-2-i].emplace_front(first);
                } else {
                    char first = lanes[lanecount-2-i].front();
                    lanes[lanecount-2-i].pop_front();
                    lanes[lanecount-2-i].emplace_back(first);
                }
            }
            // find next possible
            For(i, lanecount) {
                For(j, lanelen) {
                    if (possible[i][j]) {
                        if (lanes[i][j] != 'X') {
                            next[i][j] = 1;
                        }
                        if (i+1 < lanecount && lanes[i+1][j] != 'X') {
                            next[i+1][j] = 1;
                        }
                        if (i-1 >= 0 && lanes[i-1][j] != 'X') {
                            next[i-1][j] = 1;
                        }
                        if (j+1 < lanelen && lanes[i][j+1] != 'X') {
                            next[i][j+1] = 1;
                        }
                        if (j-1 >= 0 && lanes[i][j-1] != 'X') {
                            next[i][j-1] = 1;
                        }
                    }
                }
            }
            For(i, lanecount) {
                For(j, lanelen) {
                    possible[i][j] = next[i][j];
                    next[i][j] = 0;
                }
            }
            if (possible[0][finishInd]) {
                found = true;
                cout << "The minimum number of turns is " << d << "." << endl;
                break;
            }
        }
        if (!found) {
            cout << "The problem has no solution." << endl;
        }

    }

    return 0;
}