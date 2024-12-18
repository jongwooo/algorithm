#include <iostream>
#include <cmath>
using namespace std;

const int RANGE = 1'000'001;
int prime[RANGE];

int main() {
	cin.tie(0)->sync_with_stdio(0);

	fill_n(prime, RANGE, 1);
	prime[0] = prime[1] = 0;
	for (int i = 2; i * i <= RANGE; i++) {
		if (prime[i]) {
			for (int j = i * 2; j <= RANGE; j += i) {
				prime[j] = 0;
			}
		}
	}
	int t;
	cin >> t;
	while (t--) {
		int n;
		cin >> n;
		int cnt = 0;
		for (int i = 2; i <= n / 2; i++) {
			if (prime[i] && prime[n - i]) cnt++;
		}
		cout << cnt << '\n';
	}
}