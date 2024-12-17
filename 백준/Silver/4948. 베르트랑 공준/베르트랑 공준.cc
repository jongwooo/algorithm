#include <iostream>
#include <cmath>
using namespace std;

bool isPrimeNumber(int x) {
	if (x <= 1) return false;
	for (int i = 2; i <= (int)sqrt(x); i++) {
		if (x % i == 0) return false;
	}
	return true;
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	while (true) {
		cin >> n;
		if (n == 0) break;
		int cnt = 0;
		for (int i = n + 1; i <= 2 * n; i++) {
			if (isPrimeNumber(i)) cnt++;
		}
		cout << cnt << '\n';
	}
}