#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int g, n;
    cin >> g >> n;
    vector<pair<int, int>> opts;
    for (int i = 0; i < n; i++) {
        int start, end;
        cin >> start >> end;
        opts.push_back(pair<int, int>(start, end));
    }

    sort(opts.begin(), opts.end());
    

    vector<int> m(24001, 0);

    for (int i = 0; i < n; i++) {
        int start = opts[i].first;
        int end = opts[i].second;

        m[end] = m[start] + 1;
        for (int j = end+1; j< m.size();j++) {
            m[j] = m[end];
        } 
    }

    if (g <= m[m.size() - 1]) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}