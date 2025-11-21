#include 
#include 
#include 

using namespace std;

int main() {
    int b = 0;
    string good, bad;

    getline(cin, good);
    getline(cin, bad);

    good = good + " ";
    bad = bad + " ";

    unordered_set sticky;

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
    cout << endl;

    
    return 0;
}