#include 

using namespace std;

int main() {
    string name;
    int age;

    cin >> name;
    cin >> age;

    for (int i = 1; i <= age; i++) {
        cout << "Hipp hipp hurra, " << name << "!" << endl;
    }

    return 0;
}