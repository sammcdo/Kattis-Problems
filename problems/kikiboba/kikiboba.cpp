#include <string>
#include <iostream>

using namespace std;

int main() {
    string word;
    
    cin >> word;
    
    int b_count = 0;
    int k_count = 0;
    for (int i = 0; i < word.size(); i++) {
        if (word[i] == 'b') {
            b_count++;
        }
        if (word[i] == 'k') {
            k_count++;
        }
    }
    
    if (b_count > k_count) {
        cout << "boba" << endl;
    }
    if (k_count > b_count) {
        cout << "kiki" << endl;
    }
    if (b_count == k_count && b_count != 0) {
        cout << "boki" << endl;
    }
    if (b_count == 0 && k_count == 0) {
        cout << "none" << endl;
    }
    
    return 0;
}