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
            
            bool found = false;
            
            unordered_set<int> options1;
            for (int second = 0; second < n; second++) {
                if (graph[start][second]) {
                    options1.emplace(second);
                }
            }
            
            unordered_set<int> options2;
            for (auto second : options1) {
                for (int third = 0; third < n; third++) {
                    if (graph[second][third]) {
                        options2.emplace(third);
                    }
                }
            }
            
            for (auto third : options2) {
                if (graph[third][start]) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                failed.emplace(start);
            }
            
            
        }
        
        vector<int> output;
            for (auto i : failed) {
                output.push_back(i);
            }
            sort(output.begin(), output.end());
            
            for (int i = 0; i < output.size(); i++) {
                cout << output[i] << " ";
            }
            cout << endl;
        
        cin >> n;
    }
    
    return 0;
}