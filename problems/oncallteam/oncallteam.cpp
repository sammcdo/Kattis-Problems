#include <bits/stdc++.h>
#include <vector>
#include <bitset>

using namespace std;

void findNextPossible(int curr, vector<vector<int>>& next) {
    for (int i = 0; i < next.size(); i++) {
        int mask = 1<<i;
        // cout << "mask " << mask << endl;
        next[i].push_back(mask|curr);
    }
    // cout << "here 2" << endl;
    return;
}

int main()
{
    int n;
    int m;

    cin >> n >> m;

    // cout << "test" << endl;

    bitset<1 << 20> dp {};
    vector<vector<int>> next(20);

    findNextPossible(0, next);

    // cout << "here" << endl;
    
    for (int i = 0; i < n; i++) {
        unordered_set<int> toAdd;
        for (int j = 0; j < m; j++) {
            char s;
            cin >> s;
            s -= '0';
            if (s) {
                int curr = 1<<j;
                // cout << curr << endl;
                toAdd.insert(curr);

                // cout << "next "; 
                for (int x : next[j]) {
                    // cout << x << " ";
                    if (dp[x] == 0) {
                        toAdd.insert(x);
                    }
                }
                // cout << endl;
                next[j].clear();
            }
        }
        for (int x : toAdd) {
            dp[x] = 1;
            findNextPossible(x, next);
        }
        
    }

    // cout << dp << " " << (1<<m) << endl;

    // for (int i : dp) {
    //  cout << i;
    // }
    // cout << endl;

    int working = m;
    for (int i = 1; i < 1<<m; i++) {
        if (dp[i] == false) {
            int x = __builtin_popcount(i)-1;
            if (x < working) {
                working = x;
            }
        }
    }

    cout << working;

}