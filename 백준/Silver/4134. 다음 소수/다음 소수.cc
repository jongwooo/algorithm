#include <iostream>
#include <cmath>
using namespace std;

typedef long long ll;

bool isPrimeNumber(ll x) {
	if (x <= 1) return false;
	for (ll i = 2; i <= (ll)sqrt(x); i++) {
		if (x % i == 0) return false;
	}
	return true;
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	ll n;
	cin >> n;
	for (ll i = 0; i < n; i++) {
		ll num;
		cin >> num;
		while (true) {
			if (isPrimeNumber(num)) {
				cout << num << '\n';
				break;
			}
			num++;
		}
	}
}