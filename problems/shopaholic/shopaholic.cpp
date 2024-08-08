#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int main() {
    int count;
    vector<int> items;

    cin >> count;

    for (int i = 0; i < count; i++) {
        int tmp;
        cin >> tmp;
        items.push_back(tmp);
    }

    sort(items.begin(), items.end());

    long savings = 0;
    while (items.size() >= 3) {
        int a = items.back();
        items.pop_back();
        int b = items.back();
        items.pop_back();
        int c = items.back();
        items.pop_back();

        savings += c;
    }

    cout << savings << endl;
    
    return 0;
}