#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

int main() {
    unordered_map<string, int> codes;

    string nextCommand;

    while (cin >> nextCommand) {
        if (nextCommand == "define") {
            string key;
            int val;

            cin >> val >> key;
            codes[key] = val;
        } 
        else {
            string a, b, op;
            cin >> a >> op >> b;

            if (codes.find(a)== codes.end() || codes.find(b) == codes.end()) {
                cout << "undefined" << endl;
                continue;
            }

            int x = codes[a];
            int y = codes[b];

            if (op == ">") {
                cout << ((x > y) ? "true" : "false") << endl;
            } else if (op == "<") {
                cout << ((x < y) ? "true" : "false") << endl;
            }
            else {
                cout << ((x == y) ? "true" : "false") << endl;
            }
        }
    }

    
    return 0;
}