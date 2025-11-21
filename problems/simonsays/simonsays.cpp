#include 
#include 

using namespace std;

int main() {
    int steps;
    
    cin >> steps;
    cin.ignore();
    
    for (int i = 0; i < steps; i++) {
        string command;
        getline(cin, command);
        if (command.rfind("Simon says ", 0) == 0) {
            cout << command.substr(11, command.length()-11) << endl;
        }
    }
    
    return 0;
}