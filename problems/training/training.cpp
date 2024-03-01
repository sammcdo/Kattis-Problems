#include <iostream>

using namespace std;


int main() {
    int n, s, l, r;

    cin >> n >> s;

    for (int i = 0; i < n; i++) {
        cin >> l >> r;

        if (s >= l && s <= r) {
            s++;
        }
    }

    cout << s;


    return 0;
}