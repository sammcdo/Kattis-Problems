#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    
    cin >> n;
    cin.ignore();
    
    for (int i = 0; i < n; i++) {
        string command;
        getline(cin, command);
        if (command.rfind("Simon says ", 0) == 0) {
            cout << command.substr(10, command.length()-10) << endl;
        }
    }
    
    return 0;
}