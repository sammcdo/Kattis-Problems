#include <iostream>
#include <unordered_set>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    while (n != -1) {
        vector<vector<int>> graph;

        for (int i = 0; i < n; i++) {
            vector<int> tmp;
            for (int j = 0; j < n; j++) {
                int x;
                cin >> x;
                tmp.push_back(x);
            }
            graph.push_back(tmp);
        }

        unordered_set<int> failed;

        for (int start = 0; start < n; start++) {
            unordered_set<int> opts;
            bool found = false;

            for (int i = 0; i < n; i++) {
                if (graph[start][i]) {
                    opts.emplace(i);
                }
            }

            unordered_set<int> opts2;
            for (auto first : opts) {
                for (int i = 0; i < n; i++) {
                    if (graph[first][i]) {
                        opts2.emplace(i);
                    }
                }
            }

            for (auto second : opts2) {
                if (graph[second][start]) {
                    found = true;
                    break;
                }
            }

            if (found == false) {
                failed.emplace(start);
            }
        }

        vector<int> output;
        for (auto i : failed) {
            output.push_back(i);
        }

        sort(output.begin(), output.end());

        for (auto i : output) {
            cout << i << " ";
        }
        cout << endl;

        cin >> n;

    }
}