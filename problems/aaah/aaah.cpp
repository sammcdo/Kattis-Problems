#include <iostream>

using namespace std;

int main() {
    string one;
    string two;
    
    cin >> one;
    cin >> two;
    
    if (one.length() >= two.length()) {
        cout << "go";
    } else {
        cout << "no";
    }
    
    return 0;
}