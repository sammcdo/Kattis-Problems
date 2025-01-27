#include 
#include 
#include 

using namespace std;

int main() {
    unordered_map memory;
    
    string nextCommand;
    
    while (cin >> nextCommand) {
        if (nextCommand == "define") {
            string key;
            int value;
            cin >> value >> key;
            memory[key] = value;
        }
        else {
            string a, b, op;
            cin >> a >> op >> b;
            
            if (memory.find(a) == memory.end() || 
            memory.find(b) == memory.end()) {
                cout << "undefined" << endl;
                continue;
            }
            
            int x = memory[a];
            int y = memory[b];
            
            if (op == ">") {
                cout << ((x > y) ? "true" : "false") << endl;
            } else if (op == "<") {
                cout << ((x < y) ? "true" : "false") << endl;
            } else {
                cout << ((x == y) ? "true" : "false") << endl;
            }
        }
    }
    
    return 0;
}