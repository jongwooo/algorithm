#include <iostream>
using namespace std;

int m, n;
int sum = 0;
int minNum = 10000;

bool isPrimeNumuber(int number) {
	if (number == 1) return false;
	for (int i = 2; i < number; i++) {
		if (number % i == 0) return false;
	}
	return true;
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	cin >> m >> n;
	for (int i = m; i <= n; i++) {
		if (isPrimeNumuber(i)) {
			sum += i;
			if (i < minNum) minNum = i;
		}
	}
	if (sum == 0) cout << -1;
	else cout << sum << '\n' << minNum;
}