#include 
#include 
#include 
#include 

using namespace std;

/*
Dynamic programming/brute force. You have two choices per task,
assign to intern A or assign to B. The idea is to create dp array 
where a row i is all possible states that exists using tasks 0-i
The dp array is of the form (sum a, sum b) -> dp[sum b] = sum a
*/

// highest possible by only picking one intern
const int length = 5000001;

// matrix of (tasks) x (sum B)
int dp[50][5000001];

int main() {
    cin.tie(nullptr)->ios::sync_with_stdio(false);

    // read number of tasks
    int n;
    cin >> n;

    // parallel arrays of A and B for tasks
    int as[50] = {0};
    int bs[50] = {0};

    // read all tasks
    int a = 0;
    int b = 0;
    for (int i = 0; i < n; i++) {
        cin >> a >> b;
        as[i] = a;
        bs[i] = b;
    }

    // init dp array with -1
    memset(dp, -1, sizeof dp);

    // first move
    dp[0][0] = as[0]; // dp[task=0][b=0] = a[0], a picked
    dp[0][bs[0]] = 0; // dp[task=0][b=b[0]] = 0, b picked

    int highest = bs[0] + 1; // keep track of largest used column to save time
    for (int i = 1; i < n; i++) {
        a = as[i];
        b = bs[i];

        // every move where a is picked from previous state [i-1,j]
        for (int j = 0; j < highest; j++) {
            if (dp[i-1][j] != -1) {
                dp[i][j] = dp[i-1][j] + a;
            }
        }

        // every move where b is picked from previous state [i-1,j]
        for (int j = 0; j < highest; j++) {
            if (dp[i-1][j] != -1) {
                if (dp[i][j+b] == -1) {
                    dp[i][j+b] = dp[i-1][j];
                }
                dp[i][j+b] = min(dp[i-1][j], dp[i][j+b]);
                highest = max(highest, j+b+1);
            }
        }
    }

    int smallest_a = length;
    int smallest_b = length;
    // find best final state 
    for (int i = 0; i < length; i++) {
        if (dp[n-1][i] != -1 && max(dp[n-1][i], i) < max(smallest_a, smallest_b)) {
            smallest_a = dp[n-1][i];
            smallest_b = i;
        }
    }

    cout << max(smallest_a, smallest_b);

    
    return 0;
}