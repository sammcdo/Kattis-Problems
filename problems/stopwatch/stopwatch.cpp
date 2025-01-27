#include 

using namespace std;

int main() {
    int n;
    cin >> n;

    bool stopped = true;
    int last = 6995;
    int x;
    int time = 0;

    for (int i = 0; i < n; i++) {
        cin >> x;

        if (stopped) {
            last = x;
            stopped = false;
        }
        else {
            time += x - last;
            stopped = true;
        }
    }

    if (!stopped) {
        cout << "still running";
    }
    else {
        cout << time;
    }
}