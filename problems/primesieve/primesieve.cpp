#include 
#include 
#include 
#include 

using namespace std;

int main() {
	int high;
	int cases;
	int x;

	cin >> high;
	cin >> cases;

	vector primes(100000000, true);
	primes[0] = false;
	primes[1] = false;

	int m = floor(pow(high, 0.5)) + 1;
	int p = 2;

	for (int x = 2; x < m; x++) {
		if (primes[x] == true) {
			for (int j = x * x; j < high + 2; j += x) {
				primes[j] = false;
			}
		}
	}

	int total = 0;
	for (int i = 2; i <= high; i++) {
		if (primes[i]) {
			total++;
		}
	}

	cout << total << endl;

	for (int i = 0; i < cases; i++) {
		cin >> x;
		if (primes[x]) {
			cout << "1" << endl;
		}
		else {
			cout << "0" << endl;
		}
	}

	return 0;
}