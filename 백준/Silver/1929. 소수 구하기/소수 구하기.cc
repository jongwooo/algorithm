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

	int n, m;
	cin >> n >> m;
	for (int i = n; i <= m; i++) {
		if (isPrimeNumber(i)) cout << i << '\n';
	}
}