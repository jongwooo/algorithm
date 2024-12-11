#include <iostream>
using namespace std;

int n, num, cnt = 0;

bool isPrimeNumuber(int number) {
	if (number == 1) return false;
	for (int i = 2; i < number; i++) {
		if (number % i == 0) return false;
	}
	return true;
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> num;
		if (isPrimeNumuber(num)) cnt++;
	}
	cout << cnt;
}