#include 
#include 
#include 

using namespace std;

int main() {
    int n, m;
    
    while (cin >> n >> m) {
        int dp[1000002] = {0};
        vector moves;
        for (int i = 0; i < m; i++) {
            int a;
            cin >> a;
            moves.push_back(a);
        }
        sort(moves.begin(), moves.end());
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < m; j++) {
                int m = moves[j];
                if (i-m >= 0 && dp[i-m] == 0) {
                    dp[i] = 1;
                    break;
                }
            }
        }
        
        if (dp[n] == 1) {
            cout << "Stan wins" << endl;
        } else {
            cout << "Ollie wins" << endl;
        }
    }
}