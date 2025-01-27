#include 
#include 
#include 

using namespace std;

void findNextPossible(int curr, vector>& next) {
    for (int i = 0; i < next.size(); i++) {
        int mask = 1<> n >> m;

    // cout << "test" << endl;

    bitset<1 << 20> dp {};
    vector> next(20);

    findNextPossible(0, next);

    // cout << "here" << endl;
    
    for (int i = 0; i < n; i++) {
        unordered_set toAdd;
        for (int j = 0; j < m; j++) {
            char s;
            cin >> s;
            s -= '0';
            if (s) {
                int curr = 1<