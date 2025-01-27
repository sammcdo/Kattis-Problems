#include 

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define For(i, a) for(int i = 0; i < (a); ++i)
#define all(x) begin(x), end(x)
#define is_in(x, s) ((s).find(x) != (s).end())
#define endl '\n'
#define pi acos(-1.0)
typedef long long ll;
template using V=vector;
template using VV=vector>;
template using umap=unordered_map;
typedef pair pii;
typedef vector vi;
typedef unordered_map uimap;

const int MAX = 2'500'000;

ll factors[MAX] = {0};
ll prime_factors[MAX] = {0};

void fill() {
    factors[1] = 1;
    for (int i = 2; i < MAX; i++) {
        factors[i] += 1;
        bool set_primes = prime_factors[i] == 0;
        for (int j = i; j < MAX; j += i) {
            factors[j]++;
            if (set_primes)
                prime_factors[j]++;
        }
    }
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n = 0;

    cin >> n;

    fill();

    vi cases;

    For(i, n) {
        int test;
        cin >> test;
        cout << factors[test] - prime_factors[test] << endl;
    }

}