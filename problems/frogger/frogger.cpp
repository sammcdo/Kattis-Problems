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
    int c;
    cin >> c;

    For(scenario, c) {
        int depth;
        cin >> depth;

        int lanecount, lanelen;
        cin >> lanecount >> lanelen;
        lanecount+=2;

        vector> lanes;
        For(i, lanecount) {
            deque curr;
            char temp;
            For(j, lanelen) {
                cin >> temp;
                curr.emplace_back(temp);
            }
            lanes.push_back(curr);
        }
        
        int finishInd = 0;
        VV possible(lanecount, V(lanelen, 0));
        VV next(lanecount, V(lanelen, 0));

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