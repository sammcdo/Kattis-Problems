#include <iostream>
#include <unordered_set>
#include <string>

using namespace std;

int main() {
    string good;
    string bad;
    
    getline(cin, good);
    getline(cin, bad);
    
    good = good + " ";
    bad = bad + " ";
    
    unordered_set<char> sticky;
    
    int b = 0;
    for (int i = 0; i < good.length(); i++) {
        while (bad[b] != good[i]) {
            sticky.emplace(bad[b]);
            b++;
        }
        b++;
    }
    
    for (char c : sticky) {
        cout << c;
    }
    
    return 0;
}